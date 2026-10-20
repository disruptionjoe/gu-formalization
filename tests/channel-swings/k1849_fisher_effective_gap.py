#!/usr/bin/env python3
"""Exact polynomial and constant certificates for the actual-optimizer gap bound."""
from pathlib import Path
import json,hashlib
import sympy as s
R=Path(__file__).resolve().parents[2];p=R/'lab/process/k1849-fisher-effective-gap.json';r=json.loads(p.read_text());checks={}
def ck(k,v):
 assert bool(v),k
 checks[k]=True
x,y,b,F,k,e2,e4,I=s.symbols('x y b F k e2 e4 I',real=True)
a=F-2*b*k;E=2*F-b*k
ck('correlated quartic equation',s.expand(a*y+b*y*y-E-(b*(y*y-2*k*y+k)+F*(y-2)))==0)
ck('moment error identity',s.expand(I+a*(1+e2)+b*(k+e4)-E-(I-F+a*e2+b*e4))==0)
ck('Gaussian mixture fourth moment',s.expand((1-x)**2+6*(1-x)*x+3*x*x-(1+4*x-2*x*x))==0)
v=1-s.sqrt(3)/2
ck('trial moment',s.simplify(1+4*v-2*v*v)==s.Rational(3,2));ck('trial Fisher bound',s.simplify(1/v)==4+2*s.sqrt(3));ck('trial bound below8',s.sqrt(3)<2)
prior=json.loads((R/r['dependencies'][1]['path']).read_text());L=s.Rational(prior['lower']);U=s.Rational(prior['upper']);q=r['k2'];lo=s.Rational(q['F_lower']);hi=s.Rational(q['F_upper']);bl=s.Rational(q['b_lower']);bh=s.Rational(q['b_upper'])
ck('F bracket',lo<L<U<hi);ck('lower multiplier',bl<=lo-1);ck('upper multiplier',bh>=2*(8-lo))
ymax=s.Rational(q['L0'])**2;P=y*y-4*y+2;Pmax=P.subs(y,ymax)
ck('compact extrema',Pmax==s.Rational(17729,4096) and P.subs(y,2)==-2 and P.subs(y,0)==2)
ck('compact absolute maximum',Pmax>2 and ymax>4)
Qupper=(bh*Pmax+hi*(ymax-2))/4
ck('compact Q certificate',Qupper==s.Rational(q['compact_Q_upper']) and Qupper<s.Rational(q['kappa'])**2)
t=s.symbols('t',nonnegative=True);ys=s.Rational(q['R'])**2+t
coeff=s.Poly(s.expand(bl*P.subs(y,ys)+lo*(ys-2)-4),t).all_coeffs();ck('tail all positive coefficients',all(c>0 for c in coeff))
ck('moment penalties',s.Rational(q['moment_penalties'][0])>=4*bh and s.Rational(q['moment_penalties'][1])>=bh)
ck('Sobolev weighted coefficient',s.Rational(q['sobolev_x4_coefficient'])<=bl/2)
ck('Sobolev energy coefficient',s.Rational(q['sobolev_multiplier'])>=2*(2*hi+8*bh))
for name in ['k2','uniform']:
 q=r[name];rad,edge,kap=map(s.Rational,[q['R'],q['L0'],q['kappa']]);delta=2*kap*(edge-rad);ex=s.Rational(q['gap_exponent']);pref=4*rad*(rad+s.Rational(1,2))
 ck(name+' exponential denominator',1+delta+delta**2/2>2)
 ck(name+' exponential prefactor',sum((ex-4*kap*rad)**j/s.factorial(j) for j in range(7))>pref+1 and ex>4*kap*rad)
 ck(name+' TV factor',2*s.Rational(q['tv_exponent'])==ex)
u=r['uniform'];kl,kh=map(s.Rational,u['k_interval']);A,B,C=map(s.Rational,prior['certificate']['minorant']);Flo=s.Rational(u['F_lower']);Fhi=s.Rational(u['F_upper']);blo=s.Rational(u['b_lower']);bhi=s.Rational(u['b_upper'])
ck('uniform affine lower',A+B+C*kh==s.Rational(5599831,4000000) and A+B+C*kh>Flo and C<0)
ck('uniform multiplier lower',blo<=(Flo-1)/(3-kl));ck('uniform multiplier upper',bhi>=(8-1)/(kl-s.Rational(3,2)))
rad,edge,kap=map(s.Rational,[u['R'],u['L0'],u['kappa']]);ys=rad**2+t
ck('uniform tail polynomial',all(c>0 for c in s.Poly(s.expand(blo*(ys**2-2*kh*ys)+Flo*(ys-2)-4),t).all_coeffs()))
ck('uniform compact y range',edge**2<10)
ck('uniform compact polynomial',100+20*kh+kh<145)
ck('uniform compact Q', (bhi*145+Fhi*8)/4<kap**2)
c=s.symbols('c');ck('TV spectral factor',s.expand((2-2*c)*(2+2*c)/4)==1-c*c)
# Gaussian u*=const exp(-x²/4): H=-4d²+x², E0=2, even gap8.
psi=s.exp(-x*x/4);f=x*x-1
ck('Gaussian ground state',s.simplify(-4*s.diff(psi,x,2)+x*x*psi)==2*psi)
ck('Gaussian even excitation',s.simplify((-4*s.diff(psi*f,x,2)+x*x*psi*f)/psi)==10*f)
for d in r['dependencies']:ck('dependency '+d['path'],hashlib.sha256((R/d['path']).read_bytes()).hexdigest()==d['sha256'])
r['exact_algebra_checks']=checks;p.write_text(json.dumps(r,indent=2)+'\n');print('K1849 exact algebra groups',len(checks))
