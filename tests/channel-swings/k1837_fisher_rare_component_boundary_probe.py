#!/usr/bin/env sage-python
"""Separate likelihood algebra, rational chart and exponential-gap controls."""
import json,hashlib
from pathlib import Path
from copy import deepcopy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def run():
 p,L,x,d=s.symbols('p L x d',real=True);n=0
 def ck(v):
  nonlocal n
  assert bool(v),'mathematical control failed';n+=1
 den=1+p*(L-1);score=-x+p*d*L/den
 ck(s.cancel(den*score**2-(x*x*den-2*x*p*d*L+p*p*d*d*L*L/den))==0)
 ck(s.cancel((L*L/den-L*L)*den+p*L*L*(L-1))==0)
 # Gaussian likelihood moments by completing the square, not a Fisher jet.
 u=s.symbols('u')
 for k in range(1,7):
  exponent=-u*u/2+k*(d*u-d*d/2)
  ck(s.expand(exponent+(u-k*d)**2/2-k*(k-1)*d*d/2)==0)
 # Independent binomial coefficients for the chart's constant terms.
 # v=s^2/4-k*s^3/4+s^4/32+O(s^5), common to both orientations.
 e=s.symbols('e');k,b=s.symbols('k b',positive=True)
 v=e**2/4-k*e**3/4+e**4/32
 inv=4/e**2+4*k/e+4*k*k-s.Rational(1,2)
 ck(s.expand(v*inv).coeff(e,2)==0)
 ck(s.expand(v*inv).coeff(e,1)==0)
 for sign in [-1,1]:
  # Rare gap magnitude: b*e/2 + (k/(2b)-sign*b^2/8)e^2.
  gap=b*e/2+(k/(2*b)-sign*b*b/8)*e*e
  prob=k*e/b**2-k*k*e*e/b**4
  # p*gap^2/v^2 through its constant, using reciprocal v to one more order.
  expr=s.expand(prob*gap**2*inv**2)
  ck(s.simplify(expr.coeff(e,-1)-4*k)==0)
  expected=-sign*2*b*k+8*k*k+4*k*k/b**2
  ck(s.simplify(expr.coeff(e,0)-expected)==0)
  const=s.simplify(4*k*k-s.Rational(1,2)-expected)
  ck(s.simplify(const-(-s.Rational(1,2)+sign*2*b*k-4*k*k-4*k*k/b**2))==0)
 # Noncompact amplitude coercivity uses vanishing first lambda derivative.
 lam=s.symbols('lam');leading=4*(1-2*lam-lam**2/b**2)/(1-lam)**2
 ck(s.diff(leading,lam).subs(lam,0)==0)
 ck(s.simplify(s.diff(leading,lam,2).subs(lam,0)/2+4+4/b**2)==0)
 H=s.symbols('H',positive=True);opt=b/(4*H)
 ck(s.simplify((-s.Rational(3,2)-2*b*k+4*H*k*k)-(-s.Rational(3,2)-b*b/(4*H)+4*H*(k-opt)**2))==0)
 w=s.symbols('w');gap=s.Rational(1,2)-w*w/(4*(s.exp(w)-1-w))
 ck(s.series(gap,w,0,3).removeO()==w/6-w*w/72)
 for bv in [s.Rational(1,4),s.Rational(1,2),1,2,3]:
  # A finite positive Taylor lower bound already proves a strict gap.
  lb=bv**4/2+bv**6/6
  ck(lb>bv**4/2)
  ck(s.Rational(1,2)-bv**4/(4*lb)>0)
 a,b=s.symbols('a b',positive=True);z=1-a*a;r=b*b-1;c=z*r;h=r-z;L2=(a+b)**2
 ck(s.factor((1-c/L2)**2-(1-c/2)-c*(2*h*L2-h*h-2*c)/(2*L2**2))==0)
 # The exact two-point variance from its probability weights.
 mean=(r*a+z*b)/(r+z)
 ck(s.factor(1-mean**2-c/L2)==0)
 # Under h>=c/2 and L2>=2+h the numerator is nonnegative.
 hh,cc=s.symbols('h c',nonnegative=True)
 ck(s.expand(2*hh*(2+hh)-hh*hh-2*cc-(4*hh+hh*hh-2*cc))==0)
 cert=json.loads((ROOT/'lab/process/k1837-fisher-rare-component-boundary.json').read_text())
 for path,h in cert['inputs'].items():ck(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h)
 expected={'finite_positive_noise_scaled_radius_excluded':True,'upper_displacement_o_sqrt_delta':True,'global_scaling_compactness_proved':False,'global_shape_uniqueness_proved':False}
 def valid(c):return all(c['results'].get(k)==v for k,v in expected.items())
 assert valid(cert)
 for k in expected:
  bad=deepcopy(cert);bad['results'][k]=not expected[k];assert not valid(bad)
 print('PASS K1837 independent',n,'exact controls; 4 reporting faults')
if __name__=='__main__':run()
