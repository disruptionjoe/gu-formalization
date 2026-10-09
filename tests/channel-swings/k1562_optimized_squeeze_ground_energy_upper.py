#!/usr/bin/env python3
"""Controls for K1562's optimized squeeze upper coefficient."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1562-optimized-squeeze-ground-energy-upper.json').read_text())
ELL=math.log((1+math.sqrt(3))/math.sqrt(2));C_C=12*ELL-math.pi;C_O=2*math.sqrt(3)+8*ELL-math.pi/3
def e(g,s):return C_O/4*(s+1/s-2)+6*g*C_C**2*s*(2-s)
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 q,d=D['optimized_upper'],D['decision'];gc=C_O/(24*C_C**2)
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1562'),('factor','c_Omega/(4s)-6g c_C^2' in q['vacuum_difference']),('threshold','c_Omega/(24c_C^2)' in q['threshold']),('root','48g c_C^2 s_g^2=c_Omega(s_g+1)' in q['interior_minimizer']),('optimized coefficient','h_g=c_Omega(s_g^2-3s_g+4)/(8s_g)' in q['optimized_coefficient']),('limsup','limsup_' in q['limsup']),('corridor','positive finite quartic coefficient corridor' in q['composition']),('scope','not a phase transition of the full theory' in q['scope_guard']),('factor decision',d['vacuum_difference_factorized']),('threshold decision',d['family_threshold_proved']),('root decision',d['interior_minimizer_proved']),('limsup decision',d['explicit_ground_energy_limsup_proved']),('vacuum not sharp',not d['vacuum_coefficient_unrestricted_upper_sharp_for_large_g']),('convergence open',not d['ground_energy_ratio_convergence_proved']),('Mosco open',not d['mosco_limit_constructed']),('protected',not d['protected_status_change']),('threshold numeric',abs(gc-.0141310864013)<1e-13)]
 for g in (gc*1.1,gc*2,1.0):
  s=(C_O+math.sqrt(C_O**2+192*g*C_C**2*C_O))/(96*g*C_C**2)
  checks += [(f'root inside {g}',0<s<1),(f'strict upper {g}',e(g,s)<e(g,1))]
 checks.append(('subthreshold vacuum',all(e(gc*.5,s)>=e(gc*.5,1)-1e-12 for s in (.1,.25,.5,.75,1))))
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
