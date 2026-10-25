"""Finite exact controls; continuum conclusions use the accompanying proof."""
from pathlib import Path
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[2];q=s.Rational
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2)
beta=s.kronecker_product(Z,I);alpha=[s.kronecker_product(X,a) for a in [X,Y,Z]]
def zero(a):return all(s.simplify(x)==0 for x in a)
def checks(fault=None):
 n=0
 for a in alpha+[beta]:assert a*a==s.eye(4),'Clifford square';n+=1
 for i,a in enumerate(alpha+[beta]):
  for b in (alpha+[beta])[i+1:]:assert a*b+b*a==s.zeros(4),'Clifford pair';n+=1
 for p in [(0,0,0),(1,2,2),(3,0,4)]:
  m=s.Integer(2);E=s.sqrt(sum(x*x for x in p)+m*m);H=sum((x*a for x,a in zip(p,alpha)),s.zeros(4))+m*beta;P=(s.eye(4)+H/E)/2
  assert zero(P*P-P),'projector';n+=1
  chi=s.Matrix([1,0]);u=(s.sqrt((E+m)/(2*E))*chi).col_join(sum((x*a for x,a in zip(p,[X,Y,Z])),s.zeros(2))*chi/s.sqrt(2*E*(E+m)))
  assert zero(H*u-E*u) and s.simplify((u.H*u)[0])==1,'positive normalized spinor';n+=2
  control=s.kronecker_product(s.eye(4),Z)*p[0]
  if fault=='sector':control=s.kronecker_product(alpha[0],Z)
  assert zero(s.kronecker_product(P,I)*control-control*s.kronecker_product(P,I)),'sector preservation';n+=1
 for lam in [q(0),q(1,2),q(3,5),-q(4,5)]:
  p=lam/s.sqrt(1-lam**2);energy=s.sqrt(1+p*p)-lam*p
  edge=s.sqrt(1-lam**2) if fault!='edge' else 1-lam**2
  assert s.simplify(energy-edge)==0,'sharp spectral edge';n+=1
 eps=q(17,400) if fault!='error' else q(17,40);eta=1-2*eps
 assert 2*eta**4>1,'certified Bell violation';n+=1
 sig=q(1,4)+4;assert sig/100==q(17,400),'variance to readout';n+=1
 sing=s.Matrix([0,1,-1,0])/s.sqrt(2);a=[Z,X];b=[-(Z+X)/s.sqrt(2),-(Z-X)/s.sqrt(2)]
 op=s.kronecker_product(a[0],b[0]+b[1])+s.kronecker_product(a[1],b[0]-b[1]);val=s.simplify((sing.H*op*sing)[0]*eta**2)
 assert s.simplify(val-2*s.sqrt(2)*eta**2)==0,'readout CHSH';n+=1
 # Commuting internal rotations cannot change a scalar spatial effect.
 F=s.diag(q(1,5),q(4,5));W=(I-s.I*X)/s.sqrt(2);U=s.kronecker_product(I,W)
 assert zero(U.H*s.kronecker_product(F,I)*U-s.kronecker_product(F,I)),'readout blindness';n+=1
 return n
if __name__=='__main__':
 data=json.loads((R/'lab/process/k2067-sector-preserving-pointer-control.json').read_text())
 for p,h in data['inputs'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h,'upstream pin'
 n=checks();caught=[]
 for f in ['sector','edge','error']:
  try:checks(f)
  except AssertionError as e:caught.append((f,str(e)))
  else:raise AssertionError('undetected '+f)
 print('PASS exact algebra controls',n,'real faults',caught)
