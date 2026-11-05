"""Exact finite price/resource consumers; universal attainment proof is in K2571."""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json
import math
import sys
import sympy as sy

sys.set_int_max_str_digits(0)
ap = argparse.ArgumentParser()
ap.add_argument('--write', action='store_true')
ap.add_argument('--check', action='store_true')
args = ap.parse_args()
if args.write and args.check:
    ap.error('--write and --check are mutually exclusive')
ROOT = Path(__file__).resolve().parents[2]
checks, controls, reporting = {}, {}, {}


def ck(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def ct(name, rejected):
    controls[name] = bool(rejected)
    if not rejected:
        raise AssertionError('contrary control: ' + name)


def rp(name, condition):
    reporting[name] = bool(condition)
    if not condition:
        raise AssertionError('evidence reporting: ' + name)


def schedule_resource(stages):
    p = F(1)
    prefixes = []
    for a, b in stages:
        assert 0 <= a <= b
        if b == 0:
            assert a == 0
            continue
        p /= 1 + a
        prefixes.append(p)
    return p, 2 * sum(prefixes, F(0)), prefixes


# Solve the actual one-trial law, including costs on failure and test-pass.
a, w, lam, kap, x, value = sy.symbols('a w lam kap x value')
recurrence = sy.Eq(value, x / 2 + (1 - a) * value / 2 - lam * w - kap)
solved = sy.solve(recurrence, value)[0]
correct = (x - 2 * lam * w - 2 * kap) / (1 + a)
ck('fresh_trial_recurrence_derives_penalized_stage', sy.cancel(solved - correct) == 0)
trial_count = sy.solve(sy.Eq(value, 1 + (1 - a) * value / 2), value)[0]
ck('fresh_trial_recurrence_derives_geometric_resource', sy.cancel(trial_count - 2 / (1 + a)) == 0)
wrong = (x - 2 * lam * w - kap) / (1 + a)
ct('one_price_per_stage_omits_failure_and_pass_trials', sy.cancel(wrong - solved - kap / (1 + a)) == 0)
wrong_cost = (x - lam * w - 2 * kap) / (1 + a)
ct('use_only_leakage_omits_test_path_cost', sy.cancel(wrong_cost - solved - lam * w / (1 + a)) == 0)

# Two distinct actual stages expose survival-prefix errors.
stages = [(F(1,4), F(1,4)), (F(1,8), F(1,4))]
p, r, prefixes = schedule_resource(stages)
ck('two_stage_probability', p == F(32,45))
ck('two_stage_resource', r == F(136,45))
ck('two_stage_prefixes', prefixes == [F(4,5), F(32,45)])
ct('unweighted_trial_count_is_not_original_resource', r != 2 * len(stages))
ct('success_conditioned_trial_count_is_not_original_resource', r != 2 * len(stages) * p)
ck('padding_omission_preserves_actual_resource', schedule_resource([(F(0),F(0))] + stages) == (p,r,prefixes))

# A real zero-score boundary has an upward penalized jump, not continuity.
eps = sy.symbols('eps', positive=True)
prob = 1 / ((1 + eps) * (sy.Rational(3,2) - eps))
res = 2 / (1 + eps) + 2 * prob
limit_prob = sy.limit(prob, eps, 0, dir='+')
limit_res = sy.limit(res, eps, 0, dir='+')
dropped_prob, dropped_res, _ = schedule_resource([(F(0),F(0)), (F(1,2),F(1,2))])
ck('vanishing_stage_preserves_probability_limit', limit_prob == sy.Rational(2,3) == sy.Rational(dropped_prob.numerator,dropped_prob.denominator))
ck('vanishing_stage_loses_two_positive_trials', limit_res == sy.Rational(10,3) and dropped_res == F(4,3))
ck('penalized_boundary_jump_direction', sy.simplify((sy.Rational(2,3) - kap * sy.Rational(4,3)) - (limit_prob - kap * limit_res)) == 2 * kap)
ct('resource_continuity_at_zero_stage_is_false', limit_res != sy.Rational(dropped_res.numerator,dropped_res.denominator))
for i, e in enumerate([F(1,10), F(1,100), F(1,1000)]):
    pp, rr, _ = schedule_resource([(e,e),(F(1,2)-e,F(1,2)-e)])
    ck('actual_vanishing_stage_sequence_' + str(i), rr > F(4,3) + F(3,2) and pp < F(2,3))

# Rational Taylor-plus-geometric upper bound for exp(1/2).
partial = sum((F(1,2)**j / F(math.factorial(j)) for j in range(12)), F(0))
tail = (F(1,2)**12 / F(math.factorial(12))) / (1 - F(1,26))
exp_upper = partial + tail
ck('rigorous_exponential_upper_below_five_thirds', exp_upper < F(5,3))
s, price = F(1,2), F(1,10)
free_lower = (1 - 2 * price) / (1 + s)
cap_upper = exp_upper * (s + 2 * price) / (2 * price * (1 + s))
ck('all_multiplier_three_stage_cap', 3 < cap_upper < 4)
ck('four_stages_strictly_inferior_to_free_witness', 1 - 2 * price * F(3,5) * 4 < free_lower == F(8,15))

# Execute the exact small-resource frontier at S=1/2, M=1.
pf, rf, _ = schedule_resource([(s,s)])
mix = F(1) / rf
ck('free_stage_actual_probability_and_trials', (pf,rf) == (F(2,3),F(4,3)))
ck('budget_one_initial_mixture', mix == F(3,4) and mix * rf == 1)
ck('budget_one_exact_value', mix * pf == F(1,2))
ck('half_price_abort_and_free_tie', pf - F(1,2) * rf == 0)
ck('above_half_price_free_stage_is_strictly_negative', pf - F(3,5) * rf < 0)
ct('charging_initial_abort_as_a_trial_changes_budget', mix * rf + (1 - mix) != 1)

# Reuse the accepted original-law value interval, replay the NEW resource.
old = json.loads((ROOT / 'lab/process/k2565-bellman-supersolution.json').read_text())
old_witness = old['bounds']['executed_successor']
new_stages = [(F(8793,50000),F(151,500))]
for i in range(40):
    b = F(99,20000)
    new_stages.append((b * (F(221,500) - F(23,500) * F(2*i+1,80)), b))
wp, wr, wpref = schedule_resource(new_stages)
ck('inherited_witness_score_and_positive_controls', sum(b for a,b in new_stages) == s and all(0 < a < b for a,b in new_stages))
ck('inherited_witness_new_resource_below_82', len(new_stages) == 41 and 0 < wr < 82)
rp('original_witness_probability_matches_saved_certificate', wp == F(old_witness['probability']))
lower = F(711079567311,10**12)
rp('original_logarithmic_lower_bound_reused', F(old_witness['dual_interval'][0]) > lower)
tiny_price = F(1,100000)
priced_lower = lower - tiny_price * wr
ck('positive_price_witness_beats_global_one_stage_upper', priced_lower > F(71,100) + F(1,5000))
ck('coarse_82_trial_bound_already_suffices', lower - tiny_price * 82 == F(710259567311,10**12) and lower - tiny_price * 82 > F(71,100) + F(1,5000))
ct('finite_witness_is_not_resource_free', lower - tiny_price * wr < lower)

# Released all-adaptive one-stage price transformation and exact root certificate.
ck('effective_multiplier_enters_global_one_stage_region', F(19,8)**2 > F(16,3))
ck('small_price_witness_outside_sufficient_one_stage_region', (F(19,10)/(1-2*tiny_price))**2 < F(16,3))
pv,cv,rv=sy.symbols('pv cv rv')
ck('price_transform_gap_is_actual_excess_trials', sy.cancel((1-2*kap)*(pv-lam/(1-2*kap)*cv)-(pv-lam*cv-kap*rv)-kap*(rv-2*pv)) == 0)
ct('multistage_excess_trials_prevents_transform_equality', r-2*p == F(8,5)>0)
aa=sy.symbols('aa');zz=(sy.Rational(1,2)-aa)**2/(2*(aa+sy.Rational(1,2))*(sy.Rational(3,2)-aa))
dw=sy.factor(sy.diff(zz,aa)/(1+zz))
def frac_at(expr,a):
    v=sy.cancel(expr.subs(aa,sy.Rational(a.numerator,a.denominator)))
    return F(int(sy.numer(v)),int(sy.denom(v)))
def log_interval(z):
    t=z/(2+z)
    lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(20)),F(0))
    return lo,lo+2*t**41/(41*(1-t*t))
