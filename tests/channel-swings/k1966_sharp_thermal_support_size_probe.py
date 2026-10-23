"""Independent word enumeration from bath labels; producer DP is not imported."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def audit(fault=None):
    bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
    if fault=='bath':bath[2]=F(1,15)
    left={d:sum(bath[:4-d])/(1+sum(bath[d:])) for d in (1,2,3)}
    right={d:sum(bath[d:])/(1+sum(bath[:4-d])) for d in (1,2,3)}
    rows=json.loads((ROOT/'lab/process/k1966-sharp-thermal-support-size.json').read_text())['rows'];checks=0
    for N in range(1,10):
        best=F(1)
        for gaps in product((1,2,3),repeat=N-1):
            if fault!='gap' and any(a+b<4 for a,b in zip(gaps,gaps[1:])):continue
            for root in range(N):
                reward=F(1);v=F(1)
                for d in reversed(gaps[:root]):v*=left[d];reward+=v
                v=F(1)
                for d in gaps[root:]:v*=right[d];reward+=v
                best=max(best,reward);checks+=1
        assert best==F(rows[N-1]['bellman_reward']),'actual all-word maximum'
    for row in rows:
        N=row['N'];n=row['n'];m=row['m'];q=F(2,3);p=F(1,9)
        if fault=='allocation':m+=1
        assert n+m+1==N,'occupied cardinality'
        weights=[q**k for k in range(n+1)]+[p**k for k in range(1,m+1)];Z=sum(weights)
        assert Z==F(row['reward'])
        # Sharp population formula reconstructed from incoming actual imbalances.
        pop=[q**(n-i)/Z if i<=n else p**(i-n)/Z for i in range(N)]
        inc=[F(0)]*N
        for i in range(N-1):
            v=F(1,5)*pop[i]-F(4,5)*pop[i+1]
            inc[i]+=max(0,-v);inc[i+1]+=max(0,v)
        ret=sum(max(0,a-b) for a,b in zip(pop,inc))/(1 if fault=='half_trace' else 2)
        assert ret==F(row['return_cost']),'physical marginal half trace factor'
        energy=sum((2*i+1)*v for i,v in enumerate(pop))
        if fault=='energy':energy+=1
        assert energy==F(row['canonical_mean_energy']),'attaining mean energy'
        checks+=4
    for N in range(1,21):
        support=set(range(1,2*N,2));physical=set(range(2*N+1))
        if fault=='padding':physical.remove(0)
        energies={a+b for a in physical for b in range(4)}|{a+b for a in support for b in range(4)}
        ks=[sum(E-b in physical for b in range(4)) for E in energies]
        rs=[sum(E-b in support for b in range(4)) for E in energies]
        assert all(2*r<=k for r,k in zip(rs,ks)), 'physical shell rank'
        assert sum(rs)==4*N and sum(ks)==4*len(physical)
        assert len(physical)==2*N+1 and min(energies)==0
        checks+=3
    return checks
if __name__=='__main__':
    n=audit();caught=[]
    for fault in ['bath','gap','allocation','half_trace','padding','energy']:
        try:audit(fault)
        except AssertionError:caught.append(fault)
        else:raise AssertionError('undetected mathematical fault '+fault)
    r=json.loads((ROOT/'lab/process/k1966-sharp-thermal-support-size.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K1966 independent',n,'controls;',len(caught),'mathematical faults; pins separate')
