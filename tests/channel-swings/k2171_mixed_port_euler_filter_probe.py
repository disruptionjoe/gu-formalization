#!/usr/bin/env python3
"""Exact mixed Euler contraction and commuting and anticommuting class polynomial controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as S
from k2169_invertible_pencil_full_descent_probe import G,I,ETA,W,N,OM,mm,add,scale,blade,port,inv,bar,comm,neg,kernel,C,RR
ROOT=Path(__file__).resolve().parents[2]
def K(x):return add(*(scale(mm(mm(G[j],x),G[j]),ETA[j]) for j in N))
def filt(v,u,fault=None):
 r=add(v,scale(mm(OM,u),3));b=bar(r);p=add(r,scale(b,6));s=add(scale(r,5),scale(b,2));ww=mm(inv(p),s)
 bb=mm(b,b);rr=mm(r,r);rb=mm(r,b);br=mm(b,r)
 aa=add(scale(K(bb),3),scale(bb,34),scale(rb,36),scale(br,8),scale(rr,-24))
 be=add(scale(rr,184),scale(rb,140),scale(br,184),scale(bb,194),scale(K(br),24),scale(K(bb),15))
 if fault=='product_order':aa=add(aa,scale(add(br,neg(rb)),36))
 if fault=='K_coefficient':be=add(be,K(bb))
 return r,p,add(mm(aa,ww),neg(be)),aa,be,ww

def controls(fault=None):
 out={};ck=lambda n,x:out.__setitem__(n,bool(x))
 v=add(blade(N[:7]),scale(blade(N[3:]),F(2,3)));u=add(scale(blade(N[1:4]),F(1,5)),scale(blade(N[5:8]),F(2,7)))
 r,p,filter_,aa,be,ww=filt(v,u,fault);z=add(v,mm(OM,u));ts={j:scale(mm(inv(p),port(r)[j]),-ETA[j]) for j in N}
 qs={j:RR(ts,*C(port(z),*kernel(ts,j)))[1] for j in N}
 q=add(*(scale(mm(qs[j],G[j]),ETA[j] if fault=='extra_eta' else 1) for j in N))
 lhs=scale(mm(bar(p),q),6)
 ck('Euler_matches_original_all10_noncommuting_rows',lhs==filter_)
 ck('filter_rejects_noncommuting_fixture',bool(filter_))
 ck('trace_cyclic_K_formula',all(mm(aa,ww).get(m,0)-be.get(m,0)==mm(aa,ww).get(m,0)-184*mm(r,r).get(m,0)-564*mm(r,bar(r)).get(m,0)-344*mm(bar(r),bar(r)).get(m,0) for m in [0,sum(1<<i for i in W)]))
 # Direct grade-K instrument on every possible product grade of commuting 7 and 3.
 ck('K_grade4_and8',all(K(blade(N[:d]))==scale(blade(N[:d]),kap) for d,kap in [(4,2),(8,-6)]))
 a,b,k=S.symbols('a b k',real=True)
 # Commutative four-dimensional formal algebra v^2=a, t^2=b; h=vt.
 def mul(x,y):
  o=[0]*4
  for i,c in enumerate(x):
   for j,d in enumerate(y):o[i^j]+=c*d*(a if i&j&1 else 1)*(b if i&j&2 else 1)
  return [S.expand(c) for c in o]
 A=[84*a-36*b,0,0,(-349 if fault=='mixed_coefficient' else -348)-18*k];B=[1092*a-324*b,0,0,-60-90*k]
 residual=[S.expand(x-y) for x,y in zip(mul(A,[0,7,9,0]),mul(B,[0,7,-15,0]))]
 ck('commuting_filter_v_coefficient',S.expand(residual[1]+72*(98*a+(28+21*k)*b))==0)
 ck('commuting_filter_t_coefficient',S.expand(residual[2]-72*((210+7*k)*a-72*b))==0)
 # Independent linear consequences for both possible K eigenvalues.
 for kap in [2,-6]:
  mat=S.Matrix([[98,28+21*kap],[210+7*kap,-72]])
  if fault=='eigenvalue':mat=S.Matrix([[98,28+21*F(14,3)],[210+7*F(14,3),-72]])
  ck('nonzero_linear_determinant_'+str(kap),mat.det()==({2:-22736,-6:9408}[kap]))
 f=98*a*a-602*a*b+216*b*b
 ck('degenerate_a9b_polynomial',S.expand(f.subs(a,9*b))==2736*b*b)
 # Direct geometric coordinate cases, independent of the symbolic scalar table.
 for overlap in [1,3]:
  vv=blade(N[:7]);inds=N[:overlap]+N[7:7+3-overlap];uu=scale(blade(inds),F(1,3));tt=mm(OM,uu);h=mm(vv,tt)
  ck('commuting_coordinate_overlap_'+str(overlap),not comm(vv,tt) and bool(filt(vv,uu)[2]))
  r,p,fl,aa,bb,ww=filt(vv,uu);av=mm(vv,vv)[0];bv=mm(tt,tt)[0]
  aexpect=add(scale(I,84*av-36*bv),scale(h,-348),scale(K(h),-18))
  bexpect=add(scale(I,1092*av-324*bv),scale(h,-60),scale(K(h),-90))
  if fault=='scalar_square_sign':aexpect=add(aexpect,scale(I,72*bv))
  ck('commuting_A_B_expansion_'+str(overlap),aa==aexpect and bb==bexpect)
 # Anticommuting scalar-square reduction checked symbolically and against the full filter formula.
 d=49*a+225*b
 f_anti=343*a*a+1491*a*b-540*b*b
 # h^2=-ab, all other expressions are scalar + h.
 scalar=(84*a-36*b)*(49*a-135*b)+168*168*a*b-d*(1092*a-324*b)
 hcoef=(84*a-36*b)*168-168*(49*a-135*b)-d*(264+144*k)
 ck('anticommuting_scalar_reduction',S.expand(scalar+144*f_anti)==0)
 ck('anticommuting_h_reduction',S.expand(hcoef+144*(49*a+297*b+d*k))==0)
 ck('anticommuting_grade6_obstruction',S.expand(f_anti.subs(a,-S.Rational(153,49)*b))==-S.Rational(12960,7)*b*b)
 ck('anticommuting_grade10_obstruction',S.expand(f_anti.subs(a,-S.Rational(217,49)*b))==-416*b*b)
 for overlap in [0,2]:
  vv=blade(N[:7]);uu=scale(blade(N[:overlap]+N[7:7+3-overlap]),F(1,3));tt=mm(OM,uu);h=mm(vv,tt)
  r,p,fl,aa,be,ww=filt(vv,uu);av=mm(vv,vv)[0];bv=mm(tt,tt)[0];dd=49*av+225*bv
  ck('anticommuting_coordinate_overlap_'+str(overlap),not add(mm(vv,tt),mm(tt,vv)) and bool(fl))
  ck('anticommuting_pencil_square_'+str(overlap),mm(p,p)==scale(I,dd))
  expect=scale(add(scale(I,343*av*av+1491*av*bv-540*bv*bv),scale(h,49*av+297*bv),scale(K(h),dd)),-F(144,dd))
  ck('anticommuting_filter_formula_'+str(overlap),fl==expect)
 # Polynomial multiplier for K(h) elimination, independent formal expansion.
 x=(98*a+28*b);y=-210*a+72*b
 ck('scalar_elimination_f',S.expand(x*a+3*y*b-f)==0)
 ck('h_elimination_coefficient',S.expand(3*x+y-(84*a+156*b))==0)
 return out
FAULTS=['product_order','K_coefficient','extra_eta','eigenvalue','scalar_square_sign','mixed_coefficient']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls();assert all(cs.values()),cs
 faults={}
 for f in FAULTS:
  bad=[n for n,p in controls(f).items() if not p];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2171-mixed-port-euler-filter-2026-10-27.md','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','explorations/conditional-build/k2169-invertible-pencil-full-descent-2026-10-27.md','tests/channel-swings/k2159_commutant_equation_adapters_probe.py','tests/channel-swings/k2165_even_clifford_adapter_descent_probe.py']
 report=dict(result_id='K2171',status='conditional_exact_controls',checks=cs,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written contraction and commuting and anticommuting scalar-square class proofs independently reviewed; finite controls check original maps and symbolic identities, not all mixed ports.')
 dest=ROOT/'lab/process/k2171-mixed-port-euler-filter.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2171',checks=len(cs),faults=faults)))
if __name__=='__main__':main()
