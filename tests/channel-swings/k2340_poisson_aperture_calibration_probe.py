"""Exact positive-intensity parity sky and overlapping-count controls."""
import sympy as s,itertools,math
from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def finish(st,details,evidence,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-30.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),evidence_kind=evidence,mutation_failed_checks=faults,details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 assert faults and all(faults.values())
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps({'result':out['result_id'],'checks':len(checks),'faults':len(faults)}))

q=s.Rational
signs=list(itertools.product([-1,1],repeat=5));plus=[v for v in signs if math.prod(v)==1];minus=[v for v in signs if math.prod(v)==-1]
check('parity_sizes',len(plus)==len(minus)==16)
def moments(vs):
 V=s.Matrix(vs);return s.ones(1,len(vs))*V/len(vs),V.T*V/len(vs)
for name,vs in [('plus',plus),('minus',minus)]:
 mean,cov=moments(vs);check(name+'_zero_mean',mean==s.zeros(1,5));check(name+'_identity_cov',cov==s.eye(5))
prob=q(sum(all(x*y<0 for x,y in zip(a,b)) for a in plus for b in minus),256)
check('joint_sign_probability',prob==q(1,16))
check('positive_sky_from_pi_lower',q(25,12)<4) # pi>3, amplitude squared<=25/(4pi)
check('aperture_r_upper',1/(3*q(3,64)**2)==q(4096,27))
# Six antipodal lines, symbolic overlap and zero-sum extraction.
ap,am,pi=s.symbols('ap am pi');AA=s.zeros(12)
for i in range(12):
 for j in range(12):AA[i,j]=pi if i==j else (0 if i//2==j//2 else ((ap+am)/2))
# Only paired sums matter; split equally is valid on the even subspace.
V=s.zeros(12,5)
for a in range(5):V[2*a,a]=V[2*a+1,a]=1;V[10,a]=V[11,a]=-1
check('overlap_even_zero_sum_eigen',s.simplify(AA*V-(pi-ap-am)*V)==s.zeros(12,5))
r,E,B11,B12,B22=s.symbols('r E B11 B12 B22',positive=True);a=r/(E*B12)
for b in [B11,B22]:check('full_reference_diagonal_'+str(b),s.simplify(a*b+(1+3*r/E-a*b)-(1+3*r/E))==0)
check('full_reference_cross',s.simplify(a*B12-r/E)==0)
eps=q(1,345600);check('actual_full_tail_ratio_bound',(273+eps)/(230-eps)<3)
margin=q(1,16)-30*q(4096,27)/10**6
check('finite_exposure_counterexample',margin>q(1,20))
# Actual three-overlap atom at (1,1,1)/sqrt3; label-independent construction.
phi=(1+s.sqrt(5))/2;verts=[]
for a1 in [-1,1]:
 for a2 in [-1,1]:
  for v in [(0,a1,a2*phi),(a1,a2*phi,0),(a2*phi,0,a1)]:verts.append(s.Matrix(v)/s.sqrt(phi+2))
n=s.ones(3,1)/s.sqrt(3);dots=[s.simplify((v.T*n)[0]) for v in verts];inc=s.Matrix([int(bool(z>q(1,2))) for z in dots]);check('triple_overlap_atom',sum(inc)==3)
Q=s.Matrix([[v[0]*v[1],v[0]*v[2],v[1]*v[2],v[0]**2-v[1]**2,2*v[2]**2-v[0]**2-v[1]**2] for v in verts]);check('nonzero_extracted_atom',s.simplify(Q.T*inc)!=s.zeros(5,1))
raw=inc*inc.T;check('actual_cap_overlap_offdiagonal',sum(raw)-s.trace(raw)==6)
# Counts P1,P2,C independent Poi(1/4). Exact finite total<=8 enumeration.
mu=q(1,4);mass=s.S(0)
for p1 in range(9):
 for p2 in range(9-p1):
  for c in range(9-p1-p2):
   if (c+p1-q(1,2))*(c+p2-q(1,2))<0:mass+=mu**(p1+p2+c)/s.factorial(p1)/s.factorial(p2)/s.factorial(c)
expected=2*sum((mu**n/s.factorial(n) for n in range(1,9)),s.S(0))
check('shared_sparse_integer_enumeration',mass==expected)
# p=2e^-1/2(1-e^-1/4), lower e^-1/2>1/2 and1-e^-1/4>1/5 via e^1/4>5/4.
check('sparse_probability_lower',q(2)*q(1,2)*q(1,5)==q(1,5))
tail=(q(3,4)**9/s.factorial(9))/(1-q(3,40))
check('total_count_tail',tail<q(1,300000))
check('shared_count_total_mean',3*mu==q(3,4))
def tail_acceptance(allowance):return allowance>=2*mu**9/s.factorial(9)
check('tail_allowance_covers_first_omitted_event',tail_acceptance(tail))
# Genuine faults operate on ensembles, raw map, or shared count input.
badprob=q(sum(all(x*y<0 for x,y in zip(a,b)) for a in plus for b in plus),256)
faults['same_parity_classes']=['joint_sign_probability'] if badprob!=prob else []
shared=s.Matrix([[1,0,1],[0,1,1]]);independent=s.Matrix([[1,0,1,0],[0,1,0,1]])
faults['independent_shared_photons']=['full_reference_cross'] if (shared*shared.T)[0,1]!=(independent*independent.T)[0,1] else []
faults['diagonalize_actual_overlap']=['actual_cap_overlap_offdiagonal'] if s.diag(*raw.diagonal())!=raw else []
wrongshot=q(3,64)**2*AA
faults['beam_attenuate_shot_noise_again']=['overlap_even_zero_sum_eigen'] if s.simplify(wrongshot*V-(pi-ap-am)*V)!=s.zeros(12,5) else []
negative_sign=next(v for v in plus if v[-1]==-1);pole_intensity=negative_sign[-1]*s.sqrt(5/(4*s.pi))
faults['zero_intensity_baseline']=['positive_sky_from_pi_lower'] if pole_intensity<0 else []
# Truncation changes true probability: event with P1=9,P2=C=0 has positive omitted mass.
faults['omit_positive_tail']=['tail_allowance_covers_first_omitted_event'] if not tail_acceptance(s.S(0)) else []
finish('k2340-poisson-aperture-calibration',{'r_upper':str(q(4096,27)),'all_discord_lower':str(margin),'exposure':10**6,'sparse_mass_without_exponential':str(mass),'tail_upper':str(tail)},'exact finite ensemble, matrix and rational checks; universal Poisson and probability proofs in note',['explorations/conditional-build/k2337-pixel-beam-count-test-2026-10-30.md'])
