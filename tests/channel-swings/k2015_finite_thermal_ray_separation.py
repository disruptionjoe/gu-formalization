"""Complete exact return-cone vertex census at occupied energy cutoff nine.

Integer cofactors enumerate all arrangement vertices, including zero coordinates.
No floating optimization or arbitrary-dimensional spectrum enumeration is used.
"""
from fractions import Fraction as Q
from itertools import product, combinations
from pathlib import Path
from math import gcd
from functools import reduce
import argparse, json, hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2015-finite-thermal-ray-separation.json'
L={1:14,2:12,3:8};H={1:7,2:3,3:1}
def supports(K):
    yield (1,)
    def extend(ds):
        s=[max(1,3-ds[0])]
        for d in ds:s.append(s[-1]+d)
        if s[-1]>K:return
        yield tuple(s)
        for d in (1,2,3):
            if ds[-1]+d>=4:yield from extend(ds+(d,))
    for d in (1,2,3):yield from extend((d,))
def primitive(row):
    g=reduce(gcd,map(abs,row),0)
    if not g:return None
    r=tuple(x//g for x in row)
    return r if next(x for x in r if x)>0 else tuple(-x for x in r)
def matrices(S,o):
    n=len(S);incoming=[[0]*n for _ in S];edge=[]
    for i,sign in enumerate(o):
        d=S[i+1]-S[i];v=[0]*n;v[i]=H[d];v[i+1]=-L[d]
        edge.append(tuple(sign*x for x in v));j=i+1 if sign==1 else i
        incoming[j]=[x+sign*y for x,y in zip(incoming[j],v)]
    deficit=[tuple(15*int(i==j)-incoming[i][j] for j in range(n)) for i in range(n)]
    coords=[tuple(int(i==j) for j in range(n)) for i in range(n)]
    planes=sorted({r for row in coords+edge+deficit if (r:=primitive(row)) is not None})
    return edge,deficit,planes

def det(A):
    n=len(A)
    if not n:return 1
    a=[list(r) for r in A];sgn=1;den=1
    for k in range(n-1):
        p=next((i for i in range(k,n) if a[i][k]),None)
        if p is None:return 0
        if p!=k:a[p],a[k]=a[k],a[p];sgn=-sgn
        z=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):a[i][j]=(z*a[i][j]-a[i][k]*a[k][j])//den
            a[i][k]=0
        den=z
    return sgn*a[-1][-1]
def vertex(rows,n):
    v=[(-1)**j*det([r[:j]+r[j+1:] for r in rows]) for j in range(n)]
    d=sum(v)
    if not d:return None
    p=tuple(Q(x,d) for x in v)
    return p if min(p)>=0 else None

def rate(S,p):
    inc=[Q(0)]*len(S)
    for i in range(len(S)-1):
        d=S[i+1]-S[i];v=(H[d]*p[i]-L[d]*p[i+1])/15
        inc[i]+=max(-v,0);inc[i+1]+=max(v,0)
    return sum(max(x-y,0) for x,y in zip(p,inc))/2

def census(K=9):
    rows=[];total_bases=0;good=set();h=None;minimizers=[]
    for S in supports(K):
        n=len(S)
        for o in product((-1,1),repeat=n-1):
            edges,deficits,planes=matrices(S,o);vertices=set()
            for basis in combinations(planes,n-1):
                total_bases+=1;p=vertex(basis,n)
                if p is not None and all(sum(x*y for x,y in zip(r,p))>=0 for r in edges):vertices.add(p)
            assert vertices
            vv=[]
            for p in sorted(vertices):
                energy=sum(s*x for s,x in zip(S,p));R=rate(S,p);surplus=R+Q(3,20)*energy-Q(63,100)
                assert surplus>=0
                reduced=tuple((s,str(x)) for s,x in zip(S,p) if x)
                if surplus==0:
                    assert reduced in [((1,'9/10'),(3,'1/10')),((1,'2/5'),(3,'3/5'))];good.add(reduced)
                elif h is None or surplus<h:h=surplus;minimizers=[(S,p,R,energy)]
                elif surplus==h:minimizers.append((S,p,R,energy))
                vv.append({'p':list(map(str,p)),'energy':str(energy),'return':str(R),'surplus':str(surplus)})
            rows.append({'support':list(S),'orientation':list(o),'vertices':vv})
    return {'cutoff':K,'support_count':len(list(supports(K))),'orientation_count':len(rows),'basis_count':total_bases,'vertex_records':sum(len(r['vertices']) for r in rows),'minimum_positive_surplus':str(h),'equality_types':[[list(pair) for pair in x] for x in sorted(good)],'margin_witnesses':[{'support':list(s),'p':list(map(str,p)),'return':str(r),'energy':str(e)} for s,p,r,e in minimizers],'cells':rows}

