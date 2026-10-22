"""Independent exact differential-equation reconstruction of cut certificates."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib
import sympy as sy
import k1942_complete_scalar_energy_duality as p
x=sy.symbols('x')
@lru_cache(None)
def pieces(s):
    output=[]
    for aa,bb in p.INTERVALS:
        a,b=map(sy.Rational,(aa,bb));cuts=sorted({a,b,max(a,min(b,sy.Rational(s)))})
        cs=sy.symbols('c:'+str(2*(len(cuts)-1)));polys=[]
        for i,(l,r) in enumerate(zip(cuts,cuts[1:])):
            f=1 if (l+r)/2<sy.Rational(s) else 0;polys.append(-f*x*x/2+cs[2*i]*x+cs[2*i+1])
        eq=[polys[0].subs(x,a),polys[-1].subs(x,b)]
        for i,z in enumerate(cuts[1:-1]):eq += [(polys[i]-polys[i+1]).subs(x,z),sy.diff(polys[i]-polys[i+1],x).subs(x,z)]
        sol=sy.solve(eq,cs);output += [(l,r,sy.expand(q.subs(sol))) for l,r,q in zip(cuts,cuts[1:],polys)]
    return output

def at(parts,z):return next(q for l,r,q in parts if l<z<r)
def integral(parts):return sum(sy.integrate(q,(x,l,r)) for l,r,q in parts)
def inner(a,b):
    knots=sorted({v for parts in (a,b) for l,r,q in parts for v in (l,r)});total=0
    for l,r in zip(knots,knots[1:]):
        mid=(l+r)/2
        if any(aa<mid<bb for aa,bb in p.INTERVALS):total+=sy.integrate(sy.diff(at(a,mid),x)*sy.diff(at(b,mid),x),(x,l,r))
    return total

def projected(s):
    ps=pieces(s);mu=integral(ps)/sy.Rational(5,6);h=pieces(F(3))
    return [(l,r,sy.expand(q-mu*at(h,(l+r)/2))) for l,r,q in ps]

def check():
    count=0;r=json.loads(p.REPORT.read_text());allcuts=sorted({F(s) for row in r['cut_certificates'] for s in row['cuts']})
    for s in allcuts:
        g=projected(s);assert integral(g)==0,'zero-area actual representer';count+=1
        for t in allcuts:
            assert inner(g,projected(t))==sy.Rational(p.green(s,t)),'independent differential Gram';count+=1
    for row in r['cut_certificates']:
        cuts=list(map(F,row['cuts']));lam=list(map(sy.Rational,row['multipliers']))
        K=sy.Matrix([[inner(projected(s),projected(t)) for t in cuts] for s in cuts]);D=sy.Matrix(list(map(sy.Rational,row['deficits'])));v=sy.Matrix(lam)
        assert all(z>=0 for z in K*v-D) and all(z>=0 for z in v),'finite primal feasibility';count+=1
        assert v.dot(K*v-D)==0 and 4+v.dot(K*v)==sy.Rational(row['energy_lower']),'independent KKT and energy';count+=1
        # Whole-line affine lower certificate at other resource values.
        for M in [F(1,5),F(2,9),F(23,100),F(1,4)]:
            DM=sy.Matrix([sy.Rational(p.deficit(s,M)) for s in cuts]);direct=4+2*v.dot(DM)-v.dot(K*v)
            line=sy.Rational(row['energy_lower'])+sy.Rational(row['slope'])*(sy.Rational(M)-sy.Rational(23,100))
            assert direct==line,'dual supporting affine lower';count+=1
    assert F(r['finite_cut_counterexample']['violation'])>0,'actual missed cut';count+=1
    # Capacity complement and reflection, including unions rather than half-lines.
    for n in range(1,20):
        q=F(n,20);A=[(F(-3),-q),(q,F(3))];B=[(-q,q)]
        assert p.union_capacity(A)==p.union_capacity(B),'complement capacity';count+=1
    return count

def report_check(r):
    assert r['source_sha256']==hashlib.sha256(Path(p.__file__).read_bytes()).hexdigest(),'producer pin'
    assert r==p.calculate(),'report replay'

def detect(fn,label):
    try:fn()
    except AssertionError as e:print('DETECTED',label,':',e);return
    raise AssertionError('undetected '+label)

if __name__=='__main__':
    print('PASS',check(),'independent exact controls')
    r=json.loads(p.REPORT.read_text());report_check(r);print('PASS clean producer/report baseline')
    detect(lambda:p.calculate('projection'),'unprojected Green input')
    detect(lambda:p.calculate('multiplier'),'negative multiplier input')
    from k1940_joint_scalar_amplitude_energy_cuts import verify
    cert=json.loads((p.ROOT/'lab/process/k1940-joint-scalar-amplitude-energy-cuts.json').read_text())['affine_pulse']
    verify(cert);detect(lambda:verify(cert,'flow'),'primal pulse input')
    bad=json.loads(json.dumps(r));bad['cut_certificates'][-1]['energy_lower']='5';detect(lambda:report_check(bad),'report consistency')
    bad=json.loads(json.dumps(r));bad['source_sha256']='0'*64;detect(lambda:report_check(bad),'pin consistency')
