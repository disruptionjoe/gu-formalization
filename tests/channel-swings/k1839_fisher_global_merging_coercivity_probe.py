#!/usr/bin/env python3
"""Independent Fraction moment controls and rational asymptotic diagnostics."""
import copy,json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def normal(n):return F(0) if n%2 else F(math.factorial(n),2**(n//2)*math.factorial(n//2))
def moments(p,a,v):
 return [sum(w*sum(F(math.comb(n,j))*loc**(n-j)*v**(j//2)*normal(j) for j in range(0,n+1,2)) for w,loc in [(p,-(1-p)*a),(1-p,p*a)]) for n in range(9)]
def main():
 checks=0
 def ck(x):
  nonlocal checks
  assert x;checks+=1
 for p in [F(1,10000),F(1,12),F(1,3),F(1,2),F(2,3),F(11,12),F(9999,10000)]:
  for a,v in [(F(1,10),F(1,7)),(F(2),F(1,100)),(F(10),F(1,3))]:
   M=moments(p,a,v);S=M[2];k4=M[4]-3*S*S
   ck(M[0]==1 and M[1]==0)
   ck(M[3]==p*(1-p)*(2*p-1)*a**3)
   ck(k4==p*(1-p)*(1-6*p*(1-p))*a**4)
   g2=M[4]-S*S;g3=M[6]-6*S*M[4]+9*S**3
   ck(g2>0 and g3>0 and S*g2-M[3]**2>0)
   ck(S*g3-k4*k4>0)
   qs=[{1:F(1)},{2:F(1),0:-S},{3:F(1),1:-3*S,0:-M[3]},{4:F(1),2:-6*S,1:-4*M[3],0:3*S*S-k4}]
   G=[[sum(co*do*M[k+l] for k,co in q.items() for l,do in u.items()) for u in qs] for q in qs]
   for j,q in enumerate(qs):
    ck(sum(co*M[k] for k,co in q.items())==0)
    ck(sum(k*co*M[k-1] for k,co in q.items() if k)==(1 if j==0 else 0))
   # Fraction LDL, independent of the producer's symbolic determinant.
   C=copy.deepcopy(G)
   for j in range(4):
    pivot=C[j][j];ck(pivot>0)
    for i in range(j+1,4):
     for k in range(j+1,4):C[i][k]-=C[i][j]*C[j][k]/pivot
   ck(G[0][3]==M[5]-10*S*M[3])
   # Reverse atoms reverses third cumulant and preserves the Gram norms.
   N=moments(1-p,a,v);ck(N[3]==-M[3] and N[4]==M[4] and N[6]==M[6])
 def chart(aa,bb,v):
  z=1-aa*aa;r=bb*bb-1;c=z*r;p=r/(r+z);t=1-v;delta=2-(2-c)*t*t;mean=p*aa+(1-p)*bb
  mu=lambda n:p*(aa-mean)**n+(1-p)*(bb-mean)**n
  S=v+t*mu(2);m3sq=t**3*mu(3)**2;k4=t*t*(mu(4)-3*mu(2)**2)
  m4=3*v*v+6*v*t*mu(2)+t*t*mu(4);m6=15*v**3+45*v*v*t*mu(2)+15*v*t*t*mu(4)+t**3*mu(6)
  g3=m6-6*S*m4+9*S**3
  ck(mu(2)==c/(aa+bb)**2 and mu(3)==c*(r-z)/(aa+bb)**3)
  ck(k4==t*t*c*((r-z)**2-2*c)/(aa+bb)**4)
  return delta,z,r,c,S,m3sq,k4,g3,m4
 rare=[];merge=[]
 for n in [10,100,1000,10000]:
  delta,z,r,c,S,m3sq,k4,g3,m4=chart(1-F(1,n),1+F(1,n**4),F(1,n**3))
  ell=c*z/delta**2;lower=1/S+k4*k4/(S*S*g3)-1-4/delta;rare.append(lower)
  ck(z*z>delta and r*r<delta and k4>0)
  ck(g3<100*(delta**3+c*z**4))
  delta,z,r,c,S,m3sq,k4,g3,m4=chart(1-F(1,n*n),1+F(1,2*n*n),F(1,2*n**3))
  ell=c*(z-r)/delta**2;excess=m3sq/(S*S*(m4-S*S));merge.append(abs(ell-F(1,2)))
  ck(z*z<delta and r*r<delta)
  ck(abs(excess-2*ell*ell)<F(20,n))
 ck(all(rare[i+1]>rare[i] for i in range(3)));ck(rare[-1]>10)
 ck(all(merge[i+1]<merge[i] for i in range(3)))
 # Exact bound identity and its one-sided sharp constant.
 for u in [F(1,100),F(1,4),F(1,2),F(3,4),F(99,100)]:ck(u*(1-u)<=F(1,4))
 v=json.loads((ROOT/'lab/process/k1839-fisher-global-merging-coercivity.json').read_text())
 def report(q):
  r=q['results'];assert r['global_minimizers_z_over_sqrt_delta_tends_zero'] and r['global_minimizers_r_over_sqrt_delta_tends_zero'];assert r['global_skew_c_times_z_minus_r_over_delta_squared']=='1/2';assert not r['compact_K1835_scaling_proved'] and not r['global_next_coefficient_proved'] and not r['global_uniqueness_proved']
 report(v);mut=0
 for key in ['global_minimizers_z_over_sqrt_delta_tends_zero','compact_K1835_scaling_proved','global_next_coefficient_proved','global_uniqueness_proved']:
  q=copy.deepcopy(v);q['results'][key]=not q['results'][key]
  try:report(q)
  except AssertionError:mut+=1
  else:raise AssertionError('reporting fault escaped')
 print('PASS K1839 probe',checks,'independent rational controls;',mut,'reporting faults')
 print('Rare-sequence lower-bound diagnostics',list(map(float,rare)))
if __name__=='__main__':main()
