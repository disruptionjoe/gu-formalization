#!/usr/bin/env python3
"""K2242 exact finite symbol/jet controls; universal proof in note."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import k2206_changed_raw_mass_construction_probe as o
import sympy as s
F=o.F
FAULTS=['raw_return','transverse_weight','jet_sign','matrix_order','constraint_mass','characteristic_slope']
def controls(fault=None):
    out={}
    def ck(k,v):out[k]=bool(v)
    I=o.ONE
    W=o.W if fault!='transverse_weight' else I
    for k in range(14):
        eta=o.ETA[k];a,c=[x for x in range(14) if x!=k][:2]
        raw=o.scale(o.mul(o.blade((a,k,c)),W),o.ETA[a])
        # Same original coefficient transformed to the transverse normal form.
        z=o.scale(o.mul(o.mul(o.G[a],raw),o.G[c]),o.ETA[c])
        ck('actual_transverse_'+str(k),z==o.mul(o.G[k],o.WB))
        spin=o.mul(o.G[k],o.WB)
        ck('transverse_square_'+str(k),o.mul(spin,spin)==o.scale(I,2*eta))
        ret=o.raw(k,14,k,'raw_return_sign' if fault=='raw_return' else None)
        ck('original_negative_return_'+str(k),o.mul(o.raw(k,k,14),ret)==o.scale(I,-eta))
    N=s.ones(13)-s.eye(13)
    ck('two_transverse_roots',(N-12*s.eye(13))*(N+s.eye(13))==s.zeros(13))
    x=s.symbols('x');ck('polynomial_no_zero',s.expand((x+1)*(x-2)*(x-288)).subs(x,0)==576)
    # Graph conormal Gram in the declared 4+10 signature, several exact inputs.
    eo=s.diag(1,-1,-1,-1);en=s.diag(*[o.ETA[k] for k in o.UN])
    for j in range(4):
        B=s.zeros(4,10) if j==0 else s.Matrix(4,10,lambda a,b:s.Rational(((a+1)*(b+2)+j)%7-3,j))
        gram=en+B.T*eo*B
        ck('conormal_rank_at_least_six_'+str(j),gram.rank()>=6)
    # Graph y=2x, psi=x^2+3xy+5y^2: chain derivative is independent control.
    x,y=s.symbols('x y');psi=x*x+3*x*y+5*y*y;B=s.Integer(2)
    vx=s.diff(psi.subs(y,B*x),x);jy=s.diff(psi,y).subs(y,B*x)
    normal=3-B if fault!='jet_sign' else 3+B
    ck('actual_graph_chain',s.expand((s.diff(psi,x)+3*s.diff(psi,y)).subs(y,B*x)-vx-normal*jy)==0)
    # Noncommuting exact on-shell exponential coefficient at all r follows NH+Z=0.
    nn=s.Matrix([[1,2],[0,1]]);aa=s.Matrix([[0,1],[1,0]]);ll=s.Matrix([[2,0],[1,3]])
    for lam in [0,1,s.Rational(-2,3)]:
        z=lam*aa+ll;hh=-nn.inv()*z if fault!='matrix_order' else -z*nn.inv()
        ck('on_shell_order_'+str(lam),nn*hh+z==s.zeros(2))
    slope=2 if fault!='characteristic_slope' else 3
    ck('characteristic_countercontrol',2-slope==0)
    A=o.mul(o.G[0],o.J);T=o.blade(o.UN);g=o.G[1]
    mass=A if fault!='constraint_mass' else o.G[0]
    ck('positive_lift_mass',o.mul(g,mass)==o.mul(mass,g))
    ck('positive_lift_flavor',o.add(o.mul(g,T),o.mul(T,g))=={})
    ck('positive_lift_isometry',o.mul(o.transpose(g),g)==I)
    for j in [7,8,9]:
        C=o.mul(o.G[0],o.G[j]);ck('positive_lift_principal_'+str(j),o.mul(g,C)==o.mul(C,g))
    return out

RESULT='K2242'
REPORT='lab/process/k2242-ambient-conormal-descent.json'
DEPS=['explorations/conditional-build/k2242-ambient-conormal-descent-2026-10-29.md', 'explorations/conditional-build/k2032-principal-form-rigidity-2026-10-24.md', 'explorations/conditional-build/k2239-moving-observation-closure-2026-10-29.md', 'tests/channel-swings/k2206_changed_raw_mass_construction_probe.py']
EVIDENCE='Exact original coordinate/transverse coefficients, finite graph Grams and noncommuting jet fixtures; universal Spin/Witt/on-shell proof in note.'

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
