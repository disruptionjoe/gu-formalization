"""Exact finite controls; not a proof of continuum or universal theorems."""
import sympy as s
I=s.I
Z=s.diag(1,-1); X=s.Matrix([[0,1],[1,0]]); E=s.eye(2)
P0=s.diag(1,0); P1=s.diag(0,1)
ket0=s.Matrix([1,0]); plus=s.Matrix([1,1])/s.sqrt(2)
kron=s.kronecker_product

def zero(M): return all(s.simplify(x)==0 for x in M)
def td(A,B):
    D=(A-B).applyfunc(lambda x:s.simplify(s.expand_complex(x)))
    return s.simplify(sum(abs(e)*m for e,m in D.eigenvals().items())/2)
def pure(v): return v*v.H

def expect_rejection(label,fn):
    try: fn()
    except AssertionError: return label
    raise AssertionError('UNDETECTED genuine fault: '+label)

def control(U,identity_branch=1):
    return identity_branch*kron(P0,s.eye(U.rows))+kron(P1,U)
def phase_case(phi,correction_sign=-1):
    # Two-mode Fock code via actual ordered creation operators; second mode reflected.
    a=kron(s.Matrix([[0,1],[0,0]]),E)
    b=kron(Z,s.Matrix([[0,1],[0,0]]))
    N=b.H*b
    R=s.eye(4)-2*N
    U=s.exp(I*phi)*R
    Ucal=s.exp(correction_sign*I*phi)*U
    return R,U,Ucal

def phase_controls(sign=-1):
    R,U,C=phase_case(s.pi/2,sign)
    assert zero(C-R)
    assert zero(R.H*R-s.eye(4))
    assert zero(control(C)-control(R))
    # Global phase is invisible on EVERY matrix unit of the unconditioned channel.
    for i in range(4):
        for j in range(4):
            M=s.zeros(4);M[i,j]=1
            assert zero(U*M*U.H-R*M*R.H)
phase_controls()
R,U,C=phase_case(s.pi)
v=kron(plus,s.Matrix([1,0,0,0]))
assert td(pure(control(U)*v),pure(control(R)*v))==1

def calibrated_factory(drop_zero=False):
    R,U,C=phase_case(s.pi/2)
    W=control(C,0 if drop_zero else 1)
    assert zero(W.H*W-s.eye(8))
calibrated_factory()

def noise(rho,weights,phases,erase_phase=False):
    ans=s.zeros(rho.rows)
    for w,p in zip(weights,phases):
        D=s.diag(1,1 if erase_phase else s.exp(I*p));ans+=w*D*rho*D.H
    return s.simplify(ans)

def noise_controls(erase=False):
    rho=pure(plus)
    got=noise(rho,[s.Rational(3,4),s.Rational(1,4)],[0,s.pi],erase)
    assert td(got,rho)==s.Rational(1,4)
    assert td(noise(rho,[s.Rational(1,2)]*2,[0,s.pi],erase),rho)==s.Rational(1,2)
noise_controls()

def vacuum_lift_controls(identify_lifts=False):
    R,U,C=phase_case(s.pi)
    actual=control(R if identify_lifts else U)
    assert td(pure(actual*v),pure(control(R)*v))==1
vacuum_lift_controls()

def invariant_code_controls(mix=False):
    # A code frame is an actual embedding. Mixing flavor breaks the claimed invariant code.
    W=s.Matrix([[1],[0]]) if not mix else plus
    Ref=Z
    residual=Ref*W-W*(W.H*Ref*W)
    assert zero(residual)
invariant_code_controls()

def reference_noise_controls(correlate=False):
    bell=s.Matrix([1,0,0,1])/s.sqrt(2)
    D=kron(Z,Z if correlate else E)
    out=(pure(bell)+pure(D*bell))/2
    assert td(out,pure(bell))==s.Rational(1,2)
reference_noise_controls()
def complex_visibility_check(reverse=False):
    angle=-s.pi/2 if reverse else s.pi/2
    got=noise(pure(plus),[s.Rational(1,2)]*2,[0,angle])
    assert s.simplify(got[0,1]-(1-I)/4)==0
    assert td(got,pure(plus))==s.sqrt(2)/4
complex_visibility_check()

def exterior_check(reverse_pair=False):
    a=kron(s.Matrix([[0,1],[0,0]]),E)
    b=kron(Z,s.Matrix([[0,1],[0,0]]))
    vacuum=s.Matrix([1,0,0,0])
    # Ordered input basis is vacuum,b*vacuum,a*vacuum,a*b*vacuum.
    # One-particle X interchanges creators; the pair order must follow substitution.
    pair=(a.H*b.H if reverse_pair else b.H*a.H)*vacuum
    U=s.Matrix.hstack(vacuum,a.H*vacuum,b.H*vacuum,pair)
    assert zero(U*a.H-b.H*U)
    assert zero(U*b.H-a.H*U)
    assert zero(U*vacuum-vacuum)
    assert zero(U*(a.H*b.H*vacuum)+a.H*b.H*vacuum)
    assert zero(U*U-s.eye(4))
exterior_check()
faults=[
 expect_rejection('conjugate complex phase visibility',lambda:complex_visibility_check(True)),
 expect_rejection('reverse exterior pair order',lambda:exterior_check(True)),
 expect_rejection('wrong physical phase correction',lambda:phase_controls(1)),
 expect_rejection('missing identity control branch',lambda:calibrated_factory(True)),
 expect_rejection('erase stochastic branch phases',lambda:noise_controls(True)),
 expect_rejection('identify distinct controlled lifts',lambda:vacuum_lift_controls(True)),
 expect_rejection('noninvariant flavor code',lambda:invariant_code_controls(True)),
 expect_rejection('phase correlated with reference',lambda:reference_noise_controls(True))]
print('PASS K2117 clean baselines and',len(faults),'genuine faults:', '; '.join(faults))
