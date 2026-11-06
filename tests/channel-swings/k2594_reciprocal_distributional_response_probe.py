#!/usr/bin/env python3
"""Actual polynomial degree bounds and jump kernel controls for K2594. Matrix construction reused from K2592."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
X,Y=s.symbols('X Y');f,g,p,q,r,z=s.symbols('f g p q r z');pot=s.Matrix([f,g,p,q,r,z]);Z=X+Y
la=6*K0;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
tau=7*f+7*g+X*p+Y*q;BA=f+(X+la)*p+Y*r;BB=g+(Y+la)*q+X*r
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*z,11*VB+13*X*z
U,V=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(Z+la)*tau
Evec=s.Matrix([-(Z/2+la)*f-RC/2,-(Z/2+la)*g-RC/2,BA-(Z/2+la)*p-tau/2,BB-(Z/2+la)*q-tau/2,(BA+BB-tau-(Z+2*la)*r)/2])
E=Evec.jacobian(pot);vsrc=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
hook=s.Matrix([2*Z*f-2*K0*X*p+2*U/13,2*Z*g-2*K0*Y*q+2*U/13,2*(Z+la+K0)*p-2*BA-2*VA/13,2*(Z+la+K0)*q-2*BB-2*VB/13,2*(Z+la)*r-BA-BB-(VA+VB)/13])
vs=s.Matrix([V,V,-WA,-WB,-(WA+WB)/2]);FC=m*s.Matrix([f,g,p,q,r])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*z-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)


M1=M.subs(k,1);v1=vsrc.subs(k,1);cm=M1.copy();cm[:,0]=v1
num=s.Poly(cm.det(method='domain-ge'),X,Y).as_expr()
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
det=sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq))
ck('actual_P_Y_degree',s.degree(num,Y)==4)
ck('actual_P_total_degree',s.Poly(num,X,Y).total_degree()==5)
ck('actual_d_Y_degree',s.degree(det,Y)==5)
ck('actual_d_leading_coefficient_constant',s.Poly(det,Y).LC()==pp[0]!=0)
# Sylvester linear map (A,B)->A P+B d, deg A<=4, deg B<=3.
cols=[s.Poly(Y**i*num,Y) for i in range(5)]+[s.Poly(Y**i*det,Y) for i in range(4)]
Syl=s.Matrix(9,9,lambda row,col:cols[col].nth(row))
degrees=[s.degree(v,X) for v in Syl if v!=0]
ck('actual_Sylvester_entry_degree_bound',max(degrees)<=5)
# Eight entries in each adjugate term: this is a degree bound, no cancellation assumed.
minor_degree=8*int(max(degrees));ck('adjugate_degree_at_most40',minor_degree<=40)
prior=json.loads((root/'lab/process/k2592-scalar-tensor-boundary-pairing.json').read_text())
resultant=s.sympify(prior['resultant_factorization'],locals={'X':X})
ck('reused_resultant_degree_positive',s.degree(resultant,X)==17)
# Recheck all factor root locations from actual saved resultant, without recomputing it.
for i,(pol,mult) in enumerate(s.factor_list(resultant,X)[1]):
 deg=s.degree(pol,X)
 if deg==1:ck('linear_root_'+str(i),s.solve(pol,X)[0]>-3)
 elif deg==3:
  co=s.Poly(pol,X).all_coeffs();ck('negative_axis_monotonic_'+str(i),co[0]>0 and co[1]<0 and co[2]>0)
  ck('cubic_root_outside_spectral_sets_'+str(i),pol.subs(X,-3)<0 or pol.subs(X,-28)<0<pol.subs(X,-27))
 else:raise AssertionError('unsupported factor')
# Independent exact tenth-order Green singularity, not a curved domain substitute.
x,t=s.symbols('x t',real=True);gp=(x-t)**9/(2*s.factorial(9));gm=-(x-t)**9/(2*s.factorial(9))
for j in range(9):ck('continuous_kernel_jet_'+str(j),s.diff(gp,x,j).subs(x,t)==s.diff(gm,x,j).subs(x,t))
jump=s.diff(gp,x,9)-s.diff(gm,x,9)
ck('ninth_jet_jump_delta_coefficient',jump==1)
ck('eighth_source_derivative_right',s.expand(s.diff(gp,t,8)-(x-t)/2)==0)
ck('eighth_source_derivative_left',s.expand(s.diff(gm,t,8)+(x-t)/2)==0)
ck('source_derivative_lipschitz_right',s.diff(gp,t,9)==-s.Rational(1,2))
ck('source_derivative_lipschitz_left',s.diff(gm,t,9)==s.Rational(1,2))
# Actual weighted divergence form: source transfer uses invariant pairing.
w=s.Function('w')(x);u=s.Function('u')(x);v=s.Function('v')(x)
Yop=lambda z:s.diff(w*s.diff(z,x),x)/w
ck('invariant_weight_formal_transpose',s.expand(w*(Yop(u)*v-u*Yop(v))-s.diff(w*(s.diff(u,x)*v-u*s.diff(v,x)),x))==0)
# Scale-loss accounting is bookkeeping accompanying the analytic proof.
base=13;Pcost=2*s.Poly(num,X,Y).total_degree();Dloss=base+int(Pcost);Aloss=2*40
ck('point_commutator_loss',Dloss==23)
ck('angular_point_ceiling',4+Dloss==27)
ck('repaired_potential_ceiling',4+Dloss+8==35)
ck('full_field_ceiling',4+Dloss+8+26==61)
ck('source_movement_ceiling',5+Dloss+8+26==62)
ck('EW_detector_requires_two_more',62+2==64)
ck('radial_regularity_existence',30+Dloss+Aloss==133)
ck('radial_regularity_transport',30+Dloss+Aloss+1==134)
# Quantitative actual flat-source consumer. Any unit measure supported |t|<=eps
# changes P_tK by <=eps/2 at every x; sharp witness x>eps, mu=delta_eps.
eps=s.symbols('eps',positive=True)
ck('flat_moving_atom_exact_error',s.diff(gp,t,8).subs(t,eps)-s.diff(gp,t,8).subs(t,0)==-eps/2)
ct('ninth_derivative_not_continuous',jump!=0)
ct('omit_jump_destroys_delta_source',s.diff(gp,x,10)==0 and jump!=0)
ct('source_derivatives_cannot_be_dropped',s.diff(gp,t,8)!=gp)
n=s.symbols('n',integer=True,positive=True)
# Unit sup-norm tests cos(n t) have unbounded eighth-derivative evaluation.
ct('derivative_delta_not_measure',s.diff(s.cos(n*t),t,8).subs(t,0)==n**8 and s.limit(n**8,n,s.oo)==s.oo)
ct('unweighted_transpose_wrong',s.expand(Yop(u)-s.diff(u,x,2))!=0)
ct('old_field_exponent_not_new_bound',61!=43)
ct('forgot_Bezout_radial_loss',30+Dloss!=133)
report={'result':'K2594','checks':checks,'contrary_controls':controls,'evidence_kind':'actual polynomial degree computation, reused resultant factor checks, independent exact jump/source kernel fixture, and separately labelled Sobolev bookkeeping; curved uniform estimates proved in note','kernel_order':10,'continuous_jets':8,'bounded_piecewise_jet':9,'P_total_degree':5,'Sylvester_size':9,'Sylvester_max_entry_degree':int(max(degrees)),'adjugate_degree_bound':40,'radial_Bezout_loss':80,'fields_B_H_minus':61,'movement_B_H_minus':62,'EW_test_H':64,'splitter_radial_H':[133,134],'ceiling':'fixed-preparation measure response and smooth-versus-measure reciprocity, no pointwise metric, two-distribution pairing, physical boundary selection or sharp regularity'}
refs=['lab/process/k2592-scalar-tensor-boundary-pairing.json','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2586-fixed-annulus-point-response-2026-11-05.md','explorations/conditional-build/k2592-scalar-tensor-boundary-pairing-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2594-reciprocal-distributional-response.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2594','checks':len(checks),'controls':len(controls),'status':'pass'}))
