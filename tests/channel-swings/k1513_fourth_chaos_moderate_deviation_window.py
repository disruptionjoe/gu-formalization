#!/usr/bin/env python3
"""Controls for K1513's fourth-chaos moderate-deviation window."""
import hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];D=json.loads((ROOT/'lab/process/k1513-fourth-chaos-moderate-deviation-window.json').read_text())
def main():
 checks=[]
 for name,pin in D['pinned_inputs'].items():checks.append((f'{name} pin',hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest()==pin['sha256']))
 t,s,q=D['literature_theorem'],D['selected_scale'],D['decision']
 checks += [('schema',D['schema_version']=='1.0'),('claim',D['claim_id']=='K1513'),('primary citation','10.1016/j.jfa.2016.01.002' in t['citation']),('theorem','Theorem 5(i)' in t['citation']),('kernel normalization','sqrt(4!) g_N' in t['normalization']),('unit kernel','||h_N||=1' in t['normalization']),('variance','Var(F_N)=4!' in t['normalization']),('three contractions','1<=r<=3' in t['contraction_modulus']),('contraction power','N^(-3/2)' in t['contraction_modulus']),('contraction logs','log N)^4' in t['contraction_modulus']),('alpha','3/7' in t['graph_exponent']),('Delta power','N^(9/14)' in t['deviation_parameter']),('Delta logs','log N)^(-12/7)' in t['deviation_parameter']),('tail side','P(X_N<=-z)' in t['tail_ratio']),('Gaussian tail','Phi(-z)' in t['tail_ratio']),('tail range','Delta_N^(1/3)' in t['tail_ratio']),('cubic error','1+z^3' in t['tail_ratio']),('transfer window','R_N=o(Delta_N^(1/9))' in t['uniform_window']),('factor two','z<=2R_N' in t['uniform_window']),('selected radius','N^(1/14)/(1+log N)' in s['radius']),('strict verification','log N)^(-4/21)' in s['verification']),('beta family','beta<1/14' in s['power_family']),('relative tail',q['relative_left_tail_window_proved']),('polynomial radius',q['polynomial_moderate_deviation_radius_available']),('density fenced',not q['density_ratio_or_local_limit_proved']),('endpoint fenced',not q['endpoint_one_fourteenth_optimal']),('protected fenced',not q['protected_status_change'])]
 for n in (10**28,10**42,10**56):
  L=math.log(n);R=n**(1/14)/(1+L);Delta13=n**(3/14)*(1+L)**(-4/7);checks.append((f'window ratio {n}',R**3/Delta13<1 and R<Delta13))
 checks += [('alpha arithmetic',math.isclose((4+2)/(3*4+2),3/7)),('power arithmetic',math.isclose((3/2)*(3/7),9/14))]
 for i,(label,ok) in enumerate(checks,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(checks)}/{len(checks)}')
if __name__=='__main__':main()
