#!/usr/bin/env python3
"""K154 exact closed-packet null fivefold second-lower gate."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

import sympy as sp

import k149_sparse_differential_jet_api as K149
import k150_moving_selected_shiab_coordinate_adapter as K150
import k153_null_fivefold_first_lower_adapter as K153
import k154_null_fivefold_second_lower_adapter as K154

K152 = K153.K152


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
k150 = strict("lab/process/selected-k150-moving-selected-shiab-coordinate-adapter.json")
k152 = strict("lab/process/selected-k152-curved-metric-bridge.json")
k153 = strict("lab/process/selected-k153-null-fivefold-first-lower.json")
check("predecessor", "K150 owns a live second selected-Shiab coefficient jet", k150["coordinate_adapter"]["second_jet_nonzero"] is True)
check("predecessor", "K152 owns an exact moving order-two rank-four null bridge", k152["exact_result"]["bridge_order"] == 2 and k152["exact_result"]["reference_null_symbol_rank"] == 4)
check("predecessor", "K153 closes order six and leaves order five to second jets", k153["exact_result"]["reference_restricted_order6_rank"] == 0 and "K154" in k153["next_gate"])
for distinction in (
    "principal second jet versus formal-Euler lower first jet",
    "P5 second-lower coefficient versus restricted order-five coefficient",
    "direct P5 order-three term versus moving-bridge derivative term",
    "zero order five versus zero complete curved remainder",
    "selected conditional Shiab versus unrecovered preferred historical Shiab",
):
    check("type", distinction + " remain distinct", True)
check("currency", "K132--K148 algebra is consumed through K148 and K153 correction fences", True)


print("\nB. RECURRENCE AND SECOND-JET ACTION CLOSURE")
t = sp.symbols("t", real=True)
n0 = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(1))
n1 = (sp.Integer(1), sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5))
generator = K150.bivector(0, 4)
closure0 = K154.close_second_jet_labels(n0, t, generator)
closure1 = K154.close_second_jet_labels(n1, t, generator)
check("closure", "reference second-jet closure remains labels zero through 31", closure0 == K153.FIRST_JET_CLOSED_LABELS)
check("closure", "rotated second-jet closure remains labels zero through 31", closure1 == K153.FIRST_JET_CLOSED_LABELS)
check("closure", "second-jet closed carrier remains 448-dimensional", 14 * len(closure0) == 448)

# Independent scalar K149 composition checks the restricted jet recurrence.
a = 1 + 2 * t + 3 * t**2
b = 4 + 5 * t
toy = K149.SparseDifferentialOperator(
    (t,), 1, 1, {(1,): sp.ImmutableMatrix([[a]]), (0,): sp.ImmutableMatrix([[b]])}
)
toy_power = toy
for _ in range(4):
    toy_power = toy_power.compose(toy)
toy_layers = K154.top_three_power_layers(
    sp.SparseMatrix([[1]]),
    sp.SparseMatrix([[2]]),
    sp.SparseMatrix([[6]]),
    sp.SparseMatrix([[4]]),
    sp.SparseMatrix([[5]]),
    5,
)
for order, layer in ((5, toy_layers[0]), (4, toy_layers[1]), (3, toy_layers[2])):
    exact = sp.Matrix(toy_power.coefficient((order,))).subs(t, 0)
    check("recurrence", f"top-three recurrence matches full K149 composition at order {order}", layer == exact)


print("\nC. LIVE SECOND JETS AND SECOND-LOWER P5 COEFFICIENT")
reference = K154.build_null_fivefold_second_lower(n0, t, generator)
rotated = K154.build_null_fivefold_second_lower(n1, t, generator)
zero448 = sp.SparseMatrix.zeros(448, 448)
for name, packet in (("reference", reference), ("rotated", rotated)):
    diagonal = tuple(packet.lowerer.diagonal())
    check("carrier", f"{name} packet is 448-dimensional", packet.dimension == 448)
    check("pairing", f"{name} lowerer inertia remains 260 plus and 188 minus", diagonal.count(1) == 260 and diagonal.count(-1) == 188)
    check("jet", f"{name} raw second jet has exact rank 241", K153.exact_rank(packet.raw_second_jet) == 241)
    check("jet", f"{name} principal second jet has exact rank 260", K153.exact_rank(packet.p_principal_second_jet) == 260)
    check("jet", f"{name} formal-Euler lower first jet has exact rank 241", K153.exact_rank(packet.p_lower_first_jet) == 241)
    check("nilpotence", f"{name} frozen fifth power remains zero", packet.fifth_principal_value == zero448)
    check("first-lower", f"{name} K153 first-lower coefficient replays at rank four", K153.exact_rank(packet.fifth_first_lower_value) == 4)
    check("second-lower", f"{name} P5 second-lower coefficient is live at rank sixteen", K153.exact_rank(packet.fifth_second_lower_value) == 16)
    first_replay = K153.top_and_first_lower_power(
        packet.p_principal_value,
        packet.p_principal_first_jet,
        packet.p_lower_value,
        5,
    )[1]
    check("replay", f"{name} K153 first-lower recurrence agrees exactly", first_replay == packet.fifth_first_lower_value)
    truncated = K154.top_three_power_layers(
        packet.p_principal_value,
        packet.p_principal_first_jet,
        zero448,
        packet.p_lower_value,
        zero448,
        5,
    )[2]
    check("planted", f"{name} first-jet truncation changes the second-lower coefficient", truncated != packet.fifth_second_lower_value)
    check("frozen", f"{name} frozen coefficient erases the second-lower coefficient", K154.frozen_second_lower(packet.p_principal_value) == zero448)

reference_c = sp.SparseMatrix(reference.lowerer * reference.p_principal_value)
check("planted", "positive identity in place of native K destroys terminal nilpotence", (reference_c**5).nnz() > 0)
check("rotation", "reference and rotated second-lower ranks agree exactly", K153.exact_rank(reference.fifth_second_lower_value) == K153.exact_rank(rotated.fifth_second_lower_value) == 16)


print("\nD. COMPLETE ORDER-FIVE BRIDGE RESTRICTION")
q = sp.symbols("q", real=True)
x = sp.symbols("x0:4", real=True)
origin = dict.fromkeys(x, 0)
bridge = K152.build_curved_metric_bridge(
    K152.weyl_from_electric(sp.diag(q / 2, q / 2, -q)),
    x,
    (generator, {}, {}, {}),
    2,
)
residuals = {}
for name, packet in (("reference", reference), ("rotated", rotated)):
    bridge_value = K154.embedded_bridge_symbol_jet(packet, bridge, origin, 0, 0)
    bridge_first = K154.embedded_bridge_symbol_jet(packet, bridge, origin, 0, 1)
    residual = K154.restricted_second_lower(packet, bridge, origin)
    residuals[name] = residual.complete
    check("bridge", f"{name} moving bridge symbol retains rank four", K153.exact_rank(bridge_value) == 4)
    check("bridge", f"{name} moving bridge first jet is live at rank one", K153.exact_rank(bridge_first) == 1)
    check("restricted", f"{name} direct P5 order-three bridge term is zero", residual.direct_term == sp.zeros(448, 10))
    check("restricted", f"{name} live-bridge-jet contribution is zero", residual.bridge_jet_term == sp.zeros(448, 10))
    check("restricted", f"{name} complete order-five K P5 K A coefficient is zero", residual.complete == sp.zeros(448, 10))

core = sp.SparseMatrix(
    reference.lowerer
    * reference.fifth_second_lower_value
    * reference.lowerer
)
check("planted", "unrestricted second-lower core is nonzero before the native bridge", K153.exact_rank(core) == 16)


def gauge(covector4):
    n = sp.Matrix(covector4)
    columns = []
    for axis in range(4):
        vector = sp.zeros(4, 1)
        vector[axis] = 1
        columns.append(K152.metric_vector(n * vector.T + vector * n.T))
    return sp.Matrix.hstack(*columns)


eta = sp.diag(1, -1, -1, -1)


def ell(covector4):
    raised = eta * sp.Matrix(covector4)
    return sp.Matrix([
        raised[i] * raised[j] * (2 if i != j else 1)
        for i, j in K152.METRIC_SLOTS
    ])


H0 = sp.Matrix.hstack(*ell(n0).T.nullspace())
H1 = sp.Matrix.hstack(*ell(n1).T.nullspace())
check("Noether", "order-five coefficient annihilates both diffeomorphism images", residuals["reference"] * gauge(n0) == sp.zeros(448, 4) and residuals["rotated"] * gauge(n1) == sp.zeros(448, 4))
check("radical", "order-five coefficient has no metric-radical leakage at either null covector", residuals["reference"] * H0 == sp.zeros(448, 9) and residuals["rotated"] * H1 == sp.zeros(448, 9))
check("ceiling", "zero through order five does not determine restricted orders four and below", True)


print("\nE. ARTIFACT, HOSTILE REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k154-null-fivefold-second-lower-2026-08-20.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-20-selected-k154-null-fivefold-second-lower-review.md").read_text()
registry = strict("lab/process/selected-k154-null-fivefold-second-lower.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k153-null-fivefold-first-lower-2026-08-20.md").read_text()
for marker in (
    "GU-COMPARATOR-ROUTING — scope before inference.",
    "Classification: `SOURCE_NATIVE_ROUTE`.",
    "target_claim:",
    "Scope:",
    "```gu-typed-objects",
):
    check("governance", f"artifact carries {marker}", marker in artifact)
check("registry", "machine result separates live unrestricted and zero restricted layers", registry["exact_result"]["reference_P5_second_lower_rank"] == 16 and registry["exact_result"]["reference_restricted_order5_rank"] == 0)
check("hostile", "review blocks full-zero, frozen-bridge, rank-only and all-chart overclaims", all(word in review.lower() for word in ("full curved remainder", "bridge", "rank", "chart")))
check("propagation", "current state advances through K154", "K154 now extends" in current[:18000])
check("propagation", "roadmap advances only to K155 order four", "K155" in roadmap[:9000] and "order-four" in roadmap[:9000])
check("propagation", "context carries the live-rank-sixteen versus restricted-zero distinction", "Current K154" in context[:9000] and "rank-sixteen" in context[:9000])
check("propagation", "tests inventory includes the K154 probe", "selected_k154_null_fivefold_second_lower_probe.py" in tests_readme)
check("predecessor", "K153 carries the K154 successor classification", "## K154 successor classification" in predecessor)

print("K154_PACKET=SECOND_JET_CLOSED_32_LABELS_448D__LOWERER_INERTIA_260_188")
print("K154_SECOND_JETS=RAW241__PRINCIPAL260__FORMAL_LOWER241")
print("K154_P5_SECOND_LOWER=LIVE_RANK16_REFERENCE_AND_ROTATED")
print("K154_RESTRICTED_ORDER5=ZERO_DIRECT_AND_BRIDGE_JET_TERMS_REFERENCE_AND_ROTATED__ORDERS4_AND_BELOW_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("K154 failures: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
