"""Independent support enumeration and action on coherent bath matrix units."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from math import comb
import sympy as s
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def baseline(shell_gap=0,rank_divisor=2):
 count=0
 # Exhaust all allowed support ranks independently, including absent shells.
 for dims in [(1,1),(2,1),(1,3,2),(4,2),(3,5),(2,2,2)]:
  weights=[F(1,3**j) for j in range(len(dims))];Z=sum(d*w for d,w in zip(dims,weights));best=max(sum(r*w for r,w in zip(rs,weights))/Z for rs in product(*[range(d+1) for d in dims]) if all(2*r<=d for r,d in zip(rs,dims)))
  formula=sum((d//rank_divisor)*w for d,w in zip(dims,weights))/Z
  assert best==formula,'shell support optimum';assert best<=F(1,2),'dimension ceiling';count+=2
 # Count odd coefficients via ordinary integers, not the producer's product formula.
 for m in range(1,33):
  q=F(1,5);odd=sum(q**j*(1-q)**(m-j) for j in range(m+1) if comb(m,j)%2)
  p=sum((comb(m,j)//2)*q**j*(1-q)**(m-j) for j in range(m+1));assert 2*p+odd==1,'odd-binomial residual';count+=1
  if m&(m-1)==0:assert odd==q**m+(1-q)**m,'power-two residual';count+=1
 # General coherent input: calculate every channel matrix unit by partial trace.
 r=s.sqrt(2)/2;V=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[r,-r],[r,r]]),s.Matrix([[r,-s.I*r],[-s.I*r,r]])];W=[s.diag(v,v) for v in V]
 H=s.diag(0,shell_gap,5,5);rho=s.zeros(4);rho[0,0]=s.Rational(1,3);rho[2,2]=s.Rational(2,3);rho[0,2]=rho[2,0]=s.Rational(1,4)
 for i in range(4):
  assert W[i]*H==H*W[i],'shellwise conservation'
  for j in range(4):
   coefficient=s.trace(W[i]*rho*W[j].H);expect=(V[j].H*V[i])[0,0]
   assert s.simplify(coefficient-expect)==0,'coherent output matrix unit';count+=1
 # Wrongly using full bath rank would reject the valid coherent state here only if
 # coherence were confused with shell dimension; shell supports each have rank1.
 assert rho.rank()==2 and rho[:2,:2].rank()==rho[2:,2:].rank()==1,'shell support versus global support'
 return count+1
def caught(fn,label):
 try:fn()
 except AssertionError as e:assert str(e);print('DETECTED',label,':',e);return
 raise AssertionError('missed '+label)
def report(r):
 assert r['result_id']=='K1923' and r['example_mass']=='3/16','report mass'
 for p,h in r['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
if __name__=='__main__':
 print('PASS K1923 independent finite controls',baseline())
 caught(lambda:baseline(shell_gap=1),'mathematical shell split');caught(lambda:baseline(rank_divisor=1),'mathematical rank allowance')
 r=json.loads((ROOT/'lab/process/k1923-energy-shell-preparation-cost.json').read_text());report(r)
 caught(lambda:report(dict(r,example_mass='1/2')),'report corruption')
 bad=json.loads(json.dumps(r));bad['dependencies'][next(iter(bad['dependencies']))]='0'*64;caught(lambda:report(bad),'pin corruption')
