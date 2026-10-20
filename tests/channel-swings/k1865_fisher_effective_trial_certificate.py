#!/usr/bin/env python3
"""Symbolic Gaussian moments and exact whole-interval coefficient certificates."""
import sympy as S
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[2];m=json.loads((R/'lab/process/k1865-fisher-effective-trial-certificate.json').read_text());x,s=S.symbols('x s');count=0
C={k:S.Rational(v) for k,v in m['constants'].items()}
def ck(test,label):
 global count
 assert test,label
 count+=1
def expectation(f):
 return sum(c*(S.factorial2(i-1) if i else 1) for (i,),c in S.Poly(S.expand(f),x).terms() if i%2==0)
u=sum(S.Rational(c)*S.hermite_prob(int(n),x) for n,c in m['trial']['u'].items());v=sum(S.Rational(c)*S.hermite_prob(int(n),x) for n,c in m['trial']['v'].items());h=1+s*u+s*s*v
polys={k:sum(S.Rational(c)*s**i for i,c in enumerate(row)) for k,row in m['polynomials'].items()}
for k,integrand in [('N',h*h),('B',x*x*h*h),('C',x**4*h*h),('D',S.diff(h,x)**2)]:ck(S.expand(expectation(integrand)-polys[k])==0,'moment '+k)
N,B,K,D=[polys[k] for k in ['N','B','C','D']];q=3-K*N/B**2;J=B/N*(2-B/N+4*D/N)-1;L=q*q/(2*(3-q));M=C['s_max']
def positive_polynomial(f):
 p=S.Poly(S.expand(f),s);cs=list(reversed(p.all_coeffs()));lo=cs[0]-sum(abs(c)*M**i for i,c in enumerate(cs[1:],1));return lo
for name,f in [('q/s',q/s),('2-q/s',2-q/s),('(q-s)/s3',(q-s)/s**3),('qprime',S.diff(q,s)),('energy_positive',(J-L)/s**3),('energy_upper',C['energy_cubic_upper']-(J-L)/s**3)]:
 num,den=S.fraction(S.cancel(f));ck(positive_polynomial(num)>0,name+' numerator whole interval');ck(positive_polynomial(den)>0,name+' denominator whole interval')
ck(C['gap_floor']>0,'gap positive');ck(C['energy_cubic_upper']/C['gap_floor']==C['tv_squared_cubic_upper'],'gap conversion')
for k in ['N','B','C']:ck(positive_polynomial(polys[k])>0,k+' positive')
z=C['example_s'];qe=S.cancel(q.subs(s,z));de=S.cancel((J-L).subs(s,z));ck(de>0,'coarse gap positive')
ck(q.subs(s,M)>M,'range covers q=1/200');ck(q.subs(s,M)<S.Rational(1,100),'gap window')
for p,d in m['dependencies'].items():ck(hashlib.sha256((R/p).read_bytes()).hexdigest()==d,'dependency')
print('PASS K1865:',count,'exact groups; all interval signs use coefficient bounds, no sampling')
print('example q approximation',S.N(qe,20),'TV upper approximation',S.N(S.sqrt(de/C['gap_floor']),16))

# Strong auxiliary dual: same feasible trial, a supplied confining oscillator.
a=1-2*s-S.Rational(11,3)*s*s; b=s/3+3*s*s/4; E=2-s-S.Rational(19,12)*s*s
p1=x**4/3-2*x*x+1; p2=3*x**4/4-S.Rational(11,3)*x*x+S.Rational(19,12)
rr=s**3*(p1*v+p2*u)+s**4*p2*v
ck(S.expand(-4*S.diff(h,x,2)+4*x*S.diff(h,x)+(a*x*x+b*x**4+2-x*x-E)*h-rr)==0,'actual residual identity')
R2=S.expand(expectation(rr*rr)); hr=S.expand(expectation(h*rr))
ck(S.expand(R2-polys['R2'])==0,'residual squared norm')
ck(S.expand(hr-polys['hr'])==0,'residual overlap')
mu=E+hr/N; err=B*R2/(C['temple_denominator_floor']*N*N)
certificates=[('a harmonic floor',a-S.Rational(25,36)),('Rayleigh below3',3-mu),('residual sixth',C['residual_sixth_upper']-R2/s**6),('scale prefactor',S.Rational(64,125)-B/(2*N*N)),('q shift upper',2-(q-s)/s**3),('normalization shift',S.Rational(1,50)-(N-1)/s**3),('variance shift positive',(B/N-1)/s**3),('variance shift upper',S.Rational(1,50)-(B/N-1)/s**3),('raw Fisher upper',2-(2-B/N+4*D/N))]
for label,f in certificates:
 num,den=S.fraction(S.cancel(f));ck(positive_polynomial(num)>0,label+' numerator');ck(positive_polynomial(den)>0,label+' denominator')
ck(5-3==C['temple_denominator_floor'],'Temple separation')
ck(C['residual_sixth_upper']*S.Rational(64,125)==C['trial_energy_sixth_upper'],'energy error conversion')
ck(C['trial_energy_sixth_upper']/C['gap_floor']==C['trial_tv_cubic_upper']**2,'sharp finite TV')
ck(expectation(u*u)<S.Rational(1,16) and expectation(v*v)<S.Rational(1,16),'trial norms')
d2=2*v+u*u;ck(expectation(d2*d2)<1,'density coefficient norm')
ck(2*C['trial_tv_cubic_upper']+1+S.Rational(3,100)+4+6*M<C['density_l1_cubic_upper'],'L1 error composition')
ck(err.subs(s,z)/C['gap_floor']<C['example_tv']**2,'strong example precision')
print('PASS strengthened K1865:',count,'exact groups; Temple and all interval certificates')
print('certified example TV upper approximation',S.N(S.sqrt(err.subs(s,z)/C['gap_floor']),18))

P5=q*q/6+q**3/4+S.Rational(11,108)*q**4+C['value_fifth_coefficient']*q**5
num,den=S.fraction(S.cancel((J-P5)/s**6))
up=sum(abs(c)*M**i for (i,),c in S.Poly(num,s).terms());lo=positive_polynomial(den)
ck(lo>0 and up<3*lo,'fifth polynomial exact whole-interval remainder')
ck(C['trial_energy_sixth_upper']+3<C['value_error_sixth_upper'],'value sixth error composition')
print('FINAL PASS K1865:',count,'exact groups including fifth value with effective error')
