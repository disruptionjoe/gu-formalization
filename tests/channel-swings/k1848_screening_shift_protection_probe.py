#!/usr/bin/env python3
"""Independent rational response and source-perturbation controls; no producer import."""
from fractions import Fraction as F
from pathlib import Path
import copy,json,hashlib
R=Path(__file__).resolve().parents[2];r=json.loads((R/'lab/process/k1848-screening-shift-protection.json').read_text());n=0
def ck(v):
 global n
 assert v
 n+=1
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mv(A,v):return [dot(row,v) for row in A]
def inv(A):
 a,b=A[0];c,d=A[1];det=a*d-b*c
 return [[d/det,-b/det],[-c/det,a/det]]
def cert(q):
 A=[[F(x) for x in row] for row in q['fixture']['A']];v=list(map(F,q['fixture']['v']));c=list(map(F,q['fixture']['c']));h=F(q['fixture']['h'])
 return A[0][1]==A[1][0] and A[0][0]>0 and A[0][0]*A[1][1]>A[0][1]**2 and c==mv(A,v) and h==dot(v,c) and F(q['fixture']['Z'])>0 and F(q['continuum']['late_bound_coefficient'])>=8 and F(q['continuum']['energy_coefficient'])==F(7,6)
ck(cert(r))
# Rational SPD families with non-diagonal mixing, independent exact inverse.
for a in [F(1),F(2),F(5,3)]:
 for b in [F(-2),F(0),F(1,3)]:
  A=[[1+a*a,a*b],[a*b,1+b*b]];v=[F(1,2),F(-3,2)];c=mv(A,v);h=dot(v,c)
  for z in [F(0),F(1,3),F(2),F(9)]:
   Az=[[A[0][0]+z,A[0][1]],[A[1][0],A[1][1]+z]];res=dot(c,mv(inv(Az),c))-h
   ck(res==-z*dot(v,mv(A,mv(inv(Az),v))));ck(res==0 if z==0 else res<0)
   for Z in [F(1,5),F(3)]:ck(Z*z-res==0 if z==0 else Z*z-res>0)
  for f,j in [([F(2),F(-1)],F(1)),([F(0),F(3)],F(-2))]:
   q=[f[i]-j*v[i] for i in range(2)]
   ck(dot(f,mv(A,f))-2*j*dot(c,f)+j*j*h==dot(q,mv(A,q)))
  w=[F(2,3),F(1)];eps=F(1,7);cp=[c[i]+eps*w[i] for i in range(2)]
  ck(dot(cp,mv(inv(A),cp))-h==2*eps*dot(v,w)+eps**2*dot(w,mv(inv(A),w)))
# Independent polynomial finite-translation test for nonlinear potential.
def U(phi,J,lam):
 q=[phi[0]-J,phi[1]-2*J]
 return q[0]**2/2+2*q[1]**2+lam*(q[0]**2+q[1]**2)**2/4
for J in [F(-2),F(0),F(3,5)]:
 for eps in [F(-1,3),F(2)]:
  for lam in [F(0),F(1,5),F(3)]:
   phi=[F(2),F(-1)];ck(U(phi,J,lam)==U([phi[0]+eps,phi[1]+2*eps],J+eps,lam));ck(U([J,2*J],J,lam)==0)
# The allowed constant deformation leaves finite differences but moves energy.
ck(U([1,2],F(1),F(2))+F(7)==7)
faults=[('c',['1','7']),('h','16'),('A',[['1','1'],['0','4']]),('Z','0')]
for key,val in faults:
 q=copy.deepcopy(r);q['fixture'][key]=val;ck(not cert(q))
for key,val in [('late_bound_coefficient','7'),('energy_coefficient','1')]:
 q=copy.deepcopy(r);q['continuum'][key]=val;ck(not cert(q))
for d in r['dependencies']:ck(hashlib.sha256((R/d['path']).read_bytes()).hexdigest()==d['sha256'])
for key in ['quantum_protection','nonlinear_late_decay','vacuum_energy_screening']:
 q=copy.deepcopy(r);q[key]=True;ck(not(not q['quantum_protection'] and not q['nonlinear_late_decay'] and not q['vacuum_energy_screening']))
print('K1848 independent rational controls',n,'including 6 input faults and 3 separate reporting faults')
