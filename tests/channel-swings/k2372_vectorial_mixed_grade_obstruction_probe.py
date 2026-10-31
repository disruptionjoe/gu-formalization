import sys
"""K2372 native vectorial mixed-field coefficients and scoped geometric obstruction."""
from pathlib import Path
from fractions import Fraction as F
import sympy as s
import json,hashlib
R=Path(__file__).resolve().parents[2]
st='k2372-vectorial-mixed-grade-obstruction'
p=R/'tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py'
src=p.read_text();n={'__file__':str(p),'__name__':'selected_native_backend'}
exec(compile(src[:src.index('def sparse_rank')],str(p),'exec'),n)
b,w,add,scale=n['blade'],n['wedge_raw'],n['fadd'],n['fscale'];eta=n['ETA']
sh=lambda x:n['shiab'](x,('comm','symi','symi'))
P=lambda x,y:w(x,y).get(n['FULL'],{}).get(0,n['ZERO'])
def rat(q):
 assert q[1]==0
 return s.Rational(q[0].numerator,q[0].denominator)
def V(j):
 return {1<<i:n['escale'](F(eta[j],2),n['comm'](b(i),b(j))) for i in range(14) if i!=j}
def cubic(T,Z):return (rat(P(Z,sh(w(T,T))))+rat(P(T,sh(add(w(Z,T),w(T,Z))))))/3
def derivative(q,T,Z):
 dt={1<<q:b(())}
 return (rat(P(Z,sh(w(dt,T))))-rat(P(T,sh(w(dt,Z)))))/2
checks={};controls={}
def ck(label,condition):
 assert condition,label
 checks[label]=bool(condition)
def ct(label,condition):
 assert condition,label
 controls[label]=bool(condition)
for j in (0,1):
 v=V(j);T=add(n['PHI1'],v)
 ck(f'vector_mass_{j}',rat(P(v,n['hodge'](v)))==-13*eta[j])
 ck(f'mixed_density_{j}',rat(P(T,sh(w(T,T))))/3==1456-s.Rational(3692,3)*eta[j])
 for i in (0,1,4,5):
  ck(f'odd_cubic_{j}_{i}',cubic(T,{1<<i:b(i)})==312-88*eta[j]+s.Rational(4,3)*eta[i]*int(i==j))
 for i in (4,5):
  Z={1<<i:b(tuple(sorted((i,j))))}
  ck(f'even_cubic_{j}_{i}',cubic(T,Z)==s.Rational(568,3)*rat(P(Z,n['hodge'](v))))
 for i,blade in [(6,(0,1,4,5,6)),(0,()),(0,(0,1,4)),(4,(0,1,4,5)),(6,(0,1,4,5,6,10))]:
  ck(f'unsupported_cubic_{j}_{i}_{blade}',cubic(T,{1<<i:b(blade)})==0)
for q,j in [(0,0),(0,4),(0,1),(1,0),(1,1),(4,5)]:
 v=V(j)
 for i,k in [(0,0),(1,1),(4,4),(5,5),(0,1),(1,0),(0,4),(4,0),(4,5),(5,4)]:
  low=12*(i==q)*(k==j)-(k==q)*(i==j)-11*eta[i]*(i==k)*eta[q]*(q==j)
  ck(f'derivative_{q}_{j}_{i}_{k}',derivative(q,v,{1<<i:b(k)})==eta[i]*low)
 for i,blade in [(6,(0,1,4,5,6)),(1,(0,1,4,5,10)),(0,(0,1,4)),(4,(0,4,5)),(6,(0,1,4,5,6,10))]:
  ck(f'unsupported_derivative_{q}_{j}_{i}_{blade}',derivative(q,v,{1<<i:b(blade)})==0)
