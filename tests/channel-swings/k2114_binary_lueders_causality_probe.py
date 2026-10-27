#!/usr/bin/env python3
"""Exact finite controls; continuum statements require the linked written proofs."""
import sympy as s
I=s.I

def kron(*xs):
    out=s.Matrix([[1]])
    for x in xs: out=s.kronecker_product(out,x)
    return out

def annihilators(n, bosonic=False):
    a=s.Matrix([[0,1],[0,0]]);z=s.diag(1,-1);eye=s.eye(2)
    return [kron(*([eye if bosonic else z]*j+[a]+[eye]*(n-j-1))) for j in range(n)]

def equal(a,b):
    if isinstance(a,s.MatrixBase): return all(s.simplify(v)==0 for v in a-b)
    return s.simplify(a-b)==0

def run_suite(checks, faults):
    baseline=checks(None)
    if baseline: print('[FAIL] baseline',baseline);raise SystemExit(1)
    print('PASS clean exact finite baseline; sympy',s.__version__)
    for fault in faults:
        try: failed=checks(fault)
        except Exception as exc: print('CRASH-NOT-DETECTION',fault,repr(exc));raise SystemExit(1)
        if not failed: print('[FAIL] undetected',fault);raise SystemExit(1)
        print('DETECTED',fault,':','; '.join(failed))
    print('PASS',len(faults),'genuine input/machinery faults; no continuum certification')


def checks(fault):
    failures=[]
    def check(ok,msg):
        if not ok: failures.append(msg)
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1);eye=s.eye(2)
    import itertools
    for signs in itertools.product([-1,1],repeat=4):
        R=s.diag(*signs)
        causal=True
        for B in [X,Y,Z]:
            H=(kron(eye,B)+R*kron(eye,B)*R)/2
            causal &= equal(H[:2,:2],H[2:,2:]) and equal(H[:2,2:],s.zeros(2)) and equal(H[2:,:2],s.zeros(2))
        check(causal==(signs[0]*signs[3]==signs[1]*signs[2]),'all diagonal reflections normalizer condition')
    R=s.diag(1,1,1,-1);V=kron(Z,Z)*R;S=s.diag(1,I)
    SS=kron(S,S.H if fault=='phase_orientation' else S)
    w=s.Rational(1,3) if fault=='mixture_weight' else s.Rational(1,2)
    def phi(A): return w*A+(1-w)*R*A*R
    def psi(A): return A/2+(SS*A*SS.H+SS.H*A*SS)/4
    for i in range(4):
      for j in range(4):
        M=s.zeros(4);M[i,j]=1
        check(equal(psi(M),M/2+(R*M*R+V*M*V)/4),'all matrix-unit minimizer identity')
        check(equal(phi(M)-psi(M),(R*M*R-V*M*V)/4),'exact difference of unitary channels')
    plus=s.Matrix([1,1])/s.sqrt(2);b=plus*plus.H
    def bob(A):return A[:2,:2]+A[2:,2:]
    out0=bob(phi(kron(s.diag(1,0),b)));out1=bob(phi(kron(s.diag(0,1),b)))
    check(equal(out0,b) and equal(out1,s.eye(2)/2),'signalling marginal pair')
    ev=(out0-out1).eigenvals();check(equal(sum(abs(x)*n for x,n in ev.items())/2,s.Rational(1,2)),'sharp trace-distance lower witness')
    v=s.Matrix([1,1,0,0])/s.sqrt(2)
    if fault=='distinguishability_input':v=s.Matrix([1,0,0,0])
    check(equal((R*v).H*(V*v),s.zeros(1)),'orthogonal unitary-channel outputs')
    aa=annihilators(4,bosonic=fault=='car_sign');nums=[a.H*a for a in aa]
    check(equal(aa[0]*aa[2]+aa[2]*aa[0],s.zeros(16)),'actual interregion CAR')
    # A and B dual-rail hopping are even; corner basis |1010>,|1001>,|0110>,|0101>.
    xa=aa[0].H*aa[1]+aa[1].H*aa[0];xb=aa[2].H*aa[3]+aa[3].H*aa[2]
    C=s.zeros(16,4)
    for j,k in enumerate([10,9,6,5]):C[k,j]=1
    coarse=s.eye(16)-(s.eye(16)-nums[1])*nums[3]
    target=s.diag(1,0,1,1)
    check(equal(C.H*coarse*C,target) and equal(coarse*C,C*target),'actual coarse-projector reducing corner')
    if fault=='dual_rail_generator':xa=nums[0]-nums[1]
    check(equal(C.H*xa*C,kron(X,eye)) and equal(C.H*xb*C,kron(eye,X)),'even local logical factors')
    return failures

if __name__=='__main__':run_suite(checks,['phase_orientation','mixture_weight','distinguishability_input','car_sign','dual_rail_generator'])
