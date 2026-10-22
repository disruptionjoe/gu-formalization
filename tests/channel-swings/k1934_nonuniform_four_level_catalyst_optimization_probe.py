"""Independent rational dual, all-unitary two-site bound, and hostile input tests."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import k1934_nonuniform_four_level_catalyst_optimization as p

def independent():
    n=0
    for t in (F(1,5),F(1,2),F(4,5)):
      u=t*t;L=1/(1+u);H=1-L;z=1+2*u
      for N in range(1,13):
        w=[z**i/sum(z**k for k in range(N)) for i in range(N)]
        r=w[-1]/2
        # Reconstruct transpose recurrence, without producer matrix/inverse.
        f=[]
        for i in range(N-1):f.append((r+(L*f[-1]/2 if f else 0))/(1-L/2))
        f.append(2*(r+(L*f[-1]/2 if f else 0)))
        assert f[-1]==1 and all(0<v<=1 for v in f);n+=1
        for j in range(N):
          col=(1-L/2)*f[j]-(L*f[j-1]/2 if j else 0) if j<N-1 else f[j]/2-(L*f[j-1]/2 if j else 0)
          assert col==r;n+=1
        assert H*(1-w[-1])<=r;n+=1
        for raw in ([F(1,N)]*N,[F(i+1) for i in range(N)],[F(N-i) for i in range(N)]):
          v=[x/sum(raw) for x in raw]
          out=[L*(v[i]+v[i+1])/2 for i in range(N-1)]+[v[-1]/2]
          deficits=[v[i]-out[i] for i in range(N)]
          assert sum(max(F(0),x) for x in deficits)>=r;n+=1
        if N>1:assert r<H+(F(1,2)-H)/N;n+=1
      # Continuous piecewise-linear two-site bound: endpoints of ALL segments suffice.
      breaks=sorted(set([F(0),L/2,L,1-H/2,F(1)]))
      for x in breaks:
        M=max(L*(1-x),H*x)
        d=max(F(0),x-(L*x+M)/2)+max(F(0),1-x-(H*(1-x)+M)/2)
        assert d>=F(1,2)-L/4;n+=1
      # A tempting unweighted escaped-support bound can be too weak.
      x=F(1,10);support=L*x/2+H*(1-x)/2+min(L*(1-x),H*x)
      if t==F(1,2):assert support<F(3,10);n+=1
    import itertools
    # Independent acyclic reward recursion for every orientation; no matrix inverse.
    for t in (F(1,3),F(1,2),F(3,4)):
      u=t*t;L=1/(1+u);H=1-L;q=L/(2-L);pp=H/(2-H)
      for N in range(1,9):
        W=[2*(1+sum(q**k for k in range(1,a+1))+sum(pp**k for k in range(1,N-a))) for a in range(N)]
        for bits in itertools.product((0,1),repeat=N-1):
          memo={}
          def reward(i):
            if i in memo:return memo[i]
            left=(i==0 or bits[i-1]==0);right=(i==N-1 or bits[i]==1)
            diag=(L*left+H*right)/2
            value=F(1)
            if i>0 and left:value+=L*reward(i-1)/2
            if i<N-1 and right:value+=H*reward(i+1)/2
            memo[i]=value/(1-diag);return memo[i]
          vals=[reward(i) for i in range(N)]
          assert all(vals[i]<=W[i] for i in range(N));n+=1
        assert F(1,max(W))>=L*H;n+=1
    return n

def main():
    base=p.report();rpath=p.ROOT/'lab/process/k1934-nonuniform-four-level-catalyst-optimization.json'
    assert json.loads(rpath.read_text())==base,'report baseline'
    n=independent();caught=[]
    for fault in ('weights','dual','phase','pair','root'):
        p.calculate()
        try:p.calculate(fault)
        except AssertionError as e:caught.append(fault);print('[EXPECTED FAIL]',fault,str(e))
        else:raise AssertionError('undetected '+fault)
    for key in ('optimum','script_sha256'):
        bad=dict(base);bad[key]='corrupt'
        try:assert bad==p.report(),'report/pin equality'
        except AssertionError:print('[EXPECTED FAIL]',key)
        else:raise AssertionError('undetected report mutation')
    print(json.dumps({'independent_exact_checks':n,'mathematical_input_faults':caught,'reporting_faults':2}))
if __name__=='__main__':main()
