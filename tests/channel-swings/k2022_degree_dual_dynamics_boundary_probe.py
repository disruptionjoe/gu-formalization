"""Separate raw coefficient action and inherited Jordan-chain replay."""
from k2021_common_degree_dual_operator_probe import *
def mass_columns(coeff=None):
 cols=[{} for _ in range(N)]
 for k in range(14):
  a,c=(Q(-5301,23168),Q(7559,23168)) if k in [0,7,8,9] else (Q(-594,23168),Q(198,23168))
  if coeff is not None:a,c=(coeff[0],coeff[2]) if k in [0,7,8,9] else (coeff[1],coeff[3])
  om=[]
  for j in range(N):
   block,b=divmod(j,128);v=word(tuple(range(14)),b)[1];i,s=gam(k,b)
   om.append({128*block+i:eta[k]*s*(a+c*v)})
  dk=dmatrix(k);dk=[{i:v for i,v in z.items() if i<1792} for z in dk]
  cols=plus(cols,compose(dk,om))
 for j in range(128):
  v=word(tuple(range(14)),j)[1];i,s=gam(0,j);cols[j][1792+i]=-s*Q(3-5*v,4)
 return cols

def run():
 k=mass_columns();h=hmatrix();hk=compose(h,k);df=plus(hk,transpose(hk),-1)
 report=json.loads((ROOT/'lab/process/k2022-degree-dual-dynamics-boundary.json').read_text());md=report['mass_defect']
 assert sum(map(len,df))==md['entries'];assert sum(sum(i<1792 for i in col) for col in df[:1792])==md['upper_entries']
 i,j,s=md['witness'];assert df[j][i]==Q(s)==-Q(9,4)
 # Upper-only defect is unaffected by any changed lower-return row.
 assert any(i<1792 for col in df[:1792] for i in col)
 for x in [Q(1,3),Q(-2,5)]:
  c=cmat(x);ct=transpose(c);dq=compose(ct,compose(df,c));assert not empty(dq)
  cq=compose(ct,compose(hk,c));assert dq==plus(cq,transpose(cq),-1)
 defects=[]
 for coeff in [(Q(1),Q(0),Q(-3),Q(0)),(Q(0),Q(1),Q(4172,297),Q(-1,3))]:
  z=compose(h,mass_columns(coeff));d=plus(z,transpose(z),-1)
  defects.append([{i:v for i,v in col.items() if i<1792} for col in d[:1792]])
 assert defects[0][159][0]==24 and defects[1][159][0]==-Q(4172,33)
 for a,b in zip(*defects):
  assert {i:v*Q(-1043,198) for i,v in a.items()}==b
 scalar=report['full_upper_preserving_scalar_class'];assert scalar['rank']==1
 assert list(map(Q,scalar['upper_adjoint_survivor']))==[Q(1043,198),Q(1),Q(-1043,594),-Q(1,3)]
 # Independent exact nonzero determinant of the two necessary scalar constraints.
 assert Q(5301,594)-Q(1043,198)==Q(362,99)
 assert scalar['intersection']=='zero_only'
 base=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())
 for row in base['blocks']:
  n=len(row['jordan_u']);u=list(map(Q,row['jordan_u']));v=list(map(Q,row['jordan_v']));a=row['generators'][0]['entries']
  def act(z):
   out=[Q(0)]*n
   for i,j,s in a:out[i]+=Q(s)*z[j]
   return out
  assert act(u)==u and [a-b for a,b in zip(act(v),v)]==u and any(u)
  wrong=u.copy();wrong[next(i for i,x in enumerate(wrong) if x)]+=1
  assert [a-b for a,b in zip(act(v),v)]!=wrong
 for p,d in report['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d
 print('PASS K2022 independent full mass defect, 2 congruences, 32 Jordan chains, 32 actual chain faults; 3 provenance hashes')
if __name__=='__main__':run()
