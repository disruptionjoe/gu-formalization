"""Independent raw reconstruction, dual-relations census and prolongation checks."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import json,hashlib
import sympy as sp
from k1967_paired_raw_coefficient_observation_probe import build,gamrow,mul,add,tr
ROOT=Path(__file__).resolve().parents[2];N=128

def decode(x):return {(i,j):F(v) for i,j,v in x}
def data():
    J,*_=build();I={(i,i):F(1) for i in range(N)};V=I;gam=[]
    for k in range(14):
        g={}
        for i in range(N):j,a=gamrow(k,i);g[i,j]=F(a)
        gam.append(g);V=mul(V,g)
    ref=json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]
    T=add((-1,mul(J[0],decode(ref['M']['entries']))));a,b,c,d=map(F,ref['parameters']);O=[]
    for k in range(14):
        u,w=(a,c) if k in [0,7,8,9] else (b,d);eta=1 if k<7 else -1
        O.append(mul(gam[k],add((eta*u,I),(eta*w,V))))
    return I,V,J,T,O

def dual_dimension(J):
    p=list(range(N*N));w=[F(1)]*(N*N);dead=set()
    def find(a):
        if p[a]!=a:
            q,z=find(p[a]);w[a]*=z;p[a]=q
        return p[a],w[a]
    for k in range(14):
        rows={i:(j,a) for (i,j),a in J[k].items()}
        for i in range(N):
            a,va=rows[i];dead.add(find(N*i+a)[0])
            for j in range(i):
                b,vb=rows[j];ra,wa=find(N*i+b);rb,wb=find(N*j+a);c=-va/vb
                if ra==rb:
                    if wa!=c*wb:dead.add(ra)
                else:
                    bad=ra in dead or rb in dead;p[ra]=rb;w[ra]=c*wb/wa
                    if bad:dead.add(rb)
        dead={find(r)[0] for r in dead}
    return len({find(i)[0] for i in range(N*N)}-dead)

def check(fault=None):
    r=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text());I,V,J,T,O=data();count=0
    if fault=='coefficient':O[0]=add((2,O[0]))
    if fault=='core':J[0]=add((2,J[0]))
    assert dual_dimension(J)==2
    for fam in r['families']:
        sign=fam['sign'];H=list(map(decode,fam['identity_first_jets']));Z=list(map(decode,fam['cokernel']))
        if fault=='derivative':H[0][0,0]=H[0].get((0,0),F(0))+1
        if fault=='mass':sign=-sign
        def R(q):return add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),q),J[k])) for k in range(14)],(-sign,mul(q,T)))
        lhs={}
        for k,h in enumerate(H):
            assert h==tr(h),'symmetric jet'
            lhs=add((1,lhs),((1 if k<7 else -1),mul(h,J[k])))
        assert lhs==R(I),'raw first-jet equation';count+=15
        assert all(not(set(Z[0])&set(Z[1])) for _ in [0]) and all(Z),'independent duals'
        for z in Z:
            for j in J[:14]:
                zjt=mul(z,tr(j));assert not add((1,zjt),(1,tr(zjt))),'dual symbol annihilation';count+=1
            assert sum(v*R(I).get(ij,F(0)) for ij,v in z.items())==0
        # Independent symmetric subspace reduction, using exact symbolic elimination.
        S=decode(json.loads((ROOT/'lab/process/k1976-general-pairing-transport.json').read_text())['families'][0]['permutation']);basis=[I,V,S]
        cols=[add(((1 if k<7 else -1),mul(b,J[k]))) for k in range(14) for b in basis];rc=[R(b) for b in basis];keys=set().union(*(set(c) for c in cols+rc))
        rows=set()
        for ij in keys:
            row=tuple(c.get(ij,F(0)) for c in cols)+tuple(-c.get(ij,F(0)) for c in rc)
            if any(row):
                a=next(x for x in row if x);rows.add(tuple(x/a for x in row))
        A=sp.Matrix(sorted(rows));assert A[:,:42].rank()==42 and A.rank()==43
        null=A.nullspace();assert len(null)==2
        ratio=F(fam['reduced_a_over_b']);assert abs(ratio)<1
        for v in null:assert v[42]==ratio*v[43] and not any(v[3:42,0])
        # Differentiated algebraic constraint and its derivative eliminate all q.
        crow=[v[0]-ratio*v[1] for v in null];row=[F(0)]*45;row[0]=1;row[1]=-ratio
        sol=A.col_join(sp.Matrix([row]))
        assert any(crow) and sol.rank()==44
        for v in sol.nullspace():assert v[44]==0 and v[2]!=0
        bound=sum(max(sum(abs(v) for (r,c),v in h.items() if r==i) for i in range(N)) for h in H)
        assert 2*bound*F(fam['positive_affine_cube_radius'])==1
        assert any(R(h) for h in H),'affine trial actually fails';count+=8
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    return count
if __name__=='__main__':
    n=check();rejected=[]
    for fault in ['coefficient','core','derivative','mass']:
        try:check(fault)
        except AssertionError as e:rejected.append((fault,str(e)))
        else:raise AssertionError('undetected mathematical fault '+fault)
    print('PASS K1979 separate',n,'raw/dual/prolongation obligations;',rejected)
