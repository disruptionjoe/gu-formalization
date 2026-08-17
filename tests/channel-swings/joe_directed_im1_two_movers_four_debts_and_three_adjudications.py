#!/usr/bin/env python3
"""IM-1 probe — the v0.259 integration mint, verified from committed state.

Sections:
  A  the immutable base (v0.258) — sha and the pre-mint facts the mint moved
  B  minted structure — counts, denominator, provenance
  C  the LT-SM1 split (both movers' first half)
  D  LT-SM7 T0 -> T2 at unchanged verdict/reason
  E  the LT-GR6b carrier row (four typed debts; the second mover)
  F  CP-1 DELTA-1/DELTA-2 applied verbatim (byte-compared against CP-1's blocks)
  G  ITC D1-D4 (new kind, INHERITANCE_BRIDGE, conjunct typing, annotation)
  H  LA-2 conditional cascade (grant named on every moved row)
  I  kill-gate invariance (the eight untyped kill-bearing rows are unchanged)
  J  the SOLDERED-AD fork-registry entry (typed as SA-1 decided)
  K  the v_PSB homonym entry (verified, not duplicated)
  L  artifact conformance (routing notice, classification, typed-carrier gate)
  M  planted controls, EVERY RUN: a LAUNDER control (re-typing minted AC-A1
     unconditional MUST fail the validator), a CONTRARY control (asserting the
     denominator stayed 82 MUST fail), and a corrupt-row control (LT-SM1b
     flipped to Route A's kind without the successor note MUST fail the
     adjudication-A consistency check)

--selftest: verifies the CLEAN BASELINE FIRST (mutations are refused on a
dirty baseline), then applies six mutations that corrupt MACHINERY/REFERENCES
(a sha expectation, a file path, a verbatim anchor, a registry needle, an
adjudication-record needle, a launder expectation) — never the checks. A catch
counts ONLY via >= 1 genuine [FAIL] line through the normal path; a crash is
REJECTED.
"""
from __future__ import annotations

import copy
import hashlib
import io
import json
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "process_gates"))

ART = ("lab/active-research/joe-directed/integration-mint/"
       "im1-two-movers-four-debts-and-three-adjudications-2026-08-17.md")

REFS = {
    "base": "lab/process/conditional-physics-ledger-v0.258.json",
    "base_sha256": "540b50e386073c0f43da4e8d5a8ffdaf06fd243c6612622d7daf187c0a725047",
    "minted": "lab/process/conditional-physics-ledger-v0.259.json",
    "cp1": "lab/active-research/joe-directed/composition/cp1-three-live-pairs-adjudicated-2026-08-17.md",
    "fork_registry": "lab/process/layer0-fork-registry.yaml",
    "homonym_register": "lab/process/homonym-register.yaml",
    "artifact": ART,
    "new_kind": "SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED",
    "delta2_anchor": "rank-one orbit of V_PSB = (10bar,1,3)",
    "fork_settled_side_needle": "soldered (bundle/ambient layer)",
    "fork_gate_needle": "selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md",
    "adjA_needle": "the successor kind behind that gate is REAL_PARAMETER",
    "expected_aca1_kind": "DERIVED_CONDITIONAL",
    "kill_eight": ["AC-B5", "AC-F3", "AC-F4", "LT-GR1b", "LT-GR5", "LT-GR7",
                   "RA-D2", "RA-F3"],
}

PASSES: list[str] = []
FAILS: list[str] = []
TRIGGER = re.compile(r"(?:\b|_)(kill(?:ed|s)?|no[-_ ]?go|falsifi\w+|dead|fatal)(?:\b|_)", re.I)
CLAIM_ID = re.compile(r"SC-[A-Z]+-\d+")


def check(name: str, ok: bool, detail: str = "") -> None:
    if ok:
        PASSES.append(name)
        print(f"[PASS] {name}")
    else:
        FAILS.append(name)
        print(f"[FAIL] {name}" + (f" -- {detail}" if detail else ""))


def read(rel: str) -> str:
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else ""


def untyped_kill_rows(ledger: dict) -> list[str]:
    out = []
    for r in ledger.get("rows", []):
        blob = json.dumps(r)
        if not TRIGGER.search(blob):
            continue
        if "NONE-NOT-A-KILL" in str(r.get("target_claim", "")):
            continue
        if CLAIM_ID.search(blob):
            continue
        out.append(r.get("id", "?"))
    return sorted(out)


