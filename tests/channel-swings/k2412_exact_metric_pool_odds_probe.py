"""Exact finite metric-box odds: complete root candidates and outward enclosures."""
from pathlib import Path
from itertools import permutations
import json,hashlib,sys,math
import sympy as s
R=Path(__file__).resolve().parents[2];Q=s.Rational;x=s.Symbol('x')
def rational(v):
 if isinstance(v,(bool,float)) or not isinstance(v,(int,str,s.Integer,s.Rational)):raise ValueError('exact rational input required')
 z=Q(v)
 return z

def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
 v=[u*w for u in a for w in b];return min(v),max(v)
def polynomial_interval(p,iv):
 out=(Q(0),Q(0))
 for c in s.Poly(p,x).all_coeffs():out=add(mul(out,iv),(c,c))
 return out

def value_interval(f,iv):
 n,d=s.fraction(s.cancel(f));ni=polynomial_interval(n,iv);di=polynomial_interval(d,iv)
 if di[0]<=0<=di[1]:return None
 return mul(ni,(min(1/di[0],1/di[1]),max(1/di[0],1/di[1])))

def counts(ps):
 c=[s.Integer(1)]
 for p in ps:
  c=[s.expand((c[j] if j<len(c) else 0)*(1-p)+(c[j-1] if j else 0)*p) for j in range(len(c)+1)]
 return c

def odds(ps,q,t):
 m=len(ps);c=counts(ps)
 return s.cancel(q/(1-q)*Q(m-t+1,t)*c[t-1]/c[t])

def validate(bounds,d):
 b=[tuple(map(rational,v)) for v in bounds];d=[list(map(rational,row)) for row in d];n=len(b)
 if n<2 or any(len(v)!=2 for v in b) or len(d)!=n or any(len(row)!=n for row in d):raise ValueError('shape')
 if any(not (0<lo<=hi<1) for lo,hi in b):raise ValueError('strictly interior intervals required')
 if any(d[i][i]!=0 for i in range(n)) or any(d[i][j]<0 or d[i][j]!=d[j][i] for i in range(n) for j in range(n)):raise ValueError('pseudometric')
 if any(d[i][j]>d[i][k]+d[k][j] for i in range(n) for j in range(n) for k in range(n)):raise ValueError('triangle')
 return b,d

def solve(bounds,d,t,tol=Q(1,10**9)):
 b,d=validate(bounds,d);tol=rational(tol);m=len(b)-1
 if isinstance(t,bool) or not isinstance(t,int) or not 1<=t<=m or tol<=0:raise ValueError('t or tolerance')
 if any(b[i][0]>b[j][1]+d[i][j] for i in range(m+1) for j in range(m+1)):
  return {'status':'infeasible','scope':'No evidence factor licensed by an empty set.'}
 low=max([b[0][0]]+[b[i][0]-d[i][0] for i in range(1,m+1)])
 high=min([b[0][1]]+[b[i][1]+d[i][0] for i in range(1,m+1)])
 ca=[max(b[j][0]-d[i][j] for j in range(1,m+1)) for i in range(1,m+1)]
 cb=[min(b[j][1]+d[i][j] for j in range(1,m+1)) for i in range(1,m+1)]
 cuts=sorted({low,high}|{v for i in range(m) for v in (ca[i]+d[i+1][0],cb[i]-d[i+1][0]) if low<v<high})
 result={'status':'feasible','science_interval':list(map(str,(low,high))),'breakpoints':list(map(str,cuts)),'branches':{}}
 for kind in ('lower','upper'):
  cand=[];cells=[]
  def ps_at(z):
   return [min(cb[i],z+d[i+1][0]) if kind=='lower' else max(ca[i],z-d[i+1][0]) for i in range(m)]
  for z in cuts:
   ps=ps_at(z);v=odds(ps,z,t)
   cand.append({'kind':'breakpoint','x':str(z),'probabilities':list(map(str,ps)),'value_interval':[str(v),str(v)]})
  for l,h in zip(cuts,cuts[1:]):
   mid=(l+h)/2
   ps=[(cb[i] if cb[i]<mid+d[i+1][0] else x+d[i+1][0]) if kind=='lower' else (ca[i] if ca[i]>mid-d[i+1][0] else x-d[i+1][0]) for i in range(m)]
   f=odds(ps,x,t);num,den=s.fraction(f);der=s.Poly(s.diff(num,x)*den-num*s.diff(den,x),x)
   cell={'interval':[str(l),str(h)],'function':str(f),'probabilities':list(map(str,ps)),'derivative':str(der.as_expr()),'stationary_count':0}
   if not der.is_zero:
    sq=der.sqf_part()
    for (a,b0),mult in sq.intervals(inf=l,sup=h,eps=tol):
     if a==b0 and a in (l,h):continue
     # Isolating intervals are exact, complete; refine value, not x-width alone.
     while True:
      if a>l and b0<h or a==b0 and l<a<h:
       vi=value_interval(f,(a,b0))
       if vi is not None and vi[1]-vi[0]<=tol:break
      if a==b0:raise AssertionError('endpoint root handling')
      a,b0=sq.refine_root(a,b0,eps=(b0-a)/2)
     cand.append({'kind':'stationary','root_polynomial':str(sq.as_expr()),'root_interval':[str(a),str(b0)],'function':str(f),'probabilities':list(map(str,ps)),'value_interval':list(map(str,vi))})
     cell['stationary_count']+=1
   else:cell['constant']=True
   cells.append(cell)
  lo=[Q(c['value_interval'][0]) for c in cand];hi=[Q(c['value_interval'][1]) for c in cand]
  ext=(min(lo),min(hi)) if kind=='lower' else (max(lo),max(hi))
  result['branches'][kind]={'candidates':cand,'cells':cells,'extremum_enclosure':list(map(str,ext))}
 return result

