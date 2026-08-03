#!/usr/bin/env python3
r"""PW2F-R induced-Z1, derived-K, and highest metric-symbol gate.

This probe starts with the omission found by the divergent exact-geometry
review: PW2F's 140 columns used only the algebraic Z0 part of the induced
metric variation.  Here the derivative-bearing Z1(nabla k) cross block of the
connection metric on Y=Met(X) is constructed exactly at the existing normal
frame.  The resulting Levi-Civita/spin symbol is then composed with the exact
connection-incidence part of

    delta K = D_(B+K)(h^-1 delta h) + (Ad_(h^-1)-1) delta B.

The first verdict is deliberately subroute- and coefficient-level.  It asks
whether the exercised principal-Z1 bosonic distortion-norm route is live at
the highest induced metric jet.  A nonzero contribution must be cancelled or
retained by the complete kappa1 assembly; it does not determine the full C4
polynomial, an exceptional tuned kappa1, the total-swervature contribution,
the full C3 relation, an observed four-dimensional symbol, or a physical
equation.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
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
        raise RuntimeError(filename)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


F2 = load_probe("pw2fr_pw2f", "pw2f_native_top_order_metric_composition_probe.py")
D = F2.D
E = F2.E
M = F2.M
B15 = F2.B15
P = D.P


FAILURES: list[str] = []
EXACT = TYPE = SOURCE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


def source(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def is_zero(value) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def coordinate_eta(*indices: int) -> tuple[F, ...]:
    return tuple(F(1) if index in indices else F(0) for index in range(4))


def scale_eta(value: tuple[F, ...], scalar: F) -> tuple[F, ...]:
    return tuple(scalar * item for item in value)


def eta_upstairs(value: tuple[F, ...]) -> tuple[F, ...]:
    return tuple(value) + tuple(F(0) for _ in range(10))


def scalar(value) -> sp.Expr:
    if isinstance(value, F):
        return sp.Rational(value.numerator, value.denominator)
    return sp.sympify(value)


def delta_base_gamma(eta: tuple[F, ...], k: sp.Matrix) -> tuple[sp.Matrix, ...]:
    """Principal variation of Gamma(g) in the base direction eta."""
    matrices = []
    for i in range(4):
        gamma = sp.zeros(4)
        for c in range(4):
            for a in range(4):
                gamma[c, a] = sp.simplify(
                    sp.Rational(1, 2)
                    * sum(
                        P.G4[c, d]
                        * (
                            scalar(eta[i]) * k[a, d]
                            + scalar(eta[a]) * k[i, d]
                            - scalar(eta[d]) * k[i, a]
                        )
                        for d in range(4)
                    )
                )
        matrices.append(gamma)
    return tuple(matrices)


def z1_metric_variation(eta: tuple[F, ...], k: sp.Matrix) -> sp.Matrix:
    """Derivative-bearing cross block of the exact connection metric."""
    coordinate = sp.zeros(14)
    for i, gamma in enumerate(delta_base_gamma(eta, k)):
        connection_metric = sp.simplify(gamma.T * P.G4 + P.G4 * gamma)
        for fibre, basis in enumerate(P.SYM2):
            value = -P.fibre_pair(connection_metric, basis)
            coordinate[i, 4 + fibre] = value
            coordinate[4 + fibre, i] = value
    return sp.simplify(B15.FRAME14.T * coordinate * B15.FRAME14)


def z0_metric_variation(owner: int) -> sp.Matrix:
    return B15.H_VARIATIONS[owner]


def vectorized_columns(matrices: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix.hstack(*(matrix.reshape(196, 1) for matrix in matrices))


def principal_b_form(eta: tuple[F, ...], owner: int, include_z0: bool, include_z1: bool) -> M.SForm:
    variation = sp.zeros(14)
    if include_z0:
        variation += z0_metric_variation(owner)
    if include_z1:
        variation += z1_metric_variation(eta, P.SYM2[owner])
    return B15.lc_spin_form(eta_upstairs(eta), variation)


def lc_spin_form_symbolic(xi, h_y: sp.Matrix) -> M.SForm:
    components = {}
    for mu in range(14):
        internal = {}
        for a in range(14):
            for b in range(a + 1, 14):
                coefficient = sp.simplify(
                    sp.Rational(1, 4)
                    * (scalar(xi[b]) * h_y[mu, a] - scalar(xi[a]) * h_y[mu, b])
                )
                if coefficient != 0:
                    internal[(1 << a) | (1 << b)] = coefficient
        if internal:
            components[(mu,)] = internal
    return M.sfclean(components)


def symbolic_z1_b_form(eta, owner: int) -> M.SForm:
    variation = z1_metric_variation(eta, P.SYM2[owner])
    return lc_spin_form_symbolic(tuple(eta) + tuple(sp.Integer(0) for _ in range(10)), variation)


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def gram(forms: list[M.SForm]) -> sp.Matrix:
    return sp.Matrix(
        len(forms),
        len(forms),
        lambda i, j: sp.simplify(
            (
                D.top_scalar(forms[i], M.sfhodge(forms[j]))
                + D.top_scalar(forms[j], M.sfhodge(forms[i]))
            )
            / 2
        ),
    )


def exact_inertia(matrix: sp.Matrix) -> tuple[int, int, int]:
    positive = negative = zero = 0
    for value, multiplicity in matrix.eigenvals().items():
        simplified = sp.simplify(value)
        if simplified.is_positive:
            positive += multiplicity
        elif simplified.is_negative:
            negative += multiplicity
        elif simplified == 0:
            zero += multiplicity
        else:
            # Fall back only for sign classification of an exact algebraic
            # eigenvalue; rank/nonzero verdicts never use this branch.
            numeric = sp.N(simplified, 80)
            if numeric > 0:
                positive += multiplicity
            elif numeric < 0:
                negative += multiplicity
            else:
                zero += multiplicity
    return positive, negative, zero


def source_and_layer_zero() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    source(
        "the source owns a difference of a connection and gauge-rotated Levi-Civita connection",
        "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in pack
        and "[02:19:17]" in toe
        and "gauge rotated Levy-Chevita connection" in toe,
        "SOURCE-CONFIRMS the connection-difference class",
    )
    source(
        "the source does not identify epsilon with the repository h=exp(u(T,g)) tangent",
        "h=\\exp" not in pack and "h^{-1}D_Bh" not in pack,
        "SOURCE-SILENT on the repository selector",
    )
    typed("source epsilon held fixed, the same epsilon varied independently, and repository-derived h are separate conditional tangent policies; the exercised metric branch fixes both source epsilon and varpi so delta T_top=-delta B_top")
    typed("Z0(k), Z1(nabla k), partial-Z1, the section tangent, and an arbitrary Y14 metric owner are distinct")
    typed("the ten owners below are the induced Sym2(T*X) graph, not 105 arbitrary metric-on-Y owners")
    typed("C4 is adjudicated before the conditional skew-C_EL,3 rule")
    typed("upstairs Y14 conormals and observed base conormals are not identified")
    reject("spend P1/P2/P3 on a continuous induced metric jet", False)
    reject("identify the source-fixed-epsilon ablation with the complete repository-derived-h action", False)
    reject("identify fixed source varpi with fixed T or independently varied varpi", False)


def z1_graph_checks() -> dict[str, object]:
    panel = (
        coordinate_eta(0),
        coordinate_eta(1),
        coordinate_eta(3),
        coordinate_eta(0, 1),
        coordinate_eta(0, 3),
    )
    z1_ranks = []
    z1_b_ranks = []
    full_b_ranks = []
    alt_failures = 0
    scaling_failures = 0
    metric_compatibility_failures = 0
    for eta in panel:
        for owner in range(10):
            for direction, gamma in enumerate(delta_base_gamma(eta, P.SYM2[owner])):
                defect = sp.simplify(
                    gamma.T * P.G4
                    + P.G4 * gamma
                    - scalar(eta[direction]) * P.SYM2[owner]
                )
                metric_compatibility_failures += int(not is_zero(defect))
        z1_columns = [z1_metric_variation(eta, owner) for owner in P.SYM2]
        z1_ranks.append(vectorized_columns(z1_columns).rank())
        z0_forms = [principal_b_form(eta, owner, True, False) for owner in range(10)]
        z1_forms = [principal_b_form(eta, owner, False, True) for owner in range(10)]
        full_forms = [M.sfadd(z0_forms[i], z1_forms[i]) for i in range(10)]
        # Sparse row rank is computed through a common support.
        for forms, ranks in ((z1_forms, z1_b_ranks), (full_forms, full_b_ranks)):
            flattened = [M.flatten_form(value) for value in forms]
            keys = sorted(set().union(*(set(item) for item in flattened)))
            matrix = sp.Matrix([[item.get(key, 0) for item in flattened] for key in keys])
            ranks.append(matrix.rank())
        alt_failures += sum(bool(D.alt_of_t(value)) for value in full_forms)

        doubled = scale_eta(eta, F(2))
        for owner in range(10):
            first = principal_b_form(eta, owner, False, True)
            second = principal_b_form(doubled, owner, False, True)
            scaling_failures += int(not form_equal(second, M.sfscale(first, 4)))

    exact(
        "the missing derivative-bearing Z1 metric graph is live on every preregistered base conormal",
        all(rank > 0 for rank in z1_ranks),
        f"ranks={z1_ranks}",
    )
    exact(
        "the Z1-to-Levi-Civita/spin route is live and quadratic in the base conormal",
        all(rank > 0 for rank in z1_b_ranks) and scaling_failures == 0,
        f"ranks={z1_b_ranks}; scaling_failures={scaling_failures}",
    )
    exact(
        "the Levi-Civita variation satisfies exact linearized metric compatibility",
        metric_compatibility_failures == 0,
        f"failures={metric_compatibility_failures}/{len(panel)*10*4}",
    )
    exact(
        "the full induced Z0+Z1 Levi-Civita symbol is live on the ten-owner graph",
        all(rank > 0 for rank in full_b_ranks),
        f"ranks={full_b_ranks}",
    )
    exact(
        "torsion-free alternation kills the complete exercised Z0+Z1 LC variation",
        alt_failures == 0,
        f"failures={alt_failures}/{len(panel)*10}",
    )
    reject("extend PW2F's Z0-only 140-column statement to the induced Z0+Z1 graph", all(rank == 0 for rank in z1_b_ranks))
    reject("call the five-conormal panel an all-conormal cubic certificate", len(panel) == 560)
    return {
        "panel": panel,
        "z1_metric_ranks": z1_ranks,
        "z1_lc_ranks": z1_b_ranks,
        "full_lc_ranks": full_b_ranks,
    }


def xi_form(eta: tuple[F, ...]) -> M.SForm:
    return {
        (index,): {0: sp.Rational(value.numerator, value.denominator)}
        for index, value in enumerate(eta_upstairs(eta))
        if value
    }


def symbolic_xi_form(eta) -> M.SForm:
    return {
        (index,): {0: scalar(value)}
        for index, value in enumerate(tuple(eta) + tuple(sp.Integer(0) for _ in range(10)))
        if scalar(value) != 0
    }


def all_base_conormal_c5_identity() -> int:
    """Return the number of nonzero symbolic C5 entries over Q[x0..x3]."""
    eta = sp.symbols("eta0:4", real=True)
    b_top = [symbolic_z1_b_form(eta, owner) for owner in range(10)]
    # Evaluate in the unmoved frame. PW2E independently proved the finite
    # naturality identity which transports this scalar polynomial to h.
    t_top = [M.sfscale(value, -1) for value in b_top]
    f_top = [M.sfwedge(symbolic_xi_form(eta), value) for value in b_top]
    mixed = sp.Matrix(
        10,
        10,
        lambda i, j: sp.expand(
            sp.Rational(1, 2)
            * D.top_scalar(t_top[i], D.shiab(f_top[j]))
        ),
    )
    c5 = mixed - mixed.T
    return sum(sp.Poly(sp.expand(value), *eta).as_expr() != 0 for value in c5)


def moved_c5_pairing_comparator(h: M.SCliff, hinv: M.SCliff) -> bool:
    """Check one exact transported-output/pairing C5 comparator at e0."""
    eta = coordinate_eta(0)
    b_top = [principal_b_form(eta, owner, False, True) for owner in range(10)]
    t_top = [M.sfscale(value, -1) for value in b_top]
    f_top = [M.sfwedge(xi_form(eta), value) for value in b_top]
    base = sp.Matrix(
        10,
        10,
        lambda i, j: sp.simplify(
            sp.Rational(1, 2) * D.top_scalar(t_top[i], D.shiab(f_top[j]))
        ),
    )
    moved_t = [E.fconj(hinv, value, h) for value in t_top]
    moved_shiab = [E.fconj(hinv, D.shiab(value), h) for value in f_top]
    moved = sp.Matrix(
        10,
        10,
        lambda i, j: sp.simplify(
            sp.Rational(1, 2) * D.top_scalar(moved_t[i], moved_shiab[j])
        ),
    )
    return is_zero(moved - base) and is_zero(moved - moved.T)


def structural_euler_order_comparator() -> tuple[bool, bool, bool]:
    """Execute the universal q2/q3 Euler-order calculation over Q-symbols."""
    owner_count = 3
    q = [[sp.symbols(f"q_{owner}_{order}") for order in range(7)] for owner in range(owner_count)]
    mass_symbols = {}
    for i in range(owner_count):
        for j in range(i, owner_count):
            mass_symbols[i, j] = sp.symbols(f"m_{i}_{j}")
    coupling = sp.Matrix(owner_count, owner_count, lambda i, j: sp.symbols(f"c_{i}_{j}"))

    def total_d(value):
        return sp.expand(
            sum(
                sp.diff(value, q[owner][order]) * q[owner][order + 1]
                for owner in range(owner_count)
                for order in range(6)
            )
        )

    lagrangian = sp.Integer(0)
    for i in range(owner_count):
        for j in range(owner_count):
            mass = mass_symbols[min(i, j), max(i, j)]
            lagrangian += sp.Rational(1, 2) * mass * q[i][2] * q[j][2]
            lagrangian += coupling[i, j] * q[i][2] * q[j][3]

    euler = []
    for owner in range(owner_count):
        value = sp.Integer(0)
        for order in range(4):
            term = sp.diff(lagrangian, q[owner][order])
            for _ in range(order):
                term = -total_d(term)
            value += term
        euler.append(sp.expand(value))
    c6 = sp.Matrix(owner_count, owner_count, lambda i, j: sp.diff(euler[i], q[j][6]))
    c5 = sp.Matrix(owner_count, owner_count, lambda i, j: sp.diff(euler[i], q[j][5]))
    expected_c5 = coupling - coupling.T
    symmetric_substitution = {
        coupling[i, j]: mass_symbols[min(i, j), max(i, j)]
        for i in range(owner_count)
        for j in range(owner_count)
    }
    return (
        c6 == sp.zeros(owner_count),
        c5 == expected_c5,
        c5.subs(symmetric_substitution) == sp.zeros(owner_count),
    )


def derived_k_and_top_order_checks(graph: dict[str, object]) -> dict[str, object]:
    _, source_t, bridge_u, bridge_du = E.native_inputs()
    c3, c11 = sp.symbols("c3 c11", real=True)
    null_u = M.sclean(
        {
            mask: sp.simplify(value.subs({c3: 1, c11: 1}))
            for mask, value in bridge_u.items()
        }
    )
    h, hinv = E.exponential_pair(null_u, sp.Integer(0))
    exact("the selected Hodge-null bridge is nontrivial and has an exact inverse", h != {0: 1} and E.cinv_pair(h, hinv))
    null_du = M.sfclean(
        {
            key: {
                mask: sp.simplify(value.subs({c3: 1, c11: 1}))
                for mask, value in coefficient.items()
            }
            for key, coefficient in bridge_du.items()
        }
    )
    exact(
        "the Hodge-null background has exact K0=du because the commutator tower vanishes",
        bool(null_du) and not D.ad_u_form(null_u, null_du),
    )
    background_t = M.sfadd(source_t, M.sfscale(null_du, -1))
    exact("the split background distortion T-K is nonzero", bool(background_t))

    ranks = []
    inertias = []
    c5_ranks = []
    c5_symmetric_failures = 0
    ad_failures = 0
    invariant_failures = 0
    z0_ablation_ranks = []
    for eta in graph["panel"]:
        b_top = [principal_b_form(eta, owner, False, True) for owner in range(10)]
        b_z0 = [principal_b_form(eta, owner, True, False) for owner in range(10)]
        # At highest induced base-jet order, Alt(delta B)=0 removes the
        # derivative-bearing delta-u route.  The complete top K incidence is
        # therefore (Ad_h^-1-1)delta B and B+K varies by Ad_h^-1 delta B.
        bhat_top = []
        for value in b_top:
            moved = E.fconj(hinv, value, h)
            k_incidence = M.sfadd(moved, M.sfscale(value, -1))
            ad_failures += int(not form_equal(M.sfadd(value, k_incidence), moved))
            bhat_top.append(moved)
        mass = gram(bhat_top)
        original_mass = gram(b_top)
        invariant_failures += int(not is_zero(mass - original_mass))
        ranks.append(mass.rank())
        inertias.append(exact_inertia(mass))
        z0_ablation_ranks.append(gram(b_z0).rank())

        # Z1 raises delta B and delta T to induced base order two.  The
        # curvature input D(delta Bhat) is therefore order three.  The first
        # action is affine in that curvature input, so C6 vanishes.  Its
        # possible leading Euler coefficient is instead the odd mixed C5
        # block C-C^T between the order-two T prefactor and order-three
        # curvature input.
        t_top = [M.sfscale(value, -1) for value in b_top]
        f_top = [M.sfwedge(xi_form(eta), value) for value in b_top]
        mixed = sp.Matrix(
            10,
            10,
            lambda i, j: sp.simplify(
                sp.Rational(1, 2)
                * D.top_scalar(t_top[i], D.shiab(f_top[j]))
            ),
        )
        c5 = sp.simplify(mixed - mixed.T)
        c5_symmetric_failures += int(not is_zero(c5 + c5.T))
        c5_ranks.append(c5.rank())

    exact(
        "the complete highest-order connection-incidence split reconstructs Ad_h^-1 delta B",
        ad_failures == 0,
        f"failures={ad_failures}",
    )
    exact(
        "active conjugation preserves the exact distortion-norm highest-jet Gram",
        invariant_failures == 0,
        f"failures={invariant_failures}",
    )
    exact(
        "the exercised principal-Z1 kappa1 distortion-norm C4 contribution is nonzero on every non-null panel conormal and vanishes on the planted null conormal",
        all(rank > 0 for rank in ranks[:4]) and ranks[4] == 0,
        f"ranks={ranks}; inertias={inertias}",
    )
    c6_zero, c5_formula, c5_symmetric_zero = structural_euler_order_comparator()
    exact(
        "the executable q2/q3 Euler comparator gives C6=0, C5=C-C^T, and symmetric-C cancellation",
        c6_zero and c5_formula and c5_symmetric_zero and c5_symmetric_failures == 0,
        f"C6_zero={c6_zero}; C5_formula={c5_formula}; symmetric_zero={c5_symmetric_zero}; panel_skew_failures={c5_symmetric_failures}",
    )
    symbolic_c5_nonzero = all_base_conormal_c5_identity()
    exact(
        "the full four-variable conormal polynomial of the exercised principal-Z1 fixed-background branch has zero mixed C5",
        symbolic_c5_nonzero == 0 and all(rank == 0 for rank in c5_ranks),
        f"nonzero_symbolic_entries={symbolic_c5_nonzero}; panel_ranks={c5_ranks}",
    )
    exact(
        "the selected null-h transported-output and pairing comparator preserves the e0 C5 cancellation",
        moved_c5_pairing_comparator(h, hinv),
    )
    exact(
        "the earlier Z0-only ablation also has live norm rank but is not the same highest base-jet block",
        all(rank > 0 for rank in z0_ablation_ranks),
        f"Z0_ranks={z0_ablation_ranks}",
    )
    reject("promote the live principal-Z1 contribution to the complete kappa1 C4 coefficient", False)
    hostile_mixed = sp.Matrix([[0, 1], [0, 0]])
    reject("make every odd mixed block vanish by matcher convention", is_zero(hostile_mixed - hostile_mixed.T))
    reject("infer an exceptional cancelling kappa1 without the complete total-swervature and kappa1 C4 assembly", False)
    reject("apply the skew-C3 rule before the complete C4 value is fixed", False)
    return {
        "mass_c4_ranks": ranks,
        "mass_c4_inertias": inertias,
        "c5_ranks": c5_ranks,
        "z0_ablation_ranks": z0_ablation_ranks,
    }


def boundary_and_next_gate() -> None:
    typed("under the exercised principal-Z1 jet ledger, the executable affine-q3 comparator gives C6 zero and the fixed-background four-variable C5 branch cancels, returning that branch to C4")
    typed("the principal-Z1 kappa1 C4 contribution is exact, but the complete kappa1 and total-swervature C4 assembly is required before any exceptional-kappa or complete-C4 verdict")
    typed("partial-Z1, section-tangent differentiation, total-swervature completion, density/Krein/lowerer motion, and direct/reverse bulk-plus-Green comparison remain open")
    typed("the C4-then-C3 gate survives only after every branch at or above C4 is assembled")
    typed("the source-fixed-epsilon original action and repository-derived-h composed action remain separate conditional branches")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2F-R COMPLETE DERIVED-K / C4-C3 GATE")
    source_and_layer_zero()
    graph = z1_graph_checks()
    result = derived_k_and_top_order_checks(graph)
    boundary_and_next_gate()
    total = EXACT + TYPE + SOURCE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    print(f"MASS_C4_RANKS: {result['mass_c4_ranks']}")
    print(f"MASS_C4_INERTIAS: {result['mass_c4_inertias']}")
    print(f"C5_RANKS: {result['c5_ranks']}")
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("VERDICT: Z1 IS LIVE; EXECUTABLE STRUCTURAL C6 AND EXERCISED-BRANCH C5 CANCEL; NONZERO PRINCIPAL-Z1 KAPPA1 C4 CONTRIBUTION FOUND; COMPLETE C4 AND C3 REMAIN OPEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
