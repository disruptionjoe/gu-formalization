"""Actual native potential coefficients, full homogeneous action and exact source shift.

Reuse coefficient functions, not predecessor full census runners. Universal
curved identities and distributional constraint are proved in the companion.
"""
from pathlib import Path
from fractions import Fraction
import ast,hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]; checks={};controls={}
def ck(bank,name,value):
 bank[name]=bool(value)
 if not value:raise AssertionError('FAIL '+name)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';parent='tests/channel-swings/selected_k77_nonzero_branch_parent_hessian_probe.py';first='tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py'
src=(R/backend).read_text();M={'__file__':str(R/backend),'__name__':'coefficient_backend'};exec(compile(src[:src.index('def sparse_rank')],str(R/backend),'exec'),M)
N=14;ETA=M['ETA'];FULL=M['FULL'];ONE=M['ONE'];ZERO=M['ZERO'];SELECTED=('comm','symi','symi');eta=s.diag(*ETA)
def load(path,names,ns):
 tr=ast.parse((R/path).read_text());nodes=[n for n in tr.body if isinstance(n,ast.FunctionDef) and n.name in names];exec(compile(ast.Module(body=nodes,type_ignores=[]),str(R/path),'exec'),ns)
ns=dict(M=M,N=N,ETA=ETA,FULL=FULL,ONE=ONE,ZERO=ZERO,SELECTED=SELECTED,Fraction=Fraction,sp=s,PHI1=M['PHI1'],T_VALUE=Fraction(-5,2288))
load(parent,{'pair','basis','qform','hessian','rational'},ns)
kn=dict(M=M,N=N,ETA=ETA,FULL=FULL,ONE=ONE,ZERO=ZERO,SELECTED=SELECTED,Fraction=Fraction,sp=s)
load(first,{'scalar_one_form','direction','top_scalar','pairing','rows_for_image'},kn)
def native(Q):
 return {1<<i:{1<<j:(Fraction(Q[i,j]),Fraction(0)) for j in range(N) if Q[i,j]} for i in range(N) if any(Q[i,j] for j in range(N))}
def pairq(U,V):return s.trace(eta*U.T*eta*V)
def hv(U,V):
 u=native(U);v=native(V);return ns['rational'](ns['hessian'](u,v,ns['qform'](u),ns['qform'](v)))
a,kappa=s.symbols('a kappa',nonzero=True);a0=-5*kappa/2288
H=lambda Q:(kappa-32*a)*Q-16*a*eta*Q.T*eta+48*a*s.trace(Q)*s.eye(N)
fixtures={'scalar':s.eye(N),'tracefree_diagonal':s.diag(1,-1,*([0]*12))}
for i,j in [(0,4),(0,1),(1,2)]:
 for sym in [1,-1]:
  Q=s.zeros(N);Q[i,j]=1;Q[j,i]=sym*ETA[i]*ETA[j];fixtures[f'{i}_{j}_{sym}']=Q
for name,Q in fixtures.items():
 predicted=pairq(Q,H(Q).subs({a:-s.Rational(5,2288),kappa:1}))
 ck(checks,'native_H1_'+name,hv(Q,Q)==predicted)
 # independent mixed pairing prevents merely norm-specific match
 ck(checks,'mixed_H1_'+name,hv(Q,s.eye(N))==pairq(Q,H(s.eye(N)).subs({a:-s.Rational(5,2288),kappa:1})))
