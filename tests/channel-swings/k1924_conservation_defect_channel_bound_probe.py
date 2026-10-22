"""Separate componentwise spectral sums and polar-defect verification."""
from pathlib import Path
import sympy as s
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def baseline(gap_power=2,drop_column_weight=False):
 checks=0;B=s.Matrix([[-1,-1,s.sqrt(2),0],[-1,s.I,0,s.sqrt(2)]]);H=B.H*B
 for co,si,q,gap in [(s.Rational(3,5),s.Rational(4,5),s.Rational(1,4),3),(s.Rational(5,13),s.Rational(12,13),s.Rational(1,5),2),(s.Rational(8,17),s.Rational(15,17),s.Rational(2,5),s.Rational(1,10))]:
  # General contraction: unequal input damping makes weighted mistakes observable.
  R=s.Matrix([[co,-si],[si,co]]);A=R*s.diag(s.Rational(2,3),s.Rational(3,4));weights=[1-q,q];energies=[0,gap]
  qoff=sum(weights[j]*abs(A[i,j])**2 for i in range(2) for j in range(2) if i!=j)
  comm=sum(weights[j]*(energies[i]-energies[j])**2*abs(A[i,j])**2 for i in range(2) for j in range(2))
  assert s.simplify(comm-gap**gap_power*qoff)==0,'spectral gap power';checks+=1
  dnorm=sum(weights[j]*abs(A[j,j])**2 for j in range(2));anorm=sum(weights[j]*abs(A[i,j])**2 for i in range(2) for j in range(2))
  assert s.simplify(1-dnorm-(1-anorm)-qoff)==0,'defect decomposition';checks+=1
  polar=sum(weights[j]*(1-A[j,j])**2 for j in range(2));assert polar<=1-dnorm,'polar contraction bound';checks+=1
  mats=[A,s.eye(2),s.Matrix([[0,1],[1,0]]),s.diag(1,-1)]
  C=s.Matrix(4,4,lambda i,j:sum(weights[b]*sum(mats[i][e,b]*s.conjugate(mats[j][e,b]) for e in range(2)) for b in range(2)))
  W=sum((1 if drop_column_weight else weights[b])*abs(sum(B[l,j]*mats[j][e,b] for j in range(4)))**2 for l in range(2) for e in range(2) for b in range(2))
  assert s.simplify(s.trace(H*C)-W)==0,'weighted residual-Choi orientation';checks+=1
 # Inversion checked without square-root simplifier branch assumptions.
 aa=s.Rational(1,20)
 for z in [s.Rational(0),s.Rational(1,5),s.Rational(2,3),s.Rational(1)]:
  f=aa*(1-z)**2/4;assert s.simplify(s.sqrt(f)+s.sqrt(f+aa*z)-s.sqrt(aa))==0,'monotone boundary inversion';checks+=1
 return checks
def caught(fn,label):
 try:fn()
 except AssertionError as e:assert str(e);print('DETECTED',label,':',e);return
 raise AssertionError('missed '+label)
def report(v):
 assert v['result_id']=='K1924' and v['example_Q']=='4/25' and v['example_D2']=='36/25','report defect'
 for p,h in v['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
if __name__=='__main__':
 print('PASS K1924 independent controls',baseline())
 caught(lambda:baseline(gap_power=1),'mathematical gap exponent');caught(lambda:baseline(drop_column_weight=True),'mathematical Gibbs weight')
 r=json.loads((ROOT/'lab/process/k1924-conservation-defect-channel-bound.json').read_text());report(r)
 caught(lambda:report(dict(r,example_Q='0')),'report corruption')
 bad=json.loads(json.dumps(r));bad['dependencies'][next(iter(bad['dependencies']))]='0'*64;caught(lambda:report(bad),'pin corruption')
