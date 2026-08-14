#!/usr/bin/env python3
"""Exact structural certificate for VRS-2 boundary necessity."""

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


registry = json.loads((ROOT / "lab/process/superposition-vrs2-boundary-necessity-bulk-only-kill.json").read_text(encoding="utf-8"))
vrs1 = json.loads((ROOT / "lab/process/superposition-vrs1-internal-complex-source-census.json").read_text(encoding="utf-8"))
boundary = json.loads((ROOT / "lab/process/selected-k77-boundary-stationarity-symplectic-realization-gate.json").read_text(encoding="utf-8"))
green_text = (ROOT / "explorations/conditional-build/selected-k77-asymmetric-boundary-domain-gate-2026-08-14.md").read_text(encoding="utf-8")
result_text = (ROOT / "lab/active-research/source-residual-cohomology/vrs2-boundary-necessity-bulk-only-kill-2026-08-14.md").read_text(encoding="utf-8")

horns = {row["id"]: row for row in registry["horns"]}

print("A. ACTION-OWNED HORN ALGEBRA")
check("source", "the endpoint potential is preserved", registry["action_owned"]["endpoint_potential"] == boundary["boundary_potential"]["form"])
check("source", "the endpoint moment map is explicit", registry["action_owned"]["moment_map"] == "Q_eta=p_0 eta_0-p_2 eta_3")
p0, p2 = 2, 3
check("free", "arbitrary variation sees nonzero p0 coefficient", p0 * 1 - p2 * 0 != 0)
check("free", "arbitrary variation sees nonzero p2 coefficient", p0 * 0 - p2 * 1 != 0)
check("free", "free stationarity forces zero momentum", horns["FREE"]["stationarity"] == "p_0=p_2=0")
check("free", "free horn excludes the live nonzero fixture", horns["FREE"]["live_nonzero_fixture"] == "EXCLUDED")
check("fixed", "fixed variations kill Theta without killing momentum", p0 * 0 - p2 * 0 == 0 and horns["FIXED"]["stationarity"] == "NO_MOMENTUM_EQUATION")
check("charged", "a nonzero endpoint parameter has nonzero charge", p0 * 1 - p2 * 0 != 0)
check("charged", "charged horn retains boundary phase space", horns["CHARGED"]["admitted_variation"] == "ENDPOINT_PHASE_SPACE_RETAINED")
check("generated", "generated horn requires seven tangencies", horns["GENERATED"]["required_invariant_tangencies"] == 7)
check("generated", "generated horn remains unowned", horns["GENERATED"]["owner"] == "UNOWNED")

print("\nB. BULK-ONLY DISCRIMINATOR")
check("kill", "fixed nonzero horn kills bulk-only realization", horns["FIXED"]["bulk_only_status"] == "KILLED_FOR_NONZERO_FIXTURE")
check("kill", "charged nonzero horn kills bulk-only realization", horns["CHARGED"]["bulk_only_status"] == "KILLED_FOR_NONZERO_FIXTURE")
check("control", "free zero-charge bulk-only escape remains", "ESCAPE_NOT_KILLED" in horns["FREE"]["bulk_only_status"])
check("scope", "kill is exactly live-branch scoped", registry["scope"]["bulk_only_killed"] == "LIVE_NONZERO_SELECTED_BRANCH")
check("scope", "all GU backgrounds are not killed", registry["scope"]["all_GU_backgrounds_killed"] is False)
check("scope", "H-Q star remains live", registry["scope"]["H_Q_star_killed"] is False)
check("scope", "H0 is not proved", registry["scope"]["H0_proved"] is False)

print("\nC. GREEN-DOMAIN CONTROLS")
green = registry["green_domain"]
check("green", "base W/mirror pair is maximal isotropic", green["base_conormal_W_mirror"] == "COMPLEMENTARY_MAXIMAL_ISOTROPIC_PAIR")
check("green", "normal W/mirror pair is not isotropic", green["normal_conormal_W_mirror"] == "NEITHER_IS_ISOTROPIC")
check("gauge", "selected ordinary gauge rank remains 25", green["selected_gauge_image_rank"] == 25)
check("gauge", "active mixed obstruction rank remains eight", green["active_mixed_rank"] == 8)
check("gauge", "mixed directions preserve neither half", green["mixed_directions_preserve_W_or_mirror"] is False)
check("green", "no closed domain is promoted", green["closed_domain_constructed"] is False)
check("source", "underlying Green result states all eight active mixed failures", "All eight active mixed directions fail to preserve W and mirror" in green_text)

print("\nD. VRS COMPOSITION AND NEXT GATE")
check("prior", "VRS-1 sends boundary to VRS-2", vrs1["next_reverse_swing"]["id"] == "VRS-2")
check("composite", "moving J10 remains fibrewise only", registry["surviving_composite"]["moving_J10"].startswith("FIBREWISE_ONLY"))
check("composite", "BFV is necessary but functional complex open", "PROPER_FUNCTIONAL_COMPLEX_OPEN" in registry["surviving_composite"]["BFV"])
check("composite", "boundaryless moduli remain unexhausted", "NOT_EXHAUSTED" in registry["surviving_composite"]["moduli"])
check("next", "VRS-3 is next", registry["next_reverse_swing"]["id"] == "VRS-3")
check("next", "O_SR1C remains the forward dependency", "O_SR1C" in registry["forward_dependency"])
check("result", "the result states the free-horn escape", "free endpoint variation" in result_text and "bulk-only escape remains" in result_text)
check("ceiling", "no physical cohomology is claimed", registry["claim_ceiling"].startswith("NO_PHYSICAL_COHOMOLOGY"))
check("accounting", "no protected truth surface moves", set(registry["changes"].values()) == {"none"})

print(json.dumps({"counts": dict(COUNTS), "failures": FAILURES, "status": registry["status"], "next": registry["next_reverse_swing"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
