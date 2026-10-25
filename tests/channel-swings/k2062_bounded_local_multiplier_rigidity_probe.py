"""Independent Pauli finite-jet rank and noncommuting projector controls."""
from pathlib import Path
import sympy as s
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def rank_check(mass=True,directions=(0,1,2)):
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2);k=s.kronecker_product
 cs=[k(X,g) for g in [X,Y,Z]];b=k(Z,I);vs=s.symbols('v:64');V=s.Matrix(4,4,vs[:16]);ds=[s.Matrix(4,4,vs[16+16*j:32+16*j]) for j in range(3)];eq=[]
 for A in [V]+ds:
  for c in cs:eq+=list(c*A-A*c)
 for n in directions:eq+=list((b*V-V*b if mass else s.zeros(4))-s.I*sum((cs[j]*ds[j] for j in range(3) if j!=n),s.zeros(4)))
 mat,_=s.linear_eq_to_matrix(eq,vs);ker=mat.nullspace();return ker,vs

def fixtures(mode=None):
 P=s.diag(1,0,1,0);Q=s.eye(4)-P;I=s.eye(4);n=0
 def ck(label,v):
  nonlocal n
  assert v,label;n+=1
 for a,b in [(s.Rational(3,5),s.Rational(4,5)),(s.Rational(5,13),s.Rational(12,13))]:
  u=s.Matrix([a,b,0,0]);v=s.Matrix([0,0,b,a]);E=u*u.H+v*v.H;F=P*E*P;B=Q*E*P
  rhs=B.H*B if mode!='defect_sign' else -B.H*B
  if mode=='wrong_complement':rhs=(P*E*P).H*(P*E*P)
  ck('noncommuting compressed projection identity',F-F*F==rhs)
  ck('nontrivial region fixture is unsharp',F*F!=F)
  repair=P*E*P+Q*E*Q+(B if mode=='leave_offblock' else s.zeros(4))
  ck('block repair really commutes',repair*P==P*repair)
  ck('block repair is Hermitian',repair.H==repair)
  ck('positive defect trace',s.trace(F-F*F)>0)
 # Independent direct Pauli kernel trace, including both imaginary signs.
 X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
 for a,b in [(s.Rational(2,3),s.Rational(5,7)),(s.Rational(1,11),s.Rational(9,2))]:
  K=-s.I*X*a+Z*b
  coeff=4 if mode=='kernel_trace_factor' else 2
  ck('kernel Hilbert-Schmidt density',s.trace(K.H*K)==coeff*(a*a+b*b))
 for mu,r,t in [(1,2,s.Rational(1,4)),(3,1,2),(2,5,s.Rational(7,3))]:
  # Remaining half exponent dominates mu*r/2; an exact squared expression.
  ck('heat exponential split',mu*mu*t+r*r/(4*t)-mu*r/2-r*r/(8*t)>=0)
 return n
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2062-bounded-local-multiplier-rigidity.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 ker,vs=rank_check();assert len(ker)==1
 assert s.Matrix(4,4,ker[0][:16])==s.eye(4) and all(x==0 for x in ker[0][16:])
 massless,_=rank_check(False);assert len(massless)==2
 # Omitting one axis alone may leave enough transverse constraints; omit both.
 partial,_=rank_check(True,(0,));assert len(partial)>1
 print('PASS jet nullities massive/massless/one-direction',len(ker),len(massless),len(partial),'plus',fixtures(),'projection controls')
 caught=['mass term omitted enlarges constant class','two directions omitted leave derivative freedom']
 for mode in ['defect_sign','wrong_complement','leave_offblock','kernel_trace_factor']:
  try:fixtures(mode)
  except AssertionError as e:caught.append(mode+': '+str(e))
  else:raise AssertionError('missed mathematical fault '+mode)
 print('PASS six mathematical fault discriminators',caught)
