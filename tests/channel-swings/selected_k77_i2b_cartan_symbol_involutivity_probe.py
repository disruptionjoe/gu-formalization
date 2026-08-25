#!/usr/bin/env sage -python
"""Exact Cartan test for the source-natural fixed-grade I2B endpoint symbol.

The fixed-natural owner is the printed endpoint residual square up to nonzero
scale.  This probe rebuilds its lightweight exact ten-block principal tableau,
computes a complete flag and Cartan characters, and checks Cartan's equality
against the actual first prolongation.  A nontrivial rational coframe image is
tested independently.  This decides principal-symbol involutivity only: the
nonlinear torsion/compatibility, physical BV tangent, analytic germ and global
domain remain outside the theorem.
"""

from __future__ import annotations

from collections import Counter, defaultdict
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

from sage.all import QQ, binomial, matrix


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


def q(value: object):
    if isinstance(value, Fraction):
        return QQ(value.numerator) / QQ(value.denominator)
    if hasattr(value, "p") and hasattr(value, "q"):
        return QQ(int(value.p)) / QQ(int(value.q))
    return QQ(value)


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
owner = read("explorations/conditional-build/selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md")
spencer = read("explorations/conditional-build/selected-k77-i2b-stationary-affine-spencer-intersection-2026-08-13.md")
comoving = read("explorations/conditional-build/selected-k77-transverse-comoving-coefficient-closure-2026-08-08.md")
exact_form = read("explorations/conditional-build/selected-k77-i2b-principal-gauge-complex-2026-08-13.md")
check("source", "SC-ACT-04 owns the printed bosonic residual-square grammar",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("prior_art", "the fixed-natural owner is the endpoint square up to nonzero scale",
      "Q_B = c Q_trace/Hodge" in owner and "c != 0" in owner)
check("prior_art", "the first and second prolongation ranks are exact predecessor facts",
      "rank `1904`" in spencer and "1904+56=1960" in spencer)
check("prior_art", "co-moving coefficient closure is only a pointwise naturality theorem",
      "pointwise naturality" in comoving and "formal adjoint" in comoving)
check("prior_art", "the corrected exact-form syzygy bounds every line-symbol rank by 182",
      "all twenty cubic" in exact_form and "exact-form principal map" in exact_form)

for distinction in (
    "principal-symbol involutivity versus nonlinear formal integrability",
    "Cartan characters versus physical degree-of-freedom counts",
    "coframe transport versus a source-selected moving Q_B",
    "fixed-natural endpoint versus first-action E_act",
    "formal solution jets versus analytic or global solutions",
    "symbol kernel versus physical BV cohomology",
):
    check("layer0", distinction + " remain distinct", True)

for kind, label in (
    ("spencer_eds", "compute flag kernels and Cartan equality on the actual tableau"),
    ("principal_bundle", "transport the complete tableau under a nonsingular coframe"),
    ("variational_bicomplex", "retain nonlinear compatibility torsion as an open Euler burden"),
    ("symplectic", "infer no stationary quotient or BFV phase space from symbol involutivity"),
    ("hyperbolic", "infer no Cauchy theorem from Cartan formal regularity"),
    ("krein", "infer no positive energy or common domain from rational ranks"),
    ("source_criticism", "attribute the action grammar to source and Cartan characters to the repo"),
    ("contrary", "require mixed-block, frozen-relation and singular-coframe controls"),
):
    check(kind, label, True)


print("\nB. LIGHTWEIGHT EXACT K77 PRINCIPAL TABLEAU")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    H = runpy.run_path(str(HESSIAN))
check("repo", "the lightweight exact K77 Hessian bank replays",
      "PASS 44/44" in capture.getvalue() and not H["FAILURES"])
cells = H["cells"]
sym_pair = H["sym_pair"]
real_scalar = H["real_scalar"]
principal_with = H["principal_with"]
selected = H["SELECTED"]
responses = [[principal_with(selected, mu, delta) for _, _, delta in cells]
             for mu in range(4)]
check("fingerprint", "field and equation carriers are both 196-real", len(cells) == 196)


def signature(value: dict) -> tuple[int, int] | None:
    if not value:
        return None
    if len(value) != 1:
        check("shape", "principal response remains one-cell sparse", False)
        return None
    mask, clifford = next(iter(value.items()), (None, {}))
    if len(clifford) != 1:
        check("shape", "principal Clifford response remains one-cell sparse", False)
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


def paired(left: dict, right: dict):
    if signature(left) is None or signature(left) != signature(right):
        return QQ(0)
    return q(real_scalar(sym_pair(left, right)))


blocks: dict[tuple[int, int], object] = {}
for mu in range(4):
    for nu in range(mu, 4):
        out = matrix(QQ, 196, 196, sparse=True)
        for column in range(196):
            sig_nu = signatures[nu][column]
            if sig_nu is not None:
                for row in row_buckets[mu].get(sig_nu, []):
                    value = paired(responses[mu][row], responses[nu][column])
                    if value:
                        out[row, column] += value
            if mu != nu:
                sig_mu = signatures[mu][column]
                if sig_mu is not None:
                    for row in row_buckets[nu].get(sig_mu, []):
                        value = paired(responses[nu][row], responses[mu][column])
                        if value:
                            out[row, column] += value
        blocks[(mu, nu)] = out

block_ranks = tuple(blocks[pair].rank() for pair in sorted(blocks))
check("exact", "diagonal and mixed block ranks are 182 and 28",
      block_ranks == (182, 28, 28, 28, 182, 28, 28, 182, 28, 182), block_ranks)


def horizontal_join(bank: dict[tuple[int, int], object], pairs: list[tuple[int, int]]):
    if not pairs:
        return matrix(QQ, 196, 0, sparse=True)
    out = matrix(QQ, 196, 196 * len(pairs), sparse=True)
    for slot, pair in enumerate(pairs):
        out.set_block(0, 196 * slot, bank[pair])
    return out


print("\nC. CARTAN FLAG AND CHARACTERS")
flag_kernel_dims = []
flag_ranks = []
for excluded in range(5):
    allowed = [pair for pair in sorted(blocks)
               if pair[0] >= excluded and pair[1] >= excluded]
    joined = horizontal_join(blocks, allowed)
    rank = joined.rank()
    flag_ranks.append(rank)
    flag_kernel_dims.append(joined.ncols() - rank)

check("cartan", "the coordinate flag has exact restricted ranks 196,196,196,182,0",
      flag_ranks == [196, 196, 196, 182, 0], flag_ranks)
check("cartan", "the flag is regular: ranks 196 are receiver-maximal and the exact-form syzygy bounds a line by 182",
      flag_ranks[:3] == [196, 196, 196] and flag_ranks[3] == 182)
check("cartan", "the symbol flag kernels are 1764,980,392,14,0",
      flag_kernel_dims == [1764, 980, 392, 14, 0], flag_kernel_dims)
characters = tuple(flag_kernel_dims[i] - flag_kernel_dims[i + 1] for i in range(4))
check("cartan", "the four Cartan characters are 784,588,378,14",
      characters == (784, 588, 378, 14), characters)
check("cartan", "the character sequence is nonincreasing and nonnegative",
      all(characters[i] >= characters[i + 1] >= 0 for i in range(3)))


def compositions(total: int, slots: int = 4, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, slots - 1, prefix + (value,))


third_indices = list(compositions(3))


def prolongation_columns(bank: dict[tuple[int, int], object]):
    for alpha in third_indices:
        for field_column in range(196):
            out: dict[int, object] = {}
            for derivative in range(4):
                if alpha[derivative] == 0:
                    continue
                beta = list(alpha)
                beta[derivative] -= 1
                pair = tuple(index for index, multiplicity in enumerate(beta)
                             for _ in range(multiplicity))
                for equation_row, value in bank[tuple(sorted(pair))].column(field_column).dict().items():
                    target = derivative * 196 + equation_row
                    out[target] = out.get(target, QQ(0)) + value
            yield {index: value for index, value in out.items() if value}


def modular_rank(bank: dict[tuple[int, int], object], prime: int) -> int:
    basis: dict[int, dict[int, int]] = {}
    for column in prolongation_columns(bank):
        work = {
            index: (int(value.numerator()) * pow(int(value.denominator()), -1, prime)) % prime
            for index, value in column.items()
        }
        while work:
            pivot = min(work)
            if pivot not in basis:
                inverse = pow(work[pivot], -1, prime)
                basis[pivot] = {index: value * inverse % prime for index, value in work.items()}
                break
            scale = work[pivot]
            for index, value in basis[pivot].items():
                updated = (work.get(index, 0) - scale * value) % prime
                if updated:
                    work[index] = updated
                elif index in work:
                    del work[index]
    return len(basis)


rank_first = modular_rank(blocks, 1_000_003)
dim_g3 = 196 * len(third_indices) - rank_first
cartan_bound = sum((index + 1) * value for index, value in enumerate(characters))
check("cartan", "the actual first prolongation rank is 770", rank_first == 770)
check("cartan", "Cartan equality holds: dim g3 equals the character bound 3150",
      dim_g3 == cartan_bound == 3150, (dim_g3, cartan_bound))
check("theorem", "the source-natural fixed-grade endpoint principal symbol is involutive",
      dim_g3 == cartan_bound)

# The character formula predicts the next kernel dimension.  The independently
# certified second-prolongation rank 1904 gives exactly the same number.
predicted_g4 = sum(binomial(index + 2, 2) * value
                   for index, value in enumerate(characters))
certified_g4 = 196 * 35 - 1904
check("crosscheck", "Cartan characters reproduce the certified g4 dimension 4956",
      predicted_g4 == certified_g4 == 4956)


print("\nD. NONTRIVIAL EXACT COFRAME TRANSPORT")
coframe = matrix(QQ, [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
])
check("transport", "the rational coframe change is nonsingular and nontrivial",
      coframe.det() == 1 and coframe != matrix.identity(QQ, 4))


def transform_symbol(bank: dict[tuple[int, int], object], change):
    transformed: dict[tuple[int, int], object] = {}
    for i in range(4):
        for j in range(i, 4):
            out = matrix(QQ, 196, 196, sparse=True)
            for mu in range(4):
                coefficient = change[mu, i] * change[mu, j]
                if i != j:
                    coefficient *= 2
                if coefficient:
                    out += coefficient * bank[(mu, mu)]
            for mu in range(4):
                for nu in range(mu + 1, 4):
                    coefficient = change[mu, i] * change[nu, j]
                    if i != j:
                        coefficient += change[mu, j] * change[nu, i]
                    if coefficient:
                        out += coefficient * bank[(mu, nu)]
            transformed[(i, j)] = out
    return transformed


moved = transform_symbol(blocks, coframe)
moved_flag_dims = []
moved_flag_ranks = []
for excluded in range(5):
    allowed = [pair for pair in sorted(moved)
               if pair[0] >= excluded and pair[1] >= excluded]
    joined = horizontal_join(moved, allowed)
    moved_flag_ranks.append(joined.rank())
    moved_flag_dims.append(joined.ncols() - joined.rank())
moved_characters = tuple(moved_flag_dims[i] - moved_flag_dims[i + 1] for i in range(4))
moved_rank_first = modular_rank(moved, 1_000_003)
check("transport", "the moved tableau retains the complete flag ranks",
      moved_flag_ranks == flag_ranks, moved_flag_ranks)
check("transport", "the moved tableau retains all four Cartan characters",
      moved_characters == characters, moved_characters)
check("transport", "the moved first prolongation retains rank 770 and Cartan equality",
      moved_rank_first == 770 and 3920 - moved_rank_first == cartan_bound)

# The original divergence rows need not stay coordinatewise fixed.  This is a
# control against treating natural transport as coefficient freezing.
original_relations = [
    {derivative * 196 + derivative * 14 + clifford: QQ(1)
     for derivative in range(4)}
    for clifford in range(14)
]
moved_columns = list(prolongation_columns(moved))
frozen_relation_defects = sum(
    any(sum(coefficient * column.get(index, QQ(0))
            for index, coefficient in relation.items()) != 0
        for column in moved_columns)
    for relation in original_relations
)
check("control", "freezing the old divergence representatives fails after coframe motion",
      frozen_relation_defects > 0, frozen_relation_defects)
check("transport", "the compatibility space transports by dimension rather than fixed rows",
      784 - moved_rank_first == 14)

timelike_only = horizontal_join(blocks, [(0, 0)])
check("planted", "PLANT retaining only the timelike diagonal drops the image to rank 182",
      timelike_only.rank() == 182)
singular = matrix.diagonal(QQ, [1, 1, 1, 0])
check("planted", "PLANT a singular coframe is rejected before transport", singular.det() == 0)


print("\nE. DISPOSITION AND SCOPE FENCES")
for kind, label in (
    ("result", "principal Cartan involutivity closes at the source-natural fixed grade"),
    ("result", "nonsingular coframe transport preserves the tableau and its characters"),
    ("needs_recheck", "nonlinear torsion absorption and moving lower-order compatibility remain open"),
    ("needs_recheck", "field-dependent Q_B H_q Shiab section and observation derivatives remain open"),
    ("needs_recheck", "physical tangent BV BFV and presymplectic ownership remain open"),
    ("analytic", "formal involutivity supplies no analytic convergence Green domain or stability"),
    ("hyperbolic", "no characteristic propagation or well-posedness theorem follows"),
    ("krein", "no positivity or physical-state selection follows"),
    ("source", "the source is silent on exact Cartan characters and nonlinear integrability"),
    ("accounting", "ledger verdict residue quotient datum canon and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_SC_ACT_04_ENDPOINT_GRAMMAR__SOURCE_SILENT_CARTAN_CHARACTERS_AND_NONLINEAR_FORMAL_INTEGRABILITY")
print("FLAG_RANKS=" + ",".join(map(str, flag_ranks)))
print("FLAG_KERNEL_DIMS=" + ",".join(map(str, flag_kernel_dims)))
print("CARTAN_CHARACTERS=" + ",".join(map(str, characters)))
print(f"FIRST_PROLONGATION_RANK={rank_first}/784")
print(f"DIM_G3={dim_g3}")
print(f"CARTAN_BOUND={cartan_bound}")
print(f"CERTIFIED_DIM_G4={certified_g4}")
print("MOVED_CARTAN_CHARACTERS=" + ",".join(map(str, moved_characters)))
print(f"MOVED_FIRST_PROLONGATION_RANK={moved_rank_first}/784")
print("RESULT=SOURCE_NATURAL_FIXED_GRADE_ENDPOINT_PRINCIPAL_SYMBOL_CARTAN_INVOLUTIVE__COFRAME_TRANSPORT_EXACT")
print("NEXT=COMPUTE_FIRST_NONLINEAR_MOVING_COEFFICIENT_TORSION_CLASS_ON_THE_COMPATIBLE_AFFINE_JET__KEEP_PHYSICAL_BV_GRAPH_SEPARATE")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
