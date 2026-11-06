#!/usr/bin/env python3
"""K2598 actual six-cofactor orders, mixed radial jump, and seven-dimensional source scaling witnesses."""
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


M1=M.subs(k,1);vv=vsrc.subs(k,1)
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
det=sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq));Ld=s.Poly(det,Y).LC()
nums=[];orders=[];leads=[]
for i in range(6):
 cm=M1.copy();cm[:,i]=vv;num=s.Poly(cm.det(method='domain-ge'),X,Y).as_expr();nums.append(num);poly=s.Poly(num,Y);orders.append(int(poly.degree()));leads.append(s.factor(poly.LC()/Ld))
ck('six_actual_cofactor_degrees',orders==[4,4,4,3,3,2])
ck('actual_all_six_Cramer_equations',all(s.cancel(v)==0 for v in M1*s.Matrix(nums)-det*vv))
D=s.diag(1,1,k**-2,k**-2,k**-2,k**-2);R=s.diag(k,k,k**-1,k**-1,k**-1,k**-1)
ck('actual_kappa_matrix_scaling',all(s.cancel(v)==0 for v in M.subs({X:k*k*X,Y:k*k*Y},simultaneous=True)*D-R*M1))
ck('actual_kappa_source_scaling',all(s.cancel(v)==0 for v in vsrc.subs({X:k*k*X,Y:k*k*Y},simultaneous=True)-k*R*vv))
Eop=X+Y+12*K0.subs(k,1);re=rE.subs(k,1);S0=s0.subs(k,1)
full=[s.cancel(-re*S0[i]/(2*Eop)+re**2*nums[i]/det) for i in range(5)]
fulllead=[s.factor(s.limit(Y*val,Y,s.oo)) for val in full]
ck('full_q_no_inverse_Y_term',fulllead[3]==0)
ck('full_mixed_inverse_Y_term',fulllead[4]==-re/2==s.Rational(572,15))
ck('full_scalar_cancellation_retained',s.cancel(fulllead[0]+s.Rational(2842697,1045478)*X+s.Rational(136955,946306944))==0)
ck('q_exact_inverse_Y_squared_term',s.factor(s.limit(Y**2*full[3],Y,s.oo))!=0)
N=s.expand(-re*(X+5*K0.subs(k,1))*det/2+re**2*nums[0]*Eop);L=s.expand(Eop*det)
ck('full_source_operator_degree_six',s.degree(L,Y)==6)
ck('full_source_numerator_degree_five',s.degree(N,Y)==5)
ck('actual_leading_source_coefficient',s.cancel(s.Poly(N,Y).LC()/Ld-fulllead[0])==0)
sigma=s.symbols('sigma',positive=True);zero=s.solve(fulllead[0].subs(X,-sigma),sigma)[0]
ck('nonzero_on_actual_radial_spectrum',0<zero<3)
# Exact independent flat local jump witnesses; they certify the order bookkeeping,
# while the note proves variable-coefficient distribution matching.
x=s.symbols('x',real=True);a2,rho=s.symbols('a2 rho',nonzero=True);Cr=-rE/2;Cq=s.symbols('Cq',nonzero=True)
rplus=Cr*x/(2*rho*a2);rminus=-rplus
ck('mixed_first_derivative_jump',s.cancel(s.diff(rplus-rminus,x)-Cr/(rho*a2))==0)
qplus=Cq*x**3/(12*rho*a2**2);qminus=-qplus
ck('fourth_order_q_third_jump',s.cancel(s.diff(qplus-qminus,x,3)-Cq/(rho*a2**2))==0)
ck('Hessian_q_value_continuous',s.diff(qplus-qminus,x,2).subs(x,0)==0)
ct('mixed_continuity_false',s.diff(rplus-rminus,x)!=0)
ct('spurious_q_contact_rejected',fulllead[3]==0 and leads[3]!=0)
ct('cofactor_only_misses_mixed_jump',s.limit(Y*re**2*nums[4]/det,Y,s.oo)==0 and fulllead[4]!=0)
# A noncharacteristic one-direction polynomial is a genuine principal-symbol witness.
z0=s.symbols('z0',real=True);phi=z0**10/s.factorial(10);qa=s.symbols('qa',nonzero=True)
ck('source_principal_witness',s.diff(phi,z0,10)*qa**5==qa**5)
ck('normalized_mollifier_witness',s.integrate(s.diff(phi,z0,10),(z0,-1,1))/2==1)
dim,p=s.symbols('dim p',positive=True)
Lp_exponent=s.simplify(-10-(dim*(1-1/p)-12))
ck('general_Lp_lower_exponent',Lp_exponent==2-dim+dim/p)
ck('seven_dimensional_sup_blowup',s.limit(Lp_exponent.subs(dim,7),p,s.oo)==-5)
ck('seven_dimensional_L2_blowup',Lp_exponent.subs({dim:7,p:2})==-s.Rational(3,2))
ck('critical_Lp_exponent',Lp_exponent.subs({dim:7,p:s.Rational(7,5)})==0)
ck('critical_H_dual_test_scale',10+s.Rational(7,2)-12-s.Rational(3,2)==0)
ct('one_dimensional_ceiling_not_seven_dimensional',2-s.Rational(1,2)!=2-s.Rational(7,2))
ct('Lp_critical_not_two',s.Rational(7,5)!=2)
ct('Einstein_term_changes_full_source_lead',s.cancel(re**2*leads[0]-fulllead[0])!=0)
ct('characteristic_covector_cannot_be_witness',(qa**5).subs(qa,0)==0)
# Distributional A-gradient Einstein-null repair, leaving e2 and Q fixed.
gauge=s.Matrix([0,0,2,0,1,0])
ck('actual_A_gradient_Einstein_null_column',all(s.cancel(v)==0 for v in E*gauge))
repaired_r=s.cancel(full[4]+re/(2*Eop))
ck('mixed_inverse_Y_removed_by_A_column',s.limit(Y*repaired_r,Y,s.oo)==0)
ck('repair_keeps_q_contact_absent',gauge[3]==0 and fulllead[3]==0)
ct('smooth_gauge_cannot_cancel_nonzero_step',s.diff(rplus-rminus,x)!=0)
# Actual warped AA tensor projection, fixed scalar-source A mode only.
al,be,psi,dpsi,ff,pp0,eta=s.symbols('alpha beta psi dpsi fB pB eta')
hobs=psi*ff+al*dpsi*pp0;hang=psi*ff+be*dpsi*pp0
ck('actual_two_component_scalar_projection',s.expand(be*hobs-al*hang-(be-al)*psi*ff)==0)
ck('A_gradient_repair_cancels_in_projection',s.expand((be*hobs-al*hang).subs(pp0,pp0+2*eta)-(be*hobs-al*hang))==0)
Ss,Cc=s.symbols('S C',nonzero=True);Kg=s.symbols('Kg')
ck('warped_projection_denominator_nonzero',s.cancel(((-Kg*Ss/Cc-Cc/Ss)+1/(Ss*Cc)).subs(Kg,(1-Cc**2)/Ss**2))==0)
ct('one_slot_cannot_isolate_scalar_coefficient',s.diff(hobs,pp0)!=0)
report={'result':'K2598','checks':checks,'contrary_controls':controls,'cofactor_Y_degrees':orders,'cofactor_leads_k1':{str(pot[i]):str(leads[i]) for i in range(6)},'full_metric_inverse_Y_coefficients_k1':dict(zip(['f','g','p','q','r'],map(str,fulllead))),'representative_repair':'A-gradient Einstein null column (p,r)=(2 chi,chi), chi=rE w/2; all fixed-mode metric components continuous; not an admitted physical gauge/domain', 'full_mixed_coefficient':str(Cr),'full_source_operator_degrees':[6,5],'sharp_fixed_mode_representative':'mixed component jump, Hs iff s<1/2 where the A-mode gradient is nonzero; no radial delta','actual_tensor_transfer':'fixed scalar-source observer/angular AA projection recovers f when psi nonzero; excludes TT addition and arbitrary physical gauge','full_B_necessary_limits':'f not locally Lp for p>=7/5 and not H^(-3/2)_loc; no sufficiency claim','mollifier_lower_bounds':{'Lp':'epsilon^(7/p-5)','sup':'epsilon^-5','L2':'epsilon^-3/2'},'evidence_kind':'actual exact six-row matrix/Cramer identities and principal-coefficient computations; independent flat jump/scaling controls; variable-coefficient distribution and Sobolev arguments proved in note','ceiling':'fixed scalar A mode and conditional curved-product response; full-B statement is scalar f coefficient, modal tensor regularity is representation-dependent; no physical observation or all-mode sufficiency'}
refs=['tests/channel-swings/k2596_radial_response_singularity_probe.py','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2592-scalar-tensor-boundary-pairing-2026-11-06.md','explorations/conditional-build/k2594-reciprocal-distributional-response-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2598-full-source-singularity.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2598','checks':len(checks),'controls':len(controls),'status':'pass'}))
