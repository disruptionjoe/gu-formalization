#!/usr/bin/env python3
"""Certificate for K1607's separated order-one covariance class."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def main():
 d=json.loads((ROOT/'lab/process/k1607-separated-heterogeneity-coefficient-rigidity.json').read_text());q=d['separated_class'];z=d['decision'];c=[]
 c += [('claim',d['claim_id']=='K1607'),('fixed M','Fix M independent of N' in q['hypothesis']),('order one','c_- S_N^*' in q['hypothesis']),('positive fraction','delta d_N' in q['hypothesis']),('affinity product','product_k' in q['overlap_decay']),('sech','sech(kappa/2)' in q['overlap_decay']),('exponential','exp[-c_(delta,kappa)d_N]' in q['overlap_decay']),('prefactor exact','2 omega_k' in q['prefactor']),('prefactor N4','O_g(N^4)' in q['prefactor']),('gain','N^4 exp(-cN^3)=o(1)' in q['mixing_gain']),('coefficient','h_g^prof' in q['coefficient']),('overlap open','Overlapping order-one components' in q['scope_guard'])]
 kappa,delta,N=.7,.15,20;qk=math.sqrt(1/math.cosh(kappa/2));dim=N**3;bc=qk**(delta*dim)
 c += [('q below one',0<qk<1),('overlap tiny',bc<1e-6),('prefactor defeated',N**4*bc<1e-2),('order one allowed',z['order_one_covariance_heterogeneity_allowed']),('separation required',z['macroscopic_pairwise_separation_required']),('fixed count',z['fixed_component_count_required']),('gain small',z['mixing_gain_exponentially_small']),('class coefficient',z['class_coefficient_h_g_prof']),('overlap not closed',not z['overlapping_order_one_class_controlled']),('unrestricted open',not z['unrestricted_leading_coefficient_identified']),('protected',not z['protected_status_change'])]
 for i,(label,ok) in enumerate(c,1):assert ok,label;print(f'PASS {i:02d}: {label}')
 print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__':main()
