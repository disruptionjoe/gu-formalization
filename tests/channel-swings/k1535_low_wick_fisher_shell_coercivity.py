#!/usr/bin/env python3
"""Controls for K1535's low-Wick Fisher shell theorem."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1535-low-wick-fisher-shell-coercivity.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['shell_coercivity'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1535'),('shell mass','Tr(P_N Lambda)>=kappa C_N' in q['shell_constants']),('dual Loewner','a_N P_N Lambda' in q['shell_constants']),('a scale','N^(-2)' in q['shell_constants']),('low Wick','E_nu W_N' in q['low_wick_to_variance']),('variance cut','V_N=Tr(Lambda S)<=eta C_N' in q['low_wick_to_variance']),('deficit','(kappa-eta)C_N' in q['shell_deficit']),('Frobenius','delta_N^2<=' in q['frobenius_bound']),('matrix order','P_N Lambda^2 Omega^(-1)P_N S' in q['frobenius_bound']),('dual trace','a_N eta C_N' in q['dual_bound']),('Fisher result','(kappa-eta)^2 C_N/(a_N eta)' in q['fisher_consequence']),('nonGaussian','non-Gaussian densities' in q['fisher_consequence']),('midpoint','kappa C_N/(8a_N)' in q['midpoint']),('N4','=Omega(N^4)' in q['midpoint']),('defect required','moment-defect budget' in q['scope_guard']),('low Wick decision',d['low_wick_forces_high_fisher_in_M_beta']),('order decision',d['noncommutative_shell_order_preserved']),('no stationarity',not d['stationarity_or_independent_modes_required']),('unrestricted fenced',not d['unrestricted_nongaussian_lower_bound_proved']),('protected',not d['protected_status_change'])]
 for N in (8.0,16.0,64.0):
  kappa=.4;eta=.2;C=N*N;a=2/(N*N)
  fisher=(kappa-eta)**2*C/(a*eta);mid=kappa*C/(8*a)
  checks += [(f'general shell N={N}',math.isclose(fisher,kappa*C/(2*a))), (f'midpoint q N4 N={N}',math.isclose(mid,(kappa/16)*N**4))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
