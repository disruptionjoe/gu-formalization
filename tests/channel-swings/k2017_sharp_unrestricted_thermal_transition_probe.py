"""Separate bath-label deletion replay and real mathematical fault controls."""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def direct(s,p,t):
    b=[t**j/sum(t**k for k in range(4)) for j in range(4)]
    return sum(max(Q(0),v-sum(max(w*b[k] for y,w in zip(s,p) for k in range(4) if y+k==x+j)/2 for j in range(4))) for x,v in zip(s,p))
def shells(a,s):
    return all(sum(x+b==e for x in a for b in range(4))>=2*sum(x+b==e for x in s for b in range(4)) for e in {x+b for x in s for b in range(4)})
def check(r):
    s=list(map(Q,r['support']));p=list(map(Q,r['populations']));t=Q(r['t']);N=r['cutoff'];a=list(map(Q,r['spectrum']))
    ss=list(map(Q,r['low_support']));pp=list(map(Q,r['low_populations']));aa=list(map(Q,r['low_spectrum']))
    assert sum(p)==sum(pp)==1 and shells(a,s) and shells(aa,ss)
    q=sum(v for x,v in zip(s,p) if x>N);h=sum(x*v for x,v in zip(s,p) if x>N)
    assert q==Q(r['tail_mass']) and h==Q(r['tail_energy'])
    assert sum(x*v for x,v in zip(ss,pp))==(Q(r['mean'])-h)/(1-q)
    before=direct(s,p,t);low=direct(ss,pp,t)*(1-q)
    assert before==Q(r['return_value']) and low==Q(r['unnormalized_low_return'])
    C=(1+t+t*t)/(2*(1+t+t*t+t**3));assert C==Q(r['coarse_loss_coefficient'])
    assert low<=before+Q(r['boundary_loss'])<=before+C*q
r=json.loads((ROOT/'lab/process/k2017-sharp-unrestricted-thermal-transition.json').read_text())
for row in r['physical_deletions']:check(row)
for w in r['optimal_witnesses']:
    a=list(map(Q,w['spectrum']));s=list(map(Q,w['support']));p=list(map(Q,w['populations']));d=Q(w['delta']);E=Q(w['energy']);rv=direct(s,p,Q(1,2))
    assert shells(a,s) and min(y-x for x,y in zip(a,a[1:]))==d
    assert sum(x*v for x,v in zip(s,p))==E and rv==Q(w['return_value'])
    m=Q(3,20)/(1+d);kap=m*(9-E)-rv-Q(7,15)
    assert kap>=Q(2,285) and 1/kap==Q(w['tail_mass_per_return_error']) and 9/kap==Q(w['tail_energy_per_return_error'])
for row in r['secant_controls']:
    d,E,q,x,low,kap=map(Q,[row[k] for k in ['delta','energy','tail_mass','retained_budget','lower_return','kappa']]);m=Q(3,20)/(1+d)
    g=min(Q(9,20)-m*(E-Q(6,5)),Q(3,10)+Q(3,20)/(1-d)*(Q(11,5)-E))
    assert low>=g+kap*q and kap==m*(9-E)-g-Q(7,15)
    if q:assert 9*q<=(low-g)/m+(E+(g+Q(7,15))/m)*q
faults=[]
for name in ['normalization','completion','return','tail_energy']:
    row=deepcopy(r['physical_deletions'][0])
    if name=='normalization':row['low_populations'][0]=str(Q(row['low_populations'][0])+Q(1,100))
    elif name=='completion':row['low_spectrum']=row['low_support']
    elif name=='return':row['return_value']=str(Q(row['return_value'])+Q(1,100))
    else:row['tail_energy']=str(Q(row['tail_energy'])+1)
    try:check(row)
    except AssertionError:faults.append(name)
    else:raise AssertionError('undetected '+name)
# Explicit rejected algebraic extension: the coefficient becomes negative.
assert Q(3,20)/(1+Q(3,10))*(9-Q(6,5))-Q(9,20)-Q(7,15)<0
for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
print('PASS K2017 separate',len(r['physical_deletions']),'physical deletions,',len(r['optimal_witnesses']),'optimal witnesses,',len(r['secant_controls']),'secant controls;',len(faults),'actual faults;',len(r['inputs']),'provenance hashes')
