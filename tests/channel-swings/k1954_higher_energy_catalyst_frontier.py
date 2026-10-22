"""Higher-energy global supporting certificates with a thermally priced tail."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib,argparse,warnings
import numpy as np
from scipy.optimize import linprog
from sage.all import QQ,matrix,vector
from k1952_catalyst_path_energy_extension import entries
from k1943_arbitrary_preparation_catalyst_energy import cell,rate,shell_witness
from k1950_global_catalyst_energy_certificates import rank
warnings.filterwarnings('ignore',message='Unrecognized options detected')
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1954-higher-energy-catalyst-frontier.json'

def arrays(s,o,t,b,tail):
 A,rhs,c,eq=cell(t,s,F(0),o);A=A[:-1];n=len(s)
 if tail:
  d=s[-1]-s[-2];H=sum(t**j for j in range(d,4))/sum(t**j for j in range(4));floor=t*t/(1+t*t)**2
  A[-1]=[F(0)]*(2*n);A[-1][n-2]=-H;A[-1][n-1]=2*floor;A[-1][-1]=-1
 c=[b*s[i] if i<n else F(1,2) for i in range(2*n)]
 return A,c,eq

def opt(t,b,s,o,tail):
 A,c,eq=arrays(s,o,t,b,tail);n=len(s)
 ans=linprog(np.array(c,float),A_ub=np.array(A,float),b_ub=np.zeros(len(A)),A_eq=[np.array(eq,float)],b_eq=[1],bounds=(0,None),method='highs-ds',options={'threads':1,'primal_feasibility_tolerance':1e-10,'dual_feasibility_tolerance':1e-10});assert ans.success
 ix=[j for j,z in enumerate(ans.x) if z>1e-12];iy=[i for i,z in enumerate(ans.ineqlin.marginals) if z < -1e-12];ia=[i for i,z in enumerate(ans.ineqlin.residual) if abs(z)<5e-11]
 pr=matrix(QQ,[[eq[j] for j in ix]]+[[A[i][j] for j in ix] for i in ia]).solve_right(vector(QQ,[1]+[0]*len(ia)));x=[F(0)]*(2*n)
 for j,z in zip(ix,pr):x[j]=F(str(z))
 jx=[j for j,z in enumerate(ans.lower.marginals) if abs(z)<5e-11]
 du=matrix(QQ,[[eq[j]]+[A[i][j] for i in iy] for j in jx]).solve_right(vector(QQ,[c[j] for j in jx]));a=F(str(du[0]));y=[F(0)]*len(A)
 for i,z in zip(iy,du[1:]):y[i]=F(str(z))
 rec=dict(support=s,orientation=list(o),tail=tail,x=list(map(str,x)),y=list(map(str,y)),intercept=str(a));check(rec,t,b,a);return rec

def check(rec,t,b,bound):
 s=rec['support'];A,c,eq=arrays(s,rec['orientation'],t,b,rec['tail']);x=list(map(F,rec['x']));y=list(map(F,rec['y']));a=F(rec['intercept']);dot=lambda u,v:sum(i*j for i,j in zip(u,v))
 assert len(x)==len(c) and len(y)==len(A),'dimensions'
 assert min(x)>=0 and dot(eq,x)==1 and all(dot(row,x)<=0 for row in A),'rational primal'
 assert max(y)<=0,'dual signs'
 slack=[c[j]-a*eq[j]-sum(row[j]*z for row,z in zip(A,y)) for j in range(len(c))]
 assert min(slack)>=0 and dot(c,x)==a>=bound,'rational dual and bound'
 return A,eq,x,y,slack

def discover(specs):
 bank=[]
 for index,spec in enumerate(specs):
  b=F(spec['slope']);a=F(spec['intercept']);K=spec['cutoff'];rows=[]
  for s,tail in entries(K):
   for o in product([-1,1],repeat=len(s)-1):rows.append(opt(F(1,2),b,s,o,tail))
  checkpoint=ROOT/'_local/k1954'/('bank-'+str(index)+'.json');checkpoint.parent.mkdir(parents=True,exist_ok=True);checkpoint.write_text(json.dumps(dict(**spec,t='1/2',cells=rows)))
  low=min(F(r['intercept']) for r in rows)
  print('BANK',str(b),'K',K,'cells',len(rows),'minimum',str(low),'target',str(a),flush=True)
  assert low==a,'cutoff tail relaxation does not yet prove bound'
  bank.append(dict(**spec,t='1/2',cells=rows))
 return bank

def validate(banks):
 count=0;faces=[]
 for bank in banks:
  b=F(bank['slope']);a=F(bank['intercept']);K=bank['cutoff'];keys=[(tuple(r['support']),tuple(r['orientation']),r['tail']) for r in bank['cells']];expected={(tuple(s),o,tail) for s,tail in entries(K) for o in product([-1,1],repeat=len(s)-1)}
  assert len(keys)==len(set(keys)) and set(keys)==expected,'complete census';eqp=[];positive_tail=False;fixed=True
  for r in bank['cells']:
   A,eq,x,y,slack=check(r,F(1,2),b,a);count+=4
   if F(r['intercept'])==a:
    n=len(r['support']);active=[eq]+[row for row,z in zip(A,y) if z<0]+[[F(int(i==j)) for i in range(2*n)] for j,z in enumerate(slack) if z>0];rk=rank(active)
    isfixed=all(rank(active+[[F(int(i==j)) for i in range(2*n)]])==rk for j in range(n));fixed &= isfixed
    pop=[(e,str(p)) for e,p in zip(r['support'],x) if p]
    if pop not in eqp:eqp.append(pop)
    if r['tail'] and x[n-1]:positive_tail=True
    count+=1
  faces.append(dict(all_equality_populations_fixed=fixed,positive_equality_tail=positive_tail,equality_populations=eqp));count+=1
 return count,faces

def interval_cells(banks):
 """Endpoint signs prove the whole affine interval, not just sampled protocols."""
 out=[]
 for bank in banks[:2]:
  s=bank['right']['support'];p0=list(map(F,bank['left']['weights']))+[F(0)];p1=list(map(F,bank['right']['weights']));ds=[];deficits=[]
  for p in [p0,p1]:
   inc=[F(0)]*len(s);edge=[]
   for i in range(len(s)-1):
    d=s[i+1]-s[i];den=sum(F(1,2)**j for j in range(4));L=sum(F(1,2)**j for j in range(4-d))/den;H=sum(F(1,2)**j for j in range(d,4))/den
    v=H*p[i]-L*p[i+1];edge.append(v);inc[i]+=max(F(0),-v);inc[i+1]+=max(F(0),v)
   ds.append(edge);deficits.append([x-y for x,y in zip(p,inc)])
  assert all(x*y>=0 for x,y in zip(*ds)) and all(x*y>=0 for x,y in zip(*deficits)),'affine edge and deficit sign-cell compatibility'
  out.append(dict(edge_sign_values=[list(map(str,r)) for r in ds],deficit_sign_values=[list(map(str,r)) for r in deficits]))
 return out

def consumers(banks):
 out=[];count=0
 for k,bank in enumerate(banks[:2]):
  s=bank['right']['support'];p0=list(map(F,bank['left']['weights']))+[F(0)];p1=list(map(F,bank['right']['weights']));a=F(bank['intercept']);b=F(bank['slope'])
  for theta in [F(0),F(1,3),F(2,3),F(1)]:
   p=[(1-theta)*x+theta*y for x,y in zip(p0,p1)];E=sum(e*w for e,w in zip(s,p));r,n=shell_witness(F(1,2),s,p,list(range(s[-1]+4)))
   assert r==a-b*E,'attained segment physical channel'
   out.append(dict(kind='attained',segment=k,support=s,weights=list(map(str,p)),energy=str(E),return_cost=str(r)));count+=n+1
 # Exact finite counterexample to the tempting C-to-D secant from the cutoff14 hull.
 support=list(range(1,16,2));weights=[26244,39366,59049,6561,729,81,9,1];p=[F(w,sum(weights)) for w in weights];E=sum(e*w for e,w in zip(support,p))
 r,n=shell_witness(F(1,2),support,p,list(range(19)));candidate=F(31271,107400)-F(1943,107400)*E
 assert F(54787,14671)<E<F(4781,923) and r<candidate,'physical counterexample to finite-window secant extrapolation'
 out.append(dict(kind='rejected_secant_counterexample',support=support,weights=list(map(str,p)),energy=str(E),return_cost=str(r),rejected_line_return=str(candidate),gap=str(candidate-r),physical_spectrum=list(range(19))));count+=n+1
 return out,count

def render_report(v):
 # One certificate per line keeps the exact bank reviewable without huge indentation.
 dump=lambda x:json.dumps(x,separators=(',',':'))
 banks=[]
 for bank in v['global_duals']:
  header=dump({k:x for k,x in bank.items() if k!='cells'})[:-1]
  banks.append(header+',"cells":[\n'+',\n'.join(dump(r) for r in bank['cells'])+'\n]}')
 return '{\n'+',\n'.join(dump(k)+':'+('['+',\n'.join(banks)+']' if k=='global_duals' else dump(x)) for k,x in v.items())+'\n}\n'

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--discover',type=Path);p.add_argument('--write',action='store_true');a=p.parse_args()
 if a.discover:
  banks=discover(json.loads(a.discover.read_text()));v=dict(result_id='K1954',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',global_duals=banks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1952-catalyst-path-energy-extension.json','tests/channel-swings/k1943_arbitrary_preparation_catalyst_energy.py','lab/process/k1935-arbitrary-support-thermal-return.json']})
 else:v=json.loads(OUT.read_text())
 n,faces=validate(v['global_duals']);v['equality_faces']=faces
 v['interval_cells']=interval_cells(v['global_duals']);v['consumers'],nc=consumers(v['global_duals']);v['exact_controls']=n+nc
 v['scope']='Fixed Schur channel, t=1/2, exact conservation, marginal return; arbitrary finite nondegenerate catalysts. Two sharp segments through54787/14671, attained throughout. A physical eight-site counterexample rejects the cutoff14 hull secant to4781/923; higher frontier remains open. No GU physics or novelty claim.'
 if a.write:OUT.write_text(render_report(v))
 print('PASS K1954',n,'exact finite certificate controls;',nc,'physical controls;',sum(len(b['cells']) for b in v['global_duals']),'cells',flush=True);print('FACES',faces,flush=True)
