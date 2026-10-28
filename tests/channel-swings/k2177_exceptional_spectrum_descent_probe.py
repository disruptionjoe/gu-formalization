#!/usr/bin/env python3
"""Real scalar-square descent: exact tangent-grade and original-equation controls."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
import sympy as S
from k2173_general_mixed_port_constraints_probe import reduction,grade,scalar
from k2171_mixed_port_euler_filter_probe import G,I,ETA,W,N,OM,mm,add,scale,blade,port,inv,bar,comm,neg,kernel,C,RR,K,filt
WM=sum(1<<i for i in W)
def tang(z,d):return {m:c for m,c in z.items() if (m&WM).bit_count()==d}
def rev(z,fault=None):
 return {m:c*((-1)**(m.bit_count()*(m.bit_count()-1)//2))*(-1 if fault=='reversion_parity' and m.bit_count()==10 else 1) for m,c in z.items()}
def controls(fault=None):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v))
 a,c=S.symbols('a c',real=True);A=42*c-1470*a;B=(49*a+315*c)/2
 ck('mixed_grade_coefficients',S.expand(A-2*B)==-1519*a-273*c and S.expand(A+6*B)==-1323*a+987*c)
 ck('mixed_grade_nonzero_determinant',S.Matrix([[-1519,-273],[-1323,987]]).det()==-1860432)
 ck('degenerate_grade_coefficients',182+126*2==434 and 182-126*6==-574)
 v=blade(N[:7])
 umix=add(blade(N[:3]),scale(blade([N[3],N[7],N[8]]),F(1,3)),scale(blade([N[4],N[5],N[9]]),F(1,5)))
 utilt=mm(mm(add(G[N[0]],scale(G[N[7]],2)),add(G[N[1]],scale(G[N[8]],3))),add(G[N[2]],scale(G[N[9]],4)))
 for label,u in [('mixed',umix),('three_tilt',utilt)]:
  a,c,x,y,d,e=reduction(v,u);U=K(x);J=grade(y,10);t=mm(OM,u)
  ck(label+'_scalar_squares',mm(v,v)==scale(I,a) and mm(t,t)==scale(I,c))
  ck(label+'_both_x_grades',bool(grade(x,4)) and bool(grade(x,8)))
  ck(label+'_tangent4_ports',all(tang(z,4)==z for z in [x,y,U,J]))
  ck(label+'_tangent0_products',all(tang(mm(z,w),0)==mm(z,w) for z,w in [(x,x),(U,x),(U,y),(x,y),(J,x)]))
  if fault=='linear_x_coefficient':e=add(e,x)
  if fault=='linear_U_coefficient':e=add(e,U)
  e4=tang(e,0 if fault=='tangent_projection' else 4)
  A=42*c-1470*a;B=F(49*a+315*c,2);beta=-49*a-153*c;dd=49*a+225*c
  lin=add(scale(x,A),scale(U,-B),scale(y,beta),scale(J,-8*dd))
  ck(label+'_tangent4_projection',e4==lin)
  even=scale(add(e4,rev(e4,fault)),F(1,2))
  ck(label+'_reversion_even_projection',even==add(scale(x,A),scale(U,-B)))
  ck(label+'_normal4_projection',grade(even,4)==scale(grade(x,4),-1519*a-273*c))
  ck(label+'_normal8_projection',grade(even,8)==scale(grade(x,8),-1323*a+987*c))
  ck(label+'_necessary_filter_rejects',bool(even))
  r,p,fl,_,_,_=filt(v,u)
  ck(label+'_quartic_original_Euler',fl==scale(mm(e,inv(d)),-144))
  # Full original equations: independent consumer of the proposed rejection.
  ts={j:scale(mm(inv(p),port(r)[j]),-ETA[j]) for j in N};z=add(v,t)
  qs={j:RR(ts,*C(port(z),*kernel(ts,j)))[1] for j in N}
  q=add(*(mm(qs[j],G[j]) for j in N))
  ck(label+'_full10_match_quartic',scale(mm(bar(p),q),6)==scale(mm(e,inv(d)),-144))
  ck(label+'_full10_rejects',any(qs.values()))
 # Released successor: actual commuting NONscalar-square ports use the generic filter.
 vv=add(blade(N[:7]),scale(blade([N[i] for i in [0,1,2,3,4,7,8]]),F(2,3)))
 uu=add(blade(N[:3]),scale(blade([N[i] for i in [0,3,4]]),F(1,5)));tt=mm(OM,uu)
 V=mm(vv,vv);T=mm(tt,tt);av=scalar(V);cv=scalar(T);hh=mm(vv,tt);U=K(hh)
 ck('nonscalar_commuting_fixture',not comm(vv,tt))
 ck('nonscalar_scope_refused',bool(add(V,scale(I,-av))) and bool(add(T,scale(I,-cv))))
 ck('nonscalar_V_exact',V==add(scale(I,F(13,9)),scale(blade([N[i] for i in [5,6,7,8]]),-F(4,3))))
 ck('nonscalar_T_exact',T==add(scale(I,F(24,25)),scale(blade([N[i] for i in [1,2,3,4]]),-F(2,5))))
 kv=add(scale(V,2 if fault!='defect_grade_weight' else 10),scale(I,8*av));kt=add(scale(T,2),scale(I,8*cv))
 ck('nonscalar_grade_operator',K(V)==kv and K(T)==kt)
 rr,pp,fl,aa,bb,ww=filt(vv,uu);ss=add(scale(vv,7),scale(tt,9))
 Ap=add(scale(V,60),scale(T,-252),scale(I,24*av+216*cv),scale(hh,-348),scale(U,-18))
 Bp=add(scale(V,780),scale(T,324),scale(I,312*av-648*cv),scale(hh,-60),scale(U,-90))
 ck('nonscalar_A_B_actual',aa==Ap and bb==Bp)
 ck('nonscalar_pencil_invertible',mm(pp,inv(pp))==I and not comm(pp,ss))
 pol=add(mm(Ap,ss),neg(mm(Bp,pp)))
 ck('nonscalar_clear_denominator',pol==mm(fl,pp))
 q0=add(mm(add(scale(V,10),scale(T,16),scale(I,4*av-12*cv)),vv),scale(mm(U,tt),3))
 q4=add(mm(add(scale(V,142),scale(T,36),scale(I,68*av-108*cv)),tt),scale(mm(U,vv),7))
 ck('nonscalar_polynomial_tangent0',tang(pol,0)==scale(q0,-504 if fault!='polynomial_factor' else -503))
 ck('nonscalar_polynomial_tangent4',tang(pol,4)==scale(q4,72))
 square=add(scale(mm(V,V),35),scale(mm(V,T),-157 if fault!='square_elimination' else -156),scale(mm(T,T),-54),scale(V,14*av-42*cv),scale(T,-102*av+162*cv))
 ck('nonscalar_square_only_elimination',add(scale(mm(q0,vv),7),scale(mm(q4,tt),-3))==scale(square,2))
 ck('nonscalar_square_only_rejects',bool(square))
 ts={j:scale(mm(inv(pp),port(rr)[j]),-ETA[j]) for j in N};zz=add(vv,tt)
 qs={j:RR(ts,*C(port(zz),*kernel(ts,j)))[1] for j in N}
 q=add(*(mm(qs[j],G[j]) for j in N))
 ck('nonscalar_original10_euler',scale(mm(bar(pp),q),6)==fl)
 ck('nonscalar_fixture_rejected',bool(q0) and bool(q4) and sum(bool(z) for z in qs.values())==9)
 return out

from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 cs=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
 faults={}
 for fault in FAULTS:
  bad=[n for n,v in controls(fault).items() if not v];assert bad,('undetected',fault);faults[fault]=bad
 extra={}
 deps=['explorations/conditional-build/k2177-exceptional-spectrum-descent-2026-10-28.md', 'tests/channel-swings/k2173_general_mixed_port_constraints_probe.py', 'tests/channel-swings/k2171_mixed_port_euler_filter_probe.py', 'tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py', 'explorations/conditional-build/k2175-mixed-grade-euler-localization-2026-10-27.md']
 report=dict(result_id='K2177',status='conditional_exact_controls',checks=cs,fault_failures=faults,certificate=extra,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written proof independently reconstructed; finite formula controls supplement rather than replace universal acceptance. No proof-assistant, physical quotient or apparatus cost claim.')
 dst=ROOT/'lab/process/k2177-exceptional-spectrum-descent.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2177',checks=len(cs),faults=faults)))
FAULTS=['linear_x_coefficient', 'linear_U_coefficient', 'tangent_projection', 'reversion_parity', 'defect_grade_weight', 'polynomial_factor', 'square_elimination']
if __name__=='__main__':main()
