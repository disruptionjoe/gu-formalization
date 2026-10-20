#!/usr/bin/env python3
"""Independent rational response/moment/atom controls. No symbolic producer import."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2]
r=json.loads((R/'lab/process/k1846-continuum-screening-dephasing.json').read_text());n=0
def ck(v):
 global n
 assert v
 n+=1
def integral_poly(co,a,b):return sum(c*(b**(j+1)-a**(j+1))/F(j+1) for j,c in enumerate(co))
def cert(q):
 a,b=map(F,q['mass_interval']);u,v=map(F,q['cross_weight'])
 if not 0<a<b:return False
 zero=integral_poly([u,v],a,b);hf=integral_poly([0,0,u,v],a,b)
 contact=1/b-1/a
 energy=(1/a-1/b)/2
 norm=(1/a**3-1/b**3)/3
 return (zero==F(q['static_cross'])==0 and hf==F(q['high_frequency_cross'])!=0 and contact==F(q['contact']) and energy==F(q['equilibrium_fluctuation_energy_per_J_squared']) and norm==F(q['inverse_mass_source_norm_squared']))
ck(cert(r))
# Polynomial moments and a symmetric midpoint atom discretization: static cancellation
# is exact for each N, but time-mean-square remains positive.
for N in range(2,16):
 freqs=[F(1)+F(2*j+1,2*N) for j in range(N)];amp=[(w-F(3,2))/N for w in freqs]
 ck(sum(amp)==0);ck(sum(a*a for a in amp)/2>0)
 for z in [F(1,3),F(1),F(7)]:
  c=[F(1)]*N;d=[w*w*(w-F(3,2)) for w in freqs];h=[1/(z+w*w)/N for w in freqs]
  cc=sum(h);cd=sum(v*t for v,t in zip(h,d));dd=sum(v*t*t for v,t in zip(h,d))
  ck(cc>0 and dd>0 and cc*dd-cd*cd>0)
# Independent Taylor coefficients for continuum cosine response from moment integration.
ck(integral_poly([0,0,F(-3,2),F(1)],F(1),F(2))/2==F(1,8))
ck(integral_poly([F(-3,2),F(1)],F(1),F(2))==0)
# Degenerate frequencies must be grouped before the mean-square rule.
terms=[(F(1),F(2)),(F(1),F(-2)),(F(3),F(0))];groups={}
for w,a in terms:groups[w]=groups.get(w,F(0))+a
ck(sum(a*a for a in groups.values())==0)
ck(sum(a*a for _,a in terms)>0)
# Clean baseline precedes real input corruptions.
faults=[]
for key,val in [('cross_weight',['-1','1']),('mass_interval',['0','2']),('contact','1/2'),('high_frequency_cross','1/3'),('inverse_mass_source_norm_squared','1/4')]:
 q=copy.deepcopy(r);q[key]=val;ck(not cert(q));faults.append(key)
# Reporting predicates separate from mathematical inputs.
for key,val in [('source_claim_effect','changed'),('canon_promotion',True),('independent_agent_review',True)]:
 q=copy.deepcopy(r);q[key]=val;ck(not(q['source_claim_effect']=='none' and not q['canon_promotion'] and not q['independent_agent_review']))
print('K1846 independent rational controls',n,'including',len(faults),'input faults and 3 reporting faults')
