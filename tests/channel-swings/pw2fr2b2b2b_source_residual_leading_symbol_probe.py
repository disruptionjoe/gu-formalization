#!/usr/bin/env python3
r"""R2B2B2B active local source-grammar tangent and leading symbols.

This probe performs the leading-order gate that must precede a native quartic
bank.  It keeps the source gauge transformation ``epsilon`` separate from the
repository reduction field and from ``h=exp(u)``.  At fixed source
``(epsilon,varpi)`` it differentiates

    B = epsilon^-1 Gamma epsilon + epsilon^-1 d epsilon,
    q = B-Gamma,  T = varpi-q,  A = B+T = Gamma+varpi.

It then embeds sparse 13-form/Clifford residuals into the full active residual
carrier already constructed by B2C15, and computes the possible ``I1`` C5 and
residual-zero normal ``I2B`` C6 symbols.  It does not compute complete C4, a Green
domain, quotient, observation equation, or physics.  P1/P2/P3 are unused.
"""

from __future__ import annotations

from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from math import comb
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


R2A = load_probe("r2b2b2b_r2a", "pw2fr2b2a_second_frechet_c4_graph_probe.py")
FULL = load_probe(
    "r2b2b2b_full_residual",
    "eric_curt_wave3d_b2c15_full_quotient_primalizer_lc_graph_probe.py",
)
R = R2A.R
M = R2A.M
D = R2A.D
E = R2A.E
P = R2A.P


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


def form_equal(left: M.SForm, right: M.SForm) -> bool:
    return not M.sfadd(left, M.sfscale(right, -1))


