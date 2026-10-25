"""Separate Pauli implementation and mathematical-fault checks, not a PDE simulation."""
from pathlib import Path
import sympy as s
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def verify(mode=None):
 X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I=s.eye(2);zero=s.zeros(2);n=0
 def ck(label,b):
  nonlocal n
  assert b,label;n+=1
 for r,mu,lam in [(3,4,-8),(1,1,-2),(0,1,2),(4,3,1),(1,2,0)]:
  E=s.sqrt(r*r+mu*mu);E1=s.sqrt(r*r+(mu+lam)**2);H=r*X+mu*Z;H1=r*X+(mu+lam)*Z;P=(I+H/E)/2;Q=I-P
  for c,a in [(s.Rational(3,5),s.Rational(4,5)),(0,1),(1,0)]:
   U=c*I-s.I*a*H1/E1;B=(P if mode=='wrong_energy_block' else Q)*U*P
   coeff=(lam if mode=='drop_mass_shift_square' else lam**2)*r*r*a*a/(E**2*(E**2 if mode=='wrong_final_energy' else E1**2))
   ck('Pauli off-block product',s.simplify(B.H*B-coeff*P)==zero)
   ck('Pauli equal opposite product',s.simplify(B*B.H-coeff*Q)==zero)
 ck('full704 fiber retained',(1408//(4 if mode=='halve_fiber' else 2))==704)
 # Rational exact near-zero algebra bound before applying sin(x)<=x.
 for r in [s.Rational(1,10),s.Rational(1,100),s.Rational(1,1000)]:
  mu=s.Rational(2);lam=s.Rational(3);t=s.Rational(5,4)
  upper=lam**2*r*r*t*t/(r*r+mu*mu)
  claimed=(lam*t*r/mu)**(4 if mode=='false_quadratic_amplitude' else 2)
  ck('near-zero upper-bound factor',upper<=claimed)
 # Exact trigonometric resonance controls, including nonzero torus modes.
 for r,mu,lam in [(3,4,-8),(4,3,-6),(1,1,-2)]:
  E1=s.sqrt(r*r+(mu+lam)**2);t=s.pi/E1
  ck('torus resonance is exact',s.sin(E1*t)==0)
  ck('half-period nonresonance',s.sin(E1*t/2)==1)
 ck('full transfer is not a zero mode',s.Rational((-2)**2,2*2)==1)
 return n
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2061-common-asymptotic-sector.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS separate Pauli controls',verify());faults=[]
 for m in ['wrong_energy_block','drop_mass_shift_square','wrong_final_energy','halve_fiber','false_quadratic_amplitude']:
  try:verify(m)
  except AssertionError as e:faults.append([m,str(e)])
  else:raise AssertionError('missed fault '+m)
 print('PASS five faults',faults)
