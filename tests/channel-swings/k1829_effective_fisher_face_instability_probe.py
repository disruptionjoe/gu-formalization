#!/usr/bin/env python3
"""Independent Gaussian moment/score identities and adversarial reporting controls."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]

def validate(d):
    assert d['constants']['overlap_constant']==168
    assert d['constants']['uniform_direction_r_interval']==['1/4','1/2']
    assert d['constants']['single_direction_r']=='1/2'
    for row,(inv,a) in zip(d['interval_certificates'],[(4096,F(1,128)),(16384,F(1,512))]):
        assert row['inverse_v']==inv and F(row['exponent_coefficient'])==a
        assert F(row['q_lower'])==2*(1-F(1,inv))**2
        assert F(row['scaled_error_upper'])==168*inv**2/F(32**32,factorial(32))<F(7,144)
        assert row['half_margin_lower']=='7/144'
    assert len(d['interval_certificates'])==2
    assert d['results']['single_direction_derivative_upper']=='-7t/(72v^2)'
    assert d['results']['uniform_direction_derivative_upper']=='-kappa(r)t/(2v^2)'
    assert d['results']['kappa']=='1/(1+r)^2-1/4'
    assert d['results']['explicit_finite_descent_step']=='7*v^4*exp(-32/v)/(288*10^12)'
    assert d['results']['uniform_second_derivative_upper']=='2*10^12*v^-6*exp(32/v)'
    assert d['results']['boundary_second_variation_lower']=='exp(1/(8v))/(1024*v^(3/2))-1706/v^6'
    assert d['results']['boundary_second_variation_positive_for_v_le']=='1/4096'
    assert d['results']['z_15_over_16_derivative_less_than_z_3_over_4_on_uniform_interval'] is True
    for key in ['true_transition_located','minimizing_displacement_identified','global_shape_uniqueness','z_one_face_excluded','physical_or_canon_promotion']:assert d['results'][key] is False

count=0
for r in [F(1,4),F(1,3),F(2,5),F(1,2),F(3,4)]:
    z=1-r*r;A=1/(z*z);b=F(1,8)+1/(2*z)
    for m in [F(1,2),F(3,4),F(1)]:
        t=m*m;v=F(1,8)
        # Gplus integral against each Gaussian is 1/v - (mu-m)^2/v^2.
        # Its mean derivative at mu=m is zero; variance derivative is -1/v^2.
        isolated=A*(-(m*r-m)**2/v**2)+(-t/4)*(-1/v**2)
        k=1/(1+r)**2-F(1,4)
        assert isolated==-t*k/v**2
        second_moment=A*(m*m*r*r-m*m)+2*m*(b*m)-t/4
        assert second_moment==0
        count+=1
# Independently expand the baseline score and differentiate it.
for y in [F(-2),F(-1,4),F(0),F(1,3),F(2)]:
 for T in [F(-1),F(-2,3),F(0),F(1,4),F(1)]:
    m=F(3,4);v=F(1,8);s=(-y+m*T)/v;sp=-1/v+m*m*(1-T*T)/v**2
    G=-2*sp-s*s;Gp=2/v-(y-m)**2/v**2
    assert G-Gp==(T-1)*(2*m*y+m*m*(T+1))/v**2
# Tail density splitting: u^2/(2v) >= d^2/(4v)+u^2/(4v) when |u|>=d.
for d in [F(1,16),F(1,8),F(1,4)]:
 for u in [d,2*d,4*d]:assert u*u/2>=d*d/4+u*u/4
# Polynomial norm constants, valid for doubled variance <=1.
assert 2+2+F(1,2)*(2+1)<=7
assert 4*(1+F(3,2))*(6*F(16,9)+3*F(19,24)+F(7,8))<168
# Reporting mutations are separate from the identities above.
d=json.loads((ROOT/'lab/process/k1829-effective-fisher-face-instability.json').read_text());validate(d)
mutations=[]
x=copy.deepcopy(d);x['constants']['overlap_constant']=16;mutations.append(x)
x=copy.deepcopy(d);x['interval_certificates'][0]['inverse_v']=1024;mutations.append(x)
x=copy.deepcopy(d);x['interval_certificates'][0]['q_lower']='1';mutations.append(x)
for key in ['true_transition_located','minimizing_displacement_identified','global_shape_uniqueness','z_one_face_excluded','physical_or_canon_promotion']:
 x=copy.deepcopy(d);x['results'][key]=True;mutations.append(x)
for x in mutations:
 try:validate(x)
 except AssertionError:pass
 else:raise AssertionError('missed reporting fault')
# Sharp distinction: a first derivative never supplies a uniform step.
for M in [10,100,1000]:
    c=F(2,M)
    assert -c+M*c*c>0 # derivative at zero=-1, yet this chosen step increases value
print(f'PASS K1829 probe: {count} exact Gaussian variations, 25 score identities, 9 tail controls, 3 no-step counterexamples; {len(mutations)} reporting faults rejected')

# Independent second-variation constants and boundary-jet derivation.
z=F(3,4);b=F(1,8)+1/(2*z)
assert b*b+F(1,16)-1/(2*z*z)==-F(115,576)
assert -2/z**4==-F(512,81)
# Weighted Gaussian derivative norms from E U^(2,4,6) <= (1,3,15).
assert (3+2*3+3+2)/2==7
assert (3*2+2*7+3*(3+2*2))/2<=21
assert (3*3+2*15+6*(3+2*3)+3*(3+2))/4==27
assert 70+112+(7+7+14+42+27)==279
assert 32+6*279==1706
# Elementary hyperbolic bounds without floating approximation.
lo=sum((F(2**k,factorial(k)) for k in range(6)),F(0))
hi=sum((F(2**k,factorial(k)) for k in range(7)),F(0))+F(2**7,factorial(7))/(1-F(1,4))
assert lo>7 and hi<F(15,2)
assert F(512**32,factorial(32))>1706*1024*4096**5
print('PASS K1829 second variation: exact chart jets, Gaussian norm constants, hyperbolic controls and whole-interval exponential dominance')

# Pointwise density Hessian identity, before integration by parts of the k term.
for rho in [F(1,2),F(1),F(3)]:
 for rp in [F(-2),F(0),F(1)]:
  h=F(2,3);hp=F(-3,4);k=F(5,7);kp=F(-2,5)
  quotient_second=2*hp*hp/rho+2*rp*kp/rho-4*rp*hp*h/rho**2-rp*rp*k/rho**2+2*rp*rp*h*h/rho**3
  residual=2*(hp-rp*h/rho)**2/rho+2*rp*kp/rho-rp*rp*k/rho**2
  assert quotient_second==residual
print('PASS: 9 independent pointwise Fisher Hessian identities')

# Uniform finite-step controls, independently computed polynomial margins.
for R in [F(2),F(3),F(5),F(10)]:
 assert 4*R**3+16*R**2+14*R+16 <=8*(R+1)**3
 assert 4*R**4+32*R**3+94*R**2+144*R+86 <=100*(R+1)**4
assert 32*(9**6+15)<2*10**7 and 32*(5**6+15)<10**6
assert 2*6400*4*(2*10**7)+7200*4*10**6<2*10**12
for mu in [F(-2),F(0),F(2)]:
 for mu0 in [F(-2),F(2)]:
  for y in [F(-3),F(0),F(4)]:
   assert -(y-mu)**2+(y-mu0)**2/2 ==(mu-mu0)**2-(y-(2*mu-mu0))**2/2
for a in [F(1),F(3,2)]:
 for M in [F(10),F(100)]:
  c=a/M
  assert -a*c+M*c*c/2==-a*a/(2*M)<0
print('PASS: finite-step polynomial/moment controls, 18 Gaussian ratio identities and 4 exact Taylor descent controls')
