"""Separate recurrence and symbolic minimization of the global priced envelopes."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]

def audit(fault=None):
    W=F(25,8);c=F(163,440);D=36;C=F(1,419904)
    if fault=='constant':C=F(1,100)
    assert C<=1/(F(64)*3**8),'lower prefactor domination'
    assert 2*W*(W/c+F(1,2))<64 and D/(2*W)+2<8
    checks=2
    for n in range(9):
        # Independent populations, bath-label incoming differences.
        weights=[F(1)]
        for i in range(2*n):weights.append(weights[-1]*(F(3,2) if i<n else F(1,9)))
        if fault=='population' and n==2:weights[-1]*=2
        p=[x/sum(weights) for x in weights];E=sum((2*i+1)*x for i,x in enumerate(p));inc=[F(0)]*len(p)
        for i in range(len(p)-1):
            d=F(1,5)*p[i]-F(4,5)*p[i+1];inc[i]+=max(F(0),-d);inc[i+1]+=max(F(0),d)
        R=sum(max(F(0),x-y) for x,y in zip(p,inc))/2
        Z=sum(F(2,3)**(n-i) for i in range(n+1))+sum(F(1,9)**i for i in range(1,n+1))
        assert R==1/(2*Z),'actual bath recurrence return'
        assert E<=2*n+F(41,32) and R-F(4,25)<=F(17,50)*F(2,3)**n;checks+=2
    a,lam,Cs=s.symbols('a lambda C',positive=True);x=s.symbols('x',real=True)
    Em=s.log(a*Cs/lam)/a
    if fault=='minimizer':Em=s.log(Cs/lam)/a
    cost=Cs*s.exp(-a*x)+lam*x
    assert s.simplify(s.diff(cost,x).subs(x,Em))==0,'stationary energy'
    assert s.simplify(cost.subs(x,Em)-lam/a*(1+s.log(a*Cs/lam)))==0,'priced lower/upper envelope'
    shifted=s.log(a/lam)/a+x
    target=lam/a*s.log(a/lam)+lam*(x+Cs/a*s.exp(-a*x))
    if fault=='shift':target=target-lam*x
    assert s.simplify(cost.subs(x,shifted)-target)==0,'near optimizer localization'
    checks+=3
    return checks
if __name__=='__main__':
    n=audit();caught=[]
    for fault in ['constant','population','minimizer','shift']:
        try:audit(fault)
        except AssertionError:caught.append(fault)
        else:raise AssertionError('missed mathematical fault '+fault)
    r=json.loads((ROOT/'lab/process/k1964-nonrooted-thermal-price-test.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    assert r['constants']['Cminus']=='1/419904'
    print('PASS K1964 independent',n,'exact/symbolic controls;',len(caught),'mathematical faults')
