#!/usr/bin/env python3
"""K2609 actual source-module algebra; universal support/class proof in note."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(name,value):
    assert bool(value),'FAIL '+name
    checks.append(name)
def ct(name,value):
    assert bool(value),'FAIL contrary '+name
    controls.append(name)
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

e=X+Y+2*la
ck('actual_Einstein_scalar_source_column',all(s.cancel(t)==0 for t in E*s0-e*vsrc[:5,0]))
ck('actual_scalar_source_conservation_A',s.cancel(vsrc[0]+(X+la)*vsrc[2]+Y*vsrc[4])==0)
ck('actual_scalar_source_conservation_B',s.cancel(vsrc[1]+(Y+la)*vsrc[3]+X*vsrc[4])==0)
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
d=s.expand(sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq)))
ck('actual_determinant_rebuilt',s.cancel(M.subs(k,1).det(method='domain-ge')-d)==0)
ck('constant_nonzero_Y5_coefficient',s.degree(d,Y)==5 and s.Poly(d,Y).LC()!=0 and not s.Poly(d,Y).LC().has(X))
ck('contact_seed_degree_six',s.degree(d*e.subs(k,1),Y)==6)
fixtures=[]
for xv,yv in [(0,0),(1,2),(-2,3),(s.Rational(1,3),-s.Rational(2,5))]:
    sub={k:1,X:xv,Y:yv};mm=M.subs(sub);ee=E.subs(sub);vv=vsrc.subs(sub);en=e.subs(sub);dn=mm.det();rr=rE.subs(sub)
    qp=-rr*mm.adjugate()*vv*en;zp=-rr*s0.subs(sub)*dn/2;jp=vv*dn*en;hp=zp-rr*qp
    ck('full_six_source_rows_'+str((xv,yv)),mm*qp==-rr*jp)
    ck('Einstein_source_rows_'+str((xv,yv)),ee*zp==-rr*jp[:5,0]/2)
    ck('original_metric_rows_'+str((xv,yv)),6*a0.subs(sub)*ee*hp+ee*qp==-jp[:5,0]/2)
    if xv==1:
        bad=qp.copy();bad[5]=0
        ct('omitting_skew_breaks_full_equation',mm*bad!=-rr*jp)
        ct('shifted_metric_is_not_original',6*a0.subs(sub)*ee*zp+ee*qp!=-jp[:5,0]/2)
        ck('actual_nonzero_metric_fixture',hp[:5,0]!=s.zeros(5,1))
    fixtures.append({'X':str(xv),'Y':str(yv),'det':str(dn)})
# Actual warped scalar stress identity; coefficients, not a toy Green function.
a,b,al,al1,be,be1,l=s.symbols('a b al al1 be be1 l');u0,u1,u2,u3=s.symbols('u0:4')
H=4*al+2*be
T=al*u1-u2-H*u1-l*u0;R=-H*u1-l*u0;A=be*u1-u2-H*u1-l*u0
ck('normal_isotropy_exact_condition',s.expand(R-A)==u2-be*u1)
# alpha'+alpha^2=beta'+beta^2=-K; lambda=6K.
K=s.symbols('K');div=-(4*al1+2*be1)*u1-H*u2-l*u1+4*al*(R-T)+2*be*(R-A)
ck('actual_source_divergence',s.expand(div.subs({al1:-K-al*al,be1:-K-be*be,l:6*K}))==0)
ct('conservation_does_not_force_isotropy',(R-A).subs({u2:1,u1:0})==1)
x=s.symbols('x');rho=(1-x*x)**4
ct('compact_fixture_has_nonzero_anisotropy',s.diff(rho,x,2).subs(x,0)==-8)
# Finite jet and regularization checks are exact distribution-symbol fixtures.
xi,eta=s.symbols('xi eta');qb=xi**2-eta**2
ck('indefinite_nonzero_order_twelve_symbol',s.Poly(qb**6,xi,eta).total_degree()==12 and not s.Poly(qb**6,xi,eta).is_zero)
ct('characteristic_value_does_not_annihilate_operator',qb.subs(xi,eta)==0 and qb!=0)
ck('linear_contact_superposition',s.expand(qb**6*(a+b)-qb**6*a-qb**6*b)==0)
ct('scalar_identity_alone_does_not_check_skew',M[5,0]!=0)
# A genuine scaling control: a twelfth derivative of epsilon^-7 rho(x/epsilon)
# scales as epsilon^-19, so unit seed mass is no bounded-source claim.
eps=s.symbols('eps',positive=True);ck('twelfth_derivative_density_scaling',s.diff((x/eps)**12/eps**7,x,12)==s.factorial(12)/eps**19)
# Independent noncommutative denominator controls; NOT the uncomputed actual Ore numerator.
r=s.symbols('r',positive=True);phi=s.Function('phi')(r)
first=s.diff(phi,r);second=s.diff(phi,r)-phi/r
ck('common_RIGHT_denominator_first',s.diff(first,r)==s.diff(phi,r,2))
ck('common_RIGHT_denominator_second',s.simplify(s.diff(second,r)+second/r-s.diff(phi,r,2))==0)
wrong=s.diff(s.diff(phi,r)+phi/r,r)-(s.diff(phi,r)+phi/r)/r
ct('reversing_noncommutative_factors_fails',s.simplify(wrong-s.diff(phi,r,2))==-2*phi/r**2)
qpoly=Y+r
for j in range(4):
    coeff=s.cancel(s.diff(qpoly**4,r,j)/qpoly)
    ck('right_denominator_clear_derivative_'+str(j),s.denom(coeff)==1)
ct('one_power_does_not_clear_all_derivatives',s.denom(s.cancel(s.diff(qpoly,r)/qpoly))==Y+r)
P0,P1,P2,aa,aa1=s.symbols('P0 P1 P2 aa aa1',nonzero=True)
Aval=P0+P1/(4*aa)
ck('original_isotropic_pressure_conservation',s.simplify(P1+4*aa*(P0-Aval))==0)
ck('original_pressure_trace',s.simplify((4*Aval+3*P0)/2-(7*P0/2+P1/(2*aa)))==0)
ct('omit_pressure_derivative_breaks_conservation',P1+4*aa*(P0-P0)==P1 and P1!=0)
report={'result':'K2609','checks':checks,'contrary_controls':controls,'fixtures':fixtures,'explicit_scalar_control_B_normal_order':12,'original_pressure_B_order':'finite, at least2; numerical upper and minimum not computed','source_class':'original compact isotropic-pressure finite jets via common right denominator; explicit order12 scalar control separately anisotropic','original_isotropic_pressure_contact_existence':True,'fixed_K2594_preparation_invisibility':False,'evidence_kind':'actual exact module coefficients and rational full-row fixtures; universal cofactor/support/ODE proofs in note','ceiling':'finite-order existence, not computed actual Ore coefficients/minimum jet order, positive matter, arbitrary preparation or native GU; receiver support avoids B point'}
refs=['tests/channel-swings/k2605_source_disjoint_pressure_response_probe.py','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','explorations/conditional-build/k2548-compact-coupled-metric-detectors-2026-11-04.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2609-pressure-jet-contact-boundary.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2609','checks':len(checks),'controls':len(controls),'status':'pass'}))
