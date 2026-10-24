"""Separate bath-label transfer verification and actual physical corruptions."""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def direct(s,p,t):
    bath=[t**b/sum(t**j for j in range(4)) for b in range(4)]
    kept=[]
    for x in s:
        z=Q(0)
        for b in range(4):
            z+=max(v*bath[k] for y,v in zip(s,p) for k in range(4) if y+k==x+b)/2
        kept.append(z)
    return sum(max(v-z,0) for v,z in zip(p,kept))
def shell(a,s):
    return all(sum(x+b==e for x in a for b in range(4))>=2*sum(x+b==e for x in s for b in range(4)) for e in {x+b for x in s for b in range(4)})
def check(row,fault=None):
    a=list(map(Q,row['spectrum']));s=list(map(Q,row['support']));p=list(map(Q,row['populations']));t=Q(row['t']);N=row['N']
    q=sum(v for x,v in zip(s,p) if x>N);e=sum(x*v for x,v in zip(s,p));h=sum(x*v for x,v in zip(s,p) if x>N)
    ss=list(map(Q,row['low_support']));pp=list(map(Q,row['low_populations']));aa=list(map(Q,row['low_spectrum']))
    if fault=='normalization':pp=[v*(1-q) for v in pp]
    if fault=='completion':aa=[x for x in aa if x<=max(ss)]
    if fault=='energy_shift':ss=[x+1 for x in ss];aa=[x+1 for x in aa]
    assert sum(pp)==1 and shell(aa,ss)
    mean=sum(x*v for x,v in zip(ss,pp));assert mean==(e-h)/(1-q)
    assert mean<=Q(row['energy_bound'])==(e-N*q)/(1-q)
    before=direct(s,p,t);after=direct(ss,pp,t)
    if fault=='return_factor':after*=2
    assert before==Q(row['before']) and after==Q(row['after'])
    assert after<=before+q/(1-q)
    assert len(aa)<=2*N+7 and q==Q(row['tail']) and h==Q(row['tail_energy'])
    if t==Q(1,2):assert before-Q(63,100)+Q(3,20)*e>=Q(row['tail_coefficient'])*q
r=json.loads((ROOT/'lab/process/k2013-energy-sensitive-thermal-cutoff.json').read_text())
for row in r['physical_cases']:check(row)
faults=[]
for name in ['normalization','completion','energy_shift','return_factor']:
    try:check(r['physical_cases'][0],name)
    except AssertionError:faults.append(name)
    else:raise AssertionError('undetected '+name)
for row in r['near_optimizer_consumers']:
    e,eps,k,q=map(Q,[row[x] for x in ['energy','epsilon','kappa','tail_upper']]);assert k==(3-e)/10 and k*q==eps*(1-q)
    if eps:assert q<eps/k
for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
print('PASS K2013 separate',len(r['physical_cases']),'physical transfers,',len(r['near_optimizer_consumers']),'tail algebra groups;',len(faults),'actual physical faults;',len(r['inputs']),'hashes')
