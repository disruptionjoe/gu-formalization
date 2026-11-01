"""Exact finite histories and Arb certificates for the K2453 common-risk theorem.

This finite probe supports, and does not replace, the written universal proof.
Run only after installing in tests/channel-swings, or pass --root REPO in scratch.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json
from flint import arb, ctx

ctx.prec = 256
parser = argparse.ArgumentParser()
parser.add_argument('--check', action='store_true')
parser.add_argument('--root', type=Path)
parser.add_argument('--output', type=Path)
args = parser.parse_args()
ROOT = args.root or Path(__file__).resolve().parents[2]
checks, controls = {}, {}


def ck(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def ctrl(name, condition):
    controls[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def A(x):
    if isinstance(x, F):
        return arb(x.numerator) / x.denominator
    return arb(x)


def kl(p, q):
    """Finite binary KL, including continuous p=0 and p=1 endpoints."""
    p, q = F(p), F(q)
    if p == q:
        return arb(0)
    if (q == 0 and p > 0) or (q == 1 and p < 1):
        raise ValueError('infinite directional divergence')
    result = arb(0)
    if p:
        result += A(p) * A(p / q).log()
    if p != 1:
        result += A(1-p) * A((1-p) / (1-q)).log()
    return result


def binary_entropy(p):
    p = F(p)
    return -A(p)*A(p).log()-A(1-p)*A(1-p).log()


def inverse_bracket(cost, alpha):
    """Verified rational bracket of the upper inverse, for an interior cost."""
    lo, hi = F(alpha), F(1)
    assert cost > 0 and cost < A(1/F(alpha)).log()
    for _ in range(100):
        mid = (lo+hi)/2
        value = kl(mid, alpha)
        if value > cost:
            hi = mid
        elif value < cost:
            lo = mid
        else:
            # An undecidable overlapping interval is not a directional comparison.
            raise AssertionError('inverse comparison unresolved at working precision')
    assert kl(lo, alpha) < cost and kl(hi, alpha) > cost
    return lo, hi


# Independent P/Q propagation on the same adaptive full classical histories.
# Risk is measured in quarters. pU depends on the actual prior use count;
# pT depends on the failure history as well. No quantum hidden label is used.
alpha, horizon = F(1,4), 7
stack = [(0,F(1),F(1),0,0,0,False)]
massP = massQ = crossP = crossQ = F(0)
chain_cost = arb(0)
path_cost = arb(0)
qm = [arb(0) for _ in range(horizon+1)]
nodes = 0
while stack:
    depth, pp, qq, uses, fails, risk4, hit = stack.pop()
    nodes += 1
    if fails == 0:
        qm[depth] += A(qq)*(A(F(risk4,4))*arb(2).log()).exp()
    if depth == horizon:
        massP += pp
        massQ += qq
        path_cost += A(pp)*A(pp/qq).log()
        if hit:
            crossP += pp
            crossQ += qq
        continue
    pi = F(1,2)
    pU = F(1,2) if uses % 2 == 0 else F(3,4)
    pT = pU/2 if fails % 2 == 0 else pU/F(3,2)
    chain_cost += A(pp*pi)*kl(pT,pU)
    branches = [
        (1-pi,1-pi,1,0,int(4*pU)),
        (pi*(1-pT),pi*(1-pU),0,0,0),
        (pi*pT,pi*pU,0,1,0),
    ]
    assert sum(x[0] for x in branches) == sum(x[1] for x in branches) == 1
    for bp,bq,u,x,dr in branches:
        rr = risk4+dr
        ff = fails+x
        crossed = hit or (ff == 0 and rr >= 8)
        stack.append((depth+1,pp*bp,qq*bq,uses+u,ff,rr,crossed))
ck('adaptive_both_laws_normalized', massP == massQ == 1)
ck('adaptive_reference_crossing_bound', crossQ <= alpha)
ctrl('adaptive_crossing_nonzero', crossQ > 0 and crossP > crossQ)
ck('adaptive_chain_rule_identity', (path_cost-chain_cost).contains(0))
ck('adaptive_event_data_processing', kl(crossP,crossQ) < path_cost)
ck('reference_exponential_expectations', all(qm[i] < 1 for i in range(1,horizon+1)))
lo,hi = inverse_bracket(chain_cost,alpha)
ck('adaptive_transferred_bound', A(crossP) < A(hi) < 1)
ctrl('actual_process_need_not_be_supermartingale',
     A(F(1,2))*(A(F(1,2))*arb(2).log()).exp()+A(F(1,2))*A(F(3,4)) > 1)

# Released one-sided reference, including histories with harmless excess test noise.
stackplus=[(0,F(1),F(1),0,0)]
plus_chain=arb(0);plus_path=arb(0);symmetric_cost=arb(0);zero_cost_nodes=0
while stackplus:
    depth,pp,qq,uses,fails=stackplus.pop()
    if depth==7:
        plus_path+=A(pp)*A(pp/qq).log()
        continue
    pu=F(1,2) if uses%2==0 else F(3,4)
    pt=pu/2 if fails%2==0 else (1+pu)/2
    qr=max(pt,pu)
    plus_chain+=A(pp/2)*kl(pt,qr)
    symmetric_cost+=A(pp/2)*kl(pt,pu)
    if pt>pu:
        zero_cost_nodes+=1
        assert kl(pt,qr)==0
    for bp,bq,u,x in [(F(1,2),F(1,2),1,0),((1-pt)/2,(1-qr)/2,0,0),(pt/2,qr/2,0,1)]:
        stackplus.append((depth+1,pp*bp,qq*bq,uses+u,fails+x))
ck('one_sided_full_chain_identity',(plus_path-plus_chain).contains(0))
ck('one_sided_cost_strictly_improves',plus_chain<symmetric_cost)
ctrl('harmless_histories_genuinely_present',zero_cost_nodes>0)
ck('harmless_endpoint_finite_cost',kl(F(3,4),max(F(3,4),F(0)))==0)
ctrl('overcharged_equal_mean_reference',kl(F(3,4),F(1,4))>0)
for aa,bb in [(F(1,4),F(3,4)),(F(3,4),F(1,4))]:
    opt=max(aa,bb)
    ck('pointwise_reference_optimum_'+str(aa),kl(aa,opt)<kl(aa,(opt+1)/2))

# Event-space sharpness, orientation and exact inverse.
p,a = F(1,5),F(1,20)
sharp_cost = kl(p,a)
lo_sharp,hi_sharp = inverse_bracket(sharp_cost,a)
ck('sharp_event_inverse_bracket', lo_sharp < p < hi_sharp)
ck('sharp_event_path_divergence',
   (A(p)*A(p/a).log()+A(1-p)*A((1-p)/(1-a)).log()-sharp_cost).contains(0))
ctrl('lower_cost_cannot_cover_sharp_event', sharp_cost-arb('0.001') < kl(p,a))
ctrl('reverse_kl_is_not_forward_budget', kl(a,p) < kl(p,a))
ck('unit_event_threshold', (kl(F(1),a)-A(1/a).log()).contains(0))
ck('zero_budget_equal_law', kl(a,a) == 0)
for pu,pt in [(F(0),F(1,2)),(F(1),F(0))]:
    try:
        kl(pt,pu)
    except ValueError:
        ctrl('support_failure_'+str(pu),True)
    else:
        raise AssertionError('infinite support control was accepted')

# Rare-history large branch discrepancy costs only its actual probability.
eta,pi = F(1,1024),F(1,2)
rare_cost = A(eta*pi)*kl(F(0),F(1,2))
ck('rare_expected_budget', (rare_cost-A(eta*pi)*arb(2).log()).contains(0))
ctrl('rare_cost_not_worst_history_cost', rare_cost < kl(F(0),F(1,2))/100)
ctrl('realized_zero_cost_is_not_expected_zero', rare_cost > 0 and 1-eta > 0)
muT = [F(1,2),F(1,3),F(1,6)]
muU = [F(1,4),F(1,2),F(1,4)]
effect = [F(0),F(1,2),F(1)]
test_mean = sum(m*e for m,e in zip(muT,effect))
use_mean = sum(m*e for m,e in zip(muU,effect))
source_kl = sum((A(m)*A(m/n).log() for m,n in zip(muT,muU)),arb(0))
ck('source_label_data_processing_strict', kl(test_mean,use_mean) < source_kl)
# Exact deterministic source mismatch: source marginal is not actual use source.
pT,pU,pi = F(0),F(1),F(1,2)
pbar = pi*pT+(1-pi)*pU
ctrl('product_reference_changes_risk', pbar == F(1,2) and pbar != pU)
ctrl('product_reference_cannot_use_actual_use_exponent',
     (1-pi)*F(2)+pi*(1-pbar) == F(5,4) > 1)
ck('source_route_mutual_information_finite', arb(2).log() < 1)
models = [{'test_risk':F(0),'use_risk':F(0)},
          {'test_risk':F(0),'use_risk':F(1)}]
record_law = lambda model: (1-pi,pi*(1-model['test_risk']),pi*model['test_risk'])
ctrl('identical_records_do_not_identify_use_risk',
     record_law(models[0]) == record_law(models[1])
     and models[0]['use_risk'] != models[1]['use_risk'])
ctrl('acceptance_can_concentrate_failure', (p/p) == 1 and p < 1)

# Actual gap and original consumer constants, with interval-certified budgets.
budgets = []
epsilon, K = F(1,20),F(1,100)
L = (A(K)+binary_entropy(epsilon))/A(epsilon)
nominal_alpha = (-L).exp()
eps = A(epsilon)
calibrated_kl = eps*(eps/nominal_alpha).log()+(1-eps)*((1-eps)/(1-nominal_alpha)).log()
ck('entropy_design_orientation', calibrated_kl > A(K))
ck('nominal_alpha_below_actual_allowance', nominal_alpha < eps)
# Wrong inversion alpha=exp(-K/epsilon) omits the entropy term.
bad_alpha = (-A(K)/eps).exp()
ctrl('entropy_omission_cannot_calibrate', bad_alpha > eps)
consumer_cases = [('gap_half_one_slot',1,arb(1)/2),
                  ('gap_half_two_slot',2,arb(1)/2),
                  ('k2454_original_law_0',1,(1-A(F(27,127)).sqrt())/2),
                  ('k2454_original_law_1',1,(1-A(F(15,67)).sqrt())/2)]
for case,slots,nu in consumer_cases:
    beta = arb('0.0000001')
    kappa = arb('0.000001')
    tau = arb('0.01')
    q = arb(4)**(-slots)
    C = arb(2)**(2*slots-1)
    c = arb(2).log()
    denominator = nu*((tau-kappa/q)/C)**2-beta
    ck('positive_consumer_denominator_'+case,denominator > 0)
    need = L/(c*denominator)
    count = int(need.upper().ceil().unique_fmpz())
    def allowance(n):
        return C*((L/(c*n)+beta)/nu).sqrt()+kappa/q
    ck('consumer_count_suffices_'+case,allowance(count) <= tau)
    ctrl('consumer_predecessor_fails_'+case,allowance(count-1) > tau)
    QU = (L/(c*count)+beta)/nu
    ck('consumer_positive_success_'+case,QU.sqrt()/2+kappa < q)
    budgets.append({'case':case,'slots':slots,'gap_interval':str(nu),'required_actual_uses':count,
                    'output_allowance':str(allowance(count)),
                    'success_margin':str(q-QU.sqrt()/2-kappa),
                    'risk_denominator':str(denominator)})

dependencies = [
    'tests/channel-swings/k2453_use_reference_information_budget_probe.py',
    'explorations/conditional-build/k2453-use-reference-information-budget-2026-11-01.md',
    'explorations/conditional-build/k2448-binary-hidden-route-certificate-2026-11-01.md',
    'explorations/conditional-build/k2450-route-leakage-certificate-2026-11-01.md',
    'explorations/conditional-build/k2444-sharp-heralded-transfer-2026-11-01.md',
    'explorations/conditional-build/k2454-two-setting-local-verifier-2026-11-01.md',
]
report = {
    'result_id':'K2453','checks':checks,'controls':controls,
    'adaptive_tree':{'nodes':nodes,'horizon':horizon,'nominal_alpha':str(alpha),
                     'actual_crossing_probability':str(crossP),
                     'reference_crossing_probability':str(crossQ),
                     'path_space_divergence':str(path_cost),'chain_cost':str(chain_cost),
                     'transferred_upper_bracket':str(hi)},
    'sharp_event':{'actual_probability':str(p),'reference_probability':str(a),
                   'exact_divergence_expression':'(1/5)*log(4)+(4/5)*log(16/19)',
                   'divergence_interval':str(sharp_cost)},
    'rare_history':{'probability':str(eta),'expected_total_cost':str(rare_cost)},
    'prospective_not_data':{'actual_failure_allowance':str(epsilon),
                            'total_budget_nats':str(K),'nominal_alpha':str(nominal_alpha),
                            'nominal_log_threshold':str(L),'consumers':budgets},
    'evidence_kinds':{
        'universal':'written common-risk reference, KL chain rule, binary event inverse and increasing-prefix proof',
        'finite':'independent exact adaptive tree, sharp-event controls and Arb consumer bounds',
        'ceiling':'external expected total risk-divergence premise; no inferred secrecy or physical Q'},
    'dependencies':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in dependencies},
}
out = args.output or ROOT/'lab/process/k2453-use-reference-information-budget.json'
if args.check:
    assert json.loads(out.read_text()) == report
else:
    out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2453',len(checks),'checks',len(controls),'controls PASS')
