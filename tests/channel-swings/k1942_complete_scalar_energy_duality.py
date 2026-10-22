"""Exact projected Green multi-cut certificates; no floating optimizer."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse,hashlib,json
import sympy as sy
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1942-complete-scalar-energy-duality.json'
INTERVALS=[(F(-3),F(-2)),(F(-1),F(1)),(F(2),F(3))]

def clamp(s,a,b):return max(F(0),min(b-a,s-a))
def vint(length,t,q):
    """Integral from0 to q of the Dirichlet inverse of 1_[0,t]."""
    u=min(t,q);ans=(t-t*t/(2*length))*u*u/2-u**3/6
    if q>t:ans+=t*t/(2*length)*(length*(q-t)-(q*q-t*t)/2)
    return ans

def mean(s):return sum(vint(b-a,clamp(s,a,b),b-a) for a,b in INTERVALS)
def green(s,t,project=True):
    raw=sum(vint(b-a,clamp(s,a,b),clamp(t,a,b)) for a,b in INTERVALS)
    return raw-mean(s)*mean(t)/F(5,6) if project else raw

def union_capacity(intervals):
    """Exact capacity of a disjoint rational interval union in [-3,3]."""
    points=sorted({F(-3),F(3),F(6),F(12)}|{x+shift for ab in intervals for x in ab for shift in (0,9)})
    def lengths(z):
        a=sum(max(F(0),min(b,z)-max(l,z-9)) for l,b in intervals)
        ell=max(F(0),min(F(3),z)-max(F(-3),z-9))
        return a,ell-a
    total=F(0)
    for l,r in zip(points,points[1:]):
        al,bl=lengths(l);ar,br=lengths(r);dl=al-bl;dr=ar-br
        if dl*dr<0:
            q=l+(r-l)*dl/(dl-dr);aq,bq=lengths(q)
            total+=(q-l)*(min(al,bl)+min(aq,bq))/2+(r-q)*(min(aq,bq)+min(ar,br))/2
        else:total+=(r-l)*(min(al,bl)+min(ar,br))/2
    return total

def capacity(s):
    # These central halfcuts have |s|<=1 and d=9>=6.
    return (3-abs(s))*(6+abs(s))
def deficit(s,M):return 2-s*s/2-M*capacity(s)/2

def active_solve(cuts,M):
    K=sy.Matrix([[sy.Rational(green(s,t)) for t in cuts] for s in cuts]);D=sy.Matrix([sy.Rational(deficit(s,M)) for s in cuts]);n=len(cuts)
    for k in range(n+1):
        for ids in combinations(range(n),k):
            lam=sy.zeros(n,1)
            if ids:
                A=K.extract(ids,ids)
                if not A.det():continue
                z=A.inv()*D.extract(ids,[0])
                if any(x<0 for x in z):continue
                for i,x in zip(ids,z):lam[i]=x
            if any(x<0 for x in K*lam-D):continue
            val=sy.S(4)+(2*lam.dot(D)-lam.dot(K*lam))
            return K,D,lam,val
    raise AssertionError('no exact finite-cut KKT witness')

def verify(cuts,M,lam,fault=None):
    K=sy.Matrix([[sy.Rational(green(s,t,project=fault!='projection')) for t in cuts] for s in cuts]);D=sy.Matrix([sy.Rational(deficit(s,M)) for s in cuts]);lam=sy.Matrix(lam)
    if fault=='multiplier':lam[0]=-1
    assert all(x>=0 for x in lam),'nonnegative dual multipliers'
    slack=K*lam-D
    assert all(x>=0 for x in slack),'relaxed primal cut feasibility'
    assert lam.dot(slack)==0,'complementarity'
    value=sy.S(4)+2*lam.dot(D)-lam.dot(K*lam)
    assert value==4+lam.dot(K*lam),'primal dual energy equality'
    return value,len(cuts)*2+2

def calculate(fault=None):
    M=F(23,100);families=[[F(-9,20)],[F(-9,20),F(9,20)],list(map(F,['-1/2','-9/20','-2/5','2/5','9/20','1/2'])),list(map(F,['-227/500','-9/20','9/20','227/500']))]
    results=[];count=0;previous=F(4)
    for cuts in families:
        K,D,lam,value=active_solve(cuts,M);got,n=verify(cuts,M,list(lam),fault);count+=n
        assert got==value and value>=previous,'nested lower bounds';previous=value;count+=1
        results.append(dict(cuts=list(map(str,cuts)),gram=[[str(x) for x in K.row(i)] for i in range(len(cuts))],deficits=list(map(str,D)),multipliers=list(map(str,lam)),energy_lower=str(value),slope=str(-sum(lam[i]*sy.Rational(capacity(s)) for i,s in enumerate(cuts)))))
    assert F(results[1]['energy_lower'])>F(results[0]['energy_lower']),'symmetry improves lower bound';count+=1
    # A full-dimensional finite-cut optimum still misses an untested cut.
    c0=[F(-9,20),F(9,20)];_,_,l0,_=active_solve(c0,M);s=F(-227,500)
    violation=deficit(s,M)-sum(F(l0[i])*green(s,t) for i,t in enumerate(c0))
    assert violation>0,'finite-cut optimizer is not globally feasible';count+=1
    for n in range(-20,21):
        s=F(n,20);assert union_capacity([(F(-3),s)])==capacity(s),'actual continuum halfcut capacity';count+=1
    assert union_capacity([(F(-2),F(-1))])==9,'saturated plateau capacity';count+=1
    assert 1-F(1,5)*F(9,2)>0,'zero-Riesz infeasibility at M1/5';count+=1
    # Independently stored exact upper pulse remains a feasible consumer.
    from k1940_joint_scalar_amplitude_energy_cuts import verify as verify_pulse
    cert=json.loads((ROOT/'lab/process/k1940-joint-scalar-amplitude-energy-cuts.json').read_text())['affine_pulse'];count+=verify_pulse(cert)
    U=F(cert['energy']);L=F(results[-1]['energy_lower']);assert L<U;count+=1
    return dict(claim='K1942',evidence_kind='exact finite-cut KKT and reused exact continuum pulse; universal convergence proof in note',exact_controls=count,M=str(M),cut_certificates=results,finite_cut_counterexample={'cut':'-227/500','violation':str(violation)},upper_energy=str(U),phase_derivative_error_squared_bound=str(U-L),phase_uniform_error_squared_bound=str((U-L)/2),dependencies={'pulse_sha256':hashlib.sha256((ROOT/'lab/process/k1940-joint-scalar-amplitude-energy-cuts.json').read_bytes()).hexdigest()},source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
    if a.write:REPORT.write_text(json.dumps(r,indent=2)+'\n')
    print('PASS',r['exact_controls'],'exact controls')
    for c in r['cut_certificates']:print(c['cuts'],c['energy_lower'],float(F(c['energy_lower'])),c['multipliers'])
