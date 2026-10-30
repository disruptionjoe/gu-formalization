#!/usr/bin/env python3
"""Exact algebra controls; continuum results rely on the accompanying written proofs."""
from pathlib import Path
import json, hashlib, argparse
import sympy as s
R=Path(__file__).resolve().parents[2]

def evaluate(fault=None):
    checks={}
    def check(name, value): checks[name]=bool(value)
    x=s.symbols('x',nonnegative=True); C=s.symbols('C',positive=True)
    exponent=1 if fault=='filter_power' else 2
    sample=s.sqrt(C)/(1+x)**exponent
    check('differential_precision_spectrum',s.simplify(sample**2-C/(1+x)**4)==0)
    A=s.Matrix([[1,2,-3]]); datum=s.Matrix([1,1,1]);f=s.Rational(2,5)
    filtered=f*datum
    if fault=='partial_constraint_filter':filtered[0]=datum[0]
    check('common_filter_preserves_constraint',A*filtered==s.zeros(1,1))
    gap=s.diag(0,0,s.Rational(1,16),s.Rational(1,81))
    if fault=='gap_removed':gap[0,0]=1
    discarded=s.Matrix([1,2,0,0]);retained=s.Matrix([0,0,1,2])
    check('discarded_support_null',(discarded.T*gap*discarded)[0]==0)
    check('retained_support_positive',(retained.T*gap*retained)[0]>0)
    U=s.Matrix([[1,1],[0,1]]);N=s.eye(2);S=U*U.T
    if fault=='drop_cross':S=s.diag(*S.diagonal())
    expected=s.Matrix([[2,1],[1,1]]);Sig=N+S
    check('common_seed_cross_covariance',S==expected)
    check('noise_floor',Sig[0,0]>0 and Sig.det()>0 and S.det()>=0)
    check('known_noise_covariance_determinant',Sig.det()==5)
    check('inverse_identity',Sig*Sig.inv()==s.eye(2))
    V=s.Matrix([[0,1],[1,-1]]);H=s.Matrix([[0,-s.Rational(1,2)],[-s.Rational(1,2),0]])
    if fault=='witness_sign':H=-H
    B=[V[:,i]*V[:,i].T for i in range(2)]
    check('dual_generator_nonnegative',all(s.trace(H*b)>=0 for b in B))
    check('dual_target_negative',s.trace(H*expected)==-1)
    Ua=s.Matrix([[0,1],[1,1]]);Sa=Ua*Ua.T;Sb=V*V.T
    check('same_diagonal_distinct_covariance',Sa.diagonal()==Sb.diagonal() and Sa!=Sb)
    check('same_diagonal_dual_detects',s.trace(H*Sa)==-1)
    p1,p2=s.symbols('p1 p2');comb=p1*B[0]+p2*B[1]
    check('no_target_band_solution',s.solve(list(comb-expected),(p1,p2))==[])
    t=s.Matrix([1,2]);power=s.Rational(3,7);c=s.Rational(5,3)
    power2=power/c if fault=='wrong_rescale' else power/c**2
    check('projective_power_repair',power*t*t.T==power2*(c*t)*(c*t).T)
    other=s.Matrix([1,3]);check('noncollinear_ranges',s.Matrix.hstack(t,other).det()!=0)
    check('rank_one_signal',(t*t.T).rank()==1)
    def metric(a,b):return s.trace(Sig.inv()*a*Sig.inv()*b)/2
    M=s.eye(2);D=s.Matrix([[1,0],[0,-1]])
    proj=metric(D,M)/metric(M,M)*M
    if fault=='fisher_projection_sign':proj=-proj
    residual=D-proj
    check('nuisance_orthogonality',s.simplify(metric(residual,M))==0)
    check('positive_remaining_information',metric(residual,residual)>0)
    nuisance=2*M;fitted=metric(nuisance,M)/metric(M,M)*M
    check('nuisance_direction_zero',s.simplify(metric(nuisance-fitted,nuisance-fitted))==0)
    # Exact Gaussian fourth-moment score check for two independent standard normals.
    z1,z2=s.symbols('z1 z2');z=s.Matrix([z1,z2]);A0=s.Matrix([[2,1],[1,3]]);B0=s.Matrix([[1,2],[2,0]])
    def moment(poly):
        ans=0
        for (a,b),coeff in s.Poly(s.expand(poly),z1,z2).terms():
            def normal(n):return 0 if n%2 else (s.factorial2(n-1) if n else 1)
            ans+=coeff*normal(a)*normal(b)
        return s.simplify(ans)
    scale=s.Rational(1,1) if fault=='score_factor' else s.Rational(1,2)
    scoreA=scale*((z.T*A0*z)[0]-s.trace(A0));scoreB=scale*((z.T*B0*z)[0]-s.trace(B0))
    check('score_mean_zero',moment(scoreA)==0)
    check('score_covariance_metric',moment(scoreA*scoreB)==s.trace(A0*B0)/2)
    tt=s.symbols('t');b=s.Function('b')(tt);d=s.Function('d')(tt);entropy=s.symbols('h')
    tracer=b*d if fault=='time_bias' else d+entropy
    check('conserved_tracer_difference',s.diff(tracer-d,tt)==0)
    check('multiplicative_bias_has_extra_derivative',s.simplify(s.diff(b*d-d,tt)-s.diff(b,tt)*d-(b-1)*s.diff(d,tt))==0)
    return checks

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    clean=evaluate();failed=[k for k,v in clean.items() if not v]
    if failed:raise AssertionError('clean baseline failed: '+str(failed))
    faults=['gap_removed','filter_power','partial_constraint_filter','drop_cross','witness_sign','wrong_rescale','fisher_projection_sign','score_factor','time_bias']
    caught={}
    for fault in faults:
        result=evaluate(fault);caught[fault]=[k for k,v in result.items() if not v]
        assert caught[fault],f'uncaught altered input/operator: {fault}'
    deps=['explorations/conditional-build/k2327-constrained-seed-likelihood-2026-10-30.md','explorations/conditional-build/k2311-uniform-constrained-dust-evolution-2026-10-30.md','explorations/conditional-build/k2325-relativistic-count-covariance-2026-10-30.md',str(Path(__file__).relative_to(R))]
    report={'result':'K2327','scope':'conditional exact algebra controls; continuum and inference theorems rely on written proofs','evidence_kind':'exact_symbolic_and_rational','checks':clean,'exact_checks':len(clean),'numerical_checks':0,'changed_input_faults':caught,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
    if a.write:(R/'lab/process/k2327-constrained-seed-likelihood.json').write_text(json.dumps(report,indent=2)+'\n')
    print(f'K2327 PASS {len(clean)} exact controls; {len(caught)} genuine faults')
if __name__=='__main__':main()
