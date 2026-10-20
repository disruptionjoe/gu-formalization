#!/usr/bin/env python3
"""Independent dense Fraction arithmetic, no imports from producer or SymPy."""
import json,copy,hashlib
from pathlib import Path
from fractions import Fraction as F
from math import prod
R=Path(__file__).resolve().parents[2];M=json.loads((R/'lab/process/k1865-fisher-effective-trial-certificate.json').read_text())
def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([x*c for x in a])
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def power(a,n):
 z=[F(1)]
 for _ in range(n):z=mul(z,a)
 return z

def derivative(a):return trim([i*a[i] for i in range(1,len(a))] or [F(0)])
def value(a,x):
 y=F(0)
 for c in reversed(a):y=c+x*y
 return y

def positive(a,t):return a[0]-sum(abs(c)*t**i for i,c in enumerate(a) if i)>0

def moments(a):return sum(c*prod(range(1,i,2)) for i,c in enumerate(a) if i%2==0)
def hermites():
 H=[[F(1)],[F(0),F(1)]]
 for n in range(1,8):H.append(sub([F(0)]+H[-1],scale(H[-2],n)))
 return H

def verify(m):
 checks=0
 def ck(v,label):
  nonlocal checks
  assert v,label
  checks+=1
 cs={k:F(v) for k,v in m['constants'].items()};H=hermites()
 def expand(spec):
  a=[F(0)]
  for n,c in spec.items():a=add(a,scale(H[int(n)],F(c)))
  return a
 u,v=expand(m['trial']['u']),expand(m['trial']['v']);terms=[[F(1)],u,v]
 P={k:list(map(F,row)) for k,row in m['polynomials'].items()}
 for key,shift in [('N',0),('B',2),('C',4),('D',None)]:
  derived=[F(0)]*5
  for i,a in enumerate(terms):
   for j,b in enumerate(terms):
    p=mul(derivative(a),derivative(b)) if shift is None else [F(0)]*shift+mul(a,b)
    derived[i+j]+=moments(p)
  ck(trim(derived)==trim(P[key]),'independent Gaussian '+key)
 N,B,C,D=[P[k] for k in ['N','B','C','D']];b2=power(B,2);n2=power(N,2)
 Q=sub(scale(b2,3),mul(C,N));Jn=sub(add(sub(scale(mul(B,N),2),b2),scale(mul(B,D),4)),n2)
 A=sub(scale(mul(mul(C,b2),Jn),2),mul(N,power(Q,2)));den=scale(mul(mul(C,n2),b2),2)
 t=cs['s_max'];ck(F(0)<t,'positive window')
 for k,p in [('N',N),('B',B),('C',C),('energy denominator',den)]:ck(positive(p,t),'whole interval '+k)
 ck(Q[0]==0,'q origin');ck(positive(Q[1:],t),'q/s positive')
 qs=sub(Q,[F(0)]+b2);ck(qs[:3]==[0,0,0],'q-s order');ck(positive(qs[3:],t),'q>s')
 qp=sub(mul(derivative(Q),B),scale(mul(Q,derivative(B)),2));ck(positive(qp,t),'monotone moment map')
 ck(A[:3]==[0,0,0],'energy cubic cancellation');ck(positive(A[3:],t),'positive gap')
 ck(positive(sub(scale(den,cs['energy_cubic_upper']),A[3:]),t),'cubic energy upper')
 qm=value(Q,t)/value(b2,t);ck(t<qm<F(1,100),'range and spectral window')
 ck(cs['gap_floor']>0 and (cs['gap_floor']+3)**2<18,'inherited harmonic spectral floor')
 ck(cs['energy_cubic_upper']/cs['gap_floor']==cs['tv_squared_cubic_upper'],'TV conversion')
 z=cs['example_s'];ck(0<z<=t,'example in interval')
 excess=value(A,z)/value(den,z);ck(excess>0,'coarse gap positive')
 # Independent finite rational controls, supplementing rather than replacing interval proof.
 for z in [F(1,10000),F(1,2000),F(1,1000),F(1,500),F(1,200)]:
  if z>t:continue
  n,b,k,d=[value(P[key],z) for key in ['N','B','C','D']];q=3-k*n/(b*b);j=b/n*(2-b/n+4*d/n)-1;l=q*q/(2*(3-q))
  ck(j-l==value(A,z)/value(den,z),'separate rational gap')
  ck(0<j-l<cs['energy_cubic_upper']*z**3,'sample control')
 for p,d in m['dependencies'].items():ck(hashlib.sha256((R/p).read_bytes()).hexdigest()==d,'dependency')
 # Rebuild auxiliary oscillator residual using dense x-polynomials.
 p1=[F(1),0,F(-2),0,F(1,3)];p2=[F(19,12),0,F(-11,3),0,F(3,4)]
 r3=add(mul(p1,v),mul(p2,u));r4=mul(p2,v)
 rnorm=[F(0)]*6+[moments(mul(r3,r3)),2*moments(mul(r3,r4)),moments(mul(r4,r4))]
 overlap=[F(0)]*3+[moments(r3),moments(add(r4,mul(u,r3))),moments(add(mul(u,r4),mul(v,r3))),moments(mul(v,r4))]
 ck(trim(rnorm)==trim(P['R2']),'residual Gaussian norm');ck(trim(overlap)==trim(P['hr']),'residual overlap')
 aa=[F(1),F(-2),F(-11,3)];ee=[F(2),F(-1),F(-19,12)]
 ck(positive(sub(aa,[F(25,36)]),t),'auxiliary harmonic floor')
 ck(positive(sub(sub(scale(N,3),mul(ee,N)),overlap),t),'Rayleigh below3')
 ck(cs['temple_denominator_floor']==5-3,'Temple separation')
 ck(positive(sub([cs['residual_sixth_upper']],rnorm[6:]),t),'residual sixth interval')
 ck(positive(sub(scale(n2,F(64,125)),scale(B,F(1,2))),t),'scaled Temple prefactor')
 ck(cs['residual_sixth_upper']*F(64,125)==cs['trial_energy_sixth_upper'],'energy sixth conversion')
 ck(cs['trial_energy_sixth_upper']/cs['gap_floor']==cs['trial_tv_cubic_upper']**2,'TV cubic conversion')
 ck(positive(sub(scale(b2,2),qs[3:]),t),'q shift upper')
 nm=sub(N,[F(1)]);bm=sub(B,N)
 ck(nm[:3]==[0,0,0] and bm[:3]==[0,0,0],'normalization variance order')
 ck(positive(sub([F(1,50)],nm[3:]),t),'normalization shift bound')
 ck(positive(bm[3:],t) and positive(sub(scale(N,F(1,50)),bm[3:]),t),'dilation shift bound')
 ck(positive(sub(B,scale(D,4)),t),'raw Fisher below2')
 d2=add(scale(v,2),mul(u,u));ck(moments(mul(u,u))<F(1,16) and moments(mul(v,v))<F(1,16),'trial L2 bounds');ck(moments(mul(d2,d2))<1,'second density L2 bound')
 ck(2*cs['trial_tv_cubic_upper']+1+F(3,100)+4+6*t<cs['density_l1_cubic_upper'],'L1 composition')
 z=cs['example_s']
 err=value(B,z)*value(rnorm,z)/(cs['temple_denominator_floor']*value(N,z)**2)
 ck(err/cs['gap_floor']<cs['example_tv']**2,'strong example precision')
 # Cross-multiply the fifth value polynomial at q=Q/B^2, no series inversion.
 pq=add(add(scale(mul(power(Q,2),power(B,6)),F(1,6)),scale(mul(power(Q,3),power(B,4)),F(1,4))),add(scale(mul(power(Q,4),power(B,2)),F(11,108)),scale(power(Q,5),cs['value_fifth_coefficient'])))
 diff=sub(mul(Jn,power(B,10)),mul(n2,pq));den5=mul(n2,power(B,10))
 ck(diff[:6]==[0]*6,'fifth value cancellation')
 upper=sum(abs(c)*t**i for i,c in enumerate(diff[6:]));lower=den5[0]-sum(abs(c)*t**i for i,c in enumerate(den5) if i)
 ck(lower>0 and upper<3*lower,'fifth value whole interval')
 ck(cs['trial_energy_sixth_upper']+3<cs['value_error_sixth_upper'],'value error composition')
 ck(all(not m['scope'][k] for k in ['trial_equals_optimizer','arbitrary_moment_transfer','gu_physics','formal_proof']),'reporting ceiling')
 return checks
