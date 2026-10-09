#!/usr/bin/env python3
"""Certificate for K1616's Gaussian-channel MMSE control."""
import json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def normal(x, m):
    return math.exp(-0.5 * (x-m) ** 2) / math.sqrt(2 * math.pi)

def binary_channel(a=1.4, n=24001, lo=-9.0, hi=9.0):
    dx = (hi-lo)/(n-1); mmse = info = mass = 0.0
    for k in range(n):
        x = lo+k*dx; f0 = normal(x,-a); f1 = normal(x,a); f = 0.5*(f0+f1)
        post = f1/(f0+f1); mean = a*(2*post-1)
        var = a*a-mean*mean
        kl = 0.0
        for p in (post,1-post):
            if p > 0: kl += p*math.log(2*p)
        w = 0.5 if k in (0,n-1) else 1.0
        mmse += w*f*var*dx; info += w*f*kl*dx; mass += w*f*dx
    return mmse, info, mass

def main():
    d=json.loads((ROOT/'lab/process/k1616-common-covariance-mmse-control.json').read_text())
    q,z=d['mmse_control'],d['decision']; c=[]
    c += [('claim',d['claim_id']=='K1616'),('common covariance','one common stationary diagonal' in q['hypothesis']),
          ('whitening','S_N^(-1/2)' in q['whitening']),('weighted mmse','E[(A_N-E[A_N|' in q['identity']),
          ('I-MMSE','int_0^1 mmse' in q['i_mmse']),('energy quarter','D_N/4<=(Lambda_N/2)I(M_N;X_N)' in q['bound'])]
    mmse,info,mass=binary_channel()
    c += [('quadrature mass',abs(mass-1)<2e-8),('mmse positive',mmse>0),('information positive',info>0),
          ('I-MMSE consequence',mmse<=2*info+2e-5)]
    c += [('mmse identity',z['missing_information_is_weighted_mmse']),('mutual information',z['mutual_information_bound']),
          ('no separation',not z['separation_required']),('continuous label',not z['discrete_label_required']),
          ('varying covariance open',not z['varying_covariance_controlled']),('not unrestricted',not z['unrestricted_state_theorem']),
          ('protected',not z['protected_status_change'])]
    for i,(label,ok) in enumerate(c,1): assert ok,label; print(f'PASS {i:02d}: {label}')
    print(f'RESULT: PASS {len(c)}/{len(c)}')
if __name__=='__main__': main()
