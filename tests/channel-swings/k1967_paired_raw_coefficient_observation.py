"""Paired raw upper/lower coefficient classification and oriented scalar repair.

The lower auxiliary-output row is independent in the admitted mathematical
completion, not attributed to a source-defined bar operation.
"""
import argparse, hashlib, json
from pathlib import Path
from sage.all import QQ, GF, matrix, identity_matrix, zero_matrix, diagonal_matrix, prod
from k1836_k77_differential_dirac_quotient import enc, mat
from k1824_k77_joint_observed_symbol_algebra import tensor

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json'
INPUT='lab/process/k1951-coordinated-zero-southeast-principal.json'

def setup():
    I2=identity_matrix(QQ,2,sparse=True)
    x=matrix(QQ,[[0,1],[1,0]],sparse=True)
    z=diagonal_matrix(QQ,[1,-1]);e=matrix(QQ,[[0,1],[-1,0]],sparse=True)
    g=[tensor([z]*j+[v]+[I2]*(6-j)) for v in [x,e] for j in range(7)]
    I=identity_matrix(QQ,128,sparse=True);om=prod(g);W=(3*I-om)/2
    eta=[1]*7+[-1]*7;records=json.loads((ROOT/INPUT).read_text())['blocks']
    J=[zero_matrix(QQ,128,128,sparse=True) for _ in range(15)]
    for k,record in enumerate(records):
        js=mat(record['basis'])*mat(record['section'])
        for (r,c),v in js.dict().items():
            rr=record['coordinates'][r];J[rr//128][rr%128,4*k+c]=v
    C=[zero_matrix(QQ,128,128,sparse=True) for _ in range(3)]
    H=zero_matrix(QQ,128,128,sparse=True)
    for k,r in enumerate(records):
        H[4*k:4*k+4,4*k:4*k+4]=mat(r['quotient_energy'])
        for i in range(3):C[i][4*k:4*k+4,4*k:4*k+4]=mat(r['quotient_generators'][i])
    def apply(k,fields):
        terms=[g[c]*W*fields[c] for c in range(14)]
        total=sum(terms,zero_matrix(QQ,128,128,sparse=True))
        top=[fields[14] if r==k else eta[r]*g[r]*g[k]*(total-terms[r]-terms[k]) for r in range(14)]
        return top+[-eta[k]*fields[k]]
    DJ=apply(0,J);Fi=J[14].inverse();Ti=J[0].inverse()
    assert H==8*I and all(apply(k,J)==[a*c for a in DJ] for k,c in zip([7,8,9],C))
    return g,om,eta,J,C,H,DJ,Fi,Ti,apply

def upper_column(k,B,J,DJ,Fi,apply):
    out=apply(k,[B*a for a in J]);M=Fi*out[0]
    defect=[out[r]-DJ[r]*M for r in range(14)]
    return {(128*r+i)*128+j:v for r,A in enumerate(defect) for (i,j),v in A.dict().items()},M,out

def certify(cols):
    parent=list(range(len(cols)));owner={}
    def find(j):
        while parent[j]!=j:parent[j]=parent[parent[j]];j=parent[j]
        return j
    for j,col in enumerate(cols):
        for row in col:
            if row in owner:parent[find(j)]=find(owner[row])
            else:owner[row]=j
    groups={}
    for j in range(len(cols)):groups.setdefault(find(j),[]).append(j)
    result=[];kernels=[];rank=0
    for ids in groups.values():
        keys=sorted(set().union(*(cols[j].keys() for j in ids)))
        T=matrix(QQ,[[cols[j].get(k,0) for j in ids] for k in keys]) if keys else matrix(QQ,0,len(ids))
        pr=list(T.change_ring(GF(101)).transpose().pivots());B=T.matrix_from_rows(pr);K=B.right_kernel().basis_matrix()
        assert T*K.transpose()==0 and K.nrows()+len(pr)==len(ids)
        pc=list(B.pivots());inverse=B.matrix_from_columns(pc).inverse()
        assert inverse*B.matrix_from_columns(pc)==identity_matrix(QQ,len(pr))
        for row in K:
            v=[QQ(0)]*len(cols)
            for j,x in zip(ids,row):v[j]=x
            kernels.append(v)
        rank+=len(pr);result.append(dict(columns=ids,selected_rows=[keys[i] for i in pr],pivot_columns=pc,inverse=enc(inverse),kernel=enc(K)))
        print('upper block',len(ids),'rank',len(pr),flush=True)
    return dict(rank=rank,blocks=result,kernel=enc(matrix(QQ,kernels) if kernels else matrix(QQ,0,len(cols))))

def bar_candidates(g,eta,J,M,params):
    I=identity_matrix(QQ,128,sparse=True);om=prod(g);Z=zero_matrix(QQ,128,128,sparse=True)
    a,b,c,d=map(QQ,params);H=[0,7,8,9]
    coefficients=[eta[k]*g[k]*((a if k in H else b)*I+(c if k in H else d)*om) for k in range(14)]
    target=-J[0]*M;out=[]
    for kind in ['same','transpose']:
        for sign in [1,-1]:
            lower=sum((-sign*eta[k]*(O if kind=='same' else O.transpose())*J[k] for k,O in enumerate(coefficients)),Z)
            defect=lower-target
            out.append(dict(relation=('+' if sign==1 else '-')+kind,rank=defect.rank(),residual=enc(defect)))
    return out

def produce():
    g,om,eta,J,C,H,DJ,Fi,Ti,apply=setup();I=identity_matrix(QQ,128);Z=zero_matrix(QQ,128,128,sparse=True)
    labels=[];cols=[];outputs=[]
    for k in range(14):
        for a in range(14):
            col,M,_=upper_column(k,g[a],J,DJ,Fi,apply);labels.append([k,a]);cols.append(col);outputs.append(M)
        print('upper covector',k,flush=True)
    complete=certify(cols);K=mat(complete['kernel']);assert complete['rank']==196 and K.nrows()==0
    images=[sum((x*M for x,M in zip(row,outputs)),Z) for row in K]
    complete['induced_rank']=matrix(QQ,[M.list() for M in images]).rank() if images else 0
    complete['labels']=labels
    scalarcols=[];scalarM=[];scalarout=[]
    hs=[0,7,8,9];ns=[k for k in range(14) if k not in hs]
    for ks,volume in [(hs,False),(ns,False),(hs,True),(ns,True)]:
        sums=[zero_matrix(QQ,128,128,sparse=True) for _ in range(15)]
        for k in ks:
            _,_,out=upper_column(k,eta[k]*g[k]*(om if volume else I),J,DJ,Fi,apply)
            sums=[a+b for a,b in zip(sums,out)]
        M=Fi*sums[0];scalarM.append(M);scalarout.append(sums)
        scalarcols.append({(128*r+i)*128+j:v for r in range(14) for (i,j),v in (sums[r]-DJ[r]*M).dict().items()})
    keys=sorted(set().union(*(x.keys() for x in scalarcols)));T=matrix(QQ,[[c.get(k,0) for c in scalarcols] for k in keys]);pivs=list(T.transpose().pivots());B=T.matrix_from_rows(pivs);SK=T.right_kernel().basis_matrix()
    assert len(pivs)==2 and SK.nrows()==2
    sm=[sum((x*M for x,M in zip(row,scalarM)),Z) for row in SK]
    assert all(all(M*c+c*M==0 for c in C) for M in sm),'entire scalar kernel anticommutes'
    conservation=matrix(QQ,[(H*M+M.transpose()*H).list() for M in sm]).transpose()
    CK=conservation.right_kernel().basis_matrix();repair=[]
    for coeff in CK:
        params=coeff*SK;M=sum((x*N for x,N in zip(params,scalarM)),Z)
        assert M!=0 and H*M+M.transpose()*H==0 and all(M*c+c*M==0 for c in C)
        mu2=-(M*M)[0,0];assert mu2>0 and M*M==-mu2*I
        norm=QQ(mu2.sqrt())*(1 if params[2]>0 else -1)
        params=params/norm;M=M/norm;mu2=QQ(1)
        assert list(params)==[QQ(-5301)/23168,QQ(-594)/23168,QQ(7559)/23168,QQ(198)/23168]
        bar0=J[0]*M*Ti
        # One explicit independent lower-left completion: K_bottom=-bar0 J_time.
        assert -bar0*J[0]==DJ[14]*M and bar0==(3*g[0]-5*g[0]*om)/4
        wall=C[0]*M
        assert wall*wall==I and wall.transpose()==wall and (wall-I).rank()==64 and (wall+I).rank()==64
        assert all(c*wall==wall*c for c in C[1:])
        rawout=[sum((x*N[r] for x,N in zip(params,scalarout)),Z) for r in range(14)]+[-bar0*J[0]]
        assert rawout==[a*M for a in DJ]
        repair.append(dict(parameters=list(map(str,params)),M=enc(M),mass_squared=str(mu2),bar0=enc(bar0)))
    assert len(repair)==1
    bar_relations=bar_candidates(g,eta,J,mat(repair[0]['M']),repair[0]['parameters'])
    scalar=dict(labels=['H_grade1','N_grade1','H_grade13','N_grade13'],rank=2,selected_rows=[keys[i] for i in pivs],selected_matrix=enc(B),kernel=enc(SK),conservation_rank=conservation.rank(),conservative_parameter_kernel=enc(CK*SK),repair=repair)
    checks={'raw_core_invariance':True,'actual_energy_8I':True,'upper_rank_exact':True,'scalar_upper_kernel_complete':True,'conservative_mass_nonzero':True,'explicit_barred_return':True}
    return dict(result_id='K1967',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',scope='Fixed K1951 raw principal/core. Upper common grade-one coefficients with arbitrary independently supplied lower return; separate oriented grade-one/grade-thirteen scalar completion. Not source-selected bars or physical GU mass.',inputs={INPUT:hashlib.sha256((ROOT/INPUT).read_bytes()).hexdigest()},grade_one=complete,scalar=scalar,bar_relations=bar_relations,checks=checks)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text()),'report drift'
    print('PASS K1967',r['grade_one']['rank'],r['grade_one']['induced_rank'],r['scalar']['repair'][0]['parameters'],r['scalar']['repair'][0]['mass_squared'],flush=True)
