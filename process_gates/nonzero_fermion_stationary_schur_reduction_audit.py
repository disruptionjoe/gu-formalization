#!/usr/bin/env python3
"""Durability audit for ledger v0.155 fermion stationary reduction."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0


def check(label, condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def load_unique(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.155.json")
result = load_unique(ROOT / "lab/process/selected-k77-nonzero-fermion-stationary-schur-reduction.json")
report = (ROOT / "explorations/conditional-build/selected-k77-nonzero-fermion-stationary-schur-reduction-2026-08-10.md").read_text()
ledger_md = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.155.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-nonzero-fermion-stationary-schur-reduction-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-nonzero-fermion-stationary-schur-reduction-source-return-2026-08-10.md").read_text()
contract = load_unique(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
contract_md = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
priorities = (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text()
process_readme = (ROOT / "lab/process/README.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()
sources_readme = (ROOT / "lab/sources/README.md").read_text()

check("ledger version is v0.155", ledger["schema_version"] == "0.155")
check("predecessor is v0.154", ledger["predecessor"].endswith("v0.154.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("frontier closes two", ledger["frontier_delta"]["conditions_closed"] == 2)
check("frontier opens one", ledger["frontier_delta"]["conditions_opened"] == 1)
check("three named conditions remain", ledger["frontier_delta"]["remaining_named_conditions"] == 3)

theorem = result["theorem"]
check("operator block is typed", theorem["operator"] == "D=[[A,B],[C,0]] on X+Y")
check("B maximal-rank hypothesis explicit", "rank(B)=dim(Y)" in theorem["hypotheses"])
check("C maximal-rank hypothesis explicit", "rank(C)=dim(Y)" in theorem["hypotheses"])
check("effective map names ker and coker", "coker(B)" in theorem["effective_map"] and "ker(C)" in theorem["effective_map"])
check("kernel isomorphism is explicit", theorem["kernel_isomorphism"].startswith("ker(D) is isomorphic"))
check("rank-loss controls cover 0 1 2", theorem["exact_fixture_nullities"] == [0, 1, 2])

k77 = result["k77_conditional_instantiation"]
check("desired one-form dimension 192", k77["desired_one_form_dimension"] == 192)
check("mirror one-form dimension 192", k77["mirror_one_form_dimension"] == 192)
check("zero-form dimension 128", k77["zero_form_dimension"] == 128)
check("conditional residual dimension 64", k77["maximal_rank_effective_dimension"] == 64)
check("actual B rank absent", k77["actual_B_rank_built"] is False)
check("actual C rank absent", k77["actual_C_rank_built"] is False)
check("actual effective map absent", k77["actual_effective_map_built"] is False)
check("principal kernel not reused", k77["principal_characteristic_kernel_is_not_imported_as_stationary_kernel"] is True)

mirror = result["mirror_test"]
check("tested reality is plain conjugation", mirror["tested_relation"].startswith("ordinary coefficient conjugation"))
check("mirror residual conjugate", mirror["effective_relation"].startswith("S_mirror=conjugate"))
check("conjugate ranks equal", mirror["equal_rank"] is True)
check("conjugate nullities equal", mirror["equal_stationary_nullity"] is True)
check("symmetry-breaking plant changes nullity", mirror["planted_independent_mirror_changes_nullity"] is True)
check("source reality remains absent", mirror["source_reality_built"] is False)

fork = result["southeast_fork"]
check("displayed candidate keeps E zero", fork["displayed_candidate"] == "E=0")
check("rival keeps E nonzero", fork["rival"].startswith("E!=0"))
check("rival uses different Schur object", fork["rival_effective_operator_when_E_invertible"] == "A-B E^-1 C")
check("rival changes nullity in exact fixture", fork["exact_fixture_changes_nullity"] is True)
check("southeast parents not merged", fork["parents_merged"] is False)

parents = result["parent_ablations"]
check("full U64 parent open", parents["source_full_U64_64"] == "OPEN_LOWER_ORDER_MAP")
check("moving Spin parent open", parents["moving_Spin"] == "OPEN_LOWER_ORDER_MAP")
check("two U32 halves parent open", parents["two_U32_32_halves"] == "OPEN_LOWER_ORDER_MAP")
check("principal fingerprint shared only", parents["principal_fingerprint_shared"] is True)
check("no parent selected", parents["parents_selected"] is False)

check("report contains ten specialist lenses", report.count("ACTUAL MATH,") == 10)
check("report distinguishes odd configuration and VEV", "not automatically a fermion condensate" in report)
check("report distinguishes 64 and count", "generation count `3`" in report)
check("report keeps U64 and two U32 distinct", "full `U(64,64)`" in report and "two-`U(32,32)`" in report)
check("report preserves maximal-rank fence", "maximal-" in report and "offdiagonal-rank horn" in report)
check("hostile review contains Layer-0", "**Layer-0 semantics:**" in review)
check("hostile review contains prior art", "**Prior art:**" in review)
check("hostile review contains analytic", "**Analytic/operator:**" in review)
check("hostile review contains symplectic", "**Symplectic/BV--BFV:**" in review)
check("hostile review contains dissent", "## Dissent" in review)
check("source confirms block grammar", "SOURCE-CONFIRMS" in source and "block arena" in source)
check("source silence explicit", "SOURCE-SILENT" in source and "maximal rank" in source)

check("contract points at v0.155", contract["standing_ledger"]["ref"].endswith("v0.155.json"))
check("contract has stationary directive", "nonzero_fermion_stationary_residual_directive" in contract["standing_ledger"])
check("contract prose points at v0.155", "conditional-physics-ledger-v0.155.json" in contract_md)
check("lanes points at v0.155", "conditional-physics-ledger-v0.155.json" in lanes)
check("next steps leads with v0.155", "STATIONARY SCHUR REDUCTION (ledger v0.155)" in next_steps)
check("research status leads with v0.155", "ledger v0.155" in status.split("ledger v0.154", 1)[0])
check("context pack leads with v0.155", "Current v0.155 nonzero-fermion stationary fence" in context)
check("priorities lead with v0.155", "Ledger v0.155 narrows" in priorities)
check("process README points at v0.155", "Current append-only progress surface: ledger v0.155" in process_readme)
check("human ledger records residual target", "conditionally reduce the stationary problem to `64 x 64`" in ledger_md)
check("tests inventory names probe", "selected_k77_nonzero_fermion_stationary_schur_reduction_probe.py" in tests_readme)
check("process inventory names audit", "nonzero_fermion_stationary_schur_reduction_audit.py" in gates_readme)
check("source inventory names receipt", "selected-k77-nonzero-fermion-stationary-schur-reduction-source-return-2026-08-10.md" in sources_readme)

accounting = result["accounting"]
check("no datum booked", accounting["datum_booked"] is False)
check("P1 P2 P3 unchanged", accounting["P1_P2_P3"] == "unchanged")
check("no residue movement", accounting["residue_change"] == "none")
check("no quotient movement", accounting["quotient_change"] == "none")
check("no canon movement", accounting["canon_verdict_change"] == "none")
check("no public posture movement", accounting["public_posture_change"] == "none")
check("next gate is actual source map", result["next_gate"] == "ACTUAL_DRAFT916_VARPI_EFFECTIVE_MAP_WITH_THREE_PARENT_ABLATIONS")

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.155"]
check("six v0.155 migrations", len(migrations) == 6)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
check("expected row set migrated", {m["row_id"] for m in migrations} == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
rows = {row["id"]: row for row in ledger["rows"]}
check("migration grades match live rows", all(rows[m["row_id"]]["mapping_grade"] == m["new"][2] for m in migrations))
check("all migrated evidence points at result", all("nonzero-fermion-stationary-schur-reduction" in rows[m["row_id"]]["evidence"] for m in migrations))

print(f"PASS {CHECKS}/{CHECKS}")
