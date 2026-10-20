#!/usr/bin/env python3
"""Exact symbolic controls; analytic/domain proof belongs to the exploration."""
import json, hashlib
from pathlib import Path
import sympy as S
R=Path(__file__).resolve().parents[2]
m=json.loads((R/'lab/process/k1864-causal-scalar-tensor-completion.json').read_text())
C={k:S.Rational(v) for k,v in m['constants'].items()}
x=S.symbols('t x y z'); eta=S.diag(-1,1,1,1); signs=[-1,1,1,1]
chi=x[0]**3*x[1]+x[2]**4+x[0]*x[3]**2
box=lambda f:sum(signs[i]*S.diff(f,x[i],2) for i in range(4))
h=-eta*chi;trace=sum(signs[i]*h[i,i] for i in range(4));ric=S.zeros(4)
for a in range(4):
 for b in range(4):
  ric[a,b]=(sum(signs[j]*(S.diff(h[j,b],x[j],x[a])+S.diff(h[j,a],x[j],x[b])) for j in range(4))-box(h[a,b])-S.diff(trace,x[a],x[b]))/2
scalar=sum(signs[i]*ric[i,i] for i in range(4));G=ric-eta*scalar/2
for a in range(4):
 for b in range(4):assert S.expand(G[a,b]-(S.diff(chi,x[a],x[b])-eta[a,b]*box(chi)))==0
assert S.expand(scalar-3*box(chi))==0
c,w,z,mu,tau=S.symbols('c w z mu tau')
assert S.simplify((1-3*c)**2-(1-3*c)-3*c*(3*c-1))==0
assert 1-3*C['projector_c']==0
assert S.simplify((1-1/(2*w+3))/(1+1/(2*w+3))-(w+1)/(w+2))==0
assert (1-C['projector_c'])/(1+C['projector_c'])==C['gamma']
assert C['projector_c']/2==C['scalar_residue']
assert C['einstein_kinetic']==1/(2*C['projector_c'])
assert S.simplify(1-z/(z-mu)-C['mass_trace_numerator']*mu/(z-mu))==0
phi=C['vacuum_quadratic']*sum(signs[i]*x[i]**2 for i in range(4))
for a in range(4):
 for b in range(4):
  assert S.diff(phi,x[a],x[b])==C['vacuum_hessian']*eta[a,b]
  assert eta[a,b]*box(phi)-S.diff(phi,x[a],x[b])==-eta[a,b]
for p,d in m['dependencies'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==d
print('PASS K1864: conformal Einstein identity (16), scalar trace, projector/kinetic/PPN/mass (7), vacuum equations (32), dependency (1)')
