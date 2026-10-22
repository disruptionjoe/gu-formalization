"""Independent kernel/dual-witness checks and genuine mathematical input faults."""
import json,hashlib,itertools
from copy import deepcopy
from pathlib import Path
from sage.all import QQ,GF,matrix,identity_matrix,block_matrix,vector
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'lab/process/k1947-minimal-raw-input-support.json'
def m(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def inspect(v,old,mass):
 count=0;en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());ob=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text())
 def ck(x,s):
  nonlocal count
  assert x,s
  count+=1
 for rec in v['blocks']:
  typ=rec['type'];b=next(z for z in old['blocks'] if z['type']==typ);F=m(b['basis']);H=m(b['H']);ts=list(map(m,b['T']));C=[m(z['C']) for z in mass['blocks'][typ]['repairs']];inv=list(map(m,rec['invisible_basis']));K=m(rec['invisible_kernel'])
  ck(K.ncols()==4 and K.change_ring(GF(1009)).rank()==4 and all(t*K==0 for t in ts),'invisible carrier')
  ck(block_matrix([[t] for t in ts]).change_ring(GF(1009)).rank()==12,'invisible carrier complete')
  ck(len(inv)==6 and matrix(QQ,[z.list() for z in inv]).change_ring(GF(1009)).rank()==6,'six independent skew freedoms')
  ck(all(H*z+z.transpose()*H==0 and all(t*z==0 for t in ts) for z in inv),'invisible conservative range')
  # Every H-skew map killed by T is supported on this four-dimensional carrier;
  # six independent skew maps therefore exhaust it without producer's linear system.
  ck(all(H*c+c.transpose()*H==0 for c in C),'mass coefficients preserve energy')
  a=m(en['blocks'][typ]['matrices'][0]);dd=m(ob['target_D'][0])/24
  ck(a.change_ring(GF(1009)).rank()==16 and ts[0]*a==dd*ts[0],'arbitrary-profile uniqueness premise')
  for repair in mass['blocks'][typ]['repairs']:ck(m(repair['S'])*a==m(repair['B'])*ts[0],'forced observation correction')
  ck(len(rec['subsets'])==31 and sorted(z['mask'] for z in rec['subsets'])==list(range(1,32)),'exhaustive31 support census')
  for sub in rec['subsets']:
   mask=sub['mask'];ids=[i for i,j in enumerate(b['coordinates']) if mask&(1<<(j//128))];q=F.matrix_from_rows(ids);kn=m(sub['kernel']);ck(m(sub['Q'])==q,'actual physical slot restriction')
   ck(q*kn==0 and q.change_ring(GF(1013)).rank()+kn.change_ring(GF(1013)).rank()==16 and kn.ncols()==kn.rank(),'complete forbidden-input kernel')
   if 'rejection_dual' in sub:
    A=matrix(QQ,[(z*kn).list() for z in inv]).transpose();M=matrix(QQ,[(z*kn).list() for z in C]).transpose();dual=m(sub['rejection_dual']);ck(dual*A==0 and dual*M==identity_matrix(QQ,2),'dual excludes every nonzero mass combination');ck(sub['feasible_mass_dimension']==0,'reported negative dimension')
   else:
    ck(q.change_ring(GF(1009)).rank()==16,'full input rank');ck(all(m(w)*q==c for w,c in zip(sub['factors'],C)),'actual constructive raw factors');ck(sub['feasible_mass_dimension']==2,'reported feasible dimension')
  feasible=[s['mask'] for s in rec['subsets'] if s['feasible_mass_dimension']==2];ck(feasible==[23,27,29,30,31],'exact support classification')
 F=m(old['basis'])
 for lift in v['global_lifts']:
  ids=[g for g in range(640) if lift['mask']&(1<<(g//128))];q=F.matrix_from_rows(ids);ck(ids==lift['input_rows'] and m(lift['inverse'])*q==identity_matrix(QQ,512),'global input inverse')
  for a,w in enumerate(lift['factors']):
   c=m(w)*q
   ck(all(c[16*i:16*(i+1),16*j:16*(j+1)]==(m(mass['blocks'][b['type']]['repairs'][a]['C']) if i==j else matrix(QQ,16,16)) for i,b in enumerate(old['blocks']) for j in range(32)),'full32 actual mass lift')
 # Bit-index Clifford construction is independent of the producer tensor code.
 gs=[]
 for family in range(2):
  for pos in range(7):
   entries={}
   for col in range(128):
    bit=1<<(6-pos);prefix=col>>(7-pos);sign=(-1)**prefix.bit_count()
    if family:sign*=1 if col&bit else -1
    entries[(col^bit,col)]=sign
   gs.append(matrix(QQ,128,128,entries))
 eta=[1]*7+[-1]*7;obs=[0,7,8,9];parts=[F[128*i:128*(i+1),:] for i in range(4)]
 ck(sum((eta[a]*gs[a]*parts[i] for i,a in enumerate(obs)),matrix(QQ,128,512))==0,'independent corrected trace')
 for h in v['hidden_input_transports']:
  a=h['ambient_slot'];actual=sum((-eta[a]*gs[a]*gs[b]*parts[i]/20 for i,b in enumerate(obs)),matrix(QQ,128,512));E,Ei=m(h['time_transport']),m(h['inverse'])
  ck(actual==E*parts[0] and E*Ei==identity_matrix(QQ,128)==Ei*E,'actual hidden-slot transport')
 amap=[{7:1,8:2,9:3,14:4}.get(i,0) for i in range(15)];ck(v['ambient_information_classes']==amap,'actual ambient information classes')
 feasible_masks={23,27,29,30,31};minimum=[];classified=0
 for mask in range(1,1<<15):
  chosen=[a for a in range(15) if mask&(1<<a)];effective=sum(1<<a for a in set(amap[i] for i in chosen));feasible=effective in feasible_masks
  assert not(feasible and len(chosen)<4),'smaller ambient support'
  if feasible and len(chosen)==4:minimum.append(chosen)
  classified+=1
 ck(sorted(minimum)==sorted(v['minimal_ambient_supports']) and len(minimum)==34,'all32767 ambient subsets classified')
 count+=audit_constant(v,old,mass)
 ck(v['results']['minimum_observed_slots']==4 and v['results']['minimal_masks']==[23,27,29,30],'minimum report')
 return count
def audit_constant(v,old,mass):
 from sage.all import PolynomialRing
 data=v['constant_mass_free_observation'];R=PolynomialRing(QQ,'x');x=R.gen();p=sum(QQ(a)*x**i for i,a in enumerate(data['quadratic_polynomial']));alpha=-p[0];beta=-p[1];count=0
 def ck(b,msg):
  nonlocal count
  assert b,msg
  count+=1
 ck(p.degree()==2 and p[2]==1 and p.discriminant()>0 and not p.discriminant().is_square(),'real quadratic field')
 ck(p(3)>0 and p(4)<0 and p(11)<0 and p(12)>0,'two real embedding intervals')
 def fm(z):
  return tuple(matrix(QQ,z['rows'],z['columns'],{(i,j):QQ(t[k]) for i,j,t in z['entries']}) for k in [0,1])
 def mul(a,b):return (a[0]*b[0]+alpha*a[1]*b[1],a[0]*b[1]+a[1]*b[0]+beta*a[1]*b[1])
 def sub(a,b):return tuple(z-t for z,t in zip(a,b))
 def left(T,z):return tuple(T*a for a in z)
 def right(z,T):return tuple(a*T for a in z)
 def zero(z):return all(a==0 for a in z)
 en=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());obs=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());d=[m(a)/24 for a in obs['target_D']]
 ck(len(data['rows'])==60,'complete single and pair input census')
 for rec in data['rows']:
  typ=rec['type'];b=next(z for z in old['blocks'] if z['type']==typ);F=m(b['basis']);H=m(b['H']);A=list(map(m,en['blocks'][typ]['matrices']));T=list(map(m,obs['blocks'][typ]['T']));Bs=[m(z['B']) for z in mass['blocks'][typ]['repairs']];Q=m(rec['input_basis']);q0=F.matrix_from_rows([i for i,g in enumerate(b['coordinates']) if g//128 in rec['slots']]);ck(Q.row_space()==q0.row_space() and Q.nrows()==Q.rank(),'actual independent input rows')
  N=H.inverse()*Q.transpose();pairs=list(itertools.combinations(range(Q.nrows()),2));nC=len(pairs);E=matrix(QQ,192,nC+66)
  for axis in range(3):
   TN=T[axis]*N
   for a in range(4):
    for bcol in range(16):
     row=64*axis+16*a+bcol
     for k,(u,w) in enumerate(pairs):E[row,k]=TN[a,u]*Q[w,bcol]-TN[a,w]*Q[u,bcol]
     for sr in range(4):
      for sc in range(16):E[row,nC+16*sr+sc]=(A[axis][sc,bcol] if sr==a else 0)-(d[axis][a,sr] if sc==bcol else 0)
     for j in range(2):E[row,nC+64+j]=-(Bs[j]*T[axis])[a,bcol]
  K=m(rec['kernel']);ck([E.nrows(),E.ncols()]==rec['equation_shape'],'independent free-observation row dimensions');ck(E*K.transpose()==0 and K.change_ring(GF(1009)).rank()==K.nrows() and E.change_ring(GF(1013)).rank()==E.ncols()-K.nrows(),'complete free-observation kernel')
  if 'constant_witness' in rec:
   w=rec['constant_witness'];C,B,S,W=[fm(w[k]) for k in ['C','B','S','factor']];ck(B[0]==Bs[0] and B[1]==0,'prescribed nonzero mass');ck(zero(tuple(H*c+c.transpose()*H for c in C)),'algebraic source energy')
   for i in range(3):ck(zero(tuple(T[i]*C[k]-B[k]*T[i]+S[k]*A[i]-d[i]*S[k] for k in [0,1])),'algebraic first-order intertwiner')
   ck(zero(sub(mul(S,C),mul(B,S))),'algebraic quadratic intertwiner');ck(right(W,Q)==C,'algebraic physical raw support');ck(not zero(sub(left(T[0],C),left(d[0],S))),'constant construction not universal-profile')
   Sm=matrix(R,4,16,[S[0][i,j]+x*S[1][i,j] for i in range(4) for j in range(16)]);cols=Sm.change_ring(R.fraction_field()).pivots();ck(len(cols)==4 and Sm.matrix_from_columns(cols).det()%p!=0,'constant target surjectivity both real embeddings')
   Hi=H.inverse();alphaG=QQ(rec['Gram']['alpha']);betaG=tuple(QQ(t) for t in rec['Gram']['beta_coefficients']);I4=identity_matrix(QQ,4)
   ck(all(T[i]*Hi*T[i].transpose()==alphaG*I4 for i in range(3)) and all(T[i]*Hi*T[j].transpose()+T[j]*Hi*T[i].transpose()==0 for i in range(3) for j in range(i+1,3)),'exact principal observation Gram')
   ck(all(T[i]*Hi*S[k].transpose()-S[k]*Hi*T[i].transpose()==0 for i in range(3) for k in [0,1]),'zero linear observation Gram')
   ck(mul(right(S,Hi),tuple(a.transpose() for a in S))==tuple(a*I4 for a in betaG),'positive constant observation Gram')
   ck(p(QQ(27)/8)>0 and p(QQ(7)/2)<0 and betaG[1]>0 and betaG[0]+betaG[1]*QQ(27)/8==QQ(rec['Gram']['strict_beta_lower_bound'])>0,'both embeddings uniform positive gap')
   Js=m(rec['source_complex_structure']);Jt=d[0]*d[1]*d[2]*24**3;kn=Q.right_kernel().basis_matrix().transpose();ck(all(T[i]*Js==Jt*T[i] and Js*A[i]==A[i]*Js for i in range(3)) and H*Js+Js.transpose()*H==0 and Q*Js*kn==0 and Jt*Bs[0]==rec['mass_rotation_sign']*Bs[1],'mass-plane rotation preserves exact input support')
  elif rec['disposition']=='first_order_zero':ck(K.nrows()==0,'linear zero space')
  else:
   triples=[]
   for vv in K.rows():
    Z=matrix(QQ,Q.nrows(),Q.nrows())
    for k,(i,j) in enumerate(pairs):Z[i,j]=vv[k];Z[j,i]=-vv[k]
    C=N*Z*Q;B=vv[-2]*Bs[0]+vv[-1]*Bs[1];S=matrix(QQ,4,16,vv[nC:nC+64]);triples.append((C,B,S))
   ell=vector(QQ,list(map(QQ,rec['mass_square_functional'])))
   for i in range(K.nrows()):
    for j in range(i,K.nrows()):
     C,B,S=triples[i];D,G,U=triples[j];q=S*D-B*U
     if i!=j:q+=U*C-G*S
     goal=(K[i,-2]*K[j,-2]+K[i,-1]*K[j,-1])*(1 if i==j else 2);ck(ell*vector(QQ,q.list())==goal,'exact single-copy constant-mass exclusion')
 return count

def pins(v):
 assert v['result_id']=='K1947','report identity'
 for p,d in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'pin mismatch'
def main():
 v=json.loads(P.read_text());old=json.loads((ROOT/'lab/process/k1945-energy-compatible-raw-columns.json').read_text());mass=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());pins(v);n=inspect(v,old,mass);caught=[]
 for kind in ['restriction','dual','factor','mass','hidden','algebraic']:
  z=deepcopy(v);mm=deepcopy(mass)
  if kind=='restriction':target=z['blocks'][0]['subsets'][0]['Q']
  elif kind=='dual':target=z['blocks'][0]['subsets'][0]['rejection_dual']
  elif kind=='factor':target=z['global_lifts'][0]['factors'][0]
  elif kind=='mass':target=mm['blocks'][0]['repairs'][0]['C']
  elif kind=='hidden':target=z['hidden_input_transports'][0]['time_transport']
  else:target=next(x for x in z['constant_mass_free_observation']['rows'] if 'constant_witness' in x)['constant_witness']['C']
  if kind=='algebraic':target['entries'][0][2][0]=str(QQ(target['entries'][0][2][0])+1)
  else:target['entries'][0][2]=str(QQ(target['entries'][0][2])+1)
  try:inspect(z,old,mm)
  except AssertionError as e:caught.append(str(e))
 assert len(caught)==6,'mathematical failure path'
 consistency=[]
 for kind in ['report','pin']:
  z=deepcopy(v)
  if kind=='report':z['result_id']='K0'
  else:z['inputs'][next(iter(z['inputs']))]='0'*64
  try:pins(z)
  except AssertionError as e:consistency.append(str(e))
 assert len(consistency)==2
 print('PASS K1947',n,'independent exact controls; mathematical faults:',caught,'consistency:',consistency)
if __name__=='__main__':main()
