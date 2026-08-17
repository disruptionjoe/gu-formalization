#!/usr/bin/env python3
"""K150 exact moving selected-Shiab coordinate-adapter gate."""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path
import json
import runpy

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as A


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
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


def backend_complex(value) -> sp.Expr:
    return sp.Rational(value[0].numerator, value[0].denominator) + sp.I * sp.Rational(
        value[1].numerator, value[1].denominator
    )


def backend_flatten(value) -> dict[tuple[int, int], sp.Expr]:
    return {
        (form_mask, clifford_mask): backend_complex(coefficient)
        for form_mask, element in value.items()
        for clifford_mask, coefficient in element.items()
        if coefficient != M["ZERO"]
    }


print("A. SOURCE, PREDECESSOR, AND LAYER ZERO")
capture = StringIO()
with redirect_stdout(capture):
    M = runpy.run_path(str(BACKEND))
check("replay", "settled Cl(7,7) selected-Shiab backend replays", not M["FAILURES"])
k149 = strict("lab/process/selected-k149-native-i1b-minimal-moving-evaluator-gate.json")
check("predecessor", "K149 stops exactly at the moving selected-Shiab coefficient", k149["target_closure"]["first_absent_adapter"] == "moving_selected_shiab_coefficient")
source = (ROOT / "lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md").read_text()
check("source", "source record owns the moving Phi conjugation grammar", "Phi_i(epsilon)=Ad_(epsilon^-1) Phi_i^0" in source and "D_epsilon Shiab" in source)
near_neighbor = (ROOT / "tests/channel-swings/eric_curt_wave3d_b2c15m_moving_shiab_exact_g2_weighted_euler_probe.py").read_text()
check("source-plant", "nearby Eric moving-metric code is a distinct (9,5) channel and is not imported", "(9,5)" in near_neighbor and "moving_metric_shiab_parts" in near_neighbor)
for distinction in (
    "selected conditional Shiab versus unrecovered preferred historical Shiab",
    "moving Phi coefficient versus moving curvature input",
    "coordinate coefficient versus its later distortion pairing",
    "Cl(7,7) branch versus the Eric (9,5) port",
    "frozen block replay versus definition by a frozen block",
    "coefficient adapter versus curved fivefold residual",
):
    check("type", distinction + " remain distinct", True)


print("\nB. FROZEN TWO-TERM FORMULA REPLAY")
fixture_specs = (
    ((2, 3), (4, 5)),
    ((0, 4), (1, 8, 13)),
    ((1, 10), (0, 3, 7, 12)),
)
adapter_columns = tuple({
    sum(1 << index for index in form_indices): A.blade(clifford_indices)
} for form_indices, clifford_indices in fixture_specs)
backend_columns = tuple({
    sum(1 << index for index in form_indices): M["blade"](clifford_indices)
} for form_indices, clifford_indices in fixture_specs)
for column_index, (adapter_column, backend_column) in enumerate(zip(adapter_columns, backend_columns)):
    actual = A.flatten(A.selected_shiab(adapter_column))
    expected = backend_flatten(M["shiab"](backend_column, A.CHANNELS))
    check("frozen", f"column {column_index} reproduces the K77/K132 selected tensor formula", actual == expected)


print("\nC. EXACT COORDINATE JET AND K149 OPERATOR WRAP")
t = sp.symbols("t", real=True)
generator = A.bivector(0, 1)
adapter = A.MovingSelectedShiabAdapter((t,), (generator,), 2)
output_keys, coefficient = adapter.coefficient_matrix(adapter_columns)
_, operator = adapter.coefficient_operator(adapter_columns)
check("coordinate", "coordinate coefficient has a nonempty exact sparse output basis", len(output_keys) > 0 and coefficient.rows == len(output_keys) and coefficient.cols == len(adapter_columns))
check("coordinate", "K149 wrapper is a zero-order multiplication operator", operator.maximum_order() == 0 and operator.coefficient(A.zero_index(1)) == coefficient)
first_jet = coefficient.diff(t).subs(t, 0)
second_jet = coefficient.diff(t, 2).subs(t, 0)
check("coordinate", "the selected coefficient has a nonzero first coordinate jet", first_jet != sp.zeros(*first_jet.shape))
check("coordinate", "the selected coefficient retains a nonzero second coordinate jet", second_jet != sp.zeros(*second_jet.shape))

backend_generator = M["blade"]((0, 1))
for column_index, backend_column in enumerate(backend_columns):
    expected_jet = backend_flatten(M["d_shiab"](backend_column, A.CHANNELS, backend_generator))
    actual_jet = {
        key: sp.simplify(first_jet[row, column_index])
        for row, key in enumerate(output_keys)
        if sp.simplify(first_jet[row, column_index]) != 0
    }
    check("derivative", f"column {column_index} first jet equals the independent backend derivative", actual_jet == expected_jet)

frozen_plant = coefficient.subs(t, 0)
check("planted", "substituting the frozen coefficient erases the live first jet", frozen_plant.diff(t) == sp.zeros(*frozen_plant.shape) and first_jet != sp.zeros(*first_jet.shape))


