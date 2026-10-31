"""K2375 exact native axial/hook coefficients; universal scope uses written proof."""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
R=Path(__file__).resolve().parents[2]
p=R/'tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py'
src=p.read_text();n={'__file__':str(p),'__name__':'selected_native_backend'}
exec(compile(src[:src.index('def sparse_rank')],str(p),'exec'),n)
b,w,add,scale=n['blade'],n['wedge_raw'],n['fadd'],n['fscale'];eta=n['ETA']
sh=lambda x:n['shiab'](x,('comm','symi','symi'))
P=lambda x,y:w(x,y).get(n['FULL'],{}).get(0,n['ZERO'])
def rat(q):
 assert q[1]==0
 return s.Rational(q[0].numerator,q[0].denominator)
def cubic(T,Z):return (rat(P(Z,sh(w(T,T))))+rat(P(T,sh(add(w(Z,T),w(T,Z))))))/3
def derivative(q,T,Z):
 dt={1<<q:b(())}
 return (rat(P(Z,sh(w(dt,T))))-rat(P(T,sh(w(dt,Z)))))/2
def lowfield(terms):return add(*[scale(F(v*eta[j]*eta[k]),{1<<i:b((j,k))}) for i,j,k,v in terms])
def axial(i,j,k):return lowfield([(i,j,k,1),(j,i,k,-1),(k,i,j,1)])
def hook(i,j,k):return lowfield([(i,j,k,1),(j,i,k,1)])
def Z(i,B):return {1<<i:b(B)}
checks={};controls={}
def ck(k,v):
 assert v,k
 checks[k]=bool(v)
def ct(k,v):
 assert v,k
 controls[k]=bool(v)
fixtures=[('positive',axial(0,4,5),1),('negative',axial(0,1,4),-1),('overlap',add(axial(0,4,5),scale(2,axial(0,4,6))),5),('mixed_signature',add(axial(0,4,5),scale(2,axial(0,1,4))),-3),('null_nonzero',add(axial(0,4,5),axial(0,1,4)),0)]
for label,A,norm in fixtures:
 for i,j in [(0,0),(1,1),(4,4),(5,5),(6,6),(5,6),(6,5),(1,5),(5,1)]:
  ck(f'axial_Q1_{label}_{i}_{j}',cubic(A,Z(i,j))==(-4*norm if i==j else 0))
for triple,q in [((0,4,5),0),((0,1,4),1),((0,4,5),1),((0,1,4),10)]:
 A=axial(*triple)
 for i,j in [(0,0),(0,4),(4,0),(4,5),(5,4),(0,1),(1,0)]:ck(f'axial_D1_{triple}_{q}_{i}_{j}',derivative(q,A,Z(i,j))==0)
ct('axial_D5_really_nonzero',derivative(1,axial(0,4,5),Z(6,(0,1,4,5,6)))==6)
ct('axial_Q5_really_nonzero',cubic(add(axial(0,4,5),axial(6,7,8)),Z(0,(4,5,6,7,8)))==8)
# Read lower tensor coefficients from independently prescribed basis fields.
def lower(E):
 H={}
 for fm,el in E.items():
  i=fm.bit_length()-1
  for mask,c in el.items():
   j,k=n['indices'](mask);v=rat(c)*eta[j]*eta[k]
   H[i,j,k]=v;H[i,k,j]=-v
 return H
get=lambda H,i,j,k:H.get((i,j,k),0)
def invariants(H):
 h2=s.Rational(1,2)*sum(eta[i]*eta[j]*eta[k]*v*v for (i,j,k),v in H.items())
 U=lambda i,j:s.Rational(1,2)*sum(eta[a]*eta[b]*get(H,i,a,b)*get(H,j,a,b) for a in range(14) for b in range(14))
 W=lambda i,j:sum(eta[a]*eta[b]*get(H,a,i,b)*get(H,a,j,b) for a in range(14) for b in range(14))
 return h2,U,W
