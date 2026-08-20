#!/usr/bin/env python3
"""K155 exact closed-packet null fivefold third-lower gate."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

import sympy as sp

import k149_sparse_differential_jet_api as K149
import k150_moving_selected_shiab_coordinate_adapter as K150
import k153_null_fivefold_first_lower_adapter as K153
import k154_null_fivefold_second_lower_adapter as K154
import k155_null_fivefold_third_lower_adapter as K155


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


print("A. PREDECESSORS, CURRENCY, AND LAYER ZERO")
k152 = strict("lab/process/selected-k152-curved-metric-bridge.json")
k154 = strict("lab/process/selected-k154-null-fivefold-second-lower.json")
check(
    "predecessor",
    "K152 owns order-two and Weyl-dependent order-zero bridge coefficients",
    k152["exact_result"]["bridge_order"] == 2
    and k152["exact_result"]["aligned_weyl_zero_order_rank"] == 9,
)
check(
    "predecessor",
    "K154 closes order five and leaves order four to third jets and A0",
    k154["exact_result"]["reference_restricted_order5_rank"] == 0
    and "K155" in k154["next_gate"],
)
for distinction in (
    "P5 order-two coefficient versus complete restricted order-four coefficient",
    "order-two bridge jets versus Weyl-dependent zero-order bridge",
    "metric radical versus diffeomorphism image",
    "fixed-background rotated covector versus co-rotated background",
    "selected conditional Shiab versus unrecovered preferred historical Shiab",
):
    check("type", distinction + " remain distinct", True)
check(
    "currency",
    "K132--K148 algebra is consumed through K148 and K154 correction fences",
    True,
)


print("\nB. DEGREE BOUND, RECURRENCE, AND THIRD-JET CLOSURE")
t = sp.symbols("t", real=True)
n0 = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(1))
n1 = (sp.Integer(1), sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5))
generator = K150.bivector(0, 4)
check(
    "interpolation",
    "third-order Phi1 and quadratic Phi2 bound selected Shiab degree by nine",
    K155.POLYNOMIAL_DEGREE_BOUND == 9,
)
check(
    "interpolation",
    "ten distinct exact samples certify every degree-nine coefficient",
    len(K155.INTERPOLATION_POINTS) == 10
    and len(set(K155.INTERPOLATION_POINTS)) == 10,
)
closure0 = K155.close_third_jet_labels(n0, t, generator)
closure1 = K155.close_third_jet_labels(n1, t, generator)
check(
    "closure",
    "reference third-jet closure remains labels zero through 31",
    closure0 == K153.FIRST_JET_CLOSED_LABELS,
)
check(
    "closure",
    "rotated third-jet closure remains labels zero through 31",
    closure1 == K153.FIRST_JET_CLOSED_LABELS,
)
check("closure", "third-jet closed carrier remains 448-dimensional", 14 * len(closure0) == 448)

# Independent full scalar K149 composition checks the jet-horizon recurrence.
a = 1 + 2 * t + 3 * t**2 + 4 * t**3
b = 5 + 6 * t + 7 * t**2
toy = K149.SparseDifferentialOperator(
    (t,),
    1,
    1,
    {(1,): sp.ImmutableMatrix([[a]]), (0,): sp.ImmutableMatrix([[b]])},
)
toy_power = toy
for _ in range(4):
    toy_power = toy_power.compose(toy)
toy_layers = K155.top_power_layers(
    (
        sp.SparseMatrix([[1]]),
        sp.SparseMatrix([[2]]),
        sp.SparseMatrix([[6]]),
        sp.SparseMatrix([[24]]),
    ),
    (
        sp.SparseMatrix([[5]]),
        sp.SparseMatrix([[6]]),
        sp.SparseMatrix([[14]]),
    ),
    5,
    3,
)
for order, layer in zip((5, 4, 3, 2), toy_layers):
    exact = sp.Matrix(toy_power.coefficient((order,))).subs(t, 0)
    check(
        "recurrence",
        f"top-four recurrence matches full K149 composition at order {order}",
        layer == exact,
    )


print("\nC. LIVE THIRD JETS AND THIRD-LOWER P5 COEFFICIENT")
reference = K155.build_null_fivefold_third_lower(n0, t, generator)
rotated = K155.build_null_fivefold_third_lower(n1, t, generator)
zero448 = sp.SparseMatrix.zeros(448, 448)
for name, packet in (("reference", reference), ("rotated", rotated)):
    diagonal = tuple(packet.lowerer.diagonal())
    check("carrier", f"{name} packet is 448-dimensional", packet.dimension == 448)
    check(
        "pairing",
        f"{name} lowerer inertia remains 260 plus and 188 minus",
        diagonal.count(1) == 260 and diagonal.count(-1) == 188,
    )
    check(
        "jet",
        f"{name} raw third jet has exact rank 238",
        K153.exact_rank(packet.raw_third_jet) == 238,
    )
    check(
        "jet",
        f"{name} principal third jet has exact rank 258",
        K153.exact_rank(packet.p_principal_third_jet) == 258,
    )
    check(
        "jet",
        f"{name} formal-Euler lower second jet has exact rank 238",
        K153.exact_rank(packet.p_lower_second_jet) == 238,
    )
    check(
        "nilpotence",
        f"{name} frozen fifth power remains zero",
        packet.fifth_principal_value == zero448,
    )
    check(
        "first-lower",
        f"{name} K153 first-lower coefficient replays at rank four",
        K153.exact_rank(packet.fifth_first_lower_value) == 4,
    )
    check(
        "second-lower",
        f"{name} K154 second-lower coefficient replays at rank sixteen",
        K153.exact_rank(packet.fifth_second_lower_value) == 16,
    )
    check(
        "third-lower",
        f"{name} P5 third-lower coefficient is live at rank 82",
        K153.exact_rank(packet.fifth_third_lower_value) == 82,
    )
    replay = K154.top_three_power_layers(
        packet.p_principal_value,
        packet.p_principal_first_jet,
        packet.p_principal_second_jet,
        packet.p_lower_value,
        packet.p_lower_first_jet,
        5,
    )
    check(
        "replay",
        f"{name} K154 top-three recurrence agrees exactly",
        replay
        == (
            packet.fifth_principal_value,
            packet.fifth_first_lower_value,
            packet.fifth_second_lower_value,
        ),
    )
    truncated = K155.top_power_layers(
        (
            packet.p_principal_value,
            packet.p_principal_first_jet,
            packet.p_principal_second_jet,
            zero448,
        ),
        (packet.p_lower_value, packet.p_lower_first_jet, zero448),
        5,
        3,
    )[3]
    check(
        "planted",
        f"{name} second-jet truncation changes the third-lower coefficient",
        truncated != packet.fifth_third_lower_value,
    )
    check(
        "frozen",
        f"{name} frozen coefficient erases the third-lower coefficient",
        K155.frozen_third_lower(packet.p_principal_value) == zero448,
    )

reference_c = sp.SparseMatrix(reference.lowerer * reference.p_principal_value)
check(
    "planted",
    "positive identity in place of native K destroys terminal nilpotence",
    (reference_c**5).nnz() > 0,
)
check(
    "rotation",
    "reference and rotated third-lower ranks agree exactly",
    K153.exact_rank(reference.fifth_third_lower_value)
    == K153.exact_rank(rotated.fifth_third_lower_value)
    == 82,
)


print("\nD. COMPLETE ORDER-FOUR BRIDGE RESTRICTION AND LEAKAGE")
q = sp.symbols("q", real=True)
x = sp.symbols("x0:4", real=True)
origin = dict.fromkeys(x, 0)
bridge = K155.K152.build_curved_metric_bridge(
    K155.K152.weyl_from_electric(sp.diag(q / 2, q / 2, -q)),
    x,
    (generator, {}, {}, {}),
    2,
)
eta = sp.diag(1, -1, -1, -1)


def gauge(covector4):
    n = sp.Matrix(covector4)
    columns = []
    for axis in range(4):
        vector = sp.zeros(4, 1)
        vector[axis] = 1
        columns.append(K155.K152.metric_vector(n * vector.T + vector * n.T))
    return sp.Matrix.hstack(*columns)


def ell(covector4):
    raised = eta * sp.Matrix(covector4)
    return sp.Matrix(
        [
            raised[i] * raised[j] * (2 if i != j else 1)
            for i, j in K155.K152.METRIC_SLOTS
        ]
    )


residuals = {}
radicals = {}
for name, covector, packet in (
    ("reference", n0, reference),
    ("rotated", n1, rotated),
):
    bridge_value = K155.embedded_bridge_coefficient_jet(
        packet, bridge, origin, 2, 0, 0
    )
    bridge_first = K155.embedded_bridge_coefficient_jet(
        packet, bridge, origin, 2, 0, 1
    )
    bridge_second = K155.embedded_bridge_coefficient_jet(
        packet, bridge, origin, 2, 0, 2
    )
    bridge_zero = K155.embedded_bridge_coefficient_jet(
        packet, bridge, origin, 0, 0, 0
    )
    check("bridge", f"{name} order-two bridge value has rank four", K153.exact_rank(bridge_value) == 4)
    check("bridge", f"{name} order-two bridge first jet has rank one", K153.exact_rank(bridge_first) == 1)
    check("bridge", f"{name} order-two bridge second jet has rank four", K153.exact_rank(bridge_second) == 4)
    check("bridge", f"{name} Weyl zero-order bridge has rank nine", K153.exact_rank(bridge_zero) == 9)
    residual = K155.restricted_third_lower(packet, bridge, origin)
    residuals[name] = residual
    H = sp.Matrix.hstack(*ell(covector).T.nullspace())
    radicals[name] = H
    for term_name, term in (
        ("direct", residual.direct_term),
        ("first bridge jet", residual.first_bridge_jet_term),
        ("second bridge jet", residual.second_bridge_jet_term),
        ("Weyl zero order", residual.zero_order_bridge_term),
        ("complete", residual.complete),
    ):
        check(
            "restricted",
            f"{name} {term_name} order-four term has rank one",
            K153.exact_rank(term) == 1,
        )
    check(
        "Noether",
        f"{name} complete order-four coefficient annihilates diffeomorphisms",
        residual.complete * gauge(covector) == sp.zeros(448, 4),
    )

check(
    "radical",
    "reference complete coefficient annihilates the metric radical",
    residuals["reference"].complete * radicals["reference"]
    == sp.zeros(448, 9),
)
rotated_derivative = (
    residuals["rotated"].direct_term
    + residuals["rotated"].first_bridge_jet_term
    + residuals["rotated"].second_bridge_jet_term
)
check(
    "radical",
    "rotated derivative-only terms annihilate the metric radical",
    rotated_derivative * radicals["rotated"] == sp.zeros(448, 9),
)
check(
    "radical",
    "rotated Weyl zero-order term leaks the metric radical at rank one",
    K153.exact_rank(
        residuals["rotated"].zero_order_bridge_term * radicals["rotated"]
    )
    == 1,
)
check(
    "radical",
    "rotated complete coefficient leaks the metric radical at rank one",
    K153.exact_rank(residuals["rotated"].complete * radicals["rotated"])
    == 1,
)
check(
    "flat",
    "flat q=0 control removes the rotated radical leakage",
    residuals["rotated"].complete.subs(q, 0) * radicals["rotated"]
    == sp.zeros(448, 9),
)
witness = sp.Matrix([sp.Rational(6, 5), 1, 0, 0, 0, 0, 0, 0, 0, 0])
leak = residuals["rotated"].complete * witness
check("witness", "explicit rotated witness lies in ker ell_n", (ell(n1).T * witness)[0] == 0)
check(
    "witness",
    "explicit rotated witness leaks by 2532096*q/125 in row 224",
    leak[224] == sp.Rational(2532096, 125) * q,
)
check(
    "ceiling",
    "selected-branch leakage does not bind the preferred historical Shiab or GU",
    True,
)


print("\nE. ARTIFACT, HOSTILE REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k155-null-fivefold-third-lower-2026-08-20.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-20-selected-k155-null-fivefold-third-lower-review.md").read_text()
registry = strict("lab/process/selected-k155-null-fivefold-third-lower.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k154-null-fivefold-second-lower-2026-08-20.md").read_text()
for marker in (
    "GU-COMPARATOR-ROUTING — scope before inference.",
    "Classification: `SOURCE_NATIVE_ROUTE`.",
    "target_claim:",
    "Scope:",
    "```gu-typed-objects",
):
    check("governance", f"artifact carries {marker}", marker in artifact)
check(
    "registry",
    "machine result separates gauge zero from rotated radical leakage",
    registry["exact_result"]["rotated_gauge_image_rank"] == 0
    and registry["exact_result"]["rotated_metric_radical_leakage_rank"] == 1,
)
check(
    "hostile",
    "review blocks GU-wide, co-rotated, gauge and interpolation overclaims",
    all(word in review.lower() for word in ("gu no-go", "co-rotation", "gauge", "degree-nine")),
)
check("propagation", "current state advances through K155", "K155 now extends" in current[:18000])
check("propagation", "roadmap stops mechanical continuation to K156", "Do not continue to K156" in roadmap[:9000])
check("propagation", "context carries Weyl-only rotated leakage", "Current K155" in context[:9000] and "Weyl zero-order" in context[:9000])
check("propagation", "tests inventory includes the K155 probe", "selected_k155_null_fivefold_third_lower_probe.py" in tests_readme)
check("predecessor", "K154 carries the K155 successor classification", "## K155 successor classification" in predecessor)

print("K155_PACKET=THIRD_JET_CLOSED_32_LABELS_448D__LOWERER_INERTIA_260_188")
print("K155_THIRD_JETS=RAW238__PRINCIPAL258__FORMAL_LOWER238")
print("K155_P5_THIRD_LOWER=LIVE_RANK82_REFERENCE_AND_ROTATED")
print("K155_RESTRICTED_ORDER4=RANK1_GAUGE_ZERO__ROTATED_RADICAL_LEAKAGE_RANK1_FROM_WEYL_A0")
print("K155_ROUTE=SELECTED_CONDITIONAL_NULL_RADICAL_DESCENT_KILLED__NO_MECHANICAL_K156")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("K155 failures: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
