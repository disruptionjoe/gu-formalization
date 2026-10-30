from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as R
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
 data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied models; no GU empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='exact symbolic and rational identities/bounds; finite matrix or oscillator controls numerical only; hashes provenance only; universal proofs in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
 out=ROOT/'lab/process'/f'{stem}.json'
 if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(out.read_text())==data,'stored report stale'
 print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

import cmath,math
import numpy as np
from scipy.linalg import expm
stem='k2294-regular-scalar-transfer'
deps=['lab/process/k2291-rolling-scalar-applicability.json','lab/process/k2288-finite-frequency-tensor-bound.json','lab/process/k2283-global-quadratic-cosmology.json']
for dep in deps:verify_prior(dep)
j,h,beta,a,D,F=s.symbols('j h beta a D F',real=True,nonzero=True)
x=s.sqrt(6)*j;y=(a-D/F)/(s.sqrt(6)*h*h*beta*beta);w=(-a+2*D/F)/(3*h*h*beta*beta)
mass=w+2*x*y+3*x*x-x**4/2
qraw=h*h*beta*beta*(2-3*j*j-mass)
qfinal=h*h*beta*beta*(2-21*j*j+18*j**4)-2*j*(a-D/F)+(a-2*D/F)/3
check('canonical_scalar_potential',s.simplify(qraw-qfinal)==0)
b=s.symbols('b',real=True);check('vacuum_regular_constraint',s.expand((1+b/2)**2-(b/2)**2-(1+b))==0)
t=s.symbols('t',real=True);P=2-21*t+18*t*t
check('polynomial_minimum',s.diff(P,t).subs(t,s.Rational(7,12))==0 and P.subs(t,s.Rational(7,12))==-s.Rational(33,8))
check('polynomial_endpoints',P.subs(t,0)==2 and P.subs(t,1)==-1)
check('polynomial_convex',s.diff(P,t,2)==36)
major=R(33,8)*172**2+2*(34+2290)+R(34+4580,3)
check('whole_path_constant',major==128220 and major<129000)
check('conformal_integral',R(233,333)<1 and 129000*36==4644000)
xi=R(4644000,10**9);eps=xi/(1-xi)
check('rational_Gronwall_budget',xi==R(1161,250000) and eps==R(1161,248839) and eps<R(4666,10**6))
# Exact constant coefficient solution, including nonzero q, checks actual oscillator transfer.
def solution(q,k,t):
 omega=cmath.sqrt(k*k-q)
 return cmath.cos(omega*t)-1j*k*cmath.sin(omega*t)/omega
for q0 in [-3.,2.,8.]:
 k=4.;T=.2;v=solution(q0,k,T);bound=math.expm1(abs(q0)*T/k)
 check('constant_potential_control_'+str(q0),abs(v-cmath.exp(-1j*k*T))<bound)
check('low_frequency_tachyonic_countercontrol',abs(solution(8.,1.,2.))>10)
# Canonical differentiation: Q=v/a, Q''+2(a'/a)Q'+(k2+a2m)Q=0.
v0,v1,v2,A,Ap,App,k2,m=s.symbols('v0 v1 v2 A Ap App k2 m',nonzero=True)
q1=v1/A-v0*Ap/A**2;q2=v2/A-2*v1*Ap/A**2-v0*App/A**2+2*v0*Ap**2/A**3
check('canonical_rescaling',s.expand(A*(q2+2*Ap/A*q1+(k2+A*A*m)*v0/A)-(v2+(k2+A*A*m-App/A)*v0))==0)
# Full initial-data transfer, independent matrix exponential versus scalar formula.
for q0 in [-3.,2.,8.]:
 k=4.;dt=.2;J=np.array([[0.,1.],[-1.,0.]])
 G=k*J+np.array([[0.,0.],[q0/k,0.]])
 T=expm(dt*G);free=expm(dt*k*J);budget_x=abs(q0)*dt/k
 check('phase_space_transfer_'+str(q0),np.linalg.norm(T-free,2)<=math.expm1(budget_x)+1e-14)
 sv=np.linalg.svd(T,compute_uv=False)
 check('phase_space_two_sided_'+str(q0),sv[-1]>=math.exp(-budget_x)-1e-14 and sv[0]<=math.exp(budget_x)+1e-14)
 check('unit_determinant_'+str(q0),abs(np.linalg.det(T)-1)<1e-13)
 check('matrix_vs_oscillator_'+str(q0),abs((T@np.array([1.,-1j]))[0]-solution(q0,k,dt))<1e-13)
z,Hphysical=s.symbols('z Hphysical',positive=True)
actual_measure=(1/(1+z))**2*Hphysical**2/Hphysical
def oracle(cross=2,canonical_sign=-1,polynomial=-21,jacobian_power=2):
 cmass=w+cross*x*y+3*x*x-x**4/2
 candidate=h*h*beta*beta*(2-3*j*j+canonical_sign*cmass)
 target=h*h*beta*beta*(2+polynomial*j*j+18*j**4)-2*j*(a-D/F)+(a-2*D/F)/3
 return {'constrained_potential':s.simplify(candidate-qfinal)==0,'polynomial_identity':s.simplify(target-qraw)==0,'redshift_measure':s.simplify(Hphysical/(1+z)**jacobian_power-actual_measure)==0}
assert all(oracle().values())
mut={'omit_constraint_cross':dict(cross=0),'wrong_canonical_mass_sign':dict(canonical_sign=1),'wrong_scalar_coefficient':dict(polynomial=-20),'wrong_redshift_measure':dict(jacobian_power=1)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
finish(stem,deps,faults,dict(bounds=dict(potential_majorant=129000,integral_over_Hstar=4644000,frequency_over_Hstar=10**9,error=str(eps)),scope='prepared mode and all-initial-data canonical phase-space transfer on vacuum history; no low-frequency, sourced, matter or observed-wave conclusion'))
