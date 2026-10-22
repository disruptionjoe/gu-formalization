"""Separate recurrence, direct deficits and symbolic chord checks; no producer import."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,copy
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1960-thermal-frontier-convexification.json'

def reconstruct(n,m,fault=None):
 q=F(2,3) if fault!='left_ratio' else F(3,4);p=F(1,9)
 left=[F(1)];right=[]
 for _ in range(n):left.append(left[-1]*q)
 value=F(1)
 for _ in range(m):value*=p;right.append(value)
 a=left[::-1]+right;Z=sum(a);a=[x/Z for x in a];energies=[F(1+2*j) for j in range(len(a))]
 if fault=='energy_origin':energies=[x+1 for x in energies]
 incoming=[F(0)]*len(a)
 # Bath probabilities are formed directly, not via predecessor rate().
 bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
 for j in range(len(a)-1):
  imbalance=sum(bath[2:])*a[j]-sum(bath[:2])*a[j+1]
  incoming[j]+=max(F(0),-imbalance);incoming[j+1]+=max(F(0),imbalance)
 ret=sum(max(F(0),x-y) for x,y in zip(a,incoming))/2
 if fault=='return_factor':ret*=2
 return sum(x*y for x,y in zip(a,energies)),ret,Z

def finite_check(n,m,fault=None):
 e,r,z=reconstruct(n,m,fault);q=F(2,3);p=F(1,9);zz=F(25,8)-2*q**n-p**m/8
 moment=lambda t,k:sum(j*t**j for j in range(1,k+1))
 ee=1+2*n+2*(moment(p,m)-moment(q,n))/zz
 assert (e,r,z)==(ee,1/(2*zz),zz),'mathematical family identity'

def audit(v):
 assert v['result_id']=='K1960','identity'
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'pin'
 for row in v['vertices']:
  n=row['n'];q=F(2,3);z=F(25,8)-2*q**n
  left=6-(2*n+6)*q**n;right=F(9,64)
  E=1+2*n+2*(right-left)/z;R=1/(2*z)
  assert E==F(row['energy']) and R==F(row['return_cost']),'vertex identity'
 for mix in v['mixtures']:
  e,r,_=reconstruct(*mix['left']);f,t,_=reconstruct(*mix['right']);a=F(mix['weight']);shift=F(mix['shift'])
  assert F(mix['energy'])==a*e+(1-a)*(f+shift),'mixture shift cost'
  assert F(mix['return_cost'])==a*r+(1-a)*t,'block trace-norm sum'

def main():
 v=json.loads(OUT.read_text());audit(v);count=0
 for n in range(26):
  for m in range(19):finite_check(n,m);count+=1
 n,x=s.symbols('n x');W=s.Rational(25,8)
 E=lambda n,x:2*n-s.Rational(11,4)+(4*n+s.Rational(9,2))*x/(W-2*x)
 R=lambda x:1/(2*(W-2*x))
 assert s.factor((R(2*x/3)-R(x))/(E(n+1,2*x/3)-E(n,x))+2*x/(W*(12*W-(8*n+33)*x)))==0
 # Exact asymptotic coefficients by rational differentiation at x=0.
 assert s.diff(R(x),x).subs(x,0)==s.Rational(64,625)
 assert E(n,0)-2*n==-s.Rational(11,4)
 for fault in ['left_ratio','energy_origin','return_factor']:
  try:finite_check(3,4,fault)
  except AssertionError as e:assert str(e)=='mathematical family identity'
  else:raise AssertionError('undetected '+fault)
 bad=copy.deepcopy(v);bad['mixtures'][0]['shift']=str(F(bad['mixtures'][0]['shift'])+F(1,100))
 try:audit(bad)
 except AssertionError as e:assert str(e)=='mixture shift cost'
 else:raise AssertionError('undetected shift energy')
 for f in ['identity','pin']:
  bad=copy.deepcopy(v)
  if f=='identity':bad['result_id']='bad'
  else:bad['inputs'][next(iter(bad['inputs']))]='bad'
  try:audit(bad)
  except AssertionError as e:assert str(e)==f
  else:raise AssertionError('undetected metadata')
 print('PASS independent K1960',count,'recurrences, symbolic chord/asymptotics; four mathematical and two metadata faults')
if __name__=='__main__':main()
