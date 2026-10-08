#!/usr/bin/env python3
"""Controls for K1521's recentering corridor and BRST transfer."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1521-two-sided-recentering-corridor.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['recentering_corridor'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1521'),('lower bracket','c_g N^2<=E_N' in q['ground_energy_bracket']),('upper bracket','6gC_N^2-(1-o(1))g sigma_N R_N' in q['ground_energy_bracket']),('radius','N^(1/14)/(1+log N)' in q['ground_energy_bracket']),('low plus','plus infinity' in q['low_side']),('high minus','minus infinity' in q['high_side']),('surviving','nonmatching corridor' in q['surviving_corridor']),('exact shift open','E_N+O(1) remains unresolved' in q['surviving_corridor']),('tensor','mathbb H_N=H_N tensor 1' in q['brst_transfer']),('harmonic','P_harm' in q['brst_transfer']),('no continuum BRST','without constructing a continuum interacting BRST charge' in q['brst_transfer']),('corridor proved',d['two_sided_recentering_corridor_proved']),('mechanisms distinct',d['low_and_high_exclusion_mechanisms_distinct']),('transfer',d['harmonic_brst_transfer_proved']),('not matching',not d['corridor_endpoints_match']),('shift open',not d['ground_energy_shift_identified']),('Mosco fenced',not d['mosco_compactness_or_recovery_proved']),('BRST fenced',not d['interacting_continuum_brst_constructed']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
