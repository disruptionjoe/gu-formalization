"""Exact finite thermal/particle-hole controls, separate from spectral proof."""
from pathlib import Path
from copy import deepcopy
import json,sympy as s
ROOT=Path(__file__).resolve().parents[2]
def modes(N):
 out=[]
 for k in range(N):
  a=s.zeros(2**N)
  for w in range(2**N):
   if w>>k&1:a[w^(1<<k),w]=(-1)**sum(w>>j&1 for j in range(k))
  out.append(a)
 return out
def check(d,wrong_cov=False,wrong_flip=False,wrong_hole=False):
 # beta=log2, two energies1,2, two orthogonal multiplicities with b²=-I.
 H=s.diag(1,-2,2,-1);Q=s.diag(0,1,0,1);I=s.eye(4)
 B=s.Matrix([[0,0,0,s.I],[0,0,s.I,0],[0,-s.I,0,0],[-s.I,0,0,0]])
 C=s.diag(s.Rational(1,3),s.Rational(4,5),s.Rational(1,5),s.Rational(2,3))
 if wrong_cov:C[0,0]=s.Rational(1,4)
 assert B*s.conjugate(B)==-I and B*s.conjugate(H)*B.H==-H,'inherited sign/square'
 assert B*s.conjugate(C)*B.H==I-C and C*H==H*C,'thermal complement/stationarity'
 assert max(abs(x) for x in (C-Q).eigenvals())<=s.Rational(d['constants']['covariance_bound']),'gap covariance bound'
 CR=s.diag(1,1,0,0)
 if wrong_flip:CR[3,3]=1
 assert CR*CR==CR and CR*H==H*CR and B*s.conjugate(CR)*B.H==I-CR,'pure stationary band flip'
 a=modes(4);J=s.eye(16);n=[x.H*x for x in a];G=n[0]+2*(J-n[1])+2*n[2]+(J-n[3])
 rho=s.diag(*[s.prod(C[j,j] if w>>j&1 else 1-C[j,j] for j in range(4)) for w in range(16)])
 sea=s.eye(16)[:,10];assert G*sea==s.zeros(16,1) and min(G.eigenvals())==0
 # Actual ground inequality fails for thermal removal of a positive-energy particle.
 comm=G*a[0]-a[0]*G
 assert s.trace(rho*a[0].H*comm)<0,'thermal is not ground'
 assert (sea.H*a[0].H*comm*sea)[0]==0,'sea ground control'
 f=(4*a[0]+3*a[1])/5;cf=(3*a[2]+4*a[3])/5
 nn=f.H*f;hh=cf.H*cf if wrong_hole else J-cf.H*cf;E=nn+hh-nn*hh
 nu=s.Rational(16,25)*C[0,0]+s.Rational(9,25)*C[1,1]
 wanted=s.sympify(d['constants']['paired_probability'],locals={'nu':nu})
 assert s.trace(rho*E)==wanted,'actual thermal coarse click'
 nusea=s.Rational(9,25);assert abs(wanted-(2*nusea-nusea**2))<=2*s.Rational(1,3),'paired error transfer'
 # Rational exponential budget; no floating exp near acceptance threshold.
 delta=1/s.Integer(1+d['constants']['temperature_exponential']);tau2=s.Rational(1,250000)
 assert 2*(tau2+delta)<=s.Rational(d['constants']['paired_budget']),'temperature budget'
 # Convexity and energy-qualified floor in this actual two-energy input.
 M2=s.Rational(16,25)+4*s.Rational(9,25)
 # Finite energy-ceiling control, not an independent proof of Jensen.
 assert M2<=4,'actual graph norm ceiling'
 assert nu>=s.Rational(1,5) and 1-nu>=s.Rational(1,5),'energy-limited thermal floor'
 assert C[0,0]>Q[0,0] and C[1,1]<Q[1,1],'noise change both signs'
 return 'exact covariance, band flip, full CAR ground control, thermal product state and click budget'
def main():
 d=json.loads((ROOT/'lab/process/k2086-ground-state-selection.json').read_text());print('PASS baseline',check(d),flush=True)
 jobs=[('wrong covariance',lambda:check(d,wrong_cov=True)),('wrong band flip',lambda:check(d,wrong_flip=True)),('wrong hole',lambda:check(d,wrong_hole=True))]
 for k,v in [('covariance_bound','1/4'),('paired_probability','nu'),('temperature_exponential',100),('paired_budget','1/125000')]:
  bad=deepcopy(d);bad['constants'][k]=v;jobs.append((k,lambda b=bad:check(b)))
 for name,fn in jobs:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 print('PASS 7 genuine faults; spectral and density proofs remain analytic')
if __name__=='__main__':main()
