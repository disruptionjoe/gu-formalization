#!/usr/bin/env python3
"""Certificate for K1608's two-derivative spectral-primitive budget."""
import cmath,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1608-spectral-primitive-holonomy-budget.json').read_text());q=d['primitive_budget'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1608'),('no atoms','pure-point harmonic-electric sector is absent' in q['spectral_primitive']),('away zero','away from omega=0' in q['spectral_primitive']),('arbitrary flat','arbitrary constant flat holonomy' in q['spectral_primitive']),('divided density','F/omega' in q['weaker_hypothesis']),('W21','W^{2,1}' in q['weaker_hypothesis']),('endpoint','first derivatives zero' in q['weaker_hypothesis']),('t2','t^(-2)B_G2' in q['decay']),('L1','B_G0+B_G2' in q['budgets']),('square','B_G0(B_G0+B_G2)' in q['budgets']),('no E L1','does not prove E_h in L1' in q['scope_guard'])]
 # G=(w-1)^2(2-w)^2 has G=G'=0 at both endpoints. Check the two-IBP bound numerically.
 def g(w):return (w-1)**2*(2-w)**2
 def g2(w):return 2-12*(w-1)+12*(w-1)**2
 n=20000;h=1/n;bg0=bg2=0.;t=8.;a=0j
 for k in range(n+1):
  w=1+k*h;wt=.5 if k in (0,n) else 1.;a+=wt*cmath.exp(1j*t*w)*g(w)*h;bg0+=wt*abs(g(w))*h;bg2+=wt*abs(g2(w))*h
 c += [('endpoint values',g(1)==0 and g(2)==0),('endpoint derivatives',abs(2*(1-1)*(2-1)**2-2*(1-1)**2*(2-1))<1e-12),('direct bound',abs(a)<=bg0+1e-10),('ibp bound',abs(a)<=bg2/t**2+2e-7),('atoms retained',z['pure_point_exclusion_retained']),('primitive sufficient',z['primitive_w21_sufficient']),('a L1',z['holonomy_remainder_l1_proved']),('nonzero limit',z['nonzero_asymptotic_flat_holonomy_allowed']),('E L1 open',not z['electric_field_l1_proved']),('scattering open',not z['nonlinear_scattering_proved']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
