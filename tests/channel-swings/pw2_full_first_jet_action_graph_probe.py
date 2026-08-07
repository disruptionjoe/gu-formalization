#!/usr/bin/env python3
"""PW2 exact source-domain, moving-reduction, and full-jet gate.

This probe deliberately separates three questions which earlier finite
fixtures could conflate:

1. is a full connection displacement a gauge-orbit tangent/increment?;
2. does projecting that displacement through a moving reductive split retain
   that property?; and
3. does exterior ``dT`` own the full first jet needed after a pointwise
   distortion map is differentiated?

The finite matrix witnesses are structural comparators.  They do not replace
the literal Y^14 bundle, native Alt map, Shiab contraction, or physical Ward
identity.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "lab/process/pw2-full-first-jet-action-graph.json"


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


def p_diag(matrix: sp.Matrix) -> sp.Matrix:
    """Reductive h-projection for the exact diagonal/off-diagonal fixture."""

    return sp.diag(*matrix.diagonal())


def p_coset(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify(matrix - p_diag(matrix))


def is_zero(matrix: sp.Matrix) -> bool:
    return matrix == sp.zeros(*matrix.shape)


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


def is_u4(matrix: sp.Matrix) -> bool:
    return is_zero(sp.simplify(dagger(matrix) * KREIN4 + KREIN4 * matrix))


def sigma4(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify(C4 * bar(matrix) * C4.inv())


def project_h4(matrix: sp.Matrix) -> sp.Matrix:
    return sp.simplify((matrix + sigma4(matrix)) / 2)


exact_checks = 0
planted_checks = 0


def exact(name: str, condition: bool) -> None:
    global exact_checks
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    exact_checks += 1


def planted(name: str, false_claim: bool) -> None:
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    planted_checks += 1


def registry_checks() -> None:
    data = load(REGISTRY)
    exact("registry status", data["status"] == "PW2_EXACT_AUTOMATIC_SOURCE_INTEGRABILITY_OBSTRUCTION")
    exact("layer zero", data["layer_zero"]["B_omega"] != data["layer_zero"]["T_omega"])
    exact("source domain kill", "PROJECTED-GAUGE-DISPLACEMENT-NOT-AUTOMATICALLY-SOURCE-INTEGRABLE" in data["dispositions"])
    exact("full jet live", "EXTERIOR-DT-DOES-NOT-OWN-GENERAL-DK" in data["dispositions"])
    exact("native K not evaluated", data["actual_native_Ku"] == "NOT_EVALUATED_PENDING_LITERAL_PORT_AND_ADMISSIBLE_BACKGROUND")
    exact("PW3 stopped", data["next_gate"].startswith("PW2A-"))
    exact("datum untouched", data["external_datum"] == "P1/P2/P3 UNCHANGED AND UNUSED")
    exact("Curt separated", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    exact("third lane closed", data["third_lane_gate"] == "TG-1 AND TG-2 AND TG-3 = NOT_PROMOTED")


def main() -> None:
    registry_checks()

    # A reductive symmetric-pair fixture: diagonal h and off-diagonal m.
    x = sp.Matrix([[0, 1], [1, 0]])
    y = sp.Matrix([[0, 1], [-1, 0]])
    bracket = comm(x, y)
    exact("x is coset", is_zero(p_diag(x)) and p_coset(x) == x)
    exact("y is coset", is_zero(p_diag(y)) and p_coset(y) == y)
    exact("coset bracket returns to h", p_diag(bracket) == bracket and not is_zero(bracket))

    # At a point, prescribe the Maurer--Cartan jet omega=g^-1 dg by
    # omega_x=x, omega_y=y, and d omega_xy=-[x,y].  The full displacement
    # is flat exactly, as every genuine gauge rotation of a flat reference
    # must be.
    omega_x = x
    omega_y = y
    d_omega_xy = -bracket
    full_curvature = sp.simplify(d_omega_xy + comm(omega_x, omega_y))
    exact("full gauge displacement is flat", is_zero(full_curvature))

    # Projection does not commute with curvature.  K=p_h omega has zero
    # point value but nonzero derivative/curvature.  Therefore B+K cannot be
    # epsilon_K^-1 d epsilon_K when B is flat.  This is the exact finite
    # source-coordinate obstruction for a projected displacement.
    k_x = p_diag(omega_x)
    k_y = p_diag(omega_y)
    d_k_xy = p_diag(d_omega_xy)
    k_curvature = sp.simplify(d_k_xy + comm(k_x, k_y))
    exact("projected point displacement vanishes", is_zero(k_x) and is_zero(k_y))
    exact("projected derivative survives", d_k_xy == -bracket and not is_zero(d_k_xy))
    exact("projected displacement is curved", k_curvature == -bracket and not is_zero(k_curvature))
    planted("projection preserves Maurer-Cartan", is_zero(k_curvature))
    planted("projected K is a flat-reference gauge orbit", is_zero(k_curvature))

    # Repeat the load-bearing return in PW1's actual mixed-sign finite
    # U(2,2)/Sp(1,1) reduction rather than relying only on the small diagonal
    # pedagogical pair.
    x4 = sp.diag(I / 2, 0, I / 2, 0)
    y4 = sp.zeros(4)
    y4[0, 1] = y4[1, 0] = sp.Rational(1, 2)
    y4[2, 3] = y4[3, 2] = sp.Rational(1, 2)
    bracket4 = comm(x4, y4)
    exact("U22 carrier membership", is_u4(x4) and is_u4(y4))
    exact("U22/Sp11 x is coset", is_zero(project_h4(x4)))
    exact("U22/Sp11 y is coset", is_zero(project_h4(y4)))
    exact("U22/Sp11 bracket returns", project_h4(bracket4) == bracket4 and not is_zero(bracket4))
    arbitrary4 = sp.Matrix(4, 4, range(16))
    exact("U22/Sp11 projector idempotent", project_h4(project_h4(arbitrary4)) == project_h4(arbitrary4))
    full_curvature4 = -bracket4 + comm(x4, y4)
    projected_curvature4 = project_h4(-bracket4) + comm(project_h4(x4), project_h4(y4))
    exact("U22/Sp11 full displacement flat", is_zero(full_curvature4))
    exact("U22/Sp11 projected displacement curved", projected_curvature4 == -bracket4 and not is_zero(projected_curvature4))

    # Positive tangent control: an h-valued exact infinitesimal displacement
    # D_B zeta has vanishing linearized curvature at a flat reference.
    h = sp.diag(2, -1)
    dzeta_x = h
    dzeta_y = 3 * h
    d_dzeta_xy = sp.zeros(2)
    tangent_curvature = sp.simplify(d_dzeta_xy)
    exact("source tangent control lies in h", p_diag(dzeta_x) == dzeta_x and p_diag(dzeta_y) == dzeta_y)
    exact("source tangent control is linearly flat", is_zero(tangent_curvature))

    # Moving projector derivative.  p_s(X)=g(s)^-1 p(g(s)Xg(s)^-1)g(s).
    # Its derivative is [pX,z]-p([X,z]); freezing p drops a live owner.
    s = sp.symbols("s", real=True)
    z = sp.Matrix([[0, 1], [0, 0]])
    g = sp.eye(2) + s * z  # exact because z^2=0
    g_inv = sp.eye(2) - s * z
    arbitrary = sp.Matrix([[1, 2], [3, 4]])
    moving_projection = sp.simplify(g_inv * p_diag(g * arbitrary * g_inv) * g)
    dp_direct = moving_projection.diff(s).subs(s, 0)
    dp_formula = sp.simplify(comm(p_diag(arbitrary), z) - p_diag(comm(arbitrary, z)))
    exact("moving projector derivative formula", dp_direct == dp_formula)
    exact("moving projector derivative is live", not is_zero(dp_direct))
    planted("fixed projector owns moving variation", is_zero(dp_direct))

    # Full Spencer jet versus its exterior quotient.  These are two affine,
    # hence holonomic, germs with the same value and same dT at the origin.
    # The pointwise legal comparator K_x=T_x, K_y=-T_y has
    # dK_xy=-(partial_x T_y + partial_y T_x), so it sees the symmetric jet.
    germ_a = {"dx_Tx": 0, "dx_Ty": 1, "dy_Tx": 0, "dy_Ty": 0}
    germ_b = {"dx_Tx": 0, "dx_Ty": 2, "dy_Tx": 1, "dy_Ty": 0}

    def exterior_dt(germ):
        return germ["dx_Ty"] - germ["dy_Tx"]

    def symmetric_cross(germ):
        return germ["dx_Ty"] + germ["dy_Tx"]

    def exterior_dk(germ):
        return -symmetric_cross(germ)

    exact("same exterior dT", exterior_dt(germ_a) == exterior_dt(germ_b) == 1)
    exact("different full Spencer jets", germ_a != germ_b)
    exact("symmetric jet differs", symmetric_cross(germ_a) == 1 and symmetric_cross(germ_b) == 3)
    exact("dK distinguishes the jets", exterior_dk(germ_a) == -1 and exterior_dk(germ_b) == -3)
    planted("dT determines dK", exterior_dk(germ_a) == exterior_dk(germ_b))
    planted("Alt quotient is the full first jet", germ_a == germ_b)

    # Trace reversal is retained explicitly on the Lorentzian symmetric
    # fibre, not inferred from a Euclidean trace/traceless mnemonic.
    h4 = sp.diag(-1, 1, 1, 1)
    sym2_basis = []
    for row in range(4):
        matrix = sp.zeros(4)
        matrix[row, row] = 1
        sym2_basis.append(matrix)
    for row in range(4):
        for col in range(row + 1, 4):
            matrix = sp.zeros(4)
            matrix[row, col] = matrix[col, row] = 1
            sym2_basis.append(matrix)

    def dewitt(left, right):
        hl = h4 * left
        hr = h4 * right
        return sp.trace(hl * hr) - sp.Rational(1, 2) * sp.trace(hl) * sp.trace(hr)

    def raw_frobenius(left, right):
        return sp.trace((h4 * left) * (h4 * right))

    dewitt_gram = sp.Matrix([[dewitt(left, right) for right in sym2_basis] for left in sym2_basis])
    raw_gram = sp.Matrix([[raw_frobenius(left, right) for right in sym2_basis] for left in sym2_basis])
    inertia = {"positive": 0, "negative": 0, "zero": 0}
    for eigenvalue, multiplicity in dewitt_gram.eigenvals().items():
        if eigenvalue > 0:
            inertia["positive"] += multiplicity
        elif eigenvalue < 0:
            inertia["negative"] += multiplicity
        else:
            inertia["zero"] += multiplicity
    exact("Lorentz Sym2 dimension", len(sym2_basis) == 10 and dewitt_gram.rank() == 10)
    exact("trace-reversed Lorentz fibre inertia", inertia == {"positive": 6, "negative": 4, "zero": 0})
    raw_inertia = {"positive": 0, "negative": 0, "zero": 0}
    for eigenvalue, multiplicity in raw_gram.eigenvals().items():
        if eigenvalue > 0:
            raw_inertia["positive"] += multiplicity
        elif eigenvalue < 0:
            raw_inertia["negative"] += multiplicity
        else:
            raw_inertia["zero"] += multiplicity
    exact("unreversed Lorentz fibre inertia", raw_inertia == {"positive": 7, "negative": 3, "zero": 0})
    planted("raw Frobenius equals trace reversal", raw_gram == dewitt_gram)

    # Layer-0/source dispositions are tested as content, not just nonempty.
    data = load(REGISTRY)
    source = data["source_disposition"]
    exact("source confirms action coordinates", any("B_omega" in row and "epsilon" in row for row in source["SOURCE_CONFIRMS"]))
    exact("source corrects split", any("projected" in row for row in source["SOURCE_CORRECTS"]))
    exact("source silent on rescue", any("integrable" in row for row in source["SOURCE_SILENT"]))

    # A physical odd Ward identity remains a typed stop, not a failed zero.
    exact("physical Ward not evaluated", data["ward_status"] == "NOT_EVALUABLE_PHYSICAL_ODD_MAP_AND_SOURCE_LEGAL_SPLIT_OPEN")
    planted("P1 is a source-coordinate lift", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")

    print(f"PW2 full-jet/source-domain gate: {exact_checks} exact + {planted_checks} planted = {exact_checks + planted_checks} PASS")


if __name__ == "__main__":
    main()
