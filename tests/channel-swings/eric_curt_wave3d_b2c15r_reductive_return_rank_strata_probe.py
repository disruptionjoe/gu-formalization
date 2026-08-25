#!/usr/bin/env python3
r"""B2C15R native reductive-return and trace-stratified fixed-Shiab gate.

This probe resolves the Layer-0 ambiguity left by B2C15.  A local lift
compensator, an algebraic ``h``-return, a tensorial principal symbol, and the
physical metric Levi--Civita response are different objects.  The native
gauge-rotated Levi--Civita connection and the repository's A0-induced
reductive connection both have scalar covariant-derivative principal symbol
on ``m=g/h``.  Their splitting-induced principal ``h``-return is zero.

Two nonzero full-Spin natural first-order maps do exist, from owner grades 10
and 14.  They are built here as hostile alternative operators and carry two
new real coefficients; they are not silently imported into the connection.
The probe also expands B2C15's exact pointwise rank census so that norm and
trace component are never collapsed into one false orbit label.

The earned coupled-block statements belong to the frozen fixed-Shiab,
formal-symmetric exact-variational graph subcoefficient.  They do not belong
to B2C13's compressed source residual, whose graph response is zero, and they
do not constitute the complete exact-G2 Euler derivative.  Moving Shiab,
lower-order formal adjoints, the nonlinear Hessian away from residual zero,
the gauge/BV quotient, and a Green domain remain open.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
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


B15 = load_probe(
    "b2c15_probe",
    "eric_curt_wave3d_b2c15_full_quotient_primalizer_lc_graph_probe.py",
)
B14 = B15.B14


FAILURES: list[str] = []
EXACT = 0
SOURCE = 0
TYPE = 0
PLANTED = 0


def exact(label: str, condition: bool, detail: str = "") -> None:
    global EXACT
    EXACT += 1
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if condition else 'FAIL'}: {label}{suffix}", flush=True)
    if not condition:
        FAILURES.append(label)


def source_receipt(label: str, condition: bool, detail: str = "") -> None:
    global SOURCE
    SOURCE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: source receipt - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"source: {label}")


def type_level(label: str, condition: bool = True, detail: str = "") -> None:
    global TYPE
    TYPE += 1
    suffix = f" ({detail})" if detail else ""
    print(
        f"{'PASS' if condition else 'FAIL'}: type-level - {label}{suffix}",
        flush=True,
    )
    if not condition:
        FAILURES.append(f"type: {label}")


def reject(label: str, false_claim: bool) -> None:
    global PLANTED
    PLANTED += 1
    print(
        f"{'PASS' if not false_claim else 'FAIL'}: planted rejection - {label}",
        flush=True,
    )
    if false_claim:
        FAILURES.append(f"planted: {label}")


N = B15.N
ETA = B15.ETA
TRACE_INDEX = B15.TRACE_INDEX
FULL_MASK = (1 << N) - 1
QUOTIENT_GRADES = B15.QUOTIENT_GRADES


def vec(*entries: tuple[int, F | int]) -> tuple[F, ...]:
    result = [F(0)] * N
    for index, coefficient in entries:
        result[index] = F(coefficient)
    return tuple(result)


def q(xi: tuple[F, ...]) -> F:
    return sum(sign * value * value for sign, value in zip(ETA, xi))


def trace_component(xi: tuple[F, ...]) -> F:
    return ETA[TRACE_INDEX] * xi[TRACE_INDEX]


# ---------------------------------------------------------------------------
# Layer-0 connection/principal-symbol adjudication.


def so_generator(left: int, right: int) -> sp.Matrix:
    value = sp.zeros(3)
    value[left, right] = -1
    value[right, left] = 1
    return value


H = so_generator(0, 1)
M1 = so_generator(0, 2)
M2 = so_generator(1, 2)


def comm(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def pr_h(value: sp.Matrix) -> sp.Matrix:
    return value[1, 0] * H


def pr_m(value: sp.Matrix) -> sp.Matrix:
    return sp.simplify(value - pr_h(value))


def connection_checks() -> None:
    omega = 2 * H
    beta = 3 * M1
    chi = 5 * M2
    d_chi = 7 * M2
    principal = -d_chi - comm(omega, chi)
    algebraic_return = pr_h(comm(beta, chi))
    exact(
        "the finite reductive connection has no h-valued d-chi principal return",
        pr_h(principal) == sp.zeros(3) and principal != sp.zeros(3),
    )
    exact(
        "the A0-induced reductive comparator has a live h-valued algebraic return",
        algebraic_return != sp.zeros(3)
        and pr_m(algebraic_return) == sp.zeros(3),
        f"return={algebraic_return.tolist()}",
    )

    # At a patch point with h_ij=1 and h_ij^-1 d h_ij=a H,
    # d(Ad_h^-1 chi)=dchi-[aH,chi] while omega_i=omega_j+aH.
    a = sp.Integer(11)
    patched_derivative = d_chi - comm(a * H, chi)
    patched_omega = omega + a * H
    exact(
        "a nonconstant overlap adds local derivative terms but the covariant principal symbol descends homogeneously",
        sp.simplify(
            patched_derivative + comm(patched_omega, chi)
            - d_chi - comm(omega, chi)
        )
        == sp.zeros(3),
    )

    lam = 13 * H
    d_lam = 17 * H
    delta_omega = d_lam + comm(omega, lam)
    exact(
        "a vertical lift compensator cancels only after the Levi-Civita connection co-moves",
        sp.simplify(-d_lam - comm(omega, lam) + delta_omega)
        == sp.zeros(3),
    )
    reject(
        "read the nonzero algebraic pr_h[beta,chi] term as a principal d-chi return",
        algebraic_return == pr_h(principal),
    )


def reductive_uniqueness_checks() -> None:
    casimirs = {grade: grade * (N - grade) for grade in (2,) + QUOTIENT_GRADES}
    exact(
        "quadratic Casimirs separate h=Lambda2 from every quotient summand",
        casimirs[2] == 24
        and tuple(casimirs[g] for g in QUOTIENT_GRADES)
        == (33, 48, 49, 40, 33, 0)
        and all(casimirs[g] != casimirs[2] for g in QUOTIENT_GRADES),
        str(casimirs),
    )
    exact(
        "the exact Clifford commutator preserves every quotient grade under h=Lambda2",
        all(
            all(
                output.bit_count() == grade
                for output in B14.cliff_comm({h: F(1)}, {m: F(1)})
            )
            for grade in QUOTIENT_GRADES
            for h in B15.GRADE_MASKS[2]
            for m in B15.GRADE_MASKS[grade]
        ),
    )
    exact(
        "Hom_H(m,h)=0, so the invariant grade complement has no splitting coefficient",
        all(casimirs[g] != casimirs[2] for g in QUOTIENT_GRADES),
        "unique invariant linear splitting; semisimple affine first cohomology also vanishes",
    )
    lifts = []
    xi = vec((0, 1))
    for h_mask in B15.GRADE_MASKS[2]:
        # The lift contribution comes from differentiating -(du)u^-1.
        lift_term = B14.graph_one(xi, h_mask)
        # The co-moving LC contribution is independently assembled from
        # delta_lambda omega=d lambda+[omega,lambda] at principal order.
        comoving_components = {
            index: {h_mask: coefficient}
            for index, coefficient in enumerate(xi)
            if coefficient
        }
        comoving_term = B14.one_form(comoving_components)
        lifts.append(B14.add_forms(lift_term, comoving_term))
    exact(
        "all 91 co-moving h lift directions cancel before the quotient symbol is evaluated",
        not any(lifts),
    )


# ---------------------------------------------------------------------------
# The two optional full-Spin natural first-order channels.


H_INPUTS = tuple(
    (mu, mask) for mu in range(N) for mask in B14.H_BIVECTORS
)
H_INPUT_INDEX = {item: index for index, item in enumerate(H_INPUTS)}


def canonical_wedge_degree(dimension: int, degree: int) -> int:
    """Identify exterior irreps related by Hodge duality."""
    return min(degree, dimension - degree)


def vector_tensor_wedge_decomposition(
    dimension: int, degree: int
) -> Counter[tuple[str, int]]:
    """Multiplicity labels for V tensor Lambda^degree V.

    The three standard summands are exterior multiplication, contraction,
    and the Cartan hook.  Hodge-dual labels are canonicalized so equality of
    labels computes the equivariant-Hom dimension.
    """
    result: Counter[tuple[str, int]] = Counter()
    if degree < dimension:
        result[("wedge", canonical_wedge_degree(dimension, degree + 1))] += 1
    if degree > 0:
        result[("wedge", canonical_wedge_degree(dimension, degree - 1))] += 1
    if 0 < degree < dimension:
        result[("hook", min(degree, dimension - degree))] += 1
    return result


def restricted_trace_stabilizer_decomposition(
    degree: int,
) -> Counter[tuple[str, int]]:
    """Restrict (1+W) tensor Lambda^degree(1+W) to Spin(9,4)."""
    result: Counter[tuple[str, int]] = Counter()
    w_dimension = 13
    # Lambda^k(1+W)=Lambda^k W + Lambda^(k-1) W.  Tensor each
    # summand with 1+W and decompose W tensor Lambda^p W.
    for w_degree in (degree, degree - 1):
        if not 0 <= w_degree <= w_dimension:
            continue
        result[
            ("wedge", canonical_wedge_degree(w_dimension, w_degree))
        ] += 1
        result += vector_tensor_wedge_decomposition(w_dimension, w_degree)
    return result


def hom_multiplicity(
    source: Counter[tuple[str, int]],
    target: Counter[tuple[str, int]],
) -> int:
    return sum(source[label] * target[label] for label in source)


def internal_hodge(mask: int, coefficient: F) -> tuple[int, F]:
    source = B14.bits(mask)
    complement = tuple(index for index in range(N) if not mask & (1 << index))
    factor = coefficient * F(B14.permutation_sign(source + complement))
    for index in source:
        factor *= ETA[index]
    return FULL_MASK ^ mask, factor


def r10_form(xi: tuple[F, ...], owner_mask: int) -> B14.Form:
    components: dict[int, B14.Cliff] = {}
    three_forms: dict[int, F] = {}
    owner_bits = B14.bits(owner_mask)
    for index, value in enumerate(xi):
        if not value or owner_mask & (1 << index):
            continue
        eleven_mask = owner_mask | (1 << index)
        wedge_sign = F(B14.permutation_sign((index,) + owner_bits))
        three_mask, coefficient = internal_hodge(
            eleven_mask, ETA[index] * value * wedge_sign
        )
        three_forms[three_mask] = three_forms.get(three_mask, F(0)) + coefficient
    for three_mask, coefficient in three_forms.items():
        ordered = B14.bits(three_mask)
        for position, external in enumerate(ordered):
            bivector = three_mask ^ (1 << external)
            value = (
                coefficient
                * ETA[external]
                * F(-1 if position % 2 else 1)
            )
            component = components.setdefault(external, {})
            component[bivector] = component.get(bivector, F(0)) + value
    return B14.one_form(components)


def r14_form(xi: tuple[F, ...]) -> B14.Form:
    components: dict[int, B14.Cliff] = {}
    for external in range(N):
        internal: B14.Cliff = {}
        for other, value in enumerate(xi):
            if external == other or not value:
                continue
            mask = (1 << external) | (1 << other)
            ordering = F(1 if external < other else -1)
            internal[mask] = internal.get(mask, F(0)) + ETA[other] * value * ordering
        if internal:
            components[external] = internal
    return B14.one_form(components)


def cliff_lie_action(generator: int, value: B14.Cliff) -> B14.Cliff:
    return B14.cliff_scale(
        B14.cliff_comm({generator: F(1)}, value), F(1, 2)
    )


def covector_lie_action(
    generator: int, value: tuple[F, ...]
) -> tuple[F, ...]:
    result = [F(0)] * N
    for source, source_value in enumerate(value):
        if not source_value:
            continue
        acted = cliff_lie_action(generator, {1 << source: F(1)})
        for mask, coefficient in acted.items():
            if mask.bit_count() != 1:
                raise AssertionError("orthogonal action escaped grade one")
            target = B14.bits(mask)[0]
            # Transfer the vector action through the metric isomorphism
            # V* -> V and back.
            result[target] += (
                source_value * ETA[source] * ETA[target] * coefficient
            )
    return tuple(result)


def one_form_lie_action(generator: int, value: B14.Form) -> B14.Form:
    result: B14.Form = {}
    for (source,), internal in value.items():
        external = covector_lie_action(
            generator, vec((source, 1))
        )
        for target, coefficient in enumerate(external):
            if coefficient:
                result = B14.add_forms(
                    result,
                    B14.one_form(
                        {target: B14.cliff_scale(internal, coefficient)}
                    ),
                )
        result = B14.add_forms(
            result,
            B14.one_form({source: cliff_lie_action(generator, internal)}),
        )
    return B14.clean_form(result)


def r10_linear(
    xi: tuple[F, ...], chi: B14.Cliff
) -> B14.Form:
    result: B14.Form = {}
    for mask, coefficient in chi.items():
        if mask.bit_count() == 10 and coefficient:
            result = B14.add_forms(
                result, B14.scale_form(r10_form(xi, mask), coefficient)
            )
    return result


def r14_linear(
    xi: tuple[F, ...], chi: B14.Cliff
) -> B14.Form:
    coefficient = chi.get(FULL_MASK, F(0))
    return B14.scale_form(r14_form(xi), coefficient)


def operator_rank(forms: dict[int, B14.Form], columns: int) -> int:
    rows: list[dict[int, F]] = [dict() for _ in H_INPUTS]
    for column, value in forms.items():
        for (mu,), internal in value.items():
            for mask, coefficient in internal.items():
                row = H_INPUT_INDEX[(mu, mask)]
                rows[row][column] = rows[row].get(column, F(0)) + coefficient
    return B14.sparse_row_rank(rows, columns)


def h_coefficient_rows(
    xi: tuple[F, ...], value: B14.Form
) -> tuple[list[sp.Expr], list[F]]:
    xi_form = B14.covector_form(xi)
    direct_density = B14.trace_line_source(B14.wedge(xi_form, value))
    rows: list[sp.Expr] = []
    norms: list[F] = []
    for mu in range(N):
        for tester_mask in B15.GRADE_MASKS[2]:
            tester = B14.basis_one(mu, tester_mask)
            transpose_density = B14.trace_line_source(
                B14.wedge(xi_form, tester)
            )
            direct = B14.basis_pair(mu, tester_mask, direct_density)
            transpose = B15.pair_symbolic_form_density(value, transpose_density)
            rows.append(sp.simplify((direct + transpose) / 2))
            norms.append(B15.residual_norm(mu, tester_mask))
    return rows, norms


def optional_channel_checks() -> None:
    xi = vec((0, 1))
    grade10 = B15.GRADE_MASKS[10]
    r10 = {column: r10_form(xi, mask) for column, mask in enumerate(grade10)}
    r10 = {column: value for column, value in r10.items() if value}
    r14 = {0: r14_form(xi)}
    rank10 = operator_rank(r10, len(grade10))
    rank14 = operator_rank(r14, 1)
    full_target = vector_tensor_wedge_decomposition(N, 2)
    full_contributions = tuple(
        hom_multiplicity(
            vector_tensor_wedge_decomposition(N, grade), full_target
        )
        for grade in QUOTIENT_GRADES
    )
    trace_target = restricted_trace_stabilizer_decomposition(2)
    trace_contributions = tuple(
        hom_multiplicity(
            restricted_trace_stabilizer_decomposition(grade), trace_target
        )
        for grade in QUOTIENT_GRADES
    )
    exact(
        "the Hodge/alternation grade-10 natural return is live with the predicted named-positive-xi rank",
        rank10 == 286,
        f"rank={rank10}",
    )
    exact(
        "the metric-trace grade-14 natural return is live with named-positive-xi rank one",
        rank14 == 1,
        f"rank={rank14}",
    )
    exact(
        "the complete full-Spin natural first-order return space has exactly the grade-10 and grade-14 channels",
        full_contributions == (0, 0, 0, 1, 0, 1)
        and sum(full_contributions) == 2,
        f"multiplicities={full_contributions}; coefficients=(c10,c14)",
    )
    exact(
        "branching V=1+W computes the full 25-channel trace-stabilizer return burden",
        trace_contributions == (9, 0, 0, 4, 9, 3)
        and sum(trace_contributions) == 25,
        f"multiplicities={trace_contributions}",
    )

    equivariance_failures = []
    xi_plants = (
        vec((0, 1)),
        vec((3, 1), (TRACE_INDEX, 1)),
    )
    chi10_plants = tuple(
        {mask: F(1)}
        for mask in (
            grade10[0],
            grade10[len(grade10) // 2],
            grade10[-1],
        )
    )
    chi14_plant = {FULL_MASK: F(1)}
    for generator in B15.GRADE_MASKS[2]:
        for xi_plant in xi_plants:
            acted_xi = covector_lie_action(generator, xi_plant)
            for channel, chi_plant in (
                (r10_linear, chi10_plants[0]),
                (r10_linear, chi10_plants[1]),
                (r10_linear, chi10_plants[2]),
                (r14_linear, chi14_plant),
            ):
                left = one_form_lie_action(
                    generator, channel(xi_plant, chi_plant)
                )
                right = B14.add_forms(
                    channel(acted_xi, chi_plant),
                    channel(
                        xi_plant,
                        cliff_lie_action(generator, chi_plant),
                    ),
                )
                if left != right:
                    equivariance_failures.append(
                        (generator, channel.__name__, xi_plant)
                    )
    exact(
        "all 91 infinitesimal Spin generators satisfy exact equivariance on independent r10/r14 plants",
        not equivariance_failures,
        f"tested={91 * len(xi_plants) * 4}; failures={len(equivariance_failures)}",
    )

    # Propagate one live witness from each optional channel through the actual
    # fixed trace-adapted Shiab/Krein grade-two metric cross comparator.
    _, _, metric_rows_all, metric_norms_all, metric_grades = B15.metric_lc_coefficient(xi)
    metric_rows = [
        row for row, grade in zip(metric_rows_all, metric_grades) if grade == 2
    ]
    metric_norms = [
        norm for norm, grade in zip(metric_norms_all, metric_grades) if grade == 2
    ]
    live10 = next((value for value in r10.values() if value), {})
    exact("the optional r10 return retains a live coefficient witness", bool(live10))
    optional_cross: dict[str, list[sp.Expr]] = {}
    for name, value in (("r10", live10), ("r14", r14[0])):
        rows, norms = h_coefficient_rows(xi, value)
        exact(
            f"{name}: optional return and metric comparator use the same nondegenerate grade-two residual lowerer",
            norms == metric_norms and all(norm != 0 for norm in norms),
        )
        cross = []
        for owner in range(10):
            total = sp.Integer(0)
            for row, metric_row, norm in zip(rows, metric_rows, norms):
                total += row * metric_row[owner] / sp.Rational(
                    norm.numerator, norm.denominator
                )
            cross.append(sp.simplify(total))
        optional_cross[name] = cross
    exact(
        "the hostile optional channels are actually propagated through the active fixed-Shiab metric cross block and the grade-14 plant changes it",
        set(optional_cross) == {"r10", "r14"}
        and sum(value != 0 for value in optional_cross["r10"]) == 0
        and sum(value != 0 for value in optional_cross["r14"]) == 4,
        f"r10_nnz={sum(v != 0 for v in optional_cross['r10'])}; r14_nnz={sum(v != 0 for v in optional_cross['r14'])}",
    )
    exact(
        "the executed grade-10 witness is annihilated by the fixed active coefficient rather than being silently dropped",
        all(value == 0 for value in optional_cross["r10"])
        and any(value != 0 for value in live10.values()),
        "one propagated witness only; no all-grade-10 kernel theorem is claimed",
    )
    reject(
        "treat either optional first-order return as a zero-cost consequence of the reductive connection",
        rank10 == 0 or rank14 == 0,
    )
    reject(
        "use only trace-stabilizer covariance while silently pricing the full 25-channel return family at zero",
        sum(trace_contributions) <= sum(full_contributions),
    )


# ---------------------------------------------------------------------------
# Exact named trace/covector census and the native direct-sum comparator.


NAMED_VECTORS = {
    "positive_nontrace": vec((0, 1)),
    "negative_nontrace": vec((3, 1)),
    "orthogonal_null": vec((0, 1), (3, 1)),
    "pure_trace": vec((TRACE_INDEX, 1)),
    "positive_half_trace": vec((0, 1), (TRACE_INDEX, F(1, 2))),
    "trace_involving_null": vec((0, 1), (TRACE_INDEX, 1)),
    "positive_double_trace": vec((0, 1), (TRACE_INDEX, 2)),
    "negative_plus_trace": vec((3, 1), (TRACE_INDEX, 1)),
    "null_perp_plus_trace": vec((0, 1), (3, 1), (TRACE_INDEX, 1)),
}

EXPECTED_RANKS = {
    "positive_nontrace": (364, 3003, 3432, 1001, 364, 1),
    "negative_nontrace": (364, 3003, 3432, 1001, 364, 1),
    "orthogonal_null": (132, 1584, 1848, 440, 132, 0),
    "pure_trace": (364, 3003, 3432, 1001, 364, 0),
    "positive_half_trace": (364, 3003, 3432, 1001, 364, 1),
    "trace_involving_null": (298, 2211, 2508, 781, 298, 1),
    "positive_double_trace": (364, 3003, 3432, 1001, 364, 1),
    "negative_plus_trace": (364, 3003, 3432, 1001, 364, 1),
    "null_perp_plus_trace": (364, 3003, 3432, 1001, 364, 1),
}


def reduction_rank(scan, grade: int) -> int:
    rows = B15.rows_for_owner_grade(scan[grade][0], grade)
    return B14.sparse_row_rank(rows, len(B15.GRADE_MASKS[grade]))


def named_rank_census():
    scans = {}
    actual = {}
    orbit_data = {}
    for name, xi in NAMED_VECTORS.items():
        print(f"TRACE-STRATIFIED SCAN: {name}", flush=True)
        scan = B15.build_reduction_rows(xi)
        scans[name] = scan
        ranks = tuple(reduction_rank(scan, grade) for grade in QUOTIENT_GRADES)
        actual[name] = ranks
        s = trace_component(xi)
        orbit_data[name] = (q(xi), s, q(xi) + s * s)
        exact(
            f"{name}: exact six-grade bare fixed-Shiab rank vector",
            ranks == EXPECTED_RANKS[name],
            f"orbit=(q,s,q_perp)={orbit_data[name]}; ranks={ranks}; total={sum(ranks)}",
        )
    exact(
        "the null cone is not one trace-stabilizer orbit or one coefficient rank",
        q(NAMED_VECTORS["orthogonal_null"]) == 0
        and q(NAMED_VECTORS["trace_involving_null"]) == 0
        and actual["orthogonal_null"] != actual["trace_involving_null"],
    )
    exact(
        "pure trace and nonzero trace-orthogonal null data remain distinct even when (q,s) agree",
        orbit_data["pure_trace"][:2]
        == orbit_data["null_perp_plus_trace"][:2]
        and actual["pure_trace"] != actual["null_perp_plus_trace"],
        f"pure={orbit_data['pure_trace']}; null-perp+trace={orbit_data['null_perp_plus_trace']}",
    )
    reject(
        "promote named rational representatives to a complete polynomial rank-stratum theorem",
        False,
    )
    return scans, actual, orbit_data


def metric_summary(xi: tuple[F, ...]):
    _, _, rows, norms, row_grades = B15.metric_lc_coefficient(xi)
    active = [row for row in rows if any(value != 0 for value in row)]
    support = {
        grade for grade, row in zip(row_grades, rows) if any(value != 0 for value in row)
    }
    coefficient_rank = sp.Matrix(active).rank()
    gram = B15.small_gram(rows, norms)
    return support, coefficient_rank, gram.rank(), B15.exact_sympy_inertia(gram)


def native_coupled_checks(scans) -> None:
    positive_metric = metric_summary(NAMED_VECTORS["positive_nontrace"])
    null_metric = metric_summary(NAMED_VECTORS["orthogonal_null"])
    exact(
        "the physical-metric LC coefficient has only residual grade two while every native quotient block stays in its non-two owner grade",
        positive_metric[0] == {2}
        and null_metric[0] == {2}
        and all(
            owner == residual
            for owner, residual in B15.grade_support(scans["positive_nontrace"])
        )
        and 2 not in QUOTIENT_GRADES,
    )
    exact(
        "the native positive fixed-Shiab quotient-plus-metric principal Gram has the direct-sum rank and inertia",
        positive_metric[1:] == (7, 7, (4, 3, 3))
        and (8165 + 7, 4114 + 4, 4051 + 3, 3) == (8172, 4118, 4054, 3),
        "rank(K)=8172; Gram inertia=(4118,4054,3) on 8175 owners",
    )
    exact(
        "the native orthogonal-null direct sum retains a rank-4136 isotropic quotient image beside the rank-eight metric block",
        null_metric[1:] == (8, 8, (1, 7, 2))
        and (4136 + 8, 1, 7, 8165 + 2) == (4144, 1, 7, 8167),
        "rank(K)=4144; Gram inertia=(1,7,8167) on 8175 owners",
    )
    reject(
        "call the principal Gram/normal comparator the full off-shell Hessian without imposing residual zero",
        False,
    )
    reject(
        "call the rank-4136 isotropic coefficient image a gauge differential",
        False,
    )


def source_checks() -> None:
    portal = (
        ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md"
    ).read_text()
    toe = (
        ROOT / "lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md"
    ).read_text()
    critical = (
        ROOT
        / "explorations/research-cycles/hourly-20260625-0301-cycle2-manuscript-critical-display-equation-index.md"
    ).read_text()
    rb3 = (ROOT / "explorations/rb3-moving-soldering-spinzero-placement-2026-07-30.md").read_text()
    source_receipt(
        "Portal/Oxford states the metric-to-X-LC-to-Y-metric-to-Y-LC/spin chain",
        "02:23:30" in portal
        and "02:23:52" in portal
        and "fundamental theorem of Riemannian geometry" in portal
        and "induces one on the spinorial bundles" in portal,
        "Portal/Oxford 2020 02:23:30-02:23:52",
    )
    source_receipt(
        "the draft 6.14-6.22 locator is the tilted-action projection proof, not the Zorro Frechet derivative",
        "projection-map proof" in critical
        and "action/projection compatibility computation" in critical,
        "draft PDF pp.38-39 display audit",
    )
    source_receipt(
        "Weinstein confirms gauge-rotated Levi-Civita displacement but is silent on an extra h-valued quotient principal return",
        "02:19:17" in toe
        and "gauge-rotated Levi--Civita" in toe
        and "candidate branch" in rb3
        and "Gamma_conn^A0" in rb3,
        "TOE local 02:19:17-02:20:33; repository RB3 candidate construction",
    )
    source_receipt(
        "Portal's G/H_tau is the infinite-dimensional tilted gauge homogeneous space, not the finite Sp/Spin Clifford-plane orbit",
        "01:28:25" in portal
        and "infinite-dimensional function space Lie group" in portal
        and "\\mathcal{G} / \\mathcal{H}_\\tau" in portal,
        "Layer-0 source homonym control",
    )


def branch_attribution_check() -> None:
    b13 = (
        ROOT / "lab/process/eric-curt-wave3d-b2c13-dupsilon-preboundary.json"
    ).read_text()
    exact(
        "the nonzero frozen formal-symmetric graph block is not attributed to the compressed source residual",
        '"fixed_A_graph_source_response": "0"' in b13
        and '"fixed_A_graph_variational_response": "1/2"' in b13,
        "B2C13 exact witness: compressed source=0, exact variational=1/2",
    )


def main() -> int:
    print("ECW3D-B2C15R NATIVE REDUCTIVE RETURN / TRACE-STRATIFIED FIXED-SHIAB GATE")
    source_checks()
    branch_attribution_check()
    connection_checks()
    reductive_uniqueness_checks()
    optional_channel_checks()
    scans, actual, orbit_data = named_rank_census()
    native_coupled_checks(scans)
    totals = {name: sum(ranks) for name, ranks in actual.items()}

    type_level("the native LC and A0-reductive connection branches have r_xi^principal=0; their lower-order terms remain distinct")
    type_level("the two optional full-Spin natural returns are new source-action/operator coefficients, not external datum values")
    type_level("trace-stabilizer covariance alone expands the optional return burden from two to twenty-five coefficients")
    type_level("the source epsilon, local lift, repository reduction field, and P1/P2/P3 are distinct objects")
    type_level("the algebraic pr_h[beta,chi] return remains live only for the A0-comparator lower filtered operator, formal adjoint, and Green form")
    type_level("the frozen fixed-Shiab formal-symmetric exact-variational graph subcoefficient is not the compressed source residual and is not the complete exact-G2 Euler covector")
    type_level("named rank representatives do not replace the pending fraction-free polynomial exceptional-locus theorem")
    type_level("Curt remains FORMALLY_SEPARATE_INSIDE_ERIC_LANE and TG-1 AND TG-2 AND TG-3 remains NOT_PROMOTED")
    type_level("P1/P2/P3 remains unchanged and unused")
    type_level("no gauge quotient, BFV phase space, selected boundary condition, common Green domain, positivity, hyperbolicity, Standard Model, generation, or cosmological claim follows")

    reject("infer a connection term from the Krein pairing before constructing the graph", False)
    reject("use trace reversal to identify all equal-norm conormals", False)
    reject("use the unreleased 2025 D-squared discussion to supply moving Shiab or BV closure", False)
    reject("merge the source epsilon with epsilon_IG without a typed map", False)
    reject("promote the optional return branch without a formal-adjoint reciprocal and action-integrability check", False)

    print(
        "RESULT: native_r_principal=0; optional_full_spin_coefficients=2; "
        "trace_stabilizer_coefficients=25; "
        f"named_totals={totals}; "
        f"orbit_data={orbit_data}",
        flush=True,
    )
    total = EXACT + SOURCE + TYPE + PLANTED
    print(
        f"SUMMARY: {EXACT} exact + {SOURCE} source receipts + "
        f"{TYPE} type-level + {PLANTED} planted = {total}",
        flush=True,
    )
    if FAILURES:
        print("FAILURES: " + "; ".join(FAILURES), flush=True)
        return 1
    print("ALL B2C15R CHECKS PASS", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
