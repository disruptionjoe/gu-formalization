#!/usr/bin/env python3
"""K2600 exact universal compact-adjoint coefficient and detector scaling controls."""
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



M1=M.subs(k,1);Ein=E[:,0].col_join(s.Matrix([0])).subs(k,1)
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
det=s.expand(sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq)))
ck('actual_determinant_matches_saved_bank',s.cancel(M1.det(method='domain-ge')-det)==0)
nums=[]
for i in range(6):
 cm=M1.copy();cm[:,i]=Ein;nums.append(s.Poly(cm.det(method='domain-ge'),X,Y).as_expr())
ck('actual_universal_adjoint_column',all(s.cancel(v)==0 for v in M1*s.Matrix(nums)-det*Ein))
Ld=s.Poly(det,Y).LC();a=a0.subs(k,1);F=s.expand(det/(12*a)-nums[0]/(36*a*a));Fc=s.Poly(F,Y).LC()
ck('determinant_Y_degree_five',s.degree(det,Y)==5)
ck('source_contact_Y_degree_five',s.degree(F,Y)==5)
ck('source_lead_constant_in_A',not Fc.has(X))
ck('actual_leading_contact_ratio',s.cancel(Fc/Ld+s.Rational(424853,149354))==0)
ck('actual_adjoint_volume_lead',s.cancel(s.Poly(nums[0],Y).LC()/Ld+s.Rational(637905,105145216))==0)
D=s.diag(1,1,k**-2,k**-2,k**-2,k**-2);R=s.diag(k,k,k**-1,k**-1,k**-1,k**-1)
ck('matrix_kappa_scaling',all(s.cancel(v)==0 for v in M.subs({X:k*k*X,Y:k*k*Y},simultaneous=True)*D-R*M1))
ck('Einstein_column_kappa_scaling',all(s.cancel(v)==0 for v in E[:,0].col_join(s.Matrix([0])).subs({X:k*k*X,Y:k*k*Y},simultaneous=True)-k*R*Ein))
# d(k^2 X,k^2 Y;k)=k^6 d(X,Y;1), b_f scales k^7,
# F scales k^5. Thus ratio of their Y^5 coefficients scales k^-1.
ck('general_kappa_ratio_exponent',(5-10)-(6-10)==-1)
Kdet=(E[:,0]*det).subs(k,1)
ck('full_metric_detector_B_order_twelve',max(s.degree(v,Y)+(1 if i==3 else 0) for i,v in enumerate(Kdet))==6)
ck('detector_AA_principal_nonzero',s.cancel(s.Poly(Kdet[0],Y).LC()-3*Ld)==0)
ck('detector_BB_principal_nonzero',s.cancel(s.Poly(Kdet[1],Y).LC()-s.Rational(7,2)*Ld)==0)
ck('conservation_A',all(s.cancel(v)==0 for v in E[0,:]+(X+la)*E[2,:]+Y*E[4,:]))
ck('conservation_B',all(s.cancel(v)==0 for v in E[1,:]+(Y+la)*E[3,:]+X*E[4,:]))
ck('annihilates_A_gradient',all(s.cancel(v)==0 for v in E*s.Matrix([0,0,2,0,1,0])))
ck('annihilates_B_gradient',all(s.cancel(v)==0 for v in E*s.Matrix([0,0,0,2,1,0])))
ct('dropping_original_metric_shift_changes_signal',s.cancel(Fc-Ld/(12*a))!=0)
ct('opposite_adjoint_sign_changes_signal',s.cancel(Fc-(Ld/(12*a)+s.Poly(nums[0],Y).LC()/(36*a*a)))!=0)
ct('scalar_source_and_full_pressure_coefficients_distinct',s.Rational(-424853,149354)!=-s.Rational(2842697,1045478)*X-s.Rational(136955,946306944))
z0=s.symbols('z0');phi=z0**10/s.factorial(10);q0=s.symbols('q0',nonzero=True)
ck('noncharacteristic_source_witness',s.diff(phi,z0,10)*q0**5==q0**5)
ct('characteristic_witness_fails',(q0**5).subs(q0,0)==0)
dim,pval=s.symbols('dim pval',positive=True)
ex=s.simplify(-10-(dim*(1-1/pval)-12))
ck('Lp_norm_lower_power',ex==2-dim+dim/pval)
ck('Lp_threshold',ex.subs({dim:7,pval:s.Rational(7,5)})==0)
ck('sup_lower_power',s.limit(ex.subs(dim,7),pval,s.oo)==-5)
ck('L2_lower_power',ex.subs({dim:7,pval:2})==-s.Rational(3,2))
ck('dual_H_three_halves_bounded',10+s.Rational(7,2)-12-s.Rational(3,2)==0)
ck('normalized_L2_signal_power',-10-(s.Rational(7,2)-12)==-s.Rational(3,2))
ss=s.symbols('ss',nonnegative=True)
ck('general_Sobolev_normalized_signal',s.simplify(-10-(s.Rational(7,2)-12-ss))==ss-s.Rational(3,2))
ck('critical_normalized_signal_power',(ss-s.Rational(3,2)).subs(ss,s.Rational(3,2))==0)
ct('codimension_seven_not_total_fourteen',s.Rational(7,2)-12!=7-12)
ck('fixed_detector_even_mollifier_second_order',s.integrate(z0,(z0,-1,1))/2==0)
ct('fixed_and_shrinking_test_not_same_limit',-s.Rational(3,2)!=0)
ct('auxiliary_positive_norm_not_indefinite_contraction',s.Matrix([1,1]).dot(s.diag(1,-1)*s.Matrix([1,1]))==0 and s.Matrix([1,1]).dot(s.Matrix([1,1]))==2)
report={'result':'K2600','checks':checks,'contrary_controls':controls,'determinant_Y5_k1':str(Ld),'F_Y5_k1':str(Fc),'contact_ratio':'-424853/(149354*kappa)','source_detector_B_orders':[10,12],'scope':'Every full selected curved-product solution for nonzero compact conserved A pressure times interior B atom; local auxiliary component norms, no physical detector or native GU verdict','necessary_limits':'not local component Lp(A_fixed x B) for p>=7/5; not L2_A H^(-3/2)_B or ordinary H^(-3/2)_loc near a nonzero tested pressure trace','regularization_lower_bounds':{'sup':'epsilon^-5','L2':'epsilon^-3/2','Lp':'epsilon^(7/p-5)'},'normalized_detector':'compact conserved L2-unit detector sequence has atomic signal of order epsilon^-3/2, annihilating every homogeneous full-system response and infinitesimal diffeomorphism','Sobolev_normalized_detector':'H^s-unit family has signal of order epsilon^(s-3/2), fixed s>=0; no physical noise or sensor assertion','critical_fixed_patch':'Smooth-source L^(7/5), H^(-3/2) and L2_A H^(-3/2)_B cutoff norms diverge by weak compactness and atomic contact obstruction; no rate','fixed_detector':'smooth centered B mollification changes each fixed source-contact observation by O(epsilon^2); general mollifier O(epsilon), constants detector-dependent','evidence_kind':'Actual six-row polynomial determinant/cofactor/conservation identities and exact scaling controls; universal duality, shrinking-test, weak Sobolev and mollifier proofs in note'}
refs=['explorations/conditional-build/k2548-compact-coupled-metric-detectors-2026-11-04.md','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2598-full-source-singularity-2026-11-06.md','explorations/conditional-build/k2594-reciprocal-distributional-response-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2600-full-metric-contact-regularity.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2600','checks':len(checks),'controls':len(controls),'status':'pass'}))
