"""Separate direct shell-weight checks and physical resource mutations."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]

def return_direct(p,b):
    # Pair occupied energies1,3. Each shared shell has a separate bath-label allocation.
    incoming=[Q(0),Q(0)]
    for low_bath in [2,3]:
        high_bath=low_bath-2;left=p[0]*b[low_bath];right=p[1]*b[high_bath]
        incoming[0]+=max(right-left,0);incoming[1]+=max(left-right,0)
    return sum(max(x-y,0) for x,y in zip(p,incoming))/2

def physical(delta,w,mutation=None):
    levels=sorted([Q(i) for i in range(5)]+[Q(i)+delta for i in range(5)])
    if mutation=='collision':levels=[Q(i) for i in range(5)]*2
    assert len(set(levels))==10 and min(y-x for x,y in zip(levels,levels[1:]))>=delta
    E=Q(6,5)+w;actual=(1-w)*Q(6,5)+w*(Q(11,5)+delta)
    if mutation=='free_flag':actual-=w*delta
    assert actual-E==w*delta>0
    weights=[(1-w)*Q(9,10),(1-w)*Q(1,10),w*Q(2,5),w*Q(3,5)]
    sites=[Q(1),Q(3),1+delta,3+delta]
    assert sum(x*y for x,y in zip(sites,weights))==actual
    ret=Q(9,20)*(1-w)+Q(3,10)*w
    if mutation=='normalization':ret*=2
    assert ret+Q(3,20)*actual-Q(63,100)==Q(3,20)*w*delta

r=json.loads((ROOT/'lab/process/k2012-thermal-duality-gap-and-bath-stability.json').read_text());count=0
for d in [Q(1,100),Q(1,10),Q(1,2)]:
    for w in [Q(k,10) for k in range(1,10)]:physical(d,w);count+=1
for c in r['chords']:
    e=Q(c['E']);chord=Q(c['line'])
    for lam in [Q(k,100) for k in range(31)]:
        upper=min(Q(9,20)+lam*(Q(6,5)-e),Q(3,10)+lam*(Q(11,5)-e))
        assert upper<=chord and ((upper==chord)==(lam==Q(3,20)));count+=1
baths=[[Q(a,7),Q(b,7),Q(c,7),Q(7-a-b-c,7)] for a in range(1,4) for b in range(1,5-a) for c in range(1,6-a-b)]
for x,y in combinations(baths,2):
    for p in [[Q(k,10),1-Q(k,10)] for k in range(1,10)]:
        diff=abs(return_direct(p,x)-return_direct(p,y));tv=sum(map(abs,[a-b for a,b in zip(x,y)]))/2
        assert diff<=tv;count+=1
faults=0
for m in ['collision','free_flag','normalization']:
    try:physical(Q(1,10),Q(2,5),m)
    except AssertionError:faults+=1
    else:raise AssertionError('fault not detected '+m)
# Explicit channel-mixture face counterexample if a support weight is zero.
branches=[Q(0),Q(1)];faithful=[Q(1,2)]*2;missing=[Q(1),Q(0)]
assert sum(x*y for x,y in zip(branches,missing))==0
assert sum(x*y for x,y in zip(branches,faithful))!=0
# A false extrapolation that zero average at missing support forces each branch zero is refuted.
assert not all(x==0 for x in branches);contrary=1
# Tail comparison and coefficient are checked from stored actual physical data.
for a in r['tail_transfers']:
    high,q,e,R,gap,low=map(Q,[a[k] for k in ['high','tail','energy','return_value','gap','normalized_low']])
    expected=(1-q)*Q(9,20)+q/2
    assert R==expected and e==(1-q)*Q(6,5)+q*high
    assert q*Q(7,100)<=gap and q*7<=e-1
    assert low-R<=q/(1-q)
    assert (8-e)*(low-(Q(63,100)-Q(3,20)*e))<=(108-e)*gap
    count+=1
for a in r['linear_order_coefficients']:
    e=Q(a['E']);upper=Q(3,20)*min(e-Q(6,5),Q(11,5)-e)
    assert Q(a['limsup_upper'])==upper
    assert Q(a['liminf_lower'])*(108-e)==upper*(8-e);count+=1
# Corrupt the retained energy window in an actual shell: occupied8 needs a partner9.
levels=[Q(7),Q(8),Q(9)];occupied=Q(8)
def rank_ok(xs):return all(sum(e-x in (0,1,2,3) for x in xs)>=2 for e in [occupied+i for i in range(4)])
assert rank_ok(levels) and not rank_ok(levels[:-1]);contrary+=1
for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
print('PASS K2012',count,'separate exact groups;',faults,'mathematical mutations;',contrary,'contrary controls;',len(r['inputs']),'provenance hashes')
