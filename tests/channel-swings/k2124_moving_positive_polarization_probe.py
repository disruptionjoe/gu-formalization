"""Actual moving projector, contracted leakage, wrong-connection and domain controls."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib
import sympy as s
import k2123_same_current_potential_dynamics_probe as n
q=n.q;adj=n.adj;tr=n.tr;comm=n.comm;ROOT=n.ROOT
OUT=ROOT/'lab/process/k2124-moving-positive-polarization.json'
def norm2(a):return s.simplify(sum(s.conjugate(v)*v for v in a.values()))
def checks(fault=None):
 cs,m,fc,t,z,r,p0=n.native();ck={};put=lambda k,x:ck.__setitem__(k,bool(x));S=q.add((s.I,fc))
 rr=q.add((F(3,5),r),(s.I*F(4,5),q.mul(z,r)))
 p=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),q.add((1,q.I),(1,rr)))))
 dr=q.add((F(-4,5),r),(s.I*F(3,5),q.mul(z,r)))
 dp=q.add((F(1,4),q.mul(q.add((1,q.I),(s.I,t)),dr)))
 if fault=='projector-derivative':dp=q.add((-1,dp))
 put('derivative-from-actual-family',dp==q.add((s.I/2,comm(z,p))))
 put('moving-projector',q.mul(p,p)==p and adj(p)==p and tr(p)==32)
 put('same-current',q.mul(p,q.mul(S,p))==q.add((F(9,280),p)))
 put('offbundle-Z',not q.mul(p,q.mul(z,p)))
 grads=[(1,0,0,0),(0,1,0,0),(1,1,0,0),(2,-3,5,7)]
 for j,g in enumerate(grads):
  b=q.add(*[(F(x),A) for x,A in zip(g,[q.I]+cs)])
  actual_b=b
  if fault=='omit-spatial-transport' and j==2:actual_b=q.I
  leak=q.mul(actual_b,q.mul(dp,p));pred=q.add((s.I/2,q.mul(z,q.mul(b,p))))
  put('leakage-formula-'+str(j),leak==pred)
  put('leakage-norm-'+str(j),norm2(leak)==8*sum(x*x for x in g))
  gamma=q.add((-s.I/2,z))
  if fault=='connection-sign':gamma=q.add((-1,gamma))
  put('parallel-projector-'+str(j),not q.add((1,dp),(1,comm(gamma,p))))
  correction=q.add((-s.I/2,q.mul(z,b)))
  if fault=='missing-temporal' and g[0]:correction=q.add((1,correction),(s.I*g[0]/2,z))
  put('contracted-cancellation-'+str(j),not q.add((1,leak),(1,q.mul(q.add((1,q.I),(-1,p)),q.mul(correction,p)))))
  put('outside-raw-image-'+str(j),all(tr(q.mul(A,correction))==0 for A in [q.I]+cs) and norm2(correction)==32*sum(x*x for x in g))
 put('S-compatible',not q.add((1,q.mul(adj(q.add((-s.I/2,z))),S)),(1,q.mul(S,q.add((-s.I/2,z))))))
 # Actual endpoint and time-dependent sections, not altered expected answers.
 put('Z-involution',q.mul(z,z)==q.I)
 v={(i,0):x for (i,j),x in p0.items() if j==0}
 assert v
 psi0=v;psiL=q.add((-1,v))
 if fault=='periodic-transformed-domain':psiL=v
 U0=q.I;UL=q.add((-1,q.I)) # exact exp(i*pi*Z) from involution
 put('global-section-periodic',q.mul(UL,psiL)==q.mul(U0,psi0))
 U=q.add((F(3,5),q.I),(s.I*F(4,5),z));Ut=q.add((s.I/2,q.mul(z,U)))
 phi=q.mul(U,v);dphi=q.mul(Ut,v);H=q.add((F(-1,2),z))
 if fault=='hamiltonian-time-sign':H=q.add((-1,H))
 put('moving-section-Schrodinger',q.add((s.I,dphi),(-1,q.mul(H,phi)))=={})
 vp=q.mul(q.add((F(1,2),q.I),(F(1,2),cs[0])),v)
 vm=q.mul(q.add((F(1,2),q.I),(F(-1,2),cs[0])),v)
 # Choose nonempty test columns separately if first column lies in one eigenspace.
 for col in range(128):
  w={(i,0):x for (i,j),x in p0.items() if j==col}
  if not vp:vp=q.mul(q.add((F(1,2),q.I),(F(1,2),cs[0])),w)
  if not vm:vm=q.mul(q.add((F(1,2),q.I),(F(-1,2),cs[0])),w)
  if vp and vm:break
 Bnull=q.add((1,q.I),(1,cs[0]))
 put('null-gradient-full-fibre-fails',bool(q.mul(Bnull,vp)))
 put('null-gradient-smaller-kernel-survives',bool(vm) and not q.mul(Bnull,vm))

 return ck
FAULTS=['projector-derivative','omit-spatial-transport','connection-sign','missing-temporal','periodic-transformed-domain','hamiltonian-time-sign']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();good=checks();assert all(good.values()),[k for k,v in good.items() if not v]
 bad={f:[k for k,v in checks(f).items() if not v] for f in FAULTS};assert all(bad.values()),bad
 inp=['tests/channel-swings/k2123_same_current_potential_dynamics_probe.py','lab/process/k2120-inherited-core-current.json','lab/process/k2028-all-grade-raw-common-form.json']
 result=dict(result_id='K2124',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=good,fault_failures=bad,scope='Same current, full32 moving family and frozen whole128 raw image; not all32-only raw connections.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inp})
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text())
 print('PASS K2124',len(good),'exact checks;',len(bad),'genuine faults')
if __name__=='__main__':main()
