"""Separate Pauli representation and exact transfer checks, with real fault paths."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def check(mode=None):
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2);k=s.kronecker_product
 cs=[k(X,g) for g in [X,Y,Z]];b=k(Z,I);I4=s.eye(4);zero=s.zeros(4);n=0
 def ck(label,test):
  nonlocal n
  assert test,label;n+=1
 for p,mu,lam in [([3,0,0],4,-8),([0,3,0],4,-8),([0,0,3],4,-8),([1,0,0],1,-2),([0,0,0],2,1)]:
  pp=sum(x*x for x in p);E=s.sqrt(pp+mu*mu);Ep=s.sqrt(pp+(mu+lam)**2);H=sum((x*c for x,c in zip(p,cs)),zero)+mu*b;P=(I4+H/E)/(1 if mode=='projector_normalization' else 2);Q=I4-P
  ck('idempotent positive projection',s.simplify(P*P-P)==zero)
  ck('Hermitian positive projection',P.H==P)
  ck('Clifford massive square',H*H==E**2*I4)
  coef=s.Rational(lam**2*pp,1)/(E**2*Ep**2)
  if mode=='massless_denominator':coef=s.Rational(lam**2*pp,1)/(E**2*E**2+1)
  H2=H+lam*b
  ck('normalized pulse offdiagonal amplitude',s.simplify(P*H2*Q*H2*P/Ep**2-coef*P)==zero)
  ck('beta leakage norm',s.simplify(P*b*Q*b*P-s.Rational(pp,1)/E**2*P)==zero)
  if pp and lam:ck('constant allowed mass shift mixes sectors',s.simplify(Q*b*P)==zero if mode=='norm_implies_energy' else s.simplify(Q*b*P)!=zero)
 # Both spin signs retain all internal multiplicities; no unjustified halving.
 real=[576,576,64,64,64,64];mult=[r//(4 if mode=='halve_algebra' else 8) for r in real]
 ck('preserving algebra dimension',sum(x*x for x in mult)==10624)
 # Momentum-transfer intertwiner first-order obstruction uses invertibility C(k).
 for vec in [[1,0,0],[1,2,2],[2,-3,6]]:
  C=sum((v*c for v,c in zip(vec,cs)),zero);ck('nonzero transfer invertible',s.simplify(C*C-sum(v*v for v in vec)*I4)==zero)
 # Constant flavor rotation surviving all spin matrices, with both energy shifts.
 J=s.Matrix([[0,1],[-1,0]]);V=k(I4,-s.I*J);B=k(b,I)
 for c in cs:ck('flavor preserves spatial matrices',V*k(c,I)==k(c,I)*V)
 ck('flavor preserves mass',V*B==B*V);ck('real skew spectrum paired',set((-s.I*J).eigenvals())=={-1,1})
 for mu,r in [(2,1),(1,1),(1,2)]:
  bottom=mu+r*(-1)
  ck('positive restricted energy threshold',(bottom>=0)==(r<=mu if mode!='energy_sign' else r>=mu))
 # A symbolic component zero identity has an odd order at z=i*sqrt(c).
 z=s.symbols('z');c=s.Rational(4);root=2*s.I
 for order in [0,1,2,3]:
  f=(z-root)**order;h=(z*z+c)*f*f
  observed=next(j for j in range(10) if s.diff(h,z,j).subs(z,root)!=0)
  ck('branch zero order obstruction',observed==(2*order if mode=='forget_simple_root' else 2*order+1))
 # Exact sharp mixing: p=mu, lambda=-2mu gives Hnew purely offdiagonal.
 H=cs[0]+b;P=(I4+H/s.sqrt(2))/2;Q=I4-P;H2=cs[0]-b
 ck('complete transfer at pi over two E',s.simplify(P*H2*Q*H2*P/2-P)==zero)
 ck('zero diagonal at complete transfer',s.simplify(P*H2*P)==zero)
 return n
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2060-positive-energy-localization.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 assert d['preserving_dimension']==10624 and d['excluded_dimensions']==159360
 print('PASS separate exact Pauli/projector controls',check(),flush=True);caught=[]
 for m in ['projector_normalization','massless_denominator','norm_implies_energy','halve_algebra','energy_sign','forget_simple_root']:
  try:check(m)
  except AssertionError as e:caught.append((m,str(e)))
  else:raise AssertionError('missed mathematical fault '+m)
 print('PASS six mathematical faults',caught)
