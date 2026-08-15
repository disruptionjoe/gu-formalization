#!/usr/bin/env python3
"""Exact K105 curvature-sign construction and stationary-owner qualification."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K104_PROBE = ROOT / "tests/channel-swings/selected_k104_rsap_source_boundary_variational_owner_census_probe.py"
SR1H_PROBE = ROOT / "tests/channel-swings/selected_k77_sr1h_action_owned_point_carrier_census_probe.py"
REGISTRY = ROOT / "lab/process/selected-k105-rsap-curvature-sign-owner-qualification.json"
SR1H = ROOT / "lab/process/selected-k77-sr1h-action-owned-point-carrier-census.json"
RESULT = ROOT / "explorations/conditional-build/selected-k105-rsap-curvature-sign-owner-qualification-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k105-rsap-curvature-sign-owner-qualification-review.md"
CURRENT = ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md"
NEXT = ROOT / "NEXT-STEPS.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q = [1] * 7 + [-1] * 7


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def diagonal(values: list[int]) -> list[list[Fraction]]:
    return [[Fraction(values[i] if i == j else 0) for j in range(N)] for i in range(N)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def signature(indices: set[int]) -> tuple[int, int]:
    return (sum(Q[index] == 1 for index in indices),
            sum(Q[index] == -1 for index in indices))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def scalar_sign(value: Fraction) -> int:
    if value == 0:
        raise ValueError("spectral sign is undefined at the gap closure")
    return 1 if value > 0 else -1


print("A. PREDECESSORS AND DURABLE FILES")
k104_output = io.StringIO()
k104_code = None
with contextlib.redirect_stdout(k104_output):
    try:
        runpy.run_path(str(K104_PROBE), run_name="__main__")
    except SystemExit as error:
        k104_code = error.code
check("predecessor", "K104 boundary-owner certificate replays cleanly",
      k104_code == 0 and '"failures": []' in k104_output.getvalue())
sr1h_output = io.StringIO()
with contextlib.redirect_stdout(sr1h_output):
    runpy.run_path(str(SR1H_PROBE), run_name="__main__")
check("predecessor", "SR-1H action-owned point-carrier census replays 48/48",
      "PASS 48/48" in sr1h_output.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. EXACT ALGEBRAIC CURVATURE WITNESS")
plus = {0, 1, 2, 7, 8, 9, 10}
r_signs = [1 if i in plus else -1 for i in range(N)]
R0 = diagonal(r_signs)
QMAT = diagonal(Q)
r = matmul(QMAT, R0)
check("tensor", "Ricci bilinear r=Q R0 is symmetric", r == transpose(r))
check("tensor", "r is Q-tracefree", trace(R0) == 0)


def rm(i: int, j: int, k: int, l: int) -> Fraction:
    return (r[i][k] * QMAT[j][l] + r[j][l] * QMAT[i][k]
            - r[i][l] * QMAT[j][k] - r[j][k] * QMAT[i][l]) / (N - 2)


anti_first = True
anti_second = True
pair_exchange = True
bianchi = True
for i in range(N):
    for j in range(N):
        for k in range(N):
            for l in range(N):
                value = rm(i, j, k, l)
                anti_first &= value == -rm(j, i, k, l)
                anti_second &= value == -rm(i, j, l, k)
                pair_exchange &= value == rm(k, l, i, j)
                bianchi &= value + rm(j, k, i, l) + rm(k, i, j, l) == 0
check("tensor", "Rm is antisymmetric in its first pair", anti_first)
check("tensor", "Rm is antisymmetric in its second pair", anti_second)
check("tensor", "Rm has pair-exchange symmetry", pair_exchange)
check("tensor", "Rm obeys the first Bianchi identity", bianchi)
ricci = [[sum(Fraction(Q[i] if i == k else 0) * rm(i, j, k, l)
              for i in range(N) for k in range(N))
          for l in range(N)] for j in range(N)]
check("contraction", "exact Q contraction of Rm returns r", ricci == r)
S = matmul(QMAT, ricci)
check("contraction", "the Ricci endomorphism is S=R0", S == R0)
check("sign", "S is an exact trace-zero involution", matmul(S, S) == diagonal([1] * N) and trace(S) == 0)
check("sign", "S has seven positive and seven negative eigenvalues",
      r_signs.count(1) == 7 and r_signs.count(-1) == 7)
minus = set(range(N)) - plus
check("orbit", "the eigenspaces have balanced real signatures",
      signature(plus) == (3, 4) and signature(minus) == (4, 3))
check("sign", "the spectral gap is one and sign(S)=R0", min(abs(x) for x in r_signs) == 1 and S == R0)


print("\nC. REAL-ORBIT AND ZERO-GAP CONTROLS")
wrong_plus = set(range(7))
wrong_signs = [1 if i in wrong_plus else -1 for i in range(N)]
check("control", "the wrong real orbit has the same seven-plus-seven spectrum",
      sorted(wrong_signs) == sorted(r_signs))
check("control", "the wrong orbit has signature (7,0)|(0,7)",
      signature(wrong_plus) == (7, 0)
      and signature(set(range(N)) - wrong_plus) == (0, 7))
check("control", "spectrum alone therefore does not select the balanced real orbit",
      sorted(wrong_signs) == sorted(r_signs)
      and signature(wrong_plus) != signature(plus))
zero_sign_undefined = False
try:
    scalar_sign(Fraction(0))
except ValueError:
    zero_sign_undefined = True
check("zero", "spectral sign is undefined at zero curvature", zero_sign_undefined)
check("zero", "scalar involutions have trace plus or minus fourteen, never zero",
      {trace(diagonal([1] * N)), trace(diagonal([-1] * N))} == {14, -14})
check("zero", "a delta regularization is not involutive at the zero eigenvalue",
      Fraction(0, 1) ** 2 != 1)


print("\nD. NATURALITY CONTROL")
permutation = list(range(N))
permutation[0], permutation[3] = permutation[3], permutation[0]
G = [[Fraction(int(permutation[j] == i)) for j in range(N)] for i in range(N)]
GT = transpose(G)
check("naturality", "the planted permutation preserves Q", matmul(matmul(GT, QMAT), G) == QMAT)
S_moved = matmul(matmul(G, S), GT)
R_moved = matmul(matmul(G, R0), GT)
check("naturality", "curvature endomorphism transforms by conjugation", S_moved == R_moved)
check("naturality", "spectral sign commutes with the exact conjugation fixture",
      matmul(S_moved, S_moved) == diagonal([1] * N)
      and S_moved == R_moved)


print("\nE. CURRENT ACTION-STATIONARY OWNER CENSUS")
sr1h = read_json(SR1H)
rows = {row["id"]: row for row in sr1h["census"]}
check("census", "the current census has exactly five serialized classes", len(rows) == 5)
check("census", "the census covers seven current instances",
      sr1h["coverage"]["serialized_candidate_instances"] == 7)
check("census", "no current class survives full local stationarity",
      sr1h["coverage"]["full_local_stationarity_survivors"] == 0)
check("census", "there are zero eligible VRS-5 backgrounds",
      sr1h["coverage"]["eligible_vrs5_backgrounds"] == 0)
check("census", "the canonical zero-T class is killed by the action two-jet",
      rows["CANONICAL_ZORRO_ZERO_T"]["disposition"] == "KILLED_ACTION_TWO_JET")
check("census", "the scalar-curvature class remains ineligible rather than killed universally",
      rows["SCALAR_CURVATURE_VEV_TRACE_BRANCH"]["disposition"] == "INELIGIBLE_CANONICAL_REALISATION_OPEN")
check("ceiling", "unconstructed future classes are not counted as current",
      sr1h["coverage"]["unconstructed_future_classes_counted_as_current"] == 0)
check("ceiling", "rival Zorro and nonzero-fermion reopeners remain explicit",
      "DERIVED_RIVAL_ZORRO_CONNECTION_AND_METRIC" in sr1h["unconstructed_reopeners"]
      and "NONZERO_FERMION_COUPLED_STATIONARY_SADDLE" in sr1h["unconstructed_reopeners"])


print("\nF. REGISTRY, CLAIM CEILING AND ROADMAP")
registry = read_json(REGISTRY)
check("registry", "registry records the exact conditional curvature-sign map",
      registry["conditional_construction"]["formula"] == "R_S=S_TIMES_SQUARED_INVERSE_SQUARE_ROOT")
check("registry", "registry requires the balanced eigenspace real signatures",
      "3_4" in registry["conditional_construction"]["balanced_real_type_requirement"])
check("registry", "registry records zero current stationary carriers",
      registry["current_stationary_carrier_census"]["eligible_vrs5_backgrounds"] == 0)
check("owner", "the construction is exact while its stationary input is missing",
      registry["owner_disposition"]["conditional_curvature_sign_map"] == "CONSTRUCTED"
      and registry["owner_disposition"]["current_action_stationary_input"] == "MISSING")
check("ceiling", "the result does not claim all backgrounds exhausted",
      registry["claim_ceiling"]["all_possible_action_backgrounds_exhausted"] is False)
check("ceiling", "zero charge is not confused with zero curvature",
      registry["claim_ceiling"]["zero_charge_forces_zero_curvature"] is False)
check("routing", "the result stays source-native and changes no ledger",
      registry["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and registry["disposition"]["ledger_change"] == "none")
current_text = CURRENT.read_text(encoding="utf-8")
next_text = NEXT.read_text(encoding="utf-8")
check("roadmap", "CURRENT and NEXT park repeated owner searches pending a new background",
      "K105" in current_text and "K105" in next_text
      and "genuinely new" in next_text)


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
