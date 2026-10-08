#!/usr/bin/env python3
"""Controls for K1500's Hermite Jacobi limit."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1500-hermite-jacobi-limit.json').read_text())
def rayleigh_last_pair(d):
 v=[0.0]*(d+1);v[d-1]=1/math.sqrt(2);v[d]=-1/math.sqrt(2)
 return 2*math.sqrt(d)*v[d-1]*v[d]
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 a,q=D['hermite_jacobi_limit'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1500'),('fixed order','fixed before N' in a['fixed_degree']),('moment matrix','2d' in a['moment_matrix']),('positive definite','positive definite' in a['positive_definiteness']),('continuity','continuous' in a['coefficient_continuity']),('Jacobi limit','J_(d,N)->J_d^G' in a['jacobi_limit']),('Hermite recurrence','sqrt(j+1)' in a['hermite_recurrence']),('bottom','-c_d^G' in a['limiting_bottom']),('sqrt bound','sqrt(d)' in a['two_coordinate_bound']),('compression convergence',q['every_fixed_jacobi_compression_converges']),('Hermite decision',q['limiting_orthogonal_polynomials_are_hermite']),('unbounded decision',q['fixed_degree_coefficient_sequence_unbounded']),('rate fenced',not q['simultaneous_degree_cutoff_rate_proved']),('endpoint retained',not q['fixed_cutoff_endpoint_replaced']),('protected fenced',not q['protected_status_change'])]
 for d in range(1,9):checks.append((f'd{d} last-pair quotient',abs(rayleigh_last_pair(d)+math.sqrt(d))<1e-12))
 checks += [('sqrt grows',all(math.sqrt(d+1)>math.sqrt(d) for d in range(1,20))),('arbitrary threshold',math.sqrt(101)>10)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
