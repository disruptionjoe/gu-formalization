"""Separate subset/bath-label/Gaussian-elimination replay of the ray census."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
from math import gcd,lcm
from functools import reduce
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def normalize(row):
    d=lcm(*(x.denominator for x in row));a=[int(d*x) for x in row];g=reduce(gcd,map(abs,a),0)
    if not g:return None
    a=[x//g for x in a]
    return tuple(a if next(x for x in a if x)>0 else [-x for x in a])
def solve(rows,n):
    a=[[Q(1)]*n+[Q(1)]]+[[Q(x) for x in r]+[Q(0)] for r in rows]
    for j in range(n):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return None
        a[j],a[k]=a[k],a[j];z=a[j][j];a[j]=[x/z for x in a[j]]
        for i in range(n):
            if i!=j:
                z=a[i][j];a[i]=[x-z*y for x,y in zip(a[i],a[j])]
    p=tuple(r[-1] for r in a)
    return p if min(p)>=0 else None

def independent_supports(K):
    out=[]
    for n in range(1,6):
        for s in combinations(range(1,K+1),n):
            ds=[b-a for a,b in zip(s,s[1:])]
            if n==1:
                if s==(1,):out.append(s)
            elif all(1<=d<=3 for d in ds) and all(a+b>=4 for a,b in zip(ds,ds[1:])) and s[0]==max(1,3-ds[0]):out.append(s)
    return set(out)

def bath_planes(s,o,with_deficits=False):
    n=len(s);bath=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
    shells={T:[(i,b) for i,x in enumerate(s) for b in range(4) if x+b==T] for T in {x+b for x in s for b in range(4)}}
    kept=[[Q(0)]*n for _ in s];edges={}
    for T,items in shells.items():
        assert len(items)<=2
        if len(items)==1:winner=items[0]
        else:
            (i,b),(j,c)=sorted(items);assert j==i+1
            row=[Q(0)]*n;row[i]=bath[b]*o[i];row[j]=-bath[c]*o[i];edges[i]=row
            winner=(i,b) if o[i]==1 else (j,c)
        j,b=winner
        for i,x in enumerate(s):
            if 0<=T-x<=3:kept[i][j]+=bath[b]/2
    deficits=[[Q(int(i==j))-kept[i][j] for j in range(n)] for i in range(n)]
    coords=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    planes={r for row in coords+list(edges.values())+deficits if (r:=normalize(row)) is not None}
    return (list(edges.values()),sorted(planes),deficits) if with_deficits else (list(edges.values()),sorted(planes))
def direct(s,p):
    b=[Q(8,15),Q(4,15),Q(2,15),Q(1,15)]
    return sum(max(Q(0),v-sum(max(w*b[k] for y,w in zip(s,p) for k in range(4) if y+k==x+j)/2 for j in range(4))) for x,v in zip(s,p))
def replay(bank,fault=None):
    expected={(s,o) for s in independent_supports(9) for o in product((-1,1),repeat=len(s)-1)}
    cells=bank['cells'][:-1] if fault=='missing_cell' else bank['cells']
    assert {(tuple(c['support']),tuple(c['orientation'])) for c in cells}==expected
    assert len(cells)==len(expected)
    allpos=[];count=0;ca=[];cb=[]
    for cell in cells:
        s=tuple(cell['support']);o=tuple(cell['orientation']);n=len(s);edge,planes=bath_planes(s,o)
        actual=set()
        for rows in combinations(planes,n-1):
            p=solve(rows,n)
            if p is not None and all(sum(x*y for x,y in zip(r,p))>=0 for r in edge):actual.add(p)
        stated={tuple(map(Q,v['p'])) for v in cell['vertices']}
        assert stated==actual,'complete arrangement vertices from separate bath coefficients'
        for row in cell['vertices']:
            p=list(map(Q,row['p']));e=sum(x*v for x,v in zip(s,p));r=direct(s,p)
            assert e==Q(row['energy']) and r==Q(row['return'])
            z=r+Q(3,20)*e-Q(63,100)
            assert z==Q(row['surplus']) and z>=0
            if z:
                allpos.append(z)
                if e>Q(6,5):ca.append(z/(e-Q(6,5)))
                if e<Q(11,5):cb.append(z/(Q(11,5)-e))
            else:assert [(x,v) for x,v in zip(s,p) if v] in [[(1,Q(9,10)),(3,Q(1,10))],[(1,Q(2,5)),(3,Q(3,5))]]
            count+=1
    assert min(allpos)==Q(bank['minimum_positive_surplus'])
    assert min(ca)==Q(81,12940) and min(cb)==Q(9,7540)
    return count
if __name__=='__main__':
    r=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text());count=replay(r['census']);faults=[]
    try:replay(r['census'],'missing_cell')
    except AssertionError:faults.append('missing_cell')
    else:raise AssertionError('missing cell accepted')
    # Mathematical corruptions tested against the direct independent oracle.
    for name,pred in [('wrong_return',lambda:direct([1,3],[Q(9,10),Q(1,10)])==Q(9,10)),('inflated_margin',lambda:Q(9,7700)>=Q(1,800)),('inflated_directional_slope',lambda:Q(9,7700)>=Q(1,800)*(Q(11,5)-Q(94,77)))]:
        try:assert pred()
        except AssertionError:faults.append(name)
        else:raise AssertionError('undetected '+name)
    for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    print('PASS K2015 separate',count,'complete vertices;',len(faults),'faults;',len(r['inputs']),'provenance hashes')
