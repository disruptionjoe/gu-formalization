"""Separate symbolic polar/variance/defect derivation and mathematical faults."""
import sympy as s
from fractions import Fraction as F
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]
def check(d):
 m,r,h,a,b,c=s.symbols('m r h a b c',positive=True);theta=s.symbols('theta',real=True)
 # Minimum angular interpolation of a jump2m over each unforced quarter circle.
 slope=2*m/(s.pi/2)
 exact=s.simplify(2*s.integrate(slope**2,(theta,0,s.pi/2)))
 assert exact==16*m*m/s.pi,'angular transition energy'
 M=s.Rational(d['amplitude']);R=s.Rational(d['radius'])
 assert s.Rational(d['annular_energy_coefficient_over_pi'])==s.simplify(exact*s.pi).subs(m,M),'annular coefficient'
 # Two equal-size forced arcs contribute variance >= pi/4*(a-b)^2.
 variance=s.pi/2*((a-c)**2+(b-c)**2)
 assert s.simplify(variance-s.pi/4*(a-b)**2-s.pi*(c-(a+b)/2)**2)==0,'arc variance identity'
 D0=s.pi*M*R**2/4;C=s.pi*M*M/4
 # H >= C*(log(R/sqrt(4D/(pi M)))-1/2).
 D=s.symbols('D',positive=True)
 rhs=C*(s.log(R/s.sqrt(4*D/(s.pi*M)))-s.Rational(1,2))
 target=D0*s.exp(-1-2*h/C)
 assert s.simplify(s.expand_log(rhs.subs(D,target),force=True)-h)==0,'inverted defect bound'
 assert s.Rational(d['defect_prefactor_times_pi'])*s.pi==D0,'defect prefactor'
 assert s.Rational(d['defect_exponent_coefficient_over_pi'])==s.simplify(2/C*s.pi),'defect exponent'
 assert s.Rational(d['phase_gap_exponent_coefficient_over_pi'])==s.simplify(4/C*s.pi),'squared phase exponent'
 assert s.Rational(d['phase_gap_prefactor_times_pi_squared'])==s.simplify((D0/s.pi)**2/(2*s.Rational(51,20)**2)),'phase gap transfer'
 # Physical-to-characteristic gradient/Jacobian exactly cancel.
 vt,vx=s.symbols('vt vx',real=True)
 assert s.expand(2*((-vt+vx)**2/4+(vt+vx)**2/4)-(vt*vt+vx*vx))==0,'coordinate energy'
 # Independent rational quadrant geometry uses entire isolating interval, not its midpoint.
 lo,hi=map(F,d['root_interval']);R=F(d['radius']);n=9
 for t in [lo,hi]:
  for du in [-R/2,R/2]:
   for dz in [-R/2,R/2]:
    u=-t+du;z=3-2*t+dz
    assert -3<u<3 and u<z<u+9,'interior corner geometry'
    if du<0<dz:assert u<-t and z>3-2*t,'positive forced quadrant'
    if dz<0<du:assert -t<u<t and z<3-2*t,'negative forced quadrant'
    n+=1
 # Radially regularized angular minimizer: exact defect and gradient constants.
 rr,aa=s.symbols('rr aa',positive=True)
 defect=s.integrate(s.pi*m*(1-rr/aa)*rr,(rr,0,aa))
 assert s.simplify(defect-s.pi*m*aa**2/6)==0,'regularized defect'
 angular_norm=2*s.integrate((-m+4*m*theta/s.pi)**2,(theta,0,s.pi/2))+s.pi*m*m
 assert s.simplify(angular_norm-4*s.pi*m*m/3)==0,'angular norm'
 core=s.simplify((angular_norm+16*m*m/s.pi)/2)
 saved=d['regularized_corner']
 assert s.simplify(core.subs(m,M)-s.Rational(saved['core_energy_coefficient_times_pi'])*s.pi-s.Rational(saved['core_energy_coefficient_over_pi'])/s.pi)==0,'core gradient energy'
 assert s.Rational(saved['defect_coefficient_times_pi'])==M/6,'regularized defect coefficient'
 return n+4
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1993-pulse-sobolev-corner-obstruction.json').read_text());n=check(d);faults=[]
 for key in ['annular_energy_coefficient_over_pi','defect_prefactor_times_pi','defect_exponent_coefficient_over_pi','phase_gap_exponent_coefficient_over_pi']:
  b=copy.deepcopy(d);b[key]=str(F(b[key])*2)
  try:check(b)
  except AssertionError as e:faults.append((key,str(e)))
  else:raise AssertionError('undetected '+key)
 print('PASS K1993 separate',n,'symbolic/geometry obligations; mathematical faults',faults)
