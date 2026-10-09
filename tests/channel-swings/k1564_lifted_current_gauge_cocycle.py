#!/usr/bin/env python3
"""Controls for K1564's lifted-current gauge cocycle."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1564-lifted-current-gauge-cocycle.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['gauge_cocycle'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1564'),('density','rho_n=e Im' in q['density']),('continuity','partial_t rho_n+div j_n=0' in q['continuity']),('residual','time-independent residual temporal-gauge' in q['residual_gauge']),('matching phase','matching charge phase' in q['residual_gauge']),('cocycle','d/dt int chi rho_n' in q['boundary_cocycle']),('consequence','fix the residual gauge' in q['consequence']),('scope','does not control int A dot partial_t j_n' in q['scope_guard']),('large-gauge guard','large non-single-valued' in q['scope_guard']),('continuity decision',d['lifted_current_continuity_proved']),('cocycle decision',d['residual_gauge_cocycle_proved']),('not invariant',not d['instantaneous_gauge_invariance_proved']),('completion',d['spacetime_boundary_completion_required']),('current open',not d['differentiated_current_controlled']),('gauge open',not d['global_gauge_fixed']),('flow open',not d['global_full_pde_flow_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
