from pathlib import Path
import json,hashlib,sys
import sympy as s
from flint import arb,ctx
ctx.prec=160
R=s.Rational
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
 data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied models; no GU empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='symbolic identities and rational or outward interval bounds; finite matrices are controls; hashes provenance only; universal arguments in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
 out=ROOT/'lab/process'/f'{stem}.json'
 if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(out.read_text())==data,'stored report stale'
 print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

import numpy as np
from scipy.linalg import expm
stem='k2290-local-positive-pump'
DEPS=['lab/process/k2279-uniform-pump-energy.json','lab/process/k2285-thermal-centered-composition.json']
for dep in DEPS:verify_prior(dep)
def shell(q):return [(a,b,(q-a-b)//2) for a in range(q+1) for b in range(q-a+1) if (q-a-b)%2==0]
def matrices(q,mu=3,z=1+1j,pump=4,sign=1):
 states=shell(q);index={v:i for i,v in enumerate(states)};N=len(states);H=np.zeros((N,N),complex);D=np.diag([a*b/mu+pump*k for a,b,k in states])
 for i,(a,b,k) in enumerate(states):
  if k:
   j=index[a+1,b+1,k-1];H[j,i]=sign*1j*z*np.sqrt((a+1)*(b+1)*k/mu);H[i,j]=np.conj(H[j,i])
 return states,H,D
for q in range(9):
 st,H,D=matrices(q);low=shell(q-2) if q>=2 else [];ix={v:i for i,v in enumerate(low)};L=np.zeros((len(low),len(st)),complex)
 for i,(a,b,k) in enumerate(st):
  if a*b:L[ix[a-1,b-1,k],i]+=np.sqrt(a*b/3)
  if k:L[ix[a,b,k-1],i]+=1j*(1+1j)*np.sqrt(k)
 B=H+D;target=L.conj().T@L+np.diag([2*k for a,b,k in st])
 check('square_matrix_'+str(q),np.max(np.abs(B-target))<1e-12)
 check('positive_matrix_'+str(q),np.linalg.eigvalsh(B).min()>-1e-12)
 n=np.diag([a+b for a,b,k in st]);Q=np.diag([a+b+2*k for a,b,k in st]);check('charge_commutator_'+str(q),np.max(np.abs(Q@H-H@Q))<1e-12)
 check('diagonal_number_commutator_'+str(q),np.max(np.abs(n@D-D@n))==0)
mu=s.symbols('mu',positive=True);t=s.symbols('t');v=s.exp(t)-1
mgf=s.exp(mu*v/(1-v))/(1-v)
raw4=s.expand(s.diff(mgf,t,4).subs(t,0))
expected=mu**4+22*mu**3+133*mu**2+233*mu+75
fact=[mu+1,mu**2+4*mu+2,mu**3+9*mu**2+18*mu+6,mu**4+16*mu**3+72*mu**2+96*mu+24]
check('thermal_raw_fourth_from_mgf',raw4==expected)
check('thermal_raw_fourth_from_normal_moments',s.expand(fact[3]+6*fact[2]+7*fact[1]+fact[0])==expected)
check('fourth_moment_uniform_bound',sum(s.Poly(expected,mu).all_coeffs())==464 and 16*464<16*22**2)
check('second_moment_uniform_bound',4+20+12<=6**2)
check('commutator_uniform_constant',16**2*6**3<240**2)
# Strict positivity margin for supplied noisy local diagonal controls.
check('noisy_square_margin',R(3,4)*3>(1+R(3,10**17))**2)
base=R(600)*(1+R(1,10**17))/10**14+R(440,2**50+1)+(3600+22000+260100)*R(1,10**17)
r=10**46;e=R(1,10**122);cert={}
for tag,M,tail in [('coherent',10**28,R(2,10**14)),('thermal',4*10**28,R(1734,10**17))]:
 if tag=='thermal':check('thermal_tail_enclosure',4*(12*M+8)<tail**2*(2*M-2)**2)
 split=R(3120*M,r);area=40*r*e*(22*M*M+6*M);total=base+tail+split+area
 check(tag+'_channel_budget',total<R(93,10**13));check(tag+'_energy_budget',6300000*total<R(8,1000)**2)
 cert[tag]=dict(core=str(base),tail=str(tail),split=str(split),diagonal_errors=str(area),total=str(total))
# Noncommuting true matrices and time-varying piecewise constant z.
q=4;_,H1,D=matrices(q,mu=1,z=1);_,H2,_=matrices(q,mu=1,z=1j);dur=.1
U=expm(-1j*dur*H2)@expm(-1j*dur*H1)
def compiled(n,interleave=True):
 out=np.eye(len(D),dtype=complex)
 for H in [H1,H2]:
  if interleave:
   W=expm(1j*dur/n*D)@expm(-1j*dur/n*(D+H));out=np.linalg.matrix_power(W,n)@out
  else:out=expm(1j*dur*D)@expm(-1j*dur*(D+H))@out
 return out
err=lambda n:np.linalg.norm(compiled(n)-U,2)
check('noncentral_shift',np.linalg.norm(D@H1-H1@D)>1)
check('actual_time_dependent_convergence',err(32)<err(8)/3)
check('finite_shell_duhamel_bound',err(32)<2*dur**2*np.linalg.norm(D@H1-H1@D,2)/(2*32))
def oracle(pump=4,sign=1,weight=2,interleave=True,moment=expected):
 st,H,DD=matrices(2,mu=1,z=2,pump=pump,sign=sign);_,Htrue,Dtrue=matrices(2,mu=1,z=2)
 Q=np.diag([a+b+weight*k for a,b,k in st])
 return {'positive_generator':np.linalg.eigvalsh(DD+H).min()>-1e-12,'cross_term':np.max(np.abs(H-Htrue))<1e-12,'charge':np.max(np.abs(Q@H-H@Q))<1e-12,'compiler':np.linalg.norm(compiled(32,interleave)-U,2)<err(8)/3,'thermal_fourth':s.expand(moment-raw4)==0}
assert all(oracle().values())
mut={'insufficient_pump_stabilizer':dict(pump=3),'wrong_cross_sign':dict(sign=-1),'wrong_charge_weight':dict(weight=1),'no_interleaving':dict(interleave=False),'wrong_thermal_fourth':dict(moment=mu**4+28*mu**3+150*mu**2+196*mu+75)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
finish(stem,DEPS,faults,dict(resource_certificates=cert,pulses=str(60*r),calibration='positive B coefficient L1 errors and correction area errors <=1e-122',finite_matrix_scope='q<=8 controls, not proof of whole-Fock positivity'))
