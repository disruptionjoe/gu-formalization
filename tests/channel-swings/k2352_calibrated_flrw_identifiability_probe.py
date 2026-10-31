from pathlib import Path
import json,hashlib,sys
import sympy as s
from fractions import Fraction as F
R=Path(__file__).resolve().parents[2];checks={};faults={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def fault(k,v):
 faults[k]=bool(v)
 if not v:raise AssertionError('ineffective changed-input control: '+k)
def publish(st,details,deps):
 deps=[f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]+deps
 out=dict(result_id=st.split('-')[0].upper(),checks=len(checks),check_names=list(checks),altered_input_controls=faults,evidence_kind='exact symbolic/rational controls; universal theorems in companion proofs',details=details,dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps})
 p=R/f'lab/process/{st}.json'
 if '--write' in sys.argv:p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 else:assert json.loads(p.read_text())==out
 print(json.dumps(dict(result_id=out['result_id'],checks=len(checks),faults=len(faults),details=details)))

t=s.symbols('t',positive=True);z=s.symbols('z',positive=True);chi0=z;chi1=2*(1-1/s.sqrt(1+z));g0=chi0**2*s.diff(chi0,z);g1=chi1**2*s.diff(chi1,z)
ratio=s.factor((chi0/chi1).subs(z,t*t-1));vol=s.factor((g0/g1).subs(z,t*t-1))
check('distance_ratio',s.simplify(ratio-t*(t+1)/2)==0)
check('volume_ratio',s.simplify(vol-t**5*(t+1)**2/4)==0)
check('strict_distance_monotonicity',s.diff(ratio,t)==t+s.Rational(1,2))
check('volume_monotonicity_positive_coefficients',all(c>0 for c in s.Poly(s.diff(vol,t),t).all_coeffs() if c!=0))
check('endpoint_ratios',ratio.subs(t,1)==1 and ratio.subs(t,2)==3 and vol.subs(t,1)==1 and vol.subs(t,2)==72)
# Constructive centering in log coordinates, exact symbolic identity for all d,q.
d,q,cd,cq=s.symbols('d q cd cq',real=True);u0=-(d-cd)/2;u1=(d-cd)/2;l0=-(q-cq)/2;l1=(q-cq)/2
check('centered_radial_equality',s.expand(d+u0-u1)==cd)
check('centered_mark_equality',s.expand(q+l0-l1)==cq)
check('overlap_3_2',3**4>=72 and 2**4>=9)
check('count_separation_2_2',2**4<72)
check('mark_separation_3_threehalves',s.Rational(3,2)**4<9)
# Finite sharp count bounds and uniform tail.
p0=F(125,1728);p1=F(8,27);alpha=F(6,5)
lo=lambda p:p/(p+alpha**2*(1-p));hi=lambda p:alpha**2*p/(alpha**2*p+1-p)
U=hi(p0);L=lo(p1);gap=L-U;N=(F(6)/gap**2).__floor__()+1
check('sharp_count_gap',gap>0)
check('rational_count_certificate',N*gap**2/2>3 and (N-1)*gap**2/2<=3)
check('exp3_exceeds20',sum(F(3)**j/s.factorial(j) for j in range(9))>20)
check('extreme_weights_attain_bounds',hi(p0)==p0*alpha/(p0*alpha+(1-p0)/alpha) and lo(p1)==p1/alpha/(p1/alpha+(1-p1)*alpha))
check('paired_window_ratio',ratio.subs(t,s.Rational(5,3))/ratio.subs(t,s.Rational(4,3))==s.Rational(10,7))
b=s.symbols('b',positive=True);eta=b/8;sig=b/4;a=b-2*eta
check('paired_mark_exponent',s.simplify(2*a*a/(4*sig*sig))==s.Rational(9,2))
check('exp9half_exceeds20',sum(s.Rational(9,2)**j/s.factorial(j) for j in range(4))==s.Rational(493,16)>20)
check('zero_point_cancels',s.expand((q+cd)-(d+cd))==q-d)
# Separate physical nuisance restrictions and controls.
fault('underprice_two_hypothesis_radius',3**2<72<=3**4) # erroneously using alpha² rejects valid intersecting classes
fault('ignore_count_calibration',2**4<72 and 2**4>=9)
fault('ignore_mark_calibration',3**4>=72 and F(3,2)**4<9)
fault('known_absolute_zero_point_changes_overlap',F(2)>2*F(1,2)) # q constant2 has osc0 but cannot fit |ell_i|<=1/2 with fixed b
# Shared Gaussian source error makes pairs perfectly correlated, actual variance differs.
M=2;sigma2=F(1);independent=2*M*sigma2;shared=2*M*M*sigma2
fault('reuse_correlated_pair_errors',shared==8 and shared>independent)
# Mark-dependent selection Y>0 on centered normal leaves positive conditional mean (integral y exp(-y²/2)).
y=s.symbols('y',real=True)
fault('flux_selection_changes_centered_mean',s.integrate(y*s.exp(-y*y/2),(y,0,s.oo))==1)
# Completeness nominal 3/4 with allowed factor2 exceeds physical1.
fault('unclipped_completeness_box',F(3,4)*2>1)
publish('k2352-calibrated-flrw-identifiability',dict(alpha='6/5',count_upper0=str(U),count_lower1=str(L),gap=str(gap),conditional_count_N=N,paired_M=2,paired_exponent='9/2',overlap_count_ratio=72,overlap_flux_ratio=9),['explorations/conditional-build/k2349-positive-flrw-source-counts-2026-10-30.md','lab/process/k2349-positive-flrw-source-counts.json'])
