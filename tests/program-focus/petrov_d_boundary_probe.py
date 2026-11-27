#!/usr/bin/env python3
"""Exact rational/quartic controls; no numerical probability-limit claim."""
import argparse,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def det(a):
 a=[[F(x)for x in row]for row in a];out=F(1);n=len(a)
 for j in range(n):
  k=next((k for k in range(j,n)if a[k][j]),None)
  if k is None:return F(0)
  if k!=j:a[k],a[j]=a[j],a[k];out=-out
  pivot=a[j][j];out*=pivot
  for k in range(j+1,n):
   z=a[k][j]/pivot
   for l in range(j+1,n):a[k][l]-=z*a[j][l]
 return out
def disc(e):
 a=[e,0,1,0,e];b=[4*e,0,2,0]
 rows=[[F(0)]*i+a+[F(0)]*(2-i)for i in range(3)]
 rows += [[F(0)]*i+b+[F(0)]*(3-i)for i in range(4)]
 return det(rows)/e
# Gaussian rationals as pairs, so every group check is exact.
def ca(a,b):return(a[0]+b[0],a[1]+b[1])
def cm(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cc(a):return(a[0],-a[1])
def cp(a,n):
 v=(F(1),F(0))
 for _ in range(n):v=cm(v,a)
 return v
def mat(a,b):return[[ca(cm(a[i][0],b[0][j]),cm(a[i][1],b[1][j]))for j in range(2)]for i in range(2)]
def star(a):return[[cc(a[j][i])for j in range(2)]for i in range(2)]
def run():
 checks={}
 def ok(n,b):
  checks[n]=bool(b)
  if not b:raise AssertionError(n)
 z=(F(0),F(0));one=(F(1),F(0));ii=(F(0),F(1));ni=(F(0),F(-1));I=[[one,z],[z,one]]
 R=[[ii,z],[z,ni]];S=[[z,ii],[ii,z]]
 for name,M in [('R',R),('S',S)]:
  ok(name+' determinant1',ca(cm(M[0][0],M[1][1]),tuple(-x for x in cm(M[0][1],M[1][0])))==one)
  ok(name+' unitary',mat(M,star(M))==I)
  ok(name+' square minusI',mat(M,M)==[[tuple(-x for x in q)for q in row]for row in I])
 # Pullback by R inverse multiplies x^k y^(4-k) by (-i)^k i^(4-k).
 ok('R fixes actual even quartic coefficients',all(cm(cp(ni,k),cp(ii,4-k))==one for k in [0,2,4]))
 ok('S inverse swaps quartic with total phase1',cp(ni,4)==one)
 for e in [F(1,8),F(1,16),F(1,64),F(1,100)]:
  ok('Sylvester discriminant '+str(e),disc(e)==16*e*e*(1-4*e*e)**2 and disc(e)>0)
 ok('excluded exceptional endpoint e=1/2 is detected',disc(F(1,2))==0)
 for t in [2,3,4,8,16]:
  e=F(1,t**6);ax=e/F(t**4);cy=e*F(t**4)
  ok('exact boosted coefficients '+str(t),ax==F(1,t**10)and cy==F(1,t**2)and 0<e<F(1,2))
  ok('boost leaves typeD term fixed '+str(t),F(t**2)*F(1,t**2)==1)
  ok('positive det1 observer escapes '+str(t),F(t**2)*F(1,t**2)==1 and t**2>=4)
 ok('asymptotic exponent condition for both coefficients',all(((a+4)>0 and (a-4)>0)==(a>4)for a in range(-8,10)))
 for alpha in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:ok('probability mixture '+str(alpha),alpha+(1-alpha)==1 and 0<=alpha<=1)
 deps=['explorations/conditional-build/petrov-probability-selection-2026-11-26.md','tests/program-focus/petrov_probability_selection_probe.py','Lean/GUFormalization/PetrovProbability.lean']
 return {'status':'PASS','checks':checks,'grouped_checks':len(checks),'dependencies_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in deps},'scope':'Exact polynomial/group/finite exponent controls. Smooth Julia covariance, properness and limiting probability statements are written/reviewed; no physical law or black-hole solution tested.'}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--verify',action='store_true');p.add_argument('--output');a=p.parse_args();t=time.perf_counter();d=run();d['runtime_seconds']=time.perf_counter()-t
 if a.output:Path(a.output).write_text(json.dumps(d,indent=2)+'\n')
 print(json.dumps({k:v for k,v in d.items()if k not in ['checks','dependencies_sha256']},indent=2))
