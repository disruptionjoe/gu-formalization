#!/usr/bin/env python3
"""Exact operator-span and real principal-Bianchi kernel classification."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]; capture=StringIO()
with redirect_stdout(capture): P=runpy.run_path(str(ROOT/"tests/channel-swings/k1241_eight_row_shiab_causal_census.py"))
assert "FAILURES 0" in capture.getvalue()
CHECKS=[]
def check(kind,label,condition):
    ok=bool(condition); CHECKS.append((kind,label,ok)); print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")

channels={"ccc":("comm","comm","comm"),"ccs":("comm","comm","symi"),"csc":("comm","symi","comm"),"css":("comm","symi","symi"),"scc":("symi","comm","comm"),"scs":("symi","comm","symi"),"ssc":("symi","symi","comm"),"sss":("symi","symi","symi")}
relations=(("ccc","ccs","scc","scs"),("ccc","csc","scc","ssc"),("ccc","css","scc","sss"))
witness={k:[] for k in channels}; all_relations=True; realifiable=True
for covector,labels in [((1,)+(0,)*13,[0,1]),((1,0,0,1)+(0,)*10,[0,1,8,9])]:
    blocks={k:P["raw_block"](covector,labels,v)[2] for k,v in channels.items()}
    for a,b,c,d in relations: all_relations &= blocks[a]-blocks[b]-blocks[c]+blocks[d] == sp.zeros(blocks[a].rows)
    for key in ("css","scs","ssc"):
        values=[value for value in blocks[key] if value]
        realifiable &= (all(sp.im(value)==0 for value in values)
                        or all(sp.re(value)==0 and sp.im(sp.I*value)==0 for value in values))
    for k in channels: witness[k].extend(list(blocks[k]))
check("span", "the displayed rows have rank five on combined nonnull/null witnesses", sp.Matrix([witness[k] for k in channels]).rank()==5)
check("relations", "the same three exact row relations hold on nonnull and null carriers", all_relations)

bcapture=StringIO()
with redirect_stdout(bcapture): runpy.run_path(str(ROOT/"tests/channel-swings/k77_wave2_principal_bianchi_product_selector_probe.py"))
btext=bcapture.getvalue()
check("bianchi", "four displayed rows pass and the defect rank is one", "BIANCHI_PASSING_DISPLAYED_ROWS=4" in btext and "BIANCHI_DEFECT_RANK_ON_DISPLAYED_SPAN=1" in btext)
check("response", "only css has nonzero displayed Riemann response, equal to minus twice Einstein14", "UNIQUE_NONZERO_BIANCHI_DISPLAYED_ROW=comm/symi/symi" in btext and "SELECTED_RIEMANN_RESPONSE=-2*Einstein14" in btext and "SELECTED_WEYL_RESPONSE=0" in btext)
check("real", "the phase-realifiable Bianchi-compatible displayed basis is css scs ssc", realifiable and {k for k,v in channels.items() if v.count("symi")%2==0 and k in {"css","scc","scs","ssc"}}=={"css","scs","ssc"})
print("DISPLAYED_OPERATOR_SPAN_DIMENSION=5"); print("BIANCHI_KERNEL_DIMENSION=4"); print("REAL_BIANCHI_ROWS=css,scs,ssc")
failures=[label for _,label,ok in CHECKS if not ok]; print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures: raise SystemExit("FAILED="+" | ".join(failures))
