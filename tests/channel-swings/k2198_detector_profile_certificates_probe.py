#!/usr/bin/env python3
"""Exact finite primal-dual profile and whole-tail certificate; no float proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,json
import k2196_detector_primal_dual_certificates_probe as dual
from k2168_finite_budget_moment_envelope_probe import IV,sqrtq
ROOT=Path(__file__).resolve().parents[2];C=F(40,3)
def sqrt_iv(x):return IV(sqrtq(x.a).a,sqrtq(x.b).b)
def exact_root(x):
 x=F(x);a=isqrt(x.numerator);b=isqrt(x.denominator);assert a*a==x.numerator and b*b==x.denominator;return F(a,b)
def coordinate_box(n,u1,u0,eps,s1,s0):
 assert eps>=0 and u1>0 and u0>0 and s1>0 and s0>0
 a=4*u1*u1;b=4*u0*u0;assert a!=b
 L1=(1+2*u1)*sqrtq(8*u1*eps/(C*s1*(n+1)*dual.p(n))).b
 L0=(1+2*u0)*sqrtq(8*u0*eps/(C*s0*(n+1)*dual.p(n))).b
 center=(1-b)/(a-b);radius=(L1+L0)/abs(a-b)
 return IV(max(F(0),center-radius),min(F(1),center+radius))
def barrier(Klo,Khi,N,sigma,rho,fault=None):
 q=(1+F(1,N+1))/4
 return (Klo<=1+q if fault=='barrier_direction' else Klo>1+q) and 0<sigma<=rho<1 and 1/sigma+sigma/4>=Khi and 1/rho+q*rho<=Klo

def controls(fault=None):
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v))
 e=F(9,25);en=F(16,25);p=F(3,4);u=F(1,3);ss=F(7,6)
 x=p*e;xn=p*en/4
 gap=C*ss*((u*x+xn/u)/2-exact_root(x*xn))
 residual=(2*u*exact_root(e)-exact_root(en))**2
 coeff=C*ss*p/((4 if fault=='gap_factor' else 8)*u)
 ck('original_edge_exact_square',gap==coeff*residual)
 ck('gap_nonnegative',gap>0)
 # Exact zero-gap tangent slopes on two rational points of the unit circle.
 u1=F(2,3);u0=F(3,8);aa=(2 if fault=='ratio_factor' else 4)*u1*u1;bb=4*u0*u0
 ck('zero_gap_coordinate_identity',(aa-bb)*e==1-bb and en==aa*e)
 for n in [0,2,7]:
  eps=F(1,10**8);box=coordinate_box(n,u1,u0,eps,F(1),F(1));ck('coordinate_contains_exact_point_'+str(n),box.a<=e<=box.b)
 # Independent recurrence algebra on exact Pythagorean triples.
 ep,ec,ef=F(9,25),F(16,25),F(144,169);s1,s0=F(6,5),F(4,5);da=dual.aa(s1)-dual.aa(s0)
 for n in [1,2,7,19]:
  g1=n*exact_root(ep/ec)+F(n+1,4)*exact_root(ef/ec)
  g0=n*exact_root((1-ep)/(1-ec))+F(n+1,4)*exact_root((1-ef)/(1-ec))
  eta=((n+F(1,2))*da-C*(s1*g1-s0*g0))/(3*n-1)
  k=(F(5,4)*s1-(da-3*eta)/C)/s0
  c=s1/(4*s0)-(da/2+(-eta if fault=='eta_sign' else eta))/(C*s0)
  fac=F(1) if fault=='omit_1_over_n' else 1+F(1,n)
  kn=k+s1/s0*(exact_root(ep/ec)-1+fac*(exact_root(ef/ec)-1)/4)+c/n
  lhs=exact_root((1-ep)/(1-ec))+(1+F(1,n))*exact_root((1-ef)/(1-ec))/4
  ck('original_recurrence_kn_'+str(n),kn==lhs)
 ck('safe_barrier',barrier(F(2),F(3),2,F(1,3),F(3,5),fault))
 ck('reject_unsafe_upper_barrier',not barrier(F(2),F(3),2,F(1,10),F(1,10),fault))
 ck('reject_unsafe_lower_barrier',not barrier(F(2),F(3),2,F(3,5),F(3,5),fault))
 for t in [F(1,16),F(1,36),F(1,4)]:
  M=7
  mass=sum(t**j for j in range(M))+t**M/(1-t)
  moment=sum(j*t**j for j in range(M))+t**M*(M/(1-t)+t/(1-t)**2)
  ck('geometric_mass_'+str(t),mass==1/(1-t));ck('geometric_moment_'+str(t),moment==t/(1-t)**2)
 return cs

def certificate():
 p,x,c=dual.prior.old.reference();s1=F(105488613,10**8);s0=F(86390048,10**8);e=[xx/pp for xx,pp in zip(x,p)]
 u1=[dual.root_down(e[n+1]/e[n])/2 for n in range(9)]
 u0=[dual.root_down((1-e[n+1])/(1-e[n]))/2 for n in range(9)]
 eta=-(dual.aa(s1)-dual.aa(s0))/2+C*(s1*u1[0]-s0*u0[0])/2
 energy,w,m,*_=dual.prior.old.energy(x,c,s1,s0)
 assert 3*m-w==F(1,2) and all(0<xx<pp for xx,pp in zip(x,p)) and 0<c<1
 U=energy.b;D=dual.dual(s1,s0,u1,u0,eta,F(1,2));eps=U-D;assert eps>0
 boxes=[coordinate_box(n,u1[n],u0[n],eps,s1,s0) for n in range(3)]
 assert boxes[0].a>0 and boxes[0].b<1 and boxes[1].a>0 and boxes[1].b<1
 et=C/4*(s1*sqrt_iv(boxes[1]/boxes[0])-s0*sqrt_iv((1-boxes[1])/(1-boxes[0])))-(dual.aa(s1)-dual.aa(s0))/2
 kv=(F(5,4)*s1-(dual.aa(s1)-dual.aa(s0)-3*et)/C)/s0
 cv=s1/(4*s0)-((dual.aa(s1)-dual.aa(s0))/2+et)/(C*s0)
 assert boxes[2].a>=F(7,8) and boxes[2].b<=F(199,200)
 N=2;rt=sqrtq(F(7,8)).a;q=(1+F(1,N+1))/4
 lo=kv.a-s1/s0*(1-rt)-max(-cv.a,F(0))/(N+1)
 hi=kv.b+s1/(4*s0)*(1+F(1,N+1))*(1/rt-1)+max(cv.b,F(0))/(N+1)
 assert lo>F(13,6) and hi<F(37,12) and barrier(lo,hi,N,F(1,3),F(1,2))
 def down(v):return F((v*10**12).__floor__(),10**12)
 def up(v):return -down(-v)
 return dict(s1=str(s1),s0=str(s0),contrast='1/2',inherited_witness='K2174.reference',dual_slopes1=list(map(str,u1)),dual_slopes0=list(map(str,u0)),chosen_dual_eta=str(eta),energy_upper_exact=str(U),dual_lower_exact=str(D),gap_exact=str(eps),energy_upper=str(up(U)),dual_lower=str(down(D)),gap_upper=str(up(eps)),optimizer_coordinate_boxes=[[str(down(z.a)),str(up(z.b))] for z in boxes],true_eta_interval=[str(down(et.a)),str(up(et.b))],N=N,Kminus_lower=str(down(lo)),Kplus_upper=str(up(hi)),sigma='1/3',rho='1/2',exact_tail='(1/200)*9^(-m) <= 1-e_(2+m) <= (1/8)*4^(-m), every integer m>=0',scope='Unique optimizer at this fixed rational squeeze pair, not joint squeeze optimum; new profile enclosure using inherited feasible witness, not new energy bracket.')
FAULTS=['gap_factor','ratio_factor','omit_1_over_n','eta_sign','barrier_direction']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 cert=certificate()
 deps=['explorations/conditional-build/k2198-detector-profile-certificates-2026-10-28.md','explorations/conditional-build/k2194-detector-optimizer-structure-2026-10-28.md','explorations/conditional-build/k2196-detector-primal-dual-certificates-2026-10-28.md','tests/channel-swings/k2196_detector_primal_dual_certificates_probe.py','tests/channel-swings/k2176_detector_certified_convergence_probe.py','tests/channel-swings/k2174_joint_coherence_detector_probe.py','tests/channel-swings/k2168_finite_budget_moment_envelope_probe.py']
 report=dict(result_id='K2198',status='conditional_exact_profile_certificate',checks=cs,fault_failures=faults,finite_certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Written universal coordinate-coercivity and backward-contraction proofs; exact rational finite profile/tail certificate; inherited energy witness. No arbitrary shooting or joint uniqueness/practical complexity certification.')
 dst=ROOT/'lab/process/k2198-detector-profile-certificates.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2198',controls=len(cs),faults=faults,tail=cert['exact_tail'],gap=cert['gap_upper'])))
if __name__=='__main__':main()
