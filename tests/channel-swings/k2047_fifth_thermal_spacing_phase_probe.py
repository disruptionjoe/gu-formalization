"""Direct physical-shell replay of the new interval and equality certificates."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
from k2045_third_thermal_spacing_phase_probe import physical,common_return_cell,P as OLD_P
ROOT=Path(__file__).resolve().parents[2]
P={**OLD_P,'U':[F(x,1630) for x in [324,486,729,81,9,1]],'R':[F(x,19) for x in [4,6,9]]}
def replay(r,physical_bank=True):
 bank=json.loads((ROOT/r['bank_ref']).read_text())['bank'];points=[];records=0
 for c in bank:
  vs=[]
  for v in c['vertices']:
   e,t=map(F,[v['energy'],v['value']])
   if physical_bank:
    x,y=physical(list(map(F,c['s'])),list(map(F,v['p'])),list(map(F,range(15))),F(1));assert (x,y)==(e,t),'physical vertex'
   vs.append((e,t));records+=1
  points.append(vs)
 ep={}
 for n,p in P.items():
  if n not in r['endpoints']:continue
  ep[n]=physical(list(map(F,range(1,2*len(p),2))),p,list(map(F,range(2*len(p)+1))),F(1))
  assert list(map(str,ep[n]))==r['endpoints'][n],'endpoint'
 def coefficients(side,d):
  names={'AT':('A','T'),'TB':('T','B'),'TU':('T','U'),'CQ':('C','Q'),'QB':('Q','B')};n,m=names[side];x,y=ep[n];z,w=ep[m]
  if side in ['TB','TU']:z+=d
  if side=='CQ':x+=d
  assert z>x,'line orientation';slope=(w-y)/(z-x);return y-slope*x,slope
 def value(s,d,e):a,b=coefficients(s,d);return a+b*e
 for phase in r['phases']:
  lo,hi=map(F,phase['interval']);sides=set()
  assert 0<lo<=hi<=F(1,2),'attainment spacing range'
  for pair,labels in phase['assignments'].items():
   assert len(labels)==len(bank),'cell count'
   for vs,ls in zip(points,labels):
    assert ls,'missing low cell'
    for side in ls:
     assert side in pair.split('+');sides.add(side)
     for d in [lo,hi]:assert all(t>=value(side,d,e) for e,t in vs),'low support'
  for side in sides:
   for d in [lo,hi]:
    assert all(t>=value(side,d,e+d) for vs in points for e,t in vs),'high support'
    assert value(side,d,F(12))<0,'tail support'
 def mix(n,m,d,weight):
  p,q=P[n],P[m];ss=[F(k) for k in range(1,2*len(p),2)]+[F(k)+d for k in range(1,2*len(q),2)];pp=[(1-weight)*x for x in p]+[weight*x for x in q];sp=[F(k) for k in range(2*len(p)+1)]+[F(k)+d for k in range(2*len(q)+1)]
  return physical(ss,pp,sp,d)
 count=0
 for d in [F(2,5),F(9,20),F(5652,11755),F(49,100),F(1,2)]:
  for n,m,side in [('T','B','TB'),('T','U','TU'),('Q','C','CQ')]:
   for w in [F(1,10),F(1,2),F(9,10)]:
    e,t=mix(n,m,d,w);assert t==value(side,d,e),'physical mixture';count+=1
 # Critical contact B/U and half-spacing R/Q are actual whole chamber segments.
 for n,m in [('A','T'),('Q','B'),('B','U'),('R','Q')]:
  p=P[n]+[F(0)]*(len(P[m])-len(P[n]));q=P[m];ss=list(range(1,2*len(q),2));common_return_cell(ss,p,q)
  for w in [F(0),F(1,3),F(2,3),F(1)]:
   e,t=physical(list(map(F,ss)),[(1-w)*x+w*y for x,y in zip(p,q)],list(map(F,range(2*len(q)+1))),F(1))
   assert (e,t)==tuple((1-w)*x+w*y for x,y in zip(ep[n],ep[m])),'whole segment';count+=1
 witness=r['boundary_rival'];d=F(witness['delta']);e,t=mix('T','U',d,F(witness['shifted_U_mass']));old=min(max(value('AT',d,e),value('TB',d,e)),max(value('CQ',d,e),value('QB',d,e)))
 assert (str(e),str(t),str(old))==(witness['energy'],witness['value'],witness['previous']) and t<old,'physical boundary rival'
 # Independently extract equality from the same direct bath values.
 for side in ['AT','TB','TU','CQ','QB']:
  ds=[F(41,100),F(47,100)] if side=='TB' else [F(49,100),F(499,1000)]
  for shift in [0,1]:
   eq={tuple((x,str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)) for c,vs in zip(bank,points) for v,(e,t) in zip(c['vertices'],vs) if all(t==value(side,d,e+shift*d) for d in ds)}
   assert [[list(x) for x in z] for z in sorted(eq)]==r['strict_equalities'][side+('_high' if shift else '_low')],'strict equality'
 for shift in [0,1]:
  eq={tuple((x,str(F(p))) for x,p in zip(c['s'],v['p']) if F(p)) for c,vs in zip(bank,points) for v,(e,t) in zip(c['vertices'],vs) if t==value('CQ',F(1,2),e+shift*F(1,2))}
  assert [[list(x) for x in z] for z in sorted(eq)]==r['half_CQ_equalities']['high' if shift else 'low'],'half equality'
 # New contact R and exceptional W do NOT share a chamber with Q/W.
 ss=[1,3,5,7,10,11];w=[F(6,17),F(9,17),F(1,17),F(1,68),F(1,34),F(1,68)]
 for p in [P['Q']+[F(0)]*2,P['R']+[F(0)]*3]:
  try:common_return_cell(ss,w,p)
  except AssertionError as e:assert str(e)=='shared shell maximum'
  else:raise AssertionError('incompatible half cells merged')
 removed=0
 for n in ['C','U','R']:
  p=P[n];ss=list(map(F,range(1,2*len(p),2)));sp=list(map(F,range(2*len(p)+1)))
  for x in sp:
   try:physical(ss,p,[y for y in sp if y!=x],F(1))
   except AssertionError as e:assert str(e)=='shell capacity';removed+=1
   else:raise AssertionError('completion necessity')
 # Half-spacing R/C optimum at7/2 and all fourteen required physical levels.
 d=F(1,2);target=F(7,2);m=(ep['R'][0]-target)/(ep['R'][0]-ep['C'][0]-d)
 e,t=mix('R','C',d,m)
 assert 0<m<1 and e==target and t==value('CQ',d,e)<max(value('AT',d,e),value('TU',d,e)),'half resource witness'
 ss=[F(k) for k in [1,3,5]]+[F(k)+d for k in [1,3,5]];pp=[(1-m)*v for v in P['R']]+[m*v for v in P['C']];sp=[F(k) for k in range(7)]+[F(k)+d for k in range(7)]
 for x in sp:
  try:physical(ss,pp,[y for y in sp if y!=x],d)
  except AssertionError as er:assert str(er)=='shell capacity';removed+=1
  else:raise AssertionError('half completion necessity')
 count+=1
 # Above half the interlaced construction is impossible; a failed construction is not a global phase proof.
 try:mix('Q','C',F(501,1000),F(1,2))
 except AssertionError as e:assert str(e)=='spacing'
 else:raise AssertionError('invalid interlacing accepted')
 return dict(records=records,physical_controls=count,whole_chamber_segments=4,new_completion_removals=removed,boundary_rivals=1,half_cell_incompatibilities=2)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2047-fifth-thermal-spacing-phase.json').read_text())
 assert hashlib.sha256((ROOT/r['bank_ref']).read_bytes()).hexdigest()==r['bank_sha256']
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r),flush=True)
 faults=[]
 for label,edit in [('fifth extension',lambda x:x['phases'][0]['interval'].__setitem__(1,'49/100')),('U return',lambda x:x['endpoints']['U'].__setitem__(1,'1/4')),('rival mass',lambda x:x['boundary_rival'].__setitem__('shifted_U_mass','1/2')),('equality omission',lambda x:x['strict_equalities']['CQ_low'].clear())]:
  z=copy.deepcopy(r);edit(z)
  try:replay(z,False)
  except AssertionError as e:assert str(e);faults.append([label,str(e)])
  else:raise AssertionError('missed '+label)
 print('PASS four faults',faults)
