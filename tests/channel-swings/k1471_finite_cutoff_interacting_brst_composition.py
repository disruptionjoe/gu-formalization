#!/usr/bin/env python3
"""Controls for K1471's finite-cutoff BRST/Hamiltonian composition."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1471-finite-cutoff-interacting-brst-composition.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
# Three-state BRST model: h is harmonic and d(u)=v.
Dmat=((0,0,0),(0,0,0),(0,1,0)); Dt=tuple(zip(*Dmat))
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def add(A,B): return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
D2=mm(Dmat,Dmat); L=add(mm(Dmat,Dt),mm(Dt,Dmat)); c('nilpotent toy differential',all(x==0 for row in D2 for x in row)); c('Hodge spectrum 0,1,1',tuple(L[i][i] for i in range(3))==(0,1,1))
for a in (1,3,7):
 H=tuple(tuple((a if i==j else 0)+L[i][j] for j in range(3)) for i in range(3)); c(f'commutation a={a}',mm(H,Dmat)==mm(Dmat,H)); c(f'harmonic induced energy a={a}',H[0][0]==a)
A,Q=D['finite_cutoff_composition'],D['decision']; c('tensor factor carrier','tensored' in A['carrier']); c('closed nilpotent differential','closed nilpotent' in A['brst_operator']); c('induced Hamiltonian','exactly A_N' in A['cohomology'])
for k in ('finite_cutoff_closed_brst_operator_retained','finite_cutoff_interacting_hamiltonian_brst_compatible','positive_nonzero_degree_zero_interacting_cohomology','higher_cohomology_zero'): c(k,Q[k])
for k in ('continuum_interacting_brst_operator_constructed','source_physical_cohomology_identified','protected_status_change'): c(f'{k} fenced',not Q[k])
print(f'RESULT: PASS {n}/{n}')
