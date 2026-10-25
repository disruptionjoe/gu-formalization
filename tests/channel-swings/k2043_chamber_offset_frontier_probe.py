"""Direct bath-shell replay and independently computed line inequalities."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];weights=[F(8,15),F(4,15),F(2,15),F(1,15)]
def physical(ss,pp,spec,delta):
 assert sum(pp)==1 and min(pp)>=0,'normalization'
 spec=sorted(spec);assert min(spec)>=0 and len(set(spec))==len(spec),'spectrum'
 assert all(b-a>=delta for a,b in zip(spec,spec[1:])),'spacing'
 active=[s for s,p in zip(ss,pp) if p];ret=F(0)
 for energy in {s+b for s in active for b in range(4)}:
  incoming=sum(energy-s in range(4) for s in active);out=sum(energy-s in range(4) for s in spec)
  assert out>=2*incoming,'shell capacity'
 for s,p in zip(ss,pp):
  kept=F(0)
  for b in range(4):
   e=s+b;kept+=max([q*weights[int(e-y)] for y,q in zip(ss,pp) if e-y in range(4)])
  ret+=max(F(0),p-kept/2)
 return sum(s*p for s,p in zip(ss,pp)),ret

def replay(r,bank):
 ends={}
 for name,end in r['endpoints'].items():
  p=list(map(F,end['population']));ss=list(map(F,range(1,2*len(p),2)));sp=list(map(F,range(2*len(p)+1)))
  e,v=physical(ss,p,sp,F(1));assert [e,v]==[F(end['energy']),F(end['value'])],'endpoint actual return';ends[name]=(e,v,p)
 A,B,D=ends['A'],ends['B'],ends['D'];count=0;direct=[]
 for c in bank:
  rows=[]
  for v in c['vertices']:
   s=list(map(F,c['s']));p=list(map(F,v['p']));e,val=physical(s,p,list(map(F,range(13))),F(1))
   assert e==F(v['energy']) and val==F(v['value']),'bank shell replay';rows.append((e,val));count+=1
  direct.append(rows)
 def affine(side,phase,d):
  if side=='A':p=(A[0],A[1]);q=(B[0]+d,B[1])
  else:
   U=A if phase==1 else D;p=(U[0]+d,U[1]);q=(B[0],B[1])
  # Return cleared residual, retaining positive denominator rather than producer intercepts.
  def residue(e,v):return (q[0]-p[0])*(v-p[1])-(q[1]-p[1])*(e-p[0])
  return residue,p,q
 for cert in r['certificates']:
  lo,hi=map(F,cert['interval']);phase=cert['phase'];labels=cert['cell_labels'];assert len(labels)==len(bank)
  for d in [lo,hi]:
   for i,rows in enumerate(direct):
    for side in labels[i]:
     res,_,_=affine(side,phase,d);assert all(res(e,v)>=0 for e,v in rows),'low chamber coefficient'
   for side in ['A','B']:
    res,p,q=affine(side,phase,d);assert all(res(e+d,v)>=0 for rows in direct for e,v in rows),'shifted vertex coefficient'
    assert res(F(10),F(0))>0,'tail charge'
 assert count==r['records']==3137
 tested=0
 for phase,ds in [(1,[F(1,1000),F(1,100),F(2,181)]),(2,[(F(2,181)+F(2,145))/2,F(2,145)])]:
  for d in ds:
   U=A if phase==1 else D
   for side in ['A','B']:
    for m in [F(1,10),F(1,2),F(9,10)]:
     low,high=(A,B) if side=='A' else (B,U)
     ss=list(map(F,range(1,2*len(low[2]),2)))+[F(k)+d for k in range(1,2*len(high[2]),2)]
     pp=[(1-m)*v for v in low[2]]+[m*v for v in high[2]]
     sp=list(map(F,range(2*len(low[2])+1)))+[F(k)+d for k in range(2*len(high[2])+1)]
     e,v=physical(ss,pp,sp,d);res,_,_=affine(side,phase,d);assert res(e,v)==0,'attainment';tested+=1
 for w in r['witnesses']:
  d,e=F(w['delta']),F(w['energy'])
  if w['phase']==1:
   m=F(w['shifted_D_mass']);ss=list(map(F,[1,3,5,7,9]))+[F(k)+d for k in [1,3,5,7]];pp=[(1-m)*v for v in B[2]]+[m*v for v in D[2]];sp=list(map(F,range(11)))+[F(k)+d for k in range(9)]
  else:ss=list(map(F,[1,3,5,7]));pp=ends['Q'][2];sp=list(map(F,range(9)))
  actual_e,v=physical(ss,pp,sp,d);assert actual_e==e and v==F(w['value']),'physical rival'
  candidates=[]
  for side in ['A','B']:
   _,p,q=affine(side,w['phase'],d);candidates.append(p[1]+(q[1]-p[1])*(e-p[0])/(q[0]-p[0]))
  assert min(candidates)-v==F(w['improvement'])>0,'strict undercut'
 # Actual forced low-ground and minimal completion controls.
 forced=0
 for support in [[2,3],[1,3],[1,4],[1]]:
  d=F(1,100);ss=[F(x)+d for x in support];pp=[F(1,len(ss))]*len(ss);sp=[F(x)+d for x in range(max(support)+4)]
  physical(ss,pp,sp,d)
  try:physical(ss,pp,sp[1:],d)
  except AssertionError as e:assert str(e)=='shell capacity';forced+=1
  else:raise AssertionError('ground not forced')
 removed=0
 for name in ['A','B','D']:
  ep=ends[name];ss=list(map(F,range(1,2*len(ep[2]),2)));sp=list(map(F,range(2*len(ep[2])+1)))
  for level in sp:
   try:physical(ss,ep[2],[x for x in sp if x!=level],F(1))
   except AssertionError as e:assert str(e)=='shell capacity';removed+=1
   else:raise AssertionError('completion not necessary')
 return dict(shell_records=count,physical_mixtures=tested,physical_rivals=len(r['witnesses']),forced_ground_cases=forced,necessary_completion_removals=removed)
def main():
 r=json.loads((ROOT/'lab/process/k2043-chamber-offset-frontier.json').read_text());bank=json.loads((ROOT/'lab/process/k2037-thermal-seven-level-boundary.json').read_text())['banks']['9']
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r,bank));caught=[]
 for label,edit in [('overextended first phase',lambda z:z['certificates'][0]['interval'].__setitem__(1,'1/50')),('overextended second phase',lambda z:z['certificates'][1]['interval'].__setitem__(1,'1/50')),('corrupt endpoint',lambda z:z['endpoints']['D'].__setitem__('value','1/4')),('rival population',lambda z:z['witnesses'][0].__setitem__('shifted_D_mass','1/2'))]:
  z=copy.deepcopy(r);edit(z)
  try:replay(z,bank)
  except AssertionError as e:caught.append([label,str(e)])
  else:raise AssertionError('missed '+label)
 print('PASS faults',caught)
if __name__=='__main__':main()
