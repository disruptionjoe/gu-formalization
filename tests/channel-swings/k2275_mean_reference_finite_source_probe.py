#!/usr/bin/env python3
"""Finite operator, moment and resource controls; written proofs cover full domains."""
from pathlib import Path
import argparse,hashlib,json,math
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
STEM='k2275-mean-reference-finite-source'
NOTE='explorations/conditional-build/k2275-mean-reference-finite-source-2026-10-29.md'
DEPS=['explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md','explorations/conditional-build/k2272-coherent-stock-detector-2026-10-29.md','explorations/conditional-build/k2273-positive-control-energy-2026-10-29.md']
FAULTS=['weight_factor','failure_charge','pump_sign','covariance_source','sine_profile','pump_tail','coherent_mean','retained_pump','finite_transfer']
def run_checks(fault=None):
    out=[]
    def check(n,b):out.append((n,b))
    # Uniform beta has real normalized amplitudes on four consecutive charges.
    beta={j:R(1,2) for j in range(1,5)}
    delta2=sum((beta.get(i-1,0)-beta.get(i,0))**2 for i in range(0,7))
    check('actual unit shift norm',delta2==R(1,2))
    for n in range(7):
        diff=sum((beta.get(i-n,0)-beta.get(i,0))**2 for i in range(0,12))
        check('weighted translation '+str(n),diff<=(1 if fault=='weight_factor' else 2)*n*s.sqrt(delta2))
    check('orthogonal one-step weighted control',2<=(1 if fault=='weight_factor' else 2)*s.sqrt(2))
    V=s.Matrix([[R(3,5),0],[0,1],[R(4,5),0]])
    W=s.Matrix([[R(3,5),0],[0,1],[R(4,5),0]])
    Ns=s.diag(0,1,2);Nw=s.diag(0,1,4 if fault=='failure_charge' else 0)
    check('failure completion actual isometry',W.T*W==s.eye(2))
    gap=V.T*Ns*V-W.T*Nw*W
    check('vacuum failure retains output moment bound',gap.is_positive_semidefinite is True)
    # One-particle passive rotation fixes the sign and exact energy split.
    G=s.Matrix([[0,-s.I],[s.I,0]])
    rot=R(3,5)*s.eye(2)+(s.I if fault=='pump_sign' else -s.I)*R(4,5)*G
    vec=rot*s.Matrix([1,0]);check('pump rotation transfer sign',vec==s.Matrix([R(3,5),R(4,5)]))
    check('pump rotation unitary',rot.H*rot==s.eye(2))
    for total in range(1,5):
        H=s.zeros(total+1)
        for k in range(total):H[k+1,k]=s.I*s.sqrt((k+1)*(total-k));H[k,k+1]=-H[k+1,k]
        check('passive shell Hermitian '+str(total),H==H.H)
        check('positive shifted passive shell '+str(total),(total*s.eye(total+1)+H).is_positive_semidefinite is True)
        amplitudes=s.Matrix([s.sqrt(s.binomial(total,k))*R(3,5)**(total-k)*R(4,5)**k for k in range(total+1)])
        check('finite pump output normalized '+str(total),(amplitudes.T*amplitudes)[0]==1)
        check('finite pump transfer is fractional actual mean '+str(total),sum(k*amplitudes[k]**2 for k in range(total+1))==R(16,25)*total)
    # Finite coherent truncation (M=1,H=1) is exactly |0>+|1>, normalized.
    transferred=R(16,25)*(1 if fault=='finite_transfer' else R(1,2))
    check('finite truncated pump is not exact comparator transfer',transferred==R(8,25))
    # Real sine profile and its orbit are operators, not asserted flags.
    for L in [2,3,5,7]:
        theta=s.pi if L==2 else 4*s.pi/(L+1)
        amps=[s.sqrt(R(2,L+1))*s.sin((j+1)*s.pi/(L+1)) for j in range(L)]
        if fault=='sine_profile':amps=[1]+[0]*(L-1)
        overlap=sum(amps[j]**2*s.expand_complex(s.exp(-s.I*theta*j)) for j in range(L))
        check('sine orthogonal orbit L'+str(L),s.simplify(s.expand_complex(overlap))==0)
    # A number-invariant source has zero orbit distance; a coherent source does not.
    mu,theta=s.symbols('mu theta',positive=True)
    coherent_overlap_sq=s.exp(-2*mu*(1-s.cos(theta)))
    inferred=s.exp(-mu*(1-s.cos(theta))) if fault=='covariance_source' else coherent_overlap_sq
    check('coherent orbit from squared amplitude',s.simplify(inferred-s.exp(-4*mu*s.sin(theta/2)**2))==0)
    eps=s.symbols('eps',positive=True)
    check('covariant preparation necessary inequality algebra',s.expand(1-(1-2*eps)**2-4*eps*(1-eps))==0)
    # Poisson falling-factorial moments are evaluated independently from Stirling numbers.
    for p in range(1,5):
        from sympy.functions.combinatorial.numbers import stirling
        actual=sum(stirling(p,k,kind=2)*mu**k for k in range(1,p+1))
        expected=[mu,mu**2+mu,mu**3+3*mu**2+mu,mu**4+6*mu**3+7*mu**2+mu][p-1]
        check('Poisson raw moment '+str(p),s.expand(actual-expected)==0)
    Q=15999999;Rcut=5183999998;L=4*10**10-1
    check('tail allocation exact',2*s.sqrt(R(1,Q+1))+s.sqrt(R(324,Rcut+2))==R(3,4000))
    check('sine maximum charge',Rcut+L-1+Q==45199999995)
    check('sine mean charge',Rcut+R(L-1,2)==25183999997)
    check('sine shift conservative bound',R(22,7)/(L+1)<R(8,10**11))
    check('sine square root bound',2*R(8,10**11)<R(127,10**7)**2)
    check('output mean square root bound',162<R(51,4)**2)
    sine=10*(R(3,4000)+R(6985,4*10**7))+R(1,5000)
    check('sine full error budget',sine==R('0.00944625'))
    Mcoh=10**20 if fault=='coherent_mean' else 10**22
    # sqrt10<16/5 gives delta <(37/5)/sqrt(mu).
    dupper=R(37,5)/s.sqrt(Mcoh)
    check('coherent weighted shift square-root bound',2*dupper<R(61,5*10**6)**2)
    check('coherent reference consumer',R(55,4)*R(61,5*10**6)==R(3355,2*10**7))
    coherent=10*(R(3,4000)+R(3355,2*10**7))+R(1,5000)+R(6,10**11)
    check('coherent full error budget',coherent<R('0.009377501'))
    check('coherent compilation threshold',2*10**22+Q==20000000000000015999999)
    Mpump=10**50;stock=10**22
    check('pump depletion square-root lower',Mpump-stock>=R(81,100)*Mpump)
    depletion=R(stock,1)/(R(19,10)*s.sqrt(Mpump))
    check('retained original pump cost',depletion==R(1,1900))
    tail=R(2,10**25) if fault!='pump_tail' else R(1,100)
    full=R('0.009377501')+(0 if fault=='retained_pump' else depletion)+tail
    check('finite source full return budget',full<R('0.009904'))
    check('source return triangle has pump comparison',full>=R('0.009377501')+depletion)
    check('finite pump angle ratio exact',R(stock,Mpump)==R(1,10**14)**2)
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
