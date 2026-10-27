"""Finite exact witnesses for adaptive Gaussian bound; universal proof in note."""
from pathlib import Path
import sympy as s,json,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2121-adaptive-gaussian-parity.json'
def annih(n,j):
 a=s.zeros(2**n)
 for col in range(2**n):
  bit=1<<(n-j-1)
  if col&bit:a[col^bit,col]=(-1)**((col>>(n-j)).bit_count())
 return a
def checks(fault=None):
 a=[annih(4,j) for j in range(4)];ns=[x.H*x for x in a];eye=s.eye(16);vac=eye[:,0]
 def pair(j,k):
  g=a[j].H*a[k].H-a[k]*a[j]
  return eye+(1-1/s.sqrt(2))*g*g+g/s.sqrt(2)
 u=pair(0,1)*pair(2,3);phi=u*vac
 if fault=='missing-second-pair':phi=pair(0,1)*vac
 parity=(eye-2*ns[0])*(eye-2*ns[2])
 if fault=='wrong-system-mode':parity=(eye-2*ns[0])*(eye-2*ns[1])
 pp=(eye+parity)/2;pm=eye-pp
 cp=(eye[:,0]+eye[:,15])/s.sqrt(2);cm=(eye[:,12]+eye[:,3])/s.sqrt(2)
 if fault=='branch-phase':cp=(eye[:,0]-eye[:,15])/s.sqrt(2)
 ck={};put=lambda k,v:ck.__setitem__(k,bool(v))
 put('actual-pair-preparation-unitary',u.H*u==eye)
 put('even-Gaussian-input',phi==(eye[:,0]+eye[:,12]+eye[:,3]+eye[:,15])/2)
 put('ideal-branch-states',pp*phi==cp/s.sqrt(2) and pm*phi==cm/s.sqrt(2))
 # Pfaffian identity from an ACTUAL exponential of generic quadratic creation form.
 x=s.symbols('x0:6',real=True);pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
 b=s.zeros(16)
 for v,(j,k) in zip(x,pairs):b+=v*a[j].H*a[k].H
 if fault=='crossing-sign':b=b.subs(x[1],-x[1])
 psi=(eye+b+b*b/2)*vac;want=x[0]*x[5]-x[1]*x[4]+x[2]*x[3]
 put('actual-BCS-Pfaffian',s.expand(psi[15]-want)==0)
 # AM-GM ingredient (each paired product bounded by sum squares) is exact.
 x1,y1=s.symbols('x y',nonnegative=True)
 put('paired-AMGM',s.expand(x1*x1+y1*y1-2*x1*y1-(x1-y1)**2)==0)
 # All full 4-mode matrix units verify grouped measurement == D1 after ideal.
 p_occ=[(ns[0] if i else eye-ns[0])*(ns[2] if j else eye-ns[2]) for i in range(2) for j in range(2)]
 z1=eye-2*ns[0];allunits=True
 for i in range(16):
  for j in range(16):
   for branch,p in enumerate([pp,pm]):
    ks=[p_occ[k] for k in range(4) if (k//2+k%2)%2==branch]
    lhs=sum(k[i,i]*k[j,j] for k in ks)
    if fault=='coherent-fine-outcomes':lhs=sum(k[i,i] for k in ks)*sum(k[j,j] for k in ks)
    rhs=p[i,i]*p[j,j]*(1+z1[i,i]*z1[j,j])/2
    if lhs!=rhs:allunits=False
 put('all256-matrix-units-two-records',allunits)
 # Witness expectation for the permitted sharpness protocol, with correct records.
 probs=[]
 for branch,chi in enumerate([cp,cm]):
  ks=[p_occ[k] for k in range(4) if (k//2+k%2)%2==branch]
  if fault=='wrong-record':ks=[p_occ[k] for k in range(4) if (k//2+k%2)%2!=branch]
  probs.append(sum(abs((chi.H*k*phi)[0])**2 for k in ks))
 put('sharp-witness-half',s.simplify(sum(probs))==s.Rational(1,2))
 # Direct trace norm of classical-record output difference for same witness.
 dist=0
 for p,chi,branch in [(pp,cp,0),(pm,cm,1)]:
  actual=s.zeros(16)
  for k in range(4):
   if (k//2+k%2)%2==branch:
    v=p_occ[k]*phi;actual+=v*v.H
  ideal=p*phi*phi.H*p
  dist+=sum(abs(ev)*mult for ev,mult in (ideal-actual).eigenvals().items())/2
 put('exact-sharp-trace-distance',dist==s.Rational(1,2))
 return ck
FAULTS=['missing-second-pair','wrong-system-mode','branch-phase','crossing-sign','coherent-fine-outcomes','wrong-record']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();clean=checks();assert all(clean.values()),clean
 faults={}
 for f in FAULTS:
  bad=checks(f);fail=[k for k,v in bad.items() if not v];assert fail,f;faults[f]=fail;print('[FAIL detected]',f,fail[0])
 z=dict(result_id='K2121',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=clean,fault_failures=faults,half_diamond_optimum='1/2',scope='Finite CAR witnesses and full matrix-unit sharpness. Adaptive Gaussian closure and universal bound use attributed/written proof; no GU claim.')
 if args.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text())
 print('PASS K2121',len(clean),'exact checks;',len(faults),'genuine faults')
if __name__=='__main__':main()
