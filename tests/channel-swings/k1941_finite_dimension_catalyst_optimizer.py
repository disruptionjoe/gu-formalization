"""Exact interval-cover shell completion and finite physical-dimension return."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, hashlib, json
from k1939_physical_catalyst_resource_frontier import shell_witness, coeff
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1941-finite-dimension-catalyst-optimizer.json'

def completion(support, fault=None):
    S=set(support);empty=set()
    for e in sorted({s+b for s in S for b in range(4)}):
        n=sum(e-b in S for b in range(4))
        missing=n-sum(e-b in empty for b in range(4))
        choices=sorted({e-b for b in range(4)}-S-empty, reverse=fault!='earliest')
        if missing>len(choices):return None
        empty.update(choices[:max(0,missing)])
    return sorted(S|empty)

def paths(n):
    for ds in product((1,2,3),repeat=n-1):
        if all(a+b>=4 for a,b in zip(ds,ds[1:])):yield ds

def support_of(ds):
    S=[0]
    for d in ds:S.append(S[-1]+d)
    return S

def rooted(t,ds,r,normalization=F(1,2)):
    x=[F(0)]*(len(ds)+1);x[r]=F(1)
    for i in range(r-1,-1,-1):
        L,H=coeff(t,ds[i]);x[i]=x[i+1]*L/(1+H)
    for i in range(r,len(ds)):
        L,H=coeff(t,ds[i]);x[i+1]=x[i]*H/(1+L)
    total=sum(x);return normalization/total,[z/total for z in x]

def optimize(t,D,normalization=F(1,2)):
    if D<3:return None
    best=None
    for n in range(1,(D-1)//2+1):
        for ds in paths(n):
            S=support_of(ds);A=completion(S)
            if A is None or len(A)>D:continue
            for root in range(n):
                rate,weights=rooted(t,ds,root,normalization)
                if best is None or rate<best['rate']:
                    offset=-min(A)
                    best=dict(rate=rate,gaps=list(ds),root=root,weights=weights,support=[s+offset for s in S],physical=[a+offset for a in A])
    return best

def calculate(fault=None):
    checks=0;cover_rows=[];rows=[]
    for n in range(1,6):
        for ds in paths(n):
            S=support_of(ds);A=completion(S,fault)
            assert A is not None,'admissible path must complete'
            for e in {a+b for a in A for b in range(4)}:
                assert sum(e-b in A for b in range(4))>=2*sum(e-b in S for b in range(4)),'shell rank';checks+=1
            assert len(A)>=2*n+1,'dimension lower bound';checks+=1
            cover_rows.append(dict(gaps=list(ds),dimension=len(A),physical=A))
    # Actual full complex shell matrices on optimum spectra, including edge shells.
    for t in [F(1,2),F(3,4),F(9,10)]:
        previous=F(1)
        for D in range(3,12):
            best=optimize(t,D,F(1) if fault=='rate' else F(1,2));r=best['rate']
            assert r<=previous and len(best['physical'])<=D,'dimension monotonicity';checks+=1;previous=r
            if D in (5,6,7,8,9):
                got,k=shell_witness(t,best['support'],best['weights'],best['physical'],'phase' if fault=='phase' else None)
                assert got==r,'full-channel all-input return';checks+=k+1
            row={k:([str(v) for v in x] if k=='weights' else str(x) if k=='rate' else x) for k,x in best.items()}
            row.update(t=str(t),D=D);rows.append(row)
    assert completion([0,1,2]) is None,'three occupied inputs impossible';checks+=1
    assert rows[0]['rate']=='1/2','physical dimension3 return';checks+=1
    return dict(claim='K1941',evidence_kind='exact finite cover/reward arithmetic and full complex shell witnesses; universal proof in note',exact_controls=checks,completion_cases=cover_rows,optima=rows,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print('PASS',r['exact_controls'],'exact controls')
    for row in r['optima']:
        if row['D'] in (7,8,9):print(row)
