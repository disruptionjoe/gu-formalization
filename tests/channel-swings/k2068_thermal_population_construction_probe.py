"""Separate exact bath-label realization and family checks; no numerical solver."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,copy
R=Path(__file__).resolve().parents[2];BATH=list(map(Q,['8/15','4/15','2/15','1/15']))
def raw(s,p):
 return sum(max(Q(0),px-sum(max([Q(0)]+[py*BATH[x+j-y] for y,py in zip(s,p) if x+j-y in range(4)]) for j in range(4))/2) for x,px in zip(s,p))
def output(s,p,half=Q(1,2)):
 spec=list(range(max(s)+2));out={n:Q(0) for n in spec}
 for E in sorted({n+j for n in s for j in range(4)}):
  occ=[(n,p[i]*BATH[E-n]) for i,n in enumerate(s) if E-n in range(4)];physical=[n for n in spec if E-n in range(4)]
  assert len(physical)>=2*len(occ),'shell dimension'
  heavy=max(occ,key=lambda x:x[1]);targets=[heavy[0]]+([x[0] for x in occ if x!=heavy] if len(occ)==2 else [n for n in physical if n!=heavy[0]][:1])
  out[targets[0]]+=half*heavy[1];out[targets[1]]+=(1-half)*heavy[1]
  if len(occ)==2:
   light=next(x for x in occ if x!=heavy);empty=[n for n in physical if n not in targets];out[empty[0]]+=half*light[1];out[empty[1]]+=(1-half)*light[1]
 assert sum(out.values())==sum(p),'unitary column normalization'
 return sum(abs(out[n]-(p[s.index(n)] if n in s else 0)) for n in spec)/2

def family(B,N,E,ratio=Q(1,9)):
 rows=B+[[x*ratio**(i-9) for x in B[-1]] for i in range(10,N)]
 a,b=[sum(row[j] for row in rows) for j in range(2)];c,d=[sum((2*i+1)*row[j] for i,row in enumerate(rows)) for j in range(2)]
 det=a*d-b*c;x=(d-b*E)/det;y=(a*E-c)/det
 return [u*x+v*y for u,v in rows],x+y

def checks(d,fault=None):
 B=[[Q(x) for x in row] for row in d['basis']];count=0
 for N in [10,11,19,20,21,30,40]:
  for E in map(Q,d['uniform_feasible_interval']+['5/2']):
   p,value=family(B,N,E,Q(1,8) if fault=='tail_ratio' else Q(1,9));s=list(range(1,2*N,2))
   assert min(p)>0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==E,'actual population';count+=3
   assert raw(s,p)==value,'raw bath return equals deficit family';count+=1
   assert output(s,p)==value,'physical shell construction';count+=1
 for E in map(Q,d['energy_interval']+['5/2']):
  p=[Q(a)+E*Q(b) for a,b in d['population_affine']]
  if fault=='population':p[8]+=Q(1,1000000)
  assert min(p)>=0 and sum(p)==1,'released affine population'
  assert sum(x*y for x,y in zip(d['occupied_support'],p))==E,'released energy'
  assert raw(d['occupied_support'],p)==Q(d['line'][0])+E*Q(d['line'][1]),'affine actual return';count+=3
 vals={N:family(B,N,Q(5,2))[1] for N in range(10,41)}
 assert min(vals,key=vals.get)==(19 if fault=='minimizer' else d['all_integer_N_minimizer']),'finite controls of analytic minimum';count+=1
 assert vals[20]==Q(d['value'])<Q(d['prior_upper']) and Q(d['prior_upper'])-vals[20]==Q(d['gain']),'strict finite/countable comparison';count+=1
 assert len(d['physical_spectrum'])==41,'physical levels, not just populated levels';count+=1
 return count
if __name__=='__main__':
 d=json.loads((R/'lab/process/k2068-thermal-population-construction.json').read_text())
 for p,h in d['inputs'].items():assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h,'pin'
 n=checks(d);caught=[]
 for f in ['tail_ratio','population','minimizer']:
  try:checks(d,f)
  except AssertionError as e:caught.append((f,str(e)))
  else:raise AssertionError('undetected '+f)
 print('PASS',n,'exact raw bath/physical/affine controls; faults',caught)
