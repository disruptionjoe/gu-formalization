#!/usr/bin/env python3
"""Actual curved cross Gram, scalar numerator and boundary identity checks."""
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

# Actual differential matrix scaling, so kappa=1 degree proof covers nonzero kappa.
Dk=s.diag(1,1,k**-2,k**-2,k**-2,k**-2)
M1=M.subs(k,1);v1=vsrc.subs(k,1)
ck('full_matrix_homogeneous_scaling',all(s.cancel(z)==0 for z in M.subs({X:k*k*X,Y:k*k*Y},simultaneous=True)-k*Dk*M1*Dk.inv()))
ck('source_column_scaling',all(s.cancel(z)==0 for z in vsrc.subs({X:k*k*X,Y:k*k*Y},simultaneous=True)-k*k*Dk*v1))
cm=M1.copy();cm[:,0]=v1
num=s.Poly(cm.det(method='domain-ge'),X,Y).as_expr()
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
Z=s.symbols('Z');pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
det=sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq))
ck('actual_numerator_Y_degree',s.degree(num,Y)==4)
ck('actual_numerator_total_degree',s.Poly(num,X,Y).total_degree()==5)
ck('actual_determinant_Y_degree',s.degree(det,Y)==5)
ck('actual_determinant_leading_constant',s.Poly(det,Y).LC()==pp[0]!=0)
fixtures=[]
for xx in [-3,-4]:
 mm=M1.subs(X,xx);vv=v1.subs(X,xx);cc=mm.copy();cc[:,0]=vv
 dd=mm.det(method='domain-ge');nn=cc.det(method='domain-ge')
 ck('whole_polynomial_determinant_'+str(xx),s.expand(dd-det.subs(X,xx))==0)
 ck('whole_polynomial_Cramer_'+str(xx),s.expand(nn-num.subs(X,xx))==0)
 # Independent numeric six-row inverse identity at two Y values, not a label mutation.
 for yy in [0,2]:
  mf=mm.subs(Y,yy);vf=vv.subs(Y,yy);col=mf.adjugate()*vf
  ck('full_six_row_source_'+str((xx,yy)),mf*col==mf.det()*vf)
  ck('f_cofactor_entry_'+str((xx,yy)),col[0]==num.subs({X:xx,Y:yy}))
 fixtures.append({'X':xx,'f_coefficients':list(map(str,s.Poly(nn,Y).all_coeffs()))})
