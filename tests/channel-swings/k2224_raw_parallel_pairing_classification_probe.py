#!/usr/bin/env python3
"""Exact controls for K2224 parallel-pairing classification."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import argparse, hashlib
ROOT=Path(__file__).resolve().parents[2]
import k2206_changed_raw_mass_construction_probe as o
import json

F=o.F; I=o.ONE; Z=o.ZERO; add=o.add; mul=o.mul; scale=o.scale
def comm(a,b): return add(mul(a,b),scale(mul(b,a),-1))
def anti(a,b): return add(mul(a,b),mul(b,a))
def pairing_rhs(k,g): return add(mul(o.transpose(k),g),mul(g,k))
A=mul(o.G[0],o.J)
T=o.blade(o.UN)
X=[mul(mul(o.G[0],o.G[j]),T) for j in (7,8,9)]
B=o.blade(range(7,14))
Gsplit=mul(o.G[1],o.G[10])

def controls(fault=None):
    out={}
    def ck(k,v): out[k]=bool(v)
    generators=[A]+X
    for i,g in enumerate(generators):
        ck(f'generator_skew_{i}',o.transpose(g)==scale(g,-1))
        ck(f'generator_square_{i}',mul(g,g)==scale(I,-1))
        for j,h in enumerate(generators[:i]):
            ck(f'generator_anticommutator_{i}_{j}',anti(g,h)==Z)
    ck('B_symmetric',o.transpose(B)==B)
    ck('B_involution',mul(B,B)==I)
    ck('B_zero_trace',B.get(0,F(0))==0)
    for r,g in enumerate(o.G):
        ck(f'original_B_Clifford_adjoint_{r}',add(mul(o.transpose(g),B),mul(B,g))==Z)
    ck('B_mass_commutes',comm(B,A)==Z)
    for j,x in enumerate(X):
        ck(f'B_flavor_anticommutes_{j}',anti(B,x)==Z)
        ck(f'original_trace_Hq_{j}',all(add(mul(o.star(x),o.G[r]),mul(o.G[r],x))==Z for r in o.UN))

    m=F(2,3); aa=[F(3,7),F(-5,11),F(2,13)]; vv=[F(4,9),F(1,5),F(-3,8)]
    flavor=add(*(scale(x,a) for x,a in zip(X,aa)))
    K=add(scale(A,m),flavor)
    V=add(*(scale(x,v) for x,v in zip(X,vv)))
    s=sum(v*v for v in vv); av=sum(a*v for a,v in zip(aa,vv))
    ck('V_invertible_square',mul(V,V)==scale(I,-s))
    ck('K_V_anticommutator',anti(K,V)==scale(I,-2*av))
    rhs=add(scale(K,2*s if fault=='rigidity_sign' else -2*s),scale(V,2*av))
    ck('complete_rigidity_polynomial_identity',mul(comm(K,V),V)==rhs)
    ck('positive_parent_parallel',pairing_rhs(K,I)==Z)
    gs=o.G[1] if fault=='split_parent' else Gsplit
    ck('split_parent_symmetric',o.transpose(gs)==gs)
    ck('split_parent_involution',mul(gs,gs)==I)
    ck('split_parent_zero_trace',gs.get(0,F(0))==0)
    ck('split_parent_parallel',pairing_rhs(K,gs)==Z)
    for i,g in enumerate(generators): ck(f'split_commutator_{i}',comm(Gsplit,g)==Z)
    ck('split_does_not_retain_gamma2_B_adjoint',add(mul(o.transpose(o.G[2]),Gsplit),mul(Gsplit,o.G[2]))!=Z)
    ck('original_B_defect',pairing_rhs(K,B)==scale(mul(B,flavor),2))
    ck('original_B_defect_nonzero',pairing_rhs(K,B)!=Z)
    ck('flavor_square',mul(flavor,flavor)==scale(I,-sum(a*a for a in aa)))

    # Congruence solution exp(t K^t) B exp(t K), exact at its first jet.
    dotG=scale(comm(B,K),-1 if fault=='transport_jet' else 1)
    ck('constant_connection_moving_B_first_jet',dotG==pairing_rhs(K,B))
    ck('constant_connection_moving_B_is_nonconstant',comm(B,K)!=Z)
    ck('moving_B_jet_symmetric',o.transpose(comm(B,K))==comm(B,K))
    # A rational, exact finite orthogonal value of the same constant flow.
    # Cayley(K/2) = (I+K/2)^2/(1+|K|^2/4), since K^2=-|K|^2 I.
    kk=m*m+sum(a*a for a in aa)
    h=add(I,scale(K,F(1,2)))
    u=scale(mul(h,h),1/(1+kk/4)); ut=o.transpose(u)
    gt=mul(mul(ut,B),u)
    ck('rational_constant_flow_orthogonal',mul(ut,u)==I)
    ck('rational_constant_flow_commutes_K',comm(u,K)==Z)
    ck('transported_B_symmetric',o.transpose(gt)==gt)
    ck('transported_B_involution',mul(gt,gt)==I)
    ck('transported_B_zero_trace',gt.get(0,F(0))==0)
    ck('transported_B_jet_covariance',pairing_rhs(K,gt)==mul(mul(ut,pairing_rhs(K,B)),u))

    # a7=sin(x7), x7=t=0: K=mA, partial7K=X7. Pointwise time
    # transport has partial7 partial0 G = X7^t B+B X7 != 0.
    mixed=scale(mul(B,X[0]),-2 if fault=='mixed_jet_sign' else 2)
    ck('nonconstant_pointwise_transport_mixed_jet',mixed==pairing_rhs(X[0],B))
    ck('nonconstant_pointwise_transport_spatial_obstruction',pairing_rhs(X[0],B)!=Z)
    ck('curvature_B_obstruction_invertible',mul(pairing_rhs(V,B),pairing_rhs(V,B))==scale(I,4*s))
    # For any constant compatible G, the new trace-Hq condition becomes
    # G [gamma_r,K]; both supplied changed parents fail it for nonzero flavor.
    for name,g in [('positive',I),('split',Gsplit)]:
        r=1
        tr=add(mul(mul(o.transpose(K),g),o.G[r]),mul(mul(g,o.G[r]),K))
        ck(f'{name}_new_trace_equals_commutator',tr==mul(g,comm(o.G[r],K)))
        ck(f'{name}_new_trace_not_original_trace',tr!=Z)
    return out

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    cs=controls(); assert all(cs.values()),[k for k,v in cs.items() if not v]
    faults={f:[k for k,v in controls(f).items() if not v] for f in ['transport_jet','rigidity_sign','split_parent','mixed_jet_sign']}
    assert all(faults.values()),faults
    deps=['explorations/conditional-build/k2224-raw-parallel-pairing-classification-2026-10-28.md','explorations/conditional-build/k2221-raw-flavor-observation-2026-10-28.md','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py']
    out=dict(result='K2224',checks=cs,faults=faults,probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
    if args.write:(ROOT/'lab/process/k2224-raw-parallel-pairing-classification.json').write_text(json.dumps(out,indent=2)+'\n')
    else:assert json.loads((ROOT/'lab/process/k2224-raw-parallel-pairing-classification.json').read_text())==out, 'stale certificate; regenerate after final changes'
    print(json.dumps(dict(passed=len(cs),faults_rejected=len(faults))))