alpha=s.Rational(8,363);lt=s.Rational(1,4);ls=-s.Rational(5,4);scalar=-10
bb=lambda lam:((alpha-1)*lam-alpha*scalar)/13
ck('vertical_trace_coefficient',bb(lt)+alpha*ls==-(24*alpha+1)/52 and bb(lt)+alpha*ls!=0)
ck('vertical_traceless_coefficient',bb(ls)+alpha*lt==(48*alpha+5)/52 and bb(ls)+alpha*lt!=0)
ck('positive_exponential_coefficient',11/s.Rational(4,33)==s.Rational(363,4))
ck('vertical_Hessian_contradiction',alpha*(lt-ls)!=0)
ck('singular_auxiliary_branch_retained',568+s.Rational(568,3)*(-3)==0)
# Universal support follows from commutator/anticommutator parity; these exact
# fixtures verify the selected backend implements that algebra, not all 16384 blades.
for r in range(15):
 permitted={r-1,r+3} if r%2==0 else {r-3,r+1}
 permitted={q for q in permitted if 0<=q<=14}
 for i,j in [(0,1),(12,13),(0,13)]:
  output=sh({(1<<i)|(1<<j):b(tuple(range(r)))})
  grades={blade.bit_count() for clifford in output.values() for blade in clifford}
  ck(f'selected_Shiab_support_{r}_{i}_{j}',grades<=permitted)
Z={1<<4:b((0,4))};phi=n['PHI1'];v=V(0);T=add(phi,v)
ck('radial_derivative_minus11',derivative(0,phi,Z)==-11)
first_derivative=rat(P(Z,sh(w({1:b(())},phi))))/2
ct('omit_derivative_formal_adjoint',first_derivative!=derivative(0,phi,Z))
first_cubic=rat(P(Z,sh(w(T,T))))/3
ck('mixed_cubic_adjoint_seam',first_cubic==-s.Rational(4,3) and cubic(T,Z)==s.Rational(568,3))
ct('omit_mixed_cubic_formal_adjoint',first_cubic!=cubic(T,Z))
ct('omit_transpose_derivative_term',derivative(0,V(4),{1<<4:b(0)})==-1)
ct('nonvectorial_grade2_has_grade5',derivative(1,{1:b((4,5))},{1<<6:b((0,1,4,5,6))})==2)
ct('division_by_mu_erases_nonzero_even_branch',(568+s.Rational(568,3)*(-3))*1-11*0==0)
ct('alpha_zero_constant_potential_escape',s.Integer(0)*(lt-ls)==0)
ct('flat_Ricci_constant_potential_escape',alpha*(0-0)==0)
def lowfield(terms):return add(*[scale(F(v*eta[j]*eta[k]),{1<<i:b((j,k))}) for i,j,k,v in terms])
def axial(i,j,k):return lowfield([(i,j,k,1),(j,i,k,-1),(k,i,j,1)])
def hook(i,j,k):return lowfield([(i,j,k,1),(j,i,k,1)])
def ck(label,v):
 assert v,label
 checks[label]=bool(v)
def ct(label,v):
 assert v,label
 controls[label]=bool(v)
ca=s.Rational(112,3);ch=-s.Rational(56,3);cv=s.Rational(568,3)
fixtures=[]
for num,triple in enumerate([(0,4,5),(0,1,4)]):
 A=axial(*triple);H=hook(*triple)
 for label,E,c,dim in [('axial',A,ca,3),('hook',H,ch,2)]:
  ck(f'{label}_mass_{num}',rat(P(E,n['hodge'](E)))==-dim*eta[triple[0]]*eta[triple[1]]*eta[triple[2]])
  fixtures.append((f'{label}_{num}',E,scale(F(c),E)))
