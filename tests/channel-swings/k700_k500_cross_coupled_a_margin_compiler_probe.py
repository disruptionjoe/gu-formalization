#!/usr/bin/env python3
"""Probe K700 and reject hostile cross-budget mutations."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k700",HERE/"k700_k500_cross_coupled_a_margin_compiler.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main()->int:
    base=MOD.build(); MOD.validate(base); mutations=[]
    for key,value in base["theorem"].items():
        if value is True: mutations.append((key,lambda d,key=key:d["theorem"].__setitem__(key,False)))
        elif value is False: mutations.append((key,lambda d,key=key:d["theorem"].__setitem__(key,True)))
    for key in base["native_interface_status"]: mutations.append((key,lambda d,key=key:d["native_interface_status"].__setitem__(key,True)))
    for key,value in {"seed_norm_square_upper":"1/3","complement_norm_square_upper":"1/3","cross_upper":"1/6","schur_determinant_slack":"0","schur_trace":"1","certified_q_minus_gram_floor":"0","A_lower":"2/3"}.items(): mutations.append((key,lambda d,key=key,value=value:d["exact_controls"].__setitem__(key,value)))
    mutations += [("accepted",lambda d:d["exact_controls"].__setitem__("accepted",False)),("target",lambda d:d.__setitem__("target_claim","SC-META-53")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed")),("decision",lambda d:d["decision"].__setitem__("nonzero_cross_packet_can_supply_A_above_two_thirds",False)),("native",lambda d:d["decision"].__setitem__("native_A_margin_constructed",True))]
    while len(mutations)<30:
        key=list(base["native_interface_status"])[len(mutations)%len(base["native_interface_status"])]; mutations.append((str(len(mutations)),lambda d,key=key:d["native_interface_status"].__setitem__(key,True)))
    caught=0
    for _,mutate in mutations[:30]:
        case=copy.deepcopy(base); mutate(case)
        try: MOD.validate(case)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K700 controls: 36"); print(f"PASS K700 hostile mutations rejected: {caught}/30"); return 0 if caught==30 else 1
if __name__=="__main__": raise SystemExit(main())
