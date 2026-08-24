#!/usr/bin/env python3
"""FX-1 -- the needs/provides composition join, re-run mechanically.

Target artifact:
  lab/active-research/joe-directed/composition/
      fx1-needs-provides-join-2026-08-16.md
Gate under test (single source of the extraction logic; this probe imports it):
  process_gates/needs_provides_composition_audit.py
Alias table (no alias without a receipt):
  lab/process/needs-provides-alias-table.json

The artifact claims a mechanical JOIN exists between declared needs and
claimed supply, that it retro-detects the SA-1 documented failure, that its
alias entries have live receipts, and that every candidate pair found at
introduction is typed.  This probe re-derives each of those claims from file
facts.  Corpus-churn quantities (the live pair count) are enforced by the
GATE's ratchet, not pinned here twice; what this probe pins is the
introduction measurement recorded in the gate's ADJUDICATED map, the
extraction machinery's exact behavior on fixed inputs, and the file facts
under the four LIVE_CANDIDATE adjudications.

Run:
    python3 tests/channel-swings/joe_directed_fx1_needs_provides_join.py
    (exit 0 iff every check passes)

Selftest (baseline first, then planted false facts; every plant MUST be
caught; exits 0 on success):
    python3 tests/channel-swings/joe_directed_fx1_needs_provides_join.py --selftest

No floats are compared anywhere in this file; every quantity is an integer
count or an exact string membership.
"""

from __future__ import annotations

import importlib.util
import json
import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GATE = os.path.join(REPO, "process_gates", "needs_provides_composition_audit.py")
ARTIFACT = "lab/active-research/joe-directed/composition/fx1-needs-provides-join-2026-08-16.md"

FAIL: list[str] = []
CHECKS = 0


def check(label: str, got, want) -> None:
    global CHECKS
    CHECKS += 1
    if got != want:
        FAIL.append(f"{label}: got {got!r}, want {want!r}")
        print(f"  FAIL  {label}: got {got!r}, want {want!r}")
    else:
        print(f"  ok    {label}: {got!r}")


