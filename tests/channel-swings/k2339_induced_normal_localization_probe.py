"""Exact direction-dependent induced Gram and reduced full companion controls."""
from pathlib import Path
import sympy as sp,ast,json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};faults={};Q=sp.Rational
geom='tests/channel-swings/selected_k77_full_normal_owner_bank_probe.py'
tree=ast.parse((R/geom).read_text());exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'sym2_basis','dewitt','d_dewitt'}],type_ignores=[]),geom,'exec'),globals())
slots,bs=sym2_basis();g=sp.diag(1,-1,-1,-1);gv=dewitt(g,bs);G=sp.diag(g,gv);Gi=G.inv();Ps=[sp.diag(h,d_dewitt(g,h,bs)) for h in bs]
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError('[FAIL] '+k)
def simp(m):return m.applyfunc(sp.simplify)
def bank(v,ps=Ps):
 q=sp.zeros(14,1);q[0]=1;q[4]=v;s=(q.T*Gi*q)[0];Pi=sp.eye(14)-Gi*q*q.T/s
 Ms=[simp(Pi*Gi*p*Pi) for p in ps];C=sp.Matrix(10,10,lambda i,j:sp.simplify(sp.trace(Ms[i]*Ms[j])));t=sp.Matrix([sp.trace(m) for m in Ms]);u=C.inv()*t;tau=sp.simplify((t.T*u)[0]);return q,s,Pi,Ms,C,t,u,tau
v=sp.symbols('v');formula=4*(46*v**6+107*v**4+356*v*v+643)/(37*v**6+62*v**4+176*v*v+364)
# Exact polynomial identity via rational symbolic reconstruction, not interpolation alone.
q,ss,Pi,Ms,C,t,u,tau=bank(v)
check('symbolic_tau_identity',sp.factor(tau-formula)==0)
check('projector_idempotent',simp(Pi*Pi-Pi)==sp.zeros(14))
check('projector_G_selfadjoint',simp(Pi.T*G-G*Pi)==sp.zeros(14))
check('projector_annihilates_qsharp',simp(Pi*Gi*q)==sp.zeros(14,1))
check('normal_norm',ss==1+v*v/2)
check('tau_temporal',formula.subs(v,0)==Q(643,91))
check('tau_second_order',sp.diff(formula,v,2).subs(v,0)/2==Q(4104,8281))
for vv in [Q(1,2),sp.I/2]:
 q,ss,Pi,Ms,C,t,u,tau=bank(vv)
 check('independent_direction_tau_'+str(vv),sp.simplify(tau-formula.subs(v,vv))==0)
check('normal_s',ss==Q(7,8));check('normal_tau',tau==Q(1448,209));check('normal_Cdet',C.det()==-Q(5124528732635136,5764801))
check('normal_t',t==sp.Matrix([-Q(38,7),0,0,0,4,0,0,4,0,4]))
check('normal_u',u==sp.Matrix([-112,0,0,0,70,0,0,70,0,70])/209)
r=(1+11*tau)/(121+35*tau)
check('changed_root',r==Q(1793,8441) and r!=Q(199,931))
# Scale q to s=r with kappa=1; Pi,M,C unchanged. Write e=z ebar, z²=r.
I=Pi;M=sum((u[a]*Ms[a] for a in range(10)),sp.zeros(14))
def RR(m):return m-sp.trace(m)*I
def BB(m):return sp.trace(m)*I-2*m
o=simp(-r*((M-sp.trace(M)*I/13)/(1-4*r)-12*sp.trace(M)*I/(13*(1-121*r))));ebar=-BB(o)
check('normal_odd_companion',simp(o+r*BB(ebar)+r*RR(M))==sp.zeros(14))
check('normal_even_companion',simp(ebar+BB(o))==sp.zeros(14))
for a in range(10):check('normal_metric_'+str(a),sp.simplify(sp.trace(RR(Ms[a])*o))==0)
check('normal_curvature_nonzero',RR(M)!=sp.zeros(14))
check('normal_simple_kernel',(C-t*t.T/tau).rank()==9)
lam=sp.symbols('lam',positive=True);tau0=Q(643,91);F=1+11*tau0-lam**2*(121+35*tau0);l0=sp.sqrt(Q(199,931))
check('temporal_root',F.subs(lam,l0)==0);check('IFT_derivative',sp.diff(F,lam).subs(lam,l0)!=0)
a=sp.symbols('a');L0=Q(199,931);taucoef=-Q(4104,8281)/L0
linear=11*taucoef-((a-Q(1,2))*(121+35*tau0)+L0*35*taucoef)
slope=sp.solve(linear,a)[0]
check('normal_dispersion_slope',slope==Q(177061,370538))
check('constant_tau_shortcut_wrong',slope!=Q(1,2))
check('temporal_nonresonance',L0!=0 and 1-4*L0!=0 and 1-121*L0!=0)
# Change actual geometry/root/companion/projector data after baseline.
wrongr=Q(199,931)
wrong_o=-wrongr*((M-sp.trace(M)*I/13)/(1-4*wrongr)-12*sp.trace(M)*I/(13*(1-121*wrongr)))
faults['reuse_temporal_root_at_normal_direction']=['normal_metric_rows'] if any(sp.simplify(sp.trace(RR(m)*wrong_o))!=0 for m in Ms) else []
faults['omit_even_companion']=['normal_odd_companion'] if simp(o+r*RR(M))!=sp.zeros(14) else []
wrongPi=sp.eye(14)-Gi*q*q.T # omission of 1/s
faults['omit_projection_normalization']=['projector_idempotent'] if simp(wrongPi*wrongPi-wrongPi)!=sp.zeros(14) else []
wrongPs=[sp.diag(h,sp.zeros(10)) for h in bs]
# Actual fibre derivative input changes the trace vector, before any inverse.
wrongt=sp.Matrix([sp.trace(Pi*Gi*p*Pi) for p in wrongPs])
faults['omit_induced_fibre_derivative']=['normal_t'] if wrongt!=t else []
wronglinear=-(a-Q(1,2))*(121+35*tau0)
wrong_slope=sp.solve(wronglinear,a)[0]
faults['constant_tau_normal_dispersion']=['normal_dispersion_slope'] if wrong_slope!=Q(177061,370538) else []
assert all(faults.values()),'[FAIL] undetected geometry fault'
st='k2339-induced-normal-localization';deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R)),geom,'explorations/conditional-build/k2316-induced-metric-coupled-pencil-2026-10-30.md','explorations/conditional-build/k2313-full-metric-variation-boundary-2026-10-30.md']
out=dict(result_id='K2339',checks=len(checks),check_names=list(checks),evidence_kind='exact symbolic induced geometry/reduced companion algebra; local all-momentum and Fourier existence use written proof',mutation_failed_checks=faults,details={'tau_formula':str(formula),'normal_root':str(r),'normal_dispersion_slope':str(slope),'normal_Cdet':str(C.det())},dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps});p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({'result':'K2339','exact_checks':len(checks),'faults':len(faults)}))