def nonnegative(poly,l,h):
 p=s.Poly(poly,x)
 if p.is_zero:return True
 if p.eval(l)<0 or p.eval(h)<0:return False
 roots=p.sqf_part().intervals(inf=l,sup=h,eps=Q(1,10**10))
 # Each isolating interval contains one root. Signs on every component
 # between roots suffice; odd crossings are seen on both adjacent components.
 points=[];last=l
 for (a,b),_ in roots:
  points.extend([a,b])
  if a>last:points.append((last+a)/2)
  last=max(last,b)
 if last<h:points.append((last+h)/2)
 return all(p.eval(z)>=0 for z in points)

def verify_bound(branch,target,lower):
 for c in branch['candidates']:
  if c['kind']=='breakpoint':
   v=Q(c['value_interval'][0]);assert v>=target if lower else v<=target
 for cell in branch['cells']:
  f=s.sympify(cell['function'],locals={'x':x});n,d=s.fraction(f);l,h=map(Q,cell['interval'])
  assert not s.Poly(d,x).count_roots(l,h)
  sign=1 if d.subs(x,(l+h)/2)>0 else -1
  p=sign*(n-target*d) if lower else sign*(target*d-n)
  assert nonnegative(p,l,h)
 assert any(c['kind']=='breakpoint' and Q(c['value_interval'][0])==target for c in branch['candidates'])

checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def rejects(fn):
 try:fn()
 except ValueError:return True
 return False

