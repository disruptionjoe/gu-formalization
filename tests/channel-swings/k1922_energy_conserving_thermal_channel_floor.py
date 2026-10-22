"""Exact finite energy-conserving dilation controls, not a numerical universal proof."""
from pathlib import Path
import sympy as S
import hashlib,json,argparse
ROOT=Path(__file__).resolve().parents[2]
def calculate(sine_sign=-1,choi_norm=4):
 labels=[]
 def ck(v,label):assert bool(v),label;labels.append(label)
 def eq(a,b,label):ck(S.simplify(a-b)==0,label)
 I=S.I;r=S.sqrt(2);B=S.Matrix([[-1,-1,r,0],[-1,I,0,r]]);H=B.H*B;delta=6-4*r;hn=4+r
 U=S.eye(8);co=S.Rational(3,5);si=S.Rational(4,5);U[1,1]=U[2,2]=co;U[1,2]=sine_sign*si;U[2,1]=si
 ck(U.H*U==S.eye(8),'resonant unitarity');HB=S.diag(0,1);HS=S.diag(0,1,2,3);HT=S.kronecker_product(HS,S.eye(2))+S.kronecker_product(S.eye(4),HB)
 ck(U*HT==HT*U,'total energy conservation');rho=S.diag(S.Rational(3,4),S.Rational(1,4));A=[U[2*i:2*i+2,2*i:2*i+2] for i in range(4)]
 ck(all(a*HB==HB*a for a in A),'energy diagonal blocks')
 leak=[S.simplify(1-S.trace(rho*a.H*a)) for a in A];ck(leak==[S.Rational(4,25),S.Rational(12,25),0,0],'measured leakage')
 J=S.zeros(16)
 for b in range(2):
  for e in range(2):
   K=S.Matrix(4,4,lambda i,j:U[2*i+e,2*j+b])*S.sqrt(rho[b,b]);v=S.Matrix([K[i,j] for i in range(4) for j in range(4)]);J+=v*v.H/choi_norm
 eq(S.trace(J),1,'Choi trace');Q=S.zeros(16,4)
 for i in range(4):Q[5*i,i]=1
 D=S.Matrix(4,4,lambda i,j:S.trace(rho*A[j].H*A[i]));ck(S.simplify(Q.H*J*Q-D/4)==S.zeros(4),'actual Choi compression')
 residual=[sum((B[l,i]*A[i] for i in range(4)),S.zeros(2)) for l in range(2)];WA=S.simplify(sum(S.trace(rho*v.H*v) for v in residual));eq(S.trace(Q*H*Q.H*J),WA/4,'positive Choi witness')
 # All A are positive, so their polar extensions are identity here.
 polar=sum(S.trace(rho*(a-S.eye(2)).H*(a-S.eye(2))) for a in A);ck(polar<=sum(leak),'weighted polar error')
 ck(WA>=delta,'specific residual exceeds tracial gap');eq(sum(leak)/4,S.Rational(4,25),'mean leakage')
 X=S.Matrix([[0,1],[1,0]]);Z=S.diag(1,-1);R=S.Matrix([[co,-si],[si,co]]);V=[S.eye(2),X,Z,R]
 ck(X*Z!=Z*X,'noncommuting degenerate shell')
 wr=S.simplify(sum(S.trace(sum((B[l,i]*V[i] for i in range(4)),S.zeros(2)).H*sum((B[l,i]*V[i] for i in range(4)),S.zeros(2)))/2 for l in range(2)))
 ck(wr>=delta,'degenerate tracial residual');ck(set(H.eigenvals())=={0,4-r,hn},'witness effect norm')
 a=1/r;Vpure=[S.eye(2),X,S.Matrix([[a,-a],[a,a]]),S.Matrix([[a,-I*a],[-I*a,a]])];C=S.Matrix(4,4,lambda i,j:(Vpure[j].H*Vpure[i])[0,0]);eq(S.trace(H*C),0,'pure nonthermal escape')
 ck(Vpure[1]*HB!=HB*Vpure[1],'nondegenerate energy escape breaks conservation');ck(S.diag(1,0)!=S.eye(2)/2,'degenerate pure state is not Gibbs')
 q=S.symbols('q',nonnegative=True);rq=S.diag(1-q,q);Dq=S.Matrix(4,4,lambda i,j:S.trace(rq*Vpure[j].H*Vpure[i]));D1=S.Matrix(4,4,lambda i,j:(Vpure[j].H*Vpure[i])[1,1]);ck(S.simplify(Dq-(1-q)*C-q*D1)==S.zeros(4),'nonthermal escape mixture')
 c0=S.simplify(delta/(16*hn));ck(c0>S.Rational(39,10000),'strict rational lower floor')
 dep=['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md','explorations/conditional-build/k1913-leakage-robust-bath-bound-2026-10-21.md']
 return dict(result_id='K1922',evidence_kind='analytic energy-shell theorem plus exact matrix controls',mathematical_controls=labels,mean_leakage=str(sum(leak)/4),choi_witness=str(WA/4),floor=str(c0),floor_formula='(6-4*sqrt(2))/(16*(4+sqrt(2)))',scope='finite strict thermal operations and diamond closure; not sharp; no catalysts',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dep})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1922-energy-conserving-thermal-channel-floor.json'
 if args.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1922 exact controls',len(r['mathematical_controls']),r['floor'])
