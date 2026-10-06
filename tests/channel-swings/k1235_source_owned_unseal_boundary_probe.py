#!/usr/bin/env python3
"""K1235 hostile mutations."""
import copy,json
from pathlib import Path
from k1235_source_owned_unseal_boundary import validate
D=json.loads((Path(__file__).parents[2]/"lab/process/k1235-source-owned-unseal-boundary.json").read_text())
mut=[("decision","k1229_formula_remains_valid_under_declared_phi_plus_premise",False),("decision","channel_calibration_alone_authorizes_unseal",True),("decision","holdout_may_fit_its_own_source_certificate",True),("decision","delayed_choice_entanglement_swapping_consumed",True),("ownership","gu_native_effect","prediction"),("protected_status","SC-META-53","RESOLVED"),("claim_ceiling",None,"GU confirmation")]
for a,b,v in mut:
 x=copy.deepcopy(D)
 if b is None:x[a]=v
 else:x[a][b]=v
 try:validate(x)
 except AssertionError:continue
 raise AssertionError((a,b))
x=copy.deepcopy(D);x["required_before_unseal"].remove("independent source-state certificate for A, B and C")
try:validate(x)
except AssertionError:pass
else:raise AssertionError("source certificate")
print("K1235 probe controls: 8/8")
