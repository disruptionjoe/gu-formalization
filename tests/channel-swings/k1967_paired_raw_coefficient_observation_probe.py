"""Independent signed-bit entry replay; no producer or Sage imports.

Selected rank rows are reconstructed across ALL columns, including off-block
zeros. The actual repaired raw upper rows and independent lower return are
then checked on all 128 input basis vectors through sparse row identities.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from copy import deepcopy
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
REPORT=ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json'

def decode(x):return {(i,j):F(v) for i,j,v in x['entries']}
def add(*terms):
    out={}
    for t,A in terms:
        for k,v in A.items():out[k]=out.get(k,F(0))+t*v
    return {k:v for k,v in out.items() if v}
def mul(A,B):
    rows={}
    for (i,j),v in B.items():rows.setdefault(i,[]).append((j,v))
    out={}
    for (i,k),v in A.items():
        for j,w in rows.get(k,[]):out[i,j]=out.get((i,j),F(0))+v*w
    return {k:v for k,v in out.items() if v}
def tr(A):return {(j,i):v for (i,j),v in A.items()}
def gamrow(a,row):
    j=a%7;mask=1<<(6-j);inp=row^mask
    sign=(-1)**((inp>>(7-j)).bit_count())
    if a>=7:sign*=1 if inp&mask else -1
    return inp,sign
@lru_cache(None)
def chain(gs,row):
    sign=1
    for a in gs:row,s=gamrow(a,row);sign*=s
    return row,sign
@lru_cache(None)
def omega(row):
    rr,s=chain(tuple(range(14)),row);assert rr==row;return s

def build():
    recs=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())['blocks']
    J=[{} for _ in range(15)];C=[{} for _ in range(3)]
    for k,r in enumerate(recs):
        js=mul(decode(r['basis']),decode(r['section']))
        for (i,j),v in js.items():
            rr=r['coordinates'][i];J[rr//128][rr%128,4*k+j]=v
        for c in range(3):
            for (i,j),v in decode(r['quotient_generators'][c]).items():C[c][4*k+i,4*k+j]=v
    jr=[{} for _ in range(15)]
    for b,A in enumerate(J):
        for (i,j),v in A.items():jr[b].setdefault(i,{})[j]=v
    fi={c:(r,1/v) for (r,c),v in J[14].items()};assert len(fi)==128
    def field(b,row,grade=None,vol=False):
        if grade is None:return jr[b].get(row,{})
        row,s=gamrow(grade,row)
        if vol:s*=omega(row)
        return {j:s*v for j,v in jr[b].get(row,{}).items()}
    @lru_cache(None)
    def rawrow(k,a,rawrow,vol=False):
        r,i=divmod(rawrow,128)
        if r==14:return {j:(-1 if k<7 else 1)*v for j,v in field(k,i,a,vol).items()}
        if r==k:return field(14,i,a,vol)
        out={}
        for c in range(14):
            if c in [r,k]:continue
            row,s=chain((r,k,c),i);s*=F(3-omega(row),2)*(1 if r<7 else -1)
            out=add((1,out),(s,field(c,row,a,vol)))
        return out
    @lru_cache(None)
    def dj(rawrow):return rawrow_fn(0,None,rawrow)
    # A separate name prevents shadowing the row function in the cache wrapper.
    rawrow_fn=rawrow
    def targetrow(k,a,j):
        i,t=fi[j];return {c:t*v for c,v in rawrow(k,a,i).items()}
    def selected(k,a,key):
        rawr,col=divmod(key,128)
        return rawrow(k,a,rawr).get(col,0)-sum(v*targetrow(k,a,j).get(col,0) for j,v in dj(rawr).items())
    return J,C,rawrow,dj,selected

def rank_check(v,selected,fault=None):
    G=v['grade_one'];labels=G['labels'];assert labels==[[k,a] for k in range(14) for a in range(14)]
    allcols=[j for b in G['blocks'] for j in b['columns']];allrows=[r for b in G['blocks'] for r in b['selected_rows']]
    assert sorted(allcols)==list(range(196)) and len(set(allrows))==196
    count=0
    for b in G['blocks']:
        ids=b['columns'];rs=b['selected_rows'];pc=b['pivot_columns'];assert pc==list(range(len(ids)))
        inv=decode(b['inverse']);actual={}
        for i,key in enumerate(rs):
            for j,(k,a) in enumerate(labels):
                aa=(a+1)%14 if fault=='wrong_grade' and j==ids[0] else a
                value=selected(k,aa,key)
                if j in ids:
                    if value:actual[i,ids.index(j)]=value
                else:assert value==0,'off-block upper residual'
        assert mul(inv,actual)=={(i,i):F(1) for i in range(len(ids))},'independent upper inverse'
        count+=1
    assert G['rank']==196 and G['induced_rank']==0 and G['kernel']['rows']==0
    return count

def repair_check(v,J,C,rawrow,dj,fault=None):
    S=v['scalar'];r=S['repair'][0];p=list(map(F,r['parameters']));M=decode(r['M']);bar=decode(r['bar0']);I={(i,i):F(1) for i in range(128)}
    assert p==[F(-5301,23168),F(-594,23168),F(7559,23168),F(198,23168)]
    if fault=='drop_grade13':p[2]=p[3]=0
    if fault=='wrong_mass':M=add((2,M))
    if fault=='omit_bar':bar={}
    assert add((1,M),(1,tr(M)))=={} and mul(M,M)==add((-1,I)),'actual conservative unit mass'
    assert all(add((1,mul(M,c)),(1,mul(c,M)))=={} for c in C),'mass anticommutation'
    mr={}
    for (i,j),x in M.items():mr.setdefault(i,{})[j]=x
    H=[0,7,8,9];N=[k for k in range(14) if k not in H];groups=[(H,False),(N,False),(H,True),(N,True)]
    # All raw upper outputs, not only a sampled defect or the selected minor.
    for rr in range(1792):
        actual={}
        for weight,(ks,vol) in zip(p,groups):
            if weight:
                for k in ks:actual=add((1,actual),(weight*(1 if k<7 else -1),rawrow(k,k,rr,vol)))
        target={}
        for j,x in dj(rr).items():target=add((1,target),(x,mr.get(j,{})))
        assert actual==target,'full raw upper repair'
    assert add((-1,mul(bar,J[0])))==mul({(i,j):x for i in range(128) for j,x in dj(1792+i).items()},M),'paired lower return'
    wall=mul(C[0],M);assert tr(wall)==wall and mul(wall,wall)==I
    assert sum(wall.get((i,i),0) for i in range(128))==0,'equal wall sectors'
    assert all(mul(c,wall)==mul(wall,c) for c in C[1:])
    # Complete four-scalar upper class, reconstructed from the actual rows.
    fi={c:(i,1/x) for (i,c),x in J[14].items()}
    @lru_cache(None)
    def scalarrow(i,rr):
        ks,vol=groups[i]
        return add(*[((1 if k<7 else -1),rawrow(k,k,rr,vol)) for k in ks])
    basisM=[]
    for i in range(4):
        basisM.append({(j,c):t*x for j,(rr,t) in fi.items() for c,x in scalarrow(i,rr).items()})
    B=decode(S['selected_matrix']);SK=decode(S['kernel']);assert S['rank']==2 and S['kernel']['rows']==2
    for j,key in enumerate(S['selected_rows']):
        rr,c=divmod(key,128)
        for i in range(4):
            actual=scalarrow(i,rr).get(c,0)-sum(x*basisM[i].get((k,c),0) for k,x in dj(rr).items())
            assert actual==B.get((j,i),0),'actual scalar minor'
    assert mul(B,tr(SK))=={} and B[0,0]*B[1,1]-B[0,1]*B[1,0]==F(15093,107800)
    sym=[]
    for j in range(2):
        p0=[SK.get((j,i),F(0)) for i in range(4)]
        m0=add(*zip(p0,basisM));assert all(add((1,mul(m0,c)),(1,mul(c,m0)))=={} for c in C),'entire scalar kernel anticommutes'
        sym.append(add((1,m0),(1,tr(m0))))
        for rr in range(1792):
            actual=add(*[(x,scalarrow(i,rr)) for i,x in enumerate(p0) if x])
            target={}
            for k,x in dj(rr).items():
                target=add((1,target),(x,{c:y for (r,c),y in m0.items() if r==k}))
            assert actual==target,'complete scalar upper kernel'
    assert sym[0] and sym[1],'conservation has a nonzero constraint'
    key=next(iter(sym[0]));ratio=sym[1].get(key,0)/sym[0][key]
    assert sym[1]==add((ratio,sym[0])) and S['conservation_rank']==1
    return 15

def bar_checks(v,J):
    r=v['scalar']['repair'][0];a,b,c,d=map(F,r['parameters']);M=decode(r['M']);target=add((-1,mul(J[0],M)));H=[0,7,8,9]
    jr=[{} for _ in range(15)]
    for k,A in enumerate(J):
        for (i,j),x in A.items():jr[k].setdefault(i,{})[j]=x
    for rec in v['bar_relations']:
        relation=rec['relation'];sgn=1 if relation[0]=='+' else -1;transpose=relation[1:]=='transpose';actual={}
        for k in range(14):
            scalar=a if k in H else b;volume=c if k in H else d
            for i in range(128):
                inp,s=gamrow(k,i)
                factor=-sgn*s*((1 if k<7 else -1) if transpose else 1)*(scalar+(-1 if transpose else 1)*volume*omega(inp))
                for j,x in jr[k].get(inp,{}).items():actual[i,j]=actual.get((i,j),F(0))+factor*x
        defect=add((1,actual),(-1,target));assert defect==decode(rec['residual']),'specified bar relation residual'
        # Every tested residual is monomial: this certifies its rank over Q.
        assert len(defect)==rec['rank'] and len({i for i,j in defect})==rec['rank'] and len({j for i,j in defect})==rec['rank'],'exact monomial bar residual rank'
    assert [r['relation'] for r in v['bar_relations']]==['+same','-same','+transpose','-transpose']
    return 4

if __name__=='__main__':
    v=json.loads(REPORT.read_text());assert v['result_id']=='K1967'
    for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
    J,C,rawrow,dj,selected=build();n=rank_check(v,selected);q=repair_check(v,J,C,rawrow,dj);b=bar_checks(v,J)
    print('PASS K1967 independent',n,'full-rank blocks and',q,'repair/control obligations and',b,'bar relations',flush=True)
    caught=[]
    for fault in ['wrong_grade','drop_grade13','wrong_mass','omit_bar']:
        try:
            if fault=='wrong_grade':rank_check(v,selected,fault)
            else:repair_check(v,J,C,rawrow,dj,fault)
        except AssertionError as e:caught.append((fault,str(e)))
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K1967 actual mathematical faults',caught,flush=True)