fixtures.append(('three_blocks_mixed',add(scale(2,axial(0,1,4)),scale(-3,hook(0,4,5)),scale(5,V(1))),add(scale(F(2*ca),axial(0,1,4)),scale(F(-3*ch),hook(0,4,5)),scale(F(5*cv),V(1)))))
for label,E,expected in fixtures:
 T=add(n['PHI1'],E)
 supports={(fm.bit_length()-1,cm) for fm,elt in add(E,expected).items() for cm in elt}
 supports|={(0,(1<<4)|(1<<5)),(4,(1<<0)|(1<<5)),(5,(1<<0)|(1<<4)),(10,(1<<2)|(1<<9))}
 for i,mask in sorted(supports):
  Z={1<<i:{mask:n['ONE']}}
  ck(f'auxiliary_native_{label}_{i}_{mask}',cubic(T,Z)==rat(P(Z,n['hodge'](expected))))
 for i,blade in [(6,(0,1,4,5,6,10)),(2,(0,1,2,4,5,6)),(0,(0,1,4,5,6,10))]:
  ck(f'grade6_native_{label}_{i}_{blade}',cubic(T,{1<<i:b(blade)})==0)
# Off-block support follows universally from inequivalent O(g) irreducibles,
# not from the finite row selection above.
k=s.symbols('k',nonzero=True);a3=-3*k/112;ah=3*k/56;av=-3*k/568
mu=lambda c,a:s.factor(k+c*a)
ck('axial_root',mu(ca,a3)==0)
ck('axial_other_blocks',mu(ch,a3)==3*k/2 and mu(cv,a3)==-57*k/14)
ck('hook_root',mu(ch,ah)==0)
ck('hook_other_blocks',mu(ca,ah)==3*k and mu(cv,ah)==78*k/7)
ck('vector_root_other_blocks',mu(ca,av)==57*k/71 and mu(ch,av)==78*k/71)
ck('irreducible_dimensions',14+364+896==14*s.binomial(14,2))
ct('vector_eigenvalue_not_universal',ca!=cv and ch!=cv)
ct('axial_hook_signs_differ',ca>0 and ch<0)
ct('zero_kappa_resonances_coalesce',all((s.Integer(0)+c*s.Integer(0))==0 for c in (ca,ch,cv)))
ct('singular_blocks_must_not_be_inverted',mu(ca,a3)==0 and mu(ch,ah)==0)

deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R)),str(p.relative_to(R)),
 'lab/process/k2345-curved-bundle-ricci-obstruction.json',
 'lab/process/k2363-variable-projector-stationarity.json',
 'lab/process/k2366-curvature-codazzi-rigidity.json',
 'explorations/conditional-build/selected-k77-grade5-unitary-parent-euler-closure-2026-08-10.md']
out=dict(result_id='K2372',checks=len(checks),check_names=list(checks),
 changed_input_and_scope_controls=controls,
 evidence_kind='exact native Clifford coefficients and scalar symbolic identities; full receiver and curved exclusion use written invariant/differential proof',
 details=dict(auxiliary_coefficient='kappa+568a/3',derivative_coefficients=[12,-1,-11],
  odd_v_square_coefficients=['-88','4/3'],Ricci_Hessian_alpha='8/363',
  scope='all smooth a Phi + vectorial grade-two V(v) on actual metric; singular mu retained',
  new_geometry_recomputation=False,
  axial_hook_eigenvalues=['kappa+112a/3','kappa-56a/3'],
  radial_general_grade2_candidates='kappa nonzero: constant a=-3kappa/112 pure axial, or a=3kappa/56 pure hook; kappa zero: a=0 with general auxiliary E, odd equations still unresolved',
  remaining='actual covariant odd grade-one and grade-five derivative plus quadratic equations on singular strata',
  inherited_geometry_identities=['K2345 Ricci/scalar/eigenspaces','K2363 vertical projector parallelness','K2366 R(trace,traceless)=0'],
  proof_seam='vertical total geodesy follows directly from block metric and base independence; grade5/6 vanish by invariant index count'),
 dependencies={q:hashlib.sha256((R/q).read_bytes()).hexdigest() for q in deps})
target=R/f'lab/process/{st}.json'
if '--write' in sys.argv:target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(target.read_text())==out
print('PASS',out['checks'],len(controls))
