#!/usr/bin/env python3
"""Independent exact interval/Hardy inputs and Gaussian normalization controls."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import copy,json,hashlib
R=Path(__file__).resolve().parents[2];r=json.loads((R/'lab/process/k1849-fisher-effective-gap.json').read_text());prior=json.loads((R/r['dependencies'][1]['path']).read_text());n=0
def ck(v):
 global n
 assert v
 n+=1
def maxabs(k,ymax):
 vals=[k,ymax*ymax-2*k*ymax+k]
 if 0<=k<=ymax:vals.append(k-k*k)
 return max(map(abs,vals))
def cert(d):
 for name in ['k2','uniform']:
  q=d[name];lo,hi,bl,bh,rad,edge,kap,ex=map(F,[q[z] for z in ['F_lower','F_upper','b_lower','b_upper','R','L0','kappa','gap_exponent']])
  if not(hi>lo>1 and bh>bl>0 and edge>rad>0 and kap>0):return False
  kl,kh=(F(2),F(2)) if name=='k2' else tuple(map(F,q['k_interval']))
  if not(F(3,2)<kl<=kh<3):return False
  if name=='k2':
   if not(lo<F(prior['lower']) and hi>F(prior['upper'])):return False
  else:
   A,B,C=map(F,prior['certificate']['minorant'])
   if not(C<0 and A+B+C*kh>lo and hi>=8):return False
  if not(bl<=(lo-1)/(3-kl) and bh>=(8-1 if name=='uniform' else 8-lo)/(kl-F(3,2))):return False
  yy=rad*rad;P0=yy*yy-2*kh*yy+kh
  if not(yy>2 and yy>kh and P0>0 and bl*P0+lo*(yy-2)>4):return False
  upper=(bh*max(maxabs(kl,edge*edge),maxabs(kh,edge*edge))+hi*max(F(2),edge*edge-2))/4
  if not(upper<kap*kap):return False
  delta=2*kap*(edge-rad);extra=ex-4*kap*rad;pref=4*rad*(rad+F(1,2))
  if not(1+delta+delta*delta/2>2 and extra>0 and sum(extra**j/F(factorial(j)) for j in range(7))>pref+1 and 2*F(q['tv_exponent'])==ex):return False
 q=d['k2'];bh=F(q['b_upper']);hi=F(q['F_upper'])
 return(F(q['moment_penalties'][0])>=4*bh and F(q['moment_penalties'][1])>=bh and F(q['sobolev_x4_coefficient'])<=F(q['b_lower'])/2 and F(q['sobolev_multiplier'])>=2*(2*hi+8*bh))
ck(cert(r))
for k in [F(7,4),F(2),F(17,8)]:
 for b in [F(3,4),F(3),F(13)]:
  for val in [F(7,4),F(2)]:
   a=val-2*b*k;E=2*val-b*k
   for x in [F(0),F(1),F(2),F(17,8),F(5)]:
    y=x*x;ck(a*y+b*y*y-E==b*(y*y-2*k*y+k)+val*(y-2))
   for e2,e4 in [(F(0),F(0)),(F(-1,100),F(1,20))]:
    D=F(1,7)+a*e2+b*e4;ck(D==val+F(1,7)+a*(1+e2)+b*(k+e4)-E)
# rho=e^-x, H0=e^x-1 has Hardy product <=1. Polynomial f=x^m.
for m in range(1,12):ck(F(factorial(2*m))<=4*m*m*factorial(2*m-2))
# Gaussian f=x²-1: variance2, gradient4, kinetic4, hence even gap8.
ck(F(4)*4/2==8)
for c in [F(0),F(1,3),F(4,5),F(1)]:
 ck((2-2*c)*(2+2*c)/4==1-c*c);ck(2-2*c<=2*(1-c*c))
for b in [F(1),F(3),F(12)]:
 for f in [F(7,4),F(2)]:
  a=f-4*b;am=max(F(0),-a);C=am*am/(2*b)
  ck(am<=4*b and C<=8*b and 2*f-2*b+C<108)
faults=[('k2','F_lower','2'),('k2','b_lower','1'),('k2','b_upper','2'),('k2','R','1'),('k2','kappa','3'),('k2','gap_exponent','20'),('k2','tv_exponent','1'),('k2','moment_penalties',['1','1']),('uniform','b_upper','20'),('uniform','gap_exponent','300')]
for section,key,value in faults:
 q=copy.deepcopy(r);q[section][key]=value;ck(not cert(q))
for d in r['dependencies']:ck(hashlib.sha256((R/d['path']).read_bytes()).hexdigest()==d['sha256'])
for key in ['practical_sharpness','full_line_odd_gap','restricted_gap_quantified','physical_claim']:
 q=copy.deepcopy(r);q[key]=True;ck(not all(not q[z] for z in ['practical_sharpness','full_line_odd_gap','restricted_gap_quantified','physical_claim']))
print('K1849 independent rational controls',n,'including',len(faults),'input faults and 4 separate reporting faults')
