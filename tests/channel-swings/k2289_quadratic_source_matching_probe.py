from pathlib import Path
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=160
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(name,value): checks[name]=bool(value)
def verify_prior(path):
 data=json.loads((ROOT/path).read_text())
 for p,h in data['dependencies'].items():check('hash_'+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 return data
def finish(stem,deps,faults,extra):
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 assert all(faults.values()),faults
 paths=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),*deps]
 data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied models; no GU empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='symbolic identities and rational or outward interval bounds; hashes provenance only; universal arguments in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
 out=ROOT/'lab/process'/f'{stem}.json'
 if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(out.read_text())==data,'stored report stale'
 print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

stem='k2289-quadratic-source-matching'
dep='lab/process/k2286-quadratic-tensor-propagation.json';prior=verify_prior(dep)
trajectory=verify_prior('lab/process/k2283-global-quadratic-cosmology.json')
y,x=s.symbols('y x',positive=True)
# Dimensionless sphere: field divided by kappa*rho/(3m^2); y=mr, x=mL.
inside=1-(1+x)*s.exp(-x)*s.sinh(y)/y
outside=(x*s.cosh(x)-s.sinh(x))*s.exp(-y)/y
lap=lambda f:s.diff(f,y,2)+2*s.diff(f,y)/y-f
check('interior_equation',s.simplify(lap(inside)+1)==0)
check('exterior_equation',s.simplify(lap(outside))==0)
check('matching_value',s.simplify(s.expand_trig((inside-outside).subs(y,x)).rewrite(s.exp))==0)
check('matching_derivative',s.simplify((s.diff(inside-outside,y).subs(y,x)).rewrite(s.exp))==0)
check('regular_center',s.simplify(s.limit(inside,y,0)-(1-(1+x)*s.exp(-x)))==0)
A=3*(x*s.cosh(x)-s.sinh(x))/x**3
check('small_mass_charge',s.limit(A,x,0)==1)
check('massless_center',s.limit((1-(1+x)*s.exp(-x))/x**2,x,0)==R(1,2))
check('range_countercontrol',s.limit(A*s.exp(-2*x),x,s.oo)==0)
check('surface_range_countercontrol',s.limit(x*x*A*s.exp(-x),x,s.oo)==R(3,2))
# Finite series controls; the all-radius positive-kernel proof is in the companion.
j=s.symbols('j',integer=True,nonnegative=True)
for n in range(1,8):check('positive_charge_series_'+str(n),s.expand(s.series(A,x,0,16).removeO()).coeff(x,2*n)>0)
alpha,rho,kap,dens,RR=s.symbols('alpha rho kap dens RR',positive=True)
f=alpha*RR+RR**2/2-rho
trace=s.expand(s.diff(f,RR)*RR-2*f)
check('trace_sign',trace==-alpha*RR+2*rho)
check('positive_density_equilibrium',s.simplify((trace+kap*dens).subs(RR,(2*rho+kap*dens)/alpha))==0)
q=arb(prior['interval_results']['Xi_endpoint']);eps=arb(1)/1000
lo=q/(1+eps).sqrt();hi=q*(1+eps).sqrt()
check('endpoint_interval',lo>arb('.6347') and hi<arb('.6355'))
check('equalization_requires_strong_source',1/q**2-1>arb('1.479'))
ratio=(arb('33.8')/3).sqrt()/arb(2)**(arb(2)/3)
check('same_history_range',ratio>arb('2.114') and ratio<arb('2.115'))
# Direct first-order metric density variation of Box on homogeneous Rbar.
t,ee=s.symbols('t ee');ac=s.Function('ac')(t);psi=s.Function('psi')(t);phi=s.Function('phi')(t);rb=s.Function('rb')(t)
volume=ac**3*(1+ee*(psi-3*phi));current=-ac**3*(1-ee*(psi+3*phi))*s.diff(rb,t)
variation=s.diff(s.diff(current,t)/volume,ee).subs(ee,0)
expected=2*psi*(s.diff(rb,t,2)+3*s.diff(ac,t)/ac*s.diff(rb,t))+(s.diff(psi,t)+3*s.diff(phi,t))*s.diff(rb,t)
check('rolling_metric_wave_variation',s.simplify(variation-expected)==0)
check('arbitrary_shape_kernel_factor',R(1,12)/R(1,8)==R(2,3))
check('concentrated_source_countercontrol',1/R(1,100)==100)
# Same mathematical predicates act on changed equation/input expressions.
def oracle(source_sign=-1,charge=A,match=inside,ep=R(1,1000),metric_term=expected):
 return {'rolling_metric':s.simplify(metric_term-variation)==0,'source_equation':s.simplify(lap(match)-source_sign)==0,
 'boundary':s.simplify((match-outside).subs(y,x).rewrite(s.exp))==0,
 'unit_mass_limit':s.limit(charge,x,0)==1,
 'weak_endpoint_bound':bool(R(63509,100000)**2*(1+ep)<R(64,100)**2)}
assert all(oracle().values())
mut={'omit_rolling_metric_response':dict(metric_term=0),'wrong_source_sign':dict(source_sign=1),'drop_interior_one_plus_x':dict(match=1-s.exp(-x)*s.sinh(y)/y),'wrong_charge_normalization':dict(charge=A/3),'strong_environment_outside_class':dict(ep=2)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
finish(stem,[dep],faults,dict(interval_results=dict(endpoint_lower=str(lo),endpoint_upper=str(hi),required_observer_compactness=str(1/q**2-1),mass_over_H0=str(ratio)),scope='exact frozen elliptic model and endpoint substitution only'))
