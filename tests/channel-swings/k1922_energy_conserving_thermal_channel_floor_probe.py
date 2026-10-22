"""Independent action-on-matrix-units Choi reconstruction and energy-shell checks."""
from pathlib import Path
import sympy as s
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def baseline(gap=1,normalization=4):
 checks=0
 B=s.Matrix([[-1,-1,s.sqrt(2),0],[-1,s.I,0,s.sqrt(2)]]);H=B.H*B
 for co,si,q in [(s.Rational(3,5),s.Rational(4,5),s.Rational(1,4)),(s.Rational(5,13),s.Rational(12,13),s.Rational(1,10)),(s.Rational(8,17),s.Rational(15,17),s.Rational(1,2))]:
  U=s.eye(8);U[1,1]=U[2,2]=co;U[1,2]=-si;U[2,1]=si
  energies=[i+gap*b for i in range(4) for b in range(2)]
  assert all(U[a,b]==0 or energies[a]==energies[b] for a in range(8) for b in range(8)),'energy-shell support'
  K=[s.Matrix(4,4,lambda a,b:U[2*a+e,2*b+r])*s.sqrt([1-q,q][r]) for r in range(2) for e in range(2)]
  assert s.simplify(sum((k.H*k for k in K),s.zeros(4)))==s.eye(4),'Kraus completeness'
  J=s.zeros(16);leak=[]
  for a in range(4):
   for b in range(4):
    E=s.zeros(4);E[a,b]=1;output=sum((k*E*k.H for k in K),s.zeros(4));J+=s.kronecker_product(output,E)/normalization
    if a==b:leak.append(s.simplify(1-output[a,a]))
  assert s.trace(J)==1,'Choi trace normalization'
  assert leak==[q*si**2,(1-q)*si**2,0,0],'resonant leakage'
  D=s.Matrix(4,4,lambda a,b:J[5*a,5*b]*4)
  A=[s.diag(1,co),s.diag(co,1),s.eye(2),s.eye(2)];rho=s.diag(1-q,q)
  expected=s.Matrix(4,4,lambda a,b:s.trace(rho*A[b].H*A[a]))
  assert s.simplify(D-expected)==s.zeros(4),'Choi block orientation'
  W=sum(s.trace(rho*R.H*R) for R in [sum((B[l,a]*A[a] for a in range(4)),s.zeros(2)) for l in range(2)])
  assert s.simplify(s.trace(H*D)-W)==0,'residual-witness identity'
  assert s.simplify(W-(6-4*s.sqrt(2)))>=0,'finite residual lower bound'
  checks+=7
 # A nonthermal stationary pure state escapes: zero Hamiltonian does not force maximal mixing.
 a=s.sqrt(2)/2;v=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([a,a]),s.Matrix([a,-s.I*a])]
 C=s.Matrix(4,4,lambda i,j:(v[j].H*v[i])[0]);assert s.simplify(s.trace(H*C))==0,'pure exact target'
 assert C.det()==0 and C.rank()==2,'target rank'
 p0=s.Rational(1,3);P=s.diag(1,p0);rho=s.Matrix([[s.Rational(1,2),s.Rational(1,5)],[s.Rational(1,5),s.Rational(1,2)]])
 assert s.trace(rho*(s.eye(2)-P*P))-s.trace(rho*(s.eye(2)-P)**2)==s.Rational(2,9),'polar inequality noncommuting control'
 return checks+3
def caught(fn,label):
 try:fn()
 except AssertionError as e:assert str(e);print('DETECTED',label,':',e);return
 raise AssertionError('missed '+label)
def report(v):
 assert v['result_id']=='K1922' and v['mean_leakage']=='4/25','report result'
 assert s.simplify(s.sympify(v['floor'])-(6-4*s.sqrt(2))/(16*(4+s.sqrt(2))))==0,'report floor'
 for p,d in v['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'dependency pin'
if __name__=='__main__':
 print('PASS independent matrix controls',baseline())
 caught(lambda:baseline(gap=2),'mathematical energy corruption');caught(lambda:baseline(normalization=1),'mathematical Choi corruption')
 r=json.loads((ROOT/'lab/process/k1922-energy-conserving-thermal-channel-floor.json').read_text());report(r)
 bad=dict(r,mean_leakage='0');caught(lambda:report(bad),'report corruption')
 bad=json.loads(json.dumps(r));bad['dependencies'][next(iter(bad['dependencies']))]='0'*64;caught(lambda:report(bad),'pin corruption')
