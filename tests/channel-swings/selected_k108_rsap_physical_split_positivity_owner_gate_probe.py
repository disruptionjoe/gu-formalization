#!/usr/bin/env python3
"""Exact K108 physical-split positivity and reduction-owner gate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K107_PROBE = ROOT / "tests/channel-swings/selected_k107_rsap_phase_space_compatible_complex_positivity_probe.py"
REGISTRY = ROOT / "lab/process/selected-k108-rsap-physical-split-positivity-owner-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k108-rsap-physical-split-positivity-owner-gate-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k108-rsap-physical-split-positivity-owner-gate-review.md"
SOURCE = ROOT / "lab/sources/source-claim-register.yaml"
PHYSICAL = ROOT / "explorations/conditional-build/selected-k77-physical-diffeomorphism-split-2026-08-08.md"
K100 = ROOT / "lab/process/selected-k100-rsap-balanced-order-parameter-owner-census.json"
CURRENT = ROOT / "CURRENT-STATE.yaml"
NEXT = ROOT / "NEXT-STEPS.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
PRIME = 1_000_003


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero(n: int):
    return [[0] * n for _ in range(n)]


def basis_matrix(i: int, j: int, form: list[int]):
    value = zero(len(form))
    value[i][j] = 1
    value[j][i] = -form[i] * form[j]
    return value


def so_basis(form: list[int]):
    return [basis_matrix(i, j, form)
            for i in range(len(form)) for j in range(i + 1, len(form))]


def commutant_rows(generators, n: int):
    rows = []
    for generator in generators:
        for i in range(n):
            for j in range(n):
                row = {}
                for k in range(n):
                    if generator[i][k]:
                        key = k * n + j
                        row[key] = row.get(key, 0) + generator[i][k]
                    if generator[k][j]:
                        key = i * n + k
                        row[key] = row.get(key, 0) - generator[k][j]
                if any(row.values()):
                    rows.append(row)
    return rows


def modular_sparse_rank(rows):
    pivots = {}
    for source in rows:
        row = {key: value % PRIME for key, value in source.items() if value % PRIME}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                inverse = pow(row[pivot], PRIME - 2, PRIME)
                row = {key: (value * inverse) % PRIME
                       for key, value in row.items() if (value * inverse) % PRIME}
                pivots[pivot] = row
                break
            factor = row[pivot]
            for key, value in pivots[pivot].items():
                new = (row.get(key, 0) - factor * value) % PRIME
                if new:
                    row[key] = new
                elif key in row:
                    del row[key]
    return len(pivots)


def tensor_signature(left: tuple[int, int], right: tuple[int, int]):
    lp, ln = left
    rp, rn = right
    return lp * rp + ln * rn, lp * rn + ln * rp


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
k107_output = io.StringIO()
k107_code = None
with contextlib.redirect_stdout(k107_output):
    try:
        runpy.run_path(str(K107_PROBE), run_name="__main__")
    except SystemExit as error:
        k107_code = error.code
check("predecessor", "K107 phase-space certificate replays cleanly",
      k107_code == 0 and '"failures": []' in k107_output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. SOURCE AND OBJECT TYPING")
source_text = SOURCE.read_text(encoding="utf-8")
physical_text = PHYSICAL.read_text(encoding="utf-8")
check("source", "SC-CHI-03 records the physical carrier split", "id: SC-CHI-03" in source_text)
check("source", "the source register names TX(1,3) plus N(6,4)",
      "TX^{1,3} (+) N^{6,4}" in source_text)
check("source", "the physical-split artifact is only local kinematic naturality",
      "local kinematic naturality theorem" in physical_text)
check("owner", "the physical-split artifact does not claim selected-action Ward ownership",
      "not yet the nonlinear" in physical_text
      and "selected-action Ward theorem" in physical_text)


print("\nC. PHYSICAL STABILIZER AND CONDITIONAL QUOTIENT")
dim_so4 = 4 * 3 // 2
dim_so10 = 10 * 9 // 2
dim_h_phys = dim_so4 + dim_so10
dim_p_phys = 91 - dim_h_phys
check("dimension", "physical stabilizer dimension is 51", dim_h_phys == 51)
check("dimension", "physical isotropy dimension is 40", dim_p_phys == 40)
check("dimension", "conditional physical cotangent quotient is 80D",
      182 - 2 * dim_h_phys == 80 and 2 * dim_p_phys == 80)


print("\nD. EXACT INVARIANT-FORM CLASSIFICATION")
base_form = [1] + [-1] * 3
normal_form = [1] * 6 + [-1] * 4
base_rank = modular_sparse_rank(commutant_rows(so_basis(base_form), 4))
normal_rank = modular_sparse_rank(commutant_rows(so_basis(normal_form), 10))
check("commutant", "so(1,3) standard commutant rank is 15/16", base_rank == 15)
check("commutant", "so(6,4) standard commutant rank is 99/100", normal_rank == 99)
check("commutant", "both factor commutants are scalar",
      16 - base_rank == 1 and 100 - normal_rank == 1)
physical_signature = tensor_signature((1, 3), (6, 4))
check("signature", "physical isotropy tensor signature is exactly 18|22",
      physical_signature == (18, 22))
check("signature", "physical isotropy signature totals dimension 40",
      sum(physical_signature) == dim_p_phys)
check("positivity", "the unique invariant physical-isotropy form is indefinite",
      physical_signature[0] > 0 and physical_signature[1] > 0)
phase_signatures = {
    tensor_signature((2, 0), physical_signature),
    tensor_signature((0, 2), physical_signature),
}
check("phase", "compatible physical phase metrics have 36|44 up to sign",
      phase_signatures == {(36, 44), (44, 36)})
check("phase", "no compatible invariant physical phase metric is positive",
      (80, 0) not in phase_signatures and (0, 80) not in phase_signatures)
check("control", "neither source factor metric is positive",
      (1, 3)[0] and (1, 3)[1] and (6, 4)[0] and (6, 4)[1])


print("\nE. BALANCED COMPARISON")
k100 = load(K100)
check("balanced", "balanced stabilizer and orbit dimensions remain 42 and 49",
      k100["epsilon_dressing"]["kernel_dimension"] == 42
      and k100["epsilon_dressing"]["derivative_rank"] == 49)
check("balanced", "balanced cotangent quotient remains 98D", 182 - 2 * 42 == 98)
check("control", "physical and balanced involution multiplicities differ",
      (4, 10) != (7, 7))
check("control", "physical trace minus six differs from balanced trace zero",
      4 - 10 == -6 and 7 - 7 == 0)
check("control", "conjugation cannot turn the physical split into the balanced split",
      (4, 10, -6) != (7, 7, 0))


print("\nF. REGISTRY AND CLAIM CEILING")
registry = load(REGISTRY)
check("registry", "registry preserves source ownership only at kinematic split grade",
      registry["source_ownership"]["claim_id"] == "SC-CHI-03"
      and registry["source_ownership"]["kinematic_split_action_selected_as_boundary_reduction"] is False)
check("registry", "registry records 80D and 18|22 rather than 98D positivity",
      registry["physical_split"]["cotangent_reduction_dimension"] == 80
      and registry["physical_split"]["invariant_form_signature"] == [18, 22])
check("registry", "physical and balanced involutions are not conflated",
      registry["balanced_comparison"]["physical_and_balanced_involutions_conjugate"] is False)
check("ceiling", "the source observation construction itself is outside the negative verdict",
      "source_observation_construction_itself" in registry["claim_ceiling"]["does_not_bind"])
check("ceiling", "other concrete noninvariant selectors are not exhausted",
      registry["claim_ceiling"]["all_noninvariant_selectors_exhausted"] is False)
check("routing", "the result remains source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")
check("roadmap", "CURRENT and NEXT record K108 without attacking the observation split",
      "K108" in CURRENT.read_text(encoding="utf-8")
      and "K108" in NEXT.read_text(encoding="utf-8")
      and "Preserve the observation construction" in NEXT.read_text(encoding="utf-8"))
check("successor", "K107 records the physical-split successor closure",
      "Successor closure (K108)" in (ROOT / "explorations/conditional-build/selected-k107-rsap-phase-space-compatible-complex-positivity-2026-08-15.md").read_text(encoding="utf-8"))


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
