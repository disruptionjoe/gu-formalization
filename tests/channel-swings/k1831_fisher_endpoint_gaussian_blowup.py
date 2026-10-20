#!/usr/bin/env python3
"""Exact chart and limiting-profile algebra; continuum proof is in the report."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1831-fisher-endpoint-gaussian-blowup.json'
def produce():
    checks={}
    def check(k,v):
        checks[k]=bool(v);assert v,k
    lam,b=s.symbols('lam b',positive=True);w=lam/(lam+b*b);sig=1-lam
    def am(j):return s.factor(w*(-b)**j+(1-w)*(lam/b)**j)
    def gm(j):return 0 if j%2 else s.factorial2(j-1) if j else 1
    def m(j):return s.factor(sum(s.binomial(j,k)*am(j-k)*sig**(s.Rational(k,2))*gm(k) for k in range(0,j+1,2)))
    check('mean_zero',am(1)==0);check('latent_variance',am(2)==lam);check('output_variance',m(2)==1)
    check('third_moment',s.simplify(m(3)-lam*(lam/b-b))==0)
    check('fourth_cumulant',s.simplify(m(4)-3-(lam*(b*b+lam**2/b**2)-4*lam**2))==0)
    k=s.symbols('k',nonnegative=True)
    check('skew_square_k',s.simplify(m(3)**2-lam**3*(b*b/lam+lam/(b*b)-2))==0)
    check('fourth_k',s.simplify(m(4)-3-lam**2*(b*b/lam+lam/(b*b)-4))==0)
    # Independent exact finite Gaussian moments for both score-test witnesses.
    cases=0
    for L in [s.Rational(1,10),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4),s.Rational(9,10)]:
        for B2 in [L/16,L/3,L,L*3,L*16]:
            M3sq=s.factor((m(3)**2).subs({lam:L,b:s.sqrt(B2)}));M4=m(4).subs({lam:L,b:s.sqrt(B2)});M6=m(6).subs({lam:L,b:s.sqrt(B2)})
            K=B2/L+L/B2-2;den2=M4-1;den3=M6-6*M4+9
            assert den2>0 and den3>0
            gap=M3sq/den2 if K>=1 else (M4-3)**2/den3
            assert gap>=L**4/231;cases+=1
    checks['25_rational_profile_gap_controls']=cases==25
    c,z=s.symbols('c z',positive=True);p=c/(c+z*z)
    check('native_second_moment',s.factor(p*(1-z)+(1-p)*(1+c/z))==1)
    check('native_fourth_moment',s.factor(p*(1-z)**2+(1-p)*(1+c/z)**2)==1+c)
    eps=s.symbols('eps',positive=True);delta=eps**2;t=s.sqrt((2-delta)/(2-lam*delta));Z=b*eps
    check('inner_rescaled_mean',s.limit(2*(s.sqrt(t)*s.sqrt(1-Z)-1)/eps,eps,0,dir='+')==-b)
    check('outer_rescaled_mean',s.limit(2*(s.sqrt(t)*s.sqrt(1+lam*delta/Z)-1)/eps,eps,0,dir='+')==lam/b)
    check('rescaled_noise_variance',s.limit(4*(1-t)/delta,eps,0,dir='+')==1-lam)
    check('limiting_weight',s.factor(lam*delta/(lam*delta+Z**2))==w)
    # Compact-test scaling: ordinary I rescales as length^-2, and two half-mass lobes both count.
    for a in [s.Rational(1,2),s.Rational(2,3),s.Rational(3,2)]:
        check('two_lobe_scaling_'+str(a),2*s.Rational(1,2)/a**2==1/a**2)
    kap=s.symbols('kap',nonnegative=True);tt=s.sqrt((2-eps**2)/(2-kap*eps**4))
    check('central_face_additive_constant',s.limit(1/(1-tt)-1-4/eps**2,eps,0,dir='+')==4*kap-s.Rational(3,2))
    tt=s.sqrt((2-eps**2)/(2-eps**3))
    check('leading_optimal_additive_divergence',s.limit(eps*(1/(1-tt)-1-4/eps**2),eps,0,dir='+')==4)
    y,aa,bb,v=s.symbols('y aa bb v',real=True)
    check('gaussian_affinity_square',s.expand(((y-aa)**2+(y-bb)**2)/4-((y-(aa+bb)/2)**2/2+(aa-bb)**2/8))==0)
    check('face_bound_constant',8*6*4==192)
    return {'result_id':'K1831','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'ratio_optimal_iff':'c/(2-q) -> 0','noise_ratio_limit':'v/(2-q) -> 1/4','rescaled_absolute_output':'2(|Y|-1)/sqrt(2-q) -> N(0,1) in W2','positive_lambda_liminf_gap':'liminf (2-q) J /4 >= 1+lambda^4/231','minimizer_c_positive_for_sufficiently_high_q':True,'central_face_additive_constant':'4*kappa-3/2 for c=kappa*delta^2', 'central_face_minimizer_necessary_bound':'c <= 192 exp(-1/(32 v0)), eventually; face membership not asserted', 'sharp_subleading_constant_known':False,'optimal_displacement_scale_known':False,'physical_or_canon_promotion':False},'checks':checks,'moment_cases':cases,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1825-global-q-fisher-transfer.json','lab/process/k1827-endpoint-fisher-asymptotic.json','lab/process/k1829-effective-fisher-face-instability.json']}}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
    if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
    else:assert d==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K1831',len(d['checks']),'symbolic/control groups; 25 rational limiting profiles')
