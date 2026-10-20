#!/usr/bin/env python3
"""Exact symbolic controls; written proof owns continuum hypotheses."""
import json,hashlib
from pathlib import Path
import sympy as S
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1866-positive-scalar-screening-window.json').read_text())
def verify(m):
 c={k:S.Rational(v) for k,v in m['constants'].items()};checks=[]
 z,l,x,y,f,d,e,rho=S.symbols('z l x y f d e rho',positive=True)
 eta=S.diag(-1,1,1,1);T=S.diag(rho,0,0,0);tr=-rho
 h=2*(T-(1-c['slip_scalar_factor']*f)*eta*tr/2)/z
 ricci=S.expand(z*sum(eta[i,i]*h[i,i] for i in range(4))-z*h[3,3])
 checks += [S.simplify(ricci+(1-c['trace_scalar_factor']*f)*tr)==0,S.simplify(h[1,1]/h[0,0]-(1-f)/(1+f))==0]
 checks += [S.factor(y/(y+l)-x/(x+l)-l*(y-x)/((y+l)*(x+l)))==0,S.simplify(S.diff(z/(z+l),z)-l/(z+l)**2)==0,S.simplify(S.diff(z/(z+l),z,2)+2*l/(z+l)**3)==0]
 g=lambda v:(1-v)/(1+v)
 checks += [S.simplify(g((1-d)/3)-(2+d)/(4-d))==0,S.simplify(1-g((1-d)/3)-2*(1-d)/(4-d))==0,S.simplify(1-g(e/(2-e))-e)==0,c['example_delta_lower']==1-3*c['example_epsilon']/(2-c['example_epsilon']),g(S.Rational(1,3))==S.Rational(1,2)]
 A=S.diag(z,z+l);source=S.Matrix([1,1]);read=S.Matrix([1,-1])
 checks += [S.simplify(1/z-1/(z+l)-l/(z*(z+l)))==0,S.simplify((read.T*A.inv()*source)[0]-l/(z*(z+l)))==0,S.simplify((source.T*A.inv()*source)[0]-1/z-1/(z+l))==0]
 assert all(checks),[i for i,x in enumerate(checks) if not x]
 for p,digest in m['dependencies'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==digest
 return len(checks),len(m['dependencies'])
if __name__=='__main__':print('PASS math, dependency checks:',verify(M))
