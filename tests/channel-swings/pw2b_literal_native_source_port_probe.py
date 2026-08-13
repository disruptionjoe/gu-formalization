#!/usr/bin/env python3
"""PW2B active-real-form bridge and moving-projector gate.

This probe tests the distortion-derived grade-3/11 coordinate inside the
already-established active right-H/Krein/C-plus Clifford model. It proves
active-real-form membership and moving-projector identities. It does not
identify the public source bundle, compute the actual source-coordinate
Jacobian, solve the implicit u(T_hat) equation, or establish a global atlas.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests/channel-swings"
REGISTRY = ROOT / "lab/process/pw2b-literal-native-source-port.json"


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R2 = load_probe(
    "pw2b_r2",
    "eric_curt_wave3d_b2c15r2_full_bch_action_gauge_curvature_adjoint_probe.py",
)
Q = R2.Q
B15O = R2.B15O

EXACT = 0
TYPE = 0
SOURCE = 0
PLANTED = 0


def check(label: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(f"exact check failed: {label}")
    EXACT += 1


def type_check(label: str, condition: bool) -> None:
    global TYPE
    if not condition:
        raise AssertionError(f"type check failed: {label}")
    TYPE += 1


def source_check(label: str, condition: bool) -> None:
    global SOURCE
    if not condition:
        raise AssertionError(f"source check failed: {label}")
    SOURCE += 1


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted false claim passed: {label}")
    PLANTED += 1


def grade(value, degree: int):
    return R2.grade(value, degree)


def p2(value):
    return grade(value, 2)


def dp(u, value):
    bracket = R2.cliff_comm(u, value)
    return R2.cliff_add(p2(bracket), R2.cliff_scale(R2.cliff_comm(u, p2(value)), -1))


def inertia(matrix: sp.Matrix) -> tuple[int, int, int]:
    counts = [0, 0, 0]
    for value, multiplicity in matrix.eigenvals().items():
        counts[0 if value > 0 else 1 if value < 0 else 2] += multiplicity
    return tuple(counts)


def main() -> None:
    data = json.loads(REGISTRY.read_text())
    type_check("scoped registry status", data["status"].startswith("PW2B_ACTIVE_REAL_FORM_BRIDGE_ADMISSIBILITY"))
    type_check("candidate active component only", data["native_port"]["domain"].startswith("candidate active component"))
    type_check("public-source and active real-form fork retained", "not proved equivalent" in data["native_port"]["real_form_fork"])
    type_check("one-shot and implicit branches separated", data["layer_zero"]["one_shot_policy"].startswith("u is evaluated from the old T"))
    type_check("source epsilon and Clifford reduction separated", "not identified" in data["layer_zero"]["source_epsilon_warning"])
    type_check("algebraic endpoint and draft A_omega separated", "not thereby identified" in data["layer_zero"]["A_omega_warning"])
    type_check("datum unchanged", data["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED")
    type_check("Curt remains separate", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    type_check("third lane remains closed", data["third_lane_gate"].endswith("NOT_PROMOTED"))
    type_check("PW2C remains gated", data["next_gate"].startswith("PW2C-"))

    # Active sparse-Clifford membership gate. These word identities are the
    # executable right-H, Krein, and C-plus real-form test used by B2C15O/R2.
    A = {Q.GRADE3[0]: F(1)}
    dA = {Q.GRADE3[1]: F(1)}
    star_A = Q.internal_hodge(A)
    check("input distortion blade is grade three", set(mask.bit_count() for mask in A) == {3})
    check("internal Hodge image is grade eleven", set(mask.bit_count() for mask in star_A) == {11})
    u = R2.reduction_value(A, F(5, 3), F(4, 3))
    check("native bridge has exactly grade three and eleven support", set(mask.bit_count() for mask in u) == {3, 11})
    check("native bridge is in the active right-H/Krein/C-plus word class", B15O.word_compatible_variant(u))
    check("grade-three branch is separately real-form compatible", B15O.word_compatible_variant(A))
    check("grade-eleven branch is separately real-form compatible", B15O.word_compatible_variant(star_A))

    # Infinitesimal transport of p_hat=Ad(h^-1) p2 Ad(h).  The finite matrix
    # control proves the differentiated idempotence identity and zero rank
    # trace; the Clifford samples prove the actual native motion is live.
    P = sp.diag(1, 1, 0, 0)
    ad_u = sp.Matrix([[0, 0, 2, 0], [0, 0, 0, -1], [3, 0, 0, 0], [0, 5, 0, 0]])
    dP = P * ad_u - ad_u * P
    check("moved projector satisfies differentiated idempotence", P * dP + dP * P == dP)
    check("moved projector preserves rank infinitesimally", sp.trace(dP) == 0)
    check("frozen projector covariance defect is live", dP != sp.zeros(4))
    reject("freeze the Clifford projector under a nonstabilizer odd motion", dP == sp.zeros(4))

    samples = ({9: F(1)}, {10: F(1)}, {12: F(1)}, {11: F(1)})
    moves = tuple(dp(A, value) for value in samples)
    check("actual Clifford projector derivative is nonzero", all(moves))
    check("grade-two samples move into odd support", all(not p2(value) for value in moves[:3]))
    check("an odd sample returns into the grade-two carrier", bool(p2(moves[3])))

    # Structural block-unitriangular comparator. This is not the derivative
    # of (epsilon,varpi)->(epsilon exp u(T),varpi).
    N = sp.zeros(5)
    N[2, 0], N[3, 1], N[4, 0], N[4, 1] = 1, -2, 3, 1
    ident = sp.eye(5)
    check("tangent correction is square-zero", N * N == sp.zeros(5))
    check("I plus N has exact inverse I minus N", (ident + N) * (ident - N) == ident and (ident - N) * (ident + N) == ident)
    check("structural tangent comparator has full rank", (ident + N).rank() == 5)
    type_check("actual source-coordinate Jacobian remains open", data["native_port"]["source_coordinate_jacobian"].startswith("OPEN"))
    reject("square-zero tangent proof is a global source-atlas theorem", data["native_port"]["global_boundary"] == "PROVED")

    # Five-pair coefficient panel.  Equal Delta controls the established
    # linear-bridge grade-two reduced Maurer--Cartan return, while Hodge-null
    # u itself remains nonzero. This says nothing about the full K.
    panel = ((F(0), F(0)), (F(1), F(0)), (F(5, 3), F(4, 3)), (F(1), F(1)), (F(1), F(-1)))
    values = []
    for c3, c11 in panel:
        ui = R2.reduction_value(A, c3, c11)
        dui = R2.reduction_value(dA, c3, c11)
        qi = R2.bch_h_truncation(ui, dui, 7)
        values.append((c3 * c3 - c11 * c11, ui, qi))
    check("zero pair produces no bridge and no reduced connection return", values[0] == (F(0), {}, {}))
    check("same-Delta pairs have the same held-out reduced connection return", values[1][0] == values[2][0] == 1 and values[1][2] == values[2][2])
    check("both Hodge-null pairs have nonzero bridge", values[3][0] == values[4][0] == 0 and bool(values[3][1]) and bool(values[4][1]))
    check("both Hodge-null grade-two reduced returns vanish", values[3][2] == values[4][2] == {})
    check("both Hodge-null bridges still move the Clifford projector", all(any(dp(values[index][1], sample) for sample in samples) for index in (3, 4)))
    reject("infer u=0 from a vanishing Hodge-null reduced return", values[3][1] == {})
    type_check("reduced return is not full K", "not K_full" in data["layer_zero"]["reduced_connection_return"])
    reject("source selects c3:c11", data["coefficient_panel"]["parameter_status"].startswith("SOURCE_SELECTED"))

    # Trace reversal is kept live rather than inherited narratively.
    lorentz = sp.diag(-1, 1, 1, 1)
    basis = []
    for i in range(4):
        m = sp.zeros(4); m[i, i] = 1; basis.append(m)
    for i in range(4):
        for j in range(i + 1, 4):
            m = sp.zeros(4); m[i, j] = m[j, i] = 1; basis.append(m)
    dewitt = sp.Matrix([[sp.trace(lorentz*a*lorentz*b) - sp.Rational(1, 2)*sp.trace(lorentz*a)*sp.trace(lorentz*b) for b in basis] for a in basis])
    raw = sp.Matrix([[sp.trace(lorentz*a*lorentz*b) for b in basis] for a in basis])
    check("trace-reversed symmetric fibre has inertia six-four", inertia(dewitt) == (6, 4, 0))
    check("raw Frobenius plant has inertia seven-three", inertia(raw) == (7, 3, 0))
    reject("replace the active fibre by raw Frobenius", dewitt == raw)
    reject("substitute Curt seven-seven into the native lane", data["native_total_signature"] == [7, 7])

    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    source_check("source owns epsilon-varpi and B/T grammar", all(token in pack for token in ("B_\\omega", "T_\\omega", "\\frac12", "\\frac13")))
    source_check("source owns gauge-rotated Levi-Civita", "[02:19:17]" in toe and "gauge rotated Levi-Civita" in toe)
    source_check("source owns double-coset continuation", "[02:20:33]" in toe and "double co-set" in toe)
    source_check("source remains silent on c3:c11", any("c3:c11" in item for item in data["source_disposition"]["SOURCE_SILENT"]))

    reject("spend P1/P2/P3 on the continuous bridge", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")
    total = EXACT + TYPE + SOURCE + PLANTED
    print(f"PW2B active bridge: {EXACT} exact + {TYPE} type + {SOURCE} source + {PLANTED} planted = {total} PASS")
    print("RESULT: active-real-form bridge admissibility and moving projector PASS; structural tangent comparator PASS")
    print("BOUNDARY: public-source bundle port, actual source-coordinate Jacobian, global atlas, Ward/BV, and domain remain open")


if __name__ == "__main__":
    main()