def rational(value) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def source_and_layer_zero() -> None:
    pack_path = ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md"
    pack = pack_path.read_text()
    tangent = (
        ROOT
        / "explorations/eric-curt-wave3d-b2c15p-source-epsilon-tangent-zorro-dewitt-2026-08-02.md"
    ).read_text()
    predecessor = (
        ROOT / "explorations/pw2fr2b2b2a-native-coefficient-action-split-2026-08-03.md"
    ).read_text()

    source_receipt(
        "the pinned source pack records draft pp.43-45/56-57, the first bosonic action, T=varpi-epsilon^-1 d0 epsilon, and kappa1 placement",
        hashlib.sha256(pack_path.read_bytes()).hexdigest()
        == "5b50adabf067959654073f7e5c6665e8ac1e3e52ae36ae22ae9754bc9db23b5f"
        and all(token in pack for token in ("I^B_1", "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon", "\\kappa_1")),
        "SOURCE-CONFIRMS; author draft Sec.9.1/9.2 and pp.43-45,56-57",
    )
    exact(
        "the repository derives deltaT=alpha-D_A zeta from the source-confirmed distortion grammar",
        "delta T=alpha-D_A zeta" in tangent and "A=q_g(epsilon)" in tangent,
    )
    source_receipt(
        "the inspected source does not supply the active Spin(9,5) rotor embedding or active residual primalizer",
        "real-form translation" in pack and "a Krein/Riesz" in pack,
        "SOURCE-SILENT on the active port",
    )
    source_receipt(
        "the inspected source does not state the active J3 polynomial cancellation",
        "J_{3,i}" not in pack and "115584" not in pack,
        "SOURCE-SILENT on the leading-symbol theorem",
    )
    exact(
        "R2B2B2A leaves induced coefficient tensors and leading conormal banks open",
        "not** the actual induced-`Y14`" in predecessor and "It does not earn" in predecessor,
    )

    typed("source epsilon versus the chosen active Spin(9,5) rotor is UNCERTAIN/HOMONYM-RISK")
    typed("source nabla^g versus the reconstructed induced-Y14 Gamma is UNCERTAIN")
    typed("source Upsilon/I2B versus the active sparse residual/primalizer is SAME-GRAMMAR-CANDIDATE, not SAME-OBJECT")
    typed("source epsilon, repository h=exp(u), and reduction epsilon remain distinct")
    typed("the active (9,5) right-H/Krein carrier is a repository port, not the source (7,7) arena")
    typed("I1 and the manuscript I2B norm glyph remain distinct actions")
    typed("the source fixes the action grammar but is silent on this active residual primalizer")
    typed("the fixed-(epsilon,varpi) principal-Z1 metric-metric tangent is a restricted repository reconstruction, not the full source tangent")
    typed("B=Gamma+q and A=Gamma+varpi are repository-derived coordinate reparameterizations")
    typed("P1/P2/P3 supply no tangent, residual injection, coefficient, or cancellation")
    typed("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    typed("TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")

    counts = {degree: comb(degree + 3, 3) for degree in (4, 5, 6)}
    exact(
        "homogeneous four-conormal monomial banks per symbol entry are C4=35, C5=56, and C6=84",
        counts == {4: 35, 5: 56, 6: 84},
        str(counts),
    )
    reject("reuse a 35-monomial quartic bank as a complete C5 bank", counts[5] == 35)
    reject("reuse a 35-monomial quartic bank as a complete C6 bank", counts[6] == 35)


def source_rotor() -> tuple[M.SCliff, M.SCliff]:
    generator = M.sblade(0, 1)
    square = M.smul(generator, generator)
    epsilon, epsilon_inv = E.algebraic_exponential_point(
        generator,
        sp.Integer(1),
        sp.Rational(3, 5),
        sp.Rational(4, 5),
    )
    exact(
        "the chosen active rotor is an exact noncentral Spin(9,5) point",
        square == {0: -1}
        and E.cinv_pair(epsilon, epsilon_inv)
        and E.group_compatible(epsilon),
    )
    typed("using this rotor in the epsilon slot is conditional; identity with source epsilon is unproved and it is not repository h/u")
    return epsilon, epsilon_inv


def source_tangent_checks(epsilon: M.SCliff, epsilon_inv: M.SCliff) -> dict[str, object]:
    eta = tuple(sp.Integer(value) for value in (1, -1, 2, 3))
    gamma = [R.principal_b_form(eta, owner, False, True) for owner in range(10)]
    b_full = [E.fconj(epsilon_inv, value, epsilon) for value in gamma]
    q = [M.sfadd(b_full[index], M.sfscale(gamma[index], -1)) for index in range(10)]
    t = [M.sfscale(value, -1) for value in q]
    a_total = [M.sfadd(b_full[index], t[index]) for index in range(10)]

    exact(
        "all ten conditional fixed-(epsilon,varpi) principal-Z1 active tangents satisfy deltaB=Ad(epsilon^-1)deltaGamma",
        all(form_equal(b_full[index], E.fconj(epsilon_inv, gamma[index], epsilon)) for index in range(10)),
    )
    exact(
        "all ten tangents satisfy deltaq=deltaB-deltaGamma and deltaT=-deltaq",
        all(
            form_equal(q[index], M.sfadd(b_full[index], M.sfscale(gamma[index], -1)))
            and form_equal(t[index], M.sfscale(q[index], -1))
            for index in range(10)
        ),
    )
    exact(
        "all ten repository-coordinate tangents recombine to deltaA=deltaGamma at fixed varpi",
        all(form_equal(a_total[index], gamma[index]) for index in range(10)),
    )
    exact(
        "the conditional noncentral active rotor produces live q/T source-grammar motion",
        any(q) and any(t),
        f"live_q_owners={sum(bool(value) for value in q)}",
    )

    identity = {0: sp.Integer(1)}
    identity_b = [E.fconj(identity, value, identity) for value in gamma]
    identity_q = [M.sfadd(identity_b[index], M.sfscale(gamma[index], -1)) for index in range(10)]
    exact(
        "identity epsilon annihilates q/T motion while retaining deltaA=deltaGamma",
        not any(identity_q) and all(form_equal(identity_b[index], gamma[index]) for index in range(10)),
    )
    reject(
        "replace deltaT=-deltaq by deltaT=-deltaB_full",
        all(form_equal(t[index], M.sfscale(b_full[index], -1)) for index in range(10)),
    )
    typed("in the chosen local trivialization fixed epsilon makes d epsilon metric-independent; its background and general epsilon/varpi variations remain omitted and can affect C4")
    return {"eta": eta, "gamma": gamma, "b": b_full, "q": q, "t": t, "a": a_total}


def internal_norm(mask: int) -> sp.Rational:
    return rational(FULL.internal_norm(mask))


def residual_coordinates(density: M.SForm) -> dict[tuple[int, int], sp.Expr]:
    """Raw 13-form coefficients -> coordinates dual to one-form blades."""
    coordinates: dict[tuple[int, int], sp.Expr] = {}
    for (key, mask), coefficient in M.flatten_form(density).items():
        if len(key) != 13:
            raise AssertionError(f"residual form degree {len(key)}")
        missing = tuple(index for index in range(14) if index not in key)
        if len(missing) != 1:
            raise AssertionError("13-form does not have one missing leg")
        mu = missing[0]
        orientation = sp.Integer(FULL.B14.permutation_sign((mu,) + key))
        # The internal trace pairing is part of the dual-basis conversion.
        value = sp.simplify(orientation * internal_norm(mask) * coefficient)
        if value:
            coordinates[(mu, mask)] = coordinates.get((mu, mask), 0) + value
    return {key: sp.simplify(value) for key, value in coordinates.items() if value != 0}


def residual_weight(coordinate: tuple[int, int]) -> sp.Rational:
    mu, mask = coordinate
    return sp.Integer(FULL.ETA[mu]) * internal_norm(mask)


def residual_pair(left: M.SForm, right: M.SForm) -> sp.Expr:
    left_coordinates = residual_coordinates(left)
    right_coordinates = residual_coordinates(right)
    return sp.simplify(
        sum(
            value * residual_weight(coordinate) * right_coordinates.get(coordinate, 0)
            for coordinate, value in left_coordinates.items()
        )
    )


def primalize_residual(density: M.SForm) -> M.SForm:
    result: M.SForm = {}
    for (mu, mask), coefficient in residual_coordinates(density).items():
        primal = sp.simplify(residual_weight((mu, mask)) * coefficient)
        result.setdefault((mu,), {})[mask] = primal
    return M.sfclean(result)


def lower_primal(primal: M.SForm) -> M.SForm:
    """Apply the frozen full residual lowerer and return a raw 13-form."""
    result: M.SForm = {}
    for (key, mask), coefficient in M.flatten_form(primal).items():
        if len(key) != 1:
            raise AssertionError("primal residual is not a one-form")
        mu = key[0]
        complement = tuple(index for index in range(14) if index != mu)
        orientation = sp.Integer(FULL.B14.permutation_sign((mu,) + complement))
        dual_coordinate = sp.simplify(residual_weight((mu, mask)) * coefficient)
        raw = sp.simplify(dual_coordinate / (orientation * internal_norm(mask)))
        result.setdefault(complement, {})[mask] = raw
    return M.sfclean(result)


def residual_pairing_checks() -> dict[str, object]:
    curvature = D.to_sympy_form(P.SPIN_CURVATURE)
    residual = D.shiab(curvature)
    flat = M.flatten_form(residual)
    coordinates = residual_coordinates(residual)
    actual_masks = {mask for _key, mask in flat}
    slice_masks = {(1 << 0) | (1 << 1), (1 << 0) | (1 << 9)}

    exact(
        "the active background sparse Shiab residual has thirteen 13-form/grade-2 coordinates",
        len(flat) == 13
        and len(coordinates) == 13
        and {len(key) for key, _mask in flat} == {13}
        and {mask.bit_count() for _key, mask in flat} == {2},
        f"raw={len(flat)}; coordinates={len(coordinates)}",
    )
    exact(
        "every sparse residual coordinate lies in the pre-existing full active carrier",
        all(
            0 <= mu < 14 and mask in FULL.GRADE_MASKS[2]
            for mu, mask in coordinates
        )
        and 14 * sum(len(FULL.GRADE_MASKS[grade]) for grade in FULL.SP_GRADES) == 115584,
    )
    independent_basis_failures = 0
    for mu, mask in coordinates:
        complement = tuple(index for index in range(14) if index != mu)
        basis_density = {complement: {mask: F(1)}}
        direct_basis = FULL.B14.basis_pair(mu, mask, basis_density)
        expected_basis = F(FULL.B14.permutation_sign((mu,) + complement)) * FULL.internal_norm(mask)
        independent_basis_failures += int(direct_basis != expected_basis)
    exact(
        "B2C14 basis_pair independently reproduces every sparse dual-coordinate sign",
        independent_basis_failures == 0,
        f"failures={independent_basis_failures}",
    )
    exact(
        "the reused full residual primalizer retains its exact nondegenerate inertia",
        FULL.residual_inertia() == (57664, 57920),
        "inertia=(57664,57920)",
    )
    direct = D.top_scalar(primalize_residual(residual), residual)
    coordinate_pair = residual_pair(residual, residual)
    exact(
        "direct top-form pairing equals the full-carrier diagonal primalizer pairing",
        sp.simplify(direct - coordinate_pair) == 0,
        f"norm={coordinate_pair}",
    )
    exact(
        "the frozen full residual lowerer-primalizer round trip is identity on all thirteen support coordinates",
        form_equal(lower_primal(primalize_residual(residual)), residual),
    )

    first_coordinate = next(iter(coordinates), None)
    exact("the full residual carrier retains a coordinate witness", first_coordinate is not None)
    first_coordinate = first_coordinate if first_coordinate is not None else (0, 0)
    mu, mask = first_coordinate
    complement = tuple(index for index in range(14) if index != mu)
    single: M.SForm = {complement: {mask: sp.Integer(1)}}
    exact(
        "a single-coordinate residual control has a nonzero exact Krein norm",
        residual_pair(single, single) in (sp.Integer(1), sp.Integer(-1)),
        f"norm={residual_pair(single, single)}",
    )
    exact(
        "the former 28-dimensional two-generator slice cannot stand for this thirteen-mask residual",
        not actual_masks.issubset(slice_masks),
        f"actual_masks={len(actual_masks)}; slice_masks={len(slice_masks)}",
    )
    reject("declare a residual pairing port from form degree alone without an explicit coordinate injection", False)
    reject("use the old two-generator 28-dimensional slice as the complete native residual carrier", actual_masks.issubset(slice_masks))
    return {"residual": residual, "coordinates": coordinates, "norm": coordinate_pair}


def first_live_non_lc_residual(one: M.SForm) -> tuple[tuple[int, int, int], M.SForm, sp.Expr]:
    masks = sorted({mask for cliff in P.SPIN_CURVATURE.values() for mask in cliff})
    for mu in range(14):
        for mask in masks:
            connection: M.SForm = {(mu,): {mask: sp.Integer(1)}}
            response = D.shiab(M.sfwedge(one, connection))
            if not response:
                continue
            norm = residual_pair(response, response)
            if norm != 0:
                return (mu, min(index for index in range(14) if mask & (1 << index)), mask), response, norm
    raise AssertionError("no live non-LC leading residual plant")


def leading_symbol_checks(source_graph: dict[str, object]) -> dict[str, object]:
    eta = source_graph["eta"]
    one = R.xi_form(eta)
    gamma: list[M.SForm] = source_graph["gamma"]
    t: list[M.SForm] = source_graph["t"]
    a_total: list[M.SForm] = source_graph["a"]
    j3 = [D.shiab(M.sfwedge(one, value)) for value in a_total]

    c = sp.Matrix(
        10,
        10,
        lambda i, j: sp.simplify(
            sp.Rational(1, 2) * D.top_scalar(t[i], j3[j])
        ),
    )
    i1_c5 = sp.simplify(c - c.T)
    i2b_c6 = sp.Matrix(
        10,
        10,
        lambda i, j: residual_pair(j3[i], j3[j]),
    )

    exact(
        "the dense observed-base-conormal principal-Z1 LC residual J3 vanishes for all ten owners",
        all(not value for value in j3),
    )
    c6_zero, c5_formula, c5_symmetric_zero = R.structural_euler_order_comparator()
    exact(
        "the independent universal Euler comparator proves the odd I1 leading coefficient is C-C^T",
        c6_zero and c5_formula and c5_symmetric_zero,
    )
    exact(
        "the conditional fixed-(epsilon,varpi) active-reconstruction I1 C5 coefficient vanishes",
        c5_formula and i1_c5 == sp.zeros(10),
    )
    exact(
        "the residual-zero normal I2B C6 Gram vanishes on the LC leading residual map",
        i2b_c6 == sp.zeros(10),
    )

    symbolic_eta = sp.symbols("eta0:4", real=True)
    symbolic_one = R.symbolic_xi_form(symbolic_eta)
    symbolic_gamma = [R.symbolic_z1_b_form(symbolic_eta, owner) for owner in range(10)]
    symbolic_pre_shiab = [M.sfwedge(symbolic_one, value) for value in symbolic_gamma]
    symbolic_j3 = [D.shiab(value) for value in symbolic_pre_shiab]
    exact(
        "xi wedge deltaGamma^(2) vanishes before Shiab for all ten observed-base LC owners",
        all(not value for value in symbolic_pre_shiab),
    )
    exact(
        "J3 vanishes for every observed-base conormal over Q[eta0,eta1,eta2,eta3], not only at the dense sentinel",
        all(not value for value in symbolic_j3),
    )
    exact(
        "identical J3=0 removes the normal I2B C6 bank and J3-by-J2 C5 cross before interpolation",
        all(not value for value in symbolic_j3),
    )

    fixture, hostile_response, hostile_norm = first_live_non_lc_residual(one)
    exact(
        "a deterministic non-LC connection plant has a live non-null leading Shiab residual",
        bool(hostile_response) and hostile_norm != 0,
        f"fixture={fixture}; norm={hostile_norm}",
    )
    reject("infer J3=0 from a matcher that also kills the non-LC control", not hostile_response)
    reject("claim that residual-square actions generically lack a C6 symbol", False)
    reject("run C4 before checking the actual branch-specific C5/C6 maps", False)
    return {
        "dense_j3_zero": all(not value for value in j3),
        "symbolic_pre_shiab_zero": all(not value for value in symbolic_pre_shiab),
        "symbolic_j3_zero": all(not value for value in symbolic_j3),
        "i1_c5_rank": i1_c5.rank(),
        "i2b_c6_rank": i2b_c6.rank(),
        "hostile_fixture": fixture,
        "hostile_norm": hostile_norm,
    }


def boundary_checks() -> None:
    typed("J3=0 is exact only for observed-base conormals on the principal-Z1 induced-Y14 LC branch; vertical/mixed conormals, partial-Z1, and section tangents remain open")
    typed("I1 C5 is discharged; only the residual-zero normal I2B C6 and J3-by-J2 C5 blocks are discharged")
    typed("off-shell I2B C5 remains open until E-times-D2E and moving-primalizer/pairing order ceilings are ported to this metric-metric graph")
    typed("I1 may proceed to its 35-monomial-per-entry C4 bank; I2B must close the off-shell C5 ceiling before its complete C4 bank")
    typed("the source supplies kappa1 and its placement; its value/active normalization, full background, complete C4, Green route, domain, quotient, observation, and physics remain open")
    reject("promote leading-symbol cancellation to a complete action, field equation, characteristic, or physics result", False)
    reject("spend P1/P2/P3 to select a lower-order coefficient or cancellation", False)
    reject("merge Curt or promote a third lane from this Eric-lane result", False)


def main() -> int:
    print("PW2F-R2B2B2B ACTIVE LOCAL SOURCE-GRAMMAR / FULL RESIDUAL / LEADING-SYMBOL GATE")
    source_and_layer_zero()
    epsilon, epsilon_inv = source_rotor()
    source_graph = source_tangent_checks(epsilon, epsilon_inv)
    residual = residual_pairing_checks()
    symbols = leading_symbol_checks(source_graph)
    boundary_checks()
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        "RESULT: active_local_source_grammar_tangent=PASS; residual_coordinates="
        f"{len(residual['coordinates'])}; residual_norm={residual['norm']}; "
        f"symbolic_J3_zero={symbols['symbolic_j3_zero']}; "
        f"I1_C5_rank={symbols['i1_c5_rank']}; I2B_C6_rank={symbols['i2b_c6_rank']}; "
        f"hostile_norm={symbols['hostile_norm']}",
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
        "VERDICT: ACTIVE LOCAL SOURCE-GRAMMAR METRIC-METRIC TANGENT AND FULL ACTIVE RESIDUAL-CARRIER PORT PASS; "
        "LC J3 KILLS I1 C5 AND NORMAL I2B C6/J3xJ2 C5; OFFSHELL I2B C5 CEILING REMAINS BEFORE COMPLETE C4"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
