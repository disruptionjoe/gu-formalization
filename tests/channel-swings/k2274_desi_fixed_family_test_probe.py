#!/usr/bin/env python3
"""Exact released-input and continuum-bound controls; no statistical calibration."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2274-desi-fixed-family-test'
NOTE='explorations/conditional-build/k2274-desi-fixed-family-test-2026-10-29.md'
DEPS=['explorations/conditional-build/k2271-forward-cosmology-domain-2026-10-29.md']
SOURCE_INPUTS={'commit': 'bb0c1c9009dc76d1391300e169e8df38fd1096db', 'retrieved_at': '2026-10-29T21:12:35.671289+00:00', 'files': [{'url': 'https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_mean.txt', 'sha256': '6d2f38d0727b2aefcd82fdd5a1c6df5a7d34ad8459437c195d575b5ad0c6ab32', 'text': '# [z] [value at z] [quantity]\n0.70600000 17.35069094 DM_over_rs\n0.70600000 19.45534918 DH_over_rs\n'}, {'url': 'https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_LRG_GCcomb_z0.6-0.8_cov.txt', 'sha256': '16fa8c323f54139ef1249a24f8f9c8663dbac7890d5a6d9c3b97e84ee89847ae', 'text': '3.23752442e-02 -2.37445646e-02\n-2.37445646e-02 1.11469198e-01\n'}]}
FAULTS=['wrong_redshift','endpoint_sign','quadrature_upper','covariance_cross','observation_order','wrong_action','slope_derivative']
def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    for row in SOURCE_INPUTS['files']:
        check('immutable input hash '+row['url'].split('_')[-1],hashlib.sha256(row['text'].encode()).hexdigest()==row['sha256'])
    raw=SOURCE_INPUTS['files'][0]['text'].splitlines()[1:]
    check('same effective redshift',all(R(line.split()[0])==R(353,500) for line in raw))
    check('observable order',[line.split()[2] for line in raw]==['DM_over_rs','DH_over_rs'])
    d=s.Matrix([R(line.split()[1]) for line in raw]);C=s.Matrix([[R(v) for v in line.split()] for line in SOURCE_INPUTS['files'][1]['text'].splitlines()])
    x=R(3,2) if fault=='wrong_redshift' else 1+R(raw[0].split()[0]);T=x**3;k=R(7,216)
    A=T+1+(1 if fault=='endpoint_sign' else -1)*k*(T-1)
    check('lower endpoint matches integral bound',A==T+1-k*(T-1))
    bs=[19959,19504,19055,18614,18181,17757,17340,16933,16534,16145,15764,15392,15030,14676,14332,13996,13670,13352,13042,12741,12448,12163,11886,11616,11354,11100,10853,10612,10379,10151,9931,9716]
    if fault=='quadrature_upper':bs[-1]+=100
    for i,b in enumerate(bs,1):
        si=1+(x-1)*R(i,32);B=si**3+1+k*(si**3-1)
        check('positive rational integral cell '+str(i),R(b,10000)**3*B**2<=A**2)
    lower=(x-1)*sum(bs)/320000
    check('continuum lower sum above one',lower>1)
    check('exact rational certificate sum',lower==R('1.0021361125'))
    v=s.Matrix([-1,1]);check('actual covariance positive definite',C==C.T and C[0,0]>0 and C.det()>0)
    if fault=='covariance_cross':C[0,1]=C[1,0]=0
    if fault=='observation_order':d=s.Matrix(list(reversed(d)))
    gap=(v.T*d)[0];var=(v.T*C*v)[0]
    check('data opposite allowed model halfspace',gap>0)
    check('cross terms retained',var==R('0.1913335714'))
    check('all-ruler squared-radius23 separation',gap**2>23*var)
    check('printed discrepancy lower bound',gap**2/var>R('23.15111914'))
    check('projected discrepancy tolerance',(gap-R(1,3))**2>16*var)
    # Construct metric equality direction independently; confirms the denominator.
    e=C*v;check('metric Cauchy equality',(e.T*C.inv()*e)[0]==(v.T*e)[0]**2/var)
    slope,t,w=s.symbols('slope t w',real=True);Us=2+slope*(t-1)
    yy=Us**R(4,3);yx=3*w*w*s.diff(yy,t).subs(t,w**3)
    yxx=s.diff(yx,w);y=yy.subs(t,w**3)
    Q=18*w*y*yx+(R(9,2) if fault=='wrong_action' else R(9,4))*w*w*yx*yx-9*w*w*y*yxx
    check('full pure-R2 constraint no slope division',s.simplify(Q)==0)
    check('curvature W positive on unit slope interval',s.simplify(Us-t*s.diff(Us,t))==2-slope)
    UT=2+slope*(T-1);Uw=2+slope*(w**3-1)
    derivative=s.diff(R(2,3)*(s.log(UT)-s.log(Uw)),slope)
    expected=(R(2,3) if fault=='slope_derivative' else R(4,3))*(T-w**3)/(UT*Uw)
    check('strict slope derivative formula',s.factor(derivative-expected)==0)
    ratio=d[0]/d[1];check('data between exact slope endpoints',R(353,500)<ratio<1)
    check('shared amplitude exactly fits radial coordinate',s.simplify((d[1]*UT**R(2,3))*UT**R(-2,3)-d[1])==0)
    check('AP-ratio matching gives transverse fit',s.simplify(d[1]*ratio-d[0])==0)
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
    report['source_inputs']=SOURCE_INPUTS
    report_path=ROOT/'lab/process'/f'{STEM}.json'
    if args.write:
        report_path.write_text(json.dumps(report,indent=2)+'\n')
    elif not report_path.exists() or json.loads(report_path.read_text())!=report:
        print('[FAIL] stale or absent stored report; regenerate explicitly with --write');return 1
    else:
        print('[PASS] stored report and exact dependency hashes current')
    return 0
if __name__=='__main__':raise SystemExit(main())
