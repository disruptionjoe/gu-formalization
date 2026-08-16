#!/usr/bin/env python3
"""Exact K120 source-coordinate two-jet and scalar-bridge gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


# Exact local model of (g,T)->(g,varpi=B_LC(g)+T).
theta, h, v = sp.symbols("theta h v")
lam, b1, b2 = sp.symbols("lam b1 b2", nonzero=True)
B = b1*h + b2*h**2/2
F = sp.Matrix([h, lam*theta, v+B])
variables = (theta, h, v)
J = F.jacobian(variables).subs({theta: 0, h: 0, v: 0})

check("coordinate", "nonzero scalar slope gives a local coordinate lift", sp.factor(J.det()) == -lam)
check("coordinate", "theta column is the radial injection", J[:, 0] == sp.Matrix([0, lam, 0]))
check("coordinate", "metric column contains the LC first jet", J[:, 1] == sp.Matrix([1, 0, b1]))
check("coordinate", "distortion column is independent", J[:, 2] == sp.Matrix([0, 0, 1]))

hessians = [sp.hessian(component, variables) for component in F]
check("twojet", "metric and radial output second jets vanish in the control", hessians[0] == sp.zeros(3) and hessians[1] == sp.zeros(3))
check("twojet", "only the nonlinear LC hh second jet survives", hessians[2][1, 1] == b2 and sum(1 for x in hessians[2] if x != 0) == 1)
check("twojet", "LC second jet is independent of scalar normalization", not hessians[2].has(lam))

lam1, lam2 = sp.symbols("lam1 lam2", nonzero=True)
J1 = J.subs(lam, lam1)
J2 = J.subs(lam, lam2)
check("ambiguity", "two lifts share the metric TT column", J1[:, 1] == J2[:, 1])
check("ambiguity", "two lifts share the distortion TT column", J1[:, 2] == J2[:, 2])
check("ambiguity", "two lifts differ only in the scalar column", sp.simplify(J1[:, 0] - J2[:, 0]) == sp.Matrix([0, lam1-lam2, 0]))

# Native cubic pullback shows the common scalar rescaling.
ch, cv = sp.symbols("c_h c_v")
g, r, w = F
u = sp.expand(w - B)
check("coordinate", "independent distortion is recovered as w minus B", u == v)
I_native = ch*r*g**2/2 + cv*r*u**2/2
d_thh = sp.diff(I_native, theta, h, h).subs({theta: 0, h: 0, v: 0})
d_tvv = sp.diff(I_native, theta, v, v).subs({theta: 0, h: 0, v: 0})
check("cubic", "theta-h-h pullback scales with lambda", d_thh == lam*ch)
check("cubic", "theta-v-v pullback scales with lambda", d_tvv == lam*cv)
check("cubic", "cubic ratio is lambda independent", sp.simplify(d_thh/d_tvv - ch/cv) == 0)

# Quadratic matching is a conditional cross-action equation, not geometry.
kappa, kr = sp.symbols("kappa k_rad", nonzero=True)
native_quadratic = kr*(lam*theta)**2/2
observed_quadratic = kappa*theta**2/2
native_coefficient = sp.diff(native_quadratic, theta, 2)
observed_coefficient = sp.diff(observed_quadratic, theta, 2)
check("pairing", "native pulled scalar norm is k_rad lambda squared", native_coefficient == kr*lam**2)
check("pairing", "quadratic matching imposes lambda squared ratio", sp.solve(native_coefficient-observed_coefficient, lam**2) == [kappa/kr])
check("pairing", "quadratic matching alone is sign blind", native_coefficient.subs(lam, -lam) == native_coefficient)

# Pullback of a native preboundary one-form.
pg, pr, pw = sp.symbols("p_g p_r p_w")
theta_coeff = (sp.Matrix([pg, pr, pw]).T * J[:, 0])[0]
h_coeff = (sp.Matrix([pg, pr, pw]).T * J[:, 1])[0]
v_coeff = (sp.Matrix([pg, pr, pw]).T * J[:, 2])[0]
check("preboundary", "scalar boundary column retains lambda", theta_coeff == lam*pr)
check("preboundary", "metric boundary column contains LC soldering", h_coeff == pg+b1*pw)
check("preboundary", "distortion boundary column is owned directly", v_coeff == pw)

# Source/action and durable repository custody checks.
k119 = (ROOT / "explorations/conditional-build/selected-k119-rsap-tt-stationary-twojet-selection-obstruction-2026-08-15.md").read_text()
sourcevars = (ROOT / "explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md").read_text()
jets = (ROOT / "explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md").read_text()
intrinsic = (ROOT / "explorations/conditional-build/selected-cubic-augmented-torsion-d3-owner-decomposition-2026-08-06.md").read_text()
observer = (ROOT / "explorations/conditional-build/selected-second-layer-observation-owner-retype-2026-08-07.md").read_text()
boundary = (ROOT / "explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md").read_text()
artifact = (ROOT / "explorations/conditional-build/selected-k120-rsap-tt-geometric-twojet-custody-and-scalar-bridge-gate-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k120-rsap-tt-geometric-twojet-custody-and-scalar-bridge-gate.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("source", "K119 forbids fitted geometric jets", "without using the desired cubic as fitting data" in k119)
check("source", "source variables are g and independent varpi", "source variables | metric `g` and independent connection `varpi`" in sourcevars)
check("source", "source identity T equals varpi minus LC", "T=\\varpi-B_{LC}(g)" in sourcevars or "T=varpi-B_LC(g)" in sourcevars)
check("source", "second spin LC jet is exact and nonzero", "nonzero, symmetric second metric jet" in jets)
check("source", "intrinsic artifact keeps radial scalar distinct", "not silently identified" in intrinsic)
check("source", "observation is a receiver not a new action field", "receiver/package around the upstairs theory" in observer)
check("source", "unrestricted boundary moment map remains live", "unrestricted endpoint transformations: live moment map" in boundary)
check("artifact", "source-native routing notice is present", "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "I1B partial closure is explicit", "TT geometric two-jet is owned for `I1B`" in artifact)
check("registry", "registry owns TT columns but not the complete map", registry["i1b_twojet"]["tt_columns_independent_of_lambda"] and not registry["i1b_twojet"]["complete_three_field_map_selected"])
check("registry", "registry routes next to scalar normalization", registry["next_gate"].startswith("K121_SCALAR_BRIDGE"))
check("repo", "current question advances to scalar bridge", "scalar bridge" in current.lower())
check("repo", "roadmap leads with K120", "K120" in roadmap[:5000] and "scalar" in roadmap[:5000].lower())
check("repo", "context records TT partial closure", "tt" in context[:9000].lower() and "lambda" in context[:9000].lower())
check("repo", "K119 carries the K120 successor closure", "K120 successor closure" in k119)

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
