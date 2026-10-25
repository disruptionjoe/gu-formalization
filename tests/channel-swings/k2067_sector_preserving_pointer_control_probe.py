"""Separate finite pointer and Born probability checks, not a continuum theorem."""
from fractions import Fraction as Q
import math
# Finite lattice pointer with exact normalized symmetric density. Chosen record
# region lies away from wraparound: a finite fixture, not the massive R3 packet.
def pointer(a,fault=None):
 weights={-2:Q(1,20),-1:Q(1,5),0:Q(1,2),1:Q(1,5),2:Q(1,20)}
 assert sum(weights.values())==1
 right=sum(w for x,w in weights.items() if x+a>0)
 left=sum(w for x,w in weights.items() if x-(a if fault!='same_shift' else -a)>0)
 # Half-integer shifts avoid an atom on the threshold.
 assert right+left==1,'opposite shifts unbiased'
 return right,left

def checks(fault=None):
 count=0
 for a in [Q(1,2),Q(3,2),Q(5,2)]:
  r,l=pointer(a,fault);assert r>=l;count+=2
 r,l=pointer(Q(3,2));eta=r-l
 # Two independent pointers: all four outcomes kept; use singlet Born rule.
 axes=[(0.,1.),(1.,0.)];bs=[(-1/math.sqrt(2),-1/math.sqrt(2)),(1/math.sqrt(2),-1/math.sqrt(2))]
 S=0.
 for x,a in enumerate(axes):
  for y,b in enumerate(bs):
   corr=-sum(u*v for u,v in zip(a,b));measured=0.;total=0.
   for sa in [-1,1]:
    for sb in [-1,1]:
     prob=(1+sa*sb*corr)/4
     for oa in [-1,1]:
      for ob in [-1,1]:
       pa=float(r if oa==sa else l);pb=float(r if ob==sb else l)
       if fault=='omit_b_noise':pb=float(ob==sb)
       total+=prob*pa*pb;measured+=oa*ob*prob*pa*pb
   assert abs(total-1)<1e-12,'complete probabilities'
   assert abs(measured-float(eta**2)*corr)<1e-12,'two pointer attenuation';count+=2
   S+=(-1 if x==y==1 else 1)*measured
 assert abs(S-2*math.sqrt(2)*float(eta**2))<1e-12,'CHSH from outcomes';count+=1
 # The full-effect norm can remain one despite exact prepared-state readout.
 r,l=pointer(Q(5,2));assert (r,l)==(1,0)
 wrong=sum(w for x,w in {-10:Q(1)}.items() if x+Q(5,2)>0);assert wrong==0;count+=2
 # Speed and positivity separate: lambda=.5 keeps energy positive but changes cone.
 lam=Q(1,2);speeds=[s+lam*z for s in [-1,1] for z in [-1,1]]
 assert max(speeds)==Q(3,2),'principal speed';count+=1
 return count
if __name__=='__main__':
 n=checks();caught=[]
 for f in ['same_shift','omit_b_noise']:
  try:checks(f)
  except AssertionError as e:caught.append((f,str(e)))
  else:raise AssertionError('undetected '+f)
 print('PASS separate finite pointer/probability controls',n,'faults',caught)
