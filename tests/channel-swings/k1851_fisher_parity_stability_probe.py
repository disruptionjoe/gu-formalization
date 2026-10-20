#!/usr/bin/env python3
"""Independent Fraction replay, mathematical faults, then separate report controls."""
from fractions import Fraction as F
from pathlib import Path
import copy
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
r = json.loads((ROOT/"lab/process/k1851-fisher-parity-stability.json").read_text())
n = 0


def ck(value):
    global n
    assert value
    n += 1


def cert(v):
    # Do not import producer, Sympy, or stored check booleans.
    a, b, d, c, e = map(F, v["score"])
    slope, radius, factor = map(F, [v["compact_slope"], v["tail_radius"], v["stein_factor"]])
    if not (c > 0 and e > 0 and b > 0 and d > 0):
        return False
    z0, z1, z2 = a-slope, b-slope*c, d-slope*e
    if not (z1 > 0 and z2 > 0 and z0+z1+z2 < 0 and a+b+d > 0):
        return False
    h = radius*radius
    t0 = a-1+(b-c)*h+(d-e)*h*h
    t1 = b-c+2*(d-e)*h
    t2 = d-e
    if not (t0 > 0 and t1 > 0 and t2 > 0 and radius > 1):
        return False
    exponent = slope/2
    if not (0 < exponent < 1 and factor >= 1/(1-exponent)
            and radius-1+1/radius <= factor and 1/radius <= factor):
        return False
    A, B, C = map(F, v["minorant"])
    L, U, delta = map(F, [v["lower"], v["upper"], v["score_budget"]])
    if not (B > 0 > C and L == A+B+2*C and 0 < delta == U-L):
        return False
    sqrt_upper = F(v["score_sqrt_upper"])
    pair = F(v["optimizer_tv_rational_upper"])
    budget = F(v["moment_error_budget"])
    if not (delta < sqrt_upper*sqrt_upper
            and factor*factor*delta == F(v["reference_tv_bound_squared"])
            and 4*factor*factor*delta == F(v["optimizer_tv_bound_squared"])
            and 4*factor*factor*delta < F(93, 1000)**2 < F(1, 100)
            and pair == 2*factor*sqrt_upper
            and delta+budget == F(1, 625)
            and factor*(F(1, 25)+sqrt_upper) == F(1, 10)
            and F(v["asymmetry_budget"])+pair == F(1, 10)):
        return False
    return list(map(F, v["moment_penalties"])) == [B, -C]


ck(cert(r))  # Green baseline precedes every planted fault.
for dep in r["dependencies"]:
    ck(hashlib.sha256((ROOT/dep["path"]).read_bytes()).hexdigest() == dep["sha256"])

# Independent direct evaluations supplement, but do not replace, coefficient proof.
a, b, d, c, e = map(F, r["score"])
for j in range(33):
    x = F(j, 16)
    y = x*x
    g = x*(a+b*y+d*y*y)/(1+c*y+e*y*y)
    if x <= 1:
        ck(g <= x/2)
    if x >= 1:
        ck(g >= 0)
    if x >= F(3, 2):
        ck(g >= x)

# All-event two-bin covariance bound; not only a CDF test.
for mass in [F(1, 7), F(1, 2), F(6, 7)]:
    for left in [F(0), F(2, 5), F(1)]:
        for right in [F(0), F(3, 4), F(1)]:
            covariance = mass*left-mass*(mass*left+(1-mass)*right)
            ck(abs(covariance) <= mass*(1-mass))

# Fisher convexity from weighted Cauchy, including unequal reflection values.
for p in [F(1, 5), F(1), F(3)]:
    for q in [F(1, 3), F(2)]:
        for dp, dq in [(F(0), F(0)), (F(-2), F(1)), (p, q), (p, -q)]:
            deficit = (dp*dp/p+dq*dq/q)/2-(dp+dq)**2/(2*(p+q))
            ck(deficit == (q*dp-p*dq)**2/(2*p*q*(p+q)) and deficit >= 0)

# Discrete reflected-probability fixtures verify normalization and TV factors.
for p in [[F(1, 10), F(2, 10), F(7, 10)],
          [F(1, 4), F(1, 2), F(1, 4)],
          [F(1), F(0), F(0)]]:
    reflected = p[::-1]
    symmetric = [(u+v)/2 for u, v in zip(p, reflected)]
    alpha = sum(abs(u-v) for u, v in zip(p, symmetric))/2
    reflection_tv = sum(abs(u-v) for u, v in zip(p, reflected))/2
    ck(sum(symmetric) == 1 and symmetric == symmetric[::-1])
    ck(alpha == reflection_tv/2)
    for degree in [2, 4]:
        ck(sum(x**degree*v for x, v in zip([-1, 0, 1], p)) ==
           sum(x**degree*v for x, v in zip([-1, 0, 1], symmetric)))

# Exact signs in moment-error residual and absolute-value bound.
A, B, C = map(F, r["minorant"])
L, U = F(r["lower"]), F(r["upper"])
for e2 in [F(-1, 10000), F(0), F(1, 10000)]:
    for e4 in [F(-1, 10000), F(0), F(1, 10000)]:
        exact = U-A-B*(1+e2)-C*(2+e4)
        ck(exact == U-L-B*e2-C*e4)
        ck(exact <= U-L+B*abs(e2)-C*abs(e4))

faults = [
    ("score", ["-2", "12003/10000", "137193/500000", "266879/500000", "43447/2000000"]),
    ("score", ["-26379/25000", "12003/10000", "137193/500000", "-1", "43447/2000000"]),
    ("compact_slope", "1/10"),
    ("tail_radius", "1"),
    ("stein_factor", "1"),
    ("score_budget", "1/1000"),
    ("score_sqrt_upper", "3/100"),
    ("optimizer_tv_rational_upper", "1/20"),
    ("moment_error_budget", "1/1000"),
    ("moment_penalties", ["9487187/1000000", "-1406001/500000"]),
    ("asymmetry_budget", "1/100"),
]
for key, value in faults:
    q = copy.deepcopy(r)
    q[key] = value
    ck(not cert(q))


def report_ok(v):
    return (not v["reference_is_optimizer"] and not v["new_spectral_gap_claim"]
            and not v["vanishing_excess_modulus"] and not v["physical_claim"]
            and v["nonsymmetric_requires_asymmetry_defect"])


ck(report_ok(r))
report_faults = [("reference_is_optimizer", True), ("new_spectral_gap_claim", True),
                 ("vanishing_excess_modulus", True), ("physical_claim", True),
                 ("nonsymmetric_requires_asymmetry_defect", False)]
for key, value in report_faults:
    q = copy.deepcopy(r)
    q[key] = value
    ck(not report_ok(q))
print("K1851 independent controls", n, "including", len(faults),
      "input faults and", len(report_faults), "reporting faults")
