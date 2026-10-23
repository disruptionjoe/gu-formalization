"""Independent shell census, bath-label return and strict spacing-boundary controls."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]

def admissible(A,S):
    for z in {e+b for e in S for b in range(4)}:
        total=sum(any(a+b==z for b in range(4)) for a in A)
        occ=sum(any(a+b==z for b in range(4)) for a in S)
        if total<2*occ:return False
    return True

def actual_return(t,S,p,fault=None):
    bath=[t**b/sum(t**k for k in range(4)) for b in range(4)];keep={e:F(0) for e in S};shells={}
    for e,w in zip(S,p):
        for b,g in enumerate(bath):shells.setdefault(e+b,[]).append((e,w*g))
    for group in shells.values():
        assert len(group)<=2
        value=max(w for e,w in group)/(3 if fault=='return_factor' else 2)
        for e,w in group:keep[e]+=value
    return sum(max(F(0),w-keep[e]) for e,w in zip(S,p))

def check(fault=None):
    r=json.loads((ROOT/'lab/process/k1981-wide-spacing-thermal-frontier.json').read_text());count=0
    for rec in r['physical_controls']:
        t=F(rec['t']);S=list(map(F,rec['support']));p=list(map(F,rec['weights']));A=sorted({e+h for e in S for h in [-2,0,2]})
        if fault=='spacing':A[1]=F(1)
        if fault=='population':p[0]+=F(1,100)
        assert sum(p)==1,'population normalization'
        assert all(b-a>1 for a,b in zip(A,A[1:])),'actual physical spacing'
        assert admissible(A,S),'full shell rank'
        assert actual_return(t,S,p,fault)==F(rec['return_error'])==F(1,2),'actual bath-label return';count+=3
    for rec in r['boundary_witnesses']:
        t=F(rec['t']);S=[F(1),F(3)];p=[F(1,2),F(1,2)];A=list(map(F,range(5)))
        if fault=='energy':S[1]=F(4)
        assert sum(e*w for e,w in zip(S,p))==F(rec['mean_energy']),'mean energy'
        assert admissible(A,S)
        R=actual_return(t,S,p);assert R==F(rec['return_error'])==(1+3*t*t)/(4*(1+t*t))
        assert F(rec['right_jump_lower_bound'])==(1-t*t)/(4*(1+t*t))>0;count+=4
    # Finite witness search is a control; local shell proof supplies all real spectra.
    feasible=0
    grid=[F(i,2) for i in range(1,17)]
    for n in range(3,6):
        for tail in combinations(grid,n-1):
            A=[F(0)]+list(tail)
            if any(b-a<=1 for a,b in zip(A,A[1:])):continue
            for m in range(1,n):
                for S in combinations(A,m):
                    if not admissible(A,S):continue
                    feasible+=1
                    assert min(S)>=2 and all(abs(a-b) not in [1,2,3] for a,b in combinations(S,2)),'universal necessary condition'
                    assert actual_return(F(1,2),S,[F(1,m)]*m)==F(1,2)
    assert feasible>0
    # Planted spacing-one competitor must be excluded by the strict-spacing theorem.
    A=list(map(F,range(5)));S=[F(1),F(3)]
    allowed=all(b-a>F(1) for a,b in zip(A,A[1:]))
    assert not allowed and actual_return(F(1,2),S,[F(1,2)]*2)<F(1,2),'strict threshold is essential'
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return count,feasible
if __name__=='__main__':
    n,f=check();bad=[]
    for fault in ['spacing','return_factor','energy','population']:
        try:check(fault)
        except AssertionError as e:bad.append((fault,str(e)))
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K1981 separate',n,'bath/energy obligations;',f,'feasible spectrum/support controls;',bad)
