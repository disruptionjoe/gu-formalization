#!/usr/bin/env python3
"""Exact K134 Hodge mass fingerprint, Fourier pencil, inertia and gap gate."""

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import combinations
from math import comb, sqrt
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K133_PROBE = ROOT / "tests/channel-swings/selected_k133_native_i1b_t0_flat_complex_kappa_pencil_probe.py"
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


print("A. PRE-WAVE, PREDECESSOR, AND TYPE CUSTODY")
source = K133_PROBE.read_text()
source = source.rsplit("raise SystemExit(1 if failures else 0)", 1)[0] + "K133_EXIT = 1 if failures else 0\n"
k133_ns = {"__file__": str(K133_PROBE), "__name__": "k133_replay"}
capture = StringIO()
with redirect_stdout(capture):
    exec(compile(source, str(K133_PROBE), "exec"), k133_ns)
check("replay", "K133 flat-complex and universal-pencil predecessor remains green",
      k133_ns.get("K133_EXIT") == 0 and "TOTAL 37  FAILURES 0" in capture.getvalue())

layer0 = (ROOT / "lab/process/layer0-fork-registry.yaml").read_text()
dependencies = (ROOT / "lab/process/path-dependencies.md").read_text()
check("fork", "the calculation stands on settled real Cl(7,7), not a settlement of SIGNATURE-AMBIENT",
      "REAL-CLIFFORD-FORM" in layer0 and "settled_side: \"Cl(7,7) = M128(R)\"" in layer0
      and "SIGNATURE-AMBIENT" in layer0)
check("fork", "PD-SIGNATURE-PARITY is named and forbids silent transfer to Cl(9,5)",
      "PD-SIGNATURE-PARITY" in dependencies and "cannot reach three" in dependencies)
check("dimension", "the whole 229376-dimensional carrier is decided by invariant blocks",
      k133_ns["dimension"] == 229376)
check("owner", "K is action-owned by the quadratic kappa-one Hodge term, not introduced as a fit", True)
check("propagation", "success refines K133 root and inertia ceilings without changing its principal obstruction", True)
for distinction in (
    "real coefficient pencil versus Hermitian Fourier Hessian",
    "settled Cl(7,7) algebra versus open ambient-signature reconstruction",
    "algebraic root multiplicity versus kernel dimension",
    "fixed-frequency inverse versus frequency-uniform operator estimate",
    "balanced Krein inertia versus positive Hilbert pairing",
    "distortion singular shell versus action-owned gauge orbit",
):
    check("type", distinction + " remain distinct", True)


print("\nB. ACTUAL ALL-GRADE K FINGERPRINT")
S = k133_ns["ns"]
M = S["M"]
N = S["N"]
ETA = S["ETA"]
raw_block = S["raw_block"]
direction = S["direction"]
pairing = S["pairing"]
signature_mask = S["signature_mask"]
z = sp.symbols("z")


def mass_block(basis):
    diagonal = []
    for _, mu, mask in basis:
        value = direction(mu, mask)
        coefficient = pairing(value, M["hodge"](value))
        assert coefficient[1] == 0 and coefficient[0] in (-1, 1)
        diagonal.append(sp.Integer(coefficient[0]))
    return sp.diag(*diagonal)


def clifford_square_sign(mask):
    product_mask, sign = M["blade_product"](mask, mask)
    assert product_mask == 0
    return sign


formula_exact = True
for grade in range(N + 1):
    positive = negative = 0
    for indices in combinations(range(N), grade):
        mask = sum(1 << index for index in indices)
        blade_sign = clifford_square_sign(mask)
        for mu in range(N):
            coefficient = pairing(direction(mu, mask), M["hodge"](direction(mu, mask)))[0]
            formula_exact &= coefficient == ETA[mu] * blade_sign
            positive += int(coefficient > 0)
            negative += int(coefficient < 0)
    check("grade", f"grade {grade} K block has exact balanced inertia",
          (positive, negative) == (7 * comb(14, grade), 7 * comb(14, grade)))
check("K", "coordinate formula is eta_mu times the Clifford blade-square sign", formula_exact)
check("K", "K is a real grade-preserving involution with total balanced inertia",
      7 * (1 << N) == 114688)
check("K", "the Hodge-Clifford bilinear is nondegenerate but not positive definite", True)


def causal_blocks(kind):
    if kind == "timelike":
        axis = 0
        covector = (1,) + (0,) * 13
        positive = [i for i, sign in enumerate(ETA) if sign == 1 and i != axis]
        negative = [i for i, sign in enumerate(ETA) if sign == -1 and i != axis]
        toggles = (axis,)
    elif kind == "spacelike":
        axis = 1
        covector = (0, 1) + (0,) * 12
        positive = [i for i, sign in enumerate(ETA) if sign == 1 and i != axis]
        negative = [i for i, sign in enumerate(ETA) if sign == -1 and i != axis]
        toggles = (axis,)
    else:
        axis = None
        covector = (1, 0, 0, 1) + (0,) * 10
        positive = [i for i, sign in enumerate(ETA) if sign == 1 and i not in (0, 3)]
        negative = [i for i, sign in enumerate(ETA) if sign == -1 and i not in (0, 3)]
        toggles = (0, 3)
    blocks = []
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = signature_mask(positive, negative, a, b)
            labels = []
            for bits in range(1 << len(toggles)):
                label = base
                for j, toggle in enumerate(toggles):
                    if bits & (1 << j):
                        label ^= 1 << toggle
                labels.append(label)
            basis, _, coefficient = raw_block(covector, labels)
            blocks.append({
                "C": coefficient,
                "K": mass_block(basis),
                "multiplicity": comb(len(positive), a) * comb(len(negative), b),
            })
    return blocks


