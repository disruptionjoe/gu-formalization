from pathlib import Path
import sympy as s
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def zero(v):return s.simplify(s.expand_complex(v))==0
def check(n,v):checks[n]=bool(v)
def pilot(N,offset=2,shift=1,normalizer=1):return s.Matrix([normalizer*s.sqrt(s.Rational(2,N+offset))*s.sin(s.pi*(n+shift)/(N+offset)) for n in range(N+1)])
def adjacency(N):return s.Matrix(N+1,N+1,lambda i,j:s.Rational(1,2) if abs(i-j)==1 else 0)
def verify(N,vec):
 A=adjacency(N);return {'norm':zero((vec.T*vec)[0]-1),'mean':zero(sum(n*vec[n]**2 for n in range(N+1))-s.Rational(N,2)),'eigen':all(zero(v) for v in A*vec-s.cos(s.pi/(N+2))*vec)}
for N in (0,1,2,4):
 vec=pilot(N)
 for key,v in verify(N,vec).items():check(str(N)+'_'+key,v)
 check(str(N)+'_circular_loss',zero(2*(1-sum(vec[n]*vec[n+1] for n in range(N)))-2*(1-s.cos(s.pi/(N+2)))))
 if N>=2:check(str(N)+'_preparation_orthogonality',zero(sum(vec[n]**2*s.exp(s.I*n*4*s.pi/(N+2)) for n in range(N+1))))
# Independent Fourier integration in N=1, not just the spectral formula.
e=s.symbols('e',real=True);density=(1+s.cos(2*e))/s.pi
check('POVM_normalized',s.integrate(density,(e,-s.pi/2,s.pi/2))==1)
loss=s.integrate(4*s.sin(e)**2*density,(e,-s.pi/2,s.pi/2));check('Fourier_loss_N1',loss==1)
check('twirled_loss',s.integrate(4*s.sin(e)**2/s.pi,(e,-s.pi/2,s.pi/2))==2)
# The general recurrence is the universal path eigenvector, with both boundary zeros.
theta,j=s.symbols('theta j',real=True)
check('general_path_recurrence',s.trigsimp((s.sin((j-1)*theta)+s.sin((j+1)*theta))/2-s.cos(theta)*s.sin(j*theta))==0)
# Encoding by charge2 is pi periodic; charge1 is not (N1 is an orthogonal countercontrol).
def alias(charge):return s.simplify(abs((1+s.exp(-s.I*charge*s.pi))/2)**2)
check('charge_two_alias',alias(2)==1)
Q=s.Rational;mu=10**28;N=3*10**27;r=Q(3,10**27);delta=Q(9386,10**15);eps=Q(1,10**11);eta=Q(1,10**14);zeta=eta;pi_upper=Q(22,7)
check('pi_square_bound',pi_upper**2<10)
loss_upper=Q(10,(N+2)**2);denom_lower=4*(Q(5,6)*r)**2
check('confidence_failure',loss_upper/denom_lower<Q(2,45)<Q(1,20))
check('confidence_error',delta+2*10**14*r<Q(9986,10**15)+Q(1,10**30) and delta+2*10**14*r<eps)
check('averaged_error',delta+pi_upper*10**14/(N+2)<Q(9491,10**15))
check('imperfect_average',delta+pi_upper*10**14/(N+2)+eta+zeta<Q(9511,10**15))
check('imperfect_success',1-Q(2,45)-eta>Q(95,100) and delta+2*10**14*r+zeta<eps)
Delta=Q(2,10**25);mean=10**24
ov_lower=1-2*Delta*mean
check('general_mean_resource_control',ov_lower==Q(3,5) and 1-ov_lower**2==Q(16,25)<Q(81,100))
# Unequal exposures use the generator sum duration*K, not its coherent Fisher square.
weights=[Q(1),Q(2)];means=[Q(2),Q(3)]
check('linear_duration_resource',sum(w*n for w,n in zip(weights,means))==8)
check('preparation_log_lower',3**28<1/(4*eta*(1-eta)))
prep_lower=Q((N+2)**2*28,160)
check('coherent_preparation_price',prep_lower>Q(1575,1000)*10**54)
# Exact contraction: target orthogonal orbits, preparation error eta on each endpoint.
f=s.symbols('f',nonnegative=True);et=s.symbols('eta',real=True)
check('preparation_fidelity_threshold',zero(1-(1-2*et)**2-4*et*(1-et)))
assert all(checks.values()),[k for k,v in checks.items() if not v]
def fails(N,vec):return [k for k,v in verify(N,vec).items() if not v]
faults={
 'charge_one':['charge_two_alias'] if alias(1)!=1 else [],
 'wrong_cutoff_denominator':fails(2,pilot(2,offset=1)),
 'shifted_sine_index':fails(2,pilot(2,shift=0)),
 'missing_normalizer':fails(2,pilot(2,normalizer=s.sqrt(2))),
 'half_circular_loss':['Fourier_loss_N1'] if s.integrate(2*s.sin(e)**2*density,(e,-s.pi/2,s.pi/2))!=loss else [],
 'squared_duration_in_mean_bound':['linear_duration_resource'] if sum(w*w*n for w,n in zip(weights,means))!=8 else [],
 'amplitude_as_fidelity':['preparation_fidelity_threshold'] if s.expand((4*et*(1-et))**2-4*et*(1-et))!=0 else []}
assert all(faults.values()),faults
stem='k2309-nonclassical-pump-calibration';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2306-retained-pump-phase-calibration-2026-10-30.md']
# Pin reused preparation and sine evidence by exact native files.
for prefix in ('k2275-','k2251-','k2240-'):
 matches=list((ROOT/'explorations/conditional-build').glob(prefix+'*.md'));assert len(matches)==1;deps.append(str(matches[0].relative_to(ROOT)))
data=dict(schema_version='1.0',result_id='K2309',checks=len(checks),check_names=list(checks),mutation_failed_checks=faults,evidence_kind='exact finite Fourier/path controls, symbolic recurrence, rational budgets; uniform minimax and contraction proofs in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'cutoff':str(N),'mean':str(N//2),'average_upper':'9.491e-12','imperfect_average_upper':'9.511e-12','preparation_mean_lower':'1.575e54','success_mean_lower':'(1-sqrt(19/100))/(4e-25)'})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2309',checks=len(checks),faults=len(faults))))
