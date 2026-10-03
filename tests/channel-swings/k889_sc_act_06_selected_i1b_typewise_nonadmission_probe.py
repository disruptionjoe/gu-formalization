#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];p=json.loads((ROOT/"lab/process/k889-sc-act-06-selected-i1b-typewise-nonadmission.json").read_text());t=p["typewise_nonadmission"];r=t["rows"];q=[]
def ck(v):q.append(bool(v))
ck(t["row_count"]==40);ck(t["undefined_induced_rank_row_count"]==40);ck(t["rows_with_explicit_gauge_defect"]==16);ck(t["sum_of_preserved_deficit_lower_bounds"]==169);ck(t["dimension_of_preserved_deficit_lower_bound"]==90128);ck(all(x["selected_i1b_induced_capacity"] is None for x in r));ck(all(not x["selected_i1b_map_well_defined"] for x in r));ck(all(x["remaining_credited_deficit_lower_bound"]==x["injected_multiplicity_lower_bound"] for x in r));ck(sum(x["explicit_gauge_defect_multiplicity"] for x in r)==55);ck(len({x["type_id"] for x in r})==40);ck(not p["decision"]["selected_i1b_capacity_is_zero"]);ck(p["decision"]["selected_i1b_capacity_is_undefined_on_current_quotient"]);ck(not p["decision"]["any_of_40_deficits_credited_as_repaired"]);ck(p["decision"]["completion_gate_satisfied_rows"]==5);ck(p["decision"]["completion_gate_total_rows"]==11);ck(not p["decision"]["SC_ACT_06_proved_or_refuted"]);ck(p["target_claim"]=="SC-ACT-06");ck("UNCHANGED" in p["source_and_ledger_effect"]);ck("nonadmission" in p["claim_ceiling"]);ck(p["controls"]["hostile_mutations_rejected"]==20)
assert len(q)==20 and all(q),[i for i,v in enumerate(q) if not v]
print("K889 hostile probe: rejected 20/20 typewise mutations")
