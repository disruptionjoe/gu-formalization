"""Exact finite/data controls; universal continuum scope rests on the linked proof."""
import sympy as s

def check(value,msg):
    if not bool(value):raise AssertionError(msg)
def zero(M):return all(s.simplify(x)==0 for x in M)
def harness(test,faults):
    test(None);print('PASS clean exact baseline')
    for fault in faults:
        try:test(fault)
        except AssertionError as exc:print('DETECTED',fault,str(exc))
        else:raise AssertionError('undetected fault '+fault)
    print('PASS',len(faults),'genuine state/input/gate faults; no finite proof of continuum scope')

def annihilator(n,j):
    A=s.zeros(2**n)
    for mask in range(2**n):
      if mask&(1<<j):A[mask^(1<<j),mask]=(-1)**sum((mask>>k)&1 for k in range(j))
    return A

def test(fault):
    a0=annihilator(2,0);a1=annihilator(2,1);c=s.Rational(3,5);d=s.Rational(4,5)
    b0=c*a0+d*a1.T;b1=c*a1-d*a0.T
    if fault=='wrong_hole_sign':b1=c*a1+d*a0.T
    check(zero(b0*b1+b1*b0),'physical CAR hole sign')
    check(zero(b0*b0.T+b0.T*b0-s.eye(4)),'physical CAR normalization')
    vac=s.diag(1,0,0,0);particle=s.diag(0,1,0,0);nf=b0.T*b0
    check(s.trace(vac*nf)==d*d,'sea restricted mode occupation')
    check(s.trace(particle*nf)==1,'positive excitation fills physical mode')
    # Genuinely nonquasifree four-excitation superposition; local restriction has no Wick premise.
    q=s.Rational(9,25);rho_local=s.diag(1-q,0,0,q)
    if fault=='replace_with_same_covariance_gaussian':rho_local=s.diag((1-q)**2,q*(1-q),q*(1-q),q*q)
    n0=a0.T*a0;n1=a1.T*a1
    connected=s.trace(rho_local*n0*n1)-s.trace(rho_local*n0)*s.trace(rho_local*n1)
    check(connected==q-q*q,'nonquasifree connected correlation at fixed covariance')
    check(1-rho_local[0,0]==q,'vacuum probability')
    check(s.trace(rho_local*(n0+n1))==2*q,'local excitation expectation')
    # Coherent local vacuum/pair: trace bound must allow square root, not population q.
    psi=s.Matrix([s.Rational(4,5),0,0,s.Rational(3,5)]);D=psi*psi.T-vac
    trdist=sum(abs(ev)*mult for ev,mult in D.eigenvals().items())/2
    if fault=='erase_pair_coherence':D=s.diag(s.Rational(-9,25),0,0,s.Rational(9,25));trdist=sum(abs(ev)*mult for ev,mult in D.eigenvals().items())/2
    check(trdist==s.Rational(3,5),'coherent vacuum fidelity trace distance')
    # Integrate a genuine AC Gamma2 energy density (shift m contributes only phase).
    x=s.symbols('x',nonnegative=True);t=s.symbols('t',real=True)
    density=x*s.exp(-x)
    if fault=='wrong_energy_density':density=s.exp(-x)
    amp=s.integrate(density*s.exp(s.I*t*x),(x,0,s.oo),conds='none')
    check(s.simplify(amp-1/(1-s.I*t)**2)==0,'actual continuous spectral integral')
    check(s.simplify(amp*s.conjugate(amp)-1/(1+t*t)**2)==0,'continuous spectral decay example')
    check(s.limit(1/(1+t*t)**2,t,s.oo)==0,'AC example limit')
    H=s.diag(1,2);atomic=s.diag(0,1)
    if fault=='replace_atomic_eigenstate':atomic=s.ones(2)/2
    check(zero(H*atomic-atomic*H),'atomic stationary countercontrol')
if __name__=='__main__':harness(test,['wrong_hole_sign','replace_with_same_covariance_gaussian','erase_pair_coherence','replace_atomic_eigenstate','wrong_energy_density'])
