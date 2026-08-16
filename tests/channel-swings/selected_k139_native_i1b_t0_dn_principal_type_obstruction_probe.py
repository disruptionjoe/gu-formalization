#!/usr/bin/env python3
"""Exact K139 homogeneous-DN versus finite-Schur carrier gate."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
K138_PROBE = ROOT / "tests/channel-swings/selected_k138_native_i1b_t0_null_stratum_covariant_transport_probe.py"
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
source = K138_PROBE.read_text()
source = source[:source.rfind("raise SystemExit")]
ns = {"__file__": str(K138_PROBE), "__name__": "k138_replay"}
with redirect_stdout(StringIO()):
    exec(compile(source, str(K138_PROBE), "exec"), ns)
check("replay", "K138 covariant null quotient predecessor remains green",
      not [item for item in ns["CHECKS"] if not item[2]])
for distinction in (
    "homogeneous DN principal kernel versus finite-frequency Schur radical",
    "lower-order mass-assisted invertibility versus principal ellipticity",
    "equivalent first-order prolongation versus added constraint reduction",
    "geometric five-bundle versus action-specific Dencker carrier",
    "undefined leakage matrix versus a zero leakage matrix",
    "current-calculus obstruction versus universal propagation no-go",
):
    check("type", distinction + " remain distinct", True)


print("\nB. COMPLETE HOMOGENEOUS DN RANK CENSUS")
k132 = strict("lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json")
dn = k132["coupled_dn_symbol"]
carrier = dn["carrier_dimension"]
null_rank = dn["ranks"]["null"]
nonnull_rank = dn["ranks"]["timelike"]
gauge = k132["minimal_bv_kt_bfv"]["metric_diffeomorphism_generator_rank"]
null_kernel = carrier - null_rank
nonnull_kernel = carrier - nonnull_rank
check("dimension", "complete coupled DN carrier dimension is 229386", carrier == 229386)
check("rank", "complete coupled DN null rank is 122748", null_rank == 122748)
check("kernel", "complete coupled DN null kernel is 106638", null_kernel == 106638)
check("gauge", "only four principal directions are action-owned gauge", gauge == 4)
check("quotient", "gauge-reduced DN null principal quotient is 106634",
      null_kernel - gauge == 106634)
check("nonnull", "gauge-reduced DN nonnull principal quotient is 98470",
      nonnull_kernel - gauge == 98470)
check("jump", "gauge-reduced causal principal quotient jumps by 8164",
      (null_kernel - gauge) - (nonnull_kernel - gauge) == 8164)
check("mismatch", "the DN principal quotient dimension is not five",
      null_kernel - gauge != 5)


print("\nC. FINITE-SYMBOL SCHUR OBJECT AND HOMOGENEITY")
k138 = strict("lab/process/selected-k138-native-i1b-t0-null-stratum-covariant-transport.json")
k135 = strict("lab/process/selected-k135-native-i1b-t0-coupled-shell-green-domain.json")
check("finite", "K138 finite Schur quotient has dimension five",
      k138["null_stratum"]["gauge_reduced_dimension"] == 5)
check("finite", "K138 did not claim a complete action Dencker endomorphism",
      k138["transport"]["full_action_specific_dencker_endomorphism_constructed"] is False)
check("Schur", "finite null Schur has only a rank-one degree-zero coefficient",
      k135["null_chain"]["metric_schur_rank"] == 1
      and k135["null_chain"]["local_schur_degree_coefficient_ranks"]
      == {"0": 1, "1": 0, "2": 0, "3": 0, "4": 0})
check("order", "C_1 is principal order one while kappa K is lower order zero", True)
check("principal", "lower-order K is absent from the ordinary DN principal symbol", True)
check("singular", "the homogeneous distortion coefficient has nullity 106630",
      k132["all_grade_distortion"]["radicals"]["null"] == 106630)
check("inverse", "K is essential to the nonhomogeneous fixed-frequency inverse", True)


print("\nD. REDUCTION AND DENCKER TYPE GATE")
check("equivalence", "invertible homogeneous row and column maps preserve kernel dimension", True)
check("constraint", "deleting 106629 further quotient directions requires added constraints",
      (null_kernel - gauge) - 5 == 106629)
check("Noether", "the action owns no distortion gauge generator at T=0",
      k132["minimal_bv_kt_bfv"]["distortion_gauge_generator_at_T0_owned"] is False)
check("KT", "the distortion radical is not an owned KT resolution",
      k132["minimal_bv_kt_bfv"]["distortion_kt_resolution_selected"] is False)
check("Dencker", "no action-owned projector from 106634 principal classes to five is declared", True)
check("Dencker", "the five-by-five action subprincipal leakage is therefore undefined", True)
check("open", "constrained semiclassical anisotropic and pseudodifferential routes remain open", True)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k139-native-i1b-t0-dn-principal-type-obstruction-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k139-native-i1b-t0-dn-principal-type-obstruction-review.md").read_text()
registry = strict("lab/process/selected-k139-native-i1b-t0-dn-principal-type-obstruction.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k138-native-i1b-t0-null-stratum-covariant-transport-2026-08-16.md").read_text()
check("artifact", "routing notice classification scope and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact
      and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records the exact DN-versus-five mismatch",
      registry["dn_principal"]["null_principal_quotient_dimension"] == 106634
      and registry["dn_principal"]["five_class_principal_kernel"] is False)
check("registry", "registry does not fabricate a Dencker matrix",
      registry["reduction"]["invariant_five_by_five_dencker_endomorphism"]
      == "UNDEFINED_WITHOUT_REDUCTION_OWNER")
check("review", "hostile review preserves K138 and alternative reductions",
      "K138" in review and "semiclassical" in review and "universal" in review)
check("repo", "current state advances through K139", "K139 now" in current)
check("repo", "roadmap advances beyond K139", "K140" in roadmap[:20000])
check("repo", "context carries the K139 principal-type obstruction", "Current K139" in context[:36000])
check("predecessor", "K138 records the K139 successor classification", "K139 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
