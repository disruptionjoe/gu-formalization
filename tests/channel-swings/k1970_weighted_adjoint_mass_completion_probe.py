"""Independent sparse tensor matrices; no producer or predecessor code imports."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def plus(A,B,c=Q(1)):
    C=A.copy()
    for k,v in B.items():C[k]=C.get(k,0)+c*v
    return {k:v for k,v in C.items() if v}
def product(A,B):
    rows={};C={}
    for (i,j),v in B.items():rows.setdefault(i,[]).append((j,v))
    for (i,k),v in A.items():
        for j,w in rows.get(k,[]):C[i,j]=C.get((i,j),0)+v*w
    return {k:v for k,v in C.items() if v}
def transpose(A):return {(j,i):v for (i,j),v in A.items()}
def dec(A):return {(i,j):Q(v) for i,j,v in A['entries']}
def check(fault=None):
    I={(j,j):Q(1) for j in range(128)};gam=[]
    for k in range(14):
        axis=k%7;A={}
        for j in range(128):
            bits=[(j>>(6-n))&1 for n in range(7)];sgn=(-1)**sum(bits[:axis])
            if k>=7:sgn*=(-1 if bits[axis]==0 else 1)
            A[j^(1<<(6-axis)),j]=Q(sgn)
        gam.append(A)
    vol=I
    for A in gam:vol=product(vol,A)
    B=I
    for A in gam[:7]:B=product(B,A)
    J=[{} for _ in range(15)]
    old=json.loads((ROOT/'lab/process/k1951-coordinated-zero-southeast-principal.json').read_text())
    for n,b in enumerate(old['blocks']):
        for (i,j),v in product(dec(b['basis']),dec(b['section'])).items():
            c=b['coordinates'][i];J[c//128][c%128,4*n+j]=v
    mass=json.loads((ROOT/'lab/process/k1967-paired-raw-coefficient-observation.json').read_text())['scalar']['repair'][0]
    a,b,c,d=map(Q,mass['parameters']);T=product(J[0],dec(mass['M']));T={k:-v for k,v in T.items()}
    if fault=='drop_grade13':c=d=0
    if fault=='wrong_mass':T={k:2*v for k,v in T.items()}
    report=json.loads((ROOT/'lab/process/k1970-weighted-adjoint-mass-completion.json').read_text());n=0
    for rec,base in zip(report['families'],[I,B]):
        L={}
        for k,g in enumerate(gam):
            u,w=(a,c) if k in [0,7,8,9] else (b,d)
            diag={key:u*I[key]+w*vol[key] for key in I}
            O=product(g,diag);O={key:(1 if k<7 else -1)*v for key,v in O.items()}
            adj=product(product(transpose(base),transpose(O)),base)
            L=plus(L,product(adj,J[k]),Q(-1 if k<7 else 1))
        rp=Q(rec['positive_ratio']);rm=Q(rec['negative_ratio'])
        assert set(L)==set(T),'raw lower support'
        for (i,j),v in T.items():
            assert L[i,j]==(rp if vol[i,i]>0 else rm)*v,'independent raw matrix ratio';n+=1
        if fault=='reciprocal_error':rm=1/rp
        assert rp*rm==Q(rec['product'])!=1,'two-chirality obstruction'
        # Arbitrary positive/nonpositive bilinear weights: exact denominator-cleared
        # compatibility has q=s*rp and q=1/(s*rm), impossible for s=+/-1.
        for sign in [-1,1]:
            q=sign*rp
            assert sign*q*rm!=1,'unrepaired opposite chirality'
        if fault=='omit_component':L={k:v for k,v in L.items() if vol[k[0],k[0]]>0}
        assert len(L)==128,'both chirality components present'
        assert product(transpose(base),base)==I
    return n
if __name__=='__main__':
    n=check();caught=[]
    for f in ['drop_grade13','wrong_mass','reciprocal_error','omit_component']:
        try:check(f)
        except AssertionError as e:caught.append([f,str(e)])
        else:raise AssertionError('missed mathematical fault '+f)
    r=json.loads((ROOT/'lab/process/k1970-weighted-adjoint-mass-completion.json').read_text())
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K1970 independent raw entries',n,'mathematical faults',caught)
