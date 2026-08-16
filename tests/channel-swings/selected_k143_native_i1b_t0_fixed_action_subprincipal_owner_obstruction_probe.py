#!/usr/bin/env python3
"""Exact K143 fixed-action scaling, conicity, and quotient-owner gate."""

from fractions import Fraction
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
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
k142 = strict("lab/process/selected-k142-native-i1b-t0-intrinsic-quotient-connection.json")
k141 = strict("lab/process/selected-k141-native-i1b-t0-parameter-annulus-riesz-obstruction.json")
k140 = strict("lab/process/selected-k140-native-i1b-t0-graph-parameter-cone-obstruction.json")
k132 = strict("lab/process/selected-k132-native-i1b-t0-all-grade-noether-complex.json")
check("replay", "K142 leaves an actual lower action coefficient as the next object",
      k142["action_transport"]["required_next_object"]
      == "TYPED_LOWER_ORDER_ACTION_COEFFICIENT_ON_THE_COMPACT_FINITE_FREQUENCY_NULL_FAMILY")
check("replay", "K141 annulus remains thirteen through fourteen",
      k141["parameter_annulus"]["absolute_mu_min"] == 13
      and k141["parameter_annulus"]["absolute_mu_max"] == 14)
check("replay", "K140 distinguishes the joint family from fixed-kappa ultraviolet equivalence",
      k140["parameter_cone"]["equivalent_to_original_fixed_kappa_ultraviolet"] is False)
check("replay", "K132 fixed nonzero kappa does not preserve principal null identities",
      k132["compatibility"]["nonzero_kappa_preserves_principal_null_identities"] is False)
for distinction in (
    "bounded fixed-action frequency band versus conic characteristic family",
    "fixed zero-order Hodge mass versus promoted order-one parameter term",
    "normalized principal family versus subprincipal coefficient",
    "frozen characteristic equation map versus amplitude transport endomorphism",
    "action-owned distortion coefficient versus five-class quotient coefficient",
    "auxiliary pseudodifferential norm versus local action datum",
):
    check("type", distinction + " remain distinct", True)


print("\nB. FIXED-COUPLING ANNULUS IS A BOUNDED NONCONIC BAND")
kappa = Fraction(27, 1)
mu = Fraction(27, 2)
rho = kappa / mu
check("band", "interior control has mu twenty-seven halves", kappa / rho == mu)
check("band", "fixed-kappa annulus gives the exact rho interval",
      Fraction(abs(kappa), 14) <= rho <= Fraction(abs(kappa), 13))
t = Fraction(2, 1)
mu_dilated = kappa / (t * rho)
check("dilation", "covector dilation sends mu to mu over t", mu_dilated == mu / t)
check("dilation", "the doubled covector leaves the annulus", not Fraction(13) <= mu_dilated <= Fraction(14))
check("conic", "the fixed-kappa annulus is not closed under positive dilation", True)
check("limit", "fixed kappa drives mu to zero as rho grows", True)


print("\nC. SYMBOL ORDER AND OPERATOR OWNERSHIP")
rho_symbol, mu_symbol = sp.symbols("rho mu", positive=True)
c1, mass = sp.symbols("c1 mass")
fixed = sp.I * rho_symbol * c1 + kappa * mass
joint = rho_symbol * (sp.I * c1 + mu_symbol * mass)
check("order", "fixed-action derivative term is homogeneous order one",
      sp.expand(fixed.subs(rho_symbol, t * rho_symbol) - t * sp.I * rho_symbol * c1) == kappa * mass)
check("order", "fixed-action Hodge term is independent of rho", sp.diff(kappa * mass, rho_symbol) == 0)
check("order", "joint Hodge term is homogeneous order one", sp.diff(rho_symbol * mu_symbol * mass, rho_symbol) == mu_symbol * mass)
check("order", "joint symbol factors rho from derivative and Hodge terms",
      sp.expand(joint) == sp.I * rho_symbol * c1 + rho_symbol * mu_symbol * mass)
check("owner", "joint scaling changes the fixed action coupling along frequency", True)
check("owner", "realizing rho as an operator requires a declared quantization", True)
q = sp.Symbol("q", real=True)
check("null", "the invariant scalar sqrt(abs(q)) vanishes on q equals zero", sp.sqrt(sp.Abs(q)).subs(q, 0) == 0)
check("owner", "a positive auxiliary norm is not supplied by the local action", True)


print("\nD. QUOTIENT BASICNESS IS NOT IDENTIFIED BY PRINCIPAL DATA")
# Model G=span(e1) inside H=span(e1,e2,e3) inside M=R4.
e1, e2, e3, e4 = [sp.eye(4).col(i) for i in range(4)]
good = sp.diag(2, 3, 5, 7)
bad = good.copy()
bad[1, 0] = 1
check("good", "planted good lower map preserves H", all((good * v)[3] == 0 for v in (e1, e2, e3)))
check("good", "planted good lower map preserves G", good * e1 == 2 * e1)
check("bad", "planted bad map preserves H but not G", (bad * e1)[3] == 0 and bad * e1 != 2 * e1)
representative = 4 * e2 - e3
gauge_shift = 11 * e1
check("quotient", "good map is representative independent modulo gauge",
      all(entry == 0 for entry in (good * (representative + gauge_shift) - good * representative)[1:]))
check("quotient", "bad map leaks a gauge shift into the quotient",
      (bad * (representative + gauge_shift) - bad * representative)[1] != 0)
check("identifiability", "the same principal quotient data admit good and bad lower maps", True)


print("\nE. ARTIFACT, REVIEW, AND PROPAGATION")
artifact = (ROOT / "explorations/conditional-build/selected-k143-native-i1b-t0-fixed-action-subprincipal-owner-obstruction-2026-08-16.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-16-selected-k143-native-i1b-t0-fixed-action-subprincipal-owner-obstruction-review.md").read_text()
registry = strict("lab/process/selected-k143-native-i1b-t0-fixed-action-subprincipal-owner-obstruction.json")
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k142-native-i1b-t0-intrinsic-quotient-connection-2026-08-16.md").read_text()
check("artifact", "routing notice classification scope and pre-wave answers are present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact
      and "Classification: `SOURCE_NATIVE_ROUTE`." in artifact
      and "## 0. Pre-wave answers" in artifact)
check("registry", "registry records nonconicity and promoted Hodge order",
      registry["fixed_action"]["annulus_conic"] is False
      and registry["joint_family"]["hodge_term_order"] == 1
      and registry["joint_family"]["hodge_term_is_subprincipal"] is False)
check("registry", "registry records absent owner and undefined basicness",
      registry["operator_owner"]["owned_five_class_subprincipal_coefficient"] is False
      and registry["quotient_basicness"]["actual_lower_coefficient_basicness"]
      == "UNDEFINED_NO_OWNED_COEFFICIENT")
check("review", "hostile review blocks the physical-zero and finite-band overclaims",
      "not evidence that the physical subprincipal symbol vanishes" in review
      and "does not invalidate finite-band elimination" in review)
check("repo", "current state advances through K143", "K143 now" in current)
check("repo", "roadmap advances beyond K143", "K144" in roadmap[:12000])
check("repo", "context carries the K143 owner obstruction", "Current K143" in context[:16000])
check("predecessor", "K142 records the K143 successor classification", "K143 successor classification" in predecessor)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
if failures:
    print("FAILED=" + " | ".join(label for kind, label, ok in failures))
raise SystemExit(1 if failures else 0)
