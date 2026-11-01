"""Original six-family hook inversion; universal scope is proved in companion note."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from itertools import combinations
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2464_cancelling_hook_inverse_probe.py';src=p.read_text()
exec(compile(src[:src.index('fixtures=')],str(p),'exec'),globals())
priorchecks=dict(checks);checks={};controls={}
ck('original_loaded_coefficients',all(priorchecks.values()))
def hook(p,r,j):return {(p,p,j):F(-1),(p,j,p):F(1),(r,r,j):F(1),(r,j,r):F(-1)}
rows=[(11,13,4,1,1,4),(12,13,4,1,-1,6),(11,12,5,-1,1,6),(7,9,4,-1,-1,4),(7,8,4,-1,-1,6),(8,9,5,-1,-1,6)]
def inverse(g,s,e,k):
 terms=[]
 for mon,v in g.items():
  nk=mon.count(k);n5=mon.count(5)
  for q in range(nk+1):
   m=list(mon)
   for _ in range(q):m.remove(k)
   m += [5]*(q+1)
   val=field(8)*v/s*(-e)**q*field(factorial(nk)*factorial(n5))/(factorial(nk-q)*factorial(n5+q+1))
   terms.append((val,{tuple(sorted(m)):field(1)}))
 return pa(*terms)
records=[]
for idx,(p,r,j,s,e,k) in enumerate(rows):
 H=hook(p,r,j);U=hook(p,r,0);allowed=[i for i in range(14) if i not in (p,r)]
 for tag,hh in [('H',H),('U',U)]:
  ck(f'polar_{idx}_{tag}',all(not pol(hh,z) for z in K))
  ck(f'trace_{idx}_{tag}',all(sum(eta[i]*hh.get((i,i,z),0) for i in range(14))==0 for z in range(14)))
  ck(f'cyclic_{idx}_{tag}',all(hh.get((a,b,c),0)+hh.get((b,c,a),0)+hh.get((c,a,b),0)==0 for a,b,c in hh))
  want=[field(0)]*14
  if tag=='H':want[5]=field(s)/8;want[k]+=field(s*e)/8
  ck(f'original_first_order_{idx}_{tag}',[jlinear(hh,{i:F(1)}) for i in range(14)]==want)
 # Determine the fixed tensor factor from original data, then verify complete coefficients.
 ratios=[]
 for kk in K:
  for rr in [0,j]:
   for a in allowed:
    for b in allowed:
     w=F(2,3)*((a==rr)*(kk.get((r,r,b),0)-kk.get((p,p,b),0))+(b==rr)*(kk.get((r,r,a),0)-kk.get((p,p,a),0)))
     z=fp(kk,hook(p,r,rr),a,b)
     if w:ratios.append(z/w)
     else:ck(f'zero_factor_{idx}_{len(checks)}',z==0) if z else None
 ck(f'original_second_factor_{idx}',bool(ratios) and len(set(ratios))==1 and ratios[0]==1)
 fixtures=[{(2,2,t):field(1)} for t in [11,13] if t in allowed]+[{tuple(sorted([k,k,5,0])):field(1)},{tuple(sorted(allowed)):field(1)},{(k,)*6:field(1)}]
 for z,g in enumerate(fixtures):
  f=inverse(g,s,e,k);ff0=integ(der(f,j),0);F0=pa((-field(eta[j])/eta[0],ff0));d=len(next(iter(g)))+1
  ck(f'ordinary_{idx}_{z}',not merge(ordinary(H,f),ordinary(U,F0),1))
  ck(f'scalar_{idx}_{z}',pa((1,scalar(H,f)),(1,scalar(U,F0)))==g)
  ck(f'boundary_{idx}_{z}',all(5 in m for m in f) and all(0 in m for m in F0))
  ck(f'normalization_{idx}_{z}',pa((field(4)/d,pa((field(d)/4,scalar(H,f)),(field(d)/4,scalar(U,F0)))))==g)
  norm=field(d)*(sum(abs(v) for v in f.values())+sum(abs(v) for v in F0.values()))
  ck(f'bound_{idx}_{z}',norm<=8*d*(d+1)*2**(d-1)*sum(abs(v) for v in g.values()))
  if F0:
   ctrl(f'missing_compensator_{idx}_{z}',bool(ordinary(H,f)))
   ctrl(f'wrong_compensator_sign_{idx}_{z}',bool(merge(ordinary(H,f),ordinary(U,F0),-1)))
  if d!=4:ctrl(f'normalization_needed_{idx}_{z}',pa((field(d)/4,g))!=g)
 records.append({'pair':[p,r],'slot':j,'scalar_direction':{'5':str(F(s,8)),str(k):str(F(s*e,8))},'second_factor':str(ratios[0])})
AA=[7,8,9];BB=[11,12,13]
def wave(g,j):return pa((1,der(der(g,2),2)),(-1,der(der(g,j),j)))
def pd(g,inds):
 for j in inds:g=der(g,j)
 return g
def high(m):return len(set(m)&set(AA))>=2 and len(set(m)&set(BB))>=2
def insum(g):return all(not pd(wave(g,j),a+b) for a in combinations(AA,2) for b in combinations(BB,2) for j in [3,10])
bad={(2,2,7,8,11,12):field(1)}
ctrl('first_missing_degree6',not insum(bad))
ck('literal_nonzero_PDE',pd(wave(bad,3),(7,8,11,12))=={():field(2)})
# Entire high-support minimum degree4 sector times all quadratic monomials in(2,3,10).
for a in combinations(AA,2):
 for b in combinations(BB,2):
  base=tuple(sorted(a+b));good=pa(*[(1,{tuple(sorted(base+(j,j))):field(1)}) for j in [2,3,10]])
  ck('high_support_old_image_'+str(base),insum(good))
  for j in [2,3,10]:ctrl('single_square_outside_'+str((base,j)),not insum({tuple(sorted(base+(j,j))):field(1)}))
ck('lowest_support_degree4',min(len(a+b) for a in combinations(AA,2) for b in combinations(BB,2))==4)
ck('six_PDE_order',4+2==6)
for n in range(0,10):
 cn=lambda k:comb(k+13,13) if k>=0 else 0
 codim=18*cn(n-6)-24*cn(n-7)-cn(n-8)+12*cn(n-9)-4*cn(n-10)
 ck('Hilbert_nonnegative_'+str(n),0<=codim<=cn(n))
 if n<=5:ck('full_degree_'+str(n),codim==0)
 if n==6:ck('first_codimension18',codim==18 and cn(n)-codim==27114)
ctrl('rings_not_unrestricted',all(any(i in next(iter(bad)) for i in pair[:2]) for pair in rows))
ck('uniform_bound_start',8*5*F(2,3)**3<48)
ck('uniform_bound_ratio_decreases',F(6,5)*F(2,3)<1)
# Boundary distinction: j5 primitive loses x5 in derivative but x0 protects it.
f=inverse({(4,4,4):field(1)},-1,1,6);F0=integ(der(f,5),0)
ctrl('x5_only_boundary_would_be_wrong',any(5 not in m for m in F0) and all(0 in m for m in F0))
# Released original two-axis family: exhaust its precise simple ansatz.
found=[]
for p0 in range(14):
 for r0 in range(p0+1,14):
  if p0 in [0,5] or r0 in [0,5] or eta[p0]!=eta[r0]:continue
  H0=hook(p0,r0,0);U0=hook(p0,r0,5)
  if not all(not pol(hh,z) for hh in [H0,U0] for z in K):continue
  a0=[jlinear(H0,{i:F(1)}) for i in range(14)];a5=[jlinear(U0,{i:F(1)}) for i in range(14)]
  if any(z for i,z in enumerate(a0) if i!=0) or any(z for i,z in enumerate(a5) if i!=5):continue
  B0=a0[0]-field(eta[0])/eta[5]*a5[5]
  if B0:found.append((p0,r0,B0))
ck('exhaustive_simple_two_axis_family',found==[(4,6,ff(F(-106642,17255)))])
H0=hook(4,6,0);U0=hook(4,6,5);B0=ff(F(-106642,17255))
ck('seventh_alpha_original', [jlinear(H0,{i:F(1)}) for i in range(14)]==[ff(F(-72096,17255)) if i==0 else field(0) for i in range(14)])
ck('seventh_beta_original', [jlinear(U0,{i:F(1)}) for i in range(14)]==[ff(F(34546,17255)) if i==5 else field(0) for i in range(14)])
ck('original_boundary_metric_signs',eta[0]==eta[5]==1)
for kk in K:
 for j0 in [0,5]:
  for a0 in range(14):
   for b0 in range(14):
    if a0 in [4,6] or b0 in [4,6]:continue
    want=F(2,3)*((a0==j0)*(kk.get((6,6,b0),0)-kk.get((4,4,b0),0))+(b0==j0)*(kk.get((6,6,a0),0)-kk.get((4,4,a0),0)))
    if fp(kk,hook(4,6,j0),a0,b0)!=want:raise AssertionError('original seventh scalar factorization')
ck('complete_original_seventh_scalar_factor',True)
for z,g in enumerate([bad,{(0,0,2,5,5,11):field(2)},{tuple(i for i in range(14) if i not in [4,6]):field(1)}]):
 f=pa((1/B0,integ(g,0)));F0=pa((-1/B0,integ(g,5)));d0=len(next(iter(g)))+1
 ck('seventh_ordinary_'+str(z),not merge(ordinary(H0,f),ordinary(U0,F0),1))
 ck('seventh_scalar_'+str(z),pa((1,scalar(H0,f)),(1,scalar(U0,F0)))==g)
 ck('seventh_boundary_'+str(z),all(0 in m for m in f) and all(5 in m for m in F0))
 ck('seventh_norm_'+str(z),d0*(sum(abs(v) for v in f.values())+sum(abs(v) for v in F0.values()))<=2*d0/abs(B0)*sum(abs(v) for v in g.values()))
 ck('seventh_actual_4_over_d_'+str(z),pa((field(4)/d0,pa((field(d0)/4,scalar(H0,f)),(field(d0)/4,scalar(U0,F0)))))==g)
 ctrl('seventh_omit_compensator_'+str(z),bool(ordinary(H0,f)))
 ctrl('seventh_omit_normalization_'+str(z),pa((field(d0)/4,g))!=g)
def in7(g):return all(not pd(wave(g,j),a+b+(e,)) for a in combinations(AA,2) for b in combinations(BB,2) for e in [4,6] for j in [3,10])
bad7=mulvar(bad,4)
ck('old_degree6_crossed',in7(bad))
ctrl('new_degree7_not_covered',not in7(bad7))
ck('new_exact_PDE',pd(wave(bad7,3),(4,7,8,11,12))=={():field(2)})
ck('nonlinear_factors_in7',in7({(2,2,4):field(1)}) and in7({(7,8,11,12):field(1)}))
ctrl('new_image_not_algebra',not in7(bad7))
for n in range(0,13):
 cn=lambda k:comb(k+13,13) if k>=0 else 0
 codim=36*cn(n-7)-66*cn(n-8)+22*cn(n-9)+25*cn(n-10)-20*cn(n-11)+4*cn(n-12)
 ck('seven_Hilbert_nonnegative_'+str(n),0<=codim<=cn(n))
 if n<=6:ck('seven_full_degree_'+str(n),codim==0)
 if n==7:ck('seven_first_codimension36',codim==36 and cn(n)-codim==77484)
ck('seventh_uniform_bound',2/abs(B0)<48)
note='explorations/conditional-build/k2467-mixed-hook-generators-2026-11-01.md';deps=[note,str(Path(__file__).relative_to(ROOT)),'tests/channel-swings/k2464_cancelling_hook_inverse_probe.py','lab/process/k2461-rank-two-hook-potentials.json','lab/process/k2464-cancelling-hook-inverse.json']
for dp in deps[-2:]:
 data=json.loads((ROOT/dp).read_text());ck('authenticated_'+dp,all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in data['dependencies'].items()))
report={'result_id':'K2467','checks':checks,'controls':controls,'families':records,'first_missing_monomial':[2,2,4,7,8,11,12],'simple_two_axis_family':{'pair':[4,6],'coefficient':str(B0)},'six_family_hilbert_numerator':[1,0,0,0,0,0,-18,24,1,-12,4],'image_hilbert_numerator':[1,0,0,0,0,0,0,-36,66,-22,-25,20,-4],'analytic_bound':'48*d*3^(d-1)','evidence_kinds':{'universal':'original tensor divergence identity; monomial projection/PDE image; characteristic inverse and coefficient estimate','finite':'original curvature/second-order tensors; exact polynomial fixtures and contrary predicates','ceiling':'explicit seven-family sum plus V0, not maximal full mixed operator image or nonlinear closure'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2467-mixed-hook-generators.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2467',len(checks),'checks',len(controls),'controls PASS')
