"""Independent exhaustive paths/orientations versus DP; actual-input faults after baseline."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json,hashlib
import k1937_finite_support_thermal_optimizer as p

def reward(gaps,root,t,signs):
    n=len(gaps)+1;Z=sum(t**b for b in range(4))
    LH=[(sum(t**b for b in range(4-d))/Z,sum(t**b for b in range(d,4))/Z) for d in gaps]
    diag=[(1-(LH[i-1][0] if i else 0)-(LH[i][1] if i<n-1 else 0))/2 for i in range(n)];edges=[[] for _ in range(n)]
    for i,(L,H) in enumerate(LH):
        a,b,v=(i+1,i,L) if signs[i]==0 else (i,i+1,H);diag[a]+=v/2;edges[a].append((b,v/2))
    memo={}
    def walk(i):
        if i not in memo:memo[i]=(1+sum(v*walk(j) for j,v in edges[i]))/(1-diag[i])
        return memo[i]
    return walk(root)

def independent():
    count=0
    for t in [F(1,5),F(1,2),F(3,4),F(9,10)]:
      for N in range(1,6):
        best=F(0)
        for ds in product((1,2,3),repeat=N-1):
          if any(a+b<4 for a,b in zip(ds,ds[1:])):continue
          for root in range(N):
            outward=(0,)*root+(1,)*(N-1-root);rw=reward(ds,root,t,outward);best=max(best,rw)
            for directions in product((0,1),repeat=N-1):
                assert reward(ds,root,t,directions)<=rw,'outward maximality';count+=1
            # Physical shell populations from original weights at rho12, independently max duplicated spectrum.
            w,R,D=p.profile(t,ds,root);S=[3]
            for d in ds:S.append(S[-1]+d)
            cells={};out=[F(0)]*N;Z=sum(t**b for b in range(4))
            for i,a in enumerate(S):
                for b in range(4):cells.setdefault(a+b,[]).append((i,w[i]*t**b/Z))
            for entries in cells.values():
                assert len(entries)<=2
                for i,_ in entries:out[i]+=max(v for _,v in entries)/2
            assert sum(max(0,w[i]-out[i]) for i in range(N))==R,'mixed shell lower attainment';count+=1
        assert p.optimize(t,N)[3]==1/best,'DP versus all oriented paths';count+=1
    return count

def main():
    base=p.calculate();assert json.loads(p.REPORT.read_text())==base,'report baseline';n=independent()
    for fault in ('denominator','phase'):
        try:p.witness(F(3,4),(1,3,1),1,fault)
        except AssertionError as e:print('DETECTED mathematical input',fault,str(e))
        else:raise AssertionError('missed '+fault)
    try:p.profile(F(1,2),(1,2),1)
    except AssertionError as e:print('DETECTED mathematical input triple occupancy',str(e))
    else:raise AssertionError('missed triple')
    for key in ['exact_controls','source_sha256']:
        bad=dict(base);bad[key]='corrupted'
        try:assert bad==base,key
        except AssertionError:print('DETECTED reporting',key)
        else:raise AssertionError('missed report mutation')
    print('PASS',n,'independent exact controls; 3 math-input, 2 report/pin faults')
if __name__=='__main__':main()
