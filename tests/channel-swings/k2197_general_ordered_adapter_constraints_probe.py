#!/usr/bin/env python3
"""Exact ordered Clifford polynomials and independent original-ten-row fixtures."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import argparse,hashlib,json
import sympy as S
import k2169_invertible_pencil_full_descent_probe as o
from k2171_mixed_port_euler_filter_probe import filt
ROOT=Path(__file__).resolve().parents[2]
a,b,c,d=S.symbols('a b c d',real=True)
@lru_cache(None)
def basis(x,y):return next(iter(o.mm({x:F(1)},{y:F(1)}).items()))
def add(*xs):
 z={}
 for x in xs:
  for m,v in x.items():z[m]=z.get(m,0)+v
 return {m:S.expand(v) for m,v in z.items() if S.expand(v)!=0}
def sc(x,s):return add({m:v*s for m,v in x.items()})
def mm(x,y):
 z={}
 for i,v in x.items():
  for j,w in y.items():
   m,sg=basis(i,j);z[m]=z.get(m,0)+sg*v*w
 return add(z)
def bar(x):return {m:(-v if m&o.WM else v) for m,v in x.items()}
def K(x):return add(*(sc(mm(mm(o.G[j],x),o.G[j]),o.ETA[j]) for j in o.N))
def coeff(x,blade):
 m,sg=next(iter(blade.items()));return S.expand(x.get(m,0)/sg)
def symbolic(fault=None):
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v))
 A=o.blade(o.N[:3]);B=o.blade([o.N[i] for i in [0,3,4]]);CC=o.blade([o.N[i] for i in [0,1,5]]);inn=o.blade(o.N)
 w=add(sc(A,a),sc(B,b));u=add(sc(A,c),sc(CC,d));v=mm(inn,w);t=mm(o.OM,u)
 p=add(sc(v,7),sc(t,-15));r=add(v,sc(t,3));br=bar(r);s=add(sc(v,7),sc(t,9))
 kk=-49*a*a+49*b*b+225*c*c-225*d*d
 Y=add(mm(p,p),sc(o.I,-kk));delta=(49*a*a+49*b*b+225*c*c-225*d*d)**2-(210*a*c)**2
 num=mm(p,add(sc(o.I,kk),sc(Y,-1)))
 ck('inverse_numerator_both_sides',mm(p,num)==mm(num,p)==sc(o.I,delta))
 ck('Y_square',mm(Y,Y)==sc(o.I,-196*a*a*(49*b*b-225*d*d)))
 ck('Y_traceless',Y.get(0,0)==0)
 ck('displayed_Y_identity',Y==add(sc(mm(A,B),98*a*b),sc(mm(mm(mm(o.OM,inn),A),CC),-210*a*d)))
 aa=add(sc(K(mm(br,br)),3),sc(mm(br,br),34),sc(mm(r,br),36),sc(mm(br,r),8),sc(mm(r,r),-24))
 bb=add(sc(mm(r,r),184),sc(mm(r,br),140),sc(mm(br,r),184),sc(mm(br,br),194),sc(K(mm(br,r)),24),sc(K(mm(br,br)),15))
 ff=add(mm(mm(aa,num),s),sc(bb,-delta))
 f1=coeff(ff,o.blade([o.N[i] for i in [2,5]]));f2=coeff(ff,o.blade([o.N[i] for i in [1,3,4,5]]))
 ck('general_coefficient_n36',S.expand(f1-8064*a*a*c*d*(49*a*a+(258 if fault=='coefficient' else 259)*b*b-495*c*c+495*d*d))==0)
 ck('general_coefficient_n2456',S.expand(f2+8064*a*b*c*d*(259*a*a+49*b*b+495*c*c-495*d*d))==0)
 L=49*a*a+49*b*b-225*d*d
 f3=coeff(ff,mm(o.OM,o.blade([o.N[i-1] for i in [1,2,4,5,7,8,9,10]]))).subs(c,0)
 f4=coeff(ff,mm(o.OM,o.blade([o.N[i-1] for i in [1,3,7,8,9,10]]))).subs(c,0)
 ck('c0_tangent8',S.expand(f3-(1007 if fault=='face_coefficient' else 1008)*a*d*L*(21*a*a+29*b*b-69*d*d))==0)
 ck('c0_tangent6',S.expand(f4-144*b*d*L*(7*a*a-49*b*b+153*d*d))==0)
 ck('real_open_contradiction',S.expand((49*a*a+259*b*b-495*c*c+495*d*d)+(259*a*a+49*b*b+495*c*c-495*d*d))==308*(a*a+b*b))
 ck('real_face_contradiction',S.expand(153*(21*a*a+29*b*b-69*d*d)+69*(7*a*a-49*b*b+153*d*d))==3696*a*a+1056*b*b)
 ck('u_square_scalar',mm(u,u)==sc(o.I,-c*c+d*d))
 ck('scalar_faces',all(all(S.expand(z.subs(var,0))==0 for m,z in mm(w,w).items() if m) for var in [a,b]))
 ck('d0_commuting_wu',all(S.expand(z.subs(d,0))==0 for z in add(mm(w,u),sc(mm(u,w),-1)).values()))
 return cs

def fixtures(fault=None):
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v));A=o.blade(o.N[:3]);B=o.blade([o.N[i] for i in [0,3,4]]);C0=o.blade([o.N[i] for i in [0,1,5]])
 for ix,(a,b,c,d) in enumerate([(1,1,1,1),(1,1,0,1),(2,3,4,5)]):
  w=o.add(o.scale(A,a),o.scale(B,b));u=o.add(o.scale(A,c),o.scale(C0,d));v=o.mm(o.blade(o.N),w);t=o.mm(o.OM,u)
  r,p,f,aa,bb,ww=filt(v,u);pi=o.inv(p);Y=o.mm(pi,o.bar(p))
  ck(f'norm_one_{ix}',o.bar(Y)==o.inv(Y))
  ck(f'pencil_identity_{ix}',ww==o.scale(o.add(o.I,o.scale(Y,5 if fault=='norm_factor' else 4)),F(1,5)))
  # This identity holds off-shell, so no candidate is assumed to solve the filter.
  residual=o.add(o.scale(o.mm(aa,Y),4),o.neg(o.add(o.scale(bb,5),o.neg(aa))))
  ck(f'paired_conjugation_offshell_{ix}',o.mm(o.bar(residual),Y)==o.add(o.scale(o.bar(aa),4),o.neg(o.mm(o.add(o.scale(o.bar(bb),5),o.neg(o.bar(aa))),Y))))
  ck(f'both_commutators_nonzero_{ix}',bool(o.comm(v,t)) and bool(o.add(o.mm(v,t),o.mm(t,v))))
  ts={j:o.scale(o.mm(pi,o.port(r)[j]),-o.ETA[j]) for j in o.N};z=o.add(v,t)
  qs={j:o.RR(ts,*o.C(o.port(z),*o.kernel(ts,j)))[1] for j in o.N}
  q=o.add(*(o.scale(o.mm(qs[j],o.G[j]),o.ETA[j] if fault=='extra_eta' else 1) for j in o.N))
  ck(f'original_ten_row_contraction_{ix}',o.scale(o.mm(o.bar(p),q),6)==f)
  ck(f'all_ten_rows_reject_{ix}',all(bool(qs[j]) for j in o.N))
  if ix==0:ck('noncommuting_nilpotent_square_control',o.mm(t,t)=={} and bool(o.mm(v,v)))
 ts={j:{} for j in o.N}
 ck('zero_port_positive_control',all(o.RR(ts,*o.C([{} for _ in range(14)],*o.kernel(ts,j)))==({mu:{} for mu in o.W},{}) for j in o.N))
 return cs
FAULTS=['coefficient','face_coefficient','norm_factor','extra_eta']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=symbolic()|fixtures();assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in (symbolic(f) if f in FAULTS[:2] else fixtures(f)).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2197-general-ordered-adapter-constraints-2026-10-28.md','tests/channel-swings/k2171_mixed_port_euler_filter_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','explorations/conditional-build/k2177-exceptional-spectrum-descent-2026-10-28.md','explorations/conditional-build/k2195-anticommuting-spectral-reduction-2026-10-28.md']
 report=dict(result_id='K2197',status='conditional_exact_family_exclusion',checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal written real support-family proof; exact symbolic coefficients and independent original-ten-row rational fixtures. No general noncommuting or complex exclusion.')
 dst=ROOT/'lab/process/k2197-general-ordered-adapter-constraints.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2197',controls=len(checks),faults=faults)))
if __name__=='__main__':main()
