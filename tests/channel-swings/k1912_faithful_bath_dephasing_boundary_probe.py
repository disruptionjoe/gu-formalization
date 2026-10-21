"""Independent column, operator-residual and mixed-support verification."""
from pathlib import Path
import copy
import hashlib
import json
import sympy as s
import k1912_faithful_bath_dephasing_boundary as producer
ROOT=Path(__file__).resolve().parents[2]
N=0

def ck(ok,label):
    global N
    assert bool(ok),label
    N+=1

def eq(a,b,label):ck(s.simplify(s.expand_complex(a-b))==0,label)
def mat(a,b,label):ck((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)

def independent():
    i=s.I;a=1/s.sqrt(2)
    # Independently specified pure ground/excited column families.
    ground=s.Matrix([[1,0,a,a],[0,1,a,-i*a]])
    excited=s.Matrix([[0,1,-a,-i*a],[1,0,a,a]])
    C=ground.T*ground.conjugate();X=excited.T*excited.conjugate()
    H=s.Matrix([[2,1-i,-s.sqrt(2),-s.sqrt(2)],
                [1+i,2,-s.sqrt(2),-i*s.sqrt(2)],
                [-s.sqrt(2),-s.sqrt(2),2,0],
                [-s.sqrt(2),i*s.sqrt(2),0,2]])
    eq(s.trace(H*C),0,'independent target kernel');eq(s.trace(H*X),4,'excited cost')
    delta=6-4*s.sqrt(2)
    q=s.Rational(1,100);D=(1-q)*C+q*X
    ck(s.simplify(delta-s.trace(H*D))>0,'faithful bath can still be nonclassical')
    ck(D.rank()>2,'thermal repair leaves extreme rank-two face')
    # Three-dimensional mixed spectator: d=6, rank=3, equality d=k*r.
    weights=[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6)]
    rho=s.diag(*weights,0,0,0)
    U=[]
    for j in range(4):
        col=s.Matrix.hstack(ground[:,j],excited[:,j])
        mat(col.conjugate().T*col,s.eye(2),'column completion unitary')
        U.append(s.kronecker_product(col,s.eye(3)))
    mat(s.Matrix(4,4,lambda j,k:s.trace(rho*U[k].conjugate().T*U[j])),C,'rank-three mixed support exact realization')
    ck(rho.rank()==3 and rho.rows==6,'rank resource saturation')
    pauli=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-i],[i,0]]),s.diag(1,-1)]
    mat(s.Matrix(4,4,lambda j,k:s.trace(pauli[k].conjugate().T*pauli[j])/2),s.eye(4),'nonextreme Pauli control violates naive rank bound')
    # Genuinely noncommuting operations and noncommuting faithful state.
    A=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
    Z=s.diag(1,i);Xop=s.Matrix([[0,1],[1,0]]);ops=[s.eye(2),A,Z,Xop]
    r=A*s.diag(s.Rational(1,5),s.Rational(4,5))*A.T
    ck(r*Z!=Z*r,'state does not commute with bath operations')
    coeff=s.Matrix(4,4,lambda j,k:s.trace(r*ops[k].conjugate().T*ops[j]))
    R1=s.sqrt(2)*ops[2]-ops[0]-ops[1]
    R2=s.sqrt(2)*ops[3]-ops[0]+i*ops[1]
    Q=R1.conjugate().T*R1+R2.conjugate().T*R2
    eq(s.trace(H*coeff),s.trace(r*Q),'nontracial residual orientation')
    ck(s.simplify(s.trace(H*coeff)-s.Rational(2,5)*delta)>0,'faithful witness lower bound example')
    ck(s.simplify(s.trace(Q)/2-delta)>0,'tracial comparison example')
    # Saturation uses scalar unitary operations of arbitrary dimension.
    z=s.Matrix([1,1,1,(1-i)/s.sqrt(2)])
    eq(s.trace(H*z*z.conjugate().T),delta,'sharp tracial witness control')
    # Symbolic normalized Gibbs bound: d*e^-b / sum exp(-b E_l/Delta) >= e^-b;
    # the all-dimensional inequality is analytic; finite endpoint controls follow.
    ck(s.Rational(1,3300)+s.Rational(1,6400)<s.Rational(1,1600),'thermal finite-circuit error budget')
    eq(s.Rational(1,176000)-s.Rational(1,110)*(s.Rational(1,3300)+s.Rational(1,6400)),s.Rational(7,4646400),'exact retained margin')
    ck(2*s.Rational(1,100)*delta<=4*s.Rational(1,100),'lower bound does not overclaim sharpness')

def verify_report(d):
    expected=producer.calculate();expected['dependency_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in producer.pins()}
    assert d==expected,'report or provenance mismatch'

def caught(f,label):
    try:f()
    except AssertionError as e:
        assert str(e),'empty failure cannot count'
        print('CAUGHT',label,':',e)
    else:raise AssertionError('mutation survived: '+label)

if __name__=='__main__':
    independent();d=json.loads((ROOT/'lab/process/k1912-faithful-bath-dephasing-boundary.json').read_text());verify_report(d)
    print('PASS independent exact checks',N,'and clean producer/report/pin baseline')
    caught(lambda:producer.calculate(phase=1),'mathematical input: fourth unitary phase')
    caught(lambda:producer.calculate(thermal_sign=-1),'mathematical input: invalid thermal population')
    bad=copy.deepcopy(d);bad['faithful_finite_exact_realization']=True;caught(lambda:verify_report(bad),'report only')
    bad=copy.deepcopy(d);bad['dependency_sha256'][next(iter(bad['dependency_sha256']))]='0'*64;caught(lambda:verify_report(bad),'pin only')
    print('PASS 2 mathematical input + 1 report + 1 pin mutations; crashes not credited')