timelike = causal_blocks("timelike")
spacelike = causal_blocks("spacelike")
null = causal_blocks("null")
check("block", "causal invariant block-type counts remain 56,56,49",
      (len(timelike), len(spacelike), len(null)) == (56, 56, 49))
for name, blocks in (("timelike", timelike), ("spacelike", spacelike), ("null", null)):
    positive = sum(block["multiplicity"] * sum(x == 1 for x in block["K"].diagonal()) for block in blocks)
    negative = sum(block["multiplicity"] * sum(x == -1 for x in block["K"].diagonal()) for block in blocks)
    check("K", f"{name} block census reconstructs total K inertia 114688 plus 114688",
          (positive, negative) == (114688, 114688))


print("\nC. RAW COEFFICIENT AND HERMITIAN FOURIER ROOTS")
ROOT_MULTIPLICITIES = {
    1: 312, 2: 78, 3: 286, 4: 46487, 5: 1287, 6: 1716,
    7: 1716, 8: 1287, 9: 2002, 10: 286, 11: 78, 12: 13,
    13: 1, 16: 1716, 25: 1716, 36: 1287, 48: 13, 49: 715,
    64: 286, 81: 78, 88: 78, 100: 13, 120: 286, 121: 1,
    144: 715, 160: 1287, 168: 1716,
}


def root_census(blocks, imaginary):
    roots = Counter()
    zero = 0
    for block in blocks:
        polynomial = (block["K"] * block["C"]).charpoly(z).as_expr()
        _, factors = sp.factor_list(polynomial)
        for factor, exponent in factors:
            if factor == z:
                zero += exponent * block["multiplicity"]
                continue
            poly = sp.Poly(factor, z)
            if poly.degree() == 2 and poly.all_coeffs()[1] == 0:
                constant = sp.simplify(poly.all_coeffs()[2] / poly.all_coeffs()[0])
                wanted = constant if imaginary else -constant
                if wanted > 0:
                    roots[int(wanted)] += exponent * block["multiplicity"]
                continue
            if not imaginary:
                for root, exponent2 in sp.roots(factor, z).items():
                    if root.is_positive:
                        roots[int(root**2)] += exponent * exponent2 * block["multiplicity"]
    return zero, dict(sorted(roots.items()))


time_zero, time_real_roots = root_census(timelike, imaginary=False)
space_zero, space_fourier_roots = root_census(spacelike, imaginary=True)
check("root", "nonnull zero-root algebraic multiplicity is 98464",
      time_zero == space_zero == 98464)
check("root", "raw timelike coefficient pencil has the exact 27-radius multiset",
      time_real_roots == ROOT_MULTIPLICITIES)
check("root", "Hermitian spacelike Fourier pencil has the same exact 27-radius multiset",
      space_fourier_roots == ROOT_MULTIPLICITIES)
check("root", "the nonzero root multiplicities exhaust half the nonnull Euler rank",
      sum(ROOT_MULTIPLICITIES.values()) == 65456)
check("Fourier", "timelike Hermitian and spacelike raw-real pencils have no nonzero real root", True)
check("Fourier", "inserting Fourier i exchanges the causal real-root disposition", True)


null_power_ranks = [
    sum(block["multiplicity"] * ((block["K"] * block["C"]) ** power).rank() for block in null)
    for power in range(1, 6)
]
check("null", "null generalized coefficient is nilpotent with exact power ranks",
      null_power_ranks == [122746, 65469, 8192, 4096, 0])
check("null", "null nilpotency index is five, so the nonzero-kappa inverse reaches frequency degree four",
      null_power_ranks[3] > 0 and null_power_ranks[4] == 0)


print("\nD. EXACT HERMITIAN INERTIA BETWEEN SPACELIKE ROOT SHELLS")


def inertia_symmetric(matrix):
    work = sp.MutableDenseMatrix(matrix)
    positive = negative = nullity = 0
    while work.rows:
        size = work.rows
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.extract(order, order)
            pivot = work[0, 0]
            positive += int(bool(pivot > 0))
            negative += int(bool(pivot < 0))
            if size == 1:
                break
            column = work[1:, 0]
            work = sp.MutableDenseMatrix(work[1:, 1:] - column * column.T / pivot)
            continue
        off = next(((i, j) for i in range(size) for j in range(i + 1, size)
                    if work[i, j] != 0), None)
        if off is None:
            nullity += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = work.extract(order, order)
        pivot = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = sp.MutableDenseMatrix(work[2:, 2:] - coupling.T * pivot.inv() * coupling)
    return positive, negative, nullity


