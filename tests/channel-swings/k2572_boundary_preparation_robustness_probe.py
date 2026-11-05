#!/usr/bin/env python3
"""K2572 exact identities and finite controls; universal comparison lives in note."""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition), 'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition), 'FAIL contrary '+name
    controls.append(name)
x,d,n=s.symbols('x d n',positive=True)
S=s.sinh(n*x)/n;B=s.sinh(n*(d-x))/s.sinh(n*d);T=s.sinh(n*x)/s.sinh(n*d)
for name,f in [('S',S),('B',B),('T',T)]:
    ck(name+'_flat_comparison_ODE',s.simplify(s.diff(f,x,2)-n*n*f)==0)
ck('S_initial_value',S.subs(x,0)==0)
ck('S_initial_derivative',s.diff(S,x).subs(x,0)==1)
ck('B_initial_value',s.simplify(B.subs(x,0)-1)==0)
ck('B_far_value',B.subs(x,d)==0)
ck('T_far_value',s.simplify(T.subs(x,d)-1)==0)
beta=n*s.coth(n*d)
ck('beta_flat_DN',s.simplify(s.diff(B,x).subs(x,0)+beta)==0)
a,eps,r=s.symbols('a eps r',real=True)
y=(B+eps*S)*a
ck('perturbed_initial_value',s.simplify(y.subs(x,0)-a)==0)
ck('perturbed_initial_derivative',s.simplify(s.diff(y,x).subs(x,0)-(-beta+eps)*a)==0)
ck('perturbed_far_defect',s.simplify(y.subs(x,d)-eps*S.subs(x,d)*a)==0)
y2=B*a+T*r
ck('two_boundary_derivative',s.simplify(s.diff(y2,x).subs(x,0)+beta*a-r/S.subs(x,d))==0)
# General transfer: det=1 follows from the zero first-derivative actual ODE.
c,sp,cp,sv=s.symbols('c sp cp sv',nonzero=True)
M=s.Matrix([[c,sv],[(c*sp-1)/sv,sp]])
ck('unimodular_transfer',s.det(M)==1)
ck('DN_from_transfer',s.simplify((M*s.Matrix([a,-c*a/sv+r/sv]))[0]-r)==0)
# Independently recheck the actual potential's positive decomposition.
t=s.symbols('t',positive=True);cv=s.Rational(120691003,77168)
V=(cv+s.Rational(35,4))*s.sinh(t)**2-s.Rational(3,4)*s.tanh(t)**2
ck('actual_potential_positive_factor',s.trigsimp(V-s.sinh(t)**2*(cv+s.Rational(35,4)-s.Rational(3,4)/s.cosh(t)**2))==0)
ck('actual_potential_minimum_coefficient_positive',cv+8>0)
# Exact finite-band fixture d=log2; no numerical ODE is substituted for V.
def gain(j):return (s.Integer(2)**j-s.Rational(1,2)**j)/2
G=gain(10);eta=s.Rational(1,1000);tol=s.Rational(1,100)/G
ck('mode10_scaled_gain',G==s.Rational(1048575,2048))
ck('band_gain_increases',all(gain(j+1)>gain(j) for j in range(1,10)))
ck('mode10_mismatch_gain',eta*G==s.Rational(1048575,2048000))
ck('mode10_exact_tolerance',tol==s.Rational(512,26214375))
ck('mode10_tolerance_consumed',tol*G==s.Rational(1,100))
ct('small_polynomial_error_is_not_safe_gain',eta*G>s.Rational(1,2)>s.Rational(1,100))
ct('omit_normalization_n_changes_amplification',eta*G/10!=eta*G)
# Actual near/far correlation in a solvable positive-potential fixture:
# n=1, V=3, d=log2 gives k=2, transfer entries rational.
k=s.Integer(2);cc=s.Rational(17,8);ss=s.Rational(15,16);bb=cc/ss
ck('positive_potential_transfer_identity',cc**2-k*k*ss**2==1)
for av,rv in [(s.Rational(2,3),s.Rational(1,5)),(s.Rational(-1,3),s.Rational(2,5))]:
    slope=-bb*av+rv/ss
    ck('positive_potential_two_boundary_'+str(av),cc*av+ss*slope==rv)
ct('independent_slope_error_changes_true_far_value',cc*s.Rational(2,3)+ss*(-bb*s.Rational(2,3)+s.Rational(1,100))==ss/s.Integer(100)>0)
ck('known_stable_prior_ignores_measured_slope',cc*s.Rational(2,3)+ss*(-bb*s.Rational(2,3))==0)
# Convex contraction identity, valid for arbitrary complex phases via real bound.
u,v,A,R=s.symbols('u v A R',real=True)
ck('weighted_square_defect',s.expand((u+v)*(u*A*A+v*R*R)-(u*A+v*R)**2-u*v*(A-R)**2)==0)
for j in (1,2,4,8):
    bv=s.Rational(1,1)/(s.Integer(2)**j+s.Rational(1,2)**j)
    ck('midpoint_boundary_partition_'+str(j),0<2*bv<1)