if __name__=='__main__':
 print('BASELINE PASS',verify(M));mutants=[]
 for key in ['N','B','C','D','R2','hr']:
  b=copy.deepcopy(M);b['polynomials'][key][-1]=str(F(b['polynomials'][key][-1])+F(1,7));mutants.append((key,b))
 for key in ['u','v']:
  b=copy.deepcopy(M);n=next(iter(b['trial'][key]));b['trial'][key][n]=str(F(b['trial'][key][n])+F(1,7));mutants.append((key,b))
 for key,v in [('s_max','1/10'),('gap_floor','7/5'),('energy_cubic_upper','1/10'),('tv_squared_cubic_upper','1/10'),('example_s','1/100'),('example_tv','1/1000000000'),('residual_sixth_upper','100'),('temple_denominator_floor','3'),('trial_energy_sixth_upper','70'),('trial_tv_cubic_upper','7'),('density_l1_cubic_upper','20'),('value_fifth_coefficient','1/3'),('value_error_sixth_upper','79')]:
  b=copy.deepcopy(M);b['constants'][key]=v;mutants.append((key,b))
 for key,b in mutants:
  try:verify(b)
  except AssertionError as e:print('[DETECTED INPUT]',key,str(e))
  else:raise AssertionError('undetected '+key)
 for key in ['trial_equals_optimizer','arbitrary_moment_transfer','gu_physics','formal_proof']:
  b=copy.deepcopy(M);b['scope'][key]=True
  try:verify(b)
  except AssertionError as e:print('[DETECTED REPORT]',key,str(e))
  else:raise AssertionError('undetected reporting '+key)
 print('PASS K1865:',len(mutants),'mathematical input faults, 4 reporting faults')
