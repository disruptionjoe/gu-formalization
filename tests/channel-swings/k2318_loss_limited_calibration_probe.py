"""Loss purification and channel controls; analytic arbitrary-N proof is in note."""
from pathlib import Path
from fractions import Fraction as Q
import sympy as s
import numpy as np
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2];checks={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError('[FAIL] '+n)
eta=s.symbols('eta',positive=True)
def moments(n,enc=2,den=None):
 den=(1-eta) if den is None else den
 probs=[s.binomial(n,l)*(1-eta)**l*eta**(n-l) for l in range(n+1)]
 vals=[enc*(n-l/den) for l in range(n+1)]
 return tuple(s.simplify(sum(p*v**j for p,v in zip(probs,vals))) for j in [0,1,2])
for n in range(1,7):
 z,m,var=moments(n);check('binomial_complete_'+str(n),z==1);check('horizontal_phase_'+str(n),m==0);check('purification_variance_'+str(n),s.simplify(var-4*eta*n/(1-eta))==0)
# Rational calibration radius bridge reused on its actual working-pump formula.
mu=Q(10**28);e0=Q(1,10**25);baseline=Q(9386,10**15);target=Q(1,10**11);lo=4*mu*(e0-e0**3/6)**2;hi=4*mu*e0**2
check('success_implies_radius',lo-hi*hi/2>(target+baseline)**2)
N=3*10**27;d=3*e0;budget=4*N*d*d/Q(81,100)
check('necessary_loss_ratio',budget==Q(4,3*10**21))
check('confidence_budget',Q(43,45)-Q(1,200)>Q(95,100));check('confidence_loss',Q(1,6*10**29)*N==Q(1,200))
check('averaged_loss',Q(1,6*10**39)*N==Q(5,10**13));check('averaged_output',Q(9491,10**15)+Q(5,10**13)==Q(9991,10**15)<target)
# Exact fixed-shell pure loss Kraus maps into the complete triangular Fock space.
def kraus(N,et):
 states=[(n,r) for total in range(N+1) for n in range(total+1) for r in [total-n]];pos={a:i for i,a in enumerate(states)};Ks=[]
 for l in range(N+1):
  K=s.zeros(len(states),N+1)
  for n in range(l,N+1):K[pos[n-l,N-n],n]=s.sqrt(s.binomial(n,l))*et**s.Rational(n-l,2)*(1-et)**s.Rational(l,2)
  Ks.append(K)
 embed=s.zeros(len(states),N+1)
 for n in range(N+1):embed[pos[n,N-n],n]=1
 return Ks,embed
for nn in [1,2,3,4]:
 et=s.Rational(9,25);Ks,emb=kraus(nn,et)
 check('Kraus_complete_'+str(nn),sum((K.T*K for K in Ks),s.zeros(nn+1))==s.eye(nn+1))
 av=s.Matrix([s.Integer(j+1) for j in range(nn+1)]);av=av/s.sqrt((av.T*av)[0]);rho=emb*av*av.T*emb.T;out=sum((K*av*av.T*K.T for K in Ks),s.zeros(emb.rows));diff=np.array((out-rho).evalf(),dtype=float)
 dist=np.abs(np.linalg.eigvalsh(diff)).sum()/2;zz=sum(av[j]**2*et**s.Rational(j,2) for j in range(nn+1));yy=sum(av[j]**2*et**j for j in range(nn+1));form=(1-yy+s.sqrt((1+yy)**2-4*zz**2))/2
 check('finite_trace_norm_formula_'+str(nn),abs(dist-float(form))<1e-12)
 check('finite_channel_bound_'+str(nn),dist<=float(1-et**nn)+1e-12)
 fock=s.zeros(nn+1,1);fock[nn]=1;fo=sum((K*fock*fock.T*K.T for K in Ks),s.zeros(emb.rows));fr=emb*fock*fock.T*emb.T
 check('Fock_exact_saturation_'+str(nn),sum(abs((fo-fr)[j,j]) for j in range(emb.rows))/2==1-et**nn)
# Universal scalar comparison used in proof: direct polynomial identity.
r,u,v=s.symbols('r u v',real=True);z=r+u;y=r*r+v
check('continuity_polynomial',s.expand(z*z-r*r*(1+y-r*r))==2*r*u+u*u-r*r*v)
check('interval_coefficient',s.simplify(2-r*(1+r)-(1-r)*(r+2))==0)
# Fixed N4 code: corrects I,a, scalar projected number, live leakage generator.
code=s.zeros(5,2);code[0,0]=code[4,0]=1/s.sqrt(2);code[2,1]=1;num=s.diag(*range(5));proj=code*code.T
loss=s.zeros(4,5)
for n in range(1,5):loss[n-1,n]=s.sqrt(n)
check('code_isometry',code.T*code==s.eye(2));check('loss_KL',code.T*loss.T*loss*code==2*s.eye(2));check('projected_signal_scalar',code.T*num*code==2*s.eye(2))
leak=(s.eye(5)-proj)*num*code
check('raw_signal_leaks',leak!=s.zeros(5,2));check('raw_signal_variance',(code.T*num*num*code)[0,0]-4==4)
# Real changed machinery/reference controls. Baseline above must pass first.
Ks,emb=kraus(3,s.Rational(9,25));wrongK=Ks[:1];actual=sum((K.T*K for K in Ks),s.zeros(4));numwrong=num*num;mut_num=proj*num*proj
def leakage_of(op):return (s.eye(5)-proj)*op*code
def scalar2(mat):return mat[0,1]==0 and mat[1,0]==0 and mat[0,0]==mat[1,1]
check("actual_generator_leakage_oracle",leakage_of(num)==leak)
check("actual_projected_scalar_oracle",scalar2(code.T*num*code))
faults={
 'missing_phase_factor2':s.simplify(moments(3,enc=1)[2]-4*eta*3/(1-eta))!=0,
 'wrong_loss_denominator':moments(3,den=eta)[1]!=0,
 'discard_loss_outcomes':sum((K.T*K for K in wrongK),s.zeros(4))!=actual,
 'wrong_Kraus_amplitude':sum(((2*K).T*(2*K) for K in Ks),s.zeros(4))!=s.eye(4),
 'nonlinear_signal_not_scalar':not scalar2(code.T*numwrong*code),
 'erase_raw_code_leakage':leakage_of(mut_num)!=leak}
assert all(faults.values()),'[FAIL] undetected fault'
stem='k2318-loss-limited-calibration';deps=[f'explorations/conditional-build/{stem}-2026-10-30.md',str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2312-relational-finite-calibration-2026-10-30.md','explorations/conditional-build/k2315-calibration-control-cost-2026-10-30.md']
data=dict(schema_version='1.0',result_id='K2318',checks=len(checks),check_names=list(checks),mutation_failed_checks={n:['binomial_channel_or_code_equation'] for n in faults},evidence_kind='exact binomial/Kraus/code/rational controls; four finite numerical trace norms; universal bounds proved in note',dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},details={'necessary_loss_ratio':str(budget),'sufficient_confidence_loss':str(Q(1,6*10**29)),'sufficient_average_loss':str(Q(1,6*10**39))})
out=ROOT/'lab/process'/f'{stem}.json'
if '--write' in sys.argv:out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==data
print(json.dumps(dict(result='K2318',checks=len(checks),faults=len(faults))))
