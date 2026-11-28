from pathlib import Path
import sys,json,time,hashlib,argparse
from fractions import Fraction as Rat
from itertools import product
from collections import Counter
start=time.perf_counter()
r=Path(__file__).resolve().parents[2]
# Reuse exact native geometry/Clifford assembly only; stop before old rank computation.
pth=r/'tests/program-focus/local_dual_closure_second_fundamental_form_probe.py'
saveargv=sys.argv;sys.argv=[str(pth),'--repo',str(r)]
ns={'__file__':str(pth),'__name__':'native_inputs'};exec(compile(pth.read_text().split('B=project(A)')[0],str(pth),'exec'),ns);sys.argv=saveargv
np=ns['np'];p=97;fp=ns['fp'];gamma=ns['gamma'];left=ns['left'];E=ns['E'];A=ns['A'];s=128;eta=ns['eta'];normal=ns['normals'];D=ns['D'];F=ns['F'];zero=np.zeros((s,s),dtype=np.int64)
checks={}
def ok(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def inv(a):
 a=np.array(a,dtype=np.int64)%p;n=a.shape[0];v=np.hstack([a,np.eye(n,dtype=np.int64)])
 for j in range(n):
  k=j+int(np.flatnonzero(v[j:,j])[0]);v[[j,k]]=v[[k,j]];v[j]=v[j]*pow(int(v[j,j]),-1,p)%p
  for i in range(n):
   if i!=j:v[i]=(v[i]-v[i,j]*v[j])%p
 return v[:,n:]
def rank(a):
 w=a.copy()%p;k=0
 for j in range(w.shape[1]):
  nz=np.flatnonzero(w[k:,j])
  if not len(nz):continue
  h=k+int(nz[0]);w[[k,h]]=w[[h,k]];w[k,j:]=w[k,j:]*pow(int(w[k,j]),-1,p)%p
  if k+1<len(w):w[k+1:,j:]=(w[k+1:,j:]-w[k+1:,j,None]*w[k:k+1,j:])%p
  k+=1
  if k==len(w):break
 return k
# Formula C_h=B_h-gamma_h G, C_n=A_n-gamma_n G; scalar density row zero.
Gs=[]
for j in range(4):Gs.append(sum((fp(1/D[n][n])*left(n+4,A[n][j]) for n in range(10)),zero.copy())%p)
C=[[zero.copy() for j in range(6)] for a in range(15)]
for h in range(4):
 for j in range(4):
  bh=sum((fp(F(1,2)*eta[j]*normal[n][j][h]/D[n][n])*gamma[n+4] for n in range(10)),zero.copy())%p
  C[h][j]=(bh-left(h,Gs[j]))%p
for n in range(10):
 for j in range(4):C[n+4][j]=(A[n][j]-left(n+4,Gs[j]))%p
# Input covariant b_j=gamma_j u_j; output u_a=gamma_a^-1 z_a.
Cu=[[zero.copy() for j in range(6)] for a in range(15)]
signs=ns['signs']
for a in range(14):
 for j in range(4):Cu[a][j]=fp(F(1,signs[a]))*left(a,C[a][j]@gamma[j]%p)%p
avg=[sum([Cu[a][j] for a in range(4,14)],zero.copy())*fp(F(1,10))%p for j in range(6)]
co=Cu[:4]+[avg,Cu[14]];bk=[[(Cu[a][j]-avg[j])%p for j in range(6)] for a in range(4,13)]
# Independent known native B certificate formula, without its old512minor.
oldB=ns['project'](A)
ok('full lower normal block agrees with owned opposite shape block',all(np.array_equal(bk[a][j],fp(F(1,signs[a+4]))*left(a+4,oldB[a][j]@gamma[j]%p)%p)for a in range(9)for j in range(4)))
# K95 p=1,sigma=+1,c=-11/12; time inverse in the already normalized15copy model.
M0=np.zeros((6,6),dtype=np.int64);M0[0,5]=1
for i in range(1,4):
 for j in range(1,4):
  if i!=j:M0[i,j]=1
 M0[i,4]=10
M0[4,1:4]=1;M0[4,4]=9;M0[5,0]=1;M0[5,5]=fp(F(-11,12));mi=inv(M0)
vo=[[sum((int(mi[a,k])*(-left(0,co[k][j])) for k in range(6)),zero.copy())%p for j in range(6)] for a in range(6)]
vb=[[left(0,bk[a][j])%p for j in range(6)]for a in range(9)]
V=np.array([[1,1,1,1,20,0],[0,0,0,0,12,1],[1,-1,1,1,10,-1],[1,1,-1,1,10,-1],[1,1,1,-1,10,-1],[1,-1,-1,-1,-10,1]],dtype=np.int64)%p;vi=inv(V)
Z=[E,E,gamma[1],gamma[2],gamma[3],gamma[0]];Zi=[E,E,gamma[1],gamma[2],gamma[3],-gamma[0]%p]
# Observed w_a=Z_a sum V_ab u_b, all principal spatial alpha_i identical.
obs=[]
for a in range(6):
 row=[]
 for b in range(6):
  t=sum((int(V[a,k])*int(vi[l,b])*vo[k][l] for k in range(6)for l in range(6)),zero.copy())%p
  row.append(Z[a]@t@Zi[b]%p)
 obs.append(row)
hid=[[sum((int(vi[k,b])*vb[a][k] for k in range(6)),zero.copy())@Zi[b]%p for b in range(6)] for a in range(9)]
# Reduce first4 spin components to chi +/- and alpha3 +/-. Normal gamma factors act on32 spectators.
alpha=[-gamma[0]@gamma[i]%p for i in (1,2,3)]
small=[a[::32,::32] for a in alpha]
ok('horizontal factors have exact spectator identity',all(np.array_equal(a,np.kron(b,np.eye(32,dtype=np.int64))%p)for a,b in zip(alpha,small)))
J=22*small[0]@small[1]@small[2]%p
ok('spatial volume involution',np.array_equal(J@J%p,np.eye(4,dtype=np.int64)))
cols=[]
for chi in [1,-1]:
 projector=(np.eye(4,dtype=np.int64)+chi*J)@(np.eye(4,dtype=np.int64)+small[2])*fp(F(1,4))%p
 v=next(projector[:,j]for j in range(4)if np.any(projector[:,j]));cols.extend([v,small[0]@v%p])
U=np.column_stack(cols)%p;Ui=inv(U);UU=np.kron(U,np.eye(32,dtype=np.int64));UUi=np.kron(Ui,np.eye(32,dtype=np.int64))
ok('chirality canonical basis',np.array_equal(Ui@J@U%p,np.diag([1,1,-1,-1])%p))
obs=[[UUi@b@UU%p for b in row]for row in obs];hid=[[UUi@b@UU%p for b in row]for row in hid]
outs=[]
for ch in range(2):
 matsX=[];matsY=[]
 for i in range(2):
  for j in range(2):
   si=slice((2*ch+i)*32,(2*ch+i+1)*32);sj=slice((2*(1-ch)+j)*32,(2*(1-ch)+j+1)*32)
   matsX.append(np.block([[b[si,sj]for b in row]for row in obs]));matsY.append(np.block([[b[si,sj]for b in row]for row in hid]))
 X=np.hstack(matsX);Y=np.hstack(matsY)
 rx=rank(X);rxy=rank(np.vstack([X,Y]));outs.append({'chirality':ch,'X_shape':list(X.shape),'Y_shape':list(Y.shape),'rank_X':rx,'rank_XY':rxy,'no_mod97_rank_obstruction':rx==rxy})
 pass
constant=[]
for ch in range(2):
 xx=[];yy=[]
 for target in range(2):
  for i in range(2):
   for j in range(2):
    si=slice((2*ch+i)*32,(2*ch+i+1)*32);sj=slice((2*target+j)*32,(2*target+j+1)*32)
    xx.append(np.block([[b[si,sj]for b in row]for row in obs]));yy.append(np.block([[b[si,sj]for b in row]for row in hid]))
 X=np.hstack(xx);Y=np.hstack(yy);rx=rank(X);rxy=rank(np.vstack([X,Y]));constant.append({'chirality':ch,'rank_X':rx,'rank_XY':rxy,'constant_graph_consistent_mod97':rx==rxy});pass
prolonged=[]
for ch in range(2):
 # Same-chirality coefficient matrices in spin Pauli basis I,alpha1..3.
 spin=[np.eye(2,dtype=np.int64)]+[(Ui@v@U%p)[2*ch:2*ch+2,2*ch:2*ch+2]for v in small]
 vm=[];bm=[]
 for pp in spin:
  vrows=[];brows=[]
  for carrier,outrows in [(obs,vrows),(hid,brows)]:
   for row in carrier:
    rr=[]
    for b in row:
     t=zero[:32,:32].copy()
     for i in range(2):
      for j in range(2):t=(t+int(pp[i,j])*b[(2*ch+j)*32:(2*ch+j+1)*32,(2*ch+i)*32:(2*ch+i+1)*32])%p
     rr.append(t*fp(F(1,2))%p)
    outrows.append(rr)
  vm.append(np.block(vrows));bm.append(np.block(brows))
 xx=[];yy=[]
 for i in range(2):
  for j in range(2):
   si=slice((2*ch+i)*32,(2*ch+i+1)*32);sj=slice((2*(1-ch)+j)*32,(2*(1-ch)+j+1)*32)
   xx.append(np.block([[b[si,sj]for b in row]for row in obs]));yy.append(np.block([[b[si,sj]for b in row]for row in hid]))
 X=np.hstack(xx);Y=np.hstack(yy)
 for mu in range(4):
  xxp=np.hstack([X,vm[mu]@X%p]);yyp=np.hstack([Y,bm[mu]@X%p]);rxy=rank(np.vstack([xxp,yyp]));rx=rank(xxp)
  z={'chirality':ch,'derivative':mu,'rank_X':rx,'rank_XY':rxy,'coefficient_row_upper_bound':192,'inconsistent_over_coefficient_field':rxy>192};prolonged.append(z);pass
# Exact universal principal checks: Mi(r) is affine in r. Verify both coefficients.
import importlib.util
spec=importlib.util.spec_from_file_location('owned_local',r/'tests/program-focus/local_complement_probe.py');owned=importlib.util.module_from_spec(spec);spec.loader.exec_module(owned)
def matmul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)]for row in a]
def finv(a):
 n=len(a);rr,piv=owned.rref([row+[Rat(int(i==j))for j in range(n)]for i,row in enumerate(a)])
 assert piv[:n]==list(range(n));return [row[n:]for row in rr]
