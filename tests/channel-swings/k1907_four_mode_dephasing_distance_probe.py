"""Independent distance/phase and rigorous interval checks; input faults fail assertions."""
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
 # Derive the four-point inequality as a zero-sum quadratic form.
 w=s.Matrix([1,1,-1,-1]);z=s.Matrix(s.symbols('z0:4',real=True));D=s.Matrix(4,4,lambda j,k:(z[j]-z[k])**2/2)
 eq((w.T*D*w)[0],-(w.dot(z))**2,'conditional negative form')
 a=arb(2).sqrt()/2;pi=arb.pi();lo=arb(13)/100;hi=arb(14)/100
 f=lambda e:e*(a+e)-(a-e)**4
 ck(f(lo)<0 and f(hi)>0,'directed root bracket')
 ck(((arb(100)/13).log()*(1/(a+lo)).log()).sqrt()<pi/4,'phase bound separated from target')
 upper=a-(-pi/4).exp();ck(upper<arb(252)/1000 and upper>arb(251)/1000,'rigorous upper decimal bracket')
 ck((-pi/2).exp()<upper,'long diagonal below upper');ck(abs((-pi/8).exp()-a)<upper,'other entries below upper')
 # Independently obtain the channel from scalar coefficient differences and phases.
 l=[-1,1,0,-s.I if fault!='orientation' else s.I];h=[0,0,0,1]
 A=s.Matrix(4,4,lambda j,k:l[j]*s.conjugate(l[k])-(abs(l[j])**2+abs(l[k])**2)/2-s.I*(h[j]-h[k]))
 for j,k,phase in [(0,2,0),(0,3,0),(1,2,0),(1,3,2),(2,3,1)]:eq(s.im(A[j,k]),phase,'scaled endpoint phase')
 scale=s.Rational(1,4) if fault!='scale' else s.Rational(1,8)
 eq(s.re(A[0,1])*scale,-s.Rational(1,2),'endpoint long pair exponent')
 # Pair-input output difference eigenvalues give its trace norm exactly.
 r=s.symbols('r',positive=True);B=s.Matrix([[0,r/2],[r/2,0]]);ck(set(B.eigenvals())=={-r/2,r/2},'two-mode operational norm')
 return N

def verify(d):
 ck(d['lower_equation']=='e*(1/sqrt(2)+e)=(1/sqrt(2)-e)**4','equation report')
 ck(d['exact_complex_optimum_claimed'] is False,'no false optimum')
 ck(d['dependency_sha256']==pin('explorations/conditional-build/k1906-dephasing-divisibility-boundary-2026-10-21.md'),'dependency pin')
if __name__=='__main__':
 n=math();d=json.loads((ROOT/'lab/process/k1907-four-mode-dephasing-distance.json').read_text());verify(d);print('PASS',n,'independent exact/rigorous-interval controls; reporting and pin baseline')
 for f in ['orientation','scale']:
  try:math(f)
  except AssertionError as e:print('[FAIL expected input]',f,e)
  else:raise AssertionError('uncaught '+f)
 for f in ['report','pin']:
  bad=copy.deepcopy(d)
  if f=='report':bad['exact_complex_optimum_claimed']=True
  else:bad['dependency_sha256']='0'*64
  try:verify(bad)
  except AssertionError as e:print('[FAIL expected reporting/provenance]',f,e)
  else:raise AssertionError('uncaught '+f)
 print('PASS 2 input, 1 report, 1 pin faults')
