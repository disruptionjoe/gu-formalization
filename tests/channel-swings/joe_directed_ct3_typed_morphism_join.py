# -*- coding: utf-8 -*-
"""
CT-3 -- the typed needs/provides join, exercised end to end.

WHAT THIS PROBE IS FOR.  FX-1's join
(process_gates/needs_provides_composition_audit.py) matches EXACT TOKEN
SHAPES.  It is the merge half of a join: its alias table declares two
notations to be one object, under NO ALIAS WITHOUT A RECEIPT.  Its measured
blindness is the split half -- ONE token, TWO objects -- and the dated
instance is `v_PSB`: a rank-one vector in (10bar,1,3) and an independent
rank-one vector in (4,1,2), stabilizer dimension 12 EITHER WAY, so the one
numeric a reader would check cannot separate them.  CP-1 excluded the wrong
one BY HAND, in prose, inside the RA-A6 revival trigger.

CT-3 adds lab/process/needs-provides-typed-records.json (six-key morphism
records) and process_gates/needs_provides_typed_join_audit.py (the typed
join).  This probe certifies:

  LEG S  SCHEMA.  Every record carries exactly {key, dom, cod, map_type,
         source_file, receipt}; every source_file resolves; every receipt is
         {site, rule, quote}.

  LEG C  CODOMAIN.  dom/cod range over CT-1 object ids, CT-1 declared-unknown
         markers, or registered-homonym sense ids that resolve in the
         register; map_type ranges over CT-1's arrow labels.  A three-surface
         triangle (this probe's pinned copies / lab/methods/gu-base-categories.md
         / the gate's derived codomain) must agree, and TWO planted drift
         fixtures -- a reference with an extra layer token, and no reference
         at all -- must each drive the gate red (fail closed).

  LEG R  RECEIPTS.  Every record quote is byte-present in its own
         source_file; the register substrings the discriminator table cites
         are byte-present in the register; and the BYTE-DISJOINTNESS of the
         two v_PSB discriminator sets is RE-MEASURED on the two owning files
         rather than trusted from the register's sentence.

  LEG A  ACCEPTANCE.  The v_PSB test, constructed explicitly from the two
         carriers: RA-A6 and the cycle1 gate resolve to HOM:v_PSB#1, the
         2026-08-12 trace-hq chain gate resolves to HOM:v_PSB#2, the two
         differ, and FX-1's TOKEN join -- given one injected provide verb in
         an in-memory copy of the real trace-hq file -- offers BOTH carriers
         while the typed join rejects the wrong one.

  LEG P  PLANTED CONTROLS.  A wrong-dom edge that MUST be rejected; a forged
         dom; a forged alias with no receipt; a quote drift.  And the
         CONTRARY control, which is the point: the CORRECT cross-file typed
         edge (RA-A6 <- cycle1) must SURVIVE as TYPE-VERIFIED.  A join that
         rejected everything would pass a rejection test and be worthless.

  LEG D  DETECTOR POWER (VERIFICATION.md rule 4).  Absence results prove
         nothing unless the detector fires on synthetic positives: a
         non-CT-1 dom, a bogus arrow label, a non-disjoint discriminator, a
         registered homonym typed by its stratum, and a record whose rule
         does not re-derive its own dom are each PLANTED and each DETECTED.

  LEG F  PLANTED-FALSE.  Five predeclared FALSE propositions each observed
         False.

  LEG B  BEHAVIOUR PRESERVATION on FX-1.  Asserted unconditionally: FX-1's
         gate references NEITHER CT-3 surface, and CT-3 never writes to any
         FX-1 path.  PRINTED as a dated reconciliation, and asserted only
         under --strict (the shared-checkout rule: FX-1's owner may
         legitimately edit its own ADJUDICATED map while this probe runs):
         the FX-1 module and alias-table digests measured at the CT-3 mint,
         FX-1's gate exit code and un-adjudicated set, and FX-1's own probe
         still exiting 0.

  LEG G  RUNTIME.  The gate is green, its --selftest is GREEN by subprocess
         (12/12 machinery mutations), its --poison path refuses, and the
         design artifact carries the routing notice, the
         INTERNAL_STRUCTURAL_ONLY classification in the routing audit's
         accepted form, NONE-NOT-A-KILL, the printed integrator write, and
         exactly one gu-typed-objects block with every required key.

Exit 0 == every check passed.  --selftest verifies the CLEAN BASELINE FIRST
(an unmutated subprocess must exit 0 and print its certificate BEFORE any
mutation is attempted), then injects eleven MACHINERY mutations via
CT3P_MUTATE -- never a loosened predicate, which would be undetectable by
construction -- each required to drive exit 1 THROUGH a genuine "  FAIL" line
on a run that still prints its certificate; a nonzero exit with no
certificate is CRASH-NOT-DETECTION and fails the selftest.
--selftest --poison poisons the baseline run itself and demands the refusal.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[2]   # never mutated
MUT = os.environ.get("CT3P_MUTATE", "")

# The classic path bug (VERIFICATION.md incident 3: every mutant ran one
# directory deep and all fifteen "catches" were crashes).  Only the probe's
# FILE READS follow the mutated root, so the corruption surfaces as genuine
# FAIL lines instead of an import crash.
ROOT = REPO / "tests" if MUT == "root-elsewhere" else REPO

GATE_REL = "process_gates/needs_provides_typed_join_audit.py"
FX1_REL = "process_gates/needs_provides_composition_audit.py"
FX1_ALIAS_REL = "lab/process/needs-provides-alias-table.json"
FX1_PROBE_REL = "tests/channel-swings/joe_directed_fx1_needs_provides_join.py"
SIDECAR_REL = "lab/process/needs-provides-typed-records.json"
REFERENCE_REL = "lab/methods/gu-base-categories.md"
REGISTER_REL = "lab/process/homonym-register.yaml"
ARTIFACT_REL = ("lab/active-research/joe-directed/ct-hardening/"
                "ct3-typed-morphism-join-2026-08-17.md")

CYCLE1 = ("explorations/cycle-gates-and-audits/"
          "cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md")
TRACEHQ = ("explorations/conditional-build/"
           "selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md")

# Measured at the CT-3 mint (2026-08-17), BEFORE and AFTER the four CT-3
# writes -- identical both times.  Reconciliation pins, asserted only under
# --strict so a legitimate FX-1 edit by its own owner does not red this lane.
FX1_MINT_SHA = "e3b165261866d3b5318b8564a738b26fb00c27567fcd36ec4aa085c3be2e3e1b"
FX1_ALIAS_MINT_SHA = ("ba6a03ad03c886339b11ddcb26f1963ea342888340762d45a672"
                      "134785919033")
FX1_MINT_UNADJUDICATED = 5      # pre-existing, from live sibling channels
FX1_MINT_GATE_EXIT = 1          # pre-existing red, NOT caused by CT-3

# This probe's own pinned copies of CT-1's machine block -- the third surface
# of the triangle, so the gate and the reference cannot agree with each other
# while both having drifted from what was reviewed.
PIN_LAYER_TOKENS = ("ambient", "observed", "source-print", "toy", "UNTYPED")
PIN_MAP_TOKENS = ("projection", "contraction", "inclusion", "restriction",
                  "pullback", "pushforward", "quotient", "isomorphism",
                  "homomorphism", "intertwiner", "evaluation", "not-a-map",
                  "UNTYPED")

PASS = 0
FAIL = 0
STRICT = "--strict" in sys.argv


def check(label: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  ok    {label}")
    else:
        FAIL += 1
        print(f"  FAIL  {label}" + (f"  [{detail}]" if detail else ""))
    return bool(cond)


def note(label: str, value) -> None:
    print(f"  ..    {label}: {value}")


def read(rel: str) -> str:
    if MUT == "quote-reader-empty":              # machinery corruption
        return ""
    p = ROOT / rel
    text = p.read_text(encoding="utf-8", errors="replace") if p.is_file() else ""
    if MUT == "register-reader-truncate" and rel == REGISTER_REL:
        text = text[:500]                        # machinery corruption
    if MUT == "fx1-src-poisoned" and rel == FX1_REL:
        text += "\nSIDECAR = 'needs-provides-typed-records'\n"
    return text


def sha(rel: str) -> str:
    p = ROOT / rel
    return (hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file()
            else "<absent>")


def load_gate():
    path = REPO / GATE_REL
    spec = importlib.util.spec_from_file_location("ct3_gate", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if MUT == "fx1-import-stub":                  # machinery corruption
        mod.FX1.join = lambda extra_md=None: ({}, {}, {})
    if MUT == "sense-resolver-collapse":          # machinery corruption
        real_token = "v_PSB"
        mod.sense_index = (lambda text, entry:
                           (f"HOM:{real_token}#1",
                            "homonym-sense-by-discriminator", real_token))
    return mod


def load_sidecar() -> dict:
    data = json.loads(read(SIDECAR_REL) or "{}")
    if MUT == "sidecar-loader-drops-keys":        # machinery corruption
        for rec in data.get("records", []):
            rec.pop("cod", None)
    if MUT == "records-truncated":                # machinery corruption
        data["records"] = data.get("records", [])[:3]
    if MUT == "disjoint-swap":                    # machinery corruption
        for entry in data.get("sense_discriminators", []):
            a, b = entry["senses"][0], entry["senses"][1]
            a["discriminators"], b["discriminators"] = (
                b["discriminators"], a["discriminators"])
    return data


def run(argv: list[str], env_extra: dict | None = None):
    env = dict(os.environ)
    env.pop("CT3_MUTATE", None)
    env.pop("CT3P_MUTATE", None)
    if env_extra:
        env.update(env_extra)
    if MUT == "gate-subprocess-elsewhere" and argv and argv[0] == GATE_REL:
        argv = ["process_gates/__ct3_absent_gate__.py"] + argv[1:]
    return subprocess.run([sys.executable] + argv, cwd=str(REPO), env=env,
                          capture_output=True, text=True)


# ===========================================================================
def main() -> int:
    print("CT-3 typed morphism join -- probe")
    gate = load_gate()
    sidecar = load_sidecar()
    records = sidecar.get("records", [])
    ref = gate.load_reference()
    register = gate.load_register()
    if MUT == "codomain-parse-blind":            # machinery corruption
        ref["object_ids"] = set()
        ref["layer_object"] = {}

    # ---------------- LEG S: schema ----------------
    print("\nLEG S  SCHEMA")
    six = {"key", "dom", "cod", "map_type", "source_file", "receipt"}
    check("S1 sidecar carries the declared top-level sections",
          all(k in sidecar for k in ("record_shape", "laws", "sources",
                                     "sense_discriminators",
                                     "sense_discriminators_refused",
                                     "dom_aliases", "records")))
    check("S2 record_shape declares exactly the six briefed keys",
          list(sidecar.get("record_shape", {}).get("keys", [])) ==
          ["key", "dom", "cod", "map_type", "source_file", "receipt"],
          str(sidecar.get("record_shape", {}).get("keys")))
    bad_shape = [r.get("key") for r in records if set(r) != six]
    check("S3 every record has exactly the six keys", not bad_shape,
          str(bad_shape[:4]))
    missing_src = [r.get("key") for r in records
                   if not (ROOT / r.get("source_file", "__none__")).is_file()]
    check("S4 every source_file resolves", not missing_src,
          str(missing_src[:4]))
    bad_receipt = [r.get("key") for r in records
                   if set(r.get("receipt", {})) != {"site", "rule", "quote"}]
    check("S5 every receipt is {site, rule, quote}", not bad_receipt,
          str(bad_receipt[:4]))
    check("S6 the record population is non-trivial", len(records) >= 20,
          str(len(records)))
    note("records", len(records))

    # ---------------- LEG C: codomain ----------------
    print("\nLEG C  CODOMAIN (three-surface triangle + fail-closed drift)")
    check("C1 reference supplies the Source-Layer objects L1..L4",
          {"L1", "L2", "L3", "L4"} <= ref["object_ids"])
    check("C2 reference supplies the Carrier objects C1..C11",
          {f"C{i}" for i in range(1, 12)} <= ref["object_ids"])
    check("C3 probe pins == reference layer tokens",
          set(PIN_LAYER_TOKENS) == set(ref["layer_tokens"]),
          str(ref["layer_tokens"]))
    check("C4 probe pins == reference arrow labels",
          set(PIN_MAP_TOKENS) == set(ref["map_tokens"]))
    check("C5 the four LAYER strata map to distinct Carrier objects",
          sorted(ref["layer_object"].values()) == ["C1", "C2", "C3", "C4"],
          str(ref["layer_object"]))

    def dom_ok(v: str) -> bool:
        if v in ("UNTYPED", "HOMONYM-AMBIGUOUS") or v in ref["object_ids"]:
            return True
        if v.startswith("HOM:"):
            tok, _, n = v[4:].rpartition("#")
            return tok in register and n.isdigit() and \
                1 <= int(n) <= register[tok]["sense_count"]
        return False

    bad_dom = [(r.get("key"), r.get(s)) for r in records
               for s in ("dom", "cod") if not dom_ok(r.get(s, ""))]
    check("C6 every dom/cod is a CT-1 id, a CT-1 marker, or a resolvable "
          "sense id", not bad_dom, str(bad_dom[:4]))
    bad_map = [(r.get("key"), r.get("map_type")) for r in records
               if r.get("map_type") not in ref["map_tokens"]]
    check("C7 every map_type is a CT-1 arrow label", not bad_map,
          str(bad_map[:4]))

    with tempfile.TemporaryDirectory() as td:
        drift = pathlib.Path(td) / "ref.md"
        drift.write_text(read(REFERENCE_REL).replace(
            "layer-tokens: ambient observed",
            "layer-tokens: ambient observed extra-stratum"), encoding="utf-8")
        r = run([GATE_REL], {"CT3_MUTATE": "ref-layer-drift"})
        check("C8 planted reference drift drives the gate red",
              r.returncode == 1 and "[FAIL]" in r.stdout)
        r = run([GATE_REL], {"CT3_MUTATE": "ref-gone"})
        check("C9 an ABSENT reference drives the gate red (fail closed)",
              r.returncode == 1 and "[FAIL]" in r.stdout)

    # ---------------- LEG R: receipts ----------------
    print("\nLEG R  RECEIPTS (byte-level, re-measured)")
    lost = [r.get("key") for r in records
            if r.get("receipt", {}).get("quote", "\0")
            not in read(r.get("source_file", "__none__"))]
    check("R1 every record quote is byte-present in its own source_file",
          not lost, str(lost[:4]))
    reg_text = read(REGISTER_REL)
    disc = {e["token"]: e for e in sidecar.get("sense_discriminators", [])}
    check("R2 the discriminator table holds exactly the v_PSB entry",
          set(disc) == {"v_PSB"}, str(sorted(disc)))
    entry = disc.get("v_PSB", {"senses": [{"index": 1, "discriminators": []},
                                          {"index": 2, "discriminators": []}],
                               "receipts": {"register_must_contain": []}})
    for needle in entry["receipts"]["register_must_contain"]:
        check(f"R3 register still states {needle[:44]!r}", needle in reg_text)
    c1_text, hq_text = read(CYCLE1), read(TRACEHQ)
    # Read the discriminators OUT OF THE TABLE, so a table that no longer
    # says what the register says cannot pass by agreeing with a hardcoded
    # copy of the right answer.
    senses = {sn["index"]: sn for sn in entry["senses"]}
    d1 = senses.get(1, {}).get("discriminators", [])
    d2 = senses.get(2, {}).get("discriminators", [])
    check("R4a the table's sense-1 owning file IS the cycle1 carrier",
          senses.get(1, {}).get("owning_file") == CYCLE1)
    check("R4b the table's sense-2 owning file IS the trace-hq carrier",
          senses.get(2, {}).get("owning_file") == TRACEHQ)
    check("R4 recorded sense-1 discriminator present in the cycle1 carrier",
          bool(d1) and all(d in c1_text for d in d1), str(d1))
    check("R5 recorded sense-2 discriminator ABSENT from the cycle1 carrier",
          bool(d2) and not any(d in c1_text for d in d2), str(d2))
    check("R6 recorded sense-2 discriminator present in the trace-hq carrier",
          bool(d2) and all(d in hq_text for d in d2), str(d2))
    check("R7 recorded sense-1 discriminator ABSENT from the trace-hq carrier",
          bool(d1) and not any(d in hq_text for d in d1), str(d1))
    check("R8 both carriers really do write the SAME token",
          "v_PSB" in c1_text and "v_PSB" in hq_text)
    check("R9 the register records that the numeric cannot discriminate",
          "stabilizer dimension CANNOT" in reg_text)
    refused = sidecar.get("sense_discriminators_refused", [])
    check("R10 refused discriminator entries each carry a reason",
          all(e.get("reason", "").strip() for e in refused) and
          len(refused) == 2)
    for e in refused:
        check(f"R11 refusal receipt for {e['token']!r} is live in the register",
              e["register_must_contain"] in reg_text)
    check("R12 dom_aliases is empty (nothing merged without a receipt)",
          sidecar.get("dom_aliases", "absent") == [])

    # ---------------- LEG A: acceptance ----------------
    print("\nLEG A  ACCEPTANCE -- the two v_PSB carriers")
    acc = gate.vpsb_acceptance(records, sidecar)
    check("A1 RA-A6's need side resolves to HOM:v_PSB#1",
          acc["need_dom"] == "HOM:v_PSB#1", acc["need_dom"])
    check("A2 it resolves BY LINEAGE (its trigger names both representations, "
          "so the discriminator rule must not decide it)",
          acc["need_rule"] == "homonym-sense-by-owning-file", acc["need_rule"])
    check("A3 the cycle1 carrier resolves to HOM:v_PSB#1",
          acc["cycle1_dom"] == "HOM:v_PSB#1", acc["cycle1_dom"])
    check("A4 the trace-hq carrier resolves to HOM:v_PSB#2",
          acc["tracehq_dom"] == "HOM:v_PSB#2", acc["tracehq_dom"])
    check("A5 THE ACCEPTANCE TEST: the two carriers are distinguished",
          acc["cycle1_dom"] != acc["tracehq_dom"])
    check("A6 the planted provide-verb control applied to real bytes",
          acc["mutation_applied"])
    check("A7 FX-1's TOKEN join then offers BOTH carriers (the blindness, "
          "demonstrated rather than asserted)",
          set(acc["token_join_providers"]) == {CYCLE1, TRACEHQ},
          str(acc["token_join_providers"]))
    check("A8 the typed join REJECTS the wrong-dom carrier",
          len(acc["rejected"]) == 1 and
          acc["rejected"][0]["provider"] == TRACEHQ)
    check("A9 CONTRARY CONTROL: the correct cross-file edge SURVIVES",
          len(acc["verified"]) == 1 and
          acc["verified"][0]["provider"] == CYCLE1)
    live_records = gate.extract_records(sidecar, ref)
    live_by = {(r["receipt"]["site"], r["key"]): r for r in live_records}
    check("A10 re-derivation: the LIVE rules reproduce the cycle1 typing",
          live_by.get((f"FILE:{CYCLE1}", "v_PSB"), {}).get("dom")
          == "HOM:v_PSB#1",
          str(live_by.get((f"FILE:{CYCLE1}", "v_PSB"), {}).get("dom")))
    check("A11 re-derivation: the LIVE rules reproduce the trace-hq typing",
          live_by.get((f"FILE:{TRACEHQ}", "v_PSB"), {}).get("dom")
          == "HOM:v_PSB#2",
          str(live_by.get((f"FILE:{TRACEHQ}", "v_PSB"), {}).get("dom")))
    check("A12 re-derivation: the LIVE rules still SEPARATE the two carriers "
          "(a resolver that collapsed them would pass every recorded-value "
          "check and fail this one)",
          live_by.get((f"FILE:{CYCLE1}", "v_PSB"), {}).get("dom")
          != live_by.get((f"FILE:{TRACEHQ}", "v_PSB"), {}).get("dom"))
    check("A13 the surviving edge is typed by agreement, not by default",
          acc["verified"] and
          acc["verified"][0]["need_dom"] == acc["verified"][0]["prov_dom"]
          and acc["verified"][0]["need_dom"] not in ("UNTYPED",
                                                     "HOMONYM-AMBIGUOUS"))

    # ---------------- LEG P: planted controls ----------------
    print("\nLEG P  PLANTED CONTROLS")
    for mut, label in (("sidecar-forged-dom",
                        "P1 a forged dom (trace-hq re-typed as sense 1)"),
                       ("sidecar-forged-alias",
                        "P2 a dom alias with NO receipt"),
                       ("sidecar-quote-drift",
                        "P3 a receipt quote that no longer occurs"),
                       ("discriminator-not-disjoint",
                        "P4 a discriminator that is not byte-disjoint"),
                       ("sense-collapse",
                        "P5 a resolver that collapses both senses to one")):
        r = run([GATE_REL], {"CT3_MUTATE": mut})
        check(f"{label} is CAUGHT",
              r.returncode == 1 and "[FAIL]" in r.stdout,
              f"exit {r.returncode}")

    live = gate.typed_join(records, sidecar)
    check("P6 on the UNTOUCHED tree the join rejects nothing (stated, not "
          "hidden)", len(live["rejected"]) == 0, str(len(live["rejected"])))
    check("P7 and it does decide the one edge it can",
          len(live["verified"]) >= 1)
    note("live edges", f"{live['total']} total, {len(live['verified'])} "
                       f"verified, {len(live['rejected'])} rejected, "
                       f"{len(live['unverified'])} unverified")
    note("live pairs", f"{live['pairs_decided']}/{live['pairs']} decided")

    # ---------------- LEG D: detector power ----------------
    print("\nLEG D  DETECTOR POWER (synthetic positives)")
    base = json.loads(read(SIDECAR_REL) or "{}")

    def audit_with(mutate_records) -> bool:
        """Run the gate's own checks over a doctored sidecar in a temp copy.

        If the sidecar cannot be read at all, the fixture cannot be planted:
        report that as a FAILED detector-power check rather than crashing, so
        a machinery corruption upstream still ends in a certificate line.
        """
        doc = json.loads(read(SIDECAR_REL) or "{}")
        if not doc.get("records"):
            return False
        mutate_records(doc)
        with tempfile.TemporaryDirectory() as td:
            tmp = pathlib.Path(td) / "sidecar.json"
            tmp.write_text(json.dumps(doc), encoding="utf-8")
            real = gate.SIDECAR
            try:
                gate.SIDECAR = tmp
                fails, _rep = gate.run_audit()
            finally:
                gate.SIDECAR = real
        return bool(fails)

    if not base.get("records"):
        check("D0 the detector-power leg has a sidecar to doctor", False,
              "sidecar unreadable")
    check("D1 a non-CT-1 dom is DETECTED",
          audit_with(lambda d: d["records"][0].__setitem__("dom", "C99")))
    check("D2 a bogus arrow label is DETECTED",
          audit_with(lambda d: d["records"][0].__setitem__("map_type",
                                                           "teleportation")))
    check("D3 an out-of-range sense id is DETECTED",
          audit_with(lambda d: d["records"][0].__setitem__("dom",
                                                           "HOM:v_PSB#7")))
    check("D4 a five-key record is DETECTED",
          audit_with(lambda d: d["records"][0].pop("cod")))
    check("D5 a dangling source_file is DETECTED",
          audit_with(lambda d: d["records"][0].__setitem__(
              "source_file", "lab/process/__ct3_no_such_file__.md")))
    check("D6 a record whose rule no longer re-derives its dom is DETECTED",
          audit_with(lambda d: [r.__setitem__("dom", "C4")
                                for r in d["records"]
                                if r["key"] == "v_PSB" and
                                r["receipt"]["site"] == "LEDGER:RA-A6"]))

    # ---------------- LEG F: planted-false ----------------
    print("\nLEG F  PLANTED-FALSE PROPOSITIONS (each must be False)")
    check("F1 'the two senses differ in stabilizer dimension' is False",
          not ("stabilizer dimension CAN discriminate" in reg_text))
    check("F2 'FX-1's token join separates the two carriers' is False",
          len(set(acc["token_join_providers"])) == 2)
    ledger_text = read(gate.FX1.latest_ledger_path())
    ledger_rows = json.loads(ledger_text)["rows"] if ledger_text else None
    check("F3 'ledger v0.259 rows carry a context field' is False",
          ledger_rows is not None and
          not any("context" in r for r in ledger_rows),
          "ledger unreadable" if ledger_rows is None else "")
    check("F4 'CT-3 recorded a dom alias' is False",
          sidecar.get("dom_aliases", "absent") == [])
    check("F5 'CT-1 has an object for a mixed layer' is False",
          not any("+" in n for n in ref["layer_object"]))

    # ---------------- LEG B: behaviour preservation ----------------
    print("\nLEG B  FX-1 BEHAVIOUR PRESERVATION")
    fx1_src = read(FX1_REL)
    check("B1 FX-1's gate references neither CT-3 surface",
          "needs-provides-typed-records" not in fx1_src and
          "needs_provides_typed_join_audit" not in fx1_src)
    gate_src = read(GATE_REL)
    check("B2 CT-3's gate writes exactly one file, its own sidecar",
          re.findall(r"(\w+)\.write_text", gate_src) == ["SIDECAR"],
          str(re.findall(r"(\w+)\.write_text", gate_src)))
    fx1_sha = sha(FX1_REL)
    alias_sha = sha(FX1_ALIAS_REL)
    note("FX-1 module sha256", fx1_sha[:16] + f" (mint {FX1_MINT_SHA[:16]})")
    note("FX-1 alias-table sha256",
         alias_sha[:16] + f" (mint {FX1_ALIAS_MINT_SHA[:16]})")
    r = run([FX1_REL])
    unadj = re.search(r"(\d+) UNADJUDICATED", r.stdout + r.stderr)
    unadj_n = int(unadj.group(1)) if unadj else -1
    note("FX-1 gate", f"exit {r.returncode}, {unadj_n} un-adjudicated "
                      f"(mint: exit {FX1_MINT_GATE_EXIT}, "
                      f"{FX1_MINT_UNADJUDICATED})")
    rp = run([FX1_PROBE_REL])
    note("FX-1 probe", f"exit {rp.returncode}")
    recon = (fx1_sha == FX1_MINT_SHA and alias_sha == FX1_ALIAS_MINT_SHA and
             r.returncode == FX1_MINT_GATE_EXIT and
             unadj_n == FX1_MINT_UNADJUDICATED and rp.returncode == 0)
    if STRICT:
        check("B3 --strict: FX-1 digests, gate exit/un-adjudicated count and "
              "probe result all equal the CT-3 mint measurement", recon)
    else:
        check("B3 FX-1 reconciliation PRINTED (assert under --strict; FX-1's "
              "owner may edit its own ADJUDICATED map concurrently)",
              True if recon else True,
              "reconciled" if recon else "drifted -- see the printed lines")
        note("B3 reconciliation", "matches the mint" if recon
             else "DRIFTED from the mint (informational, not this lane's red)")
    check("B4 CT-3's gate imports FX-1 read-only (no assignment into it)",
          "FX1." in gate_src and
          not re.search(r"^\s*FX1\.\w+\s*=", gate_src, re.M))

    # ---------------- LEG G: runtime + artifact ----------------
    print("\nLEG G  RUNTIME AND ARTIFACT")
    r = run([GATE_REL])
    check("G1 the typed-join gate is GREEN",
          r.returncode == 0 and "0 FAIL" in r.stdout, r.stdout[-160:])
    r = run([GATE_REL, "--selftest"])
    check("G2 gate --selftest is GREEN by subprocess",
          r.returncode == 0 and "SELFTEST GREEN" in r.stdout)
    check("G3 gate --selftest verified its CLEAN BASELINE FIRST",
          "clean baseline first" in r.stdout)
    check("G4 gate --selftest caught 12/12 machinery mutations",
          "12/12" in r.stdout, r.stdout[-160:])
    check("G5 no gate mutation was a MISSED one", "MISSED" not in r.stdout)
    check("G6 no gate mutation was CRASH-NOT-DETECTION",
          "CRASH-NOT-DETECTION" not in r.stdout)
    r = run([GATE_REL, "--selftest", "--poison"])
    check("G7 gate --selftest --poison refuses to bank mutations",
          r.returncode == 1 and "mutations were NOT run" in r.stdout)

    art = read(ARTIFACT_REL)
    check("G8 artifact carries the routing notice", "GU-COMPARATOR-ROUTING" in art)
    check("G9 artifact points at the routing method",
          "lab/methods/source-native-comparator-routing.md" in art)
    check("G10 artifact is classified INTERNAL_STRUCTURAL_ONLY in the "
          "routing audit's accepted form",
          bool(re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                         art)))
    check("G11 artifact declares target_claim: NONE-NOT-A-KILL",
          "target_claim: NONE-NOT-A-KILL" in art)
    check("G12 artifact prints the integrator write it does NOT perform",
          '"classification": "INTERNAL_STRUCTURAL_ONLY"' in art)
    check("G13 artifact declares canonical_effect: pending_integration",
          "canonical_effect: pending_integration" in art)
    blocks = re.findall(r"^```gu-typed-objects[ \t]*\n(.*?)^```", art,
                        re.M | re.S)
    check("G14 artifact carries exactly one gu-typed-objects block",
          len(blocks) == 1, str(len(blocks)))
    if blocks:
        for key in ("result", "carrier", "pairing", "real_structure",
                    "grading", "action_owner", "target"):
            check(f"G15 typed block declares {key}:",
                  re.search(rf"^{key}:", blocks[0], re.M) is not None)
        check("G16 typed block declares its LAYER and MAP-TYPE",
              "LAYER=" in blocks[0] and "MAP-TYPE=" in blocks[0])
    check("G17 artifact states the coverage fraction rather than burying it",
          "1 of 182" in art and "1 of 69" in art)
    check("G18 artifact concedes the zero-live-rejection fact",
          "Zero rejections on the untouched corpus" in art)
    check("G19 artifact records the hostile catches that changed the build",
          all(f"Catch {n}" in art for n in (1, 2, 3)))
    check("G20 sidecar states the no-guessing law",
          "no_guessing" in read(SIDECAR_REL))
    check("G21 sidecar states the discriminator receipt law",
          "no_discriminator_without_a_receipt" in read(SIDECAR_REL))
    check("G22 sidecar declares R2 unavailable with its measurement",
          base.get("sources", {}).get("R2_ledger_context", {})
          .get("available", "absent") is False)

    print(f"\n{PASS + FAIL} checks run, {FAIL} failed.")
    print("CERTIFICATE: " + ("ALL CHECKS PASSED" if FAIL == 0
                             else f"{FAIL} FAILED"))
    return 0 if FAIL == 0 else 1


MUTATIONS = (
    "root-elsewhere", "sidecar-loader-drops-keys", "codomain-parse-blind",
    "quote-reader-empty", "disjoint-swap", "sense-resolver-collapse",
    "fx1-import-stub", "register-reader-truncate",
    "gate-subprocess-elsewhere", "fx1-src-poisoned", "records-truncated",
)


def selftest(poison: bool) -> int:
    env = dict(os.environ)
    env.pop("CT3P_MUTATE", None)
    args = [sys.executable, str(pathlib.Path(__file__).resolve())]
    if poison:
        env["CT3P_MUTATE"] = "root-elsewhere"
    base = subprocess.run(args, cwd=str(REPO), env=env, capture_output=True,
                          text=True)
    print("SELFTEST: clean baseline first --")
    print("  " + (base.stdout.strip().splitlines() or ["<no output>"])[-1])
    if base.returncode != 0:
        print("SELFTEST: clean baseline does NOT pass; mutations were NOT run")
        print("SELFTEST FAILED")
        return 1
    if poison:
        print("SELFTEST: poisoned baseline passed -- the guard is inert")
        print("SELFTEST FAILED")
        return 1
    ok = True
    for m in MUTATIONS:
        env = dict(os.environ)
        env["CT3P_MUTATE"] = m
        r = subprocess.run(args, cwd=str(REPO), env=env, capture_output=True,
                           text=True)
        completed = "CERTIFICATE:" in r.stdout
        genuine = "  FAIL" in r.stdout
        caught = r.returncode == 1 and completed and genuine
        label = ("caught (exit 1, genuine FAIL)" if caught else
                 "MISSED (exit 0)" if r.returncode == 0 else
                 "CRASH-NOT-DETECTION (no certificate line)")
        print(f"  mutation {m}: {label}")
        ok = ok and caught
    print("SELFTEST " + (f"GREEN: clean baseline first, then {len(MUTATIONS)}/"
                         f"{len(MUTATIONS)} machinery mutations each exit 1 "
                         f"via genuine FAIL lines" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(selftest(poison="--poison" in sys.argv))
    sys.exit(main())
