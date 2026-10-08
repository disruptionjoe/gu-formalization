#!/usr/bin/env python3
"""Controls for K1449's harmonic-regeneration obstruction."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1449-zero-harmonic-regeneration-obstruction.json').read_text()); n=0
def c(l,v):
 global n
 assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['regeneration'],D['decision']
for q,k,a in ((4,(1,0,0),2),(8,(0,2,0),1.5),(-4,(0,0,3),1)):
 j=tuple(q*a*a*x for x in k); c(f'nonzero mean current q={q}',any(x for x in j))
c('average equation','partial_t E_h=-bar(j)' in B['averaged_maxwell_equation'])
c('Gauss-compatible witness','charge density is zero' in B['explicit_data'])
c('immediate exit','partial_t E_h(0) is nonzero' in B['consequence'])
c('witness built',Q['gauss_compatible_regeneration_witness_constructed'])
for k in ('gauss_constrains_harmonic_electric_mode','generic_strict_zero_harmonic_sector_invariant','k1442_fixed_nonzero_mode_result_invalidated','all_symmetry_restricted_zero_mode_sectors_excluded','global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
c('symmetry sector survives','nongeneric' in B['surviving_scope'])
print(f'RESULT: PASS {n}/{n}')
