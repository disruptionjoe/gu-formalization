"""Independent bit-Clifford source action and exact exclusion certificate replay."""
from pathlib import Path
from copy import deepcopy,copy
import json,hashlib
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,prod
from k1951_coordinated_zero_southeast_principal_probe import gamma,mat
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1953-spin-connection-stable-mass.json'
def assemble(v):
 g=gamma();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);W=(3*I-prod(g))/2;Wi=(3*I+prod(g))/4;eta=[1]*7+[-1]*7
 def rawD(k):
  return block_matrix([[eta[r]*g[r]*g[k]*g[c]*W if r!=k and c not in (r,k) else Z for c in range(14)]+[I if r==k else Z] for r in range(14)]+[[-eta[c]*I if c==k else Z for c in range(14)]+[Z]],sparse=True)
 D0=rawD(0);inv=[[Z]*15 for _ in range(15)];inv[0][14]=-I;inv[14][0]=I
 for r in range(1,14):
  for c in range(1,14):inv[r][c]=Wi*eta[r]*g[r]*g[0]*g[c]*(QQ(1)/12-(1 if r==c else 0))
 Inv=block_matrix(inv,sparse=True);assert D0*Inv==identity_matrix(QQ,1920,sparse=True),'independently checked time inverse'
 rows=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks'];J=matrix(QQ,1920,128,sparse=True)
 for k,r in enumerate(rows):
  j=mat(r['basis'])*mat(r['section'])
  for (i,c),z in j.dict().items():J[r['coordinates'][i],4*k+c]=z
 ix=J.transpose().pivots();L=matrix(QQ,128,1920,sparse=True);li=J.matrix_from_rows(ix).inverse()
 for j,i in enumerate(ix):L.set_column(i,li.column(j))
 C=[block_matrix([[mat(rows[i]['quotient_generators'][k]) if i==j else zero_matrix(QQ,4,4) for j in range(32)] for i in range(32)],sparse=True) for k in range(3)]
 H=block_matrix([[mat(rows[i]['quotient_energy']) if i==j else zero_matrix(QQ,4,4) for j in range(32)] for i in range(32)],sparse=True)
 D={k:rawD(k) for k in [0,7,8,9]};A={k:Inv*d for k,d in D.items()};assert all(D[k]*J==D0*J*c for k,c in zip([7,8,9],C)),'direct source restriction'
 selected=v['selected_rows'];cols=[];cache=[]
 def column(k,a,b,fault=None,tensor=False,selected_rows=None,raw_output=False):
  G=g[a]*g[b]
  if fault=='missing_connection':G=0*G
  if fault=='wrong_real_form':G=g[a]*g[a]
  action=identity_matrix(QQ,15,sparse=True).tensor_product(G)*J
  if tensor and fault!='missing_form_action':
   # Covector action dual to [g_a g_b,g_c]=2(eta_b delta_bc g_a-eta_a delta_ac g_b).
   action[128*a:128*(a+1),:]+=2*eta[a]*J[128*b:128*(b+1),:]
   action[128*b:128*(b+1),:]-=2*eta[b]*J[128*a:128*(a+1),:]
  V=A[(7 if k==0 else 0) if fault=='wrong_covector' else k]*action
  if raw_output:return V
  chosen=selected if selected_rows is None else selected_rows
  M=L*V;pieces=[V-J*M]
  if max(chosen)>=1920*128:pieces += [M*c+c*M for c in C]+[H*M+M.transpose()*H]

  out=[]
  for n in (selected if selected_rows is None else selected_rows):
   if n<1920*128:out.append(pieces[0][n//128,n%128])
   else:
    z=n-1920*128;piece=1+z//16384;z%=16384;out.append(pieces[piece][z//128,z%128])
  return out
 for k,a,b in v['labels']:cols.append(column(k,a,b))
 T=matrix(QQ,cols).transpose()
 def rotation_check(w):
  M=mat(w['matrix']);assert w['label']==[0,1,2]
  V=column(*w['label'],tensor=True,raw_output=True)
  assert V==J*M and H*M+M.transpose()*H==0,'actual conservative potential restriction'
  assert M*M==-identity_matrix(QQ,128) and all(M*c==c*M for c in C),'internal rotation and commuting principal symbol'
 return T,column,rotation_check

def audit(v,T):
 assert v['result_id']=='K1953','identity'
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 assert v['labels']==[[k,a,b] for k in [0,7,8,9] for a in range(14) for b in range(a+1,14)],'complete real Spin connection basis'
 inv=mat(v['inverse']);assert inv*T==identity_matrix(QQ,364),'full-rank mathematical certificate'
 assert QQ(v['inverse_infinity_norm'])==max(sum(abs(z) for z in row) for row in inv.rows()),'quantitative residual constant'
 return 4
if __name__=='__main__':
 v=json.loads(OUT.read_text());T,col,rotation_check=assemble(v);print('PASS K1953 independent raw assembly',audit(v,T),flush=True)
 caught=[]
 for fault in ['missing_connection','wrong_real_form','wrong_covector']:
  bad=copy(T);changed=False
  for j,(k,a,b) in enumerate(v['labels']):
   cv=col(k,a,b,fault)
   if list(T.column(j))!=cv:bad.set_column(j,cv);changed=True;break
  assert changed,'fault must change a load-bearing equation'
  try:audit(v,bad)
  except AssertionError as e:caught.append((fault,str(e)))
  else:raise AssertionError('undetected mathematical fault')
 print('PASS mathematical faults',caught,flush=True)
 tv=v['tensorial'];assert max(tv['selected_rows'])<1920*128+3*128*128,'mass obstruction independent of energy rows'
 ker=mat(tv['kernel']);assert ker.nrows()==5 and ker.rank()==5
 ti=mat(tv['inverse']);tc=tv['selected_columns'];tr=tv['selected_rows']
 TT=matrix(QQ,[col(*v['labels'][j],tensor=True,selected_rows=tr) for j in tc]).transpose()
 assert ti*TT==identity_matrix(QQ,359),'independent tensor rank minor'
 for row in ker.rows():
  image=zero_matrix(QQ,1920,128,sparse=True)
  for j,z in enumerate(row):
   if z:image+=z*col(*v['labels'][j],tensor=True,raw_output=True)
  assert image==0,'tensor kernel acts as zero on the stable fields'
 assert tv['rank']==359 and tv['mass_image_dimension']==0
 print('PASS independent tensor rank359 plus five zero-action kernel directions',flush=True)
 for j in range(len(tc)):
  cv=col(*v['labels'][tc[j]],tensor=True,selected_rows=tr,fault='missing_form_action')
  if cv!=list(TT.column(j)):
   bad=copy(TT);bad.set_column(j,cv);assert ti*bad!=identity_matrix(QQ,359);break
 else:raise AssertionError('tensor fault did not change a load-bearing equation')
 print('PASS mathematical fault missing_form_action',flush=True)
 rotation_check(tv['nonmass_witness']);print('PASS actual conservative internal rotation',flush=True)
 for kind in ['identity','pin']:
  w=deepcopy(v)
  if kind=='identity':w['result_id']='WRONG'
  else:w['inputs'][next(iter(w['inputs']))]='0'*64
  try:audit(w,T)
  except AssertionError as e:print('PASS reporting fault',kind,str(e),flush=True)
  else:raise AssertionError('undetected reporting fault')