def read(rel: str) -> str:
    with open(os.path.join(REPO, rel), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def load_gate():
    spec = importlib.util.spec_from_file_location("npc_gate", GATE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(selftest: bool = False) -> int:
    gate = load_gate()

    print("== C1  alias table: three entries, receipts verified independently ==")
    table = json.loads(read("lab/process/needs-provides-alias-table.json"))
    entries = table["aliases"]
    check("C1 alias entry count", len(entries), 3)
    check("C1 rule states no-alias-without-a-receipt",
          table["rule"].startswith("NO ALIAS WITHOUT A RECEIPT"), True)
    receipts_ok = 0
    for entry in entries:
        for receipt in entry["receipts"]:
            text = read(receipt["path"])
            if all(needle in text for needle in receipt["must_contain"]):
                receipts_ok += 1
    check("C1 receipts resolved and byte-verified", receipts_ok, 7)
    classes = {tuple(sorted(e["class"])) for e in entries}
    check("C1 documented classes exactly",
          classes,
          {("MET(X)", "Met(X)"), ("SU(3,2)", "Spin(3,2)"),
           ("Pi_RS^phys", "Π_RS^phys")})

    print("== C2  key classes: exact accept/reject behavior ==")
    check("C2 P_H accepted bare-in-parens (the SA-1 provider spelling)",
          gate.tokens_of("it builds (P_H) from the chimeric spinors"), {"P_H"})
    check("C2 SU(3,2) accepted", gate.tokens_of("node is SU(3,2), not spin"), {"SU(3,2)"})
    check("C2 SOLDERED-AD accepted", gate.tokens_of("the SOLDERED-AD fork"), {"SOLDERED-AD"})
    check("C2 status vocabulary rejected",
          gate.tokens_of("typed MISSING_CONSTRUCTION and BLOCKED_NEEDS_SPEC"), set())
    check("C2 post-mint status/control vocabulary rejected",
          gate.tokens_of("HALF-SAME NATIVE-VACUUM LIVE-HIGH "
                         "CLEARED-CONSISTENT SECTOR-SUPPLIED"), set())
    check("C2 register/work-item IDs rejected",
          gate.tokens_of("see SC-GEO-07, LA-11 and M-H17"), set())
    check("C2 YAML field names rejected",
          gate.tokens_of("the blocked_on: and doc_type: fields"), set())
    check("C2 no unbalanced-paren token (q_H regression)",
          gate.tokens_of("only `gamma(q_H)` after `d0`"), {"q_H"})

    print("== C3  join controls on a fixed synthetic corpus ==")
    plant = {
        "lab/active-research/joe-directed/__probe_plant__.md": (
            "---\ncreated: 2026-08-16\n---\n"
            "This route requires the `Qorv_Z` half.\n"
            "Also blocked on `Norv_W` under this exact casing.\n"
        ),
        "explorations/__probe_supply__.md": (
            "---\ncreated: 2026-08-16\n---\n"
            "This artifact constructs the `Qorv_Z` half.\n"
            "It also establishes `norv_w` in lowercase only.\n"
            "And it never builds `Qorv_Neg`.\n"
        ),
        "lab/active-research/joe-directed/__probe_plant_neg__.md": (
            "---\ncreated: 2026-08-16\n---\n"
            "The last leg is blocked on `Qorv_Neg`.\n"
        ),
    }
    pairs, wide, _ = gate.join(extra_md=plant)
    everything = {**pairs, **wide}
    planted_id = "ART:lab/active-research/joe-directed/__probe_plant__.md::Qorv_Z"
    check("C3 planted pair FOUND (extractor is live)", planted_id in everything, True)
    check("C3 case-variant does NOT join without an alias receipt",
          [p for p in everything if "Norv_W" in p or "norv_w" in p], [])
    check("C3 negated provide claim is NOT supply",
          [p for p in everything if "Qorv_Neg" in p], [])

    print("== C4  the three documented cases, from file facts ==")
    md1 = read("lab/active-research/joe-directed/four-d-mode-decomposition/"
               "md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md")
    check("C4A MD-1 fork horn names P_H",
          'ad(P_H) is inert: P_H is an independent principal bundle' in md1, True)
    provider = read("explorations/conditional-build/"
                    "k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
    check("C4A provider (nine days older) claims the build",
          "it builds (P_H) from the chimeric spinors" in provider, True)
    sa1 = read("lab/active-research/joe-directed/soldered-ad/"
               "sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md")
    check("C4A SA-1 composes both halves",
          "md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md" in sa1
          and "k77-global-chimeric-spin-reduction" in sa1, True)
    reinspection = read("lab/sources/"
                        "selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md")
    check("C4B reinspection carries the MET(X) row",
          "explicit through `MET(X)`" in reinspection, True)
    bdc = read("lab/active-research/joe-directed/base-duality/"
               "bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md")
    check("C4B BD-C cites the reinspection",
          "selected-k77-source-tangent-branch-source-reinspection-2026-08-09.md" in bdc, True)
    sca = read("lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md")
    check("C4C SC-A adjudicates the one-token variant",
          "group-theoretically impossible" in sca
          and "H19-seven-seven-signature-branch-2026-07-11.md" in sca, True)
    crc = read("lab/process/CURRENT-RESEARCH-CONTEXT.md")
    check("C4 glyph split receipt: CRC carries BOTH Pi_RS spellings",
          "Pi_RS^phys" in crc and "Π_RS^phys" in crc, True)

    print("== C5  file facts under the LIVE_CANDIDATE adjudications ==")
    # C5 REFRESH, IM-1 2026-08-17: the ledger owner applied CP-1's DELTA-1 /
    # DELTA-2 at the v0.259 mint, firing the two designed C5 reds below by
    # design; expectations updated per the documented lifecycle (re-typed
    # ALREADY_COMPOSED in the gate note).  The evidence citation is CONDITION
    # machinery only — the pinned needle keeps that fence in the row text.
    ledger = json.loads(read(gate.latest_ledger_path()))
    rows = {r["id"]: r for r in ledger["rows"]}
    wave_d = read("explorations/resolver-wave-d-native-126-connection-placement-2026-08-03.md")
    check("C5 LT-SM5: wave D built the machinery and left placement open",
          "total P0/Y placement, source selection, VEV, and mass remain open" in wave_d, True)
    check("C5 LT-SM5: row evidence cites wave D since v0.259 (DELTA-1 applied "
          "2026-08-17; was a designed red while un-applied)",
          "resolver-wave-d" in rows["LT-SM5"]["evidence"], True)
    check("C5 LT-SM5: the wave-D citation is fenced as condition machinery, "
          "not advancement",
          "do not read this citation as advancement" in rows["LT-SM5"]["evidence"], True)
    cycle1 = read("explorations/cycle-gates-and-audits/"
                  "cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md")
    check("C5 RA-A6: June gate formalizes the source-selected v_PSB",
          "source-selected v_PSB" in cycle1, True)
    check("C5 RA-A6: June gate records it NOT selected",
          "not selected by current repo data" in cycle1, True)
    check("C5 RA-A6: revival trigger still opens on the watched object and is "
          "re-baselined on the June gate (DELTA-2 applied 2026-08-17; the bar "
          "only rises)",
          rows["RA-A6"]["revival_trigger"].startswith("a source-action-selected v_PSB")
          and "SourceCriticalRankOnePSBSelectionCertificate" in rows["RA-A6"]["revival_trigger"]
          and "(4,1,2) vector also named v_PSB" in rows["RA-A6"]["revival_trigger"], True)
    check("C5 RA-A6: row evidence still does not cite the June gate "
          "(DELTA-2 was trigger-field-only)",
          "cycle1-source-selected-pati-salam" in rows["RA-A6"]["evidence"], False)
    bd1 = read("lab/active-research/joe-directed/baryon-number-and-proton-decay/"
               "bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md")
    check("C5 BD-1: CI-X04 directive presupposes the SU(3,2) form",
          "CI-X04" in bd1 and "SU(3,2)" in bd1, True)
    check("C5 BD-1: does not yet cite the chain adjudication",
          "sca-right-chain" in bd1, False)

    print("== C6  the introduction measurement recorded in the gate ==")
    adjudicated = gate.ADJUDICATED
    counts = {"LIVE_CANDIDATE": 0, "ALREADY_COMPOSED": 0, "SUPERSEDED": 0, "UNTYPED": 0}
    for typ, note in adjudicated.values():
        counts[typ] += 1
        if not note.strip():
            FAIL.append("C6 adjudication with empty note")
    # C6 REFRESH, 2026-08-24: the post-v0.263 corpus has 84 live candidate
    # pairs. Six status/control tokens are excluded by explicit grammar; the
    # 20 remaining new scientific-token pairs are adjudicated from file facts.
    # CP-1's instructed BD-1 flip is applied, and the superseded LT-SM1 pair
    # moves to RETIRED_ADJUDICATIONS rather than remaining a stale live key.
    check("C6 adjudicated live pairs after the v0.263 lifecycle refresh",
          len(adjudicated), 84)
    check("C6 LIVE_CANDIDATE count", counts["LIVE_CANDIDATE"], 0)
    check("C6 ALREADY_COMPOSED count", counts["ALREADY_COMPOSED"], 51)
    check("C6 UNTYPED count", counts["UNTYPED"], 33)
    check("C6 SUPERSEDED live count", counts["SUPERSEDED"], 0)
    check("C6 retired LT-SM1 lifecycle row preserved",
          sorted(gate.RETIRED_ADJUDICATIONS), ["LEDGER:LT-SM1::zeta_F"])
    check("C6 ratchet baseline is zero and may only go down",
          gate.UNADJUDICATED_BASELINE, 0)
    gate_src = read("process_gates/needs_provides_composition_audit.py")
    check("C6 gate states the never-raise rule", "Never raise the baseline" in gate_src, True)
    live_ids = sorted(pid for pid, (typ, _) in adjudicated.items()
                      if typ == "LIVE_CANDIDATE")
    check("C6 no live pair remains after exact lifecycle adjudication",
          live_ids, [])

    print("== C7  register partition (the typing authority; if it moves, re-type) ==")
    reg = read("lab/sources/source-claim-register.yaml")
    check("C7 hard-core rows", len(re.findall(r"^  core: hard-core$", reg, re.M)), 48)
    check("C7 auxiliary rows", len(re.findall(r"^  core: auxiliary$", reg, re.M)), 51)
    check("C7 disavowed-by-source rows",
          len(re.findall(r"^  core: disavowed-by-source$", reg, re.M)), 11)

    print("== C8  the owning artifact ==")
    if os.path.exists(os.path.join(REPO, ARTIFACT)):
        art = read(ARTIFACT)
        check("C8 routing notice carried",
              "GU-COMPARATOR-ROUTING — scope before inference." in art, True)
        check("C8 method path carried",
              "lab/methods/source-native-comparator-routing.md" in art, True)
        check("C8 classification line exact",
              "Classification: `INTERNAL_STRUCTURAL_ONLY`" in art, True)
        check("C8 not-a-kill hatch", "target_claim: NONE-NOT-A-KILL" in art, True)
        check("C8 doc_type declared in the gate-visible head",
              "doc_type: stewardship_record" in art[:400], True)
        check("C8 artifact states the introduction yield",
              "63 candidate pairs" in art and "4 LIVE_CANDIDATE" in art, True)
        check("C8 artifact records the mid-pass FX-2 catch",
              "fx2-typed-carrier-declaration-2026-08-16.md" in art, True)
        check("C8 artifact states the extraction floor honestly",
              '"Neither is supplied."' in art, True)
    else:
        check("C8 artifact present", False, True)

    if os.environ.get("FX1_POISON"):
        check("POISON control (deliberate failure to prove the baseline guard "
              "has power)", True, False)

    if selftest:
        print("== SELFTEST  planted false facts (every one must FAIL a check) ==")
        before = len(FAIL)
        check("PLANT 1: the planted synthetic pair is NOT found",
              planted_id in everything, False)
        check("PLANT 2: the case-variant DOES join without an alias",
              any("norv_w" in p or "Norv_W" in p for p in everything), True)
        check("PLANT 3: the negated provide DOES count as supply",
              any("Qorv_Neg" in p for p in everything), True)
        check("PLANT 4: the alias table has no receipts", receipts_ok, 0)
        check("PLANT 5: K1 rejects the SA-1 provider spelling of P_H",
              gate.tokens_of("it builds (P_H) from the chimeric spinors"), set())
        check("PLANT 6: the register has no disavowed rows",
              len(re.findall(r"^  core: disavowed-by-source$", reg, re.M)), 0)
        check("PLANT 7: MD-1's fork horns do not name P_H",
              'ad(P_H) is inert' in md1, False)
        check("PLANT 8: the reinspection lost its MET(X) row",
              "explicit through `MET(X)`" in reinspection, False)
        caught = len(FAIL) - before
        print()
        if caught != 8:
            print(f"SELFTEST FAILED: expected 8 planted catches, got {caught}")
            return 1
        print("SELFTEST PASSED: 8 planted false facts, all 8 caught.")
        for f in FAIL[before:]:
            print(f"  planted-catch: {f}")
        return 0

    print()
    print(f"{CHECKS} checks run, {len(FAIL)} failed.")
    if FAIL:
        for f in FAIL:
            print(f"  FAILED: {f}")
        return 1
    print("ALL CHECKS PASSED")
    return 0


def run_selftest() -> int:
    """Baseline FIRST, then plants.  A selftest over a dirty baseline proves
    nothing, so it is refused; the poison meta-control proves the guard can
    actually see a dirty baseline."""
    baseline = subprocess.run([sys.executable, __file__], cwd=REPO,
                              capture_output=True, text=True)
    if baseline.returncode != 0:
        print("FX-1 selftest REFUSED: the unmutated baseline is not clean.")
        print(baseline.stdout[-3000:])
        return 1
    poisoned = subprocess.run([sys.executable, __file__], cwd=REPO,
                              capture_output=True, text=True,
                              env={**os.environ, "FX1_POISON": "1"})
    if poisoned.returncode == 0:
        print("FX-1 selftest REFUSED: the poison meta-control did not fail, "
              "so the baseline guard has no power.")
        return 1
    return main(selftest=True)


if __name__ == "__main__":
    sys.exit(run_selftest() if "--selftest" in sys.argv else main())
