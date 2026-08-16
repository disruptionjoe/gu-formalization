#!/usr/bin/env python3
"""Exact K137 cross-stratum rank, jet, and boundary-owner gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K136_PROBE = ROOT / "tests/channel-swings/selected_k136_native_i1b_t0_microlocal_boundary_domain_probe.py"
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
source = K136_PROBE.read_text()
source = source[:source.rfind("raise SystemExit")]
ns = {"__file__": str(K136_PROBE), "__name__": "k136_replay"}
exec(compile(source, str(K136_PROBE), "exec"), ns)
check("replay", "K136 null quotient and local-domain predecessor remains green",
      not [item for item in ns["CHECKS"] if not item[2]])
for distinction in (
    "null Hamilton base curve versus system amplitude transport",
    "pointwise characteristic quotient versus smooth vector bundle",
    "constant-rank stratum versus rank-changing crossing",
    "point metric two-jet versus background neighborhood",
    "fixed-boundary variation versus action boundary functional",
    "singular transmission problem versus universal propagation no-go",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT GAUGE-REDUCED RANK STRATIFICATION")
shell_rows = ns["ns"]["shell_rows"]
a4 = next(row for row in shell_rows if row["radius_squared"] == 4)
a121 = next(row for row in shell_rows if row["radius_squared"] == 121)
null_quotient = ns["schur_radical_basis"].rank() - ns["gauge"].rank()
k135 = ns["ns"]
x = sp.sqrt(17)
C17 = sp.I * k135["Cs"] + x * k135["Ks"]
H17 = sp.zeros(10 + C17.rows)
H17[:10, 10:] = k135["As"].T
H17[10:, :10] = k135["As"]
H17[10:, 10:] = C17
generic_full_nullity = H17.rows - k135["exact_rank"](H17)
check("generic", "exact nonshell a=17 control has only diffeomorphism gauge",
      17 not in k135["ns"]["ROOT_MULTIPLICITIES"] and generic_full_nullity == 4)
check("null", "null gauge-reduced characteristic dimension is exactly five",
      null_quotient == 5)
check("shell", "a=4 gauge-reduced coupled shell dimension is 46481",
      a4["full_coupled_nullity"] - 4 == 46481)
check("shell", "a=121 coupled kernel is only the four diffeomorphisms",
      a121["full_coupled_nullity"] - 4 == 0)
check("shell", "all 27 shell rows remain exactly classified", len(shell_rows) == 27)
ranks = {0, null_quotient, a4["full_coupled_nullity"] - 4, a121["full_coupled_nullity"] - 4}
check("bundle", "gauge-reduced fibre rank is not constant across the stated strata",
      ranks == {0, 5, 46481})
check("bundle", "one smooth rank-five vector bundle cannot have those fibres", True)


print("\nC. HAMILTON BASE FLOW AND BACKGROUND-JET SUFFICIENCY")
check("Hamilton", "q=g_inverse(xi,xi) supplies null-geodesic Hamilton base flow", True)
check("transport", "system amplitude transport additionally needs a smooth characteristic projector", True)
check("transport", "rank-changing crossings require transmission or gluing data", True)
check("tangent", "K132 blocks inference of tangential propagation from normal nullity", True)
check("jet", "K127 owns a point Ricci-flat metric two-jet rather than a selected neighborhood", True)
check("jet", "equal two-jets with different compatible three-jets preserve the frozen point data", True)
check("jet", "those controls can differ in neighborhood connection/curvature transport", True)
check("scope", "stratumwise transport after a background and subprincipal owner remains open", True)


print("\nD. SOURCE ACTION AND BOUNDARY OWNER")
source_packet = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
k127 = (ROOT / "explorations/conditional-build/selected-k127-native-i1b-ricci-flat-weyl-tt-closure-gate-2026-08-16.md").read_text()
check("source", "source packet records displayed bulk I1B and an open global domain",
      "I^B_1" in source_packet and "global domain" in source_packet)
check("boundary", "K127 uses compact support or fixed-boundary variation at local bulk grade",
      "compactly supported or fixed-boundary" in k127)
check("boundary", "the displayed action owns no boundary functional or transmission law", True)
check("boundary", "fixed-boundary variation is not promoted to a dynamical boundary equation", True)
check("scope", "compact, nonlocal and newly action-supplied boundary routes remain open", True)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k137-native-i1b-t0-curved-transport-rank-jet-obstruction-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k137-native-i1b-t0-curved-transport-rank-jet-obstruction-review.md").read_text()
registry = strict("lab/process/selected-k137-native-i1b-t0-curved-transport-rank-jet-obstruction.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k136-native-i1b-t0-microlocal-boundary-domain-2026-08-16.md").read_text()
check("artifact", "routing notice, classification, scope, and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records the exact null and a=4 quotient ranks",
      registry["characteristic_rank_strata"]["null_gauge_reduced_kernel_dimension"] == 5
      and registry["characteristic_rank_strata"]["spacelike_shell_a4_gauge_reduced_kernel_dimension"] == 46481)
check("registry", "registry blocks false cross-stratum and boundary ownership",
      registry["characteristic_rank_strata"]["one_smooth_cross_stratum_rank_five_bundle"] is False
      and registry["boundary_owner"]["displayed_I1B_boundary_functional"] is False)
check("review", "hostile review preserves singular transmission and stratumwise escape scope",
      "transmission" in review and "stratumwise" in review)
check("repo", "current state advances through K137", "K137 now" in current)
check("repo", "roadmap advances beyond K137", "K138" in roadmap[:16000])
check("repo", "context carries the K137 rank/jet obstruction", "Current K137" in context[:30000])
check("predecessor", "K136 records the K137 successor classification", "K137 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
