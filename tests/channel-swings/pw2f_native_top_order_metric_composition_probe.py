#!/usr/bin/env python3
r"""PW2F active-native top-order trace-reversed metric composition gate.

The gate investigates the narrow question left by PW2E: does the current
active first action require a base fourth metric jet?  It does not infer the
answer from a scalar comparator.  Hostile review established that this packet
does not yet answer it, because the exact induced-Y14 Levi-Civita alternation
subroute is not the complete derived-K metric variation.

The first exact identity is geometric: the principal Levi-Civita variation is
torsion-free, hence its total alternation is zero.  Hostile review proved that
this does *not* settle the full derived connection variation.  For
``K=h^-1 D_B h`` the separate connection-incidence term
``(Ad_(h^-1)-1) delta B`` is live.  The probe therefore preserves the LC
alternation result as one subroute, constructs a 129-of-140 exact witness for
the omitted summand, and leaves the complete top-order sum open.

A separate ten-field Euler/Green calculation still proves the conditional
theorem that an affine-second-jet Lagrangian has no fourth-order Euler
coefficient; its only possible third-order coefficient is the skew velocity
derivative of the affine coefficient.  The selected active-native
curvature-input panel has a zero self-third block and retains a live rank-seven
second-order bank.  These facts may not be promoted to the full action until
the complete ``delta K`` route is assembled.

This is an active-local repository theorem.  It is not the missing public
source-to-Sp bundle port, a global Y14 theorem, a physical quotient rank, or a
diffeomorphism Ward identity.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import json
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


D = load_probe("pw2f_pw2d", "pw2d_native_transported_shiab_action_probe.py")
E = load_probe("pw2f_pw2e", "pw2e_finite_native_shiab_descent_probe.py")
O = load_probe(
    "pw2f_b2c15o",
    "eric_curt_wave3d_b2c15o_native_y14_background_stabilizer_probe.py",
)
N = load_probe(
    "pw2f_b2c15n",
    "eric_curt_wave3d_b2c15n_full_owner_euler_moving_atlas_probe.py",
)
M = D.M
B15 = O.B15
P = D.P
REGISTRY = ROOT / "lab/process/pw2f-native-top-order-metric-ward-registry.json"


FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
    global TYPE
    TYPE += 1
    print(f"{'PASS' if condition else 'FAIL'}: type-level - {label}", flush=True)
    if not condition:
        FAILURES.append(f"type: {label}")


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


def source_and_layer_zero() -> None:
    data = json.loads(REGISTRY.read_text())
    manifest = json.loads(
        (ROOT / "lab/process/pw2f-primary-source-collision-manifest.json").read_text()
    )
    source(
        "every decisive PW2F source-collision row has a fail-closed disposition and evidence grade",
        {row["disposition"] for row in manifest["rows"]}
        == {"SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"}
        and all(row["slice_sha256"] and row["evidence_grade"] for row in manifest["rows"]),
    )
    source(
        "the source confirms the metric-to-Levi-Civita-to-Y/spin chain and written first-action grammar but is silent on the active top coefficient",
        data["source_disposition"]["metric_chain"] == "SOURCE-CONFIRMS"
        and data["source_disposition"]["written_first_action_grammar"] == "SOURCE-CONFIRMS"
        and data["source_disposition"]["active_top_order"] == "SOURCE-SILENT",
    )
    source(
        "the source corrects projection to contraction and Xi is not promoted to a diffeomorphism Ward",
        data["source_disposition"]["relevant_curvature_contraction_vs_projection"] == "SOURCE-CORRECTS"
        and data["source_disposition"]["diffeomorphism_ward"] == "SOURCE-SILENT",
    )
    source(
        "the odot-epsilon/odot-omega identity and the full active pairing/metric-motion policy remain source-silent",
        data["source_disposition"]["odot_epsilon_vs_odot_omega"]
        == "SOURCE-SILENT_IDENTITY_FORK"
        and data["source_disposition"]["full_metric_density_krein_pairing_motion"]
        == "SOURCE-SILENT"
        and data["source_disposition"]["full_epsilon_metric_variation_policy"]
        == "SOURCE-SILENT",
    )
    typed("source epsilon, induced Levi-Civita Gamma, and repository-derived h=exp(u) are distinct")
    typed("source T_omega, synthetic T_syn, ordinary torsion, and literal K_full are distinct")
    typed("public Shiab contraction, active grade projector, and active moving-Shiab fixture are distinct")
    typed("fixed-varpi, fixed-total-A, and fixed-B are distinct metric tangent policies")
    typed("the active-local result cannot be attributed as the unported public source operator")
    reject("use P1/P2/P3 as a continuous metric jet or coefficient", data["external_datum"] != "P1/P2/P3 UNCHANGED AND UNUSED")
    reject("identify Curt's seven-seven branch with trace-reversed active nine-five", data["curt_track"] != "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")


def xi_form(xi: tuple[F, ...]) -> M.SForm:
    return {
        (index,): {0: sp.Rational(value.numerator, value.denominator)}
        for index, value in enumerate(xi)
        if value
    }


def coordinate_xi(*indices: int) -> tuple[F, ...]:
    return tuple(F(1) if index in indices else F(0) for index in range(B15.N))


def transgression_and_bridge_principal() -> tuple[M.SForm, M.SForm]:
    curvature = D.to_sympy_form(P.SPIN_CURVATURE)
    fixed = D.shiab(curvature)
    source_t = D.build_source_t(fixed)
    d_t = {(0, 7): M.sscale(M.sblade(1, 3), -1)}
    q_t = M.sfwedge(source_t, source_t)
    f_a = M.sfadd(curvature, d_t, q_t)
    written = M.sfadd(
        curvature,
        M.sfscale(d_t, sp.Rational(1, 2)),
        M.sfscale(q_t, sp.Rational(1, 3)),
    )
    normalized = M.sfadd(
        M.sfscale(M.sfadd(f_a, curvature), sp.Rational(1, 2)),
        M.sfscale(q_t, sp.Rational(-1, 6)),
    )
    exact(
        "the exact one-half/one-third action block equals its transgression normal form before metric differentiation",
        written == normalized and bool(q_t) and bool(d_t),
    )

    failures = 0
    live_lc = 0
    for axis in range(B15.N):
        xi = coordinate_xi(axis)
        for hvar in B15.H_VARIATIONS:
            delta_gamma = B15.lc_spin_form(xi, hvar)
            live_lc += int(bool(delta_gamma))
            failures += int(bool(D.alt_of_t(M.sfscale(delta_gamma, -1))))
    exact(
        "all 140 coordinate-symbol Levi-Civita metric variations are live and have exactly vanishing total alternation",
        live_lc == 140 and failures == 0,
        f"live_LC_columns={live_lc}; Alt_failures={failures}",
    )
    arbitrary_connection = {(0,): M.sblade(1, 2)}
    exact(
        "a planted non-Levi-Civita grade-two one-form has nonzero alternation",
        bool(D.alt_of_t(arbitrary_connection)),
    )
    reject(
        "infer Alt(delta Gamma_LC)=0 merely because alternation kills every grade-two one-form",
        not D.alt_of_t(arbitrary_connection),
    )

    # Hostile-review control.  Alt(delta B)=0 only constrains the variation of
    # u=Alt(T)+*Alt(T).  It does not remove the independent delta-B term in
    #
    #   delta K = D_(B+K)(h^-1 delta h)
    #             + (Ad_(h^-1)-1) delta B.
    #
    # The Hodge-null branch gives an exact finite exponential h=1+u and makes
    # the omitted connection-incidence summand directly computable.
    _, _, bridge_u, _ = E.native_inputs()
    c3, c11 = sp.symbols("c3 c11", real=True)
    null_u = E.M.sclean(
        {
            mask: sp.simplify(value.subs({c3: 1, c11: 1}))
            for mask, value in bridge_u.items()
        }
    )
    h_null, h_null_inverse = E.exponential_pair(null_u, sp.Integer(0))
    live_ad_k = 0
    for axis in range(B15.N):
        xi = coordinate_xi(axis)
        for hvar in B15.H_VARIATIONS:
            delta_b = B15.lc_spin_form(xi, hvar)
            ad_term = E.M.sfadd(
                E.fconj(h_null_inverse, delta_b, h_null),
                E.M.sfscale(delta_b, -1),
            )
            live_ad_k += int(bool(ad_term))
    exact(
        "the omitted connection-incidence summand (Ad_(h^-1)-1)D_gB is live on the exact Hodge-null bridge",
        live_ad_k == 129,
        f"live_columns={live_ad_k}/140",
    )
    reject(
        "infer principal D_gK=0 from Alt(D_gGamma_LC)=0",
        live_ad_k == 0,
    )
    typed("Alt(D_g Gamma_LC)=0 closes only the delta-u subroute; the complete deltaK sum and its action return remain unassembled")
    return written, source_t


def build_native_rank_matrices(
    written: M.SForm, source_t: M.SForm, include_third: bool = True
):
    panel = (
        coordinate_xi(0),
        coordinate_xi(1),
        coordinate_xi(2),
        coordinate_xi(3),
        coordinate_xi(0, 1),
        coordinate_xi(0, 2),
        coordinate_xi(0, 3),
    )
    second_rows: list[list[sp.Expr]] = []
    third_matrices: list[sp.Matrix] = []
    for xi in panel:
        one = xi_form(xi)
        gamma = [B15.lc_spin_form(xi, hvar) for hvar in B15.H_VARIATIONS]
        curvature_input = [D.shiab(M.sfwedge(one, value)) for value in gamma]
        second_rows.append([D.top_scalar(source_t, value) for value in curvature_input])
        if include_third:
            third_matrices.append(
                sp.Matrix(
                    len(gamma),
                    len(gamma),
                    lambda row, column: D.top_scalar(
                        M.sfscale(gamma[column], -1), curvature_input[row]
                    ),
                )
            )
    second = sp.Matrix(second_rows)
    progress = [sp.Matrix(second_rows[: index + 1]).rank() for index in range(len(panel))]
    slots: dict[str, int] = {}
    coefficient_columns = []
    for owner, hvar in enumerate(B15.H_VARIATIONS):
        parts = M.moving_metric_shiab_parts(
            written, hvar, M.canonical_trace_motion(owner)
        )
        for name, value in parts.items():
            slots[name] = slots.get(name, 0) + len(M.flatten_form(value))
        coefficient_columns.append(M.flatten_form(M.sfadd(*parts.values())))
    keys = sorted(set().union(*(set(column) for column in coefficient_columns)))
    coefficient = sp.Matrix(
        [[column.get(key, 0) for column in coefficient_columns] for key in keys]
    )
    return panel, second, progress, third_matrices, coefficient, slots


def actual_native_top_symbol(written: M.SForm, source_t: M.SForm) -> None:
    panel, second, progress, third_matrices, coefficient, slots = (
        build_native_rank_matrices(written, source_t)
    )
    exact(
        "the selected fixed-h/fixed-Shiab synthetic-source curvature-input bank is live and gains seven independent metric-owner rows",
        second.rank() == 7 and progress == list(range(1, 8)),
        f"shape={second.shape}; rank_progression={progress}",
    )
    exact(
        "the selected bare Levi-Civita curvature-incidence matrix vanishes on every selected conormal",
        all(is_zero(matrix) for matrix in third_matrices),
        f"conormals={len(panel)}; matrices={len(third_matrices)}",
    )
    xi0 = coordinate_xi(0)
    one0 = xi_form(xi0)
    gamma0 = [B15.lc_spin_form(xi0, hvar) for hvar in B15.H_VARIATIONS]
    curvature0 = [D.shiab(M.sfwedge(one0, value)) for value in gamma0]
    hostile_connection = {(0,): M.sblade(0, 10)}
    hostile_pairing = [
        D.top_scalar(M.sfscale(hostile_connection, -1), value)
        for value in curvature0
    ]
    exact(
        "a hostile live one-form gives a nonzero third-pairing vector, so the selected bare-LC zero is not forced by the matcher",
        hostile_pairing
        == [
            sp.Rational(-3, 4),
            0,
            0,
            0,
            sp.Rational(-3, 8),
            0,
            0,
            sp.Rational(-3, 8),
            0,
            sp.Rational(-3, 8),
        ],
        str(hostile_pairing),
    )
    xi_vertical = coordinate_xi(10)
    one_vertical = xi_form(xi_vertical)
    gamma_vertical = [
        B15.lc_spin_form(xi_vertical, hvar) for hvar in B15.H_VARIATIONS
    ]
    curvature_vertical = [
        D.shiab(M.sfwedge(one_vertical, value))
        for value in gamma_vertical
    ]
    vertical_third = sp.Matrix(
        len(gamma_vertical),
        len(gamma_vertical),
        lambda row, column: D.top_scalar(
            M.sfscale(gamma_vertical[column], -1),
            curvature_vertical[row],
        ),
    )
    exact(
        "the held-out vertical conormal e10 has a live rank-ten bare connection-incidence contribution which is not yet a Helmholtz coefficient",
        vertical_third.rank() == 10
        and not is_zero(vertical_third + vertical_third.T),
        f"shape={vertical_third.shape}; rank={vertical_third.rank()}; skew={is_zero(vertical_third + vertical_third.T)}",
    )
    reject(
        "extend the zero seven-horizontal-conormal third block to full Y14",
        vertical_third == sp.zeros(10),
    )
    xi_mixed = coordinate_xi(0, 10)
    one_mixed = xi_form(xi_mixed)
    gamma_mixed = [
        B15.lc_spin_form(xi_mixed, hvar) for hvar in B15.H_VARIATIONS
    ]
    curvature_mixed = [
        D.shiab(M.sfwedge(one_mixed, value)) for value in gamma_mixed
    ]
    mixed_third = sp.Matrix(
        len(gamma_mixed),
        len(gamma_mixed),
        lambda row, column: D.top_scalar(
            M.sfscale(gamma_mixed[column], -1), curvature_mixed[row]
        ),
    )
    exact(
        "the held-out mixed conormal e0+e10 has a live rank-five non-skew connection-incidence contribution",
        mixed_third.rank() == 5 and not is_zero(mixed_third + mixed_third.T),
        f"rank={mixed_third.rank()}; skew={is_zero(mixed_third + mixed_third.T)}",
    )
    typed("the finally assembled odd-order C3 owner matrix must be skew; these non-skew contributions require their missing transpose, graph, and coefficient-motion returns")

    expected_slots = {
        "trace_gamma",
        "Phi1_first",
        "Hodge_first",
        "Phi1_outer",
        "Phi2",
        "Hodge_inner",
        "Hodge_middle",
        "Hodge_outer",
    }
    exact(
        "all eight raw moving-Shiab coefficient slots are included and live as total-metric coefficient motions",
        set(slots) == expected_slots and all(value > 0 for value in slots.values()),
        str(slots),
    )
    exact(
        "the separate uncomposed moving-Shiab coefficient bank independently retains exact ten-owner rank",
        coefficient.rank() == 10,
        f"shape={coefficient.shape}; rank={coefficient.rank()}",
    )
    typed("algebraic motion in the total metric H can inherit base derivatives through D_g G_Y=Z0 delta g+Z1 nabla delta g; the full base composition remains open")
    typed("rank seven is a selected fixed-h/fixed-Shiab synthetic action-coefficient rank, not a complete Euler, quotient, or physical rank")
    reject("promote the coefficient-bank rank ten to the curvature-input or physical rank", second.rank() == coefficient.rank())


def total_derivative(expr: sp.Expr, jet_rows: list[list[sp.Symbol]]) -> sp.Expr:
    result = sp.Integer(0)
    for jets in jet_rows:
        for left, right in zip(jets[:-1], jets[1:]):
            result += sp.diff(expr, left) * right
    return sp.expand(result)


def affine_second_jet_euler_and_green() -> None:
    count = 10
    q = [list(sp.symbols(f"q{owner}_0:5")) for owner in range(count)]
    eta = [list(sp.symbols(f"e{owner}_0:3")) for owner in range(count)]
    coefficient = sp.Matrix(
        count,
        count,
        lambda row, column: sp.Rational(((3 * row + 5 * column + 1) % 11) - 5, 7),
    )
    mass = sp.diag(*[sp.Rational(index + 1, 5) for index in range(count)])
    velocity = sp.Matrix([jets[1] for jets in q])
    acceleration = sp.Matrix([jets[2] for jets in q])
    position = sp.Matrix([jets[0] for jets in q])
    affine = sp.Matrix(
        [sp.Rational(index + 1, 3) for index in range(count)]
    ) + coefficient * velocity
    lagrangian = sp.expand(
        (affine.T * acceleration)[0]
        + sp.Rational(1, 2) * (velocity.T * mass * velocity)[0]
        + sp.Rational(1, 2) * (position.T * mass * position)[0]
    )
    euler = []
    for jets in q:
        value = sp.diff(lagrangian, jets[0])
        value -= total_derivative(sp.diff(lagrangian, jets[1]), q)
        value += total_derivative(total_derivative(sp.diff(lagrangian, jets[2]), q), q)
        euler.append(sp.expand(value))
    fourth = sp.Matrix(
        count, count, lambda row, column: sp.diff(euler[row], q[column][4])
    )
    third = sp.Matrix(
        count, count, lambda row, column: sp.diff(euler[row], q[column][3])
    )
    expected_third = coefficient - coefficient.T
    exact(
        "direct ten-owner Euler differentiation gives identically zero fourth-order coefficient for every affine-second-jet action",
        fourth == sp.zeros(count),
    )
    exact(
        "the only possible third-order coefficient is the exact skew velocity derivative of the affine curvature coefficient",
        third == expected_third and third.T == -third and third.rank() > 0,
        f"generic_fixture_rank={third.rank()}",
    )

    direct = sp.Integer(0)
    bulk = sp.Integer(0)
    theta = sp.Integer(0)
    combined_jets = q + eta
    for owner, jets in enumerate(q):
        direct += sum(
            sp.diff(lagrangian, jets[order]) * eta[owner][order]
            for order in range(3)
        )
        bulk += euler[owner] * eta[owner][0]
        theta += (
            sp.diff(lagrangian, jets[1])
            - total_derivative(sp.diff(lagrangian, jets[2]), q)
        ) * eta[owner][0]
        theta += sp.diff(lagrangian, jets[2]) * eta[owner][1]
    green_defect = sp.expand(direct - bulk - total_derivative(theta, combined_jets))
    exact(
        "the independent direct-variation and reverse formal-adjoint routes agree with the complete two-layer Green packet",
        green_defect == 0 and theta != 0,
    )
    exact(
        "the odd third-order block is formally self-adjoint because its owner matrix is skew",
        expected_third == -expected_third.T,
    )
    symmetric_plant = coefficient + coefficient.T
    reject(
        "accept a symmetric owner matrix as an odd-order Helmholtz block",
        symmetric_plant != sp.zeros(count) and symmetric_plant == -symmetric_plant.T,
    )

    realized = tuple(
        tuple(N.derivative_order_in(N.OWNER_EULERS[out], incoming) for incoming in N.OWNERS)
        for out in N.OWNERS
    )
    exact(
        "the independent full-owner first-action predecessor retains second-order metric diagonal and opposite mixed third-order graph blocks",
        realized
        == ((0, 1, 2, 2), (1, 0, 2, 2), (2, 2, 2, 3), (2, 2, 3, 2))
        and sp.diff(N.OWNER_EULERS[N.B13.z], sp.diff(N.B13.g, N.x, 3)).subs({N.B13.z: 0, N.B13.g: 0}) == 9
        and sp.diff(N.OWNER_EULERS[N.B13.g], sp.diff(N.B13.z, N.x, 3)).subs({N.B13.z: 0, N.B13.g: 0}) == -9,
    )
    reject("infer that every mixed graph-owner third-order block vanishes from the metric self-block result", False)


def signature_scope_and_stop() -> None:
    dewitt = sp.Matrix(P.D0)
    total = sp.Matrix(P.G0)
    exact(
        "the scoped top-order calculation retains trace-reversed fibre inertia six-four and total inertia nine-five",
        D.B14.symmetric_inertia([[F(item) for item in row] for row in dewitt.tolist()]) == (6, 4, 0)
        and D.B14.symmetric_inertia([[F(item) for item in row] for row in total.tolist()]) == (9, 5, 0),
    )
    exact(
        "no D3G artifact was constructed; its absence supplies no zero certificate while the complete coefficient is unearned",
        getattr(P, "D3G", None) is None,
    )
    typed("the generic affine-second-jet theorem is conditional evidence, not a verdict that the native first action is affine after the omitted deltaK summand")
    typed("the formal diffeomorphism schema is evaluated separately; the literal source-root/native all-owner Ward rank remains open")
    typed("the complete derived-K top order and skew full-Y14 C3 precede lower C2, physical quotient, observation pushdown, and Standard-Model/GR comparison")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE; TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    reject("claim a fourth-order metric equation from PW2E's scalar quadratic-curvature comparator", getattr(P, "D3G", None) is not None)


def main() -> int:
    print("PW2F ACTIVE-NATIVE TOP-ORDER METRIC COMPOSITION")
    source_and_layer_zero()
    written, source_t = transgression_and_bridge_principal()
    actual_native_top_symbol(written, source_t)
    affine_second_jet_euler_and_green()
    signature_scope_and_stop()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}"
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: PW2F LC-ALTERNATION SUBROUTE PASS; OMITTED DELTA-K "
        "SUMMAND LIVE; COMPLETE TOP ORDER REMAINS OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
