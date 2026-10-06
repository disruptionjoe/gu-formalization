#!/usr/bin/env python3
"""K1231 hostile mutations."""
import copy, json
from pathlib import Path
from k1231_affine_local_channel_two_qubit_law import validate
D=json.loads((Path(__file__).parents[2]/"lab/process/k1231-affine-local-channel-two-qubit-law.json").read_text())
mutations=[
 ("transformation","correlation","T'=M T"),
 ("specialization","k1229_requires",["u=0","v=0"]),
 ("ownership","channel_calibration_determines_source_state",True),
 ("decision","delayed_choice_entanglement_swapping_consumed",True),
 ("claim_ceiling",None,"Empirical Bell validation"),
]
for a,b,v in mutations:
    x=copy.deepcopy(D)
    if b is None:x[a]=v
    else:x[a][b]=v
    try: validate(x)
    except AssertionError: continue
    raise AssertionError((a,b))
print("K1231 probe controls: 5/5")
