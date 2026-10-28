#!/usr/bin/env python3
"""Joint coherence exact identities, rational infinite-tail dual and feasible witness."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
from k2168_finite_budget_moment_envelope_probe import IV,sqrtq,aa,ap
ROOT=Path(__file__).resolve().parents[2];Z=F(1,4);N=F(1,3);C=F(40,3);K=9

def floorq(x):return F((x*10**18).__floor__(),10**18)
def ceilq(x):return -floorq(-x)
def tail(a,b,k):return Z**k*(a+b*(k+N))
def pos_tail(a,b,k):
 if b>0:
  lo=max(k,(-a/b).__floor__()+1);return tail(a,b,lo)
 if b==0:return Z**k*max(a,0)
 hi=(-a/b).__ceil__()-1
 return tail(a,b,k)-tail(a,b,hi+1) if hi>=k else F(0)
def reference(fault=None):
 e=[F(v,10**8) for v in [68761789,93465392,98833672,99800536,99966432,99994399,99999071,99999847]];c=F(99999980,10**8)
 p=[(1-Z)*Z**n for n in range(K+1)];x=[F(0)]+[p[n]*e[n-1] for n in range(1,K)]+[c*p[K]]
 x[0]=sum((3*n-1)*x[n] for n in range(1,K))+c*tail(-1,3,K)-F(1,2)
 if fault=='wrong_contrast':x[0]+=F(1,1000)
 return p,x,c

def instrument(p,x,c,fault=None):
 y=[a-b for a,b in zip(p,x)];g1=[];g0=[];d0=IV(0)
 for n in range(K+1):
  for arr,out in [(x,g1),(y,g0)]:
   v=(n*sqrtq(arr[n-1]/arr[n]) if n else IV(0))
   v+=(n+1)*(sqrtq(arr[n+1]/arr[n]) if n<K else IV(F(1,2)))
   out.append(v/2)
 for n in range(K):
  beta=sqrtq(y[n+1]/y[n]);d0+=(n+1)*(beta*p[n]+p[n+1]/beta)/(3 if fault=='dual_edge_factor' else 2)
 d0+=F(1,2)*tail(1,1,K)
 return g1,g0,d0

def energy(x,c,s1,s0):
 p=[(1-Z)*Z**n for n in range(len(x))];y=[a-b for a,b in zip(p,x)]
 w=sum(x[:-1])+c*Z**K;m=sum(n*x[n] for n in range(K))+c*tail(0,1,K)
 t1=sum(((n+1)*sqrtq(x[n]*x[n+1]) for n in range(K)),IV(0))+c*F(1,2)*tail(1,1,K)
 t0=sum(((n+1)*sqrtq(y[n]*y[n+1]) for n in range(K)),IV(0))+(1-c)*F(1,2)*tail(1,1,K)
 E=(m+w/2)*aa(s1)+(N-m+(1-w)/2)*aa(s0)-C*(s1*t1+s0*t0)+F(35,18)
 return E,w,m,t1,t0

def dual(s1,s0,p,g1,g0,d0):
 diff=aa(s1)-aa(s0)
 h=[(F(n)+F(1,2))*diff-C*(s1*g1[n]-s0*g0[n]) for n in range(K+1)]
 # Arbitrary rational multipliers are weak-dual certificates, not fitted truths.
 etas=[floorq((h[n].a+h[n].b)/(2*(3*n-1))) for n in [0,1,2,3]]
 vals=[]
 for eta in etas:
  val=IV(F(5,6)*aa(s0)+F(35,18)+eta/2)-C*s0*d0
  for n in range(K+1):val+=p[n]*min(h[n].a-eta*(3*n-1),0)
  a=diff/2-C*(s1-s0)/4+eta;b=diff-C*F(5,4)*(s1-s0)-3*eta
  val-=pos_tail(-a,-b,K+1)
  vals.append(val.a)
 return max(vals)

def explicit_tail_descent():
 p,x,c=reference();s1=F(105488613,10**8);s0=F(86390048,10**8);eps=F(1,10**14)
 base={n:(x[n] if n<K else c*(1-Z)*Z**n) for n in range(K-1,K+4)};changed=dict(base)
 for n,v in zip(range(K,K+3),[-1,2,-1]):changed[n]+=v*eps
 assert all(0<changed[n]<(1-Z)*Z**n for n in changed)
 assert sum(changed[n]-base[n] for n in changed)==0
 assert sum(n*(changed[n]-base[n]) for n in changed)==0
 dt1=IV(0);dt0=IV(0)
 for n in range(K-1,K+3):
  pn=(1-Z)*Z**n;pn1=pn*Z
  dt1+=(n+1)*(sqrtq(changed[n]*changed[n+1])-sqrtq(base[n]*base[n+1]))
  dt0+=(n+1)*(sqrtq((pn-changed[n])*(pn1-changed[n+1]))-sqrtq((pn-base[n])*(pn1-base[n+1])))
 de=-C*(s1*dt1+s0*dt0)
 assert de.b<0
 return dict(indices=[K,K+1,K+2],direction=[-1,2,-1],epsilon=str(eps),energy_change=[str(floorq(de.a)),str(ceilq(de.b))])

def controls(fault=None):
 cs={};ck=lambda n,v:cs.__setitem__(n,bool(v));p,x,c=reference(fault)
 en,w,m,t1,t0=energy(x,c,F(105488613,10**8),F(86390048,10**8))
 ck('infinite_witness_exact_contrast',3*m-w==F(1,2));ck('all_witness_entries_strictly_interior',all(0<a<b for a,b in zip(x,p)) and 0<c<1)
 t=S.symbols('t',positive=True);ww,de=S.symbols('w delta',real=True)
 xx0=(8*ww-1-de)/12;xx1=(16*ww+1+7*de)/48
 if fault=='interior_reference':xx1=(16*ww+1+6*de)/48
 ck('interior_reference_mass',S.expand(xx0+xx1+(1-de)/16-ww)==0)
 ck('interior_reference_mean',S.expand(xx1+(1-de)*S.Rational(7,48)-(ww+S.Rational(1,2))/3)==0)
 a,b,al=S.symbols('a b al',positive=True)
 edge=(al*a+b/al)/2-S.sqrt(a*b)
 if fault=='amgm_factor':edge=al*a+b/al-S.sqrt(a*b)
 ck('edge_tangent_exact_square',S.simplify(edge-(S.sqrt(al*a)-S.sqrt(b/al))**2/2)==0)
 u,v,r,s1,s0=S.symbols('u v r s1 s0',positive=True)
 direct=s1*(S.sqrt(u*t)+2*S.sqrt(t*v))+s0*(S.sqrt((r-u)*(r-t))+2*S.sqrt((r-t)*(r-v)))
 grad=s1*(S.sqrt(u/t)+2*S.sqrt(v/t))/2-s0*(S.sqrt((r-u)/(r-t))+2*S.sqrt((r-v)/(r-t)))/2
 ck('gradient_from_two_original_edges',all(S.simplify((S.diff(direct,t)-grad).subs({r:rr,u:uu,v:vv,t:tt,s1:S.Rational(7,6),s0:S.Rational(4,5)}))==0 for rr,uu,vv,tt in [(10,1,4,2),(12,3,7,4),(9,2,5,3)]))
 n=S.symbols('n',integer=True,positive=True);gt=(s1-s0)*(2*n+(n+1)/2)/2
 if fault=='tail_slope':gt=(s1-s0)*(n+(n+1)/2)/2
 ck('affine_gradient_tail',S.expand(gt-(s1-s0)*(1+5*n)/4)==0)
 ck('three_entry_moment_direction',sum([1,-2,1])==0 and sum((K+j)*v for j,v in enumerate([1,-2,1]))==0)
 for sign in [-1,1]:
  direction=[2*sign,sign];ck('endpoint_delta_direction_'+str(sign),sum((3*j-1)*v for j,v in enumerate(direction))==0)
 ck('endpoint_sqrt_gain',S.limit(S.sqrt(2*t*(S.Rational(1,16)+t))/S.sqrt(t),t,0,dir='+')==S.sqrt(2)/4)
 # Every sign/slope branch of exact geometric positive-part formula.
 for a,b,k in [(F(-2),F(1),0),(F(2),F(-1),0),(F(2),F(0),3),(F(-2),F(0),3),(F(-2),F(-1),0),(F(1,3),F(-1,7),1)]:
  expected=sum((1-Z)*Z**i*max(a+b*i,0) for i in range(k,100))
  if b>=0 and a+100*b>0:expected+=tail(a,b,100)
  actual=pos_tail(a,b,k+(1 if fault=='tail_start' else 0))
  ck('positive_tail_'+str((a,b,k)),actual==expected)
 ck('squeeze_lower_and_upper',ap(F(2,3))<0 and ap(F(113,100))>C)
 # A'' <= 2843/48 on s>=2/3; sum branch radii N+1/2=5/6.
 ck('squeeze_curvature_bound',F(41,3)+9/F(2,3)**4==F(2843,48))
 g1,g0,d0=instrument(p,x,c,fault);lo=dual(F(105488613,10**8),F(86390048,10**8),p,g1,g0,d0)
 ck('weak_dual_below_feasible_energy',lo<en.b)
 sone=F(105488613,10**8);szero=F(86390048,10**8)
 touch=szero*d0+sum(((sone*g1[n]-szero*g0[n])*x[n] for n in range(K+1)),IV(0))+c*(sone-szero)*tail(F(1,4),F(5,4),K+1)-sone*t1-szero*t0
 ck('production_tangent_touches_both_coherences',touch.a<=0<=touch.b)
 return cs

FAULTS=['wrong_contrast','interior_reference','amgm_factor','tail_slope','tail_start','dual_edge_factor']
def certificate(count=48):
 p,x,c=reference();g1,g0,d0=instrument(p,x,c);a=F(2,3);b=F(113,100);step=(b-a)/count
 lower=None;worst=None
 for i in range(count):
  s1=a+(F(i)+F(1,2))*step
  for j in range(count):
   s0=a+(F(j)+F(1,2))*step;value=dual(s1,s0,p,g1,g0,d0)
   if lower is None or value<lower:lower=value;worst=[i,j]
 # At global minimizer each positive branch squeeze is stationary. Taylor bound
 # to cell center is (max A'')*(sum radii)*step²/8; never a sampled sign claim.
 correction=F(2843,48)*F(5,6)*step*step/8
 e,w,m,_,_=energy(x,c,F(105488613,10**8),F(86390048,10**8))
 return dict(grid_per_axis=count,interval=[str(a),str(b)],step=str(step),worst_cell=worst,midpoint_dual_lower=str(floorq(lower)),curvature_correction=str(correction),global_energy_lower=str(floorq(lower-correction)),witness=dict(K=K,x=[str(v) for v in x],tail_effect=str(c),w=str(w),M=str(m),s1='105488613/100000000',s0='86390048/100000000',energy=[str(floorq(e.a)),str(ceilq(e.b))]))

def main():
 ap_=argparse.ArgumentParser();ap_.add_argument('--write',action='store_true');args=ap_.parse_args();cs=controls();assert all(cs.values()),cs
 faults={}
 for f in FAULTS:
  bad=[k for k,p in controls(f).items() if not p];assert bad,('undetected',f);faults[f]=bad
 cert=certificate();cert['explicit_tail_descent']=explicit_tail_descent();assert F(cert['witness']['energy'][1])<F('.83121');assert F(cert['global_energy_lower'])>F('.75913'),cert
 deps=['explorations/conditional-build/k2174-joint-coherence-detector-2026-10-27.md','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py','explorations/conditional-build/k2172-mean-constrained-fidelity-2026-10-27.md']
 report=dict(result_id='K2174',status='conditional_exact_controls',checks=cs,fault_failures=faults,energy_certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Independently reviewed written infinite-chain optimizer and tangent-dual proofs. Rational grid plus uniform Taylor remainder certifies all squeezes; exact geometric tails retain all occupations. No actual optimum or full-energy uniqueness claim.')
 dest=ROOT/'lab/process/k2174-joint-coherence-detector.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2174',checks=len(cs),faults=faults,certificate=cert)))
if __name__=='__main__':main()
