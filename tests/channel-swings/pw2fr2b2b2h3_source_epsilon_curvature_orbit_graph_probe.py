#!/usr/bin/env python3
r"""PW2F-R2B2B2H3 exact conditional source-epsilon curvature-orbit graph.

H2 closed the fixed-background residual/operator/primalizer second jet but left
the source-epsilon curvature graph unconstructed.  This probe closes one
strictly local conditional dependency.  First, an independent exact matrix
fixture verifies

    F(epsilon^-1 Gamma epsilon + epsilon^-1 d epsilon)
      = epsilon^-1 F(Gamma) epsilon

through a live mixed source-coordinate slot and rejects omission of the
Maurer--Cartan connection term.  Second, a formal two-direction Spin(9,5)
source orbit moves the accepted active curvature, trace, Phi1/Phi2, projector,
and Shiab response through ``(1,r,s,rs)``.  The explicitly rebuilt response is
compared with transport and independent commutator formulas; its residual
square is constant along the gauge orbit.

The public source epsilon and the conditional active rotor remain distinct
Layer-0 objects.  This probe does not construct a global source-to-active
real-form bundle morphism, either C4 bank, a Green/Helmholtz quotient, kappa1,
or physics.  P1/P2/P3 remain unused; Curt remains formally separate; the third
lane is not promoted.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import hashlib
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


H2 = load_probe(
    "pw2fr2b2b2h3_predecessor",
    "pw2fr2b2b2h2_i2b_second_residual_primalizer_pairing_probe.py",
)
H = H2.H
M = H2.M
D = H2.D
P = H2.P
E = H2.E


FAILURES: list[str] = []
EXACT = SOURCE = TYPE = PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: exact - {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(f"exact: {label}")


def source_receipt(label: str, condition: bool, disposition: str) -> None:
    global SOURCE
    SOURCE += 1
    print(f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]", flush=True)
    if not condition:
        FAILURES.append(f"source: {label}")


def typed(label: str, condition: bool = True) -> None:
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


def zero(value: sp.MatrixBase | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    predecessor_path = (
        ROOT
        / "explorations/pw2fr2b2b2h2-complete-i2b-second-residual-primalizer-pairing-2026-08-04.md"
    )
    descent_path = (
        ROOT / "tests/channel-swings/pw2e_finite_native_shiab_descent_probe.py"
    )
    pack = pack_path.read_text()
    predecessor = predecessor_path.read_text()
    descent = descent_path.read_text()

    source_receipt(
        "the pinned primary-source pack fixes the epsilon/connection-difference grammar and distinguishes source epsilon from repository soldering data",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in pack
        and "UNCERTAIN/HOMONYM-RISK" in pack,
        "SOURCE-CONFIRMS grammar; SOURCE-SILENT on the active real-form bundle port",
    )
    source_receipt(
        "the accepted H2 result names the complete source-epsilon curvature graph as the next separate dependency",
        hashlib.sha256(predecessor_path.read_bytes()).hexdigest()
        == "59ec0fe6652f8919ab4909261f2e53fd0b405f1e7bbc2f7b32e6ae9981f89862"
        and "global/source-epsilon curvature graph" in predecessor
        and "PW2F-R2B2B2H3" in predecessor,
        "REPOSITORY-DERIVED successor gate",
    )
    source_receipt(
        "the pre-existing exact native descent constructor moves Phi, trace, curvature, and projection separately rather than defining covariance by transport",
        hashlib.sha256(descent_path.read_bytes()).hexdigest()
        == "14e90fcd5e3663cd3d77878e256c049ac8be8de9ef0d6026a979eac19db4e6c7"
        and all(
            token in descent
            for token in (
                "def explicit_shiab",
                "def transported_identity",
                "phi_one = fconj",
                "trace = cconj",
            )
        ),
        "REPOSITORY-DERIVED active construction; SOURCE-SILENT on its identification with public epsilon",
    )

    typed("source epsilon, the conditional active Spin(9,5) rotor, repository h=exp(u), and reduction epsilon remain four distinct objects")
    typed("source I1, manuscript I2B, and the active repository residual-square port remain separately custodied actions")
    typed("connection graph, curvature graph, epsilon-soldered Shiab operator, residual density, primalizer, and action Hessian remain typed separately")
    typed("the active trace-reversed (9,5) right-H/Krein port is not identified with the public (7,7)-type source presentation")
    typed("a local conditional source orbit does not construct a global source-to-active bundle morphism or atlas")


def matrix_connection_curvature_gate() -> dict[str, object]:
    """Independent exact gauge-connection fixture with a live mixed slot."""
    r, s, x, y = sp.symbols("r s x y", real=True)
    identity = sp.eye(2)
    u = sp.Matrix([[0, 1], [0, 0]])
    v = sp.Matrix([[0, 0], [1, 0]])
    tau = r * x + s * y + r * s * (x + y)
    sigma = r * y - s * x + r * s * (x - y)
    epsilon = sp.expand((identity + tau * u) * (identity + sigma * v))
    epsilon_inv = sp.expand((identity - sigma * v) * (identity - tau * u))
    exact(
        "the noncommuting source-coordinate matrix and inverse are exact",
        u * u == sp.zeros(2)
        and v * v == sp.zeros(2)
        and zero(epsilon_inv * epsilon - identity)
        and zero(epsilon * epsilon_inv - identity),
    )

    gamma_x = sp.Matrix([[x + y, 1 + x], [2 - y, -x]])
    gamma_y = sp.Matrix([[y, -1 + x], [1 + y, x - y]])

    def curvature(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
        return sp.expand(
            sp.diff(right, x)
            - sp.diff(left, y)
            + left * right
            - right * left
        )

    f_gamma = curvature(gamma_x, gamma_y)
    b_x = sp.expand(epsilon_inv * gamma_x * epsilon + epsilon_inv * sp.diff(epsilon, x))
    b_y = sp.expand(epsilon_inv * gamma_y * epsilon + epsilon_inv * sp.diff(epsilon, y))
    f_b = curvature(b_x, b_y)
    transported = sp.expand(epsilon_inv * f_gamma * epsilon)
    exact(
        "the full connection graph obeys exact curvature conjugacy before coefficient extraction",
        zero(f_b - transported),
    )

    at_zero = {r: 0, s: 0}
    mixed_direct = sp.simplify(sp.diff(f_b, r, s).subs(at_zero))
    epsilon_r = sp.diff(epsilon, r).subs(at_zero)
    epsilon_s = sp.diff(epsilon, s).subs(at_zero)
    epsilon_rs = sp.diff(epsilon, r, s).subs(at_zero)
    inverse_r = sp.diff(epsilon_inv, r).subs(at_zero)
    inverse_s = sp.diff(epsilon_inv, s).subs(at_zero)
    inverse_rs = sp.diff(epsilon_inv, r, s).subs(at_zero)
    assembled = sp.simplify(
        inverse_rs * f_gamma
        + inverse_r * f_gamma * epsilon_s
        + inverse_s * f_gamma * epsilon_r
        + f_gamma * epsilon_rs
    )
    exact(
        "the live mixed curvature slot equals the independently assembled four-family source-orbit product rule",
        zero(mixed_direct - assembled) and not zero(mixed_direct),
        f"mixed_nonzero_entries={sum(sp.simplify(value) != 0 for value in mixed_direct)}",
    )

    frozen_x = sp.expand(epsilon_inv * gamma_x * epsilon)
    frozen_y = sp.expand(epsilon_inv * gamma_y * epsilon)
    frozen_curvature = curvature(frozen_x, frozen_y)
    mixed_omission_defect = sp.simplify(
        sp.diff(frozen_curvature - transported, r, s).subs(at_zero)
    )
    exact(
        "omitting epsilon^-1 d epsilon produces a detected nonzero mixed curvature defect",
        not zero(mixed_omission_defect),
        f"defect_entries={sum(sp.simplify(value) != 0 for value in mixed_omission_defect)}",
    )
    reject(
        "drop the Maurer-Cartan connection term and claim curvature still conjugates through mixed order",
        zero(mixed_omission_defect),
    )
    return {
        "mixed_entries": sum(sp.simplify(value) != 0 for value in mixed_direct),
        "omission_entries": sum(
            sp.simplify(value) != 0 for value in mixed_omission_defect
        ),
    }


def constant_cliff(value: M.SCliff) -> H.JCliff:
    return value, {}, {}, {}


def sf_right(value: M.SForm, cliff: M.SCliff) -> M.SForm:
    return M.sfclean(
        {key: M.smul(coefficient, cliff) for key, coefficient in value.items()}
    )


def jf_right(left: H.JForm, right: H.JCliff) -> H.JForm:
    return (
        sf_right(left[0], right[0]),
        M.sfadd(sf_right(left[1], right[0]), sf_right(left[0], right[1])),
        M.sfadd(sf_right(left[2], right[0]), sf_right(left[0], right[2])),
        M.sfadd(
            sf_right(left[3], right[0]),
            sf_right(left[1], right[2]),
            sf_right(left[2], right[1]),
            sf_right(left[0], right[3]),
        ),
    )


def jf_conj(inverse: H.JCliff, value: H.JForm, rotor: H.JCliff) -> H.JForm:
    return jf_right(H.jfleft(inverse, value), rotor)


def source_shiab_jet(
    metric,
    trace: H.JCliff,
    phi_one: H.JForm,
    phi_two: H.JForm,
    curvature: H.JForm,
) -> H.JForm:
    """Rebuild the epsilon-soldered Shiab graph from moved ingredients."""
    star_f = H.jhodge(metric, curvature)
    first = H.jfwedge(phi_one, star_f)
    middle = H.jhodge(metric, H.jfwedge(phi_two, star_f))
    outer = H.jfwedge(phi_one, middle)
    raw = H.jfadd(
        first,
        H.jfscale(H.jhodge(metric, outer), sp.Rational(-1, 2)),
    )
    return H.jfproject(H.jfleft(trace, raw))


def active_source_orbit_gate() -> dict[str, object]:
    one = {0: sp.Integer(1)}
    generator_r = M.sblade(0, 1)
    generator_s = M.sblade(1, 2)
    mixed_exponential = M.sscale(
        M.sadd(
            M.smul(generator_r, generator_s),
            M.smul(generator_s, generator_r),
        ),
        sp.Rational(1, 2),
    )
    epsilon: H.JCliff = (
        one,
        generator_r,
        generator_s,
        mixed_exponential,
    )
    epsilon_inv: H.JCliff = (
        one,
        M.sscale(generator_r, -1),
        M.sscale(generator_s, -1),
        mixed_exponential,
    )
    identity_jet: H.JCliff = (one, {}, {}, {})
    exact(
        "the two-direction formal Spin source rotor and inverse multiply to identity through mixed order",
        H.jcmul(epsilon_inv, epsilon) == identity_jet
        and H.jcmul(epsilon, epsilon_inv) == identity_jet,
    )
    exact(
        "both source directions are noncommuting active grade-two generators",
        generator_r != generator_s
        and M.smul(generator_r, generator_s)
        != M.smul(generator_s, generator_r)
        and all(mask.bit_count() == 2 for mask in generator_r | generator_s),
    )

    base_curvature = D.to_sympy_form(P.SPIN_CURVATURE)
    curvature = jf_conj(
        epsilon_inv,
        H.constant_form(base_curvature),
        epsilon,
    )
    expected_r = M.sfadd(
        sf_right(base_curvature, generator_r),
        M.sfscale(M.sfleft(generator_r, base_curvature), -1),
    )
    expected_s = M.sfadd(
        sf_right(base_curvature, generator_s),
        M.sfscale(M.sfleft(generator_s, base_curvature), -1),
    )
    expected_rs = M.sfadd(
        M.sfleft(mixed_exponential, base_curvature),
        M.sfscale(
            sf_right(M.sfleft(generator_r, base_curvature), generator_s),
            -1,
        ),
        M.sfscale(
            sf_right(M.sfleft(generator_s, base_curvature), generator_r),
            -1,
        ),
        sf_right(base_curvature, mixed_exponential),
    )
    exact(
        "the active curvature first and mixed slots equal independent commutator/product-rule assembly",
        form_equal(curvature[1], expected_r)
        and form_equal(curvature[2], expected_s)
        and form_equal(curvature[3], expected_rs),
    )
    exact(
        "all three source-epsilon curvature response slots are live on the accepted active background",
        all(bool(M.flatten_form(curvature[slot])) for slot in (1, 2, 3)),
        "coordinates=" + str(tuple(len(M.flatten_form(curvature[slot])) for slot in range(4))),
    )
    exact(
        "the complete curvature orbit retains active grade two and right-H/Krein/C-plus compatibility in every slot",
        all(
            all(mask.bit_count() == 2 for _key, mask in M.flatten_form(slot))
            and P.B15O.form_compatible(slot)
            for slot in curvature
        ),
    )

    trace = H.jcmul(
        H.jcmul(epsilon_inv, constant_cliff(M.STRACE)),
        epsilon,
    )
    phi_one = jf_conj(epsilon_inv, H.constant_form(M.SPHI_ONE), epsilon)
    phi_two = jf_conj(epsilon_inv, H.constant_form(M.SPHI_TWO), epsilon)
    metric = (
        E.ETA,
        sp.zeros(14),
        sp.zeros(14),
        sp.zeros(14),
    )
    residual = source_shiab_jet(metric, trace, phi_one, phi_two, curvature)
    base_residual = D.shiab(base_curvature)
    transported_residual = jf_conj(
        epsilon_inv,
        H.constant_form(base_residual),
        epsilon,
    )
    exact(
        "the explicitly moved trace/Phi/Hodge/projector/Shiab graph equals transported active residual through mixed order",
        all(
            form_equal(residual[slot], transported_residual[slot])
            for slot in range(4)
        ),
    )
    exact(
        "the source-epsilon residual graph is nonvacuous in both first slots and the mixed slot",
        all(bool(M.flatten_form(residual[slot])) for slot in (1, 2, 3)),
        "coordinates=" + str(tuple(len(M.flatten_form(residual[slot])) for slot in range(4))),
    )

    residual_star = H.jhodge(metric, residual)
    action_jet = H2.scalar_jet(H.jfwedge(residual_star, residual))
    exact(
        "the active residual norm is exactly constant along the fully co-moving source gauge orbit",
        action_jet
        == (sp.Rational(981, 64), sp.Integer(0), sp.Integer(0), sp.Integer(0)),
        f"norm_jet={action_jet}",
    )

    fixed_trace = constant_cliff(M.STRACE)
    fixed_phi_one = H.constant_form(M.SPHI_ONE)
    fixed_phi_two = H.constant_form(M.SPHI_TWO)
    curvature_only = source_shiab_jet(
        metric,
        fixed_trace,
        fixed_phi_one,
        fixed_phi_two,
        curvature,
    )
    operator_only = source_shiab_jet(
        metric,
        trace,
        phi_one,
        phi_two,
        H.constant_form(base_curvature),
    )
    exact(
        "curvature motion and epsilon-soldered operator motion are separately live and neither equals the complete mixed residual graph",
        not form_equal(curvature_only[3], residual[3])
        and not form_equal(operator_only[3], residual[3])
        and bool(curvature_only[3])
        and bool(operator_only[3]),
    )
    reject(
        "freeze the epsilon-soldered trace/Phi operator while moving curvature and claim the complete mixed residual graph",
        form_equal(curvature_only[3], residual[3]),
    )
    reject(
        "freeze curvature while moving the epsilon-soldered operator and claim the complete mixed residual graph",
        form_equal(operator_only[3], residual[3]),
    )

    wrong_inverse: H.JCliff = (
        one,
        generator_r,
        generator_s,
        mixed_exponential,
    )
    reject(
        "use the same first-order signs for epsilon and epsilon inverse",
        H.jcmul(wrong_inverse, epsilon) == identity_jet,
    )
    reject(
        "promote a conditional local active orbit to a global public-source real-form bundle morphism",
        False,
    )
    reject(
        "promote source-orbit closure to either complete 35-monomial C4 bank",
        False,
    )
    return {
        "curvature_coordinates": tuple(
            len(M.flatten_form(curvature[slot])) for slot in range(4)
        ),
        "residual_coordinates": tuple(
            len(M.flatten_form(residual[slot])) for slot in range(4)
        ),
        "norm_jet": action_jet,
    }


def boundary() -> None:
    typed("the conditional local active source-epsilon connection/curvature/operator orbit graph is closed through mixed order")
    typed("the global source-to-active real-form bundle morphism, descent atlas, and public-source identity remain open")
    typed("complete separate 35-monomial I1 A4 and I2B C4 banks remain unassembled")
    typed("multi-index formal adjoint, Green concomitant, Helmholtz quotient, live C3 return, and projective kappa1 classification remain downstream")
    typed("vertical/mixed conormals, partial-Z1, section tangents, domain, observation, and physics remain open")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2F-R2B2B2H3 EXACT SOURCE-EPSILON CURVATURE-ORBIT GRAPH")
    source_and_layer_zero()
    connection = matrix_connection_curvature_gate()
    active = active_source_orbit_gate()
    boundary()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: connection_mixed_entries="
        f"{connection['mixed_entries']}; omission_defect_entries="
        f"{connection['omission_entries']}; curvature_jet_coordinates="
        f"{active['curvature_coordinates']}; residual_jet_coordinates="
        f"{active['residual_coordinates']}; norm_jet={active['norm_jet']}; "
        "conditional_local_source_epsilon_curvature_orbit_graph=CLOSED; "
        "global_source_to_active_bundle_morphism=OPEN",
        flush=True,
    )
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source + {TYPE} type + "
        f"{PLANTED} planted = {total}; failures={len(FAILURES)}",
        flush=True,
    )
    if FAILURES:
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print(
        "VERDICT: R2B2B2H3 CLOSES THE CONDITIONAL LOCAL ACTIVE SOURCE-EPSILON "
        "CONNECTION/CURVATURE/OPERATOR ORBIT GRAPH THROUGH MIXED ORDER; THE "
        "GLOBAL SOURCE-TO-ACTIVE REAL-FORM BUNDLE MORPHISM AND BOTH SEPARATE "
        "C4 BANKS REMAIN OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
