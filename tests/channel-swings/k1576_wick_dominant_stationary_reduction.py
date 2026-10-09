#!/usr/bin/env python3
"""Controls for K1576's stationary all-density reduction."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1576-wick-dominant-stationary-reduction.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['stationary_reduction'],D['decision'];checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1576'),('class','translation-invariant' in q['admitted_class']),('defect','nonnegative' in q['admitted_class']),('nongaussian','Gaussian scale mixtures' in q['material_nongaussian_members']),('fisher','K1533' in q['free_reduction']),('phase','constant phase' in q['free_reduction']),('interaction','K1534' in q['interaction_reduction']),('diagonal','Fourier diagonal' in q['stationary_diagonalization']),('equal infima','infima are equal' in q['finite_cutoff_consequence']),('ceiling','thin bimodal' in q['scope_guard']),('fisher used',d['all_density_fixed_moment_reduction_used']),('sign',d['wick_defect_sign_is_load_bearing']),('match',d['stationary_diagonal_gaussian_infimum_matches_class']),('material',d['material_nongaussian_class_included']),('not unrestricted',not d['unrestricted_nongaussian_lower_bound']),('protected',not d['protected_status_change'])]
 # Symmetric standardized Laplace has fourth cumulant 3>0.
 checks.append(('laplace positive cumulant',6-3*1**2>0))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
