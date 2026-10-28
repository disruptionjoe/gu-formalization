#!/usr/bin/env python3
"""Rational free-edge dual, explicit cutoff/mesh and inherited joint-cover controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
import k2176_detector_certified_convergence_probe as prior
ROOT=Path(__file__).resolve().parents[2];C=F(40,3)
def aa(s):return F(41,6)*s*s+F(3,2)/s**2
def p(n):return F(3,4)*F(4)**(-n)
def tail(alpha,beta,m):return F(4)**(-m)*(alpha*(m+F(1,3))+beta)
def negative_tail(alpha,beta,m):
 if alpha<0:
  lo=max(m,(-beta/alpha).__floor__()+1);return tail(alpha,beta,lo)
 if alpha==0:return F(4)**(-m)*min(beta,0)
 hi=(-beta/alpha).__ceil__()-1
 return tail(alpha,beta,m)-tail(alpha,beta,hi+1) if hi>=m else F(0)
def root_down(x,den=10**20):
 assert x>=0
 return F(isqrt(x.numerator*den*den//x.denominator),den)
def dual(s1,s0,u1,u0,eta,d,fault=None):
 assert len(u1)==len(u0) and s1>0 and s0>0 and all(u>0 for u in u1+u0)
 N=len(u1);da=aa(s1)-aa(s0);ds=s1-s0
 def b(ss,u,n):
  fw=u[n] if n<N else F(1,2)
  back=F(0) if n==0 else n/u[n-1]
  return C*ss/ (3 if fault=='edge_factor' else 2)*((n+1)*fw+back)
 value=F(35,18)+F(5,6)*aa(s0)+eta*(d+(F(1,1000) if fault=='contrast' else 0))
 for n in range(N+1):
  b0=b(s0,u0,n);b1=b(s1,u1,n)
  value+=p(n)*(-b0+min((n+F(1,2))*da-b1+b0-eta*(3*n-1),0))
 # Beyond the separately evaluated junction, both neighboring slopes equal1/2.
 m=N if fault=='junction' else N+1
 value-=C*s0/4*tail(5,1,m)
 value+=negative_tail(da-5*C*ds/4-3*eta,da/2-C*ds/4+eta,m)
 return value

def constants(s1,s0,d):
 assert s1>0 and s0>0 and 0<abs(d)<F(3,4)
 da=abs(aa(s1)-aa(s0));J=(F(5,6)*da+2*C*max(s1,s0)/3)/(F(3,4)-abs(d));M=4*C*max(s1,s0)+da+3*J
 ell=C*min(s1,s0)/(4*M);upper=2*M/(C*min(s1,s0));P=2*C*(s1+s0)/3*(1+ell**-2);Q=abs(d)+F(3,2)
 return J,M,ell,upper,P,Q
def budget(s1,s0,d,eps,fault=None):
 J,M,ell,U,P,Q=constants(s1,s0,d);N=0
 def bound(n):return (M+C*(s1+s0)/2)*(n+F(4,3))*F(4)**(-n)
 while bound(N)>=eps/3:N+=1
 h=min(ell/4,eps/(4*P));he=eps/(4*Q)
 if fault=='mesh_budget':h=eps
 return dict(N=N,tail=bound(N),slope_mesh=h,multiplier_mesh=he,total=bound(N)+P*h+Q*he,ell=ell,U=U,J=J,P=P,Q=Q)

def converted_cover(fault=None):
 rows=prior.INPUTS[:-1] if fault=='missing_rectangle' else prior.INPUTS
 assert prior.cover_ok(rows),'genuine cover failure'
 result=[];lo=F(2,3);span=F(113,100)-lo
 for row in rows:
  a,b,c,d=[lo+span*F(v,2**20) for v in row[0]];e=[F(v,10**15) for v in row[1]]
  u1=[root_down(e[n+1]/e[n])/2 for n in range(len(e)-1)]
  u0=[root_down((1-e[n+1])/(1-e[n]))/2 for n in range(len(e)-1)]
  if fault=='negative_slope':u0[0]=-u0[0]
  eta=F(row[2],10**12);val=dual((a+b)/2,(c+d)/2,u1,u0,eta,F(1,2))
  correction=F(2843,48)*F(5,6)*max((b-a)**2,(d-c)**2)/8
  result.append(dict(bounds=row[0],slopes1=list(map(str,u1)),slopes0=list(map(str,u0)),eta=str(eta),center_dual=str(val),global_lower=str(val-correction)))
 return result

def controls(fault=None):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v))
 # Exact summation against an independently specified finite head plus known tail.
 for alpha,beta,m in [(F(1),F(-7,2),0),(F(-2),F(9),1),(F(0),F(-3),4),(F(3),F(-12),4),(F(-1),F(2),2)]:
  got=negative_tail(alpha,beta,m);cut=20
  expect=sum(p(n)*min(alpha*n+beta,0) for n in range(m,cut))
  expect+=tail(alpha,beta,cut) if alpha<0 or (alpha==0 and beta<0) else 0
  ck(f'affine_negative_tail_{alpha}_{beta}_{m}',got==expect)
 for m in [0,1,9,17]:
  ck(f'mass_tail_{m}',tail(0,1,m)==F(4)**(-m))
  ck(f'contrast_tail_{m}',tail(3,-1,m)==3*m*F(4)**(-m))
 # At s1=s0=1, slopes1/2 and eta0, the AM-GM baseline is0.
 # Constant profiles attain it at d=0; on d=1/2 this is a nontight lower bound.
 for N in [0,1,4,9]:ck('constant_equality_'+str(N),dual(F(1),F(1),[F(1,2)]*N,[F(1,2)]*N,F(0),F(1,2),fault)==0)
 # eta contribution is exact even when the bound is not tight.
 args=(F(1),F(1),[F(3,4),F(2,3)],[F(1,4),F(1,3)],F(2))
 ck('contrast_affine_difference',dual(*args,F(1,2),fault)-dual(*args,F(1,3))==F(1,3))
 J,M,ell,U,P,Q=constants(F(1),F(1),F(1,2))
 ck('explicit_half_constants',(J,M,ell,U,P,Q)==(F(320,9),F(160),F(1,48),F(24),F(368800,9),F(2)))
 for d in [F(1,10),F(1,2),F(-1,2),F(749,1000)]:
  for eps in [F(1,10**6),F(1,10**12),F(1,10**30)]:
   z=budget(F(1),F(9,10),d,eps,fault)
   ck(f'budget_{d}_{eps}',z['total']<eps and 0<z['slope_mesh']<z['ell']/2)
 # Genuine exact sqrt enclosure ensures conversion input, though dual validity only needs positivity.
 for x in [F(1,7),F(4),F(19,23),F(10**12,3)]:
  rt=root_down(x);ck('sqrt_input_'+str(x),rt*rt<=x<(rt+F(1,10**20))**2)
 return out
FAULTS=['edge_factor','contrast','junction','mesh_budget']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 cover=converted_cover();lower=min(F(row['global_lower']) for row in cover)
 ckcover=prior.cover_ok(prior.INPUTS);assert ckcover and len(cover)==61 and lower>F('0.83103')
 for f in ['missing_rectangle','negative_slope']:
  try:converted_cover(f)
  except AssertionError as exc:faults[f]=[str(exc) or 'positive-slope precondition failed']
  else:raise AssertionError(('undetected',f))
 # Reuse only the prior feasible witness; no inherited full validation sweep.
 p0,x,c=prior.old.reference();energy,*_=prior.old.energy(x,c,F(105488613,10**8),F(86390048,10**8));assert energy.b<F('0.831205')
 deps=['explorations/conditional-build/k2196-detector-primal-dual-certificates-2026-10-28.md','explorations/conditional-build/k2176-detector-certified-convergence-2026-10-27.md','explorations/conditional-build/k2188-detector-variational-structure-2026-10-28.md','explorations/conditional-build/k2194-detector-optimizer-structure-2026-10-28.md','tests/channel-swings/k2176_detector_certified_convergence_probe.py','tests/channel-swings/k2174_joint_coherence_detector_probe.py','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py']
 budgets=[{k:str(v) for k,v in budget(F(1),F(1),F(1,2),F(1,10**n)).items()} for n in [6,12,30]]
 report=dict(result_id='K2196',status='conditional_exact_certificates',checks=cs,fault_failures=faults,explicit_half_budgets=budgets,inherited_cover_rational_reverification=dict(rectangles=61,lower=str(lower),upper=str(energy.b),new_sharper_bracket=False,cells=cover),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written uniform multiplier/slope bounds and cutoff/mesh theorem. Exact rational controls and inherited61-cell numerical bracket re-verification are separate evidence kinds. No efficient grid complexity, shooting convergence or joint uniqueness.')
 dst=ROOT/'lab/process/k2196-detector-primal-dual-certificates.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2196',controls=len(cs),faults=faults,rectangles=61,lower_float_display=float(lower),upper_float_display=float(energy.b),cutoffs=[z['N'] for z in budgets])))
if __name__=='__main__':main()
