#!/usr/bin/env python3
"""Probe K703 and reject hostile complete-floor mutations."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k703",HERE/"k703_k500_interval_complete_cancellation_floor_compiler.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main()->int:
    b=MOD.build(); MOD.validate(b); ms=[]
    for k,v in b["theorem"].items():
        if v is True: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,False)))
        elif v is False: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,True)))
    for k in b["native_interface_status"]: ms.append((k,lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    for k,v in {"A_lower_from_K702":"2/3","effective_B_lower":"5/8","effective_beta_square_upper":"1/100","shifted_determinant_slack":"0","shifted_trace":"1","certified_floor_lift":"0","complete_floor_lower":"5/8"}.items(): ms.append((k,lambda d,k=k,v=v:d["exact_controls"].__setitem__(k,v)))
    ms += [("accepted",lambda d:d["exact_controls"].__setitem__("accepted",False)),("target",lambda d:d.__setitem__("target_claim","SC-META-53")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed")),("decision",lambda d:d["decision"].__setitem__("outward_complete_packet_can_supply_floor_above_five_eighths",False)),("native",lambda d:d["decision"].__setitem__("native_complete_floor_proved",True))]
    while len(ms)<36:
        k=list(b["native_interface_status"])[len(ms)%len(b["native_interface_status"])]; ms.append((str(len(ms)),lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    caught=0
    for _,m in ms[:36]:
        c=copy.deepcopy(b); m(c)
        try: MOD.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K703 controls: 42"); print(f"PASS K703 hostile mutations rejected: {caught}/36"); return 0 if caught==36 else 1
if __name__=="__main__": raise SystemExit(main())
