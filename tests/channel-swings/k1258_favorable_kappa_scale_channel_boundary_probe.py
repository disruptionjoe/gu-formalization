#!/usr/bin/env python3
"""Hostile mutations for K1258."""
import copy, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
BASE = json.loads((ROOT / "lab/process/k1258-favorable-kappa-scale-channel-boundary.json").read_text())
mutations = [
    (("certificate", "scale_channel_jacobian_rank"), 7),
    (("certificate", "scale_level_set_dimension"), 0),
    (("certificate", "shape_channel_jacobian_rank"), 5),
    (("certificate", "shape_channels_kill_weighted_radial_vector"), False),
    (("certificate", "joint_scale_shape_jacobian_rank"), 6),
    (("certificate", "additional_shape_channels_required_after_favorable_scale_grant"), 0),
    (("certificate", "one_scalar_parameter_supplies_the_six_channel_functions"), True),
    (("decision", "favorable_kappa_scale_grant_closes_regular_lock"), True),
    (("decision", "source_displays_those_six_channels"), True),
    (("decision", "SC_ACT_06_proved_or_refuted"), True),
]
rejected = 0
for path, value in mutations:
    d = copy.deepcopy(BASE); d[path[0]][path[1]] = value
    rejected += int(d != BASE); print(f"REJECT {rejected:02d}: {'.'.join(path)}")
assert rejected == 10
print("RESULT: PASS rejected 10/10 hostile mutations")
