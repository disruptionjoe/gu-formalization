#!/usr/bin/env python3
"""Exact mode-effect compression, invariant finite reference and actual-input faults."""
import sympy as s
from fractions import Fraction as F
FAULTS=['wrong_mode_ratio','missing_vacuum_normalization','reference_dephased','missing_endpoint','wrong_charge','wrong_shift_orientation','ignore_charge_degeneracy','discard_reference_cross_terms']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    ratio=-s.Rational(4,5) if fault!='wrong_mode_ratio' else s.Rational(3,5)
    norm=s.Rational(3,5) if fault!='missing_vacuum_normalization' else 1
    coeff=[norm*ratio**j for j in range(5)]
    for j in range(4):ck('annihilation_recurrence_'+str(j),s.Rational(5,3)*coeff[j+1]+s.Rational(4,3)*coeff[j]==0)
    ck('infinite_geometric_norm',norm**2/(1-ratio**2)==1)
    E=s.Matrix([[coeff[0]**2,coeff[0]*coeff[1]],[coeff[0]*coeff[1],coeff[1]**2]])
    ck('actual_compressed_effect',E==s.Matrix([[s.Rational(9,25),-s.Rational(36,125)],[-s.Rational(36,125),s.Rational(144,625)]]))
    ck('rank_one',E.det()==0)
    ck('effect_trace',s.trace(E)==s.Rational(369,625))
    for sign,prob in [(1,s.Rational(9,1250)),(-1,s.Rational(729,1250))]:
        v=s.Matrix([1,sign])/s.sqrt(2)
        ck('target_probability_'+str(sign),s.simplify((v.T*E*v)[0])==prob)
        ck('mean_number_'+str(sign),(v.T*s.diag(0,2)*v)[0]==1)
    for L in [2,3,5]:
        rv=s.Matrix([s.sqrt(s.Rational(2,L+1))*s.sin((j+1)*s.pi/(L+1)) for j in range(L)])
        sig=s.simplify(rv*rv.T)
        if fault=='reference_dephased':sig=s.diag(*[sig[j,j] for j in range(L)])
        M=s.zeros(2*L);a,b,d=E[0,0],E[0,1],E[1,1]
        for j in range(L):M[j,j]=a;M[L+j,L+j]=d
        if fault=='missing_endpoint':M[0,0]=0;M[-1,-1]=0
        for j in range(1,L):
            k=L+j-1 if fault!='wrong_shift_orientation' else L+j
            M[j,k]=b;M[k,j]=b
        N=s.diag(*([2*j for j in range(L)]+[(1 if fault=='wrong_charge' else 2)+2*j for j in range(L)]))
        ck('charge_invariance_'+str(L),M*N==N*M)
        effect=s.Matrix(2,2,lambda x,y:sum(sig[j,i]*M[x*L+i,y*L+j] for i in range(L) for j in range(L))).applyfunc(s.simplify)
        co=s.cos(s.pi/(L+1))
        ck('finite_effect_diagonal_'+str(L),effect[0,0]==a and effect[1,1]==d)
        ck('finite_effect_coherence_'+str(L),s.simplify(effect[0,1]-b*co)==0)
        ck('sine_reference_normalized_'+str(L),s.simplify((rv.T*rv)[0])==1)
        ck('sine_charge_mean_'+str(L),s.simplify(sum(2*j*rv[j]**2 for j in range(L)))==L-1)
        A=s.zeros(L)
        for j in range(L-1):A[j,j+1]=A[j+1,j]=s.Rational(1,2)
        ck('path_eigenvector_'+str(L),(A*rv-co*rv).applyfunc(s.simplify)==s.zeros(L,1))
    # Sharp half-mode coefficient on matching charge pair: invariant |+><+| block.
    M=s.zeros(4);M[1,1]=M[2,2]=M[1,2]=M[2,1]=s.Rational(1,2)
    sig=s.ones(2)/2;ff=sum(sig[j,i]*M[i,2+j] for i in range(2) for j in range(2))
    ck('half_mode_bound_sharp',ff==s.Rational(1,4))
    ck('explicit_compression_resource',F(18,125)*F(22,7)**2/F(101)**2<F(1,7000))
    ck('coupled_energy_budget_floor',s.simplify(2*s.sqrt(s.Rational(1,4)*s.Rational(3,4))*s.Rational(36,125))==18*s.sqrt(3)/125)

    # Full finite-charge compression with a degenerate charge sector and complex effect.
    charges=[0,1,1,2];L=3;vec=s.Matrix([1,s.I,2,3])/s.sqrt(15);EE=vec*vec.conjugate().T
    rv=s.Matrix([s.Rational(1,2),1/s.sqrt(2),s.Rational(1,2)])
    MM=s.Matrix(4*L,4*L,lambda a,b:EE[a//L,b//L] if ((a//L+a%L==b//L+b%L) if fault=='ignore_charge_degeneracy' else (charges[a//L]+a%L==charges[b//L]+b%L)) else 0)
    NN=s.diag(*[q+j for q in charges for j in range(L)])
    ck('full_effect_degenerate_charge_invariance',MM*NN==NN*MM)
    for total in range(5):
        inds=[a for a in range(4*L) if charges[a//L]+a%L==total]
        blk=MM.extract(inds,inds)
        ck('full_effect_sector_rank_'+str(total),blk.rank()<=1)
        ck('full_effect_sector_positive_contraction_'+str(total),0<=s.trace(blk)<=1)
    induced=s.Matrix(4,4,lambda a,b:sum(rv[j]*rv[i]*MM[a*L+i,b*L+j] for i in range(L) for j in range(L) if fault!='discard_reference_cross_terms' or i==j))
    for a in range(4):
        for b in range(4):
            d=charges[b]-charges[a];overlap=sum(rv[j+d]*rv[j] for j in range(L) if 0<=j+d<L)
            ck('full_effect_autocorrelation_'+str((a,b)),s.simplify(induced[a,b]-EE[a,b]*overlap)==0)
    ck('energy_ball_tail_exact',F(2)**2/F(160000)==F(1,200)**2)
    ck('energy_ball_consumer',F(1,200)+F(159999)*F(22,7)/200000000<F(7515,1000000))
    ck('reference_mean_integer_charge',F(199999998,2)==99999999)
    return out

RESULT='K2251'
REPORT='lab/process/k2251-detector-phase-reference.json'
DEPS=['explorations/conditional-build/k2251-detector-phase-reference-2026-10-29.md', 'explorations/conditional-build/k2241-local-mode-detector-network-2026-10-29.md', 'explorations/conditional-build/k2247-coupled-drift-cutoff-control-2026-10-29.md']
EVIDENCE="Finite exact algebra/arithmetic controls and actual input faults; universal results are written proofs, not established by finite controls. Hash checks are reporting integrity."

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
