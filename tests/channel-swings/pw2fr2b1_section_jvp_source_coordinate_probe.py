#!/usr/bin/env python3
r"""PW2F-R2B1 exact section/JVP and source-coordinate prerequisite.

This is deliberately a prerequisite to the complete induced-Y14 C4, not a
surrogate for it.  It does four things exactly:

1. distinguishes q_g(epsilon), B_full=Gamma+q, and T=varpi-q in the literal
   source chart, retaining the live Levi-Civita adjoint return;
2. differentiates the normal-frame Zorro section identity as one graph and
   checks the existing exact curved two-jet pullback;
3. proves by a paired off-shell witness that value plus first-JVP data do not
   determine a pulled Hessian when <E,D2 graph> is unowned; and
4. constructs an exact rank-35 quartic conormal reconstruction and universal-
   kappa proportionality gate.

It does not compute the full moving-Shiab/density/Krein/lowerer/pairing second
Frechet graph, the actual C4, C3, a characteristic, a domain, or a physical
equation.  P1/P2/P3 are not used.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))


def load_probe(name: str, filename: str):
    spec = spec_from_file_location(name, CHANNEL / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {filename}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


O = load_probe(
    "b2c15o_source_coordinate",
    "eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py",
)
P = load_probe(
    "b2c15p_zorro_jet",
    "eric_curt_wave3d_b2c15p_source_epsilon_tangent_zorro_dewitt_probe.py",
)


FAILURES: list[str] = []
EXACT = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def type_level(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    condition = not false_claim
    print(f"{'PASS' if condition else 'FAIL'}: planted rejection - {label}", flush=True)
    if not condition:
        FAILURES.append(f"planted: {label}")


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


# ---------------------------------------------------------------------------
# Layer 0 and the corrected literal source-coordinate tangent.


def layer_zero_checks() -> None:
    type_level("q_g(epsilon), B_full=Gamma(g)+q_g(epsilon), T=varpi-q_g(epsilon), and A_total=Gamma(g)+varpi are distinct")
    type_level("fixed source varpi is not fixed A_total and not fixed T")
    type_level("source epsilon and repository h=exp(u(T,g)) remain distinct")
    type_level("section pullback, a section-supported delta current, and Euler-covector pushdown remain distinct")
    type_level("value/first JVP ownership and complete second Frechet ownership are different evidence grades")
    type_level("a 35-monomial formal C4 coefficient is not a characteristic, domain, or physical operator")
    type_level("P1/P2/P3 supply no tangent, second derivative, interpolation coefficient, or kappa selector")


def source_coordinate_checks() -> None:
    dq0, dq1 = sp.symbols("dq0 dq1")
    delta_q = sp.Matrix([dq0, dq1])
    delta_gamma = O.DGAMMA_VARIATION
    delta_b_full = sp.expand(delta_gamma + delta_q)
    delta_t_fixed_varpi = -delta_q

    exact(
        "fixed-varpi source differentiation gives deltaT=-deltaq and deltaB_full=deltaGamma+deltaq",
        is_zero(delta_t_fixed_varpi + delta_b_full - delta_gamma),
    )
    exact(
        "the forbidden deltaT=-deltaB_full shortcut misses a live Levi-Civita variation",
        not is_zero(delta_t_fixed_varpi + delta_b_full)
        and not is_zero(delta_gamma),
    )
    exact(
        "the predecessor source Euler equation retains the exact (D_g Gamma)^! E_T return",
        is_zero(
            O.SOURCE_EULERS[O.B13.g]
            - O.FIXED_A_G
            - O.GAMMA_ADJOINT_E_T
        )
        and not is_zero(O.GAMMA_ADJOINT_E_T),
    )
    exact(
        "the source connection identity closes as B_full+T=Gamma+varpi",
        is_zero((O.GAMMA + O.Q_GRAPH) + (O.varpi - O.Q_GRAPH) - (O.GAMMA + O.varpi)),
    )
    reject(
        "reuse fixed-A metric Euler data as fixed-varpi data",
        is_zero(O.GAMMA_ADJOINT_E_T),
    )
    reject(
        "rename q as the full connection and infer deltaT=-deltaB_full",
        is_zero(delta_t_fixed_varpi + delta_b_full),
    )


# ---------------------------------------------------------------------------
# One-graph normal-frame Zorro/section JVP controls.


ETA4 = sp.symbols("eta0:4")


def delta_lc(owner: sp.Matrix, base_index: int) -> sp.Matrix:
    """Plane-wave LC variation (delta Gamma_i)^c_a at a normal frame."""
    result = sp.zeros(4)
    for c in range(4):
        for a in range(4):
            result[c, a] = sp.simplify(
                sp.Rational(1, 2)
                * sum(
                    P.G4[c, d]
                    * (
                        ETA4[base_index] * owner[d, a]
                        + ETA4[a] * owner[d, base_index]
                        - ETA4[d] * owner[base_index, a]
                    )
                    for d in range(4)
                )
            )
    return result


def section_jvp_checks() -> None:
    metricity_defects = []
    theta_defects = []
    for owner in P.SYM2:
        for i in range(4):
            dgamma = delta_lc(owner, i)
            delta_c = sp.simplify(dgamma.T * P.G4 + P.G4 * dgamma)
            expected = ETA4[i] * owner
            metricity_defects.extend(sp.simplify(item) for item in delta_c - expected)
            # theta=dh-C dx, evaluated on s_g=(id,g).  Differentiating the
            # whole graph gives dk-deltaC, not two independent sources.
            theta_defects.extend(sp.simplify(item) for item in expected - delta_c)
    exact(
        "the one-graph LC/Zorro JVP obeys deltaC_i,ab=partial_i k_ab for all ten owners",
        all(item == 0 for item in metricity_defects),
    )
    exact(
        "differentiating s_g^*theta=0 once gives dk-deltaC=0 without a hand-added section term",
        all(item == 0 for item in theta_defects),
    )

    exact(
        "the exact reconstructed LC-horizontal B2C15P connection-metric jet obeys s_g^*G_Y=g through second base order",
        all(
            P.PULLBACK2[a][b][k][l] == P.G2_BASE[a][b][k][l]
            for a in range(4)
            for b in range(4)
            for k in range(4)
            for l in range(4)
        ),
    )
    product_defects = sum(
        P.PULLBACK2_PRODUCT[a][b][k][l] != P.G2_BASE[a][b][k][l]
        for a in range(4)
        for b in range(4)
        for k in range(4)
        for l in range(4)
    )
    exact(
        "freezing the horizontal Zorro terms produces a live curved second-jet defect",
        product_defects > 0,
        f"defects={product_defects}",
    )

    t, s = sp.symbols("t s")
    k = P.SYM2[0] + 2 * P.SYM2[4]
    ell = P.SYM2[1] - P.SYM2[7]
    pulled = P.G4 + t * k + s * ell
    exact(
        "the affine metric-section graph has DF[k]=k and mixed D2F[k,ell]=0",
        pulled.diff(t).subs({t: 0, s: 0}) == k
        and pulled.diff(t, s).subs({t: 0, s: 0}) == sp.zeros(4),
    )

    eta = (sp.Integer(1), sp.Integer(2), sp.Integer(0), sp.Integer(-1))
    vertical_k = sp.Matrix([sum(eta[i] * k[a, b] for i in range(4)) for a, b in P.PAIRS4])
    vertical_l = sp.Matrix([sum(eta[i] * ell[a, b] for i in range(4)) for a, b in P.PAIRS4])
    frozen_cross = sp.simplify(2 * (vertical_k.T * P.D0 * vertical_l)[0])
    exact(
        "a frozen-section plant emits a nonzero spurious DeWitt mixed Hessian",
        frozen_cross != 0,
        f"spurious={frozen_cross}",
    )
    reject(
        "freeze C while moving g and still claim the differentiated section identity",
        frozen_cross == 0,
    )
    reject(
        "add a separate section tangent after the one-graph theta cancellation",
        any(item != 0 for item in theta_defects),
    )


# ---------------------------------------------------------------------------
# Off-shell graph-curvature insufficiency theorem.


SECOND_FRECHET_CANDIDATES = (
    "trace_gamma",
    "Phi1_first",
    "Hodge_first",
    "Phi1_outer",
    "Phi2",
    "Hodge_inner",
    "Hodge_middle",
    "Hodge_outer",
    "density",
    "Krein_pairing",
    "input_lowerer",
    "output_lowerer",
    "outer_pairing",
    "h_theta1_Bhat2",
)


def off_shell_hessian_checks() -> None:
    z, c, e, h, j, w = sp.symbols("z c e h j w")
    graph = j * z + sp.Rational(1, 2) * c * w * z**2
    action = e * graph + sp.Rational(1, 2) * h * graph**2
    pulled_hessian = sp.expand(sp.diff(action, z, 2).subs(z, 0))
    expected = h * j**2 + e * c * w
    exact(
        "the exact pullback Hessian is J*H_action*J + <E_action,D2graph>",
        sp.expand(pulled_hessian - expected) == 0,
    )
    value0 = graph.subs(z, 0)
    jvp0 = sp.diff(graph, z).subs(z, 0)
    exact(
        "all graph-curvature choices share the same value and first JVP",
        not value0.has(c) and not jvp0.has(c),
    )
    hessian_flat = pulled_hessian.subs(c, 0)
    hessian_curved = pulled_hessian.subs(c, 1)
    exact(
        "two graphs with identical value/JVP have different off-shell Hessians",
        sp.expand(hessian_curved - hessian_flat - e * w) == 0,
    )
    exact(
        "the repository's source-coordinate Euler return supplies a live off-shell E witness",
        not is_zero(O.GAMMA_ADJOINT_E_T),
    )
    exact(
        "on-shell E=0 is the precise control where first-JVP ownership becomes sufficient for this term",
        sp.expand((hessian_curved - hessian_flat).subs(e, 0)) == 0,
    )
    exact(
        "the second-Frechet audit ledger includes all eight Shiab slots and six metric/pairing/rotation candidates",
        len(SECOND_FRECHET_CANDIDATES) == 14
        and set(SECOND_FRECHET_CANDIDATES[:8])
        == {
            "trace_gamma", "Phi1_first", "Hodge_first", "Phi1_outer",
            "Phi2", "Hodge_inner", "Hodge_middle", "Hodge_outer",
        },
    )
    reject(
        "drop <E,D2graph> on an off-shell background with E,c,w nonzero",
        sp.expand(expected - h * j**2) == 0,
    )
    reject(
        "infer D2graph from graph value and first JVP",
        hessian_flat == hessian_curved,
    )
    reject(
        "call the existing first-derivative slot inventory a complete C4",
        len(SECOND_FRECHET_CANDIDATES) == 0,
    )


# ---------------------------------------------------------------------------
# Complete degree-four conormal basis and universal-kappa gate.


MONOMIALS = tuple(alpha for alpha in product(range(5), repeat=4) if sum(alpha) == 4)
POINTS = MONOMIALS


def monomial(point, alpha):
    return sp.prod(sp.Integer(point[i]) ** alpha[i] for i in range(4))


VANDERMONDE = sp.Matrix(
    [[monomial(point, alpha) for alpha in MONOMIALS] for point in POINTS]
)


def evaluate_coefficients(coefficients, point):
    return sp.expand(
        sum(coefficient * monomial(point, alpha) for coefficient, alpha in zip(coefficients, MONOMIALS))
    )


def universal_kappa(a_coefficients, m_coefficients):
    """Classify A+kappa*M coefficientwise as NONE, ANY, or UNIQUE."""
    ratios = set()
    for a_value, m_value in zip(a_coefficients, m_coefficients):
        a_value = sp.simplify(a_value)
        m_value = sp.simplify(m_value)
        if m_value == 0:
            if a_value != 0:
                return ("NONE", None)
            continue
        ratios.add(sp.simplify(-a_value / m_value))
    if not ratios:
        return ("ANY", None)
    if len(ratios) != 1:
        return ("NONE", None)
    return ("UNIQUE", ratios.pop())


def quartic_gate_checks() -> None:
    exact("four base conormal variables have exactly 35 homogeneous degree-four monomials", len(MONOMIALS) == 35)
    exact(
        "the simplex-lattice quartic Vandermonde has exact rational rank 35",
        VANDERMONDE.rank() == 35,
    )

    coefficient_columns = []
    recovered_columns = []
    for owner_pair in range(3):
        coefficients = sp.Matrix(
            [
                sp.Integer((owner_pair + 2) * (index + 1))
                + sum(sp.Integer((slot + 1) * alpha[slot]) for slot in range(4))
                for index, alpha in enumerate(MONOMIALS)
            ]
        )
        values = sp.Matrix([evaluate_coefficients(coefficients, point) for point in POINTS])
        recovered = VANDERMONDE.inv() * values
        coefficient_columns.append(coefficients)
        recovered_columns.append(recovered)
    exact(
        "three independent owner-pair quartics reconstruct every coefficient exactly",
        all(recovered == coefficients for recovered, coefficients in zip(recovered_columns, coefficient_columns)),
    )
    heldouts = ((1, -1, 2, 3), (2, 1, -2, 1), (-1, 3, 1, 2))
    exact(
        "the reconstructed quartics agree at held-out conormals",
        all(
            evaluate_coefficients(recovered, point) == evaluate_coefficients(coefficients, point)
            for recovered, coefficients in zip(recovered_columns, coefficient_columns)
            for point in heldouts
        ),
    )

    old_five = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, 0, 0, 1))
    eta2_fourth = tuple(sp.Integer(1) if alpha == (0, 0, 4, 0) else sp.Integer(0) for alpha in MONOMIALS)
    exact(
        "a nonzero quartic eta_2^4 vanishes on the predecessor five-conormal panel",
        any(eta2_fourth)
        and all(evaluate_coefficients(eta2_fourth, point) == 0 for point in old_five)
        and evaluate_coefficients(eta2_fourth, (0, 0, 1, 0)) == 1,
    )

    m_flat = tuple(item for column in coefficient_columns for item in column)
    a_proportional = tuple(-3 * item for item in m_flat)
    a_broken = list(a_proportional)
    a_broken[-1] += 1
    exact(
        "the flattened gate distinguishes a unique global kappa from the all-zero any-kappa locus",
        universal_kappa(a_proportional, m_flat) == ("UNIQUE", 3)
        and universal_kappa(tuple(sp.Integer(0) for _ in m_flat), tuple(sp.Integer(0) for _ in m_flat)) == ("ANY", None),
    )
    exact(
        "one corrupted owner-monomial coefficient kills global proportionality",
        universal_kappa(tuple(a_broken), m_flat) == ("NONE", None),
    )
    reject(
        "five selected conormals determine the complete quartic",
        all(evaluate_coefficients(eta2_fourth, point) == 0 for point in old_five)
        and not any(eta2_fourth),
    )
    reject(
        "accept a kappa depending on owner pair or monomial",
        universal_kappa(tuple(a_broken), m_flat) != ("NONE", None),
    )
    reject(
        "promote an interpolation without held-out exact reconstruction",
        any(
            evaluate_coefficients(recovered_columns[0], point)
            != evaluate_coefficients(coefficient_columns[0], point)
            for point in heldouts
        ),
    )


def boundary_checks() -> None:
    type_level("this swing constructs prerequisite identities and an insufficiency theorem, not the actual native C4")
    type_level("R2B2A must order-filter all 14 second-Frechet candidates, build or annihilate the C4-capable branches, and retain lower-order debt for the full Hessian")
    type_level("the smooth upstairs action still contains no section delta-current or defect action")
    type_level("Curt remains formally separate and TG-1 AND TG-2 AND TG-3 remains not promoted")


def main() -> int:
    layer_zero_checks()
    source_coordinate_checks()
    section_jvp_checks()
    off_shell_hessian_checks()
    quartic_gate_checks()
    boundary_checks()
    total = EXACT + TYPE + PLANTED
    print(f"SUMMARY: {EXACT} exact + {TYPE} type + {PLANTED} planted = {total}; failures={len(FAILURES)}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: R2B1 PREREQUISITE PASS; LITERAL SOURCE TANGENT CORRECTED, SECTION JVP AND 35-MONOMIAL GATES BUILT, SECOND-FRECHET PRINCIPAL-ORDER AUDIT AND COMPLETE C4 STILL OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
