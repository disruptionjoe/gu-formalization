"""Independent rational spectral calculations and classical transition reconstruction."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
import sympy as s
import k1926_approximate_catalyst_return_bound as producer
ROOT=Path(__file__).resolve().parents[2]
def baseline():
 n=0
 for t in [2,3,4,5]:
  for z in [F(1,3),F(1,2),F(2,3),F(3,4)]:
   si=2*z/(1+z*z);p=F(t*t,t*t+1);q=1-p;gap=F((t-1)**2,t*t);Q=si*si/4;comm=si*si*F((t-1)**2,2*(t*t+1))
   assert gap*Q<=comm,'weighted spectral transfer';n+=1
   # Evaluate the two ordered transition distributions using exact logarithms.
   P=[p*(1-si*si),q*si*si,p*si*si,q*(1-si*si)]
   Qd=[p*(1-si*si),p*si*si,q*si*si,q*(1-si*si)]
   assert sum(P)==sum(Qd)==1,'transition normalization';n+=1
   R=sum(s.Rational(a.numerator,a.denominator)*s.log(s.Rational((a/b).numerator,(a/b).denominator)) for a,b in zip(P,Qd))/4
   expected=s.Rational((si*si*(p-q)/4).numerator,(si*si*(p-q)/4).denominator)*s.log(t*t)
   assert s.simplify(s.expand_log(R-expected,force=True))==0,'likelihood entropy';n+=1
   # Rational lower bound log(t)>=2(t-1)/(t+1) follows by integration;
   # this finite algebra checks that it implies R>=the commutator expression.
   lower=si*si*(p-q)*F(t-1,t+1)
   assert lower>=comm,'log integral lower-bound consumer';n+=1
 # Nonfaithful exact-return support example: zero block is excluded, not inverted.
 rho=s.diag(s.Rational(1,2),s.Rational(1,2),0);u=s.Matrix([[0,1,0],[1,0,0],[0,0,-1]])
 assert u*rho*u.H==rho and rho.rank()==2,'rank deficient invariant support';n+=1
 # Approximate spectral gap must collapse at a near degeneracy.
 t=s.symbols('t',positive=True);assert s.limit((t-1)**2/t**2,t,1)==0,'gap collapse';n+=1
 return n
def caught(fn,label):
 try:fn()
 except AssertionError as e:assert str(e);print('DETECTED',label,':',e);return
 raise AssertionError('missed '+label)
def report(r):
 assert r['commutator_square']=='8/125' and r['return_distance']=='3/25','report constants'
 for p,h in r['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
if __name__=='__main__':
 producer.calculate();print('PASS K1926 independent finite controls',baseline())
 caught(lambda:producer.calculate(weight=s.Rational(1,2)),'mathematical reference weight')
 caught(lambda:producer.calculate(log_sign=-1),'mathematical likelihood direction')
 r=json.loads((ROOT/'lab/process/k1926-approximate-catalyst-return-bound.json').read_text());report(r)
 caught(lambda:report(dict(r,commutator_square='4/125')),'report corruption')
 bad=json.loads(json.dumps(r));bad['dependencies'][next(iter(bad['dependencies']))]='0'*64;caught(lambda:report(bad),'pin corruption')
