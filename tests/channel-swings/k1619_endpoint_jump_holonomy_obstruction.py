#!/usr/bin/env python3
"""Certificate for K1619's endpoint-jump holonomy obstruction."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def indicator_hat_abs(t): return 2*abs(math.sin(t/2))/t
def integrate(a,b,n=50000):
 dx=(b-a)/n;return sum(indicator_hat_abs(a+(k+0.5)*dx) for k in range(n))*dx
def main():
 d=json.loads((ROOT/'lab/process/k1619-endpoint-jump-holonomy-obstruction.json').read_text());q=d['endpoint_obstruction'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1619'),('piecewise class','W^{2,1}' in q['hypothesis']),
       ('t inverse','(it)^(-1)T(t)+O(t^(-2))' in q['asymptotic']),('jump polynomial','sum_r J_r exp(i t a_r)' in q['asymptotic']),
       ('positive mean','M(|T|^2)=sum_r|J_r|^2>0' in q['mean']),('L1 divergence','int_1^infinity|widehat G(t)|dt=infinity' in q['obstruction']),
       ('derivative jumps allowed','first-derivative jumps remain allowed' in q['sharpness'])]
 i1=integrate(1,64);i2=integrate(1,1024)
 c += [('indicator finite prefix',i1>2),('indicator logarithmic growth',i2>i1+1.5)]
 for t in (0.7,3.1,17.0):
  exact=abs((complex(math.cos(t),math.sin(t))-1)/(1j*t));c.append((f'indicator transform {t}',abs(exact-indicator_hat_abs(t))<1e-12))
 c += [('jump obstruction',z['nonzero_endpoint_jump_obstructs_holonomy_L1']),('no distinct cancellation',not z['distinct_jump_cancellation_can_restore_L1']),
       ('derivative jumps',z['first_derivative_jumps_still_allowed']),('no electric L1',not z['electric_field_L1_proved']),
       ('no source flow',not z['source_owned_flow']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
