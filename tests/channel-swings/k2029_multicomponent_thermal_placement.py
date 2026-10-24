"""Exact replay of component placement certificates, without an optimizer."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import lcm
import json,zlib,base64,hashlib
from k2015_finite_thermal_ray_separation import supports,matrices
from k2006_uniform_two_component_spacing import valid,rate
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2029-multicomponent-thermal-placement.json'
A,C,B=Q(985095,2040416),Q(61407,2040416),Q(1,41);lo,hi=Q(7,5),Q(8,5)
def unpack(r):
 raw=zlib.decompress(base64.b85decode(r['payload']));assert hashlib.sha256(raw).hexdigest()==r['payload_sha256'];return json.loads(raw)
def cell(s,o):
 n=len(s);ed,df,_=matrices(s,o)
 return [[-Q(x) for x in row]+[Q(0)]*n for row in ed]+[[Q(x,30) for x in row]+[-Q(i==j) for j in range(n)] for i,row in enumerate(df)]
def verify(cost,rows,rhs,eq,cert):
 y=list(map(Q,cert['y']));z=Q(cert['z']);assert len(y)==len(rows) and max(y)<=0
 residual=[c-z*e-sum(row[j]*v for row,v in zip(rows,y)) for j,(c,e) in enumerate(zip(cost,eq))];assert min(residual)>=0
 value=z+sum(v*b for v,b in zip(y,rhs));assert value==Q(cert['value']);return value

def shortprogram(s,o,penalties):
 n=len(s);L=1 if n==1 else s[-1]+3-(s[-1]-s[-2]);offset=min(Q(L)+Q(1,2),Q(s[-1]+2))
 rows=[row+[Q(0)]*3 for row in cell(s,o)];rhs=[Q(0)]*len(rows)
 en=list(map(Q,s))+[Q(0)]*n+[Q(0),Q(1),Q(0)]
 rows.extend([en,[-v for v in en],[Q(0)]*(2*n)+[offset+1,-Q(1),Q(0)]]);rhs.extend([hi,-lo,Q(0)])
 for lam,a in penalties:rows.append([Q(0)]*(2*n)+[a+lam*offset,-lam,-Q(1)]);rhs.append(Q(0))
 return [C*x for x in s]+[Q(1)]*n+[Q(0),C,Q(1)],rows,rhs,[Q(1)]*n+[Q(0)]*n+[Q(1),Q(0),Q(0)],offset

def check(r):
 d=unpack(r);count=0;penalties=[]
 expected=[(s,o) for s in supports(14) for o in product((-1,1),repeat=len(s)-1)]
 for bank in d['banks']:
  lam,a=Q(bank['slope']),Q(bank['intercept']);assert len(bank['rows'])==len(expected)==4575
  for row,(s,o) in zip(bank['rows'],expected):
   assert row['s']==list(s) and row['o']==list(o);n=len(s);aa=cell(s,o)
   assert verify([lam*x for x in s]+[Q(1)]*n,aa,[Q(0)]*len(aa),[Q(1)]*n+[Q(0)]*n,row['cert'])>=a;count+=1
  assert 15*lam-a>0;penalties.append((lam,a))
 penalties += [(Q(1,4),Q(3,4)),(Q(3,20),Q(63,100))]
 ex=[(s,o) for s in supports(6) if min(s)==1 and (1 if len(s)==1 else s[-2]+3)<7 for o in product((-1,1),repeat=len(s)-1)]
 margins=[]
 for row,(s,o) in zip(d['short'],ex):
  assert row['s']==list(s) and row['o']==list(o);co,aa,bb,eq,off=shortprogram(s,o,penalties);assert off==Q(row['offset']);margins.append(verify(co,aa,bb,eq,row['cert'])-A)
 assert len(d['short'])==len(ex)==13 and min(margins)==Q(r['short_margin'])>0
 assert penalties[0][1]+7*B-(A-(C-B)*lo)==Q(r['long_back_margin'])>0
 assert penalties[1][1]+7*C-A==Q(r['long_main_margin'])>0
 assert min(Q(101,100)-Q(17,50)*e-(A-C*e) for e in [Q(3,2),hi])==Q(r['no_first_one_margin'])>0
 for w in r['witnesses']:
  s=w['support'];p=list(map(Q,w['population']));assert valid(w['spectrum'],s) and sum(p)==1 and min(p)>0
  en=sum(x*y for x,y in zip(s,p));assert rate(Q(1,2),s,p)==A-C*en==Q(w['return_value'])
 w=r['penalty_witness'];s=w['support'];p=list(map(Q,w['population']));assert valid(w['spectrum'],s) and sum(p)==1
 for lam,a in penalties[:2]:assert rate(Q(1,2),s,p)+lam*sum(x*y for x,y in zip(s,p))==a
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return dict(global_duals=count,short_duals=len(ex),physical_optima=len(r['witnesses']),provenance_hashes=len(r['inputs']))
if __name__=='__main__':print('PASS K2029',check(json.loads(OUT.read_text())),flush=True)
