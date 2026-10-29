#!/usr/bin/env python3
"""Exact controls for stated conditional model; universal proofs remain written."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2277-multibin-pure-r2-test'
NOTE='explorations/conditional-build/k2277-multibin-pure-r2-test-2026-10-29.md'
DEPS=['explorations/conditional-build/k2271-forward-cosmology-domain-2026-10-29.md', 'explorations/conditional-build/k2274-desi-fixed-family-test-2026-10-29.md']
SOURCE_INPUTS={'commit': 'bb0c1c9009dc76d1391300e169e8df38fd1096db', 'retrieved_on': '2026-10-29', 'files': [{'url': 'https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt', 'sha256': '9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585', 'text': '# [z] [value at z] [quantity]\n0.29500000 7.94167639 DV_over_rs\n0.51000000 13.58758434 DM_over_rs\n0.51000000 21.86294686 DH_over_rs\n0.70600000 17.35069094 DM_over_rs\n0.70600000 19.45534918 DH_over_rs\n0.93400000 21.57563956 DM_over_rs\n0.93400000 17.64149464 DH_over_rs\n1.32100000 27.60085612 DM_over_rs\n1.32100000 14.17602155 DH_over_rs\n1.48400000 30.51190063 DM_over_rs\n1.48400000 12.81699964 DH_over_rs\n2.33 8.631545674846294 DH_over_rs\n2.33 38.988973961958784 DM_over_rs\n'}, {'url': 'https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt', 'sha256': '252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509', 'text': '5.78998687e-03 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 2.83473742e-02 -3.26062007e-02 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 -3.26062007e-02 1.83928040e-01 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 3.23752442e-02 -2.37445646e-02 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 -2.37445646e-02 1.11469198e-01 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 2.61732816e-02 -1.12938006e-02 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 -1.12938006e-02 4.04183878e-02 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 1.05336516e-01 -2.90308418e-02 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 -2.90308418e-02 5.04233092e-02 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 5.83020277e-01 -1.95215562e-01 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 -1.95215562e-01 2.68336193e-01 0.00000000e+00 0.00000000e+00\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 1.02136194e-02 -2.31395216e-02\n0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00 -2.31395216e-02 2.82685779e-01\n'}]}
FAULTS=['wrong_cut', 'inflated_covariance', 'drop_covariance', 'wrong_observable', 'right_sum', 'undersized_ceiling', 'wrong_slope_derivative', 'general_coefficients']

def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    for row in SOURCE_INPUTS['files']:check('source bytes '+row['url'].split('/')[-1],hashlib.sha256(row['text'].encode()).hexdigest()==row['sha256'])
    rows=[line.split() for line in SOURCE_INPUTS['files'][0]['text'].splitlines() if line and not line.startswith('#')]
    Cfull=s.Matrix([[R(v) for v in line.split()] for line in SOURCE_INPUTS['files'][1]['text'].splitlines() if line.strip()])
    check('full covariance dimensions',Cfull.rows==len(rows)==Cfull.cols)
    check('full covariance symmetry',Cfull==Cfull.T)
    L,D=Cfull.LDLdecomposition(hermitian=False)
    check('full covariance positive LDL pivots',all(D[i,i]>0 for i in range(D.rows)))
    tags=[(R('0.510'),'DM_over_rs'),(R('0.510'),'DH_over_rs'),(R('0.934'),'DH_over_rs')]
    if fault=='wrong_observable':tags[-1]=(R('0.934'),'DM_over_rs')
    inds=[next(i for i,row in enumerate(rows) if R(row[0])==z and row[2]==tag) for z,tag in tags]
    d=s.Matrix([R(rows[i][1]) for i in inds]);C=Cfull.extract(inds,inds)
    check('selected actual vector',d==s.Matrix([R('13.58758434'),R('21.86294686'),R('17.64149464')]))
    if fault=='inflated_covariance':C*=10
    if fault=='drop_covariance':C[0,1]=C[1,0]=0
    check('negative within-bin cross retained',C[0,1]==R('-.0326062007'))
    x1=R(151,100);x3=R(967,500);cut=R(1,4) if fault=='wrong_cut' else R(3,8)
    def U(x):return 2+cut*(x**3-1)
    A=R(293,500);B=R(96,125);bs=[]
    for i in range(128):
        w=1+(x1-1)*R(i+(fault=='right_sum'),128)
        ratio=10**18*U(x1)**2/U(w)**2;lo=0;hi=10**7
        while lo+1<hi:
            mid=(lo+hi)//2
            if mid**3>=ratio:hi=mid
            else:lo=mid
        b=hi-(1 if fault=='undersized_ceiling' else 0);bs.append(b)
        left=1+(x1-1)*R(i,128)
        check('cell upper inequality '+str(i),b**3*U(left)**2>=10**18*U(x1)**2)
        check('minimal integer ceiling '+str(i),(b-1)**3<ratio)
    check('left-sum certificate digest via sum',sum(bs)==146996588)
    upper=(x1-1)*sum(bs)/(128*10**6)
    check('continuous AP upper bound',upper<A)
    check('radial upper bound',B**3*U(x3)**2>U(x1)**2)
    for name,v in [('low',s.Matrix([1,-A,0])),('high',s.Matrix([0,-B,1]))]:
        g=(v.T*d)[0];V=(v.T*C*v)[0]
        check(name+' gap positive',g>0)
        check(name+' radius4 separation',g*g>4*V)
        check(name+' robust radius4 separation',(g-R(1,20))**2>4*V)
        e=C*v;check(name+' metric support equality',(e.T*C.inv()*e)[0]==(v.T*e)[0]**2/V)
    slope,w=s.symbols('slope w',real=True);u=lambda x:2+slope*(x**3-1)
    k=R(2,3) if fault=='wrong_slope_derivative' else R(4,3)
    check('AP strict monotonic derivative',s.factor(s.diff(R(2,3)*(s.log(u(x1))-s.log(u(w))),slope)-k*(x1**3-w**3)/(u(x1)*u(w)))==0)
    check('radial strict monotonic derivative',s.factor(s.diff(R(2,3)*(s.log(u(x1))-s.log(u(x3))),slope)-R(4,3)*(x1**3-x3**3)/(u(x1)*u(x3)))==0)
    check('negative endpoint positivity boundary',u(R(2)).subs(slope,-R(2,7))==0)
    t0=s.symbols('t0');us=2+slope*(t0-1)
    W=s.expand(us-t0*s.diff(us,t0))
    check('positive-F affine intercept',W==2-slope)
    check('positive-F boundary',W.subs(slope,2)==0)
    t,a,rr,A0,B0,U0=s.symbols('t a rr A0 B0 U0',positive=True)
    ut=A0+B0*t
    residual=216*t*t*ut**R(5,3)*s.diff(ut,t,2)-6*a*ut**R(4,3)+rr
    check('nonconstant affine residual derivative',s.simplify(s.diff(residual,t)+8*a*B0*ut**R(1,3))==0)
    concrete=residual.subs({A0:1,B0:1,t:1,a:1 if fault=='general_coefficients' else 0,rr:0})
    check('pure-R2 affine full constraint',concrete==0)
    check('nonzero coefficient contrary construction',residual.subs({A0:1,B0:1,t:1,a:1,rr:0})!=0)
    check('zero a needs zero r',s.simplify(residual.subs(a,0)-rr)==0)
    constant=216*t*t*U0**R(5,3)*s.diff(U0,t,2)-6*a*U0**R(4,3)+rr
    check('constant branch permits rho relation',s.simplify(constant.subs(rr,6*a*U0**R(4,3)))==0)
    x=s.symbols('x',positive=True);y=(1+x**3)**R(4,3)
    full00=18*x*y*s.diff(y,x)+R(9,4)*x*x*s.diff(y,x)**2-9*x*x*y*s.diff(y,x,2)+3*a*y-rr/2
    check('independent full00 pure-R2 residual',s.simplify(full00.subs({a:0,rr:0}))==0)
    check('independent full00 nonzero coefficient witness',s.simplify(full00.subs({a:1,rr:0,x:1}))!=0)

    check('coordinate tolerance low',(1+A)/40<R(1,20));check('coordinate tolerance high',(1+B)/40<R(1,20))
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
        print('[PASS] genuine failing checks for '+fault+': '+', '.join(failures[:3])+f' ({len(failures)} failed checks)')
    report={'schema_version':'1.0','result_id':STEM.split('-')[0].upper(),'claim_ceiling':'conditional supplied model; no source or canon verdict',
      'evidence_kind':'finite exact algebra/matrix and resource-accounting checks; universal statements are written proofs',
      'checks':len(checks),'check_names':[n for n,_ in checks],'faults_caught':caught,
      'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in DEPS+[NOTE,str(Path(__file__).relative_to(ROOT))]}}
    report['resource_accounting_checks']=[n for n,_ in checks if any(word in n for word in ['budget','ten-call error','gates actually','field moment limit','field energy target','vacua target energy','depletion factor'])]
    if SOURCE_INPUTS: report['source_inputs']=SOURCE_INPUTS
    report_path=ROOT/'lab/process'/f'{STEM}.json'
    if args.write:
        report_path.write_text(json.dumps(report,indent=2)+'\n')
    elif not report_path.exists() or json.loads(report_path.read_text())!=report:
        print('[FAIL] stale or absent stored report; regenerate explicitly with --write');return 1
    else:
        print('[PASS] stored report and exact dependency hashes current')
    return 0
if __name__=='__main__':raise SystemExit(main())
