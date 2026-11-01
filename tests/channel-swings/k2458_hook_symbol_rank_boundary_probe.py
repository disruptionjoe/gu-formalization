"""Exact original hook-symbol sharpness and quadratic restricted-bank bound."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import product,combinations,permutations
from math import comb
import json,hashlib,sys
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
ck('original_inputs_reconstructed',all(inherited.values()))
def hook(triple,signs=(1,1,1)):
 a,b,c=triple;t1,t2,t3=signs
 vals={(b,a):t1,(c,a):-t1,(a,b):t2,(c,b):-t2,(a,c):t3,(b,c):-t3};out={}
 for (i,j),v in vals.items():out[i,i,j]=F(v);out[i,j,i]=-F(v)
 return out
# A small exact search tests original polarity; it is not a generic-rank proof.
found=None;tested=0
for tri in combinations(range(14),3):
 if len({eta[i] for i in tri})!=1:continue
 for signs in product([1,-1],repeat=2):
  hh=hook(tri,(1,*signs));tested+=1
  if all(gram(k,hh)==0 for k in K):found=(tri,(1,*signs),hh);break
 if found:break
ck('original_polar_rank2_fixture_found',found is not None)
tri,signs,hh=found
ck('repeated_only',all(len(set(ix))<3 for ix in hh))
ck('last_two_antisymmetric',all(hh.get((i,j,k),0)==-hh.get((i,k,j),0) for i,j,k in product(range(14),repeat=3)))
ck('cyclic_identity',all(hh.get((i,j,k),0)+hh.get((j,k,i),0)+hh.get((k,i,j),0)==0 for i,j,k in product(range(14),repeat=3)))
ck('actual_metric_tracefree',all(sum(eta[i]*hh.get((i,i,k),0) for i in range(14))==0 for k in range(14)))
ck('all_original_polar_constraints',all(gram(k,hh)==0 for k in K))
ck('all_original_full_polar_constraints',all(not pol(hh,k) for k in K))
S=[symbol(hh,{j:F(1)}) for j in range(14)];receivers=list(combinations_with_replacement(range(14),2))
from sage.all import matrix,QQ
M=matrix(QQ,[[S[j].get(ij,0) for j in range(14)] for ij in receivers]);ck('original_rank_exactly_two',M.rank()==2);ck('original_nullity_twelve',M.right_nullity()==12)
ctrl('universal_rank_three_refuted',M.rank()<3 and bool(hh))
# Coefficient-wise cubic identity B(v)(v,v)=0, on every original basis hook.
for hi,g in enumerate(rep):
 cubic=defaultdict(F)
 for j in range(14):
  for (i,k),z in symbol(g,{j:F(eta[j])}).items():cubic[tuple(sorted((i,j,k)))]+=(1 if i==k else 2)*z
 ck('universal_cubic_identity_basis_'+str(hi),not any(cubic.values()))
# Strongest missing-hypothesis control: nonzero fully alternating h has rank0
# but cyclic sum nonzero; treating it as a hook would contradict the theorem.
alt={}
for perm in permutations((0,1,2)):
 inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3));alt[perm]=F((-1)**inv)
ck('alternating_symbol_zero',all(not symbol(alt,{j:F(1)}) for j in range(14)))
ctrl('cyclic_hypothesis_required',alt[0,1,2]+alt[1,2,0]+alt[2,0,1]==3)
# Exact dimension identities; universal proof is in companion note.
for n in [0,1,2,12,13,50,156,1000]:
 target=comb(n+13,13);one=comb(n+12,11);ratio=F((n+13)*(n+1),156)
 ck('dimension_identity_'+str(n),F(target,one)==ratio)
 minimum=(target+one-1)//one
 ck('necessary_integer_bank_'+str(n),minimum*one>=target and (minimum-1)*one<target)
 if n>=2:ck('stronger_than_old_linear_'+str(n),ratio>F(n+1,13))
ctrl('domain_bound_is_not_surjectivity',comb(13,13)<comb(12,11))
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2458-hook-symbol-rank-boundary-2026-11-01.md','tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py','explorations/conditional-build/k2455-mixed-compatibility-filtration-2026-11-01.md']
report={'result_id':'K2458','checks':checks,'controls':controls,'original_fixture':{'triple':list(tri),'signs':list(signs),'tested_candidates':tested,'hook':{','.join(map(str,k)):str(v) for k,v in hh.items()},'rank':2,'nullity':12,'necessary_summands':'ceil((n+13)*(n+1)/156)'},'evidence_kinds':{'universal':'written cubic syzygy, polynomial-domain rank1 contradiction and homogeneous dimension theorem','exact':'original polar rank2 witness, all-basis cubic identity and missing-cyclic control','ceiling':'individually ordinary-null summands only; no full joint inverse obstruction'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2458-hook-symbol-rank-boundary.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2458',len(checks),'checks',len(controls),'controls PASS',report['original_fixture'])
