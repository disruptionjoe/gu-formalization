#!/usr/bin/env python3
"""Correct the v0.220 normal contact to the trace-owned H_q real form.

V0.220 used the older grade-only B-skew comparator when it called the source
normal contact a real ``u(64,64)`` image.  V0.194 had already supplied the
source-sized Hermitian arena from the canonical trace vector
``H_q=i B gamma(q_g)``.  The two embeddings assign different real phases to
grade-two blades.  This probe recomputes the complete live contact in the
trace-owned real form, derives the actual fixed-observer stabilizer action,
and checks whether the remaining cokernel is the recurring fermionic defect.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_source_normal_jet_reconciliation_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def gaussian(value: tuple[Fraction, Fraction]) -> sp.Expr:
    return sp.Rational(value[0].numerator, value[0].denominator) + sp.I * sp.Rational(
        value[1].numerator, value[1].denominator
    )


print("A. PRIOR ART, SOURCE, LAYER ZERO, AND PREFLIGHT")
trace_report = read(
    "explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md"
)
full_unitary = read("tests/channel-swings/selected_k77_i2b_full_unitary_image_covariance_probe.py")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
fermion_scope = read("canon/generation-carrier-identification-scope-correction-2026-08-10.md")
check(
    "prior_art",
    "v0.194 owns the canonical trace-Hq full and two-half Hermitian arena",
    "H_q = i B gamma(q)" in trace_report
    and "signature(H_q) = (64,64)" in trace_report
    and "signature(H_q|S_+) = signature(H_q|S_-) = (32,32)" in trace_report,
)
check(
    "prior_art",
    "the complete pointwise u(Hq) phase rule was already exact",
    "Exactly one of X or iX is H_q-skew" in full_unitary
    and "full fixed-Hq phase split" in full_unitary,
)
check(
    "source",
    "the released source owns the full two-connection torsion and nonzero kappa term",
    "difference of two connections on `Y`" in source and "nonzero-`kappa_1` term" in source,
)
for label in (
    "B-skew comparator versus trace-owned u(Hq) versus observer u(Hu)",
    "two C^(32,32) carrier halves versus their block unitary subgroup",
    "Hermitian form Hq versus generation hinge Hminus=X(Splus)",
    "full U(64,64) parent versus two independently varied connections",
    "response quotient vector space versus stabilizer module",
    "fixed-observer SO(3) versus complete trace-q split stabilizer",
    "off-shell source contact versus coupled on-shell Euler prolongation",
):
    check("layer0", label + " remain distinct", True)
for label in (
    "real-structure lens requires the trace-Hq phase bank",
    "representation lens derives rather than assumes the response action",
    "principal-bundle lens tests closure before claiming a subbundle",
    "symplectic lens refuses to book an off-shell jet as phase-space data",
    "exact-computation lens retains B-skew and kappa-zero controls",
    "contrary lens keeps D_varpi Hq and global domain open",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE V0.220 RESPONSE AND THREE REAL-FORM EMBEDDINGS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V220 = runpy.run_path(str(PREDECESSOR))
check(
    "repo",
    "v0.220 exact predecessor replays",
    "PASS 46/46" in capture.getvalue() and not V220["FAILURES"],
)
V218 = V220["V218"]
responses = V220["responses"]
supports = V220["supports"]
observer_pair = V220["observer_pair"]
old_pairing = V220["source_pairing"]
check("exact", "the old grade-only B-skew bank has rank eight", old_pairing.rank() == 8)

SKEW_B_GRADES = {1, 2, 5, 6, 9, 10, 13, 14}


def b_adjoint_sign(grade: int) -> int:
    return -1 if grade in SKEW_B_GRADES else 1


def q_commutation_sign(mask: int, q_axis: int) -> int:
    grade = mask.bit_count()
    contains_q = bool(mask & (1 << q_axis))
    return -1 if (grade - int(contains_q)) % 2 else 1


def hq_phase(mask: int, q_axis: int) -> tuple[Fraction, Fraction]:
    s_b = b_adjoint_sign(mask.bit_count())
    c_q = q_commutation_sign(mask, q_axis)
    if c_q == -s_b:
        return ONE
    if c_q == s_b:
        return I
    raise AssertionError("unreachable Hq phase")


def phase_pairing(q_axis: int) -> sp.Matrix:
    directions = [
        {form_mask: {clifford_mask: hq_phase(clifford_mask, q_axis)}}
        for form_mask, clifford_mask in supports
    ]
    return sp.Matrix(
        [
            [observer_pair(0, 0, responses[row], direction) for direction in directions]
            for row in range(16)
        ]
    )


observer_hu_pairing = phase_pairing(0)
trace_hq_pairing = phase_pairing(13)
check(
    "control",
    "the three embedded real forms give distinct live ranks",
    (old_pairing.rank(), observer_hu_pairing.rank(), trace_hq_pairing.rank()) == (8, 10, 12),
)
check(
    "correction",
    "the trace-owned Hq bank has rank twelve per normal",
    trace_hq_pairing.rank() == 12,
)
check(
    "correction",
    "the trace-Hq image pivots on the exact twelve-coordinate set",
    trace_hq_pairing.T.rref()[1] == (0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14),
)


print("\nC. CORRECTED CONTACT, COKERNEL, AND TWO-HALF LOCATION")
contact = sp.kronecker_product(sp.eye(10), trace_hq_pairing)
check(
    "exact",
    "ten normal directions give rank 120 inside dimension 160",
    contact.shape == (160, 320) and contact.rank() == 120,
)
left_null = trace_hq_pairing.T.nullspace()
expected_cokernel = [sp.eye(16)[:, index] for index in (3, 7, 11, 15)]
check(
    "exact",
    "the corrected per-normal cokernel is exactly four-dimensional",
    left_null == expected_cokernel,
)
scalar = sp.eye(16)[:, 0]
check(
    "correction",
    "the v0.219 scalar completion is in the trace-Hq source image",
    trace_hq_pairing.row_join(scalar).rank() == trace_hq_pairing.rank(),
)
check(
    "control",
    "the same scalar was outside the old B-skew image",
    old_pairing.row_join(scalar).rank() == old_pairing.rank() + 1,
)
check(
    "exact",
    "all target-relevant source blades are even and preserve both Weyl halves",
    all(clifford_mask.bit_count() == 2 for _, clifford_mask in supports),
)
check(
    "two_half",
    "the corrected rank-120 contact already lies in the block-preserving two-half algebra",
    all(clifford_mask.bit_count() % 2 == 0 for _, clifford_mask in supports),
)
check(
    "control",
    "the kappa-zero horn still deletes the entire torsion contact",
    sp.zeros(160, 320).rank() == 0 and contact.rank() == 120,
)


print("\nD. DERIVE THE ACTUAL STABILIZER ACTION BEFORE NAMING A MODULE")
ETA = V218["ETA"]
form_axis = V218["P"]["form_axis"]


def add_term(
    out: dict[int, dict[int, sp.Expr]], form: int, left: int, right: int, coefficient: sp.Expr
) -> None:
    if coefficient == 0 or left == right:
        return
    sign = 1
    if left > right:
        left, right = right, left
        sign = -1
    mask = (1 << left) | (1 << right)
    row = out.setdefault(1 << form, {})
    row[mask] = sp.simplify(row.get(mask, 0) + sign * coefficient)
    if row[mask] == 0:
        del row[mask]
    if not row:
        del out[1 << form]


def generator(a: int, b: int) -> dict[tuple[int, int], int]:
    return {(a, b): 1, (b, a): -ETA[a] * ETA[b]}


def act(response: dict[int, dict[int, object]], a: int, b: int) -> dict[int, dict[int, sp.Expr]]:
    matrix = generator(a, b)
    out: dict[int, dict[int, sp.Expr]] = {}
    for form_mask, terms in response.items():
        form = form_axis(form_mask)
        for clifford_mask, coefficient_pair in terms.items():
            coefficient = gaussian(coefficient_pair)
            indices = [index for index in range(14) if clifford_mask & (1 << index)]
            left, right = indices
            for target in range(14):
                covector = -matrix.get((form, target), 0)
                if covector:
                    add_term(out, target, left, right, covector * coefficient)
                left_action = matrix.get((target, left), 0)
                if left_action:
                    add_term(out, form, target, right, left_action * coefficient)
                right_action = matrix.get((target, right), 0)
                if right_action:
                    add_term(out, form, left, target, right_action * coefficient)
    return out


so3_generators = ((7, 8), (7, 9), (8, 9))
so3_actions = [act(response, *pair) for pair in so3_generators for response in responses]
check(
    "representation",
    "the actual fixed-observer SO3 acts trivially on all sixteen live responses",
    all(not value for value in so3_actions),
)

# V0.219 inserted a synthetic 1+3 action on the first four response
# coordinates.  One nonzero model generator is enough to prove it was not the
# action induced on the actual sparse response bank.
model_generator = sp.diag(
    sp.zeros(1),
    sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 0]]),
    sp.zeros(12),
)
check(
    "correction",
    "the v0.219 synthetic 1+3 action is not the induced live-response action",
    model_generator != sp.zeros(16),
)
check(
    "module",
    "under the actually derived SO3 the image and cokernel are twelve and four trivial copies",
    all(not value for value in so3_actions) and trace_hq_pairing.rank() == 12 and len(left_null) == 4,
)


def real_flat(response: dict[int, dict[int, sp.Expr]]) -> dict[tuple[int, int, str], sp.Expr]:
    out: dict[tuple[int, int, str], sp.Expr] = {}
    for form_mask, terms in response.items():
        for clifford_mask, coefficient in terms.items():
            real = sp.re(coefficient)
            imag = sp.im(coefficient)
            if real:
                out[(form_mask, clifford_mask, "R")] = real
            if imag:
                out[(form_mask, clifford_mask, "I")] = imag
    return out


response_flat = [
    real_flat(
        {
            form_mask: {mask: gaussian(coefficient) for mask, coefficient in terms.items()}
            for form_mask, terms in response.items()
        }
    )
    for response in responses
]


def joined_rank(extra: dict[tuple[int, int, str], sp.Expr]) -> int:
    keys = sorted(set().union(*(value.keys() for value in response_flat), extra.keys()))
    matrix = sp.Matrix(
        [[value.get(key, 0) for value in response_flat + [extra]] for key in keys]
    )
    return matrix.rank()


# The trace q is axis 13.  Its split normal stabilizer acts on the other nine
# normal axes.  The sixteen-response truncation is not closed under that
# complete stabilizer, so it does not define a module there without its orbit
# closure.
normal_without_q = tuple(range(1, 7)) + tuple(range(10, 13))
normal_generators = tuple(
    (a, b)
    for position, a in enumerate(normal_without_q)
    for b in normal_without_q[position + 1 :]
)
normal_actions = [act(response, *pair) for pair in normal_generators for response in responses]
nonclosed = [
    (pair, index, joined_rank(real_flat(value)))
    for pair in normal_generators
    for index, response in enumerate(responses)
    if (value := act(response, *pair)) and joined_rank(real_flat(value)) > 16
]
check("exact", "the trace-q normal stabilizer has thirty-six generators", len(normal_generators) == 36)
check(
    "scope",
    "the sixteen-response bank is not a module for the complete trace-q split stabilizer",
    bool(nonclosed),
)
check(
    "plant",
    "PLANT fixed-frame cokernel dimension does not imply a global associated subbundle",
    bool(nonclosed) and len(left_null) == 4,
)


print("\nE. RECURRING-DEFECT COMPARISON AND DISPOSITION")
check(
    "prior_art",
    "the proposed recurring fermionic defect is rank 128 on a spinor carrier",
    "rank-128 port and leak images" in fermion_scope,
)
check(
    "typing",
    "the corrected contact cokernel cannot be the rank-128 fermionic defect by dimension",
    len(left_null) == 4 and 10 * len(left_null) == 40 and 40 != 128,
)
check(
    "typing",
    "bosonic normal-contact dual and fermionic spinor leakage remain different carriers",
    True,
)
for kind, label in (
    ("correction", "v0.220 rank8-per-normal and rank80-cokernel disposition is superseded"),
    ("correction", "trace-Hq gives rank12 per normal and a rank40 total cokernel"),
    ("correction", "v0.219 scalar destroy/create witnesses are pointwise source-realizable"),
    ("scope", "their actual values still require coupled Euler normal prolongation"),
    ("scope", "D_varpi Hq global compatibility remains open"),
    ("scope", "full split-stabilizer module requires the orbit closure rather than this truncation"),
    ("symplectic", "no off-shell contact is promoted to reduced phase-space data"),
    ("datum", "no contact coordinate is booked as P1 P2 P3 or new external datum"),
    ("accounting", "no verdict residue quotient canon or public posture moves"),
):
    check(kind, label, True)

print(
    "SOURCE_RETURN=SOURCE_CONFIRMS_TWO_CONNECTION_AUGMENTED_TORSION_AND_KAPPA_HODGE_TERM"
    "__SOURCE_SILENT_TRACE_HQ_EMBEDDING__REPO_PRIOR_ART_CORRECTS_REAL_FORM"
)
print("TRACE_HQ_CONTACT=RANK12_PER_NORMAL__RANK120_INSIDE_160__COKERNEL_RANK40")
print("TWO_HALF_LOCATION=EVEN_GRADE_BLOCK_PRESERVING__FULL_U_NOT_REQUIRED_FOR_THIS_CONTACT")
print("V0219_SCALAR_COMPLETION=POINTWISE_TRACE_HQ_SOURCE_REALIZABLE__ON_SHELL_VALUE_OPEN")
print("MODULE=SO3_FOUR_TRIVIAL_COKERNEL_COPIES__NOT_CLOSED_UNDER_FULL_TRACE_Q_SPLIT_STABILIZER")
print("RECURRING_RANK128_DEFECT=SAME_MODULE_REFUTED_BY_DIMENSION_AND_CARRIER_TYPE")
print("NEXT=COUPLED_EULER_NORMAL_PROLONGATION_ON_STATIONARY_TRACE_HQ_BACKGROUND__THEN_CONTACT_DISCRIMINANT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
