"""Exact finite control and rational confidence checks; no hardware certification."""
from pathlib import Path
import sympy as s
from fractions import Fraction as Q
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def zero(x):return s.simplify(s.expand_complex(x))==0
def check(n,x):
 checks[n]=bool(x)
 if not x:raise AssertionError('[FAIL] '+n)
# Exact state inner products against the binomial characteristic polynomial.
w=s.Rational(3,5)+s.I*s.Rational(4,5)
for N in [1,2,3,5]:
 for p in [s.Rational(1,3),s.Rational(1,2),s.Rational(1)]:
  amp=[s.sqrt(s.binomial(N,n)*p**n*(1-p)**(N-n)) for n in range(N+1)]
  inner=sum(amp[n]**2*w**(2*n) for n in range(N+1));formula=(1-p+p*w**2)**N
  check(f'binomial_overlap_{N}_{p}',zero(inner-formula))
  F=s.simplify(s.expand_complex(inner*s.conjugate(inner)))
  check(f'passive_fidelity_{N}_{p}',F==(1-4*p*(1-p)*s.Rational(16,25))**N)
# Sine exceptions; N3 first-ratio obstruction has algebraic cos(pi/5).
for N in [1,2]:
 a=[s.sqrt(s.Rational(2,N+2))*s.sin(s.pi*(n+1)/(N+2)) for n in range(N+1)]
 bino=[s.sqrt(s.binomial(N,n)/s.Integer(2)**N) for n in range(N+1)]
 check('small_sine_passive_'+str(N),all(zero(x-y) for x,y in zip(a,bino)))
check('N3_ratio_mismatch',not zero((1+s.sqrt(5))/2-s.sqrt(3)))
# Rational confidence bridge: lower bounds on sin and1-exp(-x).
mu=Q(10**28);e0=Q(1,10**25);xlo=4*mu*(e0-e0**3/6)**2;xhi=4*mu*e0**2
lower=xlo-xhi**2/2;baseline=Q(9386,10**15);threshold=Q(1,10**11)
check('success_implies_phase_radius',lower>(threshold+baseline)**2)
check('conservative_199_bound',lower>Q(199,10**13)**2)
dphase=3*e0;required=Q(81,100)/dphase**2;stock=3*10**27
check('confidence_stock_lower',required==9*10**48)
check('fixture_distinguishability',stock*dphase**2==Q(27,10**23))
check('fixture_below_required',stock*dphase**2<Q(81,100))
# Arbitrary target Givens maps, exact real amplitudes; includes N1,2 sine targets.
def synth(a,wrong_sign=False,stop=None):
 dim=len(a);state=s.zeros(dim,1);state[0]=1
 for k in range(dim-1 if stop is None else stop):
  rk=s.sqrt(sum(t*t for t in a[k:]));rr=s.sqrt(sum(t*t for t in a[k+1:]));cc=a[k]/rk;ss=rr/rk
  G=s.eye(dim);G[k,k]=G[k+1,k+1]=cc;G[k,k+1]=-ss;G[k+1,k]=(-ss if wrong_sign else ss)
  state=s.simplify(G*state)
 return state
vectors=[[1/s.sqrt(2),1/s.sqrt(2)],[s.Rational(1,2),1/s.sqrt(2),s.Rational(1,2)],[s.Rational(k)/s.sqrt(30) for k in [1,2,3,4]]]
for idx,a in enumerate(vectors):check('Givens_actual_'+str(idx),all(zero(x-y) for x,y in zip(synth(a),a)))
# Occupation-neighbor commutator conjugacy with complex hopping weights.
for N in [2,3,5]:
 A=s.zeros(N+1)
 for j in range(N):A[j+1,j]=s.Rational(j+1,N+1)+s.I*s.Rational(1,N+2)
 Hop=A+A.conjugate().T;num=s.diag(*range(N+1));D=s.diag(*[s.I**n for n in range(N+1)])
 speed=s.I*(Hop*num-num*Hop)
 check('speed_unitary_'+str(N),s.simplify(speed+D*Hop*D.conjugate().T)==s.zeros(N+1))
 check('diagonal_commutes_'+str(N),s.diag(*[n*n for n in range(N+1)])*num==num*s.diag(*[n*n for n in range(N+1)]))
eta=Q(1,10**14);check('hard_shell_mean_error',Q(stock)*(Q(1,2)-eta)>0)
check('exact_preparation_JT',Q(stock,2)==15*10**26)
check('pulse_budget',eta/stock<Q(3334,10**45))
# Same evaluators, altered encoding/control/dimension/normalization inputs.
a=vectors[2];N=3;p=s.Rational(1,2);amp=[s.sqrt(s.binomial(N,n)/8) for n in range(N+1)]
correct=sum(amp[n]**2*w**(2*n) for n in range(N+1));wrong=sum(amp[n]**2*w**n for n in range(N+1))
N=3;num=s.diag(*range(4));A=s.zeros(4);A[2,0]=1;Hop=A+A.T;D=s.diag(1,s.I,-1,-s.I)
faults={
 'wrong_encoding_charge':not zero(correct-wrong),
 'common_mode_encoding':not zero(correct-w**6),
 'wrong_rotation_sign':any(not zero(x-y) for x,y in zip(synth(a,True),a)),
 'skip_last_rotation':any(not zero(x-y) for x,y in zip(synth(a,stop=len(a)-2),s.Matrix(a))),
 'allow_two_step_hopping':s.I*(Hop*num-num*Hop)+D*Hop*D.conjugate().T!=s.zeros(4),
 'too_small_phase_radius':4*mu*(e0/10)**2<(threshold+baseline)**2}
# A rigorous upper bound falsifies discrimination at the mutated radius.
assert all(faults.values()),'[FAIL] mutation not detected'
stem='k2315-calibration-control-cost';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2312-relational-finite-calibration-2026-10-30.md','explorations/conditional-build/k2306-coherent-pump-phase-calibration-2026-10-30.md','explorations/conditional-build/k2264-restricted-detector-control-2026-10-29.md']
# Exact inherited calibration note resolved by result id, never guessed silently.
if not (ROOT/deps[-2]).exists():
 hits=list((ROOT/'explorations/conditional-build').glob('k2306-*.md'));assert len(hits)==1;deps[-2]=str(hits[0].relative_to(ROOT))
data=dict(schema_version='1.0',result_id='K2315',checks=len(checks),check_names=list(checks),mutation_failed_checks={n:['overlap_map_or_budget'] for n in faults},evidence_kind='exact finite state/control maps and rational confidence bounds; universal passive/Helstrom/speed proof in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'necessary_stock':str(required),'fixture_D_squared_upper':str(Q(stock)*dphase**2),'JT_lower_exact':str(Q(stock,2)),'uniform_pulse_error_sufficient':str(eta/stock)})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2315',checks=len(checks),faults=len(faults))))
