#!/usr/bin/env python3
"""Independent rational coefficient integration and boundary certificate controls."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def derivative(f):return [i*f[i] for i in range(1,len(f))]
def val(f,t):return sum(c*t**i for i,c in enumerate(f))
def norm2(f,L):return sum(x*y*L**(i+j+1)/Q(i+j+1) for i,x in enumerate(f) for j,y in enumerate(f))
def checks(a,g,h,ell,delta,coefficient_fault=0,allocation_fault=0):
    a,g,h,ell,delta=map(Q,(a,g,h,ell,delta));D=a**3+g**3
    p=h*g/2-g**3*delta/D+Q(allocation_fault,100);v=h*a/2-a**3*delta/D
    out=[Q(0),Q(0),3*p/g**2-h/g,h/g**2-2*p/g**3+Q(coefficient_fault,100)]
    inn=[p+h*ell,h,3*v/a**2-2*h/a,h/a**2-2*v/a**3]
    assert val(out,g)==p and val(derivative(out),g)==h,'outer join'
    assert val(derivative(inn),a)==0,'central slope'
    Ac=h*(ell+(g+a)/2);assert val(inn,a)==Ac-delta,'central contact'
    assert 6*out[3]==6*inn[3]==12*delta/D,'shear cancellation'
    assert h*g/3<=p<=h*g/2 and h*a/3<=v<=h*a/2,'sign interval'
    E=2*(norm2(derivative(derivative(out)),g)+norm2(derivative(derivative(inn)),a))
    assert E==2*h*h*(1/g+1/a)+24*delta*delta/D,'full energy'
    # Independent boundary pairing: arbitrary common plateau variation r and central c<=0.
    for r,c in [(Q(3,7),Q(-1,5)),(Q(-2),Q(0))]:
        eta_out=[Q(0),Q(0),3*r/g**2,-2*r/g**3]
        eta_in=[r,Q(0),3*(c-r)/a**2,-2*(c-r)/a**3]
        def pair(f,k,L):
            x=derivative(derivative(f));y=derivative(derivative(k))
            return sum(u*w*L**(i+j+1)/Q(i+j+1) for i,u in enumerate(x) for j,w in enumerate(y))
        cross=2*(pair(out,eta_out,g)+pair(inn,eta_in,a))
        assert cross==-24*delta*c/D and cross>=0,'global boundary multiplier'
    return E

def baseline(**fault):
    for a,g in [(1,1),(1,2),(2,1),(2,3)]:
        h=Q(2);dm=h*(a**3+g**3)/Q(6*max(a*a,g*g))
        for d in [Q(0),dm/2,dm]:checks(a,g,h,1,d,**fault)
    return 12

def contact_checks(fault=False):
    for r in [Q(1),Q(3,4),Q(1,2)]:
        p=Q(1,2)-1/(6*r*r);A=1+p+r/3
        out=[Q(0),Q(0),3*p-1,1-2*p]
        inn=[Q(1),-2/r,1/(r*r)+(Q(1,100) if fault else 0)]
        assert val(inn,r)==0 and val(derivative(inn),r)==0,'contact smooth join'
        assert 6*out[3]==2/(r*r),'contact shear'
        low=val(out,1-r*r);assert low==-(1-r*r)**3/(6*r*r) and low>=-A,'lower obstacle'
        energy=2*norm2(derivative(derivative(out)),Q(1))+2*norm2(derivative(inn),r)
        assert energy==2+2/(3*r**4)+8/(3*r),'continued energy'
        # Test arbitrary plateau value, contact value and contact slope independently.
        for dp,dc,ds in [(Q(3,7),Q(-1,5),Q(2,3)),(Q(-2),Q(0),Q(-1))]:
            eta_out=[Q(0),Q(0),3*dp,-2*dp]
            z=dc-dp
            eta_in=[dp,Q(0),3*z/r**2-ds/r,ds/r**2-2*z/r**3]
            F_in=[p+1,Q(1),-1/r,1/(3*r*r)]
            def pair(f,k,L):
                xx=derivative(derivative(f));yy=derivative(derivative(k))
                return sum(u*w*L**(i+j+1)/Q(i+j+1) for i,u in enumerate(xx) for j,w in enumerate(yy))
            assert 2*(pair(out,eta_out,Q(1))+pair(F_in,eta_in,r))==-4*dc/(r*r),'contact boundary reaction'
        if r==Q(1,2):assert A==1 and energy==18,'A18 exact'
    return 3

def report(fault=False,pin=False):
    r=json.loads((ROOT/'lab/process/k1919-scalar-finite-budget-contact-solution.json').read_text())
    if fault:r['cases'][0]['energy']='0'
    if pin:r['dependencies'][next(iter(r['dependencies']))]='0'*64
    for c in r['cases']:assert checks(c['a'],c['g'],c['h'],c['ell'],c['delta'])==Q(c['energy']),'reported energy'
    for p,d in r['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'dependency pin'
def reject(fn,label):
    try:fn()
    except AssertionError as e:assert str(e);print('CAUGHT',label,':',e);return
    raise AssertionError('missed mutation '+label)
if __name__=='__main__':
    print('BASELINE K1919 independent rational profiles',baseline(),'contact profiles',contact_checks());report()
    reject(lambda:baseline(coefficient_fault=1),'cubic coefficient')
    reject(lambda:baseline(allocation_fault=1),'allocation')
    reject(lambda:contact_checks(True),'contact coefficient')
    reject(lambda:report(fault=True),'report')
    reject(lambda:report(pin=True),'pin')
    print('PASS K1919: 15 full profiles; 3 mathematical input faults, report and pin faults')
