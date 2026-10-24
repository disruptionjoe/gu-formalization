"""Replay exact rational dual certificates for the connected thermal frontier.

The compressed payload is plain UTF-8 JSON, zlib compressed and base85 encoded.
Its dual vectors are a proof object: replay requires no optimization library.
LP discovery is described in the exploration; every accepted coefficient is exact.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
from itertools import product
import json,zlib,base64,hashlib,argparse
from k2015_finite_thermal_ray_separation import supports,matrices
from k2006_uniform_two_component_spacing import rate,valid
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2027-thermal-pattern-frontier.json'
LO,HI=Q(7,5),Q(8,5);A,C=Q(985095,2040416),Q(61407,2040416);B=Q(1,41)
def line(e):return A-C*e

def unpack(r):
 raw=zlib.decompress(base64.b85decode(r['certificate_payload'].encode()))
 assert hashlib.sha256(raw).hexdigest()==r['certificate_sha256']
 return json.loads(raw)

def program(s,o,kind):
 n=len(s);ed,df,_=matrices(s,o)
 rows=[[-Q(x) for x in row]+[Q(0)]*n for row in ed]+[[Q(x,30) for x in row]+[-Q(i==j) for j in range(n)] for i,row in enumerate(df)]
 rhs=[Q(0)]*len(rows)
 if kind not in ('energy','maxenergy'):
  rows.append(list(map(Q,s))+[Q(0)]*n);rhs.append(LO if kind=='low' else HI)
 if kind=='strip':rows.append([-Q(x) for x in s]+[Q(0)]*n);rhs.append(-LO)
 cost=([(-1 if kind=='maxenergy' else 1)*Q(x) for x in s]+[Q(0)]*n if kind in ('energy','maxenergy') else [(C if kind=='strip' else B)*x for x in s]+[Q(1)]*n)
 return rows,rhs,cost

def dual(s,o,cert):
 n=len(s);kind=cert['kind'];ed,df,_=matrices(s,o)
 # Integer rows are30 times the original inequalities.
 rows=[{j:-30*x for j,x in enumerate(row) if x} for row in ed]
 rows += [{**{j:x for j,x in enumerate(row) if x},n+i:-30} for i,row in enumerate(df)]
 rhs=[Q(0)]*len(rows)
 if kind not in ('energy','maxenergy'):
  rows.append({j:30*x for j,x in enumerate(s)});rhs.append(LO if kind=='low' else HI)
 if kind=='strip':rows.append({j:-30*x for j,x in enumerate(s)});rhs.append(-LO)
 cost=([(-1 if kind=='maxenergy' else 1)*Q(x) for x in s]+[Q(0)]*n if kind in ('energy','maxenergy') else [(C if kind=='strip' else B)*x for x in s]+[Q(1)]*n)
 y=list(map(Q,cert['y']));z=Q(cert['z']);assert len(y)==len(rows) and all(v<=0 for v in y)
 d=lcm(*(v.denominator for v in y+[z]+cost));Y=[int(v*d) for v in y];Z=int(z*d)
 residual=[30*int(v*d)-30*Z*int(j<n) for j,v in enumerate(cost)]
 for row,v in zip(rows,Y):
  if v:
   for j,a in row.items():residual[j]-=a*v
 assert min(residual)>=0
 return z+sum(a*v for a,v in zip(rhs,y) if a)

def check(r,verbose=False):
 rows=unpack(r);expected=[(s,o) for s in supports(20) if min(s)<=HI for o in product((-1,1),repeat=len(s)-1)]
 assert len(rows)==len(expected)==r['orientation_cells']
 tests=0;infeasible=0
 for idx,(row,(s,o)) in enumerate(zip(rows,expected)):
  assert row['s']==list(s) and row['o']==list(o)
  assert len(row['certificates'])==2
  for kind,cert in zip(('low','strip'),row['certificates']):
   assert cert['kind']==kind
   if 'infeasible_energy' in cert:
    value=dual(s,o,cert['infeasible_energy']);assert value>(LO if kind=='low' else HI);infeasible+=1
   elif 'infeasible_maxenergy' in cert:
    value=dual(s,o,cert['infeasible_maxenergy']);assert kind=='strip' and -value<LO;infeasible+=1
   else:
    value=dual(s,o,cert);assert value>=(line(LO)+B*LO if kind=='low' else A)
   tests+=1
  if verbose and idx%20000==0:print('exact dual replay',idx,flush=True)
 # Affine populations have the same shell order and deficit signs at endpoints.
 for w in r['witnesses']:
  s=w['support'];p=list(map(Q,w['population']));spec=w['spectrum'];e=Q(w['energy'])
  assert min(p)>0 and sum(p)==1 and sum(x*y for x,y in zip(s,p))==e
  assert valid(spec,s) and rate(Q(1,2),s,p)==Q(w['return_value'])==line(e)
  assert min(y-x for x,y in zip(spec,spec[1:]))==1
 kappa=min((20-e)*B-line(e) for e in (LO,HI));assert kappa>0 and str(kappa)==r['tail_mass_coefficient']
 assert C>B>0
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return dict(dual_certificates=tests,infeasible_sections=infeasible,orientation_cells=len(rows),provenance_hashes=len(r['inputs']))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--verbose',action='store_true');a=ap.parse_args();r=json.loads(OUT.read_text());print('PASS K2027',check(r,a.verbose),flush=True)
