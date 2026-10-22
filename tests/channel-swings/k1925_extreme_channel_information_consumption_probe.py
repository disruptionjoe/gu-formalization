"""Separately reconstructed ensemble spectra, information and thermal accounting."""
from pathlib import Path
import hashlib,json
from fractions import Fraction as F
import sympy as s
import k1925_extreme_channel_information_consumption as producer
ROOT=Path(__file__).resolve().parents[2]
def baseline():
 n=0
 # Direct first-column outputs; no producer vectors or reported spectra used.
 r=s.sqrt(2)/2;us=[s.eye(2),s.Matrix([[0,-1],[1,0]]),s.Matrix([[r,-r],[r,r]]),s.Matrix([[r,-s.I*r],[-s.I*r,r]])]
 initial=s.diag(1,0);out=[u*initial*u.H for u in us]
 for weights in [(1,1,1,1),(1,1,0,0),(1,0,2,3),(0,1,1,0)]:
  total=sum(weights);m=sum((w*x for w,x in zip(weights,out)),s.zeros(2))/total
  assert m.trace()==1 and m.det()>=0,'density average';n+=1
  for rho in [s.diag(s.Rational(1,3),s.Rational(2,3)),s.diag(s.Rational(1,4),s.Rational(3,4))]:
   physical=sum((w*s.kronecker_product(x,rho) for w,x in zip(weights,out)),s.zeros(4))/total
   # Spectra reconstructed as actual roots, independently of report.
   eig=physical.eigenvals();expected={s.simplify(a*b):ma*mb for a,ma in m.eigenvals().items() for b,mb in rho.eigenvals().items()}
   # Compare characteristic polynomials to accommodate degeneracies.
   z=s.symbols('z');poly=s.prod((z-a*b)**(ma*mb) for a,ma in m.eigenvals().items() for b,mb in rho.eigenvals().items())
   assert s.simplify(physical.charpoly(z).as_expr()-poly)==0,'physical tensor spectrum';n+=1
 # Every exact population-preserving realization consumes physical information,
 # not just a complement containing a purifier. Test all pair distances.
 for i in range(4):
  for j in range(4):
   eig=(out[i]-out[j]).eigenvals();dist=sum(abs(a)*mult for a,mult in eig.items())/2
   overlap=(us[j].H*us[i])[0,0]
   assert s.simplify(dist**2-(1-overlap*s.conjugate(overlap)))==0,'physical distance';n+=1
 # Explicit thermodynamic equality with a spectator Gibbs bath, zero apparatus H.
 tau=s.diag(s.Rational(3,4),s.Rational(1,4));mu=(out[0]+out[1])/2
 def ent(x):return -sum(mult*a*s.log(a) for a,mult in x.eigenvals().items() if a!=0)
 final=s.kronecker_product(tau,mu)
 assert s.simplify(ent(final)-ent(tau)-s.log(2))==0,'entropy consumption';n+=1
 assert s.simplify(ent(tau)+ent(mu)-ent(final))==0,'no spurious bath correlation';n+=1
 assert s.simplify(sum(abs(a)*m for a,m in (mu-initial).eigenvals().items())/2-s.Rational(1,2))==0,'qubit disturbance saturation';n+=1
 # A genuine correlated thermal output: bath controls a second orientation.
 mu=sum(out,s.zeros(2))/4;Z=s.diag(1,-1);rot=Z*mu*Z
 joint=s.diag(s.Rational(3,4)*mu,s.Rational(1,4)*rot)
 app=s.Rational(3,4)*mu+s.Rational(1,4)*rot
 chi=ent(mu);info=ent(tau)+ent(app)-ent(joint)
 assert s.simplify(ent(joint)-ent(tau)-chi)==0,'conditional entropy with correlations';n+=1
 assert s.simplify(ent(app)-chi-info)==0,'consumption includes bath correlation';n+=1
 assert joint!=s.kronecker_product(tau,app),'nonzero correlation countercontrol';n+=1
 assert s.simplify(app.det()-s.Rational(31,128))==0,'correlated apparatus spectrum';n+=1
 for m in [1,4,7,16,32]:
  weights=[F(1,i) for i in range(1,2*m+1)];total=sum(weights);weights=[x/total for x in weights]
  output=sorted([x/2 for x in weights for _ in range(2)],reverse=True)
  delta=sum(max(a-b,0) for a,b in zip(weights+[F(0)]*(2*m),output))
  assert delta==sum(weights[m:]),'independent sorted spectral distance';n+=1
  # Pair each duplicated output eigenvalue to its original to check the
  # entropy increment without summing logarithms numerically.
  assert all(output[2*i]==output[2*i+1]==weights[i]/2 for i in range(2*m)),'entropy split exactly log2';n+=1
 return n
def caught(fn,label):
 try:fn()
 except AssertionError as e:assert str(e);print('DETECTED',label,':',e);return
 raise AssertionError('missed '+label)
def check_report(r):
 assert r['uniform_spectrum']==['1/2 + sqrt(2)/8','1/2 - sqrt(2)/8'],'reported spectrum'
 for p,h in r['dependencies'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
if __name__=='__main__':
 producer.calculate();print('PASS K1925 independent finite controls',baseline())
 caught(lambda:producer.calculate(phase=1),'mathematical target phase')
 caught(lambda:producer.calculate(average_divisor=3),'mathematical average normalization')
 r=json.loads((ROOT/'lab/process/k1925-extreme-channel-information-consumption.json').read_text());check_report(r)
 caught(lambda:check_report(dict(r,uniform_spectrum=['1','0'])),'report corruption')
 bad=json.loads(json.dumps(r));bad['dependencies'][next(iter(bad['dependencies']))]='0'*64;caught(lambda:check_report(bad),'pin corruption')
