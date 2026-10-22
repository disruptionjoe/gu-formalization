"""Exact observed raw-slot support required by the fixed K1840 mass observation."""
import argparse,hashlib,json,itertools
from pathlib import Path
from sage.all import QQ,matrix,vector,block_matrix,identity_matrix,block_diagonal_matrix,diagonal_matrix
from k1824_k77_joint_observed_symbol_algebra import tensor
from k1836_k77_differential_dirac_quotient import mat,enc,clifford
ROOT=Path(__file__).resolve().parents[2]
INPUTS=['lab/process/k1945-energy-compatible-raw-columns.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1832-k77-common-energy-form.json','lab/process/k1828-k77-raw-zero-form-completion.json']
OUT=ROOT/'lab/process/k1947-minimal-raw-input-support.json'
def constant_support(r,m,en):
 from sage.all import PolynomialRing,NumberField
 RR=PolynomialRing(QQ,'a');a=RR.gen();poly=a*a-QQ(23762432)/1579905*a+QQ(227569762304)/5758753725;field=NumberField(poly,'q');qroot=field.gen()
 def ef(X):
  return {'rows':int(X.nrows()),'columns':int(X.ncols()),'entries':[[int(i),int(j),[str(field(x)[k]) for k in range(2)]] for (i,j),x in sorted(X.dict().items())]}
 checks={};rows=[];d=[z/24 for z in clifford()]
 def ck(k,x):checks[k]=bool(x);assert x,k
 ck('real_roots_in_3_4_and_11_12',poly(3)>0 and poly(4)<0 and poly(11)<0 and poly(12)>0)
 ck('strict_positive_Gram_gap',poly(QQ(27)/8)>0 and poly(QQ(7)/2)<0 and QQ(185877504)/3671875*QQ(27)/8-QQ(3098415744)/18359375==QQ(38267136)/18359375)
 for typ in range(4):
  b=next(b for b in r['blocks'] if b['type']==typ);F=mat(b['basis']);T=list(map(mat,b['T']));H=mat(b['H']);A=list(map(mat,en['blocks'][typ]['matrices']));Bs=[mat(t['B']) for t in m['blocks'][typ]['repairs']]
  for slots in itertools.chain(itertools.combinations(range(5),1),itertools.combinations(range(5),2)):
   fullq=F.matrix_from_rows([i for i,g in enumerate(b['coordinates']) if g//128 in slots]);piv=list(fullq.transpose().pivots());Q=fullq.matrix_from_rows(piv);N=H.inverse()*Q.transpose();cb=[]
   for i in range(Q.nrows()):
    for j in range(i+1,Q.nrows()):
     z=matrix(QQ,Q.nrows(),Q.nrows());z[i,j]=1;z[j,i]=-1;cb.append(N*z*Q)
   cols=[sum([(t*c).list() for t in T],[]) for c in cb]
   for row in range(4):
    for col in range(16):
     S=matrix(QQ,4,16);S[row,col]=1;cols.append(sum([(S*A[i]-d[i]*S).list() for i in range(3)],[]))
   cols += [sum([(-B*t).list() for t in T],[]) for B in Bs]
   E=matrix(QQ,cols).transpose();K=E.right_kernel().basis_matrix();rec={'type':typ,'slots':list(slots),'input_basis':enc(Q),'equation_shape':[int(E.nrows()),int(E.ncols())],'kernel':enc(K),'mass_projection_dimension':int(K[:,-2:].rank())}
   triples=[]
   for vv in K.rows():
    C=sum((vv[j]*cb[j] for j in range(len(cb))),matrix(QQ,16,16));S=matrix(QQ,4,16,vv[len(cb):len(cb)+64]);B=sum((vv[-2+j]*Bs[j] for j in range(2)),matrix(QQ,4,4));triples.append((C,B,S))
   if slots==(0,4):
    L=E[:,:-2];v0=L.solve_right(-E.column(E.ncols()-2));ker=L.right_kernel().basis_matrix();ck(f'constant_affine_ten_{typ}',ker.nrows()==10)
    zz=vector(field,[0]*10);zz[2]=qroot;zz[7]=qroot;den=2000 if typ in [0,3] else 4000;num=QQ(163904)/16875 if typ in [0,3] else QQ(81952)/16875;zz[4]=num-QQ(6987)/den*qroot
    vv=vector(field,list(v0))+zz*ker;C=sum((vv[j]*cb[j] for j in range(len(cb))),matrix(field,16,16));S=matrix(field,4,16,vv[len(cb):len(cb)+64]);B=Bs[0].change_ring(field)
    ck(f'constant_real_energy_{typ}',H*C+C.transpose()*H==0 and B+B.transpose()==0)
    ck(f'constant_real_intertwiner_{typ}',all(T[i]*C-B*T[i]+S*A[i]-d[i]*S==0 for i in range(3)) and S*C==B*S)
    kn=Q.right_kernel().basis_matrix().transpose();ck(f'constant_two_slot_support_{typ}',C*kn==0)
    ck(f'constant_zero_frequency_observed_{typ}',S.rank()==4)
    ck(f'nonuniversal_profile_{typ}',T[0]*C-d[0]*S!=0)
    # Explicit raw right-factor, with the SAME physical input rows.
    select=list(Q.pivots());R=matrix(QQ,16,Q.nrows(),{(j,i):1 for i,j in enumerate(select)})*Q.matrix_from_columns(select).inverse();W=C*R;ck(f'constant_raw_factor_{typ}',W*Q==C)
    rec['constant_witness']={'C':ef(C),'B':ef(B),'S':ef(S),'factor':ef(W)}
    Hi=H.inverse();alpha=QQ(138)/25;beta=QQ(185877504)/3671875*qroot-QQ(3098415744)/18359375
    ck(f'full_frequency_principal_Gram_{typ}',all(T[i]*Hi*T[i].transpose()==alpha*identity_matrix(QQ,4) for i in range(3)) and all(T[i]*Hi*T[j].transpose()+T[j]*Hi*T[i].transpose()==0 for i in range(3) for j in range(i+1,3)))
    ck(f'full_frequency_no_linear_Gram_{typ}',all(T[i]*Hi*S.transpose()-S*Hi*T[i].transpose()==0 for i in range(3)))
    ck(f'full_frequency_positive_constant_Gram_{typ}',S*Hi*S.transpose()==beta*identity_matrix(field,4))
    rec['Gram']={'alpha':str(alpha),'beta_coefficients':[str(beta[k]) for k in range(2)],'strict_beta_lower_bound':'38267136/18359375'}
    # Constant rotations produce the whole mass plane if source symmetry preserves support.
    Jt=d[0]*d[1]*d[2]*24**3;Js=mat(en['blocks'][typ]['J'])
    if T[0]*Js==-Jt*T[0]:Js=-Js
    ck(f'constant_mass_rotation_{typ}',all(T[i]*Js==Jt*T[i] and Js*A[i]==A[i]*Js for i in range(3)) and H*Js+Js.transpose()*H==0 and Js*Js==-identity_matrix(QQ,16) and Jt*Bs[0] in [Bs[1],-Bs[1]] and Q*Js*kn==0)
    rec['source_complex_structure']=enc(Js);rec['mass_rotation_sign']=1 if Jt*Bs[0]==Bs[1] else -1
   elif not K.nrows():rec['disposition']='first_order_zero';ck(f'linear_exclusion_{typ}_{slots}',K.nrows()==0)
   else:
    coeff=[];target=[]
    for i in range(K.nrows()):
     for j in range(i,K.nrows()):
      C,B,S=triples[i];Cc,Bb,Ss=triples[j];res=S*Cc-B*Ss
      if i!=j:res+=Ss*C-Bb*S
      coeff.append(res.list());target.append(sum(K[i,-2+t]*K[j,-2+t] for t in range(2))*(1 if i==j else 2))
    V=matrix(QQ,coeff);goal=vector(QQ,target);ell=V.solve_right(goal);ck(f'constant_mass_exclusion_{typ}_{slots}',V*ell==goal)
    rec['disposition']='constant_mass_zero';rec['mass_square_functional']=list(map(str,ell))
   rows.append(rec)
 return {'quadratic_polynomial':[str(poly[i]) for i in range(3)],'rows':rows,'scope':'Single-copy two-input classification with target B in fixed mass plane and free S; block-diagonal full32 witness. No all-cross-copy exclusion for the other nine pairs.','checks':checks}

def produce():
 r,m,en,raw=[json.loads((ROOT/p).read_text()) for p in INPUTS];checks={};blocks=[];d=[z/24 for z in clifford()]
 def ck(k,x):checks[k]=bool(x);assert x,k
 for typ in range(4):
  b=next(b for b in r['blocks'] if b['type']==typ);F=mat(b['basis']);H=mat(b['H']);T=list(map(mat,b['T']));A=list(map(mat,en['blocks'][typ]['matrices']));stack=block_matrix([[x] for x in T]);K=stack.right_kernel().basis_matrix().transpose();ck(f'invisible_dimension_{typ}',K.ncols()==4)
  invisible=[]
  for i in range(4):
   for j in range(i+1,4):
    z=matrix(QQ,4,4);z[i,j]=1;z[j,i]=-1;invisible.append(K*z*K.transpose()*H)
  # Verify these are ALL conservative C changes with fixed B,S.
  hs=[];Hi=H.inverse()
  for i in range(16):
   for j in range(i+1,16):
    z=matrix(QQ,16,16);z[i,j]=1;z[j,i]=-1;hs.append(Hi*z)
  E=matrix(QQ,[(stack*c).list() for c in hs]).transpose()
  ck(f'complete_invisible_space_{typ}',E.right_nullity()==6 and matrix(QQ,[c.list() for c in invisible]).rank()==6 and all(stack*c==0 and H*c+c.transpose()*H==0 for c in invisible))
  ck(f'forced_observation_principal_{typ}',A[0].rank()==16 and T[0]*A[0]==d[0]*T[0])
  repairs=m['blocks'][typ]['repairs'];cs=[mat(t['C']) for t in repairs];ss=[mat(t['S']) for t in repairs];bs=[mat(t['B']) for t in repairs]
  for a,(C,S,B) in enumerate(zip(cs,ss,bs)):
   ck(f'universal_profile_forces_S_{typ}_{a}',S==B*T[0]*A[0].inverse() and B*d[0]+d[0]*B==0)
   ck(f'fixed_repair_{typ}_{a}',H*C+C.transpose()*H==0 and all(T[i]*C-B*T[i]+S*A[i]-d[i]*S==0 for i in range(3)) and T[0]*C==d[0]*S and S*C==B*S)
  ck(f'cross_profile_{typ}',ss[0]*cs[1]+ss[1]*cs[0]==bs[0]*ss[1]+bs[1]*ss[0])
  subsets=[]
  for mask in range(1,32):
   ids=[i for i,g in enumerate(b['coordinates']) if mask&(1<<(g//128))];Q=F.matrix_from_rows(ids);kn=Q.right_kernel().basis_matrix().transpose();AA=matrix(QQ,[(c*kn).list() for c in invisible]).transpose();MM=matrix(QQ,[(c*kn).list() for c in cs]).transpose()
   ok=mask in (23,27,29,30,31);rec={'mask':mask,'slots':[i for i in range(5) if mask&(1<<i)],'Q':enc(Q),'kernel':enc(kn),'feasible_mass_dimension':2 if ok else 0}
   if ok:
    ck(f'complete_input_{typ}_{mask}',Q.rank()==16)
    # A canonical right-factor uses the first independent rows for the redundant five-slot case.
    piv=list(Q.transpose().pivots());qi=Q.matrix_from_rows(piv);selector=matrix(QQ,16,Q.nrows(),{(i,j):1 for i,j in enumerate(piv)});Ws=[c*qi.inverse()*selector for c in cs]
    ck(f'factorization_{typ}_{mask}',all(W*Q==C for W,C in zip(Ws,cs)))
    rec['factors']=list(map(enc,Ws))
   else:
    # A dual obstruction proves every mass combination fails, despite all invisible choices.
    joined=AA.augment(MM);rhs=matrix(QQ,8,2,{(6,0):1,(7,1):1});dual=joined.transpose().solve_right(rhs).transpose()
    ck(f'no_nonzero_mass_{typ}_{mask}',dual*AA==0 and dual*MM==identity_matrix(QQ,2))
    rec['rejection_dual']=enc(dual)
   subsets.append(rec)
  blocks.append({'type':typ,'invisible_basis':list(map(enc,invisible)),'invisible_kernel':enc(K),'subsets':subsets})
 # Global observed-slot lift on every actual copy, preserving its coordinate ordering.
 F=mat(r['basis']);allc=[block_diagonal_matrix([mat(m['blocks'][b['type']]['repairs'][a]['C']) for b in r['blocks']],sparse=True) for a in range(2)];global_lifts=[]
 for mask in (23,27,29,30):
  ids=[g for g in range(640) if mask&(1<<(g//128))];Q=F.matrix_from_rows(ids);Qi=Q.inverse();W=[C*Qi for C in allc]
  ck(f'global_inverse_{mask}',Qi*Q==identity_matrix(QQ,512))
  ck(f'global_factors_{mask}',all(w*Q==c for w,c in zip(W,allc)))
  # Store compressed factors, not a large redundant ambient matrix.
  global_lifts.append({'mask':mask,'input_rows':ids,'inverse':enc(Qi),'factors':list(map(enc,W))})
 # Hidden raw input slots collapse to the time-slot information on this graph.
 I2=identity_matrix(QQ,2);x=matrix(QQ,[[0,1],[1,0]]);z=diagonal_matrix(QQ,[1,-1]);eps=matrix(QQ,[[0,1],[-1,0]])
 gs=[tensor([z]*j+[a]+[I2]*(6-j)) for a in [x,eps] for j in range(7)];eta=[1]*7+[-1]*7
 observed=[0,7,8,9];Fs=[F[128*i:128*(i+1),:] for i in range(4)]
 ck('actual_corrected_gamma_trace',sum((eta[a]*gs[a]*Fs[i] for i,a in enumerate(observed)),matrix(QQ,128,512))==0)
 hidden=[]
 for a in range(14):
  if a in observed:continue
  actual=sum((-eta[a]*gs[a]*gs[b]*Fs[i]/20 for i,b in enumerate(observed)),matrix(QQ,128,512));E=-eta[a]*gs[a]*gs[0]/10;Ei=-10*gs[0]*gs[a]
  ck(f'hidden_input_time_equivalence_{a}',actual==E*Fs[0] and E*Ei==identity_matrix(QQ,128)==Ei*E)
  hidden.append({'ambient_slot':a,'time_transport':enc(E),'inverse':enc(Ei)})
 # Every ambient subset is equivalent to its represented five information classes.
 amap=[0 if a not in [7,8,9,14] else {7:1,8:2,9:3,14:4}[a] for a in range(15)]
 minimal=[]
 for chosen in itertools.combinations(range(15),4):
  cmask=sum(1<<c for c in set(amap[a] for a in chosen))
  if cmask in [23,27,29,30]:minimal.append(list(chosen))
 ck('34_minimal_ambient_supports',len(minimal)==34 and all(14 in a for a in minimal))
 constant=constant_support(r,m,en)
 checks.update(constant['checks'])
 return {'result_id':'K1947','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','scope':'All15 raw input slots of the fixed K1828 graph; fixed K1840 target B,S; all conservative invisible corrections allowed. Not native full20 action.','slot_names':['psi0','psi7','psi8','psi9','nu'],'blocks':blocks,'constant_mass_free_observation':constant,'global_lifts':global_lifts,'hidden_input_transports':hidden,'ambient_information_classes':amap,'minimal_ambient_supports':minimal,'results':{'minimum_observed_slots':4,'minimum_ambient_slots':4,'minimal_ambient_support_count':34,'minimal_masks':[23,27,29,30],'auxiliary_slot_required':True,'additional_one_form_slots_required':3,'arbitrary_static_two_mass_profiles_preserved':True,'full20_source_identification':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1947',len(v['checks']),'exact matrix/support controls')
