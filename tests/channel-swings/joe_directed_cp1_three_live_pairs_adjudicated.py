#!/usr/bin/env python3
"""CP-1 probe: the three FX-1 live compositions, adjudicated against file facts.

Certifies the adjudication record
lab/active-research/joe-directed/composition/cp1-three-live-pairs-adjudicated-2026-08-17.md:

  L1/L2  LEDGER:LT-SM5::Y_C / ::Y_K  -> CONDITION via wave-D (DELTA-1,
         evidence field only, machinery only); the rb4 provider leg DOES NOT
         COMPOSE (provider-side mood-blindness: "until ... are built" is a
         requirement, not supply).
  L3     LEDGER:RA-A6::v_PSB         -> COMPOSES; same object by lineage
         receipt (CB-A:A6 -> cb-a:222 -> cycle1, (10bar,1,3)); DELTA-2
         re-baselines the trigger to fire on SELECTION, never formalization;
         an UNREGISTERED near-collision (the (4,1,2) trace-hq v_psb) is
         flagged to the homonym channel.
  L4     ART:bd1::SU(3,2)            -> CONSISTENT with SC-A's decided
         reading at reconstruction grade; no amendment, no promotion to a
         source determination, no delta owed anywhere.

Sections: A base-revision row facts (v0.258, the deltas' exact base);
B wave-D facts; C rb4 refusal facts; D cycle1/lineage/near-collision facts
(incl. the byte-level contrary controls: cycle1 has zero "(4,1,2)", the
trace-hq gate zero "(10bar,1,3)"); E CI-X04/BD-1/SC-A facts incl. both
no-citation directions; F composition-gate adjudication data; G artifact
conformance incl. both delta texts; H typed-carrier gate compliance;
I planted controls (validator liveness, mood discriminator both directions,
false-quote refusal).

LIFECYCLE CHECKS, by design (FX-1 Attack-5 pattern): the still-uncited /
still-unamended / still-silent checks (A3, A6, B16, D29, D30, E43, E49) red
when the respective owner ACTS -- apply the delta, add the register entry,
write SC-GRP-50 -- and the red's message names the follow-up (re-type the
pair ALREADY_COMPOSED, refresh FX-1's C5/C6, retire the check).  That red is
the designed tripwire, not a defect.

--selftest: verifies the CLEAN BASELINE passes FIRST, then applies 6
mutations, each corrupting machinery or a reference (never loosening a
check); a catch counts ONLY via >= 1 genuine [FAIL] line through the normal
check path -- a mutation "caught" by a crash is REJECTED and fails the
selftest.
"""

from __future__ import annotations

import copy
import io
import json
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "process_gates"))

ART = ("lab/active-research/joe-directed/composition/"
       "cp1-three-live-pairs-adjudicated-2026-08-17.md")

