#!/usr/bin/env python3
"""Controls for K1445's graph-equivalent dressing obstruction."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1445-unitary-dressing-form-obstruction.json').read_text()); n=0
def c(label,v):
 global n
 assert v,label; n+=1; print(f'PASS {n:02d}: {label}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
B,Q=D['dressing_boundary'],D['decision']
for needle in ('A^(1/2)U_NA^(-1/2)','U_N^(-1)'): c(f'graph hypothesis {needle}',needle in B['admitted_dressing'])
c('pullback names inverse', 'U_N^(-1)' in B['pullback_argument'])
c('K1439 contradiction','K1439' in B['contradiction'] and 'N^2' in B['contradiction'])
c('regular dressing excluded',Q['graph_equivalent_unitary_dressing_excluded'])
c('inverse bound required',Q['inverse_graph_bound_required'])
for k in ('singular_dressing_excluded','all_changed_domain_routes_excluded','source_hamiltonian_identified','protected_status_change'): c(f'{k} fenced',not Q[k])
c('singular ceiling','Singular dressings' in B['ceiling'])
print(f'RESULT: PASS {n}/{n}')