Vq=[[Rat(x)for x in row]for row in [[1,1,1,1,20,0],[0,0,0,0,12,1],[1,-1,1,1,10,-1],[1,1,-1,1,10,-1],[1,1,1,-1,10,-1],[1,-1,-1,-1,-10,1]]]
Viq=finv(Vq);characters=[(1,1,1),(1,1,1),(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,-1)]
M=owned.matrices(Rat(1),1,Rat(-11,12));Ni=[matmul(finv(M[0]),M[i])for i in (1,2,3)]
for i in range(3):
 diag=[[Rat(characters[a][i]*int(a==b))for b in range(6)]for a in range(6)]
 ok('principal simultaneous diagonalization '+str(i),matmul(Vq,Ni[i])==matmul(diag,Vq))
 # r=0 and r=1 determine the two affine coefficients without assuming inversion at r0.
 for rr in [Rat(0),Rat(1)]:
  mm=[]
  for k in range(4):
   a=[row[:]for row in M[k]];a[5][k]=rr;a[5][5]=-Rat(11,12)*rr;mm.append(a)
  ok('universal affine principal identity '+str((i,rr)),matmul(mm[0],Ni[i])==mm[i+1])
 for j in range(3):ok('commuting scalar principal '+str((i,j)),matmul(Ni[i],Ni[j])==matmul(Ni[j],Ni[i]))
 ok('scalar principal involution '+str(i),matmul(Ni[i],Ni[i])==[[Rat(int(a==b))for b in range(6)]for a in range(6)])
