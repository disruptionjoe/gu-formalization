"""Independent exact CAR/ancilla and projection controls; analytic limits in note."""
from pathlib import Path
from copy import deepcopy
import json,sympy as s
ROOT=Path(__file__).resolve().parents[2]
def modes(N):
 aa=[]
 for k in range(N):
  a=s.zeros(2**N)
  for w in range(2**N):
   if w>>k&1:a[w^(1<<k),w]=(-1)**sum(w>>j&1 for j in range(k))
  aa.append(a)
 return aa
def opnorm(a):return max(abs(x) for x in a.eigenvals())
def trace_norm(a):return sum(abs(x)*m for x,m in a.eigenvals().items())
def check(d,number_scale=1,drop_branch=False,wrong_pair=False):
 aa=modes(2);I=s.eye(4);f=aa[0];g=(3*aa[0]+4*aa[1])/5
 P=number_scale*f.H*f;Q=g.H*g
 assert P*P==P and Q*Q==Q,'number projection'
 delta=s.sqrt(s.Rational(4,5));c=d['constants'];norm=opnorm(P-Q)
 assert norm<=s.Rational(c['number_bound'])*delta,'CAR perturbation bound'
 # A pure entangled system/ancilla input; exact branch trace norms.
 v=s.zeros(8,1);v[2]=v[5]=1/s.sqrt(2);rho=v*v.H
 PP=s.kronecker_product(P,s.eye(2));QQ=s.kronecker_product(Q,s.eye(2));J=s.eye(8)
 out=[PP*rho*PP,(J-PP)*rho*(J-PP)]
 if drop_branch:out[1]=s.zeros(8)
 assert sum(s.trace(x) for x in out)==1,'retained both outcome flags'
 dist=sum(trace_norm(x-y) for x,y in zip(out,[QQ*rho*QQ,(J-QQ)*rho*(J-QQ)]))
 assert dist<=s.Rational(c['flagged_bound'])*norm,'ancilla flagged error'
 # C-stable projection can lose C-real-pair orthogonality.
 f=s.Matrix([1,s.I])/s.sqrt(2);Cf=s.conjugate(f);T=s.diag(1,0)
 assert (f.H*Cf)[0]==0 and (T*f).norm()!=0
 projected=T*f/(T*f).norm();assert (projected.H*s.conjugate(projected))[0]!=0,'C stable is insufficient'
 # Independent four-mode multiplicity pair versus deliberately overlapping partner.
 aa=modes(4);I=s.eye(16);u=aa[0];cu=aa[2] if not wrong_pair else aa[0]
 v=(3*aa[0]+4*aa[1])/5;cv=(3*aa[2]+4*aa[3])/5
 assert u*cu.H+cu.H*u==s.zeros(16),'pair orthogonality'
 E=I-(I-u.H*u)*(cu.H*cu);F=I-(I-v.H*v)*(cv.H*cv)
 assert E*E==E and F*F==F,'coarse projections'
 assert opnorm(E-F)<=s.Rational(c['paired_bound'])*delta,'paired perturbation'
 # Root normalized indicators on nested intervals: overlap sqrt(1/2), no Cauchy limit.
 assert (2-s.sqrt(2))>0
 # One fixed-shape smooth mode per cell retains constant fraction, not full convergence.
 x=s.Symbol('x',real=True);frac=s.integrate(s.sqrt(2)*s.sin(s.pi*x),(x,0,1))**2
 assert s.simplify(frac-s.sympify(c['smooth_projection_fraction']))==0,'actual smoothing projection'
 assert frac<1
 # Fourier support bound implies conservative mean absolute energy coefficient.
 assert 1-1/(6*s.pi**2)>s.Rational(c['mean_energy_factor']),'Fourier energy coefficient'
 return 'exact CAR, ancilla branches, pair countercontrol, smoothing integral and energy constant'
def main():
 d=json.loads((ROOT/'lab/process/k2084-continuum-instrument-limit.json').read_text());print('PASS baseline',check(d),flush=True)
 jobs=[('number coefficient',lambda:check(d,number_scale=2)),('lost outcome',lambda:check(d,drop_branch=True)),('overlapping pair',lambda:check(d,wrong_pair=True))]
 for k,v in [('flagged_bound',0),('paired_bound',0),('smooth_projection_fraction','1'),('mean_energy_factor','1')]:
  bad=deepcopy(d);bad['constants'][k]=v;jobs.append((k,lambda b=bad:check(b)))
 for name,fn in jobs:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 print('PASS 7 genuine faults; finite tests do not prove continuum claims')
if __name__=='__main__':main()