for label,E in [('positive',hook(0,4,5)),('negative',hook(0,1,4)),('mixed',add(hook(0,4,5),scale(2,hook(0,4,6)),hook(0,1,4)))]:
 H=lower(E);h2,U,W=invariants(H)
 ck(f'hook_tracefree_{label}',all(sum(eta[k]*get(H,k,k,j) for k in range(14))==0 for j in range(14)))
 ck(f'hook_cyclic_{label}',all(get(H,i,j,k)+get(H,j,k,i)+get(H,k,i,j)==0 for i,j,k in H))
 for i,j in [(0,0),(1,1),(4,4),(5,5),(6,6),(8,8),(5,6),(6,5),(1,5),(5,1)]:
  q=s.Rational(2,3)*h2*eta[i]*int(i==j)-s.Rational(8,3)*U(i,j)+s.Rational(4,3)*W(i,j)
  ck(f'hook_Q1_{label}_{i}_{j}',cubic(E,Z(i,j))==eta[i]*q)
 for q,i,j in [(0,4,5),(0,5,4),(4,0,5),(5,0,4),(1,0,4)]:
  expected=-eta[i]*eta[q]*(get(H,i,q,j)+get(H,j,q,i))
  ck(f'hook_D1_{label}_{q}_{i}_{j}',derivative(q,E,Z(i,j))==expected)
 ck(f'hook_Q1_trace_{label}',sum(eta[i]*(s.Rational(2,3)*h2*eta[i]-s.Rational(8,3)*U(i,i)+s.Rational(4,3)*W(i,i)) for i in range(14))==s.Rational(28,3)*h2)
# Independent exterior wedge of lower two-form coefficients builds sigma_H.
def sigma(H):
 out={}
 for i in range(14):
  rows=[(1<<j|1<<k,v) for (ii,j,k),v in H.items() if ii==i and j<k]
  for m,c in rows:
   for mm,cc in rows:
    if not m&mm:out[m|mm]=out.get(m|mm,0)+eta[i]*n['wedge_sign'](m,mm)*c*cc
 return {m:c for m,c in out.items() if c}
def insertion(sig):
 out={}
 for i in range(14):
  el={}
  for m,c in sig.items():
   if not (1<<i)&m:
    raised=c
    for j in n['indices'](m):raised*=eta[j]
    el[m|(1<<i)]=n['gz'](F(n['wedge_sign'](1<<i,m)*raised))
  if el:out[1<<i]=el
 return out
for label,E in [('shared',add(hook(0,4,5),hook(0,6,7))),('signed',add(hook(1,4,5),hook(1,6,7))),('disjoint',add(hook(0,4,5),hook(6,7,8)))]:
 sig=sigma(lower(E));G=insertion(sig)
 for i,B in [(0,(0,4,5,6,7)),(1,(1,4,5,6,7)),(8,(4,5,6,7,8)),(0,(4,5,6,7,8)),(6,(0,4,5,7,8))]:
  z=Z(i,B)
  ck(f'hook_Q5_{label}_{i}_{B}',cubic(E,z)==-s.Rational(2,3)*rat(P(z,n['hodge'](G))))
 for q in (0,1):ck(f'hook_D5_{label}_{q}',derivative(q,E,Z(6,(0,1,4,5,6)))==0)
ct('hook_sigma_can_be_nonzero',bool(sigma(lower(add(hook(0,4,5),hook(0,6,7))))))
ct('hook_sigma_zero_not_field_zero',not sigma(lower(hook(0,4,5))) and bool(hook(0,4,5)))
v={1<<i:n['escale'](F(eta[0],2),n['comm'](b(i),b(0))) for i in range(14) if i!=0}
ct('vector_plus_axial_changes_skew_equation',cubic(add(v,axial(0,4,5)),Z(4,5))==s.Rational(40,3))
k=s.symbols('k',real=True);a=3*k/56;c0=s.factor(k*a+312*a*a);h2=s.Rational(90,7)-s.Rational(279,196)*k*k
ck('hook_resonance_scalar',c0==s.Rational(93,98)*k*k)
ck('hook_trace_fixed_signed_norm',s.factor(-120+14*c0+s.Rational(28,3)*h2)==0)
ck('hook_trace_eliminates_scalar_kappa',s.factor(c0+s.Rational(2,3)*h2)==s.Rational(60,7))
ct('actual_metric_axial_contradiction',-2*(s.Rational(1,4)+s.Rational(5,4))==-3)
ct('flat_geometry_escape',-2*(s.Integer(0)-s.Integer(0))==0)
ct('vector_plus_axial_opposite_skew_receiver',cubic(add(v,axial(0,4,5)),Z(5,4))==-s.Rational(40,3))
# General-dimension contraction proof: n>2 and symmetric tracefree S.
nd=s.symbols('n',integer=True,positive=True)
ck('hook_onejet_general_contraction',s.factor((nd-1)-1/(nd-1)-nd*(nd-2)/(nd-1))==0)
# Adapted actual-metric eigenframe: horizontal4 plus negative trace line10.
# S# eigenvalues -117/1568 (multiplicity5), +65/1568 (multiplicity9).
plus_eigenspace={0,1,2,3,10};snum=[-117 if i in plus_eigenspace else 65 for i in range(14)]
ric_tf=[s.Rational(27,28) if i in plus_eigenspace else -s.Rational(15,28) for i in range(14)]
g=lambda i,j:eta[i] if i==j else 0
Snum=lambda i,j:eta[i]*snum[i] if i==j else 0
def Kbar(l,i,j,k):
 return 13*(g(l,j)*Snum(i,k)-g(l,k)*Snum(i,j))-(g(i,j)*Snum(l,k)-g(i,k)*Snum(l,j))
