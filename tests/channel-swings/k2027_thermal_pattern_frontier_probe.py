"""Separate bath-label dual replay, exhaustive gap words and physical fault tests."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import lcm
import json,zlib,base64,hashlib
ROOT=Path(__file__).resolve().parents[2]
lo,hi=F(7,5),F(8,5);intercept,slope=F(985095,2040416),F(61407,2040416);back=F(1,41)
bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
def shapes():
 yield (1,)
 def rec(s,gaps):
  yield tuple(s)
  for g in (1,2,3):
   if gaps[-1]+g>=4 and s[-1]+g<=20:yield from rec(s+[s[-1]+g],gaps+[g])
 for g in (1,2,3):
  start=max(1,3-g)
  yield from rec([start,start+g],[g])

def reconstruct(s,o,kind):
 n=len(s);edges=[]
 for i,sign in enumerate(o):
  d=s[i+1]-s[i];r=[F(0)]*(2*n);r[i]=-sign*15*sum(bath[d:]);r[i+1]=sign*15*sum(bath[:4-d]);edges.append(r)
 deficits=[]
 for i,x in enumerate(s):
  row=[F(0)]*(2*n);row[i]=1
  for b in range(4):
   shell=x+b;cc=[(j,shell-y) for j,y in enumerate(s) if shell-y in (0,1,2,3)];assert 1<=len(cc)<=2
   if len(cc)==1:j,k=cc[0]
   else:
    assert cc[1][0]==cc[0][0]+1
    j,k=cc[0] if o[cc[0][0]]==1 else cc[1]
   row[j]-=bath[k]/2
  row[n+i]=-1;deficits.append(row)
 rows=edges+deficits;rhs=[F(0)]*len(rows)
 if kind not in ('energy','maxenergy'):rows.append(list(map(F,s))+[F(0)]*n);rhs.append(lo if kind=='low' else hi)
 if kind=='strip':rows.append([-F(x) for x in s]+[F(0)]*n);rhs.append(-lo)
 cost=([(-1 if kind=='maxenergy' else 1)*F(x) for x in s]+[F(0)]*n if kind in ('energy','maxenergy') else [(slope if kind=='strip' else back)*x for x in s]+[F(1)]*n)
 return rows,rhs,cost

def validate_dual(s,o,c):
 n=len(s);kind=c['kind'];nums=[8,4,2,1];rr=[]
 for i,sign in enumerate(o):
  gap=s[i+1]-s[i];rr.append({i:-30*sign*sum(nums[gap:]),i+1:30*sign*sum(nums[:4-gap])})
 for i,x in enumerate(s):
  row={i:30,n+i:-30}
  for b in range(4):
   shell=x+b;cc=[(j,shell-y) for j,y in enumerate(s) if 0<=shell-y<=3]
   assert 1<=len(cc)<=2
   j,k=cc[0] if len(cc)==1 or o[cc[0][0]]==1 else cc[1]
   row[j]=row.get(j,0)-nums[k]
  rr.append(row)
 rhs=[F(0)]*len(rr)
 if kind not in ('energy','maxenergy'):rr.append({j:30*x for j,x in enumerate(s)});rhs.append(lo if kind=='low' else hi)
 if kind=='strip':rr.append({j:-30*x for j,x in enumerate(s)});rhs.append(-lo)
 cost=([(-1 if kind=='maxenergy' else 1)*F(x) for x in s]+[F(0)]*n if kind in ('energy','maxenergy') else [(slope if kind=='strip' else back)*x for x in s]+[F(1)]*n)
 y=list(map(F,c['y']));z=F(c['z']);assert len(y)==len(rr) and all(v<=0 for v in y)
 D=lcm(*(x.denominator for x in y+[z]+cost));yi=[int(x*D) for x in y];zi=int(z*D)
 residual=[30*int(v*D)-30*zi*int(j<n) for j,v in enumerate(cost)]
 for row,v in zip(rr,yi):
  if v:
   for j,a in row.items():residual[j]-=a*v
 assert min(residual)>=0
 return z+sum(x*v for x,v in zip(rhs,y) if x)

def physical(w):
 s=w['support'];p=list(map(F,w['population']));spec=w['spectrum'];e=F(w['energy'])
 assert min(p)>=0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==e
 assert spec==sorted(set(spec)) and spec[0]==0 and min(y-x for x,y in zip(spec,spec[1:]))>=1
 active=[x for x,y in zip(s,p) if y]
 for shell in {x+b for x in active for b in range(4)}:assert sum(shell-a in (0,1,2,3) for a in spec)>=2*sum(shell-a in (0,1,2,3) for a in active)
 deficits=[]
 for x,v in zip(s,p):deficits.append(v-sum(max(q*bath[k] for y,q in zip(s,p) for k in range(4) if y+k==x+b)/2 for b in range(4)))
 value=sum(max(x,0) for x in deficits);assert value==F(w['return_value'])
 return value,deficits

def main():
 r=json.loads((ROOT/'lab/process/k2027-thermal-pattern-frontier.json').read_text());raw=zlib.decompress(base64.b85decode(r['certificate_payload']));assert hashlib.sha256(raw).hexdigest()==r['certificate_sha256'];rows=json.loads(raw)
 # Separate recursion, exact ordered coverage, including all zero-population faces.
 expected=((s,o) for s in shapes() if min(s)<=hi for o in product((-1,1),repeat=len(s)-1));n=0;contact=None;contacts=[]
 for row in rows:
  s,o=next(expected);assert row['s']==list(s) and row['o']==list(o)
  for kind,c in zip(('low','strip'),row['certificates']):
   assert c['kind']==kind
   if 'infeasible_energy' in c:assert validate_dual(s,o,c['infeasible_energy'])>(lo if kind=='low' else hi)
   elif 'infeasible_maxenergy' in c:assert kind=='strip' and -validate_dual(s,o,c['infeasible_maxenergy'])<lo
   else:
    v=validate_dual(s,o,c);target=intercept-slope*lo+back*lo if kind=='low' else intercept;assert v>=target
    if kind=='strip' and v==target:contact=(s,o,c);contacts.append(contact)
   n+=1
  if n%40000==0:print('separate bath dual replay',n,flush=True)
 assert next(expected,None) is None and n==2*r['orientation_cells']
 ends=r['witnesses'][:2]
 for w in r['witnesses']:assert physical(w)[0]==intercept-slope*F(w['energy'])
 # Shared maximizers and deficit signs prove affine attainment between endpoints.
 s=ends[0]['support'];ps=[list(map(F,w['population'])) for w in ends]
 for shell in {x+b for x in s for b in range(4)}:
  terms=[(i,b) for i,x in enumerate(s) for b in range(4) if x+b==shell];winners=[]
  for p in ps:
   m=max(p[i]*bath[b] for i,b in terms);winners.append({(i,b) for i,b in terms if p[i]*bath[b]==m})
  assert winners[0]&winners[1]
 dd=[physical(w)[1] for w in ends];assert all(a*b>=0 for a,b in zip(*dd))
 # Independently test equality by the nullspaces of complementary-slackness equations.
 from sage.all import QQ,matrix,vector
 pp=[list(map(F,w['population'])) for w in ends];sp=ends[0]['support']
 slopes=[(b-a)/(hi-lo) for a,b in zip(*pp)];constants=[a-b*lo for a,b in zip(pp[0],slopes)]
 for ss,oo,cc in contacts:
  aa,bb,cost=reconstruct(ss,oo,'strip');nn=len(ss);yy=list(map(F,cc['y']));zz=F(cc['z'])
  reduced=[cost[j]-sum(a[j]*v for a,v in zip(aa,yy))-zz*int(j<nn) for j in range(2*nn)]
  equations=[[QQ(j<nn) for j in range(2*nn)]+[QQ(0),QQ(-1)],[QQ(ss[j]) if j<nn else QQ(0) for j in range(2*nn)]+[QQ(-1),QQ(0)]]
  for j,v in enumerate(reduced):
   if v>0:equations.append([QQ(k==j) for k in range(2*nn)]+[QQ(0),QQ(0)])
  for a,v,b in zip(aa,yy,bb):
   if v<0:equations.append(list(map(QQ,a))+[QQ(0),-QQ(b)])
  kernel=matrix(QQ,equations).right_kernel().basis_matrix()
  for j,e in enumerate(ss):
   c0,c1=(constants[sp.index(e)],slopes[sp.index(e)]) if e in sp else (F(0),F(0))
   desired=vector(QQ,[QQ(k==j) for k in range(2*nn)]+[-QQ(c1),-QQ(c0)])
   assert kernel*desired==0
 assert len(contacts)==r['equality_audit']['contact_cells']==11 and not r['equality_audit']['failed']
 forced=set()
 for shell in {e+b for e in sp for b in range(4)}:
  if sum(shell-e in (0,1,2,3) for e in sp)==2:forced.update(shell-b for b in range(4))
 assert forced==set(range(17))
 print('PASS all11 equality cells imply unique affine diagonal population;17 forced physical levels',flush=True)
 kap=min((20-e)/41-(intercept-slope*e) for e in (lo,hi));assert kap==F(r['tail_mass_coefficient'])>0
 # The rejected stronger backward line has an actual normalized physical counterexample.
 w=r['failed_backward_bound'];value,_=physical(w);assert value<intercept-slope*lo+(lo-F(w['energy']))/37
 from copy import deepcopy
 faults=[];s,o,c=contact
 for name in ('dual_normalization','dual_sign'):
  d=deepcopy(c)
  if name=='dual_normalization':d['z']=str(F(d['z'])+1)
  else:d['y'][0]='1'
  try:validate_dual(s,o,d)
  except AssertionError:faults.append(name)
  else:raise AssertionError('accepted '+name)
 for name in ('population','shell_completion','return'):
  w=deepcopy(ends[0])
  if name=='population':w['population'][0]=str(F(w['population'][0])+F(1,100))
  elif name=='shell_completion':w['spectrum']=w['support']
  else:w['return_value']=str(F(w['return_value'])-F(1,100))
  try:physical(w)
  except AssertionError:faults.append(name)
  else:raise AssertionError('accepted '+name)
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2027 independent bath-label',n,'exact dual certificates; exhaustive coverage, affine physical attainment, rejected backward bound, positive tail constant;',len(faults),'actual faults;',len(r['inputs']),'provenance hashes',flush=True)
if __name__=='__main__':main()
