#!/usr/bin/env python3
"""Symbolic identities only; the note supplies the continuum argument."""
import json, hashlib
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[2]
M=json.loads((R/'lab/process/k1868-fisher-two-well-instability.json').read_text())
def verify(m):
 c={k:s.Rational(v) for k,v in m['constants'].items()}; n=0
 def ck(v,msg):
  nonlocal n
  assert v,msg
  n+=1
 t,f,d,r=s.symbols('theta f df rho', real=True)
 plus=((1+t*f)*r+t*d)**2/(1+t*f)
 minus=((1-t*f)*(-r)+t*d)**2/(1-t*f)
 ck(s.simplify((plus+minus)/2-r*r-t*t*d*d/(1-t*t*f*f))==0,'paired Fisher identity')
 x=s.symbols('x',real=True);ff=s.sin(s.pi*x/(2*c['half_width']))
 ck(s.simplify(s.diff(ff,x)**2-c['deficit_pi2_factor']*s.pi**2*(1-ff**2))==0,'sine gradient coefficient')
 ck(ff.subs(x,s.Rational(1,4))==1,'join value');ck(s.diff(ff,x).subs(x,s.Rational(1,4))==0,'join derivative')
 ck(c['barrier_mass_factor']==4*(2*c['half_width']),'interval barrier mass')
 ck(c['barrier_exponent']==s.Rational(1,2)-c['half_width'],'comparison distance exponent')
 ck(c['spectral_pi2_factor']==4*c['deficit_pi2_factor'],'ground-state spectral factor')
 z=s.symbols('z',positive=True)
 ck(s.simplify(s.diff(1+s.sin(-s.pi/2+z),z,2).subs(z,0))==1,'endpoint quadratic zero')
 h=((1+t)*s.log(1+t)+(1-t)*s.log(1-t))/2
 ck(s.simplify(s.diff(h,t,2)-1/(1-t*t))==0,'binary entropy curvature')
 ck(s.limit(h,t,1,dir='-')==s.log(2),'one-sided entropy')
 ck(c['tv_factor']*2==1,'TV convention');ck(c['mean_sign_factor']*2==1,'sign to probability')
 ck(c['atom_transport_factor']==c['tv_factor']*4,'two-point transport cost')
 ck(c['collapse_error_factor']==2,'two collapse triangle errors')
 for path,digest in m['dependencies'].items():ck(hashlib.sha256((R/path).read_bytes()).hexdigest()==digest,'dependency bytes '+path)
 return n-len(m['dependencies']),len(m['dependencies'])
if __name__=='__main__': print('PASS symbolic mathematical identities, dependency pins:',verify(M))
