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
    aa=annihilators(4,bosonic=fault=='car_sign');b0,b1,a0,a1=aa
    check(equal(b0*a0+a0*b0,s.zeros(16)),'memory and field CAR')
    sign=-1 if fault=='orientation' else 1
    def swap(b,a):
        K=sign*(b.H*a-a.H*b)
        theta=s.pi/4 if fault=='angle' else s.pi/2
        return s.eye(16)+s.sin(theta)*K+(1-s.cos(theta))*K*K
    W=swap(b0,a0)*swap(b1,a1)
    check(equal(W.H*W,s.eye(16)),'swap unitarity')
    check(equal(W.H*b0*W,a0),'first transported annihilator')
    check(equal(W.H*b1*W,a1),'second transported annihilator')
    # Actual memory-vacuum block, independently constructed two-mode target.
    small=annihilators(2)
    for word,target in [(b0,small[0]),(b1,small[1]),(b0.H*b1.H,small[0].H*small[1].H),(b0.H*b0*b1.H*b1,small[0].H*small[0]*small[1].H*small[1])]:
        actual=(W.H*word*W)[:4,:4]
        check(equal(actual,target),'vacuum expectation word')
    v=(s.Rational(1,5) if fault=='frame_difference' else s.Rational(2,5))*a0-s.Rational(4,5)*a1
    D=b0.H*v-v.H*b0;A=D.H*D;delta2=s.Rational(4,5)
    check(equal(A*A,delta2*A) and A.trace()>0,'exact difference-generator norm squared')
    # Same phase on d=2 changes vacuum/pair relative phase, even states suffice.
    phase=I; G=s.diag(1,phase,phase,phase if fault=='accumulated_phase' else phase**2)
    psi=s.Matrix([1,0,0,1])/s.sqrt(2);rho=psi*psi.H
    out=G*rho*G.H
    check(equal(out[0,3],-s.Rational(1,2)),'two-mode coherence phase accumulation')
    return failures

if __name__=='__main__': run_suite(checks,['car_sign','orientation','angle','frame_difference','accumulated_phase'])
