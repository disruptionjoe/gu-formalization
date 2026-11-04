"""Exact reduced odd principal symbol, all-label census and full metric coupling.

Uses coefficient helpers only, never recursively reruns predecessor banks.
Real derivative covectors; action-covector matrices include the indefinite pairing.
"""
from pathlib import Path
from fractions import Fraction
from math import comb
from itertools import product
from functools import lru_cache
import ast,hashlib,json,sys
import sympy as sp
R=Path(__file__).resolve().parents[2]; checks={};controls={}
def ck(bank,name,value):
 bank[name]=bool(value)
 if not value: raise AssertionError(name)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py'
parent='tests/channel-swings/selected_k77_nonzero_branch_parent_hessian_probe.py'
first='tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py'
src=(R/backend).read_text();M={'__file__':str(R/backend),'__name__':'coefficient_backend'}
exec(compile(src[:src.index('def sparse_rank')],str(R/backend),'exec'),M)
N=14;ETA=M['ETA'];FULL=M['FULL'];ONE=M['ONE'];ZERO=M['ZERO'];SELECTED=('comm','symi','symi')
def load_functions(path,wanted,ns):
 tree=ast.parse((R/path).read_text())
 nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in wanted]
 exec(compile(ast.Module(body=nodes,type_ignores=[]),str(R/path),'exec'),ns)
ns=dict(M=M,N=N,ETA=ETA,FULL=FULL,ONE=ONE,ZERO=ZERO,SELECTED=SELECTED,Fraction=Fraction,sp=sp,PHI1=M['PHI1'],T_VALUE=Fraction(-5,2288))
load_functions(parent,{'pair','basis','qform','hessian','rational'},ns)
kn=dict(M=M,N=N,ETA=ETA,FULL=FULL,ONE=ONE,ZERO=ZERO,SELECTED=SELECTED,Fraction=Fraction,sp=sp)
load_functions(first,{'scalar_one_form','direction','top_scalar','pairing','rows_for_image'},kn)
def rank(a): return a.to_DM().rank()
@lru_cache(None)
def field(mu,mask):
 v=ns['basis'](mu,mask);return v,ns['qform'](v)
@lru_cache(None)
def aval(i,J,j,K):
 if J.bit_count()!=K.bit_count() or J^(1<<i)!=K^(1<<j):return sp.S.Zero
 u,qu=field(i,J);v,qv=field(j,K)
 return ns['rational'](ns['hessian'](u,v,qu,qv))
def raw_block(xi,labels):
 basis=[(label,mu,label^(1<<mu)) for label in sorted(labels) for mu in range(N)]
 idx={(l,i):k for k,(l,i,J) in enumerate(basis)};raw=sp.zeros(len(basis))
 kform=kn['scalar_one_form'](xi)
 for col,(lab,mu,J) in enumerate(basis):
  image=M['shiab'](M['wedge_raw'](kform,kn['direction'](mu,J)),SELECTED)
  for nu,K,value in kn['rows_for_image'](image):
   key=(K^(1<<nu),nu)
   assert key in idx,('off_orbit',key,labels)
   raw[idx[key],col]+=ns['rational'](value)
 C=(raw-raw.T)/2
 odd=[i for i,x in enumerate(basis) if x[2].bit_count()%2];even=[i for i in range(len(basis)) if i not in odd]
 os=[basis[i] for i in odd];es=[basis[i] for i in even]
 A=sp.Matrix(len(es),len(es),lambda i,j:aval(es[i][1],es[i][2],es[j][1],es[j][2]))
 assert rank(A)==len(es)
 B=C.extract(even,odd);S=B.T*A.inv()*B
 assert S==S.T
 return os,S,B,C,basis
cases={'positive':(0,),'negative':(1,),'null':(0,3)};result={};all_edges=set();reduced_edges=set();leak=None
metric_pairs=[(i,j) for i in range(N) for j in range(i,N)];eta=sp.diag(*ETA);W=sp.diag(*[ETA[i]*ETA[j]*(1 if i==j else 2) for i,j in metric_pairs])
def ein(h,xi):
 up=eta*xi;q=(xi.T*up)[0];v=h*up;t=sp.trace(eta*h)
 return (xi*v.T+v*xi.T-q*h-t*xi*xi.T-eta*((up.T*v)[0]-q*t))/2
def orbit(base,axes):
 return tuple(sorted({base^sum((1<<a)*v for a,v in zip(axes,bits)) for bits in product([0,1],repeat=len(axes))}))
