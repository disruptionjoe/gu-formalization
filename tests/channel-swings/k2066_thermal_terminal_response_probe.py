"""Separate exact raw response, Bellman and whole-bank inequality verification."""
from fractions import Fraction as Q
pos=lambda x:max(Q(0),x)
def raw(p,c0,u,L,H):return (pos(p-c0-pos(L*u-H*p))+pos(u-pos(H*p-L*u))-pos(p-c0))/2
def pieces(p,A,u,L,H):
 k=H/(1+L)
 if u<=k*p:return Q(0)
 if u<=H*p/L:return ((1+L)*u-H*p)/2
 if u<=(A+H*p)/L:return ((1-L)*u+H*p)/2
 return (u-A)/2
def env(g,p,A,L,H):return max(g*H*p/(1+L),(g-Q(1,2))*H*p/L+(Q(1,2)+(g-Q(1,2))/L)*A)
def verify():
 count=0
 for t in [Q(1,3),Q(1,2),Q(2,3)]:
  Z=sum(t**j for j in range(4))
  for d in [1,2,3]:
   L=sum(t**j for j in range(4-d))/Z;H=t**d*L;k=H/(1+L);c=(1+H-L)*(1+L)/(2*(1+H+L));alpha=L*(1+L)/(1+H+L);beta=H/(1+H+L)
   assert (1+L)/2-c==alpha
   assert (c-(1-L)/2)/L==beta
   for p in [Q(0),Q(1,5),Q(1),Q(7,3)]:
    for c0 in [Q(0),p/3,p,2*p]:
     A=pos(p-c0);bp=[Q(0),k*p,H*p/L,(A+H*p)/L];uu=sorted(set(bp+[(x+y)/2 for x,y in zip(bp,bp[1:])]+[bp[-1]+1,bp[-1]+100]))
     for u in uu:
      val=raw(p,c0,u,L,H);x=pos(u-k*p)
      assert val==pieces(p,A,u,L,H)
      assert val>=c*x+min(alpha*x,beta*(p-A))
      count+=1
     for g in [Q(0),(1-L)/2,c,(c+Q(1,2))/2,Q(1,2)]:
      ans=env(g,p,A,L,H)
      assert ans==max(g*u-raw(p,c0,u,L,H) for u in bp)
      assert all(g*u-raw(p,c0,u,L,H)<=ans for u in uu)
      count+=1
   # Analytic break slopes prove endpoint maximization, no grid reliance.
   assert (1-L)/2<c<Q(1,2)<(1+L)/2
 # The old independent sharp case cannot justify improved universal c.
 L,H=Q(4,5),Q(1,5);p=Q(1);u=Q(3,2);c=Q(9,50)
 assert raw(p,0,u,L,H)==c*(u-Q(1,9))
 assert raw(p,p,u,L,H)>c*(u-Q(1,9))
 return count

from pathlib import Path
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
K={1:Q(7,29),2:Q(1,9),3:Q(1,23)};C={1:Q(29,135),2:Q(9,50),3:Q(23,90)};LH={1:(Q(14,15),Q(7,15)),2:(Q(4,5),Q(1,5)),3:(Q(8,15),Q(1,15))}
def gaps(s):return [d for d in K if s[-1]+d>=12 and (len(s)==1 or s[-1]-s[-2]+d>=4)]
def table(a,t,offset=0):
 assert t>0 and a<=65*t,'far tail sign'
 g={}
 for n in reversed(range(12,65)):
  for d in [1,2,3]:g[n,d]=max([Q(0)]+[a-t*(n+offset)+K[e]*g.get((n+e,e),Q(0)) for e in K if d+e>=4])
 return g

def cost(s,p):
 bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
 return sum(max(Q(0),p[i]-sum(max([Q(0)]+[p[j]*bath[x+b-y] for j,y in enumerate(s) if 0<=x+b-y<=3]) for b in range(4))/2) for i,x in enumerate(s))

