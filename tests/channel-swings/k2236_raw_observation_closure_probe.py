#!/usr/bin/env python3
"""K2236 exact raw/quotient controls; universal scope is in the written proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2206_changed_raw_mass_construction_probe as o
import argparse,hashlib,json
F=o.F; I=o.ONE; Z=o.ZERO
FAULTS=['raw_return','average','leakage','quotient','mass_sign','jordan_half']
def ident(n):return [[F(a==c) for c in range(n)] for a in range(n)]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def minus(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def rank(a):
    a=[r[:] for r in a];p=0
    for c in range(len(a[0])):
        k=next((k for k in range(p,len(a)) if a[k][c]),None)
        if k is None:continue
        a[p],a[k]=a[k],a[p];z=a[p][c];a[p]=[x/z for x in a[p]]
        for k in range(len(a)):
            if k!=p:
                z=a[k][c];a[k]=[x-z*y for x,y in zip(a[k],a[p])]
        p+=1
    return p
def scalar_block(a,z=I):return {(r,c):o.scale(z,a[r][c]) for r in range(len(a)) for c in range(len(a[0])) if a[r][c]}
def run(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    Q=[[F(c==a) for c in range(15)] for a in [0,7,8,9,14]]
    E=[[F(0) for c in range(6)] for a in range(15)]
    for r,a in enumerate([0,7,8,9]):E[a][r]=1
    for a in o.UN:E[a][4]=1
    E[14][5]=1
    R=[[F(0) for c in range(15)] for a in range(6)]
    for r,a in enumerate([0,7,8,9]):R[r][a]=1
    for c in o.UN:R[4][c]=F(1,9 if fault=='average' else 10)
    R[5][14]=1
    PV=minus(ident(15),mm(E,R))
    ck('refinement_rank768',rank(R)==6)
    ck('pullback_rank640',rank(Q)==5)
    ck('RE_identity',mm(R,E)==ident(6))
    ck('PV_idempotent',mm(PV,PV)==PV)
    ck('PV_rank1152',rank(PV)==9)
    ck('pullback_kills_V',not any(map(any,mm(Q,PV))))
    tr=[o.scale(o.G[k],o.ETA[k]) for k in range(14)]+[o.WB]
    inv=o.G+[o.scale(o.W,F(1,2))]
    MS={k:[[o.scalar_m(k,a,c) for c in range(15)] for a in range(15)] for k in o.OBS}
    # Explicit inverse follows directly from M0's auxiliary plane and J13-I13 block.
    MI=[[F(0) for c in range(15)] for a in range(15)]
    MI[0][14]=-2;MI[14][0]=1
    for a in range(1,14):
        for c in range(1,14):MI[a][c]=F(1,12)-F(a==c)
    ck('M0_inverse',mm(MI,MS[0])==ident(15))
    for k in o.OBS:
        raw={(a,c):v for a in range(15) for c in range(15) if (v:=o.mul(o.mul(inv[a],o.raw(k,a,c,'raw_return_sign' if fault=='raw_return' else None)),tr[c]))}
        ck('raw_principal_'+str(k),raw==scalar_block(MS[k],o.GM[k]))
        ck('principal_V_invariance_'+str(k),mm(PV,MS[k])==mm(MS[k],PV))
    T=o.blade(o.UN);A=o.mul(o.G[0],o.J)
    C={j:o.mul(o.G[0],o.G[j]) for j in o.OBS[1:]}
    Xi={j:o.mul(C[j],T) for j in C}
    PB=scalar_block(PV);EB=scalar_block(E);RB=scalar_block(R)
    D0inv=scalar_block(MI,o.scale(o.GM[0],F(1,2)))
    for name,k,om in [('mass',0,A),*[(str(j),0,Xi[j]) for j in C],('b',7,Xi[7])]:
        K={(a,c):v for a in range(15) for c in range(15) if (v:=o.mul(o.mul(inv[a],o.mul(o.raw(k,a,c,'raw_return_sign' if fault=='raw_return' else None),om)),tr[c]))}
        ck('raw_return_'+name,o.mul(o.raw(k,14,k,'raw_return_sign' if fault=='raw_return' else None),om)==o.scale(om,-o.ETA[k]))
        ck('lower_V_C_'+name,o.blockmul(PB,K)==o.blockmul(K,PB))
        NN=o.blockmul(D0inv,K);NC=o.blockmul(o.blockmul(RB,NN),EB)
        ck('quotient_lower_intertwining_'+name,o.blockmul(NN,EB)==o.blockmul(EB,NC))
        if name=='mass':
            auxiliary=o.mul(A,o.scale(o.mul(o.WB,o.WB),F(1,2)))
            expected={(r,r):(o.scale(A,1 if fault=='mass_sign' else -1) if r==0 else A if r<5 else auxiliary) for r in range(6)}
            ck('exact_mass_quotient',NC==expected)
            hidden={(a,0):I for a in o.UN}
            ck('unseen_zero_momentum_mass',o.blockmul(scalar_block(Q),o.blockmul(NN,hidden))=={})
    for j in range(1,4):
        def tj(x):
            a=x[0];b=x[1:4];v=x[4];h=x[5];other=sum(b[l-1] for l in range(1,4) if l!=j)
            vp=(h+2*v-other)/12
            y=[F(0)]*6;y[0]=b[j-1];y[4]=vp;y[5]=other+10*v
            for l in range(1,4):y[l]=b[l-1]-v+vp if l!=j else a+other+9*v-h+vp
            return y
        TT=[list(r) for r in zip(*(tj([F(c==a) for c in range(6)]) for a in range(6)))]
        if fault=='quotient':TT[5][4]+=1
        evolution=mm(MI,MS[o.OBS[j]])
        ck('exact_six_slot_'+str(j),mm(evolution,E)==mm(E,TT))
        ck('kernel_invariance_'+str(j),mm(evolution,PV)==mm(PV,evolution))
        # Hidden normalized normal-slot seed with sigma=1; exact observed principal response.
        hidden=[[F(a==o.UN[0])] for a in range(15)]
        leak=mm(mm(Q,evolution),hidden)
        expected=[[F(0)],[F(11 if fault!='leakage' else 10,12) if j==1 else F(-1,12)],[F(11,12) if j==2 else F(-1,12)],[F(11,12) if j==3 else F(-1,12)],[F(1)]]
        ck('hidden_sum_leakage_'+str(j),leak==expected)
        N=minus(mm(TT,TT),ident(6))
        ck('Jordan_rank1_'+str(j),rank(N)==1)
        ck('Jordan_square_zero_'+str(j),not any(map(any,mm(N,N))))
        factor=F(1) if fault=='jordan_half' else F(1,2)
        S=mm(TT,minus(ident(6),[[factor*x for x in r] for r in N]))
        ck('semisimple_involution_'+str(j),mm(S,S)==ident(6))
        ck('semisimple_commutation_'+str(j),mm(S,N)==mm(N,S))
        ck('exact_Jordan_decomposition_'+str(j),minus(TT,S)==[[x/2 for x in r] for r in mm(S,N)])
    # Contrary ambient control: the fixed-plane kernel is not invariant under a normal derivative.
    normal=[[o.scalar_m(o.UN[0],a,c) for c in range(15)] for a in range(15)]
    ck('normal_derivative_breaks_fixed_plane_kernel',any(map(any,mm(mm(Q,normal),PV))))
    # Algebraic raw response is not measured time response: it directly exposes sigma.
    qd0=mm(Q,MS[0]);ck('principal_response_rank768',rank(Q+qd0)==6)
    return out
def main():
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args()
    checks=run();assert all(checks.values()),[k for k,v in checks.items() if not v]
    failures={}
    for f in FAULTS:
        bad=[k for k,v in run(f).items() if not v];assert bad,('undetected',f);failures[f]=bad
    deps=['explorations/conditional-build/k2236-raw-observation-closure-2026-10-29.md','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2034-observed-principal-forms-2026-10-24.md','explorations/conditional-build/k2233-degree-dependent-raw-pairing-2026-10-29.md','lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md']
    report=dict(result_id='K2236',status='conditional_fixed_plane_minimal_dynamic_refinement',checks=checks,fault_failures=failures,dependency_sha256={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Exact raw and six-slot identities; universal written kernel/rank/current/descent proofs; massless one-dimensional Fourier consumer only; no source observation or physical quotient selection.')
    dest=ROOT/'lab/process/k2236-raw-observation-closure.json'
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(dest.read_text())==report,'certificate drift'
    print(json.dumps(dict(result='K2236',controls=len(checks),faults=len(failures))))
if __name__=='__main__':main()
