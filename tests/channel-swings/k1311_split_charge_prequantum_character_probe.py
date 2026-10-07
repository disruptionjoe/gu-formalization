#!/usr/bin/env python3
"""Independent hostile mutations for K1311."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1311-split-charge-prequantum-character.json").read_text())
def valid(x):
 c=x["construction"]; q=x["decision"]; return c["group_dimension"]==91 and c["split_rank"]==7 and c["orbit_dimension"]==84 and c["character_modulus_one"] and c["character_exists_for_every_real_mu"] and not c["charge_integrality_lattice_required"] and q["equivariant_prequantum_line_exists"] and not q["prequantization_selects_mu"] and not q["prequantization_discretizes_mu"] and not q["source_or_physical_status_moves"]
mut=[(("construction","group_dimension"),105),(("construction","split_rank"),6),(("construction","orbit_dimension"),98),(("construction","character_modulus_one"),False),(("construction","character_exists_for_every_real_mu"),False),(("construction","charge_integrality_lattice_required"),True),(("decision","prequantization_selects_mu"),True),(("decision","prequantization_discretizes_mu"),True),(("decision","source_or_physical_status_moves"),True)]
assert valid(D)
for i,(p,v) in enumerate(mut,1): x=copy.deepcopy(D); x[p[0]][p[1]]=v; assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(p)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
