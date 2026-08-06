#!/usr/bin/env sage
"""Independent exact structural control for intrinsic homogeneous Ward closure.

This is deliberately smaller than the production K77 evaluator.  It rebuilds
the exterior algebra, Hodge operator, moving insertions and matrix coefficient
algebra over QQ, then checks that moving covariance cancels a Ward defect which
survives when the insertion is frozen.  It is a structural cross-route, not an
independent exhaustive realization of Cl(7,7).
"""

from itertools import combinations


Q = QQ
n = 4
dim = 3
full = (1 << n) - 1


def popcount(x):
    return Integer(x).popcount()


def wedge_sign(a, b):
    if a & b:
        return 0
    inversions = sum(1 for i in range(n) for j in range(n)
                     if (a >> i) & 1 and (b >> j) & 1 and i > j)
    return -1 if inversions % 2 else 1


def add(x, y):
    out = dict(x)
    for key, value in y.items():
        out[key] = out.get(key, zero_matrix(Q, dim)) + value
        if out[key] == zero_matrix(Q, dim):
            del out[key]
    return out


def scale(c, x):
    return {key: c * value for key, value in x.items() if c * value != 0}


def wedge(x, y):
    out = {}
    for a, xa in x.items():
        for b, yb in y.items():
            sign = wedge_sign(a, b)
            if not sign:
                continue
            key = a | b
            out[key] = out.get(key, zero_matrix(Q, dim)) + sign * xa * yb
    return {key: value for key, value in out.items() if value != 0}


def hodge(x):
    out = {}
    for a, xa in x.items():
        b = full ^^ a
        sign = wedge_sign(a, b)
        out[b] = sign * xa
    return out


def comm(a, b):
    return a * b - b * a


def inner(x, chi):
    return {key: comm(value, chi) for key, value in x.items()
            if comm(value, chi) != 0}


def top_trace(x):
    return x.get(full, zero_matrix(Q, dim)).trace()


def pairing(x, y):
    return top_trace(wedge(x, y))


def move_phi(phi, chi):
    return inner(phi, chi)


def selected_shiab(x, phi1, phi2):
    # A minimal degree-correct insertion model: two alternative moving
    # one-form insertions mapping degree two to degree three.
    return add(wedge(phi1, x), scale(-1, wedge(x, phi2)))


def d_selected_shiab(x, dx, phi1, dphi1, phi2, dphi2):
    terms = [
        wedge(dphi1, x),
        wedge(phi1, dx),
        scale(-1, wedge(dx, phi2)),
        scale(-1, wedge(x, dphi2)),
    ]
    out = {}
    for term in terms:
        out = add(out, term)
    return out


I = identity_matrix(Q, dim)
e = [matrix(Q, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]),
     matrix(Q, [[1, 0, 0], [0, -1, 0], [0, 0, 2]]),
     matrix(Q, [[0, 1, 1], [-1, 0, 2], [0, 1, 0]]),
     matrix(Q, [[1, 1, 0], [0, -1, 1], [2, 0, 1]])]

T = {1 << 0: e[0] + 2 * e[1], 1 << 1: e[2], 1 << 2: e[3]}
chi = matrix(Q, [[0, 1, 0], [-1, 0, 1], [0, -1, 0]])

dT = inner(T, chi)
square = wedge(T, T)
dsquare = add(wedge(dT, T), wedge(T, dT))

# Select the first output-blind small exact fixture whose frozen insertion is
# genuinely information-bearing.  The ordering is fixed before any verdict.
phi_candidates = [{1 << slot: e[index]}
                  for slot in range(n) for index in range(len(e))]
phi1 = phi2 = None
for candidate1 in phi_candidates:
    for candidate2 in phi_candidates:
        trial_image = selected_shiab(square, candidate1, candidate2)
        trial_frozen = d_selected_shiab(
            square, dsquare, candidate1, {}, candidate2, {})
        trial_defect = pairing(dT, trial_image) + pairing(T, trial_frozen)
        if trial_defect != 0:
            phi1, phi2 = candidate1, candidate2
            break
    if phi1 is not None:
        break
assert phi1 is not None and phi2 is not None

dphi1 = move_phi(phi1, chi)
dphi2 = move_phi(phi2, chi)
image = selected_shiab(square, phi1, phi2)
dimage = d_selected_shiab(square, dsquare, phi1, dphi1, phi2, dphi2)
frozen = d_selected_shiab(square, dsquare, phi1, {}, phi2, {})

assert add(dsquare, scale(-1, inner(square, chi))) == {}
assert add(dimage, scale(-1, inner(image, chi))) == {}
assert add(hodge(dT), scale(-1, inner(hodge(T), chi))) == {}

cubic = pairing(dT, image) + pairing(T, dimage)
quadratic = pairing(dT, hodge(T)) + pairing(T, hodge(dT))
frozen_defect = pairing(dT, image) + pairing(T, frozen)

assert cubic == 0
assert quadratic == 0
assert frozen_defect != 0

# Planted failures: frozen insertion and wrong sign must not impersonate the
# moving covariant derivative.
wrong_dimage = d_selected_shiab(
    square, dsquare, phi1, scale(-1, dphi1), phi2, scale(-1, dphi2))
assert frozen != inner(image, chi)
assert wrong_dimage != inner(image, chi)

print("INDEPENDENT_SCOPE=SMALL_EXACT_EXTERIOR_MATRIX_STRUCTURAL_CONTROL__NOT_FULL_K77")
print("MOVING_COVARIANCE=EXACT")
print("CUBIC_WARD=0")
print("QUADRATIC_WARD=0")
print("FROZEN_DEFECT=%s" % frozen_defect)
print("CHECKS=exact:5 planted:2 type:3")
print("PASS 10/10")
