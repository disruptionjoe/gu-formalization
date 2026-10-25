"""Separate rational resource/characteristic controls and real fault discriminators."""
from fractions import Fraction as F
from pathlib import Path
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[2]

def verify(d):
 errors=[];checks=0
 def check(ok,tag):
  nonlocal checks
  checks+=1
  if not ok:errors.append(tag)
 f=d['family'];a,b,T,J=map(F,[f['a'],f['b'],f['time_in_inverse_mass'],f['displacement_in_inverse_mass']])
 check(a>abs(b),'positive-sector elliptic domain');check(a+abs(b)<=1,'causal cone');check(b*T==J,'integrated translation');check(F(f['max_speed'])==a+abs(b),'characteristic edge')
 check(F(f['spectral_edge_squared_in_mass_squared'])==a*a-b*b,'sharp energy edge')
 variance=F(17,4);eps=variance/(J*J);check(F(f['epsilon_upper'])==eps,'prepared probability');v=1-2*eps
 check(F(f['visibility_lower'])==v,'visibility');check(F(f['chsh_squared_lower'])==8*v**4,'Bell product');check(8*v**4>4,'Bell threshold')
 for p in [F(0),F(1,3),F(1),F(3),F(20)]:
  # E>=abs(bp)+sqrt(a²-b²) after weighting by a: squared
  # residual reaches minimum0 at p²=b²/(a²-b²). Identity is exact.
  gap=a*a-b*b
  check((a*a*(1+p*p)+b*b*p*p-gap)**2-4*a*a*b*b*p*p*(1+p*p)==(gap*p*p-b*b)**2,'spectral minimization identity')
 for g2 in [F(1,9),F(1,3),F(1,2),F(9,10)]:
  aa,bb=(1+g2)/2,(1-g2)/2
  check(aa*aa-bb*bb==g2 and aa+bb==1,'sharp joint frontier')
 for p,h in d['inputs'].items():check(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input '+p)
 return errors,checks

def main():
 d=json.loads((ROOT/'lab/process/k2069-causal-budget-pointer.json').read_text());err,n=verify(d);assert not err,err
 faults={'cone':('b','1/2'),'gap':('spectral_edge_squared_in_mass_squared','2/3'),'translation':('displacement_in_inverse_mass','20'),'probability':('epsilon_upper','17/800'),'Bell':('chsh_squared_lower','8')}
 for label,(k,val) in faults.items():
  q=copy.deepcopy(d);q['family'][k]=val;err,_=verify(q);assert err,(label,'undetected');print('CAUGHT',label,err[0])
 print('PASS separate exact controls',n,'and',len(faults),'mathematical faults')
if __name__=='__main__':main()
