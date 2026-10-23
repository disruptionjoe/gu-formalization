"""Rational continuum Fenchel certificates; float coordinate search only proposes witnesses."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k1983_certified_continuum_pulse_evaluation import primitive,DG,M,TL,TR,LL,LR
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1989-capped-pulse-dual-certificates.json'
def area(a,b,c,d):
 cuts=sorted({a,b}|{x for x in [c,d,c-9,d-9] if a<x<b});out=F(0)
 for l,h in zip(cuts,cuts[1:]):
  length=lambda u:max(F(0),min(d,u+9)-max(c,u))
  out+=(h-l)*(length(l)+length(h))/2
 return out
def star(x):return x*x/2 if abs(x)<=M else M*abs(x)-M*M/2
def clip(x):return max(-M,min(M,x))
def geometry(n):
 u=[F(-3)+F(6*i,n) for i in range(n+1)];z=[F(-3)+F(6*i,n) for i in range(5*n//2+1)]
 a=[[area(l,h,c,d) for c,d in zip(z,z[1:])] for l,h in zip(u,u[1:])]
 forcing=[2*(primitive(h)-primitive(l)) for l,h in zip(u,u[1:])]
 assert sum(map(sum,a))==54
 return u,z,a,forcing
def search(n=24,cycles=240):
 u,z,A,G=geometry(n);aa=[[float(v) for v in r] for r in A];gg=list(map(float,G));q=[0.]*n;r=[0.]*(len(z)-1);m=float(M)
 def solve(values,target):
  lo=-max(v for w,v in values)-m-1;hi=-min(v for w,v in values)+m+1
  for _ in range(46):
   x=(lo+hi)/2;val=sum(w*max(-m,min(m,x+v)) for w,v in values)
   if val<target:lo=x
   else:hi=x
  return (lo+hi)/2
 for cycle in range(cycles):
  for i in range(n):q[i]=solve([(w,r[j]) for j,w in enumerate(aa[i]) if w],gg[i])
  for j in range(len(r)):r[j]=solve([(aa[i][j],q[i]) for i in range(n) if aa[i][j]],0.)
  gauge=sum(q)/n;q=[v-gauge for v in q];r=[v+gauge for v in r]
 return [F(round(v*10**8),10**8) for v in q],[F(round(v*10**8),10**8) for v in r]
def certify(q,r):
 n=len(q);u,z,A,G=geometry(n);assert len(r)==len(z)-1
 lin=sum(x*y for x,y in zip(q,G));pen=sum(A[i][j]*star(x+y) for i,x in enumerate(q) for j,y in enumerate(r));err=9*DG*sum(abs(q[i])*(u[i+1]-u[i]) for i in range(n));dual=lin-pen
 vnorm=sum(A[i][j]*clip(x+y)**2 for i,x in enumerate(q) for j,y in enumerate(r));sat=sum(A[i][j] for i,x in enumerate(q) for j,y in enumerate(r) if abs(x+y)>=M)
 # This error is an exact residual for the cell means, a lower bound on full marginal error.
 rowr=sum((sum(A[i][j]*clip(q[i]+r[j]) for j in range(len(r)))-G[i])**2/(9*(u[i+1]-u[i])) for i in range(n))
 colr=sum(sum(A[i][j]*clip(q[i]+r[j]) for i in range(n))**2/sum(A[i][j] for i in range(n)) for j in range(len(r)))
 lower=2*(dual-err);upper=54*M*M;assert 0<lower<=upper
 return dict(grid_rows=n,row_potentials=list(map(str,q)),column_potentials=list(map(str,r)),dual_value_surrogate=str(dual),forcing_error=str(err),squared_norm_lower_bound=str(lower),squared_norm_upper_bound=str(upper),clipped_witness_norm_squared=str(vnorm),strong_error_squared_upper_bound=str(upper-lower),saturated_witness_area=str(sat),cell_mean_residual_squared=str(rowr+colr),column_residual_squared=str(colr))
def produce(q,r):
 c=certify(q,r)
 return dict(result_id='K1989',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',certificate=c,root_interval=list(map(str,[TL,TR])),lambda_interval=list(map(str,[LL,LR])),scope='Exact capped continuum Fenchel dual, no duality gap without Slater or dual attainment, executable actual-phase rational dual lower bound, and certified whole-strip L2 distance to the true optimizer. The clipped witness is amplitude-feasible only; its nonzero marginal residual precludes declaring it an exact optimal pulse or phase-energy certificate.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1983_certified_continuum_pulse_evaluation.py','explorations/conditional-build/k1980-constructive-minimum-norm-pulse-2026-10-23.md','explorations/conditional-build/k1986-pulse-primal-dual-certificates-2026-10-23.md']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 if a.write:
  q,r=search();v=produce(q,r);OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:
  old=json.loads(OUT.read_text());c=old['certificate'];v=produce(list(map(F,c['row_potentials'])),list(map(F,c['column_potentials'])));assert v==old
 c=v['certificate'];print('PASS K1989 exact squared-norm interval',float(F(c['squared_norm_lower_bound'])),float(F(c['squared_norm_upper_bound'])),'distance bound',float(F(c['strong_error_squared_upper_bound']))**.5,'nonzero cell residual',float(F(c['cell_mean_residual_squared'])))
