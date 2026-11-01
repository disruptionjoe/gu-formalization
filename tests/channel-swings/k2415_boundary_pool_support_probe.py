"""Exact support-aware metric pool bounds; original zero sets precede cancellation."""
from pathlib import Path
from itertools import combinations,permutations,product
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];Q=s.Rational;x=s.Symbol('x')
p=R/'tests/channel-swings/k2412_exact_metric_pool_odds_probe.py';src=p.read_text();ns={'__file__':str(p),'__name__':'functions'}
exec(compile(src[:src.index('checks=')],str(p),'exec'),ns)
counts=ns['counts'];value_interval=ns['value_interval'];rational=ns['rational']
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def envelopes(bounds,d,q):
 b=[tuple(map(rational,z)) for z in bounds];d=[list(map(rational,z)) for z in d];n=len(b)
 if n<2 or any(len(z)!=2 or not 0<=z[0]<=z[1]<=1 for z in b) or len(d)!=n or any(len(z)!=n for z in d):raise ValueError('boundary interval shape')
 if any(d[i][j]<0 or d[i][j]!=d[j][i] or (i==j and d[i][j]) for i in range(n) for j in range(n)):raise ValueError('pseudometric')
 if any(d[i][j]>d[i][k]+d[k][j] for i in range(n) for j in range(n) for k in range(n)):raise ValueError('triangle')
 bb=[(q,q)]+b[1:] if q is not None else b
 if q is not None and not b[0][0]<=q<=b[0][1]:return None
 if any(bb[i][0]>bb[j][1]+d[i][j] for i in range(n) for j in range(n)):return None
 low=max(bb[i][0]-d[i][0] for i in range(n));high=min(bb[i][1]+d[i][0] for i in range(n))
 if q is None:return b,d,low,high
 a=[max(bb[j][0]-d[i][j] for j in range(n)) for i in range(1,n)];z=[min(bb[j][1]+d[i][j] for j in range(n)) for i in range(1,n)]
 return a,z

def group_probability(ps,q,t):
 c=counts(ps);A=q*c[t-1];B=(1-q)*c[t];Z=s.expand(A+B)
 return None if Z==0 else s.cancel(A/Z)

def supported(a,b,q,t):
 h=sum(z==1 for z in a);k=sum(bool(z>0) for z in b)
 return h<=t<=k if q==0 else (h<=t-1<=k if q==1 else h<=t and k>=t-1)

def face_witness(bounds,d,q,t,value):
 """Complete finite support-face test for an attained extreme zero or one."""
 m=len(bounds)-1
 if not 0<q<1:return None
 for subset in combinations(range(m),t-1 if value==1 else t):
  chosen=set(subset);bb=[(q,q)]+[tuple(v) for v in bounds[1:]]
  for i in range(m):
   if value==1 and i not in chosen:bb[i+1]=(0,0)
   if value==0 and i in chosen:bb[i+1]=(1,1)
   # Intersect with the original bounds, never replace a prohibition.
   bb[i+1]=(max(bb[i+1][0],bounds[i+1][0]),min(bb[i+1][1],bounds[i+1][1]))
  if any(l>u for l,u in bb):continue
  ab=envelopes(bb,d,q)
  if ab is None:continue
  witness=ab[1] if value==1 else ab[0]
  if group_probability(witness,q,t)==value:return witness
 return None

def slice_bounds(bounds,d,q,t):
 ab=envelopes(bounds,d,q)
 if ab is None:return {'status':'infeasible'}
 a,b=ab
 if not supported(a,b,q,t):return {'status':'zero_event_support'}
 mid=[(u+v)/2 for u,v in zip(a,b)]
 ans={'status':'supported','witness':list(map(str,mid))}
 if q in (0,1):
  for name in ['lower','upper']:ans[name]={'value':str(q),'attained':True,'witness':list(map(str,mid))}
  return ans
 for name,ps,fallback in [('lower',b,Q(0)),('upper',a,Q(1))]:
  value=group_probability(ps,q,t);witness=ps
  if value is None:
   value=fallback;witness=face_witness(bounds,d,q,t,value)
  ans[name]={'value':str(value),'attained':witness is not None,'witness':None if witness is None else list(map(str,witness))}
 return ans

