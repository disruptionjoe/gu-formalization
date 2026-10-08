#!/usr/bin/env python3
"""Controls for K1511's recentering and harmonic-BRST boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1511-sqrt-log-recentering-boundary.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 r,q=D['recentering_boundary'],D['decision']
 checks += [('claim',D['claim_id']=='K1511'),('necessary','liminf' in r['necessary_scale'] and '>=sqrt(3)' in r['necessary_scale']),('window','limsup' in r['excluded_window'] and '<sqrt(3)' in r['excluded_window']),('bottoms','minus infinity' in r['excluded_window']),('weak compactness','unit ball' in r['weak_compactness']),('zero allowed','may be zero' in r['weak_compactness']),('Mosco','Mosco liminf' in r['mosco_failure']),('BRST','harmonic BRST vacuum' in r['brst_transfer']),('necessity proved',q['sqrt_log_recentering_necessity_proved']),('Mosco excluded',q['fixed_gaussian_mosco_weak_liminf_window_excluded']),('BRST excluded',q['harmonic_brst_window_excluded']),('limit fenced',not q['ground_energy_recentered_limit_constructed']),('recovery fenced',not q['mosco_recovery_proved']),('changed rep open',not q['changed_representation_excluded']),('protected fenced',not q['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
