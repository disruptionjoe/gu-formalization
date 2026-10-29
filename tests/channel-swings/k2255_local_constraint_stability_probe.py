#!/usr/bin/env python3
"""Exact raw-Clifford compact-data and growing-mode controls."""
import k2206_changed_raw_mass_construction_probe as o
F=o.F
FAULTS=['mass_sign','omit_coupled_copy','inverse_order','wrong_growing_sign','spatial_signature','quotient_not_complex']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    mul,add,scale=o.mul,o.add,o.scale;I=o.ONE;Z=o.ZERO
    A=mul(o.G[0],o.J);C=mul(o.G[0],o.G[1])
    def cm(x,y):return(add(mul(x[0],y[0]),scale(mul(x[1],y[1]),-1)),add(mul(x[0],y[1]),mul(x[1],y[0])))
    def ca(x,y):return(add(x[0],y[0]),add(x[1],y[1]))
    def cs(x,q):return(scale(x[0],q),scale(x[1],q))
    H=(scale(C,5),scale(A,-3))
    if fault=='mass_sign':H=(add(scale(C,5),scale(A,-3)),Z)
    ck('actual_unstable_square',cm(H,H)==(scale(I,-16),Z))
    # H/(4i)=(imag(H)/4,-real(H)/4).
    D=(scale(H[1],F(1,4)),scale(H[0],F(-1,4)))
    Q=cs(ca((I,Z),D),F(1,2))
    if fault=='wrong_growing_sign':Q=cs(ca((I,Z),cs(D,-1)),F(1,2))
    ck('projector_idempotent',cm(Q,Q)==Q)
    ck('growing_eigenvalue',cm(H,Q)==(scale(Q[1],-4),scale(Q[0],4)))
    ck('projector_rank64_from_trace',Q[0].get(0,F(0))*128==64 and Q[1].get(0,F(0))==0)
    ck('C1_square_negative',mul(C,C)==scale(I,-1))
    ck('mass_square_negative',mul(A,A)==scale(I,-1))
    ck('mass_anticommutes',add(mul(A,C),mul(C,A))==Z)
    for a,b,c,d in [(1,2,3,4),(2,-1,4,1),(0,3,2,5),(3,0,5,-2)]:
        R=add(scale(o.G[1],a),scale(o.G[2],-b));M=add(scale(o.G[3],c),scale(o.G[4],-d));q=F(a*a+b*b)
        if fault=='spatial_signature':q=F(a*a-b*b)
        RM=mul(M,R) if fault=='inverse_order' else mul(R,M)
        w={1:scale(RM,-1),2:RM,3:scale(I,q),4:scale(I,-q)}
        if fault=='omit_coupled_copy':w[2]=Z
        ck('local_S_'+str((a,b)),add(*w.values())==Z)
        ck('local_T_'+str((a,b)),add(*[scale(mul(o.G[j],w[j]),k) for j,k in zip([1,2,3,4],[a,b,c,d])])==Z)
        ck('local_image_nonzero_'+str((a,b)),w[3]!=Z)
        ck('rank_patch_'+str((a,b)),mul(R,R)==scale(I,q))
    # Polynomial-rank algebra control; quotient complex condition is independent.
    import sympy as s
    x=s.symbols('x',real=True);Dmat=s.Matrix([[x,0],[0,x+1]])
    ck('minor_nonzero_polynomial',s.expand(Dmat.det())==x*x+x)
    ck('generic_full_rank',Dmat.rank()==2)
    ck('exceptional_rank_drop',Dmat.subs(x,0).rank()==1)
    Dc=s.Matrix([[x,0]]);P=s.Matrix([0,x])
    if fault=='quotient_not_complex':P=s.Matrix([x,0])
    ck('quotient_DP_zero',Dc*P==s.zeros(1,1))
    ck('quotient_generic_rank_sum',Dc.rank()+P.rank()==2)
    ck('quotient_exceptional_rank_drop',Dc.subs(x,0).rank()+P.subs(x,0).rank()==0)
    for R in [5,10,20,100]:ck('rho_lower_'+str(R),R*R-9>=F(R*R,4))
    return out

RESULT='K2255'
REPORT='lab/process/k2255-local-constraint-stability.json'
DEPS=['explorations/conditional-build/k2255-local-constraint-stability-2026-10-29.md', 'tests/channel-swings/k2206_changed_raw_mass_construction_probe.py', 'explorations/conditional-build/k2254-raw-nonparallel-domain-2026-10-29.md']
EVIDENCE="Finite exact algebra, changed-input faults and rational resource controls; universal proofs are written separately. Hashes check reporting integrity."

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