def solve(bounds,d,t,tol=Q(1,10**8)):
 m=len(bounds)-1;tol=rational(tol)
 if isinstance(t,bool) or not isinstance(t,int) or not 1<=t<=m or tol<=0:raise ValueError('count/tolerance')
 data=envelopes(bounds,d,None)
 if data is None:return {'status':'infeasible'}
 bounds,d,lo,hi=data
 ca=[max(bounds[j][0]-d[i][j] for j in range(1,m+1)) for i in range(1,m+1)]
 cb=[min(bounds[j][1]+d[i][j] for j in range(1,m+1)) for i in range(1,m+1)]
 cuts=sorted({lo,hi}|{z for i in range(m) for z in [ca[i]+d[i+1][0],cb[i]-d[i+1][0]] if lo<z<hi})
 candidates={'lower':[],'upper':[]};cells=[];points=[]
 for z in cuts:
  part=slice_bounds(bounds,d,z,t);points.append({'q':str(z),**part})
  if part['status']=='supported':
   for name in candidates:
    v=part[name]['value'];candidates[name].append({'kind':'supported_breakpoint','q':str(z),'value_interval':[v,v],'attained':part[name]['attained'],'witness':part[name]['witness']})
 for l,h in zip(cuts,cuts[1:]):
  mid=(l+h)/2;a,b=envelopes(bounds,d,mid)
  if not supported(a,b,mid,t):cells.append({'interval':list(map(str,(l,h))),'status':'zero_event_support'});continue
  for name in candidates:
   ps=[(min(cb[i],mid+d[i+1][0]) if name=='lower' else max(ca[i],mid-d[i+1][0])) for i in range(m)]
   symbolic=[(cb[i] if cb[i]<mid+d[i+1][0] else x+d[i+1][0]) if name=='lower' else (ca[i] if ca[i]>mid-d[i+1][0] else x-d[i+1][0]) for i in range(m)]
   c=counts(symbolic);original=s.expand(x*c[t-1]+(1-x)*c[t]);is_null=original==0
   f=(Q(0) if name=='lower' else Q(1)) if is_null else s.cancel(x*c[t-1]/original)
   if not is_null:assert original.subs(x,mid)>0
   cell={'branch':name,'interval':list(map(str,(l,h))),'status':'supported','original_support_polynomial':str(original),'function':str(f),'envelope_null':is_null};cells.append(cell)
   for endpoint,side in [(l,'+'),(h,'-')]:
    val=s.limit(f,x,endpoint,dir=side);assert 0<=val<=1
    candidates[name].append({'kind':'one_sided_limit','q':str(endpoint),'side':side,'value_interval':[str(val)]*2,'attained':'not_asserted'})
   n,den=s.fraction(f);der=s.Poly(s.diff(n,x)*den-n*s.diff(den,x),x)
   if der.is_zero:
    z=slice_bounds(bounds,d,mid,t)[name]
    candidates[name].append({'kind':'constant_cell','q':str(mid),'value_interval':[z['value']]*2,'attained':z['attained'],'witness':z['witness']});continue
   sq=der.sqf_part()
   for (a0,b0),_ in sq.intervals(inf=l,sup=h,eps=tol):
    if a0==b0 and a0 in (l,h):continue
    while True:
     if l<a0<=b0<h:
      vi=value_interval(f,(a0,b0))
      if vi is not None and vi[1]-vi[0]<=tol:break
     assert a0!=b0
     a0,b0=sq.refine_root(a0,b0,eps=(b0-a0)/2)
    candidates[name].append({'kind':'stationary','root_polynomial':str(sq.as_expr()),'root_interval':list(map(str,(a0,b0))),'function':str(f),'value_interval':list(map(str,vi)),'attained':True,'probabilities':list(map(str,symbolic))})
 if not candidates['lower']:return {'status':'zero_event_support','points':points,'cells':cells}
 out={'status':'supported','points':points,'cells':cells,'branches':{}}
 for name,cc in candidates.items():
  ll=[Q(z['value_interval'][0]) for z in cc];uu=[Q(z['value_interval'][1]) for z in cc]
  ext=(min(ll),min(uu)) if name=='lower' else (max(ll),max(uu))
  out['branches'][name]={'extremum_enclosure':list(map(str,ext)),'candidates':cc}
 return out

