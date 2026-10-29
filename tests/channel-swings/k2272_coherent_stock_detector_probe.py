#!/usr/bin/env python3
"""Exact finite controls; universal statements require the linked written proof."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2272-coherent-stock-detector'
NOTE='explorations/conditional-build/k2272-coherent-stock-detector-2026-10-29.md'
DEPS=['explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md', 'explorations/conditional-build/k2270-untruncated-detector-control-2026-10-29.md']

FAULTS=['poisson_recurrence','vacuum_boundary','translation_count','initial_return_count','compiler_threshold','drive_area','phase_source']
def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    mu=s.symbols('mu',positive=True);n=s.symbols('n',integer=True,positive=True)
    cn=s.exp(-mu/2)*mu**(n/2)/s.sqrt(s.factorial(n))
    cm=s.exp(-mu/2)*mu**((n-1)/2)/s.sqrt(s.factorial(n-1))
    recurrence=(s.sqrt(mu/n) if fault=='poisson_recurrence' else s.sqrt(n/mu))*cn
    check('Poisson amplitude shift recurrence',s.simplify(cm-recurrence)==0)
    # Explicit padded shift includes both vacuum boundary and outgoing top row.
    shift_matrix=s.zeros(4)
    for j in range(3):shift_matrix[j+1,j]=1
    if fault=='vacuum_boundary':shift_matrix[0,0]=1
    vec=s.Matrix([s.sqrt(R(1,2)),R(1,2),R(1,2),0]);shifted=shift_matrix*vec
    check('vacuum shift contribution',s.simplify((shifted-vec)[0]**2)==R(1,2))
    check('padded shift preserves supported norm',(shifted.T*shifted)[0]==1)
    z=s.symbols('z',nonnegative=True)
    check('square root inequality factor',s.simplify((z-1)**2-(s.sqrt(z)-1)**2-(s.sqrt(z)-1)**2*((s.sqrt(z)+1)**2-1))==0)
    # Stirling expansion derives raw Poisson moments from factorial moments.
    from sympy.functions.combinatorial.numbers import stirling
    moments={j:sum(stirling(j,k,kind=2)*mu**k for k in range(j+1)) for j in range(5)}
    expected=[1,mu,mu**2+mu,mu**3+3*mu**2+mu,mu**4+6*mu**3+7*mu**2+mu]
    for j in range(5):check(f'Poisson moment {j}',s.expand(moments[j]-expected[j])==0)
    check('Poisson normalized variance',s.expand((moments[2]-2*mu*moments[1]+mu**2)/mu**2)==1/mu)
    G2=sum(s.binomial(2,k)*moments[k] for k in range(3));G4=sum(s.binomial(4,k)*moments[k] for k in range(5))
    check('shifted second moment',s.expand(G2)==mu**2+3*mu+1)
    check('shifted fourth moment',s.expand(G4)==mu**4+10*mu**3+25*mu**2+15*mu+1)
    Q=15999999;Rcut=5183999998;M=10**28;upper=2*M;K=upper+(0 if fault=='compiler_threshold' else Q)
    check('low input fits physical good shell',Rcut>=Q)
    check('highest good total shell fits',K>=upper+Q)
    check('lower Poisson tail Chebyshev condition',2*Rcut<=M)
    check('tail sum bound',R(4,M)+R(1,M)==R(5,M))
    check('sqrt tail strict bound',R(5,M)<R(3,10**14)**2)
    check('sqrt twice tail strict bound',R(10,M)<R(4,10**14)**2)
    check('input tail exact',4*R(1,Q+1)==R(1,2000)**2)
    check('output tail exact',R(2*81*2,Rcut+2)==R(1,4000)**2)
    shift=R(Q+Rcut,10**14);check('coherent shift consumer',shift<R(52,10**6))
    copies=2 if fault=='translation_count' else 4
    check('two controlled translations include both tails',copies*R(4,10**14)==R(16,10**14))
    ret=1 if fault=='initial_return_count' else 2
    check('both initial and target coherent replacement',ret*R(3,10**14)==R(6,10**14))
    total=10*(R(1,2000)+R(1,4000)+shift+4*R(4,10**14))+R(1,5000)+2*R(3,10**14)
    check('ten-call full error budget',total<R(8221,10**6))
    t,T=s.symbols('t T',positive=True);u=(1 if fault=='drive_area' else 2)*s.sqrt(mu)/T*s.sin(s.pi*t/T)**2
    check('preparation pulse area',s.simplify(s.integrate(u,(t,0,T))-s.sqrt(mu))==0)
    check('preparation pulse squared area',s.simplify(s.integrate(u*u,(t,0,T))-3*mu/(2*T))==0)
    check('preparation endpoints zero',u.subs(t,0)==0 and s.simplify(u.subs(t,T))==0)
    # Actual truncated vacuum drive has a nonzero [N,H]; diagonal control cannot prepare it.
    number=s.diag(0,1);ann=s.Matrix([[0,1],[0,0]]);drive=number if fault=='phase_source' else s.I*(ann.T-ann)
    comm=number*drive-drive*number
    check('supplied drive is genuinely noncovariant',comm!=s.zeros(2))
    check('vacuum receives a charged amplitude',(drive*s.Matrix([1,0]))[1]!=0)
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