def no_launder_violations(base_rows: dict, new_rows: dict) -> list[str]:
    """DERIVED_CONDITIONAL -> DERIVED is forbidden; a verdict move to SAME must
    land on a *_CONDITIONAL or *_PARTIAL kind, never bare DERIVED."""
    bad = []
    for rid, nr in new_rows.items():
        br = base_rows.get(rid)
        if br is None:
            continue
        if br["reason_kind"] == "DERIVED_CONDITIONAL" and nr["reason_kind"] == "DERIVED":
            bad.append(f"{rid}: DERIVED_CONDITIONAL -> DERIVED")
        if (br["verdict"] != "SAME" and nr["verdict"] == "SAME"
                and nr["reason_kind"] == "DERIVED"):
            bad.append(f"{rid}: advanced to SAME on unconditional DERIVED")
    return bad


def adjudication_a_consistent(row: dict) -> bool:
    """LT-SM1b must carry MISSING_CONSTRUCTION today AND record REAL_PARAMETER
    as the named successor kind; Route A's kind without the successor note is
    exactly the corruption this rejects."""
    return (row.get("reason_kind") == "MISSING_CONSTRUCTION"
            and "REAL_PARAMETER" in row.get("distance", ""))


def extract_delta_to_texts(cp1_text: str) -> list[str]:
    """The TO: payload lines of CP-1's two published delta blocks."""
    out = []
    for block in re.findall(r"^TO:\n(.+?)$", cp1_text, re.M):
        out.append(block.strip())
    return out


