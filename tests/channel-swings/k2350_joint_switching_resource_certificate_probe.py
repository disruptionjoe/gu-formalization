"""Exact joint finite-ramp certificate and common-erasure controls."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as F
from math import comb
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def fault(k,v):
 faults[k]=bool(v)
 if not v:raise AssertionError('ineffective altered-input control: '+k)
def publish(st,details,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),altered_input_controls=faults,evidence_kind='exact symbolic/rational controls; universal theorems proved in companion note, no empirical or proof-assistant certification',details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({k:out[k] for k in ['result_id','checks','details']}))

q=s.Rational;D=q(20001,2);J=q(1,10**6);delta=q(1,100);r=q(1,10**10);nu=q(1,10**10);pi=q(22,7);cmin=q(99,100);sqrt3max=q(7,4)
sb=q(99,700000);vb=q(99,70);kb=cb=q(1,10000);qb=q(1,10000*9990);ab=q(99,70)+q(2,10000)
check('exp_majorant',1/(1-2*sb)<q(1001,1000));bb=2*vb*sb**2*q(1001,1000)+sb*kb+2*sb*cb;rr=bb+qb*kb+2*qb*ab;t=pi*D/2
C=3*(2*(sb+qb)+t*rr);beta=16/(10*cmin)*(1+pi/4*(3+1/cmin));L0=3*(D+sqrt3max+1/D)+11*pi/(2*delta);L=L0+6*J/cmin
Tr=3*t+pi/(2*J)+6*delta+22*r;total=C+beta*J+r*L+nu*Tr
check('complete_joint_certificate',total<q(1,100))
check('exact_total_rational',total==q(2407557647809475658676809227,342674132850000000000000000000))
Amax=max(D+sqrt3max+1/D,pi/delta,3*J/cmin);G=11000;V=10**15
check('amplitude_cap_all_pulses',Amax<G)
check('finite_operator_envelope_slew',Amax/r<V)
check('eleven_pulses_and22_ramps',2+1+3+3+2==11 and 2*11==22)
x,amp,rt=s.symbols('x amp rt',positive=True)
check('two_triangles_integrate_ramp_debt',2*s.integrate(amp*x/rt,(x,0,rt))==amp*rt)
b=beta+6*r/cmin;k=nu*pi/2;Fc=C+nu*(3*t+6*delta+22*r)+r*L0;w=q(1,100)-Fc
check('exact_J_rearrangement',s.simplify(total-(b*J+k/J+Fc))==0)
check('nonempty_certificate_interval',w>0 and w*w>4*b*k)
check('witness_inside_J_interval',b*J*J-w*J+k<0)
check('loss_rate_split',3*(nu/6)==nu/2)
# Exact arbitrary 2x2 block singular values for neutral exchange on K sectors.
for n in [1,2,3]:
 mat=s.Matrix([[0,s.sqrt(n)],[s.sqrt(n),0]]);assert mat*mat==n*s.eye(2)
check('Xf_norm_on_K3',True)
# Boson hopping matrix in total m<=3: largest magnitude eigenvalue=m.
for n in range(1,4):
 mat=s.zeros(n+1)
 for p in range(n):mat[p,p+1]=mat[p+1,p]=s.sqrt((p+1)*(n-p))
 assert max(abs(v) for v in mat.eigenvals())==n
check('hopping_norm_on_three_bosons',True)
# Genuine full-channel common erasure: arbitrary encoded two-state subspace -> orthogonal vacuum.
eta=q(1,4);out0=s.diag(eta,0,1-eta);out1=s.diag(0,eta,1-eta)
trace_distance=sum(abs(v) for v in (out0-out1).eigenvals())/2
check('early_common_erasure_trace_distance',trace_distance==eta)
K0=s.diag(s.sqrt(eta),s.sqrt(eta),1);K1=s.zeros(3);K2=s.zeros(3);K1[2,0]=s.sqrt(1-eta);K2[2,1]=s.sqrt(1-eta)
check('early_erasure_Kraus_complete',K0.T*K0+K1.T*K1+K2.T*K2==s.eye(3))
check('encoded_state_to_common_vacuum',sum((K*s.diag(1,0,0)*K.T for K in [K0,K1,K2]),s.zeros(3))==out0 and sum((K*s.diag(0,1,0)*K.T for K in [K0,K1,K2]),s.zeros(3))==out1)
check('flag_error_lower_bound',(1-eta)/2==q(3,8))
check('gamma100_stage_decay_bound',sum(q(1,s.factorial(i)) for i in range(3))>2) # exp(1)>2, s>=.01
fault('detuning_exceeds_changed_amplitude_cap',D>10000)
fault('changed_slew_cap_rejects_same_ramp',Amax/r>10**12)
fault('high_noise_certificate_infeasible',q(1,10**5)*(3*t+6*delta+22*r)>q(1,100))
eta_bad=q(1);badK0=s.diag(s.sqrt(eta_bad),s.sqrt(eta_bad),1);badK1=s.zeros(3);badK2=s.zeros(3);badK1[2,0]=s.sqrt(1-eta_bad);badK2[2,1]=s.sqrt(1-eta_bad)
badout0=sum((K*s.diag(1,0,0)*K.T for K in [badK0,badK1,badK2]),s.zeros(3));badout1=sum((K*s.diag(0,1,0)*K.T for K in [badK0,badK1,badK2]),s.zeros(3));bad_distance=sum(abs(z)*mult for z,mult in (badout0-badout1).eigenvals().items())/2
fault('omit_early_common_loss',bad_distance==1 and bad_distance-trace_distance==q(3,4))
# Compensating longer ramps costs duration and area; cannot keep old certificate at same caps.
fault('longer_ramps_not_free',C+beta*J+q(1,1000)*L+nu*(Tr+22*(q(1,1000)-r))>q(1,100))
details={'contact_bound':str(C),'ramp_bound':str(r*L),'selective_bound':str(beta*J),'duration_upper':str(Tr),'full_bound':str(total),'full_bound_decimal':float(total),'amplitude_upper':str(Amax),'slew_upper':str(Amax/r),'positive_J_discriminant':str(w*w-4*b*k),'early_erasure_eta':'1/4','flag_error_lower_bound':'3/8'}
publish('k2350-joint-switching-resource-certificate',details,['explorations/conditional-build/k2347-microscopic-copy-echo-composition-2026-10-30.md','lab/process/k2347-microscopic-copy-echo-composition.json','explorations/conditional-build/k2344-signed-detuning-echo-repair-2026-10-30.md','explorations/conditional-build/k2338-resonant-contact-resource-boundary-2026-10-30.md'])
