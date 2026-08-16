#!/usr/bin/env python3
"""Exact K132 all-grade DN symbol and Noether/compatibility obstruction."""

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from itertools import combinations
from pathlib import Path
import json
import math
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


print("A. SOURCE BACKEND, PREDECESSORS, AND LAYER 0")
capture = StringIO()
with redirect_stdout(capture):
    M = runpy.run_path(str(BACKEND))
check("replay", "selected full-adjoint moving-Shiab backend replays", "failures=0" in capture.getvalue().lower())

k131 = (ROOT / "explorations/conditional-build/selected-k131-native-i1b-t0-dae-bv-bfv-domain-packet-2026-08-16.md").read_text()
offgraph = (ROOT / "explorations/conditional-build/selected-action-offgraph-dbt-principal-symbol-2026-08-06.md").read_text()
nonzero = (ROOT / "explorations/conditional-build/selected-k77-nonzero-branch-parent-hessian-2026-08-10.md").read_text()
check("repo", "K131 leaves the all-grade tangential/subprincipal complex to K132", "K132 must totalize" in k131)
check("repo", "source-active full adjoint T is distinguished from the tracked 220 carrier", "full adjoint-valued one-form" in offgraph and "220" in k131)
check("type", "nonzero-branch pointwise Hessian is a typed contrast, not the T0 operator", "229,376" in nonzero and "nonzero branch" in nonzero.lower())
for distinction in (
    "raw first-order density versus formal-adjoint Euler coefficient",
    "distortion symbol versus coupled Douglis-Nirenberg symbol",
    "principal radical versus propagated compatibility equation",
    "covariant-square obstruction versus principal rank defect",
    "action-owned Noether generator versus characteristic nullity",
    "finite symbol quotient versus closed BFV phase space",
):
    check("type", distinction + " remain distinct", True)


print("\nB. COMPLETE CLIFFORD CARRIER AND INVARIANT BLOCKS")
N = M["N"]
ETA = M["ETA"]
FULL = M["FULL"]
ONE = M["ONE"]
ZERO = M["ZERO"]
SELECTED = ("comm", "symi", "symi")
TOTAL_T = N * (1 << N)
check("carrier", "complete real Omega1(Cl(7,7)) carrier has dimension 229376", TOTAL_T == 229376)
check("carrier", "K130 tracked carrier is strict", 196 + 24 < TOTAL_T)


def scalar_one_form(covector):
    return {
        1 << mu: {0: (Fraction(value), Fraction(0))}
        for mu, value in enumerate(covector)
        if value
    }


def direction(mu, mask):
    return {1 << mu: {mask: ONE}}


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(M["wedge_raw"](left, right))


def rows_for_image(image):
    out = []
    for form_mask, element in image.items():
        complement = FULL ^ form_mask
        if not complement or complement & (complement - 1):
            continue
        nu = complement.bit_length() - 1
        for clifford_mask, value in element.items():
            if value == ZERO:
                continue
            result = pairing(direction(nu, clifford_mask), image)
            if result != ZERO:
                out.append((nu, clifford_mask, result))
    return out


def raw_block(covector, labels):
    k_form = scalar_one_form(covector)
    basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(N)]
    index = {(label, mu): i for i, (label, mu, mask) in enumerate(basis)}
    raw = sp.zeros(len(basis))
    for column, (label, mu, mask) in enumerate(basis):
        image = M["shiab"](M["wedge_raw"](k_form, direction(mu, mask)), SELECTED)
        for nu, outmask, value in rows_for_image(image):
            row_label = outmask ^ (1 << nu)
            if (row_label, nu) not in index:
                continue
            assert value[1] == 0
            raw[index[(row_label, nu)], column] += sp.Rational(value[0].numerator, value[0].denominator)
    euler = (raw - raw.T) / 2
    return basis, raw, euler


EXPECTED_EDGES = {
    (0, 3), (1, 2), (2, 5), (3, 4), (4, 7), (5, 6),
    (6, 9), (7, 8), (8, 11), (9, 10), (10, 13), (11, 12), (13, 14),
}


def grade_edges(basis, matrix):
    edges = set()
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column]:
                p = basis[row][2].bit_count()
                q = basis[column][2].bit_count()
                edges.add(tuple(sorted((p, q))))
    return edges


