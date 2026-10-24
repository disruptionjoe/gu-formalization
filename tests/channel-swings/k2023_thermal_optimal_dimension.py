"""Complete exact contact extraction from the certified K2019 polynomial program."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from math import isqrt
import json,hashlib,argparse
from k2019_posttransition_thermal_frontier import A,B,C,RC,REGIMES,add,mul,sc,con,lin,curve,kink
from k2015_finite_thermal_ray_separation import matrices
from k2018_thermal_optimizer_rigidity import minimum_completion
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2023-thermal-optimal-dimension.json'
CONTACTS={};IDENTITIES={};ROOTCHECKS=0

def sign(a,b=Q(0),d=Q(0)):
 if not b or not d:return (a>0)-(a<0)
 if not a:return (b>0)-(b<0)
 if (a>0)==(b>0):return (a>0)-(a<0)
 cmp=(a*a>b*b*d)-(a*a<b*b*d)
 return cmp*((a>0)-(a<0))
def value(p,r):
 a,b,d=r
 return (p[0]+p[1]*a+p[2]*(a*a+b*b*d), b*(p[1]+2*p[2]*a),d)
def roots(p):
 a,b,c=p
 if c:
  d=b*b-4*a*c
  if d<0:return []
  n,m=isqrt(d.numerator),isqrt(d.denominator)
  if n*n==d.numerator and m*m==d.denominator:
   s=Q(n,m);return [(x,Q(0),Q(0)) for x in set([(-b-s)/(2*c),(-b+s)/(2*c)])]
  return [(-b/(2*c),sgn/(2*c),d) for sgn in [Q(-1),Q(1)]]
 if b:return [(-a/b,Q(0),Q(0))]
 return []
def descriptor(kind,ref,rs,c):
 if kind.startswith('single'):return tuple(map(str,ref))
 if kind=='sep':
  i,j,b,k=ref;e,R=rs[i];f,S=rs[j];return tuple(map(str,(e,R,b,f,S,k)))
 ci,i,j=ref;vs=c['cells'][ci]['vertices'];e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
 if e>f:e,f,R,S=f,e,S,R
 return tuple(map(str,(e,R,0,f,S,0)))
def collect(kind,cs,p,ref,lo,hi,rs,c):
 global ROOTCHECKS
 if not any(p):
  key=(kind,descriptor(kind,ref,rs,c),str(lo),str(hi),tuple(tuple(map(str,x)) for x in cs));IDENTITIES[key]=True;return
 for r in roots(p):
  ROOTCHECKS+=1
  if sign(r[0]-lo,r[1],r[2])<0 or sign(hi-r[0],-r[1],r[2])<0:continue
  if any(sign(*value(x,r))<0 for x in cs):continue
  if kind.startswith('single'):
   e,R,b=ref;e,b=Q(e),Q(b)
   if sign(e-A+b*r[0],b*r[1],r[2])<=0 or sign(B-e-b*r[0],-b*r[1],r[2])<=0:continue
  key=(kind,descriptor(kind,ref,rs,c),tuple(map(str,r)));CONTACTS[key]=True
def certificate(c,regime):
    lo,hi,f0,S0,r,vk=regime;u=RC-S0;v=f0-C;vs=Q(1)
    U=lin(v,1);V=lin(vs,vk);L=add(sc(U,r),sc(V,-u));X=add(add(sc(mul(U,V),Q(3,10)-RC),sc(U,r*B)),sc(V,-u*C));Y=add(add(sc(U,r*RC),sc(V,-u*Q(3,10))),con(r*u*(C-B)))
    assert min(L[0]+L[1]*d for d in [lo,hi])>0
    counts={};certified={};leaves=discarded=maximum=0;digest=hashlib.sha256()
    def check(kind,cs,p,ref):
        counts[kind]=counts.get(kind,0)+1
        digest.update(json.dumps([kind,cs,p,ref],default=str,separators=(',',':')).encode())
        collect(kind,cs,p,ref,lo,hi,rs,c)
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
    return dict(interval=list(map(str,[lo,hi])),obligation_counts=counts,obligation_digest=digest.hexdigest())

def minimum_dimension(d,E):
 assert Q(0)<d<=Q(1,2) and A<E<B
 if d<Q(4,15):return 10
 if E<=C:return 7
 if d==Q(4,15):return 10
 if E<kink(d):return 12 if d<=Q(36,91) else 14
 return 10 if d<Q(2,5) else 5

def physical_witness(d,E):
 from k2020_posttransition_tail_and_resources import physical,shells
 from k2017_sharp_unrestricted_thermal_transition import sharp,encode
 n=minimum_dimension(d,E)
 if n in [7,12,14]:w=physical(d,E)
 elif n==5:w=dict(spectrum=list(map(Q,range(5))),support=[Q(1),Q(3)],populations=[(3-E)/2,(E-1)/2])
 else:
  if d==Q(4,15) and E<=(A+B+d)/2:ea,eb=Q(0),d
  else:ea,eb=d,Q(0)
  t=(E-A-ea)/(B+eb-A-ea)
  pairs=sorted([(Q(i)+ea,(1-t)*p) for i,p in zip([1,3],[Q(9,10),Q(1,10)])]+[(Q(i)+eb,t*p) for i,p in zip([1,3],[Q(2,5),Q(3,5)])])
  w=dict(spectrum=sorted([Q(i)+ea for i in range(5)]+[Q(i)+eb for i in range(5)]),support=[x for x,p in pairs],populations=[p for x,p in pairs])
 a,s,p=w['spectrum'],w['support'],w['populations'];rv=sharp(s,p,Q(1,2))
 assert min(p)>=0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==E and len(a)==n
 assert shells(a,[x for x,y in zip(s,p) if y]) and min(y-x for x,y in zip(a,a[1:]))>=d and rv==curve(d,E)
 return encode(dict(delta=d,energy=E,dimension=n,spectrum=a,support=s,populations=p,return_value=rv))

def produce():
 global CONTACTS,IDENTITIES,ROOTCHECKS
 CONTACTS={};IDENTITIES={};ROOTCHECKS=0
 p=ROOT/'lab/process/k2015-finite-thermal-ray-separation.json';c=json.loads(p.read_text())['census'];banks=[certificate(c,r) for r in REGIMES]
 old=json.loads((ROOT/'lab/process/k2019-posttransition-thermal-frontier.json').read_text())['certificates']
 for a,b in zip(banks,old):
  for k in a:assert a[k]==b[k],k
 # Resolve identically-zero candidates with exact real algebra, only after deduplication.
 import sympy as s
 x=s.symbols('delta',real=True);persistent=[]
 for kind,ref,lo,hi,cs in IDENTITIES:
  cond=[x>=s.Rational(lo),x<=s.Rational(hi)]
  cond += [sum(s.Rational(v)*x**i for i,v in enumerate(poly))>=0 for poly in cs]
  if kind.startswith('single'):
   e,R,b=map(Q,ref);cond += [s.Rational(e)+s.Rational(b)*x>s.Rational(A),s.Rational(e)+s.Rational(b)*x<s.Rational(B)]
  interval=s.reduce_inequalities(cond,x)
  if interval is not s.false:persistent.append(dict(kind=kind,ref=ref,domain=str(interval)))
 unique=sorted({(Q(v['energy']),Q(v['return'])) for cell in c['cells'] for v in cell['vertices']})
 wanted={(A,Q(9,20)),(B,Q(3,10)),(C,RC),(Q(19,8),Q(9,32)),(Q(7,5),Q(1,2)),(Q(1),Q(1,2))}
 lifts={str(e)+','+str(r):set() for e,r in wanted}
 for cell in c['cells']:
  for v in cell['vertices']:
   e,r=Q(v['energy']),Q(v['return'])
   if (e,r) in wanted:lifts[str(e)+','+str(r)].add(tuple((i,str(Q(p))) for i,p in zip(cell['support'],v['p']) if Q(p)))
 assert len(CONTACTS)==6 and len(persistent)==12
 assert all(len(v)==1 for v in lifts.values())
 comps=[]
 for support in [[1],[1,3],[1,3,5]]:
  n,aa,tested=minimum_completion(support);comps.append(dict(support=support,minimum=n,completions=aa,tested=tested))
 witnesses=[]
 for d in [Q(4,15),Q(1,3),Q(36,91),Q(199,500),Q(2,5),Q(9,20),Q(1,2)]:
  X=kink(d)
  for E in [(A+C)/2,C,C+(X-C)/100,(C+X)/2,X-(X-C)/100,X,(X+B)/2,B-(B-X)/100]:witnesses.append(physical_witness(d,E))
 return dict(physical_minimal_witnesses=witnesses,dimension_law={'old_strict_onset':'10 for0<delta<4/15, fromK2018','low_energy':'7 for4/15<=delta<=1/2 and a<E<=c','sharp_onset_upper':'10 fordelta=4/15 and c<E<b','left_CB':'12 for4/15<delta<=36/91 and c<E<X(delta)','left_CD':'14 for36/91<delta<=1/2 and c<E<X(delta)','right_AB':'10 for4/15<delta<2/5 and X(delta)<=E<b','right_J':'5 for2/5<=delta<=1/2 and X(delta)<=E<b'},result_id='K2023',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',enumeration=banks,root_candidates_checked=ROOTCHECKS,isolated_contacts=[dict(kind=k,ref=r,root=z) for k,r,z in sorted(CONTACTS)],persistent_contacts=sorted(persistent,key=lambda z:json.dumps(z)),ray_lifts={k:sorted(v) for k,v in lifts.items()},minimal_completions=comps,scope='Complete lifted contact extraction and physical completion counts on the existing thermal frontier. No all-unitary or coherence classification.',inputs={q:hashlib.sha256((ROOT/q).read_bytes()).hexdigest() for q in ['lab/process/k2015-finite-thermal-ray-separation.json','lab/process/k2019-posttransition-thermal-frontier.json','lab/process/k2020-posttransition-tail-and-resources.json']})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert json.loads(json.dumps(z))==json.loads(OUT.read_text())
 print('PASS K2023',z['root_candidates_checked'],'roots',len(z['isolated_contacts']),'isolated',len(z['persistent_contacts']),'persistent')
