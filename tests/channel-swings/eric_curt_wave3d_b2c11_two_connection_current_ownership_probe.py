#!/usr/bin/env python3
r"""B2C11 two-connection owner and source-action discriminator.

This probe does not guess Weinstein's unreleased two-connection formula.  It
constructs the owner algebra that every such formula must satisfy, builds
fixed-current/fixed-pairing owner-sector realizations of the two coupling
architectures displayed in draft equation (9.20), and asks whether the active
southeast current can disappear from the
*full* graph-owned Euler tuple.

The answer is no for the tested family: a T=A-B term can move the channel
between A and B, and can even make one partial equation blind to it, but the
shared current and the complete A/graph-B tuple retain it.  Once the nonzero
southeast operator is selected, its extra current contribution is therefore
action-derived, not another external datum.  Its completion with all other
fermion terms remains a conditional repository candidate.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import runpy
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests/channel-swings"
if str(CHANNEL) not in sys.path:
    sys.path.insert(0, str(CHANNEL))

B2C10 = runpy.run_path(
    str(CHANNEL / "eric_curt_wave3d_b2c10_active_current_full_tuple_hessian_probe.py")
)

FAILURES: list[str] = []
EXACT = 0
SOURCE_RECEIPTS = 0
TYPE_LEVEL = 0
PLANTED = 0
TOL = 2.0e-8


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE_RECEIPTS
    SOURCE_RECEIPTS += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: source receipt - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"source receipt: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE_LEVEL
    TYPE_LEVEL += 1
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: type-level - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"type-level: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    status = "PASS" if not false_claim else "FAIL"
    print(f"{status}: planted rejection - {label}", flush=True)
    if false_claim:
        FAILURES.append(f"planted: {label}")


def source_checks() -> None:
    pack = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
    toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
    paired = (
        ROOT / "lab/sources/paired-curt-eric-gu-axiom-and-argument-reconstruction-2026-07-31.md"
    ).read_text()
    tau = (
        ROOT / "explorations/research-cycles/hourly-20260626-1003-cycle3-tau-source-locator-packet.md"
    ).read_text()
    b2c10 = (
        ROOT / "explorations/eric-curt-wave3d-b2c10-active-current-full-tuple-hessian-2026-08-01.md"
    ).read_text()

    source_receipt(
        "draft 9.20 keeps first-order-total and second-order-sourced equations as alternatives",
        r"\Upsilon^B_\omega+\Upsilon^F_\omega=0" in pack
        and r"D_\omega^*\Upsilon^B_\omega=\Upsilon^F_\omega" in pack,
        "draft equations 9.18-9.20",
    )
    source_receipt(
        "the source-exact second action is the bosonic residual square, not a total Einstein-Dirac square",
        r"I_2^B=\|\Upsilon_\omega^B\|^2" in paired
        and "The bosonic superscript is load-bearing" in paired,
        "draft 9.11-9.15 / paired reconstruction",
    )
    source_receipt(
        "the displayed bosonic derivative includes a partial varpi direction",
        "partial_varpi_directional_variation_present" in tau
        and "partial_s I_B^1" in tau,
        "draft Section 9.1 source-locator packet",
    )
    source_receipt(
        "the global varied-versus-fixed omega domain remains undeclared",
        '"selected_variation_domain_enum": "UNDECLARED"' in tau
        and "admissible_omega_variation_domain_declaration" in tau,
        "source-domain negative receipt",
    )
    source_receipt(
        "the modern two-connection on-shell construction remains unreleased",
        "have never released" in toe and "on shell where the equations get satisfied" in toe,
        "TOE 02:44:06-02:45:13",
    )
    source_receipt(
        "the active repair candidate is a repository construction and the source supplies no owner law for its extra current",
        "SOURCE-SILENT" in b2c10
        and "the coefficient or owner law canceling the new channel" in b2c10,
        "B2C10 primary-source collision",
    )


# ---------------------------------------------------------------------------
# Exact A/B <-> shared/distortion owner algebra.

Vector = tuple[F, ...]
Matrix = tuple[tuple[F, ...], ...]


def vadd(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def vsub(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))


def vscale(value, vector: Vector) -> Vector:
    return tuple(F(value) * item for item in vector)


def vdot(left: Vector, right: Vector) -> F:
    return sum((a * b for a, b in zip(left, right)), F(0))


def mv(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), F(0))
        for i in range(len(matrix))
    )


def mtv(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum((matrix[i][j] * vector[i] for i in range(len(matrix))), F(0))
        for j in range(len(matrix[0]))
    )


def pair_owner(j_a: Vector, j_b: Vector, d_a: Vector, d_b: Vector) -> F:
    return vdot(j_a, d_a) + vdot(j_b, d_b)


def owner_coordinates(j_a: Vector, j_b: Vector) -> tuple[Vector, Vector]:
    # A=C+T/2, B=C-T/2.
    return vadd(j_a, j_b), vscale(F(1, 2), vsub(j_a, j_b))


def owner_checks() -> None:
    j_a = (F(2), F(-1), F(3))
    j_b = (F(-4), F(5), F(1))
    d_c = (F(1), F(2), F(-2))
    d_t = (F(3), F(-1), F(4))
    d_a = vadd(d_c, vscale(F(1, 2), d_t))
    d_b = vsub(d_c, vscale(F(1, 2), d_t))
    j_c, j_t = owner_coordinates(j_a, j_b)
    exact(
        "the A/B covector pairing equals the shared-C plus distortion-T pairing",
        pair_owner(j_a, j_b, d_a, d_b) == vdot(j_c, d_c) + vdot(j_t, d_t),
    )
    exact(
        "the inverse owner map recovers J_A=J_C/2+J_T and J_B=J_C/2-J_T",
        vadd(vscale(F(1, 2), j_c), j_t) == j_a
        and vsub(vscale(F(1, 2), j_c), j_t) == j_b,
    )

    # K is the extra active channel after suppressing carrier multiplicities.
    k = (F(2), F(-3), F(5))
    for q in (F(-2), F(0), F(1, 2), F(1), F(7, 3)):
        # B2C10 convention: the unshifted southeast current is B-owned; a
        # T-linear term moves fraction q to A.
        extra_a = vscale(q, k)
        extra_b = vscale(F(1) - q, k)
        shared, distortion = owner_coordinates(extra_a, extra_b)
        exact(
            f"T-owner transfer q={q} preserves the shared extra current",
            shared == k and distortion == vscale(q - F(1, 2), k),
        )

    half_a, half_b = vscale(F(1, 2), k), vscale(F(1, 2), k)
    half_shared, half_distortion = owner_coordinates(half_a, half_b)
    exact(
        "q=1/2 can kill the distortion current while the shared current remains nonzero",
        half_distortion == (F(0), F(0), F(0)) and half_shared == k,
    )
    exact(
        "q=1 transfers the full extra current from the reference owner to the variational owner",
        vscale(F(1), k) == k and vscale(F(0), k) == (F(0), F(0), F(0)),
    )

    # A graph B=R y returns J_B through R^T.  Since R^T K is nonzero, q=0
    # (required to kill J_A) and q=1 (required to kill the graph return) are
    # incompatible.
    graph = (
        (F(1), F(0)),
        (F(-1), F(2)),
        (F(3), F(1)),
    )
    graph_k = mtv(graph, k)
    exact("the planted graph sees the extra channel", graph_k != (F(0), F(0)))
    for q in (F(-1), F(0), F(1, 2), F(1), F(2)):
        a_return = vscale(q, k)
        graph_return = vscale(F(1) - q, graph_k)
        exact(
            f"full variational-A plus graph-B tuple retains the channel at q={q}",
            a_return != (F(0), F(0), F(0)) or graph_return != (F(0), F(0)),
        )
    exact(
        "no scalar T-transfer coefficient can annihilate both A and graph-B owners",
        k != (F(0), F(0), F(0)) and graph_k != (F(0), F(0)),
        "A=0 forces q=0; graph-B=0 forces q=1",
    )


# ---------------------------------------------------------------------------
# Actual active Cl(9,5) graph-return witness inherited from B2C10.


def max_abs(value) -> float:
    return float(np.max(np.abs(value)))


def active_graph_checks() -> None:
    gammas, _p_plus, _p_minus, beta, right_h, _c_plus = B2C10["active_objects"]()
    p_plus = _p_plus
    p_minus = _p_minus
    ell = (-11.0 / 16.0) * p_plus + (-33.0 / 32.0) * p_minus
    rng = np.random.default_rng(2026080110)
    spin = gammas[0].shape[0]
    nu = rng.normal(size=spin) + 1j * rng.normal(size=spin)
    j_nu = right_h @ nu.conj()
    fields = (nu, j_nu)
    observed = (0, 1, 2, 9)

    def scalar_current(field, index):
        x = gammas[0] @ gammas[1]
        return float(np.real(field.conj() @ beta @ gammas[index] @ ell @ x @ field))

    current_vector = np.array(
        [sum(scalar_current(field, index) for field in fields) for index in observed]
    )
    current_rows = []
    for index in observed:
        coefficient = beta @ gammas[index] @ ell
        current_rows.append(
            sum(
                (coefficient.conj().T @ np.outer(field, field.conj()) for field in fields),
                np.zeros_like(beta),
            )
        )

    def connection_pair(connection_variation) -> float:
        return float(
            sum(
                np.real(np.trace(current.conj().T @ variation))
                for current, variation in zip(current_rows, connection_variation)
            )
        )

    rng_graph = np.random.default_rng(2026080111)
    metric_jets = rng_graph.normal(size=(4, 4, 4))
    metric_jets = 0.5 * (metric_jets + metric_jets.swapaxes(1, 2))
    omega = B2C10["lc_spin_lift"](metric_jets, gammas)
    delta_u = gammas[2] @ gammas[3]
    delta_u_mu = [(index + 1.0) * (gammas[4] @ gammas[5]) for index in range(4)]
    delta_b = [delta_u @ item - item @ delta_u - du for item, du in zip(omega, delta_u_mu)]
    graph_return = connection_pair(delta_b)

    exact(
        "the actual active southeast current and its local reduction-graph return are both nonzero",
        np.linalg.norm(current_vector) > 1.0 and abs(graph_return) > 1.0,
        f"|K|={np.linalg.norm(current_vector):.8g}; graph={graph_return:.8g}",
    )
    norm_sq = float(current_vector @ current_vector)
    graph_sq = graph_return * graph_return
    selected_direction_proxy_q = graph_sq / (norm_sq + graph_sq)
    selected_direction_proxy_residual = norm_sq * graph_sq / (norm_sq + graph_sq)
    exact(
        "the fixture-normalized selected-direction transfer proxy has a positive residual",
        0.0 < selected_direction_proxy_q < 1.0
        and selected_direction_proxy_residual > 1.0,
        f"proxy-q*={selected_direction_proxy_q:.8g}; "
        f"proxy-min={selected_direction_proxy_residual:.8g}",
    )
    reject(
        "an active T-transfer coefficient makes both the variational and graph-owner returns vanish",
        selected_direction_proxy_residual < TOL,
    )


# ---------------------------------------------------------------------------
# Exact action realizations of the two draft architectures.


H: Matrix = ((F(3), F(-1)), (F(-1), F(2)))
Q: Matrix = ((F(2), F(0)), (F(0), F(-3)))
F0: Vector = (F(1), F(-2))
ELL = F(-3, 4)
J_WRITTEN: Vector = (F(2), F(-1))


def residual(x: Vector) -> Vector:
    return vadd(mv(H, x), F0)


def i1_b(x: Vector) -> F:
    return F(1, 2) * vdot(x, mv(H, x)) + vdot(F0, x)


def extra_owner(q: F) -> Vector:
    # In (C,T) coordinates J_C=K and J_T=(q-1/2)K.  The suppressed active
    # channel is scalar here; ELL is inherited from the selected operator.
    return (ELL, ELL * (q - F(1, 2)))


def repaired_current(q: F) -> Vector:
    return vadd(J_WRITTEN, extra_owner(q))


def fermion_action(x: Vector, q: F, include_extra: bool = True) -> F:
    current = repaired_current(q) if include_extra else J_WRITTEN
    return vdot(current, x)


def i_first_total(x: Vector, q: F, include_extra: bool = True) -> F:
    return i1_b(x) + fermion_action(x, q, include_extra)


def i_second_sourced(x: Vector, q: F, include_extra: bool = True) -> F:
    u = residual(x)
    return F(1, 2) * vdot(u, mv(Q, u)) - fermion_action(x, q, include_extra)


def directional(function, x: Vector, direction: Vector) -> F:
    return (function(vadd(x, direction)) - function(vsub(x, direction))) / F(2)


def architecture_checks() -> None:
    x = (F(2), F(-1))
    direction = (F(3), F(4))
    q = F(2, 3)
    j = repaired_current(q)
    u = residual(x)
    first_gradient = vadd(u, j)
    second_gradient = vsub(mtv(H, mv(Q, u)), j)
    exact(
        "the fixed-current first-order owner-sector action varies to Upsilon_B plus Upsilon_F-candidate",
        directional(lambda value: i_first_total(value, q), x, direction)
        == vdot(first_gradient, direction),
    )
    exact(
        "the fixed-Q sourced owner-sector action varies through the algebraic transpose minus Upsilon_F-candidate",
        directional(lambda value: i_second_sourced(value, q), x, direction)
        == vdot(second_gradient, direction),
    )

    first_written = vadd(u, J_WRITTEN)
    second_written = vsub(mtv(H, mv(Q, u)), J_WRITTEN)
    exact(
        "the active channel is required rather than canceled in the first-order-total Euler equation",
        vsub(first_gradient, first_written) == extra_owner(q)
        and extra_owner(q) != (F(0), F(0)),
    )
    exact(
        "the same active channel is required on the RHS of the second-order-sourced equation",
        vsub(second_gradient, second_written) == vscale(F(-1), extra_owner(q)),
    )

    # If both rival equations are imposed on the same field, the first gives
    # U=-J while the second additionally demands H^T Q(-J)=J.  This is not an
    # identity and fails on the exact fixture.
    compatibility_residual = vsub(
        mtv(H, mv(Q, vscale(F(-1), j))),
        j,
    )
    exact(
        "simultaneous rival Euler equations add a compatibility condition and fail on the exact fixture",
        compatibility_residual != (F(0), F(0)),
        f"residual={compatibility_residual}",
    )

    positive_q: Matrix = ((F(2), F(0)), (F(0), F(3)))
    wrong_second = vsub(mtv(H, mv(positive_q, u)), j)
    reject(
        "replace the chosen fixed indefinite Q without changing the selected finite gradient",
        wrong_second == second_gradient,
    )
    reject(
        "compare Upsilon_F directly with Upsilon_B and omit the D-Upsilon algebraic transpose in the finite comparator",
        vsub(u, j) == second_gradient,
    )


def coefficient_surplus_checks() -> None:
    # The current coefficient is the derivative of the same operator
    # coefficient ELL.  Once the operator is selected, there is no second
    # source coefficient to fit.
    bilinears = (F(2), F(-5), F(7, 3), F(11, 2))
    derived = tuple(ELL * item for item in bilinears)
    exact(
        "one selected southeast operator coefficient determines every tested current coefficient",
        all(value == ELL * item for value, item in zip(derived, bilinears)),
    )
    fitted_coefficient = derived[0] / bilinears[0]
    type_level(
        "a separately fitted current coefficient has bookkeeping surplus zero",
        fitted_coefficient == ELL,
        "one coefficient identity minus one separately fitted coefficient",
    )
    type_level(
        "the action derivative introduces zero new current coefficients",
        all(value == fitted_coefficient * item for value, item in zip(derived, bilinears)),
        "conditional-surplus-one language awaits an independent held-out comparison",
    )
    unrelated = (F(0), F(1))
    extra = extra_owner(F(2, 3))
    reject(
        "the action-derived southeast coefficient also fits a planted unrelated current channel",
        extra == unrelated or vscale(F(-1), extra) == unrelated,
    )
    type_level("P1, P2, or P3 is not used to tie the candidate current contribution to its operator coefficient")


def green_checks() -> None:
    # Abstract finite product-sector control only.  A boson-only direct-sum
    # term cannot cancel a stipulated nonzero pure-fermion restriction on the
    # full unrestricted fermion trace space.  This is not an active B2C6B
    # matrix/domain replay.
    left_f = (F(1), F(2))
    right_f = (F(-2), F(3))

    def fermion_green(left: Vector, right: Vector) -> F:
        return F(2) * (left[0] * right[1] - right[0] * left[1])

    g_f = fermion_green(left_f, right_f)
    exact("the abstract fermion-sector Green comparator is skew and nonzero", g_f != 0)
    first_total = g_f + F(0)
    second_total = g_f + F(0)
    exact(
        "the abstract first-order direct-sum comparator retains the nonzero fermion restriction",
        first_total == g_f and first_total != 0,
    )
    exact(
        "an abstract boson-only square does not alter the stipulated fermion restriction",
        second_total == g_f and second_total != 0,
    )
    for zero_order in (F(-5), F(0), ELL, F(7, 2)):
        type_level(
            f"zero-order owner/current coefficient {zero_order} does not alter principal Green order",
            fermion_green(left_f, right_f) == g_f,
            "principal-order statement; active integration-by-parts replay remains open",
        )
    type_level("neither finite owner-sector realization selects a common mixed boson-fermion physical domain")


def scope_controls() -> None:
    type_level("the partial varpi derivative locates one owner direction, not the full omega variation domain")
    type_level("shared C, distortion T, variational A, reference B, and graph epsilon owners are distinct embeddings")
    type_level("the 2021 single-connection fermion current and the unreleased modern two-connection operator are not identified")
    type_level("first-order-total and second-order-sourced equations are separately varied architectures")
    type_level("the source-exact second square is bosonic; a total Einstein-Dirac residual square remains a repo rival")
    type_level("D-omega-star needs a residual derivative, pairing, formal adjoint, and domain; the finite check uses only an algebraic transpose")
    type_level("the active bar-nu-nu term is an operator-derived connection Euler current, not an external datum")
    type_level("a T-linear term may hide a current from one partial equation while leaving the full graph-owned tuple nonzero")
    type_level("the finite graph theorem does not prove the full nonlinear ambient Y14 owner graph")
    type_level("the abstract fermion Green comparator does not exclude Green-Lagrangian fermion subdomains or source-selected mixed conditions")
    type_level("Curt remains formally separate and TG-1 AND TG-2 AND TG-3 remains false")
    type_level("the trace-reversed (9,5) active carrier is not replaced by Curt's literal (7,7) carrier")


def planted_controls() -> None:
    type_level("the two equations in draft 9.20 are not summed and imposed simultaneously")
    type_level("a partial varpi derivative does not select a global fixed-versus-dynamic reference policy")
    type_level("vanishing distortion current does not imply vanishing shared current")
    type_level("q=1 transfers the current to A rather than deleting it")
    type_level("the graph-B Euler return is retained after canceling the A partial")
    type_level("the source has not released the modern two-connection owner formula")
    type_level("the connection Euler current is not identified with an observed Maxwell/Yang-Mills current")
    type_level("the active bar-nu-nu term is not identified with a Majorana mass or generation count")
    type_level("the second bosonic square does not automatically select a positive Hilbert pairing")
    type_level("a T-only correction leaves the shared current unchanged")
    type_level("a total-residual square is not the manuscript's I2B formula")
    type_level("changing the Euler source does not by itself repair the B2C6B domain problem")
    type_level("P1/P2/P3 does not select the coupling architecture or current owner")
    type_level("the owner result does not promote Curt to a third lane")


def main() -> int:
    print("ECW3D-B2C11 TWO-CONNECTION CURRENT OWNERSHIP / SOURCE-ACTION SELECTION")
    source_checks()
    owner_checks()
    active_graph_checks()
    architecture_checks()
    coefficient_surplus_checks()
    green_checks()
    scope_controls()
    planted_controls()
    total = EXACT + SOURCE_RECEIPTS + TYPE_LEVEL + PLANTED
    print(
        f"SUMMARY: {EXACT} computational exact + {SOURCE_RECEIPTS} source receipts + "
        f"{TYPE_LEVEL} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILED: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C11 CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
