#!/usr/bin/env python3
"""Exact actual-port control and singular-safe ordered Euler fixtures."""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,json
from pathlib import Path
import sympy as S
from itertools import combinations
I=S.eye(32); Z=S.zeros(32); gam=[]
for sign in [1,-1]:
 for j in range(5):
  G=S.zeros(32)
  for mask in range(32):
   p=(-1)**((mask&((1<<j)-1)).bit_count())
   if not mask&(1<<j): G[mask|(1<<j),mask]=p
   else: G[mask^(1<<j),mask]=sign*p
  gam.append(G)
gam[4]=S.I*gam[4]
ids=[[m for m in range(32) if m.bit_count()%2==p] for p in range(2)]
def blade(inds):
 X=I
 for j in inds:X=X*gam[j-1]
 return X
w=blade([1,2,3])+blade([1,4,5])+2*blade([2,6,7])+3*blade([3,8,9])+5*blade([4,6,10])
u=2*blade([1,2,4])+3*blade([1,5,7])+5*blade([2,6,8])+7*blade([3,9,10])+11*blade([4,5,6])
IN=blade(list(range(1,11)));v=IN*w;t=S.I*u
P=7*v-15*t;bp=7*v+15*t
pm=P.extract(ids[0],ids[1]); pp=P.extract(ids[1],ids[0]);bm=bp.extract(ids[0],ids[1]);
print('commutator_nonzero',v*t-t*v!=Z,'anticommutator_nonzero',v*t+t*v!=Z,flush=True)
print('Pblock_dets',pm.det(),pp.det(),flush=True)
Y=(pm.inv()*bm).applyfunc(S.expand)
x=S.symbols('x');f=S.Poly(Y.charpoly(x).as_expr(),x)
print('CHARPOLY_COMPLETE',f.degree(),flush=True)
q=f.exquo(S.gcd(f,f.diff()))
print('square_root_degree',q.degree(),'square_identity',q*q==f,'squarefree',S.gcd(q,q.diff()).degree()==0,flush=True)
r=S.Poly(S.expand(x**8*S.conjugate(q.as_expr().subs(x,1/S.conjugate(x))))/S.conjugate(q.nth(0)),x)
print('opposite_coprime',S.gcd(q,r).degree()==0,'gcd_degree',S.gcd(q,r).degree(),flush=True)
print('q',q.as_expr(),flush=True)
print('r',r.as_expr(),flush=True)
# Euler rejection of this control, not merely a scope warning.
R=v+3*t;br=v-3*t
K=lambda X:sum(((1 if j<4 else -1)*gam[j]*X*gam[j] for j in range(10)),Z)
AA=3*K(br*br)+34*br*br+36*R*br+8*br*R-24*R*R
BB=184*R*R+140*R*br+184*br*R+194*br*br+24*K(br*R)+15*K(br*br)
Ac=AA.extract(ids[1],ids[1]);Bc=BB.extract(ids[1],ids[1]);C=5*Bc-Ac
res00=S.expand(4*sum(Ac[0,k]*Y[k,0] for k in range(16))-C[0,0])
print('Euler_residual_00',res00,flush=True)
# Baseline checks precede deliberate faults.
checks={'pencil_equation':(pm*Y-bm).applyfunc(S.expand)==S.zeros(16),
 'square_identity':q*q==f,'q_squarefree':S.gcd(q,q.diff()).degree()==0,
 'q_reciprocal_coprime':S.gcd(q,r).degree()==0,'Euler_rejects':res00!=0}
assert all(checks.values()),checks
Ybad=Y.copy();Ybad[0,0]+=1
faults={'Y_entry_fault':(pm*Ybad-bm).applyfunc(S.expand)!=S.zeros(16),
 'q_constant_fault':(q+S.Poly(1,x))**2!=f,
 'reciprocal_scaling_fault':S.expand(r.as_expr()*S.conjugate(q.nth(0))-x**8*S.conjugate(q.as_expr().subs(x,1/S.conjugate(x))))==0 and S.expand(r.as_expr()*(S.conjugate(q.nth(0))+1)-x**8*S.conjugate(q.as_expr().subs(x,1/S.conjugate(x))))!=0}
