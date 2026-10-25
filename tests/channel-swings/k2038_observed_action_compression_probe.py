"""Independent rational raw-action compression and polynomial-variation checks.

No import of the K2038 producer, its graph routine, or its compressed matrix.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def add(*terms):
 d={}
 for c,a in terms:
  for ij,v in a.items():d[ij]=d.get(ij,0)+c*v
 return {ij:v for ij,v in d.items() if v}
def mul(a,b):
 rows={}
 for (i,j),v in b.items():rows.setdefault(i,[]).append((j,v))
 d={}
 for (i,k),v in a.items():
  for j,w in rows.get(k,[]):d[i,j]=d.get((i,j),0)+v*w
 return {ij:v for ij,v in d.items() if v}
def tr(a):return {(j,i):v for (i,j),v in a.items()}
def eye(n):return {(i,i):F(1) for i in range(n)}
def gamma(k):
 # Bit position counting directly from the right; independent from producer.
 q=6-k%7;d={}
 for j in range(128):
  sign=1 if (j>>(q+1)).bit_count()%2==0 else -1
  if k>=7:sign*=1 if j&(1<<q) else -1
  d[j^(1<<q),j]=F(sign)
 return d
def product(xs):
 a=eye(128)
 for x in xs:a=mul(a,x)
 return a
def block(blocks):
 return {(128*a+i,128*b+j):v for (a,b),m in blocks.items() for (i,j),v in m.items()}
def mv(a,v):
 out={}
 for (i,j),c in a.items():out[i]=out.get(i,0)+c*v.get(j,0)
 return {i:c for i,c in out.items() if c}
def plus(*terms):
 d={}
 for c,v in terms:
  for i,w in v.items():d[i]=d.get(i,0)+c*w
 return {i:w for i,w in d.items() if w}
def dot(u,v):return sum((x*v.get(i,0) for i,x in u.items()),F(0))
def main():
 g=list(map(gamma,range(14)));eta=[1]*7+[-1]*7;I=eye(128)
 B=product(g[7:]);V=product(g);W=add((F(3,2),I),(-F(1,2),V));Wb=add((F(3,2),I),(F(1,2),V))
 O=[0,7,8,9];U=[i for i in range(14) if i not in O]
 es={}
 for i in range(14):es[i,0 if i in O else 1+U.index(i)]=add((eta[i],g[i]))
 for j in range(11):es[14,j]=add((2 if j==0 else 1,Wb))
 E=block(es);H=block({(i,i):add((eta[i] if i<14 else 1,B)) for i in range(15)})
 def derivative(k):
  ds={}
  for r in range(14):
   if r==k:ds[r,14]=I
   else:
    for c in range(14):
     if c not in (r,k):ds[r,c]=add((eta[r],product([g[r],g[k],g[c],W])))
  ds[14,k]=add((-eta[k],I))
  return block(ds)
 Y=mul(H,mul(derivative(0),E));T=mul(tr(E),Y)
 A=[[10 if i==j==0 else 4 if i==0 or j==0 else int(i!=j) for j in range(11)] for i in range(11)]
 spin=add((-1,product([B,g[0],Wb])))
 expected=block({(i,j):add((A[i][j],spin)) for i in range(11) for j in range(11)})
 assert T==expected and tr(T)==add((-1,T)),'actual raw compression'
 assert mul(spin,spin)==add((-1,mul(Wb,Wb)))
 assert sum(V.get((i,i),0) for i in range(128))==0
 # Independent copy decomposition: sum-zero transverse space and two-dimensional span.
 for j in range(1,10):
  v=[0]*11;v[j]=1;v[10]=-1
  assert [sum(A[i][k]*v[k] for k in range(11)) for i in range(11)]==[-x for x in v]
 assert A[0][0]==10 and sum(A[0][1:])==40 and A[1][0]==4 and sum(A[1][1:])==9
 # 2x2 uniform-coordinate matrix [[10,40],[4,9]]: trace19 determinant-70.
 assert 10*9-40*4==-70 and 25**2<641<26**2
 assert sum([288**2]*2+[32**2]*4)==169984
 assert 512*513//2-128*129//2==123072
 R=block({(j,r):g[r] for j,r in enumerate([0]+U)})
 assert mul(R,E)==eye(1408)
 Q=add((1,eye(1920)),(-1,mul(E,R)))
 assert not mul(Q,E) and not any(j>=1792 for i,j in R)
 M=product([g[i] for i in (0,1,2,10)]);N=block({(j,j):M for j in range(11)})
 assert tr(N)==add((-1,N)) and mul(N,N)==add((-1,eye(1408)))
 assert mul(T,N)==mul(N,T)
 for k in (7,8,9):
  C=block({(j,j):product([g[0],g[k]]) for j in range(11)})
  assert mul(T,C)==mul(tr(E),mul(H,mul(derivative(k),E)))
  assert tr(C)==C and not add((1,mul(C,N)),(1,mul(N,C)))
 S=mul(T,N);assert tr(S)==S
 u={i:F((i*7+2)%13-6,5) for i in range(1408)}
 z={i:F((i*11+3)%17-8,7) for i in range(1920)}
 psi=mv(E,u);mu=F(2,3);coupling=F(3,5)
 def potential(v,omit=False):
  w=mv(R,v);s=dot(w,mv(S,w))/2;f=plus((mu+coupling*s,mv(N,w)))
  return mu*s+coupling*s*s/2+(0 if omit else dot(mv(Q,v),mv(Y,f)))
 def derivative_poly(fn):
  vals={t:fn(plus((1,psi),(t,z))) for t in [-2,-1,1,2]}
  return (vals[-2]-8*vals[-1]+8*vals[1]-vals[2])/12
 s=dot(u,mv(S,u))/2;flow=plus((mu+coupling*s,mv(N,u)))
 assert derivative_poly(potential)==dot(z,mv(Y,flow)), 'ambient directional quartic derivative'
 assert dot(u,flow)==0 and s!=0,'nontrivial cubic term and norm current'
 # Auxiliary second variation vanishes at arbitrary off-graph point.
 aux={1792+i:F(i%7-3,3) for i in range(128)}
 assert potential(plus((1,z),(1,aux)))-2*potential(z)+potential(plus((1,z),(-1,aux)))==0
 # Complete baseline first, then genuine corrupted constructions.
 faults=[]
 bad=add((1,expected),(1,block({(0,0):spin})))
 assert bad!=T;faults.append('wrong copy coefficient')
 wrong=block({(i,j):add((-A[i][j],product([B,g[0]]))) for i in range(11) for j in range(11)})
 assert wrong!=T;faults.append('omitted chirality weight')
 J=block({(0,1):I,(1,0):add((-1,I))})
 assert tr(J)==add((-1,J)) and mul(T,J)!=mul(J,T);faults.append('energy-only false action')
 wrongmass=product([g[i] for i in (0,1,2,3)])
 assert mul(wrongmass,wrongmass)==I and tr(wrongmass)==wrongmass;faults.append('unstable mass signature')
 assert derivative_poly(lambda v:potential(v,True))!=dot(z,mv(Y,flow));faults.append('omitted off-graph correction')
 # Nonorthogonal coordinate change preserves weighted norm, not the identity norm.
 d=[F(1+i%3) for i in range(1408)]
 NN={(i,j):v*d[j]/d[i] for (i,j),v in N.items()}
 assert tr(NN)!=add((-1,NN))
 assert all(d[i]**2*v+d[j]**2*NN.get((j,i),0)==0 for (i,j),v in NN.items())
 faults.append('untransported metric')
 result=json.loads((ROOT/'lab/process/k2038-observed-action-compression.json').read_text())
 for p,h in result['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 assert result['positive_action_coefficients']['real_dimension']==169984
 print('PASS K2038 independent raw compression, polynomial variation, coordinate metric and',len(faults),'actual faults')
if __name__=='__main__':main()