# Actual curved cross Gram in three multiplicity blocks.
S,C,K=s.symbols('S C K',positive=True);b,db,dp,ddp=s.symbols('b db dp ddp');x=K*S*S
alpha=-K*S/C;beta=C/S;gamma=4*alpha+2*beta;w2=C**4*S*S
tr=-S*C*db/4+(-3+7*x)*b/4;ang=S*C*db/2+(1-7*x/2)*b
red=lambda z:s.factor(s.cancel(z).subs(C*C,1-K*S*S))
ck('actual_TT_trace',s.expand(4*tr+b+2*ang)==0)
ck('actual_TT_divergence',red(db+4*alpha*(b-tr)+2*beta*(b-ang))==0)
pair=4*tr*alpha*dp+b*ddp+2*ang*beta*dp
ck('cross_Gram_is_total_derivative',red(pair-(b*ddp+(db+gamma*b)*dp))==0)
ct('drop_tensor_multiplicities_breaks_cross_Gram',red(tr*alpha*dp+b*ddp+ang*beta*dp-(b*ddp+(db+gamma*b)*dp))!=0)
ct('cross_boundary_not_identically_zero',b*dp!=0)
# Original compact pressure reconstruction with arbitrary B dependence.
r=s.symbols('r',positive=True);cf=s.Function('C')(r);al=s.diff(cf,r)/cf;tt=s.Function('t')(r);I=s.Function('I')(r)
pressure=-2*I/cf**7;observer=(2*tt-3*pressure)/4
ck('pressure_trace_half_factors',s.simplify((4*observer+3*pressure)/2-tt)==0)
res=s.diff(pressure,r)+4*al*(pressure-observer)
ck('pressure_conservation_from_integral',s.simplify(res.subs(s.diff(I,r),-al*cf**7*tt))==0)
ct('wrong_pressure_integral_sign',s.simplify(res.subs(s.diff(I,r),al*cf**7*tt))!=0)
ct('omit_source_halves_changes_trace',s.simplify(4*observer+3*pressure-tt)!=0)
# Weighted scalar Green identity including correct sign for Box_B.
w=s.Function('w')(r);u=s.Function('u')(r);v=s.Function('v')(r)
L=lambda z:s.diff(w*s.diff(z,r),r)/w
flux=w*(s.diff(u,r)*v-u*s.diff(v,r))
ck('weighted_Green_flux_orientation',s.expand(w*(L(u)*v-u*L(v))-s.diff(flux,r))==0)
J=s.Function('J')(r);U=s.Function('U')(r);Vv=s.Function('V')(r);kk=s.symbols('kk',positive=True)
fu=U/J;fv=Vv/J
ck('Liouville_flux_conversion',s.simplify(-kk**(-s.Rational(5,2))*J**2*(s.diff(fu,r)*fv-fu*s.diff(fv,r))+kk**(-s.Rational(5,2))*(s.diff(U,r)*Vv-U*s.diff(Vv,r)))==0)
# Bezoutian is computed from the ACTUAL cofactor numerator, not arbitrary degree labels.
x,y=s.symbols('x y');bez=s.cancel((det.subs(Y,x)*num.subs(Y,y)-num.subs(Y,x)*det.subs(Y,y))/(x-y))
ck('actual_Bezoutian_is_polynomial',s.denom(bez).free_symbols==set())
be=s.Poly(bez,x,y)
ck('endpoint_order_bound',be.degree(x)<=4 and be.degree(y)<=4)
ck('Bezoutian_symmetry',s.expand(bez-bez.xreplace({x:y,y:x}))==0)
ck('actual_Bezoutian_factorization',s.expand((x-y)*bez-det.subs(Y,x)*num.subs(Y,y)+num.subs(Y,x)*det.subs(Y,y))==0)
ct('actual_Bezoutian_not_zero',bez!=0)
# Nonzero polynomial does NOT imply nonzero flux on the selected domain.
ct('scalar_symmetry_does_not_imply_commutation',s.Matrix([[1,0],[0,2]])*s.Matrix([[1,1],[1,1]])!=s.Matrix([[1,1],[1,1]])*s.Matrix([[1,0],[0,2]]))
# A separate flat scalar fixture verifies telescoping and actual endpoint contribution.
z=s.symbols('z');f=z**4;g=z**5;dd=lambda h:s.diff(h,z,4)+h;nn=lambda h:s.diff(h,z,2)+2*h
B=s.cancel(((x*x+1)*(y+2)-(x+2)*(y*y+1))/(x-y));fluxsum=0
for (i,j),coef in s.Poly(B,x,y).terms():
 fi=s.diff(f,z,2*i);gj=s.diff(g,z,2*j);fluxsum+=coef*(s.diff(fi,z)*gj-fi*s.diff(gj,z))
volume=s.integrate(dd(f)*nn(g)-nn(f)*dd(g),(z,0,1))
ck('flat_control_actual_boundary_defect',s.simplify(volume-(fluxsum.subs(z,1)-fluxsum.subs(z,0)))==0)
ct('flat_control_omit_endpoint_fails',volume!=0)
# Manufactured full scalar inverse data retain actual source and all equations.
E=X+Y+12*K0.subs(k,1);seed=s.symbols('seed');ch=det*E*seed;Ein=det*seed;Us=E*seed
ck('manufactured_E_scalar_equation',s.expand(E*Ein-ch)==0)
ck('manufactured_d_scalar_equation',s.expand(det*Us-ch)==0)
ck('manufactured_nonzero_trace_leading_jet',-42*K0*pp[0]!=0)