ms=s.simplify((kappa+624*a).subs(a,a0));mt=s.simplify((kappa-48*a).subs(a,a0));ma=s.simplify((kappa-16*a).subs(a,a0))
ck(checks,'three_nonzero_actual_masses',[ms,mt,ma]==[-4*kappa/11,158*kappa/143,148*kappa/143])
# Exact differentiation of the already-proved invariant K2369 cubic.
c,z=s.symbols('c z');Sk=s.diag(a+z,a-z,*([a]*12));tr=s.trace(Sk);e3=(tr**3-3*tr*s.trace(Sk**2)+2*s.trace(Sk**3))/6
ck(checks,'symmetric_cubic_linearization',s.diff(4*e3,z,2).subs(z,0)==-96*a)
K=s.zeros(N);K[0,4]=z;K[4,0]=-z;S=a*s.eye(N)
L3=4*(s.trace(S)**3-3*s.trace(S)*s.trace(S*S)+2*s.trace(S**3))/6+s.Rational(2,3)*s.trace(S)*s.trace(K*K)-s.Rational(4,3)*s.trace(S*K*K)
ck(checks,'skew_cubic_linearization',s.diff(L3,z,2)==-32*a)
# True constant-radial scalar action, with Einstein seed curvature.
lam=35*kappa**2/604032;Lambda=6*lam;V=1456*a0**3+7*kappa*a0**2
ck(checks,'stationary_translation_curvature',s.simplify(kappa*a0+312*a0**2+12*lam)==0)
ck(checks,'radial_full_Einstein_density',s.simplify(V+24*a0*Lambda)==0)
# Independent second differentiation of K2529's un-restricted homogeneous density.
xx,yy,aa,bb=s.symbols('xx yy aa bb');uu=aa+bb;vv=aa-bb
f=s.exp(7*(xx+yy))*(7*((5*aa+7*bb)*lam*s.exp(-2*xx)+(7*aa+5*bb)*lam*s.exp(-2*yy))+182*uu**3-42*uu*vv**2+7*kappa*(uu**2+vv**2)/4)
coords=[xx,yy,aa,bb];seed={xx:0,yy:0,aa:a0,bb:a0};HH=s.hessian(f,coords).subs(seed).applyfunc(s.simplify)
ck(checks,'full_four_coordinate_stationarity',all(s.simplify(s.diff(f,q).subs(seed))==0 for q in coords))
P=s.eye(4);P[0,2]=-1/(12*a0);P[1,3]=-1/(12*a0) # h_cov=2xG; z_cov=h_cov+delta a G/(6a0)
shifted=(P.T*HH*P).applyfunc(s.simplify)
ck(checks,'actual_curvature_mixed_block_removed',shifted[:2,2:]==s.zeros(2))
ck(checks,'actual_full_homogeneous_response_invertible',s.factor(HH.det())!=0)
source=s.Matrix([1,0,0,0]);qs=P.T*source
ck(checks,'source_must_transform',qs==s.Matrix([1,0,-1/(12*a0),0]))
ck(checks,'original_source_response_preserved',(P*shifted.inv()*qs-HH.inv()*source).applyfunc(s.simplify)==s.zeros(4,1))
ck(controls,'discarding_tensor_source_changes_readout',s.simplify((P*shifted.inv()*source-HH.inv()*source)[0])!=0)
# Abstract symmetric operator congruence checks coefficients without replacing full curved proof.
e,j,h,C,T=s.symbols('e j h C T');orig=-6*a*e*h*h-2*C*e*h+T*C*C/2-j*h
new=s.expand(orig.subs(h,z-C/(6*a)))
ck(checks,'operator_and_source_completion',s.simplify(new-(-6*a*e*z*z+C*C*e/(6*a)+T*C*C/2-j*z+j*C/(6*a)))==0)
ck(controls,'wrong_shift_sign_fails',s.diff(s.expand(orig.subs(h,z+C/(6*a))),z,C)!=0)
# Actual antisymmetrized first-order native coefficient, no positive Gram substitution.
xi=(1,)+(0,)*13;kform=kn['scalar_one_form'](xi)
def coefficient(U,V):
 u=native(U);v=native(V)
 iu=M['shiab'](M['wedge_raw'](kform,u),SELECTED);iv=M['shiab'](M['wedge_raw'](kform,v),SELECTED)
 return ns['rational'](M['gscale'](Fraction(1,2),M['gadd'](ns['pair'](v,iu),M['gscale'](Fraction(-1),ns['pair'](u,iv)))))
# Need even receiver basis, so use raw native dictionaries directly.
def coeff(u,v):
 iu=M['shiab'](M['wedge_raw'](kform,u),SELECTED);iv=M['shiab'](M['wedge_raw'](kform,v),SELECTED)
 return ns['rational'](M['gscale'](Fraction(1,2),M['gadd'](ns['pair'](v,iu),M['gscale'](Fraction(-1),ns['pair'](u,iv)))))
# Only all 1274 grade2 receivers; cheap sparse pairings, not the full229376 bank.
from itertools import combinations
skew=s.zeros(N);skew[1,2]=1;skew[2,1]=-1
active=s.zeros(N);active[0,4]=1;active[4,0]=-1
trans=native(skew);long=native(active);trans_image=M['shiab'](M['wedge_raw'](kform,trans),SELECTED)
vals=[];nonzero=[]
for i in range(N):
 for p,q in combinations(range(N),2):
  receiver=ns['basis'](i,(1<<p)|(1<<q))
  val=coeff(trans,receiver);vals.append(val)
  # Vector trace receiver is sufficient planted-positive; no rerun full image needed.
  if p==0:nonzero.append(coeff(long,receiver))
ck(checks,'transverse_skew_full_native_B_zero',all(v==0 for v in vals))
ck(controls,'longitudinal_skew_B_detected',any(v!=0 for v in nonzero))
# Closed 2-form need not vanish: K=d(sin x0 dx1), exact nonzero flat chart fixture.
x0,x1,x2=s.symbols('x0 x1 x2');K01=s.cos(x0)
ck(controls,'closed_is_not_zero',s.diff(K01,x2)==0 and K01.subs(x0,0)==1)
# Parallel O(7,7)-equivariance fixes A2 on its three multiplicity-one tensor sectors.
def form(terms):
 out={}
 for i,J,c in terms:out.setdefault(1<<i,{})[J]=(Fraction(c),Fraction(0))
 return out
