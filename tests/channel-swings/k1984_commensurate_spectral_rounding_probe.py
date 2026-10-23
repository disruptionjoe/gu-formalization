"""Independent shell partition and rational-template checks."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product,combinations
from pathlib import Path
import json,hashlib
from k1950_global_catalyst_energy_certificates_probe import shell_return
ROOT=Path(__file__).resolve().parents[2]
def shells(spec,bath):
 d=defaultdict(set)
 for i,e in enumerate(spec):
  for j,b in enumerate(bath):d[e+b].add((i,j))
 return list(d.values())
def refines(old,new):return all(any(s<=t for t in new) for s in old)
def check(fault=None):
 r=json.loads((ROOT/'lab/process/k1984-commensurate-spectral-rounding.json').read_text());bath=list(map(F,range(4)));n=0
 for case in r['physical_families']:
  orig=list(map(F,case['original']));h=F(case['h']);q=[h*(v.numerator//(v.denominator*h)) for v in orig]
  if fault=='upward':q=[-h*((-v)//h) for v in orig]
  if fault=='collision':q=[2*h*(v//(2*h)) for v in orig]
  cap=F(2) if fault=='gap_cap' else F(3)
  c=[F(0)]
  for a,b in zip(q,q[1:]):c.append(c[-1]+min(cap,b-a))
  assert all(a<=b for a,b in zip(q,orig)),'energy nonincrease'
  assert len(set(q))==len(orig),'no level collision'
  assert q==list(map(F,case['rounded'])),'floor and exact original energies'
  assert refines(shells(orig,bath),shells(q,bath)) and refines(shells(q,bath),shells(c,bath)),'all old unitary blocks remain conserving'
  assert refines(shells([F(0),F(3),F(6)],bath),shells([F(0),min(cap,F(3)),2*min(cap,F(3))],bath)),'range3 transition retention'
  assert c==list(map(F,case['compressed'])),'compressed physical spectrum'
  assert all((v/h).denominator==1 for v in c) and min(b-a for a,b in zip(c,c[1:]))>=h
  n+=6
 # Complete h=1, at-most-five-level physical support census, a check of template reuse.
 pairs=[];shapes=0
 for dim in range(2,6):
  for gaps in product([1,2,3],repeat=dim-1):
   spec=[F(0)]
   for gap in gaps:spec.append(spec[-1]+gap)
   sh=shells(spec,bath);shapes+=1
   for size in range(2,dim+1):
    for sup in combinations(range(dim),size):
     if all(len(b)>=2*sum(i in sup for i,j in b) for b in sh):pairs.append((list(map(int,spec)),sup))
 assert len(pairs)==16 and all(sup==(1,3) for spec,sup in pairs),'complete support census'
 improving=[(spec,sup) for spec,sup in pairs if spec[sup[1]]-spec[sup[0]]<=3]
 assert improving==[([0,1,2,3,4],(1,3))],'only overlapping two-support template'
 for case in r['five_level_frontier_controls']:
  t,E,value=map(F,[case['t'],case['energy'],case['optimum']]);q=t*t
  lo=max(F(0),(3-E)/2);a=1/(2*(1+q));b=1/(1+q);c=(2+q)/(2*(1+q))
  def piece(p):
   if p<a:return (1-p)/2
   if p<b:return p/2+q/(2*(1+q))
   if p<c:return c-p/2
   return p/2
  candidates=[lo,F(1)]+[p for p in [a,b,c] if p>=lo]
  assert min(piece(p) for p in candidates)==value,'full scalar cell minimization'
  for p in candidates:assert piece(p)==shell_return(t,[F(1),F(3)],[p,1-p]),'piecewise law versus actual shell return'
  n+=1
 if fault=='bath':
  # Misuse of the rounding lemma on an off-grid bath must fail its conservation obligation.
  s=[F(0),F(3,2)];q=[F(0),F(1)];b=s
  assert refines(shells(s,b),shells(q,b)),'off-grid bath conservation'
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return n,shapes,pairs
if __name__=='__main__':
 n,shapes,pairs=check();caught=[]
 for f in ['upward','collision','gap_cap','bath']:
  try:check(f)
  except AssertionError as e:caught.append((f,str(e)))
  else:raise AssertionError('undetected mathematical fault '+f)
 print('PASS K1984 separate',n,'transition/energy controls;',shapes,'complete integer templates;',pairs,';',caught)
