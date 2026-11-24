#!/usr/bin/env python3
"""Exact controls for held EXP/COS regular initial states, not a CMB solver."""
import argparse,json
from pathlib import Path
import sympy as s
checks=[]
def check(name,ok):
    if not bool(ok): raise AssertionError(name)
    checks.append(name)
def zero(e):return s.simplify(s.expand(e))==0
F=s.Rational
# Full background and constrained Newtonian ideal-fluid perturbation algebra.
a,H,m,r,v,U,u1,u2=s.symbols('a H m r v U u1 u2',real=True)
phi,dm,vm,dr,vr,y,z,k2=s.symbols('phi dm vm dr vr y z k2',real=True)
Q=F(3,2)*a*a*m*vm+2*a*a*r*vr+v*y/2
phip=-H*phi+Q
rhs={a:a*H,H:H*H-F(3,2)*a*a*m-2*a*a*r-v*v/2,
 m:-3*H*m,r:-4*H*r,v:-2*H*v-3*a*a*u1,U:u1*v,u1:u2*v,
 phi:phip,dm:-k2*vm+3*phip,vm:-H*vm+phi,
 dr:-F(4,3)*k2*vr+4*phip,vr:dr/4+phi,
 y:z,z:-2*H*z-(k2+3*a*a*u2)*y+4*v*phip-6*a*a*u1*phi}
def D(expr):return s.expand(sum(s.diff(expr,x)*dx for x,dx in rhs.items()))
C=k2*phi+3*H*Q+F(3,2)*a*a*(m*dm+r*dr+u1*y)+(v*z-v*v*phi)/2
rho=m+r+U+v*v/(6*a*a)
Fried=H*H-a*a*rho
check('Friedmann constraint propagation',zero(D(Fried)-2*H*Fried))
check('complete Einstein00 constraint propagates Cprime=-H C',zero(D(C)+H*C))
dp=r*dr/3+(v*z-v*v*phi)/(3*a*a)-u1*y
check('momentum plus matter equations imply trace Einstein',zero(D(phip)+3*H*phip+(2*rhs[H]+H*H)*phi-F(3,2)*a*a*dp))
check('no scalar momentum denominator',all(not s.denom(s.cancel(expr)).has(v) for expr in rhs.values()))
check('frozen momentum retains scalar force',zero(rhs[z].subs({v:0,z:0,y:0})+6*a*a*u1*phi))
check('identically zero scalar perturbation fails rolling adiabatic source',rhs[z].subs({v:0,z:0,y:0})!=0)
check('stationary hilltop field decouples from momentum',not Q.subs({u1:0,v:0}).has(y,z))
check('stationary hilltop field decouples from energy constraint',not C.subs({u1:0,v:0}).has(y,z))
check('negative hilltop mass still acts on scalar',s.diff(rhs[z].subs({v:0,u1:0}),y)==-k2-3*a*a*u2)
# Background regular radiation expansion, with leading dust correction.
b,R,M,U1=s.symbols('b R M U1',positive=True)
P=-3*U1*b*b/(5*s.sqrt(R))+M*U1*b**3/(4*R**F(3,2))
X=-3*U1*b**4/(20*R)+11*M*U1*b**5/(100*R**2)
invroot=b*b/s.sqrt(R)*(1-M*b/(2*R))
check('regular momentum leading coefficient',zero(s.expand(s.diff(b**3*P,b)+3*b*b*U1*invroot).coeff(b,4)))
check('regular momentum dust coefficient',zero(s.expand(s.diff(b**3*P,b)+3*b*b*U1*invroot).coeff(b,5)))
expr=s.expand(s.diff(X,b)-P*invroot/b)
check('regular field leading coefficient',zero(expr.coeff(b,3)))
check('regular field dust coefficient',zero(expr.coeff(b,4)))
check('free momentum mode solves homogeneous radiation momentum',zero(s.diff(b**3*b**-3,b)))
check('free momentum kinetic relative to radiation grows backwards',s.simplify((b**-6)/(R*b**-4))==1/(R*b*b))
# Exact constrained Fuchsian limit and physical mode count.
A=s.Matrix([[-1,0,0,2,0,0],[-3,0,0,6,0,0],[1,0,-2,0,0,0],
 [1,0,0,-2,0,0],[0,0,0,0,0,1],[0,0,0,0,0,-1]])
