#!/usr/bin/env python3
"""Exact full-copy Clifford parametrization and finite projection/readout controls.
Continuum density and locality statements are written proofs, not these samples.
"""
import k2206_changed_raw_mass_construction_probe as o
from fractions import Fraction as F
import sympy as s
FAULTS=['r_sign','s_correction','wrong_signature','missing_free_copy','wrong_reflection','local_readout']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    add,mul,scale=o.add,o.mul,o.scale;I=o.ONE;Z=o.ZERO
    free=[a for a in o.UN if a not in (10,11)]
    momenta=[{a:F(a-5,3) for a in o.UN},{a:F(2 if a==10 else 0) for a in o.UN},{a:F((-1)**a*(a+1),5) for a in o.UN}]
    for n,k in enumerate(momenta):
        D=add(scale(o.G[10],k[10]),scale(o.G[11],-k[11]));d=-(k[10]**2+k[11]**2)
        if fault=='wrong_signature':d=-d
        ck('D_square_'+str(n),mul(D,D)==scale(I,d))
        P={}
        for a in free:
            w={b:Z for b in o.UN};w[a]=scale(I,d)
            if fault=='missing_free_copy' and a==13:w[a]=Z
            M=add(scale(o.G[a],k[a]),scale(o.G[11],-k[11]))
            w[10]=scale(mul(D,M),1 if fault=='r_sign' else -1)
            w[11]=scale(I,-d) if fault=='s_correction' else add(scale(I,-d),scale(w[10],-1))
            P[a]=w
            ck(f'S_{n}_{a}',add(*w.values())==Z)
            ck(f'T_{n}_{a}',add(*[mul(scale(o.G[b],k[b]),w[b]) for b in o.UN])==Z)
            for b in free:ck(f'readback_{n}_{a}_{b}',scale(w[b],1/d)==(I if a==b else Z))
        if n==1:
            for a in free:
                ck('center_wr_'+str(a),P[a][10]==Z)
                ck('center_ws_'+str(a),P[a][11]==scale(I,4))
    # Finite paired-band projector: original reflection must be an involution.
    V=mul(o.G[1],o.G[10]) if fault!='wrong_reflection' else o.G[1]
    ck('reflection_involution',mul(V,V)==I);ck('reflection_symmetric',o.transpose(V)==V);ck('reflection_gamma10',mul(mul(V,o.G[10]),V)==scale(o.G[10],-1));ck('reflection_gamma1',mul(mul(V,o.G[1]),V)==scale(o.G[1],-1))
    # Exact two-frequency demonstration that representative evaluation need not descend.
    P=s.Matrix([[1,1],[1,1]])/2;n=s.Matrix([1,-1]);canonical=s.Matrix([[1,0]])*P
    read=s.Matrix([[1,0]]) if fault=='local_readout' else canonical
    ck('kernel_vector',P*n==s.zeros(2,1));ck('canonical_readout_descends',read*n==s.zeros(1,1))
    ck('raw_readout_does_not_descend',(s.Matrix([[1,0]])*n)[0]==1)
    # Scalar band kernel is an illustrative finite exact control, not the raw quotient proof.
    x=s.symbols('x',positive=True);kernel=2*s.sin(x)/x
    ck('band_kernel_far_nonzero',s.simplify(kernel.subs(x,3*s.pi/2))==-4/(3*s.pi))
    ck('band_kernel_near_nonzero',s.simplify(kernel.subs(x,s.pi/2))==4/s.pi)
    ck('parametrizer_input_dimension',len(free)*128==1024)
    ck('old_single_spinor_insufficient',128<1024)
    return out

RESULT='K2261'
REPORT='lab/process/k2261-band-quotient-local-observation.json'
DEPS=['explorations/conditional-build/k2261-band-quotient-local-observation-2026-10-29.md', 'tests/channel-swings/k2206_changed_raw_mass_construction_probe.py', 'explorations/conditional-build/k2258-variable-local-preparation-2026-10-29.md', 'explorations/conditional-build/k2255-local-constraint-stability-2026-10-29.md']
EVIDENCE='Finite exact algebra, rational resource and changed-input controls. Universal continuum/channel theorems are written proofs; hashes establish report provenance only.'

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
