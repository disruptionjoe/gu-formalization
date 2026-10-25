"""Separate bath-shell replay and symbolic proof-transfer checks.

Finite controls are not labeled universal proof; the polynomial factorization
and the exploration's monotonicity/feasibility argument justify the reduction.
"""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
def physical(w):
 xs=w['support'];p=list(map(F,w['population']));spec=w['spectrum'];E=F(w['energy'])
 assert min(p)>0 and sum(p)==1,'normalization'
 assert sum(x*y for x,y in zip(xs,p))==E,'mean'
 assert spec==sorted(set(spec)) and spec[0]==0 and min(b-a for a,b in zip(spec,spec[1:]))>=1,'physical spacing'
 for z in {x+k for x in xs for k in range(4)}:
  assert sum(z-x in (0,1,2,3) for x in spec)>=2*sum(z-x in (0,1,2,3) for x in xs),'shell capacity'
 rr=sum(max(p[i]-sum(max(p[j]*bath[k] for j,x in enumerate(xs) for k in range(4) if x+k==y+b)/2 for b in range(4)),0) for i,y in enumerate(xs))
 assert rr==F(w['return_value']),'physical return'
 return rr

def summation(h,m,E):
 uweights=[F(9**(h-1-i)) for i in range(h)]+[F(1,10),F(0)]+[F(0)]*(m+1)
 vweights=[F(0)]*h+[F(2,5),F(1)]+[F(3,2*9**k) for k in range(m+1)]
 xs=list(range(1,2*len(uweights),2));a=sum(uweights);b=sum(vweights);c=sum(x*y for x,y in zip(xs,uweights));d=sum(x*y for x,y in zip(xs,vweights));det=a*d-b*c
 u=(d-b*E)/det;v=(a*E-c)/det
 return u/v,(F(9**(h-1),2)*u+F(3,4)*v)

def independently_minimize(E):
 best=None;h=1;checks=0
 while F(5,4)+F(10*(29*h+40),16*9**h+145)>=E:
  z=9**h;a=F(5*z-1,40);c=F(25*z-8*h-9,160);b=F(247,80);d=F(247*h,40)+F(3923,320);ri=(d-b*E)/(a*E-c)
  if F(8,3)<=ri<=36:
   u=(d-b*E)/(a*d-b*c);v=(a*E-c)/(a*d-b*c);value=F(9**(h-1),2)*u+F(3,4)*v
   if best is None or value<best[0]:best=(value,h,None)
  if ri>F(8,3):
   m=0
   while True:
    ratio,value=summation(h,m,E);checks+=1
    if ratio>36:break
    if ratio>=F(8,3):
     if best is None or value<best[0]:best=(value,h,m)
     # All later feasible tails are worse once the exact difference is positive.
     slope=(896*z+216)*m-1080*h*z-112*z+513+F(135*z,9**(m+1))
     if slope>0:break
    m+=1
  h+=1
 return best,h,checks

def symbolic(tail_factor=27):
 h,z,E,m,q=s.symbols('h z E m q');A=(5*z-1)/40;c=(25*z-8*h-9)/160
 B=s.Rational(247,80)-s.Rational(27,16)*q
 d=s.Rational(247,40)*h+s.Rational(3923,320)-s.Rational(tail_factor,64)*(8*m+8*h+29)*q
 D=A*d-B*c;N=z*d/18-s.Rational(3,4)*c+E*(s.Rational(3,4)*A-z*B/18)
 D2=D.subs({m:m+1,q:q/9},simultaneous=True);N2=N.subs({m:m+1,q:q/9},simultaneous=True)
 T=(896*z+216)*m-1080*h*z-112*z+513+135*z*q
 assert s.factor(N2*D-N*D2-q*(A*E-c)*T/3840)==0,'tail difference identity'
 # The head bound and ratio proof use exact infinite geometric moments.
 dinf=s.Rational(247,40)*h+s.Rational(3923,320);binf=s.Rational(247,80)
 for r,num,den in [(s.Rational(8,3),10*(29*h+40),16*z+145),(36,10*(7*h+12),72*z+35)]:
  assert s.factor((r*c+dinf)/(r*A+binf)-s.Rational(5,4)-num/den)==0,'head exclusion identity'
 return 3

