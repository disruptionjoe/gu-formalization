#!/usr/bin/env python3
"""Exact trace-polynomial certificate and original ten-row mixed-grade consumer."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as S
from k2173_general_mixed_port_constraints_probe import reduction,grade,scalar
from k2171_mixed_port_euler_filter_probe import G,I,ETA,W,N,OM,mm,add,scale,blade,port,inv,bar,comm,neg,kernel,C,RR,K,filt
ROOT=Path(__file__).resolve().parents[2]

def polynomial(fault=None):
 a,c,X=S.symbols('a c X');out=[]
 for k in [2,-6]:
  de=182+126*k;al=42*c-1470*a-S.Rational(k,2)*(49*a+315*c);f=343*a*a+1491*a*c-540*c*c
  be=-49*a-153*c;ga=392+21*k;d=49*a+225*c
  h=8*(d*be*de-d*ga*al+(-210 if fault!='trace_sign' else 210)*ga*f)-(be*be*de-be*ga*al+ga*ga*f)
  discr=al*al-4*de*f;roots=S.solve(h.subs(c,1),a)
  out.append(dict(k=k,H=str(S.factor(h)),roots=[str(q) for q in roots],multiplicity_n=[str(S.factor((-256*de*f/discr).subs({a:q,c:1}))) for q in roots]))
 return out

def controls(fault=None):
 out={};ck=lambda name,v:out.__setitem__(name,bool(v));a,c,X=S.symbols('a c X')
 expected={2:-340256*(a-3*c)*(98*a+585*c),-6:-784*(49*a+495*c)*(259*a+159*c)}
 for row in polynomial(fault):
  k=row['k'];H=S.sympify(row['H']);de=182+126*k;al=42*c-1470*a-S.Rational(k,2)*(49*a+315*c);f=343*a*a+1491*a*c-540*c*c;be=-49*a-153*c;ga=392+21*k;d=49*a+225*c;g=de*X*X+al*X+f
  ck('trace_polynomial_'+str(k),S.expand(H-expected[k])==0)
  norm=be*be-be*ga*al/de+ga*ga*f/de;inverse=be-ga*al/de-ga*X
  ck('inverse_mod_quadratic_'+str(k),S.rem(S.expand((be+ga*X)*inverse-norm),g,X)==0)
  reduced=S.rem(S.expand((d-210*X)*inverse),g,X)
  ck('trace_numerator_sign_'+str(k),S.simplify(reduced.subs(X,0)-(d*be-d*ga*al/de-210*ga*f/de))==0)
  ck('c_zero_forces_a_zero_'+str(k),H.subs(c,0)!=0 and S.degree(H.subs(c,0),a)==2)
  for j,qstr in enumerate(row['roots']):
   q=S.sympify(qstr);disc=(al*al-4*de*f).subs({a:q,c:1});ff=f.subs({a:q,c:1});nn=-256*de*ff/disc
   ck('nonzero_distinct_roots_'+str((k,j)),disc!=0 and ff!=0)
   ck('multiplicity_impossible_'+str((k,j)),nn<15 or nn>64)
 # Original fixed-splitting equations, not just assertions about the new filter.
 v=blade(N[:7]);u=mm(mm(add(G[N[0]],scale(G[N[7]],2)),add(G[N[1]],scale(G[N[8]],3))),G[N[9]])
 aa,cc,x,y,d,e=reduction(v,u);t=mm(OM,u);volume=blade(N);volfull=mm(OM,volume)
 ck('fixture_scalar_squares',mm(v,v)==I and mm(t,t)==scale(I,-24))
 ck('fixture_new_class',bool(x) and x==grade(x,8) and bool(grade(y,6)) and bool(grade(y,10)))
 ck('normal_volume_square',mm(volume,volume)==neg(I))
 ck('normal_volume_even_central',not comm(volume,x) and not comm(volume,y))
 ck('two_chiral_trace_zero',scalar(x)==0 and scalar(mm(volume,x))==0)
 ck('fixture_pencil_invertible',mm(d,inv(d))==I)
 x2=mm(x,x);ck('fixture_x_minimal_polynomial',not add(mm(x2,x2),scale(x2,-26),scale(I,25)))
 # Homogeneous-x quartic split including BOTH y grades, no commuting-order shortcut.
 k=-6;de=182+126*k;al=42*cc-1470*aa-F(k,2)*(49*aa+315*cc);f=343*aa*aa+1491*aa*cc-540*cc*cc
 even=add(scale(x2,de),scale(x,al),scale(I,f));h=add(scale(I,-49*aa-153*cc),scale(x,392+21*k));y10=grade(y,10)
 used_y=grade(y,6) if fault=='omit_complement_grade' else y
 odd=add(mm(h,used_y),scale(mm(y10,d),-8 if fault!='volume_coefficient' else -7))
 ck('quartic_split_original',add(even,odd)==e)
 ck('grade_operator_mixture',K(y)==add(scale(y,-2),scale(y10,-8)))
 r,p,fl,_,_,_=filt(v,u);ts={j:scale(mm(inv(p),port(r)[j]),-ETA[j]) for j in N};z=add(v,t)
 qs={j:RR(ts,*C(port(z),*kernel(ts,j)))[1] for j in N};q=add(*(mm(qs[j],G[j]) for j in N))
 pred=scale(mm(e,inv(d)),-144 if fault!='euler_factor' else -143)
 ck('full10_to_quartic',scale(mm(bar(p),q),6)==pred and fl==pred)
 ck('actual_residual_nonzero',bool(fl) and any(qs.values()))
 # Released mixed-grade localization, tested on an order-sensitive original fixture.
 u2=add(blade(N[:3]),scale(blade([N[3],N[7],N[8]]),F(1,3)),scale(blade([N[4],N[5],N[9]]),F(1,5)))
 aa,cc,x,y,d,e=reduction(v,u2);U=K(x);J=grade(y,10);rr=(aa+9*cc)/6;bb=(7*aa+45*cc)/6
 L=add(scale(x,126),scale(I,-F(49*aa+315*cc,2)),scale(y,21));Ls=add(scale(x,126),scale(I,-F(49*aa+315*cc,2)),scale(y,-21))
 f=343*aa*aa+1491*aa*cc-540*cc*cc
 FF=add(scale(I,f),scale(x,42*cc-1470*aa),scale(mm(x,x),182),scale(y,-49*aa-153*cc),scale(mm(x,y),392),scale(mm(J,d),-8))
 ck('localization_quartic_order',add(FF,mm(U,L))==e)
 ck('localization_F_commutes',not comm(FF,x) and not comm(FF,y))
 shifted=add(x,scale(I,-rr))
 ck('localization_pencil_factor',mm(L,Ls)==scale(mm(d,shifted),-F(147,2) if fault!='localization_factor' else -F(145,2)))
 ck('localization_commutator_identity',comm(e,x)==mm(comm(U,x),L) and comm(e,y)==mm(comm(U,y),L))
 ck('mixed_fixture_outside_exception',mm(shifted,inv(shifted))==I and bool(comm(U,x)))
 ck('mixed_fixture_rejected_by_localization',bool(mm(comm(U,x),shifted)))
 aa,cc,j=S.symbols('a c J');r=(aa+9*cc)/6;t=(aa-9*cc)/6;d0=49*aa+225*cc-210*r
 ff=343*aa**2+1491*aa*cc-540*cc**2+(42*cc-1470*aa)*r+182*r*r+(-49*aa-153*cc)*t+392*r*t-8*j*d0
 ck('singular_face_factor',S.factor(ff-S.Rational(8,9)*(7*aa-45*cc)*(17*aa+18*cc-18*j))==0)
 ck('singular_face_pencil',S.simplify(d0-2*(7*aa-45*cc))==0)
 return out
FAULTS=['trace_sign','volume_coefficient','euler_factor','omit_complement_grade','localization_factor']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for fault in FAULTS:
  bad=[k for k,v in controls(fault).items() if not v];assert bad,('undetected',fault);faults[fault]=bad
 deps=['explorations/conditional-build/k2175-mixed-grade-euler-localization-2026-10-27.md','tests/channel-swings/k2173_general_mixed_port_constraints_probe.py','tests/channel-swings/k2171_mixed_port_euler_filter_probe.py','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py']
 report=dict(result_id='K2175',status='conditional_exact_controls',checks=cs,fault_failures=faults,polynomial_certificate=polynomial(),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written finite-dimensional trace and quadratic-spectrum argument; exact coefficient and original-row controls supplement but do not replace independent proof review. General mixed-grade x and nonscalar squares remain open.')
 dst=ROOT/'lab/process/k2175-mixed-grade-euler-localization.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2175',checks=len(cs),faults=faults)))
if __name__=='__main__':main()