# Every path, needle and expectation the checks consume.  The selftest
# mutates COPIES of this dict; the checks themselves are never edited.
REFS = {
    "ledger_base": "lab/process/conditional-physics-ledger-v0.258.json",
    "row_lt_sm5": "LT-SM5",
    "row_ra_a6": "RA-A6",
    "lt_sm5_evidence": "selected-k77-varpi-radial-half-exchange-gate-2026-08-12.md",
    "ra_a6_trigger": "a source-action-selected v_PSB",
    "ra_a6_evidence": "selected-k77-moving-hq-u3_2-sm-higgs-direction-gate-2026-08-12.md",
    "wave_d": "explorations/resolver-wave-d-native-126-connection-placement-2026-08-03.md",
    "wave_d_grade_needle": "total P0/Y placement, source selection, VEV, and mass remain open",
    "wave_d_boundary": "No total `P0/rho/Y_K/Y_C/C` full-20 kernel is built.",
    "wave_d_k_density": "Herm(P0^dagger K_G c_rho(T) Y_K P0)",
    "wave_d_c_density": "P0^T C c_rho(T) Y_C P0",
    "wave_d_next_gate": "RESOLVER-WAVE-E-SOURCE-OWNED-MOVING-252-FULL20-PLACEMENT",
    "wave_d_step4": "`P0` and the actual ordered `Y_K/Y_C` factors",
    "wave_d_sa_y1": ("bare spinor factor cannot close `SA-Y1` or a mass row "
                     "without the actual total"),
    "wave_d_false_quote": ("total P0/Y placement, source selection, VEV, and "
                           "mass are now closed"),
    "rb4": "lab/evidence/predecessor-records/rb4-observer-cartan-moving-family.md",
    "rb4_until": "until the moving reduction and zero-order",
    "mood_pattern": r"\buntil\b",
    "sa1_provider_line": "it builds (P_H) from the chimeric spinors",
    "cycle1": ("explorations/cycle-gates-and-audits/"
               "cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md"),
    "cycle1_formalizes": "source-selected v_PSB in the rank-one orbit of V_PSB",
    "cycle1_not_selected": "rank-one v_PSB object: not selected by current repo data.",
    "cycle1_rep": "V_PSB = (10bar,1,3)",
    "cycle1_cert": "SourceCriticalRankOnePSBSelectionCertificate",
    "cycle1_nogo": "choose v_PSB because its stabilizer is SM-like",
    "cb_a": "explorations/conditional-build/cb-a-representation-content-2026-08-05.md",
    "cb_a_lineage": ["source-selected rank-one", "(10bar,1,3)",
                     "cycle1-source-selected-pati-salam-stabilizer-gate-2026-06-24.md"],
    "higgs_gate": ("explorations/conditional-build/"
                   "selected-k77-moving-hq-u3_2-sm-higgs-direction-gate-2026-08-12.md"),
    "homonym_register": "lab/process/homonym-register.yaml",
    "trace_hq": ("explorations/conditional-build/"
                 "selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md"),
    "trace_hq_412": "independent rank-one vector in `(4,1,2)`",
    "trace_hq_probe": ("tests/channel-swings/"
                       "selected_k77_trace_hq_connection_internal_chain_probe.py"),
    "trace_hq_kron": "v_psb = sp.kronecker_product(e4, fR)",
    "crosswalk": "lab/process/curt-iceberg-native-crosswalk.json",
    "cix04_claim": ("The SU(3,2) real form is said to avoid classic "
                    "proton-decay problems of older GUT choices."),
    "cix04_directive": ("Require the selected representation, heavy mediators, "
                        "baryon-number operators, and decay-amplitude calculation."),
    "bd1": ("lab/active-research/joe-directed/baryon-number-and-proton-decay/"
            "bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md"),
    "bd1_fence": ("reported object is `SU(3,2)`, the computed object is "
                  "`so(6,4)`"),
    "bd1_different_group": "A candidate exact mechanism now exists for a *different* group",
    "sca": "lab/active-research/joe-directed/source-chain/sca-right-chain-2026-08-15.md",
    "sca_r6": "Spin(6,4) > SU(3,2) > S(U(3)xU(2))",
    "sca_not_breaking": "its two arrows are **not** symmetry",
    "sca_reductions": "structure-group reductions of one rank-10 bundle",
    "sca_audio": "CONFIRMATION AGAINST THE ACTUAL RECORDING IS STILL OWED",
    "sca_embedding": "X^T eta_{6,4} + eta_{6,4} X = 0",
    "claim_register": "lab/sources/source-claim-register.yaml",
    "artifact": ART,
    "pair_l1": "LEDGER:LT-SM5::Y_C",
    "pair_l2": "LEDGER:LT-SM5::Y_K",
    "pair_l3": "LEDGER:RA-A6::v_PSB",
    "pair_l4": ("ART:lab/active-research/joe-directed/baryon-number-and-proton-decay/"
                "bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md::SU(3,2)"),
    "l4_expected_type": "LIVE_CANDIDATE",
    "delta1_to": ("resolver-wave-d-native-126-connection-placement-2026-08-03.md "
                  "(CONDITION, machinery only:"),
    "delta2_to": ("a SourceCriticalRankOnePSBSelectionCertificate placing v_PSB "
                  "in the rank-one orbit of V_PSB = (10bar,1,3)"),
    "delta2_from": "FROM:\na source-action-selected v_PSB",
}

