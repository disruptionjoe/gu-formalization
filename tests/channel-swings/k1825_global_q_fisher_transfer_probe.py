#!/usr/bin/env python3
"""Independent exact algebra/normalization controls plus reporting faults.

The analytic compactness theorem is reviewed in prose; these are finite
mathematical controls, not numerical integration of the Fisher objective.
"""
import copy
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
spec = importlib.util.spec_from_file_location('k1825_producer', HERE/'k1825_global_q_fisher_transfer.py')
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)


def independent_transfer(scale, j):
    # Integrate the reciprocal-information/Riccati comparison, independently
    # of the producer's denominator implementation.
    if j == 0:
        return F(0)
    return 1/((1+1/j)/scale-1)


def mathematical_controls():
    cases = 0
    for j in (F(0), F(1,1000), F(1,4), F(2,3)):
        for theta in (F(1,8), F(1,3), F(1,2), F(3,4)):
            ordinary_i = (1+j)/(theta+(1-theta)*(1+j))
            expected = ordinary_i-1
            assert expected == independent_transfer(theta,j)
            assert producer.transfer(theta,j) == expected
            assert expected <= theta*j
            if j:
                assert expected < theta*j
            for eta in (F(1,5),F(2,3)):
                assert independent_transfer(eta,expected) == independent_transfer(theta*eta,j)
            if j:
                assert independent_transfer(1/theta,expected) == j
            cases += 1
    # Valid centered unit-variance Gaussian: J=0 and every transfer is equality.
    assert independent_transfer(F(3,4),F(0)) == 0
    # Dropping centering invalidates E r'=-J and the strengthened bound.
    # A Gaussian of variance one and mean sqrt(t)*m has r=sqrt(t)*m,
    # J=t*m^2, q=t^2, r'=0, and J_q=m^2/(2*t).
    for m in (F(1,2),F(1),F(2)):
        for t in (F(1,4),F(1,2),F(3,4)):
            j=t*m*m
            actual_q_derivative=m*m/(2*t)
            claimed_bound=j*(1+j)/(2*t*t)
            assert actual_q_derivative < claimed_bound
            assert -j != 0
    # Wrong signal scale q1/q2 instead of its square root changes the theorem.
    assert independent_transfer(F(1,2),F(1,4)) == F(1,9)
    assert independent_transfer(F(1,4),F(1,4)) == F(1,19)
    assert F(1,9)>F(1,19)
    print(f'PASS: {cases} ordinary-Fisher controls with composition/inverse; Gaussian equality; 9 centering counterexamples; q-scale fault')


def chart_controls():
    cases=0
    for inner in (F(0),F(1,4),F(1,2),F(3,4)):
        for outer in (F(5,4),F(3,2),F(2)):
            z=1-inner*inner
            c=z*(outer*outer-1)
            if not 0<c<2:
                continue
            p=(outer*outer-1)/(outer*outer-inner*inner)
            moments={k:p*inner**k+(1-p)*outer**k for k in (2,4,6)}
            assert moments[2]==1 and moments[4]==1+c
            mse=p*(inner-1)**2+(1-p)*(outer-1)**2
            assert mse <= z+z*z <= 2*z
            for t in (F(1,8),F(1,4),F(1,2),F(3,4)):
                v=1-t
                q=(2-c)*t*t
                assert c<2-q
                ey2=t*moments[2]+v
                ey4=t*t*moments[4]+6*t*v*moments[2]+3*v*v
                ey6=t**3*moments[6]+15*t*t*v*moments[4]+45*t*v*v*moments[2]+15*v**3
                assert ey2==1 and ey4-3==-q
                # The H3 Stein test independently gives a positive objective
                # lower bound for each law, not a uniform infimum bound.
                stein=ey4-6*ey2+3
                gram=ey6-6*ey4+9*ey2
                assert stein==-q and gram>0
                assert 0<stein*stein/gram <= t/v
                cases+=1
    # Artificial z=0,c=1 loses fourth moment despite W2 convergence.
    for n in (10,100,1000):
        z=F(1,n*n)
        rare_weight=z*z/(1+z*z)
        b=1+1/z  # squared outer radius
        assert rare_weight < z*z
        assert rare_weight*b < 2*z
        assert rare_weight*b*b > 1
        assert (1-rare_weight)*(1-z)**2+rare_weight*b*b == 2
    print(f'PASS: {cases} normalized chart/cumulant/H3 controls; exact same-sign coupling; 3 lost-fourth-moment controls')


def collar_controls():
    # Independent rational implementation; the production samples are separate.
    for k in range(1,40):
        q=F(k,20)
        bound=4/(2-q)
        n=(2*bound+10).__ceil__()
        eps=F(1,2**n)
        c=2-q/(1-eps)**2
        assert 0<c<2-q
        assert q/2 < (bound/(1+bound))**2
        assert eps<1/(bound+1)
        assert F(n-4,2)>bound
        ratio=((1-eps/2)/(1-eps))**2
        # q' halfway to the cross-admissibility endpoint leaves noise>eps/2.
        qprime=q*(1+ratio)/2
        assert (1-eps)**2*(qprime/q)<(1-eps/2)**2
        expected=producer.compact_constants(q)
        assert expected['noise_exponent']==n
        assert F(expected['compact_c_max'])==c
    print('PASS: 39 rational collar and cross-admissibility controls, including q near 2')


