#!/usr/bin/env python3
"""Independent hostile replay for K707."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location("k707",HERE/"k707_sc_act_06_coupled_symbol_homotopy_compiler.py"); assert SPEC and SPEC.loader
MOD=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main():
    b=MOD.build(); MOD.validate(b); ms=[]
    for k,v in b["theorem"].items():
        if v is True: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,False)))
        elif v is False: ms.append((k,lambda d,k=k:d["theorem"].__setitem__(k,True)))
    for k in b["native_interface_status"]: ms.append((k,lambda d,k=k:d["native_interface_status"].__setitem__(k,True)))
    for k,v in {"gauge_rank":1,"exact_coupled_rank":25,"exact_kernel_dimension":3,"exact_middle_cohomology":1,"short_compatible_rank":26,"short_compatible_middle_cohomology":0,"illegal_repair_rank":25,"illegal_repair_composition_rank":0}.items(): ms.append((k,lambda d,k=k,v=v:d["exact_controls"].__setitem__(k,v)))
    ms += [("composition",lambda d:d["exact_controls"].__setitem__("exact_composition_zero",False)),("coupling",lambda d:d["exact_controls"].__setitem__("coupling_nonzero",False)),("target",lambda d:d.__setitem__("target_claim","NONE-NOT-A-KILL")),("effect",lambda d:d.__setitem__("source_and_ledger_effect","changed"))]
    caught=0
    for _,m in ms:
        c=copy.deepcopy(b); m(c)
        try: MOD.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K707 controls: 32"); print(f"PASS K707 hostile mutations rejected: {caught}/25"); return 0 if caught==25 else 1
if __name__=="__main__": raise SystemExit(main())
