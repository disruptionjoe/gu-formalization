#!/usr/bin/env python3
"""Controls for K1506's growing-rate recentering boundary."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1506-growing-rate-recentering.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 r,m,q=D['recentering_boundary'],D['mosco_transfer'],D['decision']
 checks += [('claim',D['claim_id']=='K1506'),('necessary rate','sqrt(log N/log log N)' in r['necessary_scale']),('little-o excluded','=o(' in r['excluded_window']),('epsilon window','c-epsilon' in r['quantitative_failure'] and '-infinity' in r['quantitative_failure']),('weak compactness','weakly convergent subsequences' in m['weak_compactness']),('zero allowed','may be zero' in m['weak_limit']),('liminf contradiction','-infinity' in m['failure'] and 'semibounded' in m['failure']),('BRST transfer','K1471' in m['brst'] and 'harmonic compression' in m['brst']),('necessity proved',q['growing_rate_recentering_necessity_proved']),('Mosco window',q['fixed_gaussian_mosco_weak_liminf_window_excluded']),('BRST window',q['harmonic_brst_window_excluded']),('nonzero fenced',not q['nonzero_weak_limit_proved']),('recovery fenced',not q['mosco_recovery_proved']),('limit fenced',not q['ground_energy_recentered_limit_proved']),('protected fenced',not q['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
