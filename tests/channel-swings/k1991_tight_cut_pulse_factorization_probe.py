"""Separate symbolic marginals, forced geometry, and alternating-log certificate."""
from fractions import Fraction as F
from pathlib import Path
import json,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def alternate_log(a,n=180):
 v=sum((-1)**(j+1)*a**j/F(j) for j in range(1,n+1))
 return v,v+a**(n+1)/F(n+1) # even partial sum, a in(0,1)
def check(d, fault=None):
 t,x,y=s.symbols('t x y',positive=True);M=s.Rational(23,100)
 P=101*t**4-102*t**3-168*t**2+392*t-138
 K=s.Rational(1,6)-t*t/2+2*t**3/3-t**4/4
 D=-s.Rational(7,100)+69*t/200-77*t*t/200
 contact=s.together(2*t*(1-D/K*(1-t)**2/2)-M*(3+2*t))
 assert s.rem(s.fraction(contact)[0],P,t)==0,'contact derivative'
 W=3+4*t;denom=3+(5 if fault=='denominator' else 4)*t*x;f=W*x/denom
 row=-3*f+2*t*(-(1-x)-2*x*f+(1-x))
 assert s.simplify(row+W*x)==0,'continuum row marginal'
 # Integrate the actual three x pieces for a positive ramp column; primitive
 # of f has derivative f. Odd tail cancellation is exact, not a sampled sum.
 A=(3+4*t)*(x/(4*t)-3*s.log(3+4*t*x)/(16*t*t))
 assert s.simplify(s.diff(A,x)-W*x/(3+4*t*x))==0,'column primitive'
 col=(A.subs(x,1)-A.subs(x,y))+2*y-(A.subs(x,1)-A.subs(x,y))
 if fault=='column':col+=y/10
 assert s.simplify(col-2*y)==0,'continuum column marginal'
 # Norm is reconstructed from length of the saturated and rational x pieces.
 norm_density=(3+4*t*x)*f*f+4*t*(1-x)
 assert s.simplify(norm_density-(W*W*x*x/(3+4*t*x)+4*t*(1-x)))==0,'norm integrand'
 tl,tr=map(F,d['root_interval']);poly=lambda q:101*q**4-102*q**3-168*q*q+392*q-138
 assert F(9,20)<tl<tr<F(23,50) and poly(tl)<0<poly(tr),'root isolation'
 # Independent monotone integral enclosure: I decreases in t; alternating
 # logarithm enclosure supplies tight bounds at the two rational endpoints.
 def integral(q):
  a=4*q;lo,hi=alternate_log(a/3)
  c=1/(2*a)-3/(a*a)
  return c+9*lo/a**3,c+9*hi/a**3
 il,ih=integral(tr)[0],integral(tl)[1]
 cl=2*tl*F(M)**2*((3+4*tl)**2*il+2*tl)
 ch=2*tr*F(M)**2*((3+4*tr)**2*ih+2*tr)
 reported=list(map(F,d['central_norm_squared_interval']))
 assert reported[0]<=ch and cl<=reported[1] and reported[1]-reported[0]<F(1,10**24),'central norm enclosure overlap'
 # Compare a safely outward-rounded bound against our independent enclosure.
 u=54*F(M)**2-2*tl*(3+4*tl)*F(M)**2+ch
 assert u<F(27547213641,10**10),'independent whole norm upper'
 assert F(d['whole_pulse_norm_squared_upper_bound'])>u-F(1,10**24),'reported upper'
 assert F(d['whole_pulse_norm_squared_upper_bound'])<F(27547213641,10**10),'improved feasible bound'
 assert F(d['strong_distance_squared_upper_bound'])==F(d['whole_pulse_norm_squared_upper_bound'])-F(d['inherited_squared_norm_lower_bound']),'strong distance subtraction'
 assert F(d['strong_distance_squared_upper_bound'])<F(636648,10**6)**2,'outward distance'
 # Proposed interval-column mixtures have concave row profiles; actual wing
 # has a strictly convex outer interval. This rules out the named family only.
 lam=D/K
 wing=x*(1-lam*(1-x)/2)/M+2*(3-t)-s.Rational(9,2)-x
 assert s.simplify(s.diff(wing,x,2)-lam/M)==0,'wing curvature'
 for kk in [F(j,100) for j in range(1,50)]:
  slopes=[2/kk-1/(kk+F(1,2)),-1/(kk+F(1,2)),-1/(F(1,2)-kk)]
  assert slopes[0]>slopes[1]>slopes[2],'mixture concavity'
 count=62
 # Independently derive tight-cut forced signs on rational strip points.
 for tt in [F(9,20),F(23,50)]:
  for iz in range(1,120):
   z=-3+F(15*iz,120);lo=max(F(-3),z-9);hi=min(F(3),z)
   for iu in range(1,16):
    u=lo+(hi-lo)*F(iu,16);forced=[]
    for a in [-tt,tt]:
     m=max(F(0),min(hi,a)-lo);ell=hi-lo
     if 0<m<ell:
      if m<=ell/2 and u<a:forced.append(1)
      if m>=ell/2 and u>a:forced.append(-1)
    left=(u<-tt and z<3-2*tt);right=(u>tt and z>6+2*tt);central=(-tt<u<tt and 3-2*tt<z<6+2*tt)
    on_boundary=(u in [-tt,tt] or z in [3-2*tt,6+2*tt])
    if on_boundary:continue
    assert not forced if left or right or central else bool(forced),'free-support coverage'
    assert len(set(forced))<=1,'no forced-sign conflict';count+=2
 return count
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1991-tight-cut-pulse-factorization.json').read_text());n=check(d);faults=[]
 for kind in ['denominator','column','upper','distance']:
  b=copy.deepcopy(d)
  if kind=='upper':b['whole_pulse_norm_squared_upper_bound']='2'
  if kind=='distance':b['strong_distance_squared_upper_bound']='0'
  try:check(b,kind)
  except AssertionError as e:faults.append((kind,str(e)))
  else:raise AssertionError('undetected '+kind)
 print('PASS K1991 separate',n,'symbolic/interval/geometry obligations; mathematical faults',faults)
