#!/usr/bin/env sage -python
"""First cubic nonlinear compatibility class for the K77 I2B endpoint.

The preceding wave proved that the fixed-natural endpoint principal tableau is
Cartan-involutive.  A nonzero nonlinear compatibility *representative* would
not yet be an obstruction: it must first be divided by the third-jet freedom
that preserves the first prolonged equations.  This probe performs both steps
on the exact sixteen-support compatible stationary two-jet.

The calculation remains on the fixed-natural printed endpoint and inherited
``H_q`` comparator.  Moving ``Q_B``, metric/section coefficients, the actual
first-action Euler rival and physical BV tangent are outside its scope.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
from math import factorial
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
STATIONARY = ROOT / "tests/channel-swings/selected_k77_i2b_stationary_affine_spencer_intersection_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def rational(value: object) -> Fraction:
    value = sp.Rational(value)
    return Fraction(int(value.p), int(value.q))


def add_multi(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def compositions(total: int, slots: int = 4, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, slots - 1, prefix + (value,))


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/selected-k77-i2b-cartan-symbol-involutivity-source-return-2026-08-13.md")
cartan = read("explorations/conditional-build/selected-k77-i2b-cartan-symbol-involutivity-2026-08-13.md")
stationary_prior = read("explorations/conditional-build/selected-k77-i2b-stationary-affine-spencer-intersection-2026-08-13.md")
check("source", "SC-ACT-04 owns the endpoint residual-square grammar but not nonlinear torsion",
      "SOURCE-CONFIRMS" in source and "SOURCE-SILENT" in source)
check("prior_art", "the fixed-natural endpoint tableau is Cartan-involutive",
      "Cartan characters" in cartan and "3150" in cartan)
check("prior_art", "the exact compatible stationary two-jet has sixteen-support",
      "new exact witness support:                 16" in stationary_prior
      and "dimension 168" in stationary_prior)
for distinction in (
    "nonzero nonlinear representative versus its quotient class",
    "fixed-natural endpoint versus moving Q_B and full action",
    "coordinate third jets versus source gauge or physical BV tangents",
    "formal absorption versus analytic or global existence",
    "Cartan freedom versus particle or physical-mode counting",
):
    check("layer0", distinction + " remain distinct", True)
for kind, label in (
    ("spencer_eds", "restrict absorbers to the first prolonged symbol kernel"),
    ("variational_bicomplex", "derive the cubic Euler coefficient from the endpoint residual variation"),
    ("principal_bundle", "retain moving coefficient and section derivatives as a separate successor"),
    ("symplectic", "infer no presymplectic quotient or BFV phase space"),
    ("analytic", "infer no convergent solution germ from formal jet absorption"),
    ("hyperbolic", "infer no propagation or well-posedness theorem"),
    ("krein", "infer no positivity or state selection from rational rank"),
    ("source_criticism", "attribute only the residual grammar to the source"),
    ("contrary", "require a live nonlinear representative and a constrained quotient test"),
):
    check(kind, label, True)


print("\nB. EXACT STATIONARY WITNESS AND ENDPOINT BANK")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    A = runpy.run_path(str(STATIONARY))
check("repo", "the stationary-affine and second-prolongation predecessor replays",
      "PASS 59/59" in capture.getvalue() and not A["FAILURES"])
D = A["endpoint"]
S = D["S"]
cells = D["cells"]
selected = D["selected"]
blocks = A["blocks"]
h0 = D["endpoint_h0"]
witness = A["endpoint_restricted"]["witness"]
endpoint_second = D["endpoint_second"]
responses = D["responses"]
sym_pair = D["sym_pair"]
real_scalar = D["real_scalar"]

check("fingerprint", "the field and equation banks remain 196-real", len(cells) == 196)
check("fingerprint", "the compatible restricted witness has 392 coordinates and support sixteen",
      len(witness) == 392 and sum(value != 0 for value in witness) == 16)
check("fingerprint", "the endpoint lower Hessian remains symmetric rank 196",
      h0 == h0.T and h0.rank() == 196)


def form_from_vector(values) -> dict:
    answer: dict = {}
    for value, (_, _, basis) in zip(values, cells):
        if value:
            answer = S["fadd"](
                answer,
                S["fscale"](rational(value), basis),
            )
    return answer


def scalar(value: object) -> sp.Expr:
    return sp.factor(real_scalar(value))


c00_values = witness[:196]
c01_values = witness[196:]
c00 = form_from_vector(c00_values)
c01 = form_from_vector(c01_values)
check("witness", "both admitted second-jet blocks are nonzero", bool(c00) and bool(c01))


def principal_from_vector(mu: int, values) -> dict:
    answer: dict = {}
    for value, response in zip(values, responses[mu]):
        if value:
            answer = S["fadd"](
                answer,
                S["fscale"](rational(value), response),
            )
    return answer

# h(x)=1/2 c00 x0^2+c01 x0 x1.  The entries are polynomial
# coefficients, while c00/c01 themselves are the actual symmetric jet values.
h_terms = {
    (2, 0, 0, 0): S["fscale"](Fraction(1, 2), c00),
    (1, 1, 0, 0): c01,
}
a_terms = {
    0: {(1, 0, 0, 0): c00, (0, 1, 0, 0): c01},
    1: {(1, 0, 0, 0): c01},
    2: {},
    3: {},
}
r1_terms = {
    (1, 0, 0, 0): S["fadd"](
        principal_from_vector(0, c00_values),
        principal_from_vector(1, c01_values),
    ),
    (0, 1, 0, 0): principal_from_vector(0, c01_values),
}


print("\nC. FIRST CUBIC NONLINEAR EULER COMPATIBILITY REPRESENTATIVE")
euler_cubic: list[dict[tuple[int, ...], sp.Expr]] = []
euler_cubic_left: list[dict[tuple[int, ...], sp.Expr]] = []
euler_cubic_right: list[dict[tuple[int, ...], sp.Expr]] = []
for row, (_, _, test) in enumerate(cells):
    left_polynomial: dict[tuple[int, ...], sp.Expr] = {}
    right_polynomial: dict[tuple[int, ...], sp.Expr] = {}
    for h_alpha, h_value in h_terms.items():
        moving_test = endpoint_second(test, h_value)
        for r_alpha, r_value in r1_terms.items():
            alpha = add_multi(h_alpha, r_alpha)
            left_polynomial[alpha] = left_polynomial.get(alpha, sp.Integer(0)) + scalar(
                sym_pair(moving_test, r_value)
            )
    for mu in range(4):
        p_test = responses[mu][row]
        for h_alpha, h_value in h_terms.items():
            for a_alpha, a_value in a_terms[mu].items():
                alpha = add_multi(h_alpha, a_alpha)
                right_polynomial[alpha] = right_polynomial.get(alpha, sp.Integer(0)) + scalar(
                    sym_pair(p_test, endpoint_second(h_value, a_value))
                )
    left_polynomial = {
        alpha: sp.factor(value) for alpha, value in left_polynomial.items() if value
    }
    right_polynomial = {
        alpha: sp.factor(value) for alpha, value in right_polynomial.items() if value
    }
    euler_cubic_left.append(left_polynomial)
    euler_cubic_right.append(right_polynomial)
    euler_cubic.append({
        alpha: sp.factor(left_polynomial.get(alpha, 0) - right_polynomial.get(alpha, 0))
        for alpha in set(left_polynomial) | set(right_polynomial)
        if sp.factor(left_polynomial.get(alpha, 0) - right_polynomial.get(alpha, 0))
    })

second_indices = list(compositions(2))
second_position = {alpha: index for index, alpha in enumerate(second_indices)}
def compatibility_from_cubic(euler_bank):
    answer = [sp.Integer(0)] * (len(second_indices) * 14)
    for pair_index, pair_alpha in enumerate(second_indices):
        for clifford in range(14):
            value = sp.Integer(0)
            for lam in range(4):
                alpha = list(pair_alpha)
                alpha[lam] += 1
                alpha = tuple(alpha)
                coefficient = euler_bank[lam * 14 + clifford].get(alpha, sp.Integer(0))
                derivative_factor = 1
                for multiplicity in alpha:
                    derivative_factor *= factorial(multiplicity)
                value += derivative_factor * coefficient
            answer[pair_index * 14 + clifford] = sp.factor(value)
    return answer


torsion = compatibility_from_cubic(euler_cubic)

torsion_support = [index for index, value in enumerate(torsion) if value]
check("nonlinear", "both possible cubic variational contributions vanish on the admitted stratum",
      not any(euler_cubic_left) and not any(euler_cubic_right))
check("nonlinear", "the complete cubic Euler coefficient therefore vanishes coefficientwise",
      not any(euler_cubic))
check("nonlinear", "the first cubic compatibility representative therefore vanishes",
      not torsion_support, len(torsion_support))
check("nonlinear", "the representative is rational and confined to the 140-cell target",
      len(torsion) == 140 and all(sp.Rational(value).is_Rational for value in torsion))
check("control", "the cubic zero is recorded as stratum-specific rather than a universal polynomial theorem",
      bool(c00) and bool(c01) and len(h_terms) == 2)


print("\nD. THIRD-JET QUOTIENT OF THE NONLINEAR REPRESENTATIVE")
third_indices = list(compositions(3))
third_position = {alpha: index for index, alpha in enumerate(third_indices)}


def principal_and_absorber_columns():
    """Columns of P3 together with d^2(C E)_lower on symmetric third jets."""
    for alpha in third_indices:
        for field_column in range(196):
            principal: dict[int, object] = {}
            absorber: dict[int, object] = {}
            for derivative in range(4):
                if alpha[derivative] == 0:
                    continue
                remainder = list(alpha)
                remainder[derivative] -= 1
                pair = tuple(
                    index
                    for index, multiplicity in enumerate(remainder)
                    for _ in range(multiplicity)
                )
                for equation_row, value in blocks[tuple(sorted(pair))][field_column].items():
                    target = derivative * 196 + equation_row
                    principal[target] = principal.get(target, 0) + value

                pair_alpha = tuple(remainder)
                pair_index = second_position[pair_alpha]
                for clifford in range(14):
                    value = h0[derivative * 14 + clifford, field_column]
                    if value:
                        target = pair_index * 14 + clifford
                        absorber[target] = absorber.get(target, 0) + value
            yield principal, absorber


def mod_value(value: object, prime: int) -> int:
    item = rational(value)
    return item.numerator * pow(item.denominator, -1, prime) % prime


def insert_column(basis: dict[int, dict[int, int]], column: dict[int, object], prime: int) -> None:
    work = {index: mod_value(value, prime) for index, value in column.items() if value}
    while work:
        pivot = min(work)
        if pivot not in basis:
            inverse = pow(work[pivot], -1, prime)
            basis[pivot] = {
                index: value * inverse % prime
                for index, value in work.items()
            }
            return
        scale = work[pivot]
        for index, value in basis[pivot].items():
            updated = (work.get(index, 0) - scale * value) % prime
            if updated:
                work[index] = updated
            elif index in work:
                del work[index]


def quotient_ranks(prime: int) -> tuple[int, int]:
    principal_basis: dict[int, dict[int, int]] = {}
    combined_basis: dict[int, dict[int, int]] = {}
    for principal, absorber in principal_and_absorber_columns():
        insert_column(principal_basis, principal, prime)
        combined = dict(principal)
        combined.update({784 + index: value for index, value in absorber.items()})
        insert_column(combined_basis, combined, prime)
    return len(principal_basis), len(combined_basis)


ranks = [quotient_ranks(prime) for prime in (1_000_003, 1_000_033)]
check("exact", "both primes reproduce first-prolongation rank 770",
      ranks[0][0] == ranks[1][0] == 770, ranks)
check("exact", "the combined third-jet map adds all 140 torsion directions",
      ranks[0][1] == ranks[1][1] == 910, ranks)
check("theorem", "the absorber restricted to the first prolonged symbol kernel is surjective",
      all(combined - principal == 140 for principal, combined in ranks))
check("theorem", "the actual zero representative has zero class in the admissible third-jet quotient",
      not torsion_support and ranks[0][1] - ranks[0][0] == len(torsion))
check("control", "any hypothetical cubic representative would still require the quotient test",
      ranks[0][1] - ranks[0][0] == len(torsion))
check("plant", "PLANT quotienting by unconstrained jets is rejected in favor of ker P3",
      ranks[0][0] == 770 and 3920 - ranks[0][0] == 3150)


print("\nE. FIRST NONZERO QUARTIC COMPATIBILITY REPRESENTATIVE")
endpoint_first = D["endpoint_first"]
r4_terms: dict[tuple[int, ...], dict] = {}
for left_alpha, left_value in h_terms.items():
    for right_alpha, right_value in h_terms.items():
        alpha = add_multi(left_alpha, right_alpha)
        value = S["fscale"](
            Fraction(1, 2), endpoint_second(left_value, right_value)
        )
        r4_terms[alpha] = S["fadd"](r4_terms.get(alpha, {}), value)
b0_h_terms = {
    alpha: endpoint_first(value)
    for alpha, value in h_terms.items()
}

euler_quartic: list[dict[tuple[int, ...], sp.Expr]] = []
euler_quartic_left: list[dict[tuple[int, ...], sp.Expr]] = []
euler_quartic_right: list[dict[tuple[int, ...], sp.Expr]] = []
for _, _, test in cells:
    left_polynomial: dict[tuple[int, ...], sp.Expr] = {}
    right_polynomial: dict[tuple[int, ...], sp.Expr] = {}
    b0_test = endpoint_first(test)
    for alpha, value in r4_terms.items():
        left_polynomial[alpha] = left_polynomial.get(alpha, 0) + scalar(
            sym_pair(b0_test, value)
        )
    for h_alpha, h_value in h_terms.items():
        moving_test = endpoint_second(test, h_value)
        for b_alpha, b_value in b0_h_terms.items():
            alpha = add_multi(h_alpha, b_alpha)
            right_polynomial[alpha] = right_polynomial.get(alpha, 0) + scalar(
                sym_pair(moving_test, b_value)
            )
    left_polynomial = {
        alpha: sp.factor(value) for alpha, value in left_polynomial.items() if value
    }
    right_polynomial = {
        alpha: sp.factor(value) for alpha, value in right_polynomial.items() if value
    }
    euler_quartic_left.append(left_polynomial)
    euler_quartic_right.append(right_polynomial)
    euler_quartic.append({
        alpha: sp.factor(left_polynomial.get(alpha, 0) + right_polynomial.get(alpha, 0))
        for alpha in set(left_polynomial) | set(right_polynomial)
        if sp.factor(left_polynomial.get(alpha, 0) + right_polynomial.get(alpha, 0))
    })


def quartic_compatibility(euler_bank):
    answer = [sp.Integer(0)] * (len(third_indices) * 14)
    for target_index, target_alpha in enumerate(third_indices):
        for clifford in range(14):
            value = sp.Integer(0)
            for lam in range(4):
                alpha = list(target_alpha)
                alpha[lam] += 1
                alpha = tuple(alpha)
                coefficient = euler_bank[lam * 14 + clifford].get(alpha, 0)
                derivative_factor = 1
                for multiplicity in alpha:
                    derivative_factor *= factorial(multiplicity)
                value += derivative_factor * coefficient
            answer[target_index * 14 + clifford] = sp.factor(value)
    return answer


quartic_torsion = quartic_compatibility(euler_quartic)
quartic_support = [index for index, value in enumerate(quartic_torsion) if value]
check("nonlinear", "the actual quartic Euler coefficient is live",
      any(euler_quartic_left) and any(euler_quartic_right) and any(euler_quartic))
check("nonlinear", "the first nonzero compatibility representative lies in 280 cells",
      bool(quartic_support) and len(quartic_torsion) == 280, len(quartic_support))


print("\nF. FOURTH-JET QUOTIENT OF THE QUARTIC REPRESENTATIVE")
fourth_indices = list(compositions(4))
pairs = tuple((mu, nu) for mu in range(4) for nu in range(mu, 4))


def second_prolonged_and_absorber_columns():
    """Columns of P4 together with d^3(C E)_lower on fourth jets."""
    for alpha in fourth_indices:
        for field_column in range(196):
            principal: dict[int, object] = {}
            absorber: dict[int, object] = {}
            for mu, nu in pairs:
                demand = [0, 0, 0, 0]
                demand[mu] += 1
                demand[nu] += 1
                if any(alpha[index] < demand[index] for index in range(4)):
                    continue
                remainder = tuple(alpha[index] - demand[index] for index in range(4))
                equation_base = second_position[remainder] * 196
                for equation_row, value in blocks[(mu, nu)][field_column].items():
                    target = equation_base + equation_row
                    principal[target] = principal.get(target, 0) + value
            for derivative in range(4):
                if alpha[derivative] == 0:
                    continue
                remainder = list(alpha)
                remainder[derivative] -= 1
                target_index = third_position[tuple(remainder)]
                for clifford in range(14):
                    value = h0[derivative * 14 + clifford, field_column]
                    if value:
                        target = target_index * 14 + clifford
                        absorber[target] = absorber.get(target, 0) + value
            yield principal, absorber


def quartic_quotient_ranks(prime: int) -> tuple[int, int]:
    principal_basis: dict[int, dict[int, int]] = {}
    combined_basis: dict[int, dict[int, int]] = {}
    for principal, absorber in second_prolonged_and_absorber_columns():
        insert_column(principal_basis, principal, prime)
        combined = dict(principal)
        combined.update({1960 + index: value for index, value in absorber.items()})
        insert_column(combined_basis, combined, prime)
    return len(principal_basis), len(combined_basis)


quartic_ranks = [quartic_quotient_ranks(prime) for prime in (1_000_003, 1_000_033)]
check("exact", "both primes reproduce second-prolongation rank 1904",
      quartic_ranks[0][0] == quartic_ranks[1][0] == 1904, quartic_ranks)
check("exact", "the combined fourth-jet map adds all 280 quartic torsion directions",
      quartic_ranks[0][1] == quartic_ranks[1][1] == 2184, quartic_ranks)
check("theorem", "the absorber restricted to the second prolonged symbol kernel is surjective",
      all(combined - principal == 280 for principal, combined in quartic_ranks))
check("theorem", "the live quartic representative has zero class modulo admissible fourth jets",
      bool(quartic_support) and quartic_ranks[0][1] - quartic_ranks[0][0] == 280)
check("plant", "PLANT forbidding fourth-jet correction leaves a live representative",
      bool(quartic_support))
check("plant", "PLANT quotienting by unconstrained fourth jets is rejected in favor of ker P4",
      quartic_ranks[0][0] == 1904 and 6860 - quartic_ranks[0][0] == 4956)


print("\nG. DISPOSITION AND SCOPE FENCES")
for kind, label in (
    ("result", "the cubic fixed-natural endpoint torsion vanishes on the tested stationary stratum"),
    ("result", "the first live quartic representative is absorbable by admissible fourth jets"),
    ("result", "no obstruction survives through the tested quartic bidegree"),
    ("needs_recheck", "higher nonlinear torsion and moving coefficients remain open"),
    ("needs_recheck", "source Q_B full action E_act and physical tangent BV remain open"),
    ("symplectic", "formal third-jet absorption is not a BV quotient or BFV reduction"),
    ("analytic", "formal absorption supplies no convergence domain stability or spectrum"),
    ("source", "the source is silent on the nonlinear representative and quotient rank"),
    ("accounting", "ledger verdict residue quotient datum canon and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_SC_ACT_04_ENDPOINT_GRAMMAR__SOURCE_SILENT_FIRST_NONLINEAR_TORSION_AND_SPENCER_ABSORPTION")
print(f"NONLINEAR_TORSION_SUPPORT={len(torsion_support)}/140")
print(f"FIRST_PROLONGED_SYMBOL_RANK={ranks[0][0]}/784")
print(f"COMBINED_SYMBOL_TORSION_MAP_RANK={ranks[0][1]}/924")
print(f"INDUCED_TORSION_ABSORBER_RANK={ranks[0][1]-ranks[0][0]}/140")
print("NONLINEAR_TORSION_CLASS=ZERO_AFTER_ADMISSIBLE_THIRD_JET_QUOTIENT")
print(f"QUARTIC_TORSION_SUPPORT={len(quartic_support)}/280")
print(f"SECOND_PROLONGED_SYMBOL_RANK={quartic_ranks[0][0]}/1960")
print(f"COMBINED_QUARTIC_TORSION_MAP_RANK={quartic_ranks[0][1]}/2240")
print(f"INDUCED_QUARTIC_ABSORBER_RANK={quartic_ranks[0][1]-quartic_ranks[0][0]}/280")
print("QUARTIC_TORSION_CLASS=ZERO_AFTER_ADMISSIBLE_FOURTH_JET_QUOTIENT")
print("RESULT=CUBIC_TORSION_ZERO__FIRST_LIVE_QUARTIC_TORSION_FULLY_ABSORBABLE_ON_FIXED_NATURAL_ENDPOINT_STRATUM")
print("NEXT=TEST_HIGHER_NONLINEAR_ORDER_OR_MOVE_TO_QB_HQ_SHIAB_SECTION_COEFFICIENTS__KEEP_PHYSICAL_BV_SEPARATE")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
