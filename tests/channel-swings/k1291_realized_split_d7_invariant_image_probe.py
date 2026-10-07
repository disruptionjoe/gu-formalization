#!/usr/bin/env python3
"""Independent hostile mutations for K1291."""
import copy, json
from pathlib import Path

D = json.loads((Path(__file__).resolve().parents[2] / "lab/process/k1291-realized-split-d7-invariant-image.json").read_text())

def valid(x):
    t = x["theorem"]
    q = x["decision"]
    return ("-I7^2" in t["characteristic_polynomial"] and
            "seven nonnegative real roots" in t["image_iff"] and
            t["complete_connected_weyl_orbit_invariant"] and
            not t["ambient_formal_base_equals_realized_image"] and
            q["realized_image_is_exact_semialgebraic_root_region"] and
            not q["arbitrary_formal_target_is_realized"] and
            not q["source_target_selected"] and
            not q["functional_phase_space_constructed"])

mutations = [
    (("theorem", "characteristic_polynomial"), "P_F(t)=t^7+I7^2"),
    (("theorem", "image_iff"), "P_F has seven complex roots"),
    (("theorem", "complete_connected_weyl_orbit_invariant"), False),
    (("theorem", "ambient_formal_base_equals_realized_image"), True),
    (("decision", "realized_image_is_exact_semialgebraic_root_region"), False),
    (("decision", "arbitrary_formal_target_is_realized"), True),
    (("decision", "source_target_selected"), True),
    (("decision", "functional_phase_space_constructed"), True),
]
assert valid(D)
for i, (path, value) in enumerate(mutations, 1):
    x = copy.deepcopy(D); x[path[0]][path[1]] = value
    assert not valid(x)
    print(f"REJECT {i:02d}: {'.'.join(path)}")
print("RESULT: PASS rejected 8/8 hostile mutations")
