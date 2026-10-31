"""Exact circuit and cross-time correction controls; theorem in companion note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys,itertools
R=Path(__file__).resolve().parents[2];st='k2359-loss-during-neutral-control';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('ineffective control '+k)
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);kron=s.kronecker_product
# Pair encoding |b> -> |b,1-b>.
W=s.zeros(4,2);W[1,0]=1;W[2,1]=1;N=s.diag(0,1,1,2);ex=(kron(X,X)+kron(Y,Y))/2;zq=kron(Z,I)
check('exchange_restricts_to_X',W.T*ex*W==X);check('local_Z_restricts_to_Z',W.T*zq*W==Z);check('number_preserving_exchange',ex*N==N*ex);check('number_preserving_Z',zq*N==N*zq)
H=(ex+zq)/s.sqrt(2);check('encoded_Hadamard',W.T*H*W==(X+Z)/s.sqrt(2));check('full_H_norm_one',max(abs(x) for x in H.eigenvals())==1)
W2=kron(W,W);ZZ=kron(zq,zq);check('physical_two_body_encoded_entangler',W2.T*ZZ*W2==kron(Z,Z))
# Code V and loss maps A_s, retaining three surviving pairs.
V=s.zeros(16,2)
def bits(b,r):return (r,r,r^b,r^b)
def num(q):return sum(x<<(len(q)-1-i) for i,x in enumerate(q))
for b,r in itertools.product(range(2),repeat=2):V[num(bits(b,r)),b]=1/s.sqrt(2)
A=[]
for lossbit in range(2):
 mat=s.zeros(8,2)
 for b,r in itertools.product(range(2),repeat=2):
  q=bits(b,r)
  if q[0]==lossbit:mat[num(q[1:]),b]=1/s.sqrt(2)
 A.append(mat)
physical=s.diag(*[(-1)**(q[0]+q[2]) for q in itertools.product(range(2),repeat=4)]);survive=s.diag(*[(-1)**q[1] for q in itertools.product(range(2),repeat=3)])
check('logical_Z_on_code',physical*V==V*Z)
for b in range(2):
 check('erasure_scalar_KL_'+str(b),A[b].T*A[b]==I/2);check('postloss_generator_'+str(b),survive*A[b]==(-1)**b*A[b]*Z)
check('orthogonal_syndrome',A[0].T*A[1]==s.zeros(2))
phi,psi,theta=s.symbols('phi psi theta',real=True)
U=lambda x:s.diag(s.exp(-s.I*x),s.exp(s.I*x))
for b in range(2):
 E=s.exp(-s.I*(theta-phi)*survive)*A[b]*U(phi);target=A[b]*U(phi+(-1)**b*(theta-phi));check('full_jump_propagation_'+str(b),s.simplify(E-target)==s.zeros(8,2))
K=s.simplify((A[1]*U(2*phi-theta)).conjugate().T*(A[1]*U(2*psi-theta)))
check('cross_time_KL_formula',s.simplify(K-U(2*(psi-phi))/2)==s.zeros(2))
control('unknown_jump_time_not_scalar',s.simplify(K.subs({phi:0,psi:s.pi/8})[0,0]-K.subs({phi:0,psi:s.pi/8})[1,1])!=0)
# Actual midpoint output of named decoder; exact trace distance from ideal on |+>.
rho=s.ones(2)/2;ideal=s.simplify(U(s.pi/4)*rho*U(s.pi/4).H);mixed=(ideal+rho)/2;err=s.simplify(sum(abs(x) for x in (mixed-ideal).eigenvals())/2)
check('midgate_exact_trace_error',err==s.sqrt(2)/4)
control('idle_erasure_not_gate_erasure',mixed!=ideal)
for b in range(2):
 ang=phi+(-1)**b*(theta-phi);check('timestamp_and_syndrome_feedforward_'+str(b),s.simplify(U(theta-ang)*U(ang)-U(theta))==s.zeros(2))
# Error-transparent sector operator: ternary pair states 0,1,2(erased).
# In each zero/one-loss sector choose surviving i from {0,1}, k from {2,3}.
# All other sectors have H=0. Orthogonal projectors make ||H||=1.
vals=[]
for q in itertools.product(range(3),repeat=4):
 lost=[i for i,v in enumerate(q) if v==2]
 val=0
 if len(lost)<=1:
  i=next(i for i in [0,1] if q[i]!=2);k=next(i for i in [2,3] if q[i]!=2);val=(-1)**(q[i]+q[k])
 vals.append(val)
check('transparent_sector_norm',max(abs(v) for v in vals)==1)
for lost in [None,0,1,2,3]:
 for b,r in itertools.product(range(2),repeat=2):
  q=list(bits(b,r))
  if lost is not None:q[lost]=2
  ix=sum(q[i]*3**(3-i) for i in range(4));check('transparent_all_code_loss_images_'+str(lost)+str(b)+str(r),vals[ix]==(-1)**b)
# Changed primitive: always choose original pair0 and pair2; vacuum has physical Z=+1.
q=[2,1,0,0];bad=(-1)**(0+q[2]);good=vals[sum(q[i]*3**(3-i) for i in range(4))]
control('omit_sector_conditioning',bad!=good)
# Preparation constraint from actual number eigenvalues.
check('code_has_four_excitations',all(sum(q+tuple(1-v for v in q))==4 for q in [bits(b,r) for b,r in itertools.product(range(2),repeat=2)]))
control('vacuum_injection_not_number_preserving',N*s.Matrix([1,0,0,0])==s.zeros(4,1) and N*W[:,0]!=s.zeros(4,1))
G,Vcap,area=s.symbols('G Vcap area',positive=True);plateau=area/G-G/Vcap;check('trapezoid_area',s.simplify(G*plateau+G**2/Vcap-area)==0)
deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),'lab/process/k2356-protected-erasure-record.json']
out=dict(result_id='K2359',checks=len(checks),check_names=list(checks),altered_input_controls=controls,evidence_kind='exact finite matrix, symbolic and code-image checks; cross-time and transparent-control proofs in note',details=dict(code_qubits=8,midgate_trace_error=str(err),unknown_time_exact_correction=False,transparent_extension_norm=1,transparent_extension='sector-conditioned many-body primitive, not supplied two-body gate',preparation='four excitations and encoded input require independent preparation',timing='known jump phase plus retained syndrome suffices; phase uncertainty epsilon gives conditional branch distance at most 2epsilon'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps(out['details']));print('PASS',len(checks),len(controls))
