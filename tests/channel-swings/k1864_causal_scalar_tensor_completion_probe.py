#!/usr/bin/env python3
"""Independent Fraction tensor controls and baseline-first input fault probes."""
import json,copy,hashlib
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[2]; M=json.loads((R/'lab/process/k1864-causal-scalar-tensor-completion.json').read_text());sg=[-1,1,1,1]
def verify(m):
 c={k:F(v) for k,v in m['constants'].items()};checks=0
 def ck(ok,label):
  nonlocal checks
  assert ok,label
  checks+=1
 # Symbolic derivative represented by covector k; Box eigenvalue k.k.
 for k in [[1,2,3,4],[3,0,1,0],[0,1,0,0],[2,1,-1,0]]:
  norm=sum(sg[i]*k[i]**2 for i in range(4));assert norm
  pi=[[F((sg[a] if a==b else 0))-F(k[a]*k[b],norm) for b in range(4)] for a in range(4)]
  ck(sum(sg[a]*pi[a][a] for a in range(4))==3,'transverse trace')
  for b in range(4):ck(sum(sg[a]*k[a]*pi[a][b] for a in range(4))==0,'conservation')
  for t in [F(-7,3),F(2),F(0)]:
   qt=[[(1-3*c['projector_c'])*t*pi[a][b] for b in range(4)] for a in range(4)]
   ck(all(v==0 for row in qt for v in row),'scalar kernel')
  # Conformal h=-eta chi: Ricci = kk chi + eta Box chi/2, R=3Box chi.
  ric=[[F(k[a]*k[b])+F((sg[a] if a==b else 0)*norm,2) for b in range(4)] for a in range(4)]
  scalar=sum(sg[a]*ric[a][a] for a in range(4));ck(scalar==3*norm,'conformal Ricci')
  for a in range(4):
   for b in range(4):ck(ric[a][b]-F((sg[a] if a==b else 0),2)*scalar==k[a]*k[b]-(sg[a] if a==b else 0)*norm,'conformal Einstein')
 ck((1-c['projector_c'])/(1+c['projector_c'])==c['gamma'],'Newton normalized gamma')
 ck(c['projector_c']/2==c['scalar_residue'],'trace exchange')
 ck(c['einstein_kinetic']*2*c['projector_c']==1,'scalar kinetic normalization')
 for omega in [F(-1),F(0),F(1),F(100)]:
  a=1/(2*omega+3);ck((1-a)/(1+a)==(omega+1)/(omega+2),'BD response')
  for t in [F(1),F(-3)]:ck((1-3*a)**2*t-(1-3*a)*t==3*a*(3*a-1)*t,'idempotence defect')
 for z,ms in [(F(-1),F(1)),(F(-4),F(3)),(F(0),F(2))]:ck(1-z/(z-ms)==c['mass_trace_numerator']*ms/(z-ms),'mass trace transfer')
 for rho in [F(-5),F(1),F(7,3)]:
  H=[[2*c['vacuum_quadratic']*rho*sg[a] if a==b else F(0) for b in range(4)] for a in range(4)]
  box=sum(sg[a]*H[a][a] for a in range(4))
  for a in range(4):
   ck(H[a][a]==c['vacuum_hessian']*rho*sg[a],'vacuum Hessian')
   ck(sg[a]*box-H[a][a]==-rho*sg[a],'vacuum metric row')
 for p,d in m['dependencies'].items():ck(hashlib.sha256((R/p).read_bytes()).hexdigest()==d,'dependency hash')
 ck(not m['scope']['native_gu_adapter'] and not m['scope']['global_positive_flat_nonzero_vacuum'] and not m['scope']['formal_proof'],'reporting ceiling')
 return checks
if __name__=='__main__':
 print('BASELINE PASS',verify(M))
 for key in M['constants']:
  b=copy.deepcopy(M);b['constants'][key]=str(F(b['constants'][key])+F(1,7))
  try:verify(b)
  except AssertionError as e:print('[DETECTED INPUT]',key,str(e))
  else:raise AssertionError('undetected input '+key)
 for key in ['native_gu_adapter','global_positive_flat_nonzero_vacuum','formal_proof']:
  b=copy.deepcopy(M);b['scope'][key]=True
  try:verify(b)
  except AssertionError as e:print('[DETECTED REPORT]',key,str(e))
  else:raise AssertionError('undetected reporting fault')
 print('PASS K1864: 7 mathematical input faults and 3 reporting faults')
