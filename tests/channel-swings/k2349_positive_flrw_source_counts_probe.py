"""Positive FLRW marked count and nuisance exact controls."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as F
from math import comb
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def fault(k,v):
 faults[k]=bool(v)
 if not v:raise AssertionError('ineffective altered-input control: '+k)
def publish(st,details,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),altered_input_controls=faults,evidence_kind='exact symbolic/rational controls; universal theorems proved in companion note, no empirical or proof-assistant certification',details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({k:out[k] for k in ['result_id','checks','details']}))

z=s.symbols('z',positive=True);Z=s.Integer(3);cut=s.Rational(5,4);x0=z;x1=2*(1-1/s.sqrt(1+z));a=s.symbols('a',positive=True)
check('dS_distance_derivative',s.diff(x0,z)==1)
check('EdS_distance_derivative',s.simplify(s.diff(x1,z)-(1+z)**(-s.Rational(3,2)))==0)
check('shell_primitive',s.diff(x1**3/3,z)==x1*x1*s.diff(x1,z))
p0=s.simplify((x0.subs(z,cut)/x0.subs(z,Z))**3);p1=s.simplify((x1.subs(z,cut)/x1.subs(z,Z))**3);threshold=(p0+p1)/2
check('exact_bin_probabilities',(p0,p1,threshold)==(s.Rational(125,1728),s.Rational(8,27),s.Rational(637,3456)))
check('concentration_exponent',s.simplify(2*128*((p1-p0)/2)**2)==s.Rational(1849,576))
check('exp3_exceeds20',sum(F(3)**j/F(__import__('math').factorial(j)) for j in range(9))>20)
# Exact integer binomial tails at the same fixed threshold.
def tails(n,pl,ph):
 k=int(s.floor(n*threshold));pl=F(str(pl));ph=F(str(ph))
 def mass(p,i):return comb(n,i)*p.numerator**i*(p.denominator-p.numerator)**(n-i)
 e0=F(sum(mass(pl,i) for i in range(k+1,n+1)),pl.denominator**n)
 e1=F(sum(mass(ph,i) for i in range(k+1)),ph.denominator**n)
 return k,e0,e1
k,e0,e1=tails(128,p0,p1);check('both_exact128_tails_below5percent',max(e0,e1)<F(1,20))
rk,re0,re1=tails(192,p0+s.Rational(1,64),p1-s.Rational(1,64));check('both_robust192_tails_below5percent',max(re0,re1)<F(1,20))
check('robust_exponent',2*192*s.Rational(37,384)**2==s.Rational(1369,384))
p,d=s.symbols('p d',positive=True);lo=p*(1-d)/(1+d*(1-2*p));hi=p*(1+d)/(1+d*(2*p-1))
check('weighted_bin_normalization',s.simplify(hi-p*(1+d)/(p*(1+d)+(1-p)*(1-d)))==0)
check('radial_distortion_budget',F(1,33)/(2*(1-F(1,33)))==F(1,64))
# Positive full-law mimic; kernel matches because its mean matches.
v0=x0*x0*s.diff(x0,z);v1=x1*x1*s.diff(x1,z);n1=s.simplify(v0/v1);L1=s.simplify(x1*x1/(x0*x0))
check('full_intensity_mimic',s.simplify(n1*v1-v0)==0)
check('flux_mimic',s.simplify(L1/((1+z)**2*x1**2)-1/((1+z)**2*x0**2))==0)
check('positive_mimic_sample',n1.subs(z,cut)>0 and L1.subs(z,cut)>0)
check('regular_origin_mimic',s.limit(n1,z,0)==1 and s.limit(L1,z,0)==1)
check('scale_count_gauge',s.simplify(a**(-3)*(a*x1)**2*s.diff(a*x1,z)-v1)==0)
check('scale_flux_gauge',s.simplify(a*a/((1+z)**2*(a*x1)**2)-1/((1+z)**2*x1**2))==0)
# Standard candle identity without fractional-power simplification assumptions.
ratio=x1/x1.subs(z,Z);flux=1/((1+z)**2*x1**2)
check('joint_flux_count_invariant',s.simplify(flux*(1+z)**2*ratio**2-1/x1.subs(z,Z)**2)==0)
# Joint Poisson factorization at nontrivial exact bin counts, exp factor cancels.
mu0,mu1=s.symbols('mu0 mu1',positive=True);N=7;k0=3
joint=mu0**k0*mu1**(N-k0)/(s.factorial(k0)*s.factorial(N-k0))
fact=(mu0+mu1)**N/s.factorial(N)*s.binomial(N,k0)*(mu0/(mu0+mu1))**k0*(mu1/(mu0+mu1))**(N-k0)
check('Poisson_multinomial_factorization',s.simplify(joint-fact)==0)
# Explicit finite-bin derivative-positive alternative: each |z-root|<=3 on[0,3].
poly=z*z*(z-cut)**2*(z-Z)**2;eps=s.Rational(1,10000);changed=z+eps*poly
check('edge_distances_same',all(s.simplify(changed.subs(z,t)-t)==0 for t in [0,cut,Z]))
check('distance_derivative_positive_bound',eps*6*3**5<1)
check('different_interior_H',s.diff(changed,z).subs(z,s.Rational(1,2))!=1)
fault('omit_density_evolution_in_mimic',s.simplify(v1-v0)!=0)
fault('omit_luminosity_evolution_in_mimic',s.simplify(1/x1**2-1/x0**2)!=0)
fault('wrong_luminosity_distance_power',s.simplify((1/((1+z)*x1**2))*(1+z)**2*ratio**2-1/x1.subs(z,Z)**2)!=0)
wrongp=s.integrate(z*z/(1+z),(z,0,cut))/s.integrate(z*z/(1+z),(z,0,Z))
fault('insert_transient_time_dilation_in_source_census',s.simplify(wrongp-p0)!=0)
# If every reported entry repeats one original draw, rejection probability is p0, not a binomial tail.
fault('duplicate_one_source128_times',p0>s.Rational(1,20) and e0<F(1,20))
details={'p0':str(p0),'p1':str(p1),'threshold':str(threshold),'N128_cut':k,'exact_tails128':[str(e0),str(e1)],'decimal_tails128':[float(e0),float(e1)],'N192_robust_cut':rk,'decimal_robust_tails192':[float(re0),float(re1)],'positive_mimic_n1':str(n1),'positive_mimic_L1':str(L1),'finite_bin_epsilon':str(eps)}
publish('k2349-positive-flrw-source-counts',details,['explorations/conditional-build/k2346-positive-count-response-discrimination-2026-10-30.md','lab/active-research/joe-directed/prediction-kickoff/late-time-finite-node-identifiability-2026-10-27.md'])
