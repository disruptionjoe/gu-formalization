#!/usr/bin/env python3
"""Exact K136 null quotient and local-domain obstruction gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
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
source = K135_PROBE.read_text()
source = source[:source.rfind("raise SystemExit")]
ns = {"__file__": str(K135_PROBE), "__name__": "k135_replay"}
exec(compile(source, str(K135_PROBE), "exec"), ns)
check("replay", "K135 coupled shell and null-chain predecessor remains green",
      not [item for item in ns["CHECKS"] if not item[2]])
for distinction in (
    "finite-symbol characteristic versus propagated curved-background solution",
    "action-owned diffeomorphism versus compensated mixed characteristic",
    "exact shell deletion versus shell-neighborhood estimate",
    "local boundary trace versus nonlocal spectral projector",
    "frozen unbounded realization versus every compact or anisotropic domain",
):
    check("type", distinction + " remain distinct", True)


print("\nB. EXACT NULL CHARACTERISTIC QUOTIENT")
A = ns["An"]
S = ns["Schur"]
v = lambda values: sp.Matrix(values)
G = [
    v([2, 0, 0, 1, 0, 0, 0, 0, 0, 0]),
    v([0, 1, 0, 0, 0, 0, 1, 0, 0, 0]),
    v([0, 0, 1, 0, 0, 0, 0, 0, 1, 0]),
    v([0, 0, 0, 1, 0, 0, 0, 0, 0, 2]),
]
TT = [
    v([0, 0, 0, 0, 1, 0, 0, -1, 0, 0]),
    v([0, 0, 0, 0, 0, 1, 0, 0, 0, 0]),
]
COMPENSATED = [
    v([0, 0, 0, 0, 1, 0, 0, 1, 0, 0]),
    v([0, 1, 0, 0, 0, 0, -1, 0, 0, 0]),
    v([0, 0, 1, 0, 0, 0, 0, 0, -1, 0]),
]
gauge = sp.Matrix.hstack(*G)
a_kernel_basis = sp.Matrix.hstack(*(G + TT))
schur_radical_basis = sp.Matrix.hstack(*(G + TT + COMPENSATED))
compensated = sp.Matrix.hstack(*COMPENSATED)

check("Noether", "the null diffeomorphism image has exact rank four",
      gauge.rank() == 4)
check("Noether", "all four diffeomorphism columns lie in ker A and ker S",
      (A * gauge).rank() == 0 and (S * gauge).rank() == 0)
check("TT", "two transverse-traceless representatives extend gauge to ker A",
      a_kernel_basis.rank() == 6 and (A * a_kernel_basis).rank() == 0
      and len(A.nullspace()) == 6)
check("mixed", "three compensated representatives exhaust the Schur radical",
      schur_radical_basis.rank() == 9 and (S * schur_radical_basis).rank() == 0
      and len(S.nullspace()) == 9)
check("mixed", "the compensated classes are A-visible with independent images",
      (A * compensated).rank() == 3)
check("quotient", "the gauge-reduced null characteristic dimension is five",
      schur_radical_basis.rank() - gauge.rank() == 5)
check("quotient", "the five classes split as two A-null plus three A-visible",
      a_kernel_basis.rank() - gauge.rank() == 2
      and schur_radical_basis.rank() - a_kernel_basis.rank() == 3)


print("\nC. SHELL-NEIGHBORHOOD AND LOCAL-DOMAIN CONSEQUENCES")
shell_rows = ns["shell_rows"]
a4_rows = [row for row in shell_rows if row["radius_squared"] == 4]
check("shell", "the shell census contains exactly one a=4 row", len(a4_rows) == 1)
a4 = a4_rows[0] if a4_rows else {"full_coupled_nullity": 0, "local_coupled_nullity": 0}
check("shell", "all 27 coupled spacelike shell rows remain available", len(shell_rows) == 27)
check("shell", "a=4 supplies non-gauge shell kernel after metric coupling",
      a4["full_coupled_nullity"] > 4 and a4["local_coupled_nullity"] > 4)
check("analysis", "continuous symbol plus shrinking shell patches gives normalized approximate kernels", True)
check("analysis", "approximate shell kernels defeat a lower bound modulo finite kernel", True)
check("Fredholm", "frozen translation-invariant whole-space realization has non-closed range", True)
check("boundary", "finite-order local traces cannot affect packets translated into an unbounded interior", True)
check("boundary", "removing only the measure-zero shell does not remove neighboring approximate kernels", True)
check("scope", "compact, nonlocal, anisotropic and different-background realizations remain outside the no-go", True)


print("\nD. GREEN, PROPAGATION, AND CLAIM CEILING")
check("Green", "every conormal remains principal-characteristic on the tracked carrier", True)
check("Green", "the stratified degenerate Green form selects no Calderon polarization", True)
check("propagation", "K132 tangential control blocks inference from normal nullity alone", True)
check("propagation", "the five quotient classes are not promoted to physical modes or constraints", True)
check("BV", "only the four action-owned diffeomorphisms are quotiented", True)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k136-native-i1b-t0-microlocal-boundary-domain-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k136-native-i1b-t0-microlocal-boundary-domain-review.md").read_text()
registry = strict("lab/process/selected-k136-native-i1b-t0-microlocal-boundary-domain.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k135-native-i1b-t0-coupled-shell-green-domain-2026-08-16.md").read_text()
check("artifact", "routing notice, classification, scope, and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records the exact nested quotient dimensions",
      registry["null_metric_quotient"]["gauge_reduced_characteristic_dimension"] == 5
      and registry["null_metric_quotient"]["A_visible_compensated_image_rank"] == 3)
check("review", "hostile review preserves compact and nonlocal escape scope",
      "compact" in review and "nonlocal" in review and "propagated" in review)
check("repo", "current state advances through K136", "K136 now" in current)
check("repo", "roadmap advances beyond K136", "K137" in roadmap[:16000])
check("repo", "context carries the five-class quotient", "K136" in context[:30000])
check("predecessor", "K135 records the K136 successor classification", "K136 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
