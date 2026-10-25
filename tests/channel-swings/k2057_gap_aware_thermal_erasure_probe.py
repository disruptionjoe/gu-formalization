"""Independent actual bath replay, tail controls and certificate inequalities."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
def cost(s,p):
 bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
 out=Q(0)
 for x,px in zip(s,p):
  incoming=Q(0)
  for j in range(4):
   candidates=[py*bath[x+j-y] for y,py in zip(s,p) if x+j-y in range(4)]
   incoming+=max(candidates,default=Q(0))
  out+=max(Q(0),px-incoming/2)
 return out
def reward(s):
 r=s[-1]-s[-2] if len(s)>1 else 4
 values={1:Q(14,55),2:Q(1,8),3:Q(3,55)}
 allowed=[v for d,v in values.items() if d+r>=4 and s[-1]+d>=12]
 return max(allowed,default=Q(0))
def tail_checks(data):
 count=0;beta={1:Q(3,55),2:Q(1,8),3:Q(14,55)};losscoef=Q(data['loss_factor']);unif=Q(data['uniform_boundary'])
 for gaps in product([1,2,3],repeat=3):
  if any(x+y<4 for x,y in zip(gaps,gaps[1:])):continue
  s=[max(1,3-gaps[0])]
  for d in gaps:s.append(s[-1]+d)
  for nums in [(8,12,3,1),(1,1,1,1),(3,0,5,0),(1,2,4,8),(81,9,1,1)]:
   p=list(map(Q,nums));R=cost(s,p)
   for cut in range(4):
    delta=R-cost(s[:cut],p[:cut]);q=sum(p[cut:])
    B=Q(0) if cut==0 else (unif if cut==1 else beta[gaps[cut-2]])*p[cut-1]
    assert q<=B+losscoef*delta,'physical gap-aware tail'
    wrong=Q(0);roots=Q(0)
    for j in range(cut,4):
     step=cost(s[:j+1],p[:j+1])-cost(s[:j],p[:j])
     if j==0:roots+=step
     elif gaps[j-1] in [1,3]:wrong+=step
    assert B+Q(25,4)*delta-q>=Q(59,44)*wrong+Q(823,220)*roots,'physical near equality';count+=1
 # Saturating gap2 sequence: finite truncations converge to equality, not sampled proof.
 for n in range(1,13):
  p=[Q(1),Q(1)]+[Q(3,2)*Q(1,9)**j for j in range(n)];s=list(range(1,2*len(p),2));delta=cost(s,p)-cost(s[:2],p[:2]);q=sum(p[2:])
  assert delta==Q(1,4),'sharp actual loss'
  assert q==Q(27,16)*(1-Q(1,9)**n),'sharp actual tail mass'
  assert q<=Q(1,8)+losscoef*delta,'sharp coefficient lower control';count+=1
 assert Q(data['sharp_gap2']['q_over_b'])-Q(data['sharp_gap2']['B_over_b'])==losscoef*Q(data['sharp_gap2']['delta_over_b']),'infinite sharp equality'
 return count

def upper_checks(data):
 u=data['upper_construction'];p=list(map(Q,u['prefix']));s=[1,3,5,7,9,11];b=p[-1]
 assert sum(p)+b/8==1,'infinite mass';assert sum(x*y for x,y in zip(s,p))+Q(53,32)*b==Q(5,2),'infinite energy'
 assert cost(s,p)==Q(data['upper']),'infinite prefix return';assert Q(u['tail_mass'])==b/8 and Q(u['tail_energy'])==Q(53,32)*b
 assert Q(u['gain_over_K2053'])==Q(7671,27472)-Q(data['upper'])>0
 for n in range(1,13):
  pp=p+[b*Q(1,9)**j for j in range(1,n+1)];ss=list(range(1,2*len(pp),2));assert cost(ss,pp)==cost(s,p),'invisible physical appended tail'
 p15=list(map(Q,u['finite15_population']));assert sum(p15)==1 and sum(x*y for x,y in zip(range(1,14,2),p15))==Q(5,2),'finite mass/energy'
 assert cost(list(range(1,14,2)),p15)==Q(u['finite15_value'])<Q(7671,27472),'finite improvement'
 old=json.loads((ROOT/data['upper_evidence']).read_text())['interval_bracket']['endpoints'];new=[]
 for v in old:
  p0=list(map(Q,v['population']));b0=p0[-1];Z=1+b0/8;E=(Q(v['energy'])+Q(53,32)*b0)/Z;R=Q(v['value'])/Z
  assert cost(s,p0)==Q(v['value']),'base family actual return';new.append((E,R))
 a,sl=map(Q,u['line']);assert [str(x[0]) for x in new]==u['interval'];assert all(R==a+sl*E for E,R in new);assert a+sl*Q(5,2)==Q(data['upper'])
 pa,ps=map(Q,u['partial_line']);pe=list(map(Q,u['partial_interval']));assert pa+ps*pe[0]==Q(old[0]['value']) and pa+ps*pe[1]==new[0][1]
 assert pe[0]==Q(old[0]['energy']) and pe[1]==new[0][0]
 for lam in [Q(0),Q(1,2),Q(1)]:
  b0=Q(old[0]['population'][-1]);Z=1+lam*b0/8;E=(Q(old[0]['energy'])+lam*b0*Q(53,32))/Z;R=Q(old[0]['value'])/Z;assert R==pa+ps*E,'partial attached family'
 assert Q(data['rigidity']['non_gap2_loss_margin'])==Q(25,4)-Q(54,11);assert Q(data['rigidity']['root_loss_margin'])==Q(25,4)-Q(138,55)
 return 15

def relaxation_dual(data):
 bank=json.loads((ROOT/data['bank_ref']).read_text())['bank'];d=data['relaxation_dual'];weights=list(map(Q,d['weights']));rows=[]
 a,s,eta=map(Q,data['assignments'][d['cell']])
 for ci,vi,shift in d['contacts']:
  c=bank[ci];v=c['vertices'][vi];e=Q(v['energy'])+shift;R=Q(v['value']);B=reward(c['s'])*Q(v['p'][-1]);rows.append((e,R,B))
  assert a+s*e+eta*B==R,'exact contact'
 rows.append((Q(d['tail_energy']),Q(0),Q(-1)))
 assert a+s*rows[-1][0]==eta,'tail contact'
 assert all(w>0 for w in weights) and sum(weights)==1,'dual normalization'
 assert sum(w*r[0] for w,r in zip(weights,rows))==Q(data['energy']),'dual energy'
 assert sum(w*r[2] for w,r in zip(weights,rows))==0,'dual boundary cancellation'
 assert sum(w*r[1] for w,r in zip(weights,rows))==Q(d['ceiling'])==Q(data['lower']),'dual ceiling'
 # Positive supports of these two proposed components collide in shell3.
 occupied=[]
 for ci,vi,shift in d['contacts']:
  occupied.extend(e+shift for e,p in zip(bank[ci]['s'],map(Q,bank[ci]['vertices'][vi]['p'])) if p>0)
 assert all(e in occupied for e in [1,2,3]),'incompatible relaxed mixture'
 return 3

def certificate(data,physical):
 bank=json.loads((ROOT/data['bank_ref']).read_text())['bank'];assert hashlib.sha256((ROOT/data['bank_ref']).read_bytes()).hexdigest()==data['bank_sha256'];assert len(bank)==len(data['assignments'])
 lines=set();allvals=[];count=0;al,sl=map(Q,data['lower_line']);left,right=map(Q,data['interval']);E=Q(data['energy'])
 for cell,line in zip(bank,data['assignments']):
  a,s,eta=map(Q,line);assert 0<=eta<=Q(4,25) and s<0,'eta/sign';lines.add((a,s,eta));vB=reward(cell['s'])
  for v in cell['vertices']:
   p=list(map(Q,v['p']));e=Q(v['energy']);R=Q(v['value']);B=vB*p[-1]
   if physical:assert cost(cell['s'],p)==R,'direct bath vertex'
   assert R-eta*B>=a+s*e,'low support';allvals.append((e,R,B));count+=1
  assert a+s*E>=Q(data['lower']),'point envelope';assert all(a+s*x>=al+sl*x for x in [left,right]),'whole interval'
  assert all(a+s*x<=eta for x in [12,13]),'tail support'
 for a,s,eta in lines:assert all(R-eta*B>=a+s*(e+1) for e,R,B in allvals),'all high supports'
 assert al+sl*E==Q(data['lower']);assert Q(data['gain_over_K2054'])==Q(data['lower'])-Q(439997389,1588579400)>0
 upper=data['upper_construction'];assert Q(data['width'])==Q(data['upper'])-Q(data['lower'])>0
 assert Q(upper['partial_interval'][0])<=left<=right<=Q(upper['interval'][1])
 return count,len(lines)
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2057-gap-aware-thermal-erasure.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS exact relaxation dual',relaxation_dual(d),flush=True);print('PASS actual tail controls',tail_checks(d),flush=True);print('PASS released witness/family checks',upper_checks(d),flush=True);print('PASS certificate vertices/unique lines',certificate(d,True),flush=True)
 faults=[]
 for name in ['loss','boundary','sharp_mass','intercept','eta','slope','tail_energy','upper_line','rigidity','dual_weight']:
  x=copy.deepcopy(d)
  if name=='loss':x['loss_factor']='6'
  elif name=='boundary':x['uniform_boundary']='0'
  elif name=='sharp_mass':x['sharp_gap2']['q_over_b']='2'
  elif name=='intercept':x['assignments'][0][0]=str(Q(x['assignments'][0][0])+1)
  elif name=='eta':x['assignments'][0][2]='1'
  elif name=='slope':x['assignments'][0][1]='0'
  elif name=='tail_energy':x['upper_construction']['tail_energy']='0'
  elif name=='upper_line':x['upper_construction']['line'][0]='0'
  elif name=='rigidity':x['rigidity']['root_loss_margin']='0'
  else:x['relaxation_dual']['weights'][0]='0'
  try:
   if name=='dual_weight':relaxation_dual(x)
   elif name in ['loss','boundary','sharp_mass']:tail_checks(x)
   elif name in ['tail_energy','upper_line','rigidity','dual_weight']:upper_checks(x)
   else:certificate(x,False)
  except AssertionError:faults.append(name)
  else:raise AssertionError('missed fault '+name)
 print('PASS ten mathematical faults',faults)
