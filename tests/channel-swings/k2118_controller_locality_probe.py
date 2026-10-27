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

def locality(P=P1,J=Z):
    V=kron(P,J);flip=kron(X,E)
    return V,flip*V-V*flip
V,C=locality()
assert not zero(C)
assert zero(C.H*C-s.eye(4))
W=kron(E,Z/2)
assert zero((V-W).H*(V-W)-s.eye(4)/4)

def commutant_check(wrong_field=False):
    # All matrix units of localized controller must commute with genuinely remote W.
    W=kron(P1 if wrong_field else E,Z)
    for a in range(2):
        for b in range(2):
            M=s.zeros(2);M[a,b]=1
            assert zero(kron(M,E)*W-W*kron(M,E))
commutant_check()

def density_check(noncommute=False):
    a=kron(P1,Z,E);b=kron(X if noncommute else P1,E,Z)
    assert zero(a*b-b*a)
    # Controller conjugate in A still fails locality against h_B.
    f=kron(X,E,E)
    assert not zero(f*b-b*f)
density_check()

def signal(theta,delete_control=False):
    U=kron(P0,E)+kron(P1,s.diag(s.exp(-I*theta),s.exp(I*theta)))
    if delete_control:U=s.eye(4)
    def remote(c):
        out=pure(U*kron(c,plus))
        return out[:2,:2]+out[2:,2:]
    return td(remote(ket0),remote(s.Matrix([0,1])))
assert signal(s.pi/2)==1
assert signal(s.pi)==0
assert signal(s.pi/6)==s.Rational(1,2)

def signal_check(delete=False):assert signal(s.pi/2,delete)==1
signal_check()

def repair(shared=False):
    # Four factors cA,systemA,cB,systemB. Local controls must commute with remote full controller.
    H_A=kron(P1,Z,E,E)
    H_B=kron(P1,E,E,Z) if shared else kron(E,E,P1,Z)
    X_A=kron(X,E,E,E)
    assert zero(X_A*H_B-H_B*X_A)
    assert zero(H_A*H_B-H_B*H_A)
repair()

def distance_check(center= s.Rational(1,2)):
    V,_=locality();D=V-kron(E,center*Z)
    op=max(abs(e) for e in D.eigenvals())
    assert op==s.Rational(1,2)
distance_check()

def causal_parity_check(omit_far=False):
    # Two bit assignments identical on collector's past cone, distinct required parity.
    a=[1,1,1];b=[1,1,-1]
    collect=lambda bits: s.prod(bits[:-1] if omit_far else bits)
    assert collect(a)!=collect(b)
causal_parity_check()
faults=[
 expect_rejection('hide controller dependence in remote observable',lambda:commutant_check(True)),
 expect_rejection('noncommuting spacelike density controller',lambda:density_check(True)),
 expect_rejection('erase controlled signal',lambda:signal_check(True)),
 expect_rejection('reuse shared controller as distributed repair',lambda:repair(True)),
 expect_rejection('wrong commutant approximant',lambda:distance_check(0)),
 expect_rejection('omit causally unavailable parity bit',lambda:causal_parity_check(True))]
print('PASS K2118 clean baselines and',len(faults),'genuine faults:', '; '.join(faults))
