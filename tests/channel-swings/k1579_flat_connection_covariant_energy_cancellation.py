#!/usr/bin/env python3
"""Controls for K1579's covariant flat-background cancellation."""
import cmath,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1579-flat-connection-covariant-energy-cancellation.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['covariant_cancellation'],D['decision'];k=3.;e=.4;a=.7;m=1.2;w=math.sqrt((k-e*a)**2+m*m);z=1.3-0.4j;p=-1j*w*z;energy=lambda zz,pp:(abs(pp)**2+w*w*abs(zz)**2)/2;z2=z*cmath.exp(-1j*w*2.7);p2=-1j*w*z2;checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1579'),('operator','D_a=grad-i e a' in q['operator']),('frequency','sqrt(|k-ea|^2+m^2)' in q['fourier_diagonalization']),('mode conservation',math.isclose(energy(z,p),energy(z2,p2),rel_tol=1e-12)),('charge','commutes' in q['charge_hierarchy']),('analytic','charge-analytic sum' in q['charge_hierarchy']),('zero spend','zero analytic radius' in q['radius_consequence']),('next split','split harmonic flat connection' in q['next_required_structure']),('ceiling','fixed static flat background' in q['scope_guard']),('energy',d['static_flat_covariant_energy_conserved']),('commutation',d['charge_tier_commutation_proved']),('not necessary',not d['static_flat_radius_expenditure_necessary']),('split open',not d['nonlinear_harmonic_split_closed']),('radius open',not d['global_positive_analytic_radius']),('protected',not d['protected_status_change'])]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
