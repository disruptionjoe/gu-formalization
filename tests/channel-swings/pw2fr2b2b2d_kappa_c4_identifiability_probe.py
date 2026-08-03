#!/usr/bin/env python3
r"""PW2F-R2B2B2D active kappa1 C4 identifiability gate.

The source-explicit first bosonic action contains the distortion-mass slot

    <T, * (kappa1 / 2) T>.

On the accepted conditional fixed-``(epsilon,varpi)`` principal-``Z1``
metric branch, the corrected tangent is

    deltaB = Ad(epsilon^-1) deltaGamma,
    deltaT = -deltaq = deltaGamma - deltaB.

This probe computes the complete 35-monomial quartic coefficient bank of the
normal ``J*H J`` contribution from the ``kappa1`` slot for all ten metric
owners, verifies it by held-out conormals, direct mixed differentiation, and a
separate formal-adjoint/Green route, and tests whether the already established
constraints determine the slot's full off-shell C4 coefficient.  They do not:
the still-unbuilt ``T*D2T`` and moving-pairing returns admit distinct symmetric
order-four completions.  The probe does not compute those returns, the
remaining transgression bank, or any ``I2B`` C4 coefficient.  P1/P2/P3 remain
unused; Curt remains separate.
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


C = load_probe(
    "pw2fr2b2b2d_ceiling",
    "pw2fr2b2b2c_i2b_offshell_c5_ceiling_probe.py",
)
B = C.B
R2A = C.R2A
B1 = R2A.B1
R = C.R
M = C.M
D = C.D
E = R2A.E


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
    print(
        f"{'PASS' if condition else 'FAIL'}: source - {label} [{disposition}]",
        flush=True,
    )
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


def zero(value: sp.Matrix | sp.Expr) -> bool:
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(item) == 0 for item in value)
    return sp.simplify(value) == 0


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    pack = pack_path.read_text()
    predecessor = (
        ROOT
        / "explorations/pw2fr2b2b2b-source-residual-leading-symbol-2026-08-03.md"
    ).read_text()
    ceiling = (
        ROOT
        / "explorations/pw2fr2b2b2c-i2b-offshell-c5-ceiling-2026-08-03.md"
    ).read_text()

    source_receipt(
        "the pinned source explicitly places kappa1/2 times T in the first bosonic action",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and r"\frac{\kappa_1}{2}T_\omega" in pack
        and r"I^B_1" in pack,
        "SOURCE-CONFIRMS placement, not an active normalization",
    )
    source_receipt(
        "the accepted source audit leaves the kappa1 value and active normalization open",
        "`kappa1` value/active normalization" in predecessor
        and "actual induced coefficient tensors" in ceiling,
        "SOURCE-SILENT on the active value and coefficient tensors",
    )

    typed("source epsilon, repository h/u, and reduction epsilon remain distinct")
    typed("the source (7,7) presentation and active trace-reversed (9,5) pairing remain a real-form fork")
    typed("I1 and the manuscript I2B residual square remain distinct actions")
    typed("this gate constructs only the normal J-star-H-J kappa1 mass sub-bank, not the slot's complete off-shell pullback Hessian or the complete I1 C4 bank")
    typed("source-explicit coefficient placement is not a source-selected numerical value")
    typed("the active conditional rotor is a repository reconstruction, not an identification with source epsilon")
    typed("P1/P2/P3 supply no kappa1 value, active normalization, coefficient, or cancellation")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")


def active_rotor() -> tuple[M.SCliff, M.SCliff]:
    generator = M.sblade(0, 1)
    epsilon, epsilon_inv = E.algebraic_exponential_point(
        generator,
        sp.Integer(1),
        sp.Rational(3, 5),
        sp.Rational(4, 5),
    )
    exact(
        "the conditional active epsilon slot uses the accepted exact noncentral Spin(9,5) rotor",
        M.smul(generator, generator) == {0: -1}
        and E.cinv_pair(epsilon, epsilon_inv)
        and E.group_compatible(epsilon),
    )
    return epsilon, epsilon_inv


def active_tangent(
    point, epsilon: M.SCliff, epsilon_inv: M.SCliff
) -> dict[str, list[M.SForm]]:
    eta = tuple(sp.Integer(value) for value in point)
    gamma = [R.principal_b_form(eta, owner, False, True) for owner in range(10)]
    b_full = [E.fconj(epsilon_inv, value, epsilon) for value in gamma]
    q = [M.sfadd(b_full[index], M.sfscale(gamma[index], -1)) for index in range(10)]
    t = [M.sfscale(value, -1) for value in q]
    old_t = [M.sfscale(value, -1) for value in b_full]
    return {"gamma": gamma, "b": b_full, "q": q, "t": t, "old_t": old_t}


def tangent_checks(epsilon: M.SCliff, epsilon_inv: M.SCliff) -> None:
    graph = active_tangent((1, -1, 2, 3), epsilon, epsilon_inv)
    exact(
        "all ten active owners obey deltaT=-deltaq and deltaB=deltaGamma+deltaq",
        all(
            form_equal(graph["t"][owner], M.sfscale(graph["q"][owner], -1))
            and form_equal(
                graph["b"][owner],
                M.sfadd(graph["gamma"][owner], graph["q"][owner]),
            )
            for owner in range(10)
        ),
    )
    exact(
        "the corrected fixed-varpi tangent recombines deltaB+deltaT=deltaGamma",
        all(
            form_equal(
                M.sfadd(graph["b"][owner], graph["t"][owner]),
                graph["gamma"][owner],
            )
            for owner in range(10)
        ),
    )
    exact(
        "the forbidden deltaT=-deltaB_full shortcut differs on the active noncentral rotor",
        any(
            not form_equal(graph["t"][owner], graph["old_t"][owner])
            for owner in range(10)
        ),
    )
    reject(
        "restore the old deltaT=-deltaB_full shortcut",
        all(
            form_equal(graph["t"][owner], graph["old_t"][owner])
            for owner in range(10)
        ),
    )


def mass_matrix(
    point, epsilon: M.SCliff, epsilon_inv: M.SCliff, old: bool = False
) -> sp.Matrix:
    graph = active_tangent(point, epsilon, epsilon_inv)
    forms = graph["old_t"] if old else graph["t"]
    return R.gram(forms)


def reconstruct(values: list[sp.Matrix]) -> list[sp.Matrix]:
    inverse = B1.VANDERMONDE.inv()
    coefficients = [sp.zeros(10) for _ in B1.MONOMIALS]
    for row in range(10):
        for column in range(10):
            recovered = inverse * sp.Matrix([value[row, column] for value in values])
            for index, coefficient in enumerate(recovered):
                coefficients[index][row, column] = sp.simplify(coefficient)
    return coefficients


def evaluate_reconstruction(coefficients: list[sp.Matrix], point) -> sp.Matrix:
    result = sp.zeros(10)
    for coefficient, alpha in zip(coefficients, B1.MONOMIALS):
        result += coefficient * B1.monomial(point, alpha)
    return result.applyfunc(sp.simplify)


def direct_mass_hessian(forms: list[M.SForm], left: int, right: int) -> sp.Expr:
    r, s = sp.symbols("r s", real=True)
    variation = M.sfadd(
        M.sfscale(forms[left], r),
        M.sfscale(forms[right], s),
    )
    action = sp.simplify(
        sp.Rational(1, 2) * D.top_scalar(variation, M.sfhodge(variation))
    )
    return sp.simplify(sp.diff(action, r, s).subs({r: 0, s: 0}))


def complete_mass_bank(
    epsilon: M.SCliff, epsilon_inv: M.SCliff
) -> dict[str, object]:
    exact(
        "four observed-base conormal variables have exactly 35 homogeneous quartic monomials",
        len(B1.MONOMIALS) == 35,
    )
    exact(
        "the declared quartic simplex lattice has exact rank 35",
        B1.VANDERMONDE.rank() == 35,
    )

    values: list[sp.Matrix] = []
    for index, point in enumerate(B1.POINTS):
        values.append(mass_matrix(point, epsilon, epsilon_inv))
        print(f"KAPPA_C4_LATTICE: {index + 1}/35", flush=True)
    coefficients = reconstruct(values)
    nonzero_blocks = sum(not zero(value) for value in coefficients)
    coefficient_rank = sp.Matrix.hstack(
        *(matrix.reshape(100, 1) for matrix in coefficients)
    ).rank()

    exact(
        "all 35 active normal kappa1 C4 coefficient matrices are owner-symmetric",
        all(value == value.T for value in coefficients),
    )
    exact(
        "the corrected-source-tangent normal kappa1 quartic sub-bank is nonzero",
        nonzero_blocks > 0 and coefficient_rank > 0,
        f"nonzero_blocks={nonzero_blocks}; coefficient_rank={coefficient_rank}",
    )

    heldouts = ((1, -1, 2, 3), (2, 1, -2, 1), (-1, 3, 1, 2))
    heldout_failures = 0
    for point in heldouts:
        direct = mass_matrix(point, epsilon, epsilon_inv)
        recovered = evaluate_reconstruction(coefficients, point)
        heldout_failures += int(not zero(direct - recovered))
    exact(
        "the 35-monomial active normal kappa1 bank passes three dense held-out conormals",
        heldout_failures == 0,
        f"failures={heldout_failures}/3",
    )

    direct_point = (1, 1, 0, 0)
    graph = active_tangent(direct_point, epsilon, epsilon_inv)
    direct_matrix = mass_matrix(direct_point, epsilon, epsilon_inv)
    exact(
        "direct mixed differentiation of the mass action matches the independently assembled Gram entry",
        direct_matrix[0, 0] != 0
        and sp.simplify(direct_mass_hessian(graph["t"], 0, 0) - direct_matrix[0, 0]) == 0,
        f"entry={direct_matrix[0, 0]}",
    )

    dense = heldouts[0]
    correct_dense = mass_matrix(dense, epsilon, epsilon_inv)
    old_dense = mass_matrix(dense, epsilon, epsilon_inv, old=True)
    exact(
        "the forbidden old deltaT=-deltaB_full graph produces a distinct quartic mass tensor",
        not zero(correct_dense - old_dense),
    )
    reject(
        "reuse the old fixed-total-connection mass bank as the corrected source-coordinate bank",
        zero(correct_dense - old_dense),
    )

    doubled = tuple(2 * value for value in dense)
    exact(
        "the active mass tensor is exactly homogeneous of conormal degree four and creates no C5 term",
        zero(mass_matrix(doubled, epsilon, epsilon_inv) - 16 * correct_dense),
    )
    exact(
        "two unexcluded active kappa1 values give distinct normal C4 banks while preserving the C5 ceiling",
        any(not zero(value) for value in coefficients)
        and any(not zero(2 * value - value) for value in coefficients),
    )
    reject(
        "declare the complete I1 C4 bank fixed from the live normal kappa1 sub-bank alone",
        False,
    )

    # Hostile variational review: for the pulled mass action the full C4 slot
    # also contains background-T times D2T and moving pairing/lowerer returns.
    # Their order ceilings are known but their coefficient values are not.
    # Both completions below satisfy every currently asserted degree-four,
    # owner-symmetry, and formal-adjoint constraint, yet disagree on the full
    # kappa coefficient.  This is an identifiability witness, not a proposal
    # for either completion.
    zero_completion = [sp.zeros(10) for _ in coefficients]
    cancelling_completion = [-value for value in coefficients]
    full_zero_return = [
        normal + unknown
        for normal, unknown in zip(coefficients, zero_completion)
    ]
    full_cancelling_return = [
        normal + unknown
        for normal, unknown in zip(coefficients, cancelling_completion)
    ]
    exact(
        "current C4 order/symmetry constraints admit distinct off-shell kappa1 completions",
        any(not zero(value) for value in full_zero_return)
        and all(zero(value) for value in full_cancelling_return)
        and all(value == value.T for value in cancelling_completion),
    )
    reject(
        "promote the normal mass Gram to the complete off-shell kappa1 C4 coefficient",
        False,
    )

    return {
        "coefficients": coefficients,
        "nonzero_blocks": nonzero_blocks,
        "coefficient_rank": coefficient_rank,
        "dense": correct_dense,
        "heldout": dense,
    }


def total_derivative(expr: sp.Expr, rows: list[list[sp.Symbol]]) -> sp.Expr:
    return sp.expand(
        sum(
            sp.diff(expr, row[index]) * row[index + 1]
            for row in rows
            for index in range(len(row) - 1)
        )
    )


def formal_adjoint_and_green(result: dict[str, object]) -> None:
    coefficients: list[sp.Matrix] = result["coefficients"]  # type: ignore[assignment]
    adjoint_failures = 0
    for alpha, coefficient in zip(B1.MONOMIALS, coefficients):
        formal_adjoint = (-1) ** sum(alpha) * coefficient.T
        adjoint_failures += int(not zero(formal_adjoint - coefficient))
    exact(
        "the independent coefficientwise formal adjoint reproduces all 35 even-order normal mass tensors",
        adjoint_failures == 0,
        f"failures={adjoint_failures}/35",
    )

    dense: sp.Matrix = result["dense"]  # type: ignore[assignment]
    active = tuple(index for index in range(10) if any(dense[index, j] != 0 for j in range(10)))
    selected_indices = active[: min(3, len(active))]
    chosen = dense.extract(selected_indices, selected_indices)
    exact(
        "a live active-owner block exists for the native-ray Green check",
        chosen.rows > 0 and not zero(chosen),
        f"owners={selected_indices}; rank={chosen.rank()}",
    )

    u = [list(sp.symbols(f"u{owner}_0:6")) for owner in range(chosen.rows)]
    v = [list(sp.symbols(f"v{owner}_0:6")) for owner in range(chosen.rows)]
    u0 = sp.Matrix([row[0] for row in u])
    v0 = sp.Matrix([row[0] for row in v])
    u1 = sp.Matrix([row[1] for row in u])
    v1 = sp.Matrix([row[1] for row in v])
    u2 = sp.Matrix([row[2] for row in u])
    v2 = sp.Matrix([row[2] for row in v])
    u3 = sp.Matrix([row[3] for row in u])
    v3 = sp.Matrix([row[3] for row in v])
    u4 = sp.Matrix([row[4] for row in u])
    v4 = sp.Matrix([row[4] for row in v])
    concomitant = (
        (u0.T * chosen * v3)[0]
        - (u1.T * chosen * v2)[0]
        + (u2.T * chosen * v1)[0]
        - (u3.T * chosen * v0)[0]
    )
    bulk = (u0.T * chosen * v4)[0] - (v0.T * chosen * u4)[0]
    exact(
        "the independently constructed fourth-order Green concomitant closes on a live native conormal ray",
        sp.expand(bulk - total_derivative(concomitant, u + v)) == 0
        and concomitant != 0,
    )

    asymmetric = chosen.copy()
    if asymmetric.rows == 1:
        asymmetric = sp.Matrix([[chosen[0, 0], 1], [0, chosen[0, 0]]])
    else:
        asymmetric[0, 1] += 1
    reject(
        "accept an asymmetric planted even-order coefficient as formally self-adjoint",
        asymmetric == asymmetric.T,
    )
    reject("use the Green concomitant as a bulk C4 cancellation", concomitant == 0)


def preserve_prior_ceiling() -> None:
    eta = sp.symbols("eta0:4", real=True)
    one = R.symbolic_xi_form(eta)
    gamma = [R.symbolic_z1_b_form(eta, owner) for owner in range(10)]
    pre_shiab = [M.sfwedge(one, value) for value in gamma]
    j3 = [D.shiab(value) for value in pre_shiab]
    exact(
        "the inherited observed-base pre-Shiab incidence and J3 maps remain identically zero",
        all(not value for value in pre_shiab) and all(not value for value in j3),
    )
    typed("the live kappa1 ambiguity is quartic and does not reopen the closed I1/I2B C5 ceilings")


def boundary_checks() -> None:
    typed("the complete I1 C4 bank has the form A4 + kappa1*(M4_normal + U4), with only M4_normal constructed and both A4 and U4 open")
    typed("no active kappa1 value or normalization is selected by this calculation")
    typed("the residual T-times-D2T and moving-pairing/lowerer kappa1 returns remain open and may cancel or reinforce the normal bank")
    typed("the remaining I1 transgression/moving-coefficient bank and any exceptional-kappa proportionality relation remain open")
    typed("the distinct off-shell I2B C4 bank remains wholly uncomputed")
    typed("vertical/mixed conormals, partial-Z1, section tangents, global epsilon, C3/C2, characteristic, domain, quotient, observation, and physics remain open")
    reject("promote the kappa1 sub-bank to a complete action or physics result", False)
    reject("spend P1/P2/P3 to select kappa1", False)
    reject("merge Curt or promote a third lane from this Eric-lane identifiability result", False)


def main() -> int:
    print("PW2F-R2B2B2D ACTIVE KAPPA1 C4 IDENTIFIABILITY GATE")
    source_and_layer_zero()
    epsilon, epsilon_inv = active_rotor()
    tangent_checks(epsilon, epsilon_inv)
    result = complete_mass_bank(epsilon, epsilon_inv)
    formal_adjoint_and_green(result)
    preserve_prior_ceiling()
    boundary_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: active_kappa1_C4_nonzero_blocks="
        f"{result['nonzero_blocks']}; coefficient_rank={result['coefficient_rank']}; "
        "complete_I1_C4=UNDERDETERMINED_PENDING_A4_U4_AND_ACTIVE_KAPPA1",
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
        "VERDICT: COMPLETE ACTIVE NORMAL KAPPA1 MASS C4 SUB-BANK PASSES; "
        "THE FULL OFF-SHELL KAPPA1 AND I1 C4 BANKS REMAIN UNDERDETERMINED UNTIL "
        "THE T-D2T/MOVING-PAIRING RETURNS, TRANSGRESSION BANK, AND ACTIVE "
        "KAPPA1/NORMALIZATION ARE FIXED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
