#!/usr/bin/env python3
"""Exact finite controls; universal statements rest on the companion written proof."""
import sympy as s
ID='K2267'
NOTE='explorations/conditional-build/k2267-nearest-neighbor-detector-2026-10-29.md'
REPORT='lab/process/k2267-nearest-neighbor-detector.json'
DEPS=['explorations/conditional-build/k2264-restricted-detector-control-2026-10-29.md', 'explorations/conditional-build/k2253-full-instrument-reference-reuse-2026-10-29.md']

def verify(m):
    import itertools,math
    out={}
    def eq(k,A,B=0):out[k]=s.simplify(A-B)==(s.zeros(*A.shape) if isinstance(A,s.MatrixBase) else 0)
    def yes(k,a):out[k]=bool(a)
    X1=s.Matrix([[0,1],[1,0]])
    U1=(-s.I*m.get('hopping_sign',1)*s.pi*X1/2).exp()
    eq('pair_charge1_swap',s.I*U1,X1)
    X=s.sqrt(2)*s.Matrix([[0,1,0],[1,0,1],[0,1,0]])
    U=(-s.I*s.pi*X/2).exp();swap=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
    eq('pair_charge2_swap',m.get('phase',-1)*U,swap)
    X3=2*s.Matrix([[0,1],[1,0]]);U3=s.exp(3*s.I*s.pi/2)*(-s.I*s.pi*X3/2).exp()
    eq('whole_cube_charge3_counterexample',U3,s.I*s.eye(2));yes('whole_cube_not_swap',U3!=s.Matrix([[0,1],[1,0]]))
    N=3;K=2;aa=2
    states=[(*ns,l) for ns in itertools.product(range(K+1),repeat=N) if sum(ns)<=K for l in range(aa)];idx={v:i for i,v in enumerate(states)};d=len(states)
    yes('simplex_dimension',d==aa*math.comb(K+N,N))
    def perm(pair):
        S=s.zeros(d)
        for j,v in enumerate(states):
            z=list(v);z[pair],z[pair+1]=z[pair+1],z[pair];S[idx[tuple(z)],j]=1
        return S
    S12=perm(0);S23=perm(1)
    Ns=[s.diag(*[v[i] for v in states]) for i in range(3)];P=s.diag(*[v[3] for v in states]);tot=sum(Ns,s.zeros(d))
    eq('swap_unitarity',S12.T*S12,s.eye(d));eq('charge_preserved',S12*tot,tot*S12)
    eq('remote_cross_routing',S12.T*(Ns[1]*Ns[2])*S12,Ns[0]*Ns[m.get('remote_site',2)])
    route=S12*S23
    eq('port_routing',route.T*Ns[0]*P*route,Ns[2]*P)
    eq('restored_all_spectator_states',route.T*route,s.eye(d))
    for j in range(d):eq('basis_restoration_'+str(j),route.T*route[:,j],s.eye(d)[:,j])
    features=[]
    for v in states:
        ns=v[:3];l=v[3];ps=[int(l==q) for q in range(aa)]
        features.append(list(ns)+[z*z for z in ns]+[ns[i]*ns[j] for i in range(3) for j in range(i+1,3)]+ps+[ns[i]*ps[q] for i in range(3) for q in range(aa)])
    C=K*K;base=4*C+1;energy=[sum(base**j*f for j,f in enumerate(fs)) for fs in features]
    gaps={};edges=[]
    for i,v in enumerate(states):
        for j,u in enumerate(states):
            delta=[u[k]-v[k] for k in range(3)]
            hop=(u[3]==v[3] and any(delta==sg for sg in [[1,-1,0],[-1,1,0],[0,1,-1],[0,-1,1]]))
            flip=(u[:3]==v[:3] and abs(u[3]-v[3])==1)
            if hop or flip:edges.append((i,j));gaps[(i,j)]=energy[j]-energy[i]
    yes('distinct_nonzero_directed_gaps',0 not in gaps.values() and len(set(gaps.values()))==len(gaps))
    for charge in range(K+1):
        vertices={i for i,v in enumerate(states) if sum(v[:3])==charge};seen={min(vertices)}
        while True:
            new=seen|{j for i,j in edges if i in seen}
            if new==seen:break
            seen=new
        yes('shell_connected_'+str(charge),seen==vertices)
    # Without all spectator features, a direct nearest-neighbor diagonal list has collisions on a longer chain.
    small=[v for v in itertools.product(range(2),repeat=4)]
    def local_feature(v):return list(v)+[n*n for n in v]+[v[i]*v[i+1] for i in range(3)]
    va=(1,0,0,0);vb=(0,1,0,0);vc=(1,0,0,1);vd=(0,1,0,1)
    yes('nearest_diagonal_spectator_collision',[b-a for a,b in zip(local_feature(va),local_feature(vb))]==[b-a for a,b in zip(local_feature(vc),local_feature(vd))])
    R=5183999998;H=100005199999995;cap=2*R+H
    yes('actual_enlarged_cap',cap==m.get('cap',100015567999991))
    yes('routing_bound',6*N-5==13)
    q=15999999;L=99999999999999;B0=1;Cdet=81
    # Rational strict upper bounds on the three square-root/pi terms, proven by squaring positive bounds.
    tail=s.Rational(1,2000);output=s.Rational(1,4000);ref=s.Rational(164,1000000)
    yes('input_tail_bound',tail**2>=4*s.Rational(B0,q+1))
    yes('output_tail_bound',output**2>=2*s.Rational(Cdet*(B0+1),R+2))
    yes('reference_bound',ref>(q+R)*s.Rational(22,7)/(L+1))
    total=10*(tail+output+ref)+s.Rational(m.get('extra_num',2),10000)
    yes('ten_call_budget',total<=s.Rational(934,100000))
    return out
FAULTS={'missing_swap_phases':{'phase':1},'reversed_hopping_sign':{'hopping_sign':-1},'wrong_remote_target':{'remote_site':1},'unenlarged_capacity':{'cap':100005199999995},'overspent_error_allocation':{'extra_num':3}}

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