def direct_general(h,l,m,E):
 aweights=[F(9**(h-1-i)) for i in range(h)]+[F(1,10)]+[F(0)]*(l+1+m)
 vweights=[F(0)]*h+[F(2,5)]+[F(3,2)**k for k in range(l+1)]+[F(3,2)**l/F(9**j) for j in range(1,m+1)]
 xs=list(range(1,2*len(aweights),2));a=sum(aweights);b=sum(vweights);c=sum(x*y for x,y in zip(xs,aweights));d=sum(x*y for x,y in zip(xs,vweights));D=a*d-b*c
 u=(d-b*E)/D;v=(a*E-c)/D
 return u/v,F(9**(h-1),2)*u+(F(3,2)**l)*v/2

def general_independent(E,seed):
 best=seed;h=1;checks=0
 while True:
  z=9**h;a=F(5*z-1,40);c=F(25*z-8*h-9,160);eu=c/a
  lower=F(4,9)-F(64,225)*min(F(1),(E-eu)/(2*h+1-eu))
  if lower>=best:break
  l=1
  while direct_general(h,l,0,E)[0]<=36:
   w=F(3,2)**l;b=25*w/8-F(8,5);d=w*F(200*h+200*l-75,32)-F(16*h-32,5);D=a*d-b*c;u=(d-b*E)/D;v=(a*E-c)/D
   ri=u/v
   if F(8,3)<=ri<=36:best=min(best,F(9**(h-1),2)*u+w*v/2)
   if ri>F(8,3):
    m=0
    while True:
     ratio,value=direct_general(h,l,m,E);checks+=1
     if ratio>36:break
     if ratio>=F(8,3):
      best=min(best,value)
      # Sign is obtained from two separately summed finite populations.
      if direct_general(h,l,m+1,E)[1]>=value:break
     m+=1
   l+=1
  h+=1
 return best,h,checks

def generalized_symbolic():
 h,z,l,w,E,m,q=s.symbols('h z l w E m q');A=(5*z-1)/40;c=(25*z-8*h-9)/160
 B=25*w/8-s.Rational(8,5)-9*w*q/8
 d=w*(200*h+200*l-75)/32-(16*h-32)/5-9*w*q*(8*h+8*l+8*m+21)/32
 D=A*d-B*c;N=z*d/18-w*c/2+E*(w*A/2-z*B/18)
 T=(640*w*z+72*w-512*z)*m-360*h*w*z-360*l*w*z+72*l*w-512*l*z+2200*w*z+99*w-2304*z+45*q*w*z
 D2=D.subs({m:m+1,q:q/9},simultaneous=True);N2=N.subs({m:m+1,q:q/9},simultaneous=True)
 assert s.factor(N2*D-N*D2-q*w*(A*E-c)*T/2880)==0,'generalized tail identity'
 assert s.factor(T.subs({m:m+1,q:q/9},simultaneous=True)-T-(640*w*z+72*w-512*z-40*w*z*q))==0,'generalized sign monotonicity'
 return 2