def main():
 bounds=[(Q(3,8),Q(5,8))]+[(Q(1,4),Q(3,4))]*4;d=[[Q(abs(i-j),16) for j in range(5)] for i in range(5)]
 expected=[(Q(105,214),Q(495,268)),(Q(642,1265),Q(2412,1265)),(Q(1265,2412),Q(1265,642)),(Q(268,495),Q(214,105))];results=[]
 for t in range(1,5):
  r=solve(bounds,d,t);results.append(r)
  for kind,val in zip(('lower','upper'),expected[t-1]):
   br=r['branches'][kind];verify_bound(br,val,kind=='lower');ck('whole_cell_sharp_'+kind+str(t),True)
   iv=list(map(Q,br['extremum_enclosure']));ck('outward_'+kind+str(t),iv[0]<=val<=iv[1] and iv[1]-iv[0]<=Q(1,10**9))
 ck('complement_reciprocity',all(expected[t][0]*expected[3-t][1]==1 for t in range(4)))
 br=results[0]['branches']['upper'];stat=[c for c in br['candidates'] if c['kind']=='stationary'];ck('bare_metric_interior_stationary_control',bool(stat))
 H=10485760*x**7-78315520*x**6+249200640*x**5-437520640*x**4+457190688*x**3-283899454*x**2+96797624*x-13939065
 ck('independent_stationary_polynomial',any(s.rem(s.Poly(s.sympify(c['root_polynomial']),x),s.Poly(H,x)).is_zero for c in stat))
 ck('stationary_is_local_minimum',s.Poly(H,x).count_roots(Q(9,16),Q(5,8))==1 and H.subs(x,Q(9,16))<0<H.subs(x,Q(5,8)))
 # Original five-label hidden-role experiment, independent of odds recurrence.
 probs=[Q(1,2),Q(7,16),Q(6,16),Q(5,16),Q(4,16)];labels=[1,1,0,0,0];mass=[Q(0)]*5
 for perm in permutations(range(5)):
  prob=s.prod(probs[perm[j]] if labels[j] else 1-probs[perm[j]] for j in range(5))/math.factorial(5)
  mass[perm.index(0)]+=prob
 total=sum(mass);post=[v/total for v in mass]
 ck('original_labeled_event_probability',total==Q(2873,81920))
 ck('original_hidden_role_probabilities',post==[Q(804,2873)]*2+[Q(1265,8619)]*3)
 normalizer=sum(post[:2]);ck('actual_factor_consumer',normalizer==Q(1608,2873) and 1/normalizer==Q(2873,1608)>Q(13,10))
 rmax=expected[1][1];ck('independent_formula_matches_original_roles',2*rmax/(2*rmax+3)==normalizer)
 conservative=Q(results[1]['branches']['upper']['extremum_enclosure'][1]);ck('conservative_factor_expected_at_most_one',normalizer/(2*conservative/(2*conservative+3))<=1)
 # Singleton, duplicated nodes, constant cells, impossible constraints.
 same=solve([(Q(1,2),Q(1,2))]*3,[[0]*3 for _ in range(3)],1)
 ck('singleton_zero_distance',same['branches']['lower']['extremum_enclosure']==['1','1'])
 same=solve([(Q(1,4),Q(3,4))]*3,[[0]*3 for _ in range(3)],1)
 ck('constant_cells',all(c.get('constant') for b in same['branches'].values() for c in b['cells']))
 bad=solve([(Q(1,4),Q(1,4)),(Q(3,4),Q(3,4))],[[0,0],[0,0]],1)
 ctrl('infeasibility_not_evidence',bad['status']=='infeasible' and 'branches' not in bad)
 ctrl('floats_rejected',rejects(lambda:solve([(0.2,0.5)]*2,[[0,1],[1,0]],1)))
 ctrl('boundary_support_rejected',rejects(lambda:solve([(0,1)]*2,[[0,1],[1,0]],1)))
 ctrl('nonmetric_rejected',rejects(lambda:solve([(Q(1,4),Q(3,4))]*3,[[0,1,3],[1,0,1],[3,1,0]],1)))
 ctrl('uncoupled_corner_is_infeasible',abs(Q(5,8)-Q(1,4))>d[0][1])
 # Demonstrate sign checker rejects a polynomial with an interior negative well.
 ctrl('interior_negative_polynomial_detected',not nonnegative((x-Q(1,3))*(x-Q(2,3)),0,1))
 ctrl('touching_isolators_negative_well_detected',not nonnegative((x-Q(1,2)-Q(1,10**12))*(x-Q(1,2)+Q(1,10**12)),0,1))
 report={'result_id':'K2412','checks':checks,'controls':controls,'fixtures':results,'sharp_bounds':[[str(a),str(b)] for a,b in expected],'factor':'2873/1608','scope':'Finite exact metric-box solver, complete stationary candidates and outward rational bounds; no measured calibration or GU verdict.'}
 deps=['explorations/conditional-build/k2409-coupled-drift-calibration-2026-10-31.md','tests/channel-swings/k2409_coupled_drift_calibration_probe.py']
 report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
 out=R/'lab/process/k2412-exact-metric-pool-odds.json'
 if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 elif '--verify-only' not in sys.argv:assert json.loads(out.read_text())==report
 print(json.dumps({'checks':len(checks),'controls':len(controls),'status':'pass'},sort_keys=True))
if __name__=='__main__':main()
