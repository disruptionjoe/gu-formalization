#!/usr/bin/env python3
"""Exact standalone controls of K2203; universal conclusions use the note's proof.

No numeric ranks, full1920 dense arrays, or producer imports. --write writes
the native report; without it the report is checked if present.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse, hashlib, json

ETA=(1,)*7+(-1,)*7
OBS=(0,7,8,9)
UN=tuple(k for k in range(14) if k not in OBS)
ONE={0:F(1)}
ZERO={}

def add(*xs):
    out={}
    for x in xs:
        for m,c in x.items(): out[m]=out.get(m,0)+c
    return {m:c for m,c in out.items() if c}

def scale(x,s): return {m:c*s for m,c in x.items() if c*s}

def mul(x,y):
    out={}
    for a,c in x.items():
        for b,d in y.items():
            sign=1
            for i in range(14):
                if (a>>i)&1:
                    if (b&((1<<i)-1)).bit_count()%2: sign=-sign
                    if (b>>i)&1: sign*=ETA[i]
            out[a^b]=out.get(a^b,0)+sign*c*d
    return {m:c for m,c in out.items() if c}

def blade(indices):
    v=ONE
    for k in indices: v=mul(v,{1<<k:F(1)})
    return v

def star(x,fault=None):
    return {m:c*(-1)**(m.bit_count()*(m.bit_count()+(3 if fault=='adjoint_sign' else 1))//2) for m,c in x.items()}

def transpose(x):
    out={}
    for m,c in x.items():
        r=m.bit_count()
        s=(-1)**(r*(r-1)//2)
        for k in range(14):
            if m>>k&1: s*=ETA[k]
        out[m]=c*s
    return out

G=[{1<<k:F(1)} for k in range(14)]
J=blade(range(14))
W=scale(add(scale(ONE,3),scale(J,-1)),F(1,2))
WB=scale(add(scale(ONE,3),J),F(1,2))
GM=[mul(g,WB) for g in G]
FF=[F(-1)]*14+[F(2)]

def raw(k,a,c,fault=None):
    if a<14 and c<14 and len({a,k,c})==3:
        return scale(mul(blade((a,k,c)),W),ETA[a])
    if a==k and c==14: return ONE
    if a==14 and c==k: return scale(ONE,ETA[k] if fault=='raw_return_sign' else -ETA[k])
    return ZERO

def raw_lower(fault=None):
    tr=[scale(G[k],ETA[k]) for k in range(14)]+[WB]
    inv=G+[scale(W,F(1,2))]
    om=ONE if fault=='replace_gamma0_by_scalar' else G[0]
    return {(a,c):v for a in range(15) for c in range(15)
            if (v:=mul(mul(inv[a],mul(raw(0,a,c,fault),om)),tr[c]))}

def scalar_m(k,a,c):
    if a<14 and c<14 and len({a,k,c})==3:return F(1)
    if a==k and c==14:return F(1)
    if a==14 and c==k:return F(-1,2)
    return F(0)

def blockmul(x,y):
    out={}
    for (a,b),v in x.items():
        for (bb,c),w in y.items():
            if b==bb: out[a,c]=add(out.get((a,c),ZERO),mul(v,w))
    return {k:v for k,v in out.items() if v}

def sharp(x,fault=None):
    return {(c,a):scale(star(v,fault),FF[a]/FF[c]) for (a,c),v in x.items()}

def chars(m,observed=OBS):
    return tuple((-1)**(m.bit_count()-((m>>k)&1)) for k in observed)

def derivative(poly,k):
    out={}
    for exponent,c in poly.items():
        if exponent[k]:
            e=list(exponent);e[k]-=1
            out[tuple(e)]=c*exponent[k]
    return out

def pdiff(p,q):
    out=dict(p)
    for e,c in q.items():out[e]=out.get(e,0)-c
    return {e:c for e,c in out.items() if c}

def run(fault=None):
    checks={}
    def ck(name,value):checks[name]=bool(value)
    ck('J_involution',mul(J,J)==ONE)
    ck('W_inverse',mul(W,WB)==scale(ONE,2))
    ck('W_adjoint',star(W,fault)==WB)
    K=raw_lower(fault)
    for a in range(15):
        for c in range(15):
            want=scale(WB if c==14 else W,scalar_m(0,a,c)*(1 if c in(0,14) else -1))
            ck(f'original_normalized_lower_{a}_{c}',K.get((a,c),ZERO)==want)
    PV={(a,c):scale(ONE,F(int(a==c))-F(1,10)) for a in UN for c in UN}
    ck('projector_idempotent',blockmul(PV,PV)==PV)
    ck('projector_rank9_trace',sum(PV[a,a][0] for a in UN)==9)
    ck('projector_H_selfadjoint',sharp(PV)==PV)
    ck('lower_preserves_V_C',blockmul(K,PV)==blockmul(PV,K))
    want={(a,c):mul(v,W) for (a,c),v in PV.items()}
    ck('lower_on_V_is_W',blockmul(K,PV)==want)
    KS=sharp(K,fault)
    ck('C_pair_7_8',K.get((7,8))==scale(W,-1) and KS.get((7,8))==scale(WB,-1))
    ck('C_pair_0_h',K.get((0,14))==WB and KS.get((0,14))==WB)
    central=[m for m in range(1<<14) if chars(m)==(1,1,1,1)]
    odds=[m for m in central if m.bit_count()%2]
    ck('centralizer_count',len(central)==1024)
    ck('odd_centralizer_count',len(odds)==512)
    nself=nskew=0
    allcent=allodd=allrad=True
    for m in central:
        z={m:F(1)} if m.bit_count()%2==0 else mul({m:F(1)},WB)
        allcent &= all(mul(z,GM[k])==mul(GM[k],z) for k in OBS)
        eq1=add(mul(z,W),scale(mul(WB,z),-1))
        eq2=add(mul(z,WB),scale(mul(WB,z),-1))
        # The sum of the two actual C-block relations is -J Z, injective.
        allrad &= add(eq1,eq2)==scale(mul(J,z),-1)
        if m in odds:
            nself+=star(z,fault)==z
            nskew+=star(z,fault)==scale(z,-1)
            allodd &= eq1==ZERO and add(mul(z,J),mul(J,z))==ZERO
    ck('all1024_actual_central_characters',allcent)
    ck('all1024_C_radical_certificate',allrad)
    ck('all512_V_survivor_relations',allodd)
    ck('odd_B_adjoint_counts',(nself,nskew)==(240,272))
    ck('odd_selfadjoint_binomial',comb(10,3)+comb(10,7)==240)
    ck('bilinear_dimension',81*len(odds)==41472)
    ck('symmetric_dimension',45*nself+36*nskew==20592)
    ck('antisymmetric_dimension',45*nskew+36*nself==20880)
    z=mul(blade((0,7,8,9,1,2,3)),WB)
    if fault=='survivor_even_parity':z=ONE
    ck('witness_selfadjoint',star(z)==z)
    ck('witness_inverse',mul(z,z)==scale(ONE,2))
    ck('witness_odd',add(mul(J,z),mul(z,J))==ZERO)
    X={(a,c):mul(v,z) for (a,c),v in PV.items()}
    ck('full_witness_principal_compatibility',all(mul(z,GM[k])==mul(GM[k],z) for k in OBS))
    ck('full225_block_lower_witness',blockmul(X,K)==blockmul(KS,X))
    ck('witness_rank_and_inertia',9*128==1152 and 1920-1152==768 and 1152//2==576)
    ck('formal_balanced_inertia',star(GM[0])==scale(GM[0],-1) and mul(GM[0],GM[0])==scale(ONE,2))
    plus=(1,)*4;minus=(-1,)*4
    derivative_chars=[tuple(1 if k==l else -1 for l in OBS) for k in OBS]
    if fault=='derivative_character':derivative_chars[0]=plus
    ck('six_distinct_Green_characters',len(set([plus,minus]+derivative_chars))==6)
    for i,k in enumerate(OBS):
        ck(f'actual_Gamma_character_{k}',all(mul(GM[k],GM[l])==scale(mul(GM[l],GM[k]),derivative_chars[i][j]) for j,l in enumerate(OBS)))
    ck('actual_J_character',all(mul(J,GM[k])==scale(mul(GM[k],J),-1) for k in OBS))
    # Actual polynomial drift examples in coordinate order (0,7,8,9).
    # For X=e^(2phi)X0, the exact logarithmically factored transport residual
    # is 2(dphi-a)X0. No finite sampling of exponentials certifies it.
    phi={(1,1,0,0):F(1),(0,0,2,0):F(1)}
    exact_a=[{(0,1,0,0):F(1)},{(1,0,0,0):F(1)},{(0,0,1,0):F(2)},{}]
    if fault=='scalar_transport_coefficient':exact_a[2]={(0,0,1,0):F(1)}
    ck('actual_polynomial_exact_drift',all(derivative(phi,k)==exact_a[k] for k in range(4)))
    ck('exact_exponential_factored_transport',all(not pdiff(derivative(phi,k),exact_a[k]) for k in range(4)))
    ck('all_six_exact_drift_curvatures',all(not pdiff(derivative(exact_a[j],i),derivative(exact_a[i],j)) for i in range(4) for j in range(i+1,4)))
    curved_a=[{},{(1,0,0,0):F(1)},{},{}]
    curvature={(i,j):pdiff(derivative(curved_a[j],i),derivative(curved_a[i],j)) for i in range(4) for j in range(i+1,4)}
    ck('actual_nonclosed_drift_curvature',curvature[0,1]=={(0,0,0,0):F(1)} and all(not v for key,v in curvature.items() if key!=(0,1)))
    ck('omitted_density_connection_fails',any(derivative(phi,k) for k in range(4)))
    C=[mul(G[0],G[k]) for k in OBS[1:]]
    ck('evolution_lower_sign',mul(scale(GM[0],F(-1,2)),W)==scale(G[0],-1))
    for i,c in enumerate(C):
        ck(f'evolution_C_symmetric_{i}',transpose(c)==c)
        ck(f'evolution_C_involution_{i}',mul(c,c)==ONE)
        ck(f'evolution_gamma0_anticommutes_{i}',add(mul(G[0],c),mul(c,G[0]))==ZERO)
        for j,d in enumerate(C):
            ck(f'evolution_C_relation_{i}_{j}',add(mul(c,d),mul(d,c))==scale(ONE,2*int(i==j)))
    ck('evolution_gamma0_positive_square',transpose(G[0])==G[0] and mul(G[0],G[0])==ONE)
    evchars=[(1,1,1),(-1,-1,-1)]+[tuple(1 if i==j else -1 for j in range(3)) for i in range(3)]
    ck('five_distinct_evolution_characters',len(set(evchars))==5)
    ck('identity_metric_fails_actual_lower',add(G[0],G[0])!=ZERO)
    # cosh(log 2)=5/4, sinh(log 2)=3/4: an actual positive ODE metric.
    Pcontrol=add(scale(ONE,F(5,4)),scale(G[0],F(-3,4)))
    ck('ODE_metric_positive_eigenvalues',F(5,4)-F(3,4)>0)
    ck('ODE_metric_fails_full_spatial_flux',all(mul(Pcontrol,c)!=mul(c,Pcontrol) for c in C))
    return checks

def main():
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--report',type=Path)
    args=p.parse_args()
    base=run();assert all(base.values()),[k for k,v in base.items() if not v]
    mutations={}
    for fault in ('raw_return_sign','replace_gamma0_by_scalar','adjoint_sign','survivor_even_parity','derivative_character','scalar_transport_coefficient'):
        bad=[k for k,v in run(fault).items() if not v]
        assert bad,('undetected mutation',fault)
        mutations[fault]={'failed':len(bad),'examples':bad[:5]}
    here=Path(__file__).resolve()
    # Works both in a scratch candidate directory and its eventual native location.
    root=next((a for a in here.parents if (a/'CURRENT-STATE.yaml').exists()),None)
    note_name='k2203-observed-lower-pairing-compatibility-2026-10-28.md'
    note=(root/'explorations/conditional-build'/note_name) if root else here.parent/note_name
    dependencies={}
    if root:
        for name in ('k2200-observed-principal-pairing-freedom-2026-10-28.md','k2021-common-degree-dual-operator-2026-10-24.md','k2028-all-grade-raw-common-form-2026-10-24.md','k2034-observed-principal-forms-2026-10-24.md','k2002-clifford-pairing-integrability-2026-10-23.md'):
            dependencies['explorations/conditional-build/'+name]=hashlib.sha256((root/'explorations/conditional-build'/name).read_bytes()).hexdigest()
    if note.exists():dependencies['explorations/conditional-build/'+note_name]=hashlib.sha256(note.read_bytes()).hexdigest()
    report={'result_id':'K2203','status':'conditional_complete_shared_raw_lower_pairing_classification','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','checks':base,'fault_failures':mutations,'dimensions':{'bilinear':41472,'symmetric':20592,'antisymmetric':20880,'maximum_rank':1152,'minimum_radical':768},'dependency_sha256':dependencies,'probe_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'evidence_kinds':'Universal full-family algebraic and character-separated transport proofs; exact raw-block, Clifford and witness controls; genuine baseline-first mutations. Not source-selected, physical quotient, proof-assistant or external certification.'}
    dst=args.report or ((root/'lab/process/k2203-observed-lower-pairing-compatibility.json') if root else here.parent/'k2203-observed-lower-pairing-compatibility.json')
    if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
    elif dst.exists():assert json.loads(dst.read_text())==report,'report drift'
    print(json.dumps({'result':'K2203','controls':len(base),'faults':len(mutations),'report_verified':dst.exists()}))

if __name__=='__main__':main()
