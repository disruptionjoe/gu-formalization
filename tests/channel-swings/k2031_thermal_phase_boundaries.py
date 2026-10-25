"""Exact optimization of the infinite geometric head/turn/tail catalyst family.

Optimizer-free replay; unbounded family reductions and a separately certified global phase.
The analytic proof in the exploration supplies the infinite search reduction.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,argparse
from k2006_uniform_two_component_spacing import rate,valid
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2031-thermal-phase-boundaries.json'
A17,C17=Q(985095,2040416),Q(61407,2040416)
def coefficients(h,m=None):
 z=9**h;A=Q(5*z-1,40);c=Q(25*z-8*h-9,160);B=Q(247,80);d=Q(247*h,40)+Q(3923,320)
 if m is not None:
  q=Q(1,9**(m+1));B-=Q(27,16)*q;d-=Q(27,64)*(8*m+8*h+29)*q
 return A,B,c,d

def ratio(h,m,E):
 A,B,c,d=coefficients(h,m);return (d-B*E)/(A*E-c)
def endpoints(h,m=None):
 A,B,c,d=coefficients(h,m)
 return (36*c+d)/(36*A+B),(Q(8,3)*c+d)/(Q(8,3)*A+B)
def line(h,m=None):
 A,B,c,d=coefficients(h,m);D=A*d-B*c;P=Q(9**(h-1),2)
 assert D>0
 return (P*d-Q(3,4)*c)/D,(Q(3,4)*A-P*B)/D

def difference_sign(h,m):
 z=9**h;return (896*z+216)*m-1080*h*z-112*z+513+135*z*Q(1,9**(m+1))
def best_tail(h):
 # Proved T_h(h)<0<T_h(2h+1) and strictly increasing for every m>=0.
 return next(m for m in range(h+1,2*h+2) if difference_sign(h,m)>0)

def witness(h,m,E):
 A,B,c,d=coefficients(h,m);D=A*d-B*c;u=(d-B*E)/D;v=(A*E-c)/D
 p=[9**(h-1-i)*u for i in range(h)]+[(u+4*v)/10,v]+[Q(3,2*9**k)*v for k in range(m+1)]
 s=list(range(1,2*len(p),2));spec=list(range(s[-1]+2));a,b=line(h,m)
 assert min(p)>0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
 assert Q(8,3)<=u/v<=36 and valid(spec,s) and rate(Q(1,2),s,p)==a+b*E
 return dict(head=h,tail=m,energy=str(E),support=s,population=list(map(str,p)),spectrum=spec,return_value=str(a+b*E),dimension=len(spec))

def solve(E):
 E=Q(E);assert Q(5,4)<E<=Q(18,5)
 candidates=[];h=1
 while endpoints(h)[1]>=E:
  rinf=ratio(h,None,E);r0=ratio(h,0,E)
  if Q(8,3)<=rinf<=36:
   a,b=line(h);candidates.append(dict(head=h,tail=None,return_value=str(a+b*E),dimension=None))
  if rinf>Q(8,3) and r0<=36:
   m=best_tail(h)
   if ratio(h,m,E)>36:
    m=max(k for k in range(m) if ratio(h,k,E)<=36)
   elif ratio(h,m,E)<Q(8,3):
    while ratio(h,m,E)<Q(8,3):m+=1
   if Q(8,3)<=ratio(h,m,E)<=36:
    w=witness(h,m,E);candidates.append(w)
  h+=1
 assert candidates
 best=min(candidates,key=lambda x:Q(x['return_value']))
 return dict(energy=str(E),first_excluded_head=h,candidates=candidates,winner=best)

def general_coefficients(h,l,m=None):
 z=9**h;w=Q(3,2)**l;A=Q(5*z-1,40);c=Q(25*z-8*h-9,160)
 B=Q(25,8)*w-Q(8,5);d=w*Q(200*h+200*l-75,32)-Q(16*h-32,5)
 if m is not None:
  q=Q(1,9**(m+1));B-=Q(9,8)*w*q;d-=Q(9,32)*w*q*(8*h+8*l+8*m+21)
 return A,B,c,d,w

def general_ratio(h,l,m,E):
 A,B,c,d,w=general_coefficients(h,l,m);return (d-B*E)/(A*E-c)
def general_line(h,l,m=None):
 A,B,c,d,w=general_coefficients(h,l,m);D=A*d-B*c;P=Q(9**(h-1),2)
 assert D>0
 return (P*d-w*c/2)/D,(w*A/2-P*B)/D

def general_sign(h,l,m):
 z=9**h;w=Q(3,2)**l;q=Q(1,9**(m+1))
 return (640*w*z+72*w-512*z)*m-360*h*w*z-360*l*w*z+72*l*w-512*l*z+2200*w*z+99*w-2304*z+45*q*w*z

def general_witness(h,l,m,E):
 A,B,c,d,w=general_coefficients(h,l,m);D=A*d-B*c;u=(d-B*E)/D;v=(A*E-c)/D
 p=[9**(h-1-i)*u for i in range(h)]+[(u+4*v)/10]+[Q(3,2)**k*v for k in range(l+1)]+[w*v/Q(9**j) for j in range(1,m+1)]
 xs=list(range(1,2*len(p),2));spec=list(range(xs[-1]+2));a,b=general_line(h,l,m)
 assert min(p)>0 and sum(p)==1 and sum(x*y for x,y in zip(xs,p))==E
 assert Q(8,3)<=u/v<=36 and valid(spec,xs) and rate(Q(1,2),xs,p)==a+b*E
 return dict(head=h,rise=l,tail=m,energy=str(E),support=xs,population=list(map(str,p)),spectrum=spec,return_value=str(a+b*E),dimension=len(spec))

def general_solve(E):
 E=Q(E);seed=solve(E)['winner'];assert seed['tail'] is not None
 best=general_witness(seed['head'],1,seed['tail'],E);inc=Q(best['return_value']);assert inc<Q(4,9)
 heads=[];candidates=[];h=1
 while True:
  z=9**h;eu=Q(25*z-8*h-9,4*(5*z-1));massbound=min(Q(1),(E-eu)/(2*h+1-eu));lower=Q(4,9)-Q(64,225)*massbound
  if lower>=inc:break
  l=1;tails=[]
  while general_ratio(h,l,0,E)<=36:
   ri=general_ratio(h,l,None,E);first=None
   if Q(8,3)<=ri<=36:
    a,b=general_line(h,l);candidates.append(dict(head=h,rise=l,tail=None,return_value=str(a+b*E),dimension=None))
    if a+b*E<inc:inc=a+b*E;best=candidates[-1]
   if ri>Q(8,3):
    m=0
    # Strict monotone sign with positive linear coefficient guarantees termination.
    while general_sign(h,l,m)<0:m+=1
    if general_ratio(h,l,m,E)>36:
     m=max(k for k in range(m) if general_ratio(h,l,k,E)<=36)
    elif general_ratio(h,l,m,E)<Q(8,3):
     while general_ratio(h,l,m,E)<Q(8,3):m+=1
    if Q(8,3)<=general_ratio(h,l,m,E)<=36:
     w=general_witness(h,l,m,E);candidates.append(w);tails.append([l,m])
     if Q(w['return_value'])<inc:inc=Q(w['return_value']);best=w
   l+=1
  heads.append(dict(head=h,first_excluded_rise=l,selected_tails=tails));h+=1
 return dict(energy=str(E),first_excluded_head=h,head_lower_bound=str(lower),heads=heads,candidates=candidates,winner=best)

def produce():
 tests=0;sequence=[]
 for h in range(1,13):
  m=best_tail(h);sequence.append(m)
  assert difference_sign(h,h)<0<difference_sign(h,2*h+1)
  assert difference_sign(h,m-1)<0<difference_sign(h,m)
  for k in range(2*h+3):
   lo,hi=endpoints(h,k);E=(lo+hi)/2;witness(h,k,E);tests+=1
   assert difference_sign(h,k+1)>difference_sign(h,k)
   a,b=line(h,k);aa,bb=line(h,k+1)
   assert ((aa+bb*E)-(a+b*E)>0)==(difference_sign(h,k)>0)
 # Explicit positive controls for both boundaries of the17-level affine face.
 lo,hi=endpoints(2,3);assert lo==Q(115329,89105) and hi==Q(14079,7295)
 assert line(2,3)==(A17,-C17)
 cross=[]
 for h,m in [(3,4),(1,2)]:
  a,b=line(h,m);e=(A17-a)/(b+C17);assert max(lo,endpoints(h,m)[0])<e<min(hi,endpoints(h,m)[1])
  cross.append(dict(head=h,tail=m,energy=str(e),return_value=str(A17-C17*e)))
 energies=[Q(1250001,1000000),Q(1251,1000),Q(63,50),Q(13,10),Q(27,20),Q(3,2),Q(17,10),Q(9,5),Q(2),Q(3),Q(18,5)]
 rows=[solve(e) for e in energies]
 counter=general_witness(3,2,1,Q(13,10));old_a,old_b=line(3,4)
 assert Q(counter["return_value"])<old_a+old_b*Q(13,10)
 ga,gb=general_line(3,2,3);cross_general=(A17-ga)/(gb+C17)
 ac,bc,cc,dc,_=general_coefficients(3,2,3)
 general_face=[(36*cc+dc)/(36*ac+bc),(Q(8,3)*cc+dc)/(Q(8,3)*ac+bc)]
 assert max(lo,general_face[0])<cross_general<min(hi,general_face[1])
 for e in [Q(13,10),Q(9,5)]:assert Q(solve(e)['winner']['return_value'])<A17-C17*e
 failed_back=dict(energy='256/205',support=[1,3,5,7],population=[str(Q(x,820)) for x in [729,81,9,1]],spectrum=list(range(9)),return_value='729/1640')
 assert valid(failed_back['spectrum'],failed_back['support']) and rate(Q(1,2),failed_back['support'],list(map(Q,failed_back['population'])))==Q(failed_back['return_value'])
 assert Q(failed_back['return_value'])<old_a+old_b*Q(13,10)+(Q(13,10)-Q(failed_back['energy']))/44
 inputs=['lab/process/k2025-wide-spacing-ladder-program.json','lab/process/k2029-multicomponent-thermal-placement.json','tests/channel-swings/k2027_thermal_pattern_frontier.py','tests/channel-swings/k2027_thermal_pattern_frontier_probe.py','tests/channel-swings/k2029_multicomponent_thermal_placement.py','tests/channel-swings/k2029_multicomponent_thermal_placement_probe.py','explorations/conditional-build/k2020-posttransition-tail-and-resources-2026-10-24.md']
 return dict(result_id='K2031',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',scope='Exact-mean optimization of the original head/turn/tail family and complete unbounded head/rise/tail optimization at the11 certified energies, using a supplied feasible incumbent below4/9. Actual physical upper bounds for every0<delta<=1. The separate certified_interval supplies the unrestricted optimum and sharp21 dimensions for13/10<=E<E*=8283273393/6147208289, with optimal value at E* and a17-level endpoint witness and1/2<delta<=1. No complete phase diagram or dimension law outside that interval.',affine17_feasibility=[str(lo),str(hi)],competing_crossings=cross,broader_family_counterexample=counter,failed_backward_bound=failed_back,generalized_low_branch=dict(head=3,rise=2,tail=3,intercept=str(ga),slope=str(gb),feasibility=list(map(str,general_face)),crossing_with17=str(cross_general)),tail_minima_first12=sequence,finite_physical_controls=tests,rows=rows,generalized_rows=[general_solve(e) for e in energies],accumulation=dict(energy='5/4',return_value='4/9',population='p_i=8/9^(i+1), occupied energies1+2i, all nonnegative integers as physical completion',claim='countable physical boundary member; no claim of unrestricted optimality or required infinite dimension'),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
def global_unpack(r):
 import zlib,base64
 raw=zlib.decompress(base64.b64decode(r['payload']))
 assert hashlib.sha256(raw).hexdigest()==r['payload_sha256']
 return json.loads(raw)

def check_global(r):
 """All rational duals, complete ordered coverage, physical witnesses and transfer margins."""
 from itertools import product
 import k2027_thermal_pattern_frontier as c
 import k2029_multicomponent_thermal_placement as p
 A,C,B=Q(15398019,32499160),Q(761157,32499160),Q(43,2000);lo,hi=Q(13,10),Q(8283273393,6147208289)
 c.A,c.C,c.B,c.LO,c.HI=A,C,B,lo,hi;p.A,p.C,p.B,p.lo,p.hi=A,C,B,lo,hi
 d=global_unpack(r);expected=iter((ss,o) for ss in c.supports(21) if min(ss)<=hi for o in product((-1,1),repeat=len(ss)-1));count=0;contacts=0
 for row in d['connected']:
  ss,o=next(expected);assert row['s']==list(ss) and row['o']==list(o)
  assert len(row['certificates'])==2
  for kind,cert in zip(('low','strip'),row['certificates']):
   assert cert['kind']==kind
   if 'infeasible_energy' in cert:assert c.dual(ss,o,cert['infeasible_energy'])>(lo if kind=='low' else hi)
   elif 'infeasible_maxenergy' in cert:assert kind=='strip' and -c.dual(ss,o,cert['infeasible_maxenergy'])<lo
   else:
    value=c.dual(ss,o,cert);target=A-C*lo+B*lo if kind=='low' else A
    assert value>=target
    if kind=='strip' and value==target:contacts+=1
   count+=1
 assert next(expected,None) is None and count==r['connected_duals']
 penalties=[];global_count=0
 for bank in d['components']['banks']:
  lam,aa=Q(bank['slope']),Q(bank['intercept']);exp=iter((ss,o) for ss in c.supports(14) for o in product((-1,1),repeat=len(ss)-1))
  for row in bank['rows']:
   ss,o=next(exp);assert row['s']==list(ss) and row['o']==list(o);n=len(ss);rows=p.cell(ss,o)
   assert p.verify([lam*x for x in ss]+[Q(1)]*n,rows,[Q(0)]*len(rows),[Q(1)]*n+[Q(0)]*n,row['cert'])>=aa;global_count+=1
  assert next(exp,None) is None and 15*lam>aa;penalties.append((lam,aa))
 assert [x[0] for x in penalties]==[B,C]
 penalties.extend([(Q(1,4),Q(3,4)),(Q(3,20),Q(63,100))])
 exp=iter((ss,o) for ss in c.supports(7) if ss[0]==1 and (1 if len(ss)==1 else ss[-2]+3)<8 for o in product((-1,1),repeat=len(ss)-1));margins=[]
 for row in d['components']['short']:
  ss,o=next(exp);assert row['s']==list(ss) and row['o']==list(o)
  co,aa,bb,eq,off=p.shortprogram(ss,o,penalties);assert off==Q(row['offset'])
  if 'infeasible_energy' in row:
   n=len(ss);k=2*n-1;en=list(map(Q,ss))+[Q(0)]*n+[Q(0),Q(1),Q(0)]
   assert p.verify(en,aa[:k]+aa[k+2:],bb[:k]+bb[k+2:],eq,row['infeasible_energy'])>hi
  else:margins.append(p.verify(co,aa,bb,eq,row['cert'])-A)
 assert next(exp,None) is None and min(margins)==Q(r['short_margin'])>0
 assert penalties[0][1]+8*B-(A-C*lo+B*lo)==Q(r['long_back_margin'])>0
 assert penalties[1][1]+8*C-A==Q(r['long_main_margin'])>0
 # Canonical connected energies are integers: erasing above21 charges at least22 per tail mass.
 assert min((22-e)*B-(A-C*e) for e in (lo,hi))==Q(r['tail_mass_coefficient'])>0
 assert C>B>0 and hi<Q(3,2)
 for w in r['witnesses']:
  ww=general_witness(3,2,3,Q(w['energy']));assert w==ww and Q(w['return_value'])==A-C*Q(w['energy'])
 assert r['endpoint17']==witness(2,3,hi) and Q(r['endpoint17']['return_value'])==A-C*hi
 assert global_count==r['component_duals'] and len(d['components']['short'])==r['short_duals']
 return dict(connected_duals=count,component_duals=global_count,short_duals=len(d['components']['short']),feasible_short=len(margins),contact_cells=contacts)

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce();r['certified_interval']=json.loads(OUT.read_text())['certified_interval'];certs=check_global(r['certified_interval'])
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2031',r['finite_physical_controls'],'finite family controls;11 exact infinite-family optimizations;two phase-crossing competitors;11 unbounded head/rise/tail optimizations;7 provenance hashes;',certs,flush=True)
