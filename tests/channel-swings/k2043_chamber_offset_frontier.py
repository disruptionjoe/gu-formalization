"""Whole-interval rational chamber/offset certificates, including first transition."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2043-chamber-offset-frontier.json'
EA,RA=Q(1575,653),Q(729,2612);EB,RB=Q(675,181),Q(81,362);ED,RD=Q(349,145),Q(81,290)
DC,D2=Q(2,181),Q(2,145)
def line(side,phase,d):
 if side=='A':e0,r0,e1,r1=EA,RA,EB+d,RB
 else:e0,r0,e1,r1=(EA if phase==1 else ED)+d,(RA if phase==1 else RD),EB,RB
 slope=(r0-r1)/(e1-e0);return r0+slope*e0,slope

def certify(bank,lo,hi,phase):
 # Denominator-cleared inequalities are affine in d, so endpoints certify intervals.
 labels=[];tail=[]
 for c in bank:
  good=[]
  for side in ['A','B']:
   if all(all(Q(v['value'])+line(side,phase,d)[1]*Q(v['energy'])>=line(side,phase,d)[0] for v in c['vertices']) for d in [lo,hi]):good.append(side)
  assert good,'low component chamber'
  labels.append(''.join(good))
 for d in [lo,hi]:
  for side in ['A','B']:
   a,k=line(side,phase,d);assert k>0
   for c in bank:
    for v in c['vertices']:assert Q(v['value'])+k*(Q(v['energy'])+d)>=a,'high component vertex'
   assert 10*k-a>0,'tail transfer'
   tail.append(str(10*k-a))
 return dict(phase=phase,interval=[str(lo),str(hi)],cell_labels=labels,label_counts={k:labels.count(k) for k in ['A','B','AB']},strict_tail_margins=tail)
def produce():
 path='lab/process/k2037-thermal-seven-level-boundary.json';bank=json.loads((ROOT/path).read_text())['banks']['9']
 certs=[certify(bank,Q(0),DC,1),certify(bank,DC,D2,2)]
 assert (RA-RB)/(EB-EA-DC)==(RD-RB)/(EB-ED-DC)
 EQ,RQ=Q(37,10),Q(9,40)
 assert RB+(RD-RB)*(EB-EQ)/(EB-ED-D2)==RQ
 # First and second physical failure witnesses arbitrarily close to critical spacing.
 witnesses=[]
 for d,phase,e in [(DC+Q(1,10**6),1,(EA+3*EB)/4),(D2+Q(1,10**6),2,EQ)]:
  old=min(a-k*e for a,k in [line('A',phase,d),line('B',phase,d)])
  if phase==1:
   m=(EB-e)/(EB-ED-d);val=RB+m*(RD-RB)
  else:m=Q(1);val=RQ
  assert val<old
  witnesses.append(dict(phase=phase,delta=str(d),energy=str(e),value=str(val),previous_formula=str(old),improvement=str(old-val),shifted_D_mass=str(m)))
 equality=[]
 for phase,lo,hi in [(1,Q(0),DC),(2,DC,D2)]:
  entry={'phase':phase}
  for side in ['A','B']:
   for shifted in [False,True]:
    points=set()
    for c in bank:
     for v in c['vertices']:
      e,r=Q(v['energy']),Q(v['value'])
      if all(r+line(side,phase,d)[1]*(e+(d if shifted else 0))==line(side,phase,d)[0] for d in [lo,hi]):
       points.add(tuple((int(x),str(Q(y))) for x,y in zip(c['s'],v['p']) if Q(y)))
    assert len(points)==1,'unique strict-interval diagonal'
    entry[side+('_high' if shifted else '_low')]=[[list(pair) for pair in p] for p in sorted(points)]
  equality.append(entry)
 # Switch feasibility and slope order are affine after positive denominator clearing.
 for phase,lo,hi in [(1,Q(0),DC),(2,DC,D2)]:
  eu,ru=(EA,RA) if phase==1 else (ED,RD)
  for d in [lo,hi]:
   aa,sa=line('A',phase,d);ab,sb=line('B',phase,d)
   assert sb>=sa and (sb>sa or d==0)
   assert aa-sa*(eu+d)<=ru and ab-sb*EA>=RA
   assert aa-sa*EB>=RB
 inputs=[path,'explorations/conditional-build/k2037-thermal-seven-level-boundary-2026-10-24.md','explorations/conditional-build/k2039-thermal-component-undercut-2026-10-24.md']
 return dict(result_id='K2043',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',first_transition=str(DC),second_phase_endpoint=str(D2),certificates=certs,strict_interval_equalities=equality,records=sum(len(c['vertices']) for c in bank),endpoints={'A':dict(energy=str(EA),value=str(RA),population=['486/1306','729/1306','81/1306','9/1306','1/1306']), 'B':dict(energy=str(EB),value=str(RB),population=['36/181','54/181','81/181','9/181','1/181']), 'D':dict(energy=str(ED),value=str(RD),population=['54/145','81/145','9/145','1/145']), 'Q':dict(energy=str(EQ),value=str(RQ),population=['1/5','3/10','9/20','1/20'])},formula='min(A at0 to B atdelta, low B to shifted A for delta<=2/181 or shifted D for2/181<=delta<=2/145)',resources=dict(phase1_strict_interior=22,phase2_left_branch=22,phase2_right_branch=20,endpoints=11,scope='strict spacing interiors; at first transition right branch admits20 and a continuum of A/D shapes; second critical equality not classified'),witnesses=witnesses,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},scope='Unrestricted finite/countable model on EA<=E<=EB; two exact spacing phases, first phase boundary sharp. No source/physics or novelty conclusion.')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2043',r['records'],'records',[(c['interval'],c['label_counts']) for c in r['certificates']])
