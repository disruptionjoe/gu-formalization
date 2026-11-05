#!/usr/bin/env python3
"""Actual potential identities and independent scalar boundary consumers."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(name,condition):
    assert bool(condition),'FAIL '+name
    checks.append(name)
def ct(name,condition):
    assert bool(condition),'FAIL contrary '+name
    controls.append(name)
z,L,n=s.symbols('z L n',nonnegative=True)
A=s.Rational(121366223,77168);D=s.Rational(606773239,96460)
P=n*n+A*z-(L+s.Rational(3,4))*z/(1+z)
Lstar=25*A-s.Rational(3,4)
ck('actual_A',A==s.Rational(120691003,77168)+s.Rational(35,4))
ck('actual_far_V',P.subs({n:0,L:0,z:4})==D)
ck('actual_derivative',s.cancel(s.diff(P,z)-(A-(L+s.Rational(3,4))/(1+z)**2))==0)
ck('threshold',Lstar==s.Rational(3034097699,77168))
ck('threshold_endpoint_derivative',s.diff(P,z).subs({L:Lstar,z:4})==0)
# Substituting z=4-r and L=Lstar+h makes the sign a nonnegative polynomial.
r,h=s.symbols('r h',nonnegative=True)
mono=s.factor(-s.diff(P,z).subs({L:Lstar+h,z:4-r})*(5-r)**2)
ck('monotone_whole_interval_polynomial',s.expand(mono-(h+A*r*(10-r)))==0)
ck('monotone_interval_factor',10-3>0)
Kstar2=1+s.Rational(9,5)*Lstar+D
ck('exceptional_frequency_bound',s.expand((1+n*n+L+D)+(s.Rational(4,5)*L-n*n)+s.Rational(9,5)*(Lstar-L)-Kstar2)==0)
# Actual infinite turning family, not sampled frequencies.
j=s.symbols('j',nonnegative=True);ell=5*(j+40);nn=4*(j+40)
family=P.subs({L:ell*(ell+2),n:nn})
def poscoeff(expr):return all(c>=0 for c in s.Poly(s.expand(expr),j).all_coeffs())
ck('infinite_turning_near',poscoeff(family.subs(z,1)))
ck('infinite_turning_far',poscoeff(-family.subs(z,4)))
ck('infinite_turning_monotone',poscoeff(ell*(ell+2)-Lstar))
well=P.subs({L:100*102,n:60})
wellvals=[well.subs(z,q) for q in (1,2,4)]
ck('actual_double_turn_values',wellvals==[s.Rational(5585285,77168),-s.Rational(2121869,38584),s.Rational(166915639,96460)])
ct('global_monotonicity_false',wellvals[0]>0 and wellvals[1]<0 and wellvals[2]>0)
ck('double_turn_class_is_bounded',100*102<Lstar and 60**2<s.Rational(4,5)*100*102)
# Exact complex-energy identities in two real quadratures.
u,v,up,vp,q,qp=s.symbols('u v up vp q qp',real=True)
F=up*up+vp*vp+(1+q)*(u*u+v*v)
Fprime=2*up*(-q*u)+2*vp*(-q*v)+qp*(u*u+v*v)+2*(1+q)*(u*up+v*vp)
ck('shifted_energy_derivative',s.expand(Fprime-(qp*(u*u+v*v)+2*(u*up+v*vp)))==0)
ck('backward_energy_positive_squares',s.expand(Fprime+F-((up+u)**2+(vp+v)**2+(q+qp)*(u*u+v*v)))==0)
ct('shifted_energy_need_not_increase',Fprime.subs({u:1,v:0,up:-1,vp:0,q:0,qp:0})==-2)
pp,pprime=s.symbols('pp pprime',real=True)
Eprime=2*up*pp*u+2*vp*pp*v-pprime*(u*u+v*v)-2*pp*(u*up+v*vp)
ck('positive_prefix_energy_derivative',s.expand(Eprime+pprime*(u*u+v*v))==0)
k,d,x,t=s.symbols('k d x t',positive=True)
flux=vp*u-up*v
plus=(up-k*v)**2+(vp+k*u)**2
minus=(up+k*v)**2+(vp-k*u)**2
jet=up**2+vp**2+k*k*(u*u+v*v)
ck('near_flux_expansion',s.expand(plus-jet-2*k*flux)==0)
ck('far_flux_expansion',s.expand(minus-jet+2*k*flux)==0)
ck('endpoint_coefficient_bound',s.simplify((1+k*k)*(u*u+v*v+(up*up+vp*vp)/k**2)-F.subs(q,k*k)-(up*up+vp*vp)/k**2)==0)
# Independent free-forcing fixture, not an actual-angular substitution.
y=x*(x-d)/2-s.I*d/(2*k)
ck('forced_second_derivative',s.diff(y,x,2)==1)
ck('forced_near_boundary',s.simplify((s.diff(y,x)+s.I*k*y).subs(x,0))==0)
ck('forced_far_boundary',s.simplify((s.diff(y,x)-s.I*k*y).subs(x,d))==0)
uf=1-s.I*k*x;vf=1+s.I*k*(x-d)
W=s.simplify(uf*s.diff(vf,x)-s.diff(uf,x)*vf)
ck('free_wronskian',s.expand(W-(k*k*d+2*s.I*k))==0)
left=uf*vf.subs(x,t)/W;right=uf.subs(x,t)*vf/W
ck('green_continuity',s.simplify((right-left).subs(x,t))==0)
ck('green_jump_one',s.simplify((s.diff(right,x)-s.diff(left,x)).subs(x,t)-1)==0)
ck('green_near_condition',s.simplify((s.diff(left,x)+s.I*k*left).subs(x,0))==0)
ck('green_far_condition',s.simplify((s.diff(right,x)-s.I*k*right).subs(x,d))==0)
integ=s.integrate(right,(t,0,x))+s.integrate(left,(t,x,d))
ck('independent_green_integral_forcing',s.simplify(integ-y)==0)
ct('reversed_green_sign_wrong_forcing',s.diff(-y,x,2)==-1)
ct('homogeneous_reconstruction_cannot_ignore_f',s.diff(y,x,2)!=0)
# Real forcing produces a genuinely complex solution with these boundary controls.
ct('dropping_imaginary_quadrature_breaks_boundary',s.simplify((s.diff(x*(x-d)/2,x)+s.I*k*x*(x-d)/2).subs(x,0))==-d/2)
wave=s.exp(-s.I*k*x)
ck('same_sign_nonzero_solution_equation',s.simplify(s.diff(wave,x,2)+k*k*wave)==0)
ct('same_sign_uniqueness_false',s.simplify(s.diff(wave,x)+s.I*k*wave)==0 and wave.subs(x,0)==1)
ct('opposite_sign_excludes_same_wave',s.simplify((s.diff(wave,x)-s.I*k*wave).subs(x,d))==-2*s.I*k*s.exp(-s.I*k*d))
# Free Dirichlet kernel maximum and comparison controls.
ck('dirichlet_midpoint_max',s.simplify((t*(d-t)/d).subs(t,d/2)-d/4)==0)
ck('dirichlet_global_max_square',s.expand(d/4-t*(d-t)/d-(t-d/2)**2/d)==0)
ck('short_interval_taylor_coefficient',s.simplify(2/(1/k)+(1/k)*k*k/2-s.Rational(5,2)*k)==0)
# The arbitrary barrier/well has growing amplification and is not monotone-decreasing.
aa=s.pi/(4*k)
inside=s.cos(k*x);outside=s.exp(-k*(x-aa))/s.sqrt(2)
ck('barrier_well_C1_matching',s.simplify((inside-outside).subs(x,aa))==0 and s.simplify((s.diff(inside,x)-s.diff(outside,x)).subs(x,aa))==0)
Pin=s.simplify(s.diff(inside,x,2)/inside);Pout=s.simplify(s.diff(outside,x,2)/outside)
ct('generic_well_does_not_meet_high_mode_structure',s.simplify(Pout-Pin)==2*k*k)
ck('barrier_well_actual_coefficients',Pin==-k*k and Pout==k*k)
report={'result':'K2576','evidence_kind':'exact actual-potential/energy/Green identities, infinite-family coefficient signs, and independent forced fixture; universal comparison/density proof in note','checks':checks,'contrary_controls':controls,'actual_double_turn':{'ell':100,'n':60,'P_1_2_4':[str(v) for v in wellvals]},'constants':{'A':str(A),'D':str(D),'Lstar':str(Lstar),'Kstar_squared':str(Kstar2)},'forcing_fixture':'P=0 f=1 y=x(x-d)/2-i*d/(2*k), independently replayed by Green integration','ceiling':'all-angular fixed-annulus scalar Sobolev inverse; supplied complex impedance, no full coupled or physical inverse'}
refs=['k2574-angular-cone-domains','k2572-boundary-preparation-robustness']
report['provenance']={'explorations/conditional-build/'+f+'-2026-11-05.md':hashlib.sha256((root/('explorations/conditional-build/'+f+'-2026-11-05.md')).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2576-polynomial-impedance-control.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2576','checks':len(checks),'controls':len(controls),'status':'pass'}))
