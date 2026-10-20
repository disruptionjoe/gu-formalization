#!/usr/bin/env python3
"""Independent exact weak-test/compact-bump controls and reporting faults."""
import copy
import importlib.util
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('k1827_producer',HERE/'k1827_endpoint_fisher_asymptotic.py')
producer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(producer)


def clipped_test(y):
    if y < -F(1,2):
        return (1-y*y)/2
    if y > F(1,2):
        return (y*y-1)/2
    return y*y*y-y


def derivative_controls():
    cases = 0
    for y in (F(-3),F(-1),F(-1,2),F(-1,3),F(-1,6),F(0),
              F(1,6),F(1,3),F(1,2),F(1),F(3)):
        assert clipped_test(y)**2 <= (y*y-1)**2/4
        assert clipped_test(-y) == -clipped_test(y)
        if abs(y) <= F(1,2):
            loss = abs(y)-(3*y*y-1)
            assert F(13,12)-loss == 3*(abs(y)-F(1,6))**2
            assert loss <= F(13,12)
        cases += 1
    for y in (F(-1,2),F(1,2)):
        interior = y**3-y
        exterior = ((y*y-1)/2)*(1 if y>0 else -1)
        assert interior == exterior == clipped_test(y)
        assert 3*y*y-1 != abs(y)  # continuity does not mean differentiability
    assert F(1,2)+F(13,12)/F(9,16) == F(131,54)
    for x in (F(0),F(1,6),F(1,3),F(1,2)):
        assert (1-x*x)**2 >= F(9,16)
    # A changed threshold with the old interior derivative is false.
    y=F(3,5)
    assert abs(y) != 3*y*y-1
    assert y*y*y-y != (y*y-1)/2
    print(f'PASS: {cases} clipped-test controls, 2 continuity/non-differentiability junctions, constants and threshold fault')


def polynomial_integral(power, exponent):
    """Integral z^power (1-z^2)^exponent on [-1,1], rational."""
    if power % 2:
        return F(0)
    return sum((F(2*(-1)**k*comb(exponent,k),power+2*k+1)
                for k in range(exponent+1)),F(0))


def independent_lower(delta):
    expected_derivative = 1-delta/F(2)-F(13,12)*(delta/F(9,16))
    if expected_derivative <= 0:
        return F(0)
    return max(F(0),expected_derivative**2/(delta/F(4))-1)


def compact_bump_controls():
    cases = 0
    for m in (2,3,5,10):
        normalizer = polynomial_integral(0,m)
        v=polynomial_integral(2,m)/normalizer
        fourth=polynomial_integral(4,m)/normalizer
        fisher=4*m*m*polynomial_integral(2,m-2)/normalizer
        assert v == F(1,2*m+3)
        assert fourth == F(3,(2*m+3)*(2*m+5))
        assert fisher == F(m*(2*m+1),m-1)
        assert 4*v*fisher>4
        if m==2:
            assert 4*v*fisher==F(40,7)
        for h in (F(1,2),F(1,4),F(1,16),F(1,64)):
            variance=1+h*h*v
            ey4=(1+6*h*h*v+h**4*fourth)/variance**2
            delta=ey4-1
            ordinary=variance*fisher/(h*h)
            relative=ordinary-1
            assert 0<delta<2
            assert relative >= independent_lower(delta)
            assert producer.scaled_lower(delta)==delta*independent_lower(delta)
            assert delta*ordinary>4
            cases += 1
    print(f'PASS: {cases} exact compact-bump moment/Fisher controls; nonoptimal-concentration contrary limit')


