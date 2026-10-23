"""Exact fast one-dimensional solve for the unboxed continuum marginal problem."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
import k1983_certified_continuum_pulse_evaluation as phase
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1986-pulse-primal-dual-certificates.json'
M=F(23,100);G=F(23,100);GM=F(2,9);Q=F(2,3)

def integral_to(f,prefix,x,step):
 if x<=-3:return F(0)
 if x>=3:return prefix[-1]
 j=int((x+3)//step);r=x+3-step*j
 return prefix[j]+f[j]*r+(f[j+1]-f[j])*r*r/(2*step)
def apply_k(f):
 n=len(f)-1;assert n%2==0;step=F(6,n);m=3*n//2
 pref=[F(0)]
 for a,b in zip(f,f[1:]):pref.append(pref[-1]+step*(a+b)/2)
 assert pref[-1]==0 and all(a==-b for a,b in zip(f,reversed(f)))
 zvals=[]
 for j in range(5*n//2):
  z=-3+step*F(2*j+1,2);a=max(F(-3),z-9);b=min(F(3),z)
  zvals.append((integral_to(f,pref,b,step)-integral_to(f,pref,a,step))/(b-a))
 pre=[F(0)]
 for x in zvals:pre.append(pre[-1]+x)
 out=[(pre[j+m]-pre[j])/m for j in range(n+1)]
 assert all(a==-b for a,b in zip(out,reversed(out)))
 assert max(map(abs,out))<=Q*max(map(abs,f))
 return out

def calculate(n=480,iterations=40,bits=60):
 assert n%6==0;phase.configure(128);step=F(6,n);m=3*n//2
 forcing=[phase.g(-3+step*j) for j in range(n+1)]
 # Force a bounded dyadic representation; include the actual rounding error.
 den=2**bits
 def quantize(x):return F(round(x*den),den)
 g=[quantize(x) for x in forcing];rounderr=max(abs(a-b) for a,b in zip(g,forcing));eg=phase.DG+3*G/n+rounderr
 f=[F(0)]*(n+1);err=F(0);history=[]
 for k in range(iterations):
  lip=max(abs(a-b)/step for a,b in zip(f,f[1:]));bound=max(map(abs,f))
  local=9*lip/(4*m)+2*bound/(3*n)
  values=[a+b for a,b in zip(g,apply_k(f))];new=[quantize(x) for x in values]
  re=max(abs(a-b) for a,b in zip(values,new));err=Q*err+eg+local+re;f=new
  history.append(dict(iteration=k+1,uniform_finite_error=str(err),operator_quadrature_interpolation_error=str(local),rounding_error=str(re)))
 total=err+3*GM*Q**iterations
 index=n//6;lower=f[index]-total;upper=f[index]+total
 assert lower>M,'certified continuum amplitude violation'
 lh=G+F(2,9)*3*GM;a=F(1,20);assert lower-M>a;gap=3*a**3/(4*lh)
 integral=sum(step*(2*g0*h0+g0*h1+g1*h0+2*g1*h1)/6 for g0,g1,h0,h1 in zip(g,g[1:],f,f[1:]))
 norm_mid=9*integral;norm_error=54*(GM*total+max(map(abs,f))*eg)
 return dict(result_id='K1986',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',grid_intervals=n,row_midpoints=m,iterations=iterations,bits=bits,forcing_uniform_error=str(eg),uniform_h_error=str(total),h_minus_two_interval=list(map(str,[lower,upper])),h_lipschitz_bound=str(lh),boxed_norm_squared_excess_lower_bound=str(gap),unboxed_norm_squared_interval=list(map(str,[norm_mid-norm_error,norm_mid+norm_error])),boxed_norm_squared_lower_bound=str(norm_mid-norm_error+gap),history=history,grid_values=list(map(str,f)),scope='Exact continuum unboxed minimum-norm pulse has both exact marginals, uniform geometric Neumann convergence, and exceeds amplitude23/100 on a certified open set. Every amplitude-feasible pulse has a strictly larger squared norm by a certified amount. This does not construct a boxed optimal pulse, change phase energy, prove smooth attainment, or identify GU physics.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1983_certified_continuum_pulse_evaluation.py','explorations/conditional-build/k1980-constructive-minimum-norm-pulse-2026-10-23.md','explorations/conditional-build/k1974-scalar-excursion-separation-2026-10-23.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=calculate()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1986 actual continuum interval',list(map(float,map(F,r['h_minus_two_interval']))),'squared norm gap',float(F(r['boxed_norm_squared_excess_lower_bound'])))
