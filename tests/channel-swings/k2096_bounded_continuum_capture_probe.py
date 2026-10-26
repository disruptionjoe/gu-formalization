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

def test(fault):
    # Exact unitary cascade, memory first and three distinct temporal bins.
    pairs=[(s.Rational(3,5),s.Rational(4,5)),(s.Rational(5,13),s.Rational(12,13)),(s.Rational(8,17),s.Rational(15,17))]
    U=s.eye(4)
    for j,(c,a) in enumerate(pairs,1):
        B=s.eye(4);B[0,0]=B[j,j]=c;B[0,j]=-a;B[j,0]=a
        if fault=='wrong_hopping_sign' and j==2:B[j,0]=-a
        U=B*U
    check(zero(U.T*U-s.eye(4)),'causal cascade unitary')
    A=s.prod(c for c,a in pairs);eta=1-A*A
    f=-s.Matrix(list(U[0,1:]))/s.sqrt(eta)
    if fault=='reverse_capture_weights':f=s.Matrix(list(reversed(f)))
    h=s.Matrix(list(U[1:,0]))/s.sqrt(eta)
    check(s.simplify((f.T*f)[0]-1)==0,'matched input norm')
    check(zero(U*s.Matrix([0,*f])-s.Matrix([-s.sqrt(eta),*(A*h)])),'matched two-column reduction')
    check(zero(U*s.Matrix([1,0,0,0])-s.Matrix([A,*(s.sqrt(eta)*h)])),'release column')
    # Pointwise energy balance is a polynomial identity for arbitrary real inputs.
    z,u,g=s.symbols('z u g',real=True)
    damping=s.Rational(1,2) if fault!='wrong_damping' else s.Rational(1,3)
    check(s.expand(2*z*(-damping*g*g*z-g*u)+(u+g*z)**2-u*u)==0,'continuum balance coefficient')
    # Exact fixed-input regularization, f=sqrt(3)t, F=t^3 on [0,1].
    t=s.symbols('t',positive=True);eps=s.Rational(1,7);F=t**3;f0=s.sqrt(3)*t
    ge=f0/s.sqrt(eps+F);Kt=s.log((eps+F)/eps);K=s.log((eps+1)/eps)
    check(s.simplify(s.diff(Kt,t)-ge**2)==0,'regularized integrated coupling')
    eta0=1/(1+eps)
    if fault=='wrong_efficiency_normalization':eta0=1/(1+2*eps)
    check(s.simplify(ge*s.sqrt((eps+F)/(eps+1))/s.sqrt(eta0)-f0)==0,'prescribed input unchanged')
    check(s.simplify(s.exp(-K)+eta0-1)==0,'probability budget')
    gr=f0/s.sqrt(eps+1-F);Kr=s.log((eps+1)/(eps+1-F))
    check(s.simplify(s.diff(Kr,t)-gr**2)==0,'release integrated coupling')
    check(s.simplify(gr*s.sqrt((eps+1-F)/(eps+1))/s.sqrt(1/(1+eps))-f0)==0,'prescribed output unchanged')
if __name__=='__main__':harness(test,['wrong_hopping_sign','reverse_capture_weights','wrong_damping','wrong_efficiency_normalization'])
