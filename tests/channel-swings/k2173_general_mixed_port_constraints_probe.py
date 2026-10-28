#!/usr/bin/env python3
"""Scalar-square noncommuting Euler reduction and homogeneous mixed-class controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as S
from k2171_mixed_port_euler_filter_probe import G,I,ETA,W,N,OM,mm,add,scale,blade,port,inv,bar,comm,neg,kernel,C,RR,K,filt
ROOT=Path(__file__).resolve().parents[2];WM=sum(1<<i for i in W)
def grade(x,d):return {m:c for m,c in x.items() if (m&~WM).bit_count()==d}
def scalar(x):return x.get(0,F(0))
def reduction(v,u,fault=None):
 t=mm(OM,u);a=scalar(mm(v,v));c=scalar(mm(t,t));x=scale(add(mm(v,t),mm(t,v)),F(1,2));y=scale(add(mm(v,t),neg(mm(t,v))),F(1,2))
 d=add(scale(I,49*a+225*c),scale(x,-210));f=343*a*a+1491*a*c-540*c*c
 e=add(scale(I,f),scale(x,42*c-1470*a),scale(mm(x,x),182),scale(y,49*a+297*c),scale(mm(x,y),-27 if fault=='xy_coefficient' else -28),mm(K(x),add(scale(x,126),scale(I,-F(49*a+315*c,2)))),scale(mm(K(x),y),21),mm(K(y),d))
 if fault=='Kx_product_order':e=add(e,scale(comm(x,K(x)),126))
 return a,c,x,y,d,e

def controls(fault=None):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v));v=blade(N[:7])
 # Genuine mixed commutation types; second fixture has nonzero square-zero y.
 fixtures=[('invertible_y',add(blade(N[:3]),scale(blade([N[3],N[4],N[7]]),F(1,3)))),('nilpotent_y',add(blade(N[:3]),blade([N[3],N[5],N[7]]),blade([N[4],N[5],N[7]])))]
 fixtures.append(('mixed_grades',add(blade(N[:3]),scale(blade([N[3],N[7],N[8]]),F(1,3)),scale(blade([N[4],N[5],N[9]]),F(1,5)))))
 for label,u in fixtures:
  a,c,x,y,d,e=reduction(v,u,fault);t=mm(OM,u)
  ck(label+'_scalar_squares',mm(v,v)==scale(I,a) and mm(t,t)==scale(I,c))
  ck(label+'_genuine_xy',bool(x) and bool(y))
  if label!='mixed_grades':ck(label+'_homogeneous_xy',x==grade(x,4) and y==grade(y,6))
  else:ck('mixed_grades_order_sensitive',bool(grade(x,4)) and bool(grade(x,8)) and bool(comm(K(x),x)))
  ck(label+'_central_x',not comm(x,v) and not comm(x,t) and not comm(x,y))
  ck(label+'_y_square',mm(y,y)==add(mm(x,x),scale(I,-a*c)))
  r,p,fl,aa,be,ww=filt(v,u)
  ck(label+'_pencil_square',mm(p,p)==d)
  predicted=scale(mm(e,inv(d)),-144 if fault!='quartic_factor' else -143)
  ck(label+'_quartic_equals_Euler',fl==predicted)
  z=add(v,t);ts={j:scale(mm(inv(p),port(r)[j]),-ETA[j]) for j in N}
  qs={j:RR(ts,*C(port(z),*kernel(ts,j)))[1] for j in N};q=add(*(mm(qs[j],G[j]) for j in N))
  if fault=='extra_eta':q=add(*(scale(mm(qs[j],G[j]),ETA[j]) for j in N))
  ck(label+'_original10_rows',scale(mm(bar(p),q),6)==predicted)
  ck(label+'_full_residual_nonzero',bool(e) and any(qs.values()))
  if label=='nilpotent_y':ck('singular_y_not_singular_pencil',not mm(y,y) and bool(y) and mm(d,inv(d))==I)
  tr=f=343*a*a+1491*a*c-540*c*c
  tr+=434*scalar(mm(grade(x,4),grade(x,4)))-574*scalar(mm(grade(x,8),grade(x,8)))
  ck(label+'_scalar_projection',scalar(e)==tr)
 a,c,X=S.symbols('a c X');f=343*a*a+1491*a*c-540*c*c
 expected={(2,-2):[S.Rational(27,49),-S.Rational(585,98)],(2,-10):[-S.Rational(585,98),S.Rational(2055,1309)],(-6,-2):[-S.Rational(495,49),S.Rational(69,343)],(-6,-10):[-S.Rational(495,49),S.Rational(1245,1351)]}
 for k in [2,-6]:
  for l in [-2,-10]:
   delta=182+126*k;alpha=42*c-1470*a-S.Rational(k,2)*(49*a+315*c);beta=49*a+297*c+l*(49*a+225*c);gamma=-28+21*k-210*l
   if fault=='odd_coefficient':gamma+=1
   g=delta*X*X+alpha*X+f;H=S.factor(g.subs(X,-beta/gamma)*gamma**2);R=S.factor((f+delta*a*c)**2-alpha*alpha*a*c)
   tag=str((k,l));ck('nonzero_gamma_'+tag,gamma in [434,2114,266,1946])
   ck('factor_roots_'+tag,all(S.simplify(H.subs({a:t,c:1}))==0 for t in expected[k,l]))
   ck('no_projective_common_root_'+tag,all(R.subs({a:t,c:1})!=0 for t in expected[k,l]) and H.subs({a:1,c:0})!=0)
   ck('resultant_of_g_and_square_'+tag,S.expand(S.resultant(g,X*X-a*c,X)-R)==0)
   ck('r_zero_degenerate_'+tag,S.factor(f.subs(a,-S.Rational(153 if l==-2 else 217,49)*c))==(-S.Rational(12960,7) if l==-2 else -416)*c*c)
 # Exact relation separates reversion-even and reversion-odd normal grades.
 ck('reversion_parities',all((-1)**(d*(d-1)//2)==s for d,s in [(4,1),(8,1),(6,-1),(10,-1)]))
 return out
FAULTS=['xy_coefficient','quartic_factor','extra_eta','odd_coefficient','Kx_product_order']
def polynomial_certificate():
 a,c,X=S.symbols('a c X');rows=[]
 for k in [2,-6]:
  for l in [-2,-10]:
   f=343*a*a+1491*a*c-540*c*c;delta=182+126*k;alpha=42*c-1470*a-S.Rational(k,2)*(49*a+315*c);beta=49*a+297*c+l*(49*a+225*c);gamma=-28+21*k-210*l;g=delta*X*X+alpha*X+f;H=S.factor(g.subs(X,-beta/gamma)*gamma**2);R=S.factor((f+delta*a*c)**2-alpha*alpha*a*c);roots=S.solve(H.subs(c,1),a)
   rows.append(dict(k=k,l=l,gamma=gamma,H=str(H),R=str(R),roots=[str(t) for t in roots],R_at_roots=[str(S.factor(R.subs({a:t,c:1}))) for t in roots],H_at_c0=str(H.subs(c,0))))
 return rows

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls();assert all(cs.values()),cs
 faults={}
 for f in FAULTS:
  bad=[n for n,p in controls(f).items() if not p];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2173-general-mixed-port-constraints-2026-10-27.md','tests/channel-swings/k2171_mixed_port_euler_filter_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','tests/channel-swings/k2165_even_clifford_adapter_descent_probe.py']
 report=dict(result_id='K2173',status='conditional_exact_controls',checks=cs,fault_failures=faults,polynomial_certificate=polynomial_certificate(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Independent written central-algebra, reversion and trace/spectral proof plus exact projective root exclusions; finite original-row controls do not exclude all mixed ports.')
 dest=ROOT/'lab/process/k2173-general-mixed-port-constraints.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2173',checks=len(cs),faults=faults)))
if __name__=='__main__':main()
