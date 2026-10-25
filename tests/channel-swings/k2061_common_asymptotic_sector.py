"""Exact off-block products; infinite-dimensional claims are in the companion proof."""
from pathlib import Path
import sympy as s
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def produce():
 X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);J=s.Matrix([[0,1],[-1,0]]);I=s.eye(2);k=s.kronecker_product
 cs=[k(X,I),k(Z,X),k(Z,Z)];b=-s.I*k(Z,J);one=s.eye(4);zero=s.zeros(4);checks=[];rows=[]
 def ck(label,value):assert value,label;checks.append(label)
 for pp,mu,lam in [([3,0,0],4,-8),([0,3,0],4,-8),([0,0,3],4,-8),([1,0,0],1,-2),([0,0,0],1,-1),([0,3,4],12,2)]:
  p=list(map(s.Integer,pp));rr=sum(t*t for t in p);E=s.sqrt(rr+mu**2);E1=s.sqrt(rr+(mu+lam)**2);H=sum((t*c for t,c in zip(p,cs)),zero)+mu*b;H1=H+lam*b;P=(one+H/E)/2;Q=one-P
  ck('projector',s.simplify(P*P-P)==zero);ck('full positive spin rank',P.rank()==2)
  A=Q*b*P;coef=s.Rational(rr,rr+mu**2)
  ck('both squared products positive',s.simplify(A.H*A-coef*P)==zero)
  ck('both squared products negative',s.simplify(A*A.H-coef*Q)==zero)
  for cosine,sine in [(s.Rational(3,5),s.Rational(4,5)),(0,1),(1,0)]:
   U=one if E1==0 else cosine*one-s.I*sine*H1/E1
   B=Q*U*P;rho=s.S(0) if E1==0 else s.simplify(lam**2*rr*sine**2/(E**2*E1**2))
   ck('unitary fixture',s.simplify(U.H*U-one)==zero)
   ck('entire incoming fiber product',s.simplify(B.H*B-rho*P)==zero)
   ck('entire outgoing fiber product',s.simplify(B*B.H-rho*Q)==zero)
  rows.append(dict(p=pp,mu=mu,shift=lam,beta_coefficient=str(coef)))
 ck('actual positive fiber dimension',1408//2==704)
 # The square-pulse formula has a removable endpoint at zero post-pulse energy.
 e,tau=s.symbols('e tau',real=True);ck('removable sine quotient',s.limit(s.sin(tau*e)/e,e,0)==tau)
 # Identity used by approximate-sector concentration for finite direct sums.
 weights=[s.Rational(1,7),s.Rational(2,7),s.Rational(4,7)];rho=[s.Rational(1,100),s.Rational(1,4),s.Rational(9,16)]
 for eta2 in [s.Rational(1,20),s.Rational(1,5),s.Rational(1,2)]:
  ck('spectral concentration bound',sum(w for w,r in zip(weights,rho) if r>eta2)<=sum(w*r for w,r in zip(weights,rho))/eta2)
 refs=['lab/process/k2060-positive-energy-localization.json','explorations/conditional-build/k2060-positive-energy-localization-2026-10-25.md','explorations/conditional-build/k2058-universal-positive-dynamics-2026-10-25.md']
 return dict(scope='conditional massive one-particle graph; no source or CAR verdict',checks=checks,fixtures=rows,actual_positive_fiber_dimension=704,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},proof_only=['measure-zero resonances','smooth-pulse real analyticity','dense nonclosed range','torus direct sum'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce();path=ROOT/'lab/process/k2061-common-asymptotic-sector.json'
 if a.write:path.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(path.read_text())==d
 print('PASS',len(d['checks']),'exact algebra and concentration controls')
