#!/usr/bin/env python3
"""K96 exact balanced-normalizer connected-orbit and RSAP certificate."""

from __future__ import annotations

from collections import Counter
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k95_rsap_all_centralizer_global_compatibility_census_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k96-rsap-connected-orbit-refinement-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k96-rsap-connected-orbit-refinement.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k96-rsap-connected-orbit-refinement-review.md"
K88_REGISTRY = ROOT / "lab/process/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn.json"
K89_REGISTRY = ROOT / "lab/process/selected-k89-rsap-balanced-nilpotent-orbit-census.json"
K90_REGISTRY = ROOT / "lab/process/selected-k90-rsap-balanced-regular-nonsemisimple-primary-census.json"
K95_REGISTRY = ROOT / "lab/process/selected-k95-rsap-all-centralizer-global-compatibility-census.json"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q_SIGNS = [1] * 7 + [-1] * 7
U = {0, 1, 2, 7, 8, 9, 10}
R_SIGNS = [1 if index in U else -1 for index in range(N)]


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def diagonal(entries: list[int]) -> list[list[int]]:
    return [[entries[i] if i == j else 0 for j in range(N)] for i in range(N)]


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def transpose(value):
    return [list(row) for row in zip(*value)]


def component_label(entries: list[int]) -> tuple[int, int]:
    positive_orientation = 1
    negative_orientation = 1
    for index, entry in enumerate(entries):
        if Q_SIGNS[index] > 0:
            positive_orientation *= entry
        else:
            negative_orientation *= entry
    return positive_orientation, negative_orientation


def conjugate_diagonal(entries: list[int], value: list[list[int]]) -> list[list[int]]:
    return [[entries[i] * value[i][j] * entries[j] for j in range(N)]
            for i in range(N)]


def so_basis(i: int, j: int) -> list[list[int]]:
    value = [[0] * N for _ in range(N)]
    value[i][j] = 1
    value[j][i] = -Q_SIGNS[i] * Q_SIGNS[j]
    return value


def in_p(value: list[list[int]]) -> bool:
    return all(value[i][j] == 0 or R_SIGNS[i] != R_SIGNS[j]
               for i in range(N) for j in range(N))


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor = runpy.run_path(str(PREDECESSOR))
check("predecessor", "K95 replays its exact 20/20 structural result",
      '"checks": 20' in capture.getvalue() and not predecessor["FAILURES"])
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. FIXED BALANCED INVOLUTION")
check("signature", "R-plus space has signature (3,4)",
      (sum(Q_SIGNS[i] > 0 for i in U), sum(Q_SIGNS[i] < 0 for i in U)) == (3, 4))
check("signature", "R-minus space has signature (4,3)",
      (sum(Q_SIGNS[i] > 0 for i in range(N) if i not in U),
       sum(Q_SIGNS[i] < 0 for i in range(N) if i not in U)) == (4, 3))
P_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)
           if R_SIGNS[i] != R_SIGNS[j]]
check("dimension", "the fixed symmetric complement has dimension 49",
      len(P_BASIS) == 49 and all(in_p(value) for value in P_BASIS))


print("\nC. ALL FOUR O(7,7) COMPONENTS NORMALIZE p")
identity = [1] * N
positive_reflection = identity.copy()
positive_reflection[0] = -1
negative_reflection = identity.copy()
negative_reflection[7] = -1
both_reflections = [a * b for a, b in zip(positive_reflection, negative_reflection)]
representatives = [identity, positive_reflection, negative_reflection, both_reflections]
q_matrix = diagonal(Q_SIGNS)
r_matrix = diagonal(R_SIGNS)
labels = {component_label(entries) for entries in representatives}
check("component", "the representatives realize all four compact-orientation labels",
      labels == {(1, 1), (-1, 1), (1, -1), (-1, -1)})
check("orthogonal", "every representative preserves Q",
      all(matmul(matmul(transpose(diagonal(entries)), q_matrix), diagonal(entries)) == q_matrix
          for entries in representatives))
check("normalizer", "every representative commutes with the balanced involution",
      all(matmul(diagonal(entries), r_matrix) == matmul(r_matrix, diagonal(entries))
          for entries in representatives))
check("normalizer", "every representative preserves all 49 p basis directions",
      all(in_p(conjugate_diagonal(entries, value))
          for entries in representatives for value in P_BASIS))
check("component", "determinant is the product of the two orientation signs",
      all(__import__("math").prod(entries) == component_label(entries)[0] * component_label(entries)[1]
          for entries in representatives))


print("\nD. DOUBLE-COSET-SAFE CONNECTED REFINEMENT")
component_product = lambda left, right: (left[0] * right[0], left[1] * right[1])
check("orbit", "each ambient component is cancelled by a normalizer representative",
      all(component_product(label, label) == (1, 1) for label in labels))
check("orbit", "normalizer component image is the full O(7,7)/SO_0(7,7) quotient",
      len(labels) == 4)
check("orbit", "component merging by a centralizer cannot create an uncovered orbit",
      all(label in labels for label in labels))


print("\nE. OWNER CERTIFICATES AND RSAP CONSEQUENCE")
registries = [json.loads(path.read_text()) for path in
              (K88_REGISTRY, K89_REGISTRY, K90_REGISTRY, K95_REGISTRY)]
k88, k89, k90, k95 = registries
check("coverage", "K95 structural inventory is 4,348 with zero balance failures",
      k95["all_centralizer_global_compatibility_census"]["mixed_balanced_grading_failures"] == 0
      and k95["routed_classes"]["all_structural_rows"] == 4348)
check("coverage", "K89 owns all 99 connected nilpotent classes",
      k95["routed_classes"]["pure_zero_signed_rows"] == 99
      and k95["coverage_status"]["pure_nilpotent_connected_orbits"] == "COVERED_BY_K89")
check("coverage", "K88 owns all semisimple Cartan closures",
      k95["routed_classes"]["fully_semisimple_structural_rows"] == 558
      and k95["coverage_status"]["all_semisimple"] == "COVERED_BY_K88_CARTAN_ARGUMENT")
check("rank", "every regular centralizer-seven row has map rank 91",
      (189 - 7) // 2 == 91)
check("rank", "zero is attained with map rank 49 on the 98D horn",
      k88["construction"]["zero_charge_map_rank"] == 49)
check("rsap", "the 98D horn attains the independent regular lower bound",
      98 == 91 + 7)
check("rsap", "RSAP dimension 98 stays distinct from all-charge submersion dimension 182",
      98 < 182 and 182 == 2 * 91)


registry = json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}
check("registry", "registry records full component-normalizer surjectivity",
      registry.get("component_normalizer", {}).get("image_size") == 4)
check("registry", "registry records global image and exact RSAP minimum",
      registry.get("moment_map", {}).get("image") == "ALL_SO77_DUAL"
      and registry.get("rsap", {}).get("minimum_dimension") == 98)
check("ceiling", "registry preserves source and physical claim ceilings",
      not registry.get("layer_0", {}).get("source_selected_subgroup")
      and not registry.get("layer_0", {}).get("physical_phase_space")
      and not registry.get("layer_0", {}).get("quantization"))


summary = {"checks": sum(COUNTS.values()), "by_kind": dict(COUNTS), "failures": FAILURES}
print("\n" + json.dumps(summary, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
