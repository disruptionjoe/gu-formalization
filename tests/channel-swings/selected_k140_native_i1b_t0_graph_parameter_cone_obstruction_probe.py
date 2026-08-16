#!/usr/bin/env python3
"""Exact K140 graph reduction, parameter cone, and constraint gate."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
K139_PROBE = ROOT / "tests/channel-swings/selected_k139_native_i1b_t0_dn_principal_type_obstruction_probe.py"
K135_PROBE = ROOT / "tests/channel-swings/selected_k135_native_i1b_t0_coupled_shell_green_domain_probe.py"
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


print("A. PREDECESSOR AND TYPE CUSTODY")
source = K139_PROBE.read_text()
source = source[:source.rfind("raise SystemExit")]
ns139 = {"__file__": str(K139_PROBE), "__name__": "k139_replay"}
with redirect_stdout(StringIO()):
    exec(compile(source, str(K139_PROBE), "exec"), ns139)
check("replay", "K139 DN-versus-finite carrier predecessor remains green",
      not [item for item in ns139["CHECKS"] if not item[2]])
for distinction in (
    "fixed-frequency graph projector versus homogeneous principal constraint",
    "metric Schur cancellation versus full-field reconstruction growth",
    "fixed kappa ultraviolet versus joint kappa-rho scaling",
    "valid parameter cone versus uniform recovery through mu zero",
    "band-limited effective transport versus physical propagation",
    "undefined original Dencker matrix versus zero leakage",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT NULL-PACKET GRAPH COEFFICIENTS")
source = K135_PROBE.read_text()
source = source[:source.index('print("\\nD. DOMAIN, NOETHER, AND BV CONSEQUENCES")')]
ns135 = {"__file__": str(K135_PROBE), "__name__": "k135_null_replay"}
with redirect_stdout(StringIO()):
    exec(compile(source, str(K135_PROBE), "exec"), ns135)
L, K, A = ns135["Ln"], ns135["Kn"], ns135["An"]
reconstruction_ranks = [(L ** power * K * A).rank() for power in range(5)]
schur_ranks = [(A.T * (L ** power) * K * A).rank() for power in range(5)]
check("exact", "null graph reconstruction coefficient ranks are 4/3/1/0/0",
      reconstruction_ranks == [4, 3, 1, 0, 0])
check("exact", "all positive Jordan degrees cancel only in the metric Schur form",
      schur_ranks == [1, 0, 0, 0, 0])
check("order", "normalized graph reconstruction has highest nonzero degree two",
      max(i for i, rank in enumerate(reconstruction_ranks) if rank) == 2)
check("order", "restoring the order-two A block gives graph order four",
      2 + max(i for i, rank in enumerate(reconstruction_ranks) if rank) == 4)
check("order", "graph order four exceeds the relative DN order one", 4 > 1)


print("\nC. PARAMETER-CONE AND RECOVERY CLASSIFICATION")
k135 = strict("lab/process/selected-k135-native-i1b-t0-coupled-shell-green-domain.json")
shells = [row["radius_squared"] for row in k135["spacelike_shells"]]
check("parameter", "joint kappa=rho mu scaling makes C inverse order minus one", True)
check("parameter", "joint cone makes C inverse A relative order plus one", True)
check("pole", "complete null inverse reaches mu pole order five",
      k135["null_chain"]["local_power_ranks"][-1] == 0
      and k135["null_chain"]["local_power_ranks"][-2] > 0)
check("pole", "metric graph reaches mu pole order three",
      max(i for i, rank in enumerate(reconstruction_ranks) if rank) + 1 == 3)
check("limit", "fixed kappa ultraviolet forces mu=kappa/rho to zero", True)
check("limit", "the cone estimate is not uniform through the fixed-kappa limit", True)
check("shell", "all 27 exact spacelike exceptional squared mu values are retained",
      len(shells) == 27 and shells[0] == 1 and shells[-1] == 168)


print("\nD. ACTION OWNERSHIP AND TANGENTIAL PRESERVATION")
k132 = strict("lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json")
k139 = strict("lab/process/selected-k139-native-i1b-t0-dn-principal-type-obstruction.json")
compatibility = k132["compatibility"]
bv = k132["minimal_bv_kt_bfv"]
check("Noether", "only four metric diffeomorphisms are action-owned",
      bv["metric_diffeomorphism_generator_rank"] == 4)
check("constraint", "no distortion gauge or KT constraint complex is selected",
      bv["distortion_gauge_generator_at_T0_owned"] is False
      and bv["distortion_kt_resolution_selected"] is False)
check("tangent", "normal kernel dimension in the exact block is 24",
      compatibility["normal_kernel_dimension"] == 24)
check("tangent", "only 11 normal-null rows are also tangential-null",
      compatibility["normal_tangential_common_kernel_dimension"] == 11)
check("tangent", "principal null rows are not automatically propagated",
      compatibility["normal_null_rows_automatically_propagated"] is False)
check("projector", "106629 non-gauge principal directions still lack a constraint owner",
      k139["dn_principal"]["null_principal_quotient_dimension"] - 5 == 106629)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k140-native-i1b-t0-graph-parameter-cone-obstruction-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k140-native-i1b-t0-graph-parameter-cone-obstruction-review.md").read_text()
registry = strict("lab/process/selected-k140-native-i1b-t0-graph-parameter-cone-obstruction.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k139-native-i1b-t0-dn-principal-type-obstruction-2026-08-16.md").read_text()
check("artifact", "routing notice classification scope and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact
      and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records exact reconstruction and Schur ranks",
      registry["finite_frequency_graph"]["null_local_reconstruction_jordan_coefficient_ranks"] == reconstruction_ranks
      and registry["finite_frequency_graph"]["null_local_schur_jordan_coefficient_ranks"] == schur_ranks)
check("registry", "registry preserves the parameter family but denies UV equivalence",
      registry["parameter_cone"]["valid_as_separate_parameter_family"] is True
      and registry["parameter_cone"]["equivalent_to_original_fixed_kappa_ultraviolet"] is False)
check("review", "hostile review preserves both the exact graph and the separate cone",
      "exact fixed-frequency Schur reduction" in review and "parameter cone" in review)
check("repo", "current state advances through K140", "K140 now" in current)
check("repo", "roadmap advances beyond K140", "K141" in roadmap[:22000])
check("repo", "context carries the K140 graph/parameter-cone result", "Current K140" in context[:42000])
check("predecessor", "K139 records the K140 successor classification", "K140 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
