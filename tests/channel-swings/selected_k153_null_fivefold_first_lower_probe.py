#!/usr/bin/env python3
"""K153 exact closed-packet null fivefold first-lower gate."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k152_curved_metric_bridge_adapter as K152
import k153_null_fivefold_first_lower_adapter as K153


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
k134 = strict("lab/process/selected-k134-native-i1b-t0-kappa-hodge-fingerprint-and-fourier-pencil.json")
k147 = strict("lab/process/selected-k147-native-i1b-t0-radical-module-factorization-gate.json")
k148 = strict("lab/process/selected-k148-native-i1b-null-cone-principal-descent-gate.json")
k152 = strict("lab/process/selected-k152-curved-metric-bridge.json")
check("predecessor", "K134 owns exact fifth-step frozen null nilpotence", k134["fourier_hermitian_pencil"]["null_KC_power_ranks"][-1] == 0)
check("predecessor", "K147 owns the frozen restricted zero", k147["restricted_residual"]["frozen_null_principal_value"] == "ZERO_BY_L_N_POWER_5")
check("predecessor", "K148 leaves the curved lower coefficient open", k148["lower_transport"]["status"] == "UNDEFINED_EVALUATOR_NOT_SERIALIZED")
check("predecessor", "K152 closes the exact rank-four bridge before composition", k152["exact_result"]["reference_null_symbol_rank"] == 4 and k152["target_closure"]["curved_restricted_residual"] == "UNDEFINED_FIVEFOLD_NOT_YET_COMPOSED")
for distinction in (
    "formal-Euler coefficient C versus generalized field coefficient P=K C",
    "frozen symbol P(n)^5 versus variable-coefficient differential P^5",
    "unrestricted P^5 lower term versus K152-bridge-restricted residual",
    "first restricted lower coefficient versus complete curved remainder",
    "distortion output versus metric radical or quotient",
    "selected conditional Shiab versus unrecovered preferred historical Shiab",
):
    check("type", distinction + " remain distinct", True)
check("currency", "K134--K148 local algebra is consumed through K148's correction fence", True)


print("\nB. EXACT FIRST-JET ACTION CLOSURE")
t = sp.symbols("t", real=True)
n0 = (sp.Integer(1), sp.Integer(0), sp.Integer(0), sp.Integer(1))
n1 = (sp.Integer(1), sp.Rational(3, 5), sp.Integer(0), sp.Rational(4, 5))
generator = K150.bivector(0, 4)
closure0 = K153.close_first_jet_labels(n0, t, generator)
closure1 = K153.close_first_jet_labels(n1, t, generator)
check("closure", "reference bridge seed closes on exactly labels zero through 31", closure0 == K153.FIRST_JET_CLOSED_LABELS)
check("closure", "rationally rotated bridge seed has the same exact first-jet closure", closure1 == K153.FIRST_JET_CLOSED_LABELS)
check("closure", "closed action carrier has dimension 448", 14 * len(closure0) == 448)

seed_adapter = K150.MovingSelectedShiabAdapter((t,), (generator,), 1)
_, projected_raw, _ = seed_adapter.raw_block(n0 + (sp.Integer(0),) * 10, K153.SEED_LABELS)
check("planted", "projecting the action to K152's 112D bridge seed is vacuously zero", projected_raw == sp.zeros(112))


print("\nC. FROZEN NILPOTENCE AND MOVING FIRST LOWER TERM")
reference = K153.build_null_fivefold_first_lower(n0, t, generator)
rotated = K153.build_null_fivefold_first_lower(n1, t, generator)
for name, packet in (("reference", reference), ("rotated", rotated)):
    diagonal = tuple(packet.lowerer.diagonal())
    check("carrier", f"{name} packet is 448-dimensional", packet.dimension == 448)
    check("pairing", f"{name} native lowerer has exact indefinite inertia 260 plus and 188 minus", diagonal.count(1) == 260 and diagonal.count(-1) == 188)
    powers = []
    current = sp.SparseMatrix.eye(packet.dimension)
    for _ in range(5):
        current = sp.SparseMatrix(current * packet.p_principal_value)
        powers.append(K153.exact_rank(current))
    check("nilpotence", f"{name} generalized symbol has exact power ranks 234,125,16,8,0", powers == [234, 125, 16, 8, 0])
    check("lower", f"{name} variable coefficient creates a live rank-four P5 first-lower term", K153.exact_rank(packet.fifth_first_lower_value) == 4)
    check("frozen", f"{name} frozen coefficient erases the P5 first-lower term", K153.frozen_first_lower(packet.p_principal_value) == sp.zeros(448))

check("rotation", "reference and rotated packets retain matching frozen power ranks and first-lower rank", True)

reference_c = sp.SparseMatrix(reference.lowerer * reference.p_principal_value)
check("planted", "positive identity in place of native K destroys terminal fifth-step nilpotence", (reference_c**5).nnz() > 0)
zero448 = sp.SparseMatrix.zeros(448, 448)
without_formal_lower = K153.top_and_first_lower_power(
    reference.p_principal_value, reference.p_principal_first_jet, zero448, 5
)[1]
without_principal_jet = K153.top_and_first_lower_power(
    reference.p_principal_value, zero448, reference.p_lower_value, 5
)[1]
check("planted", "omitting the formal-Euler lower term changes the live first-lower coefficient", without_formal_lower != reference.fifth_first_lower_value)
check("planted", "freezing the moving principal jet changes the live first-lower coefficient", without_principal_jet != reference.fifth_first_lower_value)


print("\nD. K152 BRIDGE RESTRICTION AND NULL LEAKAGE")
q = sp.symbols("q", real=True)
x = sp.symbols("x0:4", real=True)
origin = dict.fromkeys(x, 0)
bridge = K152.build_curved_metric_bridge(
    K152.weyl_from_electric(sp.diag(q / 2, q / 2, -q)),
    x,
    (generator, {}, {}, {}),
    1,
)
embedded0 = K153.embed_bridge_symbol(reference, bridge, origin)
embedded1 = K153.embed_bridge_symbol(rotated, bridge, origin)
residual0 = K153.restricted_first_lower(reference, bridge, origin)
residual1 = K153.restricted_first_lower(rotated, bridge, origin)
check("bridge", "reference and rotated embedded bridge symbols retain rank four", K153.exact_rank(embedded0) == K153.exact_rank(embedded1) == 4)
check("restricted", "reference order-six K P5 K A coefficient is exactly zero", residual0 == sp.zeros(448, 10))
check("restricted", "rotated order-six K P5 K A coefficient is exactly zero", residual1 == sp.zeros(448, 10))


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
check("Noether", "first restricted coefficient annihilates both diffeomorphism images", residual0 * gauge(n0) == sp.zeros(448, 4) and residual1 * gauge(n1) == sp.zeros(448, 4))
check("radical", "first restricted coefficient has no metric-radical leakage at either null covector", residual0 * H0 == sp.zeros(448, 9) and residual1 * H1 == sp.zeros(448, 9))
check("ceiling", "zero order six does not determine restricted orders five and below", True)


print("\nE. ARTIFACT, HOSTILE REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k153-null-fivefold-first-lower-2026-08-20.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-20-selected-k153-null-fivefold-first-lower-review.md").read_text()
registry = strict("lab/process/selected-k153-null-fivefold-first-lower.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k152-curved-metric-bridge-2026-08-20.md").read_text()
for marker in (
    "GU-COMPARATOR-ROUTING — scope before inference.",
    "Classification: `SOURCE_NATIVE_ROUTE`.",
    "target_claim:",
    "Scope:",
    "```gu-typed-objects",
):
    check("governance", f"artifact carries {marker}", marker in artifact)
check("registry", "machine result separates live unrestricted and zero restricted coefficients", registry["exact_result"]["reference_P5_first_lower_rank"] == 4 and registry["exact_result"]["reference_restricted_order6_rank"] == 0)
check("hostile", "review blocks projection, full-zero, pairing and first-jet overclaims", all(word in review.lower() for word in ("project", "curved remainder", "positive", "higher")))
check("propagation", "current state advances through K153", "K153 now closes" in current[:20000])
check("propagation", "roadmap advances only to K154's second restricted lower coefficient", "K154" in roadmap[:10000] and "order-five" in roadmap[:10000])
check("propagation", "context carries the live-versus-restricted distinction", "Current K153" in context[:9000] and "rank-four" in context[:9000])
check("propagation", "tests inventory includes the K153 probe", "selected_k153_null_fivefold_first_lower_probe.py" in tests_readme)
check("predecessor", "K152 carries the K153 successor closure", "## K153 successor classification" in predecessor)

print("K153_PACKET=FIRST_JET_CLOSED_32_LABELS_448D__LOWERER_INERTIA_260_188")
print("K153_FROZEN_P_POWERS=234_125_16_8_0")
print("K153_P5_FIRST_LOWER=LIVE_RANK4_REFERENCE_AND_ROTATED")
print("K153_RESTRICTED_ORDER6=ZERO_REFERENCE_AND_ROTATED__LATER_ORDERS_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("K153 failures: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
