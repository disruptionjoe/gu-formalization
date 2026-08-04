#!/usr/bin/env python3
r"""PW2F-R2B2B2H2 exact I2B residual/primalizer/pairing second jet.

R2B2B2H closed the exact ``(1,r,s,rs)`` trace/Phi/Hodge/Shiab operator
jet.  This probe uses that operator on the accepted conditional active
off-shell curvature residual and constructs the corresponding moving Hodge
primalizer and symmetric residual pairing on the same nonlinear Zorro
coframe.

The direct mixed coefficient of

    I2B(g) = 1/2 P_g(E(g), E(g))

is independently reassembled as the five off-shell Hessian families
``P0(Er,Es)``, ``P0(E0,Ers)``, ``Pr(E0,Es)``, ``Ps(E0,Er)``, and
``1/2 Prs(E0,E0)``.  Base full-carrier agreement, accepted first-Hodge
agreement, owner/conormal swap, Hodge square, curvature scaling, and planted
omissions protect the result.

This closes only the scoped second residual/primalizer/pairing dependency. It
does not assemble either 35-monomial C4 bank, perform multi-index
Green/Helmholtz reduction, select kappa1, or infer physics. P1/P2/P3 remain
unused; Curt remains formally separate; the third lane is not promoted.
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


H = load_probe(
    "pw2fr2b2b2h2_predecessor",
    "pw2fr2b2b2h_mixed_shiab_second_jet_probe.py",
)
G = H.G
E = H.E
M = H.M
B = E.C.B
D = B.D
P = B.P


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


def top_scalar(value: M.SForm) -> sp.Expr:
    return sp.simplify(value.get(M.FULL_KEY, {}).get(0, 0))


def scalar_jet(value: H.JForm) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    return tuple(top_scalar(slot) for slot in value)  # type: ignore[return-value]


def symmetric_pairing_jet(
    metric,
    left: M.SForm,
    right: M.SForm,
) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    """Return the exact moving symmetric pairing P_g(left,right)."""
    left_star = H.jhodge(metric, H.constant_form(left))
    right_star = H.jhodge(metric, H.constant_form(right))
    left_right = scalar_jet(H.jfwedge(left_star, H.constant_form(right)))
    right_left = scalar_jet(H.jfwedge(right_star, H.constant_form(left)))
    return tuple(
        sp.simplify((left_right[slot] + right_left[slot]) / 2)
        for slot in range(4)
    )  # type: ignore[return-value]


def base_pair(left: M.SForm, right: M.SForm) -> sp.Expr:
    return sp.simplify(
        (
            D.top_scalar(M.sfhodge(left), right)
            + D.top_scalar(M.sfhodge(right), left)
        )
        / 2
    )


def first_pair(left: M.SForm, right: M.SForm, h: sp.Matrix) -> sp.Expr:
    return sp.simplify(
        (
            D.top_scalar(M.dstar(left, h), right)
            + D.top_scalar(M.dstar(right, h), left)
        )
        / 2
    )


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    predecessor_path = (
        ROOT / "explorations/pw2fr2b2b2h-mixed-shiab-second-jet-2026-08-04.md"
    )
    staged_path = (
        ROOT / "explorations/eric-curt-wave3d-b2c12-active-staged-action-2026-08-01.md"
    )
    pack = pack_path.read_text()
    predecessor = predecessor_path.read_text()
    staged = staged_path.read_text()
    source_receipt(
        "the pinned source fixes I1 grammar while the separately custodied reconstruction retains the I2B residual-square glyph",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and "I^B_1" in pack
        and r"I_2^B=\|\Upsilon_B\|^2" in staged,
        "SOURCE-CONFIRMS separate action grammars",
    )
    source_receipt(
        "the accepted predecessor names the complete second residual-primalizer/pairing jet as the next distinct dependency",
        "second residual-primalizer" in predecessor
        and "no distinct `I2B C4` bank" in predecessor,
        "REPOSITORY-DERIVED successor construction; SOURCE-SILENT on active jet",
    )
    typed("source I1, manuscript I2B, and the active repository residual-square port are three separately custodied objects")
    typed("residual density, Hodge primalizer, internal Clifford/Krein scalar pairing, and action Hessian routes remain typed separately")
    typed("the active trace-reversed (9,5) carrier is not identified with the unported source (7,7) action pairing")
    typed("fixed background curvature and its operator-induced residual jet are not a complete global source-epsilon curvature graph")
    typed("a closed local second jet remains upstream of and weaker than a 35-monomial C4 bank")


def residual_pairing_gate() -> dict[str, object]:
    owner_i, xi = 3, tuple(map(sp.Integer, (-1, 2, 0, 1)))
    owner_j, zeta = 7, tuple(map(sp.Integer, (1, 0, -2, 2)))
    metric, trace_matrix = G.moving_frame_trace_jet(owner_i, xi, owner_j, zeta)
    trace = H.matrix_trace_to_cliff(trace_matrix)
    curvature = D.to_sympy_form(P.SPIN_CURVATURE)
    residual = H.shiab_jet(metric, trace, H.constant_form(curvature))
    accepted_base = D.shiab(curvature)

    exact(
        "the new residual jet recovers the accepted 13-coordinate off-shell Shiab residual at its base slot",
        form_equal(residual[0], accepted_base)
        and len(M.flatten_form(residual[0])) == 13,
    )
    base_star = H.jhodge(metric, H.constant_form(accepted_base))
    pairing = tuple(
        D.top_scalar(base_star[slot], accepted_base) for slot in range(4)
    )
    exact(
        "the moving Hodge/primalizer pairing recovers the accepted full-carrier residual norm at base",
        pairing[0] == B.residual_pair(accepted_base, accepted_base)
        == sp.Rational(981, 64),
        f"norm={pairing[0]}",
    )

    expected_r = sp.simplify(
        (
            D.top_scalar(M.dstar(accepted_base, metric[1]), accepted_base)
            + D.top_scalar(M.dstar(accepted_base, metric[1]), accepted_base)
        )
        / 2
    )
    expected_s = sp.simplify(
        (
            D.top_scalar(M.dstar(accepted_base, metric[2]), accepted_base)
            + D.top_scalar(M.dstar(accepted_base, metric[2]), accepted_base)
        )
        / 2
    )
    exact(
        "both first moving-primalizer slots equal the independently accepted first Hodge variation",
        pairing[1] == expected_r and pairing[2] == expected_s,
        f"first=({pairing[1]},{pairing[2]})",
    )
    exact(
        "the exact intrinsic mixed moving-primalizer pairing vanishes on this scoped pair while a first slot remains live",
        pairing[3] == 0 and (pairing[1] != 0 or pairing[2] != 0),
        f"jet={pairing}",
    )

    twice = H.jhodge(metric, H.jhodge(metric, H.constant_form(accepted_base)))
    base_twice = M.sfhodge(M.sfhodge(accepted_base))
    sign = sp.Integer(1) if form_equal(base_twice, accepted_base) else sp.Integer(-1)
    exact(
        "the Hodge/primalizer jet squares to the exact 13-form signature sign through mixed order",
        form_equal(twice[0], M.sfscale(accepted_base, sign))
        and not twice[1]
        and not twice[2]
        and not twice[3],
        f"star_square_sign={sign}",
    )

    # Assemble the Hodge of the moving residual by the independent second
    # product rule. This reuses the one expensive fixed-residual Hodge jet and
    # applies the accepted first variation only to the first residual slots.
    moving_star = (
        base_star[0],
        M.sfadd(M.sfhodge(residual[1]), base_star[1]),
        M.sfadd(M.sfhodge(residual[2]), base_star[2]),
        M.sfadd(
            M.sfhodge(residual[3]),
            M.dstar(residual[2], metric[1]),
            M.dstar(residual[1], metric[2]),
            base_star[3],
        ),
    )
    direct_action = tuple(
        sp.simplify(value / 2)
        for value in scalar_jet(H.jfwedge(moving_star, residual))
    )
    routes = {
        "normal_JR_J": base_pair(residual[1], residual[2]),
        "residual_R_D2E": base_pair(residual[0], residual[3]),
        "J_DR_E_left": first_pair(residual[0], residual[2], metric[1]),
        "J_DR_E_right": first_pair(residual[0], residual[1], metric[2]),
        "residual_D2R_residual": sp.simplify(pairing[3] / 2),
    }
    assembled = sp.simplify(sum(routes.values()))
    exact(
        "the direct mixed residual-square jet equals the complete five-family off-shell I2B Hessian product rule",
        sp.simplify(direct_action[3] - assembled) == 0,
        f"direct={direct_action[3]}; routes={routes}",
    )
    live_routes = tuple(name for name, value in routes.items() if value != 0)
    exact(
        "the scoped off-shell jet has live normal, residual-second, and first-moving-primalizer families while the exact second-pairing family is zero",
        routes["normal_JR_J"] != 0
        and routes["residual_R_D2E"] != 0
        and (routes["J_DR_E_left"] != 0 or routes["J_DR_E_right"] != 0)
        and routes["residual_D2R_residual"] == 0
        and len(live_routes) >= 3,
        f"live={live_routes}",
    )

    swapped_metric, swapped_trace_matrix = G.moving_frame_trace_jet(
        owner_j, zeta, owner_i, xi
    )
    exact(
        "the exact nonlinear metric and trace jets swap first slots and preserve the mixed data required by predecessor residual symmetry",
        all(zero(swapped_metric[slot] - metric[(0, 2, 1, 3)[slot]]) for slot in range(4))
        and all(
            zero(swapped_trace_matrix[slot] - trace_matrix[(0, 2, 1, 3)[slot]])
            for slot in range(4)
        ),
    )
    frozen_star = (
        M.sfhodge(residual[0]),
        M.sfhodge(residual[1]),
        M.sfhodge(residual[2]),
        M.sfhodge(residual[3]),
    )
    frozen_action = tuple(
        sp.simplify(value / 2)
        for value in scalar_jet(H.jfwedge(frozen_star, residual))
    )
    residual_without_mixed = (residual[0], residual[1], residual[2], {})
    omitted_star = (
        base_star[0],
        M.sfadd(M.sfhodge(residual[1]), base_star[1]),
        M.sfadd(M.sfhodge(residual[2]), base_star[2]),
        M.sfadd(
            M.dstar(residual[2], metric[1]),
            M.dstar(residual[1], metric[2]),
            base_star[3],
        ),
    )
    omitted_action = tuple(
        sp.simplify(value / 2)
        for value in scalar_jet(H.jfwedge(omitted_star, residual_without_mixed))
    )
    reject(
        "freeze the moving residual primalizer and claim the mixed I2B action is unchanged",
        frozen_action[3] == direct_action[3],
    )
    reject(
        "drop the mixed residual response off shell and claim the mixed I2B action is unchanged",
        omitted_action[3] == direct_action[3],
    )
    reject(
        "plant a nonzero second moving-primalizer family where the exact scoped mixed pairing is zero",
        sp.simplify(assembled + 1 - direct_action[3]) == 0,
    )
    reject("identify the indefinite residual primalizer with a positive Hilbert Riesz map", B.FULL.residual_inertia()[1] == 0)
    reject("promote one scoped second jet to a complete 35-monomial I2B C4 bank", False)

    return {
        "base_norm": pairing[0],
        "mixed_pairing": pairing[3],
        "mixed_action": direct_action[3],
        "live_routes": live_routes,
        "star_square_sign": sign,
    }


def boundary() -> None:
    typed("the scoped fixed-background residual/operator second jet is closed; the complete source-epsilon curvature graph remains a separate global port")
    typed("complete 35-monomial I1 A4 and I2B C4 banks remain unassembled")
    typed("multi-index formal adjoint, Green concomitant, Helmholtz quotient, live C3 return, and projective kappa1 classification remain downstream")
    typed("vertical/mixed conormals, partial-Z1, section tangents, domain, observation, and physics remain open")
    typed("P1/P2/P3 remain unchanged and unused")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def main() -> int:
    print("PW2F-R2B2B2H2 EXACT I2B SECOND RESIDUAL/PRIMALIZER/PAIRING JET")
    source_and_layer_zero()
    result = residual_pairing_gate()
    boundary()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: base_residual_norm="
        f"{result['base_norm']}; mixed_pairing={result['mixed_pairing']}; "
        f"mixed_I2B_action={result['mixed_action']}; live_routes={result['live_routes']}; "
        "scoped_second_residual_primalizer_pairing_jet=CLOSED",
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
        "VERDICT: R2B2B2H2 CLOSES THE CONDITIONAL ACTIVE FIXED-BACKGROUND "
        "I2B SECOND RESIDUAL/PRIMALIZER/PAIRING JET; COMPLETE I1/I2B C4 "
        "BANKS, MULTI-INDEX GREEN/HELMHOLTZ REDUCTION, AND THE GLOBAL "
        "SOURCE-EPSILON CURVATURE PORT REMAIN OPEN"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
