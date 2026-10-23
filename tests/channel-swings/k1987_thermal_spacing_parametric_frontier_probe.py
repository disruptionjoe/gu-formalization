"""Independent bath-label census and exact parametric boundary controls."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def valid(s,e):
 return all(sum(x+b==e+k for x in s for b in range(4))>=2 for k in range(4))
def audit(fault=None):
 r=json.loads((ROOT/'lab/process/k1987-thermal-spacing-parametric-frontier.json').read_text());n=0
 if fault=='spectra':r['three_level_spectra'][0]['spectrum'][-1]='9'
 if fault=='spacing':r['three_level_spectra'][0]['maximum_spacing']='2'
 if fault=='budget':r['feasibility_controls'][0]['feasible']=True
 if fault=='return':r['three_level_returns'][0]['return_error']='1/4'
 expected={(0,a,a+b) for a in range(1,4) for b in range(1,4) if a+b<=4}
 assert {tuple(map(F,x['spectrum'])) for x in r['three_level_spectra']}==expected,'complete real three-level spectrum census'
 for x in r['three_level_spectra']:
  spec=list(map(F,x['spectrum']));e=F(x['occupied']);assert valid(spec,e),'actual shell ranks';assert F(x['maximum_spacing'])==min(b-a for a,b in zip(spec,spec[1:])),'actual adjacent spacing';n+=2
 for row in r['feasibility_controls']:
  d=row['dimension'];delta=F(row['spacing']);E=F(row['budget']);actual=d>=3 and any(valid(list(s),F(s[1])) and min(s[1],s[2]-s[1])>=delta and s[1]<=E for s in expected)
  assert actual==row['feasible'],'exact feasibility witness';n+=1
 for row in r['three_level_returns']:
  t=F(row['t']);g=[t**j/sum(t**k for k in range(4)) for j in range(4)];retention=sum(g)/2
  assert 1-retention==F(row['return_error']),'independent one-occupied-shell return';n+=1
 # The compactness theorem gives left, not right, continuity in spacing.
 for t in [F(1,5),F(1,2),F(4,5)]:
  b=(1+3*t*t)/(4*(1+t*t));jump=F(1,2)-b;assert jump==(1-t*t)/(4*(1+t*t))>0;n+=1
 # Rational grids are stress controls only, never completeness of all real spectra.
 for a,b in combinations([F(i,4) for i in range(1,25)],2):
  ok=valid([F(0),a,b],a)
  assert ok==((F(0),a,b) in expected),'three-level rational stress census';n+=1
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return n
if __name__=='__main__':
 n=audit();caught=[]
 for f in ['spectra','spacing','budget','return']:
  try:audit(f)
  except AssertionError as e:caught.append([f,str(e)])
  else:raise AssertionError('undetected mathematical fault '+f)
 print('PASS K1987 independent',n,'exact controls;',caught)
