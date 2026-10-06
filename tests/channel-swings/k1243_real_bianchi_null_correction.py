#!/usr/bin/env python3
"""Coupled causal ranks for css + ssc, the simplest real Bianchi-null correction."""
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import combinations
from pathlib import Path
import runpy
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]; capture=StringIO()
with redirect_stdout(capture): P=runpy.run_path(str(ROOT/"tests/channel-swings/k1241_eight_row_shiab_causal_census.py"))
assert "FAILURES 0" in capture.getvalue()
M,N,ETA=P["M"],P["N"],P["ETA"]; Q=P["P"]; CHECKS=[]
CSS=("comm","symi","symi"); SSC=("symi","symi","comm")
def check(kind,label,condition):
    ok=bool(condition); CHECKS.append((kind,label,ok)); print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
def corrected(source):
    """Add css to the canonical realification i*ssc of the imaginary ssc row."""
    return M["fadd"](M["shiab"](source,CSS),M["fscale"](M["I"],M["shiab"](source,SSC)))
def raw_block(covector,labels):
    k=Q["scalar_one_form"](covector); basis=[(label,mu,label^(1<<mu)) for label in labels for mu in range(N)]; index={(label,mu):i for i,(label,mu,_) in enumerate(basis)}; raw=sp.zeros(len(basis))
    for col,(_,mu,mask) in enumerate(basis):
        image=corrected(M["wedge_raw"](k,Q["direction"](mu,mask)))
        for nu,outmask,value in Q["rows_for_image"](image):
            key=(outmask^(1<<nu),nu)
            if key in index:
                assert value[1]==0; raw[index[key],col]+=sp.Rational(value[0].numerator,value[0].denominator)
    return basis,raw,(raw-raw.T)/2

def census_nonnull(axis):
    covector=tuple(1 if i==axis else 0 for i in range(N)); positive=[i for i,s in enumerate(ETA) if s==1 and i!=axis]; negative=[i for i,s in enumerate(ETA) if s==-1 and i!=axis]; total=0
    import math
    for a in range(len(positive)+1):
        for b in range(len(negative)+1):
            base=Q["signature_mask"](positive,negative,a,b); _,_,e=raw_block(covector,[base,base^(1<<axis)]); total+=math.comb(len(positive),a)*math.comb(len(negative),b)*e.rank()
    return total
def census_null():
    covector=(1,0,0,1)+(0,)*10; positive=[i for i,s in enumerate(ETA) if s==1 and i not in (0,3)]; negative=[i for i,s in enumerate(ETA) if s==-1 and i not in (0,3)]; total=0
    import math
    for a in range(len(positive)+1):
        for b in range(len(negative)+1):
            base=Q["signature_mask"](positive,negative,a,b); _,_,e=raw_block(covector,[base,base^1,base^8,base^9]); total+=math.comb(len(positive),a)*math.comb(len(negative),b)*e.rank()
    return total

FORM_PAIRS=list(combinations(range(N),2)); METRIC_SLOTS=[(p,q) for p in range(4) for q in range(p,4)]
def metric_basis(slot,i,j): p,q=slot; return int((i,j)==(p,q) or (p!=q and (i,j)==(q,p)))
def riemann(k,slot):
    def tensor(i,j,a,b):
        h=lambda x,y:metric_basis(slot,x,y)
        return k[i]*k[a]*h(j,b)-k[i]*k[b]*h(j,a)-k[j]*k[a]*h(i,b)+k[j]*k[b]*h(i,a)
    return tensor
def inject(tensor):
    out={}
    for i,j in FORM_PAIRS:
        coefficient={}
        for a,b in FORM_PAIRS:
            value=ETA[a]*ETA[b]*tensor(i,j,a,b)
            if value: coefficient=M["eadd"](coefficient,M["escale"](value,M["emul"](M["blade"](a),M["blade"](b))))
        if coefficient: out[(1<<i)|(1<<j)]=coefficient
    return out
def columns(k):
    result=[]
    for slot in METRIC_SLOTS:
        image=corrected(inject(riemann(k,slot))); result.append({(mask^(1<<nu),nu):value for nu,mask,value in Q["rows_for_image"](image)})
    return result
def coupled(k,toggles,total):
    cols=columns(k); support={label for col in cols for label,_ in col}; labels=set()
    for label in support:
        for bits in range(1<<len(toggles)):
            moved=label
            for j,axis in enumerate(toggles):
                if bits&(1<<j): moved^=1<<axis
            labels.add(moved)
    basis,_,dist=raw_block(k,sorted(labels)); index={(label,mu):i for i,(label,mu,_) in enumerate(basis)}; mixed=sp.zeros(dist.rows,10)
    for j,col in enumerate(cols):
        for key,value in col.items():
            assert value[1]==0; mixed[index[key],j]=sp.Rational(value[0].numerator,value[0].denominator)
    h=sp.zeros(10+dist.rows); h[:10,10:]=mixed.T; h[10:,:10]=mixed; h[10:,10:]=dist
    return mixed.rank(), total-dist.rank()+h.rank()

dist=(census_nonnull(0),census_nonnull(1),census_null())
t=coupled((1,)+(0,)*13,(0,),dist[0]); s=coupled((0,1)+(0,)*12,(1,),dist[1]); n=coupled((1,0,0,1)+(0,)*10,(0,3),dist[2]); ranks=(t[1],s[1],n[1]); radicals=tuple(229386-x for x in ranks)
check("distortion","corrected distortion ranks are exact",dist==(131070,131070,122880))
check("metric","curvature-response ranks remain six six four",(t[0],s[0],n[0])==(6,6,4))
check("coupled","corrected coupled ranks are exact",ranks==(131070,131070,122882))
check("radical","corrected radicals and cross-null jump are exact",radicals==(98316,98316,106504) and radicals[2]-radicals[0]==8188)
check("gain","gains over selected K132 are 158 158 134",tuple(x-y for x,y in zip(ranks,(130912,130912,122748)))==(158,158,134))
basis,_,normal=raw_block((1,)+(0,)*13,[0,1,2,3]); _,_,tangent=raw_block((0,1)+(0,)*12,[0,1,2,3]); common=normal.rows-normal.col_join(tangent).rank()
check("propagation","normal rank radical common-null and defect remain 32 24 11 13",(normal.rank(),normal.rows-normal.rank(),common,(normal.rows-normal.rank())-common)==(32,24,11,13))
print("CORRECTED_COUPLED_RANKS=131070,131070,122882"); print("CORRECTED_RADICALS=98316,98316,106504"); print("CROSS_NULL_JUMP=8188"); print("PROPAGATION_DEFECT=13")
failures=[label for _,label,ok in CHECKS if not ok]; print(f"TOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures: raise SystemExit("FAILED="+" | ".join(failures))
