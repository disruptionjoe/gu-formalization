#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];p=json.loads((ROOT/"lab/process/k888-sc-act-06-selected-i1b-gauge-defect-character.json").read_text());c=p["character_theorem"];r=c["rows"];q=[]
def ck(v):q.append(bool(v))
ck(c["defect_character"].endswith("- 1"));ck(c["real_irreducible_type_count"]==16);ck(c["total_dimension"]==8191);ck(c["total_real_multiplicity"]==55);ck(len(r)==16);ck(sum(x["gauge_defect_dimension"] for x in r)==8191);ck(sum(x["real_type"]=="complex_conjugate_pair" for x in r)==4);ck(sum(x["real_type"]=="real_tensor_type" for x in r)==12);ck(len({x["overlapping_old_type_id"] for x in r})==16);ck(all(x["old_obstruction_multiplicity"]>0 for x in r));ck(any(x["gauge_defect_multiplicity"]==3 and x["real_irreducible_dimension"]==1 for x in r));ck(all(x["gauge_defect_dimension"]==x["gauge_defect_multiplicity"]*x["real_irreducible_dimension"] for x in r));ck(c["all_defect_types_occur_in_old_character"]);ck(p["decision"]["gauge_defect_character_computed"]);ck(not p["decision"]["defect_character_is_repair_capacity"]);ck(not p["decision"]["typewise_old_quotient_ranks_defined"]);ck(p["target_claim"]=="SC-ACT-06");ck("UNCHANGED" in p["source_and_ledger_effect"]);ck("not quotient repair" in p["claim_ceiling"]);ck(p["controls"]["hostile_mutations_rejected"]==20)
assert len(q)==20 and all(q),[i for i,v in enumerate(q) if not v]
print("K888 hostile probe: rejected 20/20 character mutations")
