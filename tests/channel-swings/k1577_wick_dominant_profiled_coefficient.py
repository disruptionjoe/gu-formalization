#!/usr/bin/env python3
"""Controls for K1577's matching class coefficient."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1577-wick-dominant-profiled-coefficient.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['coefficient_theorem'],D['decision'];checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1577'),('finite','every cutoff' in q['finite_cutoff_identity']),('limit','h_g^prof' in q['coefficient_limit']),('weak','1/(12pi)' in q['coupling_asymptotics']),('gain','pi/16' in q['coupling_asymptotics']),('strong','4sqrt(24c_Cg)' in q['coupling_asymptotics']),('rigid','constant phase' in q['rigidity']),('advance','genuinely non-Gaussian' in q['advance']),('ceiling','No bounded-error recentering' in q['scope_guard']),('finite decision',d['finite_cutoff_class_infimum_identified']),('coefficient',d['matching_class_coefficient_proved']),('rigidity',d['minimizer_rigidity_proved']),('ratio open',not d['unrestricted_ground_energy_ratio_convergence']),('bounded open',not d['bounded_error_recentering']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
