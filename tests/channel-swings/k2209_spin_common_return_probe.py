#!/usr/bin/env python3
"""Exact sparse Clifford certificate for the complete fourteen-component Spin coefficient class."""
from fractions import Fraction as F
from itertools import combinations
import json, argparse, hashlib
from pathlib import Path
ETA=(1,)*7+(-1,)*7
O=(0,7,8,9); U=tuple(i for i in range(14) if i not in O)
I={0:F(1)}; Z={}; G=[{1<<i:F(1)} for i in range(14)]
def add(*xs):
    r={}
    for x in xs:
        for m,v in x.items():r[m]=r.get(m,0)+v
    return {m:v for m,v in r.items() if v}
def sc(x,v):return {m:a*v for m,a in x.items() if a*v}
def mul(x,y):
    r={}
    for a,va in x.items():
        for b,vb in y.items():
            s=1
            for k in range(14):
                if a>>k&1:
                    s*=(-1)**((b&((1<<k)-1)).bit_count())
                    if b>>k&1:s*=ETA[k]
            r[a^b]=r.get(a^b,0)+s*va*vb
    return {m:v for m,v in r.items() if v}
def prod(ids):
    x=I
    for i in ids:x=mul(x,G[i])
    return x
def tr(x):
    r={}
    for m,v in x.items():
        d=m.bit_count();s=(-1)**(d*(d-1)//2)
        for k in range(14):
            if m>>k&1:s*=ETA[k]
        r[m]=s*v
    return r
def star(x):return {m:v*(-1)**(m.bit_count()*(m.bit_count()+1)//2) for m,v in x.items()}
def alpha(c,x):return sc(mul(mul(G[c],x),G[c]),ETA[c])
J=prod(range(14)); WB=sc(add(sc(I,3),J),F(1,2)); W=sc(add(sc(I,3),sc(J,-1)),F(1,2))
R=[sc(G[c],ETA[c]) for c in range(14)]+[WB]
RI=G+[sc(W,F(1,2))]
def raw(k,a,c):
    if a<14 and c<14 and len({k,a,c})==3:return sc(mul(prod((a,k,c)),W),ETA[a])
    if a==k and c==14:return I
    if a==14 and c==k:return sc(I,-ETA[k])
    return Z
def block(om,a,c):return add(*(mul(mul(RI[a],mul(raw(k,a,c),x)),R[c]) for k,x in om.items()))
def minus(x,y):return add(x,sc(y,-1))
def induced(om):return mul(G[0],add(*(mul(G[k],x) for k,x in om.items())))
def rank(cols):
    piv={}
    for col in cols:
        x=dict(col)
        while x:
            k=min(x)
            if k not in piv:
                piv[k]=sc(x,1/x[k]);break
            x=minus(x,sc(piv[k],x[k]))
    return len(piv)
def checks(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    blades=[prod(p) for p in combinations(range(14),2)]
    tangent=[prod(p) for p in combinations(O,2)]
    # Equality of all ten conjugations is diagonal in the entire grade-two basis.
    survivors=[x for x in blades if all(alpha(c,x)==alpha(U[0],x) for c in U)]
    ck('all91_normal_characters_complete',survivors==tangent)
    # Recover each alpha_c(Omega_k)-alpha_d(Omega_k) from original observed leakage.
    # This establishes equality of kernels, including arbitrary coefficient cancellation.
    for k in O:
        for b,x in enumerate(blades):
            om={k:x};d=U[0]
            for c in U[1:]:
                # Cancel the final invertible Wbar by multiplying W/2.
                residual={a:mul(minus(block(om,a,c),block(om,a,d)),sc(W,F(1,2))) for a in O}
                total=sc(add(*residual.values()),F(1,2) if fault=='inverse_sum' else F(1,3))
                recovered={a:sc(mul(G[a],minus(total,residual[a])),ETA[a]) for a in O}
                target={a:minus(alpha(c,x),alpha(d,x)) if a==k else Z for a in O}
                ck(f'original_leakage_inverse_{k}_{b}_{c}',recovered==target)
    # The actual bottom return first reduces every normal Spin coefficient
    # to Omega_r=eta_r*v*gamma_r with one common tangent vector v.
    common_masks=set.intersection(*(set(m for x in blades for m in mul(x,G[r])) for r in U))
    ck('all10_bottom_common_support',common_masks=={1<<a for a in O})
    for v_index in O:
        v=G[v_index];om={r:sc(mul(v,G[r]),ETA[r]) for r in U}
        ck('bottom_common_witness_'+str(v_index),all(mul(om[r],G[r])==v for r in U))
        n=sc(mul(G[0],v),-8)
        if fault=='normal_coefficient':n=sc(mul(G[0],v),-9)
        kn=sc(mul(mul(G[0],WB),n),-1)
        for c in U[1:]:
            d=U[0]
            ck(f'normal_full_raw_V_{v_index}_{c}',all(minus(block(om,a,c),block(om,a,d))==sc(kn,int(a==c)-int(a==d)) for a in range(15)))
        for a in O:
            ck(f'normal_observed_constant_{v_index}_{a}',all(block(om,a,c)==sc(mul(v,WB),-9) for c in U))
        # Exact trace-Hq defect. For q=gamma_c the c connection gives -2v.
        ck('normal_trace_defect_'+str(v_index),all(add(mul(star(om[r]),G[r]),mul(G[r],om[r]))==sc(v,-2) for r in U))
    images=[]
    for k in O:
        for b,x in enumerate(tangent):
            om={k:x};n=induced(om);images.append(n)
            # All fifteen original rows, on nine independent sum-zero columns.
            kn=sc(mul(mul(G[0],WB),n),-1)
            for c in U[1:]:
                d=U[0]
                ck(f'full_raw_V_{k}_{b}_{c}',all(minus(block(om,a,c),block(om,a,d))==sc(kn,int(a==c)-int(a==d)) for a in range(15)))
            ck(f'trace_Hq_{k}_{b}',all(add(mul(star(x),G[q]),mul(G[q],x))==Z for q in U))
            ck(f'chirality_{k}_{b}',mul(x,J)==mul(J,x))
    images += [sc(mul(G[0],G[a]),-8) for a in O]
    ck('induced_rank8',rank(images)==8)
    symmetric_defects=[add(x,tr(x)) for x in images]
    ck('conservation_constraint_rank4',rank(symmetric_defects)==4)
    Q=prod(O);C=[mul(G[0],G[j]) for j in O[1:]]
    ck('complex_structure',mul(Q,Q)==sc(I,-1) and tr(Q)==sc(Q,-1))
    ck('complex_structure_central',all(mul(Q,c)==mul(c,Q) for c in C))
    for a,c in enumerate(C):
        ck('spatial_Clifford_'+str(a),tr(c)==c and all(add(mul(c,d),mul(d,c))==sc(I,2*int(a==b)) for b,d in enumerate(C)))
    energies=[Q]+[mul(Q,c) for c in C]
    ck('energy_image4',rank(energies)==4 and all(tr(x)==sc(x,-1) for x in energies))
    # All even tangent blades; no nonzero anticommuting mass can hide in combinations.
    even=[prod(p) for r in (0,2,4) for p in combinations(O,r)]
    anticol=[]
    for x in even:
        col={}
        for j,c in enumerate(C):
            for m,v in add(mul(x,c),mul(c,x)).items():col[(j,m)]=v
        anticol.append(col)
    ck('all_even_mass_kernel_zero',rank(anticol)==8)
    # Full faithful128 Clifford spectral polynomial on both complex Q sectors.
    # Complex matrices are pairs of real sparse Clifford polynomials.
    def cmul(x,y):return (minus(mul(x[0],y[0]),mul(x[1],y[1])),add(mul(x[0],y[1]),mul(x[1],y[0])))
    c=F(7,3);b=(F(2,5),F(-3,7),F(5,11));p=(F(3,4),F(-2,9),F(11,13))
    N=mul(Q,add(sc(I,c),*(sc(C[j],b[j]) for j in range(3))))
    for s in (-1,1):
        shifted=(add(sc(I,s*c),*(sc(C[j],p[j]) for j in range(3))),sc(N,-1))
        square=cmul(shifted,shifted)
        r2=sum((p[j]-s*b[j])**2 for j in range(3))
        polynomial=(minus(square[0],sc(I,r2)),square[1])
        projection=(sc(I,F(1,2)),sc(Q,F(s,2)))
        ck('full128_sector_polynomial_'+str(s),cmul(polynomial,projection)==(Z,Z))
        ck('full128_sector_projector_'+str(s),cmul(projection,projection)==projection)
    # Exact scalar dispersion crossing, supplementary to the full matrix identity.
    # At p=s*b+(c,0,0), the spectral polynomial has root E=0.
    c=F(7,3);b=(F(2,5),F(-3,7),F(5,11))
    for s in (-1,1):
        p=tuple(s*b[j]+(c if j==0 else 0) for j in range(3))
        center=-s*c
        r2=sum((p[j]-s*b[j])**2 for j in range(3))
        if fault=='mass_shift':r2+=1
        ck('actual_zero_dispersion_'+str(s),center**2-r2==0)
    # Actual coefficient faults: mixed Spin coefficient leaks; boost evolves nonunitarily.
    mix={0:prod((0,U[0]))}
    ck('mixed_connection_leaks',any(block(mix,a,c)!=block(mix,a,U[0]) for a in O for c in U[1:]))
    boost=induced({0:prod((0,7))})
    ck('boost_fails_positive_energy',add(boost,tr(boost))!=Z)
    # Actual nonzero normal connection, with a tangent cancellation, is
    # conservative but not trace-Hq compatible: the converse also fails.
    v=G[0];normal_cancel={r:sc(mul(v,G[r]),ETA[r]) for r in U}
    normal_cancel[7]=sc(mul(G[0],G[7]),8)
    ck('normal_positive_trace_countercontrol',minus(induced({7:normal_cancel[7]}),sc(mul(G[0],v),8))==Z and add(mul(star(normal_cancel[U[0]]),G[U[0]]),mul(G[U[0]],normal_cancel[U[0]]))!=Z)
    odd=prod(tuple(i for i in range(14) if i!=0))
    ck('K2206_control_outside_Spin',all(m.bit_count()==13 for m in odd) and tr(odd)==sc(odd,-1) and all(add(mul(odd,c),mul(c,odd))==Z for c in C))
    return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');parser.add_argument('--selftest',action='store_true');parser.add_argument('--root',type=Path);args=parser.parse_args()
    baseline=checks();bad=[k for k,v in baseline.items() if not v];assert not bad,bad[:10]
    faults={}
    for f in ('inverse_sum','mass_shift','normal_coefficient'):
        failures=[k for k,v in checks(f).items() if not v];assert failures,f;faults[f]=failures
    dimensions={'Spin_all14_input':1274,'V_preserving':28,'induced':8,'induced_kernel':20,'positive_conserving':24,'conserving_image':4,'trace_Hq_compatible':24,'trace_Hq_and_positive':20}
    summary={'result_id':'K2209','checks':len(baseline),'passed':sum(baseline.values()),'coefficient_dimensions':dimensions,'fault_failure_counts':{k:len(v) for k,v in faults.items()}}
    if not args.selftest:
        root=args.root or Path(__file__).resolve().parents[2]
        dependencies=['explorations/conditional-build/k2209-spin-common-return-2026-10-28.md','explorations/conditional-build/k2206-changed-raw-mass-construction-2026-10-28.md','explorations/conditional-build/k2034-observed-principal-forms-2026-10-24.md','lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','lab/sources/selected-k77-trace-hq-connection-internal-chain-source-return-2026-08-12.md']
        report=dict(summary,status='conditional_complete_Spin_common_return_classification',checks=baseline,fault_failures=faults,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in dependencies},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal bottom-row intersection and exact inverse leakage proofs; complete Clifford support and rank calculations; full raw-row controls on every surviving basis; bounded-domain functional proofs in note. Internal only; no source selector, physical quotient, proof-assistant or external-expert claim.')
        destination=root/'lab/process/k2209-spin-common-return.json'
        if args.write:destination.write_text(json.dumps(report,indent=2)+'\n')
        else:assert json.loads(destination.read_text())==report,'stale K2209 report'
    print(json.dumps(summary,indent=2))
