"""Complete posttransition cutoff-nine frontier via exact quadratic interval certificates.

Three parameter strips retain every single ray and every compatible chord.
Bernstein bounds prove signs over intervals, not only sampled parameters.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json,hashlib,argparse
from k2015_finite_thermal_ray_separation import matrices
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2019-posttransition-thermal-frontier.json'
A=Q(6,5);B=Q(11,5);C=Q(113,91);RC=Q(81,182)
REGIMES=[(Q(4,15),Q(36,91),B,Q(3,10),Q(3,20),Q(-1)),(Q(36,91),Q(2,5),Q(19,8),Q(9,32),Q(3,20),Q(-1)),(Q(2,5),Q(1,2),Q(19,8),Q(9,32),Q(1,4),Q(0))]
def curve(d,E):
    if E<=A:return Q(63,100)-Q(3,20)*E
    if E<=C:return Q(9,20)-Q(9,76)*(E-A)
    f,S=(B,Q(3,10)) if d<=Q(36,91) else (Q(19,8),Q(9,32))
    left=RC-(RC-S)/(f+d-C)*(E-C)
    right=Q(3,10)+(Q(3,20)/(1-d) if d<=Q(2,5) else Q(1,4))*(B-E)
    return min(left,right)
def kink(d):
    f,S=(B,Q(3,10)) if d<=Q(36,91) else (Q(19,8),Q(9,32))
    ml=(RC-S)/(f+d-C);mr=Q(3,20)/(1-d) if d<=Q(2,5) else Q(1,4)
    return (Q(3,10)-RC+mr*B-ml*C)/(mr-ml)
def add(p,q):return tuple(p[i]+q[i] for i in range(3))
def mul(p,q):
 r=[Q(0)]*3
 for i,x in enumerate(p):
  for j,y in enumerate(q):
   if x and y:assert i+j<3;r[i+j]+=x*y
 return tuple(r)
def sc(p,v):return tuple(x*v for x in p)
def con(v):return (v,Q(0),Q(0))
def lin(v,w):return (v,w,Q(0))
def bounds(p,l,h):
 a,b,c=p
 v=a+b*l+c*l*l;w=a+b*h+c*h*h
 return min(v,w,v+(h-l)*(b+2*c*l)/2),max(v,w,v+(h-l)*(b+2*c*l)/2)
def prove(cs,p,lo,hi):
    todo=[(lo,hi,0)];leaves=discarded=0;maximum=0
    while todo:
        l,h,dep=todo.pop();maximum=max(maximum,dep)
        if any(bounds(c,l,h)[1]<0 for c in cs):discarded+=1;continue
        if bounds(p,l,h)[0]>=0:leaves+=1;continue
        mid=(l+h)/2
        assert not(all(sum(c[i]*mid**i for i in range(3))>=0 for c in cs) and sum(p[i]*mid**i for i in range(3))<0),'negative actual feasible inequality'
        assert dep<64,'unresolved interval; never silently accept'
        todo.extend([(l,mid,dep+1),(mid,h,dep+1)])
    return leaves,discarded,maximum
def certificate(c,regime):
    lo,hi,f0,S0,r,vk=regime;u=RC-S0;v=f0-C;vs=Q(1)
    U=lin(v,1);V=lin(vs,vk);L=add(sc(U,r),sc(V,-u));X=add(add(sc(mul(U,V),Q(3,10)-RC),sc(U,r*B)),sc(V,-u*C));Y=add(add(sc(U,r*RC),sc(V,-u*Q(3,10))),con(r*u*(C-B)))
    assert min(L[0]+L[1]*d for d in [lo,hi])>0
    counts={};certified={};leaves=discarded=maximum=0;digest=hashlib.sha256()
    def check(kind,cs,p,ref):
        nonlocal leaves,discarded,maximum
        counts[kind]=counts.get(kind,0)+1
        digest.update(json.dumps([kind,cs,p,ref],default=str,separators=(',',':')).encode())
        n,z,dep=prove(cs,p,lo,hi);leaves+=n;discarded+=z;maximum=max(maximum,dep)
        if n:certified[kind]=certified.get(kind,0)+1
    def single(e,R,b):
     E=lin(e,b);common=[lin(e-A,b),lin(B-e,-b)]
     check('single_AC',common+[lin(C-e,-b)],lin(R-Q(9,20)+Q(9,76)*(e-A),Q(9,76)*b),(str(e),str(R),b))
     check('single_CB',common+[lin(e-C,b),add(X,sc(mul(E,L),-1))],lin((R-RC)*v+u*(e-C),R-RC+u*b),(str(e),str(R),b))
     check('single_GA',common+[add(mul(E,L),sc(X,-1))],lin((R-Q(3,10))*vs-r*(B-e),(R-Q(3,10))*vk+r*b),(str(e),str(R),b))
    def pair(e,R,b,f,S,k,kind,ref):
     ec=add(X,sc(mul(lin(e,b),L),-1));fc=add(mul(lin(f,k),L),sc(X,-1))
     p=add(add(sc(fc,R),sc(ec,S)),sc(mul(Y,lin(f-e,k-b)),-1))
     check(kind,[ec,fc],p,ref)
    rs=sorted({(Q(v['energy']),Q(v['return'])) for cell in c['cells'] for v in cell['vertices']})
    for e,R in rs:
     for b in [0,1]:single(e,R,b)
    for i,(e,R) in enumerate(rs):
     for j,(f,S) in enumerate(rs):
      if e<=B and f+hi>=Q(17,10):pair(e,R,0,f,S,1,'sep',(i,j,0,1))
      if f<=B and e+hi>=Q(17,10):pair(f,S,1,e,R,0,'sep',(j,i,1,0))
    for ci,cell in enumerate(c['cells']):
     _,de,_=matrices(cell['support'],cell['orientation']);vs=cell['vertices'];signs=[[sum(Q(x)*Q(y) for x,y in zip(row,v['p'])) for row in de] for v in vs]
     for i,j in combinations(range(len(vs)),2):
      if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
      e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
      if e>f:e,f,R,S=f,e,S,R
      if e<=B and f>=Q(17,10):pair(e,R,0,f,S,0,'same',(ci,i,j))
    return dict(interval=list(map(str,[lo,hi])),obligation_counts=counts,accepted_subinterval_obligations=certified,accepted_leaves=leaves,discarded_leaves=discarded,max_bisection_depth=maximum,obligation_digest=digest.hexdigest())
def produce():
    p=ROOT/'lab/process/k2015-finite-thermal-ray-separation.json';c=json.loads(p.read_text())['census']
    banks=[]
    for reg in REGIMES:
        z=certificate(c,reg);banks.append(z);print('certified',z['interval'],z['obligation_counts'],flush=True)
    inputs=['lab/process/k2015-finite-thermal-ray-separation.json','explorations/conditional-build/k2015-finite-thermal-ray-separation-2026-10-24.md','explorations/conditional-build/k2018-thermal-optimizer-rigidity-2026-10-24.md']
    return dict(result_id='K2019',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',spacing_range=['4/15','1/2'],transitions=['36/91','2/5'],certificates=banks,scope='Complete cutoff-nine physical frontier; unrestricted transfer belongs to K2020. No GU identification or novelty claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();z=produce()
    if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
    else:assert z==json.loads(OUT.read_text()),'certificate drift'
    print('PASS K2019 three complete parameter strips')
