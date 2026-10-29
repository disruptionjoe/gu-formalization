#!/usr/bin/env python3
"""Exact finite controls; universal statements rest on the companion written proof."""
import sympy as s
ID='K2265'
NOTE='explorations/conditional-build/k2265-shared-cosmology-consistency-2026-10-29.md'
REPORT='lab/process/k2265-shared-cosmology-consistency.json'
DEPS=['lab/active-research/joe-directed/prediction-kickoff/late-time-finite-node-identifiability-2026-10-27.md']

def verify(m):
    out={}
    def eq(k,a,b=0):out[k]=s.simplify(a-b)==0
    def yes(k,a):out[k]=bool(a)
    x=s.symbols('x',positive=True);a,r,b=s.symbols('a r b',nonzero=True)
    y=s.Function('y')(x);yp=s.diff(y,x);ypp=s.diff(y,x,2)
    R=12*y-3*x*yp
    Q=18*x*y*yp+s.Rational(m.get('q_num',9),4)*x*x*yp**2-9*x*x*y*ypp
    raw=-3*R*y+R*R/4+m.get('hp_sign',3)*x*y*s.diff(R,x)
    eq('independent_redshift_substitution',raw,Q)
    H,P,R0=s.symbols('H P R0',real=True)
    C=3*b*(a-R0)*H**2+b*R0**2/4-b*r/m.get('rho_den',2)-3*b*H*P
    T=s.symbols('T')
    Hd=R0/6-2*H**2;Pd=T+(a*R0-2*r)/3-3*H*P
    Cd=s.diff(C,H)*Hd+s.diff(C,R0)*P+s.diff(C,P)*Pd
    eq('off_shell_constraint_identity',Cd+4*H*C+3*b*H*T)
    F=b*(a-R0);f=b*(a*R0-R0**2/2-r)
    Esp=F*(Hd+3*H**2)-f/2+b*Pd+2*b*H*P
    eq('actual_spatial_component',Esp-C/3-b*T)
    A,B,n=s.symbols('A B n',real=True)
    def q(v):return s.simplify(Q.subs(y,v).doit())
    v=A+B*x**n
    expected=9*n*(3-n)*A*B*x**n+s.Rational(27,4)*n*(4-n)*B*B*x**(2*n)
    eq('power_plus_constant',q(v),expected)
    eq('dust_shape_residual',q(A+B*x**3),s.Rational(81,4)*B**2*x**6)
    mat=s.Matrix([[1,1+t**3,q(1+x**3).subs(x,t)] for t in [1,2,3]])
    yes('dust_shape_augmented_rank3',mat.det()!=0)
    for t in [1,2,3]:eq('desitter_'+str(t),q(s.Integer(t)),0)
    D=s.symbols('D',nonzero=True);v=R0/12+D*x**4
    eq('constant_R_kinematics',(12*v-3*x*s.diff(v,x)),R0)
    eq('degenerate_constraint',q(v)+3*R0*v-R0**2/4)
    eq('degenerate_F',b*(R0-(12*v-3*x*s.diff(v,x))))
    c,d=s.symbols('c d',positive=True);v=c*(x**3+d)**s.Rational(4,3)
    eq('nonconstant_pure_R2_positive_control',q(v))
    eq('positive_R_formula',12*v-3*x*s.diff(v,x),12*c*d*(x**3+d)**s.Rational(1,3))
    yes('positive_control_F',12*c*d*(x**3+d)**s.Rational(1,3)>0)
    vals=[(s.Integer(t),s.Integer(7*t-5)) for t in [1,2,3,5]]
    slope=m.get('slope_sign',-1)*(vals[0][1]-vals[1][1])/(3*(vals[0][0]-vals[1][0]));intercept=2*(vals[0][1]+3*slope*vals[0][0])
    for i,(yv,qv) in enumerate(vals):eq('shared_pair_'+str(i),qv+3*slope*yv-intercept/2)
    X=s.Matrix([[3,-s.Rational(1,2)],[3,-s.Rational(1,2)]]);aug=X.row_join(s.Matrix([0,1]))
    yes('rank_deficient_inconsistent',X.rank()<aug.rank())
    scale=s.symbols('scale',positive=True);v=1+x+x*x
    eq('scale_quartic',q(scale**2*v),scale**m.get('scale_power',4)*q(v))
    eq('full_constraint_scale',q(scale**2*v)+3*scale**2*a*scale**2*v-scale**4*r/2,scale**4*(q(v)+3*a*v-r/2))
    return out
FAULTS={'quadratic_derivative_coefficient':{'q_num':8},'redshift_HP_sign':{'hp_sign':-3},'vacuum_normalization':{'rho_den':1},'shared_slope_sign':{'slope_sign':1},'scale_power':{'scale_power':2}}

def main():
    import argparse,hashlib,json
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
    checks=verify({});bad=[k for k,v in checks.items() if not v]
    if bad: raise AssertionError('BASELINE FAIL: '+str(bad))
    caught={}
    for name,change in FAULTS.items():
        result=verify(change)
        failures=[k for k,v in result.items() if not v]
        if not failures: raise AssertionError('UNDETECTED: '+name)
        caught[name]=failures
    root=Path(__file__).resolve().parents[2]
    paths=[NOTE,str(Path(__file__).resolve().relative_to(root))]+DEPS
    hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}
    report=dict(result_id=ID,status='internally_reviewed_conditional_mathematics',evidence_kind='finite_exact_symbolic_and_matrix_controls_plus_genuine_changed_input_faults',checks=len(checks),faults=len(caught),fault_failures=caught,sha256=hashes,ceiling='Finite checks supplement written proofs; no empirical, source, novelty, Lean or remote-CI certification.')
    dest=root/REPORT
    if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
    else:
        old=json.loads(dest.read_text());assert old==report,'stale report: reproduce with --write after review'
    print(ID, 'PASS',len(checks),'exact finite controls;',len(caught),'genuine faults; hashes current')
if __name__=='__main__':main()
