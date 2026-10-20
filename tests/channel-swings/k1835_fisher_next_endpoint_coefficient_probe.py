#!/usr/bin/env sage-python
"""Independent rational latent-moment recurrence; no algebraic weights or producer import."""
from sage.all import QQ,PowerSeriesRing,PolynomialRing,binomial,factorial
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2];cert=json.loads((R/'lab/process/k1835-fisher-next-endpoint-coefficient.json').read_text());checks=0

def independently(refined):
 S=PowerSeriesRing(QQ,'e',default_prec=64);e=S.gen();a=(1-e*e)/2 if refined else S(QQ(1)/2);h=-1/(1-e*e) if refined else S(-1)
 # W has mean0 and satisfies W^2=hW+a. All moments rational, including moving a,h.
 mom=[S(1),S(0)]
 for n in range(2,17):mom.append(h*mom[-1]+a*mom[-2])
 Epow=[sum((binomial(QQ(j)/2,k)*e**(4*k)*mom[k] for k in range(16)),S(0)) for j in range(13)]
 mean=Epow[1];t=((2-e**6)/(2-a*e**8)).sqrt();v=1-t;s2=1-t*mean*mean;sd=e**3*(s2/e**6).sqrt();norm=[]
 for j in range(13):norm.append(t**(QQ(j)/2)*sum((binomial(j,k)*(-mean)**(j-k)*Epow[k] for k in range(j+1)),S(0))/sd**j)
 def gm(k):return QQ(factorial(k))/(2**(k//2)*factorial(k//2)) if k%2==0 else QQ(0)
 moments=[sum((binomial(n,2*k)*gm(2*k)*(v/s2)**k*norm[n-2*k] for k in range(n//2+1)),S(0)) for n in range(13)]
 P=PolynomialRing(QQ,'y');y=P.gen();he=[P(1),y]
 for n in range(1,12):he.append(y*he[-1]-n*he[-2])
 density=[P(1)]+[P(0)]*12
 for n in range(1,13):
  hn=sum((coef*moments[k] for k,coef in enumerate(he[n].list())),S(0))/factorial(n)
  for i in range(13):density[i]+=hn[i]*he[n]
 inverse=[P(1)]+[P(0)]*12
 for i in range(1,13):inverse[i]=-sum((density[k]*inverse[i-k] for k in range(1,i+1)),P(0))
 ds=[d.derivative() for d in density]
 D=[]
 for n in range(13):
  p=sum((ds[i]*ds[j]*inverse[n-i-j] for i in range(n+1) for j in range(n-i+1)),P(0));D.append(sum(co*gm(k) for k,co in enumerate(p.list())))
 return ((1+S(D).add_bigoh(13))/s2-1),D
for refined in [False,True]:
 J,D=independently(refined)
 for k,val in [(-6,4),(0,-2),(2,0),(4,QQ(3)/8),(6,-QQ(6)/5 if refined else QQ(3)/10)]:assert J[k]==val,(refined,k,J[k]);checks+=1
 assert all(J[k]==0 for k in [-5,-3,-1,1,3,5]);checks+=1
 row=cert['refined_D_coefficients' if refined else 'fixed_D_coefficients']
 for k,v in row.items():assert D[int(k)]==QQ(v);checks+=1
# Gaussian triple products responsible for the order10 denominator correction.
P=PolynomialRing(QQ,'y');y=P.gen();H2=y*y-1;H3=y**3-3*y;H4=y**4-6*y*y+3

def gm(k):return QQ(factorial(k))/(2**(k//2)*factorial(k//2)) if k%2==0 else QQ(0)
def integ(p):return sum(c*gm(k) for k,c in enumerate(p.list()))
assert integ(H2*H3*H3)==36 and integ(H2*H2*H4)==24;checks+=2
# Uniform-window excess and refinement square are independently exact.
for alpha in [QQ(-2),QQ(-1)/3,0,QQ(3)/4]:
 for beta in [QQ(-3),0,QQ(3)/2,QQ(2)]:
  assert QQ(3)/8+2*alpha*alpha+QQ(2)/3*beta*beta>=QQ(3)/8
  assert QQ(3)/10-2*beta+QQ(2)/3*beta*beta== -QQ(6)/5+QQ(2)/3*(beta-QQ(3)/2)**2
  checks+=2
expected={'compact_window_unique_minimizer':True,'fixed_witness_eventually_nonminimal':True,'global_next_coefficient_proved':False,'global_minimizer_rates_proved':False,'effective_onset':False,'physical_or_canon_promotion':False}
def report(c):
 for k,v in expected.items():assert c['results'][k]==v
report(cert);faults=0
for k,v in expected.items():
 bad=copy.deepcopy(cert);bad['results'][k]=not v
 try:report(bad)
 except AssertionError:faults+=1
assert faults==len(expected)
print('PASS K1835 independent rational probe',checks,'mathematical controls;',faults,'reporting faults rejected')
