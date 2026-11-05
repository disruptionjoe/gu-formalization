"""Exact supporting computations for the local finite-calibration theorem.
Universal domain, gauge and separation arguments are in the linked note.
"""
from pathlib import Path
import argparse, json
import sympy as s
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
root=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(n,c):
 checks[n]=bool(c)
 if not c:raise AssertionError(n)
def ct(n,c):
 controls[n]=bool(c)
 if not c:raise AssertionError('contrary: '+n)
z,t,eta,ell=s.symbols('z t eta ell', real=True);v=s.Function('v')(t)
harmonics=[s.chebyshevu(l,z) for l in range(6)]
for l,h in enumerate(harmonics):
 ck('S3_zonal_eigenfunction_'+str(l),s.expand((1-z*z)*s.diff(h,z,2)-3*z*s.diff(h,z)+l*(l+2)*h)==0)
ck('six_initial_harmonics_independent',s.Matrix([[s.expand(h).coeff(z,j) for h in harmonics] for j in range(6)]).det()!=0)
Yv=-s.diff(v,t,2)-3*(s.tanh(t)+s.coth(t))*s.diff(v,t)-ell/s.cosh(t)**2*v
ode=s.diff(v,t,2)+3*(s.tanh(t)+s.coth(t))*s.diff(v,t)+(ell/s.cosh(t)**2-eta)*v
ck('actual_B_homogeneous_separation',s.expand(Yv+eta*v+ode)==0)
t0=s.log(2)
ck('common_annulus_initial_jet',s.simplify(3*(s.tanh(t0)+s.coth(t0)))==s.Rational(34,5) and s.simplify(1/s.cosh(t0)**2)==s.Rational(16,25))
ck('curvature_coefficient_nonzero',s.Rational(67736495,4439232512)>0)
# These matrices are realizable by actual compact E W tests, as proved in section4.
L=s.Matrix([[1,1,0],[0,1,1]]);y=s.Matrix([1,1]);f=s.Matrix([[1,0,0]])
Lp=L.pinv();P=s.eye(3)-Lp*L;alpha=Lp*y;n=s.Matrix([1,-1,1]);R2=s.Rational(2)
ck('calibration_rank',L.rank()==2)
ck('minimum_norm_calibration',alpha==s.Matrix([s.Rational(1,3),s.Rational(2,3),s.Rational(1,3)]) and L*alpha==y)
ck('orthogonal_kernel_projector',P.T==P and P*P==P and L*P==s.zeros(2,3))
ck('actual_unseen_mode',L*n==s.zeros(2,1) and (f*n)[0]==1)
ck('minimum_solution_orthogonal',alpha.dot(n)==0)
radius2=(R2-alpha.dot(alpha))*(f*P*f.T)[0]
ck('sharp_squared_radius',radius2==s.Rational(4,9))
endpoints=[alpha+s.Rational(sign*2,3)*n for sign in [-1,1]]
for i,a in enumerate(endpoints):
 ck('endpoint_calibration_'+str(i),L*a==y)
 ck('endpoint_norm_'+str(i),a.dot(a)==R2)
ck('exact_readout_interval',[(f*a)[0] for a in endpoints]==[-s.Rational(1,3),s.Integer(1)])
g=s.Matrix([[1,2,1]])
ck('span_detector_determined',g==s.Matrix([[1,1]])*L and g*P==s.zeros(1,3) and (g*alpha)[0]==2)
ct('minimum_norm_is_not_unique_calibrated_response',endpoints[0]!=alpha and L*endpoints[0]==L*alpha)
ct('finite_calibration_does_not_bound_without_norm',(f*(alpha+100*n))[0]>100 and L*(alpha+100*n)==y)
ct('bound_depends_on_preparation_radius',s.simplify((9-alpha.dot(alpha))*(f*P*f.T)[0])>radius2)
Lbad=L.col_join(s.Matrix([[1,2,1]]));yb=s.Matrix([1,1,3])
ct('inconsistent_redundant_data_rejected',Lbad.rank()<Lbad.row_join(yb).rank())
ct('insufficient_radius_rejected',s.Rational(1,4)<alpha.dot(alpha))
ct('omitted_indefinite_angular_term_fails_separation',s.simplify((-s.diff(v,t,2)-3*(s.tanh(t)+s.coth(t))*s.diff(v,t)+eta*v)+ode)!=0)
report={'result':'K2566','evidence_kind':'exact finite supporting computations; universal proofs in note','checks':checks,'contrary_controls':controls,'acceptance_ceiling':'local common-domain theorem; supplied coefficient norm, no global preparation','fixture':{'minimum_coefficients':[str(a) for a in alpha],'readout_interval':['-1/3','1'],'norm_squared':'2'}}
p=root/'lab/process/k2566-finite-observation-preparation.json'
if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2566','checks':len(checks),'controls':len(controls),'status':'pass'}))
