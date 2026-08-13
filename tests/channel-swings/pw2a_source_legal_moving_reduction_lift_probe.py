#!/usr/bin/env python3
"""PW2A exact local source lift and reductive-compensator gate.

The load-bearing distinction is between projecting a gauge displacement
against an old reduction and transporting the reduction with the source gauge
coordinate.  The former need not be integrable; the latter is a genuine local
source-coordinate construction.  All matrix fixtures here are structural and
leave the literal Y^14 atlas and active source/native bundle port open.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/pw2a-source-legal-moving-reduction-lift.json"
SOURCE_PACK = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
TOE = ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md"


class DuplicateKeyError(ValueError):
    pass


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError(key)
        out[key] = value
    return out


def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def comm(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.simplify(left * right - right * left)


def zero(matrix: sp.Matrix) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


def p_h(matrix: sp.Matrix) -> sp.Matrix:
    return sp.diag(*matrix.diagonal())


def p_m(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify(matrix - p_h(matrix))


I = sp.I
KREIN4 = sp.diag(1, -1, 1, -1)
OMEGA4 = sp.zeros(4)
OMEGA4[:2, 2:] = sp.eye(2)
OMEGA4[2:, :2] = -sp.eye(2)
C4 = -OMEGA4 * KREIN4


def bar(matrix: sp.Matrix) -> sp.Matrix:
    return matrix.applyfunc(sp.conjugate)


def dagger(matrix: sp.Matrix) -> sp.Matrix:
    return bar(matrix).T


def is_u22(matrix: sp.Matrix) -> bool:
    return zero(dagger(matrix) * KREIN4 + KREIN4 * matrix)


def sigma4(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify(C4 * bar(matrix) * C4.inv())


def project_h4(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify((matrix + sigma4(matrix)) / 2)


EXACT = 0
TYPE = 0
SOURCE = 0
PLANTED = 0


def exact(name: str, condition: bool) -> None:
    global EXACT
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    EXACT += 1


def type_level(name: str, condition: bool) -> None:
    global TYPE
    if not condition:
        raise AssertionError(f"type/registry check failed: {name}")
    TYPE += 1


def source_receipt(name: str, condition: bool) -> None:
    global SOURCE
    if not condition:
        raise AssertionError(f"source receipt failed: {name}")
    SOURCE += 1


def planted(name: str, false_claim: bool) -> None:
    global PLANTED
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    PLANTED += 1


def registry_checks() -> None:
    data = load(REGISTRY)
    type_level("registry status", data["status"] == "PW2A_ABSTRACT_LOCAL_COMOVING_GAUGE_LIFT_PASS")
    type_level("route one leads", data["route_comparison"][0]["verdict"] == "LEAD_ABSTRACT_STRUCTURAL_PASS_LITERAL_SOURCE_GATE_OPEN")
    type_level("curvature return is not a connection", data["layer_zero"]["curvature_compensator"] != data["layer_zero"]["connection_compensator"])
    type_level("connection PDE remains open", data["route_comparison"][1]["connection_level"] == "OPEN_NONLINEAR_PDE_WITH_DOMAIN_AND_HOLONOMY_BURDEN")
    type_level("independent B remains rival", data["route_comparison"][2]["source_grade"] == "REPOSITORY_EXTENSION_NOT_SOURCE_SELECTED")
    type_level("literal port open", data["literal_native_status"].startswith("NOT_EVALUATED"))
    type_level("datum unused", data["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED")
    type_level("Curt separate", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    type_level("third lane closed", data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED")
    type_level("PW3 stopped", data["next_gate"].startswith("PW2B-"))


def main() -> None:
    registry_checks()

    # A globally defined exact GL(2) local gauge chart.  X and Y are coset
    # generators for the diagonal/off-diagonal symmetric pair.
    x, y = sp.symbols("x y", real=True)
    x_gen = sp.Matrix([[0, 1], [0, 0]])
    y_gen = sp.Matrix([[0, 0], [1, 0]])
    ident = sp.eye(2)
    gauge = (ident + x * x_gen) * (ident + y * y_gen)
    gauge_inv = (ident - y * y_gen) * (ident - x * x_gen)
    exact("polynomial gauge inverse", sp.simplify(gauge_inv * gauge) == ident)

    omega_x = sp.simplify(gauge_inv * gauge.diff(x))
    omega_y = sp.simplify(gauge_inv * gauge.diff(y))
    full_curvature = sp.simplify(omega_y.diff(x) - omega_x.diff(y) + comm(omega_x, omega_y))
    exact("full Maurer-Cartan identity", zero(full_curvature))

    # Nonzero-background covariance control.  This verifies the full finite
    # curvature-conjugacy formula in the abstract GL(2) chart rather than
    # inferring it only from the flat Maurer--Cartan case.
    base_x = sp.diag(1, -1)
    base_y = sp.Matrix([[0, 2], [3, 0]])
    moved_bx = sp.simplify(gauge_inv * base_x * gauge + omega_x)
    moved_by = sp.simplify(gauge_inv * base_y * gauge + omega_y)
    moved_curvature = sp.simplify(moved_by.diff(x) - moved_bx.diff(y) + comm(moved_bx, moved_by))
    expected_moved_curvature = sp.simplify(gauge_inv * comm(base_x, base_y) * gauge)
    exact("nonzero-background curvature conjugacy", zero(moved_curvature - expected_moved_curvature))
    exact("nonzero-background control is live", not zero(expected_moved_curvature))
    planted("connection transforms homogeneously", moved_bx == gauge_inv * base_x * gauge)

    # The source coordinate composition epsilon' = epsilon g, with epsilon=1
    # and fixed varpi in this chart.  It changes B and T oppositely and keeps
    # the total connection exactly fixed.
    varpi_x = sp.Matrix([[2, 1], [3, -1]])
    varpi_y = sp.Matrix([[0, 4], [-2, 5]])
    b_prime = (omega_x, omega_y)
    t_prime = (sp.simplify(varpi_x - omega_x), sp.simplify(varpi_y - omega_y))
    exact("source total x fixed", sp.simplify(b_prime[0] + t_prime[0]) == varpi_x)
    exact("source total y fixed", sp.simplify(b_prime[1] + t_prime[1]) == varpi_y)
    planted("source composition changes total connection", sp.simplify(b_prime[0] + t_prime[0]) != varpi_x)

    # Move the reduction with the same gauge coordinate.  Compatibility is
    # exact; freezing J instead leaves a live covariant derivative.
    j0 = sp.diag(1, -1)
    j_moving = sp.simplify(gauge_inv * j0 * gauge)
    dj_x = sp.simplify(j_moving.diff(x) + comm(omega_x, j_moving))
    dj_y = sp.simplify(j_moving.diff(y) + comm(omega_y, j_moving))
    exact("moving J remains involutive", sp.simplify(j_moving * j_moving) == ident)
    exact("moving J x compatibility", zero(dj_x))
    exact("moving J y compatibility", zero(dj_y))
    origin = {x: 0, y: 0}
    frozen_j_return = comm(omega_x.subs(origin), j0)
    exact("frozen J return is live", not zero(frozen_j_return))
    planted("fixed J is compatible with nonstabilizer lift", zero(frozen_j_return))

    # Projecting against the old fixed reduction loses the coset bracket.
    k_x, k_y = p_h(omega_x), p_h(omega_y)
    phi_x, phi_y = p_m(omega_x), p_m(omega_y)
    f_k = sp.simplify(k_y.diff(x) - k_x.diff(y) + comm(k_x, k_y)).subs(origin)
    q_phi = p_h(comm(phi_x, phi_y)).subs(origin)
    h_bracket = comm(x_gen, y_gen)
    exact("projected curvature is nonzero", f_k == -h_bracket and not zero(f_k))
    exact("coset curvature return is nonzero", q_phi == h_bracket and not zero(q_phi))
    exact("forced reductive curvature completion", zero(f_k + q_phi))

    coefficient = sp.symbols("lambda", real=True)
    corrected = sp.simplify(f_k + coefficient * q_phi)
    exact("compensator coefficient uniquely one", sp.solve(corrected[0, 0], coefficient) == [1])
    planted("projected curvature is source-integrable alone", zero(f_k))
    planted("half-strength component compensator works", zero(f_k + sp.Rational(1, 2) * q_phi))

    # The m equation is a separate required half of the Maurer-Cartan split.
    m_equation = sp.simplify(
        p_m(omega_y.diff(x) - omega_x.diff(y))
        + p_m(comm(k_x, phi_y) + comm(phi_x, k_y) + comm(phi_x, phi_y))
    )
    exact("coset Maurer-Cartan equation", zero(m_equation))

    # The curvature-level Q_phi is a two-form component.  Producing a new
    # h-valued connection one-form c requires solving an equation for dc and
    # cannot be inferred by changing this coefficient.
    data = load(REGISTRY)
    type_level("curvature and connection compensators have different degrees", data["layer_zero"]["curvature_compensator_degree"] == 2 and data["layer_zero"]["connection_compensator_degree"] == 1)
    type_level("flat cohomology obstruction typed", data["connection_compensator_burden"]["flat_linearized_obstruction"] == "[R] in H2_D_B")
    type_level("curved covariant derivative is not a complex", data["connection_compensator_burden"]["curved_background"] == "D_B^2=ad(F_B), so ordinary H1/H2 language is unavailable before a deformation complex is built")
    planted("curvature return is itself a connection lift", data["layer_zero"]["curvature_compensator_degree"] == data["layer_zero"]["connection_compensator_degree"])
    planted("curved D_B defines ordinary cohomology", data["connection_compensator_burden"]["curved_background"].startswith("ordinary H"))

    # Replay the exact mixed-sign U(2,2)/Sp(1,1) return so the transparent
    # GL(2) chart does not carry the conclusion alone.
    x4 = sp.diag(I / 2, 0, I / 2, 0)
    y4 = sp.zeros(4)
    y4[0, 1] = y4[1, 0] = sp.Rational(1, 2)
    y4[2, 3] = y4[3, 2] = sp.Rational(1, 2)
    bracket4 = comm(x4, y4)
    exact("mixed-sign carrier membership", is_u22(x4) and is_u22(y4))
    exact("mixed-sign generators are coset", zero(project_h4(x4)) and zero(project_h4(y4)))
    exact("mixed-sign bracket returns", project_h4(bracket4) == bracket4 and not zero(bracket4))
    exact("mixed-sign full curvature cancels", zero(-bracket4 + comm(x4, y4)))
    projected4 = project_h4(-bracket4) + comm(project_h4(x4), project_h4(y4))
    exact("mixed-sign projection is curved", projected4 == -bracket4 and not zero(projected4))
    exact("mixed-sign compensation cancels", zero(projected4 + project_h4(bracket4)))

    # The full curvature identity cancels individually nonzero differentiated
    # and quadratic terms.  It is an order-drop certificate for curvature,
    # not yet for every slot of Weinstein's first action.
    derivative_term = sp.simplify(omega_y.diff(x) - omega_x.diff(y))
    quadratic_term = comm(omega_x, omega_y)
    exact("curvature derivative term live", not zero(derivative_term))
    exact("curvature quadratic term live", not zero(quadratic_term))
    exact("curvature order-drop cancellation", zero(derivative_term + quadratic_term))
    planted("differentiate K and keep only its Hessian", zero(derivative_term))
    planted("curvature order drop proves full action order drop", data["action_order_drop"] == "PROVED_FOR_COMPLETE_SOURCE_ACTION")

    # Local flatness does not establish a global source gauge orbit.  A flat
    # U(1) connection with half-integral circle holonomy is the exact control.
    holonomy = sp.simplify(sp.exp(2 * sp.pi * I * sp.Rational(1, 2)))
    exact("flat circle holonomy control is nontrivial", holonomy == -1)
    planted("local Maurer-Cartan implies global trivial holonomy", holonomy == 1)

    # Trace reversal remains live on the actual symmetric metric fibre.
    lorentz = sp.diag(-1, 1, 1, 1)
    sym2 = []
    for row in range(4):
        matrix = sp.zeros(4)
        matrix[row, row] = 1
        sym2.append(matrix)
    for row in range(4):
        for col in range(row + 1, 4):
            matrix = sp.zeros(4)
            matrix[row, col] = matrix[col, row] = 1
            sym2.append(matrix)

    def dewitt(left, right):
        hl, hr = lorentz * left, lorentz * right
        return sp.trace(hl * hr) - sp.Rational(1, 2) * sp.trace(hl) * sp.trace(hr)

    def raw(left, right):
        return sp.trace((lorentz * left) * (lorentz * right))

    gram = sp.Matrix([[dewitt(left, right) for right in sym2] for left in sym2])
    raw_gram = sp.Matrix([[raw(left, right) for right in sym2] for left in sym2])

    def inertia(matrix):
        counts = [0, 0, 0]
        for value, multiplicity in matrix.eigenvals().items():
            counts[0 if value > 0 else 1 if value < 0 else 2] += multiplicity
        return tuple(counts)

    exact("trace-reversed fibre inertia", inertia(gram) == (6, 4, 0))
    exact("unreversed comparator inertia", inertia(raw_gram) == (7, 3, 0))
    planted("raw Frobenius is the required fibre", gram == raw_gram)
    planted("Curt 7+7 is the active native total signature", data["native_total_signature"] == [7, 7])

    # Primary-source collision is executable and timestamped.
    source_pack = SOURCE_PACK.read_text()
    toe = TOE.read_text()
    source_receipt("source owns epsilon-varpi action coordinates", all(token in source_pack for token in ("B_\\omega", "T_\\omega", "epsilon", "varpi")))
    source_receipt("source owns gauge-rotated LC statement", "[02:19:17]" in toe and "gauge rotated Levi-Civita" in toe)
    source_receipt("source owns double-coset continuation", "[02:20:33]" in toe and "double co-set" in toe)
    source = data["source_disposition"]
    type_level("source collision and derivation buckets complete", all(source[key] for key in ("SOURCE_CONFIRMS", "SOURCE_CORRECTS", "SOURCE_SILENT", "REPOSITORY_DERIVED")))

    planted("P1 supplies the continuous gauge lift", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")
    planted("local fixture is literal Y14", data["literal_native_status"] == "PROVED")

    total = EXACT + TYPE + SOURCE + PLANTED
    print(f"PW2A abstract lift: {EXACT} algebraic exact + {TYPE} type/registry + {SOURCE} source receipts + {PLANTED} planted = {total} PASS")
    print("RESULT: the abstract co-moving mechanism passes; literal source-H and nested-native transport remain open")
    print("RESULT: the coefficient-one coset curvature return is forced but is not a connection one-form")
    print("BOUNDARY: global descent, literal active-native port, complete action order drop, and analytic domain remain open")


if __name__ == "__main__":
    main()