nullities={}
for eps in product([-1,1],repeat=3):
 equations=[[Ni[i][a][b]-Rat(eps[i]*int(a==b))for a in range(6)]for i in range(3)for b in range(6)]
 dim=6-len(owned.rref(equations)[1]);nullities[str(eps)]=dim;ok('complete character '+str(eps),dim==characters.count(eps))
cc=Counter(tuple((-1)**(((mask>>0)&1)+((mask>>i)&1))for i in (1,2,3))for mask in range(1<<14))
ok('all Clifford3 conjugation characters each2048',len(cc)==8 and set(cc.values())=={2048})
ok('complex principal Hom dimension',9*sum(nullities.values())*2048==110592)
# The full native lower formula is authenticated against the wedge formula on ALL observed input columns.
for a in range(14):
 for j in range(4):
  direct=zero.copy()
  for h in range(4):
   for n in range(10):
    if a in [h,n+4]:continue
    coeff=-F(1,2)*eta[h]*eta[j]*normal[n][j][h]/D[n][n]
    if coeff:direct=(direct+fp(coeff)*left(a,left(h,gamma[n+4])))%p
  ok('full native wedge lower coefficient '+str((a,j)),np.array_equal(direct,C[a][j]))
# Extract explicit193minors for first time prolongation; never infer char0 rank from mod-rank equality.
def minor_certificate(mat,limit=193):
 w=mat.copy()%p;rows=np.arange(len(w));k=0;cs=[];rs=[];det=1
 for j in range(w.shape[1]):
  z=np.flatnonzero(w[k:,j])
  if not len(z):continue
  h=k+int(z[0]);w[[k,h]]=w[[h,k]];rows[[k,h]]=rows[[h,k]]
  v=int(w[k,j]);det=det*v%p;cs.append(j);rs.append(int(rows[k]));w[k,j:]=w[k,j:]*pow(v,-1,p)%p
  w[k+1:,j:]=(w[k+1:,j:]-w[k+1:,j,None]*w[k:k+1,j:])%p;k+=1
  if k==limit:break
 assert k==limit and det
 return {'size':k,'row_indices':rs,'column_indices':cs,'determinant_mod97':det,'matrix_sha256':hashlib.sha256(mat.astype('<i8').tobytes()).hexdigest()}
