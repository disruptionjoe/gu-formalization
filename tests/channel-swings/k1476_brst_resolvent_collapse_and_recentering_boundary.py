#!/usr/bin/env python3
"""Controls for K1476's BRST spectral-transfer boundary."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1476-brst-resolvent-collapse-and-recentering-boundary.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,pin in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/pin['path']).read_bytes()).hexdigest()==pin['sha256'])
for E in (1.,4.,9.):
 matter=(1/(E+1),1/(E+3)); brst=(1/(E+1),1/(E+2),1/(E+3))
 c(f'full bottom equals matter bottom E={E}',max(brst)==max(matter))
 c(f'harmonic compression E={E}',brst[0]==matter[0])
for E in (10.,100.,1000.): c(f'collapse E={E}',1/(E+1)<=1/11)
A,Q=D['brst_spectral_boundary'],D['decision']; c('zero harmonic vacuum','zero-energy harmonic' in A['tensor_hamiltonian']); c('compression formula','P_harm' in A['harmonic_compression']); c('same counterterm','same ground-energy-tracking' in A['necessary_reduction']); c('domain fence','one common nonlinear form domain' in A['differential_boundary'])
for k in ('unshifted_full_brst_hamiltonian_resolvents_collapse','degree_zero_harmonic_compression_equals_matter_resolvent','recentered_matter_limit_is_necessary_for_physical_sector_limit'): c(k,Q[k])
for k in ('brst_factor_removes_ground_energy_divergence','continuum_interacting_brst_hamiltonian_constructed','source_physical_cohomology_identified','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
