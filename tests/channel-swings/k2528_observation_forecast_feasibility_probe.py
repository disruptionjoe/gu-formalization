"""Exact shifted-domain consumer and numerical dated-forecast comparison."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]: raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]: raise AssertionError(k)
p=s.symbols('p',nonnegative=True);Xa=s.S(3);Xb=s.Rational(9,2);Y=s.Rational(36,25)
ratio2=(Xb/Xa)**2*(1+2*p*Xa)/(1+2*p*Xb)
ck('ratio_decreases',s.factor(s.diff(ratio2,p))==-s.Rational(27,4)/(9*p+1)**2)
ck('endpoint_squared_margin',s.factor(ratio2.subs(p,s.Rational(1,100))-s.Rational(29,20)**2)==s.Rational(3731,43600))
ck('common_normalized_domain',s.Rational(29,20)>Y)
ct('forecast_not_low_redshift',Xa**2/(1+2*s.Rational(1,100)*Xa)>s.Rational(29,10)**2 and Xa>s.Rational(3,2))
a,C,h,alpha,rho,q0,phi,ps,es=s.symbols('a C h alpha rho q0 phi ps es',positive=True)
weak=alpha*phi*h**(-s.Rational(1,2))/36-rho*phi*h**(-s.Rational(5,2))/216-q0*es*phi*h**(-s.Rational(5,2))/108+ps*h**s.Rational(3,2)
transformed=weak.subs({h:C*h,es:a**3*es},simultaneous=True)/C**s.Rational(3,2)
target=weak.subs({alpha:alpha/C**2,rho:rho/C**4,q0:q0*a**3/C**4},simultaneous=True)
ck('all_four_shifted_weak_columns',s.simplify(transformed-target)==0)
ct('dust_shift_omission_changes_equation',s.simplify(transformed-target.subs(a,1))!=0)
prior=json.loads((R/'lab/process/k2526-geodesic-emitter-drift-repair.json').read_text())
eta=s.Rational(prior['inherited_normalized_h_error']);rstar=s.Rational(prior['velocity_uniform_Q_oscillation_sufficient'])
bound=s.Rational(9,29)
ck('inherited_tolerance_composes',s.cancel(Y*rstar/(bound-rstar)-eta)==0)
ck('positive_scale_lower_bound',bound-rstar>0)
y=s.symbols('y',real=True);lo=s.S(1);hi=s.Rational(3,2)
psi=(y-lo)**6*(hi-y)**6;f=s.expand(y*s.diff(psi,y));amp=s.Rational(1,100)
ck('bump_anchor_integral_exact',s.integrate(f/y,(y,lo,hi))==0)
ck('bump_endpoint_jets',all(s.diff(psi,y,k).subs(y,z)==0 for k in range(6) for z in [lo,hi]))
# r(y)=(y-1)(1.5-y)<=1/16; |2.5-2y|<=1/2 and y<=3/2.
ck('bump_exact_factorization',s.expand(f-6*y*(y-lo)**5*(hi-y)**5*(lo+hi-2*y))==0)
ck('bump_product_quadratic_bound',s.expand(s.Rational(1,16)-(y-lo)*(hi-y)-(y-s.Rational(5,4))**2)==0)
ck('bump_linear_extrema',abs((lo+hi-2*y).subs(y,lo))==s.Rational(1,2) and abs((lo+hi-2*y).subs(y,hi))==s.Rational(1,2))
ck('bump_positive_denominator_bound',amp*6*hi*s.Rational(1,16)**5*s.Rational(1,2)<1)
q=amp*f/(1+amp*f);qsample=s.cancel(q.subs(y,s.Rational(9,8)))
ct('same_anchor_nonzero_oscillation',abs(qsample)>rstar and q.subs(y,lo)==0 and q.subs(y,hi)==0)
H=y/(1+amp*f)
ck('physical_comoving_drift_identity',s.cancel(q-(1-H/y))==0)
ck('anchor_preserved_before_integration',s.cancel(1/H-1/y-amp*s.diff(psi,y))==0)
da=s.sqrt(s.Rational(106,100));db=s.sqrt(s.Rational(109,100))
correct_difference=2/db-1/da
ct('dropping_doppler_in_distance_difference_changes_it',correct_difference>0 and correct_difference<1)
# A common ruler error scales both terms; it is not a ratio cancellation.
La,Lb,Da,Db,A=s.symbols('La Lb Da Db A',positive=True)
Delta=Lb/Db-La/Da
ck('common_ruler_scales_difference',s.expand(Delta.subs({La:A*La,Lb:A*Lb},simultaneous=True)-A*Delta)==0)
ct('ruler_not_cancelled',s.diff(A*Delta,A)!=0)
# Joint anchor linear uncertainty form at fixed p, including cross covariance.
sa,sb,cab=s.symbols('sa sb cab',real=True)
variance=sa**2/Da**2+sb**2/Db**2-2*cab/(Da*Db)
ck('shared_ruler_covariance_control',s.factor(variance.subs({sa:La,sb:Lb,cab:La*Lb}))==s.factor(Delta**2))
# Numerical forecast only. Parsec conversion is a declared decimal unit constant.
c=s.Integer(29979245800);year=s.Integer(31557600);T=20*year
Mpc_cm=s.Rational('3.0856775814913673e24');Href=s.Integer(7000000)/Mpc_cm
velocity_scale=c*T*Href
ck('velocity_clock_dimensionless_conversion',s.cancel(velocity_scale/(c*T)-Href)==0)
rows=[]
for z in [s.S(2),s.Rational(5,2),s.S(3),s.Rational(7,2),s.Rational(9,2)]:
 exponent=s.Rational(17,10) if z<4 else s.Rational(9,10)
 sv=s.Rational(135,100)*(s.Rational(3000,2370))**-1*(s.Rational(6,30))**(-s.Rational(1,2))*((1+z)/5)**(-exponent)
 rows.append({'z':str(z),'sigma_v_cm_per_s':str(s.N(sv,15)),'sigma_dimensionless_Q':str(s.N(sv/velocity_scale,15)),'sigma_over_illustrative_uniform_budget':str(s.N(sv/(velocity_scale*rstar/2),15))})
refs=['explorations/conditional-build/k2522-redshift-drift-interface-2026-11-02.md','lab/process/k2522-redshift-drift-interface.json','explorations/conditional-build/k2526-geodesic-emitter-drift-repair-2026-11-02.md','lab/process/k2526-geodesic-emitter-drift-repair.json']
report={'result':'K2528','scope':'dated forecast does not supply joint sufficient-certificate inputs; conditional shifted-anchor repair, not empirical exclusion','checks':checks,'contrary_controls':controls,'forecast':rows,'illustrative_c_T_Href_cm_per_s':str(s.N(velocity_scale,16)),'inherited_sufficient_R':str(rstar),'illustrative_uniform_velocity_budget_cm_per_s':str(s.N(velocity_scale*rstar/2,16)),'sources':['https://arxiv.org/pdf/2305.01446#section2','https://pmc.ncbi.nlm.nih.gov/articles/PMC11413136/#Sec5'],'evidence_kinds':{'exact':'domain margin, weak-column transformation, anchor-preserving counterprofile and sufficient tolerance composition','universal':'positive-history integral inequality and compact-bump argument in note','numerical':'dated forecast sigmas and illustrative dimensional conversion only','inherited':'K2522/K2526 exact weak certificate; unchanged dependency reuse','reporting':'saved report equality and dependency hashes'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in refs}}
path=R/'lab/process/k2528-observation-forecast-feasibility.json'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(path.read_text())==report,'saved report differs'
print(json.dumps({'checks':len(checks),'contrary_controls':len(controls),'all_pass':True}))
