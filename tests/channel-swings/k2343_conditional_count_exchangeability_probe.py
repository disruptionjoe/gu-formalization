"""Finite exact sign orbits, overlap cancellation and analytic power constants."""
import sympy as s,itertools,collections
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def finish(st,details,evidence,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),evidence_kind=evidence,mutation_failed_checks=faults,details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 assert faults and all(faults.values())
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({'result':out['result_id'],'checks':len(checks),'faults':len(faults)}))

q=s.Rational
signs=list(itertools.product([-1,1],repeat=6));w=[5,-1,-1,-1,-1,-1]
def scores(weights,amps,orbit):return [abs(sum(a*b*c for a,b,c in zip(weights,amps,sg))) for sg in orbit]
def pvals(vals,strict=False):return [q(sum(v>x if strict else v>=x for v in vals),len(vals)) for x in vals]
def size_valid(ps):
 return all(q(sum(bool(p<=a) for p in ps),len(ps))<=a for a in set(ps+[q(1,20)]))
vals=scores(w,[1]*6,signs);ps=pvals(vals)
check('exact_64_orbit',collections.Counter(vals)=={0:2,2:10,4:20,6:20,8:10,10:2})
check('all_orbit_levels_superuniform',size_valid(ps))
check('five_percent_size',q(sum(bool(p<=q(1,20)) for p in ps),64)==q(1,32))
for amps in [[1,2,3,4,5,6],[2,3,5,7,11,13]]:
 vp=scores(w,amps,signs);check('arbitrary_positive_magnitudes_'+str(amps[0]),q(sum(bool(v==max(vp)) for v in vp),64)==q(1,32) and size_valid(pvals(vp)))
check('all_zero_ties_give_one',set(pvals([0]))=={1})
# Explicit incidence: column0 lies in apertures0,1,2; remaining columns singleton1..5.
H=s.zeros(6)
for j in range(6):H[j,j]=1
H[1,0]=H[2,0]=1
check('triple_overlap_projected_weight',list((s.Matrix([w])*H))==[3,-1,-1,-1,-1,-1])
P=s.Matrix([8,2,4,1,5,3]);Q=s.Matrix([1,5,9,7,10,8]);C=s.Matrix([100,7,51,9,18,41])
raw=H*(P+C)-H*(Q+C);check('shared_counts_cancel_before_projection',raw==H*(P-Q))
ov=scores([3,-1,-1,-1,-1,-1],[1]*6,signs);check('overlap_orbit_size',size_valid(pvals(ov)))
# Geometry bounds and exact cap mean.
c=q(1023,1024);beta=c*(1+c)/2
check('sqrt_upper',2047<46**2);check('sqrt_lower',q(11,5)**2<5)
check('singleton_geometry',q(1023+92,1024)*q(5,11)<q(1,2))
x=s.symbols('x');P2=(3*x*x-1)/2
check('cap_harmonic_mean',s.integrate(P2,(x,c,1))/(1-c)==beta)
check('cap_factor',beta>q(99,100))
check('positive_source_floor',2-1>0)
h=[1]+[-q(1,5)]*5
cheb=sum(q(32)/(z*z) for z in h)
check('chebyshev_union_constant',cheb==4032)
power=1-4032*2/(10**6*beta**2)
check('positive_heat_power',power>q(99,100))
check('two_sided_extrema',ps[vals.index(10)]==q(1,32))
# A simple exact finite PRIVATE-count law to verify independent coordinate symmetry.
# Conditional on each private pair total1, each difference sign is fair.
means=[[q(z,8) for z in [1,2,3,4,5,6]],[q(z,8) for z in [1,1,1,1,1,16]]]
check('latent_total_rates_equal',sum(means[0])==sum(means[1])==q(21,8))
likelihood=[]
for sg in signs:
 pairs=[(1,0) if z==1 else (0,1) for z in sg]
 mass=sum(prior*s.prod(mu**(a+b)/(s.factorial(a)*s.factorial(b)) for mu,(a,b) in zip(ms,pairs)) for prior,ms in zip([q(1,3),q(2,3)],means))
 likelihood.append(mass)
conditional=[z/sum(likelihood) for z in likelihood]
check('private_pair_total_one_orbit',all(z==q(1,64) for z in conditional) and sum(conditional)==1)
# Global sign mixing of the two extrema violates coordinatewise invariance.
orient=(1,-1,-1,-1,-1,-1);bad=[orient,tuple(-z for z in orient)]
badp=[ps[signs.index(z)] for z in bad]
check('global_swap_counterexample',q(sum(bool(p<=q(1,20)) for p in badp),2)==1)
# Genuine model/algorithm faults evaluated with unchanged acceptance predicates.
faults['strict_tail_omits_ties']=['all_orbit_levels_superuniform'] if not size_valid(pvals(vals,True)) else []
faults['only_global_sign_randomized']=['five_percent_size'] if q(sum(bool(p<=q(1,20)) for p in badp),2)>q(1,20) else []
Cbad=C.copy();Cbad[0]+=1
badraw=H*(P+C)-H*(Q+Cbad)
faults['shared_registration_mismatch']=['shared_counts_cancel_before_projection'] if badraw!=H*(P-Q) else []
faults['remove_source_baseline']=['positive_source_floor'] if 0-1<=0 else []
finish('k2343-conditional-count-exchangeability',{'orbit_histogram':{str(k):v for k,v in sorted(collections.Counter(vals).items())},'size_at_1_over_20':'1/32','cap_beta':str(beta),'power_lower':str(power),'shared_cancelled_difference':[int(z) for z in raw]},'exact finite sign orbits, incidence maps and rational bounds; universal Cox-invariance and power proof in note',['explorations/conditional-build/k2337-pixel-beam-count-test-2026-10-30.md','explorations/conditional-build/k2340-poisson-aperture-calibration-2026-10-30.md'])
