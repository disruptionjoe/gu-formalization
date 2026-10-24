"""Independent exact four-population optimization and direct shell return oracle."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product,combinations
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def direct(s,p):
    b=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
    kept=[sum(max(v*b[k] for y,v in zip(s,p) for k in range(4) if y+k==x+j)/2 for j in range(4)) for x in s]
    return sum(max(v-w,0) for v,w in zip(p,kept))
def check(row,fault=None):
    a=list(map(Q,row['spectrum']));s=list(map(Q,row['support']));p=list(map(Q,row['populations']));d=Q(row['delta']);e=Q(row['energy'])
    if fault=='free_offset':s=[x-(x%1) for x in s];a=[x-(x%1) for x in a]
    assert len(set(a))==10 and min(y-x for x,y in zip(a,a[1:]))>=d
    assert sum(x*v for x,v in zip(s,p))==e
    R=direct(s,p)
    if fault=='return_double':R*=2
    assert R==Q(row['return_value'])
    assert R-(Q(63,100)-Q(3,20)*e)==Q(row['gap'])

def exact_two_ladder(d,E):
    # Each component's full y-simplex is partitioned at every return kink.
    ys=[Q(0),Q(1,10),Q(1,5),Q(3,5),Q(1)]
    best=None
    for i,j in product(range(4),repeat=2):
        rays=[]
        for offset,ix in [(Q(0),i),(d,j)]:
            for y in ys[ix:ix+2]:
                rays.append((1+2*y+offset,direct([Q(1)+offset,Q(3)+offset],[1-y,y])))
        candidates=[r for e,r in rays if e<=E]
        for (e,r),(f,s) in combinations(rays,2):
            if e==f:continue
            w=(E-e)/(f-e)
            if 0<=w<=1:candidates.append((1-w)*r+w*s)
        if candidates:
            b=min(candidates);best=b if best is None else min(best,b)
    return best
r=json.loads((ROOT/'lab/process/k2014-unrestricted-ten-level-onset.json').read_text())
for row in r['physical_upper_witnesses']:check(row)
faults=[]
for name in ['free_offset','return_double']:
    try:check(r['physical_upper_witnesses'][0],name)
    except AssertionError:faults.append(name)
    else:raise AssertionError('undetected '+name)
programs=0
for k in [1,3,7,10,13,17,19]:
    E=Q(6,5)+Q(k,20)
    for delta in [Q(1,1000),Q(1,100),Q(1,50)]:
        rr=E-Q(6,5);g=Q(63,100)-Q(3,20)*E+Q(3,20)*delta*min(rr/(1+delta),(1-rr)/(1-delta))
        assert exact_two_ladder(delta,E)==g;programs+=1
# Genuine changed branch denominators and changed secant constant, compared with actual optimal subproblems.
for fault in ['wrong_orientation','wrong_slope']:
    E=Q(2);d=Q(1,100);rr=E-Q(6,5)
    try:
        if fault=='wrong_orientation':
            wrong=Q(63,100)-Q(3,20)*E+Q(3,20)*d*rr/(1+d)
            assert wrong==exact_two_ladder(d,E)
        else:
            x=Q(7,5);y=Q(3,2);d=Q(1,100)
            assert exact_two_ladder(d,x)>=exact_two_ladder(d,y)+Q(1,5)*(y-x)
    except AssertionError:faults.append(fault)
    else:raise AssertionError('undetected '+fault)
for row in r['conditional_regime_consumers']:
    d,E,q,drop=map(Q,[row[x] for x in ['delta','energy','preliminary_tail_upper','budget_drop_upper']]);assert drop==(9-E)*q/(1-q)<6*d
    assert Q(row['cutoff_kappa'])==(7-3*E-20*d)/(20*(1+d))>Q(1,101);assert not row['global_threshold_certified'];assert Q(row['faithful_bath_TV_radius'])==6*Q(row['gibbs_t_radius'])
for row in r['unrestricted_asymptotic_coefficients']:
    E=Q(row['energy']);rr=E-Q(6,5);d=Q(row['control_delta']);b=min(rr/(1+d),(1-rr)/(1-d))*Q(3,20)*d
    assert b-Q(row['leading'])*d-Q(row['second'])*d*d==Q(row['remainder_at_control_delta'])
for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
print('PASS K2014 separate',len(r['physical_upper_witnesses']),'physical witnesses;',programs,'complete exact four-population programs;',len(faults),'actual mathematical faults;',len(r['inputs']),'hashes')
