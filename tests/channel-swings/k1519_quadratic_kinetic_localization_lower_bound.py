#!/usr/bin/env python3
"""Controls for K1519's many-chaos localization lower bound."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1519-quadratic-kinetic-localization-lower-bound.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['localization_lower_bound'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1519'),('event','exp(-cN^2)' in q['event']),('binary entropy','binary data processing' in q['entropy_contraction']),('log delta','log(1/delta_N)' in q['entropy_contraction']),('Gross','Gross inequality' in q['log_sobolev']),('gap','omega>=omega0>0' in q['log_sobolev']),('kinetic N2','=Omega(N^2)' in q['dichotomy']),('half mass','m_N<=1/2' in q['dichotomy']),('potential N4','Theta(N^4)' in q['dichotomy']),('fixed coupling','fixed g>0' in q['energy_boundary']),('energy N2','c_g N^2' in q['energy_boundary']),('all states','every normalized vector' in q['many_chaos_scope']),('decision N2',d['unshifted_ground_energy_lower_order']=='N^2'),('log superseded',d['logarithmic_lower_boundary_superseded']),('many chaos',d['many_chaos_lower_boundary_proved']),('upper fenced',not d['matching_upper_bound_proved']),('asymptotic fenced',not d['ground_energy_asymptotic_determined']),('profile fenced',not d['localization_profile_determined']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
