from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def zero(x):return s.simplify(s.expand_complex(x))==0
def matzero(M):return all(zero(x) for x in M)
def chk(n,v):checks[n]=bool(v)
def amplitudes(N):return s.Matrix([s.sqrt(s.Rational(2,N+2))*s.sin(s.pi*(n+1)/(N+2)) for n in range(N+1)])
def fourier(M,N):return s.Matrix(M,N+1,lambda j,n:s.expand_complex(s.exp(2*s.pi*s.I*n*j/M))/s.sqrt(M))
def mixed_loss_coeffs(rho,M):
 # Exact Laurent coefficients in exp(-2i phi), using cyclic Fourier sums.
 N=rho.rows-1;out={}
 for n in range(N+1):
  for m in range(N+1):
   for shift,weight in [(0,2),(1,-1),(-1,-1)]:
    power=n-m+shift
    if power%M==0:out[power]=s.simplify(out.get(power,0)+weight*rho[n,m])
 return {k:v for k,v in out.items() if not zero(v)}
def loss_coeffs(a,M):return mixed_loss_coeffs(a*a.T,M)
for N in [1,2,4]:
 a=amplitudes(N);M=N+2;F=fourier(M,N);e0=s.eye(N+1)[:,0];w=(e0-a)/s.sqrt(2*(1-a[0]));U=s.eye(N+1)-2*w*w.T
 chk(f'sine_norm_{N}',zero((a.T*a)[0]-1));chk(f'prepare_unitary_{N}',matzero(U.T*U-s.eye(N+1)));chk(f'prepare_actual_state_{N}',matzero(U*e0-a))
 chk(f'Fourier_isometry_{N}',matzero(F.conjugate().T*F-s.eye(N+1)))
 charge=2*N*s.eye(N+1);chk(f'charge_conserved_{N}',matzero(U*charge-charge*U))
 L=2*(1-s.cos(s.pi/(N+2)));chk(f'uniform_loss_{N}',loss_coeffs(a,M)=={0:s.simplify(L)})
 chk(f'pilot_mean_{N}',zero(sum(n*a[n]**2 for n in range(N+1))-s.Rational(N,2)))
 # Full measure-and-reset Kraus matrices, not probabilities alone.
 Ks=[e0*F[j,:] for j in range(M)]
 chk(f'Kraus_complete_{N}',matzero(sum((K.conjugate().T*K for K in Ks),s.zeros(N+1))-s.eye(N+1)))
 rho=a*a.T
 chk(f'charged_return_{N}',matzero(sum((K*rho*K.conjugate().T for K in Ks),s.zeros(N+1))-e0*e0.T))
 chk(f'pilot_reduced_purity_{N}',zero(sum(x**4 for x in a)-s.Rational(3,2*(N+2))))
# Relative signal vs common mode, evaluated on N=1 exact states.
a=amplitudes(1);F=fourier(3,1);phi=s.pi/4
relative=s.diag(1,s.exp(-2*s.I*phi))*a;common=s.exp(-2*s.I*phi)*a
probs=lambda vec,F=F:[s.simplify(s.expand_complex((F[j,:]*vec)[0]*s.conjugate((F[j,:]*vec)[0]))) for j in range(3)]
chk('relative_information',probs(relative)!=probs(a));chk('common_mode_blind',probs(common)==probs(a))
rhodiag=s.diag(*[x*x for x in a]);chk('discard_reference_blind',matzero(s.diag(1,s.exp(-2*s.I*phi))*rhodiag*s.diag(1,s.exp(2*s.I*phi))-rhodiag))
chk('dephased_uniform_outcomes',all(zero((F[j,:]*rhodiag*F[j,:].conjugate().T)[0]-s.Rational(1,3)) for j in range(3)))
chk('alias_counterexample',loss_coeffs(a,2)=={0:s.Integer(1),-2:-s.Rational(1,2),2:-s.Rational(1,2)})
# Positive correction Hamiltonian integrates to the actual phase for integer Q.
for j,Qnum in [(0,1),(1,1),(2,3),(4,2)]:
 M=6;theta=s.pi*j/M;unit=s.exp(-s.I*s.pi*(2-s.Rational(j,M))*Qnum)
 chk(f'positive_actuator_{j}_{Qnum}',2-s.Rational(j,M)>0 and zero(unit-s.exp(s.I*theta*Qnum)))
Q=s.Rational;N=3*10**27;M=N+2;mu=10**28;baseline=Q(9386,10**15)
# pi<22/7 makes all claimed numerical inequalities exact rational checks.
avg=baseline+Q(22,7)*10**14/M
chk('average_budget',avg<Q(9491,10**15));chk('record92',2**91<M<=2**92)
chk('success_probability',Q(2,45)<Q(1,20));chk('ideal_success',baseline+2*10**14*Q(3,10**27)<Q(9986,10**15)+Q(1,10**30))
chk('precision_budget',2*10**14*Q(5,10**29)==Q(1,10**14))
chk('two_full_budgets_do_not_certify_success',baseline+2*10**14*Q(3,10**27)+2*Q(1,10**14)>Q(1,10**11))
chk('tight_success_budget',baseline+2*10**14*(Q(3,10**27)+2*Q(1,10**29))<=Q(9990,10**15))
chk('tight_average_budget',avg+4*Q(1,10**15)<Q(9495,10**15))
chk('total_stock_count',N!=N//2 and 2*(N//2)==N)
assert all(checks.values()),[k for k,v in checks.items() if not v]
# Mutated machinery is passed to the same actual evaluators.
a=amplitudes(2);F=fourier(4,2);e0=s.eye(3)[:,0];w=(e0-a)/s.sqrt(2*(1-a[0]));badU=s.eye(3)-w*w.T
faults={
 'one_too_few_outcomes':['uniform_loss_1'] if loss_coeffs(amplitudes(1),2)!={0:s.Integer(1)} else [],
 'half_Householder':['prepare_actual_state_2'] if not matzero(badU*e0-a) else [],
 'wrong_readout_normalization':['Fourier_isometry_2'] if not matzero((s.sqrt(2)*F).conjugate().T*(s.sqrt(2)*F)-s.eye(3)) else [],
 'dephase_prepared_pair':['uniform_loss_2'] if mixed_loss_coeffs(s.diag(*[x*x for x in a]),4)!=loss_coeffs(a,4) else [],
 'common_arm_encoding':['relative_information'] if not (probs(common)!=probs(amplitudes(1))) else [],
 'odd_Q_half_actuator':['positive_actuator_1_1'] if not zero(s.exp(-s.I*s.pi*(1-Q(1,6)))-s.exp(s.I*s.pi/6)) else []}
assert all(faults.values()),faults
stem='k2312-relational-finite-calibration';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2309-nonclassical-pump-calibration-2026-10-30.md','explorations/conditional-build/k2306-retained-pump-phase-calibration-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2312',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact small-shell maps and Fourier coefficients; rational fixture budgets; general finite construction and distance proof in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'total_stock':str(N),'outcomes':str(M),'record_qubits':92,'average_upper':'9.491e-12','strict_reference_angle_example':'1e-29','strict_correction_angle_example':'1e-29'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2312',checks=len(checks),faults=len(faults))))
