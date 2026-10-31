"""Exact calibration/profiling identities and countercontrols; --write saves report."""
from pathlib import Path
import sympy as s
import hashlib,json,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v,control=False):
 v=bool(v);(controls if control else checks)[k]=v;assert v,k
t,a=s.symbols('t a',real=True);E=s.eye(4);Xi=(3*E).row_join(s.zeros(4,5));O=Xi*Xi.T/9
ck('raw_calibration_identity',O==E)
Rt=s.Matrix([[-t,1,0,0],[0,0,-t,1]]);Sh=Rt*O*Rt.T
ck('projected_scatter',Sh==(1+t*t)*s.eye(2))
z=s.Matrix([1,a,1,-a]);q=s.factor(((Rt*z).T*Sh.inv()*(Rt*z))[0]);ck('same_gain_statistic',s.simplify(q-2*(a*a+t*t)/(1+t*t))==0)
ck('global_minimum_identity',s.simplify(q.subs(a,3)-10-8*(1-t*t)/(1+t*t))==0)
ck('threshold_tail', (1+s.Rational(9,9))**-4==s.Rational(1,16))
ck('certified_strict_rejection',10>9)
ck('wider_gain_removes_reject',q.subs({a:3,t:3})==s.Rational(18,5),True)
ck('grid_false_certificate',q.subs({a:3,t:0})>12 and q.subs({a:3,t:1})<12,True)
ck('scaled_noise_changes_decision',s.simplify(((Rt*z).T*(4*Sh).inv()*(Rt*z))[0]-q/4)==0 and s.Rational(10,4)<9,True)
# Exact exponential comparison exp(9/2)>16 from positive Taylor lower bound.
ck('known_noise_pivot_anti_conservative',sum(s.Rational(9,2)**j/s.factorial(j) for j in range(4))>16,True)
# Rational matrix Schur-complement identity supporting (not proving) the ratio law.
Z=s.Matrix([[1,2,0,1],[0,1,1,0]]);W=Z*Z.T
schur=W[0,0]-W[0,1]**2/W[1,1]
ck('schur_inverse_entry',1/W.inv()[0,0]==schur)
P=s.eye(4)-Z[1,:].T*(Z[1,:]*Z[1,:].T).inv()*Z[1,:]
ck('residual_projection_rank',P.rank()==3 and P*P==P)
ck('residual_projection_scatter',(Z[0,:]*P*Z[0,:].T)[0]==schur)
# Centering removes one calibration degree of freedom.
C=s.eye(9)-s.ones(9)/9
ck('centered_projection_df',C*C==C and C.rank()==8)
ck('centered_scatter',Xi*C*Xi.T==9*s.eye(4)-s.ones(4))
ck('incorrect_df_changes_scale',s.Rational(9*2,9-2+1)!=s.Rational(8*2,8-2+1),True)
x,y=s.symbols('x y',real=True);R3=s.Matrix([[-x,-y,1]]);Z3=s.Matrix([[1,0],[0,1],[1,1]]);v=(R3*Z3*Z3.T*R3.T)[0]
ck('uniform_rank_counterexample',s.expand(v-((x-1)**2+(y-1)**2))==0)
ck('pointwise_does_not_mean_uniform',v.subs({x:1,y:1})==0 and Z3.rank()==2,True)
ck('robust_small_radius_reject',(s.sqrt(10)-s.Rational(1,10))**2>9)
ck('robust_large_radius_nonreject',(s.sqrt(20)-s.Rational(1,2))**2/2<9,True)
ck('wrong_error_metric_factor',s.sqrt(1/s.Rational(1,100))==10,True)
ck('raw_signal_separation',s.expand((Rt*z).dot(Rt*z)).subs(a,10)==200+2*t*t)
ck('operator_norm_square',Rt*Rt.T==(1+t*t)*s.eye(2))
ck('nonempty_calibration_event_power_margin',s.sqrt(200)>2*s.sqrt(2)+6)
# Simultaneous covariance upper bound controls every same-gain quadratic form.
B=s.Matrix([[2,1],[1,2]]);U=4*s.eye(2);h=s.Matrix([1,2])
ck('loewner_inverse_order_fixture',all(ev>=0 for ev in (U-B).eigenvals()) and (h.T*U.inv()*h)[0] <= (h.T*B.inv()*h)[0])
paths=['lab/process/k2382-finite-sample-shared-calibration.json','lab/process/k2376-windowed-cosmological-null.json']
report={'result_id':'K2385','checks':len(checks),'check_names':checks,'changed_input_or_inference_controls':controls,'fixture':{'D':4,'d':2,'nu':9,'alpha':'1/16','threshold':9,'global_minimum':10},'scope':'Exact finite algebra and proof-backed inference controls; written Gaussian/Wishart proof owns size. No survey data or simulated coverage.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=json.dumps(report,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(R/'lab/process/k2385-estimated-noise-calibration.json').write_text(out)
print(out)
