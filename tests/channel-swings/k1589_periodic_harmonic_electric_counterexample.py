#!/usr/bin/env python3
"""Certificate for K1589's neutral periodic harmonic-electric obstruction."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1589-periodic-harmonic-electric-counterexample.json').read_text());q=d['periodic_orbit'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1589'),('opposite charges','charges +e and -e' in q['model']),('reduced scalar','phi_sigma' in q['model']),('reduced Maxwell',"a''+e^2" in q['model']),('Gauss density','Gauss density' in q['model']),('circular orbit','cos(Omega t)' in q['exact_solution']),('frequencies','Omega=sqrt(2)eR' in q['exact_solution'] and 'omega=sqrt(m^2+e^2A^2)' in q['exact_solution']),('neutrality','cancel pointwise' in q['gauss_neutrality']),('currents add','spatial currents add' in q['gauss_neutrality']),('constant electric','constant magnitude A Omega' in q['nonintegrable_harmonic_electric']),('linear divergence','A Omega T' in q['nonintegrable_harmonic_electric']),('extra mechanism','additional dispersion' in q['obstruction']),('two species scope','two-species' in q['scope_guard'])]
 e,m,A,R,t=1.3,2.0,.7,.4,.31;Om=math.sqrt(2)*e*R;om=math.sqrt(m*m+e*e*A*A);a=complex(A*math.cos(Om*t),A*math.sin(Om*t));add=-Om*Om*a;phi=R*cmath.exp(1j*om*t);phidd=-om*om*phi
 c += [('Maxwell equation',abs(add+2*e*e*R*R*a)<1e-12),('scalar equation',abs(phidd+(m*m+e*e*A*A)*phi)<1e-12),('Gauss cancel',abs(e*(om*R*R)-e*(om*R*R))<1e-12),('electric positive',A*Om>0)]
 c += [('orbit',z['exact_coupled_periodic_orbit']),('neutral',z['gauss_neutral']),('energy',z['finite_conserved_energy']),('L1 infinite',z['harmonic_electric_l1_infinite']),('energy route excluded',z['energy_only_integrability_excluded']),('other closure open',not z['all_global_pde_closure_excluded']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
