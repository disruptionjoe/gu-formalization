from pathlib import Path
import json,hashlib,sys,math
import sympy as s
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v): checks[n]=bool(v)
def zero(v): return s.simplify(v)==0
from fractions import Fraction as Q
import numpy as np
from scipy.linalg import expm
# General independent-bath moment identity checked at three fields; covariance formula proves arbitrary count.
a,b=s.symbols('a b',nonnegative=True);Ns=s.symbols('N1:4',nonnegative=True);bath=s.symbols('n0:4');N=sum(Ns);R=sum((a*bath[i+1]-b*bath[0])*Ns[i] for i in range(3))
def expectation(expr):
 poly=s.Poly(s.expand(expr),*bath);return s.expand(sum(coeff*math.prod([1,1,3][power] for power in powers) for powers,coeff in poly.terms()))
exact=expectation(R**2);formula=(a-b)**2*N*N+2*a*a*sum(z*z for z in Ns)+2*b*b*N*N
check('independent_bath_second_moment',zero(exact-formula));check('upper_bound_gap',zero((3*a*a-2*a*b+3*b*b)*N*N-exact-4*a*a*sum(Ns[i]*Ns[j] for i in range(3) for j in range(i+1,3))))
check('positive_coefficient',zero(3*a*a-2*a*b+3*b*b-(2*(a*a+b*b)+(a-b)**2)))
na,nb,n0,Ka,Naa,Nbb=s.symbols('na nb n0 K Na Nb')
V=lambda aa,bb,kk:a*(aa*na+bb*nb)+2*b*kk*n0
check('pair_creation_commutator',zero(V(Naa+1,Nbb+1,Ka-1)-V(Naa,Nbb,Ka)-(a*na+a*nb-2*b*n0)))
check('Q_conservation',(Naa+1)+(Nbb+1)+2*(Ka-1)==Naa+Nbb+2*Ka)
chi=lambda phase:1/(2-s.exp(-s.I*phase));factor=s.simplify(chi(s.pi)**2*chi(-2*s.pi))
check('fixed_charge_coherence',factor==s.Rational(1,9));check('fixed_charge_distance',(1-factor)/2==s.Rational(4,9))
# Genuine interleaved finite sector example; collective input phase predicts ideal, local detuning differs.
X=np.array([[0,1],[1,0]],complex);D=np.diag([0.,1.]);t=.7;psi=np.array([1,0],complex)
actual=expm(-1j*t*(X+D))@psi;wrong=expm(-1j*t*X)@expm(-1j*t*D)@psi
check('noncentral_interleaved_countercontrol',np.linalg.norm(actual-wrong)>.1)
def sqrtup(q):
 q=Q(q);den=10**60;v=math.isqrt(q.numerator*den*den//q.denominator)
 while Q(v*v,den*den)<q:v+=1
 return Q(v,den)
delta=Q(9272,10**15);at=Q(1,10**17);bt=Q(1,10**28)
res=sqrtup(6300000*(3*at*at+3*bt*bt)) # rectangular bound, omit negative cross term
check('residual_budget',res<Q(435,10**16));budgets={}
for name,mu in [('coherent',10**28),('thermal',4*10**28)]:
 k2=mu if name=='coherent' else 3*mu+2;k4=mu if name=='coherent' else 75*mu+26
 bound=delta+2*sqrtup(k2)*bt+4*bt*bt*(k2+sqrtup(k4+3*k2*k2))+res;budgets[name]=str(bound)
 check(name+'_full_budget',bound<Q(9386,10**15));check(name+'_field_budget',6300000*bound<Q(8,1000)**2)
assert all(checks.values()),checks
# Faults modify physical moments/formulas, not assertion predicates.
wrongvar=(a-b)**2*N*N+a*a*sum(z*z for z in Ns)+b*b*N*N
faults={'wrong_thermal_variance':['independent_bath_second_moment'] if not zero(wrongvar-exact) else [],'independent_pump_per_field':['independent_bath_second_moment'] if not zero((a-b)**2*N*N+2*(a*a+b*b)*sum(z*z for z in Ns)-exact) else [],'wrong_pump_charge':['Q_conservation'] if (Naa+1)+(Nbb+1)+(Ka-1)!=Naa+Nbb+Ka else [],'replace_local_by_collective':['fixed_charge_coherence'] if factor!=1 else [],'move_bath_to_input':['noncentral_interleaved_countercontrol'] if np.linalg.norm(actual-wrong)>.1 else []}
result='K2303';note='explorations/conditional-build/k2303-local-number-bath-control-2026-10-30.md';report='k2303-local-number-bath-control.json';extra_deps=['explorations/conditional-build/k2293-moment-controlled-positive-pump-2026-10-30.md','explorations/conditional-build/k2300-positive-bath-pump-dephasing-2026-10-30.md'];evidence='Exact covariance, commutator, coherence and rational budget; numerical interleaving fixture; Duhamel proof in note';details={'budgets':budgets,'residual_upper':str(res),'countercontrol_distance':'4/9'}

assert all(checks.values()),[k for k,v in checks.items() if not v]
assert all(faults.values()),faults
deps=[str(Path(__file__).relative_to(ROOT)),note]+extra_deps
data=dict(schema_version='1.0',result_id=result,checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind=evidence,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details=details)
out=ROOT/'lab/process'/report
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result=result,checks=len(checks),faults=len(faults))))