def components_rank(mat,source=None):
 # Exact disconnected-component reduction, not numeric thresholding.
 entries=mat.todok();adj=[set() for _ in range(mat.rows)]
 for (i,j),v in entries.items():
  if v:adj[i].add(j);adj[j].add(i)
 seen=set();total=0;sizes=[];residual_rows=[];witness=None
 for i in range(mat.rows):
  if i in seen:continue
  stack=[i];seen.add(i);cc=[]
  while stack:
   u=stack.pop();cc.append(u)
   for v in adj[u]-seen:seen.add(v);stack.append(v)
  cc.sort();block=mat.extract(cc,cc);rk=rank(block);total+=rk;sizes.append([len(cc),rk])
  if source is not None:
   z=source.extract(cc,list(range(source.cols)));nz=[j for j in range(z.cols) if any(z[:,j])]
   if nz:
    for nv in block.nullspace():
     residual=nv.T*z
     if any(residual):
      residual_rows.append(list(residual))
      if witness is None:
       j=next(j for j in range(105,source.cols) if residual[j]) if any(residual[105:]) else next(j for j in range(source.cols) if residual[j])
       witness=dict(null_vector={str(cc[k]):str(nv[k]) for k in range(len(cc)) if nv[k]},source_column=j,pairing=str(residual[j]))
 res=sp.Matrix(residual_rows) if residual_rows else sp.zeros(0,source.cols)
 return total,sorted(sizes),dict(Einstein_image_extra_rank=rank(res[:,:105]),all_conserved_extra_rank=rank(res[:,105:]),witness=witness)
for name,axes in cases.items():
 xi=tuple(int(i in axes) for i in range(N));pos=[i for i in range(N) if ETA[i]==1 and i not in axes];neg=[i for i in range(N) if ETA[i]==-1 and i not in axes]
 rows=[];dim=srank=brank=active_dim=active_rank=0;grade1rank=0
 for np in range(len(pos)+1):
  for nm in range(len(neg)+1):
   base=sum(1<<i for i in pos[:np]+neg[:nm]);labels=orbit(base,axes);os,S,B,C,bs=raw_block(xi,labels)
   mult=comb(len(pos),np)*comb(len(neg),nm);rk=rank(S);rb=rank(B);active=[i for i,x in enumerate(os) if x[2].bit_count() in {1,5,9,13}]
   inactive=[i for i in range(len(os)) if i not in active];assert S.extract(active,inactive)==sp.zeros(len(active),len(inactive))
   g1=[i for i,x in enumerate(os) if x[2].bit_count()==1];grade1rank+=mult*rank(S.extract(g1,g1))
   dim+=mult*len(os);srank+=mult*rk;brank+=mult*rb;active_dim+=mult*len(active);active_rank+=mult*rank(S.extract(active,active))
   for i,j in C.todok():
    if C[i,j]:all_edges.add(tuple(sorted((bs[i][2].bit_count(),bs[j][2].bit_count()))))
   if leak is None:
    for (i,j),v in S.todok().items():
     if v:reduced_edges.add(tuple(sorted((os[i][2].bit_count(),os[j][2].bit_count()))))
     if v and {os[i][2].bit_count(),os[j][2].bit_count()}=={1,5}:leak=dict(case=name,labels=list(labels),row=list(os[i]),column=list(os[j]),value=str(v))
   rows.append(dict(positive_count=np,negative_count=nm,multiplicity=mult,odd_dimension=len(os),B_rank=rb,Schur_rank=rk,active_rank=rank(S.extract(active,active))))
 ck(checks,name+'_all_odd_exhausted',dim==114688);ck(checks,name+'_active_chain_exhausted',active_dim==56448)
 ck(checks,name+'_B_matches_owned_first_order',2*brank==(122746 if name=='null' else 130912))
 # Only label0 and label-size2 contain grade1; complete all their derivative XOR orbits.
 affected={orbit(lab,axes) for lab in [0]+[(1<<i)^(1<<j) for i,j in metric_pairs if i!=j]}
 blocks=[];states=[];offset=105;entries={};affected_rank=0
 x=sp.Matrix(xi);hs=[];Es=[]
 for i,j in metric_pairs:
  h=sp.zeros(N);h[i,j]=h[j,i]=1;hs.append(h);Es.append(ein(h,x))
 E=sp.Matrix.hstack(*[sp.Matrix([ee[i,j] for i,j in metric_pairs]) for ee in Es]);G=-12*sp.Rational(-5,2288)*W*E
 entries.update(G.todok());gauge=[]
 for labset in sorted(affected):
  os,S,_,_,_=raw_block(xi,labset);affected_rank+=rank(S)
  for (i,j),v in S.todok().items():entries[offset+i,offset+j]=v
  for row,(_,i,J) in enumerate(os):
   if J.bit_count()!=1:continue
   j=J.bit_length()-1
   for col,ee in enumerate(Es):
    v=-2*ETA[i]*ee[i,j]
    if v:entries[offset+row,col]=v;entries[col,offset+row]=v
  states.extend(os);offset+=len(os)
 H=sp.SparseMatrix(offset,offset,entries)
 ck(checks,name+'_action_pairing_symmetric',H==H.T)
 for j in range(N):
  v=sp.eye(N)[:,j];h=x*v.T+v*x.T;gv=sp.Matrix([h[i,k] for i,k in metric_pairs]+[0]*len(states))
  ck(checks,name+'_diffeo_'+str(j),H*gv==sp.zeros(offset,1));gauge.append(gv[:105,:])
 # Keep actual source covector test: Einstein-conserved metric image must lie in full symbol image to solve a pure highest-order source equation.
 J=sp.Matrix.hstack(*sp.Matrix.hstack(*gauge).T.nullspace());assert J.cols==91
 Z=sp.zeros(offset,196);Z[:105,:105]=W*E;Z[:105,105:]=J
 hr,cs,compat=components_rank(H,Z)
 if compat['witness']:
  wi=compat['witness'];nv=sp.zeros(offset,1)
  for i,v in wi['null_vector'].items():nv[int(i)]=sp.Rational(v)
  j=wi['source_column'];assert H*nv==sp.zeros(offset,1) and (nv.T*Z[:,j])[0]!=0
  wi['source_metric_covector']={str(metric_pairs[i]):str(Z[i,j]) for i in range(105) if Z[i,j]}
  wi['null_vector_native']={('h'+str(metric_pairs[int(i)]) if int(i)<105 else 'Q'+str(states[int(i)-105])):v for i,v in wi.pop('null_vector').items()}
 ck(checks,name+'_complete_source_space',J.cols==91 and sp.Matrix.hstack(*gauge).T*J==sp.zeros(14,91))
 result[name]=dict(grade1_rank=grade1rank,metric_grade1_rank=grade1rank-affected_rank+hr,odd_dimension=dim,odd_rank=srank,odd_radical=dim-srank,B_rank=brank,active_dimension=active_dim,active_rank=active_rank,orbits=rows,affected_odd_dimension=len(states),affected_odd_rank=affected_rank,augmented_rank=hr,full_metric_odd_rank=srank-affected_rank+hr,full_metric_odd_dimension=114793,component_dimensions_ranks=cs,source_compatibility=compat)
 print(name,'odd',srank,'metric+odd',result[name]['full_metric_odd_rank'],'components max',max(a for a,b in cs),flush=True)