def root_interval(a):
    lo,hi=log_interval(frac_at(zz,a));der=frac_at(dw,a)
    return -2*(1+a)*der+2*lo,-2*(1+a)*der+2*hi
al=F(383330117,1073741824);ah=F(766660235,2147483648)
ck('unique_original_root_left_sign',root_interval(al)[0]>F(8,19))
ck('unique_original_root_right_sign',root_interval(ah)[1]<F(8,19))
wl,wh=log_interval(frac_at(zz,al));vl,vh=log_interval(frac_at(zz,ah))
ql=(F(4,5)-F(19,5)*wh)/(1+ah);qh=(F(4,5)-F(19,5)*vl)/(1+al)
rl=2/(1+ah);rh=2/(1+al)
ck('one_stage_global_value_rational_enclosure',F(5604579098,10**10)<ql<qh<F(5604579104,10**10))
ck('one_stage_supported_resource_rational_enclosure',F(14738350158,10**10)<rl<rh<F(14738350164,10**10))
ck('supported_budget_exceeds_free_stage_segment',rl>F(4,3))
ct('rounding_supported_resource_changes_exact_budget',not (rl<=F(1474,1000)<=rh))

# Actual logarithmic derivative for the released nonlinear resource frontier.
budgetvar=sy.symbols('budgetvar',positive=True)
wexpr=sy.log(1+zz)
aof=2/budgetvar-1
front=budgetvar/2-lam*budgetvar*wexpr.subs(aa,aof)
mfun=-2*(1+aa)*sy.diff(wexpr,aa)+2*wexpr
ck('nonlinear_budget_frontier_derivative_is_support_price',sy.simplify(sy.diff(front,budgetvar)-(1-lam*mfun.subs(aa,aof))/2)==0)
ck('nonlinear_budget_frontier_second_derivative',sy.simplify(sy.diff(front,budgetvar,2)-lam*sy.diff(mfun,aa).subs(aa,aof)/budgetvar**2)==0)
ck('nonlinear_frontier_joins_free_resource_value',sy.simplify(front.subs(budgetvar,sy.Rational(4,3))-sy.Rational(2,3))==0)
ck('nonlinear_frontier_joins_initial_half_slope',sy.simplify(sy.diff(front,budgetvar).subs(budgetvar,sy.Rational(4,3))-sy.Rational(1,2))==0)

