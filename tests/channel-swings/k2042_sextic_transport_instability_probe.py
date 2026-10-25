"""Separate exact polynomial interpolation and rational complex dynamics."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
def mul(z,w):return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def power(z,n):
 r=(F(1),F(0))
 for _ in range(n):r=mul(r,z)
 return r
def pot(u):return mul(power(u[:2],2),power((u[2],-u[3]),4))[0]
def derivative(u,j):
 # Central interpolation differentiates every polynomial of degree <=6 exactly.
 out=F(0)
 for step,weight in [(1,F(3,4)),(2,-F(3,20)),(3,F(1,60))]:
  p=list(u);m=list(u);p[j]+=step;m[j]-=step;out+=weight*(pot(p)-pot(m))
 return out
def direct(u,second_frequency=2):
 g=[derivative(u,j) for j in range(4)]
 return [-g[1],g[0],-g[3]/second_frequency,g[2]/second_frequency]
def replay(r):
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input hash'
 # Evaluate producer polynomials, never import its gradient routine.
 for n in range(1,20):
  u=[F(n-7,5),F(2*n-9,7),F(n+1,11),F(4-n,13)];ctx=dict(zip(r['variables'],u))
  f=direct(u);assert [eval(v,{'__builtins__':{}},ctx) for v in r['vector_field']]==f,'vector field'
  assert sum(x*y for x,y in zip(u,f))==0,'positive current'
 for h in [F(1,3),F(1),F(2)]:
  # Differentiate the already quintic vector field by degree-five interpolation.
  u=[F(0),F(0),h,F(0)];jac=[]
  for j in range(4):
   col=[F(0)]*4
   for step,weight in [(1,F(3,4)),(2,-F(3,20)),(3,F(1,60))]:
    p=u.copy();m=u.copy();p[j]+=step;m[j]-=step
    for i,(fp,fm) in enumerate(zip(direct(p),direct(m))):col[i]+=weight*(fp-fm)
   jac.append(col)
  for i in range(4):
   for j in range(4):assert jac[j][i]==eval(r['jacobian'][i][j],{'__builtins__':{}},{'h':h}),'equilibrium derivative'
  assert eval(r['growth_rate'],{'__builtins__':{}},{'h':h})==jac[1][0]>0,'saddle rate'
 # Avoid sqrt(2): z=(1+i)*v, w=Y; invariant mass=2v^2+Y^2.
 for v,Y in [(F(1,5),F(2)),(F(3,7),F(4,9)),(F(1),F(1))]:
  f=direct([v,v,Y,F(0)]);assert f==[2*v*Y**4,2*v*Y**4,-4*v*v*Y**3,F(0)],'transfer plane'
 for q in [F(1,100),F(1,3),F(1,2),F(99,100)]:
  dh=1/q+1/(1-q)+1/(1-q)**2;assert dh*q*(1-q)**2==1,'primitive derivative'
 return {'polynomial_fixtures':19,'jacobian_entries':48,'transfer_planes':3,'primitive_fixtures':4}
def faults(r):
 replay(r);caught=[]
 for name,edit in [('force coefficient',lambda z:z['vector_field'].__setitem__(0,'0')),('saddle sign',lambda z:z['jacobian'][0].__setitem__(1,'-2*h**4')),('growth rate',lambda z:z.__setitem__('growth_rate','h**4'))]:
  z=copy.deepcopy(r);edit(z)
  try:replay(z)
  except AssertionError as e:caught.append([name,str(e)])
  else:raise AssertionError('missed '+name)
 # Actual kinetic-frequency corruption destroys the conserved current.
 u=[F(1),F(1),F(1),F(0)];assert sum(x*y for x,y in zip(u,direct(u,3)))!=0
 caught.append(['kinetic frequency','nonzero norm source'])
 return caught
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2042-sextic-transport-instability.json').read_text());print('BASELINE',replay(r));print('PASS faults',faults(r))
