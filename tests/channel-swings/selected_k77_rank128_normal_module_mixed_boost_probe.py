#!/usr/bin/env sage-python
"""Reconfirm the K77 rank-128 normal module and resolve its convention fork.

The held v0.228 certificate already identifies the ten transverse defect
images with the canonical ``N^* tensor S`` observation kernel.  This probe
does not reopen that theorem.  It adds an exact characteristic-zero check of
the vector/covector sign convention and then replays the held GF(1009)
carrier/graph certificate.

The result distinguishes the fully ``so(6,4)``-natural carrier inclusion from
the selected H640 graph and zero-form-seed trivializations, which remain only
``so(6)+so(4)``-natural.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from runpy import run_path

from sage.all import QQ, diagonal_matrix, identity_matrix, matrix


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def tensor_all(factors):
    out = matrix(QQ, [[1]], sparse=True)
    for factor in factors:
        out = out.tensor_product(factor)
    return out


print("A. ANTI-REDO AND LAYER-ZERO RECEIPT", flush=True)
held_result = (
    ROOT
    / "explorations/conditional-build/selected-k77-rank128-observation-kernel-module-2026-08-13.md"
).read_text(encoding="utf-8")
held_ledger = (
    ROOT / "lab/process/conditional-physics-ledger-v0.228.json"
).read_text(encoding="utf-8")
for label in (
    "ten rank-128 images versus one repeated image",
    "their direct sum versus the canonical normal module",
    "carrier inclusion versus selected H640 graph splitting",
    "normal covectors versus normal vectors",
    "configuration kernel versus physical BV cohomology",
):
    check("layer0", label, True)
check(
    "prior_art",
    "v0.228 already closes the full carrier-module identification",
    "FULL_SO6_4_MODULE_EXACT" in held_result
    and "canonical 1280-dimensional observation kernel N* tensor S" in held_ledger,
)


print("B. CHARACTERISTIC-ZERO VECTOR/COVECTOR CONVENTIONS", flush=True)
i2 = identity_matrix(QQ, 2, sparse=True)
s1 = matrix(QQ, [[0, 1], [1, 0]], sparse=True)
s3 = matrix(QQ, [[1, 0], [0, -1]], sparse=True)
eps = matrix(QQ, [[0, 1], [-1, 0]], sparse=True)

plus = []
minus = []
for k in range(7):
    plus.append(tensor_all([s3] * k + [s1] + [i2] * (6 - k)))
    minus.append(tensor_all([s3] * k + [eps] + [i2] * (6 - k)))
gammas = plus + minus
eta = [1] * 7 + [-1] * 7
normal = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
pairs = [(i, j) for offset, i in enumerate(normal) for j in normal[offset + 1 :]]
metric_n = diagonal_matrix(QQ, [eta[axis] for axis in normal], sparse=True)


def vector_generator(i: int, j: int):
    generator = matrix(QQ, 14, 14, sparse=True)
    generator[i, j] = eta[j]
    generator[j, i] = -eta[i]
    return generator


def normal_block(generator):
    return matrix(
        QQ,
        10,
        10,
        lambda row, column: generator[normal[row], normal[column]],
        sparse=True,
    )


clifford_covariance = []
correct_covector = []
wrong_vector = []
metric_conjugacy = []
for i, j in pairs:
    full_vector = vector_generator(i, j)
    restricted_vector = normal_block(full_vector)
    dual_covector = -restricted_vector.transpose()
    spin_generator = gammas[i] * gammas[j] / QQ(2)
    clifford_covariance.extend(
        spin_generator * gammas[k] - gammas[k] * spin_generator
        == sum((full_vector[row, k] * gammas[row] for row in range(14)),
               matrix(QQ, 128, 128, sparse=True))
        for k in range(14)
    )
    correct_covector.append(dual_covector == -restricted_vector.transpose())
    wrong_vector.append(restricted_vector == dual_covector)
    metric_conjugacy.append(
        dual_covector == metric_n * restricted_vector * metric_n.inverse()
    )

same_sign = [pair for pair in pairs if eta[pair[0]] == eta[pair[1]]]
mixed_sign = [pair for pair in pairs if eta[pair[0]] != eta[pair[1]]]
check(
    "clifford",
    "the rational spin generators satisfy all 45-by-14 Clifford covariance identities",
    len(clifford_covariance) == 630 and all(clifford_covariance),
)
check(
    "covector",
    "the dual normal action is exactly -A^T for all 45 generators",
    len(correct_covector) == 45 and all(correct_covector),
)
check(
    "signature",
    "the (6,4) metric conjugates the vector action to the covector action",
    len(metric_conjugacy) == 45 and all(metric_conjugacy),
)
check(
    "convention",
    "using the vector action on a covector label agrees on exactly 21 compact generators",
    len(same_sign) == 21
    and len(mixed_sign) == 24
    and sum(wrong_vector) == 21
    and all(wrong_vector[pairs.index(pair)] for pair in same_sign)
    and not any(wrong_vector[pairs.index(pair)] for pair in mixed_sign),
)


print("C. HELD EXACT DEFECT AND GRAPH REPLAY", flush=True)
held = run_path(
    str(ROOT / "tests/channel-swings/portfolio_rank128_observation_kernel_module_probe.py")
)
prior = held["prior"]
check(
    "defects",
    "the ten filed defects remain pairwise disjoint with total rank 1280",
    prior["all_join"].rank() == 1280
    and set(prior["joins"].values()) == {256}
    and set(prior["intersections"].values()) == {0},
)
check(
    "kernel",
    "their direct sum remains exactly ker observation",
    prior["observation"].rank() == 640
    and (prior["observation"] * prior["all_join"]).is_zero()
    and prior["all_join"].rank() == prior["total"] - prior["observation"].rank(),
)
check(
    "module",
    "the canonical normal-covector-spinor inclusion intertwines all 45 generators",
    len(held["canonical_intertwiners"]) == 45
    and all(held["canonical_intertwiners"].values()),
)
check(
    "graph",
    "the selected H640 lift and complement intertwine exactly the 21 compact generators",
    sum(held["lift_intertwiners"].values()) == 21
    and sum(held["complement_intertwiners"].values()) == 21,
)
check(
    "graph",
    "all 24 mixed boosts still detect the selected graph/zero-seed splitting",
    all(
        not held["lift_intertwiners"][pair]
        and not held["complement_intertwiners"][pair]
        and not prior["equivariant"][pair]
        for pair in mixed_sign
    ),
)


print("D. SOURCE, SCOPE, AND FIRING CONTROLS", flush=True)
result_text = (
    ROOT
    / "explorations/conditional-build/selected-k77-rank128-normal-module-mixed-boost-2026-08-14.md"
).read_text(encoding="utf-8")
source_text = (
    ROOT
    / "lab/sources/selected-k77-rank128-normal-module-mixed-boost-source-return-2026-08-14.md"
).read_text(encoding="utf-8")
review_text = (
    ROOT
    / "lab/process/hostile-reviews/2026-08-14-selected-k77-rank128-normal-module-mixed-boost-review.md"
).read_text(encoding="utf-8")
check(
    "source",
    "SC-GEN-50/56 confirm only the carrier grammar and pullback proposal",
    "SC-GEN-50" in source_text
    and "SC-GEN-56" in source_text
    and "SOURCE-SILENT" in source_text,
)
check(
    "scope",
    "the result preserves the graph/BV, physical carrier, domain and cohomology boundary",
    "action- or BV-owned moving graph" in result_text
    and "physical cohomology" in result_text
    and "no ledger" in result_text.lower(),
)
check(
    "hostile",
    "the review rejects carrier-to-physics and convention-to-graph overclaims",
    "configuration module" in review_text
    and "does not repair the selected graph" in review_text,
)
check(
    "plant",
    "PLANT the wrong vector convention cannot be reported as full covector equivariance",
    sum(wrong_vector) == 21 and not all(wrong_vector),
)
check(
    "plant",
    "PLANT the exact carrier theorem cannot be reported as a fully natural selected graph",
    all(held["canonical_intertwiners"].values())
    and not all(held["lift_intertwiners"].values()),
)

print(
    "RESULT=HELD_V0228_FULL_NSTAR_TENSOR_S_MODULE_RECONFIRMED__"
    "VECTOR_COVECTOR_SIGN_FORK_RESOLVED_IN_CHARACTERISTIC_ZERO__"
    "SELECTED_GRAPH_REMAINS_COMPACT_NATURAL_ONLY"
)
print(
    "NEXT=CONSTRUCT_OR_KILL_ONE_ACTION_OR_BV_OWNED_MOVING_GRAPH_CORRECTION__"
    "DO_NOT_REBUILD_THE_CARRIER_OR_RUN_TEN_REPAIRS"
)
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
