"""Separate rowwise equations, finite-field completeness and genuine input faults."""
import json,hashlib
from copy import deepcopy
from itertools import combinations
from pathlib import Path
from sage.all import QQ,GF,matrix,identity_matrix
ROOT=Path(__file__).resolve().parents[2];REPORT=ROOT/'lab/process/k1945-energy-compatible-raw-columns.json'
def m(v):return matrix(QQ,v.get('rows',16),v.get('columns',16),{(i,j):QQ(x) for i,j,x in v['entries']})
def inspect(v):
    count=0
    def ck(x,msg):
        nonlocal count
        assert x,msg
        count+=1
    L,Q,N,R,H,M=[m(v[k]) for k in ['basis','Q','N','R','H','M']]
    raw=matrix(QQ,128,128,{(j^64,j):QQ(11)/(24 if j.bit_count()%2==0 else 12) for j in range(128)})
    ck(m(v['Traw'])==raw,'independent bit-Clifford raw time coefficient')
    ck(Q==L[512:640,:],'actual auxiliary extraction')
    ck(R==-L[:128,:]+raw*Q,'actual raw southeast return')
    ck(H*N==Q.transpose(),'fixed energy Riesz equation')
    ck(M==R*N and M.change_ring(GF(1009)).rank()==128,'raw map full rank')
    ck((L[:512,:]*N).change_ring(GF(1009)).rank()==128,'minimal-support exclusion rank')
    src=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());ob=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());D=list(map(m,ob['target_D']));pairs=list(combinations(range(4),2))
    for typ in range(4):
        b=next(b for b in v['blocks'] if b['type']==typ);q,h=m(b['Q']),m(b['H']);a=list(map(m,src['blocks'][typ]['matrices']));ts=list(map(m,ob['blocks'][typ]['T']));n=h.inverse()*q.transpose()
        ck(h==m(src['blocks'][typ]['H']) and ts==list(map(m,b['T'])),'unchanged energy and observation')
        eq=matrix(QQ,192,76,sparse=True)
        for i in range(3):
            for r in range(4):
                for c in range(16):
                    row=64*i+16*r+c
                    for k,(aa,bb) in enumerate(pairs):
                        eq[row,k]=sum(ts[i][r,j]*(n[j,aa]*q[bb,c]-n[j,bb]*q[aa,c]) for j in range(16))
                        eq[row,6+k]=-(ts[i][bb,c] if r==aa else 0)+(ts[i][aa,c] if r==bb else 0)
                    for rr in range(4):
                        for cc in range(16):eq[row,12+16*rr+cc]=(a[i][cc,c] if rr==r else 0)-(D[i][r,rr]/24 if cc==c else 0)
        record=v['observation'][typ];K=matrix(QQ,[[QQ(x) for x in w] for w in record['kernel']]).transpose()
        ck(eq==m(record['equation_matrix']),'independent rowwise coefficient system')
        ck(eq*K==0 and K.rank()==3 and eq.change_ring(GF(1009)).rank()==73,'complete rational nullspace with independent modular lower rank')
        tri=[tuple(m(t[k]) for k in ['C','B','S']) for t in record['triples']]
        for k,(C,B,S) in enumerate(tri):
            Z=matrix(QQ,4,4);Bt=matrix(QQ,4,4)
            for j,(aa,bb) in enumerate(pairs):Z[aa,bb]=K[j,k];Z[bb,aa]=-K[j,k];Bt[aa,bb]=K[6+j,k];Bt[bb,aa]=-K[6+j,k]
            ck(C==n*Z*q and B==Bt and S==matrix(QQ,4,16,K.column(k)[12:]),'triple matches kernel')
            ck(h*C+C.transpose()*h==0 and B+B.transpose()==0,'both fixed energies conserved')
            ck(all(ts[i]*C-B*ts[i]+S*a[i]-D[i]*S/24==0 for i in range(3)),'all first-order coefficients')
        quad=[]
        for i in range(3):
            for j in range(i,3):
                C,B,S=tri[i];Cj,Bj,Sj=tri[j];v0=S*Cj-B*Sj
                if i!=j:v0+=Sj*C-Bj*S
                quad.append(v0)
        ck(quad==list(map(m,record['quadratic_coefficients'])),'actual full zero-order defect')
        rows=matrix(QQ,[x.list() for x in quad]).transpose()
        desired=matrix(QQ,[[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,1,0,1]])
        ck(rows.row_space()==desired.row_space(),'real quadratic conditions v0^2=0 and v1^2+v2^2=0')
        for axis in range(3):
            deriv=matrix(QQ,[(ts[axis]*C-D[axis]*S/24).list() for C,B,S in tri]).transpose()
            ck(deriv.change_ring(GF(1013)).rank()==3,'arbitrary one-axis derivative obstruction')
    common=m(v['global_positive_functional']['weights'])
    for typ in range(4):
        coeff=matrix(QQ,[m(x).list() for x in v['observation'][typ]['quadratic_coefficients']])
        values=coeff*common.row(typ);mon=[i==j for i in range(3) for j in range(i,3)]
        ck(all(x>0 if diag else x==0 for x,diag in zip(values,mon)),'global diagonal strict positivity')
    for item in v['cross_copy']:
        aa,bb=item['types'];bs=[next(b for b in v['blocks'] if b['type']==typ) for typ in [aa,bb]]
        qs=[m(b['Q']) for b in bs];ns=[m(b['H']).inverse()*q.transpose() for b,q in zip(bs,qs)];ts2=[list(map(m,b['T'])) for b in bs];As=[list(map(m,src['blocks'][typ]['matrices'])) for typ in [aa,bb]]
        # Assemble row coefficients for both directions, including the required opposite transpose.
        eq=matrix(QQ,384,160,sparse=True)
        for side in range(2):
            other=1-side
            for i in range(3):
                for r in range(4):
                    for c in range(16):
                        row=192*side+64*i+16*r+c
                        for z0 in range(4):
                            for z1 in range(4):
                                za,zb=(z0,z1) if side==0 else (z1,z0);sign=1 if side==0 else -1
                                eq[row,4*z0+z1]=sign*sum(ts2[side][i][r,h]*ns[side][h,za]*qs[other][zb,c] for h in range(16))
                                eq[row,16+4*z0+z1]=-sign*(ts2[other][i][zb,c] if r==za else 0)
                        for sr in range(4):
                            for sc in range(16):eq[row,32+64*side+16*sr+sc]=(As[other][i][sc,c] if sr==r else 0)-(D[i][r,sr]/24 if sc==c else 0)
        K=matrix(QQ,[[QQ(x) for x in row] for row in item['kernel']]).transpose()
        ck(eq==m(item['equations']),'independent cross-copy row assembly')
        ck(eq*K==0 and K.rank()==4 and eq.change_ring(GF(1013)).rank()==156,'complete cross-copy kernel')
        tri=[]
        for w in K.columns():
            Z=matrix(QQ,4,4,w[:16]);B=matrix(QQ,4,4,w[16:32]);S=matrix(QQ,4,16,w[32:96]);T=matrix(QQ,4,16,w[96:]);tri.append((ns[0]*Z*qs[1],-ns[1]*Z.transpose()*qs[0],B,-B.transpose(),S,T))
        columns=[]
        for i in range(4):
            for j in range(i,4):
                terms=[(i,j)]+([(j,i)] if i!=j else []);left=matrix(QQ,4,16);right=matrix(QQ,4,16)
                for k,l in terms:
                    C,Cb,B,Bb,S,Sb=tri[k];Cj,Cbj,Bj,Bbj,Sj,Sbj=tri[l]
                    left+=S*Cbj-B*Sbj;right+=Sb*Cj-Bb*Sj
                columns.append(left.list()+right.list())
        coeff=matrix(QQ,columns).transpose();ck(coeff==m(item['quadratic_coefficients']),'actual cross-copy quadratic diagonal residual')
        functional=matrix(QQ,1,128,list(common.row(aa))+list(common.row(bb)));values=list((functional*coeff).row(0));mon=[i==j for i in range(4) for j in range(i,4)]
        ck(all(x>0 if diag else x==0 for x,diag in zip(values,mon)),'one common functional proves all-copy positivity')
    ck(v['global_positive_functional']['full_first_order_dimension']==32*3+32*31//2*4,'actual full first-order dimension')
    return count

def pins(v):
    assert v['result_id']=='K1945','report identity'
    for p,d in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==d,'upstream pin'

def main():
    v=json.loads(REPORT.read_text());pins(v);n=inspect(v);caught=[]
    for key in ['N','R','M']:
        bad=deepcopy(v);bad[key]['entries'][0][2]=str(QQ(bad[key]['entries'][0][2])+1)
        try:inspect(bad)
        except AssertionError as e:caught.append(str(e))
    bad=deepcopy(v);bad['observation'][0]['triples'][0]['S']['entries'][0][2]='999'
    try:inspect(bad)
    except AssertionError as e:caught.append(str(e))
    bad=deepcopy(v);bad['global_positive_functional']['weights']['entries'][0][2]='0'
    try:inspect(bad)
    except AssertionError as e:caught.append(str(e))
    assert len(caught)==5,'all actual matrix faults detected by assertions'
    consistency=[]
    for field in ['result_id','inputs']:
        bad=deepcopy(v)
        if field=='result_id':bad[field]='K0'
        else:bad[field][next(iter(bad[field]))]='0'*64
        try:pins(bad)
        except AssertionError as e:consistency.append(str(e))
    assert len(consistency)==2,'report/pin control power'
    print('PASS K1945',n,'independent exact controls; mathematical faults:',caught,'consistency:',consistency)
if __name__=='__main__':main()
