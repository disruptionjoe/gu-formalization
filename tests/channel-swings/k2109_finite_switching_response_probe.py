#!/usr/bin/env python3
"""Exact controls and real data/machinery mutations; not continuum certification.
Requires SymPy 1.14.0. Run this file directly; a baseline failure aborts first.
"""
import sympy as S
from sympy import Matrix, Rational as Q, sqrt, I

def eq(a,b,label):
    if isinstance(a,S.MatrixBase):
        assert all(S.simplify(x)==0 for x in a-b), label
    else:
        assert S.simplify(a-b)==0, label

def norm2(v): return S.simplify((v.conjugate().T*v)[0])

FAULTS=["radial_factor","gaussian_gap_sign","triangle_factor","adiabatic_power","creation_amplitude","absorption_frequency"]
def check(fault):
    k,w,m=S.symbols("k w m",positive=True)
    density=4*S.pi*k*k/(2*(2*S.pi)**3*w)*(w/k)
    if fault=="radial_factor":density*=2
    eq(density,k/(4*S.pi**2),"radial measure")
    # Actual massless Gaussian integral at positive gap, including normalizer.
    x=S.symbols("x",positive=True);z=S.Integer(1)
    shift=-z if fault=="gaussian_gap_sign" else z
    g=2*S.pi/(4*S.pi**2)*S.integrate(x*S.exp(-(x+shift)**2),(x,0,S.oo))
    expected=(S.exp(-z*z)-sqrt(S.pi)*z*S.erfc(z))/(4*S.pi)
    eq(g,expected,"Gaussian response integral")
    t=S.symbols("t",real=True);T,v=S.symbols("T v",positive=True)
    triangle=2*S.integrate((1-t/T)*S.cos(v*t),(t,0,T))
    if fault=="triangle_factor":triangle/=2
    eq(triangle,2*(1-S.cos(T*v))/(T*v*v),"compact triangular transform")
    eq(S.limit(triangle,v,0),T,"zero frequency continuation")
    for N in [2,3,4]:
        J=S.integrate(w/(2+w)**(2*N),(w,3,S.oo))
        eq(J,5**(2-2*S.Integer(N))/(2*N-2)-2*5**(1-2*S.Integer(N))/(2*N-1),"vacuum tail constant")
        Jminus=S.integrate(w/(w-2)**(2*N),(w,3,S.oo))
        eq(Jminus,Q(1,2*N-2)+Q(2,2*N-1),"subthreshold tail constant")
        scaled=T*T/(T*v)**(2*N)
        if fault=="adiabatic_power":scaled=T/(T*v)**(2*N)
        eq(scaled,T**(2-2*N)/v**(2*N),"dilated transform square")
    # Two-mode bosonic Fock computation, cutoff >=2 exact on all used inputs.
    a=S.zeros(3)
    for n in [1,2]:a[n-1,n]=sqrt(n) if fault!="creation_amplitude" else 1
    a0=S.kronecker_product(a,S.eye(3));a1=S.kronecker_product(S.eye(3),a)
    vac=S.zeros(9,1);vac[0]=1
    f=Matrix([Q(1,1)/sqrt(2),I/sqrt(2)]);psi=(f[0]*a0.T+f[1]*a1.T)*vac
    h=Matrix([2,1+I]);b=Matrix([1-I,3]);K=h[0]*a0+h[1]*a1+b[0]*a0.T+b[1]*a1.T
    fv=norm2(K*vac);amp=(h.T*f)[0];stim=(f.conjugate().T*b)[0]
    eq(norm2(K*psi),fv+S.Abs(amp)**2+S.Abs(stim)**2,"CCR one-particle coefficient")
    eq(fv,11,"vacuum kernel normalization")
    # Fourier frequency of annihilation is Delta-omega, not Delta+omega.
    sign=-1 if fault!="absorption_frequency" else 1
    transform=S.integrate(S.exp(-t*t/2)*S.exp(2*I*t)*S.exp(sign*3*I*t),(t,-S.oo,S.oo))
    eq(transform,sqrt(2*S.pi)*S.exp(-Q(1,2)),"actual Gaussian absorption transform")

def main():
    check(None)
    print("PASS clean exact finite/analytic controls")
    for fault in FAULTS:
        try:
            check(fault)
        except AssertionError as exc:
            print("[FAIL] planted", fault, "caught:", exc)
        else:
            raise AssertionError("UNDETECTED " + fault)
    print("PASS", len(FAULTS), "genuine faults rejected; continuum proofs are in the note")

if __name__ == "__main__":
    main()
