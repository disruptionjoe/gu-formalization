#!/usr/bin/env python3
"""K2151 exact Gaussian-mode and infinite-series algebra controls."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
RESULT='K2151';REPORT='k2151-optimal-local-mode-discrimination.json'
DEPS=['lab/process/k2148-fixed-signal-parity-response.json','lab/process/k2143-local-canonical-parity.json','explorations/conditional-build/k2133-recorded-instrument-vacuum-disturbance-2026-10-27.md']
EVIDENCE='Written two-mode Schmidt decomposition, diagonal-effect optimization and exact infinite-tail sums; finite symbolic controls do not certify continuum controller realization.'
FAULTS=['photon_subtracted','missing_normalization','wrong_threshold','missing_tie','parity_substitution','record_only','energy_link','conditional_energy']
def check(out,name,condition):out[name]=bool(condition)
def controls(fault=None):
    out={};z,t=s.symbols('z t',positive=True);P=(1-z)/(1-z*t);Q=t*(1-z)**2/(1-z*t)**2
    if fault=='photon_subtracted':Q=(1-z)**2/(1-z*t)**2
    if fault=='missing_normalization':Q=Q/(1-z)
    check(out,'distribution_normalization',s.simplify(Q.subs(t,1))==1)
    check(out,'vacuum_occupation_zero_signal',Q.subs(t,0)==0)
    check(out,'photon_added_generating_derivative',s.simplify(Q-t*(1-z)*s.diff(t*P,t))==0)
    check(out,'parity_recovery',s.simplify(Q.subs(t,-1)+(1-z)**2/(1+z)**2)==0)
    # Coefficients from normalized two-mode inverse; exact finite n witnesses.
    for n in range(1,5):
        schmidt=s.sqrt(1-z)*z**s.Rational(n-1,2)
        amplitude=s.sqrt(n)*(s.sqrt(1-z)**-1*schmidt-s.sqrt(z)/s.sqrt(1-z)*s.sqrt(1-z)*z**s.Rational(n,2))
        desired=s.diff(Q,t,n).subs(t,0)/s.factorial(n)
        check(out,f'schmidt_inverse_n{n}',s.simplify(amplitude**2-desired)==0)
    for k in [1,2,3,5]:
        lowP=sum((1-z)*z**n for n in range(k));lowQ=sum(s.diff(Q,t,n).subs(t,0)/s.factorial(n) for n in range(k))
        tail=z**(k-1)*(k-(k-1)*z)
        check(out,f'tail_k{k}',s.simplify(1-lowP-z**k)==0 and s.simplify(1-lowQ-tail)==0)
    r=s.Rational(1,4);N=r/(1-r);k=int(s.floor(N))+1+(1 if fault=='wrong_threshold' else 0)
    alpha=r**k;eta=r**(k-1)*(k-(k-1)*r)
    if fault=='parity_substitution':alpha=r/(1+r);eta=(1+((1-r)/(1+r))**2)/2
    check(out,'inherited_exact_optimum',alpha==s.Rational(1,4) and eta==1 and (alpha+1-eta)/2==s.Rational(1,8))
    r=s.Rational(2,3);n=2;likelihood=n*(1-r)/r+(1 if fault=='missing_tie' else 0)
    check(out,'integer_N_tie',likelihood==1)
    u=s.Rational(2,5);k=2;r=s.Rational(1,4)
    al=r**(k+1)+u*(1-r)*r**k;et=r**k*(k+1-k*r)+u*k*(1-r)**2*r**(k-1)
    check(out,'randomized_ROC',al==(1-u)*r**(k+1)+u*r**k and et==(1-u)*r**k*(k+1-k*r)+u*r**(k-1)*(k-(k-1)*r))
    # Actual record-block trace norm for a projector on a pure vacuum purification.
    a=s.Rational(1,4);vec=s.Matrix([s.sqrt(1-a),s.sqrt(a)]);rho=vec*vec.T;proj=s.diag(0,1);no=s.eye(2)-proj;D=no*rho*no-rho
    full=(sum(abs(ev)*mult for ev,mult in D.eigenvals().items())+a)/2
    claimed=a if fault=='record_only' else (s.sqrt(4*a-3*a*a)+a)/2
    check(out,'full_record_disturbance',s.simplify(full-claimed)==0)
    W=s.diag(1,9,4);f=s.Matrix([1,1,0])/s.sqrt(2);nu=3;xp=(s.sqrt(nu)*W**s.Rational(-1,2)+W**s.Rational(1,2)/s.sqrt(nu))*f/2;yp=(s.sqrt(nu)*W**s.Rational(-1,2)-W**s.Rational(1,2)/s.sqrt(nu))*f/2
    check(out,'mode_orthogonality',(xp.T*yp)[0]==0)
    check(out,'mode_CCR_and_N',(xp.T*xp)[0]==s.Rational(4,3) and (yp.T*yp)[0]==s.Rational(1,3))
    kk=s.symbols('k',integer=True,positive=True);NN=z/(1-z)
    nb=kk+NN;bc=s.sqrt(z)*(kk+1/(1-z));na=s.simplify((2*NN+1)*nb+NN-2*s.sqrt(z)/(1-z)*bc)
    check(out,'conditional_tail_occupation',na==(0 if fault=='conditional_energy' else kk))
    # Nonselective projection deletes exactly the Schmidt link k-1 <-> k.
    bc_unread=s.sqrt(z)/(1-z)-(1-z)*kk*z**(kk-s.Rational(1,2))
    na_unread=s.simplify((2*NN+1)*NN+NN-2*s.sqrt(z)/(1-z)*bc_unread)
    check(out,'unread_deleted_link',s.simplify(na_unread-(1 if fault=='energy_link' else 2)*kk*z**kk)==0)
    eh=s.simplify((xp.T*W*xp)[0]/(xp.T*xp)[0]);ej=s.simplify((yp.T*W*yp)[0]/(yp.T*yp)[0])
    check(out,'actual_signal_pair_energies',eh==5 and ej==5)
    am=(f.T*W.inv()*f)[0];a1=(f.T*W*f)[0];a2=(f.T*W**2*f)[0]
    check(out,'independent_spectral_energy_sum',s.simplify(eh+ej-(am*a2-a1)/(am*a1-1))==0)
    click=(eh+ej);noclick=s.Rational(1,3)*(eh+ej);unread=s.Rational(1,4)*click+s.Rational(3,4)*noclick
    check(out,'example_output_energy_account',click==10 and noclick==s.Rational(10,3) and unread==5)
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    baseline=controls();bad=[k for k,v in baseline.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for fault in FAULTS:
        result=controls(fault);failed=[k for k,v in result.items() if not v]
        if not failed: raise AssertionError('UNDETECTED '+fault)
        caught[fault]=failed
    report={'result_id':RESULT,'status':'conditional_exact_controls','exact_checks':baseline,'fault_failures':caught,'dependency_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in DEPS},'probe_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'universal_evidence':EVIDENCE}
    if args.write: (ROOT/'lab/process'/REPORT).write_text(json.dumps(report,indent=2)+'\n')
    else:
        assert json.loads((ROOT/'lab/process'/REPORT).read_text())==report, 'stored report differs from current proof controls or dependencies'
    print(json.dumps({'result':RESULT,'exact_checks':len(baseline),'faults_rejected':len(caught),'failures':caught},indent=2))
if __name__=='__main__': main()
