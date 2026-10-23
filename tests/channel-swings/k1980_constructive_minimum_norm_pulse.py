"""Exact moving-strip finite controls for the continuum contraction construction.
Finite fixtures test the algorithm; the analytic proof establishes continuum convergence.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1980-constructive-minimum-norm-pulse.json';M=F(23,100)

def area(a,b,c,d):
    pts=sorted({c,d}|{x for x in [a,b,a+9,b+9] if c<x<d})
    length=lambda z:max(F(0),min(b,z)-max(a,z-9))
    return sum((y-x)*(length(x)+length(y))/2 for x,y in zip(pts,pts[1:]))

def geometry():
    us=list(map(F,[-3,-1,1,3]));zs=list(map(F,[-3,0,3,6,9,12]));cells=[]
    for i,(a,b) in enumerate(zip(us,us[1:])):
        for j,(c,d) in enumerate(zip(zs,zs[1:])):
            w=area(a,b,c,d)
            if w:cells.append((i,j,w))
    assert sum(w for _,_,w in cells)==54
    return cells

def proj(cells,v,axis):
    ids={c[axis] for c in cells};av={i:sum(c[2]*v[k] for k,c in enumerate(cells) if c[axis]==i)/sum(c[2] for c in cells if c[axis]==i) for i in ids}
    return [av[c[axis]] for c in cells]

def norm2(cells,v):return sum(c[2]*x*x for c,x in zip(cells,v))
def step(cells,v,g,eps):
    pu,pz=proj(cells,v,0),proj(cells,v,1)
    return [max(-M,min(M,(2*x-a-b+y)/(2+eps))) for x,a,b,y in zip(v,pu,pz,g)]

def produce():
    cells=geometry();raw=[F(i-1) for i,j,w in cells];av=proj(cells,raw,1)
    witness=[M*(a-b)/2 for a,b in zip(raw,av)];assert max(map(abs,witness))<=M
    assert not any(proj(cells,witness,1));g=proj(cells,witness,0);bound=norm2(cells,witness);cases=[]
    for eps in [F(1),F(1,2),F(1,4),F(1,8)]:
        v=[F(0)]*len(cells);q=2/(2+eps);prior=F(0)
        # Exact contraction of two different starting states, not observed convergence alone.
        other=witness[:]
        for k in range(48):
            nv=step(cells,v,g,eps);no=step(cells,other,g,eps)
            assert norm2(cells,[a-b for a,b in zip(nv,no)])<=q*q*norm2(cells,[a-b for a,b in zip(v,other)])
            v,other=nv,no
        pu,pz=proj(cells,v,0),proj(cells,v,1);res=norm2(cells,[x-y for x,y in zip(pu,g)])+norm2(cells,pz)
        # Squared version of B(sqrt(eps)+sqrt(2)q^k), using (a+b)^2<=2a^2+2b^2.
        upper=bound*(2*eps+4*q**96);assert res<=upper
        cases.append(dict(epsilon=str(eps),iterations=48,contraction=str(q),residual_squared=str(res),residual_squared_bound=str(upper)))
    # Direct finite contraction spectra of the self-adjoint part are checked separately.
    return dict(result_id='K1980',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',strip_area='54',amplitude=str(M),cells=[[i,j,str(w)] for i,j,w in cells],witness=list(map(str,witness)),g=list(map(str,g)),controls=cases,scope='Continuum minimum-L2 optimal measurable pulse defined by a strongly convergent clipped integral iteration; exact finite fixtures only validate implementation, not continuum quadrature or finite-iterate endpoint feasibility.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['explorations/conditional-build/k1974-scalar-excursion-separation-2026-10-23.md','explorations/conditional-build/k1977-scalar-smooth-attainment-2026-10-23.md','lab/process/k1969-scalar-continuum-separation.json']})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
    if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
    else:assert r==json.loads(OUT.read_text())
    print('PASS K1980',len(r['cells']),'exact strip cells;',4*48,'contraction controls; continuum proof separate')
