#!/usr/bin/env python3
"""Exact sparse-Clifford controls for K2230; universal proofs are in the note."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tests/channel-swings'))
import k2206_changed_raw_mass_construction_probe as o

F=o.F; I=o.ONE; Z=o.ZERO; add=o.add; mul=o.mul; scale=o.scale
T=o.blade(o.UN); A=mul(o.G[0],o.J); B=o.blade(range(7,14))
C={j:mul(o.G[0],o.G[j]) for j in o.OBS[1:]}
X={j:mul(C[j],T) for j in C}
FAULTS=['differentiated_sign','norm_factor','temporal_sign','omit_temporal',
        'trace_lift','return_sign','raw_order','curvature_commutator']

def comm(a,b): return add(mul(a,b),scale(mul(b,a),-1))
def anti(a,b): return add(mul(a,b),mul(b,a))
def ip(a,b): return 128*mul(o.transpose(a),b).get(0,F(0))
def tracetest(om,g,r):
    return add(mul(mul(o.transpose(om),g),o.G[r]),mul(mul(g,o.G[r]),om))

def run(fault=None):
    out=[]
    def ck(k,v): out.append((k,bool(v)))
    basis=[A,*X.values()]
    ck('B_symmetric_involution',o.transpose(B)==B and mul(B,B)==I)
    ck('B_mass_commutes',comm(B,A)==Z)
    for p,e in enumerate(basis):
        ck(f'clifford_skew_{p}',o.transpose(e)==scale(e,-1))
        for q,f in enumerate(basis):
            ck(f'clifford_anti_{p}_{q}',anti(e,f)==(scale(I,-2) if p==q else Z))
        for j in X:
            ck(f'vector_bivector_orthogonal_{p}_{j}',ip(e,mul(A,X[j]))==0)
    for j in X: ck(f'B_flavor_anti_{j}',anti(B,X[j])==Z)

    # Independent nonzero coefficient and derivative jets; no static-K substitution.
    m=F(3,5); av=[F(2,7),F(-3,11),F(5,13)]
    V=add(*(scale(X[j],v) for j,v in zip(X,av)))
    K=add(scale(A,m),V); Kbar=add(scale(A,m),scale(V,-1))
    Kdot=add(scale(A,F(-4,9)),*(scale(X[j],v) for j,v in zip(X,[F(7,8),F(2,3),F(-5,6)])))
    Kbardot=mul(mul(B,Kdot),B)
    ck('bar_by_B',mul(mul(B,K),B)==Kbar)
    for r in o.UN:
        ck(f'bar_by_normal_{r}',mul(mul(o.G[r],K),scale(o.G[r],o.ETA[r]))==Kbar)
    defect=scale(mul(A,V),(2 if fault=='norm_factor' else 4)*m)
    ck('commutator_defect',scale(comm(K,V),2)==defect)
    ck('norm_AV',ip(mul(A,V),mul(A,V))==128*sum(v*v for v in av))
    norm_delta=ip(add(Kdot,defect),add(Kdot,defect))-ip(Kdot,Kdot)
    ck('norm_gap_with_independent_time_jets',norm_delta==2048*m*m*sum(v*v for v in av))
    ck('norm_gap_strict',norm_delta>0)
    # Initial trace intertwiner H=K is nonsingular and generally nonorthogonal.
    # It is an admissible point, not a claimed full solution of incompatible jets.
    H=K; G=mul(H,B); Gdot=comm(G,K); Hdot=scale(mul(H,V),-2)
    ck('initial_H_commutes_K',comm(H,K)==Z)
    ck('initial_same_G_trace',mul(G,Kbar)==mul(K,G))
    ck('H_dot_equivalence',mul(Gdot,B)==Hdot)
    ck('HHt_positive_scalar',mul(H,o.transpose(H))==scale(I,m*m+sum(v*v for v in av)))
    ck('HHt_derivative_zero',add(mul(Hdot,o.transpose(H)),mul(H,o.transpose(Hdot)))==Z)
    ck('HHt_commutes_K',comm(mul(H,o.transpose(H)),K)==Z)
    ck('variable_trace_derivative',
       add(mul(Gdot,Kbar),mul(G,Kbardot),scale(mul(Kdot,G),-1),scale(mul(K,Gdot),-1))
       ==add(mul(G,Kbardot),scale(mul(Kdot,G),-1),mul(G,comm(K,Kbar))))
    # Use rational orthogonal H=3A/5+4X7/5 for the differentiated centralizer identity.
    Q=add(scale(A,F(3,5)),scale(X[7],F(4,5)))
    Kv=Q; Vv=scale(X[7],F(4,5)); Qdot=scale(mul(Q,Vv),2 if fault=='differentiated_sign' else -2)
    lhs=mul(o.transpose(Q),add(comm(Qdot,Kv),comm(Q,Kdot)))
    rhs=add(Kdot,scale(mul(mul(o.transpose(Q),Kdot),Q),-1),scale(comm(Kv,Vv),2))
    ck('polar_orthogonal_control',mul(Q,o.transpose(Q))==I)
    ck('differentiated_centralizer_identity',lhs==rhs)
    ck('orthogonal_conjugation_norm',ip(mul(mul(o.transpose(Q),Kdot),Q),mul(mul(o.transpose(Q),Kdot),Q))==ip(Kdot,Kdot))

    # Fully supplied moving massive raw lift; phase/gradient/time jets are independent.
    spatial=F(3,7); temporal=F(5,11); mass=F(2,3)
    xx=T if fault=='trace_lift' else X[7]
    oms={k:Z for k in range(14)}
    oms[0]=add(scale(A,mass),scale(xx,spatial)); oms[7]=scale(xx,temporal)
    if fault=='temporal_sign': oms[7]=scale(oms[7],-1)
    if fault=='omit_temporal': oms[7]=Z
    induced=add(scale(A,mass),scale(xx,-spatial),scale(mul(C[7],oms[7]),-1))
    expected=add(scale(A,mass),scale(X[7],-spatial),scale(T,-temporal))
    ck('exact_induced_time_compensator',induced==expected)
    ck('conserved_reduced_current',o.transpose(induced)==scale(induced,-1))
    for k,om in oms.items():
        ck(f'I_parallel_{k}',add(o.transpose(om),om)==Z)
        for r in o.UN: ck(f'original_B_trace_{k}_{r}',tracetest(om,B,r)==Z)
    ck('B_not_parallel',add(mul(o.transpose(oms[0]),B),mul(B,oms[0]))!=Z)
    ck('I_not_same_trace',tracetest(oms[0],I,o.UN[0])!=Z)

    tr=[scale(o.G[k],o.ETA[k]) for k in range(14)]+[o.WB]
    inv=o.G+[scale(o.W,F(1,2))]
    def entry(k,om,row,col):
        rr=o.raw(k,row,col,'raw_return_sign' if fault=='return_sign' else None)
        prod=mul(om,rr) if fault=='raw_order' else mul(rr,om)
        return mul(mul(inv[row],prod),tr[col])
    # Universal linear generators for the chosen raw connection; every output row.
    for label,k,om,sgn in [('mass',0,A,-1),*[(f'flavor{k}',k,xx,1) for k in o.OBS]]:
        for col in o.UN[1:]:
            for row in range(15):
                lhs=add(entry(k,om,row,col),scale(entry(k,om,row,o.UN[0]),-1))
                rhs=scale(mul(mul(o.G[k],o.WB),om),sgn*(int(row==col)-int(row==o.UN[0])))
                ck(f'original_raw_{label}_{row}_{col}',lhs==rhs)
        rr=o.raw(k,14,k,'raw_return_sign' if fault=='return_sign' else None)
        ck(f'original_bottom_{label}',mul(rr,om)==scale(om,-o.ETA[k]))
    for col in o.UN[1:]:
        for row in range(15):
            lhs=add(*(add(entry(k,om,row,col),scale(entry(k,om,row,o.UN[0]),-1)) for k,om in oms.items() if om))
            rhs=scale(mul(mul(o.G[0],o.WB),expected),-int(row==col)+int(row==o.UN[0]))
            ck(f'combined_raw_{row}_{col}',lhs==rhs)

    u=add(scale(I,F(3,5)),scale(T,F(4,5))); ut=o.transpose(u)
    e=scale(add(I,o.G[1]),F(1,2)); p=mul(mul(u,e),ut); dp=comm(T,p)
    ck('unitary_reduced_frame',mul(u,ut)==I)
    ck('moving_projector',mul(p,p)==p and o.transpose(p)==p)
    ck('projector_rank64',128*p.get(0,F(0))==64)
    ck('projector_rank576_nine_copies',9*128*p.get(0,F(0))==576)
    ck('projector_genuine_motion',dp!=Z)
    ck('projector_mass_commutes',comm(p,A)==Z)
    for j in C:
        ck(f'T_C_commutes_{j}',comm(T,C[j])==Z)
        ck(f'projector_C_commutes_{j}',comm(p,C[j])==Z)
    ck('T_mass_commutes',comm(T,A)==Z)
    p_t=scale(dp,temporal); p_7=scale(dp,spatial)
    ck('propagated_projector_equation',add(p_t,mul(C[7],p_7),comm(induced,p))==Z)
    naive=add(scale(A,mass),scale(X[7],-spatial))
    naive_residual=add(p_t,mul(C[7],p_7),comm(naive,p))
    ck('omitted_temporal_term_nonzero',naive_residual==p_t and p_t!=Z)
    transformed_n=add(mul(mul(u,scale(A,mass)),ut),scale(mul(mul(scale(T,temporal),u),ut),-1),scale(mul(C[7],mul(mul(scale(T,spatial),u),ut)),-1))
    ck('reduced_frame_derivative_coefficients',transformed_n==expected)
    ck('full_raw_frame_is_different',any(mul(mul(ut,o.raw(k,r,c)),u)!=o.raw(k,r,c) for k in o.OBS for r in range(15) for c in range(15)))
    # theta_tt=theta_77 for epsilon sin(t)sin(x7); mixed jets cancel effectively.
    mixed=F(7,13)
    ck('effective_curvature_zero',add(scale(T,mixed),scale(T,-mixed),comm(scale(T,temporal),scale(T,spatial)))==Z)
    raw_curvature=Z if fault=='curvature_commutator' else comm(oms[0],oms[7])
    expected_curvature=scale(mul(A,X[7]),2*mass*temporal)
    ck('raw_curvature_nonzero_commutator',raw_curvature==expected_curvature and raw_curvature!=Z)
    return out



def main():
    import argparse, hashlib, json
    from pathlib import Path
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--controls-only',action='store_true')
    args=parser.parse_args()
    baseline=run()
    bad=[name for name,ok in baseline if not ok]
    if bad:
        raise AssertionError('FAIL baseline: '+repr(bad))
    detected={}
    for fault in FAULTS:
        # Exceptions propagate as errors; they never count as detection.
        checks=run(fault)
        failed=[name for name,ok in checks if not ok]
        if not failed:
            raise AssertionError('FAIL mutation escaped: '+fault)
        detected[fault]=failed
    root=Path(__file__).resolve().parents[2]
    deps=['tests/channel-swings/k2206_changed_raw_mass_construction_probe.py', 'explorations/conditional-build/k2221-raw-flavor-observation-2026-10-28.md', 'explorations/conditional-build/k2227-same-pairing-temporal-compatibility-2026-10-28.md', 'explorations/conditional-build/k2230-time-dependent-pairing-compatibility-2026-10-29.md']
    target=root/'lab/process/k2230-time-dependent-pairing-compatibility.json'
    report=dict(result='K2230',controls=[dict(name=n,passed=ok) for n,ok in baseline],faults=detected,
        evidence_kind='exact finite arithmetic/Clifford controls; universal proof is in the note',
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps})
    if not args.controls_only:
        if args.write: target.write_text(json.dumps(report,indent=2)+'\n')
        elif json.loads(target.read_text())!=report:
            raise AssertionError('FAIL stale certificate')
    print(json.dumps(dict(result='K2230',controls=len(baseline),faults={k:len(v) for k,v in detected.items()})))

if __name__=='__main__': main()
