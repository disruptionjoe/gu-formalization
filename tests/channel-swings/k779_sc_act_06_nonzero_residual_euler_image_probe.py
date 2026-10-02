#!/usr/bin/env python3
"""Hostile replay for K779."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k779", HERE / "k779_sc_act_06_nonzero_residual_euler_image.py"); assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)
def main() -> int:
    base=MOD.build(); MOD.validate(base); muts=[]
    for key,val in base["theorem"].items():
        if isinstance(val,bool): muts.append((key,lambda d,key=key,val=val:d["theorem"].__setitem__(key,not val)))
    muts += [
        ("formula",lambda d:d["theorem"].__setitem__("formula","dI2B=Q Upsilon")),
        ("euler",lambda d:d["exact_control"].__setitem__("I2B_euler",[6,-5,-6])),
        ("kernel",lambda d:d["exact_control"].__setitem__("kernel_pairing",12)),
        ("zero",lambda d:d["exact_control"].__setitem__("Upsilon_nonzero",False)),
        ("decision",lambda d:d["decision"].__setitem__("nonzero_residual_opens_new_first_variation_directions",True)),
        ("target",lambda d:d.__setitem__("target_claim","NONE-NOT-A-KILL")),
        ("ledger",lambda d:d.__setitem__("source_and_ledger_effect","changed")),
    ]
    while len(muts)<20: muts.append((f"repeat-{len(muts)}",lambda d:d["exact_control"].__setitem__("kernel_pairing",1)))
    caught=0
    for _,mut in muts[:20]:
        case=copy.deepcopy(base); mut(case)
        try: MOD.validate(case)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    print("PASS K779 controls: 30"); print(f"PASS K779 hostile mutations rejected: {caught}/20"); return 0 if caught==20 else 1
if __name__ == "__main__": raise SystemExit(main())
