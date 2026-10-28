#!/usr/bin/env python3
"""Full-tail rational interval witnesses and symbolic minimizing identities."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as S
from k2178_effective_detector_approximation_probe import p,A,sqrt_iv,ivadd,scale,point
from k2184_global_detector_structure_probe import ap,C,moments
ROOT=Path(__file__).resolve().parents[2];PREC=10**70

def root(x):return sqrt_iv(x,PREC)
def mul(a,b):
 v=[x*y for x in a for y in b];return min(v),max(v)
def inv(a):assert a[0]>0;return 1/a[1],1/a[0]
def sub(a,b):return ivadd(a,scale(-1,b))
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def Ep(s):return F(5,6)*A(s)-C*F(2,3)*s+F(35,18)
def deriv_ratio(rr):return scale(F(1,2),ivadd(rr,scale(F(1,4),inv(rr))))
def block(N=40,L=4,fault=None):
 ep=F(1,4)**N;a=p(N+L);rho=F(2)**(N-L)
 w=ep-ep*ep+a*(L+F(1,3));R=F(5,6)*ep-ep*ep*(N+F(5,6))+a*((L+F(1,3))*N+F(L*L,2)+F(L,3)+F(5,18))
 d=a*((3*L+1)*N+F(3*L*(L-1),2))-3*N*ep*ep
 T=F(2,3)*ep-2*ep*ep*(N+F(1,3))+2*N*a/rho+a*((L-F(1,3))*N+F(L*L,2)+F(L,6)+F(2,9))
 D=F(2,3)+N*p(N-1)/4*(rho+1/rho-2)+F(1,8)*sum((n+1)*p(n) for n in range(N,N+L-1))
 if fault=='block_derivative':D+=F(1,100)
 es=[ep if n<N else F(4)**(n-N-L) for n in range(N+L)];x=[p(n)*e for n,e in enumerate(es)]
 return dict(w=w,R=R,d=d,T=T,D=D,x=x,es=es,tail=F(1,4),N=N,L=L)
def spike(N=40,fault=None):
 r=F(3,13);b=F(3,100*N-33);an=(1-r)*r**N;h=root(r);u=root(1+b/an)
 w=1+b;R=F(83,100)*w;d=-w/100
 T=ivadd(scale(1/(1-r),h),scale(an,mul(ivadd(scale(N,inv(h)),scale(N+1,h)),sub(u,point(1)))))
 D0=scale(F(2,3),ivadd(h,scale(F(1,4),inv(h))))
 c1=ivadd(mul(h,sub(u,point(1))),scale(F(1,4),mul(inv(h),sub(inv(u),point(1)))))
 c2=ivadd(mul(h,sub(inv(u),point(1))),scale(F(1,4),mul(inv(h),sub(u,point(1)))))
 D=ivadd(D0,ivadd(scale(N*p(N-1)/2,c1),scale((N+1)*p(N)/2,c2)))
 if fault=='spike_derivative_tail':D=sub(D,point(F(1,100)))
 lam=p(N)/(2*(an+b))
 return dict(N=N,r=r,b=b,an=an,h=h,u=u,w=w,R=R,d=d,T=T,D=D,D0=D0,lam=lam)
def controls(fault=None):
 cs={};ck=lambda n,v:cs.__setitem__(n,bool(v))
 s,t,R,d,w,DD=S.symbols('s t R d w D',positive=True);AS=S.Rational(41,6)*s*s+S.Rational(3,2)/s**2;BS=AS-s*S.diff(AS,s)
 ck('B_derivative',S.simplify(S.diff(BS,s)+s*S.diff(AS,s,2))==0)
 rhs=S.Rational(5,4)*R-S.Rational(3,8)*(S.Rational(6,5)*R-S.Rational(2,5)*d)-DD/4
 target=S.Rational(4,5)*R+(S.Rational(1,5) if fault=='dirichlet_contrast' else S.Rational(3,20))*d-DD/4
 ck('Dirichlet_orientation',S.expand(rhs-target)==0)
 eps=S.Rational(5,6)*AS-S.Rational(80,9)*s+S.Rational(35,18)
 ck('minimizer_lower_identity',S.simplify(S.Rational(5,6)*BS+S.Rational(35,18)-eps-S.Rational(5,6)*s*(S.Rational(32,3)-S.diff(AS,s)))==0)
 ck('squeeze_at_one',ap(F(1))==C*F(4,5) and Ep(F(1))==0)
 # Exact examples of the universal B monotonicity bound (not optimizer existence).
 for sx,sy,rx in [(F(9,10),F(19,20),F(1,3)),(F(1),F(4,5),F(1,2)),(F(7,10),F(7,10),F(1,5))]:
  H=rx*(A(sx)-sx*ap(sx))+(F(5,6)-rx)*(A(sy)-sy*ap(sy))+F(35,18)
  ck('positive_region_'+str((sx,sy)),H>Ep(max(sx,sy)))
 # Exact full-tail flat-block sums and independently computed derivative series.
 z=block(fault=fault);N=z['N'];L=z['L'];x=z['x'];tail=z['tail'];rr,tt=moments(x,tail)
 wdirect=sum(x)+tail*F(1,4)**len(x);mdirect=sum(n*v for n,v in enumerate(x))+tail*F(1,4)**len(x)*(len(x)+F(1,3))
 ck('block_full_mass',wdirect==z['w']);ck('block_full_R',rr==z['R']);ck('block_full_contrast',3*mdirect-wdirect==z['d']>0);ck('block_full_T',tt[0]<=z['T']<=tt[1]);ck('block_strict_caps',all(0<e<1 for e in z['es']) and 0<tail<1)
 Ddirect=point(F(2,3))
 for n in range(len(x)):
  nxt=x[n+1] if n+1<len(x) else tail*p(n+1);ratio=root(nxt/x[n]);delta=sub(deriv_ratio(ratio),point(F(1,2)))
  Ddirect=ivadd(Ddirect,scale((n+1)*p(n),delta))
 ck('block_full_derivative',Ddirect[0]<=z['D']<=Ddirect[1])
 lo,hi=F(1011,1000),F(253,250);ck('block_squeeze_bracket',z['R']*ap(lo)<C*z['T']<z['R']*ap(hi));ql=Ep(lo)-C*hi*(z['D']-F(2,3));ck('block_positive_Q',ql>F(1,1000))
 # Negative-contrast single-spike witness: whole baseline plus only two changed edges.
 z2=spike(fault=fault);r=z2['r'];b=z2['b'];an=z2['an'];lam=z2['lam'];h=z2['h'];N=z2['N']
 ck('spike_moments',r/(1-r)+N*b+z2['w']/2==z2['R']);ck('spike_negative_contrast',3*(r/(1-r)+N*b)-z2['w']==z2['d']<0)
 ck('spike_cap_at_N',lam*(an+b)/p(N)==F(1,2));ck('spike_other_caps',0<lam<F(39,40) and F(1-r,F(3,4))==F(40,39) and r/F(1,4)==F(12,13)<1)
 Tdirect=scale(1/(1-r),h);Ddirect=z2['D0']
 for n in [N-1,N]:
  a=(1-r)*r**n;aa=(1-r)*r**(n+1);zz=a+(b if n==N else 0);zn=aa+(b if n+1==N else 0)
  Tdirect=ivadd(Tdirect,scale(n+1,sub(root(zz*zn),root(a*aa))))
  Ddirect=ivadd(Ddirect,scale((n+1)*p(n),sub(deriv_ratio(root(zn/zz)),deriv_ratio(h))))
 ck('spike_full_coherence_transfer',overlap(Tdirect,z2['T']));ck('spike_full_derivative_transfer',overlap(Ddirect,z2['D']))
 lo,hi=F(9723,10000),F(6079,6250);ck('spike_squeeze_bracket',z2['R']*ap(lo)<C*z2['T'][0] and z2['R']*ap(hi)>C*z2['T'][1]);ck('spike_D_nonnegative_defect',z2['D'][0]>F(2,3))
 ql2=Ep(hi)-C*hi*(z2['D'][1]-F(2,3));ck('spike_positive_Q',ql2>F(1,5000))
 # Complement has positive contrast and a certified energy upper bound.
 m=F(33,100)*z2['w'];upper=C*lam*(F(5,2)*m+z2['w']/2)
 if fault=='energy_bound':upper*=F(10)**30
 ck('positive_complement_contrast',-lam*z2['d']>0);ck('small_energy_upper',upper<F(1,10000));ck('beta0_positive_derivative',ql2-upper>F(1,10000))
 for e in [F(0),F(1,10),F(1,2),F(9,10),F(1)]:
  for f in [F(0),F(1,4),F(3,4),F(1)]:
   target=1-e-f
   ck('edge_complement_'+str((e,f)),target<=0 or (1-e)*(1-f)>=target**2)
 ck('edge_polynomial_identity',S.expand((1-s)*(1-t)-(1-s-t)**2-(s+t-(s+t)**2+s*t))==0)
 ck('geometric_derivative_summability',F(1,16)<r<F(1,4))
 # Changed p-tail changes neutral contrast; actual data fault, not a manifest flag.
 q=F(1,5) if fault=='thermal_tail' else F(1,4)
 ck('thermal_neutrality',3*q/(1-q)-1==0)
 return cs,dict(flat_block=dict(N=40,L=4,squeeze_bracket=['1011/1000','253/250'],Q_lower=str(ql)),negative_spike=dict(N=40,r=str(r),b=str(b),scale=str(lam),squeeze_bracket=['9723/10000','6079/6250'],Q_lower=str(ql2),energy_upper=str(upper),beta0_derivative_lower=str(ql2-upper)))
FAULTS=['dirichlet_contrast','block_derivative','spike_derivative_tail','energy_bound','thermal_tail']
def main():
 ap_=argparse.ArgumentParser();ap_.add_argument('--write',action='store_true');args=ap_.parse_args();cs,details=controls();assert all(cs.values()),[n for n,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[n for n,v in controls(f)[0].items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2190-detector-global-minimizing-structure-2026-10-28.md','explorations/conditional-build/k2188-detector-variational-structure-2026-10-28.md','explorations/conditional-build/k2186-detector-contrast-descent-2026-10-28.md','tests/channel-swings/k2178_effective_detector_approximation_probe.py','tests/channel-swings/k2184_global_detector_structure_probe.py']
 report=dict(result_id='K2190',status='conditional_exact_controls',checks=cs,fault_failures=faults,details=details,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written minimizing sign theorem, explicit full-tail branch counterconstructions and positive-contrast beta0 noise obstruction. Symbolic identities, rational intervals and finite controls are separate evidence. No global minimizing/frontier or apparatus/GU claim.')
 dest=ROOT/'lab/process/k2190-detector-global-minimizing-structure.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2190',checks=len(cs),faults=len(faults),block_Q_lower=float(F(details['flat_block']['Q_lower'])),spike_Q_lower=float(F(details['negative_spike']['Q_lower'])),beta0_derivative_lower=float(F(details['negative_spike']['beta0_derivative_lower'])))))
if __name__=='__main__':main()
