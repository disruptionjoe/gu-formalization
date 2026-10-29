#!/usr/bin/env python3
"""Exact recorded-branch overlap, phase asymmetry and conserving recharge controls."""
import sympy as s
from fractions import Fraction as F
FAULTS=['wrong_field_phase','omitted_record_branch','coherent_branch_sum','wrong_geometric_ratio','nonconserving_recharge','hidden_coherent_donor']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    p=s.Rational(9,25);r=s.Rational(16,25) if fault!='wrong_geometric_ratio' else s.Rational(15,25)
    ck('branch_norm',p*p/(1-r)==p)
    # Supply exp(-i theta); actual |j,j> rotation is its square.
    def overlaps(t):
        z=t if fault=='wrong_field_phase' else t*t
        a=s.simplify(p*p/(1-r*z));b=s.simplify(1-2*p+a)
        if fault=='omitted_record_branch':b=0
        return a,b
    def fid(t):
        a,b=overlaps(t)
        return s.simplify(abs(a+b) if fault=='coherent_branch_sum' else abs(a)+abs(b))
    ck('f_zero',fid(1)==1);ck('even_number_period',fid(-1)==1)
    ck('f_halfturn',fid(-s.I)==s.Rational(449,1025))
    ck('branch_halfturn',overlaps(-s.I)==(s.Rational(81,1025),s.Rational(368,1025)))
    t=(3-4*s.I)/5;a,b=overlaps(t)
    correct_a=s.Rational(81,625)/(1-s.Rational(16,25)*t*t);correct_b=s.Rational(7,25)+correct_a
    ck('general_recorded_fidelity',s.simplify(fid(t)-(abs(correct_a)+abs(correct_b)))==0)
    ck('record_is_essential',s.simplify(abs(correct_a)+abs(correct_b)-abs(correct_a+correct_b))>0)
    # Geometric truncated overlap plus exact tail equals closed form: no numerical cutoff claim.
    for j in [0,1,2,5,10]:
        z=t*t
        aa=sum(p*p*r**n*z**n for n in range(j+1))+p*p*(r*z)**(j+1)/(1-r*z)
        ck('whole_tail_overlap_'+str(j),s.simplify(aa-correct_a)==0)
    coeff=4*F(16,25)/F(9,25)**2;ck('angular_coefficient',coeff==F(1600,81))
    for H in [1,2,10,100]:
        lowerx=F(100,81*H*H);drop=F(9,25)*lowerx/(2*(1+lowerx))
        ck('rational_uniform_drop_'+str(H),drop>=F(18,181*H*H))
    x=F(360,181);ck('twenty_H_squared_consumer',1+x+x*x/2>4)
    # Pure two-level phase orbit saturates spectral-arc bound at rational unit-circle t.
    for H in [1,2,3,7]:
        overlap=(1+t**H)/2
        distance_sq=s.simplify(1-overlap*s.conjugate(overlap))
        expected=s.simplify((2-t**H-s.conjugate(t)**H)/4)
        ck('two_level_orbit_'+str(H),s.simplify(distance_sq-expected)==0)
        ck('number_eigenstate_no_phase_'+str(H),s.simplify(t**H*s.conjugate(t)**H)==1)
    # Explicit conserving recharge permutation on B=0..4,D=0..2.
    dimB=5;dimD=3;U=s.eye(dimB*dimD)
    for n in [2,3,4]:
        src=(n-2)*dimD+2;dst=n*dimD
        U[src,src]=U[dst,dst]=0;U[src,dst]=U[dst,src]=1
    if fault=='nonconserving_recharge':U=s.eye(dimB*dimD);U[0,0]=U[3,3]=0;U[0,3]=U[3,0]=1
    N=s.diag(*[b+d for b in range(dimB) for d in range(dimD)])
    ck('recharge_unitary',U.H*U==s.eye(dimB*dimD));ck('recharge_conserves_number',U*N==N*U)
    before=s.zeros(dimB*dimD,1);after=s.zeros(dimB*dimD,1)
    for j,c in enumerate([s.Rational(1,3),s.Rational(2,3),s.Rational(2,3)]):before[j*dimD+2]=c;after[(j+2)*dimD]=c
    ck('recharge_packet_exact',U*before==after)
    target=s.Matrix([1,0,1])/s.sqrt(2);rho=target*target.H;deph=s.diag(s.Rational(1,2),0,s.Rational(1,2));W=s.Matrix([[0,0,1],[0,0,0],[1,0,0]])
    ck('dephased_sharp_witness',s.trace(W*(rho-deph))/2==s.Rational(1,2))
    ck('dephased_distance_attained',sum(abs(x)*m for x,m in (rho-deph).eigenvals().items())/2==s.Rational(1,2))
    eta=s.diag(0,0,1) if fault!='hidden_coherent_donor' else rho
    ck('donor_joint_invariance',eta*s.diag(0,1,2)==s.diag(0,1,2)*eta)
    # A globally coherent pair with diagonal marginals is NOT invariant stock.
    pair=s.Matrix([1,0,0,1])/s.sqrt(2);pair=pair*pair.H;Nt=s.diag(0,1,1,2)
    ck('diagonal_marginals_insufficient',pair*Nt!=Nt*pair)
    return out

RESULT='K2260'
REPORT='lab/process/k2260-coherent-replenishment-bound.json'
DEPS=['explorations/conditional-build/k2260-coherent-replenishment-bound-2026-10-29.md', 'explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md', 'explorations/conditional-build/k2257-finite-battery-service-capacity-2026-10-29.md']
EVIDENCE='Finite exact algebra and rational controls; changed mathematical/resource inputs must fail unchanged checks. Universal proofs and report hashes are separate evidence.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    root=Path(__file__).resolve().parents[2];checks=controls()
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected input fault',f);faults[f]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'report drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
