"""Independent signed-bit Clifford and restricted-row replay of the even certificate."""
from pathlib import Path
import json,hashlib,copy
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,diagonal_matrix,prod
from k1951_coordinated_zero_southeast_principal_probe import gamma,mat
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1959-full-direction-even-connection.json'

def setup():
 g=gamma();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);eta=[1]*7+[-1]*7;om=prod(g);W=(3*I-om)/2;Wi=(3*I+om)/4
 def D(k):return block_matrix([[eta[r]*g[r]*g[k]*g[c]*W if r!=k and c not in (r,k) else Z for c in range(14)]+[I if r==k else Z] for r in range(14)]+[[-eta[c]*I if c==k else Z for c in range(14)]+[Z]],sparse=True)
 p=[[Z]*15 for _ in range(15)];p[0][14]=-I;p[14][0]=I
 for r in range(1,14):
  for c in range(1,14):p[r][c]=Wi*eta[r]*g[r]*g[0]*g[c]*(QQ(1)/12-(r==c))
 inv=block_matrix(p,sparse=True);assert D(0)*inv==identity_matrix(QQ,1920),'time inverse'
 records=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks'];J=matrix(QQ,1920,128,sparse=True)
 for k,r in enumerate(records):
  js=mat(r['basis'])*mat(r['section'])
  for (i,j),v in js.dict().items():J[r['coordinates'][i],4*k+j]=v
 ids=J.transpose().pivots();L=matrix(QQ,128,1920,sparse=True);b=J.matrix_from_rows(ids).inverse()
 for j,i in enumerate(ids):L.set_column(i,b.column(j))
 assert L*J==I
 return g,D,inv,J,L

