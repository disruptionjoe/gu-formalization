"""Exact finite controls for the analytic sharp mean-energy exponent."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse,hashlib,json
from k1956_finite_energy_thermal_gap import matrix_d,solve,root_family
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1958-sharp-thermal-energy-rate.json'
W=F(25,8);q=F(2,3);c=F(163,440);C=F(36)

def calculate():
 count=0;mom=F(0)
 for n in range(1,6):
  for gaps in product((1,2,3),repeat=n-1):
   if any(x+y<4 for x,y in zip(gaps,gaps[1:])):continue
   e=[max(1,3-gaps[0]) if gaps else 1]
   for d in gaps:e.append(e[-1]+d)
   for bits in product((-1,1),repeat=n-1):
    D=matrix_d(gaps,bits);cols=[solve(D,[F(i==j) for i in range(n)]) for j in range(n)];w=list(map(sum,cols))
    for j,col in enumerate(cols):
     assert all(x>=0 for x in col),'resolvent positivity'
     for i,x in enumerate(col):assert x<=q**abs(i-j),'entrywise geometric envelope'
     displacement=sum(abs(e[i]-e[j])*x for i,x in enumerate(col));mom=max(mom,displacement)
     assert displacement<=C,'uniform first displacement moment'
     count+=n+2
    # Arbitrary population and orientation: positive/negative deficits both retained.
    p=[F(i+1,n*(n+1)//2) for i in range(n)];v0=[sum(D[i][j]*p[j] for j in range(n)) for i in range(n)]
    u=[max(x,0) for x in v0];v=[max(-x,0) for x in v0];m=sum(u);h=W*m-1
    deficit=sum((W-w[i])*u[i] for i in range(n));negative=sum(w[i]*v[i] for i in range(n))
    assert h==deficit+negative and h>=0,'exact slack accounting'
    E=sum(x*y for x,y in zip(e,p))
    for cap in (F(1),F(5,2),F(e[-1]+1)):
     f=[min(x,cap) for x in e]
     assert E>=W*sum(x*y for x,y in zip(f,u))-C*m-cap*h,'capped energy inequality'
     count+=1
    count+=1
 families=[]
 for n in (1,2,4,8,16,32,64):
  support,p,E,R,Z=root_family(n);eps=R-F(4,25)
  assert eps>0 and eps<=F(17,50)*q**n,'physical family return bound'
  assert E<=2*n+F(41,32),'physical family energy bound'
  families.append(dict(n=n,energy=str(E),excess=str(eps)))
 assert C==6*q/(1-q)**2,'geometric first moment sum'
 return dict(result_id='K1958',status='active_research',scope='Fixed t=1/2 exact channel, independent registers, finite nondegenerate nonnegative catalyst spectrum; worst-input marginal return.',constants={'W':str(W),'q':str(q),'c':str(c),'displacement_bound':str(C),'sharp_log_coefficient':'2/log(3/2)'},exact_controls=count+15,largest_sample_displacement=str(mom),families=families,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1935-arbitrary-support-thermal-return.json','lab/process/k1943-arbitrary-preparation-catalyst-energy.json','lab/process/k1956-finite-energy-thermal-gap.json']})
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();r=calculate()
 if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text()),'report mismatch'
 print('PASS K1958 exact supporting controls',r['exact_controls'])
