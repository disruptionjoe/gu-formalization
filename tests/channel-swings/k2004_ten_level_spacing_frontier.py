"""Exact ten-level small-spacing programs and global fixed-budget threshold."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product,combinations,permutations
import argparse,json,hashlib
import k1968_joint_thermal_finite_dimension_program as k
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2004-ten-level-spacing-frontier.json'
TYPES=[((1,3),tuple(range(5))),((2,3),tuple(range(6))),((1,4),tuple(range(6))),((1,3,5),tuple(range(7)))]

def small_census():
 rows=[]
 for n in [5,6,7]:
  for gaps in product((1,2,3),repeat=n-1):
   A=[0]
   for g in gaps:A.append(A[-1]+g)
   for m in range(2,(n-1)//2+1):
    for S in combinations(A[1:-1],m):
     if not any(b-a<=3 for a,b in zip(S,S[1:])) or not k.shells(A,S):continue
     options=[]
     for T,B in TYPES:
      if len(T)!=len(S) or len(B)>n or any(t>s for t,s in zip(T,S)):continue
      if all(T[j]-T[i]==S[j]-S[i] for i,j in combinations(range(m),2) if S[j]-S[i]<=3):options.append((T,B))
     assert options,(A,S)
     T,B=min(options,key=lambda z:(len(z[1]),z[0]))
     rows.append(dict(spectrum=A,support=S,target_spectrum=B,target_support=T))
 return rows

def connected_reduction(bs):
 """All-temperature incoming-edge dominance, with a direct map per input."""
 kept=[];witnesses=[]
 for ix in sorted(range(len(bs)),key=lambda i:(sum(bs[i][0]),len(bs[i][1]))):
  S,A=bs[ix];hits=[]
  for j in kept:
   T,B=bs[j]
   if len(T)==len(S) and len(B)<=len(A) and all(t<=s for t,s in zip(T,S)) and all(T[v]-T[u]==S[v]-S[u] for u,v in combinations(range(len(S)),2) if S[v]-S[u]<=3):hits.append(j)
  if hits:witnesses.append(dict(source_index=ix,target_index=hits[0]))
  else:kept.append(ix)
 return kept,witnesses

def physical_templates(delta):
 out=[]
 for S,A in TYPES:
  for side in [0,1]:
   x,y=(delta,F(0)) if side else(F(0),delta)
   out.append([(tuple(x+s for s in S),tuple(x+a for a in A)),((y+1,),(y,y+1,y+2))])
 out.append([(tuple(F(s) for s in TYPES[0][0]),tuple(F(a) for a in TYPES[0][1])),(tuple(delta+s for s in TYPES[0][0]),tuple(delta+a for a in TYPES[0][1]))])
 return out

def exact_cell_hull_segments(d,bs):
 """Project every exact cell, certify its lower hull, retain only exposed edges."""
 segments={};pc=cc=vc=hc=0
 for pat in k.patterns(d,bs):
  sites,edges,_,_=k.equations(pat,bs,());pc+=1
  for orient in product((-1,1),repeat=len(edges)):
   sites,edges,rows,deficit=k.equations(pat,bs,orient)
   for signs in product((-1,1),repeat=len(sites)):
    vs=k.cell_vertices(sites,rows,deficit,signs);cc+=1;vc+=len(vs);points={}
    for p in vs:
     e=k.dot([e for tag,e in sites],p);r=k.rate(sites,p)
     assert r==sum(max(k.dot(row,p),0) for row in deficit)/2
     if e not in points or r<points[e][0]:points[e]=(r,p)
    pts=sorted((e,r,p) for e,(r,p) in points.items());hull=[]
    for q in pts:
     while len(hull)>=2:
      a,b=hull[-2:]
      if (b[0]-a[0])*(q[1]-a[1])-(b[1]-a[1])*(q[0]-a[0])>0:break
      hull.pop()
     hull.append(q)
    if not hull:continue
    assert hull[0][0]==pts[0][0] and hull[-1][0]==pts[-1][0]
    assert all(a[0]<b[0] for a,b in zip(hull,hull[1:]))
    for e,r,p in hull:segments.setdefault((e,None,F(0),r),dict(pattern=pat,p0=p,p1=p))
    for a,b in zip(hull,hull[1:]):
     e0,r0,p0=a;e1,r1,p1=b;m=(r1-r0)/(e1-e0);q=r0-m*e0
     for ee,rr,pp in pts:assert rr>=m*ee+q;hc+=1
     segments.setdefault((e0,e1,m,q),dict(pattern=pat,p0=p0,p1=p1))
 return segments,dict(patterns=pc,cells=cc,vertices=vc,hull_supporting_line_checks=hc)

def mixed_segments(delta):
 old=k.patterns;old_rates=k.rates;k.patterns=lambda d,b:[(0,1)]
 def integer_rates(g):
  assert F(g).denominator==1 and 1<=g<=3
  return old_rates(int(g))
 k.rates=integer_rates
 try:
  seg={};info=[]
  for bs in physical_templates(delta):
   A=sorted(a for S,C in bs for a in C);S=sorted(s for T,C in bs for s in T)
   assert len(A)<=10 and min(b-a for a,b in zip(A,A[1:]))>=delta and k.shells(A,S)
   ss,cc=exact_cell_hull_segments(10,bs);seg.update(ss)
   info.append(dict(spectrum=A,support=S,counts=cc))
  return seg,info
 finally:k.patterns=old;k.rates=old_rates

def parametric_mixed():
 """Cell vertices independent of spacing; retain their component offset mass."""
 ans=set()
 for ti in range(9):
  if ti<8:
   bs=[TYPES[ti//2],((1,),(0,1,2))];shifted=0 if ti%2 else 1
  else:bs=[TYPES[0],TYPES[0]];shifted=1
  pat=(0,1);sites,edges,_,_=k.equations(pat,bs,())
  for orient in product((-1,1),repeat=len(edges)):
   sites,edges,rows,deficit=k.equations(pat,bs,orient)
   for signs in product((-1,1),repeat=len(sites)):
    vs=k.cell_vertices(sites,rows,deficit,signs)
    pts={(k.dot([e for tag,e in sites],p),sum(q for q,(tag,e) in zip(p,sites) if tag==shifted),k.rate(sites,p)) for p in vs}
    for a in pts:ans.add((a,a))
    for a,b in combinations(sorted(pts),2):ans.add((a,b))
 return sorted(ans)

def wide_witnesses(rows,bs,kept):
 def first_shift(A,B):
  x=F(0);delta=F(3,4)
  for z in sorted({F(a-b) for a in A for b in B}):
   if z-delta<x<z+delta:x=z+delta
  assert all(abs(a-b-x)>=delta for a in A for b in B)
  return int(x-delta)
 cases=[]
 for row in rows:
  for l in range(1,4):
   for h in range(1,4):
    if l+h>4:continue
    for side in [0,1]:cases.append((row['spectrum'],row['support'],(0,l,l+h),(l,),side))
 cases.append((tuple(range(5)),(1,3),tuple(range(5)),(1,3),0))
 out=[]
 for A,S,B,U,side in cases:
  n=first_shift(B,A) if side else first_shift(A,B)
  aa=n+F(1,2) if side else F(0);bb=F(0) if side else n+F(1,2)
  energies=[aa+u for u in S]+[bb+u for u in U]
  edges=[(i,j,S[j]-S[i]) for i,j in combinations(range(len(S)),2) if S[j]-S[i]<=3]
  edges += [(len(S)+i,len(S)+j,U[j]-U[i]) for i,j in combinations(range(len(U)),2) if U[j]-U[i]<=3]
  incident={i for e in edges for i in e[:2]};isolated=[i for i in range(len(energies)) if i not in incident]
  groups=[[i] for i in range(len(energies))]
  if len(isolated)>=2:groups=[[i] for i in range(len(energies)) if i in incident]+[isolated]
  hit=None
  for ix in kept:
   V,C=bs[ix]
   if len(V)!=len(groups):continue
   for pi in permutations(range(len(V))):
    mapping=[None]*len(energies)
    for group,j in zip(groups,pi):
     for i in group:mapping[i]=j
    if all(V[mapping[i]]<=energies[i] for i in range(len(energies))) and all(V[mapping[j]]-V[mapping[i]]==g for i,j,g in edges):hit=(ix,mapping);break
   if hit:break
  assert hit,('wide replacement unavailable even after isolated-mass merge',A,S,B,U,side,n)
  out.append(dict(A=A,S=S,B=B,U=U,shifted='A' if side else 'B',shift_integer=n,target_index=hit[0],support_map=hit[1],isolated_source_indices=isolated))
 return out

def threshold(connected_curve,param,E):
 """Prove each candidate dominates a physical two-branch benchmark.

 Partition each candidate separately at all exact feasibility, denominator
 and benchmark-crossing roots; check every interval and positive endpoint.
 This has the same full coverage as the common refinement without its cost.
 """
 import sympy as s
 from functools import cmp_to_key
 z=s.symbols('z');rr=E-F(6,5)
 if E==F(3,2):pred=s.Rational(9,20)-s.Rational(3,20)*s.Rational(rr)/(1+z);family='B shifted'
 elif E==F(2):pred=s.Rational(63,100)-s.Rational(3,20)*s.Rational(E)+s.Rational(3,20)*s.Rational(1-rr)*z/(1-z);family='A shifted'
 else:raise ValueError('fixed budgets only')
 cv=s.Rational(k.evaluate(connected_curve,E));candidates=[((E,F(0),F(cv)),(E,F(0),F(cv)))]+param
 def roots(expr):
  num=s.fraction(s.cancel(expr))[0]
  return [] if num==0 else [q for q in s.solve(num,z) if q.is_real and bool(q>0) and bool(q<s.Rational(1,2))]
 def cmp(a,b):
  d=s.simplify(a-b)
  return 0 if d==0 else(-1 if bool(d<0) else 1)
 def ordered(xs):
  ans=sorted(set(xs),key=cmp_to_key(cmp));assert all(bool(a<b) for a,b in zip(ans,ans[1:]));return ans
 base=ordered([s.Rational(0),s.Rational(1,2)]+roots(pred-cv));checks=0;partitions=0;allroots=set(base)
 # Identical formulas and energy ranges still represent different cells, but
 # duplicating an exact scalar comparison is unnecessary.
 seen=set()
 for a,b in candidates:
  e0,c0,r0=map(s.Rational,a);e1,c1,r1=map(s.Rational,b)
  x=e0+c0*z;y=e1+c1*z
  if a==b:val=r0
  elif x==y:continue # All endpoint point-candidates are also enumerated.
  else:val=s.cancel((r0*(y-s.Rational(E))+r1*(s.Rational(E)-x))/(y-x))
  key=(x,y,val,a==b)
  if key in seen:continue
  seen.add(key)
  cuts=ordered(base+roots(x-s.Rational(E))+roots(y-s.Rational(E))+roots(y-x)+roots(val-pred)+roots(val-cv))
  allroots.update(cuts);partitions+=1
  samples=[q for q in cuts if q>0]+[(l+h)/2 for l,h in zip(cuts,cuts[1:])]
  for q in samples:
   xx=s.simplify(x.subs(z,q));yy=s.simplify(y.subs(z,q))
   if a==b:feasible=bool(xx<=s.Rational(E))
   else:feasible=(xx!=yy and bool(min(xx,yy)<=s.Rational(E)) and bool(s.Rational(E)<=max(xx,yy)))
   if not feasible:continue
   v=s.simplify(val.subs(z,q));bench=min(s.simplify(pred.subs(z,q)),cv)
   assert v.is_finite and bool(s.simplify(v-bench)>=0),('third branch',E,q,v,bench,a,b)
   checks+=1
 pieces=[];pointvals=[];first_failure=None
 for j,q in enumerate(base):
  if q>0:
   v=min(s.simplify(pred.subs(z,q)),cv);gap=s.simplify(v-pred.subs(z,q))
   pointvals.append(dict(spacing=str(q),value=str(v),target_gap=str(gap)))
  if j+1==len(base):break
  h=base[j+1];mid=(q+h)/2;form=pred if pred.subs(z,mid)<=cv else cv
  if form==cv and s.cancel(cv-pred)!=0 and first_failure is None:first_failure=q
  if pieces and pieces[-1]['formula']==str(form):pieces[-1]['hi']=str(h)
  else:pieces.append(dict(lo=str(q),hi=str(h),formula=str(form)))
 eta=s.Rational(1,2) if first_failure is None else first_failure
 return dict(energy=str(E),exact_threshold=str(eta),threshold_included=bool(min(pred.subs(z,eta),cv)==pred.subs(z,eta)),family=family,formula=str(pred),candidate_count=len(candidates),distinct_candidate_partitions=partitions,exact_cells_checked=checks,all_boundary_roots=[str(b) for b in ordered(allroots)],spacing_curve=pieces,boundary_values=pointvals,scope='Every feasible vertex/segment dominates min(shifted face, exact connected optimum), certified by exact per-candidate algebraic partition, all positive boundaries and degenerate point candidates.')

def produce(checkpoint=None):
 # Only linear rows determine normalized cell vertices. Sharing identical
 # immutable row problems across spectra avoids repeated exact elimination.
 vertex_cache={};pool_cache={}
 def memo_vertices(sites,rows,deficit,signs):
  # Changing a homogeneous inequality's sign never changes its zero plane.
  # Enumerate vertex intersections once per edge orientation, then classify
  # those same exact rational vertices into each deficit sign cell.
  n=len(sites);base=(n,tuple(tuple(r) for r in rows),tuple(tuple(r) for r in deficit))
  key=base+(tuple(signs),)
  if key not in vertex_cache:
   if base not in pool_cache:
    normals=[[F(int(i==j)) for j in range(n)] for i in range(n)]+rows+deficit
    pool=set()
    for active in combinations(normals,n-1):
     p=k.solve([[F(1)]*n]+list(active),[F(1)]+[F(0)]*(n-1))
     if p is not None and min(p)>=0 and all(k.dot(r,p)>=0 for r in rows):pool.add(p)
    pool_cache[base]=pool
   vertex_cache[key]={p for p in pool_cache[base] if all(sgn*k.dot(r,p)>=0 for sgn,r in zip(signs,deficit))}
  return vertex_cache[key]
 k.cell_vertices=memo_vertices
 rows=small_census();print('small census',len(rows),flush=True)
 bs,census,raw=k.blocks(10);print('connected census',census,raw,len(bs),flush=True)
 kept,dominance=connected_reduction(bs);assert len(kept)==18 and len(dominance)==294
 print('exact connected reduction',len(bs),'to',len(kept),flush=True)
 op=k.patterns;k.patterns=lambda d,b:((i,) for i in range(len(b)))
 try:conn,count=exact_cell_hull_segments(10,[bs[i] for i in kept])
 finally:k.patterns=op
 connected=k.envelope(conn);print('connected curve',len(connected),count,flush=True)
 mixed,templates=mixed_segments(F(1,20));full=k.envelope(conn|mixed);print('full curve',len(full),flush=True)
 if checkpoint:Path(checkpoint).write_text(json.dumps(k.encode(dict(rows=rows,bs=bs,census=census,raw=raw,kept=kept,dominance=dominance,connected=connected,count=count,full=full,templates=templates)),indent=2)+'\n')
 wide=wide_witnesses(rows,bs,kept);print('wide witnesses',len(wide),flush=True)
 half_mixed,half_templates=mixed_segments(F(1,2));half=k.envelope(conn|half_mixed)
 param=parametric_mixed();th=[threshold(connected,param,E) for E in [F(3,2),F(2)]];print('thresholds',[(r['energy'],r['exact_threshold']) for r in th],flush=True)
 return dict(result_id='K2004',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',small_component_witnesses=rows,connected_shape_count=census,raw_support_count=raw,pareto_blocks=[dict(S=S,A=A) for S,A in bs],connected_core_indices=kept,connected_dominance=dominance,connected_counts=count,connected_curve=connected,spacing='1/20',temperature='1/2',small_spacing_curve=full,shifted_templates=templates,parametric_mixed_segments=param,thresholds=th,wide_dominance_witnesses=wide,injective_only_failed_witness=dict(A=[0,1,4,5,6,7,8],S=[1,5,7],B=[0,1,4],U=[1],shifted='A',shift_integer=1,disposition='Isolated source populations at positions0 and3 merge into one distinct target node; no mass merges into an old edge endpoint.'),half_spacing_curve=half,budget_controls=[dict(E=str(e),value=str(k.evaluate(full,e)),connected=str(k.evaluate(connected,e))) for e in [F(6,5),F(7,5),F(3,2),F(17,10),F(2),F(11,5),F(3),F(5)]],scope='For every0<t<1,0<delta<=1/2,E>=1 exact d10 reduction to connected integer templates and nine shifted templates. Complete t1/2 delta1/20 budget curve and fixed E3/2 and E2 complete spacing curves computed. Wide-spacing rigidity for1/2<delta<=1 is certified by all raw placements; no all-d claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1968_joint_thermal_finite_dimension_program.py','lab/process/k1994-nine-level-thermal-reduction.json','explorations/conditional-build/k1998-uniform-small-spacing-transfer-2026-10-23.md']})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--checkpoint');a=ap.parse_args();d=k.encode(produce(a.checkpoint))
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert d==json.loads(OUT.read_text())
 print('PASS K2004',d['budget_controls'])
