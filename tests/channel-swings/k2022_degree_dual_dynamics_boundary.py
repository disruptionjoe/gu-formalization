"""Common-dual mass defect and transported full-carrier Jordan obstruction."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse
from k2021_common_degree_dual_operator import add,mul,tr,I,ETA,gamma,blade,J,B,H,raw,data,blockdiag
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2022-degree-dual-dynamics-boundary.json'
def decode(a):return {(i,j):F(v) for i,j,v in a['entries']}
def vector(a,v):
 z=[F(0)]*len(v)
 for (i,j),x in a.items():z[i]+=x*v[j]
 return z

def mass(coeff=None):
 k={}
 for i in range(14):
  a,c=(F(-5301,23168),F(7559,23168)) if i in [0,7,8,9] else (F(-594,23168),F(198,23168))
  if coeff is not None:a,c=(coeff[0],coeff[2]) if i in [0,7,8,9] else (coeff[1],coeff[3])
  om=mul(gamma(i),add((a,I),(c,J)));om=add((ETA[i],om))
  upper={(r,s):v for (r,s),v in raw(i).items() if r<1792}
  k=add((1,k),(1,mul(upper,blockdiag([om]*15))))
 b0=mul(gamma(0),add((F(3,4),I),(F(-5,4),J)))
 k.update({(1792+i,j):-v for (i,j),v in b0.items()})
 return k

def produce():
 k=mass();defect=add((1,mul(H,k)),(-1,mul(tr(k),H)));assert defect
 upper={ij:v for ij,v in defect.items() if max(ij)<1792};assert upper
 example=min(upper);checks={};rows=[]
 defects=[]
 for coeff in [(F(1),F(0),F(-3),F(0)),(F(0),F(1),F(4172,297),F(-1,3))]:
  kk=mass(coeff);dd=add((1,mul(H,kk)),(-1,mul(tr(kk),H)))
  defects.append({ij:v for ij,v in dd.items() if max(ij)<1792})
 keys=sorted(set(defects[0])|set(defects[1]));first=next(ij for ij in keys if defects[0].get(ij,0) or defects[1].get(ij,0));v=(defects[0].get(first,F(0)),defects[1].get(first,F(0)))
 second=next((ij for ij in keys if v[0]*defects[1].get(ij,0)-v[1]*defects[0].get(ij,0)),None)
 scalar=dict(rank=2 if second is not None else 1,rows=[[list(first),list(map(str,v))]])
 if second is not None:
  w=(defects[0].get(second,F(0)),defects[1].get(second,F(0)));scalar['rows'].append([list(second),list(map(str,w))]);scalar['determinant']=str(v[0]*w[1]-v[1]*w[0])

 assert second is None and v==(F(24),F(-4172,33))
 assert all(F(24)*defects[1].get(ij,0)+F(4172,33)*defects[0].get(ij,0)==0 for ij in keys)
 survivor=[F(1043,198),F(1),F(-1043,594),F(-1,3)]
 positive=[F(5301,594),F(1),F(-7559,594),F(-1,3)]
 assert survivor[0]-positive[0]==F(-362,99)
 scalar.update(upper_adjoint_survivor=list(map(str,survivor)),inherited_positive_conservation_line=list(map(str,positive)),intersection='zero_only',constraint_difference=str(survivor[0]-positive[0]),scope='Complete K1967 upper-preserving four-scalar class, this fixed H and inherited core energy; arbitrary lower return cannot change the upper defect. Upper-adjoint survivor alone is not a claimed full completion.')

 for x in [F(0),F(1,3),F(-2,5)]:
  c,ci,cp=data(x);h=mul(mul(tr(c),H),c);kq=mul(mul(ci,k),c)
  dq=add((1,mul(h,kq)),(-1,mul(tr(kq),h)));want=mul(mul(tr(c),defect),c)
  assert dq==want and dq
  rows.append(dict(x=str(x),defect_nonzero_entries=len(dq)))
 base=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text());chains=[]
 for ix,bl in enumerate(base['blocks']):
  a=decode(bl['generators'][0]);v=list(map(F,bl['jordan_v']));u=list(map(F,bl['jordan_u']));av=vector(a,v);au=vector(a,u)
  assert any(u) and [x-y for x,y in zip(av,v)]==u and au==u
  # A genuine defective Jordan chain: exp(-iz A)v=e^-iz(v-iz u).
  assert vector(a,u)==u
  chains.append(dict(block=ix,dimension=len(v),u_squared_norm=str(sum(x*x for x in u)),v_squared_norm=str(sum(x*x for x in v))))
 assert len(chains)==32
 # Cancellation under every differentiable invertible U is algebraic:
 # d(U^-1 J psi)=-U^-1(dU)U^-1 J psi+U^-1 J dpsi.
 # Validate on nonconstant rational q example using inverse derivative.
 cancellation=[]
 for x in [F(0),F(1,3),F(-2,5)]:
  c,ci,cp=data(x);cip=add((-1,mul(mul(ci,cp),ci)))
  assert add((1,mul(cp,ci)),(1,mul(c,cip)))=={}
  cancellation.append(str(x))
 inputs=['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','lab/process/k2021-common-degree-dual-operator.json']
 return dict(full_upper_preserving_scalar_class=scalar,result_id='K2022',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',mass_defect=dict(entries=len(defect),upper_entries=len(upper),witness=[*example,str(upper[example])]),moving_congruence=rows,jordan_chains=chains,inverse_derivative_controls=cancellation,scope='New composition on the supplied degree-dual class; no positive full evolution, no common-form realization of the fixed K1967 mass, inherited positive invariant core survives with transported observation. No GU verdict.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text())
 print('PASS K2022',len(z['jordan_chains']),'Jordan chains',z['mass_defect'])
