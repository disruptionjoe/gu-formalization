"""K1952: collapsed-tail global certificates and exact energy consumers."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import sys,json,warnings

from k1943_arbitrary_preparation_catalyst_energy import canonical_paths,cell
from scipy.optimize import linprog
import numpy as np
from sage.all import QQ,matrix,vector
warnings.filterwarnings('ignore',message='Unrecognized options detected')
def entries(K):
 for S in canonical_paths(K):
  yield S,False
  ds=[b-a for a,b in zip(S,S[1:])]
  for d in (1,2,3):
   if (ds and ds[-1]+d<4) or (not ds and max(1,3-d)!=S[0]):continue
   if S[-1]+d>K:yield S+[S[-1]+d],True
 # first gap1 canonical offset2, not emitted by singleton1.
 if K<3:raise ValueError('use K>=3')
def opt(t,b,S,o,tail):
 A,rhs,c,eq=cell(t,S,F(0),o);A=A[:-1];n=len(S)
 if tail:A=A[:-1]
 c=[b*S[i] if i<n else (F(0) if tail and i==2*n-1 else F(1,2)) for i in range(2*n)]
 ans=linprog(np.array(c,float),A_ub=np.array(A,float),b_ub=np.zeros(len(A)),A_eq=[np.array(eq,float)],b_eq=[1.],bounds=(0,None),method='highs-ds',options={'threads':1});assert ans.success
 # Solver support determines an exact rational linear system, never rounded acceptance.
 ix=[j for j,z in enumerate(ans.x) if z>1e-9];iy=[i for i,z in enumerate(ans.ineqlin.marginals) if z < -1e-9]
 ia=[i for i,z in enumerate(ans.ineqlin.residual) if abs(z)<1e-8]
 primal=matrix(QQ,[[eq[j] for j in ix]]+[[A[i][j] for j in ix] for i in ia]).solve_right(vector(QQ,[1]+[0]*len(ia)))
 xf=[F(0)]*(2*n)
 for j,z in zip(ix,primal):xf[j]=F(str(z))
 jx=[j for j,z in enumerate(ans.lower.marginals) if abs(z)<1e-8]
 dual=matrix(QQ,[[eq[j]]+[A[i][j] for i in iy] for j in jx]).solve_right(vector(QQ,[c[j] for j in jx]))
 af=F(str(dual[0]));yf=[F(0)]*len(A)
 for i,z in zip(iy,dual[1:]):yf[i]=F(str(z))
 x=list(map(str,xf));y=list(map(str,yf));a=str(af)
 dot=lambda x,y:sum(a*b for a,b in zip(x,y))
 assert min(xf)>=0 and dot(eq,xf)==1 and all(dot(r,xf)<=0 for r in A)
 assert max(yf)<=0 and all(c[j]-af*eq[j]-sum(A[i][j]*yf[i] for i in range(len(A)))>=0 for j in range(2*n)), (S,o,tail,a,x,y,[str(c[j]-af*eq[j]-sum(A[i][j]*yf[i] for i in range(len(A)))) for j in range(2*n)])
 assert dot(c,xf)==af
 return dict(support=S,orientation=list(o),tail=tail,x=x,y=y,intercept=a)

from k1950_global_catalyst_energy_certificates import rank
from k1943_arbitrary_preparation_catalyst_energy import rate,shell_witness
import hashlib,argparse
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1952-catalyst-path-energy-extension.json'
POINTS=[([1,3,5],[F(3,8),F(9,16),F(1,16)]),([1,3,5,7],[F(54,145),F(81,145),F(9,145),F(1,145)]),([1,3,5,7,9],[F(243,653),F(729,1306),F(81,1306),F(9,1306),F(1,1306)]),([1,3,5,7,9],[F(36,181),F(54,181),F(81,181),F(9,181),F(1,181)])]
SPECS=[(F(9,148),10,F(63,148)),(F(81,1912),12,F(729,1912)),(F(2907,69200),12,F(1053,2768))]
def arrays(s,o,t,b,tail):
 A,rhs,c,eq=cell(t,s,F(0),o);A=A[:-1];n=len(s)
 if tail:A=A[:-1]
 c=[b*s[i] if i<n else (F(0) if tail and i==2*n-1 else F(1,2)) for i in range(2*n)]
 return A,c,eq

def validate(bank):
 count=0
 for cert,(b,K,a) in zip(bank,SPECS):
  assert (F(cert['slope']),cert['cutoff'],F(cert['intercept']))==(b,K,a),'global certificate identity'
  expected={(tuple(s),o,tail) for s,tail in entries(K) for o in product([-1,1],repeat=len(s)-1)}
  actual=[(tuple(r['support']),tuple(r['orientation']),r['tail']) for r in cert['cells']]
  assert len(actual)==len(set(actual)) and set(actual)==expected,'complete finite and crossing-prefix census'
  for rec in cert['cells']:
   s=rec['support'];n=len(s);A,c,eq=arrays(s,rec['orientation'],F(cert['t']),b,rec['tail']);x=list(map(F,rec['x']));y=list(map(F,rec['y']));v=F(rec['intercept']);dot=lambda x,y:sum(a*b for a,b in zip(x,y))
   assert min(x)>=0 and dot(eq,x)==1 and all(dot(r,x)<=0 for r in A),'primal'
   assert max(y)<=0,'dual signs'
   slack=[c[j]-v*eq[j]-sum(A[i][j]*y[i] for i in range(len(A))) for j in range(2*n)]
   assert min(slack)>=0 and dot(c,x)==v>=a,'exact dual domination and equality'
   if b==SPECS[2][0] and v==a:
    act=[eq]+[r for r,z in zip(A,y) if z<0]+[[F(int(i==j)) for i in range(2*n)] for j,z in enumerate(slack) if z>0]
    r0=rank(act)
    assert all(rank(act+[[F(int(i==j)) for i in range(2*n)]])==r0 for j in range(n)),'unique equality population'
    occupied=[(e,w) for e,w in zip(s,x) if w]
    assert occupied in [list(zip(*pt)) for pt in POINTS[2:]],'only two transition equality preparations'
    if rec['tail']:assert x[n-1]==0,'no equality tail mass'
    count+=3
   count+=4
  count+=2
 return count

def consumers():
 out=[];count=0
 for k in range(2):
  b,K,a=SPECS[k];s=POINTS[k+1][0];p0=POINTS[k][1]+[F(0)];p1=POINTS[k+1][1]
  for theta in [F(0),F(1,3),F(2,3),F(1)]:
   p=[(1-theta)*x+theta*y for x,y in zip(p0,p1)];E=sum(e*w for e,w in zip(s,p));r,n=shell_witness(F(1,2),s,p,list(range(s[-1]+4)))
   assert r==a-b*E,'attained segment'
   out.append(dict(kind='attained',segment=k,support=s,weights=list(map(str,p)),energy=str(E),return_cost=str(r)));count+=n+1
 # Infimum on transition, with nondegenerate physical approximations at E=3.
 s,pA=POINTS[2];_,pB=POINTS[3];EA=sum(e*w for e,w in zip(s,pA));EB=sum(e*w for e,w in zip(s,pB));E=F(3);w=(EB-E)/(EB-EA);b,K,a=SPECS[2];target=a-b*E
 for eps in [F(1,100),F(1,1000)]:
  scale=(E-1)/(E-1+(2-w)*eps);support=[F(1)]+[F(e)+eps for e in s]+[F(e)+2*eps for e in s];p=[1-scale]+[scale*w*x for x in pA]+[scale*(1-w)*x for x in pB]
  physical=sorted({F(0),F(1),F(2)}|{F(j)+i*eps for i in [1,2] for j in range(13)})
  r,n=shell_witness(F(1,2),support,p,physical);actualE=sum(e*x for e,x in zip(support,p))
  assert actualE==E and r==scale*target+(1-scale)/2 and r>target,'finite exact-energy near-minimizer'
  out.append(dict(kind='infimum_approximation',support=list(map(str,support)),weights=list(map(str,p)),energy=str(E),return_cost=str(r),infimum=str(target),epsilon=str(eps),physical_spectrum=list(map(str,physical))));count+=n+1
 return out,count

def produce(discover=False):
 if discover:
  banks=[]
  for b,K,a in SPECS:
   rows=[opt(F(1,2),b,s,o,tail) for s,tail in entries(K) for o in product([-1,1],repeat=len(s)-1)]
   banks.append(dict(t='1/2',slope=str(b),cutoff=K,intercept=str(min(F(r['intercept']) for r in rows)),cells=rows))
 else:banks=json.loads(OUT.read_text())['global_duals']
 checks=validate(banks);cs,n=consumers();checks+=n
 return dict(result_id='K1952',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',global_duals=banks,consumers=cs,exact_controls=checks,points=[dict(support=s,weights=list(map(str,p)),energy=str(sum(e*w for e,w in zip(s,p))),return_cost=str(rate(F(1,2),s,p)[0])) for s,p in POINTS],inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1950-global-catalyst-energy-certificates.json','tests/channel-swings/k1943_arbitrary_preparation_catalyst_energy.py']},scope='Fixed exact Schur channel, t=1/2 faithful bath, finite nondegenerate catalyst; global frontier extended through675/181. Last new interior segment not finitely attained. No native GU, novelty, expert or formal-proof claim.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--discover',action='store_true');a=p.parse_args();v=produce(a.discover)
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'report drift'
 print('PASS K1952',v['exact_controls'],'exact controls')
