"""Independent geometric-shell construction and all matrix-unit channel checks."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
def reconstruct(phase_fault=False):
 n=0
 def check(x):
  nonlocal n
  assert x;n+=1
 # Build shells by multiplicities, not the producer's ceiling loop.
 for k in (2,3,4):
  for a in (1,2,3):
   den=1+(k-1)*a;d=k**a
   p=[F(k,den)]
   for ell in range(1,a):p += [F(k,den*k**ell)]*((k-1)*k**(ell-1))
   p += [F(0)]*(d-len(p));raw=sorted([x/k for x in p for _ in range(k)],reverse=True)
   q=raw[:d];check(sum(q)==sum(p)==1);check(all(x==0 for x in raw[d:]));check(sum(abs(x-y) for x,y in zip(p,q))/2==F(k-1,den))
 # Explicit d=4 preparation permutation recovered independently by equal eigenvalues.
 p=[s.Rational(2,3),s.Rational(1,3),0,0];q=[s.Rational(1,3),s.Rational(1,3),s.Rational(1,6),s.Rational(1,6)]
 initial=s.kronecker_product(s.diag(*p),s.eye(2)/2);desired=s.kronecker_product(s.diag(*q),s.diag(1,0))
 unused=list(range(8));perm=[]
 for val in desired.diagonal():
  i=next(i for i in unused if initial[i,i]==val);unused.remove(i);perm.append(i)
 U=s.zeros(8)
 for i,j in enumerate(perm):U[i,j]=1
 check(U*initial*U.H==desired);check(U*U.H==s.eye(8))
 # Same four full complex unitaries as target; test 16 off/diagonal system blocks.
 B=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[1,1],[1,-1]])/s.sqrt(2),s.Matrix([[1,1],[-s.I,s.I]])/s.sqrt(2)]
 target=[s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([1,1])/s.sqrt(2),s.Matrix([1,-s.I])/s.sqrt(2)]
 if phase_fault:B[3]=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
 for b in B:check(b.H*b==s.eye(2))
 for i in range(4):
  for j in range(4):
   block=s.kronecker_product(s.eye(4),B[i])*desired*s.kronecker_product(s.eye(4),B[j].H)
   reduced=s.Matrix(4,4,lambda x,y:s.simplify(sum(block[2*x+b,2*y+b] for b in range(2))))
   c=(target[j].H*target[i])[0]
   check(reduced.applyfunc(s.simplify)==(s.diag(*q)*c).applyfunc(s.simplify))
 # Reuse the SAME preparation unitary on the changed catalyst, with fresh I/2.
 # First operation is exact; the second need not be. Check actual matrix units.
 def step(state,i,j):
  z=U*s.kronecker_product(state,s.eye(2)/2)*U.H
  z=s.kronecker_product(s.eye(4),B[i])*z*s.kronecker_product(s.eye(4),B[j].H)
  return s.Matrix(4,4,lambda x,y:s.simplify(sum(z[2*x+b,2*y+b] for b in range(2))))
 after=step(s.diag(*p),0,0);check(after==s.diag(*q))
 second=step(after,0,0);check(sum(abs(x) for x in (second-s.diag(*p)).diagonal())/2<=s.Rational(2,3))
 failures=[]
 for i in range(4):
  for j in range(4):
   expected=(target[j].H*target[i])[0]
   failures.append(s.simplify(s.trace(step(after,i,j))-expected)!=0)
 check(any(failures))  # No false reset or exact second-use claim.
 # Faithful harmonic state: evaluate every S block after control, including A marginal.
 for d in (2,4,6):
  H=sum((s.Rational(1,i) for i in range(1,d+1)),s.S.Zero);p=[1/(i*H) for i in range(1,d+1)]
  lam=sorted([x/2 for x in p for _ in (0,1)],reverse=True)
  weights=[[lam[i],lam[d+i]] for i in range(d)];q=[sum(w) for w in weights];r=sum(lam[d:])
  check(sum(q)==1);check(sum(abs(q[i]-p[i]) for i in range(d))/2<=r)
  for j in range(4):
   recovered=[s.trace(B[j]*s.diag(*w)*B[j].H).simplify() for w in weights]
   check(recovered==q)
  check(r==1-sum(s.Rational(1,i) for i in range(1,d//2+1))/H)
 return n
def reject_bad_report(bad,expected):
 try:
  assert bad==expected,'report or dependency pin mismatch'
 except AssertionError as exc:
  print('CAUGHT reporting assertion:',exc)
 else:
  raise AssertionError('report fault escaped')
if __name__=='__main__':
 count=reconstruct();spec=importlib.util.spec_from_file_location('prod',HERE/'k1928_uniform_catalytic_channel_embezzling.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);base=m.calculate();faults=0
 for call in [lambda:m.calculate(weight=2),lambda:m.calculate(swap_fault=True),lambda:reconstruct(phase_fault=True)]:
  try:call()
  except AssertionError as exc:
   print("CAUGHT mathematical assertion:",str(exc) or "exact reconstructed equality");faults+=1
  else:raise AssertionError('mathematical fault escaped')
 report=json.loads((ROOT/'lab/process/k1928-uniform-catalytic-channel-embezzling.json').read_text());assert report==base
 bad=json.loads(json.dumps(report));bad['rank2_return']='1/a';reject_bad_report(bad,base)
 for p,h in report['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 bad=json.loads(json.dumps(report));key=next(iter(bad['dependencies']));bad['dependencies'][key]='0'*64;reject_bad_report(bad,base)
 print('PASS K1928 separate exact controls',count,'math faults',faults,'report/pin faults 1/1')
