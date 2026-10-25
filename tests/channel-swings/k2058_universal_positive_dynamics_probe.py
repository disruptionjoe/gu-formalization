"""Separate exact realification and signed-column controls; no producer imports."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
def mat(n,m=None):return [[Q(0) for _ in range(m or n)] for _ in range(n)]
def eye(n):return [[Q(i==j) for j in range(n)] for i in range(n)]
def plus(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,x):return [[x*v for v in r] for r in a]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def tr(a):return list(map(list,zip(*a)))
def block(a,b,c,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]
def realify(a,b):return block(a,scale(b,-1),b,a)
def signed_word(word):
 result=[]
 for n in range(128):
  bits=[(n>>(6-j))&1 for j in range(7)];sign=1
  for k in reversed(word):
   j=k%7;sign*=(-1)**sum(bits[:j])
   if k>=7:sign*=2*bits[j]-1
   bits[j]^=1
  result.append((sum(b<<(6-j) for j,b in enumerate(bits)),sign))
 return result
def compose(a,b):return [(a[j][0],s*a[j][1]) for j,s in b]
def neg(a):return [(j,-s) for j,s in a]
def checks(mode=None):
 count=0
 def ck(name,v):
  nonlocal count
  assert v,name;count+=1
 I2=eye(2);Z=mat(2);J=[[Q(0),Q(1)],[Q(-1),Q(0)]];I4=eye(4);JJ=realify(J,Z);ii=block(Z,scale(I2,-1),I2,Z);cc=block(I2,Z,Z,scale(I2,-1))
 for r in [Q(1),Q(2),Q(3,2)]:
  T=scale(JJ,-r);inv=scale(JJ,1/r)
  for c,d in [(Q(1),Q(0)),(Q(5,4),Q(3,4)),(Q(17,8),Q(15,8))]:
   P=realify(scale(I2,r*c),scale(J,r*d));bar=mm(mm(cc,P),cc)
   if mode=='omit_conjugation':bar=P
   if mode=='scale_metric':P=scale(P,2);bar=scale(bar,2)
   A=scale(mm(mm(ii,inv),bar),-1);Abar=mm(mm(cc,A),cc)
   ck('Hermitian realification',tr(P)==P);ck('positive two eigenvalues',r*(c-d)>0 and r*(c+d)>0)
   ck('anti square',mm(A,Abar)==scale(I4,-1));ck('kinetic transpose',mm(mm(mm(cc,tr(A)),cc),T)==mm(ii,P))
   ck('conserved allowed T',plus(mm(tr(T),P),mm(P,T))==mat(4))
   if mode=='only_real':ck('nonreal survivor',d==0)
 # anisotropic actual-plane metric succeeds kinetically and fails dynamics
 P=realify([[Q(2),Q(0)],[Q(0),Q(1,2)]],Z);T=JJ;inv=scale(JJ,-1);A=scale(mm(mm(ii,inv),P),-1)
 ck('anisotropic anti square',mm(A,mm(mm(cc,A),cc))==scale(I4,-1));defect=plus(mm(tr(T),P),mm(P,T))
 ck('anisotropic conservation fails',defect==mat(4) if mode=='kinetic_implies_dynamics' else defect!=mat(4))
 # fixed P family differentiated at theta=log4, with rational half-angle square root
 P=realify(scale(I2,Q(17,8)),scale(J,Q(15,8)));S=realify(scale(I2,Q(5,4)),scale(J,Q(3,4)));D=realify(scale(I2,Q(15,8)),scale(J,Q(17,8)));K=scale(mm(ii,JJ),Q(1,2))
 if mode=='connection_sign':K=scale(K,-1)
 ck('metric square root',mm(S,S)==P);ck('derivative is nonzero',D!=mat(4));ck('connection repairs current',plus(mm(tr(K),P),mm(P,K))==D)
 # Independent signed Clifford controls on the actual 128 spinor factor
 ident=[(j,1) for j in range(128)];M=signed_word([0,1,2,10]);G=signed_word(list(range(7,14))+[0]);V=signed_word(list(range(14)))
 ck('actual mass square',compose(M,M)==neg(ident));ck('actual G square',compose(G,G)==neg(ident));ck('mass G commute',compose(M,G)==compose(G,M));ck('mass volume commute',compose(M,V)==compose(V,M))
 cs=[signed_word([0,k]) for k in [7,8,9]]
 for C in cs:
  ck('C square',compose(C,C)==ident);ck('C mass anticommute',compose(C,M)==neg(compose(M,C)));ck('C G commute',compose(C,G)==compose(G,C))
 for j in range(3):
  for k in range(j):ck('spatial Clifford',compose(cs[j],cs[k])==neg(compose(cs[k],cs[j])))
 # Copy polynomial, avoiding radical numerical arithmetic
 A=[[Q(10 if i==j==0 else 4 if i==0 or j==0 else int(i!=j)) for j in range(11)] for i in range(11)];P2=mat(11);P2[0][0]=1
 for i in range(1,11):
  for j in range(1,11):P2[i][j]=Q(1,10)
 AP=mm(A,P2);ck('copy polynomial',mm(AP,AP)==plus(scale(AP,19),scale(P2,70)));perp=plus(eye(11),scale(P2,-1));ck('transverse copy',mm(A,perp)==scale(perp,-1))
 mult=[288,288,32,32,32,32]
 ck('complexification is not halved',sum(mult if mode=='halve_carrier' else [2*x for x in mult])==1408);ck('class dimension',sum(x*x for x in mult)==169984)
 return count
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2058-universal-positive-dynamics.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 assert d['unitary_multiplicities']==[288,288,32,32,32,32] and d['universal_metric_parameters']==6
 print('PASS independent exact obligations',checks());caught=[]
 for m in ['omit_conjugation','scale_metric','only_real','kinetic_implies_dynamics','connection_sign','halve_carrier']:
  try:checks(m)
  except AssertionError as e:caught.append((m,str(e)))
  else:raise AssertionError('missed fault '+m)
 print('PASS six mathematical faults',caught)
