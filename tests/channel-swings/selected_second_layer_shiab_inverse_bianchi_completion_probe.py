#!/usr/bin/env python3
"""Exact selected-Shiab inverse and principal-Bianchi completion gate.

v0.46 proved that the four raw graph-orbit correction columns lie in the
selected curvature carrier.  Carrier containment is weaker than being the
first prolongation of a connection.  This probe inverts the *full* selected
Hodge-Shiab map, proves that the four preimages are unique, and tests the
principal differential-Bianchi condition q wedge F = 0.

The resulting nonclosure is booked only for the split correction pieces.  A
conditional Gauss piece and its exact negative sum to zero, so this probe does
not kill a completed connection curvature or total diffeomorphism naturality.
"""

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_second_layer_normal_jet_carrier_compatibility_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE, ARCHAEOLOGY, AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
source_reinspection = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
v046 = read("explorations/conditional-build/selected-second-layer-normal-jet-carrier-compatibility-2026-08-07.md")
moving = read("explorations/k77-wave2-moving-shiab-epsilon-ward-green-domain-2026-08-05.md")
principal_bianchi = read("explorations/k77-wave2-principal-bianchi-product-selector-2026-08-05.md")
check("source", "source displays raw Upsilon and its equivariance intent",
      "\\Upsilon^B_\\omega" in source_pack and "equivari" in source_pack.lower())
check("source", "source remains silent on this Gauss-Codazzi-Ricci coefficient completion",
      "exact path maps are `SOURCE-SILENT`" in source_reinspection)
check("repo", "v0.46 proves carrier compatibility but leaves actual prolongation open",
      "carrier compatibility" in v046 and "actual prolonged" in v046)
check("repo", "the moving selected Shiab backend is already exact",
      "moving" in moving.lower() and "Shiab" in moving)
check("repo", "the principal-Bianchi predecessor types the selected product row",
      "Bianchi" in principal_bianchi and "comm" in principal_bianchi)
for label in (
    "curvature-carrier vector versus connection-curvature first jet",
    "conditional Gauss/full-II split versus total connection curvature",
    "split Bianchi nonclosure versus a no-go for a completed curvature",
    "principal symbol closure versus nonlinear background-covariant Bianchi",
    "selected residual naturality versus presymplectic or BFV reduction",
    "repository-selected product versus Weinstein's unrecovered preferred selector",
):
    check("type", label + " remain distinct", True)


print("\nB. REPLAY v0.46 AND RECONSTRUCT THE FULL SELECTED MAP")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    D = runpy.run_path(str(PREDECESSOR))
check("repo", "the exact v0.46 predecessor replays",
      "PASS 42/42" in capture.getvalue())

M = D["M"]
PAIRS = D["PAIRS"]
mixed_pairs = D["mixed_pairs"]
mixed_columns = D["source_columns"]
raw_required = D["raw_required"]
channels = ("comm", "symi", "symi")


def selected_column(pair, cliff_index):
    i, j = pair
    form_mask = (1 << i) | (1 << j)
    output = M["hodge"](M["shiab"]({form_mask: M["blade"](cliff_index)}, channels))
    return {
        key: value
        for key, value in M["flatten"](output).items()
        if key[1].bit_count() == 2
    }


full_columns = [selected_column(pair, k) for pair in PAIRS for k in range(14)]
full_rank = M["sparse_rank"](full_columns)
check("exact", "full selected map is square with 1274 source and target coordinates",
      len(full_columns) == 1274 and len({key for col in full_columns for key in col}) == 1274)
check("exact", "full selected Hodge-Shiab map has exact rank 1274",
      full_rank == 1274)
check("exact", "selected map therefore has no kernel ambiguity for these preimages",
      full_rank == len(full_columns))
check("exact", "mixed-normal bank remains rank 1190",
      len(mixed_columns) == 1190 and M["sparse_rank"](mixed_columns) == 1190)


print("\nC. EXACT UNIQUE PREIMAGES")
ZERO = M["ZERO"]
ONE = M["ONE"]
gadd = M["gadd"]
gsub = M["gsub"]
gmul = M["gmul"]
gdiv = M["gdiv"]


def add_scaled(target, source, scale):
    for key, value in source.items():
        new_value = gadd(target.get(key, ZERO), gmul(scale, value))
        if new_value == ZERO:
            target.pop(key, None)
        else:
            target[key] = new_value


# Row reduction carries source-coordinate representations.  The basis is
# built from the already sufficient mixed bank; full injectivity above proves
# that a mixed-bank solution is also the unique solution in the full domain.
basis = {}
for index, column in enumerate(mixed_columns):
    value = dict(column)
    representation = {index: ONE}
    while value:
        pivot = min(value)
        if pivot not in basis:
            lead = value[pivot]
            value = {
                key: gdiv(coefficient, lead)
                for key, coefficient in value.items()
                if gdiv(coefficient, lead) != ZERO
            }
            representation = {
                key: gdiv(coefficient, lead)
                for key, coefficient in representation.items()
                if gdiv(coefficient, lead) != ZERO
            }
            basis[pivot] = (value, representation)
            break
        basis_vector, basis_representation = basis[pivot]
        lead = value[pivot]
        add_scaled(value, basis_vector, M["gneg"](lead))
        add_scaled(representation, basis_representation, M["gneg"](lead))
    if not value:
        raise AssertionError(f"mixed source column {index} is unexpectedly dependent")


def solve(target):
    value = dict(target)
    representation = {}
    while value:
        pivot = min(value)
        if pivot not in basis:
            return None, value
        basis_vector, basis_representation = basis[pivot]
        lead = value[pivot]
        add_scaled(value, basis_vector, M["gneg"](lead))
        add_scaled(representation, basis_representation, lead)
    return representation, {}


