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
        if not ok:failures.append(msg)
    es=[s.Integer(x) for x in [2,3,4,5]];Q=s.diag(1,1,-1,-1);h=s.diag(2,3,-4,-5)
    B=s.Matrix([[1,I],[2,1-I]]);O=s.zeros(4);O[:2,2:]=B;O[2:,:2]=B.H
    K=s.zeros(4)
    for i in range(4):
      for j in range(4):
        denominator=es[i]+es[j]
        if fault=='gap_difference':denominator=1+(es[i]-es[j])**2
        K[i,j]=O[i,j]/denominator
    X=(-1 if fault!='sylvester_sign' else 1)*Q*K
    check(equal(X.H,-X),'anti-Hermitian exact inverse')
    check(equal(h*X-X*h,-O),'free-gap commutator cancellation')
    check(equal(Q*O-O*Q,(1 if fault=='commutator_factor' else 2)*Q*O),'two off-block commutator factor')
    m,v,t=s.symbols('m v t',positive=True,real=True);angle=v/(2*m)
    W=s.Matrix([[s.cos(angle),-s.sin(angle)],[s.sin(angle),s.cos(angle)]])
    H=s.Matrix([[m,v],[v,-m]]);trans=s.simplify(W.T*H*W)
    expected=v*s.cos(v/m)-m*s.sin(v/m)
    actual=trans[0,1]
    if fault=='truncate_exact_transform':actual=-v**3/(3*m*m)
    check(equal(actual,expected),'entire conjugation remainder retained')
    check(equal(s.diff(expected,v).subs(v,0),0),'first-order off-block cancelled')
    check(equal(s.diff(expected,v,3).subs(v,0)/6,-1/(3*m*m)),'nonzero cubic exact remainder')
    Wt=W.subs(v,t*t);connection=s.simplify(-I*Wt.T*s.diff(Wt,t))
    if fault=='omit_time_connection':connection=s.zeros(2)
    Y=s.Matrix([[0,-I],[I,0]])
    check(equal(connection,-t*Y/m),'moving-frame derivative connection')
    T,z=s.symbols('T z',positive=True)
    amp=T**(2 if fault=='volume_factor' else 3)
    # Direct three-dimensional square-kernel integral, not a continuum propagator check.
    integ=s.integrate(s.exp(-2*T*T*z*z),(z,-s.oo,s.oo))
    norm2=s.simplify(amp**2*integ**3)
    check(equal(norm2,T**3*(s.pi/2)**s.Rational(3,2)),'HS growing-volume factor')
    radial=s.integrate(4*s.pi*z*z/(z*z+m*m)**3,(z,0,s.oo))
    check(equal(radial,s.pi**2/(4*m**3)),'exact massive radial moment')
    # Actual polarized finite CAR control for the entire-field code extension.
    bb,pp,nn=annihilators(3);aa=annihilators(2)
    k=aa[0].H*aa[1]-aa[1].H*aa[0];cs=s.Rational(3,5);sn=s.Rational(4,5)
    uf=s.eye(4)+sn*k+(1-cs)*k*k;ue=kron(s.eye(2),uf)
    sf=cs*pp+(-1 if fault!='frame_intertwiner_sign' else 1)*sn*nn
    def sw(a):
        k=bb.H*a-a.H*bb
        return s.eye(8)+k+k*k
    wf=sw(pp);ws=sw(sf)
    check(equal(ue*wf.H,ws.H*ue),'full polarized CAR swap intertwiner')
    sea=s.Matrix([0,1,0,0]);inj=kron(s.eye(2),sea)
    encoded=(wf if fault=='encoder_adjoint' else wf.H)*inj
    jf=s.Matrix.hstack(sea,aa[0].H*sea)
    check(equal(encoded[:4,:],jf) and equal(encoded[4:,:],s.zeros(4,2)),'positive ordered creation-basis encoding')
    actual=ue*encoded
    check(equal(actual[4:,:],s.zeros(4,2)),'auxiliary memory empties for every code basis input')
    nex=aa[0].H*aa[0]+s.eye(4)-aa[1].H*aa[1]
    check(equal((sea.H*uf.H*nex*uf*sea)[0],2*sn**2),'particle-plus-hole vacuum moment')
    return failures

if __name__=='__main__':run_suite(checks,['gap_difference','sylvester_sign','commutator_factor','truncate_exact_transform','omit_time_connection','volume_factor','frame_intertwiner_sign','encoder_adjoint'])
