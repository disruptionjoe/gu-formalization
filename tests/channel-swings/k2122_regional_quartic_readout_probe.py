"""Exact regional quartic full instrument; continuum domain proof is in note."""
from pathlib import Path
import sympy as s,json,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2122-regional-quartic-readout.json'
def annih(n,j):
 a=s.zeros(2**n)
 for col in range(2**n):
  bit=1<<(n-j-1)
  if col&bit:a[col^bit,col]=(-1)**((col>>(n-j)).bit_count())
 return a
def checks(fault=None):
 a=[annih(4,j) for j in range(4)];n=[x.H*x for x in a];eye=s.eye(16)
 k=(n[0]+n[1])*n[3]
 if fault=='omit-second-system':k=n[0]*n[3]
 if fault=='quadratic-substitute':k=n[0]+n[1]+n[3]
 theta=s.pi/2 if fault=='pulse-area' else s.pi
 u=s.diag(*[s.exp(-s.I*theta*k[i,i]) for i in range(16)])
 plus=s.Matrix([0,1,1,0])/s.sqrt(2);minus=s.Matrix([0,-1,1,0])/s.sqrt(2)
 if fault=='probe-coherence':plus=s.Matrix([0,0,1,0])
 j=s.kronecker_product(s.eye(4),plus)
 lplus=s.kronecker_product(s.eye(4),s.Matrix([0,1,1,0]).T/s.sqrt(2))*u*j
 lminus=s.kronecker_product(s.eye(4),minus.T)*u*j
 targetplus=s.diag(1,0,0,1);targetminus=s.diag(0,1,1,0)
 ck={};put=lambda name,v:ck.__setitem__(name,bool(v))
 put('bounded-quartic-spectrum',sorted(set(k.diagonal()))==[0,1,2] and k.H==k)
 put('unitary',u.H*u==eye)
 put('actual-Kraus',lplus==targetplus and lminus==targetminus)
 allunits=True
 for i in range(4):
  for j0 in range(4):
   e=s.zeros(4);e[i,j0]=1
   for l,t in [(lplus,targetplus),(lminus,targetminus)]:
    if l*e*l.H != t*e*t:allunits=False
 put('all16-system-matrix-units',allunits)
 # Full-field interleaving/sign controls use actual hopping in energy commutator.
 h=a[0].H*a[2]+a[2].H*a[0]+2*(a[1].H*a[3]+a[3].H*a[1])
 comm=h*k-k*h
 rhs=(h*n[0]-n[0]*h+h*n[1]-n[1]*h)*n[3]+(n[0]+n[1])*(h*n[3]-n[3]*h)
 if fault=='omit-product-term':rhs=(h*n[0]-n[0]*h+h*n[1]-n[1]*h)*n[3]
 put('energy-product-commutator',comm==rhs and comm!=s.zeros(16))
 # Probe signal for system00 versus10, in physical dualrail basis.
 probeplus=s.Matrix([0,1,1,0])/s.sqrt(2)
 out=[]
 for b in [0,2]:
  vv=u*s.kronecker_product(s.eye(4)[:,b],probeplus)
  block=vv[4*b:4*b+4,0];out.append(block*block.H)
 distance=sum(abs(e)*mult for e,mult in (out[0]-out[1]).eigenvals().items())/2
 put('separated-support-signal',distance==1)
 # Actual freely transported output projectors; omitting transport is detectable.
 rg=eye-n[2]-n[3]+a[2].H*a[3]+a[3].H*a[2]
 put('probe-reflection',rg.H==rg and rg*rg==eye)
 hfree=a[0].H*a[2]+a[2].H*a[0]
 uf=eye+(1/s.sqrt(2)-1)*hfree*hfree-s.I*hfree/s.sqrt(2)
 qp=(eye+rg)/2;qt=uf*qp*uf.H
 if fault=='frozen-readout':qt=qp
 put('transported-readout',s.simplify(uf.H*qt*uf*u-qp*u)==s.zeros(16))
 # Unread measurement energy identity holds on all full field matrix units.
 dual=(h+rg*h*rg)/2
 put('unread-measurement-energy',dual-h==rg*(h*rg-rg*h)/2)
 # A generic nonintegral area validates actual spectral phase error squared.
 delta=s.pi/3;err=s.diag(*[s.exp(-s.I*(s.pi+delta)*k[i,i])-s.exp(-s.I*s.pi*k[i,i]) for i in range(16)])
 sq=[s.simplify(s.expand_complex(v*s.conjugate(v))) for v in err.diagonal()]
 put('area-error-norm',max(sq)==3)
 return ck
FAULTS=['omit-second-system','quadratic-substitute','pulse-area','probe-coherence','omit-product-term','frozen-readout']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();clean=checks();assert all(clean.values()),clean
 faults={}
 for f in FAULTS:
  bad=checks(f);fail=[k for k,v in bad.items() if not v];assert fail,f;faults[f]=fail;print('[FAIL detected]',f,fail[0])
 z=dict(result_id='K2122',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=clean,fault_failures=faults,scope='Actual finite regional quartic instrument; continuum common-domain and energy claims rely on written proof. Separated-support version signals; not local-density dynamics.')
 if args.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text())
 print('PASS K2122',len(clean),'exact checks;',len(faults),'genuine faults')
if __name__=='__main__':main()
