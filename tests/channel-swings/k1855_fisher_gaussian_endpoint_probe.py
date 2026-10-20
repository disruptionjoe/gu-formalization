#!/usr/bin/env python3
"""Separate Fraction polynomial/moment implementation of K1855 finite premises."""
from fractions import Fraction as Q
from pathlib import Path
from copy import deepcopy
import json,math
ROOT=Path(__file__).resolve().parents[2]
def trim(p):
 p=list(map(Q,p))
 while len(p)>1 and p[-1]==0:p.pop()
 return p
def add(p,q):
 z=[Q(0)]*max(len(p),len(q))
 for i,a in enumerate(p):z[i]+=a
 for i,a in enumerate(q):z[i]+=a
 return trim(z)
def scale(p,a):return trim([Q(a)*x for x in p])
def mul(p,q):
 z=[Q(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):z[i+j]+=a*b
 return trim(z)
def sub(p,q):return add(p,scale(q,-1))
def power(p,n):
 z=[Q(1)]
 for _ in range(n):z=mul(z,p)
 return z
def deriv(p):return trim([i*p[i] for i in range(1,len(p))] or [0])
def value(p,x):
 z=Q(0)
 for a in reversed(p):z=z*x+a
 return z
def gm(n):
 if n%2:return Q(0)
 return Q(math.factorial(n),2**(n//2)*math.factorial(n//2))
def expectation(p):return sum(a*gm(i) for i,a in enumerate(p))
def interval_lower(p,m,zero_order=0):
 assert all(a==0 for a in p[:zero_order]),'expected order of vanishing'
 p=p[zero_order:]
 return p[0]+sum(min(Q(0),a)*m**i for i,a in enumerate(p[1:],1))
def verify(d):
 n=0
 def ok(c,w):
  nonlocal n
  assert c,w;n+=1
 for a in [Q(1,1000),Q(1,6),Q(1),Q(4)]:
  den=[1,0,a*Q(d['denominator_quadratic'])]
  num=add(mul([0,1],den),[0,a*d['score_linear'],0,a*d['score_cubic']])
  # Whole polynomial numerator from quotient derivative, independent of Sympy.
  W=sub(scale(sub(mul(deriv(num),den),mul(num,deriv(den))),2),mul(num,num))
  P=[2-6*a,0,-1+12*a,0,-2*a-2*a*a]
  residual=sub(W,mul(P,mul(den,den)))
  expected=[0,0,0,0,a**3*Q(d['remainder_coefficients'][0],2),0,a**3*Q(d['remainder_coefficients'][1],2),0,a**3*(d['remainder_coefficients'][2]+a)/2]
  ok(trim(residual)==trim(expected),'whole-line score residual coefficients')
  ok(d['remainder_coefficients']==[3,-2,1],'sum of squares residual')
 H=list(map(Q,d['hermite']));Hsq=mul(H,H)
 ok(expectation(H)==0,'Hermite orthogonality constant')
 ok(expectation(mul([0,0,1],H))==0,'Hermite orthogonality quadratic')
 ok(expectation(Hsq)==d['gaussian_h4_norm'],'Hermite norm')
 N=[1,-2*expectation(H),expectation(Hsq)]
 m2=[1,-2*expectation([0,0]+H),expectation([0,0]+Hsq)]
 m4=[3,-2*expectation([0,0,0,0]+H),expectation([0,0,0,0]+Hsq)]
 ok(trim(m2)==trim(d['m2_numerator']),'second moment polynomial')
 ok(trim(m4)==trim(d['m4_numerator']),'fourth moment polynomial')
 E=[0,0,expectation(mul(deriv(H),deriv(H)))]
 Inum=add(sub(scale(N,2),m2),scale(E,d['kinetic']))
 ok(trim(Inum)==trim(m2),'signed-square kinetic identity')
 Qn=sub(scale(mul(m2,m2),3),mul(m4,N));Qd=mul(m2,m2)
 Jn=sub(mul(Inum,m2),mul(N,N));Jd=mul(N,N)
 ok(Jn[2]/Qn[1]**2==Q(d['leading_coefficient']),'sharp coefficient')
 mean=(gm(8)-2*gm(6)+3*gm(4))/2
 ok(mean==d['residual_gaussian_mean'],'Gaussian residual integral')
 ok(Q(1,18)+mean/216==Q(d['cubic_coefficient']),'cubic lower matching')
 cubic_num=sub(scale(mul(Jn,power(Qd,2)),6),mul(mul(Qn,Qn),Jd))
 ok(all(v==0 for v in cubic_num[:3]),'cubic order')
 ok(cubic_num[3]/(6*Qn[1]**3)==Q(d['cubic_coefficient']),'cubic trial upper matching')
 ok(Q(d['budget_correction'])/3+Q(3,2)==0,'inverse budget correction')
 # Derive all four interval polynomials without importing producer expressions.
 polys=[(sub(mul(deriv(Qn),Qd),mul(Qn,deriv(Qd))),0),
        (sub(Qn,mul([0,46],Qd)),1),(sub(mul([0,48],Qd),Qn),2),
        (sub(mul(mul(Qn,Qn),mul(add(Qd,scale(Qn,d['upper_factor'])),Jd)),scale(mul(Jn,power(Qd,3)),6)),3)]
 m=Q(d['s_max'])
 for i,(p,k) in enumerate(polys):ok(interval_lower(p,m,k)>0,'whole interval polynomial '+str(i))
 ok(value(Qn,m)/value(Qd,m)>Q(d['q_max']),'finite window coverage')
 ok(Q(d['q_max'])==Q(1,25),'declared window')
 for s in [Q(1,100000),Q(1,10000),Q(1,1000)]:
  q=value(Qn,s)/value(Qd,s);J=value(Jn,s)/value(Jd,s)
  ok(q*q/(2*(3-q))<=J,'trial above universal dual')
  ok(J<=q*q*(1+2*q)/6,'finite-window trial bracket')
  ok(value(m2,s)/value(N,s)>0,'variance scaling')
 for key in ['optimizer_equals_trial','sixth_moment_required','novelty']:ok(d[key] is False,'scope '+key)
 return n
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1855-fisher-gaussian-endpoint.json').read_text());print('K1855 independent polynomial/moment groups PASS',verify(d))
 faults={'score_cubic':2,'score_linear':-2,'denominator_quadratic':'1/3','hermite':[4,0,-6,0,1],'kinetic':2,'gaussian_h4_norm':25,'m2_numerator':[1,0,215],'m4_numerator':[3,-48,2951],'remainder_coefficients':[2,-2,1],'leading_coefficient':'1/5','s_max':'1/10','q_max':'1/10','upper_factor':1,'cubic_coefficient':'1/5','residual_gaussian_mean':41,'budget_correction':'-3'}
 reporting={'optimizer_equals_trial':True,'sixth_moment_required':True,'novelty':True}
 for kind,changes in [('input',faults),('reporting',reporting)]:
  for key,v in changes.items():
   bad=deepcopy(d);bad[key]=v
   try:verify(bad)
   except AssertionError as e:print('[FAIL detected]',kind,key,str(e))
   else:raise AssertionError('undetected '+key)
 print('PASS 16 mathematical input faults and 3 reporting faults; no crash catches')