PASSES: list[str] = []
FAILS: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        PASSES.append(name)
        print("[PASS] " + name)
    else:
        FAILS.append(name)
        print("[FAIL] " + name + ("  -- " + detail if detail else ""))


def read(rel: str) -> str:
    """Missing files yield '' so reference corruption fails checks through
    the normal needle path, never through a crash."""
    p = ROOT / rel
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def is_requirement(line: str, pattern: str) -> bool:
    """CP-1's mood discriminator: a provide-verb line is a REQUIREMENT, not
    supply, when the build verb sits under an 'until'-type scope."""
    return bool(re.search(pattern, line)) and "built" in line


def run_all(refs: dict) -> None:
    print("== A  base-revision row facts (the deltas' exact base) ==")
    try:
        ledger = json.loads(read(refs["ledger_base"]) or "{}")
    except json.JSONDecodeError:
        ledger = {}
    rows = {r.get("id"): r for r in ledger.get("rows", [])}
    check("A1 base revision v0.258 loads with 84 rows",
          len(rows) == 84, "got %d" % len(rows))
    sm5 = rows.get(refs["row_lt_sm5"], {})
    check("A2 LT-SM5 distance demands the total placement",
          "Build the physical P0/rho(Phi)/Y_K/Y_C/C-reality placement"
          in sm5.get("distance", ""))
    check("A3 LT-SM5 evidence at base cites exactly the varpi-radial gate "
          "(LIFECYCLE: reds when DELTA-1 is applied to a successor and "
          "backported here -- it must never be; the base is immutable)",
          sm5.get("evidence") == refs["lt_sm5_evidence"])
    check("A4 LT-SM5 verdict is SAME (DELTA-1 must not move it)",
          sm5.get("verdict") == "SAME")
    check("A5 LT-SM5 reason_kind is DERIVED_PARTIAL (DELTA-1 must not move it)",
          sm5.get("reason_kind") == "DERIVED_PARTIAL")
    a6 = rows.get(refs["row_ra_a6"], {})
    check("A6 RA-A6 revival_trigger at base is the bare watched object",
          a6.get("revival_trigger") == refs["ra_a6_trigger"])
    check("A7 RA-A6 evidence at base cites exactly the Higgs-direction gate",
          a6.get("evidence") == refs["ra_a6_evidence"])
    check("A8 RA-A6 source_row is CB-A:A6 (the lineage receipt's first hop)",
          a6.get("source_row") == "CB-A:A6")

    print("== B  wave-D facts (the CONDITION verdict's supply side) ==")
    wave_d = read(refs["wave_d"])
    check("B9 wave-D grade line keeps the placement open",
          refs["wave_d_grade_needle"] in wave_d)
    check("B10 wave-D section-9 boundary: no total full-20 kernel built",
          refs["wave_d_boundary"] in wave_d)
    check("B11 wave-D types the row's K density by name",
          refs["wave_d_k_density"] in wave_d)
    check("B12 wave-D types the row's C density by name",
          refs["wave_d_c_density"] in wave_d)
    check("B13 wave-D names the successor gate",
          refs["wave_d_next_gate"] in wave_d)
    check("B14 wave-E step 4 is the row's demanded placement work",
          refs["wave_d_step4"] in wave_d)
    check("B15 wave-D: bare spinor factor cannot close a mass row",
          refs["wave_d_sa_y1"] in wave_d)
    check("B16 live ledger: LT-SM5 evidence does NOT yet cite wave-D "
          "(LIFECYCLE: reds when the owner applies DELTA-1 -- then re-type "
          "the pair ALREADY_COMPOSED, refresh FX-1 C5, retire this check)",
          "resolver-wave-d" not in sm5.get("evidence", ""))

    print("== C  rb4 refusal facts (the leg that does NOT compose) ==")
    rb4 = read(refs["rb4"])
    until_lines = [ln for ln in rb4.splitlines() if refs["rb4_until"] in ln]
    check("C17 rb4 carries the 'until ... are built' line",
          len(until_lines) == 1, "got %d lines" % len(until_lines))
    line = until_lines[0] if until_lines else ""
    check("C18 that line names the Y_K/Y_C-reality map as the UNBUILT object",
          "Y_K/Y_C" in line and "-reality map are built" in line)
    check("C19 rb4 final boundary: compatible flag TYPED / UNSELECTED",
          any("COMPATIBLE COMPLEX--CARTAN FLAG" in ln and "TYPED / UNSELECTED" in ln
              for ln in rb4.splitlines()))
    check("C20 rb4 final boundary: SM determinant-one gate OPEN",
          any("SM DETERMINANT-ONE/EXTRA-U1 GATE" in ln and "OPEN" in ln
              for ln in rb4.splitlines()))
    check("C21 rb4 IS genuine moving-family machinery (wave-E step 2 only)",
          any("MOVING-u-CARTAN FAMILY" in ln and "CONSTRUCTED" in ln
              for ln in rb4.splitlines()))

    print("== D  cycle1 / lineage / near-collision facts ==")
    cycle1 = read(refs["cycle1"])
    check("D22 cycle1 formalizes the watched object",
          refs["cycle1_formalizes"] in cycle1)
    check("D23 cycle1 records it NOT selected",
          refs["cycle1_not_selected"] in cycle1)
    check("D24 cycle1 pins the representation (10bar,1,3)",
          refs["cycle1_rep"] in cycle1)
    check("D25 cycle1 names the selection certificate",
          refs["cycle1_cert"] in cycle1)
    check("D26 cycle1 records the target-fed no-go fence",
          refs["cycle1_nogo"] in cycle1)
    cb_a = read(refs["cb_a"])
    check("D27 cb-a lineage receipt: one line carries the rank-one "
          "(10bar,1,3) object AND the cycle1 citation",
          any(all(n in ln for n in refs["cb_a_lineage"])
              for ln in cb_a.splitlines()))
    check("D28 RA-A6's current evidence file contains ZERO v_PSB",
          "v_PSB" not in read(refs["higgs_gate"]))
    check("D29 homonym register carries NO v_PSB entry (LIFECYCLE: reds when "
          "the homonym channel registers the flagged near-collision -- then "
          "cite the entry in the gate note and retire this check)",
          "v_PSB" not in read(refs["homonym_register"]))
    check("D30 live ledger: RA-A6 evidence/trigger do NOT yet cite cycle1 "
          "(LIFECYCLE: reds when the owner applies DELTA-2 -- then re-type "
          "the pair ALREADY_COMPOSED, refresh FX-1 C5, retire this check)",
          "cycle1-source" not in a6.get("evidence", "")
          and "cycle1-source" not in a6.get("revival_trigger", ""))
    trace_hq = read(refs["trace_hq"])
    check("D31 trace-hq gate calls its v_PSB a rank-one vector in (4,1,2)",
          refs["trace_hq_412"] in trace_hq)
    check("D32 trace-hq probe computes it as kron(e4, fR)",
          refs["trace_hq_kron"] in read(refs["trace_hq_probe"]))
    check("D33 CONTRARY CONTROL: trace-hq gate contains ZERO '(10bar,1,3)' "
          "-- the two v_PSB objects are byte-disjoint",
          "(10bar,1,3)" not in trace_hq)
    check("D34 CONTRARY CONTROL: cycle1 contains ZERO '(4,1,2)'",
          "(4,1,2)" not in cycle1)

    print("== E  CI-X04 / BD-1 / SC-A facts ==")
    try:
        crosswalk = json.loads(read(refs["crosswalk"]) or "{}")
    except json.JSONDecodeError:
        crosswalk = {}
    cix04 = {}
    for row in crosswalk.get("cross_cutting_recovery_claims", []):
        if row.get("id") == "CI-X04":
            cix04 = row
    check("E35 CI-X04 curt_claim verbatim",
          cix04.get("curt_claim") == refs["cix04_claim"])
    check("E36 CI-X04 directive verbatim",
          cix04.get("directive") == refs["cix04_directive"])
    check("E37 CI-X04 source_grade is CURT_REPORT_OF_AUTHOR_CLAIM",
          cix04.get("source_grade") == "CURT_REPORT_OF_AUTHOR_CLAIM")
    check("E38 CI-X04 repo_grade is UNTESTED_PHENOMENOLOGY",
          cix04.get("repo_grade") == "UNTESTED_PHENOMENOLOGY")
    bd1 = read(refs["bd1"])
    check("E39 BD-1 fences the identification (section 5)",
          refs["bd1_fence"] in bd1)
    check("E40 BD-1 keeps CI-X04 at UNTESTED_PHENOMENOLOGY",
          "CI-X04 stays" in bd1 and "`UNTESTED_PHENOMENOLOGY`" in bd1)
    check("E41 BD-1: candidate mechanism exists for a DIFFERENT group",
          refs["bd1_different_group"] in bd1)
    check("E42 BD-1 executes directive items 1-3",
          "BD-1 executes items 1" in bd1 and "of that directive" in bd1)
    check("E43 BD-1 does not cite SC-A (frozen, predates it; LIFECYCLE: reds "
          "only if a correction block is added -- then refresh the gate note)",
          "sca-right-chain" not in bd1)
    sca = read(refs["sca"])
    check("E44 SC-A states R6, the best-supported reconstruction",
          refs["sca_r6"] in sca and "BEST-SUPPORTED RECONSTRUCTION" in sca)
    check("E45 SC-A: the arrows are NOT symmetry breakings",
          refs["sca_not_breaking"] in sca)
    check("E46 SC-A: they are structure-group reductions of one rank-10 bundle",
          refs["sca_reductions"] in sca)
    check("E47 SC-A caveat: the audio check is still owed",
          refs["sca_audio"] in sca)
    check("E48 SC-A proposed SC-GRP-50 and did not write it",
          "I did not write this" in sca and "SC-GRP-50" in sca)
    check("E49 claim register still carries NO SC-GRP-50 row (LIFECYCLE: "
          "reds when the register owner writes it -- then the reconstruction "
          "has a registered row; refresh the gate note, retire this check)",
          "SC-GRP-50" not in read(refs["claim_register"]))
    check("E50 SC-A does not cite BD-1 (uncited in both directions)",
          "bd1" not in sca and "BD-1" not in sca)
    check("E51 SC-A verifies the realification embedding generator-by-generator",
          refs["sca_embedding"] in sca)
    check("E52 SC-A: su(3,2) < so(6,4) at 24 <= 45",
          "24 <= 45" in sca)

    print("== F  composition-gate adjudication data ==")
    import needs_provides_composition_audit as gate
    check("F53 gate baseline stays 0 (never raised)",
          gate.UNADJUDICATED_BASELINE == 0)
    adj = gate.ADJUDICATED
    l1 = adj.get(refs["pair_l1"], ("", ""))
    check("F54 L1 typed LIVE_CANDIDATE with a dated CP-1 note",
          l1[0] == "LIVE_CANDIDATE" and "CP-1 2026-08-17" in l1[1])
    check("F55 L1 note carries DELTA-1 and the rb4 refusal",
          "DELTA-1" in l1[1] and "DOES NOT COMPOSE" in l1[1])
    l2 = adj.get(refs["pair_l2"], ("", ""))
    check("F56 L2 typed LIVE_CANDIDATE with the same dated adjudication",
          l2[0] == "LIVE_CANDIDATE" and "CP-1 2026-08-17" in l2[1])
    l3 = adj.get(refs["pair_l3"], ("", ""))
    check("F57 L3 typed LIVE_CANDIDATE with DELTA-2 named",
          l3[0] == "LIVE_CANDIDATE" and "CP-1 2026-08-17" in l3[1]
          and "DELTA-2" in l3[1])
    l4 = adj.get(refs["pair_l4"], ("", ""))
    check("F58 L4 type matches the recorded disposition and says no delta owed",
          l4[0] == refs["l4_expected_type"] and "CP-1 2026-08-17" in l4[1]
          and "NO DELTA IS OWED" in l4[1])
    check("F59 L4 note names the flip for the FX-1 owner's C6 refresh",
          "flip this entry to" in l4[1] and "ALREADY_COMPOSED" in l4[1])
    with redirect_stdout(io.StringIO()):
        pairs, wide, _ = gate.join()
    check("F60 all four pairs still derive from the live tree",
          all(p in pairs for p in (refs["pair_l1"], refs["pair_l2"],
                                   refs["pair_l3"], refs["pair_l4"])))
    check("F61 L1/L2 provider set is exactly {wave-D, rb4} (LIFECYCLE: a new "
          "provider means re-adjudication is owed)",
          pairs.get(refs["pair_l1"], {}).get("providers")
          == [refs["wave_d"], refs["rb4"]])
    check("F62 L3 provider set is exactly {cycle1}",
          pairs.get(refs["pair_l3"], {}).get("providers") == [refs["cycle1"]])

    print("== G  artifact conformance ==")
    art = read(refs["artifact"])
    check("G63 artifact exists and carries the routing notice with the "
          "method path",
          "GU-COMPARATOR-ROUTING" in art
          and "lab/methods/source-native-comparator-routing.md" in art)
    check("G64 classification line present and honest",
          re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`",
                    art) is not None)
    check("G65 target_claim is NONE-NOT-A-KILL (this pass kills nothing)",
          "target_claim: NONE-NOT-A-KILL" in art)
    check("G66 doc_type and created are declared honestly",
          "doc_type: stewardship_record" in art and "created: 2026-08-17" in art)
    check("G67 exactly three gu-typed-objects blocks",
          art.count("```gu-typed-objects") == 3,
          "got %d" % art.count("```gu-typed-objects"))
    check("G68 DELTA-1 TO-text present verbatim (machinery only)",
          refs["delta1_to"] in art)
    check("G69 DELTA-2 TO-text present verbatim (selection certificate, "
          "(10bar,1,3) orbit)",
          refs["delta2_to"] in art)
    check("G70 DELTA-2 FROM-text quotes the exact base trigger",
          refs["delta2_from"] in art)

    print("== H  typed-carrier gate compliance ==")
    import typed_carrier_declaration_audit as tc
    buf = io.StringIO()
    with redirect_stdout(buf):
        code, stats = tc.audit(paths=[str(ROOT / refs["artifact"])], baseline=0)
    check("H71 typed_carrier_declaration_audit exits 0 on this artifact",
          code == 0, buf.getvalue().strip().splitlines()[0] if buf.getvalue() else "")
    check("H72 scope 1, triggered 1, 3 blocks, 0 red, 0 exemptions, "
          "2 declared-ambiguous slots, no ALL-UNTYPED block",
          stats.get("scope") == 1 and stats.get("triggered") == 1
          and stats.get("blocks") == 3 and stats.get("red") == 0
          and stats.get("exemptions") == [] and stats.get("untyped_slots") == 2
          and stats.get("all_untyped") == [])
    blocks = tc.FENCE_RE.findall(art.split("---", 2)[-1])
    defect_lists = [tc.validate_block(b)[0] for b in blocks]
    check("H73 every block validates with ZERO defects",
          len(blocks) == 3 and all(d == [] for d in defect_lists),
          "; ".join(",".join(d) for d in defect_lists if d))
    fm, fm_raw = tc.frontmatter(art)
    reasons = tc.trigger_reasons(fm, fm_raw, art.split("---", 2)[-1])
    check("H74 the artifact actually TRIGGERS the gate (compliance is "
          "exercised, not vacuous)",
          len(reasons) >= 1, "reasons: %s" % reasons)

    print("== I  planted controls (must fire every run) ==")
    corrupted = tc.VALID_BLOCK.replace("so(1,3)_endo", "so(1,3)")
    defects, _, _ = tc.validate_block(corrupted)
    check("I75 validator liveness: a bare registered homonym IS caught",
          any(d.startswith("HOMONYM-BARE:so(1,3)") for d in defects),
          "defects: %s" % defects)
    check("I76 mood discriminator: rb4's 'until ... built' line IS a requirement",
          is_requirement(line, refs["mood_pattern"]))
    check("I77 mood discriminator: the SA-1 provider line is NOT a requirement",
          not is_requirement(refs["sa1_provider_line"], refs["mood_pattern"]))
    check("I78 false-quote refusal: the planted closed-placement quote does "
          "NOT verify against wave-D",
          refs["wave_d_false_quote"] not in wave_d)


