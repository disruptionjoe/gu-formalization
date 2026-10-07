#!/usr/bin/env python3
"""Independent hostile mutations for K1292."""
import copy, json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1292-normalized-shape-simplex-image.json").read_text())

def valid(x):
    t=x["theorem"]; q=x["decision"]
    return (t["orientation_relation"] == "y7^2=e7(q)=product_i q_i" and t["compact"] and
            t["upper_equality"].startswith("q1=...=q7=1/7") and
            t["opposite_sign_fixed_even_fibers_are_distinct_orbits"] and
            not t["opposite_sign_regular_orbits_are_separate_connected_components"] and
            not q["ambient_R6_shape_chart_equals_realized_shape_image"] and
            q["realized_shape_image_is_compact"] and not q["p_sign_is_a_global_component_label"] and
            not q["source_orientation_selected"])

mutations=[
    (("theorem","orientation_relation"),"y7=e7(q)"),
    (("theorem","compact"),False),
    (("theorem","upper_equality"),"all q_i distinct"),
    (("theorem","opposite_sign_fixed_even_fibers_are_distinct_orbits"),False),
    (("theorem","opposite_sign_regular_orbits_are_separate_connected_components"),True),
    (("decision","ambient_R6_shape_chart_equals_realized_shape_image"),True),
    (("decision","realized_shape_image_is_compact"),False),
    (("decision","p_sign_is_a_global_component_label"),True),
    (("decision","source_orientation_selected"),True),
]
assert valid(D)
for i,(path,value) in enumerate(mutations,1):
    x=copy.deepcopy(D); x[path[0]][path[1]]=value
    assert not valid(x); print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 9/9 hostile mutations")
