"""Exact Kraus/reference/energy controls for the written complete-instrument theorem."""
from pathlib import Path
import argparse,json,hashlib
import sympy as s
G=Path(__file__).resolve().parents[2]
def checks(fault=None):
 e=[s.eye(4)[:,i] for i in range(4)];lam=s.Rational(1,3);O=s.sqrt(lam)*e[0]+s.sqrt(1-lam)*e[3];rho=O*O.H
 k=[s.diag(1,1,0,0),s.diag(0,0,1,1)];V=s.Matrix.hstack(e[0],e[2]);I=s.eye(4)
 if fault=='nonlocal-Kraus':k=[rho,I-rho]
 if fault=='Kraus-normalization':k[0]=2*k[0]
 if fault=='record-labels':k=k[::-1]
 cs=[(O.H*x*O)[0] for x in k];d=1-sum(abs(c)**2 for c in cs)
 W=s.Matrix.vstack(*k);scalar=s.Matrix.vstack(*[c*I for c in cs]);D=W-scalar
 bp=[s.kronecker_product(s.eye(2),s.Matrix([[1/s.sqrt(lam),0],[0,0]])),s.kronecker_product(s.eye(2),s.Matrix([[0,1/s.sqrt(1-lam)],[0,0]]))]
 if fault=='commutant-preparation':bp[1]=s.kronecker_product(s.Matrix([[0,1/s.sqrt(1-lam)],[0,0]]),s.eye(2))
 out=sum((x*rho*x.H for x in k),s.zeros(4));ck={}
 ck['Kraus-completeness']=sum((x.H*x for x in k),s.zeros(4))==I
 ck['global-vacuum-loss']=s.simplify(d-s.Rational(4,9))==0 and s.simplify((O.H*out*O)[0]-(1-d))==0
 ck['vacuum-residual']=s.simplify((O.H*D.H*D*O)[0]-d)==0
 ck['commutant-preparations']=all(s.simplify(bp[j]*O-V[:,j])==s.zeros(4,1) for j in range(2)) and all(x*b==b*x for x in k for b in bp)
 C2=1/lam+1/(1-lam);ck['exact-C-norms']=C2==s.Rational(9,2) and [max((b.H*b).eigenvals()) for b in bp]==[1/lam,1/(1-lam)]
 ck['commutant-residual-transfer']=all(s.simplify(D*b*O-s.diag(b,b)*D*O)==s.zeros(8,1) for b in bp)
 ck['recorded-parity-matrix-units']=all(k[r]*V[:,j]*V[:,ell].H*k[r].H==(V[:,j]*V[:,ell].H if j==ell==r else s.zeros(4)) for r in range(2) for j in range(2) for ell in range(2))
 ck['reduced-vacuum-preserved']=s.Matrix([[out[0,0]+out[1,1],out[0,2]+out[1,3]],[out[2,0]+out[3,1],out[2,2]+out[3,3]]])==s.diag(lam,1-lam)
 H=3*(I-rho) if fault!='gap-energy' else s.zeros(4)
 ck['gapped-energy-saturation']=s.simplify(s.trace(H*out)-3*d)==0
 # Actual two parity-sector coherent input and record block differences, including reference.
 v=(s.Matrix([1,0,0,1]))/s.sqrt(2);vr=v*v.H;pr=[s.diag(1,1,0,0),s.diag(0,0,1,1)]
 norms=[]
 for p in [s.Rational(1,2),s.Rational(1,3)]:
  ns=[]
  for r,w in enumerate([p,1-p]):
   block=pr[r]*vr*pr[r]-w*vr
   if fault=='discard-reference-coherence':block=s.diag(*[block[j,j] for j in range(4)])
   val=s.simplify(sum(abs(ev)*mult for ev,mult in block.eigenvals().items()));ns.append(val)
  expected=(s.sqrt(p*p+s.Rational(1,4))+s.sqrt((1-p)**2+s.Rational(1,4)))/2
  norms.append(s.simplify(sum(ns)/2-expected)==0)
 ck['actual-reference-record-trace-norms']=all(norms)
 x,p=s.symbols('x p',real=True);Dplus=(x-p)**2+4*p*x*(1-x);Dminus=(x-p)**2+4*(1-p)*x*(1-x)
 ck['all-pure-weight-upper-polynomial']=s.expand(Dplus.subs(p,s.Rational(1,2))-(s.Rational(1,4)+x-x*x))==0 and s.expand(Dminus.subs(p,s.Rational(1,2))-(s.Rational(1,4)+x-x*x))==0
 # Exact positive root of scalar necessary condition for a nonzero rational q0.
 C=s.Rational(2);q0=s.Rational(1,2);z=(s.sqrt(C*C+2*q0-q0*q0)-C*(1-q0))/(1+C*C)
 if fault=='root-sign':z=(s.sqrt(C*C+2*q0-q0*q0)+C*(1-q0))/(1+C*C)
 ck['inverted-floor-root']=s.simplify((1-q0+C*z)**2+z*z-1)==0 and z>0 and z<1
 # Explicit escaping sequence (not an optimality claim for fixed C).
 l=s.symbols('l',positive=True);ck['nonuniform-resource-escape']=s.simplify((1/l+1/(1-l))*2*l*(1-l)-2)==0
 return {k:bool(v) for k,v in ck.items()}
FAULTS=['nonlocal-Kraus','Kraus-normalization','record-labels','commutant-preparation','gap-energy','discard-reference-coherence','root-sign']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();ck=checks();assert all(ck.values()),ck;bad={}
 for f in FAULTS:
  bad[f]=[k for k,v in checks(f).items() if not v];assert bad[f],f;print('[FAIL detected]',f,bad[f][0])
 out=dict(result_id='K2133',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=ck,fault_failures=bad,parity_half_diamond_floor='1/sqrt(2)',scope='Full recorded channel on fixed code with explicit commutant C,delta; universal bound uses written proof. No uniform energy law or causal apparatus construction.',inputs={x:hashlib.sha256((G/x).read_bytes()).hexdigest() for x in ['explorations/conditional-build/k2108-local-detector-tradeoffs-2026-10-26.md','explorations/conditional-build/k2130-stable-empty-vacuum-locality-2026-10-27.md']})
 p=G/'lab/process/k2133-recorded-instrument-vacuum-disturbance.json'
 if a.write:p.write_text(json.dumps(out,indent=2)+'\n')
 else:assert json.loads(p.read_text())==out
 print('PASS K2133',len(ck),'exact checks;',len(bad),'genuine faults')
if __name__=='__main__':main()