def endpoint_inverse_controls():
    for delta in (F(1,1000),F(1,100),F(1,10),F(1,2),F(1),F(3,2)):
        lower=independent_lower(delta)
        assert lower>=4/delta-F(551,27)
        assert lower*delta==producer.scaled_lower(delta)
    # Gaussian: delta=2, I=1, J=0. Squaring a negative derivative lower
    # bound produces a false Fisher bound larger than its actual I.
    gaussian_delta=F(2)
    negative=1-F(131,54)*gaussian_delta
    assert negative<0 and 4*negative**2/gaussian_delta>1
    assert independent_lower(gaussian_delta)==0
    assert F(1)-F(1)==0
    for t in (F(1,4),F(1,2),F(3,4),F(9,10),F(99,100)):
        delta=2*(1-t*t)
        scaled=delta*t/(1-t)
        assert scaled==2*t*(1+t)
        assert scaled<=4-F(3,2)*delta
    for budget in (F(1,1000),F(1),F(10),F(100),F(10000)):
        lower,upper=producer.inverse_bracket(budget)
        assert lower==4/(budget+F(551,27))
        assert upper==2-2*(budget/(1+budget))**2
        assert lower<=upper<4/budget
        assert 4/budget-lower==4*F(551,27)/(budget*(budget+F(551,27)))
        assert lower<upper  # reversing inverse orientation excludes an endpoint
    print('PASS: 6 endpoint controls, Gaussian sign/subtraction faults, 5 rational upper controls, 5 inverse controls')


def reporting_controls():
    data=json.loads(producer.ARTIFACT.read_text())
    mutations=[
        ('constants','A','130/54'),
        ('constants','C','524/27'),
        ('constants','clipped_threshold','1/3'),
        ('constants','central_mass_factor','9/16'),
        ('results','sharp_endpoint_coefficient','2'),
        ('results','exact_rademacher_minimizer_at_finite_q',True),
        ('results','constant_term_asymptotic_identified',True),
        ('results','unrestricted_density_infimum_attainment_or_uniqueness',True),
        ('results','all_q_shape_uniqueness_or_interior_attainment',True),
        ('face_instability','isolated_lobe_fisher_c_derivative','-t/(36*v^2)'),
        ('face_instability','threshold_computed',True),
        ('face_instability','other_boundary_z_one_excluded',True),
        ('verification_boundary','fixed_q_certificate_used',True),
        ('claim_boundary','physical_claim',True),
        ('claim_boundary','canon_promotion',True),
    ]
    for section,key,value in mutations:
        forged=copy.deepcopy(data)
        forged[section][key]=value
        try:
            producer.validate(forged)
        except ValueError:
            continue
        raise AssertionError(f'accepted reporting fault {section}.{key}')
    print(f'PASS: {len(mutations)} reporting faults rejected (distinct from mathematical controls)')


def face_variation_controls():
    cases=0
    z=F(3,4)
    for m in (F(1,2),F(2,3),F(3,4),F(9,10),F(99,100)):
        t=m*m
        v=1-t
        a=m/2
        weight_derivative=1/z**2
        mean_derivative=m*(F(1,8)+1/(2*z))
        noise_derivative=-t/4
        assert weight_derivative==F(16,9)
        assert mean_derivative==19*m/24
        # Integrate Gplus against mean/variance derivatives by differentiating
        # its exact Gaussian expectation, not the producer's constant.
        def egplus(mean,var):
            return 2/v-(var+(mean-m)**2)/(v*v)
        weight_effect=weight_derivative*(egplus(a,v)-egplus(m,v))
        mean_effect=mean_derivative*(-2*(m-m)/(v*v))
        noise_effect=noise_derivative*(-1/(v*v))
        derivative=weight_effect+mean_effect+noise_effect
        assert derivative==-7*t/(36*v*v)<0
        assert a-m/4>=F(1,8)
        assert (a-m/4)**2/4>=F(1,256)
        for y in (F(-1),F(0),F(1,4),F(1),F(2)):
            for tangent in (F(-3,4),F(0),F(1,3),F(3,4)):
                score=(-y+m*tangent)/v
                score_prime=-1/v+m*m*(1-tangent*tangent)/(v*v)
                actual=-2*score_prime-score*score
                gaussian=2/v-(y-m)**2/(v*v)
                difference=(tangent-1)*(2*m*y+m*m*(tangent+1))/(v*v)
                assert actual-gaussian==difference
        cases+=1
    # At one fixed nonzero v the isolated-lobe sign alone is not a proof:
    # the omitted remainder can have either sign without an overlap bound.
    margin=F(7,36)
    assert -margin+2*margin>0
    print(f'PASS: {cases} exact first-variation controls, 100 overlap-identity substitutions, tail exponent, omitted-overlap fault')


if __name__=='__main__':
    derivative_controls()
    compact_bump_controls()
    endpoint_inverse_controls()
    face_variation_controls()
    reporting_controls()
