#!/usr/bin/env python3
"""Exact finite controls; universal statements rest on the companion written proof."""
import sympy as s
ID='K2266'
NOTE='explorations/conditional-build/k2266-windowed-cosmology-test-2026-10-29.md'
REPORT='lab/process/k2266-windowed-cosmology-test.json'
DEPS=['explorations/conditional-build/k2265-shared-cosmology-consistency-2026-10-29.md']

def verify(m):
    out={}
    def eq(k,a,b=0):out[k]=s.simplify(a-b)==0
    def yes(k,a):out[k]=bool(a)
    x=s.symbols('x',positive=True);w=(x-1)**2*(2-x)**2
    def Q(y):return 18*x*y*s.diff(y,x)+s.Rational(9,4)*x*x*s.diff(y,x)**2-9*x*x*y*s.diff(y,x,2)
    def weak(y,w):return s.Rational(m.get('weak_num',45),4)*w*x*x*s.diff(y,x)**2-s.Rational(9,2)*(x*x*s.diff(w,x,2)+6*x*s.diff(w,x)+4*w)*y*y
    def integ(f):return s.integrate(s.expand(f),(x,1,2))
    for j,y in enumerate([x,1+x**3,1+x+x**2]):
        eq('weak_strong_'+str(j),integ(weak(y,w)),integ(w*Q(y)))
        bound=-9*w*x*x*y*s.diff(y,x)+s.Rational(9,2)*(x*x*s.diff(w,x)+4*x*w)*y*y
        eq('boundary_zero_'+str(j),bound.subs(x,2)-bound.subs(x,1))
    y=1+x*x;wt=1+x
    bound=-9*wt*x*x*y*s.diff(y,x)+s.Rational(9,2)*(x*x*s.diff(wt,x)+4*x*wt)*y*y
    eq('nonvanishing_boundary',integ(wt*Q(y)),integ(weak(y,wt))+m.get('boundary',1)*(bound.subs(x,2)-bound.subs(x,1)))
    eq('negative_exact_residual',integ(w*Q(x)),s.Rational(54,35))
    eq('one_window_false_pass',integ(w*(Q(x)+90*x-s.Rational(m.get('false_r_num',2538),14))))
    yes('false_pass_not_global',s.Poly(Q(x)+90*x-s.Rational(2538,14),x).degree()==2)
    for t in [1,2]:yes('false_pass_F_'+str(t),30-9*t>0)
    y=1+x**3;ws=[w,x*w,x*x*w]
    X=s.Matrix([[3*integ(v*y),-integ(v)/2] for v in ws]);q=s.Matrix([integ(v*Q(y)) for v in ws]);aug=X.row_join(q)
    yes('three_window_rank2',X.rank()==2);yes('three_window_obstruction',aug.det()!=0)
    theta=-(X.T*X).inv()*X.T*q;res=q+X*theta
    eq('normal_equation',sum((X.T*res)[j]**2 for j in range(2)))
    yes('positive_minimum',(res.T*res)[0]>0)
    u=X.T.nullspace()[0];u=u/sum(abs(t) for t in u)
    margin=abs((u.T*q)[0]);eq('robust_margin',margin,s.Rational(205767,24104080))
    bounds=[]
    for ww in ws:
        ll=x*x*s.diff(ww,x,2)+6*x*s.diff(ww,x)+4*ww
        lb=sum(abs(co)*s.Rational(2**(power[0]+1)-1,power[0]+1) for power,co in s.Poly(ll,x).terms())
        bounds.append(s.Rational(45,2)*13*integ(ww*x*x)+90*lb+300*integ(ww))
    robust=sum(abs(u[j])*bounds[j] for j in range(3))
    eq('robust_lipschitz_constant',robust,s.Rational(2589985595,7224))
    yes('robust_neighborhood_exclusion',robust*s.Rational(m.get('epsilon_num',1),10**8)<margin)
    yv,v,a,r=s.symbols('yv v a r',nonzero=True)
    vp=2*v/x+v*v/(4*yv)+a/(3*x*x)-r/(m.get('ode_den',18)*x*x*yv)
    eq('forward_ode',18*x*yv*v+s.Rational(9,4)*x*x*v*v-9*x*x*yv*vp+3*a*yv-r/2)
    h,hp,hpp,e=s.symbols('h hp hpp e',positive=True)
    yy=1/h**2;yv1=-2*hp/h**3;yv2=6*hp**2/h**4-2*hpp/h**3
    residual=18*x*yy*yv1+s.Rational(9,4)*x*x*yv1**2-9*x*x*yy*yv2
    eq('bump_residual',residual.subs(hpp,hpp+e)-residual,m.get('bump_coefficient',18)*x*x*yy*e/h**3)
    psi=(x-1)**4*(2-x)**4
    eq('distance_integral_control',integ(s.diff(psi,x)))
    for end in [1,2]:
        for k in range(3):eq('finite_bump_endpoint_'+str(end)+'_'+str(k),s.diff(psi,x,k).subs(x,end))
    # Explicit deterministic error bound on a pair of positive histories.
    ya=1+x;yb=ya+s.Rational(1,100)*x*x;M=4;V=2;e0=s.Rational(4,100);e1=s.Rational(4,100)
    L=x*x*s.diff(w,x,2)+6*x*s.diff(w,x)+4*w
    # Absolute integral is bounded above by sum absolute polynomial coefficients on [1,2].
    Lbound=sum(abs(co)*s.Rational(2**(power[0]+1)-1,power[0]+1) for power,co in s.Poly(L,x).terms())
    bound=s.Rational(45,2)*V*e1*integ(w*x*x)+9*M*e0*Lbound
    yes('deterministic_error_consumer',abs(integ(weak(ya,w)-weak(yb,w)))<=bound)
    return out
FAULTS={'weak_derivative_coefficient':{'weak_num':9},'missing_boundary':{'boundary':0},'wrong_profiled_constant':{'false_r_num':2539},'wrong_ode_rho_normalization':{'ode_den':9},'wrong_bump_response':{'bump_coefficient':9},'oversized_robust_radius':{'epsilon_num':3}}

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
