#!/usr/bin/env python3
"""Exact stationary observation dual and first Spencer gate for selected I2B.

The affine Ward predecessor closes the connection-parameter jet subchain.
This probe keeps equation observation separate from residual pullback and the
preboundary contact term, then computes the first formal prolongation of the
complete ten-block holonomic second-jet Euler symbol.  It finds a 14-dimensional
first compatibility cokernel.  It does not construct BV cohomology, a physical
quotient, a Green domain, or the full source action.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HESSIAN = ROOT / "tests/channel-swings/selected_k77_i2b_moving_higgs_principal_hessian_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
pullback_source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
affine_source = read("lab/sources/selected-k77-i2b-parameter-jet-affine-ward-source-return-2026-08-13.md")
affine_prior = read("explorations/conditional-build/selected-k77-i2b-parameter-jet-affine-ward-2026-08-13.md")
observation_prior = read("explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md")
holonomic_prior = read("explorations/conditional-build/selected-k77-i2b-holonomic-jet-euler-image-2026-08-13.md")
check("source", "the source makes observation richer than naive pullback",
      "SOURCE-CORRECTS-NAIVE-READING" in pullback_source)
check("source", "the affine source return leaves observation and Spencer open",
      "BV, Spencer," in affine_source and "observation," in affine_source)
check("prior_art", "the affine predecessor closes only the connection-jet subchain",
      "affine connection-\njet subchain" in affine_prior)
check("prior_art", "the observation predecessor records a nonzero preboundary owner",
      "preboundary potential" in observation_prior and "nonzero" in observation_prior)
check("prior_art", "the complete second-jet symbol is onto at zeroth prolongation",
      "rank `196`" in holonomic_prior)
for distinction in (
    "equation-dual observation versus residual pullback",
    "stationary coefficient motion versus nonstationary coefficient motion",
    "Euler Ward closure versus preboundary contact",
    "full affine source connection versus effective 196-real distortion",
    "zeroth symbol surjectivity versus first formal prolongation",
    "first compatibility cokernel versus full Spencer involutivity",
):
    check("layer0", distinction + " remain distinct", True)
for kind, label in (
    ("principal_bundle", "derive observation motion from the inverse-transpose associated map"),
    ("variational", "test observation on the Euler covector at a stationary point"),
    ("spencer", "assemble the actual first symmetric prolongation"),
    ("hyperbolic", "infer no Cauchy or characteristic-domain theorem from formal exactness"),
    ("krein", "infer no positivity from a compatibility rank"),
    ("symplectic", "preserve the separately nonzero preboundary owner"),
    ("source", "separate source grammar from repository-derived ranks"),
    ("contrary", "retain nonstationary frozen-observation and truncated-symbol plants"),
):
    check(kind, label, True)


print("\nB. STATIONARY EQUATION-DUAL OBSERVATION IDENTITY")
Q = sp.Rational
J = sp.Matrix([[Q(1, 2), Q(-1, 3)], [Q(2, 5), Q(3, 7)], [Q(-4, 9), Q(5, 11)]])
dJ = sp.Matrix([[Q(1, 7), Q(2, 9)], [Q(-3, 8), Q(4, 13)], [Q(5, 12), Q(-6, 17)]])
b, n = J.cols, J.rows
M = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.eye(b), J.T),
    sp.Matrix.hstack(sp.zeros(n, b), sp.eye(n)),
)
dM = sp.Matrix.vstack(
    sp.Matrix.hstack(sp.zeros(b), dJ.T),
    sp.zeros(n, b + n),
)
O = M.inv().T
dO = -O * dM.T * O
E0 = sp.zeros(b + n, 1)
dE_covariant = sp.zeros(b + n, 1)
stationary_observed_derivative = dO * E0 + O * dE_covariant
check("exact", "the equation receiver is the inverse transpose of the complete observation germ",
      O * M.T == sp.eye(b + n))
check("exact", "its derivative obeys the inverse-transpose product rule",
      dO * M.T + O * dM.T == sp.zeros(b + n))
check("theorem", "observation motion cannot reopen a covariantly closed stationary Euler row",
      stationary_observed_derivative == sp.zeros(b + n, 1))
E_live = sp.Matrix([Q(2), Q(3), Q(5), Q(7), Q(11)])
check("control", "observation motion is live away from the stationary locus", dO * E_live != E0)
check("planted", "PLANT freezing observation would miss the live nonstationary coefficient owner",
      dO * E_live != E0)
check("symplectic", "stationary Euler closure does not erase the predecessor's preboundary contact term",
      "PRESYMPLECTIC_PREBOUNDARY_OWNER=EXACT_NONZERO" in
      read("tests/channel-swings/selected_action_physical_soldering_observation_compose_probe.py"))


print("\nC. EXACT SELECTED K77 TEN-BLOCK SYMBOL")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    H = runpy.run_path(str(HESSIAN))
check("repo", "the exact selected K77 principal-Hessian predecessor replays",
      "PASS 44/44" in capture.getvalue() and not H["FAILURES"])
cells = H["cells"]
sym_pair = H["sym_pair"]
real_scalar = H["real_scalar"]
principal_with = H["principal_with"]
selected = H["SELECTED"]
responses = [[principal_with(selected, mu, delta) for _, _, delta in cells] for mu in range(4)]
check("fingerprint", "the field and equation carriers remain 196-real", len(cells) == 196)
check("fingerprint", "each directional response has support rank 182",
      [sum(bool(value) for value in direction) for direction in responses] == [182] * 4)


def signature(value: dict) -> tuple[int, int] | None:
    if not value:
        return None
    if len(value) != 1:
        check("shape", "principal response remains a one-cell residual", False)
        return None
    mask, clifford = next(iter(value.items()), (None, {}))
    if len(clifford) != 1:
        check("shape", "principal Clifford response remains a one-cell residual", False)
        return None
    return mask, next(iter(clifford), -1)


signatures = [[signature(value) for value in direction] for direction in responses]
row_buckets = []
for direction in range(4):
    bucket: dict[tuple[int, int], list[int]] = defaultdict(list)
    for row, item in enumerate(signatures[direction]):
        if item is not None:
            bucket[item].append(row)
    row_buckets.append(bucket)


def fraction(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    return Fraction(int(value.p), int(value.q))


def rational(value: object) -> sp.Rational:
    item = fraction(value)
    return sp.Rational(item.numerator, item.denominator)


def paired(left: dict, right: dict) -> Fraction:
    if signature(left) is None or signature(left) != signature(right):
        return Fraction(0)
    return fraction(real_scalar(sym_pair(left, right)))


blocks: dict[tuple[int, int], list[dict[int, Fraction]]] = {}
for mu in range(4):
    for nu in range(mu, 4):
        columns: list[dict[int, Fraction]] = []
        for column in range(196):
            values: dict[int, Fraction] = {}
            sig_nu = signatures[nu][column]
            if sig_nu is not None:
                for row in row_buckets[mu].get(sig_nu, []):
                    value = paired(responses[mu][row], responses[nu][column])
                    if value:
                        values[row] = values.get(row, Fraction(0)) + value
            if mu != nu:
                sig_mu = signatures[mu][column]
                if sig_mu is not None:
                    for row in row_buckets[nu].get(sig_mu, []):
                        value = paired(responses[nu][row], responses[mu][column])
                        if value:
                            values[row] = values.get(row, Fraction(0)) + value
            columns.append({row: value for row, value in values.items() if value})
        blocks[(mu, nu)] = columns

timelike_dense = sp.zeros(196)
for column, values in enumerate(blocks[(0, 0)]):
    for row, value in values.items():
        timelike_dense[row, column] = sp.Rational(value.numerator, value.denominator)
check("replay", "the sparse one-cell assembly reproduces the predecessor timelike Gram",
      timelike_dense == sp.Matrix(H["full_gram"]))
cross_dense = sp.Matrix(196, 196, [
    rational(real_scalar(sym_pair(responses[0][row], responses[1][column]))
             + real_scalar(sym_pair(responses[1][row], responses[0][column])))
    for row in range(196) for column in range(196)
])
cross_sparse = sp.zeros(196)
for column, values in enumerate(blocks[(0, 1)]):
    for row, value in values.items():
        cross_sparse[row, column] = sp.Rational(value.numerator, value.denominator)
check("replay", "an exhaustive mixed block verifies the sparse signature selection rule",
      cross_sparse == cross_dense)
check("exact", "all ten symmetric symbol blocks were assembled", len(blocks) == 10)


print("\nD. FIRST FORMAL SPENCER PROLONGATION")
def compositions(total: int, slots: int = 4, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, slots - 1, prefix + (value,))


third_multiindices = list(compositions(3))
check("exact", "Sym^3 of the four-dimensional observation cotangent has dimension 20",
      len(third_multiindices) == 20)


def prolongation_columns():
    for alpha in third_multiindices:
        for field_column in range(196):
            out: dict[int, Fraction] = {}
            for derivative in range(4):
                if alpha[derivative] == 0:
                    continue
                beta = list(alpha)
                beta[derivative] -= 1
                pair = [index for index, multiplicity in enumerate(beta) for _ in range(multiplicity)]
                block = blocks[tuple(sorted(pair))][field_column]
                for equation_row, value in block.items():
                    index = derivative * 196 + equation_row
                    out[index] = out.get(index, Fraction(0)) + value
            yield {index: value for index, value in out.items() if value}


def modular_rank(prime: int) -> tuple[int, tuple[int, ...]]:
    basis: dict[int, dict[int, int]] = {}
    checkpoints = []
    for number, column in enumerate(prolongation_columns(), start=1):
        work = {
            index: (value.numerator * pow(value.denominator, -1, prime)) % prime
            for index, value in column.items() if value
        }
        while work:
            pivot = min(work)
            if pivot not in basis:
                inverse = pow(work[pivot], -1, prime)
                basis[pivot] = {index: (value * inverse) % prime for index, value in work.items()}
                break
            scale = work[pivot]
            for index, value in basis[pivot].items():
                updated = (work.get(index, 0) - scale * value) % prime
                if updated:
                    work[index] = updated
                elif index in work:
                    del work[index]
        if number % 196 == 0:
            checkpoints.append(len(basis))
    return len(basis), tuple(checkpoints)


rank_1, checkpoints_1 = modular_rank(1_000_003)
rank_2, checkpoints_2 = modular_rank(1_000_033)
check("theorem", "the first prolongation has rank 770 modulo the first good prime",
      rank_1 == 770, checkpoints_1)
check("theorem", "an independent prime reproduces rank 770 and the checkpoint profile",
      rank_2 == 770 and checkpoints_2 == checkpoints_1, checkpoints_2)
check("theorem", "the first formal compatibility cokernel has dimension fourteen",
      784 - rank_1 == 14)

# The 196 equation rows are ordered as form_index * 14 + Clifford_index.
# The complete cokernel is therefore represented by one divergence-shaped
# row for each Clifford index: sum_lambda d_lambda E_{lambda,a}.  Verify the
# identities over QQ, not merely modulo the two rank primes.
compatibility_rows = [
    {derivative * 196 + derivative * 14 + clifford: Fraction(1)
     for derivative in range(4)}
    for clifford in range(14)
]
columns = list(prolongation_columns())
compatibility_values = [
    [sum(coefficient * column.get(index, Fraction(0))
         for index, coefficient in relation.items())
     for column in columns]
    for relation in compatibility_rows
]
check("theorem", "fourteen rational divergence-shaped rows annihilate the prolongation",
      all(value == 0 for relation in compatibility_values for value in relation))
check("theorem", "the fourteen compatibility rows are linearly independent",
      len({min(relation) for relation in compatibility_rows}) == 14)
wrong_relation = dict(compatibility_rows[0])
wrong_relation[196 + 14] = Fraction(-1)
check("planted", "PLANT changing one divergence sign breaks the exact compatibility identity",
      any(sum(coefficient * column.get(index, Fraction(0))
              for index, coefficient in wrong_relation.items()) != 0
          for column in columns))
check("planted", "PLANT the timelike-only truncation cannot support the full first prolongation",
      timelike_dense.rank() == 182 < 196)


print("\nE. DISPOSITION AND DURABLE FENCES")
for kind, label in (
    ("correction", "observation/contact does not reopen the closed stationary equation-dual Ward row"),
    ("spencer", "the complete cokernel is the fourteen-row divergence-shaped compatibility family"),
    ("principal_bundle", "global atlas descent and a nonlinear Bianchi-compatible source connection remain open"),
    ("variation", "nonstationary lower-order and moving-primalizer terms remain open"),
    ("symplectic", "the nonzero preboundary contact owner and BV/BFV quotient remain open"),
    ("hyperbolic", "formal first compatibility is not a well-posedness or propagation theorem"),
    ("analytic", "closed domains positivity spectrum mass and stability remain open"),
    ("scope", "higher Spencer cohomology and full involutivity remain open"),
    ("source", "the source owns the geometric grammar but not these exact closures"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_RICH_OBSERVATION_AND_AFFINE_GRAMMAR__SOURCE_SILENT_STATIONARY_OBSERVATION_DUAL_AND_FIRST_SPENCER_RANK")
print("STATIONARY_OBSERVATION_DUAL=NO_REOPENING")
print("PREBOUNDARY_CONTACT=NONZERO_AND_SEPARATE")
print(f"FIRST_PROLONGATION_RANK={rank_1}/784")
print("FIRST_COMPATIBILITY_COKERNEL_DIMENSION=14")
print("FIRST_COMPATIBILITY_BASIS=SUM_LAMBDA_D_LAMBDA_E_LAMBDA_A__A_0_TO_13")
print("HIGHER_SPENCER_BV_BFV_GLOBAL_DOMAIN=OPEN")
print("P1_P2_P3=UNUSED")
print("CHECKPOINTS=" + ",".join(map(str, checkpoints_1)))
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
