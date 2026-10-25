"""Exact arrangement vertices for three short-certificate global thermal phases."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,combinations
import json,hashlib,argparse
from k2015_finite_thermal_ray_separation import supports,matrices,vertex,rate
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2037-thermal-seven-level-boundary.json'
A,C=Q(15,28),Q(3,28)
LINES=[(5,Q(15,28),Q(3,28),Q(11,5),Q(19,8)),(7,Q(63,148),Q(9,148),Q(19,8),Q(349,145)),(9,Q(729,1912),Q(81,1912),Q(349,145),Q(1575,653))]
def produce():
 banks={};total=0
 for cutoff in (5,7,9):
  cells=[]
  for ss in supports(cutoff):
   n=len(ss)
   for o in product((-1,1),repeat=n-1):
    ed,df,planes=matrices(ss,o);vs=set()
    for bs in combinations(planes,n-1):
     p=vertex(bs,n)
     if p is not None and all(sum(a*b for a,b in zip(row,p))>=0 for row in ed):vs.add(p)
    assert vs
    rows=[]
    for p in sorted(vs):
     e=sum(x*y for x,y in zip(ss,p));r=rate(ss,p)
     rows.append(dict(p=list(map(str,p)),energy=str(e),value=str(r)));total+=1
    cells.append(dict(s=list(ss),o=list(o),vertices=rows))
  banks[str(cutoff)]=cells
 phases=[]
 for cutoff,A,C,lo,hi in LINES:
  contacts=set()
  for cell in banks[str(cutoff)]:
   for v in cell['vertices']:
    gap=Q(v['value'])+C*Q(v['energy'])-A;assert gap>=0,'supporting line'
    if gap==0:contacts.add(tuple((x,y) for x,y in zip(cell['s'],v['p']) if Q(y)))
  assert len(contacts)==2,contacts
  ends=sorted(contacts,key=lambda q:sum(Q(x)*Q(y) for x,y in q));assert [sum(Q(x)*Q(y) for x,y in q) for q in ends]==[lo,hi]
  ss=sorted({x for q in ends for x,y in q});pp=[[dict(q).get(x,'0') for x in ss] for q in ends]
  witnesses=[]
  for t in [Q(0),Q(1,2),Q(1)]:
   pv=[(1-t)*Q(x)+t*Q(y) for x,y in zip(*pp)];e=(1-t)*lo+t*hi;rv=rate(ss,pv);assert rv==A-C*e,(cutoff,A,C,t,rv,A-C*e)
   witnesses.append(dict(energy=str(e),support=ss,population=list(map(str,pv)),spectrum=list(range(max(x for x,y in zip(ss,pv) if y)+2)),return_value=str(rv)))
  assert C*(cutoff+1)-A>0
  phases.append(dict(cutoff=cutoff,intercept=str(A),slope=str(C),phase=[str(lo),str(hi)],tail_gap=str(C*(cutoff+1)-A),contacts=[list(x) for x in ends],witnesses=witnesses))
 lower=(Q(1053,2768),Q(2907,69200));failed_ends=[{1:Q(243,653),3:Q(729,1306),5:Q(81,1306),7:Q(9,1306),9:Q(1,1306)},{1:Q(36,181),3:Q(54,181),5:Q(81,181),7:Q(9,181),9:Q(1,181)}]
 for cell in banks['9']:
  for v in cell['vertices']:assert Q(v['value'])+lower[1]*Q(v['energy'])>=lower[0]
 mid=[(failed_ends[0][x]+failed_ends[1][x])/2 for x in [1,3,5,7,9]];me=sum(x*y for x,y in zip([1,3,5,7,9],mid));actual=rate([1,3,5,7,9],mid);bound=lower[0]-lower[1]*me;assert actual>bound
 family=[]
 for m in range(1,13):
  weights=[Q(1)]+[Q(3,2*9**j) for j in range(m+1)];ss=list(range(1,2*len(weights),2));pv=[x/sum(weights) for x in weights];e=sum(x*y for x,y in zip(ss,pv));rr=rate(ss,pv);assert rr==pv[1]/2;family.append(dict(tail=m,energy=str(e),value=str(rr),physical_dimension=ss[-1]+2))
 assert all(Q(b['energy'])>Q(a['energy']) and Q(b['value'])<Q(a['value']) for a,b in zip(family,family[1:]))
 inputs=['lab/process/k2020-posttransition-tail-and-resources.json','lab/process/k2035-thermal-five-level-phase.json','tests/channel-swings/k2015_finite_thermal_ray_separation.py']
 return dict(result_id='K2037',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',banks=banks,phases=phases,vertex_records=total,supporting_gap=dict(intercept=str(lower[0]),slope=str(lower[1]),energy=str(me),midpoint_actual=str(actual),midpoint_bound=str(bound),gap=str(actual-bound)),tail_family=family,tail_limit=dict(energy='415/172',value='12/43',status='feasible countable upper bound; optimality unproved'),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},scope='Three exact global phases for all positive spacing at most1; arbitrary finite/countable spectra under the inherited bath/channel class. Unique diagonal, not coherences or unitaries. No GU prediction.')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=produce()
 if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2037',len(r['phases']),'phases',r['vertex_records'],'vertices')