def run_all(refs: dict) -> None:
    print("== A  the immutable base ==")
    base_raw = (ROOT / refs["base"]).read_bytes() if (ROOT / refs["base"]).exists() else b""
    check("A1 base sha256 matches the recorded immutable base",
          hashlib.sha256(base_raw).hexdigest() == refs["base_sha256"])
    try:
        base = json.loads(base_raw or b"{}")
    except json.JSONDecodeError:
        base = {}
    brows = {r["id"]: r for r in base.get("rows", [])}
    check("A2 base has 84 row records and 82 canonical targets",
          len(brows) == 84
          and base.get("denominator", {}).get("canonical_target_count") == 82)
    check("A3 base LT-SM1 is one unsplit FINITE_CHOICE row",
          brows.get("LT-SM1", {}).get("reason_kind") == "FINITE_CHOICE"
          and "row_status" not in brows.get("LT-SM1", {}))
    check("A4 base AC-A1 is NEEDS / MISSING_CONSTRUCTION",
          brows.get("AC-A1", {}).get("verdict") == "NEEDS"
          and brows.get("AC-A1", {}).get("reason_kind") == "MISSING_CONSTRUCTION")
    check("A5 base LT-SM8 is MISSING_CONSTRUCTION (the kind ITC re-types)",
          brows.get("LT-SM8", {}).get("reason_kind") == "MISSING_CONSTRUCTION")
    check("A6 base verdicts are 32/19/26/5",
          base.get("progress", {}).get("verdict_counts")
          == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})

    print("== B  minted structure ==")
    try:
        led = json.loads(read(refs["minted"]) or "{}")
    except json.JSONDecodeError:
        led = {}
    rows = {r["id"]: r for r in led.get("rows", [])}
    active = [r for r in led.get("rows", []) if r.get("row_status") != "SUPERSEDED"]
    check("B7 minted ledger loads with 87 row records", len(rows) == 87,
          "got %d" % len(rows))
    check("B8 minted file records the base sha256 (per-mint provenance)",
          led.get("base_sha256") == refs["base_sha256"])
    check("B9 predecessor is v0.258 and status names v0.259",
          led.get("predecessor", "").endswith("v0.258.json")
          and led.get("status") == "CURRENT_APPEND_ONLY_LEDGER_V0_259")
    sup = sorted(r["id"] for r in led.get("rows", []) if r.get("row_status") == "SUPERSEDED")
    check("B10 exactly three superseded rows: AC-G1, LT-GR2, LT-SM1",
          sup == ["AC-G1", "LT-GR2", "LT-SM1"], str(sup))
    check("B11 84 active canonical targets = 87 - 3",
          len(active) == 84
          and led.get("denominator", {}).get("canonical_target_count") == 84
          and led.get("denominator", {}).get("row_record_count") == 87
          and led.get("denominator", {}).get("historical_superseded_count") == 3)
    vc: dict[str, int] = {}
    for r in active:
        vc[r["verdict"]] = vc.get(r["verdict"], 0) + 1
    check("B12 verdicts recount 33/19/27/5 and the progress block agrees",
          vc == {"SAME": 33, "DIFFERS": 19, "NEEDS": 27, "OVER_DETERMINED": 5}
          and led.get("progress", {}).get("verdict_counts") == vc)
    ax: dict[str, int] = {}
    for r in active:
        ax[r["axis"]] = ax.get(r["axis"], 0) + 1
    check("B13 axes recount 35/23/26 and the denominator agrees",
          ax == {"REPRESENTATION": 35, "LAGRANGIAN": 23, "ANOMALY_CONSISTENCY": 26}
          and led.get("denominator", {}).get("axes", {}).get("LAGRANGIAN") == 23)
    check("B14 source_row_count 86 and alias_count 8 unchanged (anchors never add CB rows)",
          led.get("denominator", {}).get("source_row_count") == 86
          and led.get("denominator", {}).get("alias_count") == 8)
    mig259 = [m for m in led.get("migrations", []) if m.get("to_version") == "0.259"]
    check("B15 fourteen migration entries carry to_version 0.259 with evidence",
          len(mig259) == 14 and all(m.get("evidence") for m in mig259),
          "got %d" % len(mig259))
    check("B16 migration_history equals the base's cumulative migrations (one-version lag)",
          led.get("migration_history") == base.get("migrations"))

    print("== C  the LT-SM1 split ==")
    sm1 = rows.get("LT-SM1", {})
    check("C17 LT-SM1 superseded with successors [LT-SM1a, LT-SM1b]",
          sm1.get("row_status") == "SUPERSEDED"
          and sm1.get("successors") == ["LT-SM1a", "LT-SM1b"])
    a = rows.get("LT-SM1a", {})
    b = rows.get("LT-SM1b", {})
    check("C18 LT-SM1a: NEEDS / FINITE_CHOICE, split_from, #zeta-f-horn anchor",
          a.get("verdict") == "NEEDS" and a.get("reason_kind") == "FINITE_CHOICE"
          and a.get("split_from") == "LT-SM1"
          and a.get("source_row") == "CB-B:SM-1#zeta-f-horn")
    check("C19 LT-SM1a records ONE_BIT as gated successor kind, not as its kind",
          "ONE_BIT" in a.get("distance", "")
          and "fork-completeness" in a.get("distance", ""))
    check("C20 LT-SM1a mapping grade carries the horn-cardinality certification",
          a.get("mapping_grade", "").startswith("FORM_EXACT_FORK_OPEN__HORN_CARDINALITY_2"))
    check("C21 LT-SM1b: NEEDS / MISSING_CONSTRUCTION with #relative-normalization anchor",
          b.get("verdict") == "NEEDS"
          and b.get("reason_kind") == "MISSING_CONSTRUCTION"
          and b.get("source_row") == "CB-B:SM-1#relative-normalization")
    check("C22 adjudication A recorded on the row: successor kind named",
          refs["adjA_needle"] in b.get("distance", ""))
    check("C23 LT-SM1b trigger demands the branching, not a bare number",
          "branching" in b.get("revival_trigger", ""))

    print("== D  LT-SM7 T0 -> T2 ==")
    sm7 = rows.get("LT-SM7", {})
    check("D24 grade moved to T2 sector-typed",
          sm7.get("mapping_grade", "").startswith("T2_SECTOR_TYPED__PI3_RANK3"))
    check("D25 verdict NEEDS unchanged", sm7.get("verdict") == "NEEDS")
    check("D26 reason REAL_PARAMETER unchanged",
          sm7.get("reason_kind") == "REAL_PARAMETER")
    check("D27 distance is the r-torus form with r in {2,3}",
          "r-torus" in sm7.get("distance", "") and "{2,3}" in sm7.get("distance", ""))

    print("== E  the LT-GR6b carrier row ==")
    g6 = rows.get("LT-GR6b", {})
    check("E28 exists on LAGRANGIAN with the #variational-duality anchor",
          g6.get("axis") == "LAGRANGIAN"
          and g6.get("source_row") == "CB-B:GR-6#variational-duality")
    check("E29 NEEDS / MISSING_CONSTRUCTION (head debt), one row only",
          g6.get("verdict") == "NEEDS"
          and g6.get("reason_kind") == "MISSING_CONSTRUCTION"
          and "LT-GR6c" not in rows and "LT-GR6d" not in rows)
    d = g6.get("distance", "")
    check("E30 all four debts separately typed in the distance",
          "(1) DECLARED" in d and "(2) CONDITIONAL TOPOLOGY" in d
          and "(3) EXTERNAL/OPEN" in d and "(4) MISSING CONSTRUCTION" in d)
    check("E31 the no-inheritance-without-bridge rule is carried in-row",
          "typed carrier/action/quotient bridge" in d)
    check("E32 the retired W-subscript impossibility clause is ABSENT",
          "provably does not exist" not in d)
    t = g6.get("revival_trigger", "")
    check("E33 trigger keeps the named-subscript fence and demands the action-derived construction",
          "named subscript" in t and "Gauss law" in t)
    check("E34 the defective positivity-on-quotient clause is NOT in the trigger",
          "positive on the physical quotient" not in t)
    check("E35 grade records module-vs-algebra and the Euclidean-witness caveat",
          "NOT_THE_MODULE" in g6.get("mapping_grade", "")
          and "EUCLIDEAN_WITNESS_ONLY" in g6.get("mapping_grade", ""))

    print("== F  CP-1 deltas, byte-compared ==")
    cp1 = read(refs["cp1"])
    tos = extract_delta_to_texts(cp1)
    check("F36 CP-1 publishes exactly two TO blocks", len(tos) == 2,
          "got %d" % len(tos))
    sm5 = rows.get("LT-SM5", {})
    check("F37 LT-SM5.evidence equals DELTA-1's TO text byte-for-byte",
          bool(tos) and sm5.get("evidence") == tos[0])
    check("F38 LT-SM5 verdict/reason/grade untouched (SAME / DERIVED_PARTIAL)",
          sm5.get("verdict") == "SAME" and sm5.get("reason_kind") == "DERIVED_PARTIAL"
          and sm5.get("mapping_grade") == brows.get("LT-SM5", {}).get("mapping_grade"))
    a6 = rows.get("RA-A6", {})
    check("F39 RA-A6.revival_trigger equals DELTA-2's TO text byte-for-byte",
          len(tos) == 2 and a6.get("revival_trigger") == tos[1])
    check("F40 DELTA-2 anchor present: certificate in the " + refs["delta2_anchor"],
          refs["delta2_anchor"] in a6.get("revival_trigger", ""))
    check("F41 RA-A6 evidence and distance untouched (trigger-field-only delta)",
          a6.get("evidence") == brows.get("RA-A6", {}).get("evidence")
          and a6.get("distance") == brows.get("RA-A6", {}).get("distance"))

    print("== G  ITC D1-D4 ==")
    tax = led.get("taxonomy", {}).get("verdict_kinds", {}).get("NEEDS", [])
    check("G42 taxonomy NEEDS family gained the new kind",
          refs["new_kind"] in tax)
    ext = led.get("taxonomy_extensions", [])
    check("G43 taxonomy extension block records strictly-more-indebting + non-discharge rule",
          any(e.get("new_kind") == refs["new_kind"]
              and e.get("strictly_more_indebting_than") == "MISSING_CONSTRUCTION"
              and "NOT discharged" in e.get("non_discharge_rule", "")
              for e in ext))
    sm8 = rows.get("LT-SM8", {})
    check("G44 LT-SM8 carries the new kind at unchanged NEEDS verdict",
          sm8.get("reason_kind") == refs["new_kind"] and sm8.get("verdict") == "NEEDS")
    nc = sm8.get("named_condition", {})
    check("G45 INHERITANCE_BRIDGE named with its not-established-for fence",
          nc.get("name") == "INHERITANCE_BRIDGE"
          and "interacting level" in nc.get("not_established_for", ""))
    check("G46 mandatory debt_note: NOT DISCHARGED, still rank 3, still counted",
          sm8.get("debt_note", "").startswith("NOT DISCHARGED")
          and "rank 3" in sm8.get("debt_note", ""))
    q3 = [q for q in led.get("next_work_queue", []) if q.get("rank") == 3]
    check("G47 LT-SM8 still sits in next_work_queue rank 3",
          bool(q3) and "LT-SM8" in q3[0].get("rows", []))
    d4 = rows.get("RA-D4", {})
    check("G48 RA-D4: trigger string unchanged; two conjuncts typed; pricing on conjunct 1 under the bridge",
          d4.get("revival_trigger") == brows.get("RA-D4", {}).get("revival_trigger")
          and len(d4.get("trigger_conjuncts", [])) == 2
          and d4.get("trigger_conjuncts", [{}])[0].get("bucket") == "SOURCE_DECLARED_OPEN"
          and "INHERITANCE_BRIDGE" in d4.get("trigger_conjuncts", [{}])[0].get("note", ""))
    check("G49 RA-G2 reachability recorded, PREDICTION retained; AC-F1 annotated, kind retained",
          rows.get("RA-G2", {}).get("revival_reachability") == "BLOCKED_BY_SOURCE_DECLARED_OPEN"
          and rows.get("RA-G2", {}).get("reason_kind") == "PREDICTION"
          and "SOURCE_DECLARED_OPEN" in rows.get("AC-F1", {}).get("annotation", "")
          and rows.get("AC-F1", {}).get("reason_kind") == "MISSING_CONSTRUCTION")

    print("== H  LA-2 conditional cascade ==")
    a1 = rows.get("AC-A1", {})
    check("H50 AC-A1 advanced to SAME on the expected kind",
          a1.get("verdict") == "SAME"
          and a1.get("reason_kind") == refs["expected_aca1_kind"])
    check("H51 the grant is NAMED on the row (GRANT-ACA1-C1)",
          "GRANT-ACA1-C1" in a1.get("evidence", ""))
    check("H52 successor distance names the owning fork, not this row",
          "C0-truncation-versus-C1 fork" in a1.get("distance", ""))
    check("H53 successor trigger fires on a forced chiral truncation",
          "chiral truncation" in a1.get("revival_trigger", ""))
    check("H54 AC-A2/AC-A3 declared conditional with the grant named",
          all(rows.get(rid, {}).get("reason_kind") == "DERIVED_CONDITIONAL"
              and "GRANT-ACA1-C1" in rows.get(rid, {}).get("evidence", "")
              for rid in ("AC-A2", "AC-A3")))

    print("== I  kill-gate invariance ==")
    minted_kill = untyped_kill_rows(led)
    check("I55 v0.259 untyped kill-bearing set is exactly the eight",
          minted_kill == sorted(refs["kill_eight"]), str(minted_kill))
    check("I56 ...and byte-identical to the base's set (no changed row gained kill language)",
          minted_kill == untyped_kill_rows(base))
    import kill_target_claim_audit as kg
    check("I57 kill gate LEDGER_BASELINE stands at 8 (neither raised nor lowered)",
          kg.LEDGER_BASELINE == 8)

    print("== J  the SOLDERED-AD fork entry ==")
    reg = read(refs["fork_registry"])
    check("J58 SOLDERED-AD entered with status settled",
          "- id: SOLDERED-AD" in reg
          and re.search(r"- id: SOLDERED-AD.*?status: settled", reg, re.S) is not None)
    check("J59 settled at the bundle layer on the soldered side",
          refs["fork_settled_side_needle"] in reg)
    check("J60 the inert horn is recorded AS TYPED (MD-1's verbatim horn text)",
          "an independent principal bundle and the ad index is an ordinary internal label" in reg)
    check("J61 the residual is routed to the K-lane's named gate with the exact condition",
          refs["fork_gate_needle"] in reg and "D_varpi chi_epsilon = 0" in reg)
    sa1_block = reg.split("- id: SOLDERED-AD", 1)[-1]
    check("J62 settled_by cites SA-1 and the K77 construction, both resolving",
          "sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md" in sa1_block
          and (ROOT / "explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md").exists())

    print("== K  the v_PSB homonym entry ==")
    hom = read(refs["homonym_register"])
    check("K63 register carries exactly ONE v_PSB token entry (no duplicate added)",
          hom.count("token: v_PSB") == 1)
    check("K64 both senses present with their representations",
          "(10bar,1,3)" in hom and "(4,1,2)" in hom)
    check("K65 the disambiguator names the numeric indistinguishability",
          "CANNOT" in hom and "stabilizer" in hom.split("token: v_PSB", 1)[-1][:2000])

    print("== L  artifact conformance ==")
    art = read(refs["artifact"])
    check("L66 artifact exists with the routing notice and method path",
          "GU-COMPARATOR-ROUTING" in art
          and "lab/methods/source-native-comparator-routing.md" in art)
    check("L67 classification line present and honest",
          re.search(r"Classification:\s*[*_]{0,2}`INTERNAL_STRUCTURAL_ONLY`", art) is not None)
    check("L68 target_claim is the audited not-a-kill hatch",
          "target_claim: NONE-NOT-A-KILL" in art)
    check("L69 doc_type and created honest in the gate-visible head",
          "doc_type: stewardship_record" in art[:400] and "created: 2026-08-17" in art[:400])
    check("L70 exactly three gu-typed-objects blocks",
          art.count("```gu-typed-objects") == 3,
          "got %d" % art.count("```gu-typed-objects"))
    import typed_carrier_declaration_audit as tc
    buf = io.StringIO()
    with redirect_stdout(buf):
        code, stats = tc.audit(paths=[str(ROOT / refs["artifact"])], baseline=0)
    blocks = tc.FENCE_RE.findall(art.split("---", 2)[-1])
    defects = [tc.validate_block(x)[0] for x in blocks]
    check("L71 typed-carrier gate exits 0 here; all three blocks defect-free",
          code == 0 and len(blocks) == 3 and all(dd == [] for dd in defects),
          "; ".join(",".join(dd) for dd in defects if dd))

    print("== M  planted controls (must fire every run) ==")
    # LAUNDER control: minted AC-A1 re-typed unconditional MUST fail validation.
    # (Graceful when the minted ledger is unreadable: the plant is then built
    # on the BASE row so the control still exercises the validator, and the
    # structural sections above carry the [FAIL] burden for the missing file.)
    laundered = {rid: dict(r) for rid, r in rows.items()}
    laundered["AC-A1"] = dict(laundered.get("AC-A1")
                              or brows.get("AC-A1", {"verdict": "NEEDS"}),
                              verdict="SAME", reason_kind="DERIVED")
    v = no_launder_violations(brows, laundered)
    check("M72 LAUNDER control fires: unconditional AC-A1 is rejected "
          "(and the real mint carries zero violations)",
          bool(v) and not no_launder_violations(brows, rows),
          "violations: %s" % v)
    # CONTRARY control: the pre-mint denominator MUST fail against v0.259.
    check("M73 CONTRARY control fires: 'the denominator stayed 82' is FALSE of the mint",
          led.get("denominator", {}).get("canonical_target_count") != 82)
    # Corrupt-row control: Route A's kind without the successor note MUST fail.
    corrupt = dict(rows.get("LT-SM1b", {}), reason_kind="REAL_PARAMETER",
                   distance="supply the relative normalization")
    check("M74 corrupt-row control fires: adjudication-A consistency rejects the "
          "unbridged Route-A flip (and accepts the minted row)",
          not adjudication_a_consistent(corrupt)
          and adjudication_a_consistent(rows.get("LT-SM1b", {})))


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
        print("SELFTEST: clean baseline does NOT pass (%d/%d) -- mutations NOT run"
              % (n_pass, n_pass + n_fail))
        return 1
    print("clean baseline: %d/%d checks pass" % (n_pass, n_pass))

    mutations = [
        ("M1 corrupt the immutable-base sha expectation",
         {"base_sha256": "0" * 64}),
        ("M2 corrupt the minted-ledger path reference",
         {"minted": "lab/process/conditional-physics-ledger-v9.999.json"}),
        ("M3 corrupt the DELTA-2 anchor ((10bar,1,3) -> (10bar,9,9))",
         {"delta2_anchor": "rank-one orbit of V_PSB = (10bar,9,9)"}),
        ("M4 corrupt the fork-registry settled-side needle",
         {"fork_settled_side_needle": "inert (bundle/ambient layer)"}),
        ("M5 corrupt the adjudication-A record needle",
         {"adjA_needle": "the successor kind behind that gate is INTEGER_DATUM"}),
        ("M6 LAUNDER-EXPECTATION flip: expect unconditional DERIVED on AC-A1",
         {"expected_aca1_kind": "DERIVED"}),
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
                  % (name, len(fail_lines), fail_lines[0][:110]))
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
    print("IM-1 probe: %d/%d checks pass" % (len(PASSES), total))
    if FAILS:
        print("FAILING: " + "; ".join(FAILS))
    sys.exit(1 if FAILS else 0)