def global_probe(r):
 """Separate gap recursion, bath-label rows, dual replay and equality nullspaces."""
 import zlib,base64
 from itertools import product
 import k2027_thermal_pattern_frontier_probe as c
 import k2029_multicomponent_thermal_placement_probe as p
 lo,hi=F(13,10),F(8283273393,6147208289);A,C,B=F(15398019,32499160),F(761157,32499160),F(43,2000)
 c.lo,c.hi,c.intercept,c.slope,c.back=lo,hi,A,C,B
 raw=zlib.decompress(base64.b64decode(r['payload']));assert hashlib.sha256(raw).hexdigest()==r['payload_sha256'];d=json.loads(raw)
 exp=iter((xs,o) for xs in p.words(21) if xs[0]<=hi for o in product((-1,1),repeat=len(xs)-1));count=0;contacts=[];endpoint_contacts=[]
 for row in d['connected']:
  xs,o=next(exp);assert row['s']==list(xs) and row['o']==list(o)
  assert len(row['certificates'])==2
  for kind,cc in zip(('low','strip'),row['certificates']):
   assert kind==cc['kind']
   if 'infeasible_energy' in cc:assert c.validate_dual(xs,o,cc['infeasible_energy'])>(lo if kind=='low' else hi)
   elif 'infeasible_maxenergy' in cc:assert kind=='strip' and -c.validate_dual(xs,o,cc['infeasible_maxenergy'])<lo
   else:
    vv=c.validate_dual(xs,o,cc);target=A-C*lo+B*lo if kind=='low' else A;assert vv>=target
    if kind=='strip' and vv==A:
     (endpoint_contacts if F(cc['y'][-2])<0 else contacts).append((xs,o,cc))
   count+=1
  if count%100000==0:print('separate new interval duals',count,flush=True)
 assert next(exp,None) is None and count==r['connected_duals']
 pen=[];gc=0
 for bank in d['components']['banks']:
  lam,intercept=F(bank['slope']),F(bank['intercept']);ex=iter((xs,o) for xs in p.words(14) for o in product((-1,1),repeat=len(xs)-1))
  for row in bank['rows']:
   xs,o=next(ex);assert row['s']==list(xs) and row['o']==list(o);n=len(xs);aa=p.raw(xs,o)
   assert p.dual([lam*x for x in xs]+[F(1)]*n,aa,[F(0)]*len(aa),[F(1)]*n+[F(0)]*n,row['cert'])>=intercept;gc+=1
  assert next(ex,None) is None and 15*lam>intercept;pen.append((lam,intercept))
 assert [x[0] for x in pen]==[B,C];pen.extend([(F(1,4),F(3,4)),(F(3,20),F(63,100))])
 ex=iter((xs,o) for xs in p.words(7) if xs[0]==1 and (1 if len(xs)==1 else xs[-2]+3)<8 for o in product((-1,1),repeat=len(xs)-1));margins=[]
 for row in d['components']['short']:
  xs,o=next(ex);assert row['s']==list(xs) and row['o']==list(o);n=len(xs);L=1 if n==1 else xs[-2]+3;offset=min(F(L)+F(1,2),F(xs[-1]+2));aa=[x+[F(0)]*3 for x in p.raw(xs,o)];bb=[F(0)]*len(aa)
  en=list(map(F,xs))+[F(0)]*n+[F(0),F(1),F(0)];aa.extend([en,[-x for x in en],[F(0)]*(2*n)+[offset+1,-F(1),F(0)]]);bb.extend([hi,-lo,F(0)])
  for lam,intercept in pen:aa.append([F(0)]*(2*n)+[intercept+lam*offset,-lam,-F(1)]);bb.append(F(0))
  eq=[F(1)]*n+[F(0)]*n+[F(1),F(0),F(0)]
  if 'infeasible_energy' in row:
   k=2*n-1;assert p.dual(en,aa[:k]+aa[k+2:],bb[:k]+bb[k+2:],eq,row['infeasible_energy'])>hi
  else:
   value=p.dual([C*x for x in xs]+[F(1)]*n+[F(0),C,F(1)],aa,bb,eq,row['cert']);margins.append(value-A)
 assert next(ex,None) is None and gc==r['component_duals'] and len(d['components']['short'])==r['short_duals'] and min(margins)==F(r['short_margin'])>0
 assert pen[0][1]+8*B-(A-C*lo+B*lo)==F(r['long_back_margin'])>0
 assert pen[1][1]+8*C-A==F(r['long_main_margin'])>0
 assert min((22-e)*B-(A-C*e) for e in (lo,hi))==F(r['tail_mass_coefficient'])>0
 assert physical(r['endpoint17'])==A-C*hi and len(r['endpoint17']['spectrum'])==17
 ends=r['witnesses'][:2];support=ends[0]['support'];pp=[list(map(F,w['population'])) for w in ends]
 for w in r['witnesses']:assert physical(w)==A-C*F(w['energy'])
 for shell in {x+b for x in support for b in range(4)}:
  terms=[(i,b) for i,x in enumerate(support) for b in range(4) if x+b==shell];wins=[]
  for pv in pp:
   mx=max(pv[i]*bath[b] for i,b in terms);wins.append({(i,b) for i,b in terms if pv[i]*bath[b]==mx})
  assert wins[0]&wins[1]
 ds=[c.physical(w)[1] for w in ends];assert all(a*b>=0 for a,b in zip(*ds))
 # Exact homogeneous nullspace: every equality population is the same affine diagonal.
 slopes=[(b-a)/(hi-lo) for a,b in zip(*pp)];constants=[a-b*lo for a,b in zip(pp[0],slopes)]
 for xs,o,cc in contacts:
  aa,bb,cost=c.reconstruct(xs,o,'strip');n=len(xs);yy=list(map(F,cc['y']));zz=F(cc['z'])
  reduced=[cost[j]-sum(a[j]*v for a,v in zip(aa,yy))-zz*int(j<n) for j in range(2*n)]
  equations=[[int(j<n) for j in range(2*n)]+[0,-1],[xs[j] if j<n else 0 for j in range(2*n)]+[-1,0]]
  for j,v in enumerate(reduced):
   if v>0:equations.append([int(k==j) for k in range(2*n)]+[0,0])
  for row,v,b in zip(aa,yy,bb):
   if v<0:equations.append(row+[0,-b])
  kernel=s.Matrix(equations).nullspace()
  for j,e in enumerate(xs):
   a,b=(constants[support.index(e)],slopes[support.index(e)]) if e in support else (F(0),F(0))
   desired=s.Matrix([int(k==j) for k in range(2*n)]+[-b,-a])
   assert all((v.T*desired)[0]==0 for v in kernel),'equality population'
 forced=set()
 for z in {x+b for x in support for b in range(4)}:
  if sum(z-x in (0,1,2,3) for x in support)==2:forced.update(z-b for b in range(4))
 assert forced==set(range(21))
 # Actual physical half-spacing competitors test the essential spacing boundary.
 for E in (lo,hi):
  weight=(E-F(6,5))/F(3,2);xs=[F(1),F(3,2),F(3),F(7,2)]
  pv=[(1-weight)*F(9,10),weight*F(2,5),(1-weight)*F(1,10),weight*F(3,5)];spec=[F(j,2) for j in range(10)]
  assert min(pv)>0 and sum(pv)==1 and sum(x*y for x,y in zip(xs,pv))==E
  for z in {x+b for x in xs for b in range(4)}:assert sum(z-x in (0,1,2,3) for x in spec)>=2*sum(z-x in (0,1,2,3) for x in xs)
  ret=sum(max(pv[i]-sum(max(pv[j]*bath[k] for j,x in enumerate(xs) for k in range(4) if x+k==y+b)/2 for b in range(4)),0) for i,y in enumerate(xs))
  assert ret==F(57,100)-E/10<A-C*E
 faults=[];xs,o,cc=contacts[0]
 for name in ('normalization','sign'):
  bad=deepcopy(cc)
  if name=='normalization':bad['z']=str(F(bad['z'])+1)
  else:bad['y'][0]='1'
  try:c.validate_dual(xs,o,bad)
  except AssertionError:faults.append(name)
  else:raise AssertionError('accepted dual fault')
 print('PASS global interval separate',count,'connected;',gc,'component;',len(d['components']['short']),'short certificates;',len(margins),'strict short bounds;',len(contacts),'interior equality cells force affine population;21 compulsory levels;',len(endpoint_contacts),'additional endpoint contacts;17-level endpoint witness;2 half-spacing counterexamples;',faults,flush=True)
 return dict(connected=count,components=gc,short=len(margins),equality_cells=len(contacts))

