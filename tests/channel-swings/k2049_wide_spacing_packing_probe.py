"""Direct shell return, support-line and completion replay; no hull import."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,copy
from k2045_third_thermal_spacing_phase_probe import physical,common_return_cell
ROOT=Path(__file__).resolve().parents[2]
def replay(r,physical_bank=True):
 bank=json.loads((ROOT/r['bank_ref']).read_text())['bank'];assert hashlib.sha256((ROOT/r['bank_ref']).read_bytes()).hexdigest()==r['bank_sha256']
 vals=[];n=0
 for c in bank:
  vs=[]
  for v in c['vertices']:
   e,ret=F(v['energy']),F(v['value'])
   if physical_bank:assert physical(list(map(F,c['s'])),list(map(F,v['p'])),list(map(F,range(15))),F(1))==(e,ret),'direct bath vertex'
   vs.append((e,ret));n+=1
  vals.append(vs)
 unique=set()
 for piece in r['pieces']:
  lo,hi=map(F,piece['interval']);a,s=map(F,piece['line']);assert len(piece['assignments'])==len(vals)
  for vs,line in zip(vals,piece['assignments']):
   A,S=map(F,line);assert S<0 and A+12*S<=0,'tail support'
   assert all(ret>=A+S*e for e,ret in vs),'low cell support'
   assert all(A+S*e>=a+s*e for e in [lo,hi]),'whole interval order';unique.add((A,S))
  zeros=set()
  for c,vs in zip(bank,vals):
   if all(ret>=a+s*e for e,ret in vs):
    for v in c['vertices']:
     if F(v['value'])==a+s*F(v['energy']):zeros.add(tuple((x,str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)))
  assert sorted(zeros)==sorted(tuple(tuple(x) for x in v) for v in piece['low_equality_vertices']),'complete equality vertices'
  assert all(ret>a+s*(e+1) for vs in vals for e,ret in vs),'strict high equality exclusion'
 for a,s in unique:
  assert all(ret>=a+s*(e+1) for vs in vals for e,ret in vs),'high shift support'
  assert a+13*s<=0,'high tail support'
 pop={k:list(map(F,v)) for k,v in r['populations'].items()};ep={};removed=0;controls=0
 for name,p in pop.items():
  ss=list(map(F,range(1,2*len(p),2)));spec=list(map(F,range(2*len(p)+1)));ep[name]=physical(ss,p,spec,F(1))
  for x in spec:
   try:physical(ss,p,[y for y in spec if y!=x],F(1))
   except AssertionError as ex:assert str(ex) in ['shell capacity','spectrum'];removed+=1
   else:raise AssertionError('completion not necessary')
 for piece in r['pieces']:
  n,m=piece['name'];p,q=pop[n],pop[m];p=p+[F(0)]*(len(q)-len(p));ss=list(map(F,range(1,2*len(q),2)));spec=list(map(F,range(2*len(q)+1)));common_return_cell(ss,p,q)
  a,s=map(F,piece['line'])
  for mass in [F(0),F(1,11),F(1,2),F(10,11),F(1)]:
   pp=[(1-mass)*x+mass*y for x,y in zip(p,q)]
   for delta in [F(501,1000),F(3,4),F(1)]:
    e,v=physical(ss,pp,spec,delta);assert v==a+s*e,'actual attainment';controls+=1
 # Same fractional offset grounds necessarily merge; distinct offsets below1 cannot pack.
 for diff in [F(1,100),F(1,3),F(1,2),F(2,3),F(99,100)]:
  spec=sorted([F(0),F(1),diff,diff+1]);assert min(y-x for x,y in zip(spec,spec[1:]))<=F(1,2),'ground-pair packing'
 jump=r['jump_at_energy_7_over_2'];above=F(67,280);half=F(21,88)
 assert F(jump['above_half'])==above and F(jump['half_spacing'])==half and F(jump['jump'])==above-half,'jump arithmetic'
 return dict(vertex_records=sum(map(len,vals)),unique_support_lines=len(unique),physical_controls=controls,completion_removals=removed,whole_common_cell_segments=3,ground_pair_controls=5)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2049-wide-spacing-packing.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r),flush=True);faults=[]
 for kind in ['low','high','population','jump']:
  bad=copy.deepcopy(r)
  if kind=='low':bad['pieces'][0]['assignments'][0][0]='100'
  if kind=='high':bad['pieces'][0]['line'][1]='0'
  if kind=='population':bad['populations']['R'][0]='5/19'
  if kind=='jump':bad['jump_at_energy_7_over_2']['jump']='1/1541'
  try:replay(bad,False)
  except AssertionError as e:assert str(e);faults.append([kind,str(e)])
  else:raise AssertionError('missed '+kind)
 print('PASS four faults',faults)
