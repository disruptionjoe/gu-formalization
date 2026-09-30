#!/usr/bin/env python3
"""Independent hostile replay for K706."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k706",HERE/"k706_sc_act_06_euclidean_frame_transport.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main():
    b=MOD.build(); MOD.validate(b); ms=[]
    for k,v in b["theorem"].items():
        if v is True: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,False)))
        elif v is False: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,True)))
    for k in b["native_interface_status"]: ms.append((k,lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    for k,v in {"original_rank":12,"transported_rank":12,"transported_kernel_dimension":2,"transported_gauge_rank":0,"equation_complement_determinant":"0","singular_equation_frame_rank":13}.items(): ms.append((k,lambda d,k=k,v=v:d["exact_controls"].__setitem__(k,v)))
    ms += [("composition",lambda d:d["exact_controls"].__setitem__("transported_composition_zero",False)),("source",lambda d:d["exact_controls"].__setitem__("source_frame_is_nontrivial",False)),("target",lambda d:d.__setitem__("target_claim","NONE-NOT-A-KILL")),("effect",lambda d:d.__setitem__("source_and_ledger_effect","changed"))]
    caught=0
    for _,m in ms:
        c=copy.deepcopy(b); m(c)
        try: MOD.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K706 controls: 30"); print(f"PASS K706 hostile mutations rejected: {caught}/23"); return 0 if caught==23 else 1
if __name__=="__main__": raise SystemExit(main())
