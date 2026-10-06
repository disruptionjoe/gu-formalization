#!/usr/bin/env python3
"""K1232 hostile mutations."""
import copy,json
from pathlib import Path
from k1232_same_channel_source_state_counterexamples import validate
D=json.loads((Path(__file__).parents[2]/"lab/process/k1232-same-channel-source-state-counterexamples.json").read_text())
cases=[
 ("decision","same_process_data_and_source_marginals_determine_holdout",True),
 ("decision","phi_plus_is_independent_premise",False),
 ("ownership","gu_native_effect","confirmation"),
]
for a,b,v in cases:
 x=copy.deepcopy(D);x[a][b]=v
 try:validate(x)
 except AssertionError:continue
 raise AssertionError((a,b))
x=copy.deepcopy(D);x["controls"]["Phi+"]["correlation"]="0"
try:validate(x)
except AssertionError:pass
else:raise AssertionError("correlation")
x=copy.deepcopy(D);x["controls"]["mixed"]["local_marginals"]=["1","0"]
try:validate(x)
except AssertionError:pass
else:raise AssertionError("marginal")
print("K1232 probe controls: 5/5")
