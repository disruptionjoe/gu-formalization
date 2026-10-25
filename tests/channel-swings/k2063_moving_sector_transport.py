"""Exact Clifford and scalar identities; universal claims live in the companion proof."""
from pathlib import Path
import argparse, hashlib, json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def produce():
 X=s.Matrix([[0,1],[1,0]]); Z=s.diag(1,-1); J=s.Matrix([[0,1],[-1,0]]); I=s.eye(2);k=s.kronecker_product
 cs=[k(X,I),k(Z,X),k(Z,Z)];b=-s.I*k(Z,J);one=s.eye(4);zero=s.zeros(4);checks=[];rows=[]
 def ck(name,test):
  if not test:raise AssertionError('FAIL '+name)
  checks.append(name)
 for pp,m,v in [([3,0,0],4,2),([0,3,0],4,-2),([0,0,3],4,0),([0,3,4],12,3),([0,0,0],2,7),([1,2,2],3,5)]:
  pp=list(map(s.Integer,pp));m=s.Integer(m);v=s.Integer(v);rr=sum(x*x for x in pp);E=s.sqrt(rr+m*m);A=sum((x*c for x,c in zip(pp,cs)),zero);H=A+m*b;P=(one+H/E)/2;Q=one-P
  pd=v*(rr*b-m*A)/(2*E**3);K=s.I*v*b*A/(2*E**2)
  ck('projector',s.simplify(P*P-P)==zero)
  ck('derivative tangent',s.simplify(P*pd+pd*P-pd)==zero)
  ck('correction Hermitian',K.H==K)
  ck('forced commutator',s.simplify(K*P-P*K-s.I*pd)==zero)
  ck('projector construction',s.simplify(K-s.I*(pd*P-P*pd))==zero)
  ck('offdiagonal',s.simplify(P*K*P+Q*K*Q)==zero)
  ck('norm square',s.simplify(K*K-v*v*rr/(4*E**4)*one)==zero)
  ck('real field reality',-K==-s.conjugate(K))
  D=2*P-3*Q;ck('diagonal freedom',s.simplify((K+D)*P-P*(K+D)-s.I*pd)==zero)
  rows.append(dict(p=list(map(int,pp)),mass=int(m),mass_derivative=int(v),norm_squared=str(v*v*rr/(4*E**4))))
 r,m,R=s.symbols('r m R',positive=True);v=s.symbols('v',real=True)
 q=r/(2*(r*r+m*m));ck('sharp stationary radius',s.simplify(s.diff(q,r).subs(r,m))==0);ck('sharp value',s.simplify(q.subs(r,m)-1/(4*m))==0)
 ck('global upper exact remainder',s.factor(1/(4*m)-q)==(r-m)**2/(4*m*(r*r+m*m)))
 green=s.exp(-m*r)/(4*s.pi*r);ck('Yukawa derivative',s.simplify(s.diff(green,r)+s.exp(-m*r)*(m*r+1)/(4*s.pi*r*r))==0)
 tail=s.exp(-m*R)*(R+2/m);ck('kernel radial tail antiderivative',s.simplify(s.diff(tail,R)+s.exp(-m*R)*(m*R+1))==0)
 z=s.symbols('z');poly=(z*z*b-m*z*cs[0]).subs(z,s.I*m);ck('complex characteristic obstruction',s.simplify(poly+m*m*(b+s.I*cs[0]))==zero);ck('obstruction nonzero',b+s.I*cs[0]!=zero)
 # Exact finite-mode polynomial repair, with a deliberately tested discarded mode.
 q=s.interpolate([(a,s.Rational(1,a+4)) for a in [0,1,4,9]],r)
 for radius2 in [0,1,4,9]:ck('finite-mode exact interpolation',q.subs(r,radius2)==s.Rational(1,radius2+4))
 ck('discarded mode not silently tracked',q.subs(r,16)!=s.Rational(1,20))
 refs=['lab/process/k2058-universal-positive-dynamics.json','lab/process/k2061-common-asymptotic-sector.json','explorations/conditional-build/k2062-bounded-local-multiplier-rigidity-2026-10-25.md']
 return dict(scope='conditional moving massive1408 spectral sector; added nonlocal dynamics',checks=checks,fixtures=rows,positive_fiber_dimension=704,formulas=dict(correction='i*m_dot*beta*A/(2*(r^2+m^2))',continuum_norm='abs(m_dot)/(4*m)',kernel_tail='abs(m_dot)*exp(-m*R)*(R+2/m)/2'),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},proof_only=['complete bounded operator classification','bounded measurable local impossibility','all polynomial differential orders','common H1 propagator','finite-range Duhamel bound','uniform slow-time estimate'])
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce();f=ROOT/'lab/process/k2063-moving-sector-transport.json'
 if a.write:f.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(f.read_text())==d
 print('PASS',len(d['checks']),'exact Clifford/scalar controls; proof claims separate')
