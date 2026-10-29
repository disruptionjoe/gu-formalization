#!/usr/bin/env python3
"""Exact time-compatibility obstruction and changed-spatial raw escape controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
import k2206_changed_raw_mass_construction_probe as o
F=o.F;I=o.ONE;Z=o.ZERO;add=o.add;mul=o.mul;scale=o.scale
T=o.blade(o.UN);A=mul(o.G[0],o.J);B=o.blade(range(7,14))
C={j:mul(o.G[0],o.G[j]) for j in o.OBS[1:]}
X={j:mul(c,T) for j,c in C.items()}
def comm(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def anti(a,b):return add(mul(a,b),mul(b,a))
def trace_rhs(k,g,r):return add(mul(mul(o.transpose(k),g),o.G[r]),mul(mul(g,o.G[r]),k))
def controls(fault=None):
 out={}
 def ck(k,v):out[k]=bool(v)
 m=F(2,3);aa=[F(3,7),F(-5,11),F(2,13)]
 V=add(*(scale(x,a) for x,a in zip(X.values(),aa)))
 K=add(scale(A,m),V);Kt=add(scale(A,m),scale(V,-1))
 obstruction=scale(mul(A,V),-4*m)
 ck('temporal_commutator',comm(K,Kt)==(scale(obstruction,-1) if fault=='temporal_sign' else obstruction))
 ck('temporal_obstruction_invertible',mul(obstruction,obstruction)==scale(I,-16*m*m*sum(a*a for a in aa)))
 ck('massless_commutator_zero',comm(V,scale(V,-1))==Z)
 ck('zero_flavor_commutator_zero',comm(A,A)==Z)
 dotB=comm(B,K)
 for r in o.UN:
  ck(f'normal_conjugation_{r}',mul(mul(o.G[r],K),scale(o.G[r],o.ETA[r]))==Kt)
  ck(f'initial_B_trace_passes_{r}',trace_rhs(K,B,r)==Z)
  ck(f'time_trace_derivative_{r}',trace_rhs(K,dotB,r)==mul(mul(B,obstruction),o.G[r]))
  ck(f'time_trace_derivative_nonzero_{r}',trace_rhs(K,dotB,r)!=Z)
 # Massless theta=t*a(x7), Omega=dtheta X7. Rational phase cos=3/5,sin=4/5.
 xx=X[7];u=add(scale(I,F(3,5)),scale(xx,F(4,5)));ut=o.transpose(u)
 g=mul(mul(ut,B),u)
 ck('frame_orthogonal',mul(ut,u)==I)
 ck('moving_pairing_symmetric',o.transpose(g)==g)
 ck('moving_pairing_involution',mul(g,g)==I)
 ck('moving_pairing_split',g.get(0,F(0))==0)
 ck('moving_pairing_anticommutes_axis',anti(g,xx)==Z)
 ck('moving_pairing_nonconstant',comm(g,xx)!=Z)
 # Supplied local jet: a=2/3, a'=3/7, t=5/11.
 a=F(2,3);ap=F(3,7);t=F(5,11);coeff={0:a,7:t*ap}
 omegas={k:scale(xx,coeff.get(k,0)) for k in range(14)}
 for k,om in omegas.items():
  dg=scale(comm(g,xx),coeff.get(k,0))
  if fault=='transport_sign':dg=scale(dg,-1)
  ck(f'parallel_component_{k}',dg==add(mul(o.transpose(om),g),mul(g,om)))
  for r in o.UN:ck(f'same_pairing_trace_{k}_{r}',trace_rhs(om,g,r)==Z)
 ck('flat_connection_mixed_derivatives',add(scale(xx,ap),scale(xx,-ap),comm(omegas[0],omegas[7]))==Z)
 # Original 15 rows against every basis normal-slot difference, for ALL observed k.
 tr=[scale(o.G[k],o.ETA[k]) for k in range(14)]+[o.WB]
 inv=o.G+[scale(o.W,F(1,2))]
 for k in o.OBS:
  def entry(row,col):
   rr=o.raw(k,row,col,'raw_return_sign' if fault=='return_sign' else None)
   prod=mul(xx,rr) if fault=='raw_order' else mul(rr,xx)
   return mul(mul(inv[row],prod),tr[col])
  for col in o.UN[1:]:
   for row in range(15):
    lhs=add(entry(row,col),scale(entry(row,o.UN[0]),-1))
    rhs=scale(mul(mul(o.G[k],o.WB),xx),int(row==col)-int(row==o.UN[0]))
    ck(f'original_raw_{k}_{row}_{col}',lhs==rhs)
  rr=o.raw(k,14,k,'raw_return_sign' if fault=='return_sign' else None)
  ck(f'original_bottom_{k}',mul(rr,xx)==scale(xx,-o.ETA[k]))
 n=add(scale(xx,-a),scale(T,-t*ap))
 induced=scale(add(*(mul(C[k] if k else I,om) for k,om in omegas.items() if om)),-1)
 ck('induced_spatial_connection',induced==(scale(n,-1) if fault=='induced_sign' else n))
 ck('reduced_current_skew',o.transpose(n)==scale(n,-1))
  # A genuine frame change must transform the principals too.
 ck('frame_reduced_C7_fixed',mul(mul(ut,C[7]),u)==C[7])
 ck('frame_reduced_C8_changes',mul(mul(ut,C[8]),u)!=C[8])
 ck('frame_raw_principal_changes',any(mul(mul(ut,o.raw(k,r,c)),u)!=o.raw(k,r,c) for k in o.OBS for r in range(15) for c in range(15)))
 ck('new_pairing_not_original_gamma_adjoint',add(mul(o.transpose(o.G[1]),g),mul(g,o.G[1]))!=Z)
 # A static general-frame completion transports pairing, gamma and raw principal.
 # Omega0=u^-1 A u; Omega7=u^-1 partial7u=X7 for unit phase derivative.
 kr=mul(mul(ut,A),u)
 ck('moved_mass_parallel',add(mul(o.transpose(kr),g),mul(g,kr))==Z)
 for r in o.UN:
  gr=mul(mul(ut,o.G[r]),u)
  for name,om in [('mass',kr),('spatial',xx)]:
   ck(f'moved_gamma_trace_{name}_{r}',add(mul(mul(o.transpose(om),g),gr),mul(mul(g,gr),om))==Z)
 ck('moved_mass_leaves_original_static_class',bool(set(kr)-set(add(A,*X.values()))))
 # Conjugation preserves the actual scalar off-sector lower returns.
 for k in o.OBS:
  ck(f'moved_lower_return_{k}',mul(mul(ut,o.raw(k,14,k)),u)==o.raw(k,14,k))

 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--controls-only',action='store_true');args=ap.parse_args()
 cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={f:[k for k,v in controls(f).items() if not v] for f in ['temporal_sign','transport_sign','return_sign','raw_order','induced_sign']}
 assert all(faults.values()),faults
 deps=['tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2221-raw-flavor-observation-2026-10-28.md','explorations/conditional-build/k2224-raw-parallel-pairing-classification-2026-10-28.md','explorations/conditional-build/k2227-same-pairing-temporal-compatibility-2026-10-28.md']
 if not args.controls_only:
  report=dict(result='K2227',checks=cs,faults=faults,probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
  target=ROOT/'lab/process/k2227-same-pairing-temporal-compatibility.json'
  if args.write:target.write_text(json.dumps(report,indent=2)+'\n')
  else:assert json.loads(target.read_text())==report
 print(json.dumps(dict(result='K2227',controls=len(cs),faults={k:len(v) for k,v in faults.items()})))
if __name__=='__main__':main()
