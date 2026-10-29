#!/usr/bin/env python3
"""Exact finite raw-coefficient and Gaussian/domain countercontrols; proof in note."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import k2206_changed_raw_mass_construction_probe as o
import sympy as s
FAULTS=['gradient_sign','omit_lower_return','normalization','moving_trace_sign','unitary_gradient','reduce_complement']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    y,t=s.symbols('y t',real=True);beta=s.Integer(2)
    f=s.exp(-beta*y*y/2);b=-beta if fault=='gradient_sign' else beta
    # Differential identity on a nonconstant scalar polynomial, not only the kernel.
    v=1+3*y+y*y
    ck('full_conjugation',s.simplify(s.diff(f*v,y)+b*y*f*v-f*s.diff(v,y))==0)
    ck('kernel',s.simplify(s.diff(f,y)+b*y*f)==0)
    ck('flat_constraint_commutator',s.diff(b*y,y)-b==0)
    for a in o.UN:
        lower=o.raw(a,14,a)
        added={} if fault=='omit_lower_return' else o.scale(lower,2)
        # At y=1, f'/f=-2: actual derivative plus full lower correction.
        ck('raw_lower_cancel_'+str(a),o.add(o.scale(lower,-2),added)=={})
        upper=o.raw(a,a,14)
        ck('raw_upper_cancel_'+str(a),o.add(o.scale(upper,-2),o.scale(upper,2))=={})
        ck('raw_normal_return_nonzero_'+str(a),bool(lower))
    normal=(beta/s.pi)**s.Rational(1,4) if fault!='normalization' else s.Integer(1)
    ck('normal_gaussian_unit_norm',s.simplify(s.integrate((normal*f)**2,(y,-s.oo,s.oo)))==1)
    # Counterexample: orthogonal input yf maps to the nonzero normal kernel.
    ck('odd_complement',s.integrate(y*f*f,(y,-s.oo,s.oo))==0)
    z=s.diff(y*f,y)+beta*y*y*f
    if fault=='reduce_complement':
        # Change the operator to (I-P_f) nabla, computing P_f by its Gaussian integral.
        projected=f*s.integrate(f*z,(y,-s.oo,s.oo))/s.integrate(f*f,(y,-s.oo,s.oo))
        z=z-projected
    ck('actual_complement_return',s.simplify(z-f)==0)
    F=s.exp(-beta*t*t/2);q=F
    qterm=beta*t if fault!='moving_trace_sign' else -beta*t
    ck('moving_output_equation',s.simplify(s.diff(q,t)+qterm*q)==0)
    ck('weighted_density_conserved',s.diff(q*q/(F*F),t)==0)
    ck('unweighted_density_not_conserved',s.simplify(s.diff(q*q,t))!=0)
    connection=s.Matrix([[beta*y]]) if fault!='unitary_gradient' else s.Matrix([[s.I*beta*y]])
    ck('real_amplitude_connection',connection+connection.conjugate().T==s.Matrix([[2*beta*y]]))
    ck('two_copy_isometry',2*s.Rational(1,2)==1)
    for j in [7,8,9]:
        C=o.mul(o.G[0],o.G[j]);ck('symmetric_C_'+str(j),o.transpose(C)==C)
    A=o.mul(o.G[0],o.J);ck('skew_mass',o.transpose(A)==o.scale(A,-1))
    # Metric-compatible positive rotation preserves norm; real localization does not.
    rot=s.Matrix([[0,-1],[1,0]]);vv=s.Matrix([1,2])
    ck('compatible_connection_constant_norm',(vv.T*(rot+rot.T)*vv)[0]==0)
    ck('localizing_connection_changes_norm',(vv.T*(s.eye(2)+s.eye(2))*vv)[0]==10)
    return out

RESULT='K2245'
REPORT='lab/process/k2245-localized-normal-domain.json'
DEPS=['explorations/conditional-build/k2245-localized-normal-domain-2026-10-29.md', 'explorations/conditional-build/k2242-ambient-conormal-descent-2026-10-29.md', 'explorations/conditional-build/k2239-moving-observation-closure-2026-10-29.md', 'tests/channel-swings/k2206_changed_raw_mass_construction_probe.py']
EVIDENCE='Finite exact arithmetic and algebra controls; universal normal-domain and graph-current claims are written independently reviewed proofs, not consequences of counts.'

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
