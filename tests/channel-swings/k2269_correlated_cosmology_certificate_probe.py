#!/usr/bin/env python3
"""Exact finite controls; continuum/operator claims use the companion written proof."""
import sympy as s
ID='K2269'
NOTE='explorations/conditional-build/k2269-correlated-cosmology-certificate-2026-10-29.md'
REPORT='lab/process/k2269-correlated-cosmology-certificate.json'
DEPS=['explorations/conditional-build/k2266-windowed-cosmology-test-2026-10-29.md']


def verify(m):
    out={}
    def eq(k,a,b=0):out[k]=s.simplify(a-b)==0
    def yes(k,a):out[k]=bool(a)
    x,t,z,a=s.symbols('x t z a');w=(x-1)**2*(2-x)**2
    v=s.Matrix([m.get('v0',649),-870,287])/1806;ws=[w,x*w,x*x*w]
    integ=lambda f:s.integrate(s.expand(f),(x,1,2))
    W=sum(v[j]*ws[j] for j in range(3));M={n:integ(W*x**n) for n in [0,1,2,3,4,6]}
    expected={0:0,1:-s.Rational(1,168560),2:-s.Rational(1,113778),3:0,4:s.Rational(83,2085930),6:s.Rational(7621,18078060)}
    for n in M:eq('moment_'+str(n),M[n],expected[n])
    yy=1+x**3+t+z*x
    Q=18*x*yy*s.diff(yy,x)+s.Rational(9,4)*x*x*s.diff(yy,x)**2-9*x*x*yy*s.diff(yy,x,2)
    ell=x*x*s.diff(W,x,2)+6*x*s.diff(W,x)+4*W
    weak=s.Rational(45,4)*W*x*x*s.diff(yy,x)**2-s.Rational(9,2)*ell*yy**2
    eq('strong_weak_match',integ(W*Q),integ(weak))
    closed=s.Rational(81,4)*M[6]+((18+3*a)*M[1]+s.Rational(63,2)*M[4])*z+m.get('cross_term',18)*M[1]*t*z+s.Rational(81,4)*M[2]*z*z
    eq('independent_formula',integ(W*(Q+3*a*yy)),closed)
    eq('rho_annihilator',integ(W))
    delta=s.Rational(m.get('delta_num',1),10000);H=delta**2*s.Matrix([[0,9*M[1]],[9*M[1],s.Rational(81,4)*M[2]]]);k=s.Rational(81,4)*M[6];margin=s.Rational(1,200);lam=s.Rational(1,1000)
    for av in [-100,m.get('upper_a',100)]:
        g=delta*s.Matrix([0,((18+3*av)*M[1]+s.Rational(63,2)*M[4])/2]);mat=(H+lam*s.eye(2)).row_join(g);mat=mat.col_join(g.T.row_join(s.Matrix([[k-margin-m.get('lambda_sign',1)*lam]])))
        for size in [1,2,3]:yes('PSD_'+str(av)+'_'+str(size),mat[:size,:size].det()>0)
        if not m:
            displayed=[s.Rational(1,1000),s.Rational(284124735494319999919,284124736000000000000000000),s.Rational(4777328098353873426598050367 if av==-100 else 4777328136787828986598050367,1883355475793792000000000000000000000)]
            for size in [1,2,3]:eq('displayed_minor_'+str(av)+'_'+str(size),mat[:size,:size].det(),displayed[size-1])
        u=s.Matrix(s.symbols('u1 u2'));rr=(u.T*H*u)[0]+2*g.dot(u)+k
        eq('certificate_identity_'+str(av),rr-margin,(u.col_join(s.Matrix([1])).T*mat*u.col_join(s.Matrix([1])))[0]+lam*(1-u.dot(u)))
    E=s.Matrix([[1,1],[1,2]]);Sigma=s.Rational(1,10**8)*(E*E.T)
    if m.get('diagonal_only'):Sigma=s.diag(*Sigma.diagonal())
    G=E.T*Sigma.inv()*E
    eq('correlated_design_ellipsoid',sum((G-s.Integer(10**8)*s.eye(2))[i,j]**2 for i in range(2) for j in range(2)))
    # Overdetermined correlated design, including a genuinely nonzero residual d0.
    EE=s.Matrix([[1,0],[1,1],[1,2]]);S=s.Matrix([[2,1,0],[1,2,1],[0,1,2]]);data=s.Matrix([1,2,4]);GG=EE.T*S.inv()*EE;cc=GG.inv()*EE.T*S.inv()*data;res=data-EE*cc;d0=(res.T*S.inv()*res)[0];c=s.Matrix([t,z]);err=data-EE*c
    eq('GLS_completion',(err.T*S.inv()*err)[0],d0+((c-cc).T*GG*(c-cc))[0]);yes('nonzero_d0',d0>0);yes('empty_q_case',d0>d0/2)
    eq('singleton_at_q_d0',(res.T*S.inv()*res)[0],d0);yes('full_rank',EE.rank()==2);yes('rank_deficient_control',s.Matrix([[1,1],[2,2]]).rank()==1)
    tau=s.Rational(m.get('tau_num',1),10**8);bias=s.Rational(2589985595,7224)*tau
    yes('nonpolynomial_bias_consumer',bias<margin)
    yes('positive_reconstruction',2-3*delta>0);yes('bounded_reconstruction',9+3*delta+s.Rational(1,10**8)<10);yes('bounded_derivative',12+delta+s.Rational(1,10**8)<13)
    return out

FAULTS={'wrong_annihilator': {'v0': 650}, 'lost_cross_term': {'cross_term': 0}, 'expanded_uncertainty': {'delta_num': 10000}, 'unchecked_far_endpoint': {'upper_a': 100000000}, 'wrong_S_procedure_sign': {'lambda_sign': -1}, 'lost_observation_correlations': {'diagonal_only': True}, 'excess_model_bias': {'tau_num': 2}}

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks=verify({});bad=[k for k,v in checks.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for name,change in FAULTS.items():
        result=verify(change)
        failures=[k for k,v in result.items() if not v]
        if not failures: raise AssertionError('UNDETECTED: '+name)
        caught[name]=failures
    root=Path(__file__).resolve().parents[2]
    paths=[NOTE,str(Path(__file__).resolve().relative_to(root))]+DEPS
    hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
    report=dict(result_id=ID,status='internally_reviewed_conditional_mathematics',evidence_kind='finite_exact_symbolic_and_matrix_controls_plus_genuine_changed_input_faults',checks=len(checks),faults=len(caught),fault_failures=caught,sha256=hashes,ceiling='Finite checks supplement written proofs; no empirical, source, novelty, Lean or remote-CI certification.')
    dest=root/REPORT
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:
        old=json.loads(dest.read_text());assert old==report,'stale report: reproduce with --write after review'
    print(ID, 'PASS',len(checks),'exact finite controls;',len(caught),'genuine faults; hashes current')
if __name__=='__main__':main()