# An exact affine support mixture checks both resource and objective weights.
# These are abstract support-line fixtures, NOT asserted original-law optima.
rlo, rhi, budget, q0, k0 = map(F, [2,5,3,0,0])
q0, k0 = F(1,3), F(1,20)
weight_hi = (budget-rlo)/(rhi-rlo)
jlo, jhi = q0+k0*rlo, q0+k0*rhi
ck('support_mixture_probability', weight_hi == F(1,3))
ck('support_mixture_preserves_exact_resource', (1-weight_hi)*rlo+weight_hi*rhi == budget)
ck('support_mixture_attains_support_line', (1-weight_hi)*jlo+weight_hi*jhi == q0+k0*budget)
ct('equal_weights_do_not_preserve_arbitrary_budget', (rlo+rhi)/2 != budget)

# This verifies the resource-gap rearrangement, not a new value for g_n.
eta, gap, ceiling, threshold = sy.symbols('eta gap ceiling threshold', positive=True)
bound = sy.solve(sy.Eq(ceiling, threshold*(1-eta/gap)), eta)[0]
ck('finite_budget_strict_gap_rearrangement', sy.simplify(bound-gap*(1-ceiling/threshold)) == 0)
ck('attained_high_lambda_regime_is_disjoint', F(98,51)**2 < F(16,3))

