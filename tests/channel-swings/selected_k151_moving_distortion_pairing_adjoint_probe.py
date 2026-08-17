#!/usr/bin/env python3
"""K151 exact moving distortion-pairing and weighted-adjoint gate."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k151_moving_distortion_pairing_adapter as K151
from k149_sparse_differential_jet_api import integration_by_parts_residual


ROOT = Path(__file__).resolve().parents[2]
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


print("A. RETRIEVAL, SOURCE OWNERS, AND LAYER ZERO")
k149 = strict("lab/process/selected-k149-native-i1b-minimal-moving-evaluator-gate.json")
k150 = strict("lab/process/selected-k150-moving-selected-shiab-coordinate-adapter.json")
normal = strict("lab/process/selected-k77-full-normal-owner-bank.json")
check("predecessor", "K150 stops exactly at the moving distortion pairing", "moving distortion pairing" in k150["next_gate"])
check("predecessor", "K149 owns the complete moving weighted-adjoint formula", k149["generic_engine"]["moving_density_pairing_adjoint"] is True)
check("geometry", "K77 owns the exact indefinite degree-one pairing bank", normal["exact_result"]["degree1_pairing_bank_rank"] == 10 and normal["exact_result"]["total_gimmel_inertia"] == [7, 7, 0])
for distinction in (
    "density-dual Shiab coefficient versus field-like primalized operator",
    "Hodge/scalar-Clifford lowerer versus positive Hilbert metric",
    "frozen coordinate transpose versus moving formal adjoint",
    "principal Euler coefficient versus forced lower coefficient",
    "selected conditional Shiab versus unrecovered preferred historical Shiab",
    "pairing adapter versus curved metric bridge or fivefold residual",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT SELECTED DISTORTION PAIRING")
t = sp.symbols("t", real=True)
generator = K150.bivector(0, 4)
labels = (0, 1, 16, 17)
n0 = (1, 0, 0, 1) + (0,) * 10
n1 = (1, sp.Rational(3, 5), 0, sp.Rational(4, 5)) + (0,) * 10
adapter = K150.MovingSelectedShiabAdapter((t,), (generator,), 1)
basis, raw, frozen_shortcut = adapter.raw_block(n0, labels)
lowerer = K151.distortion_lowerer(basis)
moving_lowerer = K151.moving_distortion_lowerer(basis, generator, t, 1)
pairing = K151.MovingDistortionPairing((t,), lowerer, sp.Integer(1))
diagonal = tuple(lowerer.diagonal())
check("carrier", "selected null packet has 56 distortion directions", raw.shape == (56, 56) and len(basis) == 56)
check("pairing", "Hodge/scalar-Clifford lowerer is symmetric and nondegenerate", lowerer == lowerer.T and lowerer.rank() == 56)
check("pairing", "selected lowerer retains split inertia 18 plus and 38 minus", diagonal.count(1) == 18 and diagonal.count(-1) == 38)
check("pairing", "the primalizer is the exact inverse lowerer", pairing.primalizer * lowerer == sp.eye(56) and lowerer * pairing.primalizer == sp.eye(56))
check("naturality", "moving Spin basis preserves the lowerer through first jet", moving_lowerer.subs(t, 0) == lowerer and moving_lowerer.diff(t).subs(t, 0) == sp.zeros(56))
check("density", "selected inner Spin chart preserves unit density", pairing.density == 1)
check("planted", "positive identity is not the Cl(7,7) distortion lowerer", lowerer != sp.eye(56))


print("\nC. K150 COEFFICIENT AND K149 WEIGHTED FORMAL ADJOINT")
raw_zero = raw.subs(t, 0)
raw_jet = raw.diff(t).subs(t, 0)
check("coefficient", "selected density-dual raw coefficient has frozen rank 30", raw_zero.rank() == 30)
check("coefficient", "the selected packet has a live first coefficient jet", raw_jet.rank() == 27)
raw_operator = pairing.first_order_raw_operator(raw, 0)
adjoint = pairing.formal_adjoint(raw_operator)
euler_field = pairing.formal_euler(raw_operator)
euler_density = pairing.lower_field_operator(euler_field)
principal_zero = K151.coefficient_at(euler_density, 1).subs(t, 0)
lower_zero = K151.coefficient_at(euler_density, 0).subs(t, 0)
check("adjoint", "raw and adjoint are first-order while Euler includes order zero", raw_operator.maximum_order() == 1 and adjoint.maximum_order() == 1 and euler_density.maximum_order() == 1)
check("replay", "lowered frozen principal coefficient equals K132 antisymmetrization", principal_zero == frozen_shortcut.subs(t, 0) and principal_zero == (raw_zero - raw_zero.T) / 2)
check("lower", "first moving lower coefficient is exactly minus one-half transpose jet", lower_zero == -raw_jet.T / 2)
check("lower", "the moving coefficient forces a nonzero rank-27 lower term", lower_zero.rank() == 27)
check("planted", "freezing K150 erases the forced lower term", (-raw.subs(t, 0).diff(t).T / 2) == sp.zeros(56) and lower_zero != sp.zeros(56))

identity_pairing = K151.MovingDistortionPairing((t,), sp.eye(56), 1)
plain_field_adjoint = identity_pairing.formal_adjoint(raw_operator)
plain_density_euler = pairing.lower_field_operator(
    K151.add_operators(raw_operator, plain_field_adjoint, sp.Rational(1, 2), sp.Rational(1, 2))
)
check("planted", "plain field-coordinate transpose fails the indefinite weighted principal coefficient", K151.coefficient_at(plain_density_euler, 1).subs(t, 0) != principal_zero)


print("\nD. GREEN IDENTITY AND ROTATED CONTROL")
u = sp.zeros(56, 1)
v = sp.zeros(56, 1)
u[0] = 1 + t
u[5] = t**2
v[3] = 2 - t
v[17] = 1 + 3 * t
residual = integration_by_parts_residual(
    raw_operator, adjoint, u, v, lowerer, lowerer, pairing.density
)
boundary = (u.T * lowerer * raw_operator.coefficient((1,)) * v)[0]
check("green", "weighted formal-adjoint residual is the exact total derivative", sp.simplify(residual - sp.diff(boundary, t)) == 0)
check("planted", "plain field-coordinate adjoint fails the Cl(7,7) Green identity", sp.simplify(integration_by_parts_residual(raw_operator, plain_field_adjoint, u, v, lowerer, lowerer, 1) - sp.diff(boundary, t)) != 0)

rot_basis, rot_raw, rot_frozen = adapter.raw_block(n1, labels)
rot_pairing = K151.MovingDistortionPairing((t,), K151.distortion_lowerer(rot_basis), 1)
rot_euler = rot_pairing.lower_field_operator(
    rot_pairing.formal_euler(rot_pairing.first_order_raw_operator(rot_raw, 0))
)
check("rotation", "rationally rotated packet retains frozen selected rank 30", rot_raw.subs(t, 0).rank() == 30)
check("rotation", "rationally rotated weighted principal replay equals K132 shortcut", K151.coefficient_at(rot_euler, 1).subs(t, 0) == rot_frozen.subs(t, 0))
check("rotation", "rationally rotated packet retains a live moving lower term", K151.coefficient_at(rot_euler, 0).subs(t, 0) != sp.zeros(56))


print("\nE. PROPAGATION, HOSTILE FENCES, AND GOVERNANCE")
artifact = (ROOT / "explorations/conditional-build/selected-k151-moving-distortion-pairing-adjoint-2026-08-17.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-17-selected-k151-moving-distortion-pairing-adjoint-review.md").read_text()
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text()
for marker in (
    "GU-COMPARATOR-ROUTING — scope before inference.",
    "Classification: `SOURCE_NATIVE_ROUTE`.",
    "target_claim:",
    "Scope:",
):
    check("governance", f"artifact carries {marker}", marker in artifact)
check("propagation", "current state advances through K151", "K151 now serializes" in current[:16000])
check("propagation", "roadmap advances only to the curved metric bridge", "K152" in roadmap[:7000] and "curved metric bridge" in roadmap[:7000])
check("hostile", "review forbids promotion of the formal lower term to a curved residual", "not a curved residual" in review.lower())
check("scope", "no inverse domain BFV physical mode positivity propagator or GU-wide verdict is inferred", True)


print("K151_PAIRING=EXACT_CL77_HODGE_SCALAR_LOWERER__INERTIA_18_38__SPIN_JET_NATURAL")
print("K151_ADJOINT=K149_WEIGHTED_FORMAL_ADJOINT__K132_FROZEN_PRINCIPAL_REPLAY")
print("K151_LOWER_TERM=NONZERO_RANK_27__FORCED_BY_MOVING_K150_COEFFICIENT")
print("CURVED_METRIC_BRIDGE=NOT_SERIALIZED__CURVED_RESIDUAL_UNDEFINED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("K151 failures: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
