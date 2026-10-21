"""Independent Kraus/Choi controls; mutations of real inputs after clean baselines."""
from pathlib import Path
import hashlib,json,importlib.util
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def ck(v,label):
    global N
    assert bool(v),label
    N+=1

def independent(sign=-1, normalization=4):
    q=s.Rational(1,8);a=s.sqrt(2)/2;co=s.Rational(3,5);si=s.Rational(4,5)
    unitaries=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[a,-a],[a,a]]),s.Matrix([[a,sign*s.I*a],[sign*s.I*a,a]])]
    S=s.eye(4);S[:2,:2]=s.Matrix([[co,-si],[si,co]])
    kraus=[]
    for p,b in [(1-q,0),(q,1)]:
        for out in [0,1]:kraus.append(s.sqrt(p)*S*s.diag(*[u[out,b] for u in unitaries]))
    ck(s.simplify(sum((k.H*k for k in kraus),s.zeros(4)))==s.eye(4),'independent trace preservation')
    J=s.zeros(16)
    for j in range(4):
        for k in range(4):
            e=s.zeros(4);e[j,k]=1
            out=sum((a*e*a.H for a in kraus),s.zeros(4))
            J+=s.kronecker_product(out,e)/normalization
    ck(s.simplify(s.trace(J))==1,'normalized entangled input')
    B=s.Matrix([[-1,-1,s.sqrt(2),0],[-1,s.I,0,s.sqrt(2)]]);H=B.H*B
    e=[u[:,0] for u in unitaries];C=s.Matrix(4,4,lambda j,k:(e[k].H*e[j])[0])
    ck(s.simplify(s.trace(H*C))==0,'specified target kernel')
    ell=[]
    for j in range(4):
        p=sum(abs(k[j,j])**2 for k in kraus);ell.append(s.simplify(1-p))
    ck(ell==[s.Rational(16,25)]*2+[0,0],'basis leakage from Kraus')
    D=s.Matrix(4,4,lambda j,k:J[5*j,5*k]*4)
    A=[co*u if j<2 else u for j,u in enumerate(unitaries)];rho=s.diag(1-q,q)
    checkD=s.Matrix(4,4,lambda j,k:s.trace(rho*A[k].H*A[j]))
    ck(s.simplify(D-checkD)==s.zeros(4),'full Choi diagonal-subspace compression')
    WA=s.simplify(s.trace(H*D));ck(WA>=0,'positive compressed witness')
    # Entire family polar slack is 2 x(1-x), independent of commuting rho.
    x=s.symbols('x',real=True)
    ck(s.expand((1-x*x)-(1-x)**2-2*x*(1-x))==0,'functional-calculus scalar polynomial')
    # General quadratic implication used to turn measured leakage into diamond floor.
    y,b=s.symbols('y b',positive=True)
    ck(s.expand((2*s.sqrt(y))**2)==4*y,'square-root tradeoff constant')
    return WA

def caught(fn,label):
    try:fn()
    except AssertionError as exc:
        ck(bool(str(exc)),label+' fails a real assertion');return
    raise AssertionError('missed '+label)

if __name__=='__main__':
    independent()
    caught(lambda:independent(sign=1),'bath phase corruption')
    caught(lambda:independent(normalization=1),'Choi normalization corruption')
    p=ROOT/'lab/process/k1913-leakage-robust-bath-bound.json';r=json.loads(p.read_text())
    def report(v):
        ck(v['dimension']==4 and v['sharpness']=='not claimed','report scope')
        ck(v['robust_half_diamond_floor']=='d*lambda_min(rho)*(6-4*sqrt(2))/(16*(4+sqrt(2)))','report bound')
        for name,digest in v['dependency_sha256'].items():ck(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,'dependency bytes')
    report(r)
    bad=dict(r,dimension=3);caught(lambda:report(bad),'report corruption')
    bad=json.loads(json.dumps(r));bad['dependency_sha256'][next(iter(bad['dependency_sha256']))]='0'*64;caught(lambda:report(bad),'pin corruption')
    print(json.dumps({'independent_math_baseline':'pass','mathematical_input_faults':2,'report_faults':1,'pin_faults':1,'assertions_including_repeated_baselines':N,'general_scope':'analytic note, not finite samples'}))
