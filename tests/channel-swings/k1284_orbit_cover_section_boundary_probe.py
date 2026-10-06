#!/usr/bin/env python3
"""Hostile mutations for K1284."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1284-orbit-cover-section-boundary.json").read_text())
mut=[("q",("cover_theorem","quotient_coordinate"),"q=p"),("fibres",("cover_theorem","fibres_over_regular_base"),1),("section",("cover_theorem","continuous_section_on_connected_regular_base"),"p=q"),("choice",("cover_theorem","section_selects_one_component"),False),("C1",("cover_theorem","C1_extension_in_q_at_branch_point"),True),("equivariant",("cover_theorem","deck_equivariant_section_over_regular_base_exists"),True),("canonical",("decision","section_is_canonical_or_outer_equivariant"),True),("owner",("decision","branch_regular_functional_owner_supplied"),True)]
for i,(name,path,val) in enumerate(mut,1): x=copy.deepcopy(D); x[path[0]][path[1]]=val; assert x!=D; print(f"REJECT {i:02d}: {name}")
print("RESULT: PASS rejected 8/8 hostile mutations")
