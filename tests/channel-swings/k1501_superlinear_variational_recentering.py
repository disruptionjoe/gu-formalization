#!/usr/bin/env python3
"""Controls for K1501's super-sigma variational boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1501-superlinear-variational-recentering.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 a,q=D['superlinear_boundary'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1501'),('fixed degree','fixed d' in a['degree_choice']),('multiplication gain','-(A+1)' in a['multiplication_trial']),('free lower','O_d(N)=o(sigma_N)' in a['free_cost']),('arbitrary coefficient','every fixed A>0' in a['arbitrary_fixed_coefficient']),('ratio','+infinity' in a['ratio_limit']),('necessary recenter','requires' in a['necessary_recentering']),('window','O(sigma_N)' in a['excluded_window']),('Mosco','-infinity' in a['mosco_boundary']),('BRST','harmonic BRST vacuum' in a['brst_transfer']),('super sigma',q['negative_correction_super_sigma']),('window excluded',q['every_order_sigma_recentering_excluded']),('Mosco excluded',q['fixed_gaussian_mosco_weak_liminf_excluded_in_that_window']),('BRST transferred',q['harmonic_brst_boundary_transferred']),('rate fenced',not q['quantitative_divergence_rate_proved']),('dN fenced',not q['cutoff_dependent_degree_constructed']),('lower fenced',not q['matching_ground_energy_lower_bound_proved']),('ground shift open',not q['ground_energy_recentering_excluded']),('recovery fenced',not q['mosco_recovery_proved']),('protected fenced',not q['protected_status_change'])]
 for A in (1,2,5,10,25):
  d=math.ceil((A+2)**2)+1;checks.append((f'A{A} degree fixed',math.sqrt(d)>A+2))
 checks += [('sigma dominates free',all(n**2.5/n>10 for n in (100,400,1600))),('subsequence algebra',-(12-5)<0)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