def interval_certificate(c,D=Q(4,15)):
    A=Q(6,5);B=Q(11,5);M=Q(17,10);L=Q(3,20)
    counts={};minimum=None;failures=[]
    def verify(kind,cs,num,ref):
     nonlocal minimum
     lo,hi=Q(0),D
     for a,b in cs: # a+b*d >=0
      if b>0:lo=max(lo,-a/b)
      elif b<0:hi=min(hi,-a/b)
      elif a<0:return
     if lo>hi:return
     vals=[num[0]+num[1]*d for d in (lo,hi)]
     counts[kind]=counts.get(kind,0)+1
     if min(vals)<0:failures.append((kind,lo,hi,num,ref))

    def single(e,R,b):
     common=[(e-A,b),(B-e,-b)]
     verify('single_B',common+[(M-e,Q(1,2)-b)],(R-Q(9,20)+L*(e-A),R-Q(9,20)+L*b),(e,R,b))
     verify('single_A',common+[(e-M,b-Q(1,2))],(R-Q(3,10)-L*(B-e),-(R-Q(3,10))+L*b),(e,R,b))
    def pair(e,R,b,f,S,k,kind,ref):
     # e+b*d <= M+d/2 <= f+k*d, covers equality and both orders.
     cs=[(M-e,Q(1,2)-b),(f-M,k-Q(1,2))]
     num=(R*(f-M)+S*(M-e)-Q(3,8)*(f-e),R*(k-Q(1,2))+S*(Q(1,2)-b)-Q(3,8)*(k-b))
     verify(kind,cs,num,ref)
    rs=sorted({(Q(v['energy']),Q(v['return'])) for x in c['cells'] for v in x['vertices']})
    for e,R in rs:
     for b in (0,1):single(e,R,b)
    for i,(e,R) in enumerate(rs):
     for j,(f,S) in enumerate(rs):
      if e<=M+D/2 and f+D>=M:pair(e,R,0,f,S,1,'separated',(i,j,0,1))
      if f<=M+D/2 and e+D>=M:pair(f,S,1,e,R,0,'separated',(j,i,1,0))
    for ci,cell in enumerate(c['cells']):
     _,de,_=matrices(cell['support'],cell['orientation']);vs=cell['vertices']
     signs=[[sum(Q(x)*Q(y) for x,y in zip(row,v['p'])) for row in de] for v in vs]
     for i,j in combinations(range(len(vs)),2):
      if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
      e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
      if e>f:e,f,R,S=f,e,S,R
      if e<=M+D/2 and f>=M:pair(e,R,0,f,S,0,'same_cone',(ci,i,j))
    assert not failures, failures[:2]
    return {'delta_max':str(D),'feasible_interval_obligations':counts,'failure_count':0,'method':'complete affine coefficient tests on every feasible parameter interval; actual compatible same-cone and separated rays'}

def produce():
    c=census();assert len(c['equality_types'])==2
    rays=[v for cell in c['cells'] for v in cell['vertices'] if Q(v['surplus'])>0]
    ca=min(Q(v['surplus'])/(Q(v['energy'])-Q(6,5)) for v in rays if Q(v['energy'])>Q(6,5))
    cb=min(Q(v['surplus'])/(Q(11,5)-Q(v['energy'])) for v in rays if Q(v['energy'])<Q(11,5))
    c['directional_slopes']={'without_B':str(ca),'without_A':str(cb)}
    c['compatible_interval_certificate']=interval_certificate(c)
    inputs=['explorations/conditional-build/k1943-arbitrary-preparation-catalyst-energy-2026-10-22.md','explorations/conditional-build/k1950-global-catalyst-energy-certificates-2026-10-22.md','explorations/conditional-build/k2013-energy-sensitive-thermal-cutoff-2026-10-24.md']
    return {'result_id':'K2015','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','census':c,'scope':'Complete canonical occupied-support return-cone vertices through energy nine at t=1/2. Not a complete25-level physical spectrum enumeration.','inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');args=a.parse_args();v=produce()
    if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
    else:assert v==json.loads(OUT.read_text()),'certificate drift'
    c=v['census'];print('PASS K2015',*[f'{k}={c[k]}' for k in ['support_count','orientation_count','basis_count','vertex_records','minimum_positive_surplus']])
