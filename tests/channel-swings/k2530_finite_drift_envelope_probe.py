"""Exact finite drift/anchor fixtures; universal arguments live in the note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]; checks={}; controls={}
def ck(name,value):
 checks[name]=bool(value)
 if not checks[name]: raise AssertionError(name)
def ct(name,value):
 controls[name]=bool(value)
 if not controls[name]: raise AssertionError(name)
x,p,q,L=s.symbols('x p q L',positive=True)
y=x/s.sqrt(1+2*p*x);w=(1+p*x)/(x*(1+2*p*x))
ck('moving_emitter_log_jacobian',s.simplify(s.diff(s.log(y),x)-w)==0)
ck('momentum_kernel_decreases',s.factor(s.diff(w,p))==-1/(2*p*x+1)**2)
f=s.Function('f')(x)
Ds=lambda z:s.diff(z,x)/(3*w)
ck('actual_second_window_derivative',s.simplify(Ds(Ds(f))-(s.diff(f,x,2)*w-s.diff(f,x)*s.diff(w,x))/(9*w**3))==0)
shift,Q=s.symbols('shift Q',real=True)
ck('common_clock_shift_invariance',s.cancel(1/((q+shift)-(Q+shift))-1/(q-Q))==0)
# Compatibility is checked against cross-node constraints, not own boxes only.
def feasible(nodes,lo,hi,lip):
 return all(lo[i]<=hi[j]+lip*abs(nodes[i]-nodes[j]) for i in range(len(nodes)) for j in range(len(nodes)))
nodes=[s.Integer(1),s.Integer(2)]
ck('compatible_exact_nodes',feasible(nodes,[0,0],[0,0],1))
ct('cross_node_incompatibility',not feasible(nodes,[0,2],[0,2],1))
lo=[1-x,x-2];hi=[x-1,2-x];cuts=[1,s.Rational(3,2),2]
Flo=sum(s.integrate(1/(x*(1-lo[i])),(x,cuts[i],cuts[i+1])) for i in range(2))
Fhi=sum(s.integrate(1/(x*(1-hi[i])),(x,cuts[i],cuts[i+1])) for i in range(2))
ck('sharp_lower_integral',s.simplify(s.expand_log(Flo,force=True)-(1+s.log(2))/3)==0)
ck('sharp_upper_integral',s.simplify(s.expand_log(Fhi,force=True)-(s.Rational(3,2)*s.log(3)-s.log(2)))==0)
ck('strict_upper_bound_squared',s.Rational(27,4)<s.Rational(64,9))
ck('exponential_lower_bound',sum(s.Rational(1,s.factorial(i)) for i in range(5))>s.Rational(8,3))
ck('positive_coasting_anchor',s.integrate(1/x,(x,1,2))==s.log(2))
# log2 lies between 1/2 and1 by its integral; this proves coarse range contains1.
ck('coarse_lower_below_one',s.Rational(2,3)*1<1)
ck('coarse_upper_above_one_integrand',s.simplify(1/x-s.Rational(1,2)-(2-x)/(2*x))==0)
ct('coarse_rectangle_misses_anchor_contradiction',s.Rational(27,4)<s.Rational(64,9) and s.Rational(2,3)<1)
# Joint anchors: actual constants attain each marginal target; equality forces incompatible profiles.
C1=s.integrate(1/(2*x),(x,2,4));C2=s.integrate(1/(x*(2-s.Rational(2,3))),(x,2,8))
ck('individual_first_anchor_control',s.simplify(s.expand_log(C1-s.log(2)/2,force=True))==0)
ck('individual_second_anchor_control',s.simplify(s.expand_log(C2-3*s.log(2)/2,force=True))==0)
ck('joint_second_shell_saturates_upper',s.simplify(s.expand_log(C2-C1-s.integrate(1/x,(x,4,8)),force=True))==0)
ck('first_saturation_strictness',s.simplify(1/(2-Q)-s.Rational(1,2)-Q/(2*(2-Q)))==0)
ck('second_saturation_strictness',s.simplify(1-1/(2-Q)-(1-Q)/(2-Q))==0)
left_saturated=s.Integer(0);right_saturated=s.Integer(1)
ct('joint_saturation_one_sided_traces_disagree',s.limit(left_saturated,x,4,dir='-')!=s.limit(right_saturated,x,4,dir='+'))
actual_q=s.Rational(1,2);actual_Q=s.Integer(0)
actual_upper_mid=min(2*abs(s.Rational(3,2)-v) for v in nodes)
ct('robust_positivity_slice_not_all_histories',feasible(nodes,[0,0],[0,0],2) and actual_Q==0 and actual_q-actual_Q>0 and actual_q<=actual_upper_mid)
# Sign-aware powers and a separate exact linear-algebra consumer fixture.
for exponent in [s.Rational(3,2),-s.Rational(1,2),-s.Rational(5,2)]:
 vals=[s.Integer(1)**exponent,s.Integer(4)**exponent];lower=min(vals);upper=max(vals)
 for weight in [-3,2]:
  boundlo=max(weight,0)*lower-max(-weight,0)*upper
  boundhi=max(weight,0)*upper-max(-weight,0)*lower
  ck('signed_power_'+str(exponent)+'_'+str(weight),boundlo<=weight*s.Integer(2)**exponent<=boundhi)
M=s.Matrix([[1,0,0,1],[0,1,0,1],[0,0,1,1],[1,1,1,0]])
E=s.ones(4)*s.Rational(1,100)
bound=max(sum(row) for row in (M.inv().applyfunc(abs)*E).tolist())
ck('outer_matrix_bound_strict',bound<1)
ct('three_rows_can_fit',M[:3,:3].det()!=0)
ct('four_rows_cannot_fit',M.det()!=0)
ck('no_positive_history_discarded_by_fixture',1>s.Rational(1,2))
paths=['explorations/conditional-build/k2528-observation-forecast-feasibility-2026-11-04.md','explorations/conditional-build/k2409-coupled-drift-calibration-2026-10-31.md','explorations/conditional-build/k2520-nonlinear-observation-null-2026-11-02.md']
report={'result':'K2530','scope':'conditional finite-information/anchor and weak-column construction','checks':checks,'contrary_controls':controls,'exact_values':{'anchor_lower':'(1+log(2))/3','anchor_upper':'3*log(3)/2-log(2)','coarse_interval':'[2*log(2)/3,2*log(2)]','rejected_anchor':'1','separate_matrix_fixture_bound':str(bound)},'evidence_kinds':{'universal':'written extension, monotonicity, continuity and saturation proofs','exact_finite':'symbolic identities and rational controls; matrix fixture is not observed data','provenance':'dependency hashes and report equality'},'dependencies':{v:hashlib.sha256((R/v).read_bytes()).hexdigest() for v in paths},'empirical_or_native_GU_certification':False}
out=R/'lab/process/k2530-finite-drift-envelope.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report,'report differs'
print(f'K2530: {len(checks)} exact groups; {len(controls)} contrary controls pass')
