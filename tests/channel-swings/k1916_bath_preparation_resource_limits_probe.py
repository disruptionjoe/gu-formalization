"""Independent rational support/rotation and damping verification; no expert-review claim."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import hashlib,json
import sympy as s
import k1916_bath_preparation_resource_limits as producer
ROOT=Path(__file__).resolve().parents[2]
def independent():
    vals=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
    masses=[sum(vals[i] for i in pair) for pair in combinations(range(4),2)]
    assert max(masses)==Q(4,5),'largest supported spectral probability'
    q=[Q(2,3),Q(1,3),Q(0),Q(0)]
    assert sum(abs(x-y) for x,y in zip(q,vals))/2==Q(1,5),'half l1 distance'
    # Coherent rotation into an excluded higher-energy level preserves entropy,
    # increases energy, and cannot improve the rank-resource optimum.
    O=s.Matrix([[s.Rational(3,5),0,-s.Rational(4,5),0],[0,1,0,0],[s.Rational(4,5),0,s.Rational(3,5),0],[0,0,0,1]])
    rho=s.diag(s.Rational(2,3),s.Rational(1,3),0,0);H=s.diag(0,1,2,3)
    rotated=O*rho*O.T
    assert rotated.eigenvals()==rho.eigenvals(),'rotation preserves entropy spectrum'
    assert s.trace(H*(rotated-rho))==s.Rational(64,75),'coherent orientation energy penalty'
    # Polynomial solution of population ODE under amplitude damping.
    t,gamma,q0=s.symbols('t gamma q0',positive=True)
    p=q0*s.exp(-gamma*t)
    assert s.diff(p,t)==-gamma*p,'exact damping differential equation'
    assert p.subs(t,0)==q0,'initial condition'
    # Full operator matrix, including coherence, from a separate 2x2 formula.
    a=s.Rational(3,5);b=s.Rational(1,5);r=s.Rational(3,5)
    initial=s.Matrix([[a,b],[b,1-a]])
    output=s.Matrix([[a+(1-r*r)*(1-a),r*b],[r*b,r*r*(1-a)]])
    K=s.diag(1,r);remainder=output-K*initial*K
    assert remainder==s.diag(s.Rational(32,125),0),'independent positive jump residual'
    lo=min(initial.eigenvals());bound=lo*r*r
    M=output-bound*s.eye(2)
    assert M[0,0]>=0 and M[1,1]>=0 and M.det()>=0,'noncommuting eigenvalue floor'
    assert s.simplify(sum(s.Rational(x.numerator,x.denominator)*s.log(s.Rational(x.numerator,x.denominator)/s.Rational(y.numerator,y.denominator)) for x,y in zip(q[:2],vals[:2]))-s.log(s.Rational(5,4)))==0,'independent entropy cost'
    # Gram of projectors, independently using squared overlaps rather than columns.
    h=s.Rational(1,2)
    gram=s.Matrix([[1,0,h,h],[0,1,h,h],[h,h,1,h],[h,h,h,1]])
    assert gram.det()>0,'extreme projector independence'
    assert s.kronecker_product(gram,gram).det()==gram.det()**8,'tensor independence'
    assert s.floor(s.Rational(9,4))==2,'collective rank budget'
    return 12

def caught(fn,label):
    try:fn()
    except AssertionError as e:
        assert str(e);print('CAUGHT',label,':',str(e));return
    raise AssertionError('missed '+label)
def report(r):
    assert r['retained_Gibbs_mass']=='4/5','report retained probability'
    assert r['exact_preparation_scope']=='state-resource optimum; no finite-time or total-work claim','scope'
    for p,h in r['dependency_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency bytes'
if __name__=='__main__':
    n=independent();producer.calculate()
    caught(lambda:producer.calculate(normalizer=s.Rational(1)),'mathematical: unnormalized truncated state')
    caught(lambda:producer.calculate(damping_gain=0),'mathematical: omitted jump term')
    r=json.loads((ROOT/'lab/process/k1916-bath-preparation-resource-limits.json').read_text());report(r)
    caught(lambda:report(dict(r,retained_Gibbs_mass='1')),'report corruption')
    bad=json.loads(json.dumps(r));bad['dependency_sha256'][next(iter(bad['dependency_sha256']))]='0'*64
    caught(lambda:report(bad),'pin corruption')
    print(json.dumps({'independent_exact_checks':n,'mathematical_faults':2,'report_faults':1,'pin_faults':1,'general_claims':'analytic spectral and no-jump proofs'}))