half=Q(1,2);d=[[0,half,half],[half,0,0],[half,0,0]]
up=solve([(half,half),(0,half),(0,half)],d,2)
down=solve([(half,half),(half,1),(half,1)],d,1)
ck('unattained_supremum',up['points'][0]['upper']=={'value':'1','attained':False,'witness':None})
ck('attained_lower_two_thirds',up['points'][0]['lower']['value']=='2/3' and up['points'][0]['lower']['attained'])
ck('unattained_infimum',down['points'][0]['lower']=={'value':'0','attained':False,'witness':None})
ck('attained_upper_one_third',down['points'][0]['upper']['value']=='1/3' and down['points'][0]['upper']['attained'])
ck('approach_supremum_formula',group_probability([x,x],half,2)==2*(x-1)/(x-2))
ck('approach_infimum_formula',group_probability([x,x],half,1)==(1-x)/(x+1))
joined=solve([(0,half),(0,half)],[[0,0],[0,0]],1)
ck('null_endpoint_not_value',joined['points'][0]['status']=='zero_event_support')
ck('all_supported_values_half',all(joined['branches'][k]['extremum_enclosure']==['1/2']*2 for k in ['lower','upper']))
ctrl('false_endpoint_fill_rejected',Q(0)!=Q(joined['branches']['lower']['extremum_enclosure'][0]))
c=s.Symbol('c',positive=True)
ck('path_dependent_null_limit',s.simplify(s.limit(group_probability([x],c*x,1),x,0,dir='+')-c/(c+1))==0)
ctrl('null_event_is_not_infinite_evidence',solve([(0,0),(0,0)],[[0,1],[1,0]],1)['status']=='zero_event_support')
ck('unsupported_extremal_envelope_can_be_attained',slice_bounds([(half,half),(0,1),(0,1)],[[0,1,1],[1,0,1],[1,1,0]],half,2)['upper']['attained'])
for q0 in [Q(0),Q(1)]:
 edge=solve([(q0,q0),(0,1)],[[0,1],[1,0]],1)
 ck('supported_science_endpoint_'+str(q0),all(edge['branches'][z]['extremum_enclosure']==[str(q0)]*2 for z in ['lower','upper']))
for tt,bounds0,expected in [(1,[(0,half)]*3,['0','1/2']),(2,[(half,1)]*3,['1/2','1'])]:
 edge=solve(bounds0,[[0,0,1],[0,0,1],[1,1,0]],tt)
 ck('nonconstant_endpoint_support_regression_'+str(tt),edge['branches']['lower']['extremum_enclosure']==[expected[0]]*2 and edge['branches']['upper']['extremum_enclosure']==[expected[1]]*2)
# Independent direct Bernoulli enumeration checks support and slice bounds at boundary grids.
fixtures=0
for ps in product([Q(0),Q(1,3),Q(1)],repeat=3):
 for q in [Q(0),Q(1,2),Q(1)]:
  for t in range(1,4):
   pp=[q]+list(ps);Z=Q(0);A=Q(0)
   for labels in product([0,1],repeat=4):
    if sum(labels)!=t:continue
    prob=s.prod(p if z else 1-p for p,z in zip(pp,labels));Z+=prob;A+=labels[0]*prob
   h=sum(z==1 for z in ps);k=sum(bool(z>0) for z in ps)
   assert bool(Z)==supported(ps,ps,q,t)
   assert group_probability(ps,q,t)==(A/Z if Z else None);fixtures+=1
ck('243_original_count_support_cases',fixtures==243)
# Original role-permutation consumer, labels 1,1,0 and score one only on zero.
pp=[half,Q(1,4),Q(1,4)];labels=[1,1,0];total=Q(0);score=Q(0)
for perm in permutations(range(3)):
 prob=s.prod(pp[perm[j]] if labels[j] else 1-pp[perm[j]] for j in range(3));total+=prob;score+=prob*int(labels[perm.index(0)]==0)
C=Q(1,3);ck('original_consumer_safe_unattained_endpoint',score/(total*C)==Q(3,7))
score=Q(0)
for perm in permutations(range(3)):
 prob=s.prod(pp[perm[j]] if labels[j] else 1-pp[perm[j]] for j in range(3));score+=prob*int(perm.index(0)==0)
ck('consumer_uses_unattained_upper_endpoint',score/(total*half)==Q(6,7))
# Complete interior fixture agrees with K2412 after odds-to-group transform.
metric=[[Q(abs(i-j),16) for j in range(5)] for i in range(5)];bb=[(Q(3,8),Q(5,8))]+[(Q(1,4),Q(3,4))]*4
interior=solve(bb,metric,2);old=ns['solve'](bb,metric,2)
for name in ['lower','upper']:
 l,u=map(Q,old['branches'][name]['extremum_enclosure']);target=(lambda z:2*z/(3+2*z))((l+u)/2);a,b=map(Q,interior['branches'][name]['extremum_enclosure']);ck('interior_original_odds_agreement_'+name,abs((a+b)/2-target)<Q(1,10**7))
try:solve([(-1,half),(0,half)],[[0,1],[1,0]],1)
except ValueError:ctrl('invalid_probabilities_rejected',True)
else:raise AssertionError('invalid bounds accepted')
report={'result_id':'K2415','checks':checks,'controls':controls,'upper_fixture':up,'lower_fixture':down,'coupled_null_fixture':joined,'interior_fixture':interior,'scope':'Exact support-aware infimum/supremum certificates; candidate-wise attainment only. Conditional independent labels and valid joint metric calibration required.'}
deps=['tests/channel-swings/k2412_exact_metric_pool_odds_probe.py','explorations/conditional-build/k2409-coupled-drift-calibration-2026-10-31.md']
report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps};out=R/'lab/process/k2415-boundary-pool-support.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'}))
