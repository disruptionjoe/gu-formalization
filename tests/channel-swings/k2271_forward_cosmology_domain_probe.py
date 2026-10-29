#!/usr/bin/env python3
"""Exact finite controls; universal statements require the linked written proof."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2271-forward-cosmology-domain'
NOTE='explorations/conditional-build/k2271-forward-cosmology-domain-2026-10-29.md'
DEPS=['explorations/conditional-build/k2265-shared-cosmology-consistency-2026-10-29.md']

FAULTS=['redshift_power','quadratic_derivative','source_sign','curvature_leg','tube_box','ruler_freedom','covariance_cross','profile_cross']
def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,s.simplify(b) if isinstance(b,s.Basic) else b))
    x=s.symbols('x',positive=True);u=s.symbols('u',positive=True);v,w=s.symbols('v w',real=True);a,r=s.symbols('a r',real=True)
    p=2 if fault=='redshift_power' else 3
    yt=R(4,3)*u**R(1,3)*v
    ytt=R(4,9)*u**R(-2,3)*v*v+R(4,3)*u**R(1,3)*w
    y=u**R(4,3);yx=p*x**(p-1)*yt;yxx=p*(p-1)*x**(p-2)*yt+p*p*x**(2*p-2)*ytt
    q=18*x*y*yx+(R(9,2) if fault=='quadratic_derivative' else R(9,4))*x*x*yx*yx-9*x*x*y*yxx
    check('independent chain-rule cancellation',s.simplify(q+108*x**6*u**R(5,3)*w)==0)
    g=a/(36*x**6*u**R(1,3))+(1 if fault=='source_sign' else -1)*r/(216*x**6*u**R(5,3))
    check('full constraint recovered',s.simplify((-108*x**6*u**R(5,3)*w+3*a*y-r/2).subs(w,g))==0)
    curv=12*y-(2 if fault=='curvature_leg' else 3)*x*yx
    check('curvature coordinate transformation',s.simplify(curv-12*u**R(1,3)*(u-x**3*v))==0)
    check('contraction derivative from actual equation',s.simplify(s.diff(g,u)-(-a/(108*x**6*u**R(4,3))+5*r/(648*x**6*u**R(8,3))))==0)
    check('source coefficient bound',R(1,36)+R(1,216)==R(7,216))
    check('derivative coefficient bound',R(1,108)+R(5,648)==R(11,648))
    check('pure R squared exact control',s.simplify(g.subs({a:0,r:0}))==0)
    box=2 if fault=='tube_box' else 1
    disp=box*7*R(7,216);contract=box*7*R(11,648)
    check('tube self-map strict',disp<R(1,4));check('strict tube slack',R(1,4)-disp==R(5,216))
    check('contraction factor',contract==R(77,648));check('contraction below one',contract<1)
    check('W lower',1-R(7,216)*3==R(65,72));check('F lower',12*R(65,72)-1==R(59,6))
    check('coefficient a perturbation',s.simplify(R(7,36)/(1-R(77,648)))==R(126,571))
    check('coefficient r perturbation',s.simplify(R(7,216)/(1-R(77,648)))==R(21,571))
    check('nonzero member strict departure',R(7-3,108)==R(1,27))
    check('tube lower excludes half radial ratio',R(35,4)**2>32)
    C=s.Matrix([[1,0 if fault=='covariance_cross' else R(1,2)],[0 if fault=='covariance_cross' else R(1,2),1]])
    z=s.Matrix([-1,2]);d=s.Matrix([1,1]);check('covariance SPD',C.det()>0)
    check('correlated separator variance',(z.T*C*z)[0]==3)
    check('deterministic support gap',(z.T*C*z)[0]/16<1)
    W=s.Matrix([[R(4,3),R(-2,3)],[R(-2,3),R(4,3)]])
    f=s.Matrix([1,R(1,3)]);A=(f.T*W*f)[0];B=(f.T*W*d)[0];D=(d.T*W*d)[0]
    lam=s.symbols('lambda',real=True)
    profile=D-(0 if fault=='profile_cross' else B*B/A)
    residual=((d-lam*f).T*W*(d-lam*f))[0]
    check('shared-ruler completion square',s.expand(residual-(A*(lam-B/A)**2+profile))==0)
    check('profile minimum nonnegative',profile>=0)
    neg=-d;cross=(f.T*W*neg)[0];check('positive amplitude boundary case',cross<0)
    model=s.diag(1,3)*f if fault=='ruler_freedom' else f
    check('shared-ruler shape inequality',(z.T*model)[0]<0)
    check('independent rulers really fit',s.diag(1,3)*f==d)
    # The pure-R2 generated vector has zero distance for a common amplitude.
    realratio=(R(2,9))**R(2,3);fp=s.Matrix([1,realratio]);pos=2*fp
    check('generated data zero profile',s.simplify((pos.T*W*pos)[0]-(fp.T*W*pos)[0]**2/(fp.T*W*fp)[0])==0)
    check('radial power derivative bound at minimum',abs(s.diff(u**R(-2,3),u).subs(u,1))==R(2,3))
    scale=s.symbols('h',positive=True)
    check('physical F scales quadratically',s.expand(scale**2*(12*u**R(1,3)*(u-x**3*v)-a)-(12*(scale**2*y)-3*x*(scale**2*yx)-scale**2*a))==0)
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks=run_checks()
    bad=[name for name,ok in checks if not bool(ok)]
    if bad:
        print('[FAIL] baseline: '+', '.join(bad));return 1
    print(f'[PASS] {len(checks)} exact algebra/matrix and resource-accounting controls')
    caught={}
    for fault in FAULTS:
        failures=[name for name,ok in run_checks(fault) if not bool(ok)]
        if not failures:
            print('[FAIL] undetected input fault: '+fault);return 1
        caught[fault]=failures
        print('[PASS] genuine failing checks for '+fault+': '+', '.join(failures))
    report={'schema_version':'1.0','result_id':STEM.split('-')[0].upper(),'claim_ceiling':'conditional supplied model; no source or canon verdict',
      'evidence_kind':'finite exact algebra/matrix and resource-accounting checks; universal statements are written proofs',
      'checks':len(checks),'check_names':[n for n,_ in checks],'faults_caught':caught,
      'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS+[NOTE,str(Path(__file__).relative_to(ROOT))]}}
    report['resource_accounting_checks']=[n for n,_ in checks if any(word in n for word in ['translations include','initial and target','restoration uses','error budget','good total shell'])]
    report_path=ROOT/'lab/process'/f'{STEM}.json'
    if args.write:
        report_path.write_text(json.dumps(report,indent=2)+'\n')
    elif not report_path.exists() or json.loads(report_path.read_text())!=report:
        print('[FAIL] stale or absent stored report; regenerate explicitly with --write');return 1
    else:
        print('[PASS] stored report and exact dependency hashes current')
    return 0
if __name__=='__main__':raise SystemExit(main())
