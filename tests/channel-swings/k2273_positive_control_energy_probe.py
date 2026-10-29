#!/usr/bin/env python3
"""Exact finite controls; universal statements require the linked written proof."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2273-positive-control-energy'
NOTE='explorations/conditional-build/k2273-positive-control-energy-2026-10-29.md'
DEPS=['explorations/conditional-build/k2270-untruncated-detector-control-2026-10-29.md', 'explorations/conditional-build/k2225-positive-drift-detector-control-2026-10-28.md', 'explorations/conditional-build/k2272-coherent-stock-detector-2026-10-29.md']

FAULTS=['noninteger_spectrum','hopping_number','missing_phase','spectator_identity','pulse_area','moment_order','restoration_moment','drift_duration']
def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    theta=-s.pi/2;r=3*s.pi/2
    for n in range(5):
        D=R(n*n,2) if fault=='noninteger_spectrum' else n*n
        check(f'finite Kerr spectral control {n}',s.simplify(s.exp(-s.I*r*D)-s.exp(-s.I*theta*D))==0)
    # Complete charge-one and charge-two shells of genuine bosons.
    for charge in [1,2,3]:
        X=s.zeros(charge+1)
        for j in range(charge):X[j,j+1]=X[j+1,j]=s.sqrt((j+1)*(charge-j))
        N=charge*s.eye(charge+1);coef=R(1,2) if fault=='hopping_number' else 1
        B=coef*N+X
        check(f'positive hopping shell {charge}',all(v>=0 for v in B.eigenvals()))
        check(f'hopping commutes with charge {charge}',N*X==X*N)
    # Charge0 plus charge1 makes the number repair a physically visible relative phase.
    X=s.Matrix([[0,0,0],[0,0,1],[0,1,0]]);N=s.diag(0,1,1);angle=s.pi/2
    first=(-s.I*angle*(N+X)).exp();repair=s.eye(3) if fault=='missing_phase' else (-s.I*3*s.pi/2*N).exp()
    check('phase-corrected full unitary',(repair*first-(-s.I*angle*X).exp()).applyfunc(s.simplify)==s.zeros(3))
    Y=s.Matrix([[0,1,0],[1,0,0],[0,0,0]]);I=s.diag(1,1,0) if fault=='spectator_identity' else s.eye(3)
    target=(-s.I*angle*Y).exp()*s.exp(-s.I*angle)
    check('neutral spectator full identity phase',((-s.I*angle*(I+Y)).exp()-target).applyfunc(s.simplify)==s.zeros(3))
    check('full neutral shifted flip positive',all(v>=0 for v in (s.eye(3)+Y).eigenvals()))
    t,T,area=s.symbols('t T area',positive=True);g=(1 if fault=='pulse_area' else 2)*area/T*s.sin(s.pi*t/T)**2
    check('positive pulse exact area',s.simplify(s.integrate(g,(t,0,T))-area)==0)
    check('positive pulse C1 left',g.subs(t,0)==0 and s.diff(g,t).subs(t,0)==0)
    check('positive pulse C1 right',s.simplify(g.subs(t,T))==0 and s.simplify(s.diff(g,t).subs(t,T))==0)
    check('positive pulse peak',s.simplify(g.subs(t,T/2))==2*area/T)
    check('positive pulse slope',s.simplify(s.diff(g,t).subs(t,T/4))==2*s.pi*area/T**2)
    check('pulse total variation from monotone halves',s.simplify(2*g.subs(t,T/2))==4*area/T)
    omega=s.pi/7;Tnew=1;Tc=2
    repair=2*s.pi-omega*(Tnew+(0 if fault=='drift_duration' else Tc))
    check('repair includes its own drift duration',s.simplify(omega*(Tnew+Tc)+repair)==2*s.pi)
    check('finite peak repair budget',2*repair/Tc<=2*s.pi)
    check('finite slew repair budget',2*s.pi*repair/Tc**2<=s.pi**2)
    delta=R(1,25);M=10;mean=delta*M;moment=delta*M**(1 if fault=='moment_order' else 2)
    check('energy continuity equality is sharp',s.sqrt(moment*delta)==mean)
    check('tiny probability allows fixed mean',R(1,1000000)*1000000==1)
    n=s.symbols('n',positive=True,integer=True);pn=6/(n*(n+1)*(n+2)*(n+3))
    check('tail mass telescoping',s.simplify(pn-2*(1/(n*(n+1)*(n+2))-1/((n+1)*(n+2)*(n+3))))==0)
    check('second moment summable comparison',s.limit(n**2*(n*n*pn),n,s.oo)==6)
    check('fourth moment terms do not vanish',s.limit(n**4*pn,n,s.oo)==6)
    check('tail normalization',R(2,1*2*3)==R(1,3))
    # A coherent donor's second moment, not its mean, controls unbounded restoration.
    mu=R(100);second=mu if fault=='restoration_moment' else mu*mu+mu
    check('restoration uses actual Poisson second moment',second==10100)
    witness=R(64,25)*(1-R(16,25));check('bounded field charge witness',witness==R(576,625))
    lower=(witness-R(2,100))**2/second;check('finite positive restoration floor',lower>0)
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
