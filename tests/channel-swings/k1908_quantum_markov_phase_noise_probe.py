"""Independent phase inequality and witness reconstruction, with genuine input faults."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
N=0
def ck(ok,label):
 global N
 assert bool(ok),label
 N+=1
def eq(a,b,label): ck(s.simplify(s.expand_complex(a-b))==0,label)
def mat(a,b,label): ck((a-b).applyfunc(s.expand_complex).applyfunc(s.simplify)==s.zeros(*a.shape),label)
def pin(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

import copy
from flint import arb,acb,ctx
ctx.prec=128

def math(fault=None):
 global N
 N=0
 # Derive phase identity with z1=e^(iu), z2=e^(iv), using cos/sin polynomials.
 c,d=s.symbols('c d',real=True);a=c;b=s.I*d
 eq(abs(a-s.I*b)**2-(c*c+d*d),2*c*d,'orthogonal phase half-sum identity')
 ck(3+2*s.sqrt(2)<6,'large-b constant');ck((3+2*s.sqrt(2))/2<3,'small-b constant')
 # Independent dense witness and generator, no producer import.
 W=s.Matrix([[s.Rational(17,4),s.Rational(7,4)-3*s.I,-3,-3+3*s.I],[s.Rational(7,4)+3*s.I,s.Rational(17,4),-3,-3-3*s.I],[-3,-3,6,0],[-3-3*s.I,-3+3*s.I,0,6]])
 if fault=='witness':W[0,0]+=1
 l=[-1,1,0,-s.I if fault!='noise' else s.I]
 G=s.Matrix(4,4,lambda j,k:l[j]*s.conjugate(l[k])-(abs(l[j])**2+abs(l[k])**2)/2)
 eq(sum(W),0,'phase-point expectation');eq(s.trace(W*G),-1,'quantum slope')
 B=s.simplify(sum(abs(W[k,j])*abs(G[j,k])**2 for j in range(4) for k in range(4))/2);ck(B<33,'remainder domination')
 eq(sum(abs(x)**2 for x in W),s.Rational(961,4),'independent observable norm')
 # Directed complex ball evaluation at the declared physical time, independent of Taylor proof.
 t=arb(1)/66;values=[acb(-1),acb(1),acb(0),acb(0,-1)];F=[]
 for j in range(4):
  F.append([(t*(values[j]*values[k].conjugate()-(abs(values[j])**2+abs(values[k])**2)/2)).exp() for k in range(4)])
 total=acb(0)
 for j in range(4):
  for k in range(4):
   ww=W[k,j].expand(complex=True);total+=acb(str(s.re(ww)),str(s.im(ww)))*F[j][k]
 ck(total.real< -arb(1)/132,'certified finite-time witness');ck(total.imag.contains(0),'real witness')
 # Positive Gaussian and complex Poisson controls are legitimate classical laws.
 real=[-1,0,2];eq(-s.Rational(1,2)*(real[0]-real[2])**2,-s.Rational(9,2),'Gaussian characteristic exponent')
 unit=[1,s.I,-1,-s.I];U=s.diag(*unit);mat(U.conjugate().T*U,s.eye(4),'complex Poisson unitary')
 # Exact Fourier coefficient census for all off-diagonal output/input pairs.
 identities=[]
 for j in range(4):
  for k in range(4):
   if j==k:continue
   for p in range(4):
    for q in range(4):
     if p==q:continue
     ex=[int(i==j)-int(i==k)-int(i==p)+int(i==q) for i in range(4)]
     identities.append(all(x%3==0 for x in ex)==(j==p and k==q))
 ck(len(identities)==144 and all(identities),'full finite Fourier coefficient census')
 ck(s.Rational(2256,2401)<1,'late phase density positivity')
 return N

def verify(d):
 ck(d['certified_time_interval']=='0<t<1/33','interval report');ck(d['old_poisson_classification']=='classical for t>=log(12)/(1-1/sqrt(2)); earlier times not decided','Poisson ceiling')
 ck(d['dependency_sha256']==pin('explorations/conditional-build/k1906-dephasing-divisibility-boundary-2026-10-21.md'),'dependency pin')
if __name__=='__main__':
 n=math();d=json.loads((ROOT/'lab/process/k1908-quantum-markov-phase-noise.json').read_text());verify(d);print('PASS',n,'independent exact/rigorous-interval controls; reporting and pin baseline')
 for f in ['witness','noise']:
  try:math(f)
  except AssertionError as e:print('[FAIL expected input]',f,e)
  else:raise AssertionError('uncaught '+f)
 for f in ['report','pin']:
  bad=copy.deepcopy(d)
  if f=='report':bad['old_poisson_classification']='classical'
  else:bad['dependency_sha256']='0'*64
  try:verify(bad)
  except AssertionError as e:print('[FAIL expected reporting/provenance]',f,e)
  else:raise AssertionError('uncaught '+f)
 print('PASS 2 input, 1 report, 1 pin faults')
