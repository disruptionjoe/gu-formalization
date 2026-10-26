"""K2095 finite/analytic countercontrols, not finite proof of continuum spectrum."""
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
    # Finite box has an excited stationary nonquasifree density; must not infer continuum uniqueness.
    L=s.diag(0,1,2,3);rho=s.diag(s.Rational(1,2),0,0,s.Rational(1,2))
    if fault=='nonstationary_box_state':rho[0,3]=rho[3,0]=s.Rational(1,2)
    check(zero(L*rho-rho*L),'box stationary control')
    n1=s.diag(0,0,1,1);n2=s.diag(0,1,0,1)
    check(s.trace(rho*n1*n2)-s.trace(rho*n1)*s.trace(rho*n2)==s.Rational(1,4),'nonquasifree box mixture')
    # Two atomic energy points: time-average survival retains sum of squared weights.
    weights=[s.Rational(1,3),s.Rational(2,3)]
    if fault=='discard_spectral_atoms':weights=[0,0]
    check(sum(x*x for x in weights)==s.Rational(5,9),'Cesaro atomic weight retention')
    # Absolutely continuous uniform energy shell, exact spectral integral and low-time variance.
    x,t=s.symbols('x t',real=True);d=s.symbols('d',positive=True)
    amp=s.integrate(s.exp(-s.I*x*t),(x,-d,d))/(2*d)
    check(s.simplify(amp.subs(t,s.pi/(2*d))-2/s.pi)==0,'uniform shell Fourier amplitude')
    variance=s.integrate(x*x,(x,-d,d))/(2*d)
    check(s.simplify(variance-d*d/3)==0,'finite shell energy variance')
    T=s.symbols('T',positive=True)
    upper=s.simplify((1/d+s.integrate(1/(d*d*x*x),(x,1/d,T)))/T)
    check(s.simplify(upper-(2/(d*T)-1/(d*d*T*T)))==0,'split-integral envelope for T>=1/d')
    # Discrete approximant demonstrates phase removal and exact fidelity, not a continuum selector.
    phase=s.pi/6
    if fault=='wrong_spectral_phase':phase=s.pi/3
    psi=s.Matrix([1,1])/s.sqrt(2);evolved=s.diag(s.exp(s.I*phase),s.exp(-s.I*phase))*psi
    overlap=s.simplify(s.expand_complex((psi.H*evolved)[0]));check(s.simplify(1-abs(overlap)**2-s.Rational(1,4))==0,'finite-window pure distance')
    # Vacuum/excitation global distance remains1; compact-test limit cannot be extended to I-P0.
    P0=s.diag(1,0,0);exc=s.diag(0,1,0);N=s.eye(3)-P0
    if fault=='drop_excitation_observable':N=P0
    check(s.trace(exc*N)==1,'noncompact-observable conceptual countercontrol')
    check(s.trace(exc*P0)==0,'orthogonality to vacuum')

if __name__=='__main__':
    harness(test,['nonstationary_box_state','discard_spectral_atoms','wrong_spectral_phase','drop_excitation_observable'])