paths = [
    'explorations/conditional-build/k2571-stopping-resource-price-2026-11-05.md',
    'explorations/conditional-build/k2569-stopping-maximizing-sequences-2026-11-05.md',
    'explorations/conditional-build/k2567-stopping-family-structure-2026-11-05.md',
    'explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md',
    'explorations/conditional-build/k2559-parametric-stopping-concavity-2026-11-05.md',
    'lab/process/k2565-bellman-supersolution.json',
    'lab/process/k2561-higher-budget-stopping.json',
]
report = {
    'result': 'K2571',
    'checks': checks,
    'contrary_controls': controls,
    'reporting_checks': reporting,
    'evidence_kinds': {
        'exact': 'actual-law recurrence, original survival-prefix resources, padding jump, finite price/budget consumers and rational exponential enclosure',
        'supporting': 'abstract affine support-mixture fixture and resource-gap rearrangement; neither proves universal compactness or duality',
        'reused': 'K2569 resource reduction and positive gaps; K2567 nonattainment; K2565 original 41-stage logarithmic bound; K2561 global one-stage upper; K2559 contrary attained regime',
        'universal': 'positive-price cap, upper-semicontinuous attainment, supporting-price positivity, optimizer compactness and two-schedule attained frontier in accompanying note',
        'not_claimed': 'computed unpriced intermediate optimum, rate for vanishing price, physical controller price, external-expert or proof-assistant certification',
    },
    'executed_consumers': {
        'global_one_stage_priced_consumer': {'lambda':'19/10','kappa':'1/10','S':'1/2','effective_lambda':'19/8','a_bracket':[str(al),str(ah)],'Q_outer':['5604579098/10000000000','5604579104/10000000000'],'R_outer':['14738350158/10000000000','14738350164/10000000000'],'supported_budget':'exact R*=2/(1+a*), not a rounded decimal'},
        'nonlinear_resource_frontier': {'lambda':'0<lambda<4/sqrt(3)','range':'2/(1+S)<=m<=2/(1+a_critical(S))','value':'m/2-lambda*m*w(2/m-1,S)','support_price':'(1-lambda*Mfun(2/m-1,S))/2','scope':'original expected-positive-trial budget, not leakage budget'},
        'finite_search': {'S':'1/2','kappa':'1/10','lambda':'all positive','max_positive_stages':3},
        'exact_small_resource': {'S':'1/2','M':'1','free_stage_probability':'3/4','J':'1/2','C':'0','R':'1'},
        'positive_price_intermediate_witness': {'S':'1/2','lambda':'19/10','kappa':'1/100000','stages':41,'exact_expected_positive_trials':str(wr),'reused_unpriced_lower':str(lower),'coarse_priced_lower':'710259567311/1000000000000','one_stage_upper':'71/100','margin_more_than':'1/5000'},
    },
    'dependencies': {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
}
destination = ROOT / 'lab/process/k2571-stopping-resource-price.json'
if args.write:
    destination.write_text(json.dumps(report, indent=2) + '\n')
else:
    assert json.loads(destination.read_text()) == report, 'saved report mismatch'
print(json.dumps({'result':'K2571','checks':len(checks),'controls':len(controls),'reporting_checks':len(reporting),'status':'pass'}))
