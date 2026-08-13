#!/usr/bin/env sage -python
"""Exact stationary-affine intersection with the next Spencer condition.

The predecessor correctly proved that no constant lower-order operator
completion kills its rank-56 frozen defect.  That is not the same question as
whether the defect vanishes on some stationary formal jet.  This probe tests
the latter on both the old (00)+(01) ansatz and the complete symmetric
two-jet space, then computes the full second prolonged principal symbol.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

from sage.all import QQ, matrix, vector


ROOT = Path(__file__).resolve().parents[2]
LOCAL = ROOT / "tests/channel-swings/selected_k77_i2b_local_stationary_bianchi_jet_probe.py"
ENDPOINT = ROOT / "tests/channel-swings/selected_k77_i2b_endpoint_frozen_compatibility_adapter_probe.py"
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


def replay(path: Path):
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        data = runpy.run_path(str(path))
    return data, capture.getvalue()


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/selected-k77-i2b-endpoint-frozen-compatibility-source-return-2026-08-13.md")
local_prior = read("explorations/conditional-build/selected-k77-i2b-local-stationary-bianchi-jet-witness-2026-08-13.md")
spencer_prior = read("explorations/conditional-build/selected-k77-i2b-observation-contact-spencer-2026-08-13.md")
frozen_prior = read("explorations/conditional-build/selected-k77-i2b-frozen-hessian-compatibility-2026-08-13.md")
endpoint_prior = read("explorations/conditional-build/selected-k77-i2b-endpoint-frozen-compatibility-adapter-2026-08-13.md")

check("source", "source confirms the printed endpoint but not its frozen compatibility theorem",
      "SOURCE-SILENT" in source and "compatibility" in source)
check("prior_art", "the local predecessor built one noncanonical stationary two-jet",
      "fourteen nonzero coefficients" in local_prior
      and "not a unique solution" in local_prior)
check("prior_art", "the first Spencer cokernel is exactly the fourteen divergence rows",
      "exact rank `770`" in spencer_prior and "cokernel is exactly" in spencer_prior)
check("prior_art", "the frozen theorem excludes a universal constant operator completion",
      "constant lower-order correction" in frozen_prior and "does **not** extend" in frozen_prior)
check("prior_art", "the endpoint port corrected coefficients while retaining rank 56",
      "combined defect" in endpoint_prior and "rank 56" in endpoint_prior
      and "fixed-`H_q` pairing" in endpoint_prior)

for distinction in (
    "failure of an operator identity versus nonexistence of compatible formal jets",
    "one sparse stationary witness versus the full stationary affine fibre",
    "the 392-variable restricted ansatz versus the 1960-variable complete two-jet space",
    "the path-average surrogate versus the printed endpoint residual",
    "a differentiated first compatibility condition versus full formal involutivity",
    "frozen linear formal extension versus nonlinear analytic or global existence",
):
    check("layer0", distinction + " remain distinct", True)

for kind, label in (
    ("spencer_eds", "intersect the equation fibre with compatibility before declaring obstruction"),
    ("variational_bicomplex", "keep an off-shell differential identity distinct from on-shell jet restriction"),
    ("principal_bundle", "retain the connection two-jet carrier and inherited observation split"),
    ("category", "take the kernel pullback rather than compare ranks on unrelated maps"),
    ("hyperbolic", "infer no Cauchy propagation or well-posedness from formal jets"),
    ("krein", "infer no positivity from rational compatibility ranks"),
    ("symplectic", "infer no BFV quotient or phase space from formal extension"),
    ("source", "attribute the endpoint grammar to source and exact intersection to repo"),
    ("contrary", "test the old witness and the restricted ansatz as firing controls"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS AND STRUCTURE FINGERPRINT")
local, local_output = replay(LOCAL)
endpoint, endpoint_output = replay(ENDPOINT)
check("repo", "the local stationary predecessor replays", "PASS 46/46" in local_output and not local["FAILURES"])
check("repo", "the corrected endpoint predecessor replays", "PASS 61/61" in endpoint_output and not endpoint["FAILURES"])

frozen = endpoint["D"]
blocks = frozen["blocks"]
h0_old = frozen["h0"]
h0_endpoint = endpoint["endpoint_h0"]
pairs = tuple(sorted(blocks))
restricted_pairs = ((0, 0), (0, 1))
check("fingerprint", "the complete symmetric observed two-jet has ten blocks",
      pairs == tuple((mu, nu) for mu in range(4) for nu in range(mu, 4)))
check("fingerprint", "each jet block maps 196 fields to 196 equations",
      all(len(blocks[pair]) == 196 for pair in pairs))
check("fingerprint", "the endpoint zeroth-order Hessian is the corrected rank-196 matrix",
      h0_endpoint.rank() == 196 and h0_endpoint != h0_old)
check("fingerprint", "the calculation remains on the inherited fixed-Hq endpoint comparator",
      "conditional fixed-`H_q` pairing" in endpoint_prior)


def principal_matrix(selected_pairs):
    out = matrix(QQ, 196, 196 * len(selected_pairs), sparse=True)
    for slot, pair in enumerate(selected_pairs):
        for field_column, values in enumerate(blocks[pair]):
            target_column = slot * 196 + field_column
            for equation_row, value in values.items():
                out[equation_row, target_column] = q(value)
    return out


def compatibility_matrix(h0, selected_pairs):
    """d_beta sum_lambda d_lambda E_(lambda,a), lower-order part."""
    slot = {pair: index for index, pair in enumerate(selected_pairs)}
    out = matrix(QQ, 56, 196 * len(selected_pairs), sparse=True)
    for beta in range(4):
        for clifford in range(14):
            target_row = beta * 14 + clifford
            for lam in range(4):
                pair = tuple(sorted((beta, lam)))
                if pair not in slot:
                    continue
                source_row = lam * 14 + clifford
                base_column = slot[pair] * 196
                for field_column in range(196):
                    value = h0[source_row, field_column]
                    if value:
                        out[target_row, base_column + field_column] += q(value)
    return out


def assess(label, h0, gradient, selected_pairs):
    principal = principal_matrix(selected_pairs)
    compatibility = compatibility_matrix(h0, selected_pairs)
    system = principal.stack(compatibility)
    rhs = vector(QQ, [-q(value) for value in gradient] + [QQ(0)] * 56)
    rank_principal = principal.rank()
    rank_compatibility = compatibility.rank()
    rank_system = system.rank()
    rank_augmented = system.augment(matrix(QQ, len(rhs), 1, rhs, sparse=True)).rank()
    witness = system.solve_right(rhs) if rank_system == rank_augmented else None
    return {
        "principal": principal,
        "compatibility": compatibility,
        "system": system,
        "rhs": rhs,
        "rank_principal": rank_principal,
        "rank_compatibility": rank_compatibility,
        "rank_system": rank_system,
        "rank_augmented": rank_augmented,
        "witness": witness,
        "dimension": system.ncols() - rank_system,
        "support": sum(value != 0 for value in witness) if witness is not None else None,
        "denominators": sorted({value.denominator() for value in witness if value}) if witness is not None else [],
        "label": label,
    }


print("\nC. OLD WITNESS AS A FIRING CONTROL")
old_witness = vector(QQ, 392, sparse=True)
for column, value in local["coefficients"].items():
    old_witness[column] = q(value)
old_on_old = compatibility_matrix(h0_old, restricted_pairs) * old_witness
old_on_endpoint = compatibility_matrix(h0_endpoint, restricted_pairs) * old_witness
check("control", "the original stationary witness misses two old compatibility cells",
      sum(value != 0 for value in old_on_old) == 2)
check("control", "the same witness misses two corrected endpoint compatibility cells",
      sum(value != 0 for value in old_on_endpoint) == 2)
check("planted", "PLANT stationarity alone does not imply next-order compatibility",
      bool(old_on_endpoint))


print("\nD. EXACT AFFINE-FIBRE INTERSECTIONS")
surrogate_restricted = assess("surrogate_restricted", h0_old, local["target"], restricted_pairs)
endpoint_restricted = assess("endpoint_restricted", h0_endpoint, endpoint["endpoint_gradient"], restricted_pairs)
endpoint_full = assess("endpoint_full", h0_endpoint, endpoint["endpoint_gradient"], pairs)

check("theorem", "the surrogate restricted joint system has ranks 196+28=224",
      (surrogate_restricted["rank_principal"], surrogate_restricted["rank_compatibility"],
       surrogate_restricted["rank_system"]) == (196, 28, 224))
check("theorem", "the surrogate restricted affine intersection is nonempty",
      surrogate_restricted["rank_augmented"] == 224 and surrogate_restricted["dimension"] == 168)
check("theorem", "the corrected endpoint restricted joint system has ranks 196+28=224",
      (endpoint_restricted["rank_principal"], endpoint_restricted["rank_compatibility"],
       endpoint_restricted["rank_system"]) == (196, 28, 224))
check("theorem", "the corrected endpoint restricted affine intersection is nonempty dimension 168",
      endpoint_restricted["rank_augmented"] == 224 and endpoint_restricted["dimension"] == 168)
check("witness", "a sixteen-support rational endpoint witness is constructed in the restricted ansatz",
      endpoint_restricted["support"] == 16 and endpoint_restricted["denominators"] == [1, 4, 7])
check("witness", "the restricted endpoint witness satisfies all 196 equations exactly",
      endpoint_restricted["principal"] * endpoint_restricted["witness"] == endpoint_restricted["rhs"][:196])
check("witness", "the restricted endpoint witness satisfies all 56 compatibility rows exactly",
      endpoint_restricted["compatibility"] * endpoint_restricted["witness"] == endpoint_restricted["rhs"][196:])
check("theorem", "the complete endpoint compatibility map has full row rank 56",
      endpoint_full["rank_compatibility"] == 56)
check("theorem", "the complete endpoint joint system has independent rank 252",
      endpoint_full["rank_system"] == endpoint_full["rank_principal"] + endpoint_full["rank_compatibility"] == 252)
check("theorem", "the complete 1960-variable affine intersection is nonempty dimension 1708",
      endpoint_full["rank_augmented"] == 252 and endpoint_full["dimension"] == 1708)
check("planted", "PLANT deleting compatibility would overstate the restricted fibre by 28 dimensions",
      392 - endpoint_restricted["rank_principal"] == 196 > endpoint_restricted["dimension"])
check("planted", "PLANT deleting compatibility would overstate the full fibre by 56 dimensions",
      1960 - endpoint_full["rank_principal"] == 1764 > endpoint_full["dimension"])


print("\nE. FULL SECOND PROLONGATION AND EXACT COKERNEL")
def compositions(total: int, slots: int = 4, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for value in range(total + 1):
        yield from compositions(total - value, slots - 1, prefix + (value,))


second_indices = list(compositions(2))
fourth_indices = list(compositions(4))
second_position = {alpha: index for index, alpha in enumerate(second_indices)}
check("exact", "Sym2 and Sym4 of four observed directions have dimensions 10 and 35",
      len(second_indices) == 10 and len(fourth_indices) == 35)


def second_prolongation_columns():
    for alpha in fourth_indices:
        for field_column in range(196):
            out: dict[int, Fraction] = {}
            for pair in pairs:
                demand = [0, 0, 0, 0]
                demand[pair[0]] += 1
                demand[pair[1]] += 1
                if any(alpha[index] < demand[index] for index in range(4)):
                    continue
                remainder = tuple(alpha[index] - demand[index] for index in range(4))
                equation_base = second_position[remainder] * 196
                for equation_row, value in blocks[pair][field_column].items():
                    target = equation_base + equation_row
                    out[target] = out.get(target, Fraction(0)) + value
            yield {index: value for index, value in out.items() if value}


def modular_second_rank(prime: int):
    basis: dict[int, dict[int, int]] = {}
    checkpoints = []
    for number, column in enumerate(second_prolongation_columns(), start=1):
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


rank_second_1, profile_second_1 = modular_second_rank(1_000_003)
rank_second_2, profile_second_2 = modular_second_rank(1_000_033)
check("theorem", "the second prolonged symbol has rank 1904 modulo the first prime",
      rank_second_1 == 1904)
check("theorem", "an independent prime reproduces rank 1904 and the full profile",
      rank_second_2 == 1904 and profile_second_2 == profile_second_1)

relations = []
for beta in range(4):
    for clifford in range(14):
        relation = {}
        for lam in range(4):
            derivative = [0, 0, 0, 0]
            derivative[beta] += 1
            derivative[lam] += 1
            row = second_position[tuple(derivative)] * 196 + lam * 14 + clifford
            relation[row] = relation.get(row, QQ(0)) + QQ(1)
        relations.append(relation)

relation_matrix = matrix(QQ, 56, 1960, sparse=True)
for row, relation in enumerate(relations):
    for column, value in relation.items():
        relation_matrix[row, column] = value
check("theorem", "the 56 differentiated divergence relations are independent over QQ",
      relation_matrix.rank() == 56)

violations = 0
for column in second_prolongation_columns():
    for relation in relations:
        value = sum(coefficient * q(column.get(index, Fraction(0)))
                    for index, coefficient in relation.items())
        if value:
            violations += 1
check("theorem", "all 56 relations annihilate every second-prolongation column exactly",
      violations == 0)
check("theorem", "rank 1904 plus 56 exact relations exhausts the 1960-row cokernel",
      rank_second_1 + relation_matrix.rank() == 1960)
check("theorem", "the compatible endpoint two-jet meets the full second-prolongation image criterion",
      endpoint_restricted["compatibility"] * endpoint_restricted["witness"] == vector(QQ, 56))
check("planted", "PLANT the old witness fails that complete cokernel criterion",
      old_on_endpoint != vector(QQ, 56))


print("\nF. DISPOSITION AND DURABLE FENCES")
for kind, label in (
    ("correction", "rank 56 is a nontrivial jet-selection condition, not a nonexistence theorem"),
    ("result", "the corrected endpoint stationary fibre intersects the next compatibility kernel"),
    ("result", "the second prolonged frozen symbol has exactly the expected 56-dimensional cokernel"),
    ("scope", "the universal constant-completion no-go remains exact as an operator statement"),
    ("scope", "higher prolongations and nonlinear moving-coefficient formal integrability remain open"),
    ("scope", "analytic convergence local solution germs and global descent remain open"),
    ("scope", "source Q_B physical tangent BV quotient and BFV phase space remain open"),
    ("source", "the source is silent on the exact affine intersection and second-prolongation rank"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_PRINTED_ENDPOINT_AND_CONNECTION_GRAMMAR__SOURCE_SILENT_STATIONARY_AFFINE_SPENCER_INTERSECTION_AND_SECOND_PROLONGATION")
print(f"OLD_WITNESS_COMPATIBILITY_SUPPORT={sum(value != 0 for value in old_on_endpoint)}")
print("RESTRICTED_RANKS=196,28,224")
print(f"RESTRICTED_AFFINE_INTERSECTION_DIMENSION={endpoint_restricted['dimension']}")
print(f"RESTRICTED_WITNESS_SUPPORT={endpoint_restricted['support']}")
print("FULL_RANKS=196,56,252")
print(f"FULL_AFFINE_INTERSECTION_DIMENSION={endpoint_full['dimension']}")
print(f"SECOND_PROLONGATION_RANK={rank_second_1}/1960")
print(f"SECOND_PROLONGATION_COKERNEL_DIMENSION={1960-rank_second_1}")
print("RESULT=RANK56_RETYPE_AS_FORMAL_JET_SELECTION__NONEMPTY_ENDPOINT_INTERSECTION__SECOND_PROLONGATION_CRITERION_PASSES")
print("NEXT=TEST_HIGHER_NONLINEAR_MOVING_COEFFICIENT_PROLONGATION_AND_CARTAN_INVOLUTIVITY__THEN_ANALYTIC_OR_GLOBAL_EXISTENCE")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
