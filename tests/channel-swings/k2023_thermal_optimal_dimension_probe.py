"""Independent bath-label/interpolation contact replay and physical dimension checks.
No contact-producer imports. Root decisions reduce domain polynomials modulo the
quadratic and compare exact radical signs. Whole-domain arithmetic, not sampling.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from math import isqrt
import json,hashlib
from k2019_posttransition_thermal_frontier_probe import poly,extrema,REGIMES,A,B,C,RC
from k2015_finite_thermal_ray_separation_probe import bath_planes
ROOT=Path(__file__).resolve().parents[2]
POINTS=set();ZERO=set();evaluated=0

def radical_sign(x,y,d):
 if not y or not d:return (x>0)-(x<0)
 if not x:return (y>0)-(y<0)
 if x>0 and y>0:return 1
 if x<0 and y<0:return -1
 delta=x*x-y*y*d
 if not delta:return 0
 return ((delta>0)-(delta<0))*((x>0)-(x<0))

def consume(kind,p,cs,lo,hi,ref):
 global evaluated
 ref=tuple(map(str,ref))
 if p==(0,0,0):ZERO.add((kind,ref,str(lo),str(hi),tuple(tuple(map(str,c)) for c in cs)));return
 mi,ma=extrema(p,lo,hi)
 if mi>0 or ma<0:return
 a,b,c=p
 if c:
  disc=b*b-4*a*c
  if disc<0:return
  n,d=isqrt(disc.numerator),isqrt(disc.denominator)
  if n*n==disc.numerator and d*d==disc.denominator:roots=[((-b+sgn*Q(n,d))/(2*c),Q(0),Q(0)) for sgn in set([-1,1])]
  else:roots=[(-b/(2*c),Q(sgn)/(2*c),disc) for sgn in [-1,1]]
 elif b:roots=[(-a/b,Q(0),Q(0))]
 else:return
 for r,s,t in roots:
  evaluated+=1
  if radical_sign(r-lo,s,t)<0 or radical_sign(hi-r,-s,t)<0:continue
  def at(z):
   # Divide by the defining quadratic before evaluating at its root.
   if c:z=(z[0]-z[2]*a/c,z[1]-z[2]*b/c,Q(0))
   return radical_sign(z[0]+z[1]*r+z[2]*r*r,z[1]*s,t)
  if any(at(z)<0 for z in cs):continue
  if kind.startswith('single'):
   e,R,k=map(Q,ref)
   if radical_sign(e+k*r-A,k*s,t)<=0 or radical_sign(B-e-k*r,-k*s,t)<=0:continue
  POINTS.add((kind,ref,tuple(map(str,(r,s,t)))))
def replay(c,reg):
    lo,hi,top,rv,rr,k=reg;u=RC-rv;v=top-C;counts={};parts=0
    def targets(d):
        ul=v+d;ur=1+k*d;den=rr*ul-u*ur
        x=(Q(3,10)-RC)*ul*ur+rr*B*ul-u*C*ur
        y=rr*RC*ul-u*Q(3,10)*ur+rr*u*(C-B)
        return den,x,y
    for fn in [lambda d:targets(d)[0],lambda d:targets(d)[1]-Q(17,10)*targets(d)[0],lambda d:B*targets(d)[0]-targets(d)[1]]:
        assert extrema(poly(fn),lo,hi)[0]>0
    def check(kind,fn,conditions,ref):
        counts[kind]=counts.get(kind,0)+1
        consume(kind,poly(fn),[poly(f) for f in conditions],lo,hi,ref)
    rs=sorted({(Q(v['energy']),Q(v['return'])) for cell in c['cells'] for v in cell['vertices']})
    for e,R in rs:
      for b in (0,1):
        common=[lambda d:e+b*d-A,lambda d:B-e-b*d]
        check('single_AC',lambda d:R-Q(9,20)+Q(9,76)*(e+b*d-A),common+[lambda d:C-e-b*d],(e,R,b))
        check('single_CB',lambda d:(R-RC)*(v+d)+u*(e+b*d-C),common+[lambda d:e+b*d-C,lambda d:targets(d)[1]-(e+b*d)*targets(d)[0]],(e,R,b))
        check('single_GA',lambda d:(R-Q(3,10))*(1+k*d)-rr*(B-e-b*d),common+[lambda d:(e+b*d)*targets(d)[0]-targets(d)[1]],(e,R,b))
    def pair(e,R,b,f,S,j,kind):
        def gap(d):
            den,x,y=targets(d)
            return R*((f+j*d)*den-x)+S*(x-(e+b*d)*den)-(f-e+(j-b)*d)*y
        check(kind,gap,[lambda d:targets(d)[1]-(e+b*d)*targets(d)[0],lambda d:(f+j*d)*targets(d)[0]-targets(d)[1]],(e,R,b,f,S,j))
    for e,R in rs:
      for f,S in rs:
        if e<=B and f+hi>=Q(17,10):pair(e,R,0,f,S,1,'sep')
        if f<=B and e+hi>=Q(17,10):pair(f,S,1,e,R,0,'sep')
    for cell in c['cells']:
        _,_,df=bath_planes(tuple(cell['support']),tuple(cell['orientation']),True);vs=cell['vertices']
        signs=[[sum(a*Q(b) for a,b in zip(row,v['p'])) for row in df] for v in vs]
        for i,j in combinations(range(len(vs)),2):
            if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
            e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,S=Q(vs[j]['energy']),Q(vs[j]['return'])
            if e>f:e,f,R,S=f,e,S,R
            if e<=B and f>=Q(17,10):pair(e,R,0,f,S,0,'same')
    return counts,parts


def main():
 import sympy as sy
 report=json.loads((ROOT/'lab/process/k2023-thermal-optimal-dimension.json').read_text());bank=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census']
 for reg,cert in zip(REGIMES,report['enumeration']):
  counts,_=replay(bank,reg);assert counts==cert['obligation_counts'];print('contacts independently enumerated',cert['interval'],flush=True)
 expected={(z['kind'],tuple(z['ref']),tuple(z['root'])) for z in report['isolated_contacts']};assert POINTS==expected,(POINTS-expected,expected-POINTS)
 x=sy.symbols('delta',real=True);actual=set()
 for kind,ref,lo,hi,cs in ZERO:
  cond=[x>=sy.Rational(lo),x<=sy.Rational(hi)]+[sum(sy.Rational(a)*x**i for i,a in enumerate(p))>=0 for p in cs]
  if kind.startswith('single'):
   e,R,b=map(Q,ref);cond += [sy.Rational(e)+sy.Rational(b)*x>sy.Rational(A),sy.Rational(e)+sy.Rational(b)*x<sy.Rational(B)]
  domain=sy.reduce_inequalities(cond,x)
  if domain is not sy.false:actual.add((kind,ref,str(domain)))
 assert actual=={(z['kind'],tuple(z['ref']),z['domain']) for z in report['persistent_contacts']}
 # Independently inspect physical completions, including every smaller subset.
 counts=0
 for rec in report['minimal_completions']:
  support=set(rec['support']);universe=range(max(support)+4);valid=[]
  for n in range(rec['minimum']+1):
   for spec in combinations(universe,n):
    if not support.issubset(spec) or 0 not in spec:continue
    counts+=1
    need={e:2*sum(i+b==e for i in support for b in range(4)) for e in {i+b for i in support for b in range(4)}}
    if all(sum(i+b==e for i in spec for b in range(4))>=v for e,v in need.items()):valid.append(spec)
  assert valid==[tuple(x) for x in rec['completions']] and all(len(x)==rec['minimum'] for x in valid)
 # Actual return from bath labels, not the dimension producer's sharp() helper.
 from k2017_sharp_unrestricted_thermal_transition_probe import direct as actual_return
 for rec in report['physical_minimal_witnesses']:
  d,E=Q(rec['delta']),Q(rec['energy']);spec=list(map(Q,rec['spectrum']));support=list(map(Q,rec['support']));p=list(map(Q,rec['populations']))
  assert len(spec)==rec['dimension'] and min(y-x for x,y in zip(spec,spec[1:]))>=d
  assert sum(p)==1 and sum(a*b for a,b in zip(support,p))==E
  assert actual_return(support,p,Q(1,2))==Q(rec['return_value'])
  for e in {a+b for a,v in zip(support,p) if v for b in range(4)}:
   assert sum(a+b==e for a in spec for b in range(4))>=2*sum(a+b==e for a,v in zip(support,p) if v for b in range(4))
 # Fault tests of exact root/domain arithmetic, not report metadata.
 before=set(POINTS)
 consume('fault',(Q(-2),Q(0),Q(1)),[(Q(0),Q(1),Q(0))],Q(1),Q(2),('1','1','0','2','0','1'))
 assert len(POINTS-before)==1 # positive sqrt2, not negative root
 POINTS.clear();POINTS.update(before)
 for p,h in report['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2023 separate complete contacts',len(expected),len(actual),'retained-root evaluations',evaluated,'completion subsets',counts,'physical witnesses',len(report['physical_minimal_witnesses']))
if __name__=='__main__':main()
