#!/usr/bin/env python3
"""Controls for K1468's spatial-versus-Lorentz null-order boundary."""
import hashlib,json,math
from pathlib import Path
R=Path(__file__).resolve().parents[2]; D=json.loads((R/'lab/process/k1468-spatial-null-order-boundary.json').read_text()); n=0
def c(l,v):
 global n; assert v,l; n+=1; print(f'PASS {n:02d}: {l}')
for k,p in D['pinned_inputs'].items(): c(f'{k} pin',hashlib.sha256((R/p['path']).read_bytes()).hexdigest()==p['sha256'])
M2=5.0
def vals(K):
 w=math.sqrt(M2+K*K+1); wp=math.sqrt(M2+(K+1)**2+1)
 direct=1+w-wp; phi=2*(M2+1)/((w+K)*(1+w+wp)); n0=(M2+1)/(w+K)
 exact=direct
 return w,wp,phi,exact,n0
raw=[]; spatial_energy=[]; lorentz_energy=[]
for K in (64,128,256,512):
 w,wp,phi,exact,n0=vals(K); c(f'exact phase {K}',math.isclose(phi,exact,rel_tol=2e-9,abs_tol=2e-14))
 raw.append(1/phi/K**2); spatial_energy.append(1/(w*phi)/K); lorentz_energy.append(n0/(w*phi))
c('raw spatial two-derivative order',abs(raw[-1]-2/(M2+1))<.01)
c('energy-normalized spatial one-derivative order',abs(spatial_energy[-1]-2/(M2+1))<.01)
c('Lorentz same-tier limit',abs(lorentz_energy[-1]-1)<.01)
c('orders improve',abs(lorentz_energy[-1]-1)<abs(lorentz_energy[0]-1))
A,Q=D['null_order_boundary'],D['decision']; c('angular witness','|p cross k|=1' in A['spatial_angular_numerator']); c('Lorentz identity','omega(k)-K' in A['lorentz_numerator'])
c('exact phase proved',Q['exact_near_parallel_phase_order_proved']); c('Lorentz normalized pass',Q['lorentz_null_same_tier_after_energy_normalization'])
for k in ('spatial_angular_null_same_tier_after_one_energy_normalization','full_k1413_current_decomposition_constructed','global_full_pde_flow_constructed','protected_status_change'): c(f'{k} fenced',not Q[k])
c('ceiling preserved','not a no-go' in A['ceiling'])
print(f'RESULT: PASS {n}/{n}')
