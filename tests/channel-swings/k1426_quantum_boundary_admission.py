#!/usr/bin/env python3
"""Controls for K1426's quantum-boundary admission replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'lab/process/k1426-quantum-boundary-admission.json').read_text()); n=0
def check(label,value):
 global n
 assert value,label; n+=1; print(f'PASS {n:02d}: {label}')
for key,pin in D['pinned_inputs'].items(): check(f'{key} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
B,Q=D['bridge_census'],D['decision']
check('census sum',B['row_count']==sum(B[k] for k in ('satisfied_count','conditional_count','excluded_count','missing_count')))
check('census exact',(B['row_count'],B['satisfied_count'],B['conditional_count'],B['excluded_count'],B['missing_count'])==(92,65,7,16,4))
check('four satisfied',len(B['new_satisfied_rows'])==4)
check('one conditional',len(B['new_conditional_rows'])==1)
check('one excluded',len(B['new_excluded_rows'])==1)
check('four missing',len(B['missing_rows'])==4)
for key in ('finite_cylindrical_positive_quantum_control_constructed','stratum_compatible_compact_projection_constructed','closed_gauge_fixed_brst_hilbert_complex_constructed','positive_interacting_finite_block_hamiltonian_constructed','bare_noncompact_gauge_volume_obstruction_proved'): check(key,Q[key])
for key in ('continuum_quantum_physical_hilbert_cohomology_constructed','completed_full_pde_global_flow_constructed','source_selected_reduction_constructed','k1145_k1150_candidate_counts_move','protected_status_change'): check(f'{key} fenced',not Q[key])
check('ledger unchanged','LEDGER_UNCHANGED' in D['source_and_ledger_effect'])
print(f'RESULT: PASS {n}/{n}')
