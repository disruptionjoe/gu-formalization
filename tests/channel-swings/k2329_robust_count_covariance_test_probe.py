#!/usr/bin/env python3
"""Exact finite controls; continuum/tail theorems are proved in the companion note."""
import argparse, copy, hashlib, json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[2]
ST='k2329-robust-count-covariance-test'
BASE=dict(cross=1,dual_error=-1,power_cap=2,shift=s.Rational(1,98),mgf_center=-1,radial_sign=-1,lens_sign=1,tail_factor=2,trace_den=-2,shared=True)
def evaluate(c):
    checks=[]
    def ck(name,ok): checks.append((name,bool(ok)))
    H=s.Matrix([[0,-s.Rational(1,2)],[-s.Rational(1,2),0]]);I=s.eye(2)
    v1=s.Matrix([0,1]);v2=s.Matrix([1,-1]);Ms=[v1*v1.T,v2*v2.T]
    SA=s.Matrix([[1,c['cross']],[c['cross'],2]])
    ck('null dual exact',[s.trace(H*M) for M in Ms]==[0,1])
    ck('actual alternative cross signal',s.trace(H*SA)==-1)
    ck('same diagonal cannot distinguish',SA.diagonal()==sum(Ms,s.zeros(2)).diagonal())
    ck('noise positive and alternative PSD',(I+SA).det()>0 and SA.det()>0)
    ck('Frobenius and operator norms',s.trace(H*H)==s.Rational(1,2) and H**2==I/4)
    # Certified errors use conservative norm_F<=1. The first margin is genuinely negative.
    eps=s.Rational(1,100);cs=[s.trace(H*M)+c['dual_error']*eps for M in Ms]
    L=sum(c['power_cap']*min(x,0) for x in cs)
    ck('uncertainty has adverse sign',cs==[-eps,1-eps])
    ck('bounded-power robust minimum',L==-s.Rational(1,50))
    # PSD witness attaining an adverse interval contribution; a sign reversal is unsafe.
    pert=eps*s.Matrix([[1,1],[1,1]])/2
    ck('interval perturbation trace support',abs(s.trace(H*pert))<=eps and pert.det()==0)
    V=1+2*(1+eps)+2*(2+eps)
    ck('uniform covariance bound',V==s.Rational(176,25) and V<8)
    a=s.Rational(1,50);rr=c['tail_factor']*8*a+8*a*a
    ck('sample consumer exact radius',rr==s.Rational(202,625))
    ck('separation exceeds both tails',s.Rational(49,50)>2*rr)
    rho=c['shift'];K=H+rho*I;tau=s.Rational(49,50)
    ck('trace lower bounds safe',all(s.trace(M)-s.sqrt(2)*eps>=tau for M in Ms))
    ck('shift repairs BOTH interval margins',all(x+rho*tau>=0 for x in cs))
    ck('shift preserves alternative separation',s.trace(K*SA)==-s.Rational(95,98))
    ck('shift norm exact',max(abs(x) for x in K.eigenvals())==s.Rational(25,49))
    denom=1+c['trace_den']*a
    fac=2*s.Rational(25,49)*(a+a*a)/denom
    ck('trace-calibrated threshold factor',fac==s.Rational(17,784))
    # Actual Gaussian polynomial moments, not an assumed fourth-moment flag.
    x,y=s.symbols('x y',real=True);q=x*x-y*y
    def eg(p):
        total=0
        for (i,j),coef in s.Poly(s.expand(p),x,y).terms():
            if i%2==0 and j%2==0:total+=coef*s.factorial2(i-1)*s.factorial2(j-1)
        return s.simplify(total)
    ck('signed quadratic mean/variance',eg(q)==0 and eg(q*q)==4)
    p=s.symbols('p',positive=True)
    ck('unknown amplitude really scales variance',s.simplify(eg(((1+p)*q)**2)-4*(1+p)**2)==0)
    z=s.symbols('z');lam=s.Rational(-3,2)
    logmgf=c['mgf_center']*z*lam-s.log(1-2*z*lam)/2
    ck('Gaussian MGF is centered',s.diff(logmgf,z).subs(z,0)==0)
    ck('MGF variance coefficient',s.diff(logmgf,z,2).subs(z,0)==2*lam**2)
    ck('signed MGF coefficient bound',all(abs(s.expand(s.series(logmgf,z,0,8).removeO()).coeff(z,j))<=2**(j-2)*abs(lam)**j for j in range(2,8)))
    # Full count angular reduction checked on actual P2 polynomial integrals.
    mu,k,r=s.symbols('mu k r',real=True);xx=s.symbols('xx',real=True)
    P2=(3*mu**2-1)/2
    ang=s.integrate(P2*s.exp(s.I*xx*mu),(mu,-1,1),conds='none')
    j2=(3/xx**3-1/xx)*s.sin(xx)-3*s.cos(xx)/xx**2
    ck('normalized quadrupole plane wave',s.simplify(s.expand_complex(ang+2*j2))==0)
    ck('first angular derivative',s.simplify(s.expand_complex(s.diff(ang,xx)+2*s.diff(j2,xx)))==0)
    # mu² is minus second derivative; normalized angular transform divides by -2.
    angular_mu2=-s.diff(ang,xx,2)/(-2)
    ck('radial velocity sign in actual kernel',s.simplify(s.expand_complex(angular_mu2-c['radial_sign']*s.diff(j2,xx,2)))==0)
    ck('spherical harmonic normalization',s.integrate(P2**2,(mu,-1,1))*s.Rational(5,2)==1)
    lap=s.diff((1-mu**2)*s.diff(P2,mu),mu)
    ck('lens actual spherical operator sign',s.simplify(-c['lens_sign']*lap-6*P2)==0)
    # A shared seed has cross covariance; repeated noise on same seed is not IID.
    A=s.Matrix([[1],[2]]);signal=A*A.T
    joint=s.BlockMatrix([[signal+I,signal if c['shared'] else s.zeros(2)],[signal if c['shared'] else s.zeros(2),signal+I]]).as_explicit()
    ck('same-sky repeats retain correlations',joint[:2,2:]==signal)
    # L2 kernel perturbation bound by actual rational outer products.
    b=s.Matrix([1,2]);e=s.Matrix([s.Rational(1,10),-s.Rational(1,5)])
    diff=(b+e)*(b+e).T-b*b.T
    ck('kernel-to-matrix Frobenius bound',s.sqrt(s.trace(diff.T*diff))<=2*s.sqrt((b.T*b)[0])*s.sqrt((e.T*e)[0])+(e.T*e)[0])
    return checks

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks=evaluate(BASE);fail=[n for n,v in checks if not v]
    if fail:raise AssertionError('BASELINE FAIL '+str(fail))
    faults=dict(wrong_cross={'cross':-1},uncertainty_sign={'dual_error':1},missing_power_cap={'power_cap':1},no_dual_repair={'shift':0},uncentered_mgf={'mgf_center':1},radial_sign={'radial_sign':1},lens_sign={'lens_sign':-1},tail_constant={'tail_factor':1},trace_denominator={'trace_den':2},independent_sky_fiction={'shared':False})
    caught={}
    for name,change in faults.items():
        altered=copy.deepcopy(BASE);altered.update(change);bad=[n for n,v in evaluate(altered) if not v]
        if not bad:raise AssertionError('MUTATION ESCAPED '+name)
        caught[name]=bad
    deps=[f'explorations/conditional-build/{ST}-2026-10-30.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2325-relativistic-count-covariance-2026-10-30.md','explorations/conditional-build/k2327-constrained-seed-likelihood-2026-10-30.md']
    out=dict(result_id='K2329',status='PASS',scope='Exact symbolic/rational finite controls; general probability and continuum claims use written proofs. No actual full-count covariance integrals evaluated.',exact_checks=len(checks),numerical_checks=0,checks=[n for n,v in checks],mutations=caught,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
    if args.write:(R/f'lab/process/{ST}.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['result_id','status','exact_checks','numerical_checks']}),'faults',len(caught))
if __name__=='__main__':main()
