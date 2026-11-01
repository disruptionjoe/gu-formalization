"""Rigorous full-carrier interval certificate for reordered local measurements.

Analytical locality/completeness is proved in the companion note. Interval
residuals are consistency checks; positive LDL pivots certify the spectral bound.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
from fractions import Fraction as F
import json,hashlib,sys
from flint import arb,acb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,b):
 checks[k]=bool(b)
 if not b:raise AssertionError(k)
def ctrl(k,b):
 controls[k]=bool(b)
 if not b:raise AssertionError(k)
def aa(x):
 z=F(x);return arb(z.numerator)/z.denominator
strings=[(0,0,0,0),(0,1,1,0),(1,0,0,1),(1,0,1,2),(1,1,1,3),(1,1,0,4),(2,1,0,5),(2,1,1,6),(2,0,1,7),(2,0,0,8)]
coords=list(product(range(3),range(2),range(2),range(9)));idx={x:i for i,x in enumerate(coords)};ref={e:(f,r,b) for f,r,b,e in strings};ref[0]=(0,0,0)
def character(x):
 f,r,b,e=x;fe,re,be=ref[e];return tuple(int(f==j)-int(fe==j) for j in range(3))+(r-b-re+be,)
groups=defaultdict(list)
for x in coords:groups[character(x)].append(idx[x])
ck('complete_108_carrier_31_blocks',len(coords)==108 and len(groups)==31 and len(groups[(0,0,0,0)])==14)
ck('finite_group_no_alias',len({tuple(c%3 for c in z[:3])+(z[3]%5,) for z in groups})==31)
ctrl('support_truncation_rejected',len(groups[(0,0,0,0)])!=len(strings))
dims=[3,2,2,9]
phase={d:[acb(0,2*arb.pi()*j/d).exp() for j in range(d)] for d in [2,3,9]}
def basis(x,out,last):
 a=acb(1)
 for j,k in zip([t for t in range(4) if t!=last],out):a*=phase[dims[j]][(k*x[j])%dims[j]]/arb(dims[j]).sqrt()
 return a
def build(mu,last,wrong=False,no_feed=False):
 measured=[j for j in range(4) if j!=last];columns=[];ps=[]
 for out in product(*[range(dims[j]) for j in measured]):
  c=[acb(0) for _ in range(dims[last])]
  for i,x in enumerate(strings):
   z=basis(x,out,last);c[x[last]]+=aa(mu[i]).sqrt()*(z if wrong else z.conjugate())
  if no_feed:
   c=[acb(1)]+[acb(0) for _ in c[1:]]
  p=sum((z*z.conjugate()).real for z in c);assert p>0
  columns.append([basis(x,out,last)*c[x[last]] for x in coords]);ps.append(p)
 return columns,ps
def act(columns,ps,psi):
 ans=[acb(0) for _ in coords]
 for v,p in zip(columns,ps):
  dot=sum(z.conjugate()*q for z,q in zip(v,psi))/p
  ans=[x+z*dot for x,z in zip(ans,v)]
 return ans
def matrix_block(cols,ps,ix):
 return [[sum(v[i]*v[j].conjugate()/p for v,p in zip(cols,ps)) for j in ix] for i in ix]
def ldl(M):
 M=[r[:] for r in M];piv=[]
 for k in range(len(M)):
  p=M[k][k].real
  if not p>0:return False,piv+[p]
  assert M[k][k].imag.contains(0);piv.append(p)
  for i in range(k+1,len(M)):
   for j in range(k+1,i+1):
    z=M[i][j]-M[i][k]*M[j][k].conjugate()/p
    M[i][j]=acb(z.real) if i==j else z;M[j][i]=M[i][j].conjugate()
 return True,piv
dual_seeds=[[465, 325, -149, 73, -254, 186, 570, 51, 336, 114, 18, -243, -96, 172], [446, 337, -136, 213, -269, 112, 521, 0, 276, 91, -128, -290, -66, 281]]
prior=json.loads((ROOT/'lab/process/k2454-two-setting-local-verifier.json').read_text());fixtures=[]
for law,data in enumerate(prior['original_laws']):
 mu=[F(z) for z in data['weights']];ck(f'original_positive_normalized_{law}',len(mu)==10 and sum(mu)==1 and all(z>0 for z in mu))
 psi=[acb(0) for _ in coords]
 for x,m in zip(strings,mu):psi[idx[x]]=acb(aa(m).sqrt())
 banks={last:build(mu,last) for last in [3,2,1,0]}
 for last,(cols,ps) in banks.items():
  ck(f'positive_conditional_probs_{law}_{last}',all(p>0 for p in ps))
  ck(f'probabilities_sum_consistency_{law}_{last}',sum(ps).contains(1))
  out=act(cols,ps,psi);ck(f'complete_original_target_consistency_{law}_{last}',all((x-y).contains(0) for x,y in zip(out,psi)))
  # Each disjoint measured-basis column has unit norm after normalization;
  # orthogonality follows analytically from the product Fourier bases.
  ck(f'column_norm_consistency_{law}_{last}',all((sum((z*z.conjugate()).real for z in v)-p).contains(0) for v,p in zip(cols,ps)))
  bad=act(*build(mu,last,wrong=True),psi)
  ctrl(f'wrong_Fourier_conjugation_{law}_{last}',sum(((x-y)*(x-y).conjugate()).real for x,y in zip(bad,psi))>aa('1/1000000'))
  bad=act(*build(mu,last,no_feed=True),psi)
  ctrl(f'missing_conditional_feedforward_{law}_{last}',sum(((x-y)*(x-y).conjugate()).real for x,y in zip(bad,psi))>aa('1/1000000'))
 blockrows=[]
 for gi,(char,ix) in enumerate(sorted(groups.items())):
  mats={last:matrix_block(*banks[last],ix) for last in banks};n=len(ix)
  O=[[mats[3][i][j]/2+mats[2][i][j]/4+mats[1][i][j]/8+(acb(aa('1/8')) if i==j and coords[ix[i]] in strings else 0) for j in range(n)] for i in range(n)]
  H=[[acb(aa('11/20'))*(i==j)+psi[ix[i]]*psi[ix[j]].conjugate()-O[i][j] for j in range(n)] for i in range(n)]
  ok,piv=ldl(H);ck(f'full_block_LDL_{law}_{gi}',ok)
  blockrows.append({'character':list(char),'dimension':n,'minimum_pivot':str(min(piv,key=lambda z:float(z.mid())))})
  if char==(0,0,0,0):
   # Mistakenly asserting gap 3/4 has an actual negative direction.
   bad=[[acb(aa('1/4'))*(i==j)+psi[ix[i]]*psi[ix[j]].conjugate()-O[i][j] for j in range(n)] for i in range(n)]
   wrong,pv=ldl(bad);ctrl(f'overclaimed_three_quarter_gap_{law}',not wrong and pv[-1]<0)
   # Exact rational seed, then analytical orthogonal projection to Psi-perp.
   # Numerical optimization selected the seed only; all decisions below use balls.
   seed=[acb(v) for v in dual_seeds[law]];target=[psi[i] for i in ix]
   dot=sum(z.conjugate()*u for z,u in zip(target,seed));wv=[u-z*dot for u,z in zip(seed,target)]
   norm=sum((z*z.conjugate()).real for z in wv);assert norm>0
   Qmat=[[acb(int(i==j and coords[ix[i]] in strings)) for j in range(n)] for i in range(n)]
   dual_bounds=[]
   for ti,mat in enumerate([Qmat,mats[3],mats[2],mats[1],mats[0]]):
    val=sum(wv[i].conjugate()*mat[i][j]*wv[j] for i in range(n) for j in range(n)).real
    ck(f'convex_family_dual_witness_{law}_{ti}',val>aa('13/25')*norm)
    dual_bounds.append(str(val/norm))
   ctrl(f'half_gap_impossible_in_five_effect_hull_{law}',all(arb(x)>aa('1/2') for x in dual_bounds))
 fixtures.append({'law':law+1,'weights':list(map(str,mu)),'certified_gap':'9/20','conditional_outcome_counts':{str(k):len(v[1]) for k,v in banks.items()},'blocks':blockrows,'dual_seed':dual_seeds[law],'dual_Rayleigh_bounds':dual_bounds,'convex_family_gap_upper_bound':'12/25'})
# Compose the same independently justified K2456 budget with the K2459 theorem.
pi=arb(1)/2;eta=arb(1)/2;c=arb(2).log();J=(1-c)/2;C=(pi+eta*J)**2/(4*J*(1-eta)**2);gamma=C/pi
B=arb('1e-6');beta=arb('1e-8');kap=arb('1e-6');tau=arb('.01');nu=arb(9)/20;L=arb(20).log();D=nu*((tau-4*kap)/2)**2-beta
N=int(((gamma*B+L)/(c*D)).upper().ceil().unique_fmpz())
def bound(n):return 2*((beta+(gamma*B+L)/(c*n))/nu).sqrt()+4*kap
ck('composed_new_certificate',bound(N)<=tau);ctrl('previous_count_fails_declared_budget',bound(N-1)>tau)
ck('positive_actual_mean_success',((beta+(gamma*B+L)/(c*N))/nu).sqrt()/2+kap<arb(1)/4)
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2460-reordered-local-verification-2026-11-01.md','lab/process/k2454-two-setting-local-verifier.json','tests/channel-swings/k2454_two_setting_local_verifier_probe.py','explorations/conditional-build/k2457-local-verifier-phase-design-2026-11-01.md','explorations/conditional-build/k2459-direct-leakage-certificate-2026-11-01.md']
report={'result_id':'K2460','checks':checks,'controls':controls,'original_laws':fixtures,'prospective':{'actual_uses':N,'allowance':str(bound(N)),'gamma':str(gamma)},'evidence_kinds':{'proof':'written conditional local projection, character pinching and operator-order implication','rigorous_interval':'Arb/acb256 all31 full-carrier block LDL certificates for each original law','consistency':'interval target/norm residuals support analytic construction, not exact symbolic zero certificates','consumer':'hypothetical original budget; no measured operation costs'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2460-reordered-local-verification.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2460',len(checks),'checks',len(controls),'controls PASS',report['prospective'])