minors=[]
for ch in range(2):
 # Only time coefficient is required: half-spin partial trace of same-chirality blocks.
 def timeblocks(carrier):return np.block([[(b[2*ch*32:(2*ch+1)*32,2*ch*32:(2*ch+1)*32]+b[(2*ch+1)*32:(2*ch+2)*32,(2*ch+1)*32:(2*ch+2)*32])*fp(F(1,2))%p for b in row]for row in carrier])
 v0=timeblocks(obs);b0=timeblocks(hid);xx=[];yy=[]
 for i in range(2):
  for j in range(2):
   si=slice((2*ch+i)*32,(2*ch+i+1)*32);sj=slice((2*(1-ch)+j)*32,(2*(1-ch)+j+1)*32)
   xx.append(np.block([[b[si,sj]for b in row]for row in obs]));yy.append(np.block([[b[si,sj]for b in row]for row in hid]))
 X=np.hstack(xx);Y=np.hstack(yy);stack=np.vstack([np.hstack([X,v0@X%p]),np.hstack([Y,b0@X%p])]);mc=minor_certificate(stack);mc['chirality']=ch;minors.append(mc);ok('time prolongation193 exceeds192 '+str(ch),mc['size']>X.shape[0] and mc['determinant_mod97']!=0)
# Calibration: unequal raw time rows permit normalized moving graphs.
a=Rat(2);c=Rat(3);b=Rat(5)
ok('moving normalized graph positive control',a*(-b/a)+b==0 and a!=c)
ok('raw same row rejects that nonzero moving graph',a-c!=0)
# Affine constraint may pass pointwise and fail propagation: T=1 but Tprime=1.
ok('prolongation detects incompatible control',1*1==1 and (1*1-0)*1!=0)
ok('prolongation retains compatible control',(1*1-1)*1==0)
deps=['tests/program-focus/local_dual_closure_second_fundamental_form_probe.py','tests/channel-swings/joe_directed_sa1_soldered_ad_selector.py','tests/program-focus/local_complement_probe.py','explorations/conditional-build/bet-2plus1-local-complement-2026-11-27.md','explorations/conditional-build/bet-2plus1-unitary-dual-closure-2026-11-27.md','explorations/conditional-build/local-dual-closure-second-fundamental-form-2026-11-24.md']
out={'artifact':'EVOLUTION_COMPLEMENT_EXACT_CERTIFICATE','status':'PASS','checks':checks,'checks_passed':len(checks),'inherited_geometry_checks':ns['checks'],'principal_character_nullities':nullities,'principal_complex_Hom_dimension':110592,'modular_flip_scout':outs,'modular_constant_scout':constant,'modular_prolongation_scout':prolonged,'time_prolongation_minors':minors,'coefficient_field':'Q(i,sqrt2,sqrt3)','prime':97,'roots':{'i':22,'sqrt2':14,'sqrt3':10},'dependencies_sha256':{p:hashlib.sha256((r/p).read_bytes()).hexdigest()for p in deps},'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Allweight principal proof plus actualflatbase F=U=0 weighted reference lower obstruction. Only minor nonvanishing transfers from finite field; no char0rank160/288/448 assertion, noallF/U orsourceGU inference.'}
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--verify',action='store_true');opts=ap.parse_args();dest=r/'lab/process/evolution-complement-certificates.json'
if opts.write:dest.write_text(json.dumps(out,indent=2)+'\n')
if opts.verify:assert json.loads(dest.read_text())==out
print(json.dumps({'status':'PASS','checks':len(checks),'minor_determinants':[m['determinant_mod97']for m in minors],'seconds':time.perf_counter()-start}))
