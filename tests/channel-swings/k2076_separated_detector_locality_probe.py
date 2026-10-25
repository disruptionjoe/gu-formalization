"""Symbolic/rational identities plus labeled numerical kernel and matrix corroboration."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,isqrt
import json,hashlib
import sympy as s
import numpy as np
import mpmath as mp
R=Path(__file__).resolve().parents[2]
def exact(data,fault=None):
    z=s.symbols('z',positive=True);x=s.symbols('x',nonnegative=True)
    # Elementary integrand majorant, exact Gamma coefficients and derivative normalization.
    assert s.expand((1+x/4)**2-(1+x/2))==x*x/16
    relative=s.simplify(s.gamma(s.Rational(5,2))/(4*s.gamma(s.Rational(3,2))))
    assert relative==(s.Rational(1,8) if fault=='bessel_coefficient' else s.Rational(3,8))
    constant=2+relative+1;assert constant==s.Rational(27,8)
    h=s.besselk(1,z)/z
    deriv=s.simplify(s.diff(h,z).expand(func=True))
    proposed=-s.besselk(0,z)/z-(1 if fault=='derivative' else 2)*s.besselk(1,z)/z**2
    assert s.simplify(s.expand_func(deriv-proposed))==0
    # Heat kernel/Gamma prefactor is exactly 1/(8*pi^2); Bessel integration contributes4/r.
    heat=s.simplify((4*s.pi)**(-s.Rational(3,2))/s.gamma(s.Rational(1,2)))
    assert heat==(1/(16*s.pi**2) if fault=='kernel_half' else 1/(8*s.pi**2))
    for row in data['resources']:
        a=row['mass_times_separation'];lo=isqrt(a);hi=lo+(lo*lo<a)
        poly=sum((F(a**k,factorial(k)) for k in range(81)),F(0));bound=min(F(1,2),(2*hi+F(27,8*lo))/(2*poly))
        assert F(row['cross_norm_upper'])==bound
        assert F(row['luders_disturbance_upper'])==3*bound
        assert F(row['unitary_operator_order_upper'])==2*bound
        assert F(row['unitary_probability_order_upper'])==min(F(1),4*bound)
    # Exact Clifford singular values: beta=diag(1,-1), alpha=[[0,1],[1,0]].
    A=s.Matrix([[0,1],[1,0]]);B=s.diag(1,-1)
    for u,v in [(s.Rational(1,3),s.Rational(2,5)),(1,2),(2,1)]:
        u,v=s.sympify(u),s.sympify(v);M=(u*B+s.I*v*A)/2;assert max((M.conjugate().T*M).eigenvals())==(u+v)**2/4
    for row in data['free_unequal_time_resources']:
        a=F(row['mass'])*(F(row['spatial_gap'])-abs(F(row['time_gap'])))
        if fault=='omit_time_gap':a=F(row['mass'])*F(row['spatial_gap'])
        assert a==F(row['effective_mass_gap']) and a>0
    return 34

def sqrtm(A):
    w,v=np.linalg.eigh((A+A.conj().T)/2);return (v*np.sqrt(np.maximum(w,0)))@v.conj().T

def matrices(fault=None):
    rng=np.random.default_rng(2076);count=0;seen=False
    for n,k in [(4,2),(7,3),(12,5)]:
        for repeat in range(10):
            U,_=np.linalg.qr(rng.normal(size=(n,k))+1j*rng.normal(size=(n,k)))
            P=U@U.conj().T;f=np.diag([1.]*(n//2)+[0.]*(n-n//2));g=np.eye(n)-f
            A=U.conj().T@f@U;B=U.conj().T@g@U
            # For noncomplementary scalar effects, avoid an artificially commuting fixture.
            g=g@np.diag(np.linspace(.2,1,n));B=U.conj().T@g@U
            eta=np.linalg.norm(f@P@g,2);tol=2e-12
            assert eta<=.5+tol and np.linalg.norm(A@B,2)<=eta+tol
            comm=np.linalg.norm(A@B-B@A,2);seen |= comm>1e-6
            assert comm<=2*eta+tol
            if fault=='exact_commutation':assert comm<1e-14,'separation of coordinate supports is not compressed commutation'
            sa=sqrtm(A);ca=sqrtm(np.eye(k)-A);sb=sqrtm(B);cb=sqrtm(np.eye(k)-B)
            D=np.eye(k)-ca;assert np.linalg.norm(D@B,2)<=eta+tol
            assert np.linalg.norm(sa@B@sa,2)<=eta+tol
            assert np.linalg.norm(sa@B@sa+ca@B@ca-B,2)<=3*eta+tol
            psi=rng.normal(size=k)+1j*rng.normal(size=k);psi/=np.linalg.norm(psi)
            # Ordered distributions with labels (A result,B result) kept fixed.
            ab=[];ba=[]
            for ax in [sa,ca]:
                for bx in [sb,cb]:ab.append(np.linalg.norm(bx@ax@psi)**2);ba.append(np.linalg.norm(ax@bx@psi)**2)
            assert abs(sum(ab)-1)<tol and abs(sum(ba)-1)<tol
            assert sum(abs(x-y) for x,y in zip(ab,ba))/2<=min(1,8*eta)+tol
            count+=1
    assert seen
    # Same effect A=0 may be realized by outcome-zero reset channel: no universal instrument bound.
    eta=0;before=0;after=1
    if fault=='arbitrary_instrument':assert abs(after-before)<=3*eta,'reset instrument is not Lueders'
    return count

def numeric():
    mp.mp.dps=35;count=0
    for a in map(mp.mpf,['1','4','8','20']):
        k0=mp.besselk(0,a);k1=mp.besselk(1,a);c=mp.sqrt(mp.pi/2)
        assert k0<=c*mp.exp(-a)/mp.sqrt(a)
        assert k1<=c*mp.exp(-a)/mp.sqrt(a)*(1+3/(8*a))
        # Numerical special-function corroboration, not a proof by sampling.
        integral=mp.quad(lambda z:mp.besselk(0,z),[a,a+2,a+10,mp.inf])
        tail=((a+2)*k0+a*k1+integral)/mp.pi
        upper=mp.exp(-a)/mp.sqrt(2*mp.pi)*(2*mp.sqrt(a)+27/(8*mp.sqrt(a)))
        assert 0<tail<upper;count+=3
    for r in map(mp.mpf,['1','4']):
        heat=mp.quad(lambda t:mp.exp(-t-r*r/(4*t))/t**2,[0,1,mp.inf])/(8*mp.pi**2)
        bessel=mp.besselk(1,r)/(2*mp.pi**2*r)
        assert abs(heat-bessel)<mp.mpf('1e-30');count+=1
    return count
if __name__=='__main__':
    d=json.loads((R/'lab/process/k2076-separated-detector-locality.json').read_text())
    for p,h in d['inputs'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h
    n=exact(d);mat=matrices();num=numeric();faults=[]
    for f,fn in [('bessel_coefficient',lambda f:exact(d,f)),('derivative',lambda f:exact(d,f)),('kernel_half',lambda f:exact(d,f)),('omit_time_gap',lambda f:exact(d,f)),('exact_commutation',matrices),('arbitrary_instrument',matrices)]:
        try:fn(f)
        except AssertionError:faults.append(f)
        else:raise AssertionError('undetected fault '+f)
    print('PASS',n,'symbolic/rational controls;',mat,'finite matrix scenarios and',num,'numerical kernel corroborations; six faults',faults)
