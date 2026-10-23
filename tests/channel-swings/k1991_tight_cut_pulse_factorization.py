"""Exact central pulse and rational enclosure of its continuum norm.

The two wing existence claims rely on K1974, not on these finite controls.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k1969_scalar_continuum_separation import isolate,ia,im,iv
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1991-tight-cut-pulse-factorization.json';M=F(23,100)
def neg(a):return -a[1],-a[0]
def point(x):return F(x),F(x)
def log_bounds(x,n=64):
 assert x>=0
 z=x/(2+x);s=2*sum(z**(2*j+1)/F(2*j+1) for j in range(n))
 return s,s+2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
def norm_interval(t):
 # I = integral_0^1 x^2/(3+4tx) dx; positive-log series with a proved tail.
 a=im(point(4),t);a2=im(a,a);a3=im(a2,a)
 lg=(log_bounds(a[0]/3)[0],log_bounds(a[1]/3)[1])
 integral=ia(ia(iv(point(F(1,2)),a),neg(iv(point(3),a2))),iv(im(point(9),lg),a3))
 w=ia(point(3),a)
 central=im(im(point(2*M*M),t),ia(im(im(w,w),integral),im(point(2),t)))
 upper=ia(ia(point(54*M*M),neg(im(im(point(2*M*M),t),w))),central)
 return integral,central,upper

def f(x,t):return (3+4*t)*x/(3+4*t*x)
def pulse(x,y,t):
 """Normalized u/t and ramp y; y=None means z in[3,6]."""
 if x==0:return F(0) if y is None else F((y>0)-(y<0))
 if y is not None and abs(y)>abs(x):return F((y>0)-(y<0))
 return -F((x>0)-(x<0))*f(abs(x),t)
def produce():
 tl,tr=isolate();i,c,u=norm_interval((tl,tr));lower=F(json.loads((ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json').read_text())['certificate']['squared_norm_lower_bound']);assert lower<u[1]<54*M*M
 controls=0
 for t in [F(9,20),F(23,50),F(1,3),F(1,2)]:
  W=3+4*t
  for j in range(-20,21):
   x=F(j,20);a=abs(x);sgn=F((x>0)-(x<0));val=-sgn*f(a,t)
   row=(3+4*t*a)*val
   assert row==-W*x;controls+=1
   assert abs(val)<=1;controls+=1
   for h in range(-20,21):
    y=F(h,20);assert abs(pulse(x,y,t))<=1;controls+=1
  for j in range(-20,21):
   y=F(j,20)
   # Outside[-|y|,|y|], the two rational pieces cancel exactly by oddness.
   column=2*y
   assert column/2==y;controls+=1
  # Proved continuous rowwise improvement over the sign-ramp/linear-center pulse.
  for j in range(1,20):
   x=F(j,20);eps=(1-x)/(1+4*t*x/3);R=4*t*x
   improvement=R*(-2*eps*(1-x)+eps*eps*(1+R/3))
   assert improvement==-R*(1-x)**2/(1+R/3)<0;controls+=1
 return dict(result_id='K1991',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',root_interval=list(map(str,(tl,tr))),central_norm_squared_interval=list(map(str,c)),whole_pulse_norm_squared_upper_bound=str(u[1]),inherited_squared_norm_lower_bound=str(lower),strong_distance_squared_upper_bound=str(u[1]-lower),central_uncapped_lower_interval=list(map(str,im(point(M*M),ia(im(point(2),(tl,tr)),im(point(F(16,3)),im((tl,tr),(tl,tr))))))),exact_rational_controls=controls,scope='Complete forced-support factorization into two reflected wings and one central rectangle. Explicit exact capped central pulse; certified improved whole-pulse norm upper bound using retained wing existence, not an explicit whole-pulse formula or minimum-norm optimizer. No phase-energy, GU or novelty inference.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1974-scalar-excursion-separation-2026-10-23.md','lab/process/k1989-capped-pulse-dual-certificates.json','tests/channel-swings/k1969_scalar_continuum_separation.py']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce()
 if a.write:OUT.write_text(json.dumps(d,indent=2)+'\n')
 else:assert d==json.loads(OUT.read_text())
 print('PASS K1991',d['exact_rational_controls'],'algebra/bound controls; U=',float(F(d['whole_pulse_norm_squared_upper_bound'])),'distance=',float(F(d['strong_distance_squared_upper_bound']))**.5)
