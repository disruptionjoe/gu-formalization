"""Exact contact cocycles, CAR instruments and fractional-energy integral controls.
Finite checks do not certify continuum local nets or infinite-domain theorems.
"""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as F
import argparse,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2125-local-two-field-collision.json'
def step(x):return int(x>0)
def count(xs,ys):return sum(step(x-y) for x in xs for y in ys)
def crossing(xs,ys,t,velocity=1):return count([x+t for x in xs],[y-velocity*t for y in ys])-count(xs,ys)
def ann(n,j):
 a=s.zeros(2**n)
 for k in range(2**n):
  bits=[(k>>(n-1-i))&1 for i in range(n)]
  if bits[j]:a[k-(1<<(n-1-j)),k]=(-1)**sum(bits[:j])
 return a

def checks(fault=None):
 ck={};put=lambda k,x:ck.__setitem__(k,bool(x));points=[F(-3),F(-1,2),F(3,4),F(2)]
 # General signed time: actual phase differences, with initial phase essential.
 phase=lambda xs,ys,t:count([x+t for x in xs],[y-t for y in ys])-(0 if fault=='omit-initial-conjugacy' else count(xs,ys))
 cocycle=True;initial=True;reverse=True;perm=True
 for xs in combinations(points,2):
  for ys in combinations([p+F(1,7) for p in points],2):
   initial &= phase(xs,ys,0)==0
   perm &= phase(xs,ys,F(2,3))==phase(xs[::-1],ys[::-1],F(2,3))
   for t,u in [(F(1,3),F(5,7)),(F(-2,3),F(1,5)),(F(3),F(-4))]:
    xt=[x+t for x in xs];yt=[y-t for y in ys]
    cocycle &= phase(xs,ys,t+u)==phase(xs,ys,t)+phase(xt,yt,u)
    reverse &= phase(xs,ys,t)+phase(xt,yt,-t)==0
 put('initial-identity',initial);put('signed-cocycle',cocycle);put('reverse-time',reverse);put('fermionic-permutation',perm)
 # Derive field strings by removing actual coordinates before/after collision.
 strings=True;support=True
 for a,b,c in product(points,repeat=3):
  if len({a,b,c})<3:continue
  t=F(4,5);xs=[a,b];ys=[c]
  actual=crossing(xs,ys,t,velocity=(-1 if fault=='wrong-left-velocity' else 1))-crossing([b],ys,t,velocity=(-1 if fault=='wrong-left-velocity' else 1))
  expected=int(a<c<a+2*t)
  strings &= actual==expected and ((s.I if fault=='contact-sign' else -s.I)**actual==(-s.I)**expected)
  if actual:support &= abs(c-(a+t))<=t
 put('R-field-string-from-pairs',strings);put('string-support-cone',support)
 ls=True
 for a,b,c in product(points,repeat=3):
  if len({a,b,c})<3:continue
  t=F(4,5);actual=crossing([a],[b,c],t)-crossing([a],[c],t)
  ls &= actual==int(b-2*t<a<b) and ((s.I if fault=='contact-sign' else -s.I)**actual==(-s.I)**int(b-2*t<a<b))
 put('L-field-string-from-pairs',ls)
 aa=[ann(4,j) for j in range(4)];I=s.eye(16);nn=[a.H*a for a in aa]
 put('actual-CAR',all(aa[i]*aa[j].H+aa[j].H*aa[i]==(I if i==j else s.zeros(16)) for i in range(4) for j in range(4)))
 nr=nn[0]+nn[1];na=nn[3];nb=nn[2]
 if fault=='omit-system-mode':nr=nn[0]
 # Complete crossing phase is a genuine quartic number interaction.
 h=nr*na;U=s.diag(*[(-1)**int(h[i,i]) for i in range(16)])
 if fault=='incomplete-crossing':U=s.diag(*[(-1)**int((nn[0]*na)[i,i]) for i in range(16)])
 env=s.Matrix([0,1,1,0])/s.sqrt(2);embed=s.kronecker_product(s.eye(4),env)
 plus=s.Matrix([0,1,1,0])/s.sqrt(2);minus=s.Matrix([0,-1,1,0])/s.sqrt(2)
 if fault=='uncompensated-readout-phase':plus=s.Matrix([0,s.I,1,0])/s.sqrt(2);minus=s.Matrix([0,-s.I,1,0])/s.sqrt(2)
 ks=[s.kronecker_product(s.eye(4),e.H)*U*embed for e in [plus,minus]]
 pe=s.diag(1,0,0,1);po=s.eye(4)-pe
 units=True
 for i,j in product(range(4),repeat=2):
  E=s.zeros(4);E[i,j]=1
  units &= ks[0]*E*ks[0].H==pe*E*pe and ks[1]*E*ks[1].H==po*E*po
 put('all16-system-matrix-units-recorded',units)
 # Choi/reference equality is checked through actual system-reference vector.
 omega=sum((s.kronecker_product(s.eye(4)[:,i],s.eye(4)[:,i]) for i in range(4)),s.zeros(16,1))/2
 put('reference-record',all(s.kronecker_product(k,s.eye(4))*omega*(s.kronecker_product(k,s.eye(4))*omega).H==s.kronecker_product(p,s.eye(4))*omega*(s.kronecker_product(p,s.eye(4))*omega).H for k,p in zip(ks,[pe,po])))
 # A quarter-turn distinguishes the contact sign; theta=pi alone cannot.
 sign=-1 if fault!='contact-sign' else 1
 Uq=s.diag(*[(sign*s.I)**int(h[i,i]) for i in range(16)])
 onepair=9 # occupation1001: first R and active L1
 put('quarter-turn-contact-sign',Uq[onepair,onepair]==-s.I)
 phaseL=s.diag(*[(-s.I)**int(na[i,i]) for i in range(16)])
 phaseR=s.diag(*[(-s.I)**int((nn[0]+nn[1])[i,i]) for i in range(16)])
 put('quarter-turn-R-CAR-string',Uq.H*aa[0]*Uq==phaseL*aa[0])
 put('quarter-turn-L-CAR-string',Uq.H*aa[3]*Uq==phaseR*aa[3])
 Us=s.diag(*[(-1)**int(((nn[0]+nn[1]+I)*na)[i,i]) for i in range(16)])
 spectator_k=s.kronecker_product(s.eye(4),s.Matrix([0,1,1,0]).T/s.sqrt(2))*Us*embed
 put('crossed-spectator-flips-label',spectator_k==po)
 put('zero-phase-no-readout',s.kronecker_product(s.eye(4),s.Matrix([0,1,1,0]).T/s.sqrt(2))*embed==s.eye(4))

 put('zero-and-full-turn-free',s.diag(*[s.exp(-2*s.pi*s.I*int(h[i,i])) for i in range(16)])==I)
 # Actual even probe-rail coherence distinguishes interaction from Gaussian/free.
 X=aa[2].H*aa[3]+aa[3].H*aa[2]
 put('probe-coherence-transformed',U.H*X*U!=X)
 # Analytic model integral supporting the written jump proof; no finite cutoff claim.
 r,u,e,d=s.symbols('r u e d',positive=True)
 power=2 if fault!='wrong-fractional-kernel' else 1
 integral=s.integrate(s.integrate((r+u)**(-power),(u,d,e)),(r,d,e))
 put('fractional-jump-log',s.simplify(s.diff(integral,d)-(2/(e+d)-1/d))==0)
 put('fractional-jump-diverges',s.limit(integral,d,0,dir='+')==s.oo)
 return ck
FAULTS=['omit-initial-conjugacy','wrong-left-velocity','omit-system-mode','incomplete-crossing','uncompensated-readout-phase','contact-sign','wrong-fractional-kernel']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();good=checks();assert all(good.values()),[k for k,v in good.items() if not v]
 bad={f:[k for k,v in checks(f).items() if not v] for f in FAULTS};assert all(bad.values()),bad
 result=dict(result_id='K2125',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_checks=good,fault_failures=bad,scope='Exact finite contact/cocycle/CAR and integral controls; continuum selfadjointness, local-vN causality and energy divergence require written proofs. Empty Fock, nonsemibounded energy; no GU claim.')
 if args.write:OUT.write_text(json.dumps(result,indent=2)+'\n')
 else:assert result==json.loads(OUT.read_text())
 print('PASS K2125',len(good),'exact checks;',len(bad),'genuine faults')
if __name__=='__main__':main()
