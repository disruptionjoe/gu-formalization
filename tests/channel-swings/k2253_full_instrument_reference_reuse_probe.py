#!/usr/bin/env python3
"""Exact finite complex Stinespring completion and physical charge-shell lift."""
import sympy as s
from fractions import Fraction as F
FAULTS=['omit_failure','wrong_failure_norm','reverse_shift','wrong_degenerate_charge','discard_phase','wrong_discarded_row','wrong_squeeze_energy','wrong_reference_range']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    simp=lambda M:M.applyfunc(s.simplify)
    # Nontrivial Fourier-unitary columns: complex amplitudes and a degenerate charge.
    V=s.Matrix(4,3,lambda a,b:s.I**(a*b)/2)
    ck('original_isometry',V.H*V==s.eye(3))
    A=V[:3,:];v=V[3:4,:]
    drow=V[2:3,:] if fault=='wrong_discarded_row' else v
    D=2/s.sqrt(3)*(drow.H*drow)
    if fault=='omit_failure':D=s.zeros(3)
    if fault=='wrong_failure_norm':D=D/2
    W=A.col_join(s.zeros(1,3)).col_join(D)
    ideal=V.col_join(s.zeros(3,3))
    ck('failure_square',simp(D.H*D)==s.eye(3)-A.H*A)
    ck('completed_isometry',simp(W.H*W)==s.eye(3))
    diff=W-ideal
    ck('exact_output_tail_gram',simp(diff.H*diff-2*v.H*v)==s.zeros(3))
    inp=[0,1,1];outq=[0,1,1,3,0,0,0]
    Q=1;R=1;L=3;H=R+L-1+Q
    if fault=='wrong_reference_range':H-=1
    beta=s.zeros(H+1,1)
    for j,x in enumerate([s.Rational(1,2),s.sqrt(2)/2,s.Rational(1,2)]):beta[R+j]=x
    lift=s.zeros(7*(H+1),3*(H+1))
    bad_boundary=False
    for a,n in enumerate(inp):
        if fault=='wrong_degenerate_charge' and a==2:n=2
        for b in range(H+1):
            total=n+b
            if not (R<=total<=H):continue
            for m,q in enumerate(outq):
                if W[m,a]==0:continue
                bb=b+n-q if fault!='reverse_shift' else b-n+q
                if 0<=bb<=H:lift[m*(H+1)+bb,a*(H+1)+b]=W[m,a]
                else:bad_boundary=True
    ck('good_shells_no_lost_amplitude',not bad_boundary)
    good=[a*(H+1)+b for a,n in enumerate(inp) for b in range(H+1) if R<=n+b<=H]
    part=lift[:,good]
    ck('actual_shell_columns_orthonormal',simp(part.H*part)==s.eye(len(good)))
    Nin=s.diag(*[n+b for n in inp for b in range(H+1)])
    Nout=s.diag(*[q+b for q in outq for b in range(H+1)])
    ck('actual_lift_charge_conservation',simp(Nout*lift-lift*Nin)==s.zeros(*lift.shape))
    J=lift*s.kronecker_product(s.eye(3),beta)
    ck('actual_reference_dilation_isometry',simp(J.H*J)==s.eye(3))
    # Independently write every lifted input amplitude, preserving offdiagonal phases.
    direct=s.zeros(*J.shape)
    for a,n in enumerate(inp):
        for m,q in enumerate(outq):
            for b in range(H+1):
                src=b-n+q
                if 0<=src<=H:direct[m*(H+1)+b,a]=W[m,a]*beta[src]
    ck('controlled_translation_factorization',simp(J-direct)==s.zeros(*J.shape))
    # Full field/reference output on a coherent input, not only outcome probabilities.
    psi=s.Matrix([1,s.I,2])/s.sqrt(6);joint=J*psi
    if fault=='discard_phase':joint=joint.applyfunc(lambda z:abs(z))
    ck('full_joint_amplitudes',simp(joint-direct*psi)==s.zeros(*joint.shape))
    ck('joint_norm',s.simplify((joint.H*joint)[0])==1)
    bell=s.zeros(9,1)
    for a in range(3):bell[3*a+a]=1/s.sqrt(3)
    entangled=s.kronecker_product(J,s.eye(3))*bell
    ck('entangled_reference_full_amplitudes',simp(entangled-s.kronecker_product(direct,s.eye(3))*bell)==s.zeros(len(entangled),1))
    refstate=s.Matrix(3,3,lambda a,b:sum(entangled[3*j+a]*s.conjugate(entangled[3*j+b]) for j in range(J.rows)))
    ck('entangled_reference_marginal',simp(refstate)==s.eye(3)/3)
    # No periodic endpoint wrap is used; output reference starts below initial padding when charged output rises.
    ck('physical_reference_dimension',H+1==5)
    ck('degenerate_input_is_retained',inp[1]==inp[2] and s.simplify((J[:,1].H*J[:,2])[0])==0)
    # Bounded target charge distribution and honest consumer, all rational.
    ratio=F(16,25);weight=F(162,625)
    ck('vacuum_distribution_norm',F(337,625)+weight*ratio/(1-ratio)==1)
    ck('vacuum_output_charge',weight*2*ratio/(1-ratio)**2==F(64,25))
    for j in [1,2,5]:
        truncated=sum(weight*ratio**n*2*n for n in range(1,j))+2*j*weight*ratio**j/(1-ratio)
        ck('bounded_restoration_witness_'+str(j),truncated==F(64,25)*(1-ratio**j))
    ck('bounded_first_witness',F(64,25)*(1-ratio)==F(576,625))
    C=9 if fault=='wrong_squeeze_energy' else 81
    q=15999999;rr=5183999998;ll=99999999999999
    ck('consumer_input_tail',F(4,q+1)==F(1,2000)**2)
    ck('consumer_output_tail',F(2*C*2,rr+2)==F(1,4000)**2)
    ck('consumer_phase',F(q+rr)*F(22,7)/(ll+1)<F(164,10**6))
    ck('ten_call_error',10*(F(1,2000)+F(1,4000)+F(q+rr)*F(22,7)/(ll+1))<F(914,100000))
    ck('reference_maximum',rr+ll-1+q==100005199999995)
    ck('reference_mean',F(rr)+F(ll-1,2)==50005183999997)
    ck('same_records_wrong_backaction',1-F(9,25)==F(4,5)**2)
    return out

RESULT='K2253'
REPORT='lab/process/k2253-full-instrument-reference-reuse.json'
DEPS=['explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md','explorations/conditional-build/k2251-detector-phase-reference-2026-10-29.md','explorations/conditional-build/k2241-local-mode-detector-network-2026-10-29.md']
EVIDENCE='Exact finite complex isometry/shell/charge and rational resource controls; universal Hilbert and adaptive hybrid claims are written proofs. Hash checks report integrity.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    args=argparse.ArgumentParser();args.add_argument('--write',action='store_true');a=args.parse_args()
    root=Path(__file__).resolve().parents[2]
    checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v]
        assert bad,('undetected mathematical input fault',fault)
        faults[fault]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'certificate drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
