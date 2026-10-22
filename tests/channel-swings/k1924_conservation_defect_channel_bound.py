"""Exact weighted-pinching and Choi controls for the analytic defect inequality."""
from pathlib import Path
import sympy as s
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
def calculate(gap_square=2,choi_divisor=4):
 labels=[]
 def ck(v,n):assert bool(v),n;labels.append(n)
 def eq(a,b,n):ck(s.simplify(a-b)==0,n)
 B=s.Matrix([[-1,-1,s.sqrt(2),0],[-1,s.I,0,s.sqrt(2)]]);H=B.H*B;delta=6-4*s.sqrt(2);h=4+s.sqrt(2);a=delta/(4*h)
 tau=s.diag(s.Rational(3,4),s.Rational(1,4));HB=s.diag(0,3);co=s.Rational(3,5);si=s.Rational(4,5);R=s.Matrix([[co,-si],[si,co]])
 A=[R,s.eye(2),s.Matrix([[1,0],[0,-1]]),s.eye(2)];D=[s.diag(*v.diagonal()) for v in A];norm=lambda v:s.simplify(s.trace(tau*v.H*v))
 qs=[norm(v-d) for v,d in zip(A,D)];Q=sum(qs)/4;D2=sum(norm(HB*v-v*HB) for v in A)/4
 eq(Q,s.Rational(4,25),'off-shell mass');eq(D2,3**gap_square*Q,'gap-squared identity')
 for i,(v,d) in enumerate(zip(A,D)):
  eq(norm(v),norm(d)+norm(v-d),'weighted Pythagoras '+str(i));eq(1-norm(d),1-norm(v)+qs[i],'leakage plus defect '+str(i))
 residual=lambda xs:[sum((B[l,j]*xs[j] for j in range(4)),s.zeros(2)) for l in range(2)]
 WA=sum(norm(v) for v in residual(A));WD=sum(norm(v) for v in residual(D));WO=sum(norm(v) for v in residual([v-d for v,d in zip(A,D)]));eq(WA,WD+WO,'residual orthogonal split')
 C=s.Matrix(4,4,lambda i,j:s.trace(tau*A[j].H*A[i]));J=s.zeros(16)
 for i in range(4):
  for j in range(4):J[5*i,5*j]=C[i,j]/choi_divisor
 eq(s.trace(J),1,'Choi normalization');eq(s.trace(H*C),WA,'complex residual orientation')
 # A nontrivial block-degenerate shell pinching with noncommuting matrices.
 X=s.Matrix([[0,1,0],[1,0,1],[0,1,0]])/3;P=s.diag(1,1,0);Pc=s.eye(3)-P;DX=P*X*P+Pc*X*Pc;t3=s.diag(s.Rational(2,5),s.Rational(2,5),s.Rational(1,5))
 eq(s.trace(t3*DX.H*(X-DX)),0,'degenerate weighted orthogonality');ck(DX*X!=X*DX,'noncommuting pinched matrix')
 z=s.symbols('z',nonnegative=True);eps=a*(1-z)**2/4
 eq((s.sqrt(a)*(1-z)/2)**2,eps,'inverted root first term');eq((s.sqrt(a)*(1+z)/2)**2,eps+a*z,'inverted root second term')
 eq(a/4,delta/(16*h),'zero-defect floor');ck(a>0,'positive witness threshold')
 # Nonzero population leakage with zero off-shell diagonal defect.
 U=s.eye(8);U[1,1]=U[2,2]=co;U[1,2]=-si;U[2,1]=si
 HT=s.diag(*[i+b for i in range(4) for b in range(2)]);ck(U*HT==HT*U,'resonant total conservation')
 blocks=[U[2*j:2*j+2,2*j:2*j+2] for j in range(4)];eq(sum(1-norm(v) for v in blocks)/4,s.Rational(4,25),'resonant mean leakage');ck(all(v==s.diag(*v.diagonal()) for v in blocks),'resonant zero Q')
 deps=['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md','explorations/conditional-build/k1913-leakage-robust-bath-bound-2026-10-21.md','explorations/conditional-build/k1922-energy-conserving-thermal-channel-floor-2026-10-22.md']
 return dict(result_id='K1924',evidence_kind='analytic weighted pinching proof and exact finite controls',mathematical_controls=labels,example_Q=str(Q),example_D2=str(D2),bound='max(a-Q,0)^2/(4*a), a=(6-4*sqrt(2))/(4*(4+sqrt(2)))',scope='arbitrary finite joint unitary with Gibbs reference; bound not sharp',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1924-conservation-defect-channel-bound.json'
 if args.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1924 exact controls',len(r['mathematical_controls']))