def replay(v):
 g,D,inv,J,L=setup();labels=v['labels'];blocks=v['blocks'];I15=identity_matrix(QQ,15,sparse=True)
 assert sorted(j for b in blocks for j in b['columns'])==list(range(1274)),'column partition'
 assert len({r for b in blocks for r in b['rows']})==sum(len(b['rows']) for b in blocks),'distinct selected rows'
 allrows=sorted({r for b in blocks for r in b['rows']});rawrows=sorted({r//128 for r in allrows});pos={r:i for i,r in enumerate(rawrows)}
 smallJ=J.matrix_from_rows(rawrows);Bs=[matrix(QQ,len(b['rows']),len(b['columns'])) for b in blocks];input_faults=[];locations={j:(b,i) for b,x in enumerate(blocks) for i,j in enumerate(x['columns'])}
 for k in range(14):
  A=inv*D(k);R=A.matrix_from_rows(rawrows)-smallJ*(L*A)
  if k==0:
   first=next(j for j,label in enumerate(labels) if label[0]==0);bi,ci=locations[first];_,aa,bb=labels[first];picked=blocks[bi]['rows']
   for name,slots,gen in [('wrong_generator',I15,g[(aa+1)%14]*g[bb]),('omitted_connection',I15,0*g[aa]),('reversed_bivector_order',I15,g[bb]*g[aa])]:
    bad=R*slots.tensor_product(gen)*J
    input_faults.append((name,bi,ci,[bad[pos[r//128],r%128] for r in picked]))
  for j,(kk,a,b) in enumerate(labels):
   if kk!=k:continue
   vj=R*I15.tensor_product(g[a]*g[b])*J;bi,ci=locations[j]
   own=set(blocks[bi]['rows']);assert all(vj[pos[r//128],r%128]==0 for r in allrows if r not in own),'independent off-block zero'
   Bs[bi].set_column(ci,[vj[pos[r//128],r%128] for r in blocks[bi]['rows']])
  print('independent covector',k,flush=True)
 total=0
 for b,B in zip(blocks,Bs):
  minor=B.matrix_from_columns(b['pivot_columns']);iv=mat(b['inverse']);K=mat(b['kernel'])
  assert minor*iv==identity_matrix(QQ,minor.nrows()),'opposite-side minor inverse'
  assert B*K.transpose()==0,'selected kernel'
  total+=minor.nrows()
 assert total==v['rank']==v['parameter_count']==1274,'complete full-rank class'
 assert max(sum(abs(z) for z in row) for b in blocks for row in mat(b['inverse']).rows())==QQ(505487620559)/71559153,'exact inverse norm'
 assert mat(v['kernel']).nrows()==0 and v['induced_rank']==v['mass_image_rank']==0,'zero class'
 for name,bi,ci,values in input_faults:
  original=Bs[bi];bad=copy.copy(original);bad.set_column(ci,values);b=blocks[bi]
  assert bad!=original,'nontrivial raw-input fault '+name
  assert bad.matrix_from_columns(b['pivot_columns'])*mat(b['inverse'])!=identity_matrix(QQ,len(b['rows'])),'raw-input fault caught '+name
 print('PASS three raw Clifford input faults',flush=True)
 # Matrix-certificate mutations (separate from the raw-input faults above).
 # Real mathematical mutations of an independently formed leakage matrix.
 B=Bs[0];b=blocks[0];iv=mat(b['inverse']);cs=b['pivot_columns'];minor=B.matrix_from_columns(cs)
 faults=[]
 for kind in ['deleted_column','reversed_column','wrong_entry','wrong_coordinate']:
  bad=copy.copy(minor)
  if kind=='deleted_column':bad.set_column(0,[0]*bad.nrows())
  elif kind=='reversed_column':bad.set_column(0,-bad.column(0))
  elif kind=='wrong_entry':bad[0,0]+=1
  else:bad.swap_columns(0,1)
  assert bad!=minor and bad*iv!=identity_matrix(QQ,bad.nrows()),'nontrivial fault detection';faults.append(kind)
 return len(blocks),faults

def metadata(v):
 assert v['result_id']=='K1959','identity'
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'pin'

def replay_tensor(v):
 t=v['tensorial'];g,D,inv,J,L=setup();labels=v['labels'];blocks=t['blocks'];I15=identity_matrix(QQ,15,sparse=True);eta=[1]*7+[-1]*7
 rr=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
 H=block_matrix([[mat(rr[i]['quotient_energy']) if i==j else zero_matrix(QQ,4,4) for j in range(32)] for i in range(32)],sparse=True)
 C=[L*inv*D(k)*J for k in [7,8,9]]
 assert sorted(j for b in blocks for j in b['columns'])==list(range(1274)),'tensor column partition'
 assert len({r for b in blocks for r in b['rows']})==sum(len(b['rows']) for b in blocks),'tensor row partition'
 allrows=sorted({r for b in blocks for r in b['rows']});rawrows=sorted({r//128 for r in allrows});pos={r:i for i,r in enumerate(rawrows)};smallJ=J.matrix_from_rows(rawrows)
 Bs=[matrix(QQ,len(b['rows']),len(b['columns'])) for b in blocks];locations={j:(b,i) for b,x in enumerate(blocks) for i,j in enumerate(x['columns'])};As={k:inv*D(k) for k in range(14)}
 def connection(a,b):
  JJ=I15.tensor_product(g[a]*g[b])*J
  JJ[128*a:128*(a+1),:]+=2*eta[a]*J[128*b:128*(b+1),:]
  JJ[128*b:128*(b+1),:]-=2*eta[b]*J[128*a:128*(a+1),:]
  return JJ
 for k in range(14):
  A=As[k];R=A.matrix_from_rows(rawrows)-smallJ*(L*A)
  for j,(kk,a,b) in enumerate(labels):
   if kk!=k:continue
   V=R*connection(a,b);bi,ci=locations[j]
   own=set(blocks[bi]['rows']);assert all(V[pos[r//128],r%128]==0 for r in allrows if r not in own),'tensor off-block zero'
   Bs[bi].set_column(ci,[V[pos[r//128],r%128] for r in blocks[bi]['rows']])
  print('independent tensor covector',k,flush=True)
 total=0
 for b,B in zip(blocks,Bs):
  minor=B.matrix_from_columns(b['pivot_columns']);assert minor*mat(b['inverse'])==identity_matrix(QQ,minor.nrows()),'tensor minor'
  total+=minor.nrows()
 K=mat(t['kernel']);assert K.rank()==K.nrows() and total+K.nrows()==1274 and total==t['rank'],'tensor rank completeness'
 images=[]
 for row in K.rows():
  V=zero_matrix(QQ,1920,128,sparse=True)
  for j,z in enumerate(row):
   if z:
    k,a,b=labels[j];V+=z*As[k]*connection(a,b)
  M=L*V;assert V==J*M,'full raw tensor kernel';images.append(M)
 F=matrix(QQ,[sum([(M*c+c*M).list() for c in C],[])+(H*M+M.transpose()*H).list() for M in images]).transpose()
 MK=mat(t['mass_kernel']);assert F*MK.transpose()==0 and MK.rank()+F.rank()==K.nrows(),'complete mass conditions'
 mi=[sum((z*M for z,M in zip(row,images)),zero_matrix(QQ,128,128)) for row in MK.rows()]
 rank=matrix(QQ,[M.list() for M in mi]).rank() if mi else 0
 assert rank==t['mass_image_rank']==0,'mass image'
 assert t['induced_rank']==K.nrows()-MK.nrows()==91,'induced rank from exact zero-action kernel'
 R=mat(t['rotation_matrix']);actual=L*connection(1,2)
 assert R==actual and connection(1,2)==J*R and R*R==-identity_matrix(QQ,128) and H*R+R.transpose()*H==0 and all(R*c==c*R for c in C),'actual temporal rotation'
 # A contrary spinor-only placement removes the covector action and MUST leak.
 V=I15.tensor_product(g[1]*g[2])*J
 assert V!=J*(L*V),'removing covector input changes invariance'
 print('PASS independent tensor kernel/mass/rotation',total,K.nrows(),MK.nrows(),rank,flush=True)
 return total,K.nrows(),MK.nrows(),rank


def check_spacetime():
 g,D,inv,J,L=setup();I=identity_matrix(QQ,128,sparse=True);eta=[1]*7+[-1]*7
 JJ=identity_matrix(QQ,15,sparse=True).tensor_product(g[1]*g[2])*J
 JJ[128:256,:]+=2*eta[1]*J[256:384,:]
 JJ[256:384,:]-=2*eta[2]*J[128:256,:]
 R=L*JJ;assert JJ==J*R and R*R==-I,'gauge generator'
 rows=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
 H=block_matrix([[mat(rows[i]['quotient_energy']) if i==j else zero_matrix(QQ,4,4) for j in range(32)] for i in range(32)],sparse=True)
 for k in [0,7,8,9]:
  A=inv*D(k);C=L*A*J;M=C*R
  assert A*JJ==J*M and C*R==R*C and H*M+M.transpose()*H==0,'actual spacetime gauge coefficient'
 print('PASS four actual spacetime gauge coefficients, conservation and conjugacy algebra',flush=True)

if __name__=='__main__':
 v=json.loads(OUT.read_text());metadata(v);n,faults=replay(v);replay_tensor(v);check_spacetime()
 for f in ['identity','pin']:
  bad=copy.deepcopy(v)
  if f=='identity':bad['result_id']='bad'
  else:bad['inputs'][next(iter(bad['inputs']))]='bad'
  try:metadata(bad)
  except AssertionError as e:assert str(e)==f
  else:raise AssertionError('undetected metadata fault')
 print('PASS independent full1274 class',n,'exact block inverses;',faults,'and two metadata faults')
