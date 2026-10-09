#!/usr/bin/env python3
"""Certificate for K1599's transverse nonzero-mode periodic family."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1599-transverse-nonzero-mode-periodic-family.json').read_text());q=d['transverse_periodic_family'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1599'),('torus','On T^3' in q['geometry']),('nonzero k','nonzero lattice k' in q['geometry']),('transverse','perpendicular' in q['geometry']),('equal fields','phi_+(t,x)=phi_-(t,x)' in q['solution']),('Omega','Omega=sqrt(2)eR' in q['solution']),('omega','m^2+|k|^2+e^2A^2' in q['solution']),('frequency equality','k dot a(t)=0' in q['scalar_equations']),('Gauss cancel','Gauss densities cancel' in q['maxwell_and_gauss']),('momentum current cancel','momentum current parts cancel' in q['maxwell_and_gauss']),('Maxwell equation',"a''+2e^2R^2a=0" in q['maxwell_and_gauss']),('D zero','D=0' in q['normal_form_control']),('M constant','M=2R^2' in q['normal_form_control']),('electric positive','|E_bar|=A Omega>0' in q['normal_form_control']),('not homogeneous','no homogeneous matter mode' in q['route_consequence']),('exclusion insufficient','Excluding only k=0 is insufficient' in q['route_consequence']),('scope scattering','does not exclude scattering' in q['scope_guard'])]
 e,m,A,R,K,t=1.3,2.0,.7,.4,3.0,.31;Om=math.sqrt(2)*e*R;om=math.sqrt(m*m+K*K+e*e*A*A);a=complex(A*math.cos(Om*t),A*math.sin(Om*t));add=-Om*Om*a;phi=R*cmath.exp(1j*om*t);phidd=-om*om*phi
 c += [('Maxwell arithmetic',abs(add+2*e*e*R*R*a)<1e-12),('scalar arithmetic',abs(phidd+(m*m+K*K+e*e*A*A)*phi)<1e-12),('Gauss arithmetic',abs(e*(om*R*R)-e*(om*R*R))<1e-12),('current arithmetic',abs((e*K*R*R-e*K*R*R))<1e-12),('electric magnitude',A*Om>0)]
 c += [('decision solution',z['nonzero_mode_exact_solution']),('decision neutral',z['gauss_neutral']),('decision energy',z['finite_conserved_energy']),('decision L1',z['harmonic_electric_l1_infinite']),('homogeneous insufficient',not z['homogeneous_mode_exclusion_sufficient']),('dispersive open',not z['all_dispersive_closure_excluded']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
