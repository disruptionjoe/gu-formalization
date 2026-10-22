"""Finite exact controls for the analytic KSW/tomography/entropy argument."""
from pathlib import Path
import argparse, hashlib, json, math
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def calculate(phase=-s.I, cross_sign=1):
 labels=[]
 def eq(x,y,label):
  z=x-y
  assert (z.applyfunc(s.simplify)==s.zeros(*z.shape) if isinstance(z,s.MatrixBase) else s.simplify(z)==0),label
  labels.append(label)
 vs=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,phase])/s.sqrt(2)]
 P=[v*v.H for v in vs];X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]])
 eq(2*P[2]-P[0]-P[1],X,'X tomography');eq(P[0]+P[1]-2*P[3],Y,'Y tomography')
 eq((X+cross_sign*s.I*Y)/2,s.Matrix([[0,1],[0,0]]),'offdiagonal tomography')
 M=s.Matrix.hstack(*[p.reshape(4,1) for p in P]);eq(M.det()**2,-s.Rational(1,4),'four projector informational completeness')
 # An explicit physical recovery: qubit target plus arbitrary mixed spectator.
 rho=s.diag(s.Rational(2,3),s.Rational(1,3))
 outs=[s.kronecker_product(p,rho) for p in P]
 for j,out in enumerate(outs):
  rec=s.Matrix(2,2,lambda a,b:sum(out[2*a+t,2*b+t] for t in range(2)))
  eq(rec,P[j],f'physical recovery {j}')
 eq(sum(abs(x) for x in (outs[0]-outs[1]).diagonal())/2,1,'orthogonal physical outputs')
 # Mixed bath without extremality: Pauli unitaries have unchanged marginals.
 unitaries=[s.eye(2),X,Y,s.diag(1,-1)]
 C=s.Matrix(4,4,lambda i,j:s.trace(unitaries[j].H*unitaries[i])/2)
 eq(C,s.eye(4),'nonextreme dephasing Gram')
 for j,u in enumerate(unitaries):eq(u*(s.eye(2)/2)*u.H,s.eye(2)/2,f'nonextreme no physical leakage {j}')
 # Actual leaking pure state; projection trace distance and conditional entropy.
 for p in [s.Rational(1,100),s.Rational(1,5),s.Rational(1,2)]:
  psi=s.Matrix([s.sqrt(1-p),0,0,s.sqrt(p)]);out=psi*psi.H;post=s.diag(1,0,0,0)
  eig=(out-post).eigenvals();D=sum(abs(z)*m for z,m in eig.items())/2
  eq(D,s.sqrt(p),f'gentle normalized projection {p}')
  # The actual bath marginal and normalized projection differ by p, <=sqrt(p).
  bath=s.diag(1-p,p);eq(sum(abs(z) for z in (bath-s.diag(1,0)).diagonal())/2,p,f'marginal conditioning {p}')
 deps=['explorations/conditional-build/k1925-extreme-channel-information-consumption-2026-10-22.md','explorations/conditional-build/k1926-approximate-catalyst-return-bound-2026-10-22.md']
 return {'result_id':'K1927','evidence_kind':'analytic KSW and entropy continuity proof; finite exact controls only','mathematical_controls':labels,'tomography_diamond_coefficient':10,'recovery_full_diamond_coefficient':2,'asymptotic_return_log_dimension':'ln(2)','dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
def bounds(eps):
 h=lambda x:0.0 if x in (0,1) else -x*math.log(x)-(1-x)*math.log1p(-x)
 delta=math.sqrt(2*eps);eta=min(2,10*delta);e=min(.5,delta+math.sqrt(eta));t=min(1,2*math.sqrt(eps))
 L=math.log(2)-h(e);g=2*t*math.log(4)+(1+t)*h(t/(1+t))
 return L,g,L-g
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1927-robust-physical-environment-information.json'
 if a.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1927 exact controls',len(r['mathematical_controls']),'illustrative consumption at epsilon1e-12',bounds(1e-12)[2])
