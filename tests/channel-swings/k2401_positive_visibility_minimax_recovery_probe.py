#!/usr/bin/env python3
"""Symbolic CP/support identities and exact rational global-bound fixture."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,importlib.util,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2];dep=ROOT/'tests/channel-swings/k2398_uncertain_clock_law_recovery_probe.py'
sp=importlib.util.spec_from_file_location('old',dep);old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
def sqbounds(x,bits=100):
 assert x>=0
 scale=1<<bits;q=isqrt((x.numerator*scale*scale)//x.denominator)
 return F(q,scale),F(q+1,scale)
def mul(a,b):return a[0]*b[0],a[1]*b[1]
def div(a,b):assert b[0]>0;return a[0]/b[1],a[1]/b[0]
def exact_bounds(ell,v):
 A=ell*ell-v*v;B=ell*ell+8*v*v;D=sqbounds(A*B)
 h=div((ell*B/4,)*2,D);c=div(((ell*ell-4*v*v)*(ell*ell+2*v*v),)*2,(A*D[0],A*D[1]))
 y=3*v*v/A;z=div((3*v*ell,)*2,D);x=(y*z[0],y*z[1]);a,b=F(1,4),F(3,4);t=(1-ell)/3
 flo=a*c[0]+v*(a*x[0]+b*z[0]);radhi=2-flo;skewhi=b*c[1]
 upper=(1+sqbounds(radhi*radhi+skewhi*skewhi)[1])/4
 lower=(1+(2-h[1])/sqbounds(1+t*t)[1])/4
 return lower,upper

def run():
 checks={};controls={}
 def ck(name,ok):
  checks[name]=bool(ok)
  if not ok:raise AssertionError('[FAIL] '+name)
 def ctrl(name,ok):
  controls[name]=bool(ok)
  if not ok:raise AssertionError('[FAIL] '+name)
 l,v=s.symbols('ell v',positive=True);A=l*l-v*v;B=l*l+8*v*v;D=s.sqrt(A*B)
 h=l*B/(4*D);c=(l*l-4*v*v)*(l*l+2*v*v)/(A*D);y=3*v*v/A;z=3*v*l/D;x=y*z
 # Radical products are positive on the declared ell>2v>0 domain.
 simp=lambda expr:s.factor(s.radsimp(s.simplify(expr)))
 ck('CP_boundary_identity',simp(c*c-(1-y*y)*(1-z*z))==0)
 ck('CP_plus_determinant',simp((1+x)**2-c*c-(y+z)**2)==0)
 ck('CP_minus_determinant',simp((1-x)**2-c*c-(y-z)**2)==0)
 ck('support_function_attained',simp(l*c/4+v*x/4+3*v*z/4-h)==0)
 ck('support_derivative',simp(4*s.diff(h,l)-c)==0)
 t=(1-l)/3;f=c/4+v*x/4+3*v*z/4
 ck('support_alignment_trace_relation',simp(f-h-(1-l)*c/4)==0)
 cc0,hh0=s.symbols('cc0 hh0',real=True)
 ck('support_alignment_stationarity',s.expand(12*(3*cc0/4-t*(2-hh0-(1-l)*cc0/4))-(cc0*(9+(1-l)**2)-4*(1-l)*(2-hh0)))==0)
 pp=-32*l**5+302*l**4+22*l**3-40*l*l+l-10
 poly=s.expand(pp**2-8*(1-l)**2*(16*l*l-1)**3*(2*l*l+1))
 P=(9+(1-l)**2)*(l*l-4*v*v)*(l*l+2*v*v)+(1-l)*l*B*A
 raw=s.expand((P*P-64*(1-l)**2*A**3*B).subs(v,s.Rational(1,4)))
 ck('squared_polynomial_identity',s.Poly(raw,l).monic()==s.Poly(poly,l).monic())
 coeff=list(map(int,s.Poly(poly,l).all_coeffs()))
 def pe(q):
  out=F(0)
  for cc in coeff:out=out*q+cc
  return out
 lo,hi=F(1,2),F(3,4)
 ck('root_bracket_signs',pe(lo)<0<pe(hi))
 # Exact Sturm count independently checks the analytic uniqueness in this fixture.
 ck('exact_Sturm_unique_root',s.Poly(poly,l).count_roots(s.Rational(1,2),s.Rational(3,4))==1)
 for _ in range(60):
  mid=(lo+hi)/2
  if pe(mid)<0:lo=mid
  else:hi=mid
 ell=(lo+hi)/2;lower,upper=exact_bounds(ell,F(1,4))
 ck('rigorous_optimum_gap_below_1e12',0<=upper-lower<F(1,10**12))
 ck('strict_gain_over_identity',upper<F(11,16))
 ck('unsquared_positive_numerator',P.subs({l:s.Rational(3,4),v:s.Rational(1,4)})>0)
 wrong_support=(l*(-c)/4+v*x/4+3*v*z/4-h).subs({l:s.Rational(3,4),v:s.Rational(1,4)})
 ctrl('wrong_radical_translation_sign_rejected',s.simplify(wrong_support)<0)
 # Rational feasible channel, independent of root isolation or search.
 Q=s.Rational;I,X,Y,Z=old.I,old.X,old.Y,old.Z;pa=[X,Y,Z];cc=xx=Q(12,25);yy=Q(3,5);zz=Q(4,5)
 def rec(op):
  tr=s.trace(op);r=[s.trace(op*P0) for P0 in pa]
  return s.simplify((tr*I+(cc*tr+xx*r[0])*X+yy*r[1]*Y+zz*r[2]*Z)/2)
 J=old.choi_apply(rec);ck('actual_decoder_Choi_CP_TP_rank2',old.psd(J) and old.ptr(J)==I and J.rank()==2)
 a,b=Q(1,4),Q(3,4);M=s.diag(a,b);nu=Q(1,4);expected=(1+s.sqrt(7549)/50)/4
 def blocks(op,sg,m,Qmat=nu*M):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);tr=s.trace(op);vec0=nu*m*tr+sg*Qmat*rr
  return ((tr+sg*m.dot(rr))*I+vec0[0]*X+vec0[1]*Z)/4
 for sign in (-1,1):
  m=s.Matrix([a,sign*b]);BB=s.Matrix([cc,0])*m.T+nu*s.diag(xx,zz)*M
  def recovered(op):return s.simplify(rec(blocks(op,1,m))+Y*rec(blocks(op,-1,m))*Y)
  for j,op in enumerate([I/2,X,Y,Z]):
   rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);out=BB*rr
   ck('original_sign_composition_'+str(sign)+'_'+str(j),old.zero(recovered(op)-(s.trace(op)*I+out[0]*X+out[1]*Z)/2))
  jt=old.choi_apply(recovered);ck('recovered_CP_TP_'+str(sign),old.psd(jt) and old.ptr(jt)==I)
  ck('independent_Bell_trace_norm_'+str(sign),old.zero(old.trace_norm_hermitian(old.choi_apply(lambda op:op)-jt)/4-expected))
 ck('rational_channel_strict_margin',Q(49,16)-Q(7549,2500)==Q(429,10000))
 ctrl('dropped_skew_term_incorrect',not old.zero(expected-(3-Q(3,10))/4))
 ctrl('wrong_output_sign_order_incorrect',not old.zero(rec(blocks(I/2,1,m))+rec(Y*blocks(I/2,-1,m)*Y)-I/2))
 # Physical axis-dependent visibility fixture belongs to enlargement, not common-v.
 ps=[Q(1,4),Q(3,4)];rs=[Q(1,16),Q(3,8)];axes=[s.Matrix([1,0]),s.Matrix([0,1])]
 ck('physical_uncertain_visibility_linear_constraints',all(Q(1,4)*p<=r<=Q(1,2)*p for p,r in zip(ps,rs)))
 ctrl('enlargement_not_common_visibility',rs[0]/ps[0]!=rs[1]/ps[1])
 mm=sum((p*n for p,n in zip(ps,axes)),s.zeros(2,1));qm=sum((r*n*n.T for r,n in zip(rs,axes)),s.zeros(2))
 vv=sum((r*n for r,n in zip(rs,axes)),s.zeros(2,1))
 def varied(op,sg):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);tr=s.trace(op);vec0=vv*tr+sg*qm*rr
  return ((tr+sg*mm.dot(rr))*I+vec0[0]*X+vec0[1]*Z)/4
 ck('axis_visibility_instrument_CP',all(old.psd(old.choi_apply(lambda op:varied(op,sg))) for sg in (-1,1)))
 ck('axis_visibility_total_TP',old.ptr(old.choi_apply(lambda op:varied(op,1)+varied(op,-1)))==I)
 Bvar=s.Matrix([cc,0])*mm.T+s.diag(xx,zz)*qm
 for j,op in enumerate([I/2,X,Y,Z]):
  rr=s.Matrix([s.trace(op*X),s.trace(op*Z)]);bb=Bvar*rr;out=rec(varied(op,1))+Y*rec(varied(op,-1))*Y
  ck('axis_visibility_composition_'+str(j),old.zero(out-(s.trace(op)*I+bb[0]*X+bb[1]*Z)/2))
 ctrl('nonphysical_pointer_weight_rejected',not old.psd(old.choi_apply(lambda op:((s.trace(op)+s.trace(op*X))*I+2*(s.trace(op)+s.trace(op*X))*X)/4)))
 return {'result':'K2401','status':'PASS','checks':checks,'controls':controls,'fixture':{'nu':'1/4','ell_interval':[str(lo),str(hi)],'value_interval':[str(lower),str(upper)],'interval_width':str(upper-lower),'decimal_display_only':[float(lower),float(upper)],'polynomial_coefficients':coeff},'dependencies':{str(dep.relative_to(ROOT)):hashlib.sha256(dep.read_bytes()).hexdigest()},'scope':'Exact symbolic support/CP identities, Sturm root isolation, rational norm brackets and actual sign-instrument controls; universal all-CPTP theorem uses the written proof.'}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();report=run()
 if args.write:(ROOT/'lab/process/k2401-positive-visibility-minimax-recovery.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,sort_keys=True))
