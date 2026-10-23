"""Independent log-integral residual certificate for the continuum row solution.
All integration and error bounds use rational arithmetic; no floating reference.
"""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import k1983_certified_continuum_pulse_evaluation as phase
ROOT=Path(__file__).resolve().parents[2]
def log_bounds(x):
 assert x>0
 if x<1:
  a,b=log_bounds(1/x);return -b,-a
 y=(x-1)/(x+1);n=36;s=2*sum(y**(2*k+1)/(2*k+1) for k in range(n));tail=2*y**(2*n+1)/((2*n+1)*(1-y*y))
 return s,s+tail

def analytic_k(f):
 n=len(f)-1;step=F(6,n);P=F(0);left=[(F(0),F(0))];right=[(F(0),F(0))]
 for i in range(n):
  a=-3+i*step;b=a+step;c2=(f[i+1]-f[i])/(2*step);c1=f[i]-2*c2*a;c0=P-c2*a*a-c1*a
  for side,out in [(1,left),(-1,right)]:
   if side==1:
    rem=c0-3*c1+9*c2;base=c2*(b*b-a*a)/2+(c1-3*c2)*(b-a);ratio=(b+3)/(a+3) if a!=-3 else None
   else:
    rem=-(c0+3*c1+9*c2);base=-c2*(b*b-a*a)/2-(c1+3*c2)*(b-a);ratio=(3-b)/(3-a) if b!=3 else None
   if ratio is None:assert rem==0;lo=hi=base
   else:
    l,h=log_bounds(ratio);lo=base+min(rem*l,rem*h);hi=base+max(rem*l,rem*h)
   out.append((out[-1][0]+lo,out[-1][1]+hi))
  P+=step*(f[i]+f[i+1])/2
 assert P==0
 return [((left[-1][0]-left[i][1]-right[i][1])/9,(left[-1][1]-left[i][0]-right[i][0])/9) for i in range(n+1)]

def check(fault=None):
 r=json.loads((ROOT/'lab/process/k1986-pulse-primal-dual-certificates.json').read_text());f=list(map(F,r['grid_values']));n=len(f)-1;step=F(6,n);phase.configure(128)
 if fault=='forcing_sign':f=[-v for v in f]
 if fault=='row_scale':f=[v*F(9,8) for v in f]
 if fault=='shape':f[n//6]+=F(1,10);f[5*n//6]-=F(1,10)
 values=analytic_k(f);node=F(0)
 for i,(lo,hi) in enumerate(values):
  forcing=phase.g(-3+i*step);node=max(node,abs(f[i]-forcing-lo),abs(f[i]-forcing-hi))
 lip=max(abs(a-b)/step for a,b in zip(f,f[1:]));bound=max(map(abs,f));residual=node+phase.DG+step*(lip+F(23,100)+2*bound/9)/2;error=3*residual
 low=f[n//6]-error;hi=f[n//6]+error
 assert low>F(28,100),'independent continuum amplitude violation by more than1/20'
 if fault=='gap':r['boxed_norm_squared_excess_lower_bound']='1'
 # Independently justified open-rectangle gap, with conservative overshoot1/20.
 lh=F(23,100)+F(4,27);gap=3*F(1,20)**3/(4*lh)
 assert F(r['boxed_norm_squared_excess_lower_bound'])<=gap,'certified squared-norm penalty'
 assert F(r['h_lipschitz_bound'])==lh
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return n+1,(float(low),float(hi)),str(gap)
if __name__=='__main__':
 n,interval,gap=check();caught=[]
 for f in ['forcing_sign','row_scale','shape','gap']:
  try:check(f)
  except AssertionError as e:caught.append([f,str(e)])
  else:raise AssertionError('undetected mathematical fault '+f)
 print('PASS K1986 independent',n,'rational log-integral rows; h(-2) interval',interval,'gap',gap,'faults',caught)
