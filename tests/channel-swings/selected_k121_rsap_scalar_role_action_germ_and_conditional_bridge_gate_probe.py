#!/usr/bin/env python3
"""Exact K121 scalar role, action-germ, and conditional-bridge gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


# Exact scalar restrictions and their stationary germs.
theta, t, x = sp.symbols("theta t x")
a, beta, kappa, rho, R, kappa1 = sp.symbols(
    "a beta kappa rho R kappa_1", nonzero=True
)
lam, mu, q = sp.symbols("lambda mu q", nonzero=True)

W_sc = beta*R*theta + kappa*theta**2/2 - rho
W_1b = 1456*t**3 + 7*kappa1*t**2
theta_star = -beta*R/kappa
t_star = -kappa1/312

check("stationary", "scalar horn stationary point is minus beta R over kappa",
      sp.diff(W_sc, theta).subs(theta, theta_star) == 0)
check("stationary", "native nonzero radial point is stationary",
      sp.factor(sp.diff(W_1b, t)) == 14*t*(312*t+kappa1)
      and sp.diff(W_1b, t).subs(t, t_star) == 0)
check("germ", "scalar horn Hessian is kappa",
      sp.diff(W_sc, theta, 2).subs(theta, theta_star) == kappa)
check("germ", "scalar horn pure third derivative vanishes",
      sp.diff(W_sc, theta, 3) == 0)
check("germ", "native radial Hessian is minus fourteen kappa one",
      sp.simplify(sp.diff(W_1b, t, 2).subs(t, t_star)) == -14*kappa1)
check("germ", "native radial third derivative is 8736",
      sp.diff(W_1b, t, 3) == 8736)

# No nonzero affine bridge, even with an overall action rescaling, can equate
# the stationary action germs.
native_affine = sp.expand(mu*W_1b.subs(t, t_star+lam*x))
observed_centered = sp.expand(W_sc.subs(theta, theta_star+x))
affine_d2 = sp.diff(native_affine, x, 2).subs(x, 0)
affine_d3 = sp.diff(native_affine, x, 3).subs(x, 0)
check("affine", "pulled native Hessian has the expected scaled value",
      sp.simplify(affine_d2) == -14*mu*kappa1*lam**2)
check("affine", "pulled native cubic stays nonzero symbolically",
      affine_d3 == 8736*mu*lam**3)
check("affine", "observed centered cubic is zero",
      sp.diff(observed_centered, x, 3) == 0)
check("affine", "strict affine action-germ equality is impossible for nonzero scale and slope",
      sp.simplify(affine_d3/(mu*lam**3)) == 8736)
check("pairing", "quadratic equality is only the conditional cross-action equation",
      sp.solve(sp.Eq(affine_d2, kappa), lam**2) == [-kappa/(14*kappa1*mu)])
check("pairing", "quadratic equality is blind to scalar orientation",
      affine_d2.subs(lam, -lam) == affine_d2)

# The two stationary families cannot choose a universal origin-preserving
# scalar normalization.
R_star = 2*rho/a
theta_family = sp.simplify(theta_star.subs(R, R_star))
lambda_bg = sp.simplify(t_star/theta_family)
check("background", "observed constant-field scalar tracks rho",
      theta_family == -2*beta*rho/(a*kappa))
check("background", "point-matching slope is inverse in rho",
      lambda_bg == a*kappa*kappa1/(624*beta*rho))
check("background", "point-matching slope is not universal in rho",
      sp.diff(lambda_bg, rho) != 0)
check("background", "background-centered affine point matching leaves lambda free",
      sp.simplify((t_star+lam*((theta_family+x)-theta_family)).subs(x, 0)-t_star) == 0)

# A nonlinear map can cancel the native cubic, but only by adding a precise
# new scalar second jet that is not part of K120's affine scalar bridge.
t_nonlinear = t_star + lam*x + q*x**2/2
native_nonlinear = sp.expand(W_1b.subs(t, t_nonlinear))
nonlinear_d3 = sp.factor(sp.diff(native_nonlinear, x, 3).subs(x, 0))
q_cancel = 208*lam**2/kappa1
check("nonlinear", "composite cubic contains Hessian times scalar second jet",
      sp.expand(nonlinear_d3) == -42*kappa1*lam*q + 8736*lam**3)
check("nonlinear", "unique scalar second jet cancels the native cubic",
      sp.simplify(nonlinear_d3.subs(q, q_cancel)) == 0)
check("nonlinear", "cancelling second jet is nonzero for an invertible bridge",
      sp.simplify(q_cancel/(lam**2/kappa1)) == 208)

# Source, action custody, and repository routing.
source = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text()
horn = (ROOT / "explorations/conditional-build/selected-branch-bv-tt-and-curvature-vev-flrw-2026-08-05.md").read_text()
native = (ROOT / "explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md").read_text()
intrinsic = (ROOT / "explorations/conditional-build/selected-cubic-augmented-torsion-d3-owner-decomposition-2026-08-06.md").read_text()
k119 = (ROOT / "explorations/conditional-build/selected-k119-rsap-tt-stationary-twojet-selection-obstruction-2026-08-15.md").read_text()
k120 = (ROOT / "explorations/conditional-build/selected-k120-rsap-tt-geometric-twojet-custody-and-scalar-bridge-gate-2026-08-15.md").read_text()
artifact = (ROOT / "explorations/conditional-build/selected-k121-rsap-scalar-role-action-germ-and-conditional-bridge-gate-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k121-rsap-scalar-role-action-germ-and-conditional-bridge-gate.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("source", "source explicitly changes the dark-energy carrier to parameterized torsion",
      "new dark energy candidate from metrics to parameterized torsion" in source)
check("source", "source theta is a connection difference rather than a scalar coefficient",
      "theta, which is given by pi minus epsilon inverse b epsilon" in source)
check("source", "source calls the replacement a field rather than a constant",
      "It's a field" in source)
check("custody", "I_sc is described as a minimal scalar-irrep reduction",
      "minimal scalar-irrep reduction" in horn)
check("custody", "native radial action polynomial is exact",
      "I(t)=1456t^3+7\\kappa_1t^2" in native)
check("custody", "intrinsic artifact forbids silent observed-scalar identification",
      "not silently identified" in intrinsic)
check("custody", "K119 forbids fitted scalar second jets",
      "manufactured by a fitted `D2F`" in k119)
check("custody", "K120 isolates lambda as the remaining bridge",
      "conditional scalar bridge" in k120 and "lambda" in k120)
check("artifact", "source-native routing notice is present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "twenty lenses and explicit vote are recorded",
      "Twenty-lens reassessment and vote" in artifact and "H_B 15" in artifact)
check("artifact", "Variancer reverse scaffold is retained",
      "Retaining Variancer's reverse conditional" in artifact)
check("artifact", "I_sc coefficient import is explicitly forbidden",
      "without importing\n+`I_sc` coefficients" in artifact or "cannot be imported into `I1B`" in artifact)
check("artifact", "nonlinear reopening is fenced on an independently owned scalar jet",
      "only when a source/action/observation theorem independently owns" in artifact)
check("registry", "strict affine identity is serialized as false",
      registry["action_germs"]["nonzero_affine_action_germ_identity"] is False)
check("registry", "lambda remains an explicit translation datum",
      "LAMBDA_EXPLICIT" in registry["selected_scaffold"]["observed_translation"])
check("registry", "next gate is native I1B assembly",
      registry["next_gate"].startswith("K122_NATIVE_I1B"))
check("repo", "current question advances to native K122 assembly",
      "K122" in current and "native" in current.lower())
check("repo", "roadmap leads with K121",
      "K121" in roadmap[:5500] and "8736" in roadmap[:5500])
check("repo", "context records role link and action-germ separation",
      "role" in context[:10000].lower() and "action germ" in context[:10000].lower())

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
