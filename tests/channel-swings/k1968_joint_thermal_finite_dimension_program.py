"""Finite exact joint energy/dimension programs; small-d complete rational frontiers.

Exponential reference implementation. No floating optimizer is used. Canonical
physical spectra are exhaustively enumerated before Pareto-safe pruning.
"""
from fractions import Fraction as F
from itertools import product, combinations, combinations_with_replacement
from pathlib import Path
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1968-joint-thermal-finite-dimension-program.json'

def shells(A,S):
    return all(sum(e-a in (0,1,2,3) for a in A)>=2*sum(e-s in (0,1,2,3) for s in S) for e in {s+b for s in S for b in range(4)})

def blocks(d):
    """Physical connected shapes min0 span<=3(k-1), then valid occupied sets."""
    found={};census=0
    for k in range(3,d+1):
        for gaps in product((1,2,3),repeat=k-1):
            A=[0]
            for g in gaps:A.append(A[-1]+g)
            census+=1
            for n in range(1,(k-1)//2+1):
                for S in combinations(A[1:],n):
                    if shells(A,S) and (S not in found or k<len(found[S])):found[S]=tuple(A)
    # Same relative occupied spectrum: smaller offset and no greater dimension
    # weakly improves energy, preserves return, and leaves every other tag alone.
    kept=[]
    for S,A in found.items():
        rel=tuple(s-S[0] for s in S)
        if any(len(B)<=len(A) and T[0]<=S[0] and (len(B)<len(A) or T[0]<S[0]) and tuple(t-T[0] for t in T)==rel for T,B in found.items()):continue
        kept.append((S,A))
    return sorted(kept,key=lambda x:(len(x[1]),x[0])),census,len(found)

def patterns(d,bs):
    """Tagged physical components, repetitions allowed. Zero-mass tags permitted."""
    def visit(start,used,chosen):
        if chosen:yield tuple(chosen)
        for j in range(start,len(bs)):
            if used+len(bs[j][1])<=d:yield from visit(j,used+len(bs[j][1]),chosen+[j])
    yield from visit(0,0,[])

def rates(g,t=F(1,2)):
    L=sum(t**b for b in range(4-g))/sum(t**b for b in range(4));return L,t**g*L

def equations(pattern,bs,orientation):
    sites=[];edges=[]
    for tag,j in enumerate(pattern):
        S,A=bs[j];off=len(sites);sites.extend((tag,e) for e in S)
        for i in range(len(S)):
            for j in range(i+1,len(S)):
                if S[j]-S[i] in (1,2,3):edges.append((off+i,off+j,S[j]-S[i]))
    n=len(sites);inc=[[F(0)]*n for _ in sites];constraints=[]
    for (i,j,g),sign in zip(edges,orientation):
        L,H=rates(g);v=[F(0)]*n;v[i]=H;v[j]=-L
        row=[sign*x for x in v];constraints.append(row) # row.p>=0
        target=j if sign==1 else i
        inc[target]=[a+b for a,b in zip(inc[target],row)]
    deficit=[[F(int(i==j))-inc[i][j] for j in range(n)] for i in range(n)]
    return sites,edges,constraints,deficit

def solve(rows,rhs):
    n=len(rows);a=[list(map(F,row))+[F(b)] for row,b in zip(rows,rhs)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return None
        a[j],a[pivot]=a[pivot],a[j];q=a[j][j];a[j]=[x/q for x in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return tuple(row[-1] for row in a)

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def rate(sites,p):
    inc=[F(0)]*len(p)
    for i,(tag,e) in enumerate(sites):
        for j,(tag2,f) in enumerate(sites):
            if i<j and tag==tag2 and f-e in (1,2,3):
                L,H=rates(f-e);x=H*p[i]-L*p[j];inc[i]+=max(-x,0);inc[j]+=max(x,0)
    return sum(max(x-y,0) for x,y in zip(p,inc))/2

def cell_vertices(sites,orient_rows,deficit,signs):
    n=len(sites);rows=[[F(int(i==j)) for j in range(n)] for i in range(n)]+orient_rows+[[s*x for x in row] for s,row in zip(signs,deficit)]
    vertices=set()
    for active in combinations(rows,n-1):
        p=solve([[F(1)]*n]+list(active),[F(1)]+[F(0)]*(n-1))
        if p is not None and all(dot(row,p)>=0 for row in rows):vertices.add(p)
    return vertices

def segments_for(d,bs):
    segments={};pc=cc=vc=0
    for pat in patterns(d,bs):
        sites,edges,_,_=equations(pat,bs,());pc+=1
        for orient in product((-1,1),repeat=len(edges)):
            sites,edges,rows,deficit=equations(pat,bs,orient)
            for signs in product((-1,1),repeat=len(sites)):
                vertices=cell_vertices(sites,rows,deficit,signs);cc+=1;vc+=len(vertices)
                points={}
                for p in vertices:
                    E=dot([e for tag,e in sites],p);R=rate(sites,p)
                    assert R==sum(max(dot(row,p),0) for row in deficit)/2
                    if E not in points or R<points[E][0]:points[E]=(R,p)
                pts=sorted((e,r,p) for e,(r,p) in points.items())
                # Every pair lies in one convex cell, and its return is affine.
                # Every lower face of the projection has a vertex-pair endpoint.
                for a,b in combinations(pts,2):
                    e0,r0,p0=a;e1,r1,p1=b
                    if e1==e0:continue
                    slope=(r1-r0)/(e1-e0);intercept=r0-slope*e0
                    key=(e0,e1,slope,intercept)
                    segments.setdefault(key,dict(pattern=pat,p0=p0,p1=p1))
                for e,r,p in pts:segments.setdefault((e,None,F(0),r),dict(pattern=pat,p0=p,p1=p))
    return segments,dict(patterns=pc,cells=cc,vertices=vc)

def envelope(segments):
    # All segment endpoints/intersections are exact. Positive-slope pieces are
    # dominated by their starting point's horizontal energy-budget ray.
    seg={k:v for k,v in segments.items() if k[2]<=0};cuts={F(1)}
    keys=list(seg)
    for lo,hi,m,b in keys:
        cuts.add(lo)
        if hi is not None:cuts.add(hi)
    for i,(l,h,m,b) in enumerate(keys):
        for ll,hh,mm,bb in keys[i+1:]:
            if m==mm:continue
            x=(bb-b)/(m-mm)
            if x>=max(l,ll) and (h is None or x<=h) and (hh is None or x<=hh):cuts.add(x)
    cuts=sorted(cuts);pieces=[]
    for l,h in zip(cuts,cuts[1:]+[None]):
        test=l+1 if h is None else (l+h)/2
        options=[(m*test+b,key) for key in keys for lo,hi,m,b in [key] if lo<=test and (hi is None or test<=hi)]
        assert options
        _,key=min(options);m,b=key[2:]
        if pieces and pieces[-1]['slope']==m and pieces[-1]['intercept']==b:pieces[-1]['hi']=h
        else:pieces.append(dict(lo=l,hi=h,slope=m,intercept=b))
    return pieces

def evaluate(pieces,E):
    return next(p['slope']*E+p['intercept'] for p in pieces if E>=p['lo'] and (p['hi'] is None or E<=p['hi']))

def calculate(limit=8):
    bs,census,raw=blocks(limit);out=[]
    for d in range(3,limit+1):
        seg,count=segments_for(d,bs);pieces=envelope(seg)
        out.append(dict(d=d,pieces=pieces,census=count))
    return dict(result_id='K1968',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',scope='Finite exact joint infimum program for all d; complete enumerated frontiers only through stated limit, bath t=1/2. No finite attainment assertion for colliding tags.',limit=limit,shape_count=census,raw_valid_supports=raw,pareto_blocks=[dict(S=s,A=a) for s,a in bs],frontiers=out,inputs={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in ['lab/process/k1943-arbitrary-preparation-catalyst-energy.json','lab/process/k1966-sharp-thermal-support-size.json']})

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');ap.add_argument('--limit',type=int,default=8);a=ap.parse_args();r=encode(calculate(a.limit))
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1968',r['shape_count'],'physical shapes;',len(r['pareto_blocks']),'Pareto blocks')
    for row in r['frontiers']:print(row)
