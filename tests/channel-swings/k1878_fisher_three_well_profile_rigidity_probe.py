#!/usr/bin/env python3
"""Independent rational controls; analytic compactness is proved in the note."""
import copy,hashlib,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'lab/process/k1878-fisher-three-well-profile-rigidity.json'
def verify_math(c):
 n=0
 def ck(v,name):
  nonlocal n
  if not v:raise AssertionError('FAIL '+name)
  n+=1
 for k in [F(7,2),F(4),F(5),F(11)]:
  for eta in [F(0),F(1,7),F(1,2),F(1)]:
   p=[1-1/k,eta/k,(1-eta)/k];a=[k,2*k,2*k]
   q=[c['central']/(k*(k+1)),c['outer']/(k*(k+1)),c['outer']/(k*(k+1))]
   ck(sum(p)==1,'mass');ck(sum(p[i]*a[i] for i in range(3))==k+1,'slope_sum')
   ck(sum(p[i]*a[i]**2*q[i] for i in range(3))==1,'slack_allocation')
   ck(sum(p[i]/q[i] for i in range(3))==c['energy']*(k+1)**2,'energy_allocation')
   ck(q[0]/q[1]==2,'width_ratio')
   ck(sum(p[i]/q[i] for i in range(3))==sum(p[i]/q[i] for i in [0,2,1]),'sign_swap')
 for z in [F(i,12) for i in range(-60,61)]:
  dist=min(abs(z-r) for r in [-1,0,1]);ck((z**3-z)**2>=c['distance']*dist**2,'global_distance')
 # Nontrivial equality defect evaluated without importing the producer.
 for shift in [F(0),F(1,3),F(-2)]:
  for var in [F(1,7),F(1),F(3)]:
   ck((var+shift*shift)/var-1==shift*shift/var,'mean_shift_defect')
 for t in [F(1,2),F(1),F(2),F(5)]:
  p=[F(1,2),F(1,3),F(1,6)];a=[F(1),F(3),F(2)];q=[t,F(2),F(4)]
  gap=sum(p[i]/q[i] for i in range(3))*sum(p[i]*a[i]**2*q[i] for i in range(3))-sum(p[i]*a[i] for i in range(3))**2
  pair=sum(p[i]*p[j]*(a[i]*q[i]-a[j]*q[j])**2/(q[i]*q[j]) for i in range(3) for j in range(i+1,3))
  ck(gap==pair and gap>=0,'weighted_Cauchy_gap')
 return n
def verify_report(v):
 assert v['result_id']=='K1878','FAIL result id'
 assert v['constants']=={'distance_square_lower':'9*k^2/16','central_variance':'1/(k*(k+1))','outer_variance':'1/(2*k*(k+1))','sharp_scaled_energy':'(k+1)^2','central_mass':'1-1/k','total_outer_mass':'1/k'},'FAIL constants reporting'
 assert v['scope']=={'all_asymptotically_optimal_densities':True,'positive_mass_cells_TV_and_W2':True,'vanishing_cells_profile_unconstrained':True,'even_optimizer_equal_outer_weights':True,'all_near_minimizers_even':False,'effective_rate':False,'sextic_multiplier_or_gap':False,'native_GU_claim':False},'FAIL scope reporting'
 for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'FAIL input pin'
 return 3+len(v['inputs'])
def main():
 v=json.loads(P.read_text());base={'central':F(1),'outer':F(1,2),'energy':F(1),'distance':F(9,16)}
 n=verify_math(base);m=verify_report(v);caught=[]
 for key,bad in [('central',F(2)),('outer',F(1)),('energy',F(2)),('distance',F(1))]:
  c=dict(base);c[key]=bad
  try:verify_math(c)
  except AssertionError as e:assert str(e).startswith('FAIL ');caught.append(str(e))
  else:raise AssertionError('undetected '+key)
 reporting=[]
 for key in ['all_near_minimizers_even','effective_rate','native_GU_claim','vanishing_cells_profile_unconstrained']:
  w=copy.deepcopy(v);w['scope'][key]=not w['scope'][key]
  try:verify_report(w)
  except AssertionError as e:assert str(e).startswith('FAIL ');reporting.append(str(e))
  else:raise AssertionError('undetected reporting '+key)
 print('PASS K1878 independent',n,'rational controls;',m,'reporting/pins;',len(caught),'math faults;',len(reporting),'reporting faults');print(caught,reporting)
if __name__=='__main__':main()
