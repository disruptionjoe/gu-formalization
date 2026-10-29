#!/usr/bin/env python3
"""Exact compatible connection, whole Gram, rank and hypothesis countercontrols."""
import sympy as s
FAULTS=['positive_form','wrong_connection_sign','wrong_null_line','missing_normalization','wrong_metric_growth','omit_connection_component']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    y,z=s.symbols('y z',real=True);beta=s.Integer(2)
    G=s.diag(1,-1) if fault!='positive_form' else s.eye(2)
    K=s.Matrix([[0,1],[1,0]])
    vp=s.Matrix([1,1 if fault!='wrong_null_line' else -1])/s.sqrt(2)
    f=s.exp(-beta*(y*y+z*z)/2)
    Ay=beta*y*K*(-1 if fault=='wrong_connection_sign' else 1)
    Az=beta*z*K if fault!='omit_connection_component' else s.zeros(2)
    ck('G_compatibility_y',Ay.T*G+G*Ay==s.zeros(2))
    ck('G_compatibility_z',Az.T*G+G*Az==s.zeros(2))
    ck('parallel_y',s.simplify(s.diff(f*vp,y)+Ay*f*vp)==s.zeros(2,1))
    ck('parallel_z',s.simplify(s.diff(f*vp,z)+Az*f*vp)==s.zeros(2,1))
    ck('pointwise_inherited_null',s.simplify((vp.T*G*vp)[0])==0)
    ck('positive_auxiliary_line',s.simplify((vp.T*vp)[0])==1)
    ck('not_positive_compatible',Ay.T+Ay!=s.zeros(2))
    ck('flat_actual_connection',s.diff(Az,y)-s.diff(Ay,z)+Ay*Az-Az*Ay==s.zeros(2))
    norm=(beta/s.pi)**s.Rational(1,4) if fault!='missing_normalization' else s.Integer(1)
    ck('normalized_1d',s.simplify(s.integrate(norm**2*s.exp(-beta*y*y),(y,-s.oo,s.oo)))==1)
    vm=s.Matrix([1,-1])/s.sqrt(2)
    ck('growing_partner_parallel',s.simplify(s.diff(s.exp(beta*y*y/2)*vm,y)+beta*y*K*s.exp(beta*y*y/2)*vm)==s.zeros(2,1))
    ck('hyperbolic_cross_pairing',(s.Matrix([1,1]).T*G*s.Matrix([1,-1]))[0]==2)
    for p,q in [(1,1),(3,2),(2,4)]:
        n=p+q;gg=s.diag(*([1]*p+[-1]*q));V=s.zeros(n,min(p,q))
        for j in range(min(p,q)):V[j,j]=1;V[p+j,j]=1
        ck('whole_Gram_'+str((p,q)),V.T*gg*V==s.zeros(min(p,q)))
        ck('sharp_rank_'+str((p,q)),V.rank()==min(p,q))
        ck('auxiliary_Gram_'+str((p,q)),V.T*V==2*s.eye(min(p,q)))
    # Nonzero constant pairing for an actual unbounded G-compatible field.
    growth=beta if fault!='wrong_metric_growth' else -beta
    gy=s.exp(growth*y*y)*s.diag(1,-1);aa=beta*y*s.eye(2)
    ck('variable_form_compatibility',s.simplify(s.diff(gy,y)-aa.T*gy-gy*aa)==s.zeros(2))
    psi=s.exp(-beta*y*y/2)*s.Matrix([1,0])
    ck('variable_form_constant_nonzero',s.simplify((psi.T*gy*psi)[0])==1)
    ck('reciprocal_form_integrable',s.integrate(s.exp(-beta*y*y),(y,-s.oo,s.oo))==s.sqrt(s.pi/beta))
    ck('finite_density_nonzero_pairing',s.integrate(s.exp(-y*y),(y,-s.oo,s.oo))==s.sqrt(s.pi))
    # Differential Gram identity tested on nonparallel polynomial sections as well.
    u=s.Matrix([1+y,y*y]);v=s.Matrix([y,2-y]);A=beta*y*K
    defect=s.diff((u.T*G*v)[0],y)-((s.diff(u,y)+A*u).T*G*v+u.T*G*(s.diff(v,y)+A*v))[0]
    ck('full_Gram_differential_identity',s.simplify(defect)==0)
    return out

RESULT="K2248"
REPORT="lab/process/k2248-indefinite-parallel-localization.json"
DEPS=['explorations/conditional-build/k2248-indefinite-parallel-localization-2026-10-29.md', 'explorations/conditional-build/k2245-localized-normal-domain-2026-10-29.md']
EVIDENCE="Finite exact controls and actual changed-input faults; universal theorem proofs are written mathematics and independently reviewed, not certified by counts."

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
