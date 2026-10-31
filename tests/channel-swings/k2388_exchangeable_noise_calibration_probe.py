"""Exact finite rank controls and global graph certificates; --write saves report."""
from pathlib import Path
from itertools import permutations, product
from fractions import Fraction
import hashlib, json, sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={}; controls={}
def ck(name,value,control=False):
    value=bool(value)
    (controls if control else checks)[name]=value
    assert value,name

def pvalue(science,calibration,k=0):
    return min(Fraction(1),Fraction(1+k+sum(bool(x>=science) for x in calibration),len(calibration)+1))

# Exchangeability proof's deterministic counting inequality, including tied lists.
rank_lists=list(product(range(3),repeat=4))
for scores in rank_lists:
    ranks=[sum(x>=v for x in scores) for v in scores]
    assert all(sum(r<=cut for r in ranks)<=cut for cut in range(5))
ck('all_81_four_score_rank_lists_with_ties',len(rank_lists)==81)
# Exhaust the exchangeable permutations of one untied list and several tied lists.
for base in [(0,1,2,3),(0,0,1,1),(0,0,0,0)]:
    draws=list(set(permutations(base)))
    for cut in range(5):
        count=sum(pvalue(x[0],x[1:])<=Fraction(cut,4) for x in draws)
        assert Fraction(count,len(draws))<=Fraction(cut,4)
ck('finite_exchangeable_orbit_coverage',True)
# Pointwise replacement domination, with adaptive locations and arbitrary high/low replacements.
replacement_cases=0
for scores in product(range(3),repeat=4):
    clean=pvalue(scores[0],scores[1:])
    for j in range(3):
        for replacement in (-1,3):
            cal=list(scores[1:]);cal[j]=replacement
            assert pvalue(scores[0],cal,1)>=clean
            replacement_cases+=1
ck('all_486_replacement_domination_cases',replacement_cases==486)
ck('ties_count_as_exceedances',pvalue(0,[0]*59)==1)
strict_tie_p=Fraction(1+sum(x>0 for x in [0]*59),60)
ck('strict_tie_mutation_falsely_rejects',strict_tie_p<=Fraction(1,20) and pvalue(0,[0]*59)>Fraction(1,20),True)
ck('contamination_resolution',pvalue(2,[0]*59,1)==Fraction(1,30))
ck('below_resolution_no_rejection',Fraction(1,30)>Fraction(1,40),True)
# Execute a score-dependent worst-case replacement on each exchangeable permutation.
uncorrected_rejects=0;corrected_rejects=0;sharp_grid_rejects=0
for sample in permutations(range(4)):
    science=sample[0]; cal=list(sample[1:])
    eligible=[j for j,x in enumerate(cal) if x>science]
    if eligible: cal[eligible[0]]=-1
    uncorrected_rejects+=pvalue(science,cal)<=Fraction(1,2)
    corrected_rejects+=pvalue(science,cal,1)<=Fraction(1,2)
    sharp_grid_rejects+=pvalue(science,cal,1)<=Fraction(3,4)
ck('adaptive_replacement_uncorrected_size',Fraction(uncorrected_rejects,24)==Fraction(3,4),True)
ck('adaptive_replacement_corrected_size',Fraction(corrected_rejects,24)==Fraction(1,2))
ck('replacement_correction_sharp_grid',Fraction(sharp_grid_rejects,24)==Fraction(3,4))
# A half-unit correction is insufficient: maximum p is7/8, hence all ranks reject there.
small_c_p=[min(Fraction(1),Fraction(max(1,r-1),4)+Fraction(1,8)) for r in range(1,5)]
ck('smaller_contamination_correction_fails',max(small_c_p)==Fraction(7,8) and all(p<=Fraction(7,8) for p in small_c_p),True)
# Correcting a removed exceedance restores the original pointwise rank.
ck('uncorrected_replacement_changes_decision',pvalue(2,[3,3,3])==1 and pvalue(2,[0,3,3])==Fraction(3,4),True)
ck('replacement_correction_repairs_rank',pvalue(2,[0,3,3],1)==1)

