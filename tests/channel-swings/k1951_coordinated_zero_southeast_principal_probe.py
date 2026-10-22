"""Independent bit-basis raw action, cyclic span, energy and Jordan checks."""
from pathlib import Path
from copy import deepcopy
from itertools import product
import json,hashlib
from sage.all import QQ,matrix,identity_matrix,block_matrix,vector,prod
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json'
def mat(x):return matrix(QQ,x['rows'],x['columns'],{(i,j):QQ(v) for i,j,v in x['entries']})
def gamma():
    out=[]
    for odd in [False,True]:
        for j in range(7):
            mask=1<<(6-j);d={}
            for col in range(128):
                sign=(-1)**((col>>(7-j)).bit_count())
                if odd:sign*=1 if col&mask else -1
                d[col^mask,col]=sign
            out.append(matrix(QQ,128,128,d,sparse=True))
    return out

def audit(v,math_only=False):
    count=0
    if not math_only:
        assert v['result_id']=='K1951','report identity'
        for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
    g=gamma();I=identity_matrix(QQ,128);vol=prod(g);W=(3*I-vol)/2;eta=[1]*7+[-1]*7
    def action(k,J):
        fields=[J[128*i:128*(i+1),:] for i in range(15)];out=[]
        for r in range(14):
            total=matrix(QQ,128,J.ncols())
            if r==k:total=fields[14]
            else:
                for c in range(14):
                    if c not in [r,k]:total+=eta[r]*g[r]*g[k]*g[c]*W*fields[c]
            out.append(total)
        out.append(-eta[k]*fields[k])
        return block_matrix([[a] for a in out])
    assert len(v['blocks'])==32,'copy count'
    assert sorted(i for r in v['blocks'] for i in r['coordinates'])==list(range(1920)),'raw partition'
    for rec in v['blocks']:
        c=rec['coordinates'];J=mat(rec['basis']);b=list(map(mat,rec['generators']));seed=mat(rec['seed']);Q=mat(rec['quotient']);K=mat(rec['positive_submodule']);R=mat(rec['radical']);sec=mat(rec['section']);qb=list(map(mat,rec['quotient_generators']));kb=list(map(mat,rec['submodule_generators']));Hq=mat(rec['quotient_energy']);Hk=mat(rec['submodule_energy']);n=20;Id=identity_matrix(QQ,n)
        assert J.rank()==20 and seed.rank()==4,'actual carrier ranks'
        big=matrix(QQ,1920,20,{(c[r],j):z for (r,j),z in J.dict().items()},sparse=True);T=action(0,big)
        assert T.rank()==20,'time coefficient injective on carrier'
        for k,B in zip([7,8,9],b):assert T*B==action(k,big),'independent raw coefficient intertwining'
        js=J.solve_right(seed);span=js
        for expected in [16,20]:
            span=block_matrix([[span]+[B*span for B in b]]);span=span.matrix_from_columns(span.pivots());assert span.ncols()==expected,'minimal cyclic carrier'
        ds=[B*B-Id for B in b]+[b[i]*b[j]+b[j]*b[i] for i in range(3) for j in range(i+1,3)];exps=[(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
        polys={}
        for ea,A in zip(exps,ds):
            for eb,B in zip(exps,ds):
                e=tuple(a+b for a,b in zip(ea,eb));polys[e]=polys.get(e,matrix(QQ,n,n))+A*B
        assert all(M==0 for M in polys.values()),'all-coefficient quartic identity'
        assert R.rank()==16 and Q.rank()==4 and Q*R==0,'quotient dimension'
        D=block_matrix([ds]);G=block_matrix([[D]+[B*D for B in b]])
        assert D.rank()==12 and G.rank()==16 and block_matrix([[R,G]]).rank()==16,'generated defect ideal complete'
        E=block_matrix([[d] for d in ds]);EE=block_matrix([[E]]+[[E*B] for B in b])
        assert E.rank()==12 and EE.rank()==16 and EE*K==0 and K.rank()==4,'maximal good invariant kernel'
        assert Q*sec==identity_matrix(QQ,4) and block_matrix([[K,sec]]).rank()==4,'actual positive section'
        for B,C,A in zip(b,qb,kb):assert Q*B==C*Q and B*K==K*A and B*sec==sec*C,'quotient submodule and section identities'
        for H,bs in [(Hq,qb),(Hk,kb)]:
            assert H==H.transpose() and H.is_positive_definite(),'positive energy'
            assert all(H*B==B.transpose()*H for B in bs),'same energy for all axes'
            assert all(bs[i]*bs[j]+bs[j]*bs[i]==(2*identity_matrix(QQ,4) if i==j else 0) for i in range(3) for j in range(3)),'Clifford relations'
        mass=rec['mass'];C=mat(mass['C']);M=mat(mass['M']);F=-J.matrix_from_rows([j for j,x in enumerate(c) if x<128]);Ea=J.solve_right(seed)
        assert F*C*Ea==0 and Q*C==M*Q and C*sec==sec*M,'raw SE zero and stable mass consumer'
        assert Hq*M+M.transpose()*Hq==0 and all(M*A+A*M==0 for A in qb),'conservative anticommuting mass'
        assert QQ(mass['mass_squared'])>0 and M*M==-QQ(mass['mass_squared'])*identity_matrix(QQ,4),'actual mass gap'
        u=vector(QQ,rec['jordan_u']);w=vector(QQ,rec['jordan_v']);assert u!=0 and (b[0]-Id)*w==u and (b[0]-Id)*u==0,'nontrivial exact Jordan chain'
        count+=26
    return count+2

def main():
    v=json.loads(REPORT.read_text());print('PASS K1951 independent baseline',audit(v),'exact controls',flush=True)
    caught=[]
    for kind in ['principal','quotient','energy','section']:
        w=deepcopy(v);b=w['blocks'][0];obj=b[{'principal':'generators','quotient':'quotient','energy':'quotient_energy','section':'section'}[kind]]
        if kind=='principal':obj=obj[0]
        obj['entries'][0][2]=str(QQ(obj['entries'][0][2])+1)
        try:audit(w,True)
        except AssertionError as e:caught.append((kind,str(e)))
        else:raise AssertionError('undetected input fault '+kind)
    print('PASS genuine mathematical faults',caught,flush=True)
    for kind in ['identity','pin']:
        w=deepcopy(v)
        if kind=='identity':w['result_id']='K0'
        else:w['inputs'][next(iter(w['inputs']))]='0'*64
        try:audit(w)
        except AssertionError as e:print('PASS reporting fault',kind,str(e))
        else:raise AssertionError('undetected reporting fault')
if __name__=='__main__':main()
