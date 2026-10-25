"""Finite exact controls for the written causal-budget and calibration proofs."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
Q=s.Rational;I=s.I
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-I],[I,0]]);sz=s.diag(1,-1)
alpha=[s.kronecker_product(sx,z) for z in [sx,sy,sz]];beta=s.kronecker_product(sz,s.eye(2))

PINS={'explorations/conditional-build/k2067-sector-preserving-pointer-control-2026-10-25.md': 'c078954e7418622126cd9aabdb8ae07e12f110c139ba6cda8134e89ce7fea037', 'lab/process/k2067-sector-preserving-pointer-control.json': '88dfa52e0c15716c11db0c5ca6b6941b2932eb777c0cb204d8c9b0ac4d71ef9e', 'explorations/conditional-build/k2062-bounded-local-multiplier-rigidity-2026-10-25.md': 'ec9b23eb2b0d81139a84465844f47a3b3c9f3a80bfd907432824f1fb145864e5'}

def produce():
 for p,h in PINS.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 checks=0
 def check(b):
  nonlocal checks
  assert b;checks+=1
 for A in alpha+[beta]:check(A*A==s.eye(4));check(A.H==A)
 for i,A in enumerate(alpha+[beta]):
  for B in (alpha+[beta])[i+1:]:check(A*B+B*A==s.zeros(4))
 a,b,m,p=s.symbols('a b m p',real=True);E=s.sqrt(p*p+m*m)
 # Stationary momentum and sharp lower-edge identity, with a>b>0.
 aa,bb,mm=s.symbols('aa bb mm',positive=True);gap2=aa*aa-bb*bb
 # Squared stationarity and value identities avoid branch-unsafe simplification.
 p2=bb*bb*mm*mm/gap2;ep2=aa*aa*mm*mm/gap2
 check(s.simplify(ep2-p2-mm*mm)==0);check(s.simplify(aa*aa*p2-bb*bb*ep2)==0)
 gamma=s.symbols('gamma',positive=True);optb=(1-gamma**2)/2;opta=(1+gamma**2)/2
 check(s.expand(opta+optb)==1);check(s.expand(opta**2-optb**2)==gamma**2)
 a0,b0=Q(2,3),Q(1,3);check(a0+b0==1);check(a0*a0-b0*b0==Q(1,3));check(b0*30==10)
 eps=Q(17,400);visibility=1-2*eps;bell_squared=8*visibility**4
 check(visibility==Q(183,200));check(bell_squared>4)
 for n in [(1,0,0),(0,1,0),(Q(3,5),Q(4,5),0)]:
  A=sum((ni*ai for ni,ai in zip(n,alpha)),s.zeros(4));full=a0*s.kronecker_product(A,s.eye(2))+b0*n[0]*s.kronecker_product(s.eye(4),sz)
  ev=full.eigenvals();check(all(abs(x)<=1 for x in ev));check(sum(ev.values())==8)
  C=s.kronecker_product(A,s.eye(2));delta=1-s.trace(C*full)/8;check(s.simplify(delta-(1-a0))==0)
  dist=s.trace((full-C).H*(full-C));check(s.simplify(dist-16*delta)<=0)
 # Exact control showing A=C is forced at zero normalized trace deficit;
 # the general proof uses I-A^2 positive and trace positivity, not samples.
 C=s.diag(1,-1);A=Q(1,2)*C+Q(1,3)*sx;delta=1-s.trace(C*A)/2
 check((2*2*delta-s.trace((A-C).H*(A-C)))==Q(23,18))
 refs=['explorations/conditional-build/k2067-sector-preserving-pointer-control-2026-10-25.md','lab/process/k2067-sector-preserving-pointer-control.json','explorations/conditional-build/k2062-bounded-local-multiplier-rigidity-2026-10-25.md']
 return dict(id='K2069',scope='conditional massive complex1408 positive sector; imported control and Born apparatus; no source or spacelike-laboratory claim',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},finite_exact_controls=checks,family={'a':'2/3','b':'1/3','time_in_inverse_mass':'30','displacement_in_inverse_mass':'10','spectral_edge_squared_in_mass_squared':'1/3','max_speed':'1','epsilon_upper':str(eps),'visibility_lower':str(visibility),'chsh_squared_lower':str(bell_squared)},calibration={'deficit':'1-ReTr(C(n)A(n))/N','operator_bound':'sqrt(2*N*deficit)','exact_zero':'A(n)=C(n)'},uniform_gap_frontier={'a_max_shift':'(1+gamma^2)/2','b_max_shift':'(1-gamma^2)/2','time_for_displacement':'T>=2*abs(J)/(1-gamma^2)'},limitations=['spatially homogeneous controls','noncompact positive-energy preparation','changed common kinetic coefficient','source real/dual and physical quotient unbuilt'])

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();d=produce();f=ROOT/'lab/process/k2069-causal-budget-pointer.json'
 if a.write:f.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(f.read_text())==d
 print('PASS finite exact controls',d['finite_exact_controls'])
