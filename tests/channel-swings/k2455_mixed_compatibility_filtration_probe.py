"""Original mixed compatibility fixture and exact finite-bank dimension controls."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from math import comb
import json,hashlib,sys,ast
ROOT=Path(__file__).resolve().parents[2]
p37=ROOT/'tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py';src=p37.read_text()
exec(compile(src[src.index('source25path='):src.index('for deg in range(8):')],str(p37),'exec'),globals())
inherited=dict(checks);checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
ck('original_bank_reconstructed',all(inherited.values()))
hh={(5,5,1):F(1),(5,1,5):F(-1),(6,6,1):F(-1),(6,1,6):F(1)}
ck('full_original_polarity',all(not pol(hh,k) for k in K))
ck('last_slots_antisymmetric',all(hh.get((i,j,k),0)==-hh.get((i,k,j),0) for i,j,k in product(range(14),repeat=3)))
ck('original_cyclic_hook',all(hh.get((i,j,k),0)+hh.get((j,k,i),0)+hh.get((k,i,j),0)==0 for i,j,k in product(range(14),repeat=3)))
ck('tracefree_hook',all(sum(eta[i]*hh.get((i,i,k),0) for i in range(14))==0 for k in range(14)))
ck('actual_covectors',covs[2]=={5:F(1)} and covs[3]=={6:F(1)} and covs[7]=={1:F(-1)})
expected=[{(1,5):F(1)},{(1,6):F(-1)},{(5,5):F(-2),(6,6):F(2)}]
for r,want in zip((2,3,7),expected):ck('original_symbol_'+str(r),symbol(hh,covs[r])==want)
ck('equal_repeated_coefficients',-F(15,168)+F(27,14)/70+F(3,7)/420==-F(17,280))
P={(2,2,2,7):field(1)};out={}
for r in range(14):
 for ij,v in symbol(hh,covs[r]).items():out[ij]=pa((1,out.get(ij,{})),(ff(v),der(P,r)))
out={k:v for k,v in out.items() if v}
want={(5,5):{(2,2,2):field(-2)},(6,6):{(2,2,2):field(2)},(1,5):{(2,2,7):field(3)}}
ck('original_degree4_Euler_image',out==want)
def div2(bank,transverse=False,offdiag=2,wrong_sign=False):
 ans={}
 for (i,j),p in bank.items():
  for r in range(7 if transverse else 14):
   for t in range(7 if transverse else 14):
    cr=covs[r].get(i,0);ct=covs[t].get(j,0)
    if wrong_sign and r==7:cr=-cr
    if wrong_sign and t==7:ct=-ct
    z=(1 if i==j else offdiag)*eta[i]*eta[j]*cr*ct
    if z:ans=pa((1,ans),(ff(z),der(der(p,r),t)))
 return ans
ck('original_full_trace',not pa(*[(eta[i],p) for (i,j),p in out.items() if i==j]))
ck('original_full_double_divergence',not div2(out))
f0={ij:{m:v for m,v in p.items() if all(r<7 for r in m)} for ij,p in out.items()};f0={ij:p for ij,p in f0.items() if p}
f1={ij:{m:v for m,v in p.items() if any(r>=7 for r in m)} for ij,p in out.items()};f1={ij:p for ij,p in f1.items() if p}
ck('highest_degree_compatible',not div2(f1,True))
ck('lower_coefficient_exact_residual',div2(f0,True)=={(2,):field(-12)})
ctrl('coefficientwise_compatibility_false',bool(div2(f0,True)))
ctrl('raw_symmetric_factor_required',bool(div2(out,offdiag=1)))
ctrl('actual_passive_sign_required',bool(div2(out,wrong_sign=True)))
ck('boundary_ideal_preserved',all(any(r<7 for r in m) for m in P))
# Symbol-zero plus antisymmetry yields full alternation, whose cyclic sum is3h.
# Test the crucial missing cyclic hypothesis with a genuine alternating tensor.
from itertools import permutations
alt={}
for p in permutations((0,1,2)):
 inv=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3));alt[p]=F((-1)**inv)
ck('alternating_symbol_zero',all(not symbol(alt,{r:F(1)}) for r in range(14)))
ctrl('cyclic_condition_essential',alt[0,1,2]+alt[1,2,0]+alt[2,0,1]==3)
# Exact dimension identity at threshold and well beyond, not an all-degree proof.
for M in (1,2,7,117):
 for n in (13*M-1,13*M,26*M):
  dom=M*comb(n+13,12);tar=comb(n+13,13)
  ck(f'dimension_ratio_{M}_{n}',F(tar,dom)==F(n+1,13*M))
  ck(f'dimension_threshold_{M}_{n}',(tar>dom)==(n+1>13*M))
ctrl('finite_probe_cannot_exclude_small_degrees',comb(4+13,13)<comb(4+13,12))
# Explicit cancellation counters the forbidden inference from sum to each term.
ctrl('sum_null_does_not_imply_each_null',bool(symbol(hh,covs[7])) and not symbol({k:-v for k,v in hh.items()},covs[7])==symbol(hh,covs[7]))
ck('opposite_responses_cancel',all(v+symbol({k:-v for k,v in hh.items()},covs[7]).get(ij,0)==0 for ij,v in symbol(hh,covs[7]).items()))
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2455-mixed-compatibility-filtration-2026-11-01.md','tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py','explorations/conditional-build/k2452-partial-analytic-hook-inverse-2026-11-01.md','explorations/conditional-build/k2449-full-mixed-boundary-adjoint-2026-11-01.md']
report={'result_id':'K2455','checks':checks,'controls':controls,'fixture':{'field':'h*y2^3*z0','full_double_divergence':'0','transverse_lower_coefficient':'-12*y2','scalar_bank_threshold':'n+1>13M'},'evidence_kinds':{'universal':'written proper symbol kernel, homogeneous dimension exclusion and leading-residual induction','exact':'original hook/polar/symbol/compatibility fixture; dimension identities and contrary controls','ceiling':'not full joint inverse obstruction or nonlinear convergence'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2455-mixed-compatibility-filtration.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2455',len(checks),'checks',len(controls),'controls PASS')
