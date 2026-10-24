"""Exact wide-spacing program for cutoff-nine connected occupied ladders.

Consecutive physical completion is an explicit restriction, not an all-spectrum theorem.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import json,hashlib,argparse
from k2015_finite_thermal_ray_separation import matrices
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2025-wide-spacing-ladder-program.json'
A=Q(6,5);B=Q(11,5)
def ladder(s):return tuple(range(s[-1]+(2 if len(s)>1 and s[-1]-s[-2]==1 else 1)+1))
def bank():
 c=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census'];rays={};segments={}
 for ci,cell in enumerate(c['cells']):
  S=cell['support'];N=len(ladder(S));vs=cell['vertices'];_,de,_=matrices(S,cell['orientation'])
  signs=[[sum(Q(x)*Q(y) for x,y in zip(row,v['p'])) for row in de] for v in vs]
  for i,v in enumerate(vs):
   e,R=Q(v['energy']),Q(v['return']);rays.setdefault((e,R,N),(ci,i))
  for i,j in combinations(range(len(vs)),2):
   if any(x*y<0 for x,y in zip(signs[i],signs[j])):continue
   e,R=Q(vs[i]['energy']),Q(vs[i]['return']);f,T=Q(vs[j]['energy']),Q(vs[j]['return'])
   if e>f:e,f,R,T=f,e,T,R;i0,j0=j,i
   else:i0,j0=i,j
   if e<f and e<B and f>A:segments.setdefault((e,R,f,T),(ci,i0,j0))
 return c,rays,segments

def evaluate(d,E,rays,segments):
 best=(Q(1,2),('pure',))
 for (e,R,N),ref in rays.items():
  if e<=E and R<best[0]:best=(R,('single',*ref))
 for (e,R,f,T),ref in segments.items():
  if e<=E<=f:
   z=((f-E)*R+(E-e)*T)/(f-e)
   if z<best[0]:best=(z,('same',*ref))
 for (e,R,N),ref in rays.items():
  if e>E:continue
  for (f,T,M),ref2 in rays.items():
   ff=f+N-1+d
   if ff<E or T>=best[0] and R>=best[0]:continue
   z=((ff-E)*R+(E-e)*T)/(ff-e)
   if z<best[0]:best=(z,('separated',*ref,*ref2,str(N-1+d)))
 return best

def witness(c,d,E,ref):
 cells=c['cells'];kind=ref[0]
 if kind=='pure':return dict(spectrum=['0','1','2'],support=['1'],population=['1'],mean='1',return_value='1/2')
 ci,vi=ref[1:3];cell=cells[ci];S=list(map(Q,cell['support']));p=list(map(Q,cell['vertices'][vi]['p']));spec=list(map(Q,ladder(cell['support'])))
 if kind=='same':
  w=cell['vertices'][ref[3]];e=Q(cell['vertices'][vi]['energy']);f=Q(w['energy']);theta=(f-E)/(f-e);p=[theta*x+(1-theta)*Q(y) for x,y in zip(p,w['p'])]
 elif kind=='separated':
  cj,vj=ref[3:5];other=cells[cj];w=other['vertices'][vj];x=Q(ref[5]);e=Q(cell['vertices'][vi]['energy']);f=Q(w['energy'])+x;theta=(f-E)/(f-e)
  p=[theta*y for y in p]+[(1-theta)*Q(y) for y in w['p']];S += [Q(y)+x for y in other['support']];spec=sorted(spec+[Q(y)+x for y in ladder(other['support'])])
 from k2006_uniform_two_component_spacing import rate,valid
 assert valid(spec,[x for x,y in zip(S,p) if y]) and sum(p)==1 and min(p)>=0
 assert min(b-a for a,b in zip(spec,spec[1:]))>=d
 mean=sum(x*y for x,y in zip(S,p));assert mean<=E
 return dict(spectrum=list(map(str,spec)),support=list(map(str,S)),population=list(map(str,p)),mean=str(mean),return_value=str(rate(Q(1,2),S,p)))

LARGER_WITNESSES = [{'n': 6, 'energy': '13/10', 'support': ['1', '3', '5', '7', '9', '11'], 'population': ['18063/20440', '2007/20440', '223/20440', '79/40880', '43/20440', '129/40880'], 'mean': '13/10', 'return_value': '7251/16352', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], 'orientation': [1, 1, 1, -1, -1]}, {'n': 6, 'energy': '7/5', 'support': ['1', '3', '5', '7', '9', '11'], 'population': ['27054/31115', '3006/31115', '57/4445', '246/31115', '369/31115', '41/31115'], 'mean': '7/5', 'return_value': '27423/62230', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], 'orientation': [1, 1, -1, -1, 1]}, {'n': 6, 'energy': '3/2', 'support': ['1', '3', '5', '7', '9', '11'], 'population': ['5328/6223', '592/6223', '13/889', '159/12446', '477/24892', '53/24892'], 'mean': '3/2', 'return_value': '21789/49784', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], 'orientation': [1, 1, -1, -1, 1]}, {'n': 6, 'energy': '8/5', 'support': ['1', '3', '5', '7', '9', '11'], 'population': ['26226/31115', '2914/31115', '73/4445', '549/31115', '1647/62230', '183/62230'], 'mean': '8/5', 'return_value': '54099/124460', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], 'orientation': [1, 1, -1, -1, 1]}, {'n': 7, 'energy': '13/10', 'support': ['1', '3', '5', '7', '9', '11', '13'], 'population': ['321732/364025', '35748/364025', '3972/364025', '681/364025', '1419/728050', '4257/1456100', '473/1456100'], 'mean': '13/10', 'return_value': '258237/582440', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'], 'orientation': [1, 1, 1, -1, -1, 1]}, {'n': 7, 'energy': '7/5', 'support': ['1', '3', '5', '7', '9', '11', '13'], 'population': ['27344/31445', '27344/283005', '724/56601', '246/31445', '369/31445', '41/31445', '41/283005'], 'mean': '7/5', 'return_value': '27713/62890', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'], 'orientation': [1, 1, -1, -1, 1, 1]}, {'n': 7, 'energy': '3/2', 'support': ['1', '3', '5', '7', '9', '11', '13'], 'population': ['10771/12578', '10771/113202', '3299/226404', '159/12578', '477/25156', '53/25156', '53/226404'], 'mean': '3/2', 'return_value': '22019/50312', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'], 'orientation': [1, 1, -1, -1, 1, 1]}, {'n': 7, 'energy': '8/5', 'support': ['1', '3', '5', '7', '9', '11', '13'], 'population': ['26511/31445', '8837/94335', '617/37734', '549/31445', '1647/62890', '183/62890', '61/188670'], 'mean': '8/5', 'return_value': '54669/125780', 'spectrum': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'], 'orientation': [1, 1, -1, -1, 1, 1]}]

def rectangle(rays,segments):
 lo,hi=Q(7,5),Q(8,5)
 # The same-cone chord from cell57, vertices14 and10.
 e,r,f,t=Q(945,733),Q(651,1466),Q(335,179),Q(153,358)
 slope=(t-r)/(f-e);intercept=r-slope*e
 def line(E):return intercept+slope*E
 count=0;digest=hashlib.sha256()
 def check(gap):
  nonlocal count
  assert gap>=0;count+=1;digest.update((str(gap)+';').encode())
 for (e,r,N),ref in sorted(rays.items()):
  if e<=hi:check(r-line(max(lo,e)))
 for (e,r,f,t),ref in sorted(segments.items()):
  a,b=max(lo,e),min(hi,f)
  if a<=b:
   for E in [a,b]:check((f-E)*r+(E-e)*t-line(E)*(f-e))
 for (e,r,N),ref in sorted(rays.items()):
  if e>hi:continue
  for (f,t,M),ref2 in sorted(rays.items()):
   # The high endpoint is always beyond this energy rectangle.
   assert f+N-Q(1,2)>hi
   for d in [Q(1,2),Q(1)]:
    ff=f+N-1+d
    for E in [max(lo,e),hi]:check((ff-E)*r+(E-e)*t-line(E)*(ff-e))
 return dict(delta_open_interval=['1/2','1'],energy_closed_interval=['7/5','8/5'],intercept=str(intercept),slope=str(slope),corner_inequalities=count,digest=digest.hexdigest())

def larger_controls(rows,rect):
 from k2006_uniform_two_component_spacing import rate,valid
 out=[]
 for w in LARGER_WITNESSES:
  s=list(map(Q,w['support']));p=list(map(Q,w['population']));a=list(map(Q,w['spectrum']));E=Q(w['energy']);R=Q(w['return_value'])
  assert sum(p)==1 and min(p)>=0 and sum(x*y for x,y in zip(s,p))==E and valid(a,s)
  assert min(y-x for x,y in zip(a,a[1:]))==1 and rate(Q(1,2),s,p)==R
  comparisons=[dict(delta=r['delta'],strict_improvement=str(Q(r['value'])-R)) for r in rows if r['energy']==w['energy']]
  assert all(Q(v['strict_improvement'])>0 for v in comparisons)
  out.append(dict(**w,comparisons=comparisons))
 branches=[]
 for n in [6,7]:
  ends=[next(w for w in out if w['n']==n and w['energy']==E) for E in ['7/5','8/5']]
  s=list(map(int,ends[0]['support']));p,q=[list(map(Q,w['population'])) for w in ends];o=ends[0]['orientation'];assert o==ends[1]['orientation']
  edges,df,_=matrices(s,o)
  for a in edges:
   assert sum(Q(x)*y for x,y in zip(a,p))>=0 and sum(Q(x)*y for x,y in zip(a,q))>=0
  for a in df:assert sum(Q(x)*y for x,y in zip(a,p))*sum(Q(x)*y for x,y in zip(a,q))>=0
  m=(Q(ends[1]['return_value'])-Q(ends[0]['return_value']))/Q(1,5);b=Q(ends[0]['return_value'])-m*Q(7,5)
  gaps=[Q(rect['intercept'])+Q(rect['slope'])*E-(b+m*E) for E in [Q(7,5),Q(8,5)]];assert min(gaps)>0
  branches.append(dict(levels=2*n+1,energy_interval=['7/5','8/5'],intercept=str(b),slope=str(m),minimum_improvement=str(min(gaps)),meaning='Actual affine populations and return across entire interval, all positive spacing<=1; not globally optimal.'))
 return out,branches


def tail_family():
 # Exact summation proof: q=9^(-m-1), A=sum9^-k, B=sum k9^-k.
 from k2006_uniform_two_component_spacing import rate,valid
 lo,hi=Q(7,5),Q(8,5);a,c=Q(101,10),Q(25,2);D=134375;cc=21816;dd=109215
 endpoints=[];controls=[]
 for E in [lo,hi]:
  AA=64875-4044*E;BB=1215*(4*E-45);CC=-9720
  alpha=AA*cc+D*CC;beta=AA*dd+D*BB;h=cc*BB-CC*dd
  # For m>=3 the successive-difference numerator is positive:
  # -8 beta+alpha(1-8m)+q h; alpha<0, h>0, base at3>0.
  assert alpha<0 and h>0 and -8*beta-23*alpha>0
  steps=[-8*beta+alpha*(1-8*m)+Q(1,9**(m+1))*h for m in range(3)]
  assert max(steps)<0
  endpoints.append(dict(E=str(E),alpha=str(alpha),beta=str(beta),h=str(h),first_three_step_numerators=list(map(str,steps)),all_later_lower_bound=str(-8*beta-23*alpha)))
  for m in range(9):
   q=Q(1,9**(m+1));As=sum(Q(1,9**k) for k in range(m+1));Bs=sum(Q(k,9**k) for k in range(m+1))
   assert As==Q(9,8)*(1-q) and Bs==Q(9,64)*(1-(8*m+9)*q)
   b=Q(247,80)-Q(27,16)*q;d=Q(1575,64)-Q(27*(8*m+45),64)*q
   assert b==Q(7,5)+Q(3,2)*As and d==9+Q(3,2)*(9*As+2*Bs)
   det=a*d-b*c;u=(d-b*E)/det;v=(a*E-c)/det
   pop=[9*u,u,(u+4*v)/10,v]+[Q(3,2)*v*Q(1,9**k) for k in range(m+1)]
   support=list(range(1,2*m+10,2));spec=list(range(2*m+11))
   R=(64875-4044*E+1215*q*(4*E-8*m-45))/(D-27*q*(808*m+4045))
   assert sum(pop)==1 and min(pop)>0 and sum(x*y for x,y in zip(support,pop))==E
   assert Q(8,3)<u/v<36 and valid(spec,support) and rate(Q(1,2),support,pop)==R==Q(9,2)*u+Q(3,4)*v
   controls.append(dict(m=m,energy=str(E),spectrum=list(map(str,spec)),support=list(map(str,support)),population=list(map(str,pop)),mean=str(E),return_value=str(R)))
 # Uniform ratio bounds: d_m-b_m E increases with m; ratio decreases with E.
 lower=Q(893,183);upper=Q(32459,2624);assert Q(8,3)<lower<upper<36
 q=Q(1,9**4);den=D-27*q*(808*3+4045)
 slope=(-4044+4860*q)/den;intercept=(64875-1215*q*69)/den
 return dict(energy_interval=['7/5','8/5'],all_positive_spacing_at_most='1',dimension='2m+11',population_formula=['9u','u','(u+4v)/10','v','(3v/2)9^-k for k=0..m'],u_v_ratio_bounds=list(map(str,[lower,upper])),successive_difference_endpoint_certificates=endpoints,finite_controls=controls,unique_minimizing_m=3,minimizing_levels=17,minimum_intercept=str(intercept),minimum_slope=str(slope),limit_intercept=str(Q(64875,D)),limit_slope=str(Q(-4044,D)),ceiling='Exact optimum ONLY within this explicit one-parameter geometric-tail family; no unrestricted optimum or infinite-dimension necessity. Finite17 beats its infinite tail limit.')

def produce():
 c,rays,segs=bank();print('bank',len(rays),len(segs),flush=True)
 rows=[]
 for d in [Q(501,1000),Q(3,5),Q(3,4),Q(99,100)]:
  for E in [A,Q(113,91),Q(13,10),Q(7,5),Q(3,2),Q(8,5),Q(17,10),Q(9,5),Q(2),B]:
   value,ref=evaluate(d,E,rays,segs);row=dict(delta=str(d),energy=str(E),value=str(value),ref=list(ref));row['witness']=witness(c,d,E,ref);assert Q(row['witness']['return_value'])==value;rows.append(row);print({k:v for k,v in row.items() if k!='witness'},flush=True)
 rect=rectangle(rays,segs);larger,branches=larger_controls(rows,rect)
 return dict(geometric_tail_family=tail_family(),rectangle_certificate=rect,larger_witnesses=larger,larger_affine_branches=branches,result_id='K2025',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',rows=rows,rays=len(rays),segments=len(segs),scope='Finite consecutive-completion ladder family, canonical connected occupied supports through9, at most two such ladders with delta in(1/2,1); not unrestricted frontier or all holed completions.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k2015-finite-thermal-ray-separation.json','lab/process/k2006-uniform-two-component-spacing.json']})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text())
 print('PASS K2025')
