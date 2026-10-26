"""K2094 finite kernel controls; nonatomic continuum proof is in the note."""
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
    f=s.Matrix([s.Rational(3,5),s.Rational(4,5)])
    if fault=='unnormalized_mode': f=s.Matrix([s.Rational(3,5),s.Rational(3,5)])
    P=f*f.H;I=s.eye(2)
    check(zero(P*P-P),'rank-one projection')
    check(P[0,1]==s.Rational(12,25),'offdiagonal cross-block norm')
    check(zero((P-I/2)**2-I/4),'generator half-norm upper saturation')
    # Finite upper-bound saturator checks only; finite grids do not prove essential norms.
    z=s.I;U=I+(z-1)*P;c=(1+s.I)/s.sqrt(2)
    if fault=='wrong_phase':U=I+(z+1)*P
    check(zero((U-c*I).H*(U-c*I)-(2-s.sqrt(2))*I),'phase half-angle distance')
    R=I-2*P;check(zero((R-s.I*I).H*(R-s.I*I)-2*I),'reflection sqrt2 distance')
    # Existing spatial-rotation repair, exact two-site version, no novelty claim.
    G=s.Matrix([[s.Rational(3,5),s.Rational(4,5)],[-s.Rational(4,5),s.Rational(3,5)]])
    if fault=='missing_return': actual=s.diag(z,1)*G
    else:actual=G.H*s.diag(z,1)*G
    check(zero(actual-U),'local rotate-phase-return synthesis')
    atom=s.Matrix([1,0]);Pa=atom*atom.H;Ua=I+(z-1)*Pa
    check(zero(Ua-s.diag(z,1)),'atomic countercontrol zero multiplier distance')
    # One nearest-neighbor layer cannot connect sites0 and3.
    W=s.eye(4);W[0,0]=W[1,1]=0;W[0,1]=W[1,0]=1
    if fault=='hidden_long_range_gate':W[0,3]=1
    check(W[0,3]==0,'depth-one propagation support')
    ff=s.Matrix([1,0,0,1])/s.sqrt(2);VV=s.eye(4)-2*ff*ff.H
    check(abs((VV-W)[0,3])==1,'disjoint-support endpoint lower bound')

if __name__=='__main__':
    harness(test,['unnormalized_mode','wrong_phase','missing_return','hidden_long_range_gate'])