def check_assignment(ci,v,bank,high=True):
 a,t=Q(v['a']),-Q(v['s']);ss=bank[ci]['s'];ell=max(1,ss[-2]+1) if len(ss)>1 else 1;g=table(a,t);h=table(a,t,ell)
 first={(ss[-1]+d,d) for d in gaps(ss)};reach=set(first)
 for n in range(12,65):
  for d in [1,2,3]:
   if (n,d) in reach:reach.update((n+e,e) for e in K if d+e>=4 and n+e<=64)
 assert all(g[n,d]<=(Q(1,2) if (n,d) in first else C[d]) for n,d in reach),'first/deeper loss caps'
 assert all(x<=C[d] for (n,d),x in h.items()),'high loss caps'
 assert all(a-t*(n+ell)+K[d]*h.get((n+d,d),Q(0))<=Q(1,2) for n in range(12,65) for d in K),'whole root'
 count=0
 for z in bank[ci]['vertices']:
  pp=list(map(Q,z['p']));p=pp[-1];c0=Q(0)
  if len(ss)>1:
   L,H=LH[ss[-1]-ss[-2]];c0=max(Q(0),H*pp[-2]-L*p)
  A=max(Q(0),p-c0);boundary=max([Q(0)]+[env(g[ss[-1]+d,d],p,A,*LH[d]) for d in gaps(ss)])
  # Crucially tested even when the outgoing set is empty.
  assert Q(z['value'])>=a-t*Q(z['energy'])+boundary,'low zero/envelope inequality'
  assert cost(ss,pp)==Q(z['value']),'raw low-cell bath return';count+=1
 if high:
  for cell in bank:
   coef=max([Q(0)]+[K[d]*h.get((cell['s'][-1]+d,d),Q(0)) for d in gaps(cell['s'])])
   for z in cell['vertices']:
    assert Q(z['value'])>=a-t*(Q(z['energy'])+ell)+coef*Q(z['p'][-1]),'high-bank inequality';count+=1
 return count

def certificate(data):
 for p,h in data['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 old=json.loads((ROOT/data['base_ref']).read_text());bank=json.loads((ROOT/old['bank_ref']).read_text())['bank'];assign=list(old['assignments']);count=0
 for key,v in data['replacements'].items():ci=int(key);count+=check_assignment(ci,v,bank);assign[ci]=v
 a,s=map(Q,data['lower_line']);left,right=map(Q,data['interval']);assert left<Q(5,2)<right
 assert all(Q(v['a'])+Q(v['s'])*E>=a+s*E for v in assign for E in [left,right]),'all671 interval lines'
 lower,ci=min((Q(v['a'])+Q(5,2)*Q(v['s']),i) for i,v in enumerate(assign));assert Q(data['lower'])==lower==a+Q(5,2)*s,'reported global lower';assert ci==data['bottleneck']
 assert Q(data['upper'])==Q(old['upper']) and Q(data['width'])==Q(data['upper'])-lower>0,'upper/width';assert Q(data['gain'])==lower-Q(old['lower'])>0,'strict improvement'
 return count,bank
if __name__=='__main__':
 local=verify();d=json.loads((ROOT/'lab/process/k2066-thermal-terminal-response.json').read_text());count,bank=certificate(d);print('PASS raw-response controls',local,'new low/high inequalities',count,'all671 line interval')
 # Baseline was checked above. Mutate mathematical coefficients/data, never checks.
 faults=[]
 for name,fn in [('response_factor',lambda: raw(Q(1),Q(1),Q(2),Q(4,5),Q(1,5))*2==pieces(Q(1),Q(0),Q(2),Q(4,5),Q(1,5))),('envelope_incoming',lambda: env(Q(2,5),Q(1),Q(0),Q(4,5),Q(1,5))==env(Q(2,5),Q(1),Q(1),Q(4,5),Q(1,5)))]:
  if fn():raise AssertionError('undetected formula fault '+name)
  faults.append(name)
 # Wrong high intercept on a no-outgoing-tail cell must hit its unconditional low check.
 v=copy.deepcopy(d['replacements']['152']);v['a']=str(Q(v['a'])+Q(1,1000))
 try:check_assignment(152,v,bank,False)
 except AssertionError as e:faults.append('no_attachment_intercept:'+str(e))
 else:raise AssertionError('undetected no-tail fault')
 bad=copy.deepcopy(d);bad['lower']='1/2'
 # Target the global consistency check directly, without repeating unchanged bank work.
 if Q(bad['lower'])==Q(bad['lower_line'][0])+Q(5,2)*Q(bad['lower_line'][1]):raise AssertionError('undetected lower fault')
 faults.append('reported_lower')
 # Strict g cap is necessary: past the last breakpoint, reward grows for g>1/2.
 g=Q(3,5);p=A=Q(1);L,H=Q(4,5),Q(1,5);u=Q(100)
 assert g*u-raw(p,0,u,L,H)>env(g,p,A,L,H),'planted over-cap reward must escape finite envelope';faults.append('overcap_reward')
 print('PASS mathematical fault discriminators',faults)
