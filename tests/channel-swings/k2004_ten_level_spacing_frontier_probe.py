"""Separate shell census, fixed-budget solver and exact spacing consumers."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,copy
from k1992_wide_spacing_eight_level_rigidity_probe import ok,ret,minimum
ROOT=Path(__file__).resolve().parents[2]

def census():
 found={};small=[];count=0
 for n in range(3,11):
  for word in product([1,2,3],repeat=n-1):
   A=[0]
   for gap in word:A.append(A[-1]+gap)
   count+=1
   for m in range(1,(n-1)//2+1):
    for S in combinations(A[1:-1],m):
     if ok(A,S):
      found[S]=min(n,found.get(S,99))
      if n<=7 and m>=2 and any(b-a<=3 for a,b in zip(S,S[1:])):small.append((tuple(A),S))
 return found,small,count

def curve_value(curve,E):
 return next(F(p['slope'])*E+F(p['intercept']) for p in curve if F(p['lo'])<=E and(p['hi'] is None or E<=F(p['hi'])))

def independent_templates(delta):
 types=[([1,3],list(range(5))),([2,3],list(range(6))),([1,4],list(range(6))),([1,3,5],list(range(7)))];out=[]
 for S,A in types:
  for side in [0,1]:
   x,y=(delta,F(0)) if side else(F(0),delta)
   out.append((sorted([x+a for a in A]+[y,y+1,y+2]),sorted([x+s for s in S]+[y+1])))
 out.append((sorted(list(map(F,range(5)))+[delta+a for a in range(5)]),[F(1),1+delta,F(3),3+delta]))
 return out

def half_jump_control(d):
 # The open energy interval is reconstructed from every rational curve cell.
 curves=[d['connected_curve'],d['half_spacing_curve']]
 cuts=sorted({F(p['lo']) for c in curves for p in c}|{F(p['hi']) for c in curves for p in c if p['hi'] is not None})
 positive=[];n=0
 for lo,hi in zip(cuts,cuts[1:]+[None]):
  e=lo+1 if hi is None else(lo+hi)/2
  a=curve_value(curves[0],e)-curve_value(curves[1],e)
  assert a>=0,'half-spacing cannot beat spacing monotonicity'
  for x in [lo]+([] if hi is None else[hi]):
   gap=curve_value(curves[0],x)-curve_value(curves[1],x)
   assert (gap>0)==(F(1029,820)<x<F(28,15)) and gap>=0,'exact jump endpoints'
  if a>0:positive.append((lo,hi))
  n+=1
 assert positive[0][0]==F(1029,820) and positive[-1][1]==F(28,15)
 assert all(a[1]==b[0] for a,b in zip(positive,positive[1:])), 'connected positive jump interval'
 assert curve_value(curves[0],F(3,2))-curve_value(curves[1],F(3,2))==F(23,1100)
 assert curve_value(curves[0],F(2))==curve_value(curves[1],F(2))==F(7,20)
 assert F(1,2)-curve_value(curves[0],F(2))==F(3,20)
 return n+4

def pure_component_merge_control():
 # An actual eleven-level5+3+3 protocol reduces to5+3 without changing return.
 A=sorted(list(map(F,range(5)))+[F(1,5)+i for i in range(3)]+[F(2,5)+i for i in range(3)])
 S=[F(1),F(3),F(6,5),F(7,5)];p=[F(1,10),F(3,10),F(1,5),F(2,5)]
 B=sorted(list(map(F,range(5)))+[F(1,5)+i for i in range(3)])
 T=S[:3];q=p[:2]+[p[2]+p[3]]
 assert len(A)==11 and len(B)==8 and ok(A,S) and ok(B,T)
 assert min(b-a for a,b in zip(B,B[1:]))>=F(1,5)
 assert sum(x*y for x,y in zip(T,q))<sum(x*y for x,y in zip(S,p))
 for t in [F(1,3),F(1,2),F(3,4)]:assert ret(t,S,p)==ret(t,T,q)
 return 6

def unsafe_merge_control():
 # Adding isolated mass to an old edge endpoint is NOT a valid transfer.
 old=ret(F(1,2),[F(1),F(3),F(10)],[F(1,45),F(1,5),F(7,9)])
 merged=ret(F(1,2),[F(1),F(3)],[F(4,5),F(1,5)])
 assert old==F(22,45) and merged==F(1,2) and old<merged
 return 1

def check(d,cache=None):
 if cache is None:
  found,small,count=census();print('probe census',count,len(found),len(small),flush=True)
  # A positive budget only permits supports containing a site <=E; no-edge
  # supports have return1/2 and are independently included by the pure case.
  con={};opt={}
  for E in [F(3,2),F(2)]:
   vals=[F(1,2)]
   for ix in d['connected_core_indices']:
    b=d['pareto_blocks'][ix];S=list(map(F,b['S']))
    if min(S)>E or not any(y-x in(1,2,3) for x,y in combinations(S,2)):continue
    v=minimum(F(1,2),S,E)
    if v is not None:vals.append(v)
   con[E]=min(vals)
   for delta in [F(1,20),F(1,4),F(2,5),F(9,20),F(1,2)]:
    vals=[con[E]]
    for A,S in independent_templates(delta):
     v=minimum(F(1,2),S,E)
     if v is not None:vals.append(v)
    opt[(E,delta)]=min(vals)
   print('probe independent budgets',E,con[E],flush=True)
  cache=found,small,count,con,opt
 found,small,count,con,opt=cache;n=unsafe_merge_control()+half_jump_control(d)+pure_component_merge_control()
 assert count==d['connected_shape_count']==29520,'complete shape census'
 assert len(found)==d['raw_support_count']==1216,'complete support count'
 assert set(small)=={(tuple(r['spectrum']),tuple(r['support'])) for r in d['small_component_witnesses']},'complete improving census'
 assert len(small)==107,'107 small improving shapes'
 for S,size in found.items():
  assert any(len(b['A'])<=size and b['S'][0]<=S[0] and tuple(x-b['S'][0] for x in b['S'])==tuple(x-S[0] for x in S) for b in d['pareto_blocks']),'Pareto coverage';n+=1
 for b in d['pareto_blocks']:assert ok(b['A'],b['S']),'connected physical shells';n+=1
 core=set(d['connected_core_indices']);mapped=set()
 assert len(core)==18 and len(d['connected_dominance'])==294,'18 connected core templates'
 for row in d['connected_dominance']:
  i,j=row['source_index'],row['target_index'];assert j in core and i not in core and i not in mapped,'direct connected reduction map'
  mapped.add(i);source,target=d['pareto_blocks'][i],d['pareto_blocks'][j];S,T=source['S'],target['S']
  assert len(T)==len(S) and len(target['A'])<=len(source['A']) and all(t<=s for s,t in zip(S,T)),'connected energy/dimension domination'
  assert all(T[v]-T[u]==S[v]-S[u] for u,v in combinations(range(len(S)),2) if S[v]-S[u]<=3),'connected preserved edges';n+=1
 assert mapped|core==set(range(len(d['pareto_blocks']))),'complete connected reduction'
 for r in d['small_component_witnesses']:
  S,T=r['support'],r['target_support'];A,B=r['spectrum'],r['target_spectrum']
  assert len(A)>=len(B) and len(S)==len(T) and all(t<=s for s,t in zip(S,T)),'component energies'
  assert ok(B,T),'component shell'
  assert all(T[j]-T[i]==S[j]-S[i] for i,j in combinations(range(len(S)),2) if S[j]-S[i]<=3),'preserve every old edge'
  for t in [F(1,3),F(1,2),F(3,4)]:
   # Nonuniform inputs separately test actual incoming-flow domination.
   pp=[F(i+1,sum(range(1,len(S)+1))) for i in range(len(S))]
   assert ret(t,T,pp)<=ret(t,S,pp),'all-edge return controls';n+=1
 assert len(d['shifted_templates'])==9,'nine shifted templates'
 for row,(A,S) in zip(d['shifted_templates'],independent_templates(F(1,20))):
  assert list(map(F,row['spectrum']))==A and sorted(map(F,row['support']))==sorted(S),'template identity'
  assert len(A)<=10 and min(b-a for a,b in zip(A,A[1:]))>=F(1,20) and ok(A,S),'physical spacing/shells';n+=1
 # Rebuild every wide placement before testing its exact edge-preserving map.
 expected=set()
 pure=[(0,a,b) for b in range(2,7) for a in range(1,b) if max(a,b-a)<=3 and ok([0,a,b],[a])]
 assert len(pure)==6
 for A,S in small:
  for B in pure:
   for side in ['A','B']:expected.add((A,S,B,(B[1],),side))
 expected.add((tuple(range(5)),(1,3),tuple(range(5)),(1,3),'B'))
 actual={(tuple(r['A']),tuple(r['S']),tuple(r['B']),tuple(r['U']),r['shifted']) for r in d['wide_dominance_witnesses']}
 assert expected==actual and len(actual)==1285,'complete wide placement census'
 for row in d['wide_dominance_witnesses']:
  A,S,B,U=row['A'],row['S'],row['B'],row['U'];side=row['shifted']=='A';delta=F(3,4)
  C,D=(B,A) if side else(A,B)
  candidates={F(0)}|{F(c-d)+delta for c in C for d in D}
  least=min(x for x in candidates if x>=0 and all(abs(c-d-x)>=delta for c in C for d in D))
  assert least==row['shift_integer']+delta,'independent least wide offset'
  target=d['pareto_blocks'][row['target_index']];V=target['S'];mp=row['support_map']
  assert len(mp)==len(S)+len(U) and len(target['A'])<=10 and len(A)+len(B)<=10,'wide complete population/dimension map'
  assert set(mp)==set(range(len(V))),'wide surjective population map'
  aa=row['shift_integer']+F(1,2) if side else F(0);bb=F(0) if side else row['shift_integer']+F(1,2)
  source=[aa+x for x in S]+[bb+x for x in U]
  assert all(V[mp[i]]<=source[i] for i in range(len(source))),'wide energy domination'
  edges=[(i,j,S[j]-S[i]) for i,j in combinations(range(len(S)),2) if S[j]-S[i]<=3]+[(len(S)+i,len(S)+j,U[j]-U[i]) for i,j in combinations(range(len(U)),2) if U[j]-U[i]<=3]
  assert all(V[mp[j]]-V[mp[i]]==g for i,j,g in edges),'wide preserved old edges'
  incident={i for e in edges for i in e[:2]}
  assert sorted(row['isolated_source_indices'])==[i for i in range(len(source)) if i not in incident],'actual isolated source vertices'
  for j in range(len(V)):
   pre=[i for i,v in enumerate(mp) if v==j]
   assert len(pre)==1 or all(i not in incident for i in pre),'merge isolated mass only, never an edge endpoint'
  pp=[F(i+1,len(source)*(len(source)+1)//2) for i in range(len(source))];qq=[F(0)]*len(V)
  for i,j in enumerate(mp):qq[j]+=pp[i]
  assert sum(qq)==sum(pp)==1,'mass aggregation conservation'
  aa=row['shift_integer']+F(3,4) if side else F(0);bb=F(0) if side else row['shift_integer']+F(3,4)
  old=[aa+x for x in S]+[bb+x for x in U]
  for t in [F(1,3),F(1,2),F(3,4)]:assert ret(t,V,qq)<=ret(t,old,pp),'aggregated return domination';n+=1
  for delta in [F(51,100),F(1)]:
   aa=row['shift_integer']+delta if side else F(0);bb=F(0) if side else row['shift_integer']+delta
   spec=sorted([aa+x for x in A]+[bb+x for x in B]);support=[aa+x for x in S]+[bb+x for x in U]
   assert len(spec)<=10 and min(b-a for a,b in zip(spec,spec[1:]))>=delta and ok(spec,support),'actual wide shell and spacing';n+=1
  n+=3
 for E,v in con.items():assert curve_value(d['connected_curve'],E)==v,'independent connected optimum';n+=1
 for E in con:
  assert curve_value(d['small_spacing_curve'],E)==opt[(E,F(1,20))],'independent budget curve'
  assert curve_value(d['half_spacing_curve'],E)==opt[(E,F(1,2))],'independent half-spacing curve';n+=2
 import sympy as s
 z=s.symbols('z')
 assert len(d['thresholds'])==2,'two distinct threshold consumers'
 for row in d['thresholds']:
  E=F(row['energy']);eta=s.sympify(row['exact_threshold']);assert 0<eta<=s.Rational(1,2),'threshold range'
  for delta in [F(1,20),F(1,4),F(2,5),F(9,20),F(1,2)]:
   x=s.Rational(delta)
   piece=next(p for p in row['spacing_curve'] if s.sympify(p['lo'])<=x<=s.sympify(p['hi']))
   assert s.simplify(s.sympify(piece['formula']).subs(z,x)-s.Rational(opt[(E,delta)]))==0,'independent spacing optimum';n+=1
  # Exact cutoff is the first branch departure; boundaries are attested too.
  forms=[(s.sympify(p['lo']),s.sympify(p['hi']),s.sympify(p['formula'])) for p in row['spacing_curve']]
  target=s.sympify(row['formula']);different=[lo for lo,hi,f in forms if s.cancel(f-target)!=0]
  assert eta==(min(different) if different else s.Rational(1,2)),'exact threshold'
  boundary=next(p for p in row['boundary_values'] if s.sympify(p['spacing'])==eta)
  assert (s.sympify(boundary['target_gap'])==0)==row['threshold_included'],'threshold boundary'
 return n,cache
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2004-ten-level-spacing-frontier.json').read_text());n,c=check(d);faults=[]
 for name in ['component','coverage','spacing','curve','threshold','wide']:
  b=copy.deepcopy(d)
  if name=='component':b['small_component_witnesses'].pop()
  if name=='coverage':b['pareto_blocks']=[p for p in b['pareto_blocks'] if len(p['S'])<4]
  if name=='spacing':b['shifted_templates'][0]['spectrum'][1]='0'
  if name=='curve':
   p=next(p for p in b['small_spacing_curve'] if F(p['lo'])<=F(2) and(p['hi'] is None or F(2)<=F(p['hi'])));p['intercept']=str(F(p['intercept'])+1)
  if name=='threshold':b['thresholds'][1]['exact_threshold']='1/100'
  if name=='wide':b['wide_dominance_witnesses'][0]['support_map'][0]=b['wide_dominance_witnesses'][0]['support_map'][1]
  try:check(b,c)
  except AssertionError as e:faults.append((name,str(e)))
  else:raise AssertionError('undetected mathematical fault '+name)
 print('PASS K2004 separate',n,'exact census/coverage/physical/budget obligations;',len(faults),'mathematical faults',faults)
