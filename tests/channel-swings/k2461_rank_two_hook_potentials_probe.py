"""Original rank-two classification witnesses and twelve-variable analytic primitive.
Exhaustiveness and analytic scope use the companion proof, not sampled ranks.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,combinations_with_replacement,product
from math import comb,factorial
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
ck('original_input_reconstruction',all(inherited.values()))
def make(tri,signs):
 a,b,c=tri;mm={a:F(1),b:F(signs[0]),c:F(signs[1])};om={}
 for i,j,v in [(a,b,1/mm[c]),(b,c,1/mm[a]),(c,a,1/mm[b])]:om[i,j]=v;om[j,i]=-v
 hh={}
 for i,j in om:hh[i,i,j]=mm[i]*om[i,j];hh[i,j,i]=-mm[i]*om[i,j]
 return hh,mm,om
survivors=[];total=0;badpolar=None
for tri in combinations(range(14),3):
 if len({eta[i] for i in tri})!=1:continue
 for signs in product((1,-1),repeat=2):
  total+=1;hh,mm,om=make(tri,signs)
  ck('trace_'+str(total),all(sum(eta[i]*hh.get((i,i,k),0) for i in range(14))==0 for k in range(14)))
  ck('cyclic_'+str(total),all(hh.get((i,j,k),0)+hh.get((j,k,i),0)+hh.get((k,i,j),0)==0 for i,j,k in product(tri,repeat=3)))
  ck('normal_form_'+str(total),all(hh.get((i,j,k),0)==(2*mm.get(i,0)*om.get((j,k),0)-om.get((i,j),0)*mm.get(k,0)+om.get((i,k),0)*mm.get(j,0))/3 for i,j,k in product(tri,repeat=3)))
  if all(gram(k,hh)==0 for k in K):
   ck('full_polar_'+str(total),all(not pol(hh,k) for k in K))
   survivors.append((tri,signs,hh,mm))
  else:badpolar=hh
ck('complete_real_line_enumeration',total==280)
ck('exact_original_survivor_count',len(survivors)==16)
ck('exact_original_supports',sorted(set(t for t,s,h,m in survivors))==[(2,3,10),(4,5,6),(7,8,9),(11,12,13)])
ctrl('tracefree_does_not_imply_original_polar',badpolar is not None and any(gram(k,badpolar)!=0 for k in K))
from sage.all import matrix,QQ
receivers=list(combinations_with_replacement(range(14),2));line_data=[]
for idx,(tri,signs,hh,mm) in enumerate(survivors):
 S=[{i:F(1)} for i in range(14) if i not in tri]+[mm]
 mat=matrix(QQ,[[symbol(hh,{j:F(1)}).get(ij,0) for j in range(14)] for ij in receivers]);ck('survivor_rank2_'+str(idx),mat.rank()==2)
 ck('null_ring_'+str(idx),all(not symbol(hh,x) for x in S))
 # Full original scalar second coefficient on every pair of null directions
 # and every original background hook; no projected subcarrier assumption.
 zeros=all(not sum(F(eta[i]*eta[j],2)*av*bv*fp(kk,hh,i,j) for i,av in x.items() for j,bv in y.items()) for kk in K for x in S for y in S)
 ck('all_second_terms_zero_'+str(idx),zeros)
 aa=[jlinear(hh,x) for x in S];line_data.append({'triple':list(tri),'signs':list(signs),'first_order':[str(z) for z in aa],'null_covectors':[{str(i):str(v) for i,v in x.items()} for x in S]})
 print('line',idx,'checked',flush=True)
# Exact predecessor witness, not a new arbitrary hook.
old=json.loads((ROOT/'lab/process/k2458-hook-symbol-rank-boundary.json').read_text())['original_fixture']
hh={tuple(map(int,k.split(','))):F(v) for k,v in old['hook'].items()}
ck('original_witness_recovered',any(hh==g for t,s,g,m in survivors))
S=[{i:F(1)} for i in range(14) if i not in (2,3,10)]+[{2:F(1),3:F(-1),10:F(1)}]
aa=[jlinear(hh,x) for x in S];ck('complete_original_first_order_on_ring',aa==[field(0)]*3+[field(-1)/16,field(1)/16]+[field(0)]*7)
ck('boundary_coordinate_owned',covs[2]=={5:F(1)} and covs[3]=={6:F(1)})
ck('original_hook_norm',sum(abs(v) for v in hh.values())==12)
# coordinates3,4 are t=x5 and u=x6; use the full finite inverse expansion.
def prim(P):
 out=defaultdict(lambda:field(0))
 for mon,v in P.items():
  nt=mon.count(3);nu=mon.count(4)
  for j in range(nu+1):
   z=list(mon)
   for _ in range(j):z.remove(4)
   z += [3]*(j+1)
   out[tuple(sorted(z))]+=-16*v*field(factorial(nu)*factorial(nt))/field(factorial(nu-j)*factorial(nt+j+1))
 return {m:v for m,v in out.items() if v}
def scalar(P):return pa((field(-1)/16,der(P,3)),(field(1)/16,der(P,4)))
def ordinary(P):
 out={}
 for r,x in enumerate(S):
  for ij,z in symbol(hh,x).items():out[ij]=pa((1,out.get(ij,{})),(ff(z),der(P,r)))
 return {k:v for k,v in out.items() if v}
fixtures=[{(0,2,11):field(2),(3,4,8):root2},{(4,)*8:field(1)},{(1,5,6,7,9,10,11):field(-3)}]
for i,P in enumerate(fixtures):
 V=prim(P);fixture_degree=len(next(iter(P)));d=fixture_degree+1
 ck('scalar_inverse_'+str(i),scalar(V)==P)
 ck('full_ordinary_zero_'+str(i),not ordinary(V))
 ck('original_boundary_ideal_'+str(i),all(3 in mon for mon in V))
 ck('analytic_coefficient_bound_'+str(i),3*field(d)*sum(abs(v) for v in V.values())<=48*d*2**(d-1)*sum(abs(v) for v in P.values()))
 ck('actual_diagonal_normalization_'+str(i),pa((field(4)/d,scalar(pa((field(d)/4,V)))))==P)
ctrl('wrong_scalar_sign_detected',pa((field(1)/16,der(prim(fixtures[1]),3)),(field(1)/16,der(prim(fixtures[1]),4)))!=fixtures[1])
ctrl('omitted_diagonal_factor_detected',scalar(pa((field(9)/4,prim(fixtures[1]))))!=fixtures[1])
ctrl('arbitrary_ambient_extension_rejected',bool(symbol(hh,{2:F(1)})))
# Real mixed-sign repeats do not satisfy the tracefree normal form.
mixed=next(t for t in combinations(range(14),3) if len({eta[i] for i in t})>1);bad,_,_=make(mixed,(1,1))
ctrl('mixed_sign_equal_real_amplitudes_rejected',any(sum(eta[i]*bad.get((i,i,k),0) for i in range(14))!=0 for k in range(14)))
# A cyclic tracefree rank2 hook can have distinct entries: repeatedness is essential.
a,b,c=0,1,2
alpha={a:F(1)};beta={b:F(1)};mm={c:F(1)};om={(a,b):F(1),(b,a):F(-1)}
full={}
for i,j,k in product(range(14),repeat=3):
 val=F(2*mm.get(i,0)*om.get((j,k),0)-om.get((i,j),0)*mm.get(k,0)+om.get((i,k),0)*mm.get(j,0),3)
 if val:full[i,j,k]=val
fullmat=matrix(QQ,[[symbol(full,{j:F(1)}).get(ij,0) for j in range(14)] for ij in receivers])
ck('nonrepeated_control_is_tracefree_cyclic',all(sum(eta[i]*full.get((i,i,k),0) for i in range(14))==0 for k in range(14)) and all(full.get((i,j,k),0)+full.get((j,k,i),0)+full.get((k,i,j),0)==0 for i,j,k in product(range(3),repeat=3)))
ctrl('rank2_does_not_imply_repeated',fullmat.rank()==2 and any(len(set(ix))==3 for ix in full))
for dim_degree in [0,1,43,44,100,203]:
 ratio=F(comb(dim_degree+13,13),comb(dim_degree+12,11));ck('dimension_ratio_'+str(dim_degree),ratio==F((dim_degree+13)*(dim_degree+1),156))
ck('first_original_dimension_exclusion',56*44<=16*156 and 57*45>16*156)
ctrl('arbitrary_repetition_not_new_dimension',16*comb(56,11)<comb(57,13))

# Released exact full-bank image: only four lines are scalar-active.
active=[z for z in line_data if any(v!='0' for v in z['first_order'])]
ck('only_four_scalar_active_lines',len(active)==4 and all(z['triple']==[2,3,10] for z in active))
ck('active_derivatives_exact',all(z['first_order'][3]==str(field(z['signs'][0])/16) and z['first_order'][4]==str(-field(z['signs'][0])/16) and all(v=='0' for j,v in enumerate(z['first_order']) if j not in (3,4)) for z in active))
from sage.all import PolynomialRing
PR=PolynomialRing(field,14,'x');xs=PR.gens();outside=[i for i in range(14) if i not in (2,3,10)]
def contrast(g):return g.derivative(xs[2],2)-g.derivative(xs[3],2),g.derivative(xs[2],2)-g.derivative(xs[10],2)
def monomial(exps):
 out=PR(1)
 for i,power in enumerate(exps):out*=xs[i]**power
 return out
fixtures2=[xs[5]*(xs[2]+xs[3]+xs[10])**3+xs[6]**2*(xs[2]-xs[3]+xs[10])**2,
 (xs[2]+xs[3]-xs[10])**5-3*(xs[2]-xs[3]-xs[10])**5,
 xs[0]**3*(xs[2]+2*xs[3]-xs[10])]
for fi,g in enumerate(fixtures2):
 ck('full_image_PDE_'+str(fi),not any(contrast(g)))
 groups={}
 for powers,vv in g.dict().items():
  special=tuple(powers[i] for i in (2,3,10));k=sum(special);spect=tuple(powers[i] if i in outside else 0 for i in range(14));groups.setdefault((spect,k),{})[special]=vv
 rec=PR(0);field_norm=field(0);n0=g.total_degree();parts={sign:{} for sign in product((1,-1),repeat=2)}
 for (spect,k),P in groups.items():
  for sig in parts:
   sj,tj=sig
   val=P.get((k,0,0),0)
   if k>=1:val+=sj*P.get((k-1,1,0),0)/field(k)+tj*P.get((k-1,0,1),0)/field(k)
   if k>=2:val+=sj*tj*P.get((k-2,1,1),0)/field(k*(k-1))
   val=field(val)/4
   if not val:continue
   rec+=val*monomial(spect)*(xs[2]+sj*xs[3]+tj*xs[10])**k
   key=tuple(sorted([j for j,ix in enumerate(outside) for _ in range(spect[ix])]+[11]*k))
   parts[sig][key]=parts[sig].get(key,field(0))+val
 ck('character_reconstruction_'+str(fi),rec==g)
 for (sj,tj),P in parts.items():
  if not P:continue
  V=pa((-sj,prim(P)))
  ck(f'all_line_primitive_{fi}_{sj}_{tj}',pa((field(sj)/16,der(V,3)),(-field(sj)/16,der(V,4)))==P)
  ck(f'all_line_boundary_{fi}_{sj}_{tj}',all(3 in mon for mon in V))
  # Expand the ridge coordinate into original axes for the actual coefficient norm.
  VP=PR(0)
  for mon,vv in V.items():
   term=PR(vv)
   for j in mon:term*=xs[outside[j]] if j<11 else xs[2]+sj*xs[3]+tj*xs[10]
   VP+=term
  field_norm+=3*field(n0+1)*sum(abs(vv) for vv in VP.coefficients())
 ck('synthesized_original_coordinate_bound_'+str(fi),field_norm<=48*(n0+1)*3**n0*sum(abs(vv) for vv in g.coefficients()))
ctrl('quadratic_receiver_excluded',any(contrast(xs[2]**2)))
ctrl('actual_top_jet_cubic_excluded',any(contrast(xs[2]**3)))
ctrl('image_not_an_algebra',not any(contrast(xs[2])) and any(contrast(xs[2]**2)))
y1=sum(ff(vv)*xs[i] for i,vv in covs[1].items())
ck('old_rank3_direction_ordinary_null',not symbol(h,covs[1]))
ctrl('rank3_image_not_excluded',any(contrast(y1**3)) and jlinear(h,covs[1])==field(2253)/2)
# Actual four signed-power coefficient ranks, distinct from universal proof.
for k in range(8):
 mons=[(i,j,k-i-j) for i in range(k+1) for j in range(k-i+1)]
 mat=matrix(QQ,[[F(factorial(k),factorial(i)*factorial(j)*factorial(l))*sj**j*tj**l for sj,tj in product((1,-1),repeat=2)] for i,j,l in mons])
 ck('ridge_degree_rank_'+str(k),mat.rank()==min(4,1 if k==0 else (3 if k==1 else 4)))
def choose(n,k):return comb(n,k) if n>=k>=0 else 0
for degree in range(10):
 dim=sum((1 if k==0 else (3 if k==1 else 4))*choose(degree-k+10,10) for k in range(degree+1))
 ck('full_hilbert_dimension_'+str(degree),dim==choose(degree+11,11)+2*choose(degree+10,11)+choose(degree+9,11))
ck('first_scalar_image_deficit',choose(13,11)+2*choose(12,11)+choose(11,11)==103 and choose(15,13)==105)
# Released cancellation rigidity: original full three-dimensional triple span.
active_hooks=[hh0 for tr,sg,hh0,mm0 in survivors if tr==(2,3,10)]
entry_keys=sorted(set().union(*(set(hh0) for hh0 in active_hooks)))
HM=matrix(QQ,[[hh0.get(ix,0) for hh0 in active_hooks] for ix in entry_keys])
ck('active_constant_span_dimension',HM.rank()==3)
base_hooks=[active_hooks[j] for j in HM.pivots()]
for kd in range(7):
 mons3=[(i,j,kd-i-j) for i in range(kd+1) for j in range(kd-i+1)]
 outmons=[(i,j,kd-1-i-j) for i in range(kd) for j in range(kd-i)] if kd else []
 outkeys=[(ij,mo) for ij in receivers for mo in outmons];outix={z:j for j,z in enumerate(outkeys)}
 cols=[]
 for hb in base_hooks:
  for mo in mons3:
   vec=[QQ(0)]*len(outkeys)
   for local,axis in enumerate((2,3,10)):
    if not mo[local]:continue
    dd=list(mo);dd[local]-=1
    for ij,vv in symbol(hb,{axis:F(1)}).items():vec[outix[ij,tuple(dd)]]+=QQ(vv)*mo[local]
   cols.append(vec)
 CM=matrix(QQ,len(outkeys),len(cols),lambda i,j:cols[j][i])
 nullity=CM.ncols()-CM.rank();expected_null=3 if kd==0 else 4
 ck('cancel_kernel_dimension_'+str(kd),nullity==expected_null)
 ridgecols=[]
 BM=matrix(QQ,[[hb.get(ix,0) for hb in base_hooks] for ix in entry_keys])
 for hb,sg in zip(active_hooks,[sg for tr,sg,hh0,mm0 in survivors if tr==(2,3,10)]):
  from sage.all import vector
  co=BM.solve_right(vector(QQ,[hb.get(ix,0) for ix in entry_keys]));sj,tj=sg
  vec=[co[hi]*QQ(factorial(kd))/QQ(factorial(i)*factorial(j)*factorial(l))*sj**j*tj**l for hi in range(3) for i,j,l in mons3]
  ck('cancel_ridge_is_null_'+str(kd)+'_'+str(sg),not any(CM*vector(QQ,vec)))
  ridgecols.append(vec)
 RM=matrix(QQ,len(cols),4,lambda i,j:ridgecols[j][i])
 ck('cancel_ridges_span_kernel_'+str(kd),RM.rank()==nullity)
deps=[str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2461-rank-two-hook-potentials-2026-11-01.md','tests/channel-swings/k2437_augmented_compatibility_adjoint_probe.py','tests/channel-swings/k2425_frame_euler_module_probe.py','tests/channel-swings/k2405_fifth_euler_compatibility_probe.py','tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py','lab/process/k2458-hook-symbol-rank-boundary.json','explorations/conditional-build/k2452-partial-analytic-hook-inverse-2026-11-01.md']
report={'result_id':'K2461','checks':checks,'controls':controls,'candidate_lines':total,'original_lines':line_data,'actual_witness_first_order':[str(x) for x in aa],'dimension_exclusion_from_receiver_degree':44,'exact_scalar_image':'kernel(d2^2-d3^2) intersect kernel(d2^2-d10^2)','cancelling_rank_two_span_same_scalar_image':True,'scalar_active_lines':len(active),'exact_scalar_image_first_deficit_degree':2,'actual_top_jet_obstruction_degree':3,'evidence_kinds':{'universal':'rank2 normal form; real repeated tracefree support classification; exact two-PDE scalar image via parity recurrence; four-character synthesis and analytic bound48*d*3^(d-1)','exact':'complete280 candidate polarization enumeration,16 full-rank/null-ring/scalar coefficients, original boundary and polynomial controls','ceiling':'entire rank2 constant span including ordinary cancellations only; distinct12-variable ring, no full mixed analytic/nonlinear inverse'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2461-rank-two-hook-potentials.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2461',len(checks),'checks',len(controls),'controls PASS',flush=True)
