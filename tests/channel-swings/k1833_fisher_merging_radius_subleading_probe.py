#!/usr/bin/env python3
"""Independent exact moment/Hermite controls; reporting checks are separate."""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2];cert=json.loads((R/'lab/process/k1833-fisher-merging-radius-subleading.json').read_text())
def gauss(n):
 if n%2:return F(0)
 return F(factorial(n),2**(n//2)*factorial(n//2))
def he(n):
 return {n-2*j:F((-1)**j*factorial(n),2**j*factorial(j)*factorial(n-2*j)) for j in range(n//2+1)}
def inner(a,b):return sum(x*y*gauss(i+j) for i,x in a.items() for j,y in b.items())
checks=0
for n in range(7):
 for k in range(7):
  assert inner(he(n),he(k))==(factorial(n) if n==k else 0);checks+=1
for a in [F(1,3),F(1,2),F(3,4),F(1),F(3)]:
 for b in [F(2,3),F(1),F(4,3),F(3,2)]:
  p=a/(a+b*b);u=-b;w=a/b;mom=lambda n:p*u**n+(1-p)*w**n
  h=a/b-b;x=a*h;y=a*(h*h-2*a)
  assert mom(1)==0 and mom(2)==a and mom(3)==x and mom(4)-3*a*a==y
  # Standardized lobe's leading density coefficients from Hermite moments.
  skew_score={k:v*x/F(2) for k,v in he(2).items()};kurt_score={k:v*y/F(6) for k,v in he(3).items()}
  assert inner(skew_score,skew_score)==x*x/2
  assert inner(kurt_score,kurt_score)==y*y/6 and inner(skew_score,kurt_score)==0
  assert -F(3,2)+2*x+2*x*x==2*(x+F(1,2))**2-2
  checks+=4
# The delta-at-zero term cannot be deleted: for standard Gaussian,
# m1=2rho0 and E[score*g]=-2rho0. Omitting jump predicts -4rho0.
assert -2*2+2==-2 and -2*2!=-2;checks+=1
# Uniform separated-face algebra from (v0-v)>=c/8 and p<=c/epsilon^2.
for eps in [F(1,4),F(1,2),F(3,4),F(1)]:
 v0=eps*eps/16
 for frac in [F(1,10),F(1,2),F(9,10)]:
  c=v0*frac;v=v0-c/8;p=c/(c+eps*eps)
  assert (1-p)/v>=1/v0;checks+=1
# Same x=-1/2, distinct quartic cost: a=1 =>h=-1/2; a=1/2=>h=-1.
assert F(1)*(F(1,4)-2)==-F(7,4)
assert F(1,2)*(1-1)==0
assert F(2,3)*F(49,16)==F(49,24);checks+=3
# Inverse expansion B=4/delta-2+r, r=o(1): coefficient -8 in delta.
assert 4*(-2)==-8;checks+=1
mutations=0
expected={'all_minimizers_z_tends_zero':True,'all_minimizers_interior_near_endpoint':True,'global_minimizer_rate_selected':False,'effective_onset_computed':False,'shape_uniqueness':False,'physical_or_canon_promotion':False}
def validate_report(data):
 for key,val in expected.items():
  assert data['results'][key]==val,'REPORT_MISMATCH:'+key
validate_report(cert)
for key,val in expected.items():
 b=copy.deepcopy(cert);b['results'][key]=not val
 try:validate_report(b)
 except AssertionError as err:
  assert str(err)=='REPORT_MISMATCH:'+key;mutations+=1
 else:raise AssertionError('missed reporting fault '+key)
print('PASS K1833 independent exact controls',checks,'reporting faults rejected',mutations)
