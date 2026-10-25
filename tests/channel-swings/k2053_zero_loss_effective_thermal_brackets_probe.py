"""Direct bath-label and rational inequality replay, without convex hull calculations."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,copy
from k2045_third_thermal_spacing_phase_probe import physical,common_return_cell
ROOT=Path(__file__).resolve().parents[2]
def replay(r,full=True):
 bank=json.loads((ROOT/r['bank_ref']).read_text())['bank'];assert hashlib.sha256((ROOT/r['bank_ref']).read_bytes()).hexdigest()==r['bank_sha256']
 vals=[];records=0
 for c in bank:
  vs=[]
  for v in c['vertices']:
   e,ret=F(v['energy']),F(v['value'])
   if full:assert physical(list(map(F,c['s'])),list(map(F,v['p'])),list(map(F,range(15))),F(1))==(e,ret),'physical bank return'
   vs.append((e,ret));records+=1
  vals.append(vs)
 E=F(r['energy']);lo=F(r['lower']);hi=F(r['upper']);lines=r['low_cell_assignments'];assert len(lines)==len(vals),'low-cell coverage';unique=set()
 for vs,line in zip(vals,lines):
  a,s=map(F,line);assert s<0 and a+12*s<=0,'low tail sign';assert all(ret>=a+s*e for e,ret in vs),'low-cell support';assert a+s*E>=lo,'bracket lower';unique.add((a,s))
 for a,s in unique:
  assert a+13*s<=0,'high tail sign';assert all(ret>=a+s*(e+1) for vs in vals for e,ret in vs),'high-cell support'
 w=r['witness'];p=list(map(F,w['population']));ss=list(map(F,w['support']));spec=list(map(F,w['physical_spectrum']))
 for delta in [F(501,1000),F(3,4),F(1)]:assert physical(ss,p,spec,delta)==(E,hi),'physical upper witness'
 assert hi>=lo and F(r['width'])==hi-lo,'exact bracket width'
 # Whole-energy interval: shared maxima/clipping signs prove an affine physical family.
 ib=r['interval_bracket'];ends=ib['endpoints'];p0,p1=[list(map(F,e['population'])) for e in ends]
 common_return_cell(ss,p0,p1)
 for end,pop in zip(ends,[p0,p1]):assert physical(ss,pop,spec,F(1))==(F(end['energy']),F(end['value'])),'interval endpoint'
 al,sl=map(F,ib['lower_line']);au,su=map(F,ib['upper_line']);left,right=map(F,ib['interval'])
 assert F(ends[0]['energy'])<=left<=right<=F(ends[1]['energy']),'physical interpolation domain'
 for energy in [left,right]:
  assert all(F(a)+F(s)*energy>=al+sl*energy for a,s in lines),'whole-interval lower order'
  mass=(energy-F(ends[0]['energy']))/(F(ends[1]['energy'])-F(ends[0]['energy']))
  pop=[(1-mass)*a+mass*b for a,b in zip(p0,p1)]
  assert physical(ss,pop,spec,F(1))==(energy,au+su*energy),'whole-interval physical upper'
 assert al+sl*E==lo and au+su*E==hi,'point bracket composition'
 # Normalization inequality is checked with a real erasure equality case.
 e,ret=physical([F(1),F(3)],[F(9,10),F(1,10)],list(map(F,range(5))),F(1))
 _,normalized=physical([F(1)],[F(1)],list(map(F,range(5))),F(1));q=F(1,10)
 assert ret==F(9,20) and normalized==F(1,2),'erasure equality witness'
 assert normalized==r['coefficients']['tail_normalization_numerator']*ret/(1-q),'sharp normalization coefficient'
 assert normalized-ret==q*normalized,'multiplicative rearrangement'
 for row in r['approximation_controls']:
  energy,eps=F(row['E']),F(row['epsilon']);N,D=row['N'],row['D'];Q=(energy-1)/(N-1)
  assert N>energy and F(row['Q'])==Q and F(row['alpha'])==1-Q,'energy tail factor'
  assert D==r['coefficients']['dimension_factor']*N+r['coefficients']['dimension_offset']==2*N+7,'physical completion dimension'
  assert F(row['error'])==Q/r['coefficients']['error_denominator_factor']==Q/2<=eps,'error/tolerance bound'
  # Every endpoint pair of an interval for finite F_D obeys the stated algebra.
  for finite_lo,finite_hi in [(F(0),F(1,2)),(F(1,5),F(1,3)),(F(3,10),F(3,10))]:
   assert finite_hi-(1-Q)*finite_lo==(finite_hi-finite_lo)+Q*finite_lo,'certified interval algebra'
 return dict(physical_bank_records=records,low_cells=len(vals),unique_support_lines=len(unique),physical_witnesses=3,normalization_equality=1,dimension_controls=len(r['approximation_controls']),finite_solver_intervals=27,whole_energy_interval=1)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2053-zero-loss-effective-thermal-brackets.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r),flush=True);faults=[]
 for kind in ['support','population','width','normalization','dimension','error','interval']:
  bad=copy.deepcopy(r)
  if kind=='support':bad['low_cell_assignments'][0][0]='100'
  elif kind=='population':bad['witness']['population'][0]='1/2'
  elif kind=='width':bad['width']='0'
  elif kind=='normalization':bad['coefficients']['tail_normalization_numerator']=2
  elif kind=='dimension':bad['coefficients']['dimension_offset']=3
  elif kind=='error':bad['coefficients']['error_denominator_factor']=3
  else:bad['interval_bracket']['upper_line'][1]='0'
  try:replay(bad,False)
  except AssertionError as e:assert str(e);faults.append([kind,str(e)])
  else:raise AssertionError('missed '+kind)
 print('PASS seven mathematical faults',faults)
