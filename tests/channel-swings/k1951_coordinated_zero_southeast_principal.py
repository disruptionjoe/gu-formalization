"""K1951: all-covector zero-SE symbol and maximal positive Clifford consumers."""
import sys,json
from pathlib import Path

from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,diagonal_matrix,prod
from k1824_k77_joint_observed_symbol_algebra import tensor
from itertools import product
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"lab/process/k1951-coordinated-zero-southeast-principal.json"

def raw():
    I2=identity_matrix(QQ,2,sparse=True);x=matrix(QQ,[[0,1],[1,0]],sparse=True);z=diagonal_matrix(QQ,[1,-1]);e=matrix(QQ,[[0,1],[-1,0]],sparse=True)
    g=[tensor([z]*j+[v]+[I2]*(6-j)) for v in [x,e] for j in range(7)];eta=[1]*7+[-1]*7;I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);om=prod(g);W=(I+om)/2+I-om;Wi=(I+om)/2+(I-om)/4
    blk=lambda rows:block_matrix(QQ,rows,sparse=True)
    def D(k):return blk([[eta[r]*g[r]*g[k]*g[c]*W if r!=k and c not in (r,k) else Z for c in range(14)]+[I if r==k else Z] for r in range(14)]+[[-eta[c]*I if c==k else Z for c in range(14)]+[Z]])
    inv=[[Z]*15 for _ in range(15)];inv[0][14]=-I;inv[14][0]=I
    for r in range(1,14):
     for c in range(1,14):inv[r][c]=Wi*eta[r]*g[r]*g[0]*g[c]*(QQ(1)/12-(1 if r==c else 0))
    Di=blk(inv);assert Di*D(0)==identity_matrix(QQ,1920,sparse=True)
    As=[Di*D(k) for k in [7,8,9]];
    adj=[set() for _ in range(1920)]
    for A in As:
     for i,j in A.dict():adj[i].add(j);adj[j].add(i)
    seen=set();components=[]
    for v in range(1920):
     if v in seen:continue
     st=[v];c=set()
     while st:
      a=st.pop()
      if a in c:continue
      c.add(a);st.extend(adj[a]-c)
     seen.update(c);components.append(sorted(c))

    return g,As,components,D

def image(M):return M.matrix_from_columns(M.pivots())
def left(J):
    rr=J.transpose().pivots();L=matrix(QQ,J.ncols(),J.nrows());C=J.matrix_from_rows(rr).inverse()
    for j,c in enumerate(rr):L.set_column(c,C.column(j))
    assert L*J==identity_matrix(QQ,J.ncols())
    return L
def clifford_form(a):
    words=[prod([a[i] for i in range(3) if bits[i]],identity_matrix(QQ,a[0].nrows())) for bits in product([0,1],repeat=3)]
    return sum((w.transpose()*w for w in words),matrix(QQ,a[0].nrows(),a[0].nrows()))
