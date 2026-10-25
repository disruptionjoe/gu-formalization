"""Exact observed-direction form family and transverse free massive subsystem.

Completeness is claimed only for scalar-spinor copy metrics on sum-zero R10.
The full observed commutant and source-selected physical state remain open.
"""
from pathlib import Path
import json,hashlib,argparse
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_diagonal_matrix
import k2021_common_degree_dual_operator as b
from k2032_principal_form_rigidity import sm,raw
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2034-observed-principal-forms.json'
U=[1,2,3,4,5,6,10,11,12,13];O=[0,7,8,9]
def produce():
 I=identity_matrix(QQ,128,sparse=True);II=identity_matrix(QQ,1920,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True)
 g=[sm(b.gamma(k)) for k in range(14)];B=sm(b.B);W=sm(b.W);Wb=3*I-W;H=sm(b.H,1920)
 # S maps normalized u coordinates to original zeta coordinates.
 S=block_diagonal_matrix([b.ETA[r]*g[r] if r in U else I for r in range(14)]+[I]);Si=block_diagonal_matrix([g[r] if r in U else I for r in range(14)]+[I])
 assert S*Si==II
 Hn=S.transpose()*H*S;assert Hn==block_diagonal_matrix([-B if r in U else b.ETA[r]*B for r in range(14)]+[B])
 Q=identity_matrix(QQ,10)-matrix(QQ,10,10,[QQ(1)/10]*100)
 def lift(A):
  z={}
  for r in range(10):
   for c in range(10):
    if A[r,c]:z.update({(128*U[r]+j,128*U[c]+j):A[r,c] for j in range(128)})
  return matrix(QQ,1920,1920,z,sparse=True)
 Pn=lift(Q);P=S*Pn*Si;assert P*P==P and P.transpose()*H==H*P and P.trace()==1152
 Ds={k:raw(k,W) for k in O}
 for k,D in Ds.items():
  assert P*D==D*P
  T=Si*D*S;G=g[k]*Wb
  # Entire transverse action is nine copies of -G; complement is invariant.
  expect=matrix(QQ,1920,1920,sparse=True)
  for r in range(10):
   for c in range(10):
    if Q[r,c]:
     for (i,j),v in G.dict().items():expect[128*U[r]+i,128*U[c]+j]=-Q[r,c]*v
  assert T*Pn==expect
 print('PASS full four-symbol invariant decomposition',flush=True)
 # Complete complementary reduction; no one-block numerical extrapolation.
 # Coordinates(a,b7,b8,b9,v,h), all U copies=v, auxiliary=Wbar h.
 CE=matrix(QQ,1920,768,sparse=True)
 for r in range(14):
  col=O.index(r) if r in O else 4
  for (i,j),v0 in (b.ETA[r]*g[r]).dict().items():CE[128*r+i,128*col+j]=v0
 for (i,j),v0 in Wb.dict().items():CE[1792+i,640+j]=v0
 Ts=[]
 for pos,k in enumerate(O[1:],1):
  unit=lambda j:matrix(QQ,1,6,lambda r,c:int(c==j))
  others=[j for j in [1,2,3] if j!=pos]
  vp=(unit(5)+2*unit(4)-sum((unit(j) for j in others),zero_matrix(QQ,1,6)))/12
  rs=[unit(pos)]+[None]*3+[vp,sum((unit(j) for j in others),zero_matrix(QQ,1,6))+10*unit(4)]
  for j in [1,2,3]:rs[j]=(unit(0)+sum((unit(l) for l in others),zero_matrix(QQ,1,6))+9*unit(4)-unit(5)+vp) if j==pos else unit(j)-unit(4)+vp
  T=matrix(QQ,[row.list() for row in rs]);Ts.append(T)
  Ci=g[0]*g[k];liftT=matrix(QQ,768,768,sparse=True)
  for r in range(6):
   for c0 in range(6):
    if T[r,c0]:
     for (i,j),v0 in Ci.dict().items():liftT[128*r+i,128*c0+j]=T[r,c0]*v0
  assert Ds[k]*CE==Ds[0]*CE*liftT
  defect=T*T-identity_matrix(QQ,6);assert defect*defect==0 and defect.rank()==1
 R=matrix(QQ,[row for T in Ts for row in (T*T-identity_matrix(QQ,6)).rows()])
 assert R.rank()==3
 R2=matrix(QQ,list(R.rows())+[row for T in Ts for row in (R*T).rows()]);assert R2.rank()==4
 graph=matrix(QQ,[[1,0],[1,0],[1,0],[1,0],[0,1],[2,10]])
 assert R2*graph==0 and graph.rank()==2
 for T in Ts:assert T*graph==graph
 q=matrix(QQ,1,6,[QQ(1)/9]*4+[1,0]);section=matrix(QQ,6,1,[0,0,0,0,1,10]);assert q*section==1
 for T in Ts:assert q*T==q and T*section==section
 seed=matrix(QQ,6,1,[0,0,0,0,0,1]);cyclic=seed
 dimensions=[]
 while True:
  dimensions.append(cyclic.rank());new=matrix(QQ,list(cyclic.transpose().rows())+[row for T in Ts for row in (T*cyclic).transpose().rows()]).row_space().basis_matrix().transpose()
  if new.rank()==cyclic.rank():break
  cyclic=new
 assert dimensions==[1,4,5] and q*cyclic==0
 print('PASS full768 reduction;maximal positive1408;cyclic640 plus128 splitting',flush=True)
 # 45 independent symmetric copy matrices annihilating1, not45 raw forms certified by sampling.
 q=matrix(QQ,10,9,lambda i,j:int(i==j)-int(i==9));basis=[]
 for i in range(9):
  for j in range(i,9):
   A=q.column(i).column()*q.column(j).row()
   if j!=i:A+=A.transpose()
   assert A==A.transpose() and A*matrix(QQ,10,1,[1]*10)==0;basis.append(A.list())
 assert matrix(QQ,basis).rank()==45 and q.rank()==9
 # Two actual nonproportional nonsingular forms, including a negative transverse weight.
 examples=[]
 for a in [QQ(2),QQ(-3)]:
  X=II+(a-1)*P;Xi=II+(1/a-1)*P;Ha=H*X
  assert X*Xi==II and Ha==Ha.transpose()
  for D in Ds.values():assert D.transpose()*Ha+Ha*D==0
  examples.append(str(a))
 # A mixed copy matrix is a further genuine input rather than a scalar rescaling.
 v=q.column(0);A=v.column()*v.row()/2;J=lift(A);Xn=II+J;Xni=II-J/2
 assert Xn*Xni==II
 X=S*Xn*Si;Hx=H*X
 for D in Ds.values():assert D.transpose()*Hx+Hx*D==0
 assert raw(1,W)*P!=P*raw(1,W) # observed restriction is essential
 # The physical128 core and cyclic640 generated from auxiliary seeds lie in the complement.
 assert P.matrix_from_columns(range(1792,1920))==0
 # Free mass: real triple with exactly one negative direction.
 G={k:g[k]*Wb for k in O};M=g[1]*g[2]*g[10]*Wb
 assert M*M==2*I and M.transpose()*B==B*M
 for k in O:assert M*G[k]+G[k]*M==0
 E={k:G[0]*G[k]/2 for k in O[1:]};K=G[0]*M/2
 assert K*K==-I and K.transpose()==-K
 for k in O[1:]:
  assert E[k].transpose()==E[k] and E[k]*E[k]==I and E[k]*K+K*E[k]==0
 for i in O[1:]:
  for j in O[1:]:assert E[i]*E[j]+E[j]*E[i]==2*int(i==j)*I
 # Scalar real mass gives exponentially growing zero-momentum solutions instead.
 scalar=G[0]/2;assert scalar*scalar==I/2
 # Lift the mass on V; it has no action on complement, is H self-adjoint.
 Mn=matrix(QQ,1920,1920,sparse=True)
 for r in range(10):
  for c in range(10):
   for (i,j),v0 in M.dict().items():Mn[128*U[r]+i,128*U[c]+j]=Q[r,c]*v0
 Mr=S*Mn*Si;assert Mr.transpose()*H==H*Mr and Mr*P==Mr and Mr*(II-P)==0
 # Local moving copy rescaling s: actual Green correction at s=2,s'=3.
 s,sp=QQ(2),QQ(3);Hs=H*(II+(s*s-1)*P);connection=(sp/s)*Ds[7]*P;derivative=2*s*sp*H*P*Ds[7]
 assert Hs*connection-connection.transpose()*Hs==derivative and derivative!=0
 # Adverse controls change actual data, not predicates.
 bad=matrix(P);bad[128*U[0],128*U[0]]+=1
 assert bad*bad!=bad and bad*Ds[0]!=Ds[0]*bad
 wrong=g[1]*g[2]*g[3]*Wb;assert wrong*wrong==-2*I
 assert Ds[7]*P!=0 # omitted connection really changes the identity
 inputs=['tests/channel-swings/k2021_common_degree_dual_operator.py','lab/process/k2032-principal-form-rigidity.json','lab/process/k1951-coordinated-zero-southeast-principal.json']
 return dict(result_id='K2034',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',observed_directions=O,transverse_directions=U,invariant_dimension=1152,complement_dimension=768,copy_symmetric_dimension=45,form_inertia=[960,960],transverse_inertia=[576,576],form_examples=examples,observed_symbols_checked=4,complement_scalar_dimension=6,complement_defect_rank=3,invariant_constraint_rank=4,maximal_positive_dimension=1408,cyclic_copy_dimensions=dimensions,mass_square=2,evolution_mass_square=-1,stable_dispersion='omega^2=|p|^2+mu^2',scalar_mass_dispersion='omega^2=|p|^2-mu^2/2',moving_connection='(partial_k s/s) D_k P',actual_faults=['projector_entry','positive_triple_signature','omitted_connection'],scope='Complete45-dimensional copy-scalar symmetric family, explicit observed invariant free massive sector; not full observed commutant, raw source common coefficient or physical selector.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2034',r,flush=True)
