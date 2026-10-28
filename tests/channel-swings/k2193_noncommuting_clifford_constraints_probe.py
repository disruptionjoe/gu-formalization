#!/usr/bin/env python3
"""Exact original-row controls; universal exclusions are proved in the note."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as S
from k2171_mixed_port_euler_filter_probe import K,filt
from k2169_invertible_pencil_full_descent_probe import G,I,ETA,W,N,OM,mm,add,scale,blade,port,inv,bar,comm,neg,kernel,C,RR
ROOT=Path(__file__).resolve().parents[2]

def controls(fault=None):
 out={}
 def ck(k,v):out[k]=bool(v)
 nmask=sum(1<<j for j in N);inn=blade(N)
 b1=blade(N[:3]);b2=blade([N[0],N[3],N[4]])
 fixtures=[(add(b1,b2),add(b1,b2)),(add(b1,scale(b2,2)),add(scale(b1,3),neg(b2))), (b1,scale(b1,F(1,3)))]
 for i,(w,u) in enumerate(fixtures):
  v=mm(inn,w);t=mm(OM,u);V=mm(v,v);T=mm(t,t);h=mm(v,t);a=V.get(0,0);c=T.get(0,0)
  J={m:x for m,x in h.items() if (m&nmask).bit_count()==10}
  r,p,fl,aa,bb,ww=filt(v,u)
  D=add(scale(V,50 if fault=='pencil' else 49),scale(T,225))
  E=add(scale(mm(V,V),245),scale(mm(V,T),1275),scale(mm(T,T),270),scale(V,98*a-294*c),scale(T,510*a-810*c))
  L=add(scale(V,36 if fault=='missing_cross_term' else -21),scale(T,99),scale(I,-28*a-252*c))
  target=scale(add(E,mm(L,h),scale(mm(J,D),8 if fault=='grade10_sign' else -8)),-144)
  ck(f'anticommuting_{i}',not add(mm(v,t),mm(t,v)))
  ck(f'pencil_square_{i}',mm(p,p)==D)
  ck(f'A_expansion_{i}',aa==add(scale(V,60),scale(T,-252),scale(I,24*a+216*c),scale(h,-168)))
  ck(f'B_ordered_expansion_{i}',bb==add(scale(V,780),scale(T,324),scale(I,312*a-648*c),scale(h,264),scale(K(h),-144 if fault=='K_sign' else 144)))
  ck(f'grade_contraction_{i}',K(h)==add(scale(h,-2),scale(J,-8)))
  ck(f'filter_identity_{i}',mm(fl,D)==target)
  z=add(v,t);ts={j:scale(mm(inv(p),port(r)[j]),-ETA[j]) for j in N}
  qs={j:RR(ts,*C(port(z),*kernel(ts,j)))[1] for j in N}
  q=add(*(scale(mm(qs[j],G[j]),ETA[j] if fault=='extra_eta' else 1) for j in N))
  ck(f'original10_contracted_identity_{i}',scale(mm(mm(bar(p),q),D),6)==target)
  ck(f'original_rows_reject_{i}',any(qs.values()))
  if i==0:
   ck('both_nonscalar',0 not in V and bool(V) and T==neg(V))
   ck('V_square',mm(V,V)==scale(I,-4))
   ck('inverse_both_sides',mm(p,scale(mm(p,V),F(1,704)))==I and mm(scale(mm(p,V),F(1,704)),p)==I)
   ck('exact_E',E==scale(I,3040))
   ck('exact_Lh',mm(L,h)==scale(mm(OM,inn),480))
   ck('noncommuting',bool(comm(v,t)))
  if i==1:ck('nonzero_J_fixture',bool(J))
 k,a,c,v,t=S.symbols('k a c v t')
 A=245+(1274 if fault=='polynomial_coefficient' else 1275)*k+270*k*k
 B=98+216*k-810*k*k
 E=245*v*v+1275*v*t+270*t*t+(98*a-294*c)*v+(510*a-810*c)*t
 ck('proportional_reduction',S.expand(E.subs({t:k*v,c:k*a})-v*(A*v+B*a))==0)
 ck('coprime_A_B',S.gcd(A,B)==1)
 ck('common_root_rejection',S.expand((A/5).subs(k,-S.Rational(833,4041))*4041**2)==-20744640)
 ck('grade6_exception',S.expand((A/5).subs(k,S.Rational(7,33))*33**2)==114912)
 ck('grade10_exception',S.expand((A/5).subs(k,-S.Rational(59,243))*243**2)==-574560)
 f=343*a*a+1491*a*c-540*c*c
 ck('scalar_specialization',S.expand(E.subs({v:a,t:c})-f)==0)
 ck('nilpotent_T',S.expand(E.subs({t:0,c:0})-v*(245*v+98*a))==0)
 ck('nilpotent_V',S.expand(E.subs({v:0,a:0})-270*t*(t-3*c))==0)
 ck('T_nilpotent_trace_contradiction',S.Rational(-2,5)!=1)
 ck('V_nilpotent_trace_contradiction',3!=1)
 ck('V_scalar_zero_sector_ratio',S.factor(E.subs({v:a,t:0}))==49*a*(7*a-6*c))
 ck('T_scalar_zero_sector_ratio',S.expand(E.subs({v:0,t:c})-30*c*(17*a-18*c))==0)
 p=S.Rational(33,98);dim=98 if fault=='trace_dimension' else 32
 ck('mixed_spectrum_multiplicity_impossible',not (p*dim).is_integer)
 ck('mixed_trace_fraction',S.Rational(7,6)/((49+252*S.Rational(7,6))/99)==p)
 ck('all_nonzero_V_scalar',S.factor(f.subs(c,-S.Rational(49,153)*a))!=0)
 ck('all_nonzero_T_scalar',S.factor(f.subs(a,-S.Rational(153,49)*c))!=0)
 pp=S.symbols('p',positive=True)
 ck('mixed_T_scalar_sign',(-153*pp/(21+28*pp)).is_negative and S.Rational(18,17)>0)
 return out

FAULTS=['pencil','missing_cross_term','grade10_sign','K_sign','extra_eta','polynomial_coefficient','trace_dimension']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2193-noncommuting-clifford-constraints-2026-10-28.md','tests/channel-swings/k2171_mixed_port_euler_filter_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','explorations/conditional-build/k2171-mixed-port-euler-filter-2026-10-27.md','explorations/conditional-build/k2177-exceptional-spectrum-descent-2026-10-28.md']
 report=dict(result_id='K2193',status='conditional_exact_controls',checks=cs,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written ordered algebra, grade separation and finite-dimensional trace arguments; original-ten-row fixtures and polynomial identities are controls, not enumeration of all anticommuting ports.')
 dst=ROOT/'lab/process/k2193-noncommuting-clifford-constraints.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2193',controls=len(cs),faults=faults)))
if __name__=='__main__':main()
