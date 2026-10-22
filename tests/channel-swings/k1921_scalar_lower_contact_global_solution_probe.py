"""Independent rational Hermite reconstruction and boundary-functional checks."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def add(a,b):return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def der(p):return [i*p[i] for i in range(1,len(p))]
def val(p,x):return sum(a*x**i for i,a in enumerate(p))
def integ(p,l):return sum(a*l**(i+1)/F(i+1) for i,a in enumerate(p))
def energy(p,l):return integ(mul(der(der(p)),der(der(p))),l)
def hermite(a,b,v0,v1,l):
 # Endpoint interpolation independently from four boundary values.
 D=b-a-v0*l;V=v1-v0
 return [a,v0,3*D/l**2-V/l,V/l**2-2*D/l**3]
def baseline(moment_factor=1,reaction_factor=1):
 n=0
 for x,w,s,h in [(F(3,4),F(1,4),F(1),F(1)),(F(4,5),F(1,5),F(1),F(2)),(F(2,3),F(1,8),F(1),F(3)),(F(3,4),F(1,2),F(2),F(1))]:
  d=s-w;tau=w/x;k=h*(1-x*x)/w;A=k*d*d/6;j=2*h/tau**2
  # Derive plateau length from endpoint area, rather than solving the producer polynomial.
  p=-A+k*w*w/2+j*w**3/6;ell=(A-p)/h-tau/3
  assert ell>0 and w<=s*x*x and tau<=s,'admissible rational parameters'
  left=hermite(F(0),-A,F(0),F(0),d);right=hermite(-A,p,F(0),h,w);inner=hermite(p+h*ell,A,h,F(0),tau)
  assert val(der(der(left)),d)==moment_factor*val(der(der(right)),0),'contact moment continuity'
  assert val(der(der(inner)),tau)==0,'upper contact moment'
  jr=val(der(der(der(right))),0);ji=val(der(der(der(inner))),0);jl=val(der(der(der(left))),0)
  assert jr==ji==j,'plateau shear cancellation';mu=jr-jl
  assert mu>=0,'lower reaction sign'
  total=2*(energy(left,d)+energy(right,w)+energy(inner,tau))
  formula=2*(12*A*A/d**3+k*k*w+k*j*w*w+j*j*w**3/3+4*h*h/(3*tau))
  assert total==formula,'integrated energy'
  # Arbitrary boundary perturbations include nonzero contact derivative.
  for vm,dm,vp,dp,vb in [(F(2),F(7),F(-3),F(11),F(5)),(F(0),F(-9),F(0),F(6),F(-4)),(F(1,3),F(5,2),F(-1,7),F(9),F(0))]:
   pairing=(val(der(der(left)),d)*dm-jl*vm)+(-jr*vb-val(der(der(right)),0)*dm+jr*vm)+(-ji*vp+ji*vb+val(der(der(inner)),tau)*dp)
   assert pairing==reaction_factor*mu*vm-j*vp,'global boundary certificate'
   assert pairing>=0,'signed reaction positivity'
   n+=1
  if x==F(3,4) and s==h==1:
   assert (ell,A,total)==(F(133,1152),F(21,128),F(147,8)),'independent example'
   assert tau<=F(1,2) and integ([F(0)],F(1,2)-tau)==0,'unequal shorter central gap adds zero energy'
  n+=6
 return n
def caught(fn,label):
 try:fn()
 except AssertionError as e:assert str(e);print('DETECTED',label,':',e);return
 raise AssertionError('missed '+label)
def report(v):
 assert v['result_id']=='K1921' and v['example']['E']=='147/8','report exact example'
 for p,d in v['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'dependency pin'
if __name__=='__main__':
 n=baseline();print('PASS independent rational/boundary controls',n)
 caught(lambda:baseline(moment_factor=2),'mathematical moment corruption');caught(lambda:baseline(reaction_factor=-1),'mathematical reaction corruption')
 p=ROOT/'lab/process/k1921-scalar-lower-contact-global-solution.json';r=json.loads(p.read_text());report(r)
 bad=json.loads(json.dumps(r));bad['example']['E']='845/48';caught(lambda:report(bad),'report corruption')
 bad=json.loads(json.dumps(r));bad['dependencies'][next(iter(bad['dependencies']))]='0'*64;caught(lambda:report(bad),'pin corruption')
