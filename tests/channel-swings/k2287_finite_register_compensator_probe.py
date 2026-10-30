from pathlib import Path
import json,hashlib,sys
import sympy as s
R=s.Rational
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(name,value):
    checks[name]=bool(value)
def report(stem,deps,faults,extra):
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    assert all(faults.values()),faults
    paths=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),*deps]
    data=dict(schema_version='1.0',result_id=stem.split('-')[0].upper(),claim_ceiling='conditional supplied model; no GU, empirical or hardware acceptance',checks=len(checks),check_names=list(checks),evidence_kind='symbolic identities, finite circuit controls and rational or interval bounds; universal proofs in companion',mutation_failed_checks=faults,dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},**extra)
    out=ROOT/'lab/process'/f'{stem}.json'
    if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(out.read_text())==data,'stored report stale'
    print(json.dumps(dict(result=data['result_id'],checks=len(checks),faults=len(faults),**extra)))

import numpy as np
stem='k2287-finite-register-compensator'

def one_h(q,j):
 D=2**q;H=np.zeros((D,D),complex)
 for n in range(D):
  bit=(n>>j)&1;zero=n^(bit<<j)
  H[n,zero]=1/np.sqrt(2);H[n,zero|(1<<j)]=(-1)**bit/np.sqrt(2)
 return H
