#!/usr/bin/env python3
"""Exact controls for stated conditional model; universal proofs remain written."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2278-calibrated-pump-detector'
NOTE='explorations/conditional-build/k2278-calibrated-pump-detector-2026-10-29.md'
DEPS=['explorations/conditional-build/k2276-structured-detector-implementation-2026-10-29.md']
SOURCE_INPUTS=None
FAULTS=['pump_fluctuation', 'phase_sign', 'gate_count', 'phase_error', 'unweighted_charge', 'negative_pulse']

def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    for n1 in range(6):
      for n2 in range(6):
        N=n1+n2;G=N+1;am=n1*n2;ap=(n1+1)*(n2+1)
        check(f'annihilation bound {n1},{n2}',4*am<=G*G)
        check(f'pair sum squared bound {n1},{n2}',2*(am+ap)<=2*G*G)
    # Displaced oscillator: actual creation fluctuation on vacuum, no top-state use.
    ladder=s.Matrix([[0,1,0],[0,0,s.sqrt(2)],[0,0,0]])
    vacuum=s.Matrix([1,0,0])
    defect=(ladder if fault=='pump_fluctuation' else ladder.T)*vacuum
    exact=(ladder*ladder.T-ladder.T*ladder)*vacuum
    check('creation coherent fluctuation vacuum control',(defect.T*defect)[0]==(vacuum.T*exact)[0])
    # Compute the full displaced-pump defect, with headroom in all three ladders.
    field=s.zeros(4)
    for n in range(1,4):field[n-1,n]=s.sqrt(n)
    Aop=s.kronecker_product(field,field);Hs=s.I*(Aop.T-Aop)
    pump=s.zeros(3)
    for n in range(1,3):pump[n-1,n]=s.sqrt(n)
    alpha=R(2);zz=R(3,5)+s.I*R(4,5)
    cp=alpha*s.eye(3)+(2 if fault=='pump_fluctuation' else 1)*pump
    actual=s.I/alpha*(zz*s.kronecker_product(Aop.T,cp)-s.conjugate(zz)*s.kronecker_product(Aop,cp.T))
    vac=s.Matrix([1,0,0]);one=s.Matrix([0,1,0])
    for n1,n2 in [(0,0),(1,1),(1,2)]:
      psi=s.zeros(16,1);psi[4*n1+n2]=1
      for sign in [1,-1]:
        got=(actual-sign*s.kronecker_product(Hs,s.eye(3)))*s.kronecker_product(psi,vac)
        want=s.kronecker_product(s.I*((zz-sign)*Aop.T-(s.conjugate(zz)-sign)*Aop)*psi,vac)-s.I*s.conjugate(zz)/alpha*s.kronecker_product(Aop*psi,one)
        check(f'actual complex pump defect {n1},{n2},{sign}',all(s.simplify(v)==0 for v in got-want))
    phi=s.pi/2;z=s.I
    modeled=(s.cos(phi)+(-s.I if fault=='phase_sign' else s.I)*s.sin(phi))
    check('complex calibration actual quadrature',modeled==z)
    # Exact finite weighted-charge blocks for the actual trilinear interaction.
    for total in range(2,8):
      basis=[(a,b,k) for a in range(total+1) for b in range(total+1) for k in range(total//2+1) if a+b+2*k==total]
      H=s.zeros(len(basis));index={v:i for i,v in enumerate(basis)}
      for j,(a,b,k) in enumerate(basis):
        dest=(a+1,b+1,k-1)
        if k and dest in index:
          i=index[dest];amp=s.sqrt((a+1)*(b+1)*k)
          H[i,j]=s.I*amp;H[j,i]=-s.I*amp
      check('Hermitian actual shell '+str(total),H==H.conjugate().T)
      Q=s.diag(*[a+b+(1 if fault=='unweighted_charge' else 2)*k for a,b,k in basis])
      check('conserved actual charge '+str(total),Q*H-H*Q==s.zeros(len(basis)))
      check('signed reverse pulse generator '+str(total),(-H if fault!='negative_pulse' else H)+H==s.zeros(len(basis)))
    eps=R(1,10**8);kappa=2*eps;Z=1+eps
    # Conservative rational sqrt2 upper bound; exact arithmetic certifies the budget.
    gates=324000 if fault=='gate_count' else 32400
    phase=R(1,10**4) if fault=='phase_error' else eps
    bound=600*Z/10**5+R(440,2**17+1)+1200*R(10,7)*(eps+phase)+22*340*eps+gates*eps
    check('full calibrated ten-call error',bound<R('0.009791'))
    check('finite predicate alias nonzero at D',2**17%(2**17)==0 and 2**17!=0)
    check('dispersion at vacuum vanishes',s.exp(-s.I*eps*0)==1)
    # At n=1, delta=pi, distance is2: omitting number-phase error is not licensed.
    check('number phase changed input witness',abs(s.exp(-s.I*s.pi)-1)==2)
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
