"""Exact mixed-parity auxiliary and singular-stratum variation controls."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as F
from math import comb
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def fault(k,v):
 faults[k]=bool(v)
 if not v:raise AssertionError('ineffective altered-input control: '+k)
def publish(st,details,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),altered_input_controls=faults,evidence_kind='exact symbolic/rational controls; universal theorems proved in companion note, no empirical or proof-assistant certification',details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({k:out[k] for k in ['result_id','checks','details']}))

backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';src=(R/backend).read_text();ns={'__file__':str(R/backend),'__name__':'selected_native_arithmetic'}
exec(compile(src[:src.index('def sparse_rank')],backend,'exec'),ns)
blade=ns['blade'];wedge=ns['wedge_raw'];fadd=ns['fadd'];zero=ns['ZERO'];S=lambda c:ns['shiab'](c,('comm','symi','symi'))
pair=lambda a,b:wedge(a,b).get(ns['FULL'],{}).get(0,zero)
Ee={1:blade((0,1))};Oo={2:blade(1)};mix=fadd(wedge(Ee,Oo),wedge(Oo,Ee));T=fadd(Ee,Oo)
check('native_even_square_zero',not wedge(Ee,Ee))
check('native_cubic_coefficient',pair(Ee,S(mix))==(F(-4),F(0)))
check('native_full_cubic_matches_polarization',pair(T,S(wedge(T,T)))==(F(-4),F(0)) and pair(Oo,S(wedge(Ee,Ee)))==zero)
fault('delete_native_even_even_odd_cubic',pair(T,S(wedge(T,T)))!=zero)
u,v,x,xp,xpp,k,f=s.symbols('u v x xp xpp k f',real=True);a=k+x
L=a*u*u/2-k*v*v/2+u*xp+f*x+k*x*x/2+x**3/3
us=-xp/a;Le=s.factor(L.subs({u:us,v:0}));expected=f*x+k*x*x/2+x**3/3-xp*xp/(2*a)
check('exact_auxiliary_substitution',s.simplify(Le-expected)==0)
check('even_Euler_substitution',s.simplify(s.diff(L,u).subs(u,us))==0 and s.diff(L,v).subs(v,0)==0)
def Dz(z):return s.diff(z,x)*xp+s.diff(z,xp)*xpp
Eeff=s.simplify(s.diff(Le,x)-Dz(s.diff(Le,xp)));Eold=s.simplify((u*u/2+f+k*x+x*x).subs(u,us)-Dz(us))
check('full_odd_Euler_equivalence',s.simplify(Eeff-Eold)==0)
check('explicit_reduced_Euler',s.simplify(Eeff-(f+k*x+x*x+xpp/a-xp*xp/(2*a*a)))==0)
check('zero_odd_field_retains_forcing',Eeff.subs({x:0,xp:0,xpp:0})==f)
# Exact singular stationary branches of this control.
for sign in [-1,1]:
 vals={k:1,f:-s.Rational(1,2),x:-1,xp:0,u:sign,v:0}
 assert s.diff(L,u).subs(vals)==s.diff(L,v).subs(vals)==(u*u/2+f+k*x+x*x).subs(vals)==0
check('singular_full_stationary_control',True)
check('singular_even_matrix',s.det(s.diag(a,-k)).subs({k:1,x:-1})==0)
# Moving coefficient formal adjoint: Lcross=1/2(E P O'+O Q E').
t=s.symbols('t',real=True);E=s.Function('E')(t);O=s.Function('O')(t);P=1+t;Q=2+t*t
Lc=(E*P*s.diff(O,t)+O*Q*s.diff(E,t))/2
Evar=s.diff(Lc,E)-s.diff(s.diff(Lc,s.diff(E,t)),t)
b=((P-Q)*s.diff(O,t)-s.diff(Q,t)*O)/2
check('variable_cross_coefficient_adjoint',s.simplify(Evar-b)==0)
# Finite nonlinear two-variable Schur consumer, independent of field integration.
A=2+x;bb=x+x*x;cc=x+3*x*x/2+x**3/3;If=A*u*u/2+bb*u+cc;uu=-bb/A;eff=s.simplify(If.subs(u,uu))
H=s.hessian(If,(u,x));schur=s.simplify((H[1,1]-H[1,0]*H[0,1]/H[0,0]).subs(u,uu))
check('nonlinear_Schur_hessian',s.simplify(s.diff(eff,x,2)-schur)==0)
M=s.diag(1,-1);C=s.diag(s.Rational(1,4),s.Rational(1,3));Ar=M+C
check('indefinite_mass_retained',M.det()==-1)
check('Neumann_norm_bound',max(abs(z) for z in (M*C).eigenvals())==s.Rational(1,3) and max(abs(z) for z in Ar.inv().eigenvals())<=s.Rational(3,2))
check('determinant_nonzero_constant',s.det(s.diag(k+x,-k)).subs(x,0)==-k*k)
# Commutative scalar coefficient bookkeeping verifies generic parity allowed cubic polarization.
e1,e2,o1,o2,A1,A2,A3=s.symbols('e1 e2 o1 o2 A1 A2 A3');quad=(A1+2*A2+3*A3)*o1*e1**2/3
polar=(s.expand(quad.subs(e1,e1+e2))-quad-quad.subs(e1,e2))/2
check('cubic_polarization_half',s.simplify(polar.subs(e2,e1)-quad)==0)
fault('drop_integrated_derivative',s.simplify(Eold-(u*u/2+f+k*x+x*x).subs(u,us))!=0)
wrong=-xp/k
fault('discard_cubic_even_coefficient',s.simplify(s.diff(L,u).subs(u,wrong))!=0)
fault('freeze_inverse_in_reduced_Euler',s.simplify(Eeff-(f+k*x+x*x+xpp/a))!=0)
fault('omit_variable_coefficient_adjoint',s.simplify(Evar-(P-Q)*s.diff(O,t)/2)!=0)
fault('discard_singular_solutions',a.subs({k:1,x:-1})==0 and s.diff(L,u).subs({k:1,x:-1,xp:0,u:1})==0)
fault('import_zero_curvature_forcing',Eeff.subs({x:0,xp:0,xpp:0,f:1})!=0)
wrong_frozen_inverse=s.diff(cc,x,2)-(s.diff(bb,x)**2+bb*s.diff(bb,x,2))/A
fault('freeze_inverse_in_finite_Hessian',s.simplify(s.diff(eff,x,2)-wrong_frozen_inverse).subs(x,1)!=0)
details={'even_stationary_graph':str(us),'effective_density':str(Le),'reduced_Euler':str(Eeff),'singular_control':{'kappa':1,'f':'-1/2','x':-1,'u':[-1,1],'v':0},'Schur_hessian':str(schur),'variable_adjoint':str(b),'Neumann_rho':'1/3'}
publish('k2351-mixed-parity-auxiliary-reduction',details,[backend,'explorations/conditional-build/k2348-even-distortion-stationarity-boundary-2026-10-30.md','lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md','explorations/conditional-build/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification-2026-08-16.md'])