assert all(faults.values()),faults
print('baseline',checks,flush=True);print('faults',faults,flush=True)

# Strengthen the actual fixture beyond characteristic-square reporting.
qY=S.zeros(16)
for coefficient in q.all_coeffs(): qY=(qY*Y+coefficient*S.eye(16)).applyfunc(S.expand)
checks['actual_degree8_annihilator']=qY==S.zeros(16)
checks['actual_clifford_signature']=all(g*g==(1 if j<4 else -1)*I for j,g in enumerate(gam))
checks['actual_odd_pencils']=P.extract(ids[0],ids[0])==S.zeros(16) and P.extract(ids[1],ids[1])==S.zeros(16)
# Abstract Euler fixtures retain singular A: solve stacked systems exactly.
AA0=S.diag(1,0); CC0=S.diag(8,0); BA0=S.diag(0,3); BC0=S.diag(0,4)
MM=(4*AA0).col_join(BC0); NN=CC0.col_join(4*BA0)
ZZ=S.diag(2,3); LL=(MM.T*MM).inv()*MM.T
checks['singular_A_full_stack']=AA0.det()==0 and MM.rank()==2 and MM*ZZ==NN
checks['unique_left_inverse_reconstruction']=LL*NN==ZZ and MM*(LL*NN)==NN
checks['full_stack_image_equality']=MM.row_join(NN).rank()==MM.rank()==NN.rank()
MD=S.Matrix([[1,0],[0,0],[0,0],[0,0]]);ND=MD*S.diag(2,3)
checks['deficient_image_invertible_factor']=MD.rank()==1 and MD.row_join(ND).rank()==1 and MD*S.diag(2,3)==ND
# beta is identity in this real diagonal two-half example; the second half
# is forced inverse, rather than an independent arbitrary solution.
Zminus=ZZ.inv()
checks['paired_norm_one_completion']=4*BA0*Zminus==BC0 and CC0*Zminus==4*AA0 and ZZ*Zminus==S.eye(2)
assert all(checks.values()),[k for k,v in checks.items() if not v]
Nbad=NN.copy();Nbad[1,0]=1
faults['stacked_image_fault']=MM.row_join(Nbad).rank()>MM.rank()
faults['independent_opposite_half_fault']=ZZ*ZZ!=S.eye(2)
assert all(faults.values()),faults
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
root=Path(__file__).resolve().parents[2]
deps=['explorations/conditional-build/k2202-ordered-clifford-adapter-consequences-2026-10-28.md','explorations/conditional-build/k2197-general-ordered-adapter-constraints-2026-10-28.md','explorations/conditional-build/k2171-mixed-port-euler-filter-2026-10-27.md','explorations/conditional-build/k2205-ordered-pencil-real-constraints-2026-10-28.md']
report=dict(result_id='K2205',status='conditional_actual_port_countercontrol_and_Euler_reconstruction',checks={k:bool(v) for k,v in checks.items()},fault_failures={k:['corrupted equation rejected'] for k,v in faults.items() if v},q_coefficients=[str(a) for a in q.all_coeffs()],opposite_coefficients=[str(a) for a in r.all_coeffs()],pencil_block_determinants=[str(pm.det()),str(pp.det())],Euler_residual_00=str(res00),dependency_sha256={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal image-space/norm-one-completion proof; exact actual grade3/7 nonsolution spectral certificate; abstract singular-stack controls; equation/data faults. No full adapter solution, source verdict or physical claim.')
dst=root/'lab/process/k2205-ordered-pencil-real-constraints.json'
if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(dst.read_text())==report,'report drift'
print(json.dumps(dict(result='K2205',checks=len(checks),faults=len(faults))))
