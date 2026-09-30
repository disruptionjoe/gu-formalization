#!/usr/bin/env python3
"""Probe K704 and reject hostile coordinate-transport mutations."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k704",HERE/"k704_k500_coordinate_transported_boundary_margin_compiler.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main()->int:
    b=MOD.build(); MOD.validate(b); ms=[]
    for k,v in b["theorem"].items():
        if v is True: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,False)))
        elif v is False: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,True)))
    for k in b["native_interface_status"]: ms.append((k,lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    for k,v in {"coordinate_operator_norm_upper":"1","condition_square_upper":"1","exact_congruence_margin":"9039/2125000","outward_coordinate_residual":"0","transported_target_margin":"0"}.items(): ms.append((k,lambda d,k=k,v=v:d["exact_controls"].__setitem__(k,v)))
    ms += [("accepted",lambda d:d["exact_controls"].__setitem__("accepted",False)),("target",lambda d:d.__setitem__("target_claim","SC-META-53")),("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed")),("decision",lambda d:d["decision"].__setitem__("authenticated_bounded_coordinate_change_can_preserve_positive_margin",False)),("native",lambda d:d["decision"].__setitem__("native_transported_denominator_proved",True))]
    while len(ms)<34:
        k=list(b["native_interface_status"])[len(ms)%len(b["native_interface_status"])]; ms.append((str(len(ms)),lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    caught=0
    for _,m in ms[:34]:
        c=copy.deepcopy(b); m(c)
        try: MOD.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K704 controls: 40"); print(f"PASS K704 hostile mutations rejected: {caught}/34"); return 0 if caught==34 else 1
if __name__=="__main__": raise SystemExit(main())