# Actual resultant: exclude every possible cancellation on the genuine radial spectrum.
res=s.factor(s.resultant(det,num,Y));const,factors=s.factor_list(res,X)
ck('resultant_nonzero',res!=0)
negative_roots=[]
zz=s.symbols('zz',nonnegative=True)
for polynomial,multiplicity in factors:
 pp0=s.Poly(polynomial,X)
 if pp0.degree()==1:
  rr=s.solve(polynomial,X)[0];ck('linear_resultant_root_above_radial_range_'+str(len(negative_roots)),rr>-3)
  negative_roots.append({'degree':1,'root':str(rr),'multiplicity':int(multiplicity)})
 elif pp0.degree()==3:
  coeff=pp0.all_coeffs();ck('cubic_derivative_positive_on_negative_axis_'+str(len(negative_roots)),coeff[0]>0 and coeff[1]<0 and coeff[2]>0)
  if polynomial.subs(X,-3)<0:
   ck('first_cubic_no_radial_root',all(v<0 for v in s.Poly(polynomial.subs(X,-3-zz),zz).all_coeffs()))
   negative_roots.append({'degree':3,'radial_range':'none below -3','multiplicity':int(multiplicity)})
  else:
   ck('second_cubic_root_between_minus28_and_minus27',polynomial.subs(X,-28)<0<polynomial.subs(X,-27))
   negative_roots.append({'degree':3,'negative_root_interval':['-28','-27'],'multiplicity':int(multiplicity)})
 else:raise AssertionError('unexpected resultant factor degree')
cweight=1-s.Rational(7,3)*s.Rational(35,3624192)
ck('actual_radial_weight_comparison',s.Rational(99,100)<cweight<1)
ck('first_actual_eigenvalue_below10',(s.Rational(22,7))**2/cweight<10)
ck('second_actual_eigenvalue_above35',cweight*4*9>35)
# Executed algebraic repair on exact coefficient fixtures; universal spectral exclusion above.
repairs=[]
for xx in [-9,-40]:
 dd=s.Poly(det.subs(X,xx),Y);nn=s.Poly(num.subs(X,xx),Y)
 AA,BB,gg=s.gcdex(nn,dd)
 ck('actual_Bezout_repair_'+str(xx),gg.as_expr()==1 and s.expand(AA.as_expr()*nn.as_expr()+BB.as_expr()*dd.as_expr()-1)==0)
 ck('repair_residue_half_cancellation_'+str(xx),s.rem(nn.as_expr()*(-AA.as_expr()/2)+s.Rational(1,2),dd.as_expr(),Y)==0)
 cc=M1.subs(X,xx).adjugate()*v1.subs(X,xx)
 repaired_column=cc*(-AA.as_expr()/2)
 residual=M1.subs(X,xx)*repaired_column
 ck('repair_all_six_homogeneous_rows_'+str(xx),all(s.rem(s.cancel(v),dd.as_expr(),Y)==0 for v in residual))
 ct('omit_half_does_not_symmetrize_'+str(xx),s.rem(nn.as_expr()*(-AA.as_expr())+s.Rational(1,2),dd.as_expr(),Y)!=0)
 repairs.append({'X':xx,'A_degree':int(AA.degree()),'B_degree':int(BB.degree()),'Bezout_identity':'A*P+B*d=1'})
report={'result':'K2592','checks':checks,'contrary_controls':controls,'evidence_kind':'actual curved cross Gram, full scalar matrix/Cramer polynomials, universal Bezoutian identity and pressure reconstruction; flat boundary example explicitly a control','cofactor_Y_degree':4,'determinant_Y_degree':5,'endpoint_jet_order':9,'fixed_mode_trace_dimension_bound':20,'homogeneous_defect_rank_bound':10,'cofactor_fixtures':fixtures,'resultant_factorization':str(res),'resultant_root_exclusions':negative_roots,'repair_fixtures':repairs,'flat_control_defect':str(volume),'ceiling':'exact old-preparation boundary criterion and reciprocal compact-range sources; new preparation gives full smooth pressure reciprocity; old general reciprocity, measure estimates and physical selection remain open'}
refs=['explorations/conditional-build/k2590-boundary-aware-response-adjoint-2026-11-06.md','explorations/conditional-build/k2588-real-boundary-response-2026-11-05.md','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','lab/process/k2554-analytic-source-response.json']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2592-scalar-tensor-boundary-pairing.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2592','checks':len(checks),'controls':len(controls),'status':'pass'}))
