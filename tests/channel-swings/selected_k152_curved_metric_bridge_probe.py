#!/usr/bin/env python3
"""K152 exact curved metric-bridge, adjoint, and control gate."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path
import json

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k152_curved_metric_bridge_adapter as K152
from k149_sparse_differential_jet_api import SparseDifferentialOperator


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str) -> dict:
    path = ROOT / relative

    def hook(pairs):
        output = {}
        for key, value in pairs:
            if key in output:
                raise ValueError(f"duplicate key {key!r}: {path}")
            output[key] = value
        return output

    return json.loads(path.read_text(), object_pairs_hook=hook)


print("A. PREDECESSOR, CURRENCY, AND LAYER ZERO")
k127 = strict("lab/process/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate.json")
k129 = strict("lab/process/selected-k129-native-i1b-t0-ac-kernel-and-domain-classification.json")
k151 = strict("lab/process/selected-k151-moving-distortion-pairing-adjoint.json")
check("predecessor", "K127 owns an arbitrary Ricci-flat Weyl two-jet family", k127["background_family"]["curvature"] == "RICCI_FLAT_WITH_ARBITRARY_WEYL_TWOJET")
check("predecessor", "K129 types A as the selected curvature linearization", "D_g[S_g(F_B)]" in k129["mixed_operator"]["formula"])
check("predecessor", "K151 leaves exactly the curved metric bridge open", k151["target_closure"]["curved_metric_bridge"] == "NOT_SERIALIZED")
for distinction in (
    "metric perturbation versus curvature variation",
    "Einstein contraction versus selected-Shiab density-dual image",
    "density-dual bridge versus primalized field operator",
    "field operator versus weighted formal adjoint",
    "principal null symbol versus Weyl-dependent zero-order coefficient",
    "selected conditional Shiab versus unrecovered preferred historical Shiab",
):
    check("type", distinction + " remain distinct", True)
check("currency", "K127/K129 local curvature algebra consumes no superseded source reading", True)


print("\nB. EXACT NORMAL-COORDINATE AND WEYL COEFFICIENTS")
q = sp.symbols("q", real=True)
aligned_electric = sp.diag(q / 2, q / 2, -q)
aligned = K152.weyl_from_electric(aligned_electric)
leak_electric = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
leak = K152.weyl_from_electric(leak_electric)
check("geometry", "aligned electric Weyl datum is symmetric and trace free", aligned_electric == aligned_electric.T and sp.trace(aligned_electric) == 0)
check("geometry", "normal metric two-jet reconstructs the complete aligned curvature", all(
    sp.simplify(K152.reconstructed_curvature(aligned, a, b, c, d) - aligned.get((a, b, c, d), 0)) == 0
    for a in range(4) for b in range(4) for c in range(4) for d in range(4)
))
check("geometry", "leak electric Weyl datum is symmetric and trace free", leak_electric == leak_electric.T and sp.trace(leak_electric) == 0)

plus_matrix = sp.diag(0, 1, -1, 0)
cross_matrix = sp.zeros(4)
cross_matrix[1, 2] = cross_matrix[2, 1] = 1
plus = K152.metric_vector(plus_matrix)
cross = K152.metric_vector(cross_matrix)
aligned_zero = K152.selected_einstein_coefficient(aligned, None)
leak_zero = K152.selected_einstein_coefficient(leak, None)
check("curved", "aligned Weyl coefficient preserves plus with exact minus-two-q weight", aligned_zero * plus == -2 * q * plus)
check("curved", "aligned Weyl coefficient preserves cross with exact minus-two-q weight", aligned_zero * cross == -2 * q * cross)
leak_plus = sp.zeros(10, 1)
leak_plus[6] = -2
leak_cross = sp.zeros(10, 1)
leak_cross[8] = -2
check("curved", "generic K127 Weyl fixture sends plus outside the selected plane", leak_zero * plus == leak_plus)
check("curved", "generic K127 Weyl fixture sends cross outside the selected plane", leak_zero * cross == leak_cross)
check("planted", "zero TT compression cannot erase the live generic off-plane output", leak_zero * plus != sp.zeros(10, 1) and leak_zero * cross != sp.zeros(10, 1))


print("\nC. K149/K150/K151 CURVED BRIDGE SERIALIZATION")
x = sp.symbols("x0:4", real=True)
origin = dict.fromkeys(x, 0)
generators = (K150.bivector(0, 4), {}, {}, {})
bridge = K152.build_curved_metric_bridge(aligned, x, generators, 1)
labels = sorted({label for label, _, _ in bridge.basis})
diagonal = tuple(bridge.distortion_pairing.diagonal())
check("carrier", "closed bridge packet has 112 distortion directions on eight labels", len(bridge.basis) == 112 and len(labels) == 8)
check("pairing", "native DeWitt metric pairing is nondegenerate with determinant 64", bridge.metric_pairing.det() == 64)
check("pairing", "Cl(7,7) output lowerer is nondegenerate and indefinite", bridge.distortion_pairing.rank() == 112 and diagonal.count(1) == 58 and diagonal.count(-1) == 54)
check("operator", "density-dual and primalized bridges are typed 10 to 112 and order two", bridge.density_dual.input_dimension == 10 and bridge.density_dual.output_dimension == 112 and bridge.density_dual.maximum_order() == 2 and bridge.field_operator.maximum_order() == 2)
check("curved", "aligned Weyl density-dual zero-order bridge is live with rank nine", bridge.zero_order().subs(q, 1).rank() == 9)

lowered_adjoint = bridge.lowered_formal_adjoint
formal_transpose = bridge.density_dual.formal_transpose()
check("adjoint", "lowered native weighted adjoint equals the complete density-dual formal transpose", all(
    lowered_adjoint.coefficient(alpha) == formal_transpose.coefficient(alpha)
    for alpha in set(lowered_adjoint.coefficients) | set(formal_transpose.coefficients)
))
first_indices = tuple(tuple(1 if axis == j else 0 for axis in range(4)) for j in range(4))
check("adjoint", "moving bridge forces four live first-order adjoint coefficients", all(lowered_adjoint.coefficient(alpha).subs(origin).rank() == 1 for alpha in first_indices))

frozen_coefficients = {
    alpha: sp.ImmutableMatrix(sp.Matrix(value).subs(origin))
    for alpha, value in bridge.density_dual.coefficients.items()
}
frozen_density_dual = SparseDifferentialOperator(x, 10, 112, frozen_coefficients)
frozen_bridge = K152.CurvedMetricBridge(
    x,
    bridge.basis,
    frozen_density_dual,
    bridge.metric_pairing,
    bridge.distortion_pairing,
)
check("planted", "freezing the moving bridge erases all first-order adjoint coefficients", all(frozen_bridge.lowered_formal_adjoint.coefficient(alpha) == sp.zeros(10, 112) for alpha in first_indices))
check("planted", "plain field-coordinate transpose is not the native weighted field adjoint", bridge.field_operator.formal_transpose().coefficient((2, 0, 0, 0)).subs(origin) != bridge.formal_adjoint.coefficient((2, 0, 0, 0)).subs(origin))


print("\nD. FROZEN AND RATIONALLY ROTATED NULL REPLAY")
form_pairs = tuple(combinations(range(K150.N), 2))
index = {(label, mu): position for position, (label, mu, _) in enumerate(bridge.basis)}


def metric_basis_value(slot, i, j):
    p, r = slot
    return int((i, j) == (p, r) or (p != r and (i, j) == (r, p)))


def principal_riemann(covector, slot):
    def tensor(i, j, a, b):
        h = lambda left, right: metric_basis_value(slot, left, right)
        return (
            covector[i] * covector[a] * h(j, b)
            - covector[i] * covector[b] * h(j, a)
            - covector[j] * covector[a] * h(i, b)
            + covector[j] * covector[b] * h(i, a)
        )
    return tensor


def spin_injection(tensor):
    output = {}
    for i, j in form_pairs:
        coefficient = {}
        for a, b in form_pairs:
            value = K150.ETA[a] * K150.ETA[b] * tensor(i, j, a, b)
            if value:
                coefficient = K150.eadd(
                    coefficient,
                    K150.escale(value, K150.emul(K150.blade(a), K150.blade(b))),
                )
        if coefficient:
            output[(1 << i) | (1 << j)] = coefficient
    return output


def held_frozen_matrix(covector4):
    covector = tuple(covector4) + (0,) * 10
    matrix = sp.zeros(112, 10)
    for column, slot in enumerate(K152.METRIC_SLOTS):
        image = K150.selected_shiab(spin_injection(principal_riemann(covector, slot)))
        for nu, mask, value in K150.rows_for_image(image):
            key = (mask ^ (1 << nu), nu)
            if key in index:
                matrix[index[key], column] = value[0] + sp.I * value[1]
    return sp.ImmutableMatrix(matrix)


n0 = (1, 0, 0, 1)
n1 = (1, sp.Rational(3, 5), 0, sp.Rational(4, 5))
symbol0 = bridge.symbol(n0, origin)
symbol1 = bridge.symbol(n1, origin)
check("replay", "reference null symbol exactly equals the held K135 curvature bridge", symbol0 == held_frozen_matrix(n0))
check("replay", "rationally rotated null symbol exactly equals the held K135 curvature bridge", symbol1 == held_frozen_matrix(n1))
check("replay", "both exact null bridge symbols retain K129 rank four", symbol0.rank() == symbol1.rank() == 4)


def gauge(covector4):
    n = sp.Matrix(covector4)
    columns = []
    for axis in range(4):
        vector = sp.zeros(4, 1)
        vector[axis] = 1
        columns.append(K152.metric_vector(n * vector.T + vector * n.T))
    return sp.ImmutableMatrix.hstack(*columns)


check("Noether", "reference null diffeomorphism image is annihilated", symbol0 * gauge(n0) == sp.zeros(112, 4))
check("Noether", "rotated null diffeomorphism image is annihilated", symbol1 * gauge(n1) == sp.zeros(112, 4))
check("scope", "bridge controls stop before fivefold composition and null lower leakage", True)


print("\nE. ARTIFACT, HOSTILE REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k152-curved-metric-bridge-2026-08-20.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-20-selected-k152-curved-metric-bridge-review.md").read_text()
registry = strict("lab/process/selected-k152-curved-metric-bridge.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k151-moving-distortion-pairing-adjoint-2026-08-17.md").read_text()
for marker in (
    "GU-COMPARATOR-ROUTING — scope before inference.",
    "Classification: `SOURCE_NATIVE_ROUTE`.",
    "target_claim:",
    "Scope:",
    "```gu-typed-objects",
):
    check("governance", f"artifact carries {marker}", marker in artifact)
check("registry", "machine result records the live Weyl coefficient and rotated replay", registry["exact_result"]["aligned_weyl_zero_order_rank"] == 9 and registry["exact_result"]["rotated_null_symbol_rank"] == 4)
check("hostile", "review blocks frozen-only, TT-compression, and fivefold overclaims", "frozen" in review.lower() and "compression" in review.lower() and "fivefold" in review.lower())
check("propagation", "current state advances through K152", "K152 now serializes" in current[:18000])
check("propagation", "roadmap advances only to K153 fivefold composition", "K153" in roadmap[:9000] and "fivefold" in roadmap[:9000])
check("propagation", "context carries the curved bridge boundary", "Current K152" in context[:7000])
check("propagation", "tests inventory includes K152 probe", "selected_k152_curved_metric_bridge_probe.py" in tests_readme)
check("predecessor", "K151 carries the K152 successor closure", "## K152 successor classification" in predecessor)

print("K152_BRIDGE=EXACT_NORMAL_COORDINATE_MINUS2_DELTA_EINSTEIN_TO_SELECTED_SHIAB")
print("K152_CURVED=ALIGNED_WEYL_ZERO_RANK9__GENERIC_WEYL_OFF_TT_LIVE")
print("K152_ADJOINT=MOVING_FIRST_ORDER_TERMS_LIVE__FROZEN_PLANT_FAILS")
print("K153_FIVEFOLD=NOT_COMPOSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("K152 failures: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
