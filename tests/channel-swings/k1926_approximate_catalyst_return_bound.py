"""Exact matrices and transition identities for the analytic return bound."""
from pathlib import Path
import argparse,hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def calculate(weight=s.Rational(4,5),log_sign=1):
 labels=[]
 def eq(a,b,n):assert s.simplify(s.expand_log(a-b,force=True))==0,n;labels.append(n)
 def ok(x,n):assert bool(x),n;labels.append(n)
 p=s.Rational(4,5);q=1-p;rho=s.diag(p,q);root=s.diag(s.sqrt(p),s.sqrt(q));co=s.Rational(3,5);si=s.Rational(4,5);V=s.Matrix([[co,-si],[si,co]])
 U=s.diag(V,s.eye(2),s.eye(2),s.eye(2));gamma=s.kronecker_product(s.eye(4)/4,rho);rg=s.kronecker_product(s.eye(4)/2,root);g=list(gamma.diagonal());R=0;aff=0;pt=qt=0
 for i in range(8):
  for j in range(8):
   z=U[i,j]*s.conjugate(U[i,j]);pt+=z*g[j];qt+=z*g[i]
   R+=log_sign*z*g[j]*s.log(g[j]/g[i]);aff+=z*s.sqrt(g[j]*g[i])
 comm=s.trace((U*rg-rg*U).H*(U*rg-rg*U));eq(pt,1,'P normalization');eq(qt,1,'Q normalization');eq(comm,2-2*aff,'Hellinger commutator identity');eq(comm,s.Rational(8,125),'square-root state commutator')
 eq(R,s.Rational(12,125)*s.log(4),'relative entropy orientation')
 D=s.diag(*V.diagonal());Q=s.trace(s.diag(weight,1-weight)*(V-D).H*(V-D))/4
 eq(Q,s.Rational(4,25),'weighted off-spectrum mass')
 # An asymmetric contraction detects a wrong reference weight, unlike the rotation.
 A=s.Matrix([[0,s.Rational(1,2)],[0,0]])
 eq(s.trace(s.diag(weight,1-weight)*A.H*A),s.Rational(1,20),'asymmetric weighted matrix entry')
 kap=(s.sqrt(p)-s.sqrt(q))**2/p;eq(kap,s.Rational(1,4),'ordered relative separation');ok(kap*Q<=comm,'spectral transfer')
 final=U*gamma*U.H;cat=s.zeros(2)
 for j in range(4):cat+=final[2*j:2*j+2,2*j:2*j+2]
 logrho=s.diag(s.log(p),s.log(q));eq(-s.trace(logrho*(cat-rho)),R,'degenerate energy return identity')
 dist=s.sqrt(s.trace((cat-rho)**2)/2);eq(dist,s.Rational(3,25),'return trace distance')
 # Noncontrolled resonant mixing: exact energy conservation but population leakage.
 W=s.eye(8);W[1,1]=W[2,2]=co;W[1,2]=-si;W[2,1]=si
 HS=s.diag(0,1,2,3);HA=s.diag(0,1);HT=s.kronecker_product(HS,s.eye(2))+s.kronecker_product(s.eye(4),HA)
 ok(W*HT==HT*W,'noncontrolled exact conservation');f=W*gamma*W.H
 sp=s.Matrix(4,4,lambda i,j:sum(f[2*i+b,2*j+b] for b in range(2)));ap=sum((f[2*j:2*j+2,2*j:2*j+2] for j in range(4)),s.zeros(2));deltaE=s.trace(HS*(sp-s.eye(4)/4))
 eq(deltaE+s.trace(HA*(ap-rho)),0,'energy exchange');eq(-deltaE-s.trace((HA+logrho)*(ap-rho)),R,'nonunital entropy identity')
 ok(sp!=s.eye(4)/4,'nonunital countercontrol')
 # Entirely degenerate state gives zero defect for a nontrivial rotation.
 tracial=s.eye(8)/8;ok(W*tracial*W.H==tracial,'single spectral block')
 x=s.symbols('x',positive=True);eps=1/(1+s.sqrt(1+x))**2
 eq(x*eps+2*s.sqrt(eps),1,'exact-return quadratic root')
 deps=['explorations/conditional-build/k1912-faithful-bath-dephasing-boundary-2026-10-21.md','explorations/conditional-build/k1913-leakage-robust-bath-bound-2026-10-21.md','explorations/conditional-build/k1924-conservation-defect-channel-bound-2026-10-22.md']
 return dict(result_id='K1926',evidence_kind='analytic spectral/Hellinger proof and finite exact identities',mathematical_controls=labels,kappa='1/4',Q='4/25',commutator_square='8/125',relative_entropy='12*log(4)/125',return_distance='3/25',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=calculate();p=ROOT/'lab/process/k1926-approximate-catalyst-return-bound.json'
 if args.write:p.write_text(json.dumps(r,indent=2)+'\n')
 else:assert json.loads(p.read_text())==r,'report consistency'
 print('PASS K1926 exact controls',len(r['mathematical_controls']))
