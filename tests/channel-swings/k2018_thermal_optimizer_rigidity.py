"""Complete equality events for the reused cutoff-nine cone census."""
import json,hashlib,argparse
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from k2015_finite_thermal_ray_separation import matrices
from k2017_sharp_unrestricted_thermal_transition import encode,sharp
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2018-thermal-optimizer-rigidity.json'
D=Q(4,15);A=Q(6,5);Z=Q(11,5);M=Q(17,10);L=Q(3,20);EC=Q(113,91)
def shells(spectrum,support):
    return all(sum(x+b==e for x in spectrum for b in range(4))>=2*sum(x+b==e for x in support for b in range(4)) for e in {x+b for x in support for b in range(4)})
def minimum_completion(s):
    candidates=range(max(s)+4);good=[];tested=0
    for n in range(len(candidates)+1):
      for aa in combinations(candidates,n):
       if not set(s).issubset(aa) or 0 not in aa:continue
       tested+=1
       if shells(aa,s):good.append(aa)
      if good:return n,good,tested
    raise AssertionError('no completion')
def produce():
 c=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census']
 zero={};counts={};bad=[]
 def check(kind,cs,num,ref):
  lo,hi=Q(0),D
  for a,b in cs:
   if b>0:lo=max(lo,-a/b)
   elif b<0:hi=min(hi,-a/b)
   elif a<0:return
  if lo>hi:return
  counts[kind]=counts.get(kind,0)+1
  assert all(num[0]+num[1]*d>=0 for d in [lo,hi])
  ds=[lo,hi]
  if num[0]==0 and num[1]==0 and lo<hi:ds.append((lo+hi)/2)
  for d in set(ds):
   if d>0 and num[0]+num[1]*d==0:
    if kind.startswith('single'):
     e,R,b=ref
     if not A<e+b*d<Z:continue
    zero.setdefault(kind,[]).append((str(d),str(lo),str(hi),list(map(str,ref))))
 def single(e,R,b):
  common=[(e-A,b),(Z-e,-b)]
  check('single_B',common+[(M-e,Q(1,2)-b)],(R-Q(9,20)+L*(e-A),R-Q(9,20)+L*b),(e,R,b))
  check('single_A',common+[(e-M,b-Q(1,2))],(R-Q(3,10)-L*(Z-e),-(R-Q(3,10))+L*b),(e,R,b))
 def pair(e,R,b,f,S,k,kind,ref):
  cs=[(M-e,Q(1,2)-b),(f-M,k-Q(1,2))]
  num=(R*(f-M)+S*(M-e)-Q(3,8)*(f-e),R*(k-Q(1,2))+S*(Q(1,2)-b)-Q(3,8)*(k-b))
  check(kind,cs,num,ref)
 rs=sorted({(Q(v['energy']),Q(v['return'])) for cell in c['cells'] for v in cell['vertices']})
 for e,R in rs:
  for b in [0,1]:single(e,R,b)
 for i,(e,R) in enumerate(rs):
  for j,(f,S) in enumerate(rs):
   if e<=M+D/2 and f+D>=M:pair(e,R,0,f,S,1,'separated',(e,R,0,f,S,1))
   if f<=M+D/2 and e+D>=M:pair(f,S,1,e,R,0,'separated',(f,S,1,e,R,0))
 for ci,cell in enumerate(c['cells']):
  _,de,_=matrices(cell['support'],cell['orientation']);vs=cell['vertices'];signs=[[sum(Q(x)*Q(y) for x,y in zip(row,v['p'])) for row in de] for v in vs]
  for i,j in combinations(range(len(vs)),2):
   if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
   e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
   if e>f:e,f,R,S=f,e,S,R
   if e<=M+D/2 and f>=M:pair(e,R,0,f,S,0,'same_cone',(e,R,0,f,S,0))
 assert counts=={'single_B':337,'single_A':83,'separated':194017,'same_cone':4818}
 # Every positive-spacing equality event is either a persistent A/B chord,
 # the endpoint C ray, or the endpoint C/B-shift chord.
 contacts={k:sorted(set((d,lo,hi,tuple(ref)) for d,lo,hi,ref in rows)) for k,rows in zero.items()}
 assert set(contacts)=={'single_B','separated'}
 assert contacts['single_B']==[('4/15','0','4/15',('113/91','81/182','0'))]
 AB={(str(A),'9/20','0',str(Z),'3/10','1'),(str(A),'9/20','1',str(Z),'3/10','0')}
 CB=('113/91','81/182','0',str(Z),'3/10','1')
 for d,lo,hi,ref in contacts['separated']:
  assert ref in AB or (Q(d)==D and ref==CB)
 assert len(contacts['separated'])==5
 # Energy-return projection does not hide a different preparation.
 known={(A,Q(9,20)):((1,Q(9,10)),(3,Q(1,10))), (Z,Q(3,10)):((1,Q(2,5)),(3,Q(3,5))), (EC,Q(81,182)):((1,Q(81,91)),(3,Q(9,91)),(5,Q(1,91)))}
 matches={x:set() for x in known}
 for cell in c['cells']:
  for v in cell['vertices']:
   key=(Q(v['energy']),Q(v['return']))
   if key in known:matches[key].add(tuple((s,Q(p)) for s,p in zip(cell['support'],v['p']) if Q(p)))
 for key in known:assert matches[key]=={known[key]}
 # A and C share the actual oriented deficit cone on support 1,3,5.
 _,df,_=matrices([1,3,5],[1,1]);pa=[Q(9,10),Q(1,10),Q(0)];pc=[Q(81,91),Q(9,91),Q(1,91)]
 assert all(sum(x*y for x,y in zip(row,pa))*sum(x*y for x,y in zip(row,pc))>=0 for row in df)
 seven=[]
 from k2014_unrestricted_ten_level_onset import G
 for k in range(1,21):
  w=Q(k,20);p=[(1-w)*x+w*y for x,y in zip(pa,pc)];E=(1-w)*A+w*EC;rv=sharp([Q(1),Q(3),Q(5)],p,Q(1,2))
  assert rv==G(D,E) and shells(list(range(7)),[1,3,5])
  seven.append(dict(energy=E,populations=p,return_value=rv,spectrum=list(range(7))))
 completions=[]
 for s in [[1,3],[1,3,5]]:
  n,aa,tested=minimum_completion(s);assert n==(5 if len(s)==2 else 7)
  completions.append(dict(support=s,minimum=n,minimal_completions=aa,candidates_tested=tested))
 above=[]
 for delta in [Q(4,15)+Q(1,10000),Q(3,10),Q(2,5),Q(1,2)]:
  cross=Z-440*delta*(1-delta)/(895*delta-4)
  assert M+delta/2<cross<Z
  for E in [A+(EC-A)/2,EC,EC+(cross-EC)/2,cross,(cross+Z)/2]:
   if E<=EC:
    theta=(E-A)/(EC-A);ss=[Q(1),Q(3),Q(5)];pp=[(1-theta)*x+theta*y for x,y in zip(pa,pc)];aa=list(map(Q,range(7)));kind='seven'
   else:
    theta=(E-EC)/(Z+delta-EC);pairs=sorted([(Q(x),(1-theta)*p) for x,p in zip([1,3,5],pc)]+[(1+delta,theta*Q(2,5)),(3+delta,theta*Q(3,5))]);ss=[x for x,p in pairs];pp=[p for x,p in pairs];aa=sorted(list(map(Q,range(7)))+[Q(i)+delta for i in range(5)]);kind='twelve'
   rv=sharp(ss,pp,Q(1,2));assert shells(aa,ss) and sum(pp)==1 and sum(x*y for x,y in zip(ss,pp))==E and min(y-x for x,y in zip(aa,aa[1:]))>=delta
   assert (rv<G(delta,E))==(E<cross)
   assert (rv==G(delta,E))==(E==cross)
   above.append(dict(delta=delta,energy=E,crossing_energy=cross,kind=kind,spectrum=aa,support=ss,populations=pp,return_value=rv,two_ladder_return=G(delta,E)))
 inputs=['lab/process/k2015-finite-thermal-ray-separation.json','lab/process/k2017-sharp-unrestricted-thermal-transition.json']
 return encode(dict(result_id='K2018',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',equality_interval_counts=counts,positive_spacing_contacts=contacts,endpoint_energy=EC,above_transition_witnesses=above,endpoint_seven_level_witnesses=seven,physical_minimum_completions=completions,minimum_dimension={'strict_window':'10 for 0<delta<4/15 and6/5<E<11/5','endpoint_low_energy':'7 at delta=4/15 and6/5<E<=113/91','endpoint_upper_energy':'10 at delta=4/15 and113/91<E<11/5'},scope='Physical minimal dimensions and optimal lifted-ray contacts; not classification of every unitary, optional unused level or coherent state.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K2018',r['equality_interval_counts'],'contacts',sum(map(len,r['positive_spacing_contacts'].values())),'physical seven-level witnesses',len(r['endpoint_seven_level_witnesses']))
