"""Exact fixed-energy raw-column classification on the existing K77 fixture."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,GF,matrix,identity_matrix,diagonal_matrix,block_matrix,block_diagonal_matrix,prod,vector,PolynomialRing,zero_vector
from k1824_k77_joint_observed_symbol_algebra import build_family,tensor
from k1836_k77_differential_dirac_quotient import mat,enc,clifford
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1945-energy-compatible-raw-columns.json'
def build():
    P,f,ck,g0=build_family(); n=640
    adj=[set() for _ in range(n)]
    for M in [P]+f:
     for i,j in M.dict():adj[i].add(j);adj[j].add(i)
    seen=set();cs=[]
    for s in range(n):
     if s in seen:continue
     todo=[s];c=set()
     while todo:
      v=todo.pop()
      if v in c:continue
      c.add(v);todo.extend(adj[v]-c)
     seen.update(c);cs.append(sorted(c))
    src=json.load(open(ROOT/'lab/process/k1832-k77-common-energy-form.json'));obs=json.load(open(ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json'))
    Bs=[];Hs=[];Qs=[];As=[];Ts=[];records=[]
    for ix,c in enumerate(cs):
     pb=P.matrix_from_rows_and_columns(c,c);B=pb.matrix_from_columns(pb.pivots());rr=B.transpose().pivots();Li=B.matrix_from_rows(rr).inverse();a=[Li*M.matrix_from_rows_and_columns(c,c).matrix_from_rows(rr)*B for M in f];typ=src['component_types'][ix];H=mat(src['blocks'][typ]['H']);assert a==list(map(mat,src['blocks'][typ]['matrices']))
     q=B.matrix_from_rows([j for j,s in enumerate(c) if s>=512]); assert q.nrows()==4
     hiq=H.inverse()*q.transpose();t=list(map(mat,obs['blocks'][typ]['T']));stack=block_matrix([[x] for x in t]);
     records.append({'coordinates':c,'type':typ,'basis':enc(B),'Q':enc(q),'H':enc(H),'T':list(map(enc,t))})
     Bs.append(B);Hs.append(H);Qs.append(q);As.append(a);Ts.append(t)
    # 640 observed coordinates ->512 basis injection, and correct global zero retraction.
    Lb=matrix(QQ,640,512,{(c[r],16*k+j):v for k,(c,B) in enumerate(zip(cs,Bs)) for (r,j),v in B.dict().items()},sparse=True)
    H=block_diagonal_matrix(Hs,sparse=True);Hi=block_diagonal_matrix([h.inverse() for h in Hs],sparse=True);Q=Lb[512:640,:]
    I2=identity_matrix(QQ,2);s1=matrix(QQ,[[0,1],[1,0]]);s3=diagonal_matrix(QQ,[1,-1]);ep=matrix(QQ,[[0,1],[-1,0]])
    gs=[tensor([s3]*j+[v]+[I2]*(6-j)) for v in [s1,ep] for j in range(7)];vol=prod(gs);I=identity_matrix(QQ,128);S=11*(I+vol)/48+11*(I-vol)/24;T=g0*S
    R=-Lb[:128,:]+T*Q;N=Hi*Q.transpose();M=R*N
    return {'blocks':records,'M':enc(M),'R':enc(R),'N':enc(N),'Q':enc(Q),'H':enc(H),'Traw':enc(T),'basis':enc(Lb),'fixture_checks':ck}

def cross_certificate(v):
    src=json.load(open(ROOT/'lab/process/k1832-k77-common-energy-form.json'));d=[x/24 for x in clifford()];records=[]
    for aa in range(4):
     for bb in range(aa,4):
      blocks=[next(b for b in v['blocks'] if b['type']==typ) for typ in [aa,bb]];q=[mat(b['Q']) for b in blocks];n=[mat(b['H']).inverse()*qi.transpose() for b,qi in zip(blocks,q)];ts=[list(map(mat,b['T'])) for b in blocks];a=[list(map(mat,src['blocks'][typ]['matrices'])) for typ in [aa,bb]]
      cols=[]
      for kind in range(4):
       size=16 if kind<2 else 64
       for k in range(size):
        Z=matrix(QQ,4,4);B=matrix(QQ,4,4);Sab=matrix(QQ,4,16);Sba=matrix(QQ,4,16)
        if kind==0:Z[k//4,k%4]=1
        elif kind==1:B[k//4,k%4]=1
        elif kind==2:Sab[k//16,k%16]=1
        else:Sba[k//16,k%16]=1
        Cab=n[0]*Z*q[1];Cba=-n[1]*Z.transpose()*q[0];Bab=B;Bba=-B.transpose()
        col=sum([(ts[0][i]*Cab-Bab*ts[1][i]+Sab*a[1][i]-d[i]*Sab).list() for i in range(3)],[])+sum([(ts[1][i]*Cba-Bba*ts[0][i]+Sba*a[0][i]-d[i]*Sba).list() for i in range(3)],[])
        cols.append(col)
      E=matrix(QQ,cols).transpose();ker=E.right_kernel();assert ker.dimension()==4, 'cross-copy first-order nullity'
      # Norm-square coefficient trace of residual products detects a positive definite linear functional if available.
      triples=[]
      for vs in ker.basis():
       Z=matrix(QQ,4,4,vs[:16]);B=matrix(QQ,4,4,vs[16:32]);Sab=matrix(QQ,4,16,vs[32:96]);Sba=matrix(QQ,4,16,vs[96:]);triples.append((n[0]*Z*q[1],-n[1]*Z.transpose()*q[0],B,-B.transpose(),Sab,Sba))
      quads=[]
      for i in range(len(triples)):
       for j in range(i,len(triples)):
        def pair(t,u):
         C,D,B,G,S,T=t;Cj,Dj,Bj,Gj,Sj,Tj=u
         return vector(QQ,(S*Dj-B*Tj).list()+(T*Cj-G*Sj).list())
        quads.append(pair(triples[i],triples[j])+(pair(triples[j],triples[i]) if i!=j else zero_vector(QQ,128)))
      coeff=matrix(QQ,quads).transpose();dim=len(triples)
      want=vector(QQ,[1 if i==j else 0 for i in range(dim) for j in range(i,dim)])
      assert want in coeff.row_space(), 'isolated pair real positivity'
      records.append({'types':[aa,bb],'dimension':dim,'equations':enc(E),'kernel':[list(map(str,x)) for x in ker.basis()],'quadratic_coefficients':enc(coeff),'sum_squares_in_rowspan':bool(want in coeff.row_space())})
    return records

def produce():
    v=build();checks={}
    def ck(k,x):checks[k]=bool(x);assert x,k
    L,Q,N,R,H,M=[mat(v[k]) for k in ['basis','Q','N','R','H','M']]
    ck('actual_Riesz_map',H*N==Q.transpose())
    ck('raw_southeast_map',M==R*N and M.rank()==128)
    ck('minimal_two_cell_energy_defect_injective',(L[:512,:]*N).rank()==128)
    ck('global_coordinate_retraction',Q==L[512:640,:] and Q.rank()==128)
    # Explicit nonzero conservative and dissipative full-carrier completions.
    Z=matrix(QQ,128,128);Z[0,1]=1;Z[1,0]=-1
    C=N*Z*Q;B=M*Z
    ck('conservative_witness',H*C+C.transpose()*H==0 and R*N*Z==B and C.rank()==2)
    ck('conservative_not_nilpotent',C*C!=0)
    Cplus=N*Q
    ck('dissipative_witness',H*Cplus+Cplus.transpose()*H==2*Q.transpose()*Q and Cplus.rank()==128)
    ck('raw_fixed_B_unique',M.inverse()*B==Z)
    src=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());d=[x/24 for x in clifford()];obs=[]
    for typ in range(4):
        b=next(b for b in v['blocks'] if b['type']==typ);q,h=map(mat,[b['Q'],b['H']]);n=h.inverse()*q.transpose();T=list(map(mat,b['T']));a=list(map(mat,src['blocks'][typ]['matrices']));kerq=q.right_kernel().basis_matrix().transpose()
        ck(f'unchanged_observation_forces_target_zero_{typ}',all((t*kerq).rank()==4 for t in T))
        ck(f'unchanged_observation_forces_source_zero_{typ}',all((t*n).rank()==4 for t in T))
        skew=[]
        for i in range(4):
            for j in range(i+1,4):
                z=matrix(QQ,4,4);z[i,j]=1;z[j,i]=-1;skew.append(z)
        cols=[]
        for z in skew:cols.append(vector(QQ,sum([(t*n*z*q).list() for t in T],[])))
        for bt in skew:cols.append(vector(QQ,sum([(-bt*t).list() for t in T],[])))
        for r in range(4):
            for c in range(16):
                s=matrix(QQ,4,16);s[r,c]=1;cols.append(vector(QQ,sum([(s*ai-di*s).list() for ai,di in zip(a,d)],[])))
        E=matrix(QQ,cols).transpose();ker=E.right_kernel();ck(f'first_order_rank73_{typ}',E.rank()==73 and ker.dimension()==3)
        triples=[]
        for w in ker.basis():
            z=sum((w[i]*skew[i] for i in range(6)),matrix(QQ,4,4));bt=sum((w[6+i]*skew[i] for i in range(6)),matrix(QQ,4,4));s=matrix(QQ,4,16,w[12:]);triples.append((n*z*q,bt,s))
        quad=[triples[i][2]*triples[j][0]-triples[i][1]*triples[j][2]+(triples[j][2]*triples[i][0]-triples[j][1]*triples[i][2] if i!=j else matrix(QQ,4,16)) for i in range(3) for j in range(i,3)]
        # Row spaces provide exact implications both ways, without using a solver's ideal label.
        coeff=matrix(QQ,[x.list() for x in quad]).transpose()
        wanted=matrix(QQ,[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,1]])
        ck(f'quadratic_real_zero_ideal_{typ}',coeff.row_space()==wanted.row_space())
        ck(f'arbitrary_profile_derivative_injective_{typ}',all(matrix(QQ,[(T[k]*c-d[k]*s).list() for c,bt,s in triples]).rank()==3 for k in range(3)))
        obs.append({'type':typ,'equation_matrix':enc(E),'kernel':[list(map(str,w)) for w in ker.basis()],'triples':[{'C':enc(c),'B':enc(bt),'S':enc(s)} for c,bt,s in triples],'quadratic_coefficients':list(map(enc,quad))})
    v['cross_copy']=cross_certificate(v)
    witness=matrix(QQ,4,64)
    witness[0,0]=QQ('6403900421875/769148374464')
    witness[0,46]=QQ('-13001828125/64095697872')
    witness[1,3]=QQ('90921875/322486272')
    witness[1,11]=QQ('-90921875/107495424')
    witness[2,0]=QQ('90921875/322486272')
    witness[2,3]=QQ('90921875/322486272')
    witness[3,3]=QQ('90921875/20155392')
    witness[3,53]=QQ('90921875/6718464')
    weights=[]
    for typ in range(4):
        coeff=matrix(QQ,[mat(x).list() for x in obs[typ]['quadratic_coefficients']])
        values=coeff*witness.row(typ);diagonal=[i==j for i in range(3) for j in range(i,3)]
        ck(f'global_diagonal_positive_{typ}',all(x>0 if diag else x==0 for x,diag in zip(values,diagonal)))
        weights.append(list(map(str,values)))
    pairweights=[]
    for item in v['cross_copy']:
        aa,bb=item['types'];coef=mat(item['quadratic_coefficients']);functional=vector(QQ,list(witness.row(aa))+list(witness.row(bb)))
        values=functional*coef;diagonal=[i==j for i in range(4) for j in range(i,4)]
        ck(f'global_pair_positive_{aa}_{bb}',all(x>0 if diag else x==0 for x,diag in zip(values,diagonal)))
        pairweights.append(list(map(str,values)))
    v['global_positive_functional']={'weights':enc(witness),'diagonal_weights':weights,'pair_weights':pairweights,'full_first_order_dimension':2080}
    v.update(result_id='K1945',status='active_research',observation=obs,checks=checks,results={'conservative_dimension':8128,'dissipative_cone':'Z+Z^T positive semidefinite','fixed_raw_B_unique':True,'nonzero_minimal_two_cell_dissipative':False,'nonzero_constant_same_block_corrected_observation':False,'global_cross_copy_corrected_observation_classified':True,'nonzero_global_constant_conservative_corrected_observation':False,'source_pairing_selected':False})
    v['inputs']={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest() for s in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','tests/channel-swings/k1824_k77_joint_observed_symbol_algebra.py']}
    return v
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
    if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K1945',len(v['checks']),'new exact matrix controls;',len(v['fixture_checks']),'reused fixture checks')
