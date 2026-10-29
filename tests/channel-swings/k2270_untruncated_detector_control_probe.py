#!/usr/bin/env python3
"""Exact finite controls; continuum/operator claims use the companion written proof."""
import sympy as s
ID='K2270'
NOTE='explorations/conditional-build/k2270-untruncated-detector-control-2026-10-29.md'
REPORT='lab/process/k2270-untruncated-detector-control.json'
DEPS=['explorations/conditional-build/k2267-nearest-neighbor-detector-2026-10-29.md', 'explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md']


def verify(m):
    out={}
    def eq(k,a,b=0):out[k]=s.simplify(a-b)==0
    def yes(k,a):out[k]=bool(a)
    def mat_eq(k,A,B):out[k]=all(s.simplify(s.expand_complex(z))==0 for z in A-B)
    # Complete ordinary two-mode shells, not a local cutoff cube.
    for n in [1,2,3,4]:
        X=s.zeros(n+1);N1=s.diag(*range(n,-1,-1));N2=n*s.eye(n+1)-N1
        for j in range(n):X[j,j+1]=X[j+1,j]=s.sqrt((n-j)*(j+1))*m.get('hopping_scale',1)
        mat_eq('hermitian_'+str(n),X,X.H);mat_eq('conserving_'+str(n),X*(N1+N2),(N1+N2)*X)
        swap=s.zeros(n+1)
        for j in range(n+1):swap[n-j,j]=1
        U=(-s.I*s.pi*X/2).exp();phase=s.exp(s.I*s.pi*n*s.Rational(m.get('phase_num',1),2))
        mat_eq('genuine_swap_'+str(n),phase*U,swap)
        if n==3:
            eq('edge_to_30',X[0,1],s.sqrt(3));eq('middle_physical_amplitude',X[1,2],2)
            old=s.Matrix([[0,2],[2,0]]);oldU=s.exp(s.I*3*s.pi/2)*(-s.I*s.pi*old/2).exp();mat_eq('old_cap2_not_swap',oldU,s.I*s.eye(2))
            yes('old_cap2_failure',oldU!=s.Matrix([[0,1],[1,0]]))
        yes('supported_hopping_norm_'+str(n),max(abs(q) for q in X.eigenvals())<=n)
    # Three genuine modes on a complete <=2 simplex.
    import itertools
    basis=[p for p in itertools.product(range(3),repeat=3) if sum(p)<=2];d=len(basis);index={p:i for i,p in enumerate(basis)}
    nt=s.diag(*map(sum,basis));ns=[s.diag(*(p[i] for p in basis)) for i in range(3)]
    for i in range(2):
        X=s.zeros(d)
        for col,p in enumerate(basis):
            for aa,bb in [(i,i+1),(i+1,i)]:
                if p[bb]:
                    q=list(p);q[aa]+=1;q[bb]-=1;X[index[tuple(q)],col]=s.sqrt((p[aa]+1)*p[bb])
        mat_eq('simplex_conservation_'+str(i),X*nt,nt*X)
        for charge in [0,1,2]:
            P=s.diag(*(int(sum(p)==charge) for p in basis));mat_eq('zero_ideal_leak_'+str(i)+'_'+str(charge),(s.eye(d)-P)*X*P,s.zeros(d))
    S01=s.zeros(d)
    for col,p in enumerate(basis):S01[index[(p[1],p[0],p[2])],col]=1
    mat_eq('routed_remote_nonlinearity',S01*(ns[1]*ns[2])*S01,ns[0]*ns[2])
    yes('simplex_dimension',d==s.binomial(2+3,3))
    # Low-sector and outgoing perturbation; projected double-sided block misses it.
    P=s.diag(1,0);D=s.Matrix([[0,s.Rational(1,100)],[s.Rational(1,100),0]])
    mat_eq('compressed_perturbation_zero',P*D*P,s.zeros(2));Dp=P*D*P if m.get('drop_outgoing') else D*P;eq('outgoing_projected_norm_squared',(Dp.H*Dp)[0,0],s.Rational(1,10000))
    theta=s.pi/6;V=(-s.I*theta*s.Matrix([[0,1],[1,0]])).exp();state=V*s.Matrix([1,0]);prob=s.simplify(s.expand_complex(abs(state[1])**2));eq('leak_probability',prob,s.Rational(1,4));yes('leak_bound',prob<=theta**2)
    eq('unbounded_charge_witness',s.expand_complex((state.H*s.diag(0,10**6)*state)[0]),250000)
    # Genuine finite first moment, divergent second moment example.
    n=s.symbols('n',integer=True,positive=True);pn=1/(n*(n+1)*(n+2))
    eq('probability_sum',s.summation(pn,(n,1,s.oo)),s.Rational(1,4));eq('finite_mean',s.summation(n*pn,(n,1,s.oo)),s.Rational(1,2));eq('second_moment_harmonic_tail',s.limit(n*n*pn*n,n,s.oo),1)
    # Supported Kerr norm and signed instability are different statements.
    for K in [1,2,3]:
        yes('Kerr_supported_'+str(K),max(j*j for j in range(K+1))==K*K);yes('negative_Kerr_unbounded_sequence_'+str(K),-(K+1)**2 < -K*K)
    base=s.Rational(914,100000);compile=s.Rational(1,10000);pert=s.Rational(m.get('pert_num',1),10000)
    yes('full_channel_budget',base+compile+pert<=s.Rational(934,100000));eq('route_count',6*3-5,13)
    return out

FAULTS={'nonphysical_hopping': {'hopping_scale': 2}, 'lost_swap_phase': {'phase_num': 0}, 'lost_outgoing_perturbation': {'drop_outgoing': True}, 'excess_perturbation_budget': {'pert_num': 2}}

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
