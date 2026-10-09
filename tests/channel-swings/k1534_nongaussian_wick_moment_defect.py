#!/usr/bin/env python3
"""Controls for K1534's exact moment defect and two-well boundary."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1534-nongaussian-wick-moment-defect.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['moment_defect'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1534'),('central moments','third central moment' in q['central_data']),('exact remainder','4h(x)mu3(x)+mu4(x)-3v(x)^2' in q['exact_identity']),('K1529 recovery',"K1529's Gaussian polynomial" in q['exact_identity']),('class beta','0<=beta<c_*' in q['wick_dominant_class']),('integrated defect','int R_N(x)dx' in q['wick_dominant_class']),('class coercivity','(c_*-beta)C_N V_N' in q['class_coercivity']),('nonGaussian class','nonnegative fourth cumulants' in q['non_gaussian_members']),('scale mixtures','Gaussian scale mixtures' in q['non_gaussian_members']),('two well','kappa4(Y)=-2a^4' in q['smooth_two_well_counterexample']),('two well zero','tending to zero' in q['smooth_two_well_counterexample']),('cutoff cat','6epsilon(2-epsilon)C_N^2' in q['cutoff_cat_squeeze']),('cat Fisher','Theta(N^4/epsilon)' in q['cat_squeeze_cost']),('cat N6','Theta(N^6)' in q['cat_squeeze_cost']),('scope platykurtic','platykurtic' in q['scope_guard']),('identity decision',d['exact_nongaussian_moment_identity_proved']),('material class',d['material_nongaussian_class_identified']),('variance false',d['variance_only_wick_coercivity_false']),('cat no N2',not d['cat_squeeze_order_N2_trial_exists']),('all open',not d['all_nongaussian_states_classified']),('protected',not d['protected_status_change'])]
 # Exact smooth two-well moments and the cutoff formula.
 for C,eps in [(2.0,0.2),(5.0,0.05),(11.0,0.6)]:
  a2=3*C-eps*eps
  var=a2+eps*eps
  fourth=a2*a2+6*a2*eps*eps+3*eps**4
  defect=fourth-3*var*var
  centered_square=fourth-var*var
  expected=4*a2*eps*eps+2*eps**4
  checks += [(f'variance {C,eps}',math.isclose(var,3*C)),(f'kappa4 {C,eps}',math.isclose(defect,-2*a2*a2)),(f'two-well square {C,eps}',math.isclose(centered_square,expected))]
 for eps in (0.1,0.4,0.8):
  C=7.0;a2=3*(1-eps)*C;var=a2+eps*C;fourth=a2*a2+6*a2*eps*C+3*(eps*C)**2
  w=fourth-6*C*var+9*C*C
  checks.append((f'cat formula eps={eps}',math.isclose(w,6*eps*(2-eps)*C*C,rel_tol=1e-12)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
