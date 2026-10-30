"""Exact spacetime-window algebra; infinite-domain arguments are in companion note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError('[FAIL] '+n)
D1,D2=s.symbols('D1 D2',positive=True);c1=D2/(D2-D1);c2=-D1/(D2-D1)
check('unit_DC',s.simplify(c1+c2)==1);check('growth_null',s.simplify(c1*D1+c2*D2)==0)
check('l1_cost',s.simplify(c1-c2-(D1+D2)/(D2-D1))==0)
e1,e2=s.symbols('e1 e2',real=True);leak=s.factor(c1*(D1+e1)+c2*(D2+e2));check('leakage',s.simplify(leak-(-D1*e2+D2*e1)/(D2-D1))==0)
check('nonzero_error_can_cancel',s.simplify(leak.subs({e1:D1,e2:D2}))==0)
check('constant_error_leaks',s.simplify(leak.subs({e1:1,e2:1}))==1)
# A concrete pair of temporal bins in a supplied growing response, no claim to solve background.
a=s.Matrix([2,-1]);T=s.Matrix([1,2]);P=s.Rational(3,7);cov=P*T*T.T
check('coherent_time_variance_zero',(a.T*cov*a)[0]==0)
check('false_independent_time_variance_positive',(a.T*s.diag(*cov.diagonal())*a)[0]>0)
# Finite real modal covariance fixture; conjugate normalization inherited from K2314.
weights=[s.Rational(2,3),s.Rational(-1,3)];transfers=[s.Matrix([1,3]),s.Matrix([2,1])];power=[s.Rational(3,2),s.Rational(4,3)]
B=s.Matrix.hstack(*transfers);temporal=s.Matrix(weights);full=B*s.diag(*power)*B.T
check('time_covariance_isometry',s.simplify((temporal.T*full*temporal)[0]-sum(power[j]*(temporal.dot(transfers[j]))**2 for j in range(2)))==0)
noise1,noise2=s.symbols('noise1 noise2',nonnegative=True)
check('disjoint_noise_amplification',s.simplify(c1*c1*noise1+c2*c2*noise2-(D2**2*noise1+D1**2*noise2)/(D2-D1)**2)==0)
for d1,d2 in [(1,2),(2,3),(99,100)]:
 check('ordered_normalization_'+str(d1),s.simplify((c1+c2).subs({D1:d1,D2:d2}))==1)
 check('positive_cost_'+str(d1),((c1-c2).subs({D1:d1,D2:d2}))>1)
# Slab window: direct integration and supported moving phase.
x,t=s.symbols('x t',real=True)
for n in range(1,9):
 w=s.integrate(s.exp(-s.I*n*x),(x,0,s.pi))/(2*s.pi)
 formula=(1-(-1)**n)/(2*s.pi*s.I*n)
 check('slab_coefficient_'+str(n),s.simplify(w-formula)==0)
 check('odd_mode_tail_'+str(n),s.simplify(n*n*w*s.conjugate(w))==(1/s.pi**2 if n%2 else 0))
 k=s.Matrix([n,0,0]);check('transverse_no_phase_'+str(n),k.dot(s.Matrix([0,1,0]))==0)
 check('longitudinal_phase_'+str(n),k.dot(s.Matrix([1,0,0]))==n)
# Finite smooth polynomial zero-endpoint weight: exact integration by parts identity.
g=t*t*(1-t)**2
for n in [1,2,3]:
 Bn=s.integrate(g*s.exp(s.I*n*t),(t,0,1));ibp=-s.integrate(s.diff(g,t)*s.exp(s.I*n*t),(t,0,1))/(s.I*n)
 check('integration_by_parts_'+str(n),s.simplify(Bn-ibp)==0)
# Faults alter input/filter/covariance/phase rather than the acceptance predicates.
faults={
 'wrong_filter_sign':s.simplify(c1*D1-c2*D2)!=0,
 'wrong_filter_ratio':s.simplify(c1*D1-(D2/(D2-D1))*D2)!=0,
 'independent_temporal_signal':(a.T*s.diag(*cov.diagonal())*a)[0]!=(a.T*cov*a)[0],
 'replace_dot_by_norm':s.Matrix([3,0,0]).dot(s.Matrix([0,1,0]))!=3,
 'omit_noise_cross_bin_scale':s.simplify(c1*c1*noise1+c2*c2*noise2-noise1-noise2)!=0,
 'constant_response_calibration_shift':s.simplify(c1*(D1+1)+c2*(D2+1))!=0}
assert all(faults.values()),'[FAIL] fault not detected'
stem='k2317-spacetime-dust-windows';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2314-windowed-dust-observables-2026-10-30.md','explorations/conditional-build/k2311-uniform-constrained-dust-evolution-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2317',checks=len(checks),check_names=list(checks),mutation_failed_checks={n:['filter_covariance_or_direction_equation'] for n in faults},evidence_kind='exact symbolic filter/covariance/Fourier controls; uniform transfer inherited and infinite Gaussian/summability proofs in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'compensation':[str(c1),str(c2)],'leakage':str(leak),'l1_norm':str(s.factor(c1-c2))})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2317',checks=len(checks),faults=len(faults))))
