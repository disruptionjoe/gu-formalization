"""Finite-tail improvements and exact priced optimization within rooted families."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json
from k1960_thermal_frontier_convexification import family,vertex,slope,Q,P,W
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1962-finite-tail-thermal-improvement.json'

def priced(n,lam):
 """First nondecreasing append is a global right-arm minimum for this n."""
 m=0
 while True:
  _,_,E,R,Z=family(n,m);f=R+lam*E
  if lam*(2*n+2*m+3)>=f:return m,E,R,f
  m+=1

def optimize(lam):
 # E_nm>=2n-3, R_nm>4/25. Bounds n in every winning family.
 cutoff=int(2+F(17,100)/lam)+1
 rows=[(priced(n,lam)[3],n,*priced(n,lam)[:3]) for n in range(cutoff+1)]
 return min(rows),cutoff

def produce():
 from k1943_arbitrary_preparation_catalyst_energy import rate
 from k1939_physical_catalyst_resource_frontier import shell_witness
 count=0;physical=0;witnesses=[]
 for n in range(1,9):
  En,Rn=vertex(n);El,_=vertex(n-1);Z=W-2*Q**n;s=slope(n-1)
  # Choose m analytically beyond the price threshold, then ensure chord membership.
  m=max(1,int((En+1/(2*Z*(-s))-2*n-F(13,4))/2)+1)
  while family(n,m)[2]<El:m+=1
  _,p,E,R,z=family(n,m);h=P**m/8;B=2*n+2*m+F(13,4)
  gap=h/(Z-h)*((-s)*(B-En)-1/(2*Z))
  assert E>=El and E<En and gap>0,'finite-tail chord improvement'
  assert gap==Rn+s*(E-En)-R,'exact improved return';count+=2
  witnesses.append(dict(n=n,m=m,energy=str(E),return_cost=str(R),gap=str(gap)))
 for n in range(12):
  En,Rn=vertex(n);Z=W-2*Q**n
  for m in range(12):
   S,p,E,R,z=family(n,m);h=P**m/8;B=2*n+2*m+F(13,4)
   assert En-E==h*(B-En)/(Z-h),'tail first moment'
   assert R-Rn==h/(2*Z*(Z-h)),'tail return difference'
   assert E>=2*n-3 and R>F(4,25),'root index lower bound'
   assert R==rate(F(1,2),S,p)[0],'actual deficit return';count+=4
 prices=[]
 for lam in [F(1,4),F(1,10),F(1,25),F(1,50),F(1,100)]:
  best,cut=optimize(lam);f,n,m,E,R=best
  for j in range(cut+1):
   k,e,r,v=priced(j,lam)
   for z in range(max(12,k+5)):
    _,_,ee,rr,_=family(j,z);assert rr+lam*ee>=v,'all checked tails above exact optimizer';count+=1
   assert lam*(2*j+2*k+3)>=v,'stopping inequality';count+=1
  prices.append(dict(price=str(lam),n=n,m=m,energy=str(E),return_cost=str(R),value=str(f),n_cutoff=cut))
 # Distinct newly relevant finite witnesses, including n3,m4 beyond earlier sharp facets.
 for n,m in [(3,4),(4,8)]:
  S,p,E,R,z=family(n,m);actual,k=shell_witness(F(1,2),S,p,list(range(S[-1]+4)))
  assert actual==R,'full complex finite physical shell realization';physical+=k
 return dict(result_id='K1962',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',exact_controls=count,physical_shell_controls=physical,witnesses=witnesses,priced_family_optima=prices,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1960-thermal-frontier-convexification.json','lab/process/k1958-sharp-thermal-energy-rate.json']},scope='Every limiting root vertex has finite-tail improvements; priced optimum only within the rooted family, not all finite spectra.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text()),'report mismatch'
 print('PASS K1962',r['exact_controls'],'exact',r['physical_shell_controls'],'physical',flush=True)
