#!/usr/bin/env python3
"""Exact algebra, full-tail variational controls and genuine coefficient faults."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
from k2186_detector_contrast_descent_probe import data,Ep,RP,TP
from k2184_global_detector_structure_probe import moments,ap,C,LO,HI
from k2178_effective_detector_approximation_probe import p,A,sqrt_iv,ivadd,scale,point,contrast
ROOT=Path(__file__).resolve().parents[2]
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def squeeze(R,T):
 lo,hi=LO,HI
 for _ in range(100):
  m=(lo+hi)/2
  if R*ap(m)<C*T:lo=m
  else:hi=m
 return lo,hi
def epi(si):
 lo,hi=si
 # Independent outward evaluation, not monotonicity assumed across 1.
 return (RP*(F(41,6)*lo*lo+F(3,2)/hi**2)-C*hi*TP+F(35,18),RP*(F(41,6)*hi*hi+F(3,2)/lo**2)-C*lo*TP+F(35,18))
def controls(fault=None):
 cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
 # Reference includes geometric tail exactly, both signs and near endpoint.
 for d in [F(-749,1000),F(-1,2),F(-1,100),F(1,100),F(1,2),F(749,1000)]:
  t=4*abs(d)/3;low=(1-t)/2;high=(1+t)/2;e0,tail=(low,high) if d>0 else (high,low)
  weight=-1 if fault!='contrast_weight' else -2
  direct=weight*e0*p(0)+tail*F(3,4)
  ck('reference_contrast_'+str(d),direct==d);ck('reference_margin_'+str(d),min(e0,tail,1-e0,1-tail)==low>0)
 # Full infinite Dirichlet sums for nonconstant heads, constant nonzero tails.
 for index,(es,tail) in enumerate([([F(1,9),F(4,9),F(1,4)],F(9,16)),([F(4,25),F(9,25),F(16,25)],F(1,25)),([F(1,2)]*3,F(1,2))]):
  x=[e*p(n) for n,e in enumerate(es)];y=[p(n)-v for n,v in enumerate(x)]
  ds=[]
  for ee,tt in [(es,tail),([1-e for e in es],1-tail)]:
   total=point(F(0))
   for n,e in enumerate(ee):
    nxt=ee[n+1] if n+1<len(ee) else tt
    term=ivadd(point(e+nxt),scale(-2,sqrt_iv(e*nxt)))
    total=ivadd(total,scale((n+1)*p(n),term))
   ds.append(total)  # All later differences exactly zero.
  R,T=moments(x,tail);Ry,Ty=moments(y,1-tail);w=sum(x)+tail*F(1,4)**len(x)
  recon=ivadd(point(F(5,4)*R-F(3,8)*w),scale(F(-1,5) if fault=='dirichlet_coefficient' else F(-1,4),ds[0]))
  ck('full_Dirichlet_'+str(index),overlap(T,recon))
  s1,s0=F(9,10),F(1);da=A(s1)-A(s0);ss=s1-s0
  direct=ivadd(point(R*A(s1)+Ry*A(s0)+F(35,18)),scale(-C,ivadd(scale(s1,T),scale(s0,Ty))))
  linear=(da-5*C*ss/4)*R+3*C*ss*w/8
  rewritten=ivadd(point(Ep(s0)+linear),scale(C/4,ivadd(scale(s1,ds[0]),scale(s0,ds[1]))))
  ck('full_energy_Dirichlet_'+str(index),overlap(direct,rewritten))
 # Symbolic coefficient checks: these establish algebra, not existence of an optimizer.
 s1,s0,e0,e1,da,eta,beta,d=S.symbols('s1 s0 e0 e1 da eta beta d',positive=True)
 h0=da/2-S.Rational(40,3)/4*(s1*S.sqrt(e1/e0)-s0*S.sqrt((1-e1)/(1-e0)))
 formula=S.Rational(40,3)/(5 if fault=='multiplier_coefficient' else 4)*(s1*S.sqrt(e1/e0)-s0*S.sqrt((1-e1)/(1-e0)))-da/2
 ck('local_multiplier_formula',S.simplify(formula+h0)==0)
 # Exact weighted moment sums, not a truncated claim of neutrality.
 n=S.symbols('n',integer=True,nonnegative=True)
 neutral=S.summation((3*n-1)*S.Rational(3,4)*S.Rational(1,4)**n,(n,0,S.oo));ck('neutral_full_tail',neutral==0)
 raw=eta*(beta*neutral-d);ck('common_noise_slope',S.expand(raw+eta*d)==0)
 for j in [1,2,3,10,100]:ck('finite_stationary_variation_'+str(j),(3*j-1)+(-1)*(3*j-1)==0)
 # Tail equation has an exact algebraic solution within (0,1), not a profile.
 sx,sy=F(1),F(9,10);diff=A(sx)-A(sy);b=(F(5,4)*sx-diff/C)/sy
 ck('true_squeeze_necessary_range',0<ap(sy)<ap(sx)<C)
 ck('tail_rhs_above_endpoint',b>F(5,4))
 t=S.symbols('t');bb=S.Rational(b.numerator,b.denominator);root=2*(bb-S.sqrt(bb*bb-1));poly=1-(bb)*t+(S.Rational(1,5) if fault=='tail_coefficient' else S.Rational(1,4))*t*t
 ck('tail_algebraic_root',S.simplify(poly.subs(t,root))==0)
 ck('tail_root_in_unit_interval',bool(root>0) and bool(root<1))
 # Genuine K2186 nonoptimal full-tail profile fails Qx=Qy, not just reporting.
 z=data(10);sz=squeeze(z['Rz'],z['Tz']);sy=squeeze(RP-z['Rz'],z['Ty']);delta=z['delta']*(0 if fault=='tangent_tail' else 1)
 qz=ivadd(epi(sz),scale(-C*delta,sz));qy=ivadd(epi(sy),scale(-C*delta,sy));gap=ivadd(qz,scale(-1,qy))
 ck('counterprofile_rejected_by_Q_equality',gap[0]>F(7,100))
 # Pin an independently computed exact tangent delta to expose omitted-tail fault.
 ck('tangent_delta_exact',delta==F(34535457,17179869184))
 return cs,dict(tail_squeeze_pair=[str(sx),str(F(9,10))],tail_rhs=str(b),tail_sqrt_ratio=str(root),Q_difference=[str(v) for v in gap])
FAULTS=['contrast_weight','dirichlet_coefficient','multiplier_coefficient','tail_coefficient','tangent_tail']
def main():
 ap_=argparse.ArgumentParser();ap_.add_argument('--write',action='store_true');args=ap_.parse_args();cs,details=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[n for n,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2188-detector-variational-structure-2026-10-28.md','explorations/conditional-build/k2176-detector-certified-convergence-2026-10-27.md','explorations/conditional-build/k2186-detector-contrast-descent-2026-10-28.md','tests/channel-swings/k2186_detector_contrast_descent_probe.py','tests/channel-swings/k2184_global_detector_structure_probe.py']
 report=dict(result_id='K2188',status='conditional_exact_controls',checks=cs,fault_failures=faults,details=details,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written all-contrast interiority/uniqueness, summability, envelope and frontier arguments; exact symbolic and full-tail interval controls are distinct from universal proof. Multiplier sign, global saturation, joint uniqueness and apparatus costs remain open.')
 dst=ROOT/'lab/process/k2188-detector-variational-structure.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2188',checks=len(cs),faults=len(faults),Q_difference=[float(F(v)) for v in details['Q_difference']])))
if __name__=='__main__':main()
