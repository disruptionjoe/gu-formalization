"""Independent population recurrence and symbolic tail/price identities."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib
import sympy as sy
ROOT=Path(__file__).resolve().parents[2];v=json.loads((ROOT/'lab/process/k1962-finite-tail-thermal-improvement.json').read_text())

def native(n,m,fault=None):
 left=[F(1)]
 for j in range(n):left.insert(0,left[0]*F(2,3))
 w=left.copy()
 for j in range(m):w.append(w[-1]*(F(1,8) if fault=='tail_ratio' else F(1,9)))
 S=[1+2*i for i in range(len(w))];Z=sum(w);p=[x/Z for x in w]
 incoming=[F(0)]*len(w)
 for i in range(len(w)-1):
  # Reconstruct occupied bath-label weights for gap2 at t=1/2: H=1/5,L=4/5.
  d=p[i]/5-4*p[i+1]/5
  incoming[i]+=max(F(0),-d);incoming[i+1]+=max(F(0),d)
 r=sum(max(F(0),x-y) for x,y in zip(p,incoming))/2
 E=sum(x*y for x,y in zip(S,p))
 if fault=='energy_origin':E-=1
 if fault=='return_normalization':r*=2
 return E,r,Z

def verify(fault=None):
 count=0
 for row in v['witnesses']:
  n,m=row['n'],row['m'];E,R,Z=native(n,m,fault)
  assert E==F(row['energy']) and R==F(row['return_cost']),'independent actual populations/deficit'
  q=F(2,3);z=F(25,8)-2*q**n;en=2*n-F(11,4)+(4*n+F(9,2))*q**n/z;rn=1/(2*z)
  zm=F(25,8)-2*q**(n-1);em=2*(n-1)-F(11,4)+(4*(n-1)+F(9,2))*q**(n-1)/zm;rm=1/(2*zm)
  chord=rn+(rm-rn)*(en-E)/(en-em)
  assert chord-R==F(row['gap'])>0 and em<=E<en,'strict polygon improvement';count+=2
 for row in v['priced_family_optima']:
  lam=F(row['price']);n=row['n'];m=row['m'];E,R,Z=native(n,m)
  assert E==F(row['energy']) and R==F(row['return_cost']) and R+lam*E==F(row['value']),'priced winner values'
  # Independent exhaustive recurrence over each proved n range until first append reverses.
  for j in range(row['n_cutoff']+1):
   k=0;ee,rr,_=native(j,k);prev=rr+lam*ee
   while True:
    k+=1;ee,rr,_=native(j,k);cur=rr+lam*ee
    assert prev>=F(row['value']),'independent price minimum'
    count+=1
    if cur>=prev:break
    prev=cur
  assert F(4,25)+lam*(2*(row['n_cutoff']+1)-3)>F(1,2)+lam,'all larger root indices excluded'
 return count
print('PASS independent K1962',verify(),'exact population/price comparisons')
for f in ['tail_ratio','energy_origin','return_normalization']:
 try:verify(f)
 except AssertionError as e:print('CAUGHT mathematical input',f,str(e))
 else:raise AssertionError('undetected '+f)
z,h,e,B,lam=sy.symbols('z h e B lam',nonzero=True)
fm=(sy.Rational(1,2)+lam*(z*e-h*B))/(z-h);fi=1/(2*z)+lam*e
assert sy.simplify(fi-fm-h/(z-h)*(lam*B-fi))==0
assert sy.simplify((lam*(B-sy.Rational(1,4))-fm)*(z-h)-(z*(lam*(B-sy.Rational(1,4))-fi)+lam*h/4))==0
# Incorrect missing normalization must fail the symbolic identity, not crash.
bad=(sy.Rational(1,2)+lam*(z*e-h*B))/z
assert sy.simplify(fi-bad-h/(z-h)*(lam*B-fi))!=0
print('CAUGHT mathematical input missing_tail_normalization; PASS two symbolic identities')
assert v['result_id']=='K1962'
for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'dependency pin'
print('PASS report identity/pins; universal conclusions rely on the analytic proof')
