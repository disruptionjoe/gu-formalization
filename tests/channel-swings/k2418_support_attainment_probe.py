"""Support-cardinality DP and exact global attainment for metric pool bounds."""
from pathlib import Path
import sympy as s
from itertools import product
from functools import cmp_to_key
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];p=R/'tests/channel-swings/k2415_boundary_pool_support_probe.py';src=p.read_text();ns={'__file__':str(p),'__name__':'functions'}
exec(compile(src[:src.index('half=Q(1,2);')],str(p),'exec'),ns)
Q=ns['Q'];x=ns['x'];envelopes=ns['envelopes'];group_probability=ns['group_probability'];old_face=ns['face_witness'];value_interval=ns['value_interval']
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def positive_support_witness(bounds,d,q,target):
 ab=envelopes(bounds,d,q)
 if ab is None:return None
 a,b=ab;m=len(a);classes=[];remaining=set(range(m))
 while remaining:
  i=min(remaining);C=sorted(j for j in remaining if d[i+1][j+1]==0);remaining.difference_update(C);classes.append(C)
 forced=sum(bool(z>0) for z in a);optional=[C for C in classes if a[C[0]]==0 and b[C[0]]>0];need=target-forced
 if need<0:return None
 reach={0:[]}
 for C in optional:
  for k,used in list(reach.items()):
   nxt=k+len(C)
   if nxt<=need and nxt not in reach:reach[nxt]=used+[C]
 if need not in reach:return None
 selected=[i for C in reach[need] for i in C];out=list(a)
 if selected:
  eps=min([Q(1)]+[Q(v) for row in d for v in row if v>0]+[Q(bounds[i+1][1]) for i in selected])/2
  for i in selected:out[i]=eps
 return out

def face_dp(bounds,d,q,t,value):
 if not 0<q<1:return None
 if value==1:return positive_support_witness(bounds,d,q,t-1)
 if value!=0:raise ValueError('face value')
 cb=[(1-u,1-l) for l,u in bounds];w=positive_support_witness(cb,d,1-q,len(bounds)-1-t)
 return None if w is None else [1-v for v in w]

ns['face_witness']=face_dp
# K2415 calls through its global namespace, now using the proved DP.
solve=ns['solve']
def exact_value(c):
 if c['kind']!='stationary':return Q(c['value_interval'][0])
 l,h=map(Q,c['root_interval']);poly=s.Poly(s.sympify(c['root_polynomial'],locals={'x':x}),x)
 roots=[r for r in poly.real_roots(radicals=False) if bool(r>=l) and bool(r<=h)]
 if len(roots)!=1:raise ValueError('root isolator does not select exactly one root')
 return s.cancel(s.sympify(c['function'],locals={'x':x}).subs(x,roots[0]))
def candidate_cmp(c,d):
 ec,ed=exact_value(c),exact_value(d)
 if all(v==0 for v in s.polys.numberfields.to_number_field(ec-ed).coeffs()):return 0
 intervals=[]
 for a in [c,d]:
  if a['kind']=='stationary':intervals.append(tuple(map(Q,a['root_interval'])))
  else:intervals.append(None)
 while True:
  vals=[]
  for j,a in enumerate([c,d]):
   if intervals[j] is None:vals.append((exact_value(a),)*2)
   else:
    f=s.sympify(a['function'],locals={'x':x});v=value_interval(f,intervals[j]);vals.append(v)
  if all(v is not None for v in vals):
   if vals[0][1]<vals[1][0]:return -1
   if vals[1][1]<vals[0][0]:return 1
  for j,a in enumerate([c,d]):
   if intervals[j] is not None:
    l,h=intervals[j]
    if l!=h:intervals[j]=s.Poly(s.sympify(a['root_polynomial'],locals={'x':x}),x).refine_root(l,h,eps=(h-l)/2)

def solve_attainment(bounds,d,t):
 report=solve(bounds,d,t)
 if report['status']!='supported':return report
 for name,branch in report['branches'].items():
  cc=branch['candidates'];ordered=sorted(range(len(cc)),key=cmp_to_key(lambda a,b:candidate_cmp(cc[a],cc[b])))
  best=ordered[0 if name=='lower' else -1];ties=[i for i in ordered if candidate_cmp(cc[i],cc[best])==0]
  attained=[i for i in ties if cc[i].get('attained') is True]
  branch['exact_extremum']=str(exact_value(cc[best]));branch['extremizing_candidates']=ties;branch['globally_attained']=bool(attained);branch['attaining_candidates']=attained
 return report

def valid_witness(bounds,d,q,t,p,value):
 if p is None:return False
 pp=[q]+p
 return all(l<=v<=h for v,(l,h) in zip(pp,bounds)) and all(abs(pp[i]-pp[j])<=d[i][j] for i in range(len(pp)) for j in range(len(pp))) and group_probability(p,q,t)==value
