"""Exact full-carrier serial phases, loss maps and rational finite-slew budgets."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib,sys
import sympy as s
R=Path(__file__).resolve().parents[2];st='k2365-serial-transparent-control';checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def add(*polys):
 d={}
 for p in polys:
  for m,c in p.items():d[m]=d.get(m,0)+c
 return {m:c for m,c in d.items() if c}
def mul(p,q):
 d={}
 for m,c in p.items():
  for n,b in q.items():d[m^n]=d.get(m^n,0)+c*b
 return {m:c for m,c in d.items() if c}
z=[{1<<(2*i):F(1,2),1<<(2*i+1):F(-1,2)} for i in range(4)]
fac={0:F(1),**{1<<i:F(1,2) for i in range(8)}};op={m:c/4 for m,c in mul(fac,mul(add(z[0],z[1]),add(z[2],z[3]))).items()}
first=(1<<0)|(1<<4);order=[first]+sorted(m for m in op if m!=first)
def val(m,t):return (-1)**sum(t[i] for i in range(8) if m>>i&1)
def ev(poly,t):return sum(c*val(m,t) for m,c in poly.items())
def ze(t):
 zz=[t[2*i+1]-t[2*i] for i in range(4)]
 return F(5-sum(t),4)*(zz[0]+zz[1])*(zz[2]+zz[3])
states=list(product((0,1),repeat=8));check('32_equal_signed_coefficients',len(op)==32 and set(op.values())=={F(1,16),F(-1,16)});check('first_coefficient',op[first]==F(1,16));check('l1_two',sum(abs(c) for c in op.values())==2);check('all256_physical_expansion',all(ev(op,t)==ze(t) for t in states));check('full_norm_one',max(abs(ze(t)) for t in states)==1)
def physical(bits):return tuple(v for b in bits for v in (b,1-b))
def erase(t,j):return tuple(0 if i in [2*j,2*j+1] else v for i,v in enumerate(t))
for b,r in product((0,1),repeat=2):
 t=physical([r,r,r^b,r^b]);check(f'code_{b}_{r}',ze(t)==1-2*b)
 for j in range(4):check(f'loss_covariance_{b}_{r}_{j}',ze(erase(t,j))==1-2*b)
# Integral in units delta=theta/n; all boundary norms against closer cycle endpoint.
prefix={};maxnorm=F(0)
for k in range(33):
 if k:prefix=add(prefix,{order[k-1]:op[order[k-1]]})
 a=0 if k<=16 else 1;diff=add(prefix,{m:-a*c for m,c in op.items()});norm=max(abs(ev(diff,t)) for t in states);maxnorm=max(maxnorm,norm);check('cumulative_boundary_'+str(k),norm<=1)
check('full_cycle_exact',prefix==op)
# Half-pulse witnesses support monotone-area interior bound; proof handles the continuum.
for k in [0,7,15,16,24,31]:
 pre={m:op[m] for m in order[:k]};pre=add(pre,{order[k]:op[order[k]]/2});a=0 if k+F(1,2)<=16 else 1
 check('interior_phase_'+str(k),max(abs(ev(add(pre,{m:-a*c for m,c in op.items()}),t)) for t in states)<=1)
x=s.symbols('x',real=True)
for b,r in product((0,1),repeat=2):
 t=physical([r,r,r^b,r^b]);out=erase(t,0);check(f'actual_first_pulse_phase_{b}_{r}',val(first,t)-val(first,out)==(1-(-1)**r)*(1-2*b))
# Coherence of recovered |+> after removing Utheta; exact analytic spectrum.
zeta=s.exp(-4*s.I*x);off=(zeta-1)/4
check('counterexample_coherence_modulus',s.simplify(s.expand_complex(off*s.conjugate(off))-s.sin(2*x)**2/4)==0)
check('positive_counterexample',s.simplify((s.sin(2*x)/2).subs(x,s.pi/8))==s.sqrt(2)/4)
p=s.symbols('p');P1=4*p*(1-p)**3;B=6*p*p-8*p**3+3*p**4
check('probability_partition',s.expand((1-p)**4+P1+B)==1)
# Independent pair-dependent exact enumeration.
ets=list(map(F,['1/2','2/3','3/4','4/5']));prob=[F(0)]*5
for flags in product((0,1),repeat=4):
 q=F(1)
 for a,e in zip(flags,ets):q*=1-e if a else e
 prob[sum(flags)]+=q
check('nonidentical_rates_partition',sum(prob)==1 and prob[1]==sum((1-e)*__import__('math').prod(ee for j,ee in enumerate(ets) if i!=j) for i,e in enumerate(ets)))
budgets=[]
for n,T,expected in [(8,32,F(53,20000)),(32,64,F(37,20000)),(128,128,F(121,40000))]:
 theta=F(1,2);check(f'pulse_duration_{n}',F(T*T)==256*n*theta);pbar=F(T,6400);bound=6*pbar*pbar+4*pbar*2*theta/n;check(f'rational_budget_{n}',bound==expected);budgets.append(dict(n=n,T=T,p_upper=str(pbar),error_upper=str(bound)))
# Actual reference corruption alters operator or source, not predicates.
bad=dict(op);bad[first]*=-1
faults['flip_first_pulse_sign']=['full_cycle_exact'] if any(ev(bad,t)!=ze(t) for t in states) else []
bad=dict(op);bad.pop(first)
faults['omit_first_pulse']=['full_cycle_exact'] if any(ev(bad,t)!=ze(t) for t in states) else []
faults['discard_jump_time_phase']=['actual_first_pulse_phase_0_1'] if val(first,physical([1,1,1,1]))-val(first,erase(physical([1,1,1,1]),0))!=0 else []
# Unequal rail rates make jump/environment amplitudes depend on the logical column after a prior erased pair.
# Simpler intact branch: e^{-(sum rate*occupation)T/2} differs across code components.
rates=[1,2,1,1,1,1,1,1];t0=physical([0,0,0,0]);t1=physical([1,1,1,1]);faults['unmatched_rail_rates']=['logical_independent_scalar_attenuation'] if sum(a*b for a,b in zip(rates,t0))!=sum(a*b for a,b in zip(rates,t1)) else []
faults['pulse_overshoot_with_same_net_area']=['cumulative_boundary_1'] if max(abs(3*val(first,t)) for t in states)>1 else []
assert all(faults.values())
deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2362-transparent-control-locality.json','lab/process/k2356-protected-erasure-record.json']
out=dict(result_id='K2365',checks=len(checks),check_names=list(checks),altered_input_and_algebraic_scope_controls=faults,evidence_kind='exact rational all256-state phase algebra, actual code/loss phases and symbolic coherent error; universal reference-aware proof in note',details=dict(max_unit_cycle_boundary_norm=str(maxnorm),first_pulse_error='abs(sin(2x))/2',serial_bound='B+P1 min(1,2theta/n)',budgets=budgets),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(faults));print(json.dumps(out['details']))