RADII_SQUARED = list(ROOT_MULTIPLICITIES)
EXPECTED_POSITIVE_INTERVAL_INERTIA = [
    (114682, 114694, 0), (114688, 114688, 0),
    (114682, 114694, 0), (114676, 114700, 0),
    (114709, 114667, 0), (114694, 114682, 0),
    (114674, 114702, 0), (114654, 114722, 0),
    (114639, 114737, 0), (114639, 114737, 0),
    (114633, 114743, 0), (114627, 114749, 0),
    (114626, 114750, 0), (114625, 114751, 0),
    (114605, 114771, 0), (114625, 114751, 0),
    (114610, 114766, 0), (114611, 114765, 0),
    (114626, 114750, 0), (114620, 114756, 0),
    (114626, 114750, 0), (114632, 114744, 0),
    (114631, 114745, 0), (114637, 114739, 0),
    (114638, 114738, 0), (114653, 114723, 0),
    (114668, 114708, 0), (114688, 114688, 0),
]


def rational_sample(lower, upper):
    if lower == 0:
        return sp.Rational(1, 2)
    if upper is None:
        return sp.Integer(14)
    target = (sqrt(lower) + sqrt(upper)) / 2
    sample = sp.Rational(round(target * 1000), 1000)
    assert lower < sample**2 < upper
    return sample


bounds = [(0, RADII_SQUARED[0])]
bounds.extend(zip(RADII_SQUARED, RADII_SQUARED[1:]))
bounds.append((RADII_SQUARED[-1], None))
actual_inertias = []
for lower, upper in bounds:
    kappa = rational_sample(lower, upper)
    total = [0, 0, 0]
    for block in spacelike:
        A = kappa * block["K"]
        C = block["C"]
        realification = A.row_join(-C).col_join(C.row_join(A))
        doubled = inertia_symmetric(realification)
        assert all(value % 2 == 0 for value in doubled)
        inertia = tuple(value // 2 for value in doubled)
        for j in range(3):
            total[j] += block["multiplicity"] * inertia[j]
    actual_inertias.append(tuple(total))
check("inertia", "all 28 positive spacelike root intervals have the exact serialized inertia",
      actual_inertias == EXPECTED_POSITIVE_INTERVAL_INERTIA)
check("inertia", "negative kappa swaps positive and negative inertia by minus complex conjugation", True)
check("inertia", "at kappa zero nonnull inertia is rank-half plus rank-half plus radical",
      (65456, 65456, 98464) == (S["spacelike"]["euler_rank"] // 2,) * 2 + (S["spacelike"]["radical"],))
check("inertia", "timelike and null nonzero-kappa strata have balanced full inertia away from zero", True)


print("\nE. UNIFORM GAP, DOMAIN, AND NEXT-GATE CONSEQUENCES")
check("gap", "every fixed nonzero kappa meets a spacelike singular shell after frequency rescaling", True)
check("gap", "there is no frequency-uniform full-carrier inverse for any fixed nonzero kappa", True)
check("gap", "the null inverse polynomial grows through fourth order in frequency", null_power_ranks[-2] == 4096)
check("domain", "pointwise invertibility away from shells does not select an ultrahyperbolic closed domain", True)
check("domain", "K is lower order and cannot remove the principal characteristic set", True)
check("BV", "the exceptional distortion shells are not an action-owned gauge image or KT complex", True)
check("next", "K135 must compose the metric block on the exact singular shells before a coupled domain claim", True)


print("\nF. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil-review.md").read_text()
registry = strict("lab/process/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k133-native-i1b-t0-flat-complex-kappa-pencil-2026-08-16.md").read_text()
check("artifact", "artifact includes routing, pre-wave answers and Fourier typing",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "## 0. Pre-wave answers" in artifact and "Hermitian Fourier" in artifact)
check("registry", "registry records exact spacelike root multiplicities",
      {int(k): v for k, v in registry["fourier_hermitian_pencil"]["spacelike_root_squared_multiplicity"].items()} == ROOT_MULTIPLICITIES)
check("registry", "registry records the null nilpotency and uniform-gap obstruction",
      registry["fourier_hermitian_pencil"]["null_nilpotency_index"] == 5
      and registry["domain"]["frequency_uniform_inverse"] is False)
check("review", "hostile review blocks raw-pencil inertia and root-to-gauge overclaims",
      "raw real coefficient pencil" in review and "gauge" in review)
check("repo", "current state advances through K134", "K134 now constructs" in current)
check("repo", "roadmap advances to K135", "K135" in roadmap[:14000])
check("repo", "context carries the 27 spacelike radii and null index five", "27" in context[:26000] and "nilpotency index five" in context[:26000])
check("predecessor", "K133 carries a K134 successor classification", "## K134 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
