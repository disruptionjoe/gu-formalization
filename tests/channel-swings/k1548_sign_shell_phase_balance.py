#!/usr/bin/env python3
"""Controls for K1548's universal sign-shell phase balance."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1548-sign-shell-phase-balance.json').read_text())
def main():
 q,d=D['phase_balance'],D['decision'];checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1548'),('T3','normalized T3' in q['definitions']),('cutoff','|k|_2<=N' in q['definitions']),('tail norm','||s_N-f_N||_2^2<=delta_N' in q['tail_bridge']),('tail projection','|k|_2>N' in q['tail_bridge']),('variance','4p_N(1-p_N)' in q['variance_bridge']),('phase eta','eta/4' in q['phase_floor']),('bad density','9/16' in q['good_core']),('core eta','eta/8' in q['good_core']),('capacity fenced','does not by itself' in q['scope_guard']),('tail decision',d['universal_tail_bound_proved']),('balance decision',d['shell_phase_balance_proved']),('core decision',d['macroscopic_core_phases_proved']),('exponent open',not d['transition_defect_exponent_proved']),('capacity open',not d['capacity_computed']),('protected',not d['protected_status_change'])]
 for eta in (.1,.4,.8):
  p=eta/4;checks.append((f'phase algebra eta={eta}',4*p*(1-p)>=eta*(1-eta/4)))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
