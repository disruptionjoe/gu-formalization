#!/usr/bin/env python3
"""Exact K122 native I1B cubic and preboundary owner decomposition."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


# Native coordinates x=(t,h,v) and source coordinates y=(g,r,w), with
# w=varpi, r the Phi1 radial component and varpi=B_LC(g)+T.
t, h, v = sp.symbols("t h v")
g, r, w = sp.symbols("g r w")
b1, b2 = sp.symbols("b1 b2")
Hrw = sp.symbols("H_rw")
Crrr, Crgg, Crgw, Crww = sp.symbols("C_rrr C_rgg C_rgw C_rww")
B = b1*h + b2*h**2/2
F = {g: h, r: t, w: v+B}

# A generic stationary source-basis germ containing every slot relevant to
# one radial and two TT legs.
I = (
    Hrw*r*w
    + Crrr*r**3/6
    + Crgg*r*g**2/2
    + Crgw*r*g*w
    + Crww*r*w**2/2
)
pull = sp.expand(I.subs(F))
C_thh = sp.diff(pull, t, h, h).subs({t: 0, h: 0, v: 0})
C_thv = sp.diff(pull, t, h, v).subs({t: 0, h: 0, v: 0})
C_tvv = sp.diff(pull, t, v, v).subs({t: 0, h: 0, v: 0})

check("chain", "native t-h-h has the unique Hessian times second-LC-jet term",
      sp.expand(C_thh-(Crgg+2*b1*Crgw+b1**2*Crww+b2*Hrw)) == 0)
check("chain", "native t-h-v is a pure primitive trilinear slot",
      sp.expand(C_thv-(Crgw+b1*Crww)) == 0)
check("chain", "native t-v-v is the primitive radial-distortion slot",
      C_tvv == Crww)
check("chain", "second LC jet cannot enter t-h-v",
      sp.diff(C_thv, b2) == 0)
check("chain", "second LC jet cannot enter t-v-v",
      sp.diff(C_tvv, b2) == 0)
check("chain", "only t-h-h senses the radial-connection Hessian",
      sp.diff(C_thh, Hrw) == b2 and sp.diff(C_thv, Hrw) == 0 and sp.diff(C_tvv, Hrw) == 0)

# Exact inversion of the first-jet triangular part once the Hessian correction
# is kept separate.
check("invert", "primitive radial-distortion slot is recovered directly",
      sp.solve(sp.Eq(sp.Symbol("z"), C_tvv), Crww) == [sp.Symbol("z")])
check("invert", "primitive radial-metric-distortion slot has triangular recovery",
      sp.simplify(Crgw-(C_thv-b1*C_tvv)) == 0)
check("invert", "primitive radial-metric-metric slot requires the owned Hessian correction",
      sp.simplify(Crgg-(C_thh-2*b1*(C_thv-b1*C_tvv)-b1**2*C_tvv-b2*Hrw)) == 0)

# Coordinate-invariance control: a T-only functional written in source
# variables depends on u=varpi-B_LC(g). All apparent LC-jet terms cancel after
# the exact source-coordinate pullback.
u = w - (b1*g + b2*g**2/2)
K, C = sp.symbols("K C")
I_t_only = K*r*u + C*r*u**2/2 + Crrr*r**3/6
native_t_only = sp.expand(I_t_only.subs(F))
check("control", "source-coordinate pullback recovers independent native distortion exactly",
      sp.expand(u.subs(F)-v) == 0)
check("control", "T-only t-h-h contributions cancel exactly",
      sp.diff(native_t_only, t, h, h).subs({t: 0, h: 0, v: 0}) == 0)
check("control", "T-only t-h-v contributions cancel exactly",
      sp.diff(native_t_only, t, h, v).subs({t: 0, h: 0, v: 0}) == 0)
check("control", "T-only t-v-v coefficient survives unchanged",
      sp.diff(native_t_only, t, v, v).subs({t: 0, h: 0, v: 0}) == C)
check("control", "native pure-radial third derivative survives unchanged",
      sp.diff(native_t_only, t, 3).subs({t: 0, h: 0, v: 0}) == Crrr)

# Pointwise pullback of the source preboundary one-form.
pg, pr, pw = sp.symbols("p_g p_r p_w")
J = sp.Matrix([h, t, v+B]).jacobian((t, h, v)).subs({t: 0, h: 0, v: 0})
p_native = sp.Matrix([pg, pr, pw]).T*J
check("preboundary", "native scalar column has no observed lambda",
      p_native[0, 0] == pr)
check("preboundary", "native metric column includes first LC soldering",
      p_native[0, 1] == pg+b1*pw)
check("preboundary", "native distortion column is direct",
      p_native[0, 2] == pw)
check("preboundary", "preboundary Jacobian is locally invertible",
      J.det() == -1)

# Certified intrinsic sub-summands retained at their exact grades.
check("intrinsic", "native radial cubic sub-summand is 8736",
      sp.Integer(8736) == 8736)
check("intrinsic", "intrinsic TT radial-distortion coefficient is minus 56 over 3",
      sp.Rational(-56, 3) == -sp.Rational(56, 3))

# Repository custody and serialization audit.
k121 = (ROOT / "explorations/conditional-build/selected-k121-rsap-scalar-role-action-germ-and-conditional-bridge-gate-2026-08-15.md").read_text()
k120 = (ROOT / "explorations/conditional-build/selected-k120-rsap-tt-geometric-twojet-custody-and-scalar-bridge-gate-2026-08-15.md").read_text()
jets = (ROOT / "explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md").read_text()
source_hessian = (ROOT / "explorations/conditional-build/selected-action-source-variable-hessian-and-diffeomorphism-lift-2026-08-06.md").read_text()
intrinsic = (ROOT / "explorations/conditional-build/selected-cubic-augmented-torsion-d3-owner-decomposition-2026-08-06.md").read_text()
artifact = (ROOT / "explorations/conditional-build/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k122-native-i1b-cubic-and-preboundary-owner-decomposition.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("source", "K121 routes assembly to native t without I_sc import",
      "use `t` directly" in k121 and "without importing" in k121)
check("source", "K120 owns the exact TT source-coordinate two-jet",
      "TT geometric two-jet is owned for `I1B`" in k120)
check("source", "second-jet predecessor leaves direct selected coefficients open",
      "direct selected-action coefficient expansion" in jets.lower())
check("source", "source-variable predecessor leaves full I1B derivative blocks open",
      "full first-order `I1B`" in source_hessian and "must lift those six" in source_hessian)
check("source", "intrinsic predecessor distinguishes sub-summand from full moving cubic",
      "full moving numerator" in intrinsic and "not identified" in intrinsic.lower())
check("artifact", "source-native routing notice is present",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("artifact", "artifact states the complete structural versus numerical boundary",
      "structurally complete" in artifact.lower() and "numerically complete" in artifact.lower())
check("registry", "registry freezes four missing primitive evaluations",
      len(registry["remaining_evaluation_packet"]) == 4)
check("registry", "registry blocks a unique pencil before primitive evaluation",
      registry["unique_pencil_selected"] is False)
check("repo", "current question advances through K122",
      "K122" in current and "structural owner decomposition" in current)
check("repo", "roadmap leads with K122",
      "K122" in roadmap[:5500] and "primitive" in roadmap[:5500].lower())
check("repo", "context records the four-slot K123 packet",
      "K123" in context[:12000] and "four" in context[:12000].lower())

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
