"""Finite exact controls for the analytic extreme-environment entropy theorem."""
from pathlib import Path
import argparse, hashlib, json
from fractions import Fraction as F
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def calculate(phase=-1,average_divisor=4):
 checks=[]
 def eq(a,b,label):
  assert s.simplify(a-b)==s.zeros(*a.shape) if isinstance(a,s.MatrixBase) else s.simplify(a-b)==0,label
  checks.append(label)
 rt=s.sqrt(2); vs=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/rt,s.Matrix([1,phase*s.I])/rt]
 ps=[v*v.H for v in vs]; C=s.Matrix(4,4,lambda i,j:(vs[j].H*vs[i])[0]);B=s.Matrix([[-1,-1,rt,0],[-1,s.I,0,rt]])
 eq(s.trace(B.H*B*C),0,'target residual orientation')
 eq(s.Matrix.hstack(*[p.reshape(4,1) for p in ps]).rank(),4,'projector span gives extremality')
 mu=sum(ps,s.zeros(2))/average_divisor
 eq(s.trace(mu),1,'average normalization');eq(mu.det(),s.Rational(7,32),'uniform determinant')
 lam=s.Rational(1,2)+rt/8;eq(lam*(1-lam),mu.det(),'uniform spectrum');eq((ps[0]+ps[1])/2,s.eye(2)/2,'maximal-information prior')
 rho=s.diag(s.Rational(2,3),s.Rational(1,3))
 for i,p in enumerate(ps):
  out=s.kronecker_product(p,rho)
  eq(out.trace(),1,'physical trace '+str(i));eq(out.rank(),2,'physical rank '+str(i))
  for j,q in enumerate(ps):
   # Each two-dimensional difference is traceless: trace norm/2 squared=Tr(D^2)/2.
   eq(s.trace((p-q)**2)/2,1-C[i,j]*C[j,i],'pair discrimination '+str((i,j)))
 avg=sum([s.kronecker_product(p,rho) for p in ps],s.zeros(4))/4
 eq(avg,s.kronecker_product(mu,rho),'physical mixed-environment average')
 eq(avg.det(),mu.det()**2*rho.det()**2,'tensor average determinant')
 # Actual unitary extension on the initially pure apparatus.
 V=[]
 for v in vs:
  w=s.Matrix([-s.conjugate(v[1]),s.conjugate(v[0])]);u=s.Matrix.hstack(v,w);V.append(u)
  eq(u.H*u,s.eye(2),'unitary extension '+str(len(V)))
 for i in range(4):
  for j in range(4):eq((V[j].H*V[i])[0,0],C[i,j],'full channel matrix unit '+str((i,j)))
 pair=[s.kronecker_product(p,q).reshape(16,1) for p in ps for q in ps]
 eq(s.Matrix.hstack(*pair).rank(),16,'tensor-target extremality')
 eq(s.kronecker_product(s.eye(2)/2,s.eye(2)/2),s.eye(4)/4,'two-use optimal prior')
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);pauli=[s.eye(2),X,Y,Z]
 eq(s.Matrix(4,4,lambda i,j:s.trace(pauli[j].H*pauli[i])/2),s.eye(4),'nonextreme countercontrol channel')
 for i,u in enumerate(pauli):eq(u*(s.eye(2)/2)*u.H,s.eye(2)/2,'nonextreme no information '+str(i))
 for m in [1,2,3,5,10,20]:
  r=2*m;hr=sum(F(1,i) for i in range(1,r+1));hm=sum(F(1,i) for i in range(1,m+1))
  initial=[F(1,i)/hr for i in range(1,r+1)]+[F(0)]*r
  final=[F(1,2*((i+1)//2))/hr for i in range(1,2*r+1)]
  eq(sum(abs(a-b) for a,b in zip(initial,final))/2,(hr-hm)/hr,'harmonic return '+str(m))
  eq(sum(final),1,'harmonic normalization '+str(m))
 deps=['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md','explorations/conditional-build/k1923-energy-shell-preparation-cost-2026-10-22.md']
 return dict(result_id='K1925',evidence_kind='analytic physical-support and entropy proof; finite exact controls',mathematical_controls=checks,uniform_spectrum=['1/2 + sqrt(2)/8','1/2 - sqrt(2)/8'],maximum_information='log(2)',thermal_identity='beta*(F_initial-F_final)=chi+mutual_information+relative_entropy',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1925-extreme-channel-information-consumption.json'
 if args.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1925 exact controls',len(r['mathematical_controls']))
