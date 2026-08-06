#!/usr/bin/env python3
"""Structural certificate for the trace-omega Higgs/chirality Compose wave."""

from pathlib import Path
from collections import Counter
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative
    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=hook)


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


source = (ROOT / "lab/sources/weinstein-levi-civita-contorsion-reinspection-2026-08-05.md").read_text()
admission = (ROOT / "explorations/conditional-build/trace-q-higgs-chirality-admission-test-2026-08-05.md").read_text()
weld = (ROOT / "explorations/conditional-build/k77-epsilon-gravitational-soldering-weld-2026-08-05.md").read_text()
report = (ROOT / "explorations/conditional-build/trace-omega-higgs-chirality-compose-reconciliation-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-trace-omega-higgs-chirality-compose-review.md").read_text()
registry = strict("lab/process/trace-omega-higgs-chirality-compose-reconciliation.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.19.json")
rows = {row["id"]: row for row in ledger["rows"] if row.get("row_status") != "SUPERSEDED"}

print("A. SOURCE AND REPOSITORY COMPOSITION")
check("source", "Weinstein confirms the gauge-rotated Levi-Civita displaced-connection arena",
      "gauge-rotated Levi-Civita" in source and "Omega1(Y" in source)
check("source", "source does not identify q with the Higgs cell",
      "does not fix" in source and "canonical trace vector" in source)
check("source", "decisive return is SOURCE-CORRECTS", registry["source_return"] == "SOURCE-CORRECTS")
check("repo", "q is canonical and no P1 line is added", "q=g/2" in admission and "not a new external datum" in admission)
check("repo", "bare gamma(q) failed only the finite standalone admission screen",
      "not admitted" in admission and "not a global theorem" in admission)
check("repo", "sigma_epsilon already has conditional rank ten", "rank ten" in weld and r"sigma_\epsilon" in weld)
check("repo", "the corrected chain is explicitly written", "T_\\omega" in report and "h_\\omega" in report)

print("\nB. LEDGER MIGRATION")
check("compose", "ledger advances append-only from v0.18 to v0.19",
      ledger["schema_version"] == "0.19" and ledger["predecessor"].endswith("v0.18.json"))
check("compose", "the four touched rows are exact",
      registry["touched_rows"] == ["RA-D2", "RA-G2", "RA-E3", "RA-E5"])
check("compose", "RA-D2 genuine falsification is preserved",
      rows["RA-D2"]["verdict"] == "OVER_DETERMINED"
      and rows["RA-D2"]["reason_kind"] == "GENUINE_FALSIFICATION")
check("compose", "RA-D2 now names the connection-derived candidate without passing revival",
      "sigma_epsilon" in rows["RA-D2"]["distance"] and "PHYSICAL_CHIRAL_QUOTIENT_OPEN" in rows["RA-D2"]["mapping_grade"])
check("compose", "RA-G2 now tests actual mirror-free positive cohomology",
      "positive physical cohomology" in rows["RA-G2"]["distance"] and "MIRROR_FREE_COHOMOLOGY_OPEN" in rows["RA-G2"]["mapping_grade"])
check("compose", "RA-E3 now owns varpi cell adapter and observed doublet descent",
      "varpi one-form cell" in rows["RA-E3"]["distance"] and "OBSERVED_SCALAR_DOUBLET_OPEN" in rows["RA-E3"]["mapping_grade"])
check("compose", "RA-E5 now owns observation-cell and mass-operator splitting",
      "survive observation descent" in rows["RA-E5"]["distance"] and "DOUBLET_TRIPLET_MASS_SELECTION_OPEN" in rows["RA-E5"]["mapping_grade"])
check("compose", "exactly four v0.19 migration edges exist",
      [m["row_id"] for m in ledger["migrations"] if m["to_version"] == "0.19"]
      == ["RA-D2", "RA-G2", "RA-E3", "RA-E5"])
check("compose", "no migration changes row meaning",
      all(not m["meaning_changed"] for m in ledger["migrations"] if m["to_version"] == "0.19"))
check("compose", "verdict counts and residue stay frozen",
      ledger["progress"]["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6}
      and ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["function_valued_at_least"] == 19
      and ledger["residue"]["open_discrete_forks"] == 9)
check("compose", "quotient count stays four", ledger["residue"]["quotients_ranked"] == 4)
check("compose", "full-moving cubic remains Build rank one",
      ledger["next_work_queue"][0]["rank"] == 1 and "complete moving third derivative" in ledger["next_work_queue"][0]["why"])
check("compose", "connection-derived h_omega gate is rank two",
      ledger["next_work_queue"][1]["rows"] == ["RA-D2", "RA-G2", "RA-E3", "RA-E5"])

print("\nC. COST, PHYSICAL BOUNDARY AND REVIEWS")
check("type", "the shared chain adds zero fields coefficients and selectors",
      registry["shared_chain"]["new_fields"] == registry["shared_chain"]["new_coefficients"] == registry["shared_chain"]["new_selectors"] == 0)
check("type", "P1 P2 P3 remain unused", registry["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("type", "global epsilon common carrier vacuum doublet and physical quotient remain open",
      all(registry["boundaries"][key] == "OPEN" for key in (
          "global_epsilon_ig", "common_k77_fermion_carrier", "action_selected_non_null_vacuum",
          "observed_scalar_doublet", "physical_bv_krein_quotient")))
check("type", "Curt and third-lane fences remain",
      registry["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and registry["third_lane"] == "NOT_PROMOTED")
check("type", "hostile review carries both charges and symplectic veto",
      "summary_outruns_artifact" in review and "rigor_defends_superseded_or_mistyped_object" in review and "symplectic_reduction_veto" in review)
check("type", "no canon verdict claim status or public posture changes",
      registry["claim_status_change"] == registry["canon_verdict_change"] == registry["public_posture_change"] == "NONE")

print("\nD. PLANTED FAILURES")
check("planted", "PLANT source assignment is not observed-doublet derivation", registry["boundaries"]["observed_scalar_doublet"] == "OPEN")
check("planted", "PLANT rank ten is not a doublet count", registry["shared_chain"]["adapter"] != "OBSERVED_HIGGS_DOUBLET")
check("planted", "PLANT no-new-datum does not mean action-selected vacuum", registry["boundaries"]["action_selected_non_null_vacuum"] == "OPEN")
check("planted", "PLANT bare q non-admission does not kill connection-derived h_omega", registry["boundaries"]["bare_gamma_q"].startswith("NOT_ADMITTED") and registry["boundaries"]["physical_bv_krein_quotient"] == "OPEN")
check("planted", "PLANT distance migration does not resolve RA-D2", rows["RA-D2"]["verdict"] == "OVER_DETERMINED")
check("planted", "PLANT a pointwise Clifford map is not a fifth quotient", ledger["residue"]["quotients_ranked"] == 4)
check("planted", "PLANT rank-two gate does not displace rank-one Build", ledger["next_work_queue"][0]["rank"] == 1)
check("planted", "PLANT migration consumes no external datum", set(registry["external_datum"].values()) == {"UNUSED"})

total = sum(COUNTS.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in COUNTS.items()), "=", total)
if FAILURES:
    print("FAILURES", FAILURES)
    raise SystemExit(1)
print(f"PASS: {total}/{total}")
print("SOURCE_RETURN=SOURCE-CORRECTS")
print("LEDGER=V0.19__FOUR_DISTANCE_MIGRATIONS__ZERO_VERDICT_OR_RESIDUE_MOVEMENT")
print("NEXT_BUILD=FULL_MOVING_SELECTED_CUBIC_D3I")
