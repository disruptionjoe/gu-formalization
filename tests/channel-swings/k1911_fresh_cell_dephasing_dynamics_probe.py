"""Independent Kraus and finite-circuit replay; assertion-only mutation accounting."""
from pathlib import Path
import copy
import hashlib
import json
import sympy as s
import k1911_fresh_cell_dephasing_dynamics as producer
ROOT=Path(__file__).resolve().parents[2]
N=0

def ck(ok,label):
    global N
    assert bool(ok),label
    N+=1

def eq(a,b,label):ck(s.simplify(s.expand_complex(a-b))==0,label)
def mat(a,b,label):ck((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)

def independent():
    a=1/s.sqrt(2);i=s.I;h=s.Rational(1,5)
    # Diagonal Kraus operators, independently of the producer's bath rotations.
    K=[s.sqrt(1-h)*s.eye(4),s.sqrt(h)*s.diag(1,0,a,a),s.sqrt(h)*s.diag(0,1,a,-i*a)]
    mat(sum((k.conjugate().T*k for k in K),s.zeros(4)),s.eye(4),'Kraus completeness')
    expected=s.Matrix([[1,1-h,1-h+h*a,1-h+h*a],[1-h,1,1-h+h*a,1-h+i*h*a],
                      [1-h+h*a,1-h+h*a,1,1-h+h*(1+i)/2],
                      [1-h+h*a,1-h-i*h*a,1-h+h*(1-i)/2,1]])
    for j in range(4):
        for k in range(4):
            E=s.zeros(4);E[j,k]=1
            mat(sum((z*E*z.conjugate().T for z in K),s.zeros(4)),expected[j,k]*E,'all matrix units')
    # Direct fixed fifteen-step witness, not a sampled exponential or report flag.
    C=(expected-(1-h)*s.ones(4))/h
    step=(1-s.Rational(1,1650))*s.ones(4)+s.Rational(1,1650)*C
    W=s.Matrix([[630,152-159*i,-463-258*i,-319+417*i],
                [152+159*i,133,-339-8*i,54-151*i],
                [-463+258*i,-339+8*i,1015,-213-266*i],
                [-319-417*i,54+151*i,-213+266*i,478]])/1000
    F=step.applyfunc(lambda x:s.expand(x**15))
    witness=s.simplify(s.expand_complex(s.trace(W*F)))
    ck(witness.is_negative is True,'exact finite fifteen-cell witness negative')
    ck(s.simplify(-witness/16-s.Rational(1,5808000)).is_positive is True,'direct witness exceeds conservative margin')
    # Arbitrary scalar channel coefficient composed via explicit two-event convolution.
    c=s.symbols('c',real=True)
    two=(1-h)**2+2*h*(1-h)*c+h*h*c*c
    eq(two,(1-h+h*c)**2,'two-cell convolution')
    for n in [1,2,4,7]:
        probs=[s.binomial(n,k)*h**k*(1-h)**(n-k) for k in range(n+1)]
        eq(sum(probs),1,'probabilities normalize')
        eq(sum(k*p for k,p in enumerate(probs)),n*h,'emitted mean count and energy')
    # General population energy slope from explicit event mean, without reading report.
    p=[s.Rational(1,2),s.Rational(1,4),s.Rational(1,8),s.Rational(1,8)]
    mean=s.Matrix([p[0]+a*(p[2]+p[3]),p[1]+a*p[2]-i*a*p[3]])
    eq(1-(mean.conjugate().T*mean)[0],1-sum(p[j]*C[j,k]*p[k] for j in range(4) for k in range(4)),'nonuniform perturbation slope')

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
    independent();d=json.loads((ROOT/'lab/process/k1911-fresh-cell-dephasing-dynamics.json').read_text());verify_report(d)
    print('PASS independent exact checks',N,'and clean producer/report/pin baseline')
    caught(lambda:producer.calculate(phase=1),'mathematical input: conjugated fourth vector')
    caught(lambda:producer.calculate(event_scale=2),'mathematical input: event amplitude')
    bad=copy.deepcopy(d);bad['cell_dimension']=2;caught(lambda:verify_report(bad),'report only')
    bad=copy.deepcopy(d);bad['dependency_sha256'][next(iter(bad['dependency_sha256']))]='0'*64;caught(lambda:verify_report(bad),'pin only')
    print('PASS 2 mathematical input + 1 report + 1 pin mutations; crashes not credited')
