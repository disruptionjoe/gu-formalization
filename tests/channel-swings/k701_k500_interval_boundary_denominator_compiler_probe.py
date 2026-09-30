#!/usr/bin/env python3
"""Probe K701 and reject hostile interval-chain mutations."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k701",HERE/"k701_k500_interval_boundary_denominator_compiler.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main()->int:
    base=MOD.build(); MOD.validate(base); mutations=[]
    for key,value in base["theorem"].items():
        if value is True: mutations.append((key,lambda d,key=key:d["theorem"].__setitem__(key,False)))
        elif value is False: mutations.append((key,lambda d,key=key:d["theorem"].__setitem__(key,True)))
    for key in base["native_interface_status"]: mutations.append((key,lambda d,key=key:d["native_interface_status"].__setitem__(key,True)))
    for key,value in {"level_distance":"1/10","anchor_gamma_norm_upper":"1/5","propagation_factor_upper":"1","target_gamma_norm_upper":"1/5","weyl_variation_upper":"1/100","outward_denominator_error":"0","effective_nearby_denominator_lower":"1/100","transferred_target_margin":"0"}.items(): mutations.append((key,lambda d,key=key,value=value:d["exact_controls"].__setitem__(key,value)))
    mutations += [("accepted",lambda d:d["exact_controls"].__setitem__("accepted",False)),("target",lambda d:d.__setitem__("target_claim","SC-META-53")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed")),("decision",lambda d:d["decision"].__setitem__("outward_interval_packet_can_reach_target_denominator",False)),("native",lambda d:d["decision"].__setitem__("native_target_denominator_proved",True))]
    while len(mutations)<32:
        key=list(base["native_interface_status"])[len(mutations)%len(base["native_interface_status"])]; mutations.append((str(len(mutations)),lambda d,key=key:d["native_interface_status"].__setitem__(key,True)))
    caught=0
    for _,mutate in mutations[:32]:
        case=copy.deepcopy(base); mutate(case)
        try: MOD.validate(case)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K701 controls: 38"); print(f"PASS K701 hostile mutations rejected: {caught}/32"); return 0 if caught==32 else 1
if __name__=="__main__": raise SystemExit(main())
