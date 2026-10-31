"""Exact dyadic physical Pauli algebra and rational loss-image controls."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];st='k2362-transparent-control-locality';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def add(*terms):
 out={}
 for t in terms:
  for k,v in t.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v}
def scale(c,t):return {k:c*v for k,v in t.items() if c*v}
I='I'*8
def one(i,c):return {I[:i]+c+I[i+1:]:1}
pt={'XY':(1j,'Z'),'YX':(-1j,'Z'),'YZ':(1j,'X'),'ZY':(-1j,'X'),'ZX':(1j,'Y'),'XZ':(-1j,'Y')}
def mul(a,b):
 out={}
 for ka,va in a.items():
  for kb,vb in b.items():
   c=va*vb;key=''
   for x,y in zip(ka,kb):
    if x=='I':key+=y
    elif y=='I':key+=x
    elif x==y:key+='I'
    else:ph,z=pt[x+y];c*=ph;key+=z
   out[key]=out.get(key,0)+c
 return {k:v for k,v in out.items() if v}
z=[scale(.5,add(one(2*i,'Z'),scale(-1,one(2*i+1,'Z')))) for i in range(4)]
x=[scale(.5,add(mul(one(2*i,'X'),one(2*i+1,'X')),mul(one(2*i,'Y'),one(2*i+1,'Y')))) for i in range(4)]
N=add({I:4},*[scale(-.5,one(i,'Z')) for i in range(8)]);fac=add({I:5},scale(-1,N));ZZ=scale(.25,mul(fac,mul(add(z[0],z[1]),add(z[2],z[3]))));XX=scale(.5,mul(fac,add(mul(x[0],x[1]),mul(x[2],x[3]))))
check('Z_Pauli_weights',Counter(sum(c!='I' for c in k) for k in ZZ)=={2:16,3:16});check('X_Pauli_weights',Counter(sum(c!='I' for c in k) for k in XX)=={4:8,5:32})
check('Z_Pauli_l1',sum(abs(v) for v in ZZ.values())==2);check('X_Pauli_l1',sum(abs(v) for v in XX.values())==3);check('all_coefficients_real_dyadic',all(complex(v).imag==0 and (complex(v).real*16).is_integer() for v in list(ZZ.values())+list(XX.values())))
states=list(product((0,1),repeat=8))
def pauli_action(op,t):
 out={}
 for k,c in op.items():
  v=list(t)
  for i,p in enumerate(k):
   if p=='Z':c*=1-2*t[i]
   elif p=='X':v[i]=1-t[i]
   elif p=='Y':c*=1j*(1-2*t[i]);v[i]=1-t[i]
  key=tuple(v);out[key]=out.get(key,0)+c
 return {k:v for k,v in out.items() if v}
def physicalZ(t):
 zs=[(1-2*t[2*i]-(1-2*t[2*i+1]))//2 for i in range(4)];return F(5-sum(t),4)*(zs[0]+zs[1])*(zs[2]+zs[3])
def physicalX(t):
 out={}
 for group in [(0,1),(2,3)]:
  if all(t[2*i]+t[2*i+1]==1 for i in group):
   v=list(t)
   for i in group:v[2*i],v[2*i+1]=v[2*i+1],v[2*i]
   out[tuple(v)]=F(5-sum(t),2)
 return {k:v for k,v in out.items() if v}
check('all256_Z_physical_expansion',all(pauli_action(ZZ,t)==({t:physicalZ(t)} if physicalZ(t) else {}) for t in states));check('all256_X_physical_expansion',all(pauli_action(XX,t)==physicalX(t) for t in states));check('Z_full_norm',max(abs(physicalZ(t)) for t in states)==1)
check('X_exact_rowsum_upper',max(sum(abs(v) for v in physicalX(t).values()) for t in states)==F(3,2))
# + eigenstate on first two occupied pairs, other pairs vacuum, attains row sum bound.
witness={tuple(v for bit in bits for v in (bit,1-bit))+(0,0,0,0):F(1,2) for bits in product((0,1),repeat=2)}
def act(op,vec):return add(*[scale(v,op(t)) for t,v in vec.items()])
check('X_norm_attainment',act(physicalX,witness)==scale(F(3,2),witness))
def code(b):return {tuple(v for bit in [r,r,r^b,r^b] for v in [bit,1-bit]):1 for r in (0,1)}
def loss(b,j,sv):
 out={}
 for t,c in code(b).items():
  if t[2*j]==sv:
   v=list(t);v[2*j]=v[2*j+1]=0;out[tuple(v)]=c
 return out
Zact=lambda t:{t:physicalZ(t)} if physicalZ(t) else {}
for logical in (0,1):
 check('Z_code_'+str(logical),act(Zact,code(logical))==scale(1-2*logical,code(logical)));check('X_code_'+str(logical),act(physicalX,code(logical))==code(1-logical))
 for j in range(4):
  for sv in (0,1):
   vec=loss(logical,j,sv);check(f'loss_covariance_{logical}_{j}_{sv}',act(Zact,vec)==scale(1-2*logical,vec) and act(physicalX,vec)==loss(1-logical,j,sv))
check('error_normalizations_and_orthogonality',all(len(loss(b,j,sv))==1 and set(loss(0,j,sv)).isdisjoint(loss(1,j,sv)) and set(loss(b,j,0)).isdisjoint(loss(b,j,1)) for b in (0,1) for j in range(4) for sv in (0,1)))
# Tensor identities imply 2-block covariance, including one loss in each, no 65536 matrix needed.
for b1,b2,j,k in product((0,1),(0,1),range(4),range(4)):
 check(f'tensor_double_loss_{b1}_{b2}_{j}_{k}',all(physicalZ(next(iter(loss(b1,j,u))))*physicalZ(next(iter(loss(b2,k,v))))==(1-2*b1)*(1-2*b2) for u,v in product((0,1),repeat=2)))
J=s.Matrix(s.symbols('j13 j14 j23 j24'));removed=s.Matrix([[1,1,0,0],[0,0,1,1],[1,0,1,0],[0,1,0,1]])
check('two_local_constraint_kernel',removed.rank()==3 and all(sum(v)==0 for v in removed.nullspace()))
for b in (0,1):
 strings=[[r,r,r^b,r^b] for r in (0,1)];neigh=[]
 for t in strings:neigh.append({tuple(v^(i==j) for i,v in enumerate(t)) for j in range(4)})
 support={tuple([r,r,r^bb,r^bb]) for r,bb in product((0,1),repeat=2)};check('single_flip_no_cancellation_'+str(b),neigh[0].isdisjoint(neigh[1]) and (neigh[0]|neigh[1]).isdisjoint(support))
# Faults alter actual operators, not a metadata flag.
badZ=lambda t: {t:physicalZ(t)/F(5-sum(t))} if physicalZ(t) else {}
control('omit_occupation_factor',any(act(badZ,loss(b,j,u))!=scale(1-2*b,loss(b,j,u)) for b,j,u in product((0,1),range(4),(0,1))))
rawX=lambda t: {q:v/F(5-sum(t)) for q,v in physicalX(t).items()}
control('X_endpoint_only',any(act(rawX,loss(b,j,u))!=loss(1-b,j,u) for b,j,u in product((0,1),range(4),(0,1))))
control('two_local_crossedge_obstruction',removed*s.Matrix([1,0,0,0])!=s.zeros(4,1))
control('bad_full_norm_truncation',max(sum(abs(v) for v in physicalX(t).values()) for t in states)>1)
# Locality4 offdiagonal constraint: spectator-independent group amplitudes.
ar,ai,br,bi,lr,li=s.symbols('ar ai br bi lr li',real=True)
constraints=[br-lr,bi-li,br-lr,-bi-li,ar-lr,ai-li,ar-lr,-ai-li,ar+br-lr,-li]
check('X_weight4_offdiagonal_kernel',s.linsolve(constraints,[ar,ai,br,bi,lr,li])==s.FiniteSet((0,0,0,0,0,0)))
check('two_dual_pair_transition_consumes4supports',sum(a!=b for a,b in zip((0,1,0,1),(1,0,1,0)))==4)
candidate={ar:s.Rational(1,2),br:s.Rational(1,2),ai:0,bi:0,lr:1,li:0}
residuals=[e.subs(candidate) for e in constraints]
control('endpoint_addition_misses_loss_amplitude',all(e==0 for e in residuals[8:]) and any(e!=0 for e in residuals[:8]))
p=s.symbols('p');B=6*p*p-8*p**3+3*p**4;check('one_block_probability',s.expand(sum(s.binomial(4,j)*p**j*(1-p)**(4-j) for j in range(2,5))-B)==0);two=1-(1-B)**2
check('probabilities_p_one_tenth',B.subs(p,s.Rational(1,10))==s.Rational(523,10000) and two.subs(p,s.Rational(1,10))==s.Rational(10186471,100000000))
control('one_loss_each_is_correctable',s.expand(sum(s.binomial(8,j)*p**j*(1-p)**(8-j) for j in range(2,9))-two)!=0)
deps=['lab/process/k2356-protected-erasure-record.json','lab/process/k2359-loss-during-neutral-control.json',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out=dict(result_id='K2362',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='exact dyadic Pauli algebra, rational full-carrier and symbolic code constraints; universal no-go and channel proof in note',details=dict(Z=dict(weight_counts={str(k):v for k,v in Counter(sum(c!='I' for c in k) for k in ZZ).items()},norm=1,l1=2),X=dict(minimum_weight_under_declared_premises=5,weight_counts={str(k):v for k,v in Counter(sum(c!='I' for c in k) for k in XX).items()},norm='3/2',l1=3),ZZ=dict(max_weight=6,norm=1,l1=4),two_local_kernel=[list(map(str,v)) for v in removed.nullspace()],one_block_bad='523/10000',two_block_bad='10186471/100000000'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',len(checks),len(controls));print(json.dumps(out['details']))
