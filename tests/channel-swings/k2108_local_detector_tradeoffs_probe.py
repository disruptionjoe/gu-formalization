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

FAULTS=["dark_weight","dephase_coherence","root_cross_term","commutant_scale","missing_complement","sharpness_effect"]
def check(fault):
    p=Q(1,3); omega=Matrix([sqrt(p),0,0,sqrt(1-p)]);rho=omega*omega.T
    E=S.diag(1,1,0,0)
    dark=(omega.T*E*omega)[0]
    if fault=="dark_weight": dark=1-dark
    eq(dark,Q(1,3),"faithful vacuum event")
    K0=E;K1=S.eye(4)-E
    if fault=="missing_complement":K1=S.zeros(4)
    eq(K0*K0+K1*K1,S.eye(4),"complete Kraus map")
    out=K0*rho*K0+K1*rho*K1
    if fault=="dephase_coherence":out=rho
    eq((omega.T*out*omega)[0],Q(5,9),"global vacuum disturbance")
    # The reduced diagonal state is unchanged despite global disturbance.
    eq(Matrix([[out[0,0]+out[1,1],out[0,2]+out[1,3]],
               [out[2,0]+out[3,1],out[2,2]+out[3,3]]]),S.diag(p,1-p),"local restriction")
    C=2;delta=Q(1,5)
    x=(sqrt(1+C*C-delta*delta)-C*delta)/(1+C*C)
    if fault=="root_cross_term": x=(sqrt(1+C*C-delta*delta)+C*delta)/(1+C*C)
    eq(1-x*x,(C*x+delta)**2,"error root solves original positive crossing")
    # Exact sharpness at delta=0, C=2 in a diagonal algebra.
    eps=Q(1,5);om=Matrix([sqrt(eps),sqrt(1-eps)]);ps=Matrix([sqrt(1-eps),sqrt(eps)])
    event=S.diag(1,0) if fault!="sharpness_effect" else S.diag(0,1)
    B=S.diag(2,Q(1,2));eq(B*om,ps,"bounded diagonal preparation")
    eq((om.T*event*om)[0],eps,"dark sharpness");eq(1-(ps.T*event*ps)[0],eps,"miss sharpness")
    # Finite Schmidt-weight controls of preparation cost; fixed-vacuum sequence is proved in the note.
    for n in [2,3,5,8]:
        lam=Q(1,n);om=Matrix([sqrt(lam),0,0,sqrt(1-lam)]);target=Matrix([1,0,0,0])
        b=S.kronecker_product(S.eye(2),S.diag(1/sqrt(lam),0))
        if fault=="commutant_scale": b=S.kronecker_product(S.eye(2),S.diag(sqrt(lam),0))
        eq(b*om,target,"commutant preparation norm cost")
        eq(E*b,b*E,"commutant condition")
    # Removing separating assumption permits a nonzero silent event.
    eq((Matrix([1,0]).T*S.diag(0,1)*Matrix([1,0]))[0],0,"nonseparating countercontrol")

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
