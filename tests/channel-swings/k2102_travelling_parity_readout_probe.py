"""Exact finite gate and characteristic controls; not a continuum proof."""
import sympy as s
I=s.I; X=s.Matrix([[0,1],[1,0]]); eye=s.eye

def zero(a): return all(s.simplify(x)==0 for x in a)
def ket(i,n): return eye(n)[:,i]
def check(fault):
    U=s.zeros(8)
    for a in range(4):
        n=(a//2)+(a%2)
        generator=(eye(2)-X) if fault!='omit_identity' else -X
        angle=s.pi/2 if fault!='wrong_area' else s.pi/4
        block=s.exp(-I*n*angle*generator)
        U[2*a:2*a+2,2*a:2*a+2]=block
    assert zero(U.H*U-eye(8)), 'unitarity'
    # Actual pointer Kraus operators read from unitary, all code matrix units.
    K=[s.Matrix(4,4,lambda a,c:U[2*a+b,2*c]) for b in range(2)]
    P=[s.diag(1,0,0,1),s.diag(0,1,1,0)]
    for a in range(4):
        for c in range(4):
            E=ket(a,4)*ket(c,4).T
            for b in range(2):
                actual=K[b]*E*K[b].H
                if fault=='refined_record': actual=s.diag(*actual.diagonal())
                assert zero(actual-P[b]*E*P[b]), ('full instrument',a,c,b)
    # Zero-extended C1 polynomial control, distinct from the smooth theorem.
    x,q,t=s.symbols('x q t',real=True);v=s.symbols('v',positive=True)
    profile=(1-x*x)**2
    norm=s.integrate(profile,(x,-1,1))
    kappa=s.pi*v*profile/(2*norm)
    assert s.integrate(kappa,(x,-1,1))==s.pi*v/2
    A=s.integrate(kappa/v,(x,q,q+v*t))
    assert s.simplify(s.diff(A,t)-kappa.subs(x,q+v*t))==0
    # Cumulative is clipped outside [-1,1]; verify empty, full and partial paths.
    F=s.integrate(profile,(x,-1,q))/norm
    def cumulative(z):
        if z<=-1:return s.S.Zero
        if z>=1:return s.S.One
        return s.simplify(F.subs(q,z))
    assert cumulative(3)-cumulative(2)==0
    assert cumulative(-2)-cumulative(-3)==0
    assert cumulative(2)-cumulative(-2)==1
    assert cumulative(0)-cumulative(-2)==s.Rational(1,2)
    # Actual bad-trajectory mixture, not a declared error flag.
    p=s.Rational(1,5); psi=(ket(0,4)+ket(1,4))/s.sqrt(2);rho=psi*psi.H
    ideal=s.diag(0,0) # build record blocks explicitly
    ideal=s.diag(P[0]*rho*P[0],P[1]*rho*P[1])
    bad=s.diag(rho,s.zeros(4));mixed=(1-p)*ideal+p*bad
    delta=mixed-ideal
    trace_norm=sum(abs(e)*m for e,m in delta.eigenvals().items())
    assert s.simplify(trace_norm/2-p)<=0
    # Correlated memory-position pure input: sqrt(1-p)|00,g>+sqrt(p)|01,b>.
    # Position trace removes g/b coherence; only bad branch has wrong record.
    good=ket(0,4)*ket(0,4).T;bad_state=ket(1,4)*ket(1,4).T
    correlated_actual=s.diag((1-p)*good+p*bad_state,s.zeros(4))
    correlated_ideal=s.diag((1-p)*good,p*bad_state)
    cd=correlated_actual-correlated_ideal
    assert sum(abs(e)*m for e,m in cd.eigenvals().items())/2==p

FAULTS=['omit_identity','wrong_area','refined_record']


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
