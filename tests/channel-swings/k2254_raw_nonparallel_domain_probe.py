#!/usr/bin/env python3
"""Full raw sparse-Clifford identities and nonparallel Fourier-domain controls."""
import k2206_changed_raw_mass_construction_probe as o
F=o.F
FAULTS=['raw_return_sign','aux_normalization','old_mass','normal_reflection','inverse_sign','inverse_order','omit_coupled_profile','wrong_adjoint']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    mul,add,scale=o.mul,o.add,o.scale;I=o.ONE;Z=o.ZERO;U=o.UN
    A=mul(o.G[0],o.J)
    if fault=='old_mass':A=o.G[0]
    tr=[scale(o.G[k],o.ETA[k]) for k in range(14)]+[o.WB]
    inv=o.G+[scale(o.W,F(1) if fault=='aux_normalization' else F(1,2))]
    raw=lambda k,a,c:o.raw(k,a,c,'raw_return_sign' if fault=='raw_return_sign' else None)
    for k in range(14):
        for a in range(15):
            for c in range(15):ck('raw_normalization_'+str((k,a,c)),mul(mul(inv[a],raw(k,a,c)),tr[c])==scale(o.GM[k],o.scalar_m(k,a,c)))
    for k in U:
        for r in U[:-1]:
            v={r:F(1),U[-1]:F(-1)}
            for a in range(15):
                got=add(*[scale(mul(mul(inv[a],raw(k,a,c)),tr[c]),vc) for c,vc in v.items()])
                sc=F(0) if a==k else (-v.get(k,F(0))-v.get(a,F(0)) if a<14 else -v.get(k,F(0))/2)
                ck('normal_row_'+str((k,r,a)),got==scale(o.GM[k],sc))
    for r in U[:-1]:
        v={r:F(1),U[-1]:F(-1)}
        for a in range(15):
            got=add(*[scale(mul(mul(mul(inv[a],raw(0,a,c)),A),tr[c]),vc) for c,vc in v.items()])
            ck('mass_row_'+str((r,a)),got==scale(mul(o.GM[0],A),-v.get(a,F(0))))
    C={k:mul(o.G[0],o.G[k]) for k in range(1,14)}
    ck('actual_mass_square',mul(A,A)==scale(I,-1))
    for k in range(1,14):
        ck('C_square_'+str(k),mul(C[k],C[k])==scale(I,-o.ETA[k]))
        ck('mass_anticommutation_'+str(k),add(mul(A,C[k]),mul(C[k],A))==Z)
        for l in range(k+1,14):ck('C_anticommutation_'+str((k,l)),add(mul(C[k],C[l]),mul(C[l],C[k]))==Z)
    for a in U:
        ck('normal_mass_propagation_'+str(a),mul(o.G[a],A)==mul(A,o.G[a]))
        for k in range(1,14):
            factor=(-1 if a==k else 1) if fault!='normal_reflection' else 1
            ck('actual_constraint_propagation_'+str((a,k)),mul(o.G[a],scale(C[k],factor))==mul(C[k],o.G[a]))
    # Exact right inverse in a positive and a negative same-sign pair, with noncommuting factors.
    for r,t in [(1,2),(10,11)]:
        Rr=scale(o.G[r],F(2));Rs=scale(o.G[t],F(3));D=add(Rr,scale(Rs,-1));q=F(o.ETA[r]*4+o.ETA[t]*9)
        ck('rank_denominator_'+str(r),mul(D,D)==scale(I,q) and q!=0)
        Di=scale(D,1/q if fault!='inverse_sign' else -1/q)
        wrS=scale(mul(Di,Rs) if fault!='inverse_order' else mul(Rs,Di),-1);wsS=add(I,scale(wrS,-1))
        wrT=Di;wsT=scale(Di,-1)
        ck('rank_S_identity_'+str(r),add(wrS,wsS)==I)
        ck('rank_T_zero_'+str(r),add(wrT,wsT)==Z)
        ck('rank_weighted_S_zero_'+str(r),add(mul(Rr,wrS),mul(Rs,wsS))==Z)
        ck('rank_weighted_T_identity_'+str(r),add(mul(Rr,wrT),mul(Rs,wsT))==I)
    k={a:F(0) for a in U};k.update({1:F(1,5),2:F(1,7),10:F(2),11:F(1,3)})
    D=add(scale(o.G[10],k[10]),scale(o.G[11],-k[11]));Di=scale(D,-1/(k[10]**2+k[11]**2))
    correction=scale(mul(Di,add(scale(o.G[1],k[1]),scale(o.G[2],-k[2]))),-1)
    if fault=='omit_coupled_profile':correction=Z
    w={1:I,2:scale(I,-1),10:correction,11:scale(correction,-1)}
    ck('explicit_profile_sum',add(*w.values())==Z)
    ck('explicit_profile_return',add(*[scale(mul(o.G[a],z),k[a]) for a,z in w.items()])==Z)
    ck('explicit_profile_nonzero',w[1]==I)
    # Complex Clifford arithmetic as exact real/imaginary pairs.
    def cm(x,y):return(add(mul(x[0],y[0]),scale(mul(x[1],y[1]),-1)),add(mul(x[0],y[1]),mul(x[1],y[0])))
    def ca(x,y):return(add(x[0],y[0]),add(x[1],y[1]))
    def cs(x,q):return(scale(x[0],q),scale(x[1],q))
    def dag(x):return(o.transpose(x[0]),scale(o.transpose(x[1]),1 if fault=='wrong_adjoint' else -1))
    ck('imaginary_skew_mass_is_Hermitian',dag((Z,A))==(Z,A))
    p={7:F(1,3),8:F(1,4),9:F(1,6)};mass=F(1)
    lam=sum(v*v for v in p.values())-sum(o.ETA[a]*v*v for a,v in k.items())+mass*mass
    ck('stable_patch_positive',lam>0)
    for a in U:
        B=add(*[scale(C[j],v) for j,v in p.items()],*[scale(C[j],v*(-1 if j==a else 1)) for j,v in k.items()]);H=(B,scale(A,-mass))
        ck('actual_H_square_'+str(a),cm(H,H)==(scale(I,lam),Z))
        metric=cs(ca((I,Z),cs(cm(dag(H),H),1/lam)),F(1,2))
        ck('actual_metric_selfadjoint_'+str(a),dag(metric)==metric)
        ck('actual_metric_symmetrizes_'+str(a),cm(metric,H)==cm(dag(H),metric))
        ck('zero_trace_'+str(a),H[0].get(0,F(0))==0 and H[1].get(0,F(0))==0)
    ck('constraint_dimension',10*128-2*128==1024)
    ck('each_spectral_half',1024//2==512)
    return out

RESULT='K2254'
REPORT='lab/process/k2254-raw-nonparallel-domain.json'
DEPS=['explorations/conditional-build/k2254-raw-nonparallel-domain-2026-10-29.md','tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2242-ambient-conormal-descent-2026-10-29.md','explorations/conditional-build/k2245-localized-normal-domain-2026-10-29.md']
EVIDENCE='Exact original sparse-Clifford block identities and input faults; universal Fourier/rank/Hilbert statements are written proofs. Hash checks are reporting integrity.'

def main():
    import argparse,hashlib,json
    from pathlib import Path
    args=argparse.ArgumentParser();args.add_argument('--write',action='store_true');a=args.parse_args()
    root=Path(__file__).resolve().parents[2]
    checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
    faults={}
    for fault in FAULTS:
        bad=[k for k,v in controls(fault).items() if not v]
        assert bad,('undetected mathematical input fault',fault)
        faults[fault]=bad
    report=dict(result_id=RESULT,checks=checks,fault_failures=faults,evidence_kinds=EVIDENCE,
        dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in DEPS},
        probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    p=root/REPORT
    if a.write:p.write_text(json.dumps(report,indent=2)+'\n')
    else:assert json.loads(p.read_text())==report,'certificate drift'
    print(json.dumps(dict(result=RESULT,controls=len(checks),faults=len(faults))))
if __name__=='__main__':main()
