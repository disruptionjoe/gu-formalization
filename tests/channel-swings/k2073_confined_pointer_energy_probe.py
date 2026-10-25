"""Separate finite spectral checks, including actual small-probability countercontrols."""
from pathlib import Path
from fractions import Fraction as Q
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]
def check(d):
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 count=0
 for r in d['explicit_resources']:
  e=Q(r['eta']);rho=Q(r['ramp_width']);M=8+4/rho
  assert Q(r['rms_free_upper'])==M,'uniform second moment'
  assert Q(r['negative_energy_upper'])==2*e*M,'negative energy Cauchy bound'
  assert Q(r['absolute_mean_change_upper'])==2*e*(M+2),'mean difference bound'
  assert Q(r['sector_probability_upper'])==4*e*e,'sector probability'
  assert Q(r['radius'])*e==24,'preparation radius';count+=5
 for r in d['tolerance_resources']:
  e=Q(r['eta']);eps=Q(r['epsilon']);assert 24*e<=eps,'simultaneous energy tolerance'
  assert Q(r['negative_energy_upper'])==24*e,'reported energy'
  bell=Q(14,5)*Q(183,200)**2-32*e-16*e*e
  assert Q(r['bell_lower'])==bell>2,'all outcome Bell';count+=3
 r=d['optimized_resource'];x=Q(r['initial_radius']);y=Q(r['ramp_width']);eta=Q(r['eta'])
 assert eta*x==24 and eta*(16+8/y)==Q(r['negative_energy_upper'])==Q(r['epsilon']),'optimized energy resource'
 assert Q(r['control_radius'])==x+30+2*y and Q(r['detector_radius'])==x+30,'optimized radii'
 assert Q(r['strict_center_separation'])==2*(x+30+2*y)+30,'optimized separation'
 # Exact minimization with rational sqrt(1+w)=u; equality and off-minimum controls.
 for u in [Q(2),Q(5),Q(10),Q(100)]:
  w=u*u-1;y0=(u-1)/2
  for y in [y0/2,y0,3*y0/2]:
   x=w-2*y
   if x>0:assert (384+192/y)/x>=384/(u-1)**2;count+=1
 return count+3

def spectral_controls():
 count=0
 # A normalized rational two-mode vector with positive and negative energies.
 # Direct spectral expectation vs norm-probability Cauchy bound, not producer formulas.
 for r in [Q(1,30),Q(1,10),Q(1,3),Q(2,3)]:
  a=(1-r*r)/(1+r*r);b=2*r/(1+r*r);assert a*a+b*b==1
  for lam in [Q(1),Q(5),Q(100),Q(10000)]:
   probability=b*b;negative=lam*probability;rms2=a*a+lam*lam*b*b
   assert negative*negative<=probability*rms2
   for cutoff in [Q(1),Q(10),Q(1000)]:
    tail=probability if lam>=cutoff else Q(0)
    assert tail<=negative/cutoff and tail<=rms2/(cutoff*cutoff);count+=2
   count+=1
 # Same probability, arbitrarily high energy: a forbidden probability-only bound fails.
 b=Q(20,101);p=b*b;assert Q(10000)*p>100*p
 # Mean energy does not bound the second moment: probability 1/N^2 at energy N^2.
 for N in [10,100,1000]:
  q=Q(1,N*N);mean=1-q+q*N*N;second=1-q+q*N**4
  assert mean<2 and second>100;count+=1
 return count
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2073-confined-pointer-energy.json').read_text());count=check(d);sc=spectral_controls();bad=[]
 for name,key in [('rms','rms_free_upper'),('negative','negative_energy_upper'),('mean','absolute_mean_change_upper'),('probability','sector_probability_upper'),('radius','radius')]:
  q=copy.deepcopy(d);q['explicit_resources'][0][key]=str(Q(q['explicit_resources'][0][key])/2);bad.append((name,q))
 q=copy.deepcopy(d);q['tolerance_resources'][-1]['eta']='1/100';bad.append(('tolerance',q))
 for name,q in bad:
  try:check(q)
  except AssertionError as e:assert str(e);print('REJECT',name,str(e))
  else:raise AssertionError('mutation accepted '+name)
 print('PASS',count,'resource checks',sc,'finite spectral checks',len(bad),'real resource faults')
