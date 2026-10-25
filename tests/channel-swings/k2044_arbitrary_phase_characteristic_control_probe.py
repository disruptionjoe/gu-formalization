"""Independent rational directional differentiation and bound controls."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def power(a,n):
 r=(F(1),F(0))
 for _ in range(n):r=mul(r,a)
 return r
def potential(q):return mul(power((q[0],q[1]),2),power((q[2],-q[3]),4))[0]
def derivative(q,j):
 # Degree-six centered interpolation: exact for this polynomial, independent of symbolic producer.
 vals={}
 for k in [-3,-2,-1,1,2,3]:
  t=q.copy();t[j]+=k;vals[k]=potential(t)
 return (vals[3]-vals[-3])/60-3*(vals[2]-vals[-2])/20+3*(vals[1]-vals[-1])/4

def check(report=None,force_scale=F(1),w_kinetic=F(2),flux_factor=F(2),threshold=F(2)):
 for n in range(1,25):
  q=[F((n*(j+2))%13-6,j+2) for j in range(4)];g=[derivative(q,j) for j in range(4)]
  dz=mul((F(0),2),mul((q[0],-q[1]),power((q[2],q[3]),4)));dw=mul((F(0),force_scale*2),mul(power((q[0],q[1]),2),power((q[2],-q[3]),3)))
  f=list(dz+dw)
  if report is not None:assert [eval(v,{'__builtins__':{}},dict(zip(['x','y','u','v'],q))) for v in report['force']]==f,'reported force'
  assert f==[-g[1],g[0],-g[3]/w_kinetic,g[2]/w_kinetic],'real force'
  a=q[0]**2+q[1]**2;b=q[2]**2+q[3]**2;sa=2*sum(q[j]*f[j] for j in [0,1]);sb=2*sum(q[j]*f[j] for j in [2,3]);assert sa+sb==0,'current'
  assert sa*sa+16*potential(q)**2==16*a*a*b**4,'source magnitude'
 # Divergence theorem boundary coefficient: rho-j=2b and rho+j=2a.
 for a,b in [(F(2,3),F(7,5)),(F(0),F(3)),(F(5),F(0))]:
  rho,j=a+b,a-b;assert rho-j==flux_factor*b and rho+j==flux_factor*a,'null flux'
 for M,B in [(F(1,10),F(1,3)),(F(1),F(1,10)),(F(1,2),F(9,10))]:
  exact_reciprocal=1/B-4*M/2;proposed=1/B-threshold*M
  assert proposed<=exact_reciprocal,'reciprocal underestimate'
  assert 1/(B/(1-2*M*B))==exact_reciprocal>0
 return {'field_fixtures':24,'directional_derivatives':96,'flux_fixtures':3,'bound_fixtures':3}
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2044-arbitrary-phase-characteristic-control.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',check(report=r));caught=[]
 for label,kw in [('force coefficient',{'force_scale':F(3,2)}),('kinetic frequency',{'w_kinetic':F(1)}),('null flux',{'flux_factor':F(1)}),('weakened smallness',{'threshold':F(1)})]:
  try:check(**kw)
  except AssertionError as e:caught.append([label,str(e)])
  else:raise AssertionError('missed '+label)
 print('PASS four actual algebra/bound faults',caught)
 corrupted=copy.deepcopy(r);corrupted['force'][0]='0'
 try:check(report=corrupted)
 except AssertionError as e:assert str(e)=='reported force';print('PASS separate reported-force corruption')
 else:raise AssertionError('missed report corruption')
