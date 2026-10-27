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

FAULTS=["filter_orientation","signal_phase","tail_factor","effect_product","record_coherence","low_band_transfer"]
def check(fault):
    energies=[0,1,2];A=Matrix([[0,1,1],[1,0,0],[1,0,0]])
    weights={-1:S.Integer(1),-2:Q(1,2)}
    if fault=="filter_orientation":weights={1:S.Integer(1),2:Q(1,2)}
    if fault=="signal_phase":weights[-2]=-1
    B=Matrix(3,3,lambda i,j:A[i,j]*weights.get(energies[i]-energies[j],0))
    vac=Matrix([1,0,0]);psi=Matrix([0,1,1])/sqrt(2)
    eq(B*vac,S.zeros(3,1),"negative energy transfer annihilates vacuum")
    eq((vac.T*B*psi)[0],3/(2*sqrt(2)),"positive spectral-band signal")
    # General finite spectral transfer also kills a whole low-energy band.
    energies=[0,Q(1,2),1,2];a=Q(3,4)
    W=Matrix(4,4,lambda i,j:1 if -Q(3,2)<energies[i]-energies[j]<-a else 0)
    if fault=="low_band_transfer":W[0,1]=1
    eq(W*S.diag(1,1,0,0),S.zeros(4),"low-energy dark subspace")
    t,T=S.symbols("t T",positive=True)
    tail=2*S.integrate(1/(2*S.pi*t**3),(t,T,S.oo))
    if fault=="tail_factor":tail/=2
    eq(tail,1/(2*S.pi*T*T),"two-sided integration-by-parts tail")
    r=Q(1,5);bound=r*(2-r)
    if fault=="effect_product":bound=r*r
    eq(bound,1-(1-r)**2,"product error bound at scalar saturation")
    # Noncommuting effects; exact positive square roots and actual full records.
    U=Matrix([[Q(3,5),-Q(4,5)],[Q(4,5),Q(3,5)]])
    E=S.diag(Q(1,4),Q(9,16));F=U*S.diag(Q(1,9),Q(4,9))*U.T
    e1=S.diag(Q(1,2),Q(3,4));e0=S.diag(sqrt(3)/2,sqrt(7)/4)
    f1=U*S.diag(Q(1,3),Q(2,3))*U.T;f0=U*S.diag(2*sqrt(2)/3,sqrt(5)/3)*U.T
    eq(e1*e1+e0*e0,S.eye(2),"first complete instrument")
    eq(f1*f1+f0*f0,S.eye(2),"second complete instrument")
    assert E*F!=F*E,"noncommuting test must be nontrivial"
    rho=Matrix([[1,1],[1,1]])/2
    out=S.diag(1,0) # record labels are separate from system matrices
    block=e1*rho*e1
    if fault=="record_coherence":block=S.diag(block[0,0],block[1,1])
    eq(block[0,1],Q(3,16),"recorded conditional system coherence")
    # Diamond bound rests on the note proof; finite exact TP/dilation controls only.
    eq(S.trace(e0*rho*e0)+S.trace(e1*rho*e1),1,"all outcomes retained")

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