def run():
 r=json.loads((ROOT/'lab/process/k2031-thermal-phase-boundaries.json').read_text());symbolic();count=0;fixture=None
 for row in r['rows']:
  E=F(row['energy']);best,h,n=independently_minimize(E);count+=n
  assert h==row['first_excluded_head'] and best[0]==F(row['winner']['return_value']),'family optimum'
  for w in row['candidates']:
   if w['tail'] is not None:physical(w);fixture=w
  if row['winner']['tail'] is not None:assert best[1:]==(row['winner']['head'],row['winner']['tail'])
 generalized_symbolic();general_count=0
 for row in r['generalized_rows']:
  E=F(row['energy']);seed=next(F(x['winner']['return_value']) for x in r['rows'] if F(x['energy'])==E)
  best,h,n=general_independent(E,seed);general_count+=n
  assert best==F(row['winner']['return_value']) and h==row['first_excluded_head'],'unbounded three-parameter optimum'
  assert F(row['head_lower_bound'])>=best,'head exclusion bound'
  for w in row['candidates']:
   if w['tail'] is not None:physical(w)
 assert physical(r['failed_backward_bound'])<F(20321037,42923912)-F(992331,42923912)*F(13,10)+(F(13,10)-F(r['failed_backward_bound']['energy']))/44,'failed backward proof transfer'
 assert physical(r['broader_family_counterexample'])<F(20321037,42923912)-F(992331,42923912)*F(13,10),'longer rise counterexample'
 # Independently derive all shell-order and positive-deficit face inequalities
 # for the old17 affine diagonal from its two prior physical witnesses.
 old=json.loads((ROOT/'lab/process/k2029-multicomponent-thermal-placement.json').read_text())['witnesses']
 p0=list(map(F,old[0]['population']));p1=list(map(F,old[1]['population']));beta=[5*(b-a) for a,b in zip(p0,p1)];alpha=[a-F(7,5)*b for a,b in zip(p0,beta)];xs=old[0]['support'];constraints=list(zip(alpha,beta));deficits=[]
 for i,x in enumerate(xs):
  da,db=alpha[i],beta[i]
  for b in range(4):
   terms=[(j,k) for j,y in enumerate(xs) for k in range(4) if y+k==x+b]
   winner=max(terms,key=lambda jk:(alpha[jk[0]]+F(3,2)*beta[jk[0]])*bath[jk[1]])
   j,k=winner;da-=alpha[j]*bath[k]/2;db-=beta[j]*bath[k]/2
   for jj,kk in terms:constraints.append((alpha[j]*bath[k]-alpha[jj]*bath[kk],beta[j]*bath[k]-beta[jj]*bath[kk]))
  sig=1 if da+F(3,2)*db>=0 else -1;constraints.append((sig*da,sig*db))
 lo=max([-a/b for a,b in constraints if b>0]);hi=min([-a/b for a,b in constraints if b<0]);assert [str(lo),str(hi)]==r['affine17_feasibility']
 # Explicit crossing signs are evaluated by actual bath populations, not labels.
 for E in [F(13,10),F(9,5)]:
  w=next(x['winner'] for x in r['rows'] if F(x['energy'])==E)
  assert physical(w)<F(985095,2040416)-F(61407,2040416)*E
 faults=[]
 for kind in ('population','completion','return'):
  w=deepcopy(fixture)
  if kind=='population':w['population'][0]=str(F(w['population'][0])+F(1,100))
  elif kind=='completion':w['spectrum'].remove(2)
  else:w['return_value']=str(F(w['return_value'])-F(1,100))
  try:physical(w)
  except AssertionError as e:assert str(e);faults.append([kind,str(e)])
  else:raise AssertionError('accepted physical fault')
 try:symbolic(26)
 except AssertionError as e:faults.append(['tail_coefficient',str(e)])
 else:raise AssertionError('accepted tail fault')
 bad=deepcopy(r['rows'][5]['winner']);bad['return_value']=str(F(bad['return_value'])+F(1,100000))
 try:physical(bad)
 except AssertionError as e:faults.append(['phase_coefficient',str(e)])
 else:raise AssertionError('accepted phase fault')
 global_probe(r['certified_interval'])
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2031 separate:',count,'finite candidate evaluations;3 symbolic identities;whole17 face;11 complete family searches;2 actual phase competitors;',faults,';',general_count,'generalized candidates;2 generalized symbolic identities;11 unbounded head/rise/tail optima;7 provenance hashes',flush=True)
if __name__=='__main__':run()
