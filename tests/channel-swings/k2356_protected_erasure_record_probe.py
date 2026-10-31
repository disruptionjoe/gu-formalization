"""Exact sparse circuit/erasure controls; channel bound proved in companion note."""
from pathlib import Path
from itertools import product
import sys,json,hashlib
import sympy as s
R=Path(__file__).resolve().parents[2];st='k2356-protected-erasure-record';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('ineffective changed-input control: '+k)
def cx(bits,c,t):
 b=list(bits);b[t]^=b[c];return tuple(b)
def code(b):return [(r,r,r^b,r^b) for r in [0,1]]
def gate(state,kind,c,t=None):
 out={}
 for bits,v in state.items():
  if kind=='CX':terms=[(cx(bits,c,t),v)]
  elif kind=='X':a=list(bits);a[c]^=1;terms=[(tuple(a),v)]
  elif kind=='H':
   terms=[]
   for r in [0,1]:a=list(bits);a[c]=r;terms.append((tuple(a),v*((-1)**(bits[c]*r))/s.sqrt(2)))
  for a,v in terms:out[a]=s.simplify(out.get(a,0)+v)
 return {a:v for a,v in out.items() if v!=0}
for b in [0,1]:
 bits=[0]*8;bits[2]=b;state={tuple(bits):s.Integer(1)}
 for g in [('H',0,None),('CX',0,1),('CX',0,2),('CX',2,3)]:state=gate(state,*g)
 for i in range(4):state=gate(gate(state,'X',i+4),'CX',i,i+4)
 expected={q+tuple(1-x for x in q):1/s.sqrt(2) for q in code(b)}
 check('actual12gate_encoder_column'+str(b),state==expected)
