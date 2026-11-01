"""Original cancelling-hook scalar lift; analytic proof in companion note."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement
from math import factorial,comb
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
ck('original_inputs',all(inherited.values()))
cc=F(9012,8519);A=F(2253,17038)
U={(11,11,12):F(1),(11,12,11):F(-1),(13,13,12):F(-1),(13,12,13):F(1)}
allowed=[i for i in range(14) if i not in (11,13)]
for name,hh in [('h',h),('U',U)]:
 ck(name+'_original_polar',all(not pol(hh,k) for k in K))
 ck(name+'_tracefree',all(sum(eta[i]*hh.get((i,i,j),0) for i in range(14))==0 for j in range(14)))
 ck(name+'_cyclic',all(hh.get((i,j,k),0)+hh.get((j,k,i),0)+hh.get((k,i,j),0)==0 for i,j,k in hh))
 aa=[jlinear(hh,{i:F(1)}) for i in range(14)]
 ck(name+'_complete_first_order',aa==[ff(A) if name=='h' and i in (4,5) else field(0) for i in range(14)])
# Original coefficient identity proves cancellation on every original background slot.
def T(j):return {(11,11,j):F(-1),(11,j,11):F(1),(13,13,j):F(1),(13,j,13):F(-1)}
for ell,kk in enumerate(K):
 ok=True
 for rr in allowed:
  hh=T(rr)
  for i in allowed:
   for j in allowed:
    want=F(2,3)*((1 if i==rr else 0)*(kk.get((13,13,j),0)-kk.get((11,11,j),0))+(1 if j==rr else 0)*(kk.get((13,13,i),0)-kk.get((11,11,i),0)))
    ok &= fp(kk,hh,i,j)==want
 ck('original_second_coefficient_factorization_'+str(ell),ok)
def integ(P,r):return {tuple(sorted(m+(r,))):v/(m.count(r)+1) for m,v in P.items()}
def primitive(P):
 terms=[]
 for mon,v in P.items():
  n4=mon.count(4);n5=mon.count(5)
  for j in range(n4+1):
   z=list(mon)
   for _ in range(j):z.remove(4)
   z += [5]*(j+1)
   val=v*(-1)**j*field(factorial(n4)*factorial(n5))/(ff(A)*factorial(n4-j)*factorial(n5+j+1))
   terms.append((val,{tuple(sorted(z)):field(1)}))
 return pa(*terms)
def comp(f):return integ(pa((-1,der(f,2)),(ff(cc),der(f,4))),12)
def ordinary(hh,P):
 out={}
 for i in range(14):
  for ij,v in symbol(hh,{i:F(1)}).items():out[ij]=pa((1,out.get(ij,{})),(ff(v),der(P,i)))
 return {k:v for k,v in out.items() if v}
def merge(out,other,scale=-1):
 result=dict(out)
 for ij,v in other.items():result[ij]=pa((1,result.get(ij,{})),(scale,v))
 return {ij:v for ij,v in result.items() if v}
def scalar(hh,P):
 terms=[(jlinear(hh,{i:F(1)}),der(P,i)) for i in range(14)]
 for ell,kk in enumerate(K):
  for i in range(14):
   for j in range(14):
    val=-F(eta[i]*eta[j],2)*fp(kk,hh,i,j)
    if val:terms.append((ff(val),mulvar(der(der(P,i),j),ell)))
 return pa(*terms)
fixtures=[{(2,2,2):field(1)},{(0,2,2):field(1)},{(2,4,12):field(1)},{(4,)*6:field(1)},{(0,1,2,3,4,5,6,7,8,9,10,12):field(1)}]
for z,g in enumerate(fixtures):
 f=primitive(g);F0=comp(f);d=len(next(iter(g)))+1
 ck('ordinary_cancellation_'+str(z),not merge(ordinary(h,f),ordinary(U,F0)))
 ck('original_Jstar_'+str(z),pa((1,scalar(h,f)),(-1,scalar(U,F0)))==g)
 ck('boundary_ideal_'+str(z),all(5 in mon for P in [f,F0] for mon in P))
 ck('ring_preserved_'+str(z),all(set(mon)<=set(allowed) for P in [f,F0] for mon in P))
 ck('actual_degree_normalization_'+str(z),pa((field(4)/d,pa((field(d)/4,scalar(h,f)),(-field(d)/4,scalar(U,F0)))))==g)
 bound=field(d*(d+1))*(1+ff(cc))*2**(d-1)/ff(A)*sum(abs(v) for v in g.values())
 upper=field(d)/4*(ff(sum(abs(v) for v in h.values()))*sum(abs(v) for v in f.values())+ff(sum(abs(v) for v in U.values()))*sum(abs(v) for v in F0.values()))
 ck('geometric_bound_'+str(z),upper<=bound)
 ctrl('omitting_compensator_'+str(z),bool(ordinary(h,f)))
 ctrl('wrong_compensator_sign_'+str(z),bool(merge(ordinary(h,f),ordinary(U,F0),1)))
 if d!=4:ctrl('omitting_4_over_d_'+str(z),pa((field(d)/4,g))!=g)
# Explicit former obstruction and a nonzero mixed scalar contribution.
f=primitive(fixtures[0]);F0=comp(f)
ck('explicit_x2_cubed_f',f=={(2,2,2,5):1/ff(A)})
ck('explicit_x2_cubed_comp',F0=={(2,2,5,12):-3/ff(A)})
ctrl('rank_two_PDE_obstruction_crossed',bool(der(der(fixtures[0],2),2)))
bad={(2,2,5,11):field(1)}
ctrl('forbidden_coordinate_not_unrestricted_inverse',bool(merge(ordinary(h,bad),ordinary(U,comp(bad)))))
# Unintegrated H does not cancel d/dx12, even though it has same boundary factor.
H=pa((-1,der(f,2)),(ff(cc),der(f,4)))
ctrl('omitted_integral_rejected',bool(merge(ordinary(h,f),ordinary(U,H))))
# Enlarged-span necessity: original rank-two hooks have no off-triple slots.
p61=ROOT/'lab/process/k2461-rank-two-hook-potentials.json';prior=json.loads(p61.read_text())
for key in [(2,11),(4,11),(2,13),(4,13)]:
 ck('new_unmatched_symbol_'+str(key),any(symbol(h,{i:F(1)}).get(key,0) for i in [11,13]))
# The old span consists of the full repeated tracefree spaces on four triples.
old_basis=[]
for a0,b0,c0 in [(2,3,10),(4,5,6),(7,8,9),(11,12,13)]:
 for j0,i0,k0 in [(b0,a0,c0),(c0,a0,b0),(a0,b0,c0)]:
  hh={(i0,i0,j0):F(1),(i0,j0,i0):F(-1),(k0,k0,j0):F(-1),(k0,j0,k0):F(1)};old_basis.append(hh)
ck('old_span_no_off_block_cancellation',all(not symbol(hh,{i:F(1)}).get(key,0) for hh in old_basis for i in range(14) for key in [(2,11),(4,11),(2,13),(4,13)]))
from sage.all import matrix,QQ
slots=sorted(set().union(*[set(g) for g in old_basis+[h]]))
ck('enlarged_span_dimension13',matrix(QQ,[[g.get(ix,0) for ix in slots] for g in old_basis+[h]]).rank()==13)
def wave(P,j):return pa((1,der(der(P,2),2)),(-1,der(der(P,j),j)))
def enlarged(P):return all(not der(wave(P,j),r) for j in [3,10] for r in [11,13])
ck('new_scalar_monomials_in_enlarged_image',all(enlarged(g) for g in fixtures))
ctrl('enlarged_span_cubic_obstruction',not enlarged({(2,2,11):field(1)}))
ck('individual_factors_allowed',enlarged({(11,):field(1)}) and enlarged({(2,2):field(1)}))
ctrl('enlarged_image_not_algebra',not enlarged({(2,2,11):field(1)}))
ck('bound_comparison_degree4',F(5*35062,2253)*F(2,3)**3<48)
ck('bound_ratio_monotone',F(6,5)*F(2,3)<1)
for n0 in range(2,8):
 binom=lambda a0,b0:comb(a0,b0) if a0>=b0>=0 else 0
 vdim=binom(n0+11,11)+2*binom(n0+10,11)+binom(n0+9,11)
 idim=binom(n0+9,9)+2*binom(n0+8,9)+binom(n0+7,9)
 dim=binom(n0+11,11)+vdim-idim
 ck('Hilbert_identity_'+str(n0),dim==binom(n0+11,11)+2*binom(n0+10,11)+3*binom(n0+9,11)-binom(n0+7,11))
 if n0==2:ck('all_quadratics',dim==105)
 if n0==3:ck('cubic_dimension556',dim==556)
note='explorations/conditional-build/k2464-cancelling-hook-inverse-2026-11-01.md'
deps=[note,str(Path(__file__).relative_to(ROOT)),'tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py','lab/process/k2452-partial-analytic-hook-inverse.json','lab/process/k2461-rank-two-hook-potentials.json']
for dep in deps[-2:]:
 data=json.loads((ROOT/dep).read_text());ck('authenticated_'+Path(dep).stem,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==hh for p,hh in data['dependencies'].items()))
report={'result_id':'K2464','checks':checks,'controls':controls,'original_h':[[list(ix),str(v)] for ix,v in h.items()],'compensator_U':[[list(ix),str(v)] for ix,v in U.items()],'allowed_ambient_coordinates':allowed,'scalar_coefficient':str(A),'inverse_bound':'d(d+1)(1+9012/8519)*2^(d-1)/(2253/17038)','evidence_kinds':{'universal':'weighted-divergence factorization and explicit characteristic integral; analytic coefficient estimate','finite':'all original background coefficients and exact scalar/ordinary/boundary fixtures','ceiling':'twelve-variable restricted scalar inverse; full mixed and nonlinear convergence open'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2464-cancelling-hook-inverse.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2464',len(checks),'checks',len(controls),'controls PASS')
