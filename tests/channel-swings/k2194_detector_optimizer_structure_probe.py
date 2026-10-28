#!/usr/bin/env python3
"""Exact recurrence and root controls; the note proves the infinite theorem."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
Q=S.Rational

def controls(fault=None):
 out={}
 def ck(k,v):out[k]=bool(v)
 n=S.symbols('n',integer=True,nonnegative=True)
 eta,DA,DS=S.symbols('eta DA DS',real=True);C=Q(40,3)
 B=(DA-3*eta)/C-Q(5,4)*DS;D=(DA/2+eta)/C-DS/4
 fw=Q(1,5) if fault=='forward_weight' else Q(1,4)
 ck('affine_forcing',S.expand((n+Q(1,2))*DA/C-eta*(3*n-1)/C-(n+fw*(n+1))*DS-(n*B+D))==0)
 xm,x,xp,p,em,e,ep=S.symbols('xm x xp p em e ep',positive=True)
 raw=S.diff(n*S.sqrt(xm*x)+(n+1)*S.sqrt(x*xp),x)
 ratio=Q(1,5) if fault=='thermal_ratio' else Q(1,4)
 got=raw.subs({xm:p*em/ratio,x:p*e,xp:p*ratio*ep})
 ck('differentiated_geometric_gradient',S.simplify(got-(n*S.sqrt(em/e)+(n+1)*S.sqrt(ep/e)/4))==0)
 ck('contrast_summation_by_parts',S.expand(4*n-(n+1)-(3*n-1))==0)
 a,b,z,R=S.symbols('a b z R',positive=True);L=a*a+b*b
 alpha=(a*z+b*R)/L;beta=(a*R-b*z)/L
 ck('inversion_unsquared',S.cancel(a*alpha-b*beta-z)==0)
 ck('inversion_norm',S.factor((alpha**2+beta**2).subs(R**2,L-z*z)-1)==0)
 circles=[(Q(3,5),Q(4,5)),(Q(5,13),Q(12,13)),(Q(8,17),Q(15,17)),(Q(7,25),Q(24,25))]
 sign=1 if fault=='complement_sign' else -1
 def kval(u,v,s1,s0):return s1*S.sqrt(v/u)+sign*s0*S.sqrt((1-v)/(1-u))
 for i,(au,bu) in enumerate(circles):
  u=au**2
  for j,(av,bv) in enumerate(circles):
   v=av**2;s1=Q(5,4);s0=Q(2,3);aa=s1/au;bb=s0/bu;ll=aa*aa+bb*bb
   zz=kval(u,v,s1,s0);rad=S.sqrt(ll-zz*zz)
   recovered=S.simplify(((aa*zz+bb*rad)/ll)**2)
   ck(f'unique_next_rational_{i}_{j}',recovered==v)
   ck(f'correct_range_{i}_{j}',-bb<zz<aa)
   if i==j:ck(f'diagonal_K_{i}',zz==s1-s0)
   ck(f'monotone_K_{i}_{j}',S.sign(kval(u,v,s1,s0)-(s1-s0))==S.sign(v-u))
   # Rationalization of a difference in sqrt-complement coordinates.
   if v>u:
    delta=bu-bv
    forward=delta*(s0/bu+s1*(bu+bv)/(au*(au+av)))
    backward=(bu-bv)*(s0/bv+s1*(bu+bv)/(av*(au+av)))
    ck(f'forward_rationalization_{i}_{j}',S.simplify(kval(u,v,s1,s0)-(s1-s0)-forward)==0)
    ck(f'backward_rationalization_{i}_{j}',S.simplify((s1-s0)-kval(v,u,s1,s0)-backward)==0)
 # Explicit admissibility control: squaring a real radical outside the K range is false.
 aa=bb=S.Integer(1);zz=Q(6,5);ll=aa*aa+bb*bb
 allowed=(-bb<zz<aa) if fault!='admissibility' else (zz*zz<ll)
 vv=S.simplify(((aa*zz+bb*S.sqrt(ll-zz*zz))/ll)**2)
 ck('reject_exterior_real_radical',not allowed)
 ck('exterior_squared_branch_not_original',S.simplify(S.sqrt(vv)-S.sqrt(1-vv)-zz)!=0)
 for kk,rr in [(Q(5,4),S.Integer(1)),(Q(17,8),Q(1,2)),(Q(65,16),Q(1,4))]:
  root=2*kk+(2 if fault=='large_tail_root' else -2)*S.sqrt(kk*kk-1)
  ck(f'tail_root_{kk}',S.simplify(root)==rr)
  ck(f'tail_polynomial_{kk}',rr*rr-4*kk*rr+4==0)
  ck(f'fixed_point_{kk}',1/(kk-rr/4)==rr)
  ck(f'admissible_root_{kk}',0<root<=1)
 tt,kk=S.symbols('t k',real=True)
 ck('contraction_derivative',S.simplify(S.diff(1/(kk-tt/4),tt)-1/(4*(kk-tt/4)**2))==0)
 ck('contraction_uniform_bound',1/(4*(Q(5,4)-Q(1,4))**2)==Q(1,4))
 # Local max/min sign instrument. This is a finite control of the written argument.
 vals=[Q(1,5),Q(2,5),Q(3,5),Q(4,5)]
 for i,u in enumerate(vals):
  for j,v in enumerate(vals):
   for k,w in enumerate(vals):
    left=2*(kval(u,v,1,1))+Q(3,4)*kval(u,w,1,1)
    if u>=max(v,w):ck(f'maximum_nonpositive_{i}_{j}_{k}',left<=0)
    if u<=min(v,w):ck(f'minimum_nonnegative_{i}_{j}_{k}',left>=0)
 ck('first_flat_forces_negative_forcing',2*(S.sqrt(Q(1,4)/Q(1,2))-S.sqrt(Q(3,4)/Q(1,2)))<0)
 # B=0 amplification is an exact consequence; ratio tends1 in the proof.
 nn=S.symbols('n',positive=True)
 ck('critical_amplification_eventually_above2',S.limit(4*nn/(nn+1),nn,S.oo)==4)
 return out

FAULTS=['forward_weight','thermal_ratio','complement_sign','admissibility','large_tail_root']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2194-detector-optimizer-structure-2026-10-28.md','explorations/conditional-build/k2188-detector-variational-structure-2026-10-28.md','explorations/conditional-build/k2192-detector-smoothing-and-sign-2026-10-28.md']
 report=dict(result_id='K2194',status='conditional_exact_controls',checks=cs,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written affine-forcing maximum principle, polarized-tail proof, critical-case exclusion, backward contraction and infinite convex supporting argument. Symbolic/rational controls are not finite-prefix optimization certificates or a proof of joint uniqueness.')
 dst=ROOT/'lab/process/k2194-detector-optimizer-structure.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2194',controls=len(cs),faults=faults)))
if __name__=='__main__':main()
