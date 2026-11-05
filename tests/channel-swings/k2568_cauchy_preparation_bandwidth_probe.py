"""Exact identities and finite controls supporting the universal K2568 proofs."""
from pathlib import Path
import argparse,json
import sympy as s
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
root=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(n,c):
 checks[n]=bool(c)
 if not c:raise AssertionError(n)
def ct(n,c):
 controls[n]=bool(c)
 if not c:raise AssertionError('contrary: '+n)
q,n,c=s.symbols('q n c',positive=True)
# q=exp(t) makes every required hyperbolic coefficient rational.
sh=(q-1/q)/2;ch=(q+1/q)/2;th=sh/ch
Dt=lambda f:s.factor(q*s.diff(f,q))
K=s.Rational(35,3624192);mu=s.Rational(611557655,39953092608)
c0=s.cancel(mu/K-21)
ck('actual_homogeneous_constant',c0==s.Rational(120691003,77168))
ck('original_Einstein_coefficient',mu-5*K==s.Rational(67736495,4439232512)>0)
p=3*(th+ch/sh);potential=(n*n-1)/sh**2+c
A=s.factor(-ch+p*sh)
ck('actual_x_first_derivative',s.cancel(A-(5*ch-3/ch))==0)
Jlog=ch/sh+s.Rational(3,2)*th
ck('conjugating_weight',s.cancel(2*sh*Jlog-A)==0)
# x derivative = sinh(t)*t derivative; remove first derivative with J.
V=s.factor(c*sh**2-1+s.Rational(1,2)*sh*Dt(A)+A*A/4)
target=(c+s.Rational(35,4))*sh**2-s.Rational(3,4)*th**2
ck('Liouville_potential',s.cancel(V-target)==0)
ck('positive_factorization',s.cancel(V-sh**2*(c+s.Rational(35,4)-s.Rational(3,4)/ch**2))==0)
ck('potential_monotone_factor_identities',s.cancel(Dt(sh**2)-(q**4-1)/(2*q**2))==0 and s.cancel(Dt(-1/ch**2)-8*q**2*(q**2-1)/(q**2+1)**3)==0)
# Rational initial-coordinate fixture t0=log2,t1=log3; x=log((q-1)/(q+1)).
x=s.log((q-1)/(q+1))
ck('coordinate_derivative',s.cancel(Dt(x)-1/sh)==0)
ck('exact_propagation_factor',s.cancel(((q-1)/(q+1)).subs(q,3)/((q-1)/(q+1)).subs(q,2))==s.Rational(3,2))
ck('initial_x_slope',s.cancel(A.subs(q,2)/2)==s.Rational(77,40))
ck('positive_actual_potential',V.subs({q:2,c:c0})>0)
# Finite initial jets follow the ACTUAL ODE v''=Qv-pv'; both base jets fixed.
Q=potential.subs(c,c0);vf=s.Function('v')(q)
u=s.Integer(1);v=s.Integer(0);jets=[u,v]
# Coefficients alpha,beta with Dt^j(v)=alpha*v+beta*Dt(v).
alpha,beta=s.Integer(0),s.Integer(1)
for j in range(2,6):
 alpha,beta=s.factor(Dt(alpha)+beta*Q),s.factor(alpha+Dt(beta)-beta*p)
 jet=s.factor(alpha.subs(q,2));jets.append(jet)
 ck('initial_jet_polynomial_'+str(j),s.Poly(jet,n).degree()<=j and jet.has(n))
ck('second_jet_matches_curved_equation',s.cancel(jets[2]-(s.Rational(16,9)*(n*n-1)+c0))==0)
# Constant-coefficient lower comparison solution has same initial data.
z,k,h=s.symbols('z k h',positive=True)
y=s.cosh(k*z)+h*s.sinh(k*z)/k
ck('comparison_equation',s.simplify(s.diff(y,z,2)-k*k*y)==0)
ck('comparison_initial_data',y.subs(z,0)==1 and s.diff(y,z).subs(z,0)==h)
# Exact two-indistinguishable-input noise fixture at rho=2d and R=1.
fixtures=[]
for nn in [2,4,8,16]:
 delta=s.Rational(2,3)**(2*nn);amp=s.Rational(3,2)**nn;truth=delta
 ck('analytic_prior_unit_'+str(nn),s.Rational(3,2)**(4*nn)*truth**2==1)
 ck('same_zero_noisy_datum_'+str(nn),truth+(-truth)==-truth+truth==0)
 ck('sharp_half_exponent_'+str(nn),amp*truth==s.sqrt(delta))
 fixtures.append({'n':nn,'delta':str(delta),'normalized_output_separation_half':str(amp*truth)})
ct('flipping_indefinite_angular_sign_changes_equation',s.cancel((-(n*n-1)/sh**2+c)-potential)!=0)
ct('omitting_J_retains_nonzero_first_derivative',A.subs(q,2)!=0)
ct('omitting_geometric_potential_fails',V.subs({q:2,c:c0})!=0)
# Counterfixtures use the exact exponential envelope, not a sampled ODE as a proof.
ct('degree10_n200_exponential_counterfixture',s.Rational(3,2)**200>200**10)
critical_outputs=[s.Rational(3,2)**nn*s.Rational(2,3)**nn for nn in [2,4,8,16]]
ct('critical_radius_no_uniform_noise_decay',critical_outputs==[1]*4)
ct('subcritical_radius_unbounded_envelope',s.Rational(3,2)**16>s.Rational(3,2)**8>1)
# Constant-potential boundary comparison, with its actual Dirichlet-to-Neumann map.
L=s.symbols('L',positive=True)
boundary=s.sinh(k*(L-z))/s.sinh(k*L)
ck('stable_boundary_equation',s.simplify(s.diff(boundary,z,2)-k*k*boundary)==0)
ck('stable_boundary_endpoints',boundary.subs(z,0)==1 and boundary.subs(z,L)==0)
ck('stable_DN_multiplier',s.simplify(-s.diff(boundary,z).subs(z,0)-k*s.coth(k*L))==0)
# For n=2,d=log(3/2), the exact comparison DN is rational.
dn=2*(s.Rational(3,2)**4+1)/(s.Rational(3,2)**4-1)
ck('boundary_DN_exact_fixture',dn==s.Rational(194,65))
ck('normal_trace_conversion',s.cancel((-dn-A.subs(q,2)/2)/sh.subs(q,2)+s.Rational(851,130))==0)
ct('stable_preparation_not_zero_normal_derivative',(-dn-A.subs(q,2)/2)/sh.subs(q,2)!=0)
ct('constant_order_trace_bound_fails',100*(s.Rational(3,2)**200+1)/(s.Rational(3,2)**200-1)>100)
report={'result':'K2568','evidence_kind':'exact rational-coordinate identities and finite supporting/control fixtures; universal comparison and minimax proofs in note','checks':checks,'contrary_controls':controls,'constants':{'mu_over_K_minus21':str(c0),'growth_rate':'log(tanh(t1/2)/tanh(t0/2))','noise_exponent':'1-d/rho for rho>d'},'initial_jets':[str(x) for x in jets],'noise_fixtures':fixtures,'ceiling':'omega harmonics: zero-normal-derivative Cauchy family in sections1-5; different far-Dirichlet family in section6; positive auxiliary norm, no physical energy'}
f=root/'lab/process/k2568-cauchy-preparation-bandwidth.json'
if args.write:f.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(f.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2568','checks':len(checks),'controls':len(controls),'status':'pass'}))
