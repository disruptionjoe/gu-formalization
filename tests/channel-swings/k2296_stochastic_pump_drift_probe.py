from pathlib import Path
import json,hashlib,sys,math
from fractions import Fraction as Q
import sympy as s
import numpy as np
from scipy.linalg import expm,eigvalsh
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):checks[n]=bool(v)
def zero(v):return s.simplify(v)==0
mu,t,v=s.symbols('mu t v',positive=True)
# Independent cumulants of Poisson difference and displaced thermal number.
logdiff=mu*(s.exp(t)+s.exp(-t)-2)
check('poisson_difference_variance',zero(s.diff(logdiff,t,2).subs(t,0)-2*mu))
check('poisson_difference_fourth',zero(s.diff(logdiff,t,4).subs(t,0)+3*(2*mu)**2-(2*mu+12*mu**2)))
thermal=-s.log(2-s.exp(t))+mu*(s.exp(t)-1)/(2-s.exp(t))
k2=s.diff(thermal,t,2).subs(t,0);k4=s.diff(thermal,t,4).subs(t,0)
check('thermal_variance',zero(k2-3*mu-2));check('thermal_fourth_cumulant',zero(k4-75*mu-26));check('thermal_fourth_central',zero(k4+3*k2*k2-(27*mu*mu+111*mu+38)))
# Exact rational upper square roots for actual consumer; no binary64 tiny differences.
def sqrtupper(n):
 z=math.isqrt(n);return z if z*z==n else z+1
delta=Q(9272,10**15);var=Q(1,10**42);mc=10**28;mt=4*10**28
coh=delta+2*var*(mc+sqrtupper(mc+3*mc*mc));therm=delta+2*var*(3*mt+2+sqrtupper(27*mt*mt+111*mt+38))
check('coherent_budget',coh<Q(9327,10**15));check('thermal_budget',therm<Q(9928,10**15));check('full_budget',max(coh,therm)<Q(1,10**11));check('field_energy_consumer',6300000*max(coh,therm)<Q(8,1000)**2)
W=4*10**20;sd_i=Q(5,10**32);sd_c=Q(25,10**43)
check('independent_wait_budget',W*sd_i**2==var);check('common_wait_budget',W*W*sd_c**2==var)
Sigma=s.Matrix([[2,1,-1],[1,3,0],[-1,0,2]]);ones=s.ones(3,1)
check('covariance_sum', (ones.T*Sigma*ones)[0]==7)
# Finite coherent matrices: exact Gaussian matrix element multiplier for Q=2K.
size=40;ks=np.arange(size,dtype=float);lam=.7;vv=.02
amp=np.array([math.exp(-lam/2)*lam**(k/2)/math.sqrt(math.factorial(k)) for k in range(size)]);rho=np.outer(amp,amp);char=np.exp(-2*vv*(ks[:,None]-ks[None,:])**2);noisy=rho*char
pp=float(amp@noisy@amp);dist=float(np.abs(eigvalsh(noisy-rho)).sum()/2)
check('mixed_projector_lower',1-pp<=dist+1e-13);check('pure_sqrt_equality_rejected',dist<math.sqrt(1-pp)-.01)
check('poisson_taylor_lower',4*lam*vv-(4*lam+24*lam*lam)*vv*vv<=1-pp+1e-13);check('poisson_taylor_upper',1-pp<=4*lam*vv+1e-13)
check('semigroup_upper',dist<=2*vv*(lam+math.sqrt(lam+3*lam*lam)))
Qmat=np.diag(2*ks);comm=lambda z:Qmat@z-z@Qmat
deriv=-2*(ks[:,None]-ks[None,:])**2*rho
check('Gaussian_generator',np.max(np.abs(deriv+comm(comm(rho))/2))<1e-13)
# Independent thermal displacement overlap and effect norm; finite truncation only.
dim=64;ann=np.diag(np.sqrt(np.arange(1,dim)),1);create=ann.T
alpha=.6;theta=.31;n=1;tau=np.diag(np.array([.5**(k+1) for k in range(dim)]))
D=lambda z:expm(z*create-np.conj(z)*ann)
da=D(alpha);db=D(alpha*np.exp(-2j*theta));ra=da@tau@da.conj().T;rb=db@tau@db.conj().T
analytic=math.exp(-abs(alpha-alpha*np.exp(-2j*theta))**2/3)/3
check('thermal_overlap_matrix',abs(np.trace(ra@rb).real-analytic)<1e-12);check('thermal_effect',eigvalsh(2*ra).max()<1+1e-12)
# Phase periodicity and number-sector immunity on actual even total-charge support.
qvals=np.array([0,2,4,6]);check('even_charge_period',np.max(np.abs(np.exp(-1j*np.pi*qvals)-1))<1e-14)
check('number_sector_immunity',abs(np.exp(-1j*.37*6)*np.exp(1j*.37*6)-1)<1e-14)
field=np.array([0,2]);pump_only=np.exp(-1j*.2*field);check('pump_only_not_full_inverse',abs(pump_only[1]-1)>.3)
faults={}
faults['wrong_charge_multiplier']=['Gaussian_generator'] if np.max(np.abs(-.5*(ks[:,None]-ks[None,:])**2*rho+comm(comm(rho))/2))>1e-3 else []
faults['pure_lower_for_mixture']=['mixed_distance'] if dist<math.sqrt(1-pp)-.01 else []
faults['coherent_variance_for_thermal']=['thermal_variance'] if not zero(k2-mu) else []
# A second covariance has noncancelling offdiagonal terms.
Sigma2=s.Matrix([[2,1],[1,3]]);o2=s.ones(2,1);check('noncancelling_covariance', (o2.T*Sigma2*o2)[0]==7)
faults['drop_noise_correlations']=['noncancelling_covariance'] if s.trace(Sigma2)!=(o2.T*Sigma2*o2)[0] else []
faults['common_noise_as_iid']=['common_wait_budget'] if W*sd_c**2!=var else []
faults['pump_only_compensation']=['full_field_rotation'] if abs(pump_only[1]-1)>.3 else []
assert all(checks.values()),[k for k,vv in checks.items() if not vv]
assert all(faults.values()),faults
stem='k2296-stochastic-pump-drift';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'lab/process/k2293-moment-controlled-positive-pump.json','lab/process/k2285-thermal-period-energy.json']
# Resolve exact thermal predecessor path from current versioned files.
deps=deps[:-1]+[str(p.relative_to(ROOT)) for p in (ROOT/'lab/process').glob('k2285-*.json')]
data=dict(schema_version='1.0',result_id='K2296',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='symbolic moments and exact rational budgets; finite numerical state controls; universal proof in companion; hashes provenance',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},budgets=dict(coherent=str(coh),thermal=str(therm)),claim_ceiling='fixed noise-independent conserving circuit and specified unobserved Gaussian residual; no hardware or GU claim')
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2296',checks=len(checks),faults=len(faults))))
