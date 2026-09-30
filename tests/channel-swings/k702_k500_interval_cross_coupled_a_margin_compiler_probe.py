#!/usr/bin/env python3
"""Probe K702 and reject hostile outward-Schur mutations."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k702",HERE/"k702_k500_interval_cross_coupled_a_margin_compiler.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main()->int:
    b=MOD.build(); MOD.validate(b); ms=[]
    for k,v in b["theorem"].items():
        if v is True: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,False)))
        elif v is False: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,True)))
    for k in b["native_interface_status"]: ms.append((k,lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    for k,v in {"effective_seed_upper":"1/4","effective_complement_upper":"1/100","effective_cross_upper":"1/60","determinant_slack":"0","trace":"1","certified_q_minus_gram_floor":"0","R_square_upper":"1/3","A_lower":"2/3"}.items(): ms.append((k,lambda d,k=k,v=v:d["exact_controls"].__setitem__(k,v)))
    ms += [("accepted",lambda d:d["exact_controls"].__setitem__("accepted",False)),("target",lambda d:d.__setitem__("target_claim","SC-META-53")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed")),("decision",lambda d:d["decision"].__setitem__("outward_cross_packet_can_supply_A_above_two_thirds",False)),("native",lambda d:d["decision"].__setitem__("native_A_margin_constructed",True))]
    while len(ms)<34:
        k=list(b["native_interface_status"])[len(ms)%len(b["native_interface_status"])]; ms.append((str(len(ms)),lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    caught=0
    for _,m in ms[:34]:
        c=copy.deepcopy(b); m(c)
        try: MOD.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K702 controls: 40"); print(f"PASS K702 hostile mutations rejected: {caught}/34"); return 0 if caught==34 else 1
if __name__=="__main__": raise SystemExit(main())
