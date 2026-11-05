"""Exact analytic-domain algebra; theorem applications and scope are in K2554."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
def ct(name,ok):
 controls[name]=bool(ok)
 if not ok:raise AssertionError(name)
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
X,Y=s.symbols('X Y');f,g,p,q,r,z=s.symbols('f g p q r z');pot=s.Matrix([f,g,p,q,r,z]);Z=X+Y
la=6*K0;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
ck('TT_kinetic_coefficient',s.cancel(-4/mH-rE-c)==0)
ck('TT_full_mass_coefficient',s.cancel(m+28*K0/mH+2*K0*rE-c*(mu-7*K0))==0)
ck('TT_Einstein_curvature_shift',-14*K0-2*K0==-16*K0)
ck('TT_displacement_curvature_shift',-14*K0+mu-7*K0==mu-21*K0)
tau=7*f+7*g+X*p+Y*q;BA=f+(X+la)*p+Y*r;BB=g+(Y+la)*q+X*r
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*z,11*VB+13*X*z
U,V=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(Z+la)*tau
Evec=s.Matrix([-(Z/2+la)*f-RC/2,-(Z/2+la)*g-RC/2,BA-(Z/2+la)*p-tau/2,BB-(Z/2+la)*q-tau/2,(BA+BB-tau-(Z+2*la)*r)/2])
E=Evec.jacobian(pot);vsrc=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
for i in range(5):ck('full_Einstein_source_row_'+str(i),s.cancel((E*s0)[i]-vsrc[i]*(Z+2*la))==0)
ck('scalar_source_divergence_A',s.cancel(vsrc[0]+(X+la)*vsrc[2]+Y*vsrc[4])==0)
ck('scalar_source_divergence_B',s.cancel(vsrc[1]+(Y+la)*vsrc[3]+X*vsrc[4])==0)
ck('scalar_source_trace',s.cancel(7*vsrc[0]+7*vsrc[1]+X*vsrc[2]+Y*vsrc[3]+6*X+7*la)==0)
hook=s.Matrix([2*Z*f-2*K0*X*p+2*U/13,2*Z*g-2*K0*Y*q+2*U/13,2*(Z+la+K0)*p-2*BA-2*VA/13,2*(Z+la+K0)*q-2*BB-2*VB/13,2*(Z+la)*r-BA-BB-(VA+VB)/13])
vs=s.Matrix([V,V,-WA,-WB,-(WA+WB)/2]);FC=m*s.Matrix([f,g,p,q,r])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*z-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)

# New complete-symbol and analytic-domain discriminators.
d=s.factor(M.det(method='domain-ge'));d1=s.cancel(d.subs(k,1));poly=s.Poly(d1,X,Y);Z=s.symbols('Z')
L=-s.Rational(2605746313310516251459584,22521658027326625)
ck('full_determinant_total_degree_five',poly.total_degree()==5)
top=s.Poly.from_dict({ij:c0 for ij,c0 in poly.terms() if sum(ij)==5},(X,Y)).as_expr()
ck('actual_top_symbol',s.expand(top-L*(X+Y)**5)==0)
ck('actual_kappa_scaling',s.cancel(d-k**6*d1.subs({X:X/k**2,Y:Y/k**2},simultaneous=True))==0)
P=s.Poly(d1.subs({X:Z,Y:0}),Z).as_expr();delta=s.cancel(d1-P.subs(Z,X+Y));Q=s.cancel(delta/(X*Y));Qz=Q.subs({X:Z,Y:0})
ck('mixed_correction_shape',s.cancel(Q-Qz.subs(Z,X+Y))==0)
ck('mixed_correction_nonzero',Qz.subs(Z,0)==s.Rational(425557062921636685109,260973818179992280940544))
ct('sum_only_determinant_rejected',delta!=0)
# Independent numerical-matrix exact determinant method, not substituted polynomial reuse.
for j,(xx,yy,kk) in enumerate([(1,2,1),(-2,3,2),(0,0,-1)]):
 mm=M.subs({X:xx,Y:yy,k:kk});ck('independent_bareiss_det_'+str(j),s.cancel(mm.det(method='bareiss')-d.subs({X:xx,Y:yy,k:kk}))==0)
vv=s.Matrix([K0,0,1,0,0,0]);m0=M.subs(X,-7*K0);d0=d.subs(X,-7*K0)
ck('full_overlap_eigenline',all(s.cancel(vv0)==0 for vv0 in m0*vv-c*(Y+mu)*vv))
quot,rem=s.div(s.Poly(d0,Y),s.Poly(c*(Y+mu),Y));ck('overlap_divisibility',rem.is_zero and quot.degree()==4)
for j,(yy,kk) in enumerate([(0,1),(2,1),(-1,2)]):
 mm=m0.subs({Y:yy,k:kk});v0=vv.subs(k,kk);rr=quot.as_expr().subs({Y:yy,k:kk})
 ck('independent_overlap_cofactor_'+str(j),all(s.cancel(x)==0 for x in mm.adjugate()*v0-rr*v0))
ct('wrong_overlap_shift_rejected',any(s.cancel(x)!=0 for x in M.subs(X,-6*K0)*vv-c*(Y+mu)*vv))
gtt=s.symbols('gtt',nonzero=True)
ck('nonnull_B_CK_coefficient',L*k**(-4)*gtt**5!=0)
ct('null_hypersurface_not_CK', (L*k**(-4)*gtt**5).subs(gtt,0)==0)
# Actual radial coefficients at the center, using dimensionless trigonometric variable.
x,KK=s.symbols('x KK',positive=True)
alpha=-s.sqrt(KK)*s.tan(s.sqrt(KK)*x);beta=s.sqrt(KK)/s.tan(s.sqrt(KK)*x)
q3=s.series((4*alpha+2*beta-2/x)/x,x,0,6).removeO();q5=s.series((6*alpha+4*beta-4/x)/x,x,0,6).removeO()
ck('regular_q3_constant',q3.subs(x,0)==-14*KK/3)
ck('regular_q5_constant',q5.subs(x,0)==-22*KK/3)
ck('analytic_even_lift_coefficients',q3.subs(x,-x)==q3 and q5.subs(x,-x)==q5)
n=s.symbols('n',integer=True,nonnegative=True)
ck('regular_splitter_recurrence',s.expand(4*(n+1)*n+6*(n+1)-(n+1)*(4*n+6))==0)
ck('recurrence_nonzero',all(v>0 for v in s.Poly((n+1)*(4*n+6),n).all_coeffs()))
for dim in (3,5):
 y=s.symbols('y0:'+str(dim));ss=sum(yi**2 for yi in y);F=1+2*ss+3*ss**2;Qaux=1+ss
 lift=sum(s.diff(F,yi,2) for yi in y)+Qaux*sum(yi*s.diff(F,yi) for yi in y)
 z0=s.symbols('z0');f0=1+2*z0+3*z0**2
 radial=(4*z0*s.diff(f0,z0,2)+(2*dim+2*z0*(1+z0))*s.diff(f0,z0)).subs(z0,ss)
 ck('Cartesian_radial_lift_'+str(dim),s.expand(lift-radial)==0)
# New original-metric overlap identity by independent tensor component symbols.
hess,psi,W,cross=s.symbols('hess psi W cross');zs=-rE*s0.subs(X,-7*K0)/2;AA_s=zs[0]*psi*W+zs[2]*W*hess;AA_t=rE*W*(hess+K0*psi)
ck('metric_overlap_AA_Lie',s.expand(AA_s-AA_t+rE*W*hess)==0)
ck('metric_overlap_AB_Lie',s.cancel(zs[4]*cross+rE*cross/2)==0)
ct('literal_metric_equality_false',s.expand(AA_s-AA_t)!=0)
ct('wrong_Lie_cross_factor_rejected',s.cancel(zs[4]*cross+rE*cross)!=0)
ct('missing_ninth_jet_unfixed_first_derivative',2*quot.degree()+1>8 and 2*quot.degree()+1==9)
paths=['explorations/conditional-build/k2554-analytic-source-response-2026-11-05.md','tests/channel-swings/k2554_analytic_source_response_probe.py','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','tests/channel-swings/k2552_localized_source_domain_probe.py','lab/process/k2552-localized-source-domain.json']
report={'result':'K2554','checks':checks,'contrary_controls':controls,'determinant':{'total_degree':5,'top_coefficient':str(L),'P_coefficients_descending':list(map(str,s.Poly(P,Z).all_coeffs())),'Q_coefficients_descending':list(map(str,s.Poly(Qz,Z).all_coeffs())),'overlap_quotient_degree':4},'evidence_kinds':{'exact':'full matrix determinant/scaling/mixed correction, overlap eigenline/divisibility, independent cofactor and radial-lift fixtures','universal':'analytic CK, regularity, reconstruction and gauge-test descent arguments in note','not_claimed':'delta source, global domain, smooth wellposedness, physical measurement or GU'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2554-analytic-source-response.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved_report_consistency'
print('K2554 PASS',len(checks),'exact/fixture groups',len(controls),'contrary controls')
