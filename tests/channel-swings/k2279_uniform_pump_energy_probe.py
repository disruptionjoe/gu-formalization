#!/usr/bin/env python3
"""Exact controls for stated conditional model; universal proofs remain written."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2279-uniform-pump-energy'
NOTE='explorations/conditional-build/k2279-uniform-pump-energy-2026-10-29.md'
DEPS=['explorations/conditional-build/k2278-calibrated-pump-detector-2026-10-29.md', 'explorations/conditional-build/k2273-positive-control-energy-2026-10-29.md', 'explorations/conditional-build/k2276-structured-detector-implementation-2026-10-29.md', 'explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md']
SOURCE_INPUTS=None
FAULTS=['commutator_denominator', 'unweighted_shell', 'row_degree', 'inflated_calibration', 'missing_neutral_cost']

def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    # Construct actual H and normalized commutator, then compare to independent bounds.
    for t in range(1,9):
      basis=[(a,b,k) for a in range(t+1) for b in range(t+1) for k in range(t//2+1) if a+b+2*k==t]
      index={v:i for i,v in enumerate(basis)};H=s.zeros(len(basis))
      for j,(a,b,k) in enumerate(basis):
        dst=(a+1,b+1,k-1)
        if k and dst in index:
          i=index[dst];amp=s.sqrt((a+1)*(b+1)*k);H[i,j]=s.I*amp;H[j,i]=-s.I*amp
      if fault=='row_degree' and t>=4:
        i=index[(1,1,(t-2)//2)] if t%2==0 else index[(1,2,(t-3)//2)]
        candidates=[j for j,v in enumerate(basis) if j!=i and H[i,j]==0 and sum(v[:2])!=sum(basis[i][:2])]
        if candidates:H[i,candidates[0]]=H[candidates[0],i]=1
      L=s.diag(*[a+b+2 for a,b,k in basis]);inverse=s.diag(*[R(1,a+b+(1 if fault=='commutator_denominator' else 2)) for a,b,k in basis])
      C=(L*H-H*L)*inverse
      Q=s.diag(*[a+b+(1 if fault=='unweighted_shell' else 2)*k for a,b,k in basis])
      check('actual charge shell '+str(t),Q*H-H*Q==s.zeros(len(basis)))
      check('actual commutator squared bound shell '+str(t),all(s.simplify(s.conjugate(v)*v)<=R(t,2) for v in C))
      check('actual row and column degree shell '+str(t),all(sum(C[i,j]!=0 for j in range(C.cols))<=2 for i in range(C.rows)) and all(sum(C[i,j]!=0 for i in range(C.rows))<=2 for j in range(C.cols)))
    a=R(44,5);J=10;mu=10**10;u=a/(2*mu)
    exponent=a/2+a*J/(4*mu)+mu*u/(1-u)
    check('Poisson exponential positive domain',0<u<1)
    check('uniform exponent upper',exponent<R(881,100))
    check('exact exponential integer majorant',100000**1000<7000*99119**1000)
    check('field moment limit',9*J*J*7000==6300000)
    check('ideal moment smaller',400*11**4==5856400<6300000)
    # Independent Poisson polynomial identities through four moments.
    m=s.symbols('m',positive=True)
    moments=[s.Integer(1)]
    for order in range(4):moments.append(s.expand(m*(moments[-1]+s.diff(moments[-1],m))))
    k=s.symbols('k');poly=s.Poly((2*k+2)**2,k)
    mean=sum(coef*moments[pow[0]] for pow,coef in poly.terms())
    check('weighted quadratic Poisson mean',s.expand(mean-(4*m*m+12*m+4))==0)
    eps=R(1,10**15) if fault=='inflated_calibration' else R(1,10**17)
    gates=0 if fault=='missing_neutral_cost' else 260100
    bound=R(600,10**14)*(1+eps)+R(440,2**50+1)+2400*R(10,7)*eps+22*1000*eps+gates*eps
    check('complete expensive channel budget',bound<R(1,10**11))
    check('neutral gates actually counted',gates==10*10*51**2)
    check('field energy target',R(6300000,10**11)<R(8,1000)**2)
    check('ten fresh vacua target energy',10*R(64,25)==R(128,5))
    check('pump energy depletion factor two',R(128,5)/2==R(64,5))
    # Trace-small contamination defeats second-moment inference, without asserting dynamics.
    epsilon=R(1,10**6);M=10**10;contaminating=epsilon*M*M
    rho=s.diag(1-epsilon,epsilon);sigma=s.diag(1,0);number=s.diag(0,M)
    measured_distance=sum(abs(v) for v in (rho-sigma).diagonal())/2
    check('trace-close preparation has huge actual moment',measured_distance==epsilon and s.trace(rho*number*number)==contaminating>6300000)
    fourth=s.Poly((2*k+2)**4,k)
    second=sum(coef*moments[pow[0]] for pow,coef in fourth.terms())
    check('positive compensator phase variance',s.expand(second-mean**2-16*(4*m**3+14*m*m+9*m))==0)
    # Sharp energy continuity saturation for a two-point law.
    delta=R(1,100);level=1000;moment=delta*level*level;gain=delta*level
    check('moment continuity equality',gain*gain==moment*delta)
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
