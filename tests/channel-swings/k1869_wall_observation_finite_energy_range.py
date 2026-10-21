#!/usr/bin/env python3
"""Exact symbolic range-consumer identities; does not re-certify upstream matrices."""
from pathlib import Path
import json,hashlib
import sympy as s
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1869-wall-observation-finite-energy-range.json').read_text())
def verify(m):
 c={k:s.Rational(v) for k,v in m['constants'].items()};n=0
 def ck(v,msg):
  nonlocal n
  assert v,msg
  n+=1
 b,t,x,mu,m0,alpha=s.symbols('b t x mu m0 alpha',positive=True)
 ck(2*c['normal_factor']/c['speed_inverse']==1,'normal sech square integral')
 ck(c['mass_square_factor']==c['speed_inverse']**2,'mass scale')
 ck(s.integrate(s.exp(-t),(t,0,s.oo))==c['fourier_gaussian_norm_squared'],'Fourier Gaussian normalization')
 J=s.symbols('J');jp=J-1/b
 budget=J+b*jp;error=-b*b*jp
 ck(s.expand(budget-(c['budget_J_coefficient']*(1+b)*J+c['budget_constant']))==0,'budget via J derivative')
 ck(s.expand(error-(c['error_linear']*b+c['error_J_coefficient']*b*b*J))==0,'error via J derivative')
 diff=s.exp(-t)*(t/(t+b)**2-((1+b)/(t+b)-1))
 ck(s.simplify(diff+s.diff(s.exp(-t)*t/(t+b),t))==0,'budget integrand boundary identity')
 ck(s.simplify(s.diff(s.exp(-t)/(t+b),t)+s.exp(-t)/(t+b)+s.exp(-t)/(t+b)**2)==0,'J recurrence integration by parts')
 eps=s.symbols('eps',positive=True)
 ck(s.integrate(s.exp(-t),(t,0,eps**2))==1-s.exp(-eps**2),'cutoff target error')
 sig,u,y,tau=s.symbols('sig u y tau',real=True)
 ck(s.factor((sig*u-y)**2+tau*u*u-tau*y*y/(sig*sig+tau)-(sig*sig+tau)*(u-sig*y/(sig*sig+tau))**2)==0,'optimality square completion')
 ck(s.diff(t/(t+b)**2,b)==-2*t/(t+b)**3,'strict budget monotonicity')
 for path,digest in m['dependencies'].items():ck(hashlib.sha256((R/path).read_bytes()).hexdigest()==digest,'dependency '+path)
 return n-len(m['dependencies']),len(m['dependencies'])
if __name__=='__main__':print('PASS symbolic mathematical identities, dependency pins:',verify(M))
