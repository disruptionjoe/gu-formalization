from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as R
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(name,value): checks[name]=bool(value)
def verify_prior(path):
 data=json.loads((ROOT/path).read_text())
 for p,h in data['dependencies'].items():check('hash_'+p,hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h)
 return data
def finish(stem,deps,faults,extra):
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 assert all(faults.values()),faults
 paths=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),*deps]
 data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied models; no GU empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='exact rational identities/bounds and outward Arb interval bound; finite matrix and Poisson overlap controls numerical; hashes provenance only; universal proofs in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
 out=ROOT/'lab/process'/f'{stem}.json'
 if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(out.read_text())==data,'stored report stale'
 print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

import numpy as np
from scipy.linalg import expm
from math import sqrt,exp,sin,factorial
stem='k2293-moment-controlled-positive-pump'
deps=['lab/process/k2290-local-positive-pump.json','lab/process/k2281-thermal-pump-preparation.json','lab/process/k2279-uniform-pump-energy.json']
for dep in deps:verify_prior(dep)
def matrices(mu,charge,coef=4,charge_weight=2):
 basis=[(a,b,k) for k in range(charge//2+1) for a in range(charge-2*k+1) for b in [charge-2*k-a]];idx={x:i for i,x in enumerate(basis)};n=len(basis);H=np.zeros((n,n),complex)
 for i,(a,b,k) in enumerate(basis):
  target=(a+1,b+1,k-1)
  if target in idx:
   j=idx[target];H[j,i]=2j*sqrt((a+1)*(b+1)*k/mu);H[i,j]=np.conj(H[j,i])
 D=np.diag([a*b/mu+coef*k for a,b,k in basis]);L=np.diag([a+b+2 for a,b,k in basis]);Q=np.diag([a+b+charge_weight*k for a,b,k in basis]);return basis,H,D,L,Q
for mu in [1,2,3,6]:
 for charge in [2*mu,4*mu]:
  basis,H,D,L,Q=matrices(mu,charge);Li=np.diag(1/np.diag(L));C=D@H-H@D
  check(f'weighted_H_entries_{mu}_{charge}',np.max(np.abs(H@Li))<=sqrt(2)+1e-12)
  check(f'weighted_commutator_norm_{mu}_{charge}',np.linalg.norm(C@Li,2)<12)
  check(f'positive_shell_{mu}_{charge}',np.linalg.eigvalsh(D+H).min()>-1e-11)
  check(f'charge_conservation_{mu}_{charge}',np.linalg.norm(Q@H-H@Q)<1e-12)
  phase=np.diag(np.exp(1j*.173*np.diag(D)));check(f'diagonal_dressing_{mu}_{charge}',np.linalg.norm(phase@C@phase.conj().T@Li,2)<12)
# Genuine weighted edge countercontrols, computed independently from occupations.
def edge(mu,a,b,k,z=2,weighted=True):
 increment=R(a+b+1,mu)-4
 amp2=R(z*z*(a+1)*(b+1)*k,mu)
 if weighted:amp2/= (a+b+2)**2
 return increment**2*amp2
check('unweighted_countercontrol',edge(6,4,4,8,z=1,weighted=False)>144)
check('outside_charge_countercontrol',edge(1,10,10,1)>144)
_,H,D,L,Q=matrices(2,8);tau=.02;exact=expm(-1j*tau*H)
err=[]
for slices in [4,8,16]:
 delta=tau/slices;W=expm(1j*delta*D)@expm(-1j*delta*(D+H));err.append(np.linalg.norm(np.linalg.matrix_power(W,slices)-exact,2))
check('finite_product_convergence',err[2]<err[1]<err[0])
check('single_final_cancellation_not_exact',np.linalg.norm(expm(1j*tau*D)@expm(-1j*tau*(D+H))-exact,2)>1e-7)
par=np.diag([(-1)**x[2] for x in matrices(2,8)[0]])
check('parity_flips_H_not_D',np.linalg.norm(par@H@par+H)<1e-12 and np.linalg.norm(par@D@par-D)<1e-12)
check('weighted_constant',128<144)
check('moment_sqrt_constant',63000<251**2)
check('split_constant',10*R(11,10)**2*12*251<37000)
core=600*(1+R(1,10**17))/10**14+R(440,2**50+1)+R(3600+22000+260100,10**17)
def budget(mu,tail,slices=10**19,err=R(1,10**95),weighted=True):
 split=R(37000,slices) if weighted else R(3120*mu,slices)
 return core+tail+split+40*slices*err*(22*mu*mu+6*mu)
co=budget(10**28,R(2,10**14));th=budget(4*10**28,R(1734,10**17));bound=R(9272,10**15)
check('coherent_budget',co<bound);check('thermal_budget',th<bound)
check('energy_consumer',6300000*bound<R(8,1000)**2)
check('pulse_reduction',6*10**47//(6*10**20)==10**27)
check('precision_allowance_change',R(1,10**95)/R(1,10**122)==10**27)
check('thermal_tail',R(4*(12*(4*10**28)+8),(2*(4*10**28)-2)**2)<R(1734,10**17)**2)
# Finite Poisson sum is a numerical control of analytic coherent overlap.
mu=2;phi=.17;overlap=sum(exp(-mu)*mu**k/factorial(k)*np.exp(-2j*phi*k) for k in range(60))
check('coherent_drift_overlap',abs(abs(overlap)**2-exp(-4*mu*sin(phi)**2))<1e-13)
from flint import arb,ctx
ctx.prec=160
muA=arb(10**28);phiA=arb(1)/10**14
lower=(1-(-4*muA*phiA.sin()**2).exp()).sqrt()
check('idle_drift_large_at_fixed_phase',lower>arb('.98'))
def oracle(dcoef=4,qweight=2,slices=10**19,err=R(1,10**95),drift_charge=2):
 _,h,d,l,q=matrices(2,8,coef=dcoef,charge_weight=qweight)
 overlap_candidate=sum(exp(-2)*2**k/factorial(k)*np.exp(-1j*drift_charge*.17*k) for k in range(60))
 return {'weighted_commutator':np.linalg.norm((d@h-h@d)@np.diag(1/np.diag(l)),2)<12,
 'charge_commutator':np.linalg.norm(q@h-h@q)<1e-12,
 'complete_budget':budget(4*10**28,R(1734,10**17),slices,err)<bound,
 'drift_overlap':abs(abs(overlap_candidate)**2-exp(-8*sin(.17)**2))<1e-13}
assert all(oracle().values())
mut={'wrong_diagonal_generator':dict(dcoef=40),'wrong_charge_weight':dict(qweight=1),'too_few_slices':dict(slices=1000),'loose_diagonal_errors':dict(err=R(1,10**70)),'missing_pump_charge_in_drift':dict(drift_charge=1)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
finish(stem,deps,faults,dict(bounds=dict(coherent=str(co),thermal=str(th),common=str(bound),slices=10**19,positive_pulses=6*10**20,diagonal_allowance='1e-95',idle_coherent_distance=str(lower)),scope='state-dependent same alphabet; no arbitrary-input operator bound or hardware synthesis'))