lam=s.symbols('lam')
check('constrained Fuchsian characteristic polynomial',zero(A.charpoly(lam).as_expr()-lam**3*(lam+1)*(lam+2)*(lam+3)))
check('three regular zero modes',len(A.nullspace())==3)
check('zero eigenvalue semisimple',6-(A*A).rank()==3)
ad=s.Matrix([1,-F(3,2),F(1,2),F(1,2),0,0])
mi=s.Matrix([0,1,0,0,0,0]);si=s.Matrix([0,0,0,0,1,0])
check('adiabatic regular kernel seed',A*ad==s.zeros(6,1))
check('matter entropy regular kernel seed',A*mi==s.zeros(6,1))
check('independent frozen scalar regular kernel seed',A*si==s.zeros(6,1))
check('regular amplitudes independent',s.Matrix.hstack(ad,mi,si).rank()==3)
# The seven-variable unconstrained limit has one spurious regular C!=0 mode.
A7=s.Matrix([[-1,0,0,0,2,0,0],[-3,0,0,0,6,0,0],[1,0,-2,0,0,0,0],
 [-4,0,0,0,8,0,0],[1,0,0,F(1,4),-1,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,-1]])
check('unconstrained positive eigenvalue is present',A7.eigenvals().get(s.Integer(1),0)==1)
false=s.Matrix([1,3,F(1,3),4,1,0,0])
check('spurious mode solves unconstrained evolution',A7*false==false)
check('spurious mode violates leading Einstein00',6*false[4]+F(3,2)*false[3]!=0)
# Leading radiation seed coefficients, with dust kept in the stated remainder.
t,Phi0,S=s.symbols('t Phi0 S',real=True)
bg_v=-3*R*U1*t**3/5
isoA=-R*U1*S/14
iso={a:s.sqrt(R)*t,H:1/t,m:0,r:1/(R*t**4),v:bg_v,u1:U1,
 phi:isoA*t**4,dm:3*isoA*t**4,dr:4*isoA*t**4,
 vm:isoA*t**5/6,vr:2*isoA*t**5/5,y:S-k2*S*t*t/6,z:-k2*S*t/3}
def coeff(expr,power):return s.expand(expr).coeff(t,power)
check('isocurvature momentum coefficient',zero(coeff(s.diff(iso[phi],t)-phip.subs(iso),3)))
check('isocurvature Einstein00 coefficient',zero(coeff(C.subs(iso),2)))
check('isocurvature radiation density coefficient',zero(coeff(s.diff(iso[dr],t)-rhs[dr].subs(iso),3)))
check('isocurvature matter density coefficient',zero(coeff(s.diff(iso[dm],t)-rhs[dm].subs(iso),3)))
check('isocurvature radiation velocity coefficient',zero(coeff(s.diff(iso[vr],t)-rhs[vr].subs(iso),4)))
check('isocurvature matter velocity coefficient',zero(coeff(s.diff(iso[vm],t)-rhs[vm].subs(iso),4)))
check('isocurvature field gradient coefficient',zero(coeff(s.diff(iso[z],t)-rhs[z].subs(iso),0)))
ady=-3*R*U1*Phi0*t**4/10
adi={a:s.sqrt(R)*t,H:1/t,m:0,r:1/(R*t**4),v:bg_v,u1:U1,
 phi:Phi0,dm:-F(3,2)*Phi0,dr:-2*Phi0,vm:Phi0*t/2,vr:Phi0*t/2,y:ady,z:s.diff(ady,t)}
check('adiabatic Einstein00 leading coefficient',zero(coeff(C.subs(adi),-2)))
check('adiabatic momentum leading coefficient',zero(coeff(phip.subs(adi),-1)))
check('adiabatic forced scalar coefficient',zero(coeff(s.diff(adi[z],t)-rhs[z].subs(adi),2)))
check('adiabatic scalar time-shift expression',zero(ady-bg_v*Phi0*t/2))
# Exact scalar-to-fluid division trap and held potential signs.
p=s.symbols('p',real=True)
check('scalar enthalpy vanishes at frozen momentum',s.simplify((p*p/6+U)+(p*p/6-U)).subs(p,0)==0)
x,u0=s.symbols('x u0',positive=True)
check('EXP curvature positive factor',zero(s.diff(u0*s.exp(-s.sqrt(2)*x),x,2)-2*u0*s.exp(-s.sqrt(2)*x)))
check('COS hilltop negative curvature',s.diff(u0*(1+s.cos(x)),x,2).subs(x,0)==-u0)
check('COS stationary endpoints',s.diff(u0*(1+s.cos(x)),x).subs(x,0)==0 and s.diff(u0*(1+s.cos(x)),x).subs(x,s.pi)==0)
result={'status':'PASS','checks_passed':len(checks),'checks':checks,
 'scope':'held EXP/COS canonical scalar plus perfect dust/radiation; no anisotropic stress; no CMB likelihood or GU bridge',
 'regular_modes':['adiabatic','matter_entropy','scalar_isocurvature'],
 'constraint_propagation':'Cprime=-Hcal C',
 'scalar_isocurvature_metric_leading':'Phi=-omega_r Ux(x0) S eta^4/14',
 'claim_ceiling':'analytic regular-branch and finite-interval constrained linear theorem; no small-growth, nonlinear, empirical, bet-kill or matrix claim',
 'new_potential_variants':0,'numerical_likelihood_runs':0}
parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))