def transfer_consumers(data):
    q0=F(data['fixed_q']['q0'])
    lo=F(data['fixed_q']['value_lower'])
    hi=F(data['fixed_q']['value_upper'])
    rows=data['inherited_value_transfers']
    for row in rows['higher_q_strict_lower']:
        scale=F(row['scale'])
        assert F(row['q'])==q0*scale*scale
        assert F(row['strict_lower'])==independent_transfer(scale,lo)
        assert F(row['strict_lower'])>lo
    for row in rows['lower_q_strict_upper']:
        scale=F(row['scale'])
        assert F(row['q'])==q0*scale*scale
        assert F(row['strict_upper'])==independent_transfer(scale,hi)
        assert F(row['strict_upper'])<hi
    for row in rows['inverse_budget_exclusions']:
        budget=F(row['budget'])
        cap=F(row['q_cap'])
        scale=(1+1/lo)/(1+1/budget)
        assert cap==q0*scale*scale
        assert independent_transfer(scale,lo)==budget
    assert F(rows['higher_q_strict_lower'][4]['strict_lower'])>F(50937,10**10)
    assert F(rows['lower_q_strict_upper'][0]['strict_upper'])<F(79590,10**12)
    assert F(rows['inverse_budget_exclusions'][1]['q_cap'])<F(1,256)
    assert F(rows['inverse_budget_exclusions'][2]['q_cap'])<F(39,1000)
    for row in rows['lower_budget_inverse_strict_lower']:
        budget=F(row['budget'])
        scale=(1+1/hi)/(1+1/budget)
        assert 0<scale<1
        assert F(row['strict_q_lower'])==q0*scale*scale
        assert independent_transfer(scale,hi)==budget
    # Exact endpoint sequences for the analytic limit proof. At q=2/n^2
    # the Rademacher candidate upper bound is 1/(n-1). At
    # q=2*(1-2^-n)^2 the entropy floor is (n-4)*log2>(n-4)/2.
    for n in (5,10,20,40):
        qsmall=F(2,n*n)
        tsmall=F(1,n)
        assert tsmall*tsmall==qsmall/2
        assert tsmall/(1-tsmall)==F(1,n-1)
        tlarge=1-F(1,2**n)
        qlarge=2*tlarge*tlarge
        assert 0<qsmall<qlarge<2
        assert 1-tlarge==F(1,2**n)
        assert F(n-4,2)>0
    print('PASS: 12 independent reciprocal transfers, 6 inverse consumers, 4 displayed bounds and 4 endpoint-sequence controls')


def reporting_faults(data):
    mutations=[]
    for key in ('all_q_regular_open_chart_attainment','all_q_uniqueness_or_smooth_optimizer_branch','endpoint_q_zero_or_two_included'):
        bad=copy.deepcopy(data); bad['global_results'][key]=True; mutations.append(bad)
    for key in ('arbitrary_channel_optimizer','physical_claim','source_or_physics_ledger_change','canon_promotion'):
        bad=copy.deepcopy(data); bad['claim_boundary'][key]=True; mutations.append(bad)
    bad=copy.deepcopy(data); bad['verification_boundary']['new_numeric_integration']=True; mutations.append(bad)
    bad=copy.deepcopy(data); bad['fixed_q']['q0']='1/512'; mutations.append(bad)
    bad=copy.deepcopy(data); bad['compact_constant_controls'][0]['noise_exponent']=1; mutations.append(bad)
    bad=copy.deepcopy(data); bad['inherited_value_transfers']['higher_q_strict_lower'][0]['scale']='4'; mutations.append(bad)
    bad=copy.deepcopy(data); bad['input_sha256'].pop(next(iter(bad['input_sha256']))); mutations.append(bad)
    for bad in mutations:
        try:
            producer.validate(bad)
        except ValueError:
            continue
        raise AssertionError('accepted reporting mutation')
    for q in (F(0),F(-1),F(2),F(3)):
        try:
            producer.compact_constants(q)
        except ValueError:
            continue
        raise AssertionError('accepted invalid q')
    try:
        producer.transfer(3,1)
    except ValueError:
        pass
    else:
        raise AssertionError('accepted nonpositive transfer denominator')
    print(f'PASS: {len(mutations)} reporting mutations, four domain faults and one denominator fault')


def main():
    data=json.loads((ROOT/'lab/process/k1825-global-q-fisher-transfer.json').read_text())
    producer.validate(data)
    mathematical_controls()
    chart_controls()
    collar_controls()
    transfer_consumers(data)
    reporting_faults(data)


if __name__=='__main__':
    main()