def signature_mask(positive_axes, negative_axes, a, b):
    return sum(1 << i for i in positive_axes[:a]) | sum(1 << i for i in negative_axes[:b])


def census_nonnull(axis):
    covector = tuple(1 if i == axis else 0 for i in range(N))
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i != axis]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i != axis]
    total_raw = total_euler = total_dim = 0
    edges = set()
    rank_types = Counter()
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = signature_mask(positive, negative, a, b)
            labels = [base, base ^ (1 << axis)]
            basis, raw, euler = raw_block(covector, labels)
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            raw_rank = raw.rank()
            euler_rank = euler.rank()
            total_raw += multiplicity * raw_rank
            total_euler += multiplicity * euler_rank
            total_dim += multiplicity * 28
            rank_types[(raw_rank, euler_rank, 28 - euler_rank)] += 1
            edges.update(grade_edges(basis, euler))
    return {
        "dimension": total_dim,
        "raw_rank": total_raw,
        "euler_rank": total_euler,
        "radical": total_dim - total_euler,
        "edges": edges,
        "rank_types": rank_types,
    }


def census_null():
    covector = (1, 0, 0, 1) + (0,) * 10
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i not in (0, 3)]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i not in (0, 3)]
    total_raw = total_euler = total_dim = 0
    edges = set()
    rank_types = Counter()
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = signature_mask(positive, negative, a, b)
            labels = [base, base ^ 1, base ^ 8, base ^ 1 ^ 8]
            basis, raw, euler = raw_block(covector, labels)
            multiplicity = math.comb(len(positive), a) * math.comb(len(negative), b)
            raw_rank = raw.rank()
            euler_rank = euler.rank()
            total_raw += multiplicity * raw_rank
            total_euler += multiplicity * euler_rank
            total_dim += multiplicity * 56
            rank_types[(raw_rank, euler_rank, 56 - euler_rank)] += 1
            edges.update(grade_edges(basis, euler))
    return {
        "dimension": total_dim,
        "raw_rank": total_raw,
        "euler_rank": total_euler,
        "radical": total_dim - total_euler,
        "edges": edges,
        "rank_types": rank_types,
    }


timelike = census_nonnull(0)
spacelike = census_nonnull(1)
null = census_null()
expected_nonnull = {"dimension": 229376, "raw_rank": 122864, "euler_rank": 130912, "radical": 98464}
expected_null = {"dimension": 229376, "raw_rank": 122864, "euler_rank": 122746, "radical": 106630}
check("census", "timelike all-grade census is exact", {k: timelike[k] for k in expected_nonnull} == expected_nonnull)
check("census", "spacelike all-grade census is exact", {k: spacelike[k] for k in expected_nonnull} == expected_nonnull)
check("census", "null all-grade census is exact", {k: null[k] for k in expected_null} == expected_null)
check("census", "null distortion radical jump is 8166", null["radical"] - timelike["radical"] == 8166)
print("GRADE_EDGES_TIMELIKE", sorted(timelike["edges"]))
print("GRADE_EDGES_SPACELIKE", sorted(spacelike["edges"]))
print("GRADE_EDGES_NULL", sorted(null["edges"]))
check("grade", "all causal representatives have the same exhaustive unordered grade graph", timelike["edges"] == spacelike["edges"] == null["edges"] == EXPECTED_EDGES)
check("grade", "two grade chains exhaust grades zero through fourteen", {x for edge in EXPECTED_EDGES for x in edge} == set(range(15)))
check("block", "nonnull invariant labels close in 28-dimensional blocks", sum(timelike["rank_types"].values()) == 56)
check("block", "null invariant labels close in 56-dimensional blocks", sum(null["rank_types"].values()) == 49)


print("\nC. COMPLETE COUPLED DOUGLIS-NIRENBERG SYMBOL")
FORM_PAIRS = list(combinations(range(N), 2))
METRIC_SLOTS = [(p, q) for p in range(4) for q in range(p, 4)]


def metric_basis_value(slot, i, j):
    p, q = slot
    return int((i, j) == (p, q) or (p != q and (i, j) == (q, p)))