def self_test() -> int:
    print("== SELFTEST: clean baseline first ==")
    PASSES.clear()
    FAILS.clear()
    buf = io.StringIO()
    with redirect_stdout(buf):
        run_all(REFS)
    n_pass, n_fail = len(PASSES), len(FAILS)
    if n_fail:
        sys.stdout.write(buf.getvalue())
        print("SELFTEST: clean baseline does NOT pass (%d/%d) -- "
              "mutations NOT run" % (n_pass, n_pass + n_fail))
        return 1
    print("clean baseline: %d/%d checks pass" % (n_pass, n_pass))

    mutations = [
        ("M1 corrupt row-id reference (LT-SM5 -> LT-SM99)",
         {"row_lt_sm5": "LT-SM99"}),
        ("M2 falsify the wave-D grade needle",
         {"wave_d_grade_needle":
          "total P0/Y placement, source selection, VEV, and mass are closed"}),
        ("M3 falsify the expected L4 typing (LIVE -> ALREADY_COMPOSED)",
         {"l4_expected_type": "ALREADY_COMPOSED"}),
        ("M4 corrupt the artifact path reference",
         {"artifact": ART.replace("2026-08-17", "2099-01-01")}),
        ("M5 corrupt the DELTA-2 anchor ((10bar,1,3) -> (10bar,9,9))",
         {"delta2_to":
          "a SourceCriticalRankOnePSBSelectionCertificate placing v_PSB "
          "in the rank-one orbit of V_PSB = (10bar,9,9)"}),
        ("M6 break the mood-discriminator pattern",
         {"mood_pattern": r"\bzzznever\b"}),
    ]
    caught = 0
    for name, patch in mutations:
        refs = copy.deepcopy(REFS)
        refs.update(patch)
        PASSES.clear()
        FAILS.clear()
        crashed = False
        out = io.StringIO()
        try:
            with redirect_stdout(out):
                run_all(refs)
        except Exception as exc:  # crash-catches are REJECTED
            crashed = True
            print("  %s: CRASH (%s) -- REJECTED, a catch must be a genuine "
                  "[FAIL] line" % (name, type(exc).__name__))
        fail_lines = [ln for ln in out.getvalue().splitlines()
                      if ln.startswith("[FAIL]")]
        if not crashed and FAILS and fail_lines:
            caught += 1
            print("  %s: CAUGHT via %d genuine [FAIL] line(s), e.g. %s"
                  % (name, len(fail_lines), fail_lines[0][:100]))
        elif not crashed:
            print("  %s: NOT CAUGHT -- the checks are inert against this "
                  "corruption" % name)
    print("SELFTEST: %d/%d mutations caught, clean baseline verified first"
          % (caught, len(mutations)))
    return 0 if caught == len(mutations) else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        sys.exit(self_test())
    run_all(REFS)
    total = len(PASSES) + len(FAILS)
    print("CP-1 probe: %d/%d checks pass" % (len(PASSES), total))
    if FAILS:
        print("FAILING: " + "; ".join(FAILS))
    sys.exit(1 if FAILS else 0)