def qft_gates(q,omit_controlled=False):
 D=2**q;U=np.eye(D,dtype=complex)
 for j in reversed(range(q)):
  U=one_h(q,j)@U
  for k in reversed(range(j)):
   phase=np.array([np.exp(1j*np.pi/2**(j-k)) if ((n>>j)&1 and (n>>k)&1) else 1 for n in range(D)])
   if not omit_controlled:U=phase[:,None]*U
 for j in range(q//2):
  k=q-1-j;swap=np.zeros((D,D))
  for n in range(D):
   m=n
   if ((n>>j)&1)!=((n>>k)&1):m=n^(1<<j)^(1<<k)
   swap[m,n]=1
  U=swap@U
 return U
for q in (2,3,4):
 D=2**q;ix=np.arange(D);dense=np.exp(2j*np.pi*np.outer(ix,ix)/D)/np.sqrt(D)
 check('elementary_QFT_'+str(q),np.linalg.norm(qft_gates(q)-dense)<1e-12)
prior=json.loads((ROOT/'lab/process/k2285-thermal-centered-composition.json').read_text())
for path,h in prior['dependencies'].items():check('prior_hash_'+path,hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==h)

# Finite controls implement the counted elementary QFT and compute/phase/uncompute.
def circuit(q,charge,m,theta,*,signed=True,cross=True,offset=True,uncompute=True):
 D=2**q;indices=np.arange(D);bits=((indices[:,None]>>np.arange(q))&1);w=2.**np.arange(q)
 if signed:w[-1]=-w[-1]
 square=(bits*w*w).sum(axis=1)
 if cross:
  for j in range(q):
   for k in range(j+1,q):square+=2*w[j]*w[k]*bits[:,j]*bits[:,k]
 fourier=qft_gates(q)
 phase=np.exp(2j*np.pi*indices*(charge-(m if offset else 0))/D)
 # Actual C=F† diag(phase) H_all, including the counted local Hadamards.
 hall=np.eye(D,dtype=complex)
 for j in range(q):hall=one_h(q,j)@hall
 C=fourier.conj().T@np.diag(phase)@hall
 e0=np.eye(D,dtype=complex)[:,0]
 v=C@e0;v=np.exp(-1j*theta*square)*v
 if uncompute:v=C.conj().T@v
 return v
for q in (2,3,4):
 D=2**q;m=3;theta=.137
 for delta in (-D//2+1,-1,0,1,D//2-1):
  Q=m+delta
  if Q<0:continue
  target=np.zeros(D,complex);target[0]=np.exp(-1j*theta*delta**2)
  check(f'circuit_q{q}_delta{delta}',np.linalg.norm(circuit(q,Q,m,theta)-target)<1e-12)
 # Actual coherent superposition keeps the relative phase, not just probabilities.
 qs=[m-1,m,m+1];amp=np.array([1,1j,-1],complex)/np.sqrt(3)
 actual=np.concatenate([b*circuit(q,Q,m,theta) for b,Q in zip(amp,qs)])
 ideal=np.concatenate([np.r_[b*np.exp(-1j*theta*(Q-m)**2),np.zeros(D-1)] for b,Q in zip(amp,qs)])
 check('coherent_superposition_q'+str(q),np.linalg.norm(actual-ideal)<1e-12)
# Outside the exact window the error exists; absence of physical cutoff is essential.
out=circuit(3,12,3,.137);check('outside_window_alias_present',abs(out[0]-np.exp(-1j*.137*81))>.1)
# Algebraic square and integer-spectrum positive wrapping controls.
b0,b1,b2=s.symbols('b0 b1 b2');square=(b0+2*b1-4*b2)**2
expanded=s.expand(square).subs({b0**2:b0,b1**2:b1,b2**2:b2})
check('signed_binary_square',s.expand(expanded-(b0+4*b1+16*b2+4*b0*b1-8*b0*b2-16*b1*b2))==0)
for n in range(8):check('positive_inverse_period_'+str(n),abs(np.exp(1j*.31*n)-np.exp(-1j*(2*np.pi-.31)*n))<1e-12)
H=np.array([[1,1],[1,-1]])/np.sqrt(2);P=(np.eye(2)-H)/2
check('hadamard_positive_generator',np.linalg.eigvalsh(P).min()>-1e-14 and np.linalg.norm((np.eye(2)-2*P)-H)<1e-14)
# Local number couplings preserve every field number, also with a nonreset register.
Q=s.diag(0,2,1,3);N=s.diag(0,0,1,1);G=s.diag(0,2,0,3)
check('charge_commutator',Q*G-G*Q==s.zeros(4));check('field_commutator',N*G-G*N==s.zeros(4))
mu=s.symbols('mu',positive=True)
check('coherent_second_moment',(4*mu**2+4*mu)-(2*mu)**2==4*mu)
check('thermal_second_moment',s.expand((4*mu**2+20*mu+12)-(2*mu+2)**2)==12*mu+8)
core=R(600)*(1+R(1,10**17))/10**14+R(440,2**50+1)+R(3600+22000+260100,10**17)
results={}
for name,q,mm,ec,eq,sqrtc,sqrtq in [('coherent',96,10**28,4*10**28+1,4*10**56+4*10**28,2*10**14+1,2*10**28+1),('thermal',98,4*10**28,48*10**28+24,4*(4*10**28)**2+20*4*10**28+12,692820323027551,8*10**28+5)]:
 nd=42*q;nn=7*q+3*q*(q-1)//2+2*(q//2)
 check(name+'_sqrtC_upper',sqrtc**2>ec);check(name+'_sqrtQ_upper',sqrtq**2>eq)
 alias=R(2*sqrtc,2**(q-1));disp=R(nd*sqrtq,10**47);neu=R(nn,10**19);budget=alias+disp+neu
 check(name+'_complete_budget',core+budget<R('9.27e-12'))
 check(name+'_energy',R(6300000,10**11)<R('.008')**2)
 check(name+'_gate_count',nd==(4032 if name=='coherent' else 4116) and nn==(14448 if name=='coherent' else 15043))
 results[name]=dict(qubits=q,number_pulses=nd,neutral_gates=nn,alias_upper=str(alias),dispersive_upper=str(disp),neutral_upper=str(neu),compiler_upper_decimal=str(s.N(budget,16)),complete_upper_decimal=str(s.N(core+budget,16)))
def oracle(signed=True,cross=True,offset=True,uncompute=True,pump_weight=2):
 q=3;m=3;theta=.137;states=[(0,1),(1,1),(2,1)]
 checks0={}
 for field,pump in states:
  charge=field+pump_weight*pump;expectedcharge=field+2*pump
  target=np.zeros(8,complex);target[0]=np.exp(-1j*theta*(expectedcharge-m)**2)
  checks0[f'field{field}_pump{pump}']=np.linalg.norm(circuit(q,charge,m,theta,signed=signed,cross=cross,offset=offset,uncompute=uncompute)-target)<1e-12
 return checks0
assert all(oracle().values())
mut={'unsigned_top_bit':dict(signed=False),'missing_square_cross_terms':dict(cross=False),'missing_center_offset':dict(offset=False),'missing_uncompute':dict(uncompute=False),'wrong_pump_weight':dict(pump_weight=1)}
faults={n:[k for k,v in oracle(**kw).items() if not v] for n,kw in mut.items()}
faults['omitted_QFT_controlled_phases']=['elementary_QFT'] if np.linalg.norm(qft_gates(3,True)-qft_gates(3))>1e-12 else []
# Tail underallocation is an actual parameter fault against unchanged budget predicate.
lowq=32;bad=R(2*(2*10**14+1),2**(lowq-1))+R(42*lowq*(2*10**28+1),10**47)
faults['undersized_register']=['complete_budget'] if core+bad>=R('9.27e-12') else []
# Successor: a bounded modular shift does not stabilize the instantaneous pump.
kvar=s.symbols('k',positive=True)
check('rayleigh_growth',s.Poly(4*kvar*kvar-kvar*(kvar*kvar+1)+65,kvar).LC()==-1)
n=100;off=(n+1)*10;W=65;compression=s.Matrix([[W,s.I*off],[-s.I*off,W]])
vector=s.Matrix([1,s.I])/s.sqrt(2)
check('negative_compression_rayleigh',s.simplify((s.conjugate(vector).T*compression*vector)[0])==W-off and W-off<0)
check('same_charge_pair',2*n+2*n==2*(n+1)+2*(n-1))

report(stem,['lab/process/k2285-thermal-centered-composition.json','explorations/conditional-build/k2282-centered-positive-control-2026-10-29.md'],faults,dict(resource_certificates=results,unbounded_claim='modular identity plus tail and hybrid proof; finite matrices are controls only'))
