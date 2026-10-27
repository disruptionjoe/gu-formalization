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

from itertools import product
n=3;d=8
local=[kron(Z,E,E),kron(E,Z,E),kron(E,E,Z)]
R=local[0]*local[1]*local[2]
psi=s.zeros(d,1);psi[0]=psi[7]=1/s.sqrt(2)
rho=pure(psi)
bits=list(product((0,1),repeat=n));labels=list(product((1,-1),repeat=n))

def resource(p,z,leak=False):
    out=s.zeros(8);out[0,0]=p;out[7,7]=1-p;out[0,7]=z;out[7,0]=s.conjugate(z)
    if leak:out=(out+s.eye(8)/8)/2
    return out

def actual(tau,rho,omit_gate=False,wrong_readout=False,wrong_parity=False):
    # Contract the actual cat density through local controlled reflections and X bras.
    U=[]
    for b in bits:
        u=s.eye(d)
        for j,v in enumerate(b):
            if v and not(omit_gate and j==0):u=local[j]*u
        U.append(u)
    out={1:s.zeros(d),-1:s.zeros(d)}
    fine={}
    nonzero=[(a,b,tau[a,b]) for a in range(8) for b in range(8) if tau[a,b]!=0]
    for x in labels:
        amp=[s.prod(x[j]**b[j] for j in range(n))/s.sqrt(8) for b in bits]
        if wrong_readout:amp=[int(all(x[j]==(1 if b[j]==0 else -1) for j in range(n))) for b in bits]
        q=s.prod(x[:2] if wrong_parity else x)
        M=s.zeros(d)
        for a,b,val in nonzero:M+=amp[a]*s.conjugate(amp[b])*val*U[a]*rho*U[b].H
        fine[x]=s.simplify(M);out[q]+=M
    return {q:s.simplify(m) for q,m in out.items()},fine

def expected(p,z,rho):
    return {q:s.simplify((p*rho+(1-p)*R*rho*R+q*(z*rho*R+s.conjugate(z)*R*rho))/2) for q in (1,-1)}

def circuit_check(omit=False,readout=False,parity=False,leak=False,conjugate=False):
    p=s.Rational(3,5);z=(2+I)/5
    tau=resource(p,z,leak)
    want=expected(p,s.conjugate(z) if conjugate else z,rho)
    got,fine=actual(tau,rho,omit,readout,parity)
    for q in (1,-1):assert zero(got[q]-want[q])
    # Unchanged fine maps for equal parity; strict proper subset has no information.
    for x,m in fine.items():assert zero(m-got[s.prod(x)]/4)
    for x0 in (1,-1):assert s.simplify(sum(s.trace(m) for x,m in fine.items() if x[0]==x0))==s.Rational(1,2)
circuit_check()

def exact_distance(p,z):
    got,_=actual(resource(p,z),rho)
    ideal=expected(s.Rational(1,2),s.Rational(1,2),rho)
    return s.simplify(sum(td(got[q],ideal[q]) for q in (1,-1)))
for p,z in [(s.Rational(3,5),(2+I)/5),(s.Rational(1,2),0),(s.Rational(1,2),I/2),(s.Rational(1,2),-s.Rational(1,2)),(1,0)]:
    assert s.simplify(exact_distance(p,z)-s.sqrt((p-s.Rational(1,2))**2+abs(z-s.Rational(1,2))**2))==0

# Dephased resource leaves ideal unread channel while destroying recorded coherence.
got,_=actual(resource(s.Rational(1,2),0),rho)
ideal=expected(s.Rational(1,2),s.Rational(1,2),rho)
assert zero(got[1]+got[-1]-ideal[1]-ideal[-1])
assert exact_distance(s.Rational(1,2),0)==s.Rational(1,2)

def noisy_resource(correlated=False):
    tau=resource(s.Rational(1,2),s.Rational(1,2));r=s.Rational(1,4);out=s.zeros(8)
    for flips in bits:
        weight=s.prod(r if b else 1-r for b in flips)
        if correlated:weight=(r if flips==(1,1,1) else 1-r if flips==(0,0,0) else 0)
        M=kron(*[Z if b else E for b in flips]);out+=weight*M*tau*M.H
    return out

def dephasing_check(correlated=False):
    out=noisy_resource(correlated)
    assert out[0,7]==s.Rational(1,16) # (1/2)*(1-2r)^3
    assert exact_distance(out[0,0],out[0,7])==s.Rational(7,16)
dephasing_check()
faults=[
 expect_rejection('omit one actual local gate',lambda:circuit_check(omit=True)),
 expect_rejection('measure Z instead of X',lambda:circuit_check(readout=True)),
 expect_rejection('omit one record from parity',lambda:circuit_check(parity=True)),
 expect_rejection('unreported resource leakage',lambda:circuit_check(leak=True)),
 expect_rejection('reverse phase-reference convention',lambda:circuit_check(conjugate=True)),
 expect_rejection('replace independent by correlated phase flips',lambda:dephasing_check(True))]
print('PASS K2119 clean baselines and',len(faults),'genuine faults:', '; '.join(faults))