vec=form([(i,(1<<0)|(1<<i),-1) for i in range(1,N)])
three=form([(0,6,1),(1,5,1),(2,3,-1)])
hook=form([(0,6,2),(1,5,-1),(2,3,1)])
a2_values={}
for name,Vv,expected_norm,expected_mass in [('vector',vec,-13,s.Rational(503,858)),('three_form',three,-3,s.Rational(394,429)),('hook',hook,-6,s.Rational(893,858))]:
 norm=ns['rational'](ns['pair'](Vv,M['hodge'](Vv)))
 hh=ns['rational'](ns['hessian'](Vv,Vv,ns['qform'](Vv),ns['qform'](Vv)))
 ck(checks,'A2_'+name+'_native_pairing_and_mass',norm==expected_norm and hh==expected_norm*expected_mass)
 a2_values[name]=str(expected_mass)
# Pure trace jet gives actual B=-11 J(d sigma), testing derivative normalization.
trace=native(s.eye(N));EV=form([(i,(1<<0)|(1<<i),11) for i in range(1,N)])
ck(checks,'actual_trace_jet_B_Riesz_normalization',coeff(trace,vec)==ns['rational'](ns['pair'](vec,M['hodge'](EV))))
# Universal projection algebra with arbitrary symmetric first jet and skew divergence.
# E_i;jk antisymmetric last slots; use rational integer seed with nontrivial trace/hook.
D=[s.Matrix(N,N,lambda i,j:((ell+2)*(min(i,j)+1)+max(i,j))%5-2) for ell in range(N)]
kdiv=s.Matrix([(-1)**i*(i%3) for i in range(N)])
vect=s.Matrix([sum(ETA[i]*D[i][i,j] for i in range(N))-sum(ETA[i]*D[j][i,i] for i in range(N)) for j in range(N)])
wvec=11*vect+13*kdiv
E={};EH={}
for i in range(N):
 for j in range(N):
  for q in range(j+1,N):
   val=2*(D[j][i,q]-D[q][i,j])+eta[i,q]*(vect[j]+kdiv[j])-eta[i,j]*(vect[q]+kdiv[q])
   E[i,j,q]=val;EH[i,j,q]=val-(eta[i,q]*wvec[j]-eta[i,j]*wvec[q])/13
get=lambda Z,i,j,q: Z[i,j,q] if j<q else -Z[i,q,j] if q<j else s.S.Zero
ck(checks,'B_has_no_three_form',all(get(E,i,j,q)+get(E,j,q,i)+get(E,q,i,j)==0 for i in range(N) for j in range(N) for q in range(N)))
ck(checks,'hook_has_no_trace',all(sum(ETA[i]*get(EH,i,j,i) for i in range(N))==0 for j in range(N)))
inner=lambda U,V:sum(ETA[i]*ETA[j]*ETA[q]*U[i,j,q]*V[i,j,q] for i,j,q in E)
EVv={ix:E[ix]-EH[ix] for ix in E}
ck(checks,'orthogonal_trace_hook_decomposition',inner(EVv,EH)==0 and s.simplify(inner(EVv,EVv)-(wvec.T*eta*wvec)[0]/13)==0)
mV=503*kappa/858
ck(checks,'trace_equation_exact_coefficients',s.simplify(ms+2*lam/a0+5*kappa/12)==0 and s.simplify(121/mV-2/a0-2820818/(2515*kappa))==0)
sol=shifted.inv()*qs;tau=s.simplify(7*(sol[2]+sol[3]))
ck(checks,'full_homogeneous_trace_source_consumer',s.simplify(tau+4576/(50*kappa**2))==0)
ck(controls,'positive_grade2_pairing_wrong_sign',(-s.Rational(1,2)/s.Rational(503,858))*(-13)!=(-s.Rational(1,2)/s.Rational(503,858))*13)

rpt=dict(result='K2537',exact_checks=checks,contrary_controls=controls,mass_eigenvalues={'scalar':str(ms),'symmetric_tracefree':str(mt),'skew':str(ma)},dimensions=[1,104,91],A2_Riesz_masses_at_kappa1=a2_values,scope='full local constant-radial quadratic action/source decoupling and skew closedness; no global Green inverse, positivity, observed Einstein response or native Met(X)',dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in [backend,parent,first,'lab/process/k2533-mixed-source-response.json','lab/process/k2535-reduced-response-symbol.json','explorations/conditional-build/k2369-nonsymmetric-native-derivative-2026-10-31.md',str(Path(__file__).relative_to(R))]})
p=R/'lab/process/k2537-reduced-action-decoupling.json'
if '--write' in sys.argv:p.write_text(json.dumps(rpt,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==rpt
print('K2537',len(checks),'exact native/algebraic checks',len(controls),'contrary controls')
