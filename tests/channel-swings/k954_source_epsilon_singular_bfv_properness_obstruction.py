#!/usr/bin/env python3
"""K954: the one-scalar Koszul complex resolves the wrong observable algebra."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k954-source-epsilon-singular-bfv-properness-obstruction.json"
PATHS={"k951":ROOT/"lab/process/k951-source-epsilon-singular-scalar-isolation.json","k952":ROOT/"lab/process/k952-source-epsilon-principal-ideal-fat-point.json","k953":ROOT/"lab/process/k953-source-epsilon-seven-generator-lower-bound.json"}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():return json.loads(OUTPUT.read_text())
def validate(d):
 t,q=d["theorem"],d["decision"]
 checks=[d["result_id"]=="K954-SOURCE-EPSILON-SINGULAR-BFV-PROPERNESS-OBSTRUCTION",set(d["pinned_inputs"])==set(PATHS),all(d["pinned_inputs"][k]["sha256"]==digest(p) for k,p in PATHS.items()),t["constraint_conormal_rank_at_target"]==0,t["desired_point_conormal_rank"]==7,t["hamiltonian_constraint_vector_field_rank_at_target"]==0,t["koszul_H0"]=="A/(F)",not t["koszul_H0_equals_point_algebra"],t["koszul_H1_vanishes_for_nonzero_divisor"],t["koszul_complex_resolves_principal_hypersurface_ideal"],t["new_degree_one_constraint_generators_needed"]==7,not t["point_selection_properness_passes"],not t["regular_constraint_BFV_transfer_applies"],not q["exact_koszul_resolution_of_wrong_ideal_counts_as_point_selector"],not q["higher_stage_ghosts_without_new_degree_one_constraints_repair_H0"],not q["singular_one_constraint_supplies_proper_point_BFV"],not q["SC_ACT_06_proved_or_refuted"],d["controls"]["controls_passed"]==24,d["controls"]["hostile_mutations_rejected"]==10,d["gu_typed_objects"]["target"].startswith("BFV-TYPE="),"LEDGER_UNCHANGED" in d["source_and_ledger_effect"],"finite formal Koszul/BFV" in d["claim_ceiling"],"delta b=F" in d["gu_typed_objects"]["differential"],"Compose the singular-scalar failure" in q["next_exact_input"]]
 assert len(checks)==24 and all(checks),[i for i,x in enumerate(checks) if not x]
def main():
 p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args();d=build();validate(d)
 if not a.check:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())
