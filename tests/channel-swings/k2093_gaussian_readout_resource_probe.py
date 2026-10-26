"""Exact finite controls for K2093; not a continuum proof or channel optimizer."""
from __future__ import annotations
import sympy as s

def check(condition, message):
    if not bool(condition):
        raise AssertionError(message)

def zero(M):
    return all(s.simplify(x)==0 for x in M)

def harness(test, faults):
    test(None)
    print("PASS clean exact baseline")
    for fault in faults:
        try:
            test(fault)
        except AssertionError as exc:
            print(f"[FAIL detected {fault}] {exc}")
        else:
            raise AssertionError(f"undetected fault: {fault}")
    print(f"PASS {len(faults)} genuine input/gate/state faults; universal scope rests on written proofs")

def test(fault):
    I=s.eye(4); E=s.diag(1,0,1,1)
    if fault=='wrong_coarse_sector': E=s.diag(1,0,0,1)
    F=I-E
    psi=s.Matrix([0,1,1,0])/s.sqrt(2); rho=psi*psi.H
    target=s.diag(0,s.Rational(1,2),s.Rational(1,2),0)
    phi=lambda A:E*A*E+F*A*F
    check(zero(phi(rho)-target),'Slater coarse output')
    n1=s.diag(0,0,1,1);n2=s.diag(0,1,0,1)
    a1=s.zeros(4); a1[0,2]=a1[1,3]=1
    a2=s.zeros(4); a2[0,1]=1;a2[2,3]=-1
    for a in [a1,a2]:check(zero(a*a.H+a.H*a-I),'CAR')
    check(zero(a1*a2+a2*a1),'cross CAR')
    state=target if fault!='false_gaussian_output' else I/4
    occ=lambda A:s.simplify(s.trace(state*A))
    defect=s.simplify(occ(n1*n2)-occ(n1)*occ(n2)+abs(occ(a1.H*a2))**2-abs(occ(a1*a2))**2)
    check(defect==-s.Rational(1,4),'nonGaussian Wick defect')
    p=1/s.sqrt(2);q=1-p
    if fault=='wrong_saturator':q=p
    sigma=s.diag((1-p)*(1-q),(1-p)*q,p*(1-q),p*q)
    dist=s.simplify(sum(abs(sigma[i,i]-target[i,i]) for i in range(4))/2)
    check(s.simplify(dist-(s.sqrt(2)-1))==0,'sharp state distance')
    # Genuine even pairing rotation: acts only on |00>,|11>, generated quadratically.
    B=s.eye(4);B[0,0]=B[3,3]=s.Rational(3,5);B[0,3]=s.Rational(4,5);B[3,0]=-s.Rational(4,5)
    check(zero(B*B.H-I) and zero(B*target*B.H-target),'pairing invariance')
    generic=s.diag(s.Rational(1,2),s.Rational(1,4),s.Rational(1,6),s.Rational(1,12))
    paired=B*generic*B.H
    check(paired[0,3]!=0 and zero(B*target*B.H-target),"nontrivial anomalous pairing control")
    check(s.simplify((paired-target).charpoly().as_expr()-(generic-target).charpoly().as_expr())==0,"paired distance spectrum")
    rotated=B*sigma*B.H; check(s.simplify((rotated-target).det()-(sigma-target).det())==0,'paired spectrum check')
    W=s.diag(1,s.I,-s.I,1)
    if fault=='wrong_random_phase':W=s.diag(1,s.I,s.I,1)
    psi_channel=lambda A:(A+W*A*W.H)/2
    parity=[0,1,1,0]
    for i in range(4):
        for j in range(4):
            A=s.zeros(4);A[i,j]=1
            if parity[i]==parity[j]:check(zero(psi_channel(A)-phi(A)),'all even matrix units')
    check(zero(psi_channel(rho)-target),'random quadratic repair of witness')
    # Full extension differs on an odd system direction, visible with fermionic reference.
    A=s.zeros(4);A[0,1]=1
    check(s.simplify((psi_channel(A)-phi(A))[0,1]-(1-s.I)/2)==0,'cross-parity extension')
    check(s.simplify(abs((1-s.I)/2)/2-1/(2*s.sqrt(2)))==0,'total-even reference distance')
    R=2*E-I
    check(s.det(R.extract([0,3],[0,3]))==-s.det(R.extract([1,2],[1,2])),'reflection not quadratic')
    check(s.det(W.extract([0,3],[0,3]))==s.det(W.extract([1,2],[1,2])),'quadratic parity determinant')
    # Partial trace of fixed product bath is contractive; no numerical optimization claimed.

if __name__=='__main__':
    harness(test,['wrong_coarse_sector','false_gaussian_output','wrong_saturator','wrong_random_phase'])
