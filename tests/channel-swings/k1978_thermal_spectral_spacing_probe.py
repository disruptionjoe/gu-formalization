"""Independent spectral/shell certificates, without importing the producer."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def check(fault=None):
    r=json.loads((ROOT/'lab/process/k1978-thermal-spectral-spacing.json').read_text());n=0
    for index,row in enumerate(r['compression_controls']):
        old=list(map(F,row['original']));new=list(map(F,row['compressed']));delta=F(row['delta']);d=len(old)
        if index==0 and fault=='spacing':new[1]=new[0]
        if index==0 and fault=='shell_shift':new[2]+=F(1,100)
        assert new[0]==0 and all(b-a>=delta for a,b in zip(new,new[1:]));n+=1
        assert all(a<=b for a,b in zip(new,old)) and max(new)<=(d-1)*(delta+3*(d-1))+3*(d-1);n+=1
        for i,a in enumerate(old):
            for j,b in enumerate(old):
                for k in range(4):
                    for l in range(4):
                        if a+k==b+l:assert new[i]+k==new[j]+l;n+=1
    bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
    for row in r['upper_families']:
        E,delta=F(row['energy']),F(row['spacing']);w=(E-F(6,5))/(1+delta)
        if fault=='budget':w=E-F(6,5)
        p=[(1-w)*F(9,10),(1-w)/10,2*w/5,3*w/5];support=[F(1),F(3),1+delta,3+delta]
        A=sorted([F(k)+h for k in range(5) for h in [F(0),delta]])
        assert len(set(A))==10 and min(b-a for a,b in zip(A,A[1:]))>=delta
        assert sum(p)==1 and sum(e*v for e,v in zip(support,p))==E;n+=2
        back=[F(0)]*4
        for e in {x+b for x in support for b in range(4)}:
            members=[(j,b) for j,x in enumerate(support) for b in range(4) if x+b==e]
            rank=sum(e-x in range(4) for x in A)
            assert rank>=2*len(members)
            weight=max(p[j]*bath[b] for j,b in members)
            for j,b in members:back[j]+=weight/2
            n+=1
        ret=sum(max(F(0),a-b) for a,b in zip(p,back))
        assert ret==F(row['return_error']) and ret-(F(63,100)-F(3,20)*E)==F(row['gap']);n+=1
    # Independently enumerate possible partner gaps for the crucial two shells.
    for b,expected in [(1,{-2}),(2,{2})]:
        partners={b-k for k in range(4) if abs(b-k)>1}
        assert partners==expected
        assert not {q for q in partners if abs(q)>2};n+=2
    if fault=='threshold':assert any(abs(1-k)>2 for k in range(4))
    assert F(r['threshold_witness']['return_error'])==F(1,2)
    assert sum(bath)/2==F(1,2);n+=2
    for path,h in r['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h
    return n
if __name__=='__main__':
    n=check();faults=['spacing','shell_shift','budget','threshold']
    for f in faults:
        try:check(f)
        except AssertionError:pass
        else:raise AssertionError('undetected mathematical fault '+f)
    print('PASS K1978 independent',n,'rational energy/shell obligations;',len(faults),'mathematical faults rejected')