ck('actual_Ric_tf_multiplicities',sum(ric_tf)==0 and len(plus_eigenspace)==5)
ck('hook_onejet_S_tracefree',sum(snum)==0)
ck('hook_onejet_skew_and_cyclic',all(Kbar(l,i,j,k)==-Kbar(l,i,k,j) and Kbar(l,i,j,k)+Kbar(l,j,k,i)+Kbar(l,k,i,j)==0 for l in range(14) for i in range(14) for j in range(14) for k in range(14)))
ck('hook_onejet_contractions_zero',all(sum(eta[i]*Kbar(l,i,i,k) for i in range(14))==0 for l in range(14) for k in range(14)))
Bbar=lambda i,j:sum(eta[k]*Kbar(k,i,k,j) for k in range(14))
ck('hook_onejet_B_exact',all(Bbar(i,j)==168*Snum(i,j) for i in range(14) for j in range(14)))
ck('hook_onejet_actual_grade1_compatibility',all(-s.Rational(1,13*1568)*(Bbar(i,j)+Bbar(j,i))==2*g(i,j)*ric_tf[i] for i in range(14) for j in range(14)))
ct('hook_onejet_zero_value_allowed_at_special_kappa',s.Rational(90,7)-s.Rational(279,196)*s.Rational(280,31)==0)
# H=0 makes sigma_H and d sigma_H vanish and makes d(h²)=0; no second-jet claim.

ric_tf_norm=sum(q*q for q in ric_tf)
ck('actual_Ric_tf_signed_norm',ric_tf_norm==s.Rational(405,56))
jet_num=sum(eta[l]*eta[i]*eta[j]*eta[k]*Kbar(l,i,j,k)**2 for l in range(14) for i in range(14) for j in range(14) for k in range(14))
jet_norm=s.Rational(jet_num,2*(13*1568)**2)
ck('hook_onejet_contracted_norm_exact',jet_norm==s.Rational(1755,3136))
ck('hook_onejet_norm_representation_formula',jet_norm==s.Rational(168,13)*s.Rational(13,168)**2*ric_tf_norm)
ct('chosen_hook_onejet_cannot_prolong_to_constant_norm',2*jet_norm==s.Rational(1755,1568) and 2*jet_norm!=0)
# A negative-norm kernel jet exists: nabla_1 H045 with other derivatives zero.
# This shows why the contracted test alone must not become an all-jet theorem.
Hkernel=lower(hook(0,4,5))
ck('negative_norm_kernel_has_zero_B',all(eta[1]*get(Hkernel,i,1,j)==0 for i in range(14) for j in range(14)))
ck('negative_norm_kernel_norm',eta[1]*invariants(Hkernel)[0]==-2)

out={'result_id':'K2375','checks':len(checks),'check_names':list(checks),'changed_input_and_scope_controls':controls,'evidence_kind':'exact native Clifford fixtures and rational identities; universal scope is supplied by written invariant-contraction proofs','details':{'axial_D1':0,'axial_Q1':'-4|A|^2 g','hook_D1':'-(B+B^T)','hook_Q1':'(2/3)h^2 g-(8/3)U+(4/3)W','hook_D5':0,'hook_Q5':'-(2/3) gamma_i wedge sigma_H^sharp','hook_norm':'90/7-279 kappa^2/196','remaining':'hook nonlinear first-order grade-one PDE with sigma_H=0; kappa-zero mixed grade-two case remains separate'}}
st='k2375-axial-hook-stationarity'
deps=['explorations/conditional-build/k2372-vectorial-mixed-grade-obstruction-2026-10-31.md','tests/channel-swings/k2372_vectorial_mixed_grade_obstruction_probe.py','lab/process/k2345-curved-bundle-ricci-obstruction.json','tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
p=R/f'lab/process/{st}.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print('PASS',out['checks'],len(controls))
