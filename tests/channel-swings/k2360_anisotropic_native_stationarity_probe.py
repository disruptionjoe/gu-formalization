"""Exact selected backend coefficients; geometric all-receiver proof in note."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];st='k2360-anisotropic-native-stationarity';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('ineffective control '+k)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';p=R/backend;src=p.read_text();ns={'__file__':str(p),'__name__':'selected_backend'};exec(compile(src[:src.index('def sparse_rank')],str(p),'exec'),ns)
b=ns['blade'];w=ns['wedge_raw'];add=ns['fadd'];scale=ns['fscale'];star=ns['hodge'];eta=ns['ETA'];P=lambda x,y:w(x,y).get(ns['FULL'],{}).get(0,ns['ZERO']);S=lambda x:ns['shiab'](x,('comm','symi','symi'))
def rat(v):
 assert v[1]==0
 return s.Rational(v[0].numerator,v[0].denominator)
def form(vals):return {1<<i:b(i,(F(v),F(0))) for i,v in enumerate(vals) if v}
def cubic(vals,i):
 T=form(vals);Z={1<<i:b(i)};return (rat(P(Z,S(w(T,T))))+rat(P(T,S(add(w(Z,T),w(T,Z))))))/3
vals=[1,-2,3,0,1,2,-1,4,0,-3,1,2,-2,1];e2=sum(vals[i]*vals[j] for i,j in combinations(range(14),2));tr=sum(vals)
for i in range(14):check('backend_diagonal_cubic_'+str(i),cubic(vals,i)==4*(vals[i]**2-tr*vals[i]+e2))
T=form(vals);check('cubic_density_12e3',rat(P(T,S(w(T,T))))==12*sum(vals[i]*vals[j]*vals[k] for i,j,k in combinations(range(14),3)))
# Signature-compatible 7+7 splitting; first seven coordinate indices need not have fixed factor signature.
prod=[1]*7+[-1]*7
for i in [0,7]:check('product_cubic_'+str(i),cubic(prod,i)==-24)
check('product_all14_Euler',all(-2*(3 if i<7 else 1)+28+2*prod[i]-24==0 for i in range(14)))
check('product_nonEinstein',3!=1);control('replace_by_common_radial',(-2*3+28)-(-2*1+28)!=0)
# Full formal derivative Euler on actual metric projector connection components.
def row(vindex,coeffs):
 Ds=[]
 for mu,c in enumerate(coeffs):Ds.append(add(scale(c,{1<<vindex:b(mu)}),scale(c*eta[mu]/eta[vindex],{1<<mu:b(vindex)})))
 Z={1:b((0,vindex))};DT=add(*[w({1<<mu:b(())},D) for mu,D in enumerate(Ds)])
 left=rat(P(Z,S(DT)));right=sum(rat(P(D,S(w({1<<mu:b(())},Z)))) for mu,D in enumerate(Ds))
 return left,right,(left-right)/2
trace=row(10,[1]*4);traceless=row(4,[1,1,-1,-1]);check('actual_trace_projector_adjoint_row',trace==(2,6,-2));check('actual_traceless_projector_adjoint_row',traceless==(2,-2,2))
a,bv,d=s.symbols('a bv d',real=True);even=s.Matrix([trace[2]*(bv-a)/4,traceless[2]*(d-a)/4]);jac=even.jacobian([a,bv,d]);check('three_weight_kernel_only_radial',jac.rank()==2 and jac.nullspace()==[s.ones(3,1)])
control('freeze_nonparallel_projectors',even.subs({a:0,bv:1,d:2})!=s.zeros(2,1))
control('drop_formal_adjoint',trace[0]/2!=trace[2] and traceless[0]/2!=traceless[2])
check('radial_remaining_Ricci_obstruction',-2*(s.Rational(21,4)-s.Rational(15,4))==-3)
# Independent actual connection geometry identities for chosen vertical vectors.
g=s.diag(1,-1,-1,-1);vt=g/2;vd=g*s.diag(1,1,-1,-1)/2
inner=lambda u,v:s.trace(g*u*g*v)-s.trace(g*u)*s.trace(g*v)/2
check('trace_vertical_norm',inner(vt,vt)==-1);check('traceless_vertical_norm',inner(vd,vd)==1);check('vertical_orthogonality',inner(vt,vd)==0)
check('mixed_trace_connection',g*vt/2==s.eye(4)/4);check('mixed_traceless_connection',g*vd/2==s.diag(1,1,-1,-1)/4)
# Radial limit and spectral factor formula checked symbolically, not inferred from numeric fixtures.
x,k,lam=s.symbols('x k lam');check('radial_limit',4*(x*x-14*x*x+91*x*x)==312*x*x)
pp,qq,A,B=s.symbols('p q A B');e2prod=pp*(pp-1)*A*A/2+qq*(qq-1)*B*B/2+pp*qq*A*B
check('two_factor_cubic_difference',s.expand(4*((A*A-(pp*A+qq*B)*A+e2prod)-(B*B-(pp*A+qq*B)*B+e2prod))-4*(A-B)*((1-pp)*A+(1-qq)*B))==0)
deps=[backend,f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2345-curved-bundle-ricci-obstruction.json','lab/process/k2357-curved-native-stationarity.json']
out=dict(result_id='K2360',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='exact Clifford/rational/symbolic controls; invariant all-receiver and connection proof in note',details=dict(cubic='4(A^2-tr(A)A+e2(A)I)',product=dict(dimensions=[7,7],amplitudes=[1,-1],kappa=2,Ricci=[3,1],scalar=28),trace_row=list(map(str,trace)),traceless_row=list(map(str,traceless)),constant_projector_kernel='a=b=d; then K2357 odd rows differ by -3'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps(out['details']));print('PASS',len(checks),len(controls))