def produce():
    g,As,components,D=raw();rows=[];checks={}
    def ck(k,v):checks[k]=bool(v);assert v,k
    for ix,c in enumerate(components):
        a=[A.matrix_from_rows_and_columns(c,c) for A in As];E=matrix(QQ,len(c),sum(i>=1792 for i in c),{(j,k):1 for k,j in enumerate(j for j,i in enumerate(c) if i>=1792)})
        J=E;dims=[J.ncols()]
        while True:
            new=image(block_matrix([[J]+[A*J for A in a]]));dims.append(new.ncols())
            if new.ncols()==J.ncols():break
            J=new
        b=[left(J)*A*J for A in a];n=J.ncols();Id=identity_matrix(QQ,n)
        ck(f'cyclic640_block{ix}',dims==[4,16,20,20] and all(A*J==J*B for A,B in zip(a,b)))
        ds=[B*B-Id for B in b]+[b[i]*b[j]+b[j]*b[i] for i in range(3) for j in range(i+1,3)]
        # Exact quartic homogeneous polynomial, all coefficients, no sampling.
        exps=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)];coeffs={}
        for u,A in zip(exps,ds):
            for v,B in zip(exps,ds):
                e=tuple(x+y for x,y in zip(u,v));coeffs[e]=coeffs.get(e,matrix(QQ,n,n))+A*B
        ck(f'all_covector_quartic{ix}',all(M==0 for M in coeffs.values()))
        ck(f'genuine_Jordan{ix}',ds[0].rank()==4 and ds[0]*ds[0]==0 and (b[0]-Id).rank()==12 and (b[0]+Id).rank()==12)
        cp=b[0].charpoly();x=cp.parent().gen();ck(f'characteristic_multiplicities{ix}',cp==(x-1)**10*(x+1)**10)
        R=image(block_matrix([ds]));rd=[R.ncols()]
        while True:
            new=image(block_matrix([[R]+[B*R for B in b]]));rd.append(new.ncols())
            if new.ncols()==R.ncols():break
            R=new
        Q=R.transpose().right_kernel().basis_matrix();right=left(Q.transpose()).transpose();qb=[Q*B*right for B in b]
        K=block_matrix([[d] for d in ds]).right_kernel().basis_matrix().transpose();kd=[K.ncols()]
        while True:
            ann=K.transpose().right_kernel().basis_matrix();ker=block_matrix([[ann*B*K] for B in b]).right_kernel().basis_matrix().transpose();new=K*ker;kd.append(new.ncols())
            if new.ncols()==K.ncols():break
            K=new
        kb=[left(K)*B*K for B in b];Hq=clifford_form(qb);Hk=clifford_form(kb)
        ck(f'maximal_consumers{ix}',rd==[12,16,16] and kd==[8,4,4] and Q.rank()==4 and K.rank()==4)
        ck(f'quotient_and_submodule{ix}',all(Q*B==C*Q and B*K==K*T for B,C,T in zip(b,qb,kb)))
        ck(f'Clifford_consumers{ix}',all(a[i]*a[j]+a[j]*a[i]==(2*identity_matrix(QQ,4) if i==j else 0) for a in [qb,kb] for i in range(3) for j in range(3)))
        ck(f'positive_energies{ix}',all(H==H.transpose() and all(H*A==A.transpose()*H for A in a) and H.is_positive_definite() for H,a in [(Hq,qb),(Hk,kb)]))
        ck(f'positive_splitting{ix}',(Q*K).rank()==4)
        section=K*(Q*K).inverse();ck(f'invariant_section{ix}',Q*section==identity_matrix(QQ,4) and all(B*section==section*C for B,C in zip(b,qb)))
        # Preserve both the stable submodule and quotient while cancelling the raw added SE cell.
        F=-J.matrix_from_rows([j for j,x in enumerate(c) if x<128]);Ea=left(J)*E;Pi=section*Q
        Ar=left(R)*(Id-Pi)*Ea;FR=F*R;X=left(FR.transpose()).transpose();Y=left(Ar)
        cols=[]
        for j in range(16):
            M=matrix(QQ,4,4);M[j//4,j%4]=1
            cols.append(sum([(M*C+C*M).list() for C in qb],[])+(Hq*M+M.transpose()*Hq).list())
        mk=matrix(QQ,cols).transpose().right_kernel().basis_matrix();M=matrix(QQ,4,4,mk.row(0));mu2=-(M*M)[0,0]
        Cbad=R*X*(-F*section*M*Q*Ea)*Y*left(R)*(Id-Pi);Cmass=section*M*Q+Cbad
        ck(f'mass_space{ix}',mk.nrows()==2 and mu2>0 and M*M==-mu2*identity_matrix(QQ,4))
        ck(f'SEzero_mass{ix}',F*Cmass*Ea==0 and Q*Cmass==M*Q and Cmass*section==section*M and Pi*Cmass==Cmass*Pi)
        ck(f'conservative_mass{ix}',Hq*M+M.transpose()*Hq==0 and all(M*C+C*M==0 for C in qb))
        # Exact Jordan chain: (A-I)v=u nonzero, (A-I)u=0.
        T=b[0]-Id;general=T*T;ker=general.right_kernel().basis_matrix().transpose();v=next(v for v in ker.columns() if T*v!=0);u=T*v
        ck(f'frequency_growth{ix}',T*u==0 and u!=0)
        rows.append(dict(mass={'C':enc(Cmass),'M':enc(M),'mass_squared':str(mu2),'raw_return':enc(F),'auxiliary_inclusion':enc(Ea),'radical_input':enc(Ar),'output_right_inverse':enc(X),'input_left_inverse':enc(Y)},coordinates=c,basis=enc(J),generators=list(map(enc,b)),seed=enc(E),closure_dimensions=dims,radical=enc(R),radical_dimensions=rd,quotient=enc(Q),quotient_generators=list(map(enc,qb)),quotient_energy=enc(Hq),section=enc(section),positive_submodule=enc(K),submodule_generators=list(map(enc,kb)),submodule_energy=enc(Hk),kernel_dimensions=kd,jordan_v=list(map(str,v)),jordan_u=list(map(str,u))))
    ck('all_raw_coordinates',len(rows)==32 and sorted(i for r in rows for i in r['coordinates'])==list(range(1920)))
    return dict(result_id='K1951',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',blocks=rows,checks=checks,scope='Conditional all-SE-zero raw principal symbol. Full cyclic640 weakly hyperbolic; maximal positive invariant submodule and Clifford quotient both128, with a constant invariant splitting and a conservative quotient mass lifted with zero added SE cell. No source bars, physical quotient or GU result.',inputs={p:__import__('hashlib').sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1824-k77-joint-observed-symbol-algebra.json','lab/process/k1949-southeast-zero-mass-compatibility.json']})
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
    if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text()),'report drift'
    print('PASS K1951',len(v['checks']),'exact controls')
