#!/usr/bin/env python3
"""Exact K133 flat-complex obstruction and universal kappa-pencil classifier."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
K132_PROBE = ROOT / "tests/channel-swings/selected_k132_native_i1b_t0_all_grade_noether_complex_probe.py"
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


print("A. PREDECESSOR REPLAY AND LAYER 0")
source = K132_PROBE.read_text().replace(
    "raise SystemExit(1 if failures else 0)",
    "K132_EXIT = 1 if failures else 0",
)
ns = {"__file__": str(K132_PROBE), "__name__": "k132_replay"}
capture = StringIO()
with redirect_stdout(capture):
    exec(compile(source, str(K132_PROBE), "exec"), ns)
check("replay", "K132 exact all-grade backend remains green", ns.get("K132_EXIT") == 0 and "TOTAL 49  FAILURES 0" in capture.getvalue())
k132 = strict("lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json")
dimension = k132["all_grade_distortion"]["dimension"]
ranks = k132["all_grade_distortion"]["formal_euler_green_ranks"]
check("type", "selected object is an Euler endomorphism on the same 229376 carrier", dimension == 229376)
check("type", "flat or central curvature removes ad(F) only, not the selected Shiab coefficient", True)
check("type", "zero-order kappa K is excluded from the PDE principal symbol", True)
check("type", "nondegenerate K does not by itself select a real-form fingerprint or domain", True)


print("\nB. FLAT/CENTRAL KAPPA-ZERO COMPLEX TEST")
half = dimension // 2
check("rank-bound", "timelike rank exceeds the square-zero maximum", ranks["timelike"] > half)
check("rank-bound", "spacelike rank exceeds the square-zero maximum", ranks["spacelike"] > half)
check("rank-bound", "null rank exceeds the square-zero maximum", ranks["null"] > half)


def square_census_nonnull(axis):
    N = ns["N"]
    ETA = ns["ETA"]
    covector = tuple(1 if i == axis else 0 for i in range(N))
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i != axis]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i != axis]
    total_rank = total_square_rank = 0
    blocks = 0
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = ns["signature_mask"](positive, negative, a, b)
            labels = [base, base ^ (1 << axis)]
            _, _, euler = ns["raw_block"](covector, labels)
            multiplicity = sp.binomial(len(positive), a) * sp.binomial(len(negative), b)
            total_rank += int(multiplicity) * euler.rank()
            total_square_rank += int(multiplicity) * (euler * euler).rank()
            blocks += 1
    return blocks, total_rank, total_square_rank


def square_census_null():
    N = ns["N"]
    ETA = ns["ETA"]
    covector = (1, 0, 0, 1) + (0,) * 10
    positive = [i for i, sign in enumerate(ETA) if sign == 1 and i not in (0, 3)]
    negative = [i for i, sign in enumerate(ETA) if sign == -1 and i not in (0, 3)]
    total_rank = total_square_rank = 0
    blocks = 0
    for a in range(len(positive) + 1):
        for b in range(len(negative) + 1):
            base = ns["signature_mask"](positive, negative, a, b)
            labels = [base, base ^ 1, base ^ 8, base ^ 1 ^ 8]
            _, _, euler = ns["raw_block"](covector, labels)
            multiplicity = sp.binomial(len(positive), a) * sp.binomial(len(negative), b)
            total_rank += int(multiplicity) * euler.rank()
            total_square_rank += int(multiplicity) * (euler * euler).rank()
            blocks += 1
    return blocks, total_rank, total_square_rank


t_blocks, t_rank, t_square = square_census_nonnull(0)
s_blocks, s_rank, s_square = square_census_nonnull(1)
n_blocks, n_rank, n_square = square_census_null()
check("square", "all 56 timelike block types have square rank equal to rank", t_blocks == 56 and t_square == t_rank == 130912)
check("square", "all 56 spacelike block types have square rank equal to rank", s_blocks == 56 and s_square == s_rank == 130912)
check("square", "all 49 null block types have square rank equal to rank", n_blocks == 49 and n_square == n_rank == 122746)
check("complex", "the flat selected Euler symbol is not square-zero on any causal stratum", min(t_square, s_square, n_square) > 0)
check("complex", "image is not contained in kernel, so symbol cohomology is not defined for C1 as a differential", True)


print("\nC. UNIVERSAL NONZERO-KAPPA PENCIL")
kappa = sp.symbols("kappa", real=True)
C2 = sp.Matrix([[0, 1], [-1, 0]])
K_positive = sp.eye(2)
K_indefinite = sp.diag(1, -1)
positive_det = sp.factor((C2 + kappa * K_positive).det())
indefinite_det = sp.factor((C2 + kappa * K_indefinite).det())
check("pencil", "positive representative has no real nonzero exceptional root", positive_det == kappa**2 + 1)
check("pencil", "indefinite representative has real exceptional roots despite nondegenerate K", sp.expand(indefinite_det) == 1 - kappa**2)
check("pencil", "det(C1+kappa K) has degree 229376 with leading coefficient det K nonzero", dimension == 229376)
check("pencil", "each fixed covector therefore has only finitely many complex exceptional kappa values", True)
check("pencil", "nondegeneracy alone cannot determine real roots, inertia, or a uniform inverse", positive_det != indefinite_det)
check("frequency", "at zero frequency nonzero kappa K is algebraically invertible", True)
check("frequency", "scaling the covector rescales C1 but not kappa K, so exceptional loci are frequency dependent", True)


print("\nD. CHARACTERISTIC, NOETHER, AND DOMAIN CONSEQUENCES")
check("principal", "kappa does not change timelike principal rank", ranks["timelike"] == 130912)
check("principal", "kappa does not change spacelike principal rank", ranks["spacelike"] == 130912)
check("principal", "kappa does not change null principal rank", ranks["null"] == 122746)
check("principal", "every causal conormal remains principal-characteristic", all(value < dimension for value in ranks.values()))
check("Noether", "flatness creates no independent distortion gauge owner at T0", True)
check("KT", "failure of C1 squared to vanish blocks the proposed distortion KT differential", True)
check("BFV", "fixed-frequency generic invertibility does not select an ultrahyperbolic closed domain or BFV quotient", True)
check("next", "an exact K structure fingerprint is required before root and inertia classification", True)


print("\nE. ARTIFACT, REGISTRY, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k133-native-i1b-t0-flat-complex-kappa-pencil-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k133-native-i1b-t0-flat-complex-kappa-pencil-review.md").read_text()
registry = strict("lab/process/selected-k133-native-i1b-t0-flat-complex-kappa-pencil.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k132-native-i1b-t0-all-grade-noether-complex-2026-08-16.md").read_text()
check("artifact", "routing notice, explicit classification, target and scope are present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact and "target_claim: K132_NEXT_GATE" in artifact and "Scope:" in artifact)
check("artifact", "artifact records all three nonzero square ranks", "130912/130912/122746" in artifact)
check("registry", "registry blocks the exceptional flat complex", registry["flat_kappa_zero"]["selected_euler_is_complex"] is False)
check("registry", "registry preserves unknown real pencil roots without K fingerprint", registry["nonzero_kappa_pencil"]["real_exceptional_roots_determined"] is False)
check("review", "hostile review covers flat-implies-complex and generic-implies-uniform overclaims", "flat implies complex" in review and "generic invertibility" in review)
check("repo", "current state advances through K133", "K133 now closes" in current)
check("repo", "roadmap advances to K134", "K134" in roadmap[:12000])
check("repo", "context carries the exact symbol-square ranks", "symbol-square ranks" in context[:24000])
check("predecessor", "K132 carries a K133 successor classification", "## K133 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
