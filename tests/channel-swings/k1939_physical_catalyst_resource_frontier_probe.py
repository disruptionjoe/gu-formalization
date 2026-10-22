"""Separate shell census and breakpoint-free rational controls; honest input faults."""
from fractions import Fraction as F
from itertools import combinations
import hashlib,json
from pathlib import Path
import k1939_physical_catalyst_resource_frontier as p

def independent(t,d,x):
    w=[t**b/sum(t**j for j in range(4)) for b in range(4)];a=[F(0),F(0)]
    for E in range(d+4):
        inputs=[]
        if 0<=E<4:inputs.append(x*w[E])
        if 0<=E-d<4:inputs.append((1-x)*w[E-d])
        if not inputs:continue
        eig=max(inputs)/2
        if 0<=E<4:a[0]+=eig
        if 0<=E-d<4:a[1]+=eig
    return sum(max(F(0),s-z) for s,z in zip([x,1-x],a))

def check():
    count=0;mins={1:None,2:None,3:None};gapdims={1:99,2:99,3:99}
    for D in range(2,8):
      for tail in combinations(range(1,8),D-1):
        A=(0,)+tail
        for N in range(1,min(3,D)+1):
          for S in combinations(A,N):
            feasible=all(2*sum(E-b in S for b in range(4))<=sum(E-b in A for b in range(4)) for E in range(max(A)+4))
            if feasible:
                assert D>=2*N+1,'global physical dimension';mins[N]=D if mins[N] is None else min(D,mins[N]);count+=1
                if N==2 and S[1]-S[0] in gapdims:gapdims[S[1]-S[0]]=min(D,gapdims[S[1]-S[0]])
    assert mins=={1:3,2:5,3:7}
    assert gapdims=={1:6,2:5,3:6};count+=1
    for t in [F(1,4),F(1,2),F(3,4)]:
      for d in (1,2,3):
       for j in range(101):
        x=F(j,100);r=independent(t,d,x);assert r==p.rate(t,d,x);count+=1
        E=F(max(1,3-d))+d*(1-x)
        assert p.optimum(t,E)[0]<=r,'global budget minimum below each candidate';count+=1
    # Important frozen example: plateau versus later high-root transition.
    assert p.optimum(F(1,2),F(6,5))[0]==F(9,20)
    assert p.optimum(F(1,2),F(8,5))[0]==F(9,20)
    assert p.optimum(F(1,2),F(11,5))[0]==F(3,10)
    report=json.loads(p.REPORT.read_text());assert report==p.calculate(),'report reproduction'
    assert report['source_sha256']==hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest(),'source pin'
    print('PASS',count+6,'independent exact controls')
    for fault in ['phase','return_factor','empty_level']:
        try:p.calculate(fault)
        except AssertionError as ex:print('DETECTED mathematical input',fault,':',ex)
        else:raise AssertionError('undetected '+fault)
    for name,mut in [('report',dict(report,dimension='D_min=2N')),('pin',dict(report,source_sha256='0'*64))]:
        try:assert mut==report,'report or pin mismatch'
        except AssertionError as ex:print('DETECTED consistency',name,':',ex)
        else:raise AssertionError('undetected reporting fault')
if __name__=='__main__':check()
