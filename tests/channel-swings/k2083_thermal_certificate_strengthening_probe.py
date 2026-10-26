"""Independent raw-bath inequalities and rational row-reduced new geometry."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import importlib.util,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('prior_probe',ROOT/'tests/channel-swings/k2074_subdivided_incoming_thermal_bound_probe.py');prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
Z=Q(0);K=prior.K;C=prior.C;LH=prior.LH;bell=prior.bell;allowed=prior.allowed;raw=prior.raw;strong_shift=prior.strong_shift
PREFIXES={(2,2,2),(2,2,3),(2,3,2),(3,1,3),(3,2,2)}
def covered_caps(ci,s,prefixes=PREFIXES):
 if ci==235:return set()
 assert ci==188
 seen=set()
 def walk(ds,n):
  if n>20:return
  if len(ds)>=4 and (n,ds[-1]) in {(18,2),(19,2),(20,2)}:
   assert len(ds)==4 and tuple(ds[:3]) in prefixes,'removed cap has unexpanded route'
   seen.add(tuple(ds))
  for gap in K:
   if ds[-1]+gap>=4:walk(ds+[gap],n+gap)
 for gap in allowed(s):walk([gap],s[-1]+gap)
 assert seen=={(2,2,2,2),(2,2,3,2),(2,3,2,2),(3,1,3,2),(3,2,2,2)},'cap route census'
 return {(18,2),(19,2),(20,2)}
def assignment(ci,v,bank,geom,geom3,geom4=None,high=True,prefixes=PREFIXES):
 a,t=Q(v['a']),-Q(v['s']);s=bank[ci]['s'];z=s[-1];ell=strong_shift(s);g=bell(a,t);h=bell(a,t,ell);count=0
 third=set()
 for d in allowed(s):
  for e in K:
   if d+e>=4:
    for f in K:
     if e+f>=4:third.update((z+d+e+f+h,h) for h in K if f+h>=4)
 for n in range(12,65):
  for d in K:
   if (n,d) in third:third.update((n+e,e) for e in K if d+e>=4 and n+e<=64)
 exemptions=covered_caps(ci,s,prefixes)
 assert all(g[n,d]<=C[d] for n,d in third if n<=64 and (n,d) not in exemptions),'fourth-plus caps'
 theta=Q(v['common_tail_weight']);assert 0<=theta<=1
 prices=[]
 def add_price(points,rewards,d):
  L,H=LH[d]
  price=max(sum(q*x for q,x in zip(rewards,row[:-1]))-row[-1]-theta*min(Q(1),max(Z,L*row[0]-H))/2 for row in points)
  prices.append(price)
 for d in allowed(s):
  n=z+d;q=a-t*n;L,H=LH[d]
  assert q<=Q(1,2),'single recession'
  pts=[(x,raw([0,d],[Q(1),x])-Q(1,2)) for x in [Z,K[d],H/L,(1+H)/L]];add_price(pts,[q],d)
  for e in K:
   if d+e<4:continue
   gg=a-t*(n+e);vs,rs=geom[d,e]
   assert all(q*x+gg*y<=c for x,y,c in rs),'joint recession';add_price(vs,[q,gg],d)
   for f in K:
    if e+f<4:continue
    extended=ci==188 and (d,e,f) in prefixes;g3=a-t*(n+e+f) if extended else g[n+e+f,f];vs3,rs3=geom3[d,e,f]
    assert all(q*x+gg*y+g3*z<=c for x,y,z,c in rs3),'triple recession';add_price(vs3,[q,gg,g3],d)
    if extended:
     for h4 in K:
      if f+h4<4:continue
      vs4,rs4=geom4[d,e,f,h4];gg4=g[n+e+f+h4,h4]
      assert all(q*x+gg*y+g3*z+gg4*w<=c for x,y,z,w,c in rs4),'four-terminal recession'
      add_price(vs4,[q,gg,g3,gg4],d)
 for vv in bank[ci]['vertices']:
  pp=list(map(Q,vv['p']));p=pp[-1];A=p
  if len(s)>1:
   L,H=LH[s[-1]-s[-2]];A=max(Z,p-max(Z,H*pp[-2]-L*p))
  boundary=max([Z]+[p*price+theta*A/2 for price in prices])
  assert Q(vv['value'])>=a-t*Q(vv['energy'])+boundary,'low joint inequality'
  assert raw(s,pp)==Q(vv['value']),'low raw bath return';count+=1
 if high:
  assert all(x<=C[d] for (n,d),x in h.items()),'high caps'
  assert all(a-t*(n+ell)+K[d]*h.get((n+d,d),Z)<=Q(1,2) for n in range(12,65) for d in K),'erased root'
  for cell in bank:
   coef=max([Z]+[K[d]*h.get((cell['s'][-1]+d,d),Z) for d in allowed(cell['s'])])
   for vv in cell['vertices']:
    assert Q(vv['value'])>=a-t*(Q(vv['energy'])+ell)+coef*Q(vv['p'][-1]),'high-component inequality';count+=1
 return count

def global_check(d,ass):
 aa=deepcopy(ass)
 for ci,v in d['replacements'].items():aa[int(ci)]=v
 a,s=map(Q,d['lower_line']);left,right=map(Q,d['interval']);pl,pr=map(Q,d['previous_interval'])
 assert left<pl<pr<right,'strict interval extension'
 for v in aa:
  for E in [left,right]:assert Q(v['a'])+Q(v['s'])*E>=a+s*E,'all-cell dominance'
 assert [[i for i,v in enumerate(aa) if Q(v['a'])+Q(v['s'])*E==a+s*E] for E in [left,right]]==[[164,187],[185,187]],'exact endpoint tie census'
 mid=(left+right)/2
 assert all(Q(v['a'])+Q(v['s'])*mid>a+s*mid for i,v in enumerate(aa) if i!=187),'strict interior competitors'
 return len(aa)
def endpoint_checks(doc,bank,ass,g2,g3,g4):
 import sys
 p=sys.modules[__name__]
 a,t=Q(ass[164]['a']),-Q(ass[164]['s']);ss=bank[164]['s'];z=ss[-1];g=p.bell(a,t);theta=Q(69,100);values=[];rays=[]
 def add(ds,pts,rewards):
  L,H=p.LH[ds[0]]
  for row in pts:values.append((sum(q*x for q,x in zip(rewards,row[:-1]))-row[-1]-theta*min(Q(1),max(Q(0),L*row[0]-H))/2,ds,row[:-1]))
 for d in p.allowed(ss):
  n=z+d;q=a-t*n;L,H=p.LH[d];rays.append(Q(1,2)-q);add((d,),[(x,p.raw([0,d],[Q(1),x])-Q(1,2)) for x in [Q(0),p.K[d],H/L,(1+H)/L]],[q])
  for e in p.K:
   if d+e<4:continue
   qq=a-t*(n+e);vs,rs=g2[d,e];add((d,e),vs,[q,qq]);rays.extend(c-q*x-qq*y for x,y,c in rs)
   for f in p.K:
    if e+f<4:continue
    ext=(d,e,f) in [(3,1,3),(3,2,2),(3,2,3),(3,3,2)];q3=a-t*(n+e+f) if ext else g[n+e+f,f];vs,rs=g3[d,e,f];add((d,e,f),vs,[q,qq,q3]);rays.extend(c-q*x-qq*y-q3*z for x,y,z,c in rs)
    if ext:
     for h4 in p.K:
      if f+h4<4:continue
      vs,rs=g4[d,e,f,h4];q4=g[n+e+f+h4,h4];add((d,e,f,h4),vs,[q,qq,q3,q4]);rays.extend(c-q*x-qq*y-q3*z-q4*w for x,y,z,w,c in rs)
 beta=max(v for v,ds,x in values);w=[(ds,x) for v,ds,x in values if v==beta];assert w==[((3,1,3,1),(Q(1,23),Q(7,667),Q(7,15341),Q(49,444889)))], 'unique164 terminal contact';assert min(rays)>0,'strict164 recession'
 zeros=[]
 for vi,v in enumerate(bank[164]['vertices']):
  pp=list(map(Q,v['p']));L,H=p.LH[ss[-1]-ss[-2]];A=max(Q(0),pp[-1]-max(Q(0),H*pp[-2]-L*pp[-1]));sl=Q(v['value'])-a+t*Q(v['energy'])-max(Q(0),beta*pp[-1]+theta*A/2)
  if sl==0: zeros.append((vi,pp,A))
 assert zeros==[(26,list(map(Q,['243/653','729/1306','81/1306','9/1306','1/1306'])),Q(0))], 'unique164 low contact'
 for vi,pp,A in zeros:
  for ds,xs in w:
   sup=list(ss);pop=list(pp)
   for gap,x in zip(ds,xs):sup.append(sup[-1]+gap);pop.append(pp[-1]*x)
   n,d=sup[-1],ds[-1];policy=[]
   while True:
    opts=[(a-t*n+p.K[e]*g.get((n+e,e),Q(0)),e) for e in p.K if d+e>=4];best=max([Q(0)]+[v for v,e in opts]);assert best==g[n,d] and best>0,'positive164 Bellman state'
    choices=[e for v,e in opts if v==best and g.get((n+e,e),Q(0))>0];policy.append((n,d,p.C[d]-g[n,d],choices))
    if len(choices)!=1:
     assert choices==[] and best==a-t*n,'164 terminal reward'
     break
    d=choices[0];n+=d;sup.append(n);pop.append(pop[-1]*p.K[d])
   assert sup==[1,3,5,7,9,12,13,16,17,20,21,24,25,28,29,32,33,36,37,40,41,44],'forced164 support'
   assert all(sl>0 for n,gap,sl,choices in policy),'strict164 visited caps'
   assert all(a-t*(n+e)<0 for e in p.K if d+e>=4),'strict164 final negative rewards'
   energy=sum(n*x for n,x in zip(sup,pop))/sum(pop)
   assert energy==Q(doc['endpoint164_necessary_energy']) and energy!=Q(doc['interval'][0]),'164 energy incompatibility'
 # Strict high/root margins exclude all other components for164.
 a,t=Q(ass[164]['a']),-Q(ass[164]['s']);ell=Q(21,2);h=bell(a,t,ell)
 high=[]
 for bc in bank:
  coef=max([Q(0)]+[K[dd]*h.get((bc['s'][-1]+dd,dd),Q(0)) for dd in allowed(bc['s'])])
  high.extend(Q(v['value'])-a+t*(Q(v['energy'])+ell)-Q(v['p'][-1])*coef for v in bc['vertices'])
 assert min(high)>0 and all(x<=C[dd] for (n,dd),x in h.items()),'strict164 high and caps'
 assert min(Q(1,2)-a+t*(n+ell)-K[dd]*h.get((n+dd,dd),Q(0)) for n in range(12,65) for dd in K)>0,'strict164 roots'
 # Cell185 retains the original uniform certificate, not a fitted Bellman replacement.
 v=ass[185];a,t,eta=Q(v['a']),-Q(v['s']),Q(v['eta']);assert v['kind']=='uniform' and Q(v['shift'])==10
 assert a-12*t==eta and 0<t<eta and bank[185]['s']==[1,3,5,7,9,11]
 assert min(11+dd for dd in allowed(bank[185]['s']))==13,'185 true erased threshold'
 beta=max({1:Q(14,55),2:Q(1,8),3:Q(3,55)}[dd] for dd in allowed(bank[185]['s'])) # inherited uniform boundary constants
 assert beta==Q(doc['endpoint185_boundary_factor'])==Q(1,8),'185 boundary allowance'
 # The universal piecewise linear inequality reduces to two exact coefficients.
 assert t>0 and eta-t>0,'185 slack tq+max(0,eta(B-q)) >= tB'
 return len(values),len(high)

def main():
 d=json.loads((ROOT/'lab/process/k2083-thermal-certificate-strengthening.json').read_text())
 for path,h in d['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h,'pin'
 prev=json.loads((ROOT/'lab/process/k2074-subdivided-incoming-thermal-bound.json').read_text());_,bank,ass,g2,g3,g4=prior.inputs(prev)
 for ci,v in prev['replacements'].items():ass[int(ci)]=v
 oldkeys=set(g4);stored=prior.decode(d['quad_arrangements'])
 for key in oldkeys:assert stored[key]==g4[key],'reused geometry equals pinned rows'
 g4.update(stored)
 count=sum(assignment(int(ci),v,bank,g2,g3,g4) for ci,v in d['replacements'].items());print('PASS low/high vertex inequalities',count,flush=True)
 n=global_check(d,ass);print('PASS endpoint164 census/high rows',endpoint_checks(d,bank,ass,g2,g3,g4),flush=True);geometry=0
 for gaps,(vs,rs) in g4.items():
  if gaps in oldkeys:continue
  pts,rays=prior.old.geometry4(gaps)
  assert {r[:-1] for r in vs}==pts and {r[:-1] for r in rs}==rays,'new geometry completeness'
  ss=[0]
  for gap in gaps:ss.append(ss[-1]+gap)
  for row in vs:assert raw(ss,[Q(1),*row[:-1]])-Q(1,2)==row[-1],'raw tail return';geometry+=1
  for row in rs:assert raw(ss,[Z,*row[:-1]])==row[-1],'raw tail recession';geometry+=1
 witness=json.loads((ROOT/'lab/process/k2068-thermal-population-construction.json').read_text());left,right=map(Q,d['interval']);ul,ur=map(Q,witness['energy_interval'])
 assert ul<left<right<ur,'physical population chamber'
 assert list(map(Q,witness['line']))==list(map(Q,d['lower_line'])),'same optimizer line'
 for E in [left,Q(5,2),right]:
  pop=[Q(a)+E*Q(b) for a,b in witness['population_affine']];ss=witness['occupied_support']
  assert min(pop)>0 and sum(pop)==1 and sum(Q(n)*p for n,p in zip(ss,pop))==E,'physical witness'
  assert raw(ss,pop)==Q(d['lower_line'][0])+E*Q(d['lower_line'][1]),'raw physical return'
  assert set().union(*(set(range(n-1,n+2)) for n in ss))==set(range(41)),'compulsory physical shells'
 # Prior K2068 exact chamber proof and K2074 countable transfer are inherited.
 print('PASS BASELINE',n,'global lines',geometry,'new exact geometry rows; 3 physical witnesses',flush=True)
 faults=[]
 badenergy=deepcopy(d);badenergy['endpoint164_necessary_energy']=d['interval'][0];faults.append(('false164 equality energy',lambda:endpoint_checks(badenergy,bank,ass,g2,g3,g4)))
 badfactor=deepcopy(d);badfactor['endpoint185_boundary_factor']='1/7';faults.append(('false185 boundary',lambda:endpoint_checks(badfactor,bank,ass,g2,g3,g4)))
 bad=deepcopy(d);bad['interval'][0]='2';faults.append(('false extension',lambda:global_check(bad,ass)))
 for missing in [(2,2,2),(2,2,3),(2,3,2),(3,1,3),(3,2,2)]:
  faults.append(('missing '+str(missing),lambda m=missing:covered_caps(188,bank[188]['s'],PREFIXES-{m})))
 wrong=deepcopy(d['replacements']['188']);wrong['a']='1'
 faults.append(('false coefficient',lambda:assignment(188,wrong,bank,g2,g3,g4,high=False)))
 corrupt=deepcopy(g4);key=(2,2,3,2);vs,rs=corrupt[key];corrupt[key]=(vs,[(Q(1),Q(0),Q(0),Q(0),Q(-100))]+rs)
 faults.append(('false tail loss',lambda:assignment(188,d['replacements']['188'],bank,g2,g3,corrupt,high=False)))
 for name,check in faults:
  try:check()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e))
  else:raise AssertionError('undetected '+name)
 print('PASS',len(faults),'faults; finite geometry/inequalities separate from analytic transfer')
if __name__=='__main__':main()
