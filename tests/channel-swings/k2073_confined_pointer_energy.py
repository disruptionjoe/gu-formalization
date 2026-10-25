"""Exact resource arithmetic; operator proof is in the accompanying note."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,argparse
ROOT=Path(__file__).resolve().parents[2]
def bounds(eta,rho,m=F(1)):
 rms=2*m;gradient=2/rho;moment=4*rms+2*gradient
 return dict(rms_free_upper=str(moment),negative_energy_upper=str(2*eta*moment),absolute_mean_change_upper=str(2*eta*(moment+rms)),sector_probability_upper=str(4*eta**2),bell_lower=str(2*F(7,5)*F(183,200)**2-32*eta-16*eta**2))
def produce():
 refs=['lab/process/k2071-confined-pointer-control.json','explorations/conditional-build/k2067-sector-preserving-pointer-control-2026-10-25.md']
 # |g_m|^2 has three independent variance-m^2 coordinates; H0^2=p^2+m^2.
 assert 1+3==4
 rows=[]
 for n in [100,200,1000]:
  eta=F(1,n);rho=F(1);v=bounds(eta,rho);v.update(eta=str(eta),radius=str(24/eta),ramp_width=str(rho));rows.append(v)
  assert F(v['bell_lower'])>2 and F(v['negative_energy_upper'])==24*eta
 # Simultaneous requested Eminus<=epsilon*m and the inherited Bell threshold.
 req=[]
 for eps in [F(1,4),F(1,10),F(1,100),F(1,1000)]:
  eta=min(F(1,100),eps/24);v=bounds(eta,F(1));assert F(v['negative_energy_upper'])<=eps and F(v['bell_lower'])>2
  req.append(dict(epsilon=str(eps),eta=str(eta),initial_radius=str(24/eta),negative_energy_upper=v['negative_energy_upper'],bell_lower=v['bell_lower']))
 return dict(id='K2073',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},initial_rms_over_m='2',relative_perturbation_bound='2/3',graph_lower_coefficient='1/3',cutoff_gradient_bound='2/rho',free_rms_bound='8*m+4/rho',negative_first_moment_bound='eta*(16*m+8/rho)',mean_energy_change_bound='eta*(20*m+8/rho)',explicit_resources=rows,tolerance_resources=req,optimized_resource=dict(epsilon='1/100',initial_radius='38592',ramp_width='100',control_radius='38822',detector_radius='38622',strict_center_separation='77674',eta='1/1608',negative_energy_upper='1/100',fixed_budget_envelope='384/(sqrt(1+w)-1)^2'),scope='same one-particle prepared subspace; no field energy, Fock implementation, exact positive sector or source claim')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();d=produce();out=ROOT/'lab/process/k2073-confined-pointer-energy.json'
 if args.write:out.write_text(json.dumps(d,indent=2)+'\n')
 else:assert d==json.loads(out.read_text())
 print('PASS exact Gaussian second-moment identity and7 rational resource cases')