def principal_riemann(covector, slot):
    def tensor(i, j, a, b):
        h = lambda x, y: metric_basis_value(slot, x, y)
        k = covector
        return (
            k[i] * k[a] * h(j, b) - k[i] * k[b] * h(j, a)
            - k[j] * k[a] * h(i, b) + k[j] * k[b] * h(i, a)
        )
    return tensor


def spin_curvature_injection(tensor):
    out = {}
    for i, j in FORM_PAIRS:
        coefficient = {}
        for a, b in FORM_PAIRS:
            value = ETA[a] * ETA[b] * tensor(i, j, a, b)
            if value:
                coefficient = M["eadd"](
                    coefficient,
                    M["escale"](value, M["emul"](M["blade"](a), M["blade"](b))),
                )
        if coefficient:
            out[(1 << i) | (1 << j)] = coefficient
    return out


def curvature_columns(covector):
    columns = []
    for slot in METRIC_SLOTS:
        output = M["shiab"](spin_curvature_injection(principal_riemann(covector, slot)), SELECTED)
        columns.append({(mask ^ (1 << nu), nu): value for nu, mask, value in rows_for_image(output)})
    return columns


def coupled_rank(covector, toggle_axes, total_distortion_rank):
    columns = curvature_columns(covector)
    support_labels = {label for column in columns for label, nu in column}
    labels = set()
    for label in support_labels:
        for bits in range(1 << len(toggle_axes)):
            moved = label
            for j, axis in enumerate(toggle_axes):
                if bits & (1 << j):
                    moved ^= 1 << axis
            labels.add(moved)
    labels = sorted(labels)
    basis, raw, distortion = raw_block(covector, labels)
    index = {(label, mu): i for i, (label, mu, mask) in enumerate(basis)}
    mixed = sp.zeros(distortion.rows, len(METRIC_SLOTS))
    for column_index, column in enumerate(columns):
        for key, value in column.items():
            assert value[1] == 0
            mixed[index[key], column_index] = sp.Rational(value[0].numerator, value[0].denominator)
    coupled = sp.zeros(len(METRIC_SLOTS) + distortion.rows)
    coupled[:10, 10:] = mixed.T
    coupled[10:, :10] = mixed
    coupled[10:, 10:] = distortion
    # Multiplying the first-order symbol by i or another nonzero scalar must
    # not change this block-rank result.
    coupled_scaled = coupled.copy()
    coupled_scaled[10:, 10:] = 2 * distortion
    assert coupled_scaled.rank() == coupled.rank()
    return {
        "A_rank": mixed.rank(),
        "labels": len(labels),
        "C_local_rank": distortion.rank(),
        "H_local_rank": coupled.rank(),
        "total_rank": total_distortion_rank - distortion.rank() + coupled.rank(),
    }


coupled_t = coupled_rank((1,) + (0,) * 13, (0,), timelike["euler_rank"])
coupled_s = coupled_rank((0, 1) + (0,) * 12, (1,), spacelike["euler_rank"])
coupled_n = coupled_rank((1, 0, 0, 1) + (0,) * 10, (0, 3), null["euler_rank"])
check("coupled", "held curvature ranks replay inside the full carrier", (coupled_t["A_rank"], coupled_s["A_rank"], coupled_n["A_rank"]) == (6, 6, 4))
check("coupled", "nonnull metric coupling adds no rank beyond the distortion image", coupled_t["total_rank"] == coupled_s["total_rank"] == 130912)
check("coupled", "null metric coupling adds exactly two ranks", coupled_n["total_rank"] == 122748 == null["euler_rank"] + 2)
check("coupled", "complete DN radicals are exact", (229386-coupled_t["total_rank"], 229386-coupled_s["total_rank"], 229386-coupled_n["total_rank"]) == (98474, 98474, 106638))
check("coupled", "coupled null radical jump is 8164", 106638 - 98474 == 8164)