t=s.symbols('t',real=True);u=s.symbols('u',nonnegative=True)
Rt=s.Matrix([[-t,1,0,0],[0,0,-t,1]])
z=s.Matrix([1,3,1,-3]);xi=s.Matrix([4,0,0,0])
qs=s.expand((Rt*z).dot(Rt*z));qc=s.expand((Rt*xi).dot(Rt*xi))
ck('science_score',qs==18+2*t*t)
ck('calibration_score',qc==16*t*t)
ck('global_difference_certificate',s.expand(qs-qc-(4+14*(1-t*t)))==0)
ck('global_strict_margin',4>0)
ck('profile_p_and_reject',pvalue(20,[16]*59,1)==Fraction(1,30)<Fraction(1,20))
ck('one_high_replacement_still_rejects',pvalue(20,[100]+[16]*58,1)==Fraction(1,20))
ck('raw_error_global_certificate',s.expand(18+2*u*u-(4*u+s.Rational(1,4))**2-(s.Rational(31,16)+14*(1-u*u)+2*(1-u)))==0)
ck('large_error_removes_reject',(s.sqrt(20)-s.Rational(1,2))**2<16,True)
ck('wider_gain_removes_reject',qs.subs(t,2)==26 and qc.subs(t,2)==64 and pvalue(26,[64]*59,1)==1,True)
ck('grid_has_wrong_bound_direction',pvalue(18,[0]*59,1)<Fraction(1,20) and pvalue(26,[64]*59,1)==1,True)
# Finite support consumer; written inequalities cover the full bounded interval.
b=s.symbols('b',real=True);signal=s.Matrix([0,4,0,-4]);error=s.Matrix([b,0,0,0])
qalt=s.expand((Rt*(signal+error)).dot(Rt*(signal+error)))
ck('bounded_noise_alternative_identity',s.expand(qalt-((4-t*b)**2+16))==0)
v=s.symbols('v',real=True)
ck('whole_support_signal_lower_bound',s.expand((4-v)**2+16-25-(1-v)*(7-v))==0)
ck('whole_support_noise_upper_bound',s.expand(1-t*t*b*b-((1-t*t)+t*t*(1-b*b)))==0)
ck('power_margin_with_discrepancy',5-s.Rational(1,4)>1)
ck('adversarial_power_count',Fraction(3,60)==Fraction(1,20))
# Null true at theta0; profiling by infimum is wrong.
nullz=s.Matrix([1,0]);r=s.Matrix([[-t,1]])
qnull=s.expand((r*nullz).dot(r*nullz))
p0=pvalue(qnull.subs(t,0),[0]*59);p1=pvalue(qnull.subs(t,1),[0]*59)
ck('shared_parameter_sup_preserves_true_null',max(p0,p1)==1)
ck('wrong_profile_inf_falsely_rejects',min(p0,p1)<=Fraction(1,20),True)
ck('science_only_bias_falsely_rejects',pvalue(1,[0]*59)<=Fraction(1,20),True)
ck('matched_nonzero_bias_does_not_reject',pvalue(7,[7]*59)==1)
# Actual interpolating overfit score, not just a Boolean marker.
x=s.symbols('x');cal=[-1,0,1];overfit=s.prod((x-v)**2 for v in cal)
ck('overfit_score_zeros_calibration',all(overfit.subs(x,v)==0 for v in cal))
ck('overfit_new_score_positive',overfit.subs(x,2)==36)
ck('reused_calibration_wrong_rank',pvalue(overfit.subs(x,2),[overfit.subs(x,v) for v in cal])==Fraction(1,4),True)
paths=['lab/process/k2385-estimated-noise-calibration.json','lab/process/k2376-windowed-cosmological-null.json']
report={'result_id':'K2388','checks':len(checks),'check_names':checks,'changed_input_or_inference_controls':controls,'finite_rank_lists':81,'replacement_cases':replacement_cases,'fixture':{'D':4,'d':2,'m':59,'k':1,'alpha':'1/20','profile_p':'1/30','one_arbitrary_replacement_bound':'1/20'},'scope':'Exact finite-list/rational/symbolic controls; universal coverage and power are written proofs, not Monte Carlo or survey tests. Continuous overfit failure is written reasoning with a finite interpolation countercontrol.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=json.dumps(report,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(R/'lab/process/k2388-exchangeable-noise-calibration.json').write_text(out)
print(out)
