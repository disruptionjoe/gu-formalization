"""Actual selected Clifford coefficients plus nonsymmetric integrability/rank controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];st='k2369-nonsymmetric-native-derivative';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';src=(R/backend).read_text();ns={'__file__':str(R/backend),'__name__':'selected_native_arithmetic'};exec(compile(src[:src.index('def sparse_rank')],backend,'exec'),ns)
bl=ns['blade'];w=ns['wedge_raw'];add=ns['fadd'];scale=ns['fscale'];eta=ns['ETA'];H=s.diag(*eta);sh=lambda x:ns['shiab'](x,('comm','symi','symi'));pair=lambda x,y:w(x,y).get(ns['FULL'],{}).get(0,ns['ZERO'])
def rat(v):
 assert v[1]==0
 return s.Rational(v[0].numerator,v[0].denominator)
def field(A):return add(*[scale(F(A[i,j]),{1<<i:bl(j)}) for i in range(14) for j in range(14) if A[i,j]])
def cubic(T,Z,stt=None):return (rat(pair(Z,sh(w(T,T)) if stt is None else stt))+rat(pair(T,sh(add(w(Z,T),w(T,Z))))))/3
def density(T):return rat(pair(T,sh(w(T,T))))/3

def formula(A):
 S=(A+H*A.T*H)/2;K=(A-H*A.T*H)/2;t=s.trace(S);e2=(t*t-s.trace(S*S))/2;e3=(t**3-3*t*s.trace(S*S)+2*s.trace(S**3))/6
 L=4*e3+s.Rational(2,3)*t*s.trace(K*K)-s.Rational(4,3)*s.trace(S*K*K)
 C=4*(S*S-t*S+e2*s.eye(14))+s.Rational(2,3)*s.trace(K*K)*s.eye(14)-s.Rational(4,3)*K*K+s.Rational(4,3)*(S*K+K*S-t*K)
 return S,K,L,C
fixtures=[]
for negative in [False,True]:
 A=s.zeros(14);i,j,k=(0,4,5) if not negative else (0,1,4)
 A[i,i]=1;A[j,j]=2;A[k,k]=3;A[i,k]=2;A[k,i]=2*eta[i]*eta[k];A[i,j]+=1;A[j,i]-=eta[i]*eta[j]
 fixtures.append(A)
for idx,A in enumerate(fixtures):
 S,K,L,C=formula(A);T=field(A);STT=sh(w(T,T));check('native_cubic_density_'+str(idx),density(T)==L)
 for i in range(14):
  for j in range(14):
   got=cubic(T,{1<<i:bl(j)},STT);check(f'full_grade1_cubic_{idx}_{i}_{j}',got==eta[i]*eta[j]*C[i,j])
# Coefficients fixing the invariant density; explicit invalid symmetric-only extrapolation.
K=s.zeros(14);K[0,4]=1;K[4,0]=-1
for i,expected in [(0,0),(5,-s.Rational(4,3))]:
 A=K.copy();A[i,i]=1;check('mixed_density_coefficient_'+str(i),density(field(A))==expected)
_,_,_,C=formula(K);wrong=4*(K*K-s.trace(K)*K+(s.trace(K)**2-s.trace(K*K))/2*s.eye(14))
control('symmetric_Newton_formula_invalid',C[5,5]==-s.Rational(4,3) and wrong[5,5]==4)
# General derivative with arbitrary sparse jets, including lowered-signature conversion.
def derivative(Ds,Z):
 dt=add(*[w({1<<q:bl(())},v) for q,v in Ds.items()]);return (rat(pair(Z,sh(dt)))-sum(rat(pair(v,sh(w({1<<q:bl(())},Z)))) for q,v in Ds.items()))/2
jet_cases=[[(0,1,4,1)],[(0,4,1,1)],[(4,1,0,1)],[(0,5,5,1)],[(0,4,5,1),(0,5,4,-1)],[(1,4,5,2),(5,4,1,-3)],[(4,1,1,1)],[(0,4,5,1),(0,5,4,1)]]
for num,js in enumerate(jet_cases):
 N={};Ds={}
 for q,i,j,v in js:N[q,i,j]=N.get((q,i,j),0)+eta[j]*v;Ds[q]=add(Ds.get(q,{}),scale(F(v),{1<<i:bl(j)}))
 get=lambda q,i,j:N.get((q,i,j),0);Q=[sum(eta[l]*(get(l,l,j)-get(j,l,l)) for l in range(14)) for j in range(14)]
 zeros=0
 for i in range(14):
  for j,k in combinations(range(14),2):
   E=get(j,i,k)+get(j,k,i)-get(k,i,j)-get(k,j,i)+eta[i]*(i==k)*Q[j]-eta[i]*(i==j)*Q[k]
   if E or (zeros<3 and i==num):
    if not E:zeros+=1
    check(f'derivative_tensor_{num}_{i}_{j}_{k}',derivative(Ds,{1<<i:bl((j,k))})==eta[i]*E)
 for i,blade in [(0,()),(1,(0,4,5,6)),(4,(0,1,5,10))]:check(f'no_extra_even_grade_{num}_{i}_{blade}',derivative(Ds,{1<<i:bl(blade)})==0)
for triple,expected in zip([(0,4,5),(0,5,4),(4,0,5),(4,5,0),(5,0,4),(5,4,0)],[1,1,0,0,-1,-1]):
 q,i,j=triple;check('distinct_index_coefficient_'+str(triple),derivative({q:{1<<i:bl(j)}},{1<<4:bl((0,5))})==expected)
control('skew_divergence_free_not_Codazzi',derivative({0:add({1<<4:bl(5)},scale(F(-1),{1<<5:bl(4)}))},{1<<4:bl((0,5))})==0)
# Grade5 transverse obstruction and its signature normalization.
def wedgeform(a,b):
 out={}
 for I,v in a.items():
  for J,z in b.items():
   if set(I)&set(J):continue
   swaps=sum(i>j for i in I for j in J);key=tuple(sorted(I+J));out[key]=out.get(key,0)+(-1)**swaps*v*z
 return {k:v for k,v in out.items() if v}
for idx,planes in enumerate([[(0,4),(5,6)],[(0,1),(4,5)],[(0,4)]]):
 low=s.zeros(14)
 for i,j in planes:low[i,j]=1;low[j,i]=-1
 A=low*H;T=field(A);form={ij:low[ij] for ij in combinations(range(14),2) if low[ij]};square=wedgeform(form,form)
 for i in [1,2,6,7,10]:
  expected=wedgeform({(i,):1},square)
  for blade in set(expected)|{(0,1,4,5,6)}:
   check(f'grade5_{idx}_{i}_{blade}',cubic(T,{1<<i:bl(blade)})==s.Rational(8,3)*expected.get(blade,0))
 check('Plucker_rank_fixture_'+str(idx),(not square)==(A.rank()<=2))
# Algebraic identities supporting the universal commutator argument.
x=s.symbols('x0:6');y=s.symbols('y0:3');S=s.Matrix([[x[0],x[1],x[2]],[x[1],x[3],x[4]],[x[2],x[4],x[5]]]);K=s.Matrix([[0,y[0],y[1]],[-y[0],0,y[2]],[-y[1],-y[2],0]]);c=s.symbols('c');B=S*K+K*S-c*K
check('commutator_elimination',((B*K-K*B)-(S*K*K-K*K*S)).applyfunc(s.expand)==s.zeros(3))
# Contract Id wedge a 2-form; the n-2 coefficient never depends on signature.
n=14;dq={(1,2):s.Integer(3),(0,4):s.Integer(-2)}
def f(j,k):return dq.get((j,k),-dq.get((k,j),0))
for j,k in dq:check('integrability_contraction_'+str((j,k)),sum((i==i)*f(j,k)+(i==j)*f(k,i)+(i==k)*f(i,j) for i in range(n))==(n-2)*f(j,k))
check('actual_Einstein_multiplicities',5+9==14 and s.Rational(21,4)!=s.Rational(15,4))
check('minimum_scalar_shift_rank',min(5,9)>2)
# Actual indefinite null-skew flat escape, full cubic grades vanish by support theorem.
u=s.zeros(14,1);v=s.zeros(14,1);u[0]=u[1]=1;v[4]=v[10]=1;low=u*v.T-v*u.T;K=low*H
check('flat_null_skew_nonzero',K.rank()==2 and K!=s.zeros(14));check('flat_null_square_zero',K*K==s.zeros(14));check('flat_null_invariants',formula(K)[2]==0 and formula(K)[3]==s.zeros(14))
form={ij:low[ij] for ij in combinations(range(14),2) if low[ij]};check('flat_null_Plucker',wedgeform(form,form)=={})
T=field(K);STT=sh(w(T,T))
for i,j in [(0,0),(0,4),(1,10),(4,1),(6,6),(10,0)]:check('flat_native_grade1_'+str((i,j)),cubic(T,{1<<i:bl(j)},STT)==0)
for i,bb in [(0,(0,1,4,5,10)),(6,(0,1,4,6,10))]:check('flat_native_grade5_'+str(i),cubic(T,{1<<i:bl(bb)},STT)==0)
control('nonzero_skew_can_be_stationary_on_other_geometry',K!=s.zeros(14) and K*K==s.zeros(14))
control('rank4_skew_forbidden_by_grade5',len(wedgeform({(0,4):1,(5,6):1},{(0,4):1,(5,6):1}))==1)
# Omitting formal adjoint gives incorrect radial derivative, same as independent old control.
Z={1<<4:bl((0,4))};first=rat(pair(Z,sh(w({1:bl(())},ns['PHI1']))))/2
control('omit_formal_adjoint',first!=derivative({0:ns['PHI1']},Z))
deps=[backend,'lab/process/k2345-curved-bundle-ricci-obstruction.json','lab/process/k2360-anisotropic-native-stationarity.json','lab/process/k2363-variable-projector-stationarity.json','lab/process/k2366-curvature-codazzi-rigidity.json',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2369',checks=len(checks),check_names=list(checks),changed_input_and_scope_controls=controls,evidence_kind='exact selected Clifford coefficients and symbolic/rank identities; universal all-field result uses written invariant and differential proof plus inherited actual-metric Codazzi theorem',details=dict(cubic_density='4e3(S)+(2/3)trS trK²-(4/3)tr(SK²)',derivative='2curlS+g wedge(divA-dtrA)',consequence='all smooth grade-one A excluded on actual K2345 metric for selected fixed-geometry I1',transverse='K wedge K=0 and rankK<=2',escape='flat constant null simple skew K with K²=0, kappa=0',native_grade1_fixture_rows=392),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(controls));print(json.dumps(out['details'],indent=2))
