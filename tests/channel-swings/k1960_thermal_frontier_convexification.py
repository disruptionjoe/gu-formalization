"""Exact controls for physical convexification and the rooted-family upper envelope."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1960-thermal-frontier-convexification.json'
Q=F(2,3);P=F(1,9);W=F(25,8)

def family(n,m):
 raw=[Q**(n-i) if i<=n else P**(i-n) for i in range(n+m+1)];Z=sum(raw);p=[x/Z for x in raw];s=list(range(1,2*(n+m)+2,2));E=sum(x*y for x,y in zip(s,p));R=1/(2*Z)
 return s,p,E,R,Z

def vertex(n):
 x=Q**n;Z=W-2*x
 return F(2*n)-F(11,4)+(4*n+F(9,2))*x/Z,1/(2*Z)

def slope(n):return -2/(W*(12*W/Q**n-(8*n+33)))

def produce():
 from k1943_arbitrary_preparation_catalyst_energy import rate
 from k1939_physical_catalyst_resource_frontier import shell_witness
 count=0;physical=0
 for n in range(20):
  last=F(0);er,rr=vertex(n)
  for m in range(12):
   s,p,E,R,Z=family(n,m)
   assert Z==W-2*Q**n-F(1,8)*P**m,'asymmetric normalization'
   assert R==rate(F(1,2),s,p)[0],'actual return objective'
   assert E<er and R>rr and E>last,'finite right-tail approach';last=E;count+=3
  e1,r1=vertex(n+1)
  assert e1>er and r1<rr and (r1-rr)/(e1-er)==slope(n),'exact chord slope'
  assert slope(n)<slope(n+1)<0,'strict convexity of root vertices'
  count+=2
 # Actual physical shifted direct sum, both components finite and nondegenerate.
 mixtures=[]
 for n,m,j,k,alpha,shift in [(0,1,1,1,F(2,5),F(1,100)),(1,2,2,1,F(3,7),F(1,1000))]:
  s,p,E,R,_=family(n,m);t,w,Fen,S,_=family(j,k)
  a=list(range(s[-1]+4));b=[F(i)+shift for i in range(t[-1]+4)]
  support=list(map(F,s))+[F(x)+shift for x in t];weights=[alpha*x for x in p]+[(1-alpha)*x for x in w]
  assert len(set(a+b))==len(a+b),'nondegenerate shifted catalyst'
  assert all((x-y).denominator!=1 for x in a for y in b),'disjoint resonance classes'
  actual,nc=shell_witness(F(1,2),support,weights,a+b)
  expected=alpha*R+(1-alpha)*S
  assert actual==expected,'actual mixture all-input return'
  energy=sum(x*y for x,y in zip(support,weights));assert energy==alpha*E+(1-alpha)*(Fen+shift),'shift energy cost'
  physical+=nc;count+=4
  mixtures.append(dict(left=[n,m],right=[j,k],weight=str(alpha),shift=str(shift),energy=str(energy),return_cost=str(expected)))
 vertices=[dict(n=n,energy=str(vertex(n)[0]),return_cost=str(vertex(n)[1]),next_slope=str(slope(n))) for n in range(21)]
 return dict(result_id='K1960',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=count,physical_shell_controls=physical,vertices=vertices,mixtures=mixtures,constants={'q':str(Q),'p':str(P),'W':str(W),'energy_offset':'-11/4','excess_coefficient':'64/625','upper_envelope':'(64/625)*(2/3)^(11/8-theta)*(1-theta/3)','theta_max':'3-1/log(3/2)','scope':'upper envelope only; not a global asymptotic equality'},inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1956-finite-energy-thermal-gap.json','lab/process/k1958-sharp-thermal-energy-rate.json','lab/process/k1954-higher-energy-catalyst-frontier.json']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text()),'report mismatch'
 print('PASS K1960',r['exact_controls'],'exact,',r['physical_shell_controls'],'physical shell controls')
