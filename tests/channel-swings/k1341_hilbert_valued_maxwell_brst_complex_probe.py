#!/usr/bin/env python3
"""Hostile mutations for K1341."""
import copy,json
from pathlib import Path
D=json.loads((Path(__file__).resolve().parents[2]/"lab/process/k1341-hilbert-valued-maxwell-brst-complex.json").read_text()); tests=[]
def rejects(label,mut,pred):
 x=copy.deepcopy(D); mut(x); assert not pred(x),label; tests.append(label); print(f"PASS {len(tests):02d}: rejects {label}")
rejects("trivial sequence",lambda x:x["detour_complex"].__setitem__("sequence","Omega1 only"),lambda x:x["detour_complex"]["sequence"].startswith("Omega0"))
rejects("lost gauge identity",lambda x:x["detour_complex"].__setitem__("identities",[]),lambda x:"delta_d_d=0" in x["detour_complex"]["identities"])
rejects("lost Noether identity",lambda x:x["detour_complex"]["identities"].remove("delta_delta_d=0"),lambda x:"delta_delta_d=0" in x["detour_complex"]["identities"])
rejects("wrong transverse rank",lambda x:x["mode_control"].__setitem__("projector_rank",3),lambda x:x["mode_control"]["projector_rank"]==2)
rejects("zero mode restored",lambda x:x["mode_control"].__setitem__("zero_mode_disposition","included"),lambda x:x["mode_control"]["zero_mode_disposition"].startswith("excluded"))
rejects("complex removed",lambda x:x["decision"].__setitem__("nontrivial_gauge_detour_complex_constructed",False),lambda x:x["decision"]["nontrivial_gauge_detour_complex_constructed"])
rejects("source overclaim",lambda x:x["decision"].__setitem__("gu_action_owned",True),lambda x:not x["decision"]["gu_action_owned"])
rejects("interaction overclaim",lambda x:x["decision"].__setitem__("interacting",True),lambda x:not x["decision"]["interacting"])
rejects("GU BV-BFV overclaim",lambda x:x["decision"].__setitem__("gu_bv_bfv_complex_constructed",True),lambda x:not x["decision"]["gu_bv_bfv_complex_constructed"])
rejects("equivariance lost",lambda x:x["decision"].__setitem__("internal_principal_series_equivariance",False),lambda x:x["decision"]["internal_principal_series_equivariance"])
assert len(tests)==10; print("RESULT: PASS 10/10")