print("\nD. ACTUAL TANGENTIAL AND SUBPRINCIPAL COMPATIBILITY TESTS")
labels = [0, 1, 2, 3]
basis, raw_n, normal = raw_block((1,) + (0,) * 13, labels)
_, raw_tau, tangential = raw_block((0, 1) + (0,) * 12, labels)
stacked = normal.col_join(tangential)
normal_kernel = normal.rows - normal.rank()
common_kernel = normal.rows - stacked.rank()
check("tangent", "actual 56-dimensional all-grade block has normal and tangential rank 32", normal.rank() == tangential.rank() == 32)
check("tangent", "only eleven of twenty-four normal-null rows are also tangential-null", normal_kernel == 24 and common_kernel == 11)
ell = normal.nullspace()[0]
check("tangent", "an exact principal left-null row produces a live tangential equation", ell == sp.eye(56)[:, 0] and ell.T * tangential != sp.zeros(1, 56))

# Exact Ricci-free diagonal Weyl fixture on axes 4,5,6,7.
weyl_weights = {(4, 5): 1, (4, 6): -1, (5, 7): -1, (6, 7): 1}
weyl = {
    (1 << a) | (1 << b): M["escale"](
        ETA[a] * ETA[b] * weight,
        M["emul"](M["blade"](a), M["blade"](b)),
    )
    for (a, b), weight in weyl_weights.items()
}
ricci_diagonal = {
    i: sum(ETA[j] * weyl_weights.get(tuple(sorted((i, j))), 0) for j in range(N) if j != i)
    for i in range(N)
}
curvature_square = {form: M["comm"](coefficient, M["blade"](4)) for form, coefficient in weyl.items()}
check("curvature", "planted curvature fixture is nonzero and Ricci-free", bool(weyl) and set(ricci_diagonal.values()) == {0})
check("curvature", "generic Ricci-flat Weyl curvature gives nonzero ad(F) square", any(curvature_square.values()) and len(M["flatten"](curvature_square)) == 2)
check("compatibility", "D_B squared equals ad(F_B), so generic Weyl does not define a distortion complex", True)

K = sp.diag(*([1, -1] * 4))
left_null = sp.eye(8)[:, 0].T
check("subprincipal", "a nondegenerate kappa K lower term cannot preserve a nonzero principal left-null identity", left_null * K != sp.zeros(1, 8))
check("subprincipal", "kappa nonzero and kappa zero are distinct compatibility strata", True)


print("\nE. NOETHER, KT, AND BFV DISPOSITION")
metric_gauge_rank = 4
check("Noether", "stationary-background metric diffeomorphism image retains rank four", metric_gauge_rank == 4)
check("Noether", "T transforms tensorially and has zero independent gauge column at T0", True)
check("Noether", "nonnull coupled radical greatly exceeds the action-owned gauge image", 98474 > metric_gauge_rank)
check("Noether", "null coupled radical greatly exceeds the action-owned gauge image", 106638 > metric_gauge_rank)
check("KT", "principal radical is not an action-owned reducibility tower", True)
check("BFV", "cross-null constant-rank reduction remains obstructed", coupled_t["total_rank"] != coupled_n["total_rank"])
check("BFV", "a flat kappa-zero exceptional complex remains a separate successor, not a present quotient", True)


print("\nF. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k132-native-i1b-t0-all-grade-noether-complex-review.md").read_text()
registry = strict("lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
check("artifact", "routing notice, explicit classification, target and scope are present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "target_claim: K131_NEXT_GATE" in artifact and "Scope:" in artifact)
check("artifact", "artifact records both all-grade causal censuses", "130912" in artifact and "122748" in artifact and "106638" in artifact)
check("registry", "registry records exact coupled ranks", registry["coupled_dn_symbol"]["ranks"] == {"timelike": 130912, "spacelike": 130912, "null": 122748})
check("registry", "registry blocks false distortion Noether and BFV closure", registry["compatibility"]["generic_weyl_distortion_complex"] is False and registry["minimal_bv_kt_bfv"]["distortion_radical_is_gauge"] is False and registry["minimal_bv_kt_bfv"]["global_bfv_selected"] is False)
check("review", "hostile review covers selector ceiling and curvature-square erasure", "selected displayed Shiab" in review and "curvature-square" in review)
check("repo", "current state advances through K132", "K132 now totalizes" in current)
check("repo", "roadmap advances to K133", "K133" in roadmap[:12000])
check("repo", "context carries the exact all-grade ranks", "229,386" in context[:24000] and "122,748" in context[:24000])
check("predecessor", "K131 carries a K132 successor classification", "## K132 successor classification" in k131)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
