"""Exact sea/CAR and antilinear-sign controls; no continuum certification by matrices."""
from pathlib import Path
from copy import deepcopy
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def modes(N):
 aa=[]
 for k in range(N):
  a=s.zeros(2**N)
  for w in range(2**N):
   if w>>k&1:a[w^(1<<k),w]=(-1)**sum(w>>j&1 for j in range(k))
  aa.append(a)
 return aa
def num(a):return a.H*a
def eq(a,b):return (a-b).applyfunc(s.simplify)==s.zeros(a.rows,a.cols)
def check(d,wrong_hole=False,wrong_square=False):
 a=modes(4);I=s.eye(16);vac=s.eye(16)[:,0];sea=a[1].H*a[3].H*vac;electron=a[0].H*sea
 f=(4*a[0]+3*a[1])/5;cf=(3*a[2]+4*a[3])/5;n=num(f);h=num(cf) if wrong_hole else I-num(cf);E=n+h-n*h
 nu=s.Rational(9,25);a2=s.Rational(16,25);c=d['constants']
 formula=lambda text:s.sympify(text,locals={'nu':nu,'a2':a2})
 assert eq(n*h,h*n) and eq(E*E,E),'commuting OR projection'
 assert (sea.H*E*sea)[0]==formula(c['paired_vacuum']),'paired vacuum formula'
 assert (electron.H*E*electron)[0]==formula(c['paired_signal']),'paired electron formula'
 assert eq(E.H*E+(I-E).H*(I-E),I),'complete instrument'
 # Linear particle-hole automorphism with b^2=-I on the one-particle space.
 # b e0=-i e3, b e1=-i e2, b e2=i e1, b e3=i e0.
 B=s.Matrix([[0,0,0,s.I],[0,0,s.I,0],[0,-s.I,0,0],[-s.I,0,0,0]])
 if wrong_square:B[3,0]=B[2,1]=s.I
 H=s.diag(2,-3,3,-2);Q=s.diag(0,1,0,1)
 assert eq(B.H*B,s.eye(4)) and eq(B*s.conjugate(B),-s.eye(4)),'antilinear square'
 assert eq(B*s.conjugate(H)*B.H,-H),'energy sign exchange'
 assert eq(B*s.conjugate(Q)*B.H,s.eye(4)-Q),'sea complement'
 # a is antilinear; a*(b e_i) is linear in b e_i.
 image=[sum((B[j,i]*a[j].H for j in range(4)),s.zeros(16)) for i in range(4)]
 fn=(4*image[0]+3*image[1])/5;cfn=(3*image[2]+4*image[3])/5
 an=num(fn);ah=I-num(cfn)
 assert eq(an,h) and eq(ah,n) and eq(an+ah-an*ah,E),'even charge invariance'
 # Ordinary conjugation in a real Majorana basis: two-mode spectral model.
 Hr=s.Matrix([[0,-s.I],[s.I,0]]);Qr=(s.eye(2)-Hr)/2;real=s.Matrix([1,0])
 assert s.conjugate(Hr)==-Hr and (real.T*Qr*real)[0]==s.Rational(c['real_mode_noise']),'real mode half noise'
 # Coarse OR Lueders differs from resolving both binary occupations.
 candidates=[s.eye(16)[:,j] for j in range(16)]
 assert any(not eq(E*(x*y.H)*E,sum((P*(x*y.H)*P for P in [n*h,n*(I-h),(I-n)*h]),s.zeros(16))) for x in candidates for y in candidates),'coarse refinement differs'
 G=2*num(a[0])+3*(I-num(a[1]))+3*num(a[2])+2*(I-num(a[3]));assert G*sea==s.zeros(16,1)
 post=E*sea*sea.H*E+(I-E)*sea*sea.H*(I-E)
 exact=s.trace(G*post);Hf2=s.Rational(16,25)*4+s.Rational(9,25)*9
 assert exact>=0 and exact**2 <= s.Rational(c['energy_factor'])**2*Hf2*formula(c['paired_vacuum']),'coarse measurement energy bound'
 assert c['anti_square']==-1 and c['automorphism_square']=='fermion_parity','reported square'
 return 'exact four-mode paired detector, sea/sign/automorphism identities, coarse-channel and energy controls'
def main():
 d=json.loads((ROOT/'lab/process/k2082-charge-conjugate-detectors.json').read_text());print('PASS baseline',check(d));faults=[]
 for key,val in [('paired_vacuum','0'),('paired_signal','a2'),('real_mode_noise','0'),('energy_factor','0')]:
  b=deepcopy(d);b['constants'][key]=val;faults.append((key,lambda z=b:check(z)))
 faults += [('wrong hole',lambda:check(d,wrong_hole=True)),('wrong antilinear square',lambda:check(d,wrong_square=True))]
 for name,fn in faults:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e))
  else:raise AssertionError('undetected '+name)
 print('PASS 6 faults; finite identities and reported bounds, not source reality proof')
if __name__=='__main__':main()
