"""Exact selected-Shiab parity, frame-jet Euler and action-owner controls."""
from pathlib import Path
import ast,hashlib,json,sys,itertools
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';source=(R/backend).read_text();ns={'__file__':str(R/backend),'__name__':'selected_arithmetic'}
# Only pure arithmetic definitions and constants before the rank/testing driver.
exec(compile(source[:source.index('def sparse_rank')],backend,'exec'),ns)
blade=ns['blade'];hodge=ns['hodge'];shiab=ns['shiab'];flat=ns['flatten'];wedge=ns['wedge_raw'];fadd=ns['fadd'];fscale=ns['fscale'];zero=ns['ZERO'];full=ns['FULL'];F=ns['Fraction'];channels=('comm','symi','symi')
def form(indices,coefficient):return {sum(1<<i for i in indices):coefficient}
def pair(a,b):return wedge(a,b).get(full,{}).get(0,zero)
def inner(a,b):return pair(a,hodge(b))
T=form((0,),blade((0,1)));X=form((1,),blade(0));Fe=form((0,1),blade((0,1)));Fo=form((0,1),blade(0))
Se=shiab(Fe,channels);So=shiab(Fo,channels)
check('even_curvature_to_nonzero_odd',len(flat(Se))==12 and all(cm.bit_count()%2 for fm,cm in flat(Se)))
check('odd_curvature_to_nonzero_even',len(flat(So))==1 and all(cm.bit_count()%2==0 for fm,cm in flat(So)))
check('even_odd_pair_zero',pair(T,Se)==zero)
check('odd_translation_live',pair(form((2,),blade(2)),Se)==(F(2),F(0)))
check('frame_jet_Euler_coefficient',pair(T,So)==(F(2),F(0)))
check('even_pairing_nonzero',inner(T,T)==(F(1),F(0)))
# Verify parity in all eight product channels on two explicit nonzero inputs.
for ch in itertools.product(('comm','symi'),repeat=3):
 for parity,C in [(0,Fe),(1,Fo)]:
  assert all(cm.bit_count()%2==1-parity for fm,cm in flat(shiab(C,ch)))
check('all_eight_channel_parities',True)
# Exact null even one-form and independent dual test.
Tminus=form((1,),blade((0,1)));N=fadd(T,Tminus)
check('even_null_nonzero',bool(N) and inner(N,N)==zero)
check('null_detected_by_independent_dual',inner(T,N)==(F(1),F(0)))
# Clifford scalar pairing is diagonal and every blade square is nonzero.
# All 2^13 even blades checked cheaply by the actual multiplication rule.
for mask in range(1<<14):
 if mask.bit_count()%2==0:
  out,sign=ns['blade_product'](mask,mask);assert out==0 and sign in [-1,1]
check('all8192_even_blade_squares_nondegenerate',True)
check('one_form_metric_nondegenerate',all(v in [-1,1] for v in ns['ETA']))
c=s.symbols('c',real=True);e0=s.symbols('e0',real=True)
shift=F(1,2)*pair(T,So)[0]
check('kappa_zero_Euler_family_slope',shift==1)
check('two_flat_members_cannot_both_vanish',s.solve([e0,e0+1],[e0])==[])
x,eps,a=s.symbols('x eps a',real=True);U=x+x*x;Q=1+x;I2=Q*U*U/2
check('moving_I2_first_variation_zero',s.diff(I2,x).subs(x,0)==0)
check('I2_hessian_not_zero',s.diff(I2,x,2).subs(x,0)==1)
Uchanged=2*x+x*x;I2changed=Q*Uchanged**2/2
check('equal_residual_different_hessian',U.subs(x,0)==Uchanged.subs(x,0)==0 and s.diff(I2changed,x,2).subs(x,0)==4)
I1=x+x*x/2;curve=eps+a*eps*eps/2;curved=s.diff(I1.subs(x,curve),eps,2).subs(eps,0)
check('nonstationary_second_jet',curved==1+a)
# Genuine changed objects: an even multiplier does NOT implement selected odd Shiab.
identity_S=hodge(Fe) # wrong degree12 as well, detected by parity not a new target.
faults['replace_odd_S_by_parity_preserving_Hodge']=['even_curvature_to_nonzero_odd'] if any(cm.bit_count()%2==0 for fm,cm in flat(identity_S)) else []
faults['radial_test_only_on_null_T']=['null_detected_by_independent_dual'] if inner(N,N)==zero and inner(T,N)!=zero else []
faults['omit_adjoint_derivative_term']=['kappa_zero_Euler_family_slope'] if F(0)!=shift else []
faults['reuse_hessian_from_equal_residual']=['equal_residual_different_hessian'] if s.diff(I2changed,x,2).subs(x,0)!=s.diff(I2,x,2).subs(x,0) else []
faults['discard_path_acceleration']=['nonstationary_second_jet'] if curved.subs(a,2)!=1 else []
assert all(faults.values())
deps=['explorations/conditional-build/k2348-even-distortion-stationarity-boundary-2026-10-30.md',str(Path(__file__).relative_to(R)),backend,'lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md','explorations/conditional-build/k2345-curved-bundle-ricci-obstruction-2026-10-30.md']
out=dict(result_id='K2348',checks=len(checks),check_names=list(checks),evidence_kind='exact Clifford/exterior rational and symbolic variation controls; universal parity and local jet arguments in note',mutation_failed_checks=faults,details={'channels':list(channels),'even_shiab_terms':len(flat(Se)),'odd_shiab_terms':len(flat(So)),'frame_Euler_shift':'c','null_dual_pairing':str(inner(T,N)),'I2_hessians':[1,4],'nonstationary_path_second_derivative':str(curved)},dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
p=R/'lab/process/k2348-even-distortion-stationarity-boundary.json'
if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==out
print(json.dumps({k:out[k] for k in ['result_id','checks','details']}))