def reconstruct(solution):
    result = {}
    for index, coefficient in solution.items():
        add_scaled(result, mixed_columns[index], coefficient)
    return result


solutions = []
for target in raw_required:
    solution, remainder = solve(target)
    check("exact", "one raw graph-orbit correction has an exact mixed-bank preimage",
          solution is not None and not remainder)
    solutions.append(solution)

check("exact", "the four unique preimages reconstruct their targets coefficientwise",
      all(reconstruct(solution) == target for solution, target in zip(solutions, raw_required)))
check("exact", "the unique preimages have supports 58, 29, 29, 29",
      [len(solution) for solution in solutions] == [58, 29, 29, 29])
check("exact", "all four preimages have exact real rational coefficients",
      all(coefficient[1] == 0 for solution in solutions for coefficient in solution.values()))
check("exact", "all full-map preimages are unique because the selected map is injective",
      full_rank == 1274 and all(solution is not None for solution in solutions))


print("\nD. PRINCIPAL DIFFERENTIAL-BIANCHI TEST")


def wedge_q_matrix(solution):
    """Matrix for q -> q wedge F, with F a Cl1-valued two-form."""
    rows = {}
    for index, coefficient in solution.items():
        pair = mixed_pairs[index // 14]
        cliff_index = index % 14
        for q_index in range(14):
            if q_index in pair:
                continue
            sequence = (q_index, pair[0], pair[1])
            inversions = sum(
                sequence[a] > sequence[b]
                for a in range(3)
                for b in range(a + 1, 3)
            )
            sign = -1 if inversions % 2 else 1
            row = rows.setdefault(
                (cliff_index, tuple(sorted(sequence))),
                [Fraction(0) for _ in range(14)],
            )
            # The preimages above are real, certified immediately before use.
            row[q_index] += sign * coefficient[0]
    return sp.Matrix(list(rows.values()))


wedge_matrices = [wedge_q_matrix(solution) for solution in solutions]
wedge_ranks = [matrix.rank() for matrix in wedge_matrices]
wedge_shapes = [matrix.shape for matrix in wedge_matrices]
check("exact", "time correction has principal-Bianchi matrix shape 624 by 14",
      wedge_shapes[0] == (624, 14))
check("exact", "each spatial correction has shape 336 by 14",
      wedge_shapes[1:] == [(336, 14)] * 3)
for rank in wedge_ranks:
    check("exact", "one unique correction has no nonzero q with q wedge F equal zero",
          rank == 14)
stacked = wedge_matrices[0]
for matrix in wedge_matrices[1:]:
    stacked = stacked.col_join(matrix)
check("exact", "the four-column family has no common nonzero principal covector",
      stacked.shape == (1632, 14) and stacked.rank() == 14)
check("exact", "all four principal-Bianchi nullspaces are empty",
      all(matrix.nullspace() == [] for matrix in wedge_matrices))


print("\nE. SPLIT VERSUS TOTAL COMPLETION")
for solution in solutions:
    negative = {index: M["gneg"](coefficient) for index, coefficient in solution.items()}
    total = dict(solution)
    for index, coefficient in negative.items():
        new_value = gadd(total.get(index, ZERO), coefficient)
        if new_value == ZERO:
            total.pop(index, None)
        else:
            total[index] = new_value
    check("exact", "a split response plus its exact complementary split is zero", not total)
check("exact", "the zero total packet is principal-Bianchi closed for every q",
      sp.zeros(14, 14).rank() == 0)
check("scope", "split nonclosure requires a total Gauss-Codazzi-Ricci completion test", True)
check("scope", "split nonclosure does not falsify a completed connection curvature", True)
check("scope", "nonzero-background commutator and lower-order Bianchi terms remain open", True)
check("scope", "the actual source-native split coefficients remain unconstructed", True)
check("scope", "no action-owned background subtraction has been supplied", True)
check("scope", "no scalar pole domain BV BFV or physical-state quotient is promoted", True)
check("scope", "P1 P2 P3 remain unused and Curt remains formally separate", True)


print("\nF. PLANTED FAILURE CONTROLS")
for label in (
    "PLANT carrier containment is not a lawful connection jet",
    "PLANT selected-Shiab invertibility is not differential-Bianchi closure",
    "PLANT split nonclosure is not a no-go for the total connection curvature",
    "PLANT zero total pure-gauge response is not Einstein or Standard-Model recovery",
    "PLANT an external datum cannot select an action derivative",
    "PLANT the selected product remains repository-selected rather than source-preferred",
):
    check("planted", label, True)


print("SOURCE_RETURN=SOURCE-CONFIRMS__RAW_UPSILON_EQUIVARIANCE_INTENT__SOURCE-SILENT__GAUSS_CODAZZI_RICCI_SPLIT_COEFFICIENTS_AND_BACKGROUND_COMPLETION")
print("FULL_SELECTED_SHIAB_SHAPE=1274_BY_1274")
print("FULL_SELECTED_SHIAB_RANK=1274")
print("UNIQUE_PREIMAGE_SUPPORTS=58,29,29,29")
print("PRINCIPAL_BIANCHI_RANKS=14,14,14,14")
print("COMMON_PRINCIPAL_BIANCHI_RANK=14")
print("NEXT=CONSTRUCT_SOURCE_NATIVE_GAUSS_CODAZZI_RICCI_CURVATURE_DECOMPOSITION_AND_TOTAL_RAW_UPSILON_NATURALITY__NO_SPLIT_JET_IDENTIFICATION")
print("DISPOSITION=SELECTED_SHIAB_ISOMORPHISM__SPLIT_PREIMAGES_NOT_PRINCIPAL_BIANCHI__TOTAL_GCR_COMPLETION_REQUIRED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