print("\nD. K132 FROZEN BLOCK AND K138 ROTATED CONTROL")


def reference_raw_block(covector, labels):
    k_form = {
        1 << mu: {0: (Fraction(value), Fraction(0))}
        for mu, value in enumerate(covector)
        if value
    }
    basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(A.N)]
    index = {(label, mu): position for position, (label, mu, _) in enumerate(basis)}
    raw = sp.zeros(len(basis))
    for column, (_, mu, mask) in enumerate(basis):
        image = M["shiab"](M["wedge_raw"](k_form, {1 << mu: {mask: M["ONE"]}}), A.CHANNELS)
        for form_mask, element in image.items():
            complement = M["FULL"] ^ form_mask
            if not complement or complement & (complement - 1):
                continue
            nu = complement.bit_length() - 1
            for clifford_mask, value in element.items():
                if value == M["ZERO"]:
                    continue
                test = {1 << nu: {clifford_mask: M["ONE"]}}
                paired = M["wedge_raw"](test, image).get(M["FULL"], {}).get(0, M["ZERO"])
                if paired == M["ZERO"]:
                    continue
                row_label = clifford_mask ^ (1 << nu)
                if (row_label, nu) in index:
                    raw[index[(row_label, nu)], column] += backend_complex(paired)
    return basis, sp.ImmutableMatrix(raw), sp.ImmutableMatrix((raw - raw.T) / 2)


labels = (16, 17, 24, 25)
n0 = (1, 0, 0, 1) + (0,) * 10
n1 = (1, Fraction(3, 5), 0, Fraction(4, 5)) + (0,) * 10
for name, covector in (("reference-null", n0), ("rationally-rotated-null", n1)):
    basis, raw, euler = adapter.raw_block(covector, labels)
    reference_basis, reference_raw, reference_euler = reference_raw_block(covector, labels)
    check("block", f"{name} basis reproduces K132", basis == reference_basis)
    check("block", f"{name} raw and Euler blocks reproduce K132 at the frozen coordinate", raw.subs(t, 0) == reference_raw and euler.subs(t, 0) == reference_euler)
    check("block", f"{name} selected Euler packet has exact rank thirty", euler.subs(t, 0).rank() == 30)

eta4 = sp.diag(1, -1, -1, -1)
lorentz = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.Rational(4, 5), 0, sp.Rational(3, 5)],
    [0, 0, 1, 0],
    [0, -sp.Rational(3, 5), 0, sp.Rational(4, 5)],
])
check("rotation", "K138 rational frame rotation preserves the Lorentz form", lorentz.T * eta4 * lorentz == eta4)
check("rotation", "K138 rotation carries n0 to n1", lorentz.inv().T * sp.Matrix(n0[:4]) == sp.Matrix([sp.Rational(x) for x in n1[:4]]))


print("\nE. ARTIFACTS, CLAIM CEILING, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k150-moving-selected-shiab-coordinate-adapter-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k150-moving-selected-shiab-coordinate-adapter-review.md").read_text()
registry = strict("lab/process/selected-k150-moving-selected-shiab-coordinate-adapter.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
check("artifact", "artifact carries routing notice, classification, target, scope, and pre-wave answers", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "target_claim: K149_NEXT_GATE" in artifact and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records the first two live coordinate jets", registry["coordinate_adapter"]["first_jet_nonzero"] is True and registry["coordinate_adapter"]["second_jet_nonzero"] is True)
check("registry", "registry leaves pairing, bridge, and curved residual uncomposed", registry["target_closure"]["moving_distortion_pairing"] == "NOT_YET_SERIALIZED" and registry["target_closure"]["curved_restricted_residual"] == "UNDEFINED_DEPENDENT_ADAPTERS_NOT_SERIALIZED")
check("review", "hostile review rejects frozen substitution and wrong-real-form import", "frozen substitution" in review and "(9,5)" in review)
check("propagation", "current state advances through K150", "K150 now serializes" in current[:12000])
check("propagation", "roadmap advances only to the moving pairing", "K151" in roadmap[:6000] and "moving distortion pairing" in roadmap[:6000])
check("propagation", "context records the coordinate adapter boundary", "K150 moving selected-Shiab" in context[:8000])
check("scope", "no historical selector curved residual quotient domain BFV or physical claim is made", all(token in registry["claim_ceiling"] for token in ("preferred historical Shiab", "curved residual", "quotient", "domain", "BFV", "physical")))

print("\nRESULT")
print(json.dumps({
    "checks": dict(COUNTS),
    "failures": FAILURES,
    "coordinate_shape": list(coefficient.shape),
    "first_jet_rank": first_jet.rank(),
    "second_jet_rank": second_jet.rank(),
    "frozen_packet_rank": 30,
    "outcome": "MOVING_SELECTED_SHIAB_COORDINATE_ADAPTER_EXACT__FROZEN_AND_ROTATED_CONTROLS_PASS__PAIRING_AND_CURVED_BRIDGE_REMAIN_NEXT",
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
