"""Exact local bar-contour obstruction. Root-serialized; no positivity imposed.
Use --certificate to replay an existing dyadic witness without QR/inversion.
The450 principal-class completeness and derivative-parity argument are written
mathematics; exact finite controls and root-ball minor certificates support them.
"""
import sys,json,argparse
from pathlib import Path
from fractions import Fraction as Q
p=argparse.ArgumentParser();p.add_argument('--repo',default=str(Path(__file__).resolve().parents[2]));p.add_argument('--output');p.add_argument('--certificate');args=p.parse_args()
sys.path.insert(0,str(Path(args.repo)/'tests/program-focus'))
import source_action_deep_geometry as g
from source_action_deep_algebra import add,scale,certificate_for

def mul(A,B):
 o={}
 for a,x in A.items():
  for b,y in B.items():
   c,s=g.cliff_mul(a,b);o[c]=o.get(c,Q(0))+x*y*s
 return {k:v for k,v in o.items() if v}
def sharp(A):return {c:(-1)**(c.bit_count()*(c.bit_count()+1)//2)*v for c,v in A.items()}
def ga(i):return {1<<i:Q(1)}
def madd(*xs):
 o={}
 for M in xs:
  for k,v in M.items():o[k]=add(o.get(k,{}),v)
 return {k:v for k,v in o.items() if v}
def mscale(c,M):return {k:scale(c,v)for k,v in M.items() if c}
def mm(A,B):
 o={}
 for (i,k),a in A.items():
  for (l,j),b in B.items():
   if k==l:o[i,j]=add(o.get((i,j),{}),mul(a,b))
 return {k:v for k,v in o.items() if v}
def ms(M):return {(j,i):sharp(v)for(i,j),v in M.items()}
I={(i,i):{0:Q(1)}for i in range(15)}
R=dict(I);FI=dict(I)
for a in range(14):
 for b in range(14):R[a,b]=add(R.get((a,b),{}),scale(-Q(1,4)/g.d[b],mul(ga(a),ga(b))))
 R[a,14]=scale(Q(1,2),ga(a));R[14,a]=scale(-Q(1,2)/g.d[a],ga(a))
 FI[a,14]=scale(-Q(1,2),ga(a));FI[14,a]=scale(1/g.d[a],ga(a))
FI[14,14]={0:Q(-6)}

def CT(T):
 slash=add(*(scale(1/g.d[a],mul(ga(a),T[a]))for a in range(14)))
 V={}
 for a in range(14):
  for b in range(14):
   v=add(slash if a==b else {},scale(-1/g.d[b],mul(ga(b),T[a])))
   if v:V[a,b]=v
  if T[a]:V[a,14]=T[a];V[14,a]=scale(1/g.d[a],T[a])
 V[14,14]=scale(-Q(1,2),slash)
 return mm(mm(R,V),FI)
spinSum=add(*(scale(1/g.d[i],mul(ga(i),g.spin[i]))for i in range(14)))
C0={}
for a in range(14):
 for b in range(14):
  v=add(spinSum if a==b else {},*(scale(-g.Lambda[i][a][b]/g.d[i],ga(i))for i in range(14)))
  if v:C0[a,b]=v
C0[14,14]=scale(-1,spinSum)
div=[sum(g.Lambda[j][i][j]for j in range(14))for i in range(14)]
assert div[4]==-4
PA=[{(j,j):scale((1 if j<14 else -1)/g.d[i],ga(i))for j in range(15)}for i in range(14)]
DivA=madd(*(mscale(div[i],PA[i])for i in range(14)))
# Full Clifford volume normalized to square+1.
vol=Q(1)
for d in g.d:vol*=abs(d)
from math import isqrt
rootvol=Q(isqrt(vol.numerator),isqrt(vol.denominator));assert rootvol**2==vol
Om={(1<<14)-1:1/rootvol};assert mul(Om,Om)=={0:Q(1)}
Ks=[{(a,a):1/g.d[a]for a in range(4)}, {(a,a):1/g.d[a]for a in range(5,14)}, {(4,4):Q(1)},{(14,14):Q(1)}, {(4,14):Q(1)}, {(14,4):Q(1)}]
Ws=[];Vs=[]
for parity in range(2):
 for K in Ks:
  W={k:scale(v,Om if parity else {0:Q(1)})for k,v in K.items()}
  V={(a,b):scale((1 if parity else -1)*(1 if a<14 else -1)*(1 if b<14 else -1),c)for(a,b),c in W.items()}
  Ws.append(W);Vs.append(V)
  for A in PA:assert mm(W,A)==mm(ms(A),V)

def defects(C,with_div=True):
 out=[];CS=ms(C)
 for W,V in zip(Ws,Vs):
  M=madd(mm(W,C),mm(CS,V),mscale(-1,mm(W,DivA))if with_div else {})
  out.append({(a,b,c):v for(a,b),row in M.items()for c,v in row.items() if v})
 return out
D0=defects(C0)
# Natural Clifford-compatible reference contour W=diag(G^-1,1) H.
nat=[Q(1),Q(1),1/g.d[4],Q(1),Q(0),Q(0)]+[Q(0)]*6
allrows=set().union(*(x.keys()for x in D0))
assert all(sum(nat[j]*D0[j].get(k,Q(0))for j in range(12))==0 for k in allrows),'reference natural contour failed'
data=json.loads((Path(args.repo)/'lab/process/source-action-deep-coefficients.json').read_text())
for root in data['certified_roots']:
 cert=certificate_for(data,root)
 assert cert['status']=='exact_local_root_certified' and Q(str(root['h']))==1
 for key in ('e','a','b','radius','ball_image_bound','lipschitz_bound'):
  assert cert[key]==root['certificate'][key],(root['id'],key)
# Check every matrix-unit member of the450-dimensional principal family
# against every covector; the classification proof separately owns completeness.
principal_controls=0
for parity in range(2):
 blade=Om if parity else {0:Q(1)}
 for a in range(15):
  for b in range(15):
   sa=1 if a<14 else -1;sb=1 if b<14 else -1
   vb=scale((1 if parity else -1)*sa*sb,blade)
   for i in range(14):
    assert mul(blade,scale(sb/g.d[i],ga(i)))==mul(scale(-sa/g.d[i],ga(i)),vb)
    principal_controls+=1
Cb=[]
for row in data['basis']:
 T=[{}for _ in range(14)]
 for e,c,v in row:T[int(e).bit_length()-1][int(c)]=Q(v)
 Cb.append(CT(T))
# All variable principal graphs: derivatives contribute odd Clifford grades.
# This even-grade algebraic condition is independent of coefficient derivatives.
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS"):
 os.environ.setdefault(key,"1")
import numpy as np
if not args.certificate:
 from scipy.linalg import qr
from math import lcm,frexp
assert all(c.bit_count()%2 for row in C0.values()for c in row)
full=(1<<14)-1
J=[1]*14+[-1]

def rowcoef(C,key):
 i,j,c=key;cc=full^c
 _,factor=g.cliff_mul(full,cc);factor=Q(factor)/rootvol
 sc=(-1)**(c.bit_count()*(c.bit_count()+1)//2)
 scc=(-1)**(cc.bit_count()*(cc.bit_count()+1)//2)
 o={}
 def put(k,v):
  if v:o[k]=o.get(k,Q(0))+v
 for b in range(15):
  row=C.get((b,j),{})
  put(i*15+b,row.get(c,Q(0)))
  put(225+i*15+b,factor*row.get(cc,Q(0)))
 for a in range(15):
  row=C.get((a,i),{})
  put(a*15+j,-J[a]*J[j]*sc*row.get(c,Q(0)))
  put(225+a*15+j,J[a]*J[j]*scc*factor*row.get(cc,Q(0)))
 return {k:v for k,v in o.items()if v}

# Authenticate sparse row assembly against prior full matrix arithmetic for
# the twelve invariant directions on a nonzero basis combination.
controlC=madd(*Cb[:3]);controlD=defects(controlC,False)
Kcoords=[]
for parity in range(2):
 for K in Ks:Kcoords.append({225*parity+15*a+b:v for(a,b),v in K.items()})
controlrows=sorted(set().union(*(D.keys()for D in controlD)))
for key in controlrows:
 if key[2].bit_count()%2:continue
 row=rowcoef(controlC,key)
 for j,K in enumerate(Kcoords):assert sum(v*row.get(k,Q(0))for k,v in K.items())==controlD[j].get(key,Q(0))

def replay_certificate(path):
 import zlib,base64,hashlib
 raw=json.loads(Path(path).read_text())
 raw=raw.get('contours',{}).get('all_local',raw)
 certs=raw['roots'];assert len(certs)==2
 actual={r['id']:r for r in data['certified_roots']}
 assert {r['root']for r in certs}==set(actual)
 replayed=[]
 for record in certs:
  root=actual[record['root']]
  x=list(map(Q,root['coordinates']));radius=Q(root['certificate']['radius'])
  C=madd(*(mscale(v,T)for v,T in zip(x,Cb)))
  selected=[tuple(map(int,key))for key in record['selected_rows']]
  scales=list(map(Q,record['row_scales']))
  assert len(selected)==len(scales)==450 and len(set(selected))==450
  assert all(s for s in scales)
  assert all(0<=i<15 and 0<=j<15 and 0<=c<(1<<14) and c.bit_count()%2==0 for i,j,c in selected)
  M=[]
  for key,s in zip(selected,scales):
   row=rowcoef(C,key);M.append([s*row.get(j,Q(0))for j in range(450)])
  assert record['inverse_witness_encoding']=='zlib_base64_json_decimal_integer_matrix'
  payload=zlib.decompress(base64.b64decode(record['inverse_witness_compressed']))
  assert hashlib.sha256(payload).hexdigest()==record['inverse_witness_sha256']
  integer_rows=json.loads(payload)
  assert len(integer_rows)==450 and all(len(row)==450 for row in integer_rows)
  Rint=np.array([[int(v)for v in row]for row in integer_rows],dtype=object)
  denR=int(record['inverse_witness_denominator']);assert denR>0
  denM=1
  for row in M:
   for v in row:denM=lcm(denM,v.denominator)
  Mint=np.array([[v.numerator*(denM//v.denominator)for v in row]for row in M],dtype=object)
  product=Rint@Mint;totalDen=denR*denM
  residual=max(sum(abs((totalDen if i==j else 0)-int(product[i,j]))for j in range(450))for i in range(450))
  a=Q(residual,totalDen)
  errors=[radius*abs(s)*sum(sum(abs(v)for v in rowcoef(T,key).values())for T in Cb)for key,s in zip(selected,scales)]
  uncertainty=max(sum(Q(abs(int(Rint[i,k])),denR)*errors[k]for k in range(450))for i in range(450))
  bound=a+uncertainty
  assert a==Q(record['exact_inverse_residual_bound'])
  assert uncertainty==Q(record['exact_root_uncertainty_bound'])
  assert bound==Q(record['total_bound']) and bound<1
  replayed.append({'root':root['id'],'certified_rank450':True,'total_bound':str(bound),'approximate_total_bound':float(bound)})
 return {'mode':'exact_witness_replay_no_QR_or_inversion','all_passed':True,
         'root_certificates_recomputed':2,'principal_matrix_unit_controls':principal_controls,
         'natural_reference_contour_control':True,'even_assembly_control':True,'roots':replayed,
         'scope':'all smooth pointwise nondegenerate antilinear graphs mapping every freely initialized candidate solution to its independent row equation are excluded at these backgrounds; restricted/nonlocal contours and source selection remain open'}

if args.certificate:
 out=replay_certificate(args.certificate)
 text=json.dumps(out,indent=2)+'\n'
 if args.output:Path(args.output).write_text(text)
 else:print(text)
 sys.exit(0)

outputs=[]
for root in data['certified_roots']:
 x=list(map(Q,root['coordinates']));r=Q(root['certificate']['radius'])
 C=madd(*(mscale(v,T)for v,T in zip(x,Cb)))
 masks=set(c for row in C.values()for c in row if c.bit_count()%2==0)
 masks|={full^c for c in list(masks)}
 # A bounded subset of equations is sufficient for a full-rank certificate.
 # Never allocate all225*8192 possible rows. Stratify over Clifford grades.
 import random
 rng=random.Random(450)
 chosen=set()
 def include(c):
  pair={c,full^c}&masks
  if len(chosen|pair)<=32:chosen.update(pair)
 for c in (0,full):
  if c in masks:include(c)
 low=sorted(c for c in masks if c.bit_count()==2)
 for j in range(min(8,len(low))):include(low[j*(len(low)-1)//max(1,min(8,len(low))-1)])
 rest=list(sorted(masks));rng.shuffle(rest)
 for c in rest:
  include(c)
  if len(chosen)==32:break
 assert len(chosen)<=32
 keys=[(i,j,c)for i in range(15)for j in range(15)for c in sorted(chosen)]
 assert len(keys)<=7200
 rows=[];kept=[]
 for key in keys:
  row=rowcoef(C,key)
  if row:rows.append(row);kept.append(key)
 print(json.dumps({'event':'even450_rows','root':root['id'],'rows':len(rows)}),file=sys.stderr,flush=True)
 dense=np.zeros((len(rows),450))
 for i,row in enumerate(rows):
  for j,v in row.items():dense[i,j]=float(v)
 norm=np.linalg.norm(dense,axis=1)
 _,RR,piv=qr((dense/norm[:,None]).T,mode='economic',pivoting=True)
 diagnostic_rank=int(np.sum(np.abs(np.diag(RR))>1e-11))
 result={'root':root['id'],'rows':len(rows),'selected_clifford_masks':sorted(chosen),'floating_diagnostic_rank':diagnostic_rank,'full_equation_system_exhausted':False}
 if diagnostic_rank<450:
  result['certified_rank450']=False;result['status']='inconclusive_bounded_subset';outputs.append(result);continue
 if len(piv)<450:
  outputs.append(result);continue
 selected=[int(j)for j in piv[:450]]
 M=[];scales=[]
 for idx in selected:
  exponent=frexp(norm[idx])[1];s=Q(2)**(-exponent);scales.append(s)
  M.append([s*rows[idx].get(j,Q(0))for j in range(450)])
 MF=np.array([[float(v)for v in row]for row in M])
 try:RF=np.linalg.inv(MF)
 except np.linalg.LinAlgError:
  result['certified_rank450']=False;outputs.append(result);continue
 # Numerical inversion proposes a witness only. Common-denominator integer
 # arithmetic authenticates its exact inverse defect.
 denR=1<<50
 Rint=np.array([[int(round(float(v)*denR))for v in row]for row in RF],dtype=object)
 denM=1
 for row in M:
  for v in row:denM=lcm(denM,v.denominator)
 Mint=np.array([[v.numerator*(denM//v.denominator)for v in row]for row in M],dtype=object)
 product=Rint@Mint
 totalDen=denR*denM
 residual=max(sum(abs((totalDen if i==j else 0)-int(product[i,j]))for j in range(450))for i in range(450))
 a=Q(residual,totalDen)
 errors=[]
 for idx,s in zip(selected,scales):
  key=kept[idx]
  errors.append(r*abs(s)*sum(sum(abs(v)for v in rowcoef(T,key).values())for T in Cb))
 uncertainty=max(sum(Q(abs(int(Rint[i,k])),denR)*errors[k]for k in range(450))for i in range(450))
 bound=a+uncertainty
 result.update({'certified_rank450':bound<1,'exact_inverse_residual_bound':str(a),
                'exact_root_uncertainty_bound':str(uncertainty),'total_bound':str(bound),
                'approximate_total_bound':float(bound),'selected_rows':[kept[i]for i in selected],
                'row_scales':list(map(str,scales)),'inverse_witness_denominator':str(denR),
                'inverse_witness_integer_matrix':[[str(v)for v in row]for row in Rint]})
 import zlib,base64,hashlib
 payload=json.dumps(result.pop('inverse_witness_integer_matrix'),separators=(',',':')).encode()
 result['inverse_witness_encoding']='zlib_base64_json_decimal_integer_matrix'
 result['inverse_witness_sha256']=hashlib.sha256(payload).hexdigest()
 result['inverse_witness_compressed']=base64.b64encode(zlib.compress(payload,9)).decode()
 outputs.append(result)
 print(json.dumps({'event':'even450_certificate','root':root['id'],'certified':bound<1,'bound':float(bound)}),file=sys.stderr,flush=True)
out={'principal_matrix_unit_controls':principal_controls,'root_certificates_recomputed':2,'principal_complex_dimension':450,'even_constraints_ignore_all_contour_derivatives':True,
     'independent_twelve_subfamily_assembly_control':True,'roots':outputs,
     'scope':'certified rank450 excludes smooth local nondegenerate antilinear graphs preserving every freely initialized local solution on these candidate backgrounds; restricted/nonlocal graphs and source necessity remain open'}
s=json.dumps(out,indent=2)
if args.output:Path(args.output).write_text(s+'\n')
else:print(s)
