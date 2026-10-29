#!/usr/bin/env python3
"""Sparse exact raw-Clifford, reflected-band and two-sided evolution controls."""
import k2206_changed_raw_mass_construction_probe as o
F=o.F
FAULTS=['single_reflection','wrong_V','mass_phase','wrong_G','projector_sign','one_sided_growth']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    add,mul,scale=o.add,o.mul,o.scale;I=o.ONE;Z=o.ZERO
    def cm(x,y):return(add(mul(x[0],y[0]),scale(mul(x[1],y[1]),-1)),add(mul(x[0],y[1]),mul(x[1],y[0])))
    def ca(x,y):return(add(x[0],y[0]),add(x[1],y[1]))
    def cs(x,q):return(scale(x[0],q),scale(x[1],q))
    def adj(x):return(o.transpose(x[0]),scale(o.transpose(x[1]),-1))
    one=(I,Z);zero=(Z,Z);V=mul(o.G[1],o.G[10]) if fault!='wrong_V' else o.G[1];v=(V,Z)
    ck('V_involution',mul(V,V)==I);ck('V_real_orthogonal',mul(o.transpose(V),V)==I);ck('V_symmetric',o.transpose(V)==V)
    A=mul(o.G[0],o.J);C={j:mul(o.G[0],o.G[j]) for j in range(1,14)}
    for j in range(14):ck('V_gamma_'+str(j),mul(mul(V,o.G[j]),V)==scale(o.G[j],-1 if j in [1,10] else 1))
    ck('mass_preserved',mul(mul(V,A),V)==A)
    k={j:F(0) for j in o.UN};k[1]=3;k[10]=4
    ks={j:(-x if j in ([1] if fault=='single_reflection' else [1,10]) else x) for j,x in k.items()}
    def h(a,kk):
        real=add(*[scale(C[j],(1-2*int(a==j))*kk[j]) for j in o.UN]);imag=scale(A,-3)
        return (add(real,imag),Z) if fault=='mass_phase' else (real,imag)
    def g(hh):
        return cs(ca(one,cs(cm(adj(hh),hh),F(1,16 if fault!='wrong_G' else 17))),F(1,2))
    for a in o.UN:
        H=h(a,k);Hs=h(a,ks);G=g(H);Gs=g(Hs)
        ck('square_'+str(a),cm(H,H)==cs(one,16))
        ck('reflection_H_'+str(a),cm(cm(v,H),v)==Hs)
        ck('reflection_G_'+str(a),cm(cm(v,G),v)==Gs)
        ck('G_adjoint_'+str(a),cm(adj(H),G)==cm(G,H))
        ck('G_hermitian_'+str(a),adj(G)==G)
        ck('T_intertwiner_'+str(a),mul(scale(o.G[a],ks[a]),V)==mul(V,scale(o.G[a],k[a])))
    # Two-fibre matrices of Clifford pairs, avoiding dense256 matrices.
    def bm(X,Y):return [[ca(cm(X[i][0],Y[0][j]),cm(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
    R=[[zero,v],[v,zero]];ident=[[one,zero],[zero,one]]
    P=[[cs(one,F(1,2)),cs(v,F(1,2))],[cs(v,F(1,2)),cs(one,F(1,2))]]
    if fault=='projector_sign':P[1][0]=cs(v,F(-1,2))
    ck('paired_R_involution',bm(R,R)==ident);ck('paired_projection',bm(P,P)==P)
    Hpair=[[h(3,k),zero],[zero,h(3,ks)]]
    ck('paired_commutation',bm(P,Hpair)==bm(Hpair,P))
    mult=[[one,zero],[zero,cs(one,2)]]
    ck('not_fibrewise',bm(P,mult)!=bm(mult,P))
    # Exact unstable raw projectors and opposite-time growth, not finite evidence for the continuum theorem.
    H=(scale(C[1],5),scale(A,-3));D=(scale(H[1],F(1,4)),scale(H[0],F(-1,4)))
    Qp=cs(ca(one,D),F(1,2));Qm=cs(ca(one,cs(D,-1)),F(1,2))
    if fault=='one_sided_growth':Qm=Qp
    ck('unstable_square',cm(H,H)==cs(one,-16));ck('unstable_split',ca(Qp,Qm)==one)
    ck('unstable_projector_plus',cm(Qp,Qp)==Qp);ck('unstable_projector_minus',cm(Qm,Qm)==Qm)
    ck('growing_eigenvalue',cm(H,Qp)==(scale(Qp[1],-4),scale(Qp[0],4)))
    expected_minus=(scale(Qm[1],4),scale(Qm[0],-4))
    ck('opposite_time_eigenvalue',cm(H,Qm)==expected_minus)
    ck('stable_band_center_lambda',4**2-3**2+3**2==16)
    return out

RESULT='K2258'
REPORT='lab/process/k2258-variable-local-preparation.json'
DEPS=['explorations/conditional-build/k2258-variable-local-preparation-2026-10-29.md', 'tests/channel-swings/k2206_changed_raw_mass_construction_probe.py', 'explorations/conditional-build/k2254-raw-nonparallel-domain-2026-10-29.md', 'explorations/conditional-build/k2255-local-constraint-stability-2026-10-29.md']
EVIDENCE='Finite exact algebra and rational controls; changed mathematical/resource inputs must fail unchanged checks. Universal proofs and report hashes are separate evidence.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args()
    root=Path(__file__).resolve().parents[2];checks=controls()
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for f in FAULTS:
        bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected input fault',f);faults[f]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'report drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
