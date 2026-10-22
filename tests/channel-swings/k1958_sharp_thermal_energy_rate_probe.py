"""Independent bath-derived DAG and capped-energy verification, no producer import."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]

def instance(gaps,bits):
 n=len(gaps)+1;bath=[F(8,15),F(4,15),F(2,15),F(1,15)];D=[[F(i==j) for j in range(n)] for i in range(n)];edges=[]
 for i,(d,bit) in enumerate(zip(gaps,bits)):
  lo=sum(bath[:4-d]);hi=sum(bath[d:])
  donor,receiver,rate,diag=(i,i+1,hi,lo) if bit else (i+1,i,lo,hi)
  D[receiver][donor]-=rate;D[receiver][receiver]+=diag;edges.append((donor,receiver,rate))
 def column(j):
  seen={}
  def at(i):
   if i not in seen:seen[i]=(F(i==j)+sum(rate*at(k) for k,r,rate in edges if r==i))/D[i][i]
   return seen[i]
  return [at(i) for i in range(n)]
 R=[column(j) for j in range(n)]
 e=[max(1,3-gaps[0]) if gaps else 1]
 for d in gaps:e.append(e[-1]+d)
 return D,R,e

def audit(D,R,e,sign=-1,moment=F(36)):
 n=len(e);q=F(2,3);W=F(25,8);count=0
 for j,col in enumerate(R):
  assert [sum(D[i][k]*col[k] for k in range(n)) for i in range(n)]==[F(i==j) for i in range(n)],'independent inverse equation'
  assert all(F(0)<=x<=q**abs(i-j) for i,x in enumerate(col)),'independent geometric envelope'
  assert sum(abs(e[i]-e[j])*x for i,x in enumerate(col))<=moment,'independent displacement moment'
  count+=3
 w=list(map(sum,R));p=[F((i+1)**2,sum((k+1)**2 for k in range(n))) for i in range(n)];d=[sum(x*y for x,y in zip(row,p)) for row in D];u=[max(x,0) for x in d];v=[max(-x,0) for x in d]
 assert [sum(R[j][i]*(u[j]+sign*v[j]) for j in range(n)) for i in range(n)]==p,'negative deficit reconstruction'
 m=sum(u);h=W*m-1;slack=sum((W-w[i])*u[i] for i in range(n));loss=sum(w[i]*v[i] for i in range(n));assert h==slack+loss,'slack balance'
 for L in (F(1),F(7,3),F(e[-1]+2)):
  f=[min(x,L) for x in e];lhs=sum(x*y for x,y in zip(e,p));rhs=W*sum(x*y for x,y in zip(f,u))-moment*m-L*h
  assert lhs>=rhs,'capped energy inequality';count+=1
 return count+2

def main():
 count=0;witness=None
 for n in range(1,6):
  for gaps in product((1,2,3),repeat=n-1):
   if any(a+b<4 for a,b in zip(gaps,gaps[1:])):continue
   for bits in product((0,1),repeat=n-1):
    D,R,e=instance(gaps,bits);count+=audit(D,R,e)
    if n==3 and gaps==(2,2) and bits==(0,0):witness=(D,R,e)
 print('PASS independent exact baseline',count)
 D,R,e=witness;caught=[]
 for name in ['wrong_diagonal','wrong_transition','negative_deficit_sign','missing_displacement']:
  dd=[r[:] for r in D];rr=[r[:] for r in R];kwargs={}
  if name=='wrong_diagonal':dd[0][0]+=1
  if name=='wrong_transition':dd[0][1]=-dd[0][1]
  if name=='negative_deficit_sign':kwargs['sign']=1
  if name=='missing_displacement':kwargs['moment']=F(0)
  try:audit(dd,rr,e,**kwargs)
  except AssertionError as err:
   assert str(err) in ['independent inverse equation','negative deficit reconstruction','independent displacement moment'];caught.append(name);print('CAUGHT',name,str(err))
  else:raise AssertionError('mutation not detected: '+name)
 r=json.loads((ROOT/'lab/process/k1958-sharp-thermal-energy-rate.json').read_text())
 def metadata(value):
  assert value['result_id']=='K1958','identity'
  for p,h in value['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'pin'
  assert value['constants']=={'W':'25/8','q':'2/3','c':'163/440','displacement_bound':'36','sharp_log_coefficient':'2/log(3/2)'},'constant identity'
 metadata(r)
 from copy import deepcopy
 for fault in ['identity','pin']:
  bad=deepcopy(r)
  if fault=='identity':bad['result_id']='bad'
  else:bad['inputs'][next(iter(bad['inputs']))]='bad'
  try:metadata(bad)
  except AssertionError as err:assert str(err)==fault
  else:raise AssertionError('undetected metadata fault')
 print('PASS four mathematical faults and two separate metadata faults')
if __name__=='__main__':main()
