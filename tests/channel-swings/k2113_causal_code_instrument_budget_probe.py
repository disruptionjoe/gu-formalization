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
    # Two system modes followed by two probe modes. Full CAR exchange, not qubit SWAP.
    a0,a1,b0,b1=annihilators(4,bosonic=fault=='car_sign')
    eye=s.eye(16)
    def quarter(b,a,sign):
        K=sign*(b.H*a-a.H*b)
        return eye+K+K*K
    capture=quarter(b0,a0,1)*quarter(b1,a1,1)
    check(equal(capture.H*b0*capture,a0),'fermionic capture intertwiner')
    release=capture if fault=='release_sign' else capture.H
    if fault=='missing_release': release=eye
    # E=0 is an even projection: no-readout control must return the full code.
    total=release*capture
    check(equal(total.H*a0*total,a0),'no-readout complete mode return')
    n0=b0.H*b0;n1=b1.H*b1;E=n0+n1-2*n0*n1
    W0=eye-E;W1=E
    s0,s1=annihilators(2);ns0=s0.H*s0;ns1=s1.H*s1;Es=ns0+ns1-2*ns0*ns1
    # Pull full recorded effects back, test every code matrix unit in each branch.
    for b in [0,1]:
        L=release*(W1 if b else W0)*capture
        P=Es if b else s.eye(4)-Es
        for i in range(4):
            for j in range(4):
                X=s.zeros(4);X[i,j]=1
                actual=L.H*kron(X,s.eye(4))*L
                expected=kron(P*X*P,s.eye(4))
                check(equal(actual,expected),'recorded matrix-unit identity')
    psi=s.Matrix([1,0,0,1])/s.sqrt(2);rho=psi*psi.H
    if fault=='fine_readout':
        coarse=s.diag(*list(rho.diagonal()))
    else: coarse=(s.eye(4)-Es)*rho*(s.eye(4)-Es)+Es*rho*Es
    check(equal(coarse,rho),'vacuum-pair coherence retained')
    fine=s.diag(*list(rho.diagonal()));diff=rho-fine
    check(equal(sum(abs(ev)*multiplicity for ev,multiplicity in diff.eigenvals().items())/2,s.Rational(1,2)),'exact refined readout trace distance')
    # Bounded even gate can mix the vacuum with an energetically bad pair.
    vac=s.diag(1,0,0,0);mix=rho*vac*rho+(s.eye(4)-rho)*vac*(s.eye(4)-rho)
    check(equal(mix,s.diag(s.Rational(1,2),0,0,s.Rational(1,2))),'energy counterexample mixture')
    # Wrong sigma_x phase is modeled by omitted -i number-phase calibration.
    phase=s.diag(1,-I,-I,-1) if fault=='phase_calibration' else s.eye(4)
    check(equal(phase*rho*phase.H,rho),'signed-swap phase calibration')
    return failures

if __name__=='__main__': run_suite(checks,['car_sign','release_sign','fine_readout','phase_calibration','missing_release'])
