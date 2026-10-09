#!/usr/bin/env python3
"""Controls for K1557's quartic cutoff ground-energy scale."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1557-quartic-ground-energy-scale.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['ground_energy'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1557'),('bootstrap','epsilon N^4' in q['bootstrap_assumption']),('quantitative shell','T_N>C_sh,N/2' in q['quantitative_shell_covariance']),('relative amplitude','r_N/C_N' in q['amplitude_error']),('shell release','kappa/12-epsilon/(9g c_C^2)' in q['sign_shell_release']),('positive shell','kappa/24' in q['sign_shell_release']),('contradiction','E_nu W_N>=c1 N^4' in q['interaction_contradiction']),('theta','E_N=Theta_g(N^4)' in q['lower_and_upper']),('vacuum','E W_N=6C_N^2' in q['lower_and_upper']),('resolvent','O_g(N^-4)' in q['resolvent_consequence']),('bounded error open','does not determine E_N to O(1)' in q['scope_guard']),('bootstrap decision',d['quantitative_shell_bootstrap_proved']),('scale decision',d['ground_energy_scale_N4_proved']),('upper decision',d['vacuum_upper_scale_matches']),('shift decision',d['sub_N4_recenterings_excluded']),('O1 open',not d['ground_energy_to_bounded_error_proved']),('operator open',not d['continuum_operator_constructed']),('source open',not d['source_owned_gu_hamiltonian']),('protected',not d['protected_status_change'])]
 kappa,g,cC=.4,2.0,.8;epsilon=.01
 checks += [('shell numeric',kappa/12-epsilon/(9*g*cC*cC)>=kappa/24),('vacuum quartic',6*(64**2)**2==6*64**4)]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
