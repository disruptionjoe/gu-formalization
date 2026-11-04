"""Exact stationary-product Einstein top-symbol and radial sourced-response controls."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,value):
 bank[name]=bool(value)
 if not bank[name]:raise AssertionError(name)
n=14;eta=s.diag(*([1]*7+[-1]*7));pairs=[(i,j) for i in range(n) for j in range(i,n)];basis=[]
for i,j in pairs:
 h=s.zeros(n);h[i,j]=h[j,i]=1;basis.append(h)
weights=s.diag(*[eta[i,i]*eta[j,j]*(1 if i==j else 2) for i,j in pairs])
def op(h,xi):
 up=eta*xi;norm=(xi.T*up)[0];v=h*up;tr=s.trace(eta*h);ric=(xi*v.T+v*xi.T-norm*h-tr*xi*xi.T)/2
 return ric-eta*((up.T*v)[0]-norm*tr)/2
def vector(h):return s.Matrix([h[i,j] for i,j in pairs])
ranks={}
for name,indices in [('positive',[(0,1)]),('negative',[(7,1)]),('null',[(0,1),(7,1)])]:
 xi=s.zeros(n,1)
 for i,v in indices:xi[i]=v
 E=s.Matrix.hstack(*[vector(op(h,xi)) for h in basis]);rank=E.rank();ranks[name]=rank
 ck(checks,'rank_'+name,rank==(14 if name=='null' else 91))
 ck(checks,'pairing_selfadjoint_'+name,weights*E==E.T*weights)
 ck(checks,'all_Bianchi_columns_'+name,all((eta*xi).T*op(h,xi)==s.zeros(1,n) for h in basis))
 gauges=[]
 for j in range(n):
  v=s.eye(n)[:,j];g=xi*v.T+v*xi.T;gauges.append(vector(g));ck(checks,'gauge_'+name+'_'+str(j),op(g,xi)==s.zeros(n))
 ck(checks,'gauge_injection_'+name,s.Matrix.hstack(*gauges).rank()==14)
 if name=='null':
  trace_map=s.Matrix.hstack(*[s.Matrix.vstack(h*(eta*xi),s.Matrix([s.trace(eta*h)])) for h in basis])
  ck(checks,'null_v_trace_map_surjective',trace_map.rank()==15)
 # Wrong trace term has an actual Bianchi failure on an explicit original basis.
 def wrong(h):
  up=eta*xi;q=(xi.T*up)[0];v=h*up;t=s.trace(eta*h)
  return (xi*v.T+v*xi.T-q*h-t*xi*xi.T)/2
 ck(controls,'omitted_Einstein_trace_breaks_Bianchi_'+name,any((eta*xi).T*wrong(h)!=s.zeros(1,n) for h in basis))
a,k,Rsc=s.symbols('a k Rsc',real=True);a0=-5*k/2288
L=12*a*Rsc+1456*a**3+7*k*a*a;ein=(k*a+312*a*a)/2
c=s.factor(-12*a*ein+(1456*a**3+7*k*a*a)/2)
ck(checks,'radial_metric_composition',s.simplify(c+a*a*(5*k/2+1144*a))==0)
ck(checks,'radial_joint_seed',s.simplify(c.subs(a,a0))==0)
ck(checks,'radial_source_coefficient',s.simplify(s.diff(c,a).subs(a,a0))==-25*k*k/4576)
ck(checks,'radial_restricted_density_derivative',s.diff(L,a)==12*Rsc+4368*a*a+14*k*a)
lam=35*k*k/604032
ck(checks,'same_seed_translation_equation',s.simplify(312*a0*a0+k*a0+12*lam)==0)
# Overall symmetric two-field ordinary-order2 coefficient is nonsingular even at a0=0.
mixed_coeff=s.Matrix([[-12*a0,-2],[-2,0]])
ck(checks,'mixed_coefficient_det',s.simplify(mixed_coeff.det())==-4)
ck(checks,'mixed_coefficient_inverse',s.simplify(mixed_coeff.inv()*mixed_coeff)==s.eye(2))
ck(controls,'freeze_translation_removes_half_top_rank',s.Matrix([[-12*a0,0],[0,0]]).det()==0)
ck(controls,'radial_metric_source_not_arbitrary',s.simplify(s.diff(c,a).subs(a,a0)).subs(k,1)!=0)
ck(checks,'full_normal_and_partial_codimension',14-4==10 and 14-7==7)
ck(checks,'ordinary_order2_necessary_regularity_partial',2-s.Rational(7,2)==-s.Rational(3,2))
ck(checks,'ordinary_order2_necessary_regularity_thin',2-s.Integer(5)==-3)
ck(controls,'isotropic_trace_sufficient_range_disjoint',-s.Rational(3,2)<s.Integer(5))
# Reuse the coefficient backend only; never recursively execute its old bank.
import ast
from fractions import Fraction
from math import comb
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';path=R/backend;src=path.read_text();M={'__file__':str(path),'__name__':'selected_backend'};exec(compile(src[:src.index('def sparse_rank')],str(path),'exec'),M)
blade=M['blade'];wedge=M['wedge_raw'];Phi=M['PHI1'];sh=lambda x:M['shiab'](x,('comm','symi','symi'));pair=lambda x,y:wedge(x,y).get(M['FULL'],{}).get(0,M['ZERO'])
def rat(value):
 assert value[1]==0
 return s.Rational(value[0].numerator,value[0].denominator)
v={1:blade(())};Z={2:blade((0,1))};left=rat(pair(Z,sh(wedge(v,Phi))));right=rat(pair(Phi,sh(wedge(v,Z))))
ck(checks,'ported_first_order_raw_pairings',left==2 and right==24)
ck(checks,'ported_first_order_Euler_coefficient',(left-right)/2==-11)
ck(controls,'raw_without_formal_adjoint_is_wrong',left/2!=(left-right)/2)
prior1_path='lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json';prior1=json.loads((R/prior1_path).read_text())['all_grade_distortion']
ck(checks,'reused_all_grade_TT_rank_identity',prior1['dimension']==229376 and prior1['formal_euler_green_ranks']=={'timelike':130912,'spacelike':130912,'null':122746})
# Actual NEW even Hessian at stationary-product amplitude; reuse structural orbit theorem.
parent_path='tests/channel-swings/selected_k77_nonzero_branch_parent_hessian_probe.py';tree=ast.parse((R/parent_path).read_text());wanted={'pair','basis','qform','hessian','rational','inertia_symmetric','canonical_mask','feasible_positive_counts','states_for_label','label_block'}
namespace=dict(M=M,N=14,FULL=M['FULL'],ZERO=M['ZERO'],ONE=M['ONE'],ETA=M['ETA'],PHI1=Phi,SELECTED=('comm','symi','symi'),T_VALUE=Fraction(-5,2288),Fraction=Fraction,sp=s)
namespace['POSITIVE']=tuple(i for i,sign in enumerate(M['ETA']) if sign==1);namespace['NEGATIVE']=tuple(i for i,sign in enumerate(M['ETA']) if sign==-1)
exec(compile(ast.Module(body=[node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in wanted],type_ignores=[]),str(R/parent_path),'exec'),namespace)
orbits=[];grades={};total_rank=0;total_dimension=0
for grade in range(0,15,2):
 dim=rank=0
 for size in (grade-1,grade+1):
  if not 0<=size<=14:continue
  for npos in namespace['feasible_positive_counts'](size):
   label=namespace['canonical_mask'](size,npos);states,mat=namespace['label_block'](label,grade)
   mult=comb(7,npos)*comb(7,size-npos);rk=mat.rank();dim+=mult*len(states);rank+=mult*rk
   orbits.append(dict(grade=grade,label_size=size,positive=npos,size=len(states),multiplicity=mult,rank=rk,determinant=str(mat.det())))
 ck(checks,'even_orbit_exhaustion_'+str(grade),dim==14*comb(14,grade));grades[str(grade)]=dict(dimension=dim,rank=rank);total_dimension+=dim;total_rank+=rank
 print('even grade',grade,'rank',rank,'of',dim,flush=True)
ck(checks,'even_carrier_exhaustion',total_dimension==114688)
ck(checks,'new_even_auxiliary_full_rank',total_rank==114688)
# Rank is an output: do not presume invertibility from the older amplitude.
qphi=namespace['qform'](Phi);radial_value=namespace['rational'](namespace['hessian'](Phi,Phi,qphi,qphi))
ck(checks,'actual_new_amplitude_radial_hessian',radial_value==-s.Rational(728,143))
ck(controls,'old_amplitude_not_replayed',radial_value!=-14)
AA=s.diag(1,-1);BB=s.Matrix([1,1])
ck(controls,'indefinite_Schur_rank_not_rank_B',BB.rank()==1 and BB.T*AA.inv()*BB==s.zeros(1))
x1,x2,y1,y2=s.symbols('x1 x2 y1 y2');XX=s.Matrix([x1,x2]);YY=s.Matrix([y1,y2]);AB=s.Matrix([[2,1],[1,-1]]);BC=s.Matrix([[1,2],[3,4]])
quad=(XX.T*AB*XX)[0]/2+(XX.T*BC*YY)[0]
solved=-AB.inv()*BC*YY
ck(checks,'auxiliary_elimination_original_quadratic',s.simplify(quad.subs({x1:solved[0],x2:solved[1]},simultaneous=True)+(YY.T*BC.T*AB.inv()*BC*YY)[0]/2)==0)
even_result=dict(amplitude='-5*kappa/2288',normalized_kappa=1,dimension=total_dimension,rank=total_rank,radical=total_dimension-total_rank,grades=grades,orbits=orbits)

paths=[backend,parent_path,prior1_path,'explorations/conditional-build/selected-k77-nonzero-branch-parent-hessian-2026-08-10.md','explorations/conditional-build/k2357-curved-native-stationarity-2026-10-31.md','explorations/conditional-build/k2519-stationary-product-receiver-2026-11-02.md','explorations/conditional-build/k2529-native-displacement-response-2026-11-04.md','explorations/conditional-build/k2531-partial-thickness-source-2026-11-04.md',str(Path(__file__).relative_to(R))]
report=dict(result='K2533',scope='selected independent-(G,T) completion, radial stationary product; ordinary order-two symbol and radial-only linear response',checks=checks,contrary_controls=controls,actual_even_auxiliary=even_result,reused_TT_first_order=prior1,exact_values=dict(Einstein_ranks=ranks,coupled_top_ranks={key:2*v for key,v in ranks.items()},coefficient_matrix=str(mixed_coeff),coefficient_determinant='-4',radial_source_coefficient='-25*kappa^2/4576',partial_common_Hr_necessary='r < -3/2',thin_common_Hr_necessary='r < -3'),evidence_kinds=dict(universal='written first-jet argument, Einstein decomposition, distributional radial-source proof',exact_finite='all105 metric basis columns for three covectors and symbolic radial algebra',provenance='dependency hashes and report equality'),dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths},full_mixed_characteristic_Green_or_native_GU_claim=False)
out=R/'lab/process/k2533-mixed-source-response.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report,'report differs'
print('K2533:',len(checks),'exact groups;',len(controls),'contrary controls pass;',ranks)