half=Q(1,2)
# Gapped zero-distance classes of size2 and3.
d=[[Q(0) if i==j or (i and j and ((i<=2)==(j<=2))) else half for j in range(6)] for i in range(6)];bounds=[(half,half)]+[(Q(0),half)]*5
witnesses={}
for t in range(1,6):
 w=face_dp(bounds,d,half,t,1);witnesses[str(t)]=None if w is None else list(map(str,w))
 ck('gapped_attainment_'+str(t),(w is not None)==(t-1 in {0,2,3,5}))
 if w is not None:ck('original_supported_witness_'+str(t),valid_witness(bounds,d,half,t,w,1))
ctrl('interval_of_counts_would_be_false',face_dp(bounds,d,half,2,1) is None)
# Exhaustive independent comparison to old face enumeration on small rational metric fixtures.
fixtures=0
for dd in [Q(0),Q(1,3),Q(1)]:
 for boxes in product([(Q(0),half),(half,Q(1)),(Q(0),Q(1))],repeat=3):
  bb=[(half,half)]+list(boxes);metric=[[Q(0) if i==j else (Q(1) if i==0 or j==0 else dd) for j in range(4)] for i in range(4)]
  for t in range(1,4):
   for val in [0,1]:
    a=face_dp(bb,metric,half,t,val);b=old_face(bb,metric,half,t,val)
    assert (a is None)==(b is None)
    if a is not None:assert valid_witness(bb,metric,half,t,a,val)
    fixtures+=1
ck('486_exhaustive_old_face_comparisons',fixtures==486)
# Boundary science endpoints and a genuinely interior-valued unattained endpoint.
metric=[[0,0,half],[0,0,half],[half,half,0]]
f=solve_attainment([(0,half),(0,half),(half,half)],metric,2)
ck('interior_valued_infimum_unattained',f['branches']['lower']['exact_extremum']=='1/2' and not f['branches']['lower']['globally_attained'])
ck('upper_two_thirds_attained',f['branches']['upper']['exact_extremum']=='2/3' and f['branches']['upper']['globally_attained'])
g=solve_attainment([(half,1),(half,1),(half,half)],metric,1)
ck('complement_interior_supremum_unattained',g['branches']['upper']['exact_extremum']=='1/2' and not g['branches']['upper']['globally_attained'])
ctrl('interior_value_does_not_imply_attainment',not f['branches']['lower']['globally_attained'])
for q in [0,1]:
 z=solve_attainment([(q,q),(0,1)],[[0,1],[1,0]],1)
 ck('supported_science_endpoint_'+str(q),all(v['exact_extremum']==str(q) and v['globally_attained'] for v in z['branches'].values()))
# Null conditioning and infeasible families must never emit a value.
for q0 in [0,1]:
 z=solve_attainment([(q0,q0)]*3,[[0,1,1],[1,0,1],[1,1,0]],1)
 ck('null_family_no_value_'+str(q0),z['status']=='zero_event_support' and 'branches' not in z)
z=solve_attainment([(0,0),(1,1)],[[0,0],[0,0]],1)
ck('infeasible_family_no_value',z['status']=='infeasible' and 'branches' not in z)
# Algebraic equal values require equality testing before interval refinement.
c={'kind':'stationary','root_polynomial':'x**3-x-1','root_interval':['1','2'],'function':'x/(1+x)'};e={**c,'function':'(x**3-1)/x**3'}
ck('different_algebraic_expressions_tie',candidate_cmp(c,e)==0)
ck('nearby_unequal_algebraic_values_ordered',candidate_cmp(c,{**e,'function':'(x**3-1)/x**3+1/1000000'})==-1)
# Thirty equal coordinates give two reachable support counts, not 155117520 faces.
metric=[[Q(0) if i==j or (i>0 and j>0) else half for j in range(31)] for i in range(31)]
ck('thirty_tied_coordinates_no_middle_support',face_dp([(half,half)]+[(0,half)]*30,metric,half,16,1) is None)
# Nontrivial original interior root candidates; exact global comparison.
metric=[[Q(abs(i-j),16) for j in range(5)] for i in range(5)];bb=[(Q(3,8),Q(5,8))]+[(Q(1,4),Q(3,4))]*4
interior=solve_attainment(bb,metric,2);ck('interior_extrema_attained',all(v['globally_attained'] for v in interior['branches'].values()))
report={'result_id':'K2418','checks':checks,'controls':controls,'face_comparisons':fixtures,'gapped_witnesses':witnesses,'interior_unattained_fixture':f,'complement_fixture':g,'interior_fixture':interior,'scope':'Exact conditional support-cardinality and global attainment; valid joint calibration and original positive event support remain required.'}
report['dependencies']={str(z.relative_to(R)):hashlib.sha256(z.read_bytes()).hexdigest() for z in [p,R/'tests/channel-swings/k2412_exact_metric_pool_odds_probe.py']};out=R/'lab/process/k2418-support-attainment.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:
 saved=json.loads(out.read_text());assert saved==report,[k for k in report if saved.get(k)!=report[k]]
print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'}))
