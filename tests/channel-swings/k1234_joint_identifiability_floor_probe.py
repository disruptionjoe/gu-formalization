#!/usr/bin/env python3
"""K1234 hostile mutations."""
import copy,json
from pathlib import Path
from k1234_joint_identifiability_floor import validate
D=json.loads((Path(__file__).parents[2]/"lab/process/k1234-joint-identifiability-floor.json").read_text())
mut=[("dimensions","joint_full_owner",26),("block_jacobian","process_rows_on_source_columns",1),("block_jacobian","selected_holdout_source_rank",2),("decision","eighteen_process_reads_identify_general_source",True),("decision","full_source_tomography_required_for_single_holdout",True),("decision","independent_three_scalar_source_certificate_suffices_for_single_holdout",False),("ownership","physical_frame_still_requires_independent_authentication",False)]
for a,b,v in mut:
 x=copy.deepcopy(D);x[a][b]=v
 try:validate(x)
 except AssertionError:continue
 raise AssertionError((a,b))
print("K1234 probe controls: 7/7")
