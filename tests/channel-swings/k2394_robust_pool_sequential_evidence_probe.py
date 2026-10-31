#!/usr/bin/env python3
"""K2394 exact fixtures; universal claims rest on the accompanying proofs."""
from fractions import Fraction as F
from itertools import product
import json, hashlib, sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]

checks = {}

def normalizer(values, gamma):
    v = sorted(map(F, values), reverse=True)
    n = len(v)
    return max((gamma * sum(v[:k]) + sum(v[k:])) / (gamma*k+n-k)
               for k in range(n+1))

def corner_max(values, gamma):
    return max(sum(w*x for w,x in zip(ws, values))/sum(ws)
               for ws in product((F(1), gamma), repeat=len(values)))


def run():
    tested=0
    for n in range(2,6):
        for v in product((F(0),F(1),F(3)), repeat=n):
            for gamma in (F(1),F(3,2),F(2),F(3)):
                assert normalizer(v,gamma)==corner_max(v,gamma)
                tested+=1
    checks['normalizer_corner_cases']=tested
    q=(F(3,4),F(1,8),F(1,8))
    p=(F(1,2),F(1,4),F(1,4))
    e=tuple(x/y for x,y in zip(q,p))
    assert e==(F(3,2),F(1,2),F(1,2))
    assert normalizer(e,F(2))==1
    assert sum(x*y for x,y in zip(p,e))==1
    checks['log_optimal_finite_certificate']=True
    # Exact graph-cell representatives AND every root/endpoint.
    cells=(F(-1),F(-3,4),F(-1,2),F(0),F(1,2),F(3,4),F(1))
    ev=[]
    for th in cells:
        a=(1-th)**2>F(1,4)
        b=(1+th)**2>F(1,4)
        assert a or b
        ev.append((F(7,4) if a else F(1,4)) *
                  (F(7,4) if b else F(1,4))*F(7,4)**7)
    cert=F(1,4)*F(7,4)**8
    assert min(ev)==cert==F(5764801,262144)>20
    assert F(1,4)**2*F(7,4)**7==F(823543,262144)<20
    def binary_factor(z, calibrations, theta, gamma):
        scores=[(F(y)-theta*F(x))**2 for x,y in (z,)+calibrations]
        unique_high=all(scores[0]>s for s in scores[1:])
        return F(len(calibrations)+gamma,gamma) if unique_high else F(0)
    assert binary_factor((1,1),((0,F(1,2)),)*2,F(1),F(2))==0
    assert binary_factor((1,-1),((0,F(1,2)),)*2,F(-1),F(2))==0
    assert binary_factor((0,4),((0,F(1,2)),)*2,F(1),F(2))==2
    checks['continuous_fixture_cells_endpoints']=len(cells)
    B=[F(0)]*15
    paths=[None]*15
    B[0]=F(1)
    paths[0]=()
    for c in range(2,15):
        for j in range(2,c+1):
            if paths[c-j] is not None:
                val=B[c-j]*F(j+1,2)
                if val>B[c]:
                    B[c]=val
                    paths[c]=paths[c-j]+(j,)
    assert all(x<20 for x in B[:13])
    assert B[13]==20 and B[14]==25
    positive=F(39,20)**2*F(97,40)**2
    assert positive==F(14311089,640000)>20
    assert F(19,10)**2*F(47,20)**2<20  # lambda=.9 is insufficient for these costs
    checks['pair_cost_dynamic_program']={'B13':str(B[13]),'B14':str(B[14]),'path13':paths[13],'path14':paths[14]}
    checks['positive_28_exposure_certificate']=str(positive)
    assert cert/(1+F(3,2)*F(1,200))**9>20
    assert cert/(1+F(3,2)*F(1,100))**9<20
    # Saturated two-event null and TV shift attain oscillation correction.
    for delta in (F(0),F(1,200),F(1,100),F(1,4)):
        expect=(F(1,2)+delta)*F(7,4)+(F(1,2)-delta)*F(1,4)
        assert expect==1+F(3,2)*delta
    checks['conditional_tv_controls']=4
    assert normalizer((3,1,1),F(2))/F(5,3)==F(6,5)>1
    assert F(7,4)**5<20<F(7,4)**6
    assert F(1,2)>F(1,20)
    # Label-selected b invalid: selected assignment pays 2 whatever label occurs.
    assert F(3)/normalizer((3,0,0),F(2))==2>1
    # Construct SAME-signal exposure realizations from a symmetric finite support.
    support={(0,0),(1,-3),(-1,3),(1,-5),(-1,5),(0,1),(0,-1)}
    assert all((-x,-y) in support for x,y in support)
    s=(0,4)
    for eta,z in (((1,-3),(1,1)),((1,-5),(1,-1)),((0,0),(0,4))):
        assert eta in support
        assert tuple(s[i]+eta[i] for i in range(2))==z
    assert tuple(F(a-b,2) for a,b in zip((0,1),(0,0)))==(F(0),F(1,2))
    checks['finite_symmetric_exposure_realization']=True
    checks['finite_counterexample_assumption_controls']=5
    report={'result':'K2394','status':'pass','evidence_kind':'Exact finite normalizer enumeration, rational cost/TV/counterexample fixtures; universal and continuous claims are written proofs, not sample counts','checks':checks,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['lab/process/k2391-shifted-sequential-calibration.json']}}
    if '--write' in sys.argv:(R/'lab/process/k2394-robust-pool-sequential-evidence.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(report,sort_keys=True))

if __name__=='__main__':
    run()
