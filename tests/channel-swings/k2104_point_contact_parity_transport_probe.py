"""Exact contact/gauge/kernel controls; continuum results are proved in the note."""
import sympy as s
I=s.I;X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
def zero(a): return all(s.simplify(x)==0 for x in a)
def check(fault):
    angle=s.pi/2 if fault!='wrong_jump' else s.pi/4
    U=s.exp(-I*angle*(s.eye(2)-X))
    assert zero(U-X), 'transmission jump'
    # Ordered general jumps: propagator must remove initial cumulative gauge.
    A=s.exp(-I*s.pi*X/4);B=Z
    end=B*A;start=A
    actual=end*start.H
    if fault=='omit_initial_gauge': actual=end
    assert zero(actual-B), 'crossed contacts only'
    # Scalar n=1, X=-1 control of gauge potential sign.
    x=s.symbols('x',real=True);v=s.symbols('v',positive=True)
    alpha=x**3+x;g=s.exp(-2*I*alpha)
    if fault=='wrong_gauge_sign': g=s.conjugate(g)
    potential=I*v*s.diff(g,x)*s.conjugate(g)
    assert s.simplify(potential-2*v*s.diff(alpha,x))==0, 'gauge sign'
    # Actual half-line kernel squared integral; D=1 per coordinate.
    y,eta=s.symbols('y eta',positive=True)
    exponent=2 if fault!='wrong_kernel_decay' else 1
    integral=s.integrate(s.exp(-exponent*eta*y/v)/v**2,(y,0,s.oo))
    assert s.simplify(integral-1/(2*v*eta))==0, 'resolvent kernel normalization'
    # Symmetric polynomial C1 profile exact cumulative at a moving initial point.
    z,e=s.symbols('z e',real=True,positive=True)
    u=s.symbols('u',real=True);norm=s.integrate((1-u*u)**2,(u,-1,1))
    F=s.integrate((1-u*u)**2,(u,-1,z))/norm
    alpha0=s.pi*F.subs(z,-e)/2
    smooth=s.exp(-2*I*(s.pi/2-alpha0))
    assert s.limit(smooth,e,0,dir='+')==-I, 'boundary layer phase'
    diff=s.simplify((-1+I)*(-1-I))
    assert diff==2, 'nonuniform dynamics witness'
    # Periodic cos(x) on half-integer Fourier modes: actual sign crossing.
    V=s.zeros(4)
    for j in range(3): V[j,j+1]=V[j+1,j]=s.Rational(1,2)
    if fault=='positive_band_deleted': V[1,2]=V[2,1]=0
    P=s.diag(0,0,1,1);cross=(s.eye(4)-P)*V*P
    assert cross[1,2]==s.Rational(1,2), 'positive momentum not reducing'
    assert zero(P*s.eye(4)-s.eye(4)*P), 'constant multiplier countercontrol'

FAULTS=['wrong_jump','omit_initial_gauge','wrong_gauge_sign','wrong_kernel_decay','positive_band_deleted']


def main():
    check(None)
    print('PASS clean exact baseline')
    for fault in FAULTS:
        try:
            check(fault)
        except AssertionError as exc:
            print('DETECTED', fault, str(exc))
        else:
            raise AssertionError('undetected actual fault: '+fault)
    print('PASS', len(FAULTS), 'genuine faults rejected; universal claims require written proof')

if __name__ == '__main__':
    main()
