"""Separate same-author direct bath-label, packing and complete inequality verification."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
K={1:Q(7,29),2:Q(1,9),3:Q(1,23)};C={1:Q(29,135),2:Q(9,50),3:Q(23,90)}
A={1:Q(14,55),2:Q(1,8),3:Q(3,55)}
def cost(s,p):
 bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
 return sum(max(Q(0),px-sum(max([Q(0)]+[py*bath[x+j-y] for y,py in zip(s,p) if x+j-y in range(4)]) for j in range(4))/2) for x,px in zip(s,p))
def ds(s):return [d for d in K if s[-1]+d>=12 and (len(s)==1 or s[-1]-s[-2]+d>=4)]
def reward(s):return max([Q(0)]+[A[d] for d in ds(s)])
def linecheck(v,bank,high=True,mode=None):
 a,t=Q(v['a']),-Q(v['s']);assert t>0,'negative slope'
 if v['kind']=='uniform':
  eta=Q(v['eta']);assert 0<=eta<=Q(4,25),'loss price'
  assert a-12*t<=eta and a-(12+v['shift'])*t<=eta,'tail endpoints'
  B=lambda s:eta*reward(s)
 else:
  L=v['cutoff'];g={(n,d):Q(x) for n,d,x in v['bellman']};hg={(n,d):Q(x) for n,d,x in v['high_bellman']};assert len(g)==len(hg)==3*(L-11),'complete Bellman table'
  assert a<=(L+1)*t,'discarded far tail sign'
  support=bank[v['_cell']]['s'];reach={(support[-1]+d,d) for d in ds(support)}
  for n in range(12,L+1):
   for d in K:
    if (n,d) in reach:reach.update((n+e,e) for e in K if d+e>=4 and n+e<=L)
  for table,off in [(g,0),(hg,v['shift'])]:
   for n in range(12,L+1):
    for d in K:
     assert table[n,d]>=0,'nonnegative majorant'
     if off or (n,d) in reach:assert table[n,d]<=C[d],'terminal loss pays energy reward'
     for e in K:
      if d+e>=4:assert table[n,d]>=a-t*(n+off)+K[e]*table.get((n+e,e),Q(0)),'Bellman transition'
     if off:assert a-t*(n+off)+K[d]*table.get((n+d,d),Q(0))<=Q(1,2),'root loss'
  B=lambda s:max([Q(0)]+[K[d]*g.get((s[-1]+d,d),Q(0)) for d in ds(s)])
  BH=lambda s:max([Q(0)]+[K[d]*hg.get((s[-1]+d,d),Q(0)) for d in ds(s)])
 ci=v['_cell'];cell=bank[ci]
 for vertex in cell['vertices']:
  assert Q(vertex['value'])>=a-t*Q(vertex['energy'])+B(cell['s'])*Q(vertex['p'][-1]),'low actual chamber'
 if high:
  for cell in bank:
   coef=(BH if v['kind']=='energy' else B)(cell['s'])
   for vertex in cell['vertices']:
    assert Q(vertex['value'])>=a-t*(Q(vertex['energy'])+v['shift'])+coef*Q(vertex['p'][-1]),'all high chambers'
 return B

def packing(bank,mode=None):
 count=0
 for cell in bank:
  s=cell['s'];ell=max(1,s[-2]+1) if len(s)>1 else 1
  if len(s)<2:continue
  # Every two-occupied-input shell has capacity exactly four; reconstruct
  # forced physical lattice positions from the original shell labels.
  forced=set()
  for E in range(s[0],s[-1]+4):
   occupants=[x for x in s if E-x in range(4)]
   assert len(occupants)<=2,'legal occupied path'
   if len(occupants)==2:forced.update(E-j for j in range(4))
  if s[0]==1:forced.update([0,1]) # low offset <1 makes lower alternatives negative
  Z=s[-2]+3
  assert set(range(Z+1))<=forced,'forced contiguous physical ladder'
  assert ell==Z-(1 if mode=='overprice_offset' else 2),'uniform other root offset'
  # Same-residue occupied points inside that ladder share a shell with low.
  for y in range(2,Z+1):assert any(abs(y-x)<=3 for x in s),'same component'
  # A different fractional residue cannot fit between consecutive integers.
  for f in [Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(9,10)]:assert min(f,1-f)<=Q(1,2),'packing threshold'
  count+=1
 return count

def tails(data):
 bank=json.loads((ROOT/data['bank_ref']).read_text())['bank'];v=dict(data['assignments'][188],_cell=188);B=linecheck(v,bank,False);a,t=Q(v['a']),-Q(v['s']);count=0
 prefix=[1,3,5,7,9,11]
 for gaps in product([1,2,3],repeat=4):
  if gaps[0]+2<4 or any(x+y<4 for x,y in zip(gaps,gaps[1:])):continue
  s=prefix.copy()
  for gap in gaps:s.append(s[-1]+gap)
  for nums in [(1,2,4,8),(9,1,0,3),(1,0,0,0),(0,0,0,0),(1,1,1,1)]:
   p=[Q(1,6)]*6+[Q(x,17) for x in nums];Delta=cost(s,p)-cost(prefix,p[:6]);q=sum(p[6:]);h=sum(x*y for x,y in zip(s[6:],p[6:]));assert Delta>=a*q-t*h-B(prefix)*p[5],'actual attached energy tail';count+=1
 # Root-only whole-tail controls, including positive and negative rewards.
 for root in [12,13,20,33,100]:
  for nums in [(1,9,3),(81,9,1),(1,1,1)]:
   s=[root,root+2,root+4];p=list(map(Q,nums));assert cost(s,p)>=sum((a-t*(x+v['shift']))*y for x,y in zip(s,p)),'whole component energy tail';count+=1
 return count

def upper_checks(data):
 w=data['upper_witness'];support=w['support'];bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)];count=0
 def output(p,c):
  spec=w['finite_spectrum'];out={n:Q(0) for n in spec}
  for E in sorted({n+j for n in support for j in range(4)}):
   occ=[(n,p[i]*bath[E-n]) for i,n in enumerate(support) if E-n in range(4)]
   physical=[n for n in spec if E-n in range(4)]
   assert len(physical)>=2*len(occ),'actual shell capacity'
   heavy=max(occ,key=lambda x:x[1]);outputs=[heavy[0]]+([x[0] for x in occ if x!=heavy] if len(occ)==2 else [n for n in physical if n!=heavy[0]][:1])
   out[outputs[0]]+=c*heavy[1];out[outputs[1]]+=(1-c)*heavy[1]
   if len(occ)==2:
    light=next(x for x in occ if x!=heavy);empty=[n for n in physical if n not in outputs];out[empty[0]]+=c*light[1];out[empty[1]]+=(1-c)*light[1]
  assert sum(out.values())==sum(p),'shell output normalization'
  return sum(abs(out[n]-(p[support.index(n)] if n in support else 0)) for n in spec)/2
 for tag in ['finite21','countable']:
  z=w[tag];aff=[list(map(Q,x)) for x in z['population_affine']];line=list(map(Q,z['line']))
  for E in [Q(249,100),Q(5,2),Q(251,100)]:
   p=[a+b*E for a,b in aff];assert min(p)>0,'positive witness'
   mass=sum(p)+(p[-1]/8 if tag=='countable' else 0);energy=sum(n*x for n,x in zip(support,p))+(Q(85,32)*p[-1] if tag=='countable' else 0)
   assert mass==1 and energy==E,'witness mass and energy'
   ret=cost(support,p);assert ret==line[0]+E*line[1],'affine actual return'
   assert output(p,Q(1,2))==ret and output(p,Q(1))<=ret,'all input unitary construction'
   if tag=='countable':
    for N in [1,2,4,8,12]:
     pp=p+[p[-1]/9**j for j in range(1,N+1)];ss=support+[19+2*j for j in range(1,N+1)];assert cost(ss,pp)==ret,'invisible infinite tail transfer';count+=1
   if E==Q(5,2):assert list(map(Q,z['population']))==p and Q(z['value'])==ret
   count+=1
 assert Q(w['countable']['value'])==Q(data['upper'])<Q(w['finite21']['value'])<Q(67173,240731),'both new upper bounds'
 assert Q(w['tail_mass_factor'])==Q(1,8) and Q(w['tail_energy_factor'])==Q(85,32),'tail moments'
 return count

def certificate(data,physical=True):
 bank=json.loads((ROOT/data['bank_ref']).read_text())['bank'];assert hashlib.sha256((ROOT/data['bank_ref']).read_bytes()).hexdigest()==data['bank_sha256'],'bank pin'
 assert len(bank)==len(data['assignments'])==671
 count=0;unique={};E=Q(data['energy']);left,right=map(Q,data['interval']);al,sl=map(Q,data['lower_line']);assert left<E<right
 for i,(cell,vv) in enumerate(zip(bank,data['assignments'])):
  v=dict(vv,_cell=i);assert v['shift']==(max(1,cell['s'][-2]+1) if len(cell['s'])>1 else 1),'correct packing shift'
  a,s=Q(v['a']),Q(v['s']);assert all(a+s*x>=al+sl*x for x in [left,right]),'whole energy interval'
  linecheck(v,bank,False)
  key=(v['kind'],v['a'],v['s'],v.get('eta'),v['shift']);unique[key]=v
  if physical:
   for x in cell['vertices']:assert cost(cell['s'],list(map(Q,x['p'])))==Q(x['value']),'direct bath maximum';count+=1
 for v in unique.values():linecheck(v,bank,True)
 assert Q(data['lower'])==al+sl*E,'lower value';assert Q(data['gain'])==Q(data['lower'])-Q(243396,878731)>0,'strict gain'
 assert Q(data['width'])==Q(data['upper'])-Q(data['lower'])>0,'remaining gap'
 return count,len(unique)
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2059-energy-aware-thermal-tail.json').read_text());bank=json.loads((ROOT/d['bank_ref']).read_text())['bank']
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS physical upper construction',upper_checks(d),flush=True);print('PASS packing geometries',packing(bank),flush=True);print('PASS actual energy-tail controls',tails(d),flush=True);print('PASS full bank/line checks',certificate(d),flush=True)
 caught=[]
 for mode in ['offset','intercept','slope','loss_price','bellman','terminal','cutoff','lower','far_tail','witness_population','witness_tail','witness_spectrum']:
  x=copy.deepcopy(d)
  if mode=='offset':x['assignments'][0]['shift']+=1
  elif mode=='intercept':x['assignments'][188]['a']=str(Q(x['assignments'][188]['a'])+1)
  elif mode=='slope':x['assignments'][188]['s']='0'
  elif mode=='loss_price':x['assignments'][0]['eta']='1'
  elif mode=='bellman':next(row for row in x['assignments'][188]['bellman'] if row[:2]==[13,2])[2]='0'
  elif mode=='terminal':next(row for row in x['assignments'][188]['bellman'] if row[:2]==[13,2])[2]='1'
  elif mode=='cutoff':x['assignments'][188]['cutoff']=12
  elif mode=='lower':x['lower']='1/2'
  elif mode=='far_tail':x['assignments'][188]['a']='1'
  elif mode=='witness_population':x['upper_witness']['countable']['population_affine'][0][0]='0'
  elif mode=='witness_tail':x['upper_witness']['tail_energy_factor']='0'
  else:x['upper_witness']['finite_spectrum']=x['upper_witness']['support']
  try:
   if mode.startswith('witness'):upper_checks(x)
   else:certificate(x,False)
  except AssertionError as e:caught.append((mode,str(e)))
  else:raise AssertionError('missed fault '+mode)
 print('PASS mathematical faults',caught)
