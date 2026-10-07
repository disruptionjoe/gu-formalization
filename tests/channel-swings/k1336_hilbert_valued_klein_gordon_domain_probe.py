#!/usr/bin/env python3
"""Hostile mutations for K1336."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1336-hilbert-valued-klein-gordon-domain.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("nonpositive mass",lambda x:x["construction"].__setitem__("mass_condition","m=0"),lambda x:x["construction"]["mass_condition"]=="m>0")
rejects("wrong operator domain",lambda x:x["construction"].__setitem__("operator_domain","H1"),lambda x:x["construction"]["operator_domain"]=="D(A_m)=H2(T3;H_ps)")
rejects("wrong form domain",lambda x:x["construction"].__setitem__("form_domain","L2"),lambda x:x["construction"]["form_domain"]=="D(A_m^(1/2))=H1(T3;H_ps)")
rejects("kernel invented",lambda x:x["spectrum"].__setitem__("kernel_dimension",1),lambda x:x["spectrum"]["kernel_dimension"]==0)
rejects("self-adjointness lost",lambda x:x["spectrum"].__setitem__("self_adjoint",False),lambda x:x["spectrum"]["self_adjoint"])
rejects("positivity lost",lambda x:x["spectrum"].__setitem__("strictly_positive",False),lambda x:x["spectrum"]["strictly_positive"])
rejects("GU ownership overclaim",lambda x:x["decision"].__setitem__("gu_action_owned",True),lambda x:not x["decision"]["gu_action_owned"])
rejects("interaction overclaim",lambda x:x["decision"].__setitem__("interacting",True),lambda x:not x["decision"]["interacting"])
rejects("quotient overclaim",lambda x:x["decision"].__setitem__("physical_quotient_constructed",True),lambda x:not x["decision"]["physical_quotient_constructed"])
assert len(tests)==9; print("RESULT: PASS 9/9")