ck(checks,'two_grade_chains',all_edges=={(0,3),(1,2),(2,5),(3,4),(4,7),(5,6),(6,9),(7,8),(8,11),(9,10),(10,13),(11,12),(13,14)})
ck(checks,'all_offgrade_reduced_cancellation',all(a==b for a,b in reduced_edges))
AA=sp.diag(1,-1);BB=sp.Matrix([1,1]);ck(controls,'rank_B_not_Schur_rank',rank(BB)==1 and BB.T*AA.inv()*BB==sp.zeros(1))
# Actual nonzero orbit: a real derivative skew coefficient produces PLUS Schur.
os,SS,BB,CC,bs=raw_block((1,)+(0,)*13,orbit(0,(0,)))
ix=next((i,j) for (i,j),v in SS.todok().items() if v)
ck(controls,'wrong_adjoint_sign_changes_actual_orbit',(-SS)[ix]!=SS[ix])
odd=[i for i,x in enumerate(bs) if x[2].bit_count()%2];even=[i for i,x in enumerate(bs) if not x[2].bit_count()%2]
es=[bs[i] for i in even];AA=sp.Matrix(len(es),len(es),lambda i,j:aval(es[i][1],es[i][2],es[j][1],es[j][2]))
ck(checks,'actual_orbit_original_elimination',CC.extract(odd,even)*(-AA.inv()*BB)==SS)
# Algebraic product curvature controls the hypothesis of the written remainder proof.
def curvature(i,j,k,l):
 return (sp.Integer(1) if i//7==j//7==k//7==l//7 else sp.Integer(0))*(eta[i,k]*eta[j,l]-eta[i,l]*eta[j,k])
ck(checks,'product_curvature_first_Bianchi',all(curvature(i,j,k,l)+curvature(i,k,l,j)+curvature(i,l,j,k)==0 for i in range(14) for j in range(14) for k in range(14) for l in range(14)))
def broken(i,j,k,l):
 ids=[i,j,k,l]
 if sorted(ids)!=[0,1,2,3]:return 0
 return (-1)**sum(ids[a]>ids[b] for a in range(4) for b in range(a+1,4))
ck(controls,'Bianchi_broken_four_tensor_rejected',broken(0,1,2,3)+broken(0,2,3,1)+broken(0,3,1,2)!=0)
ck(checks,'broken_fixture_preserves_pair_symmetries',all(broken(i,j,k,l)==-broken(j,i,k,l)==-broken(i,j,l,k)==broken(k,l,i,j) for i in range(4) for j in range(4) for k in range(4) for l in range(4)))

report=dict(result='K2535',checks=checks,contrary_controls=controls,causal_census=result,grade1_grade5_witness=leak,grade_edges=sorted(map(list,all_edges)),reduced_grade_edges=sorted(map(list,reduced_edges)),scope='exact frozen reduced principal symbol at radial stationary product, kappa nonzero; no Green inverse, physical quotient or native GU claim',dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in [backend,parent,first,'lab/process/k2533-mixed-source-response.json',str(Path(__file__).relative_to(R))]})
p=R/'lab/process/k2535-reduced-response-symbol.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==report
print('K2535',len(checks),'exact groups',len(controls),'contrary controls')
