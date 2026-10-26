"""Exact even/neutral CAR ground witnesses and finite-sector countercontrols."""
from pathlib import Path
from copy import deepcopy
import json,sympy as s
ROOT=Path(__file__).resolve().parents[2]
def modes(N):
 out=[]
 for j in range(N):
  a=s.zeros(2**N)
  for w in range(2**N):
   if w&(1<<j):a[w^(1<<j),w]=(-1)**sum((w>>k)&1 for k in range(j))
  out.append(a)
 return out
def check(d,comm_sign=1,b_sign=-1,neutral=True):
 a=modes(4);I=s.eye(16);es=[1,3,-1,-3];cs=list(map(s.Rational,['1/3','1/9','2/3','8/9']))
 H=s.diag(*es);C=s.diag(*cs);B=s.zeros(4)
 B[2,0]=B[3,1]=1;B[0,2]=B[1,3]=b_sign
 assert B*B==-s.eye(4) and B*H*B.H==-H,'inherited anti-involution'
 assert B*C*B.H==s.eye(4)-C,'thermal complement'
 G=sum((e*x.H*x for e,x in zip(es,a)),s.zeros(16))
 rho=s.diag(*[s.prod(cs[j] if w>>j&1 else 1-cs[j] for j in range(4)) for w in range(16)])
 N=sum((x.H*x for x in a),s.zeros(16));parity=s.diag(*[(-1)**w.bit_count() for w in range(16)])
 energy=lambda A:s.trace(rho*A.H*(comm_sign*(G*A-A*G)))
 pair=a[0]*a[1]
 assert parity*pair==pair*parity and energy(pair)==-s.Rational(4,27),'positive pair witness'
 holepair=a[2].H*a[3].H;assert energy(holepair)==-s.Rational(4,27),'negative hole witness'
 A=a[2].H*a[0] if neutral else a[0]
 assert A*N==N*A,'actual neutral witness'
 assert energy(A)==d['constants']['neutral_witness_factor']*cs[0]**2,'particle-hole neutral energy'
 assert energy(A)<0,'thermal not ground'
 # Exhaust the finite odd cyclic sector via its actual Hamiltonian spectrum.
 aa=modes(2);e1,e2=d['constants']['finite_odd_energies'];GG=e1*aa[0].H*aa[0]+e2*aa[1].H*aa[1]
 assert e1>0 and e2>e1,'declared two positive levels'
 odd=GG.extract([1,2],[1,2])-e1*s.eye(2)
 assert min(odd.eigenvals())>=0 and (aa[0].H*(GG*aa[0]-aa[0]*GG))[1,1]<0,'finite even not full ground'
 # Shifted-sea neutral ground: matrix units inside each fixed N block exhaust neutral algebra.
 mu=d['constants']['neutral_shift'];occ=[int(e<mu) for e in es];w=sum(o<<j for j,o in enumerate(occ));E0=G[w,w]
 assert occ==[1,0,1,1],'nontrivial shifted occupation'
 for v in range(16):
  if v.bit_count()==w.bit_count():assert G[v,v]>=E0,'neutral shifted ground'
 CC=s.diag(*occ);assert B*CC*B.H!=s.eye(4)-CC,'shifted rival lacks complement'
 return 'pair/neutral exact signs, quaternionic complement, finite parity and chemical-potential countercontrols'
def main():
 d=json.loads((ROOT/'lab/process/k2088-even-ground-selection.json').read_text());print('PASS baseline',check(d),flush=True)
 jobs=[('reversed energy commutator',lambda:check(d,comm_sign=-1)),('wrong anti-involution',lambda:check(d,b_sign=1)),('odd neutral substitute',lambda:check(d,neutral=False))]
 for key,value in [('neutral_witness_factor',-1),('neutral_shift',0),('finite_odd_energies',[3,1])]:
  bad=deepcopy(d);bad['constants'][key]=value;jobs.append((key,lambda b=bad:check(b)))
 for name,fn in jobs:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 print('PASS 6 mathematical faults; nonatomic spectral proof is analytic')
if __name__=='__main__':main()
