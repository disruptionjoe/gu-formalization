"""Exact finite CAR energy identities; continuum domain proof is in the note."""
from pathlib import Path
from copy import deepcopy
import json,sympy as s
ROOT=Path(__file__).resolve().parents[2]
def modes(N):
 out=[]
 for k in range(N):
  a=s.zeros(2**N)
  for w in range(2**N):
   if w>>k&1:a[w^(1<<k),w]=(-1)**sum(w>>j&1 for j in range(k))
  out.append(a)
 return out
def check(d,hole=True,coarse=True):
 a=modes(4);I=s.eye(16);energies=[-1,1,-1,1];c=[s.Rational(3,4),s.Rational(1,4)]*2
 G=sum((e*x.H*x for e,x in zip(energies,a)),s.zeros(16))
 rho=s.diag(*[s.prod(c[j] if w>>j&1 else 1-c[j] for j in range(4)) for w in range(16)])
 f=(a[0]+a[1])/s.sqrt(2);b=(a[2]+a[3])/s.sqrt(2);n=f.H*f;k=b.H*b
 h=I-k if hole else k;E=n+h-n*h
 def D(P):return P*G*P+(I-P)*G*(I-P)-G
 nu=s.trace(rho*n);delta=s.trace(rho*D(n));db=s.trace(rho*D(k))
 refined_kraus=[x*y for x in [n,I-n] for y in [k,I-k]]
 refined_post=sum((L*rho*L.H for L in refined_kraus),s.zeros(16))
 assert s.trace(G*(refined_post-rho))==s.trace(rho*(D(n)+D(k))),'four Kraus refined energy'
 costs=[s.trace(rho*D(n)),s.trace(rho*D(E)),s.trace(rho*(D(n)+D(k)))]
 assert costs==[s.Rational(1,2),s.Rational(1,2),1],'full Fock energy costs'
 predicted=d['constants']['single_factor']*(nu*0-(-s.Rational(1,4)))
 assert delta==predicted,'single trace formula'
 actual=costs[1] if coarse else costs[2]
 assert actual==d['constants']['paired_factor']*(1-nu)*delta,'coarse versus refined cost'
 assert s.simplify(D(E)-D(n)*k-(I-n)*D(k))==s.zeros(16),'operator factorization'
 assert D(E)==(2*E-I)*(G*E-E*G),'bounded relative observable'
 # Two-point covariance pinching, directly from the Fock density after measurement.
 post=n*rho*n+(I-n)*rho*(I-n)
 C=s.diag(*c);v=s.Matrix([1,1,0,0])/s.sqrt(2);R=v*v.H
 Cp=R*C*R+(s.eye(4)-R)*C*(s.eye(4)-R)
 assert s.Matrix(4,4,lambda i,j:s.trace(post*a[j].H*a[i]))==Cp,'actual covariance pinching'
 assert s.trace(s.diag(*energies)*(Cp-C))==delta,'finite rank trace'
 # Pair-integral sign and equality at infinite temperature; inverted control costs negative.
 def energy_formula(es,cs):
  return sum((x-y)*(cy-cx)/4 for x,cx in zip(es,cs) for y,cy in zip(es,cs))
 assert energy_formula([-1,1],[s.Rational(3,4),s.Rational(1,4)])==delta
 assert energy_formula([-1,1],[s.Rational(1,2)]*2)==0
 assert energy_formula([-1,1],[s.Rational(1,4),s.Rational(3,4)])<0,'negative population control'
 # Equal means without complement are insufficient: independently build the Fock input.
 es=[1,2,-1,-2];cs=list(map(s.Rational,['1/5','1/10','7/10','1']))
 GG=sum((e*x.H*x for e,x in zip(es,a)),s.zeros(16));rr=s.diag(*[s.prod(cs[j] if w>>j&1 else 1-cs[j] for j in range(4)) for w in range(16)])
 DD=lambda P:P*GG*P+(I-P)*GG*(I-P)-GG
 df=s.trace(rr*DD(n));dg=s.trace(rr*DD(k));nu2=s.trace(rr*n)
 assert nu2==1-s.trace(rr*k)==s.Rational(3,20)
 assert (df,dg)==(s.Rational(1,20),s.Rational(3,20))
 cc=s.trace(rr*DD(E));assert cc==s.Rational(d['constants']['unequal_coarse']),'unequal-cost counterexample'
 assert cc==(1-nu2)*(df+dg) and cc!=2*(1-nu2)*df
 assert d['constants']['commutator_bound']>=4,'paired CAR product-rule coefficient'
 return 'CAR covariance, full Fock coarse/refined costs, thermal sign and equal-mean counterexample'
def main():
 d=json.loads((ROOT/'lab/process/k2087-relative-measurement-energy.json').read_text());print('PASS baseline',check(d),flush=True)
 jobs=[('wrong hole effect',lambda:check(d,hole=False)),('refined substitute',lambda:check(d,coarse=False))]
 for key,value in [('single_factor',1),('paired_factor',1),('unequal_coarse','17/200')]:
  b=deepcopy(d);b['constants'][key]=value;jobs.append((key,lambda b=b:check(b)))
 for name,fn in jobs:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 print('PASS 5 mathematical faults; no continuum certification by finite matrices')
if __name__=='__main__':main()