ct('uncorrelated_jets_not_bounded_boundary_data',gain(8)>gain(4)>gain(2))
# Exponentially small normalized error produces bounded gains at equality.
vals=[s.Rational(1,2)**j*gain(j) for j in (1,2,4,8)]
ck('critical_normalized_error_bounds',all(s.Rational(3,8)<=z<s.Rational(1,2) for z in vals))
ct('critical_gain_does_not_vanish',vals[-1]>s.Rational(49,100))
# Released angular-mixing consumer in the exact flat comparison family.
Dmat=s.diag(gain(1),gain(2));Kmat=s.Matrix([[0,1],[-1,0]])
Emat=Dmat.inv()*Kmat
ck('mixed_filtered_error_endpoint',Dmat*Emat==Kmat)
ck('mixed_feedback_isometry',Kmat.T*Kmat==s.eye(2))
ct('omitting_exponential_filter_changes_mixed_endpoint',Dmat*Kmat!=Kmat)
# Square-frequency finite rank-one fixtures use a rapidly decaying sequence.
rankone=[]
for j in (2,3,4):
    freq=j*j;u=s.Rational(1,2)**j
    rankone.append(gain(freq)*u)
ck('smooth_rankone_fixture_growth',rankone[2]>rankone[1]>rankone[0]>1)
ct('small_rankone_norm_does_not_control_endpoint',rankone[-1]/100>10)
# Actual theta-sector term and rigorous oscillation certificate (not a zero scout).
ell=s.symbols('ell',nonnegative=True)
theta_term=-ell*(ell+2)/s.cosh(t)**2
ck('liouville_theta_term',s.trigsimp(s.sinh(t)**2*theta_term+ell*(ell+2)*s.tanh(t)**2)==0)
qmin=s.Integer(20164)-4*cv
ck('actual_theta200_oscillation_lower',qmin>10000)
ck('theta200_exact_coefficient',s.Integer(200)*202/2-1-4*(cv+s.Rational(35,4))==qmin)
# 3sqrt5+5>8sqrt2 proves endpoint ratio>4/3 using rational bounds.
ck('radical_lower_sqrt5',s.Rational(11,5)**2<5)
ck('radical_upper_sqrt2',s.Rational(10,7)**2>2)
ck('annulus_ratio_lower',3*s.Rational(11,5)+5>8*s.Rational(10,7))
ck('log_ratio_integral_lower',(s.Rational(4,3)-1)/s.Rational(4,3)==s.Rational(1,4))
ck('oscillation_length_inside_annulus',s.Rational(4,100)<s.Rational(1,4))
# Derive the comparison Wronskian derivative from two actual ODE residuals.
yf=s.Function('y')(x);zf=s.Function('z')(x);qf=s.Function('q')(x)
Wr=s.diff(yf,x)*zf-yf*s.diff(zf,x)
Wd=s.diff(Wr,x).subs({s.diff(yf,x,2):-qf*yf,s.diff(zf,x,2):-10000*zf})
ck('oscillation_comparison_Wronskian',s.expand(Wd-(10000-qf)*yf*zf)==0)
ct('theta_sign_omission_changes_actual_equation',theta_term.subs(ell,200)!=0)
ct('positive_potential_comparison_cannot_cover_theta200',1+4*(cv+s.Rational(35,4))-20200<0)
provenance={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['explorations/conditional-build/k2564-localized-spectral-response-2026-11-05.md','explorations/conditional-build/k2568-cauchy-preparation-bandwidth-2026-11-05.md','explorations/conditional-build/k2570-detector-recovery-2026-11-05.md']}
report={'result':'K2572','evidence_kind':'exact symbolic identities, actual potential sign factor, finite positive/zero-potential comparison fixtures and contrary controls; universal proofs separate','checks':checks,'contrary_controls':controls,'provenance':provenance,'finite_band':{'d':'log2','N':10,'normalized_error':'1/1000','flat_lower_gain':str(eta*G),'exact_flat_tolerance_for_1_over_100':str(tol)},'ceiling':'stable theta-zero family plus a proved resonant theta200 annulus; no arbitrary-fixed-domain resonance, physical selection or physical-time claim'}
out=root/'lab/process/k2572-boundary-preparation-robustness.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2572','checks':len(checks),'controls':len(controls),'status':'pass'}))
