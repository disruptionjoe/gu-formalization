"""Independent polygon integration and conjugate inequalities for the actual phase dual."""
from pathlib import Path
from fractions import Fraction as F
import json,copy
ROOT=Path(__file__).resolve().parents[2];M=F(23,100)
def polygon_area(a,b,c,d):
 points=[(a,c),(b,c),(b,d),(a,d)]
 for sign,offset in [(1,F(0)),(-1,F(9))]:
  old=points;points=[]
  for x,y in zip(old,old[1:]+old[:1]):
   fx=sign*(x[1]-x[0])+offset;fy=sign*(y[1]-y[0])+offset
   if fx>=0:points.append(x)
   if (fx>=0)!=(fy>=0):
    t=fx/(fx-fy);points.append(tuple(p+t*(q-p) for p,q in zip(x,y)))
 return abs(sum((x[0]*y[1]-y[0]*x[1] for x,y in zip(points,points[1:]+points[:1])),F(0)))/2
def ip(c,iv):
 a=b=F(0)
 for q in reversed(c):
  v=[a*iv[0],a*iv[1],b*iv[0],b*iv[1]];a,b=min(v)+q,max(v)+q
 return a,b
def check(d):
 tl,tr=map(F,d['root_interval']);ll,lr=map(F,d['lambda_interval']);P=[-138,392,-168,-102,101]
 ev=lambda x:sum(F(c)*x**i for i,c in enumerate(P))
 assert F(9,20)<tl<tr<F(23,50) and ev(tl)<0<ev(tr),'algebraic root'
 dl,dr=ip([F(-7,100),F(69,200),F(-77,200)],(tl,tr));kl,kr=ip([F(1,6),0,F(-1,2),F(2,3),F(-1,4)],(tl,tr));assert 0<kl and ll<=dl/kr<=dr/kl<=lr,'lambda enclosure'
 T=(tl+tr)/2;L=(ll+lr)/2
 pieces=[(F(0),T,[0,-1+L*(1-T)**2/2]),(T,F(1),[-L*T*T/2,-1+L*(1+T*T)/2,-L/2]),(F(1),F(2),[-1]),(F(2),F(3),[-3-3*L,1+5*L/2,-L/2])]
 def prim(x):
  x=abs(x);s=F(0)
  for a,b,c in pieces:
   if x>a:s+=sum(v*(min(x,b)**(i+1)-a**(i+1))/F(i+1) for i,v in enumerate(c))
  return s
 c=d['certificate'];q=list(map(F,c['row_potentials']));r=list(map(F,c['column_potentials']));n=len(q);u=[-3+F(6*i,n) for i in range(n+1)];z=[-3+F(6*i,n) for i in range(len(r)+1)]
 assert z[-1]==12 and n==c['grid_rows'],'grid geometry'
 lin=sum(2*q[i]*(prim(u[i+1])-prim(u[i])) for i in range(n));pen=F(0);area=F(0);norm=F(0);sat=F(0);count=0;row=[F(0)]*n;col=[F(0)]*len(r);colarea=[F(0)]*len(r)
 for i,x in enumerate(q):
  for j,y in enumerate(r):
   a=polygon_area(u[i],u[i+1],z[j],z[j+1]);h=x+y;v=max(-M,min(M,h));conjugate=h*v-v*v/2
   pen+=a*conjugate;area+=a;norm+=a*v*v;row[i]+=a*v;col[j]+=a*v;colarea[j]+=a
   if abs(h)>=M:sat+=a
   count+=1
 assert area==54,'whole strip area'
 err=2*((lr-ll)/4+F(7,100)*(tr-tl)/2)*sum(abs(q[i])*(u[i+1]-u[i]) for i in range(n));lo=2*(lin-pen-err);up=54*M*M
 assert lo==F(c['squared_norm_lower_bound']) and err==F(c['forcing_error']),'dual lower bound'
 assert up==F(c['squared_norm_upper_bound']) and up-lo==F(c['strong_error_squared_upper_bound']),'strong bound'
 assert norm==F(c['clipped_witness_norm_squared']) and sat==F(c['saturated_witness_area']),'witness norm'
 resid=sum((row[i]-2*(prim(u[i+1])-prim(u[i])))**2/(9*(u[i+1]-u[i])) for i in range(n))+sum(v*v/a for v,a in zip(col,colarea));assert resid==F(c['cell_mean_residual_squared']) and resid>0,'finite infeasibility'
 assert sum(v*v/a for v,a in zip(col,colarea))==F(c['column_residual_squared'])>0,'exact column residual'
 # Independently test the exact strong Fenchel inequality on clipped and unclipped regimes.
 for h in [F(-3),-M,F(-1,10),F(0),F(1,10),M,F(3)]:
  v=max(-M,min(M,h));star=h*v-v*v/2
  for w in [-M,F(-1,10),F(0),F(1,10),M]:
   assert w*w/2+star-h*w>=(w-v)**2/2,'strong conjugate';count+=1
 return count
if __name__=='__main__':
 d=json.load(open(ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json'));n=check(d);faults=[]
 for kind in ['root','potential','lower','strong']:
  b=copy.deepcopy(d);c=b['certificate']
  if kind=='root':b['root_interval']=['1/10','1/5']
  if kind=='potential':c['row_potentials'][0]=str(F(c['row_potentials'][0])+1)
  if kind=='lower':c['squared_norm_lower_bound']='3'
  if kind=='strong':c['strong_error_squared_upper_bound']='0'
  try:check(b)
  except AssertionError as e:faults.append((kind,str(e)))
  else:raise AssertionError('undetected '+kind)
 print('PASS K1989 independent',n,'polygon/conjugate controls; faults',faults)
