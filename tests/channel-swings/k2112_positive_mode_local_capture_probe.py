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
    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
    alpha=[kron(X,q) for q in [X,Y,Z]];beta=kron(Z,s.eye(2));mass=s.Integer(2)
    if fault=='mass_sign': beta=-beta
    p=s.Matrix([1,2,2]);q=s.Matrix([2,-1,2]);ep=s.sqrt(13);eq=s.sqrt(13)
    hp=sum((p[j]*alpha[j] for j in range(3)),s.zeros(4))+mass*beta
    # Independent q-side fixed mass matrix catches inconsistent symbol mutation.
    hq=sum((q[j]*alpha[j] for j in range(3)),s.zeros(4))+mass*kron(Z,s.eye(2))
    P=(s.eye(4)+hp/ep)/2;Q=(s.eye(4)-hq/eq)/2
    overlap=s.simplify(s.trace(P*Q));expected=1-(p.dot(q)+mass**2)/(ep*eq)
    check(equal(overlap,expected),'independent Dirac trace overlap')
    flavor=X if fault=='flavor_axis' else Y
    rotation=-I*flavor
    check(equal(rotation,s.Matrix([[0,-1],[1,0]])),'real signed flavor swap')
    # Support agreement plus exact worst-case tail, not a discretized PDE certificate.
    U=s.diag(1,1,-1,-1);U0=s.eye(4);phi=s.Matrix([s.Rational(3,5),0,s.Rational(4,5),0])
    if fault=='plateau': U[0,0]=-1
    inside=s.diag(1,1,0,0);check(equal((U-U0)*inside,s.zeros(4)),'exact supported-data agreement')
    error=(U-U0)*phi;tail=(s.eye(4)-inside)*phi
    check(equal((error.H*error)[0],4*(tail.H*tail)[0]),'sharp factor-two tail bound')
    # Fourier scaling of normalized fixed-area switch and three-dimensional dilation.
    T=s.symbols('T',positive=True);n=s.Integer(3)
    # Actual scaled-switch Fourier integral; polynomial control is not C-infinity.
    u=s.symbols('u',real=True);theta=s.pi/2
    amplitude=6*theta if fault=='switch_area' else 6*theta/T
    fourier=s.integrate(amplitude*u*(1-u)*s.exp(I*u)*T,(u,0,1))
    check(equal(fourier,6*theta*(-1+2*I-(1+2*I)*s.exp(I))),'fixed-area switch Fourier integral')
    power=s.simplify(T**3*(T**(-n))**2)
    check(equal(power,T**(3-2*n)),'same-family Born scaling')
    r=s.symbols('r',positive=True)
    radial=s.integrate(4*s.pi*r*r/(r*r+mass*mass)**3,(r,0,s.oo))
    if fault=='radial_measure': radial=s.integrate(4*s.pi/(r*r+mass*mass)**3,(r,0,s.oo))
    check(equal(radial,s.pi**2/(4*mass**3)),'independent exact massive radial moment')
    flavorcount=s.trace(flavor.H*flavor)
    if fault=='flavor_multiplicity': flavorcount=1
    check(equal(flavorcount,2),'two-species Born multiplicity')
    # Actual Dirac overlap Taylor coefficient, not an assumed aperture exponent.
    eps=s.symbols('eps',real=True);rr,uu,ww,mm=s.symbols('rr uu ww mm',positive=True)
    transverse=0 if fault=='transfer_direction' else eps*uu
    Eq=s.sqrt(rr**2+mm**2);Ep=s.sqrt(transverse**2+(rr+eps*ww)**2+mm**2)
    overlap_eps=1-((rr+eps*ww)*rr+mm**2)/(Ep*Eq)
    coefficient=s.simplify(s.diff(overlap_eps,eps,2).subs(eps,0)/2)
    expected_coefficient=((uu**2+ww**2)/Eq**2-rr**2*ww**2/Eq**4)/2
    check(equal(coefficient,expected_coefficient),'actual aperture Taylor coefficient')
    # A Gaussian moment control: not asserted to be a positive-energy Dirac packet.
    x=s.symbols('x',real=True)
    norm=s.integrate(s.exp(-x*x)/s.sqrt(s.pi),(x,-s.oo,s.oo))
    moment=s.integrate(x*x*s.exp(-x*x)/s.sqrt(s.pi),(x,-s.oo,s.oo))
    check(equal(norm,1) and equal(moment,s.Rational(1,2)),'normalized Gaussian second moment')
    return failures

if __name__=='__main__': run_suite(checks,['mass_sign','flavor_axis','plateau','switch_area','radial_measure','flavor_multiplicity','transfer_direction'])
