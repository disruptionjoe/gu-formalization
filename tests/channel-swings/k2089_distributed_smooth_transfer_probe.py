"""Exact CAR exterior-power swap and coherent-readout controls, not PDE proof."""
from pathlib import Path
from copy import deepcopy
import json,sympy as s
ROOT=Path(__file__).resolve().parents[2]
def exterior(U):
 n=U.rows;G=s.zeros(2**n)
 for i in range(2**n):
  rows=[k for k in range(n) if i>>k&1]
  for j in range(2**n):
   cols=[k for k in range(n) if j>>k&1]
   if len(rows)==len(cols):G[i,j]=U.extract(rows,cols).det() if rows else 1
 return G
def check(d,use_x=False,refine=False,half=False):
 I=s.eye(2);Z=s.zeros(2);sy=s.Matrix([[0,-s.I],[s.I,0]]);sx=s.Matrix([[0,1],[1,0]])
 sig=sx if use_x else sy
 assert s.conjugate(sig)==-sig and sig.H==sig,'real-compatible pulse'
 # Constant diagonalization to two scalar potentials.
 T=s.Matrix([[1,1],[s.I,-s.I]])/s.sqrt(2)
 assert T.H*sy*T==s.diag(1,-1),'scalar-pulse reduction'
 U=s.Matrix.vstack(s.Matrix.hstack(Z,-I),s.Matrix.hstack(I,Z))
 if half:U=(s.eye(4)+U)/s.sqrt(2)
 assert U.H*U==s.eye(4),'one-particle unitarity'
 F=exterior(U);assert F.H*F==s.eye(16)
 # Even non-number-conserving coherence |vac>+|two system particles>.
 psi=(s.eye(16)[:,0]+s.eye(16)[:,3])/s.sqrt(2);out=F*psi
 target=(s.eye(16)[:,0]+s.eye(16)[:,12])/s.sqrt(2)
 assert out==target,'exact even-state transfer including anomalous coherence'
 # sigma_x swap would flip the two-particle coherence; do not assume even means neutral.
 Ux=-s.I*s.Matrix.vstack(s.Matrix.hstack(Z,I),s.Matrix.hstack(I,Z));outx=exterior(Ux)*psi
 assert outx==(s.eye(16)[:,0]-s.eye(16)[:,12])/s.sqrt(2),'quarter gauge rotation countercontrol'
 # Occupation transfer for every full input basis state, not just vacuum apparatus.
 ns=s.diag(*[int(w&1!=0) for w in range(16)]);na=s.diag(*[int(w&4!=0) for w in range(16)])
 assert F.H*na*F==ns,'apparatus marginal transfers independently of its input'
 # Coarse click vs individual readouts: preserve |00><11| coherence only in coarse branch.
 E=s.diag(1,1,0,1);v=(s.eye(4)[:,0]+s.eye(4)[:,3])/s.sqrt(2);rho=v*v.H
 coarse=E*rho*E+(s.eye(4)-E)*rho*(s.eye(4)-E)
 refined=s.diag(*[rho[k,k] for k in range(4)])
 measured=refined if refine else coarse
 assert measured[0,3]==s.Rational(d['constants']['coarse_coherence']),'collective instrument coherence'
 assert refined[0,3]==d['constants']['refined_coherence'],'refined coherence'
 # Quarter-area swap exposes apparatus contamination.
 V=(s.eye(4)+U)/s.sqrt(2);FV=exterior(V)
 # input system mode empty, apparatus mode occupied
 assert (FV.H*na*FV)[4,4]==s.Rational(1,2),'partial swap retains apparatus input'
 # Forward drift plus sign-reversed pulse is not generally the inverse.
 drift=s.Matrix([[0,-s.I],[-s.I,0]]);kick=s.diag(1,s.I)
 assert (drift*kick.H)*(drift*kick)!=s.eye(2),'forward drift is not reversed by opposite kick'
 return 'signed swap, anomalous coherence, marginal identity, readout counterexample and inverse-control warning'
def main():
 d=json.loads((ROOT/'lab/process/k2089-distributed-smooth-transfer.json').read_text());print('PASS baseline',check(d),flush=True)
 jobs=[('real sigma-x pulse',lambda:check(d,use_x=True)),('refined readout',lambda:check(d,refine=True)),('incomplete swap',lambda:check(d,half=True))]
 for key,value in [('coarse_coherence','1'),('refined_coherence',1)]:
  b=deepcopy(d);b['constants'][key]=value;jobs.append((key,lambda b=b:check(b)))
 for name,fn in jobs:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 print('PASS 5 mathematical faults; continuum propagation and energy use written proofs')
if __name__=='__main__':main()
