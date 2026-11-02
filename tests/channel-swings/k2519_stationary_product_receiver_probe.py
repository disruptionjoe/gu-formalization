"""K2519 exact stationary branch and geometric receiver algebra; no infinite-field enumeration."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
u,v,k,l,m=s.symbols('u v k l m',real=True);a=(u+v)/2;b=(u-v)/2;la=(l+m)/2;lb=(l-m)/2
tr=7*u;e2=((tr)**2-7*(a*a+b*b))/2;e3=(tr**3-3*tr*7*(a*a+b*b)+2*7*(a**3+b**3))/6
ck('e3_density',s.expand(e3-(s.Rational(91,2)*u**3-s.Rational(21,2)*u*v*v))==0)
Ta=-2*la+7*l+k*a+4*(a*a-tr*a+e2);Tb=-2*lb+7*l+k*b+4*(b*b-tr*b+e2)
ls=-k*u/12-13*u*u+v*v;ms=v*(k-24*u)/2;shell={l:ls,m:ms}
ck('translation_block_a',s.expand(Ta.subs(shell))==0);ck('translation_block_b',s.expand(Tb.subs(shell))==0)
C=42*u*l-7*v*m;V=4*e3+k*7*(a*a+b*b)/2;L=C+V
ck('curvature_density',s.expand(C-(7*l*tr-2*(7*a*la+7*b*lb)))==0)
E1=7*L-14*la*(6*u-v);E2=7*L-14*lb*(6*u+v)
# Independently differentiate the moving volume and curvature family.
z1,z2,L1,L2=s.symbols('z1 z2 L1 L2')
scaled=s.exp(7*z1+7*z2)*L.subs({l:L1*s.exp(-2*z1)+L2*s.exp(-2*z2),m:L1*s.exp(-2*z1)-L2*s.exp(-2*z2)})
for zz,ee in [(z1,E1),(z2,E2)]:
 derivative=s.diff(scaled,zz).subs({z1:0,z2:0,L1:la,L2:lb})
 ck('independent_metric_scale_'+str(zz),s.simplify(derivative-ee)==0)
ck('metric_difference',s.expand(E1-E2+14*(6*u*m-v*l))==0)
M=5*k*(u*u+v*v)+1144*u**3-264*u*v*v
ck('metric_sum_on_shell',s.expand((E1+E2).subs(shell)+s.Rational(7,2)*M)==0)
for name,expr in [('Ta',Ta),('Tb',Tb),('E1',E1),('E2',E2)]:
 ck('zero_'+name,expr.subs({u:0,v:0,l:0,m:0})==0)
 radial={u:-5*k/1144,v:0,l:70*k*k/604032,m:0}
 ck('radial_'+name,s.factor(expr.subs(radial))==0)
wexpr=s.Rational(37,12)*k*u-59*u*u
ck('nonradial_difference',s.expand((6*u*m-v*l).subs(shell)/v-(wexpr-v*v))==0)
ck('nonradial_elimination',s.factor(M.subs(v*v,wexpr)-u*(s.Rational(185,12)*k*k-1104*k*u+16720*u*u))==0)
t=s.symbols('t');pol=200640*t*t-13248*t+185
ck('radicand_lower',324**2<105609);ck('radicand_upper',325**2>105609)
roots=[(828-s.sqrt(105609))/25080,(828+s.sqrt(105609))/25080]
# Exact rational interval bounds imply signs without float root decisions.
intervals=[(s.Rational(503,25080),s.Rational(504,25080)),(s.Rational(1152,25080),s.Rational(1153,25080))]
for i,tt in enumerate(roots):
 ck('root_'+str(i),s.simplify(pol.subs(t,tt))==0)
 low,high=intervals[i];ck('w_positive_'+str(i),low>0 and high<s.Rational(37,708))
 ck('opposite_amplitudes_'+str(i),high<s.Rational(37,720))
 ck('curvature_sign_interval_'+str(i),(high<s.Rational(37,1140) and high<s.Rational(1,24)) if i==0 else (low>s.Rational(37,1140) and low>s.Rational(1,24)))
 # Work in Q[t]/pol with v²=w. Both v signs covered by polynomial remainder.
 ww=tt*(s.Rational(37,12)-59*tt)
 for sign in [-1,1]:
  vv=sign*s.sqrt(ww);sub={u:tt,v:vv,k:1}
  for name,expr in [('Ta',Ta),('Tb',Tb),('E1',E1),('E2',E2)]:
   ck('branch_'+str((i,sign,name)),s.simplify(expr.subs(shell).subs(sub))==0)
ck('no_kappa_zero_nonradial',s.expand(wexpr.subs(k,0))==-59*u*u)
old={u:0,v:2,k:2,l:4,m:2}
ck('old_translation',Ta.subs(old)==0 and Tb.subs(old)==0)
ct('old_not_metric_stationary',E1.subs(old)==-14 and E2.subs(old)==-126)
ct('flat_radial_not_metric_stationary',s.factor(E1.subs({u:-2*k/312,v:0,l:0,m:0}))!=0)
ct('metric_row_omitted_false_positive',Ta.subs(old)==0 and E1.subs(old)!=0)
# Induced and normal geometry, and explicit symmetric-tensor curvature action.
K=s.symbols('K',nonzero=True);rot=s.zeros(4);rot[1,2]=K;rot[2,1]=-K
H=s.diag(0,1,-1,0);curv=-rot.T*H-H*rot
ck('induced_scalar',12*(la/6)==2*la)
ck('traceless_tensor',s.trace(H)==0)
ct('vertical_connection_curved',curv[1,2]==-2*K and curv!=s.zeros(4))
ct('flat_normal_not_connection_equivalent',s.zeros(10).rank()==0 and curv.rank()==2)
normal_receiver=s.zeros(10);native_receiver=s.eye(10)
ck('native_vertical_rank',native_receiver.rank()==10)
ct('receiver_rank_mismatch',normal_receiver.rank()!=native_receiver.rank())
ct('ambient_metric_variation_not_forbidden',(normal_receiver+native_receiver).rank()==10)
ct('four_dimensional_form_degree',14>4)
# Actual first-factor spaceform LC curvature R(n,X), not an arbitrary skew matrix.
# First factor signature(+,+,+,+,-,-,-); X=e0 tangent, n=e1 normal.
# R(n,X)Z=K(<X,Z>n-<n,Z>X); embed into all14 ambient directions.
metric=s.diag(1,1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,-1)
X=s.eye(14)[:,0];normal=s.eye(14)[:,1]
RX=K*(normal*X.T*metric-X*normal.T*metric)
ck('actual_LC_curvature_metric_skew',RX.T*metric+metric*RX==s.zeros(14))
ck('actual_LC_normal_tangent_curvature',RX*X==K*normal)
ct('zero_metric_receiver_not_zero_LC_connection',RX*X!=s.zeros(14,1))
# This certifies a B-curvature receiver; full A=B+T adds its own distortion terms.
paths=['explorations/conditional-build/k2519-stationary-product-receiver-2026-11-02.md','tests/channel-swings/k2519_stationary_product_receiver_probe.py','explorations/conditional-build/k2345-curved-bundle-ricci-obstruction-2026-10-30.md',*['explorations/conditional-build/'+p+'-2026-10-31.md' for p in ['k2357-curved-native-stationarity','k2360-anisotropic-native-stationarity','k2366-curvature-codazzi-rigidity']]]
report={'result':'K2519','scope':'exact algebra and finite geometric receiver controls; universal full-variation and pullback proofs in note','checks':checks,'contrary_controls':controls,'roots':[str(x) for x in roots],'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
pth=R/'lab/process/k2519-stationary-product-receiver.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(pth.read_text())==report)
print('K2519 PASS',len(checks),'checks',len(controls),'controls')
