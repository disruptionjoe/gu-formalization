#!/usr/bin/env python3
"""K1233 hostile mutations."""
import copy,json
from pathlib import Path
from k1233_minimal_holdout_source_certificate import validate
D=json.loads((Path(__file__).parents[2]/"lab/process/k1233-minimal-holdout-source-certificate.json").read_text())
mut=[("minimum_independent_statistics",None,2),("certificate",None,["A","B"]),("decision","normalization_alone_reduces_four_probabilities_to_three",False),("decision","process_calibration_supplies_certificate",True),("claim_ceiling",None,"Empirical source validation")]
for a,b,v in mut:
 x=copy.deepcopy(D)
 if b is None:x[a]=v
 else:x[a][b]=v
 try:validate(x)
 except AssertionError:continue
 raise AssertionError((a,b))
print("K1233 probe controls: 5/5")
