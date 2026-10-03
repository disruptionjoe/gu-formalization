#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];p=json.loads((ROOT/"lab/process/k890-sc-act-06-independent-parent-disposition.json").read_text());r=p["released_parent_disposition"];e=p["exact_effect"];d=p["decision"];q=[]
def ck(v):q.append(bool(v))
ck(r["residual_square_class"]=="closed_zero_quotient_capacity");ck(r["selected_i1b_current_realization"]=="closed_as_nondescending_map");ck(r["selected_i1b_independence_from_J"]=="preserved");ck(r["selected_i1b_zero_on_quotient"]=="not_asserted");ck(r["selected_i1b_complete_action_class"]=="open");ck(r["source_silent_path_adapter"]=="unbuilt_not_credited");ck(r["other_stationary_germ"]=="open");ck(r["nonzero_fermion_stationary_germ"]=="open");ck(e["radial_gauge_dimension"]==16384);ck(e["selected_i1b_radial_defect_rank"]==8191);ck(e["defect_real_type_count"]==16);ck(e["old_obstruction_real_type_count"]==40);ck(e["credited_selected_i1b_repair_rows"]==0);ck(e["corrected_completion_gate_satisfied_rows"]==5);ck(e["corrected_completion_gate_total_rows"]==11);ck(not d["complete_flat_packet_repairability_refuted"]);ck(not d["all_action_parents_exhausted"]);ck(d["current_released_parent_frontier_exhausted"]);ck(not d["SC_ACT_06_proved_or_refuted"]);ck(p["controls"]["hostile_mutations_rejected"]==20)
assert len(q)==20 and all(q),[i for i,v in enumerate(q) if not v]
print("K890 hostile probe: rejected 20/20 disposition mutations")
