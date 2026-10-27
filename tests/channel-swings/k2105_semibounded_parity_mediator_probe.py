"""Exact gauge, transmission, coherent instrument and variational controls."""
import sympy as s
I=s.I

def zero(a): return all(s.simplify(v)==0 for v in a)
def check(fault):
    x=s.symbols('x',real=True);g=s.exp(-I*x*x);f=(1+x)*s.exp(-x*x)
    A=(2*x if fault!='gauge_sign' else -2*x)
    p=lambda v:-I*s.diff(v,x)
    direct=g*p(p(s.conjugate(g)*f))
    expanded=p(p(f))+A*p(f)+p(A*f)+(A*A*f if fault!='lost_square' else 0)
    assert s.simplify(direct-expanded)==0,'full covariant square'
    # Full pointer instrument, independent matrix-unit extraction.
    X=s.Matrix([[0,1],[1,0]]);E=s.eye(2);U=s.zeros(8)
    for a in range(4):
        angle=s.pi/2 if fault!='wrong_gate_area' else s.pi/4
        U[2*a:2*a+2,2*a:2*a+2]=s.exp(-I*angle*a.bit_count()*(E-X))
    kraus=[s.Matrix(4,4,lambda a,c:U[2*a+b,2*c]) for b in range(2)]
    P=[s.diag(1,0,0,1),s.diag(0,1,1,0)]
    for a in range(4):
        for c in range(4):
            e=s.zeros(4);e[a,c]=1
            for b in range(2): assert zero(kraus[b]*e*kraus[b].H-P[b]*e*P[b]),'record coherence'
    # Complex W (not selfinverse) prevents a reverse-direction sign error hiding.
    W=s.diag(I,1);q=s.Matrix([1,2]);k=s.Rational(3,2)
    left=W.H*q if fault!='reverse_transmission' else W*q
    assert zero(W*left-q),'right incoming amplitude'
    assert zero(I*k*(W*q)-W*(I*k*q)),'left derivative trace'
    derivative_jump=W if fault!='wrong_contact_derivative' else E
    assert zero(derivative_jump*(I*k*q)-I*k*(W*q)),'both transmission traces'
    # z=-1/2,m=1 gives k=i and kernel exp(-abs(x-y)).
    y=s.symbols('y',positive=True)
    kernel=(s.exp(-y) if fault!='kernel_decay' else s.exp(-2*y))
    assert 2*s.integrate(kernel**2,(y,0,s.oo))==1,'resolvent row norm'
    # Negative energy for square pulse A=2 on [-1,1] with f_R=R^-1/2 exp(-abs(x)/R).
    R=s.Integer(4);kinetic=1/(2*R**2);potential=-2*(1-s.exp(-2/R))
    assert s.simplify(kinetic+potential)<0,'omitting square gives negative trial energy'

FAULTS=['gauge_sign','lost_square','wrong_gate_area','reverse_transmission','wrong_contact_derivative','kernel_decay']


def main():
    check(None)
    print('PASS clean exact baseline')
    for fault in FAULTS:
        try: check(fault)
        except AssertionError as e: print('DETECTED',fault,str(e))
        else: raise AssertionError('undetected changed-data fault: '+fault)
    print('PASS',len(FAULTS),'genuine faults; analytic continuum proofs are separate')

if __name__=='__main__': main()
