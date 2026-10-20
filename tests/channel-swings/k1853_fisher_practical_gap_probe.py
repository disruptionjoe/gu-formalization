#!/usr/bin/env python3
"""Independent arithmetic and input-fault controls; no import of producer."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]
def check(d):
 a,b,c=map(F,d['N']);u,v,w=map(F,d['D']);assert min(u,v,w)>0
 assert b*u-a*v>0 and 2*(c*u-a*w)>0 and c*v-b*w>0
 # Independently refined Darboux enclosure, including every partial cell.
 val=lambda y:(a+b*y+c*y*y)/(u+v*y+w*y*y)
 step=F(1,64);lower=upper=F(0)
 lo=hi=F(0)
 for j in range(256):
  left=val(j*step);right=val((j+1)*step)
  lo=min(lo,lower+min(F(0),step*left/2))
  hi=max(hi,upper+max(F(0),step*right/2))
  lower+=step*left/2;upper+=step*right/2
 assert lo>F(d['potential_lower'])>=-F(1,5)
 assert hi<F(d['potential_upper'])<=2
 # Validate inherited tail polynomial independently after y=z+9/4.
 A=a-u;B=b-v;C=c-w;t=F(9,4)
 assert C>0 and B+2*C*t>0 and A+B*t+C*t*t>0
 ref=F(d['reference_density_lower']);assert 0<ref<=F(1,25)
 assert d['second_moment']==1 and d['fourth_moment']==2
 eps=F(d['delta']);assert eps==F(243,200000)
 assert eps/(2*ref)<F(1,64)
 lower_true=ref*(F(6,7)-F(1,8))**2
 m=F(d['true_density_lower']);assert 0<m<=lower_true
 bound=1/m+F(1,4);assert bound<d['gap_denominator']
 # Actual transform -4d² supplies 4 times the Dirichlet form;
 # Hardy constant4B therefore leaves spectral lower bound1/B.
 assert F(d['kinetic_coefficient'],4)==1
 assert d['gap_denominator']*eps<F(36,625)
 return True
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1853-fisher-practical-gap.json').read_text());assert check(d)
 mutations=[('N',['1','12003/10000','137193/500000']),('N',['-26379/25000','-12003/10000','137193/500000']),('D',['1','-1','43447/2000000']),('delta','1/10'),('potential_upper','1'),('potential_lower','0'),('reference_density_lower','1/5'),('true_density_lower','1/5'),('gap_denominator',10),('kinetic_coefficient',1),('second_moment',2)]
 for key,val in mutations:
  m=copy.deepcopy(d);m[key]=val
  try:check(m)
  except AssertionError as exc:
   import traceback
   frame=traceback.extract_tb(exc.__traceback__)[-1]
   print("[DETECTED mathematical fault]",key,"at",frame.lineno,frame.line)
  else:raise AssertionError('undetected input fault '+key)
 # Gaussian ground-state transform control: phi=exp(-x²/4), H=-4d²+x²,
 # Hphi=2phi; first odd x*phi has energy6, gap4.
 for x in [F(-2),F(-1),F(0),F(1,2),F(3)]:
  assert -4*(x*x/4-F(1,2))+x*x==2
  assert -4*(x*x*x/4-3*x/2)+x*x*x==6*x
 flags=lambda z:z['full_line'] is True and z['optimizer_equals_reference'] is False and z['novelty'] is False
 assert flags(d)
 for key in ['full_line','optimizer_equals_reference','novelty']:
  m=copy.deepcopy(d);m[key]=not m[key];assert not flags(m)
 print('K1853 independent refined rational enclosure PASS; 11 mathematical input faults and 3 reporting faults detected; 10 Gaussian identity controls')