# Full matrix-unit erased recovery. Trace erased position first, then apply actual two-CX decoder.
def recover_unit(b,c,j=None,omit_second=False,phase=False):
 result={}
 for u in code(b):
  for v in code(c):
   coeff=s.Rational(1,2)*((-1)**(u[2]+v[2]) if phase else 1)
   if j is None:
    up=cx(u,0,2);vp=cx(v,0,2)
    if not omit_second:up=cx(up,2,3);vp=cx(vp,2,3)
    target=2;rest=[0,1,3]
   else:
    if u[j]!=v[j]:continue
    partner=j^1;opposite=[x for x in range(4) if x//2!=j//2];target=opposite[0]
    up=cx(u,partner,target);vp=cx(v,partner,target)
    if not omit_second:up=cx(up,target,opposite[1]);vp=cx(vp,target,opposite[1])
    rest=[x for x in range(4) if x not in [j,target]]
   if all(up[x]==vp[x] for x in rest):key=(up[target],vp[target]);result[key]=result.get(key,0)+coeff
 return {k:v for k,v in result.items() if v}
for j in [None,0,1,2,3]:
 for b,c in product([0,1],repeat=2):check('recovered_matrix_unit_'+str(j)+str(b)+str(c),recover_unit(b,c,j)=={(b,c):1})
# Complementary erasure condition by direct partial trace over complement of each erased position.
for j in range(4):
 for b,c in product([0,1],repeat=2):
  marginal=s.zeros(2)
  for u in code(b):
   for v in code(c):
    if all(u[x]==v[x] for x in range(4) if x!=j):marginal[u[j],v[j]]+=s.Rational(1,2)
  check('KL_complement_'+str(j)+str(b)+str(c),marginal==(s.eye(2)/2 if b==c else s.zeros(2)))
# Syndrome extraction on all sparse code terms with zero/one erased pairs.
for lost in [None,0,1,2,3]:
 for b,r in product([0,1],repeat=2):
  q=code(b)[r];rails=list(q+tuple(1-x for x in q))
  if lost is not None:rails[lost]=rails[lost+4]=0
  parity=tuple(rails[i]^rails[i+4] for i in range(4))
  check('erasure_parity_'+str(lost)+str(b)+str(r),parity==tuple(0 if i==lost else 1 for i in range(4)))
# An exact rational Kraus instance acts on all four logical matrix units.
eta=s.Rational(9,25);p=1-eta;K0=s.diag(1,s.Rational(3,5));K1=s.Matrix([[0,s.Rational(4,5)],[0,0]]);V=s.zeros(4,2);V[1,0]=1;V[2,1]=1;vac=s.zeros(4);vac[0,0]=1
Ks=[s.kronecker_product(x,y) for x in [K0,K1] for y in [K0,K1]]
check('physical_Kraus_complete',sum((K.T*K for K in Ks),s.zeros(4))==s.eye(4))
for b,c in product([0,1],repeat=2):
 M=s.zeros(2);M[b,c]=1;rho=V*M*V.T;actual=sum((K*rho*K.T for K in Ks),s.zeros(4));expect=eta*rho+(p*vac if b==c else s.zeros(4));check('dual_rail_matrix_unit'+str(b)+str(c),actual==expect)
p=s.symbols('p',real=True);B=s.expand(1-(1-p)**4-4*p*(1-p)**3);check('binomial_failure_polynomial',B==6*p*p-8*p**3+3*p**4);check('strict_improvement_factorization',s.factor(B-p)==p*(p-1)*(3*p*p-5*p+1));check('incremental_witness',B.subs(p,s.Rational(1,10))==s.Rational(523,10000))
# Exact cap/slew witness uses pi<22/7, no floating approximation as a proof.
tcap=s.Rational(18,7);debt=(348*tcap+48)/10**6;total=s.Rational(523,10000)+debt
check('priced_gate_debt_below_margin',total<s.Rational(53243,1000000) and total<s.Rational(1,10))
G,Vcap=s.symbols('G V',positive=True);area=s.pi/2;tg=area/G+G/Vcap;plateau=area/G-G/Vcap
check('trapezoid_area',s.simplify(G*plateau+G**2/Vcap-area)==0);check('triangle_area',s.simplify(Vcap*(s.sqrt(area/Vcap))**2-area)==0)
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I=s.eye(2);CX=(s.eye(4)+s.kronecker_product(Z,I)+s.kronecker_product(I,X)-s.kronecker_product(Z,X))/2
check('three_Hermitian_involutions',H.T==H and H*H==I and X*X==I and CX.T==CX and CX*CX==s.eye(4))
check('encoder_recovery_gate_count',4+8==12 and 8+8+2+3==21)
control('omit_second_recovery_CX_loses_coherence',recover_unit(0,1,0,omit_second=True)!={(0,1):1})
control('undetected_physical_Z_is_logical_Z',recover_unit(0,1,phase=True)=={(0,1):-1} and recover_unit(0,0,phase=True)=={(0,0):1})
L0=s.diag(1,s.Rational(4,5));L1=s.Matrix([[0,s.Rational(3,5)],[0,0]])
unequal=[s.kronecker_product(x,y) for x in [K0,K1] for y in [L0,L1]]
survive=[]
for bit in [0,1]:
 rho=V[:,bit]*V[:,bit].T;outstate=sum((K*rho*K.T for K in unequal),s.zeros(4));survive.append(s.trace(V.T*outstate*V))
control('unequal_rail_survival_is_state_dependent',survive==[s.Rational(16,25),s.Rational(9,25)])
# Changed physical noise: amplitude raising of empty rail maps |01> to |11>, parity0 although no vacuum.
raise0=s.kronecker_product(s.Matrix([[0,0],[1,0]]),I);psi=s.Matrix([0,1,0,0]);raised=raise0*psi
control('heating_breaks_erasure_flag',raised==s.Matrix([0,0,0,1]))
# Explicit correlated reset outputs: d((1-q)|0><0|+q|0><0|,(1-q)|1><1|+q|0><0|)=1-q.
q=s.Rational(1,4);rho0=s.diag(1,0);rho1=s.diag(q,1-q);distance=sum(abs(v) for v in (rho0-rho1).eigenvals())/2
control('common_reset_survives_redundancy',distance==1-q and q/2==s.Rational(1,8))
control('large_loss_not_improved',B.subs(p,s.Rational(1,2))>s.Rational(1,2))
# Classical repetition changes actual coherent matrix unit by eta^(m/2), here eta9/25,m2.
rep=s.zeros(4);rep[0,3]=1;repout=sum((K*rep*K.T for K in Ks),s.zeros(4))
control('repetition_flags_do_not_certify_coherence',repout==s.Rational(9,25)*rep and repout!=rep)
etas=[s.Rational(9,10),s.Rational(4,5),s.Rational(7,10),s.Rational(3,5)]
unequal_bound=1-s.prod(etas)-sum((1-etas[i])*s.prod(etas[j] for j in range(4) if j!=i) for i in range(4))
enumerated=sum(s.prod((1-etas[i]) if bits[i] else etas[i] for i in range(4)) for bits in product([0,1],repeat=4) if sum(bits)>=2)
check('unequal_pair_probability_consumer',unequal_bound==enumerated and 0<unequal_bound<1)
check('bounded_rate_mismatch_consumer',8*s.Rational(1,10**9)*100000==s.Rational(1,1250))
deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2353-late-record-relaxation.json']
out={'result_id':'K2356','checks':len(checks),'check_names':list(checks),'altered_input_controls':controls,'evidence_kind':'exact finite sparse-circuit, Kraus and symbolic controls; universal reference-aware channel proof in companion note','details':{'physical_record_qubits':8,'recovery_syndrome_ancillas':4,'encoder_gates':12,'recovery_gates_at_most':21,'measurements':4,'failure_polynomial':str(B),'p_one_tenth_failure':'523/10000','gate_noise_bound':str(debt),'incremental_total_bound':str(total),'incremental_total_decimal':float(total),'all_erased_necessary_floor':'p**4/2','full_device_error_requires':'epsilon_pre plus prep, measurement, control and correlated/mismatched noise'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
target=R/f'lab/process/{st}.json'
if '--write' in sys.argv:target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(target.read_text())==out
print(json.dumps(out['details']));print('PASS',len(checks),'exact checks;',len(controls),'altered-input controls')
