from pathlib import Path
import json,hashlib,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v): checks[n]=bool(v)
def zero(v): return s.simplify(v)==0

from fractions import Fraction as Q
# Coherent state expansion gives overlap²=exp[-2M(1-cos(2dphi))].
a,M,F=s.symbols('a M F',real=True);check('coherent_charge_two',s.trigsimp(2*(1-s.cos(2*a))-4*s.sin(a)**2)==0)
# Pure state pair sqrtF|0>+sqrt(1-F)|1>: half trace norm from eigenvalues.
D=s.Matrix([[1-F,-s.sqrt(F*(1-F))],[-s.sqrt(F*(1-F)),-(1-F)]])
check('Helstrom_two_dimensional',all(zero(q) for q in D*D-(1-F)*s.eye(2)))
alpha=Q(1,20);check('Helstrom_threshold',4*alpha*(1-alpha)==Q(19,100))
mu=10**28;r0=Q(1,10**25);epsilon=Q(1,10**11);delta=Q(9386,10**15)
sine_lo=lambda x:x-x**3/6
qlo=4*mu*sine_lo(r0)**2
check('necessary_phase_radius',qlo-qlo*qlo/2>(epsilon+delta)**2)
check('two_hypothesis_exponent',4*10**49*(2*r0)**2==Q(8,5))
def exp_upper(x,n):
 total=sum((x**j/Q(__import__('math').factorial(j)) for j in range(n+1)),Q(0));term=x**(n+1)/Q(__import__('math').factorial(n+1));return total+term/(1-x/(n+2))
def exp_lower(x,n):return sum((x**j/Q(__import__('math').factorial(j)) for j in range(n+1)),Q(0))
check('exact_exp_overlap_bound',exp_upper(Q(8,5),16)<5 and Q(1,5)>Q(19,100))
r=Q(3,10**27);M95=10**53;Mavg=10**54
check('heterodyne95_exponent',M95*sine_lo(2*r)**2>Q(7,2))
check('heterodyne95_tail',exp_lower(Q(7,2),8)>20)
check('success_error',delta+2*10**14*r==Q(9986,10**15) and delta+2*10**14*r<epsilon)
check('averaged_exponent',Mavg*sine_lo(2*r)**2>35)
check('averaged_tail',exp_lower(Q(35),90)>10**15)
check('averaged_total',delta+2*10**14*r+Q(1,10**15)==Q(9987,10**15) and delta+2*10**14*r+Q(1,10**15)<epsilon)
# Exact fixed unequal-duration fixture for the resource second derivative.
theta=s.symbols('theta',real=True);m1,m2,t1,t2=s.symbols('m1 m2 t1 t2',positive=True)
loge=-4*(m1*s.sin(t1*theta)**2+m2*s.sin(t2*theta)**2)
check('duration_weighted_curvature',s.diff(loge,theta,2).subs(theta,0)==-8*(m1*t1*t1+m2*t2*t2))
check('known_phase_zero',s.sin(0)==0);check('phase_mod_pi',s.trigsimp(s.sin(a+s.pi)**2-s.sin(a)**2)==0)
check('confidence_not_average',delta+2*10**14*r+alpha>epsilon)
# Heterodyne disk tangent radius is R sin(2r), not R sin(r).
R=s.symbols('R',positive=True);t=s.symbols('t',real=True);dist=(t*s.cos(2*a)-R)**2+(t*s.sin(2*a))**2;closest=R*s.cos(2*a)
check('wedge_tangent_geometry',zero(s.diff(dist,t).subs(t,closest)) and s.diff(dist,t,2).simplify()==2 and zero(dist.subs(t,closest)-R**2*s.sin(2*a)**2))
assert all(checks.values()),[a for a,b in checks.items() if not b]
def evaluate(charge=2,helstrom_squared=True,duration_weights=True,angle=2,baseline=delta,failure=Q(1,10**15)):
 return {
 'coherent_charge_two':zero(2*(1-s.cos(charge*a))-4*s.sin(a)**2),
 'Helstrom_two_dimensional':all(zero(q) for q in D*D-(1-(F if helstrom_squared else F*F))*s.eye(2)),
 'duration_weighted_curvature':zero(s.diff(loge,theta,2).subs(theta,0)+8*(m1*t1*t1+m2*t2*t2 if duration_weights else m1+m2)),
 'heterodyne95_exponent':M95*sine_lo(angle*r)**2>Q(7,2),
 'success_error':baseline+2*10**14*r==Q(9986,10**15),
 'averaged_total':baseline+2*10**14*r+failure<epsilon,
 }
assert all(evaluate().values())
mutations={'omit_pump_charge_two':{'charge':1},'overlap_not_squared':{'helstrom_squared':False},'omit_duration_weight':{'duration_weights':False},'wrong_heterodyne_angle':{'angle':1},'omit_baseline_error':{'baseline':Q(0)},'use_95percent_budget_for_average':{'failure':Q(1,20)}}
faults={name:[key for key,ok in evaluate(**change).items() if not ok] for name,change in mutations.items()}
result='K2306';note='explorations/conditional-build/k2306-retained-pump-phase-calibration-2026-10-30.md';report='k2306-retained-pump-phase-calibration.json';extra_deps=['explorations/conditional-build/k2303-local-number-bath-control-2026-10-30.md','explorations/conditional-build/k2293-moment-controlled-positive-pump-2026-10-30.md'];evidence='Exact coherent overlap, two-state discrimination and rational sine/exponential budget bounds; operational theorem and heterodyne proof in note';details={'necessary_effective_photons':'>1e49','sufficient95_photons':'1e53','sufficient_average_photons':'1e54','success_error':'<9.986e-12','averaged_error':'<9.987e-12'}

assert all(checks.values()),[k for k,v in checks.items() if not v]
assert all(faults.values()),faults
deps=[str(Path(__file__).relative_to(ROOT)),note]+extra_deps
data=dict(schema_version='1.0',result_id=result,checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind=evidence,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details=details)
out=ROOT/'lab/process'/report
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result=result,checks=len(checks),faults=len(faults))))
