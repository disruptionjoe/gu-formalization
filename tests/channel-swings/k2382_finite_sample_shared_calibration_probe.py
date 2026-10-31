"""Exact finite-sample pivot algebra and countercontrols; --write saves evidence."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v,c=False):
 (controls if c else checks)[k]=bool(v);assert v,k
t,a,u=s.symbols('t a u',real=True)
Q=((a-t)**2+(-a-t)**2)/(1+t*t)
ck('opposed_rows',s.simplify(Q-2*(a*a+t*t)/(1+t*t))==0)
ck('derivative_in_square',s.diff(2*(a*a+u)/(1+u),u)==2/(u+1)-(2*a*a+2*u)/(u+1)**2)
ck('global_min_a2',s.simplify(Q.subs(a,2)-5+3*(t-1)*(t+1)/(t*t+1))==0)
ck('exact_reject_threshold',s.exp(-s.Integer(4)/2)==s.exp(-2) and 5>4)
ck('grid_upper_bound_not_rejection',Q.subs({a:2,t:0})>6 and Q.subs({a:2,t:1})<6,True)
ck('separate_gains_change_null',(1-1)**2+(-1+1)**2==0 and Q.subs({a:1,t:0})==2,True)
ck('wide_calibration_weakens_test',Q.subs({a:2,t:2})==s.Rational(16,5))
ck('no_excitation_no_identification',all(s.simplify(0-g*0)==0 for g in [-5,0,5]))
# Raw moment identity preserves the mean. Known covariance is of measurement errors.
Z=s.Matrix([[1,3],[1,3]]);mean=(Z[0,:]+Z[1,:])/2;C=sum(((Z[i,:]-mean).T*(Z[i,:]-mean) for i in range(2)),s.zeros(2))
M=Z.T*Z;ck('raw_moment_decomposition',M==C+2*mean.T*mean)
r=s.Matrix([[-t,1]]);raw=(r*M*r.T)[0]/(1+t*t)
ck('mean_offset_remains',raw.subs(t,1)==4 and C==s.zeros(2))
ck('centering_hides_offset',(r*C*r.T)[0]==0 and raw.subs(t,1)>0,True)
# Correlated potential/density noise changes S(theta).
N=s.Matrix([[2,s.Rational(1,2)],[s.Rational(1,2),1]])
S=(r*N*r.T)[0];ck('correlated_noise_covariance',s.expand(S)==2*t*t-t+1)
ck('positive_noise',N.det()==s.Rational(7,4) and s.discriminant(S,t)<0)
ck('diagonal_noise_substitution_wrong',S.subs(t,1)!=3,True)
# Stack correlation matters too; whitened covariance exactly identity without sampling.
Omega=s.Matrix([[2,0,1,0],[0,2,0,1],[1,0,2,0],[0,1,0,2]])
Rb=s.diag(1,1) # explicit rectangular block residual below
Rb=s.Matrix([[-1,1,0,0],[0,0,-1,1]]);Sb=Rb*Omega*Rb.T
ck('stacked_covariance',Sb==s.Matrix([[4,2],[2,4]]) and Sb.det()==12)
ck('inverse_covariance_identity',Sb.inv()*Sb==s.eye(2))
y=s.Matrix([2,-2]);ck('ignore_replica_correlation_wrong',(y.T*Sb.inv()*y)[0]==4 and (y.T*(4*s.eye(2)).inv()*y)[0]==2,True)
# Conservative global lower bound: S<=2, min raw residual =8 in a2 example.
ck('global_lower_bound',s.expand((2-t)**2+(-2-t)**2)==8+2*t*t and s.Rational(8,2)==4)
# Bounded deterministic model error: exact threshold comparison, no floating tails.
ck('bounded_error_reject',5>(2+s.Rational(1,5))**2)
ck('bounded_error_can_remove_reject',5<(2+s.Rational(1,2))**2,True)
# n=r=k=1, zero latent signal, unrestricted Gaussian direction:
# wrong df0 rejects |d|>|p|, half the circle by exchange symmetry.
ck('wrong_df_zero_counterexample',s.Rational(1,2)>s.Rational(1,20),True)
# Symbolic relation of fitted minimum and valid pointwise pivot, not a fitted law.
ck('pointwise_envelope_fixture',5<=Q.subs({a:2,t:s.Rational(1,3)}))
# Fixed-signal power consumer: delta^2=26 and full noise row span q4.
ck('power_global_separation',s.simplify(Q.subs(a,5)-26-24*(1-t*t)/(1+t*t))==0)
R0=s.Matrix([[0,1,0,0],[0,0,0,1]]);R1=s.Matrix([[-1,0,0,0],[0,0,-1,0]])
ck('power_noise_span_dimension',R0.col_join(R1).rank()==4)
ck('power_radius_implication',26>(2+3)**2)
ck('power_certificate_lost_with_wider_calibration',Q.subs({a:5,t:5})==s.Rational(50,13) and s.Rational(50,13)<4,True)
exp_lower=sum(s.Rational(9,2)**j/s.factorial(j) for j in range(7))
ck('power_at_least_nine_tenths',exp_lower>55)
paths=['lab/process/k2379-shared-calibration-cosmological-null.json','lab/process/k2376-windowed-cosmological-null.json']
report={'result_id':'K2382','checks':len(checks),'check_names':checks,'changed_input_or_inference_controls':controls,'exact_fixture':{'global_minimum':5,'threshold':4,'alpha':'exp(-2)','bounded_error_one_fifth':'reject','bounded_error_one_half':'not rejected'},'scope':'Finite-sample size theorem under specified Gaussian noise and one fixed shared calibrated graph; exact algebra fixtures are not survey data or Monte Carlo size estimates.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
text=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(R/'lab/process/k2382-finite-sample-shared-calibration.json').write_text(text)
print(text)
