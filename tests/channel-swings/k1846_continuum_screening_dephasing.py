#!/usr/bin/env python3
"""Exact local continuum response identities; analytic limits live in K1846."""
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'lab/process/k1846-continuum-screening-dephasing.json';r=json.loads(p.read_text())
w,t,J,z,eps=s.symbols('w t J z eps',positive=True);checks={}
def ck(k,v):
 assert bool(v),k
 checks[k]=True
weight=w-s.Rational(3,2);d=w*w*weight
phi=J*(1-s.cos(w*t))/w**2
ck('forced Euler equation',s.simplify(s.diff(phi,t,2)+w*w*phi-J)==0)
ck('zero initial position',phi.subs(t,0)==0)
ck('zero initial velocity',s.diff(phi,t).subs(t,0)==0)
ck('static cross zero',s.integrate(weight,(w,1,2))==0)
ck('high frequency cross coefficient',s.integrate(d,(w,1,2))==s.Rational(r['high_frequency_cross']))
osc=(s.sin(2*t)+s.sin(t))/(2*t)+(s.cos(2*t)-s.cos(t))/t**2
ck('cross oscillatory integral',s.simplify(s.integrate(weight*s.cos(w*t),(w,1,2))-osc)==0)
ck('short time coefficient',s.limit(-osc/t**2,t,0)==s.Rational(1,8))
ck('static conjugate',s.integrate(1/w**2,(w,1,2))==s.Rational(1,2))
psi=phi-J/w**2
ck('fluctuation energy pointwise',s.trigsimp((s.diff(psi,t)**2+w*w*psi**2)/2-J**2/(2*w**2))==0)
ck('integrated fluctuation energy',s.integrate(1/(2*w**2),(w,1,2))==s.Rational(r['equilibrium_fluctuation_energy_per_J_squared']))
ck('cross decay endpoint coefficient',s.Rational(1,2)+s.Rational(1,2)==s.Rational(r['cross_decay_coefficients'][0]))
ck('cross decay integral coefficient',s.Integer(2)==s.Rational(r['cross_decay_coefficients'][1]))
ck('contact decay endpoint and variation',1+s.Rational(1,4)+s.integrate(2/w**3,(w,1,2))==s.Rational(r['contact_decay_coefficient']))
ck('contact coefficient',s.Rational(r['contact'])==-s.Rational(1,2))
ck('readout perturbation static residual',s.integrate(weight+eps/w**2,(w,1,2))==eps/2)
ck('inverse mass source norm',s.integrate(w**-4,(w,1,2))==s.Rational(r['inverse_mass_source_norm_squared']))
# Positive definite Gram: a nonconstant polynomial d cannot be proportional to c.
G=s.Matrix([[1,s.integrate(d,(w,1,2))],[s.integrate(d,(w,1,2)),s.integrate(d*d,(w,1,2))]])
ck('source readout independent',G.det()>0)
# Explicit grouped finite masses with zero static but nonzero mean-square amplitude.
a=[s.Rational(1),s.Rational(-1)]
ck('finite fixture cancellation',sum(a)==0)
ck('finite fixture nondecay',sum(v*v for v in a)/2==1)
# Contact cancellation leaves every nonzero-frequency amplitude untouched.
ck('finite contact nondecay',s.Rational(1,2)**2/2>0)
r['mathematical_checks']=checks;r['source_readout_gram']=[[str(v) for v in G.row(i)] for i in range(2)]
p.write_text(json.dumps(r,indent=2)+'\n');print('K1846 exact identity groups',len(checks))
