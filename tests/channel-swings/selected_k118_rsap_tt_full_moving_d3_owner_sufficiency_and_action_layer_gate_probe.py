#!/usr/bin/env python3
"""Exact K118 full-moving D3 owner-sufficiency and action-layer gate."""

from pathlib import Path
import json
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHECKS = []


def check(kind, label, condition):
    ok = bool(condition)
    CHECKS.append((kind, label, ok))
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")


k117 = (ROOT / "explorations/conditional-build/selected-k117-rsap-tt-symbol-order-custody-and-moving-hessian-gate-2026-08-15.md").read_text()
intrinsic = (ROOT / "explorations/conditional-build/selected-cubic-augmented-torsion-d3-owner-decomposition-2026-08-06.md").read_text()
layers = (ROOT / "explorations/conditional-build/two-layer-action-selected-cubic-owner-retype-2026-08-06.md").read_text()
jets = (ROOT / "explorations/conditional-build/selected-action-second-soldering-observation-jets-2026-08-06.md").read_text()
normal = (ROOT / "explorations/conditional-build/selected-k77-full-normal-owner-bank-2026-08-08.md").read_text()
noether = (ROOT / "explorations/conditional-build/selected-k77-action-noether-preboundary-2026-08-08.md").read_text()

check("source", "K117 restores the z-dependent hh owner", "delta J_hh(z)=d z E_hh" in k117)
check("source", "intrinsic D3 distinguishes radial scalar from observed scalar", "It is not silently identified" in intrinsic and "theta_rad" in intrinsic)
check("source", "intrinsic mixed q0-qm summand is zero", "D^3I_T[\\theta_{\\rm rad},q_0,q_m]=0" in intrinsic)
check("source", "intrinsic massive summand is nonzero", "-\\frac{56}{3}\\alpha_{II}^2" in intrinsic)
check("source", "action-layer retype names I1B", "first layer `I1B`" in layers)
check("source", "action-layer retype names I2B", "second layer `I2B`" in layers)
check("source", "action-layer retype names observer I_II", "observer `I_II`" in layers)
check("source", "second-jet artifact leaves coefficient expansion open", "direct selected-action coefficient expansion" in jets.lower())
check("source", "normal owner split is noncanonical", "seven-way **owner split**" in normal and "does not transfer canonically" in normal)
check("source", "unrestricted boundary moment map remains live", "Unrestricted endpoint" in noether and "boundary moment map" in noether)

# Stationary pullback formula in one dimension.
x, H, C3, p, q2, r3, ell = sp.symbols("x H C3 p q2 r3 ell")
F = p*x + q2*x**2/2 + r3*x**3/6
I_stationary = H*F**2/2 + C3*F**3/6
pullback_d3 = sp.expand(I_stationary).diff(x, 3).subs(x, 0)
check("pullback", "stationary pullback uses only first and second map jets", sp.expand(pullback_d3 - (C3*p**3 + 3*H*p*q2)) == 0)
check("pullback", "stationary pullback is independent of third map jet", sp.diff(pullback_d3, r3) == 0)
I_offshell = ell*F + I_stationary
off_d3 = sp.expand(I_offshell).diff(x, 3).subs(x, 0)
check("control", "off-shell tadpole restores the third-map-jet term", sp.expand(off_d3 - pullback_d3) == ell*r3)

# Residual-square cubic at residual zero.
A, B, Q0, Q1 = sp.symbols("A B Q0 Q1")
U = A*x + B*x**2/2
Qx = Q0 + Q1*x
I2 = sp.expand(Qx*U**2/2)
I2_d2 = I2.diff(x, 2).subs(x, 0)
I2_d3 = I2.diff(x, 3).subs(x, 0)
check("residual-square", "residual-zero Hessian is A squared Q0", I2_d2 == A**2*Q0)
check("residual-square", "residual-zero cubic needs D2U and DQ", sp.expand(I2_d3 - (3*A*B*Q0 + 3*A**2*Q1)) == 0)
check("control", "Hessian does not determine residual-square cubic", sp.diff(I2_d3, B) != 0 and sp.diff(I2_d3, Q1) != 0)

# First-order pencil ambiguity.
a, b, d, c, e, m, q, s, t = sp.symbols("a b d c e m q s t", nonzero=True, real=True)
K0 = sp.Matrix([[a, 1], [1, 0]])
M0 = sp.Matrix([[0, 0], [0, b]])
K1 = sp.Matrix([[d, c], [c, e]])
M1 = sp.Matrix([[m, q], [q, s]])
coefficients = (d, c, e, m, q, s)
constraint_matrix = sp.Matrix([[1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1]])
check("dimension", "symmetric kinetic plus mass deformation has six coefficients", len(coefficients) == 6)
check("dimension", "hh kinetic and vv mass constraints have rank two", constraint_matrix.rank() == 2)
check("dimension", "four first-order pencil coefficients remain", len(coefficients) - constraint_matrix.rank() == 4)
check("dimension", "remaining slots are c e m q", all(v not in (d, s) for v in (c, e, m, q)))

Kdir = K0 + t*sp.Matrix([[d, 0], [0, 0]])
Mdir = M0 + t*sp.Matrix([[0, 0], [0, s]])
Ldir = sp.simplify(Kdir.inv()*Mdir)
Ddir = sp.factor(sp.trace(Ldir)**2 - 4*Ldir.det())
Ddir1 = sp.factor(Ddir.diff(t).subs(t, 0))
check("direct", "direct completion shares hh kinetic projection", Kdir.diff(t)[0, 0] == d)
check("direct", "direct completion shares vv mass projection", Mdir.diff(t)[1, 1] == s)
check("direct", "direct discriminant derivative", sp.factor(Ddir1 - 2*a*b*(a*s+b*d)) == 0)

xr, yr = sp.symbols("xr yr", real=True)
R = sp.Matrix([[xr, yr], [d/2-a*xr, s/(2*b)]])
Kfr1 = sp.simplify(R.T*K0 + K0*R)
Mfr1 = sp.simplify(R.T*M0 + M0*R)
L0 = K0.inv()*M0
Lfr1 = sp.simplify(-K0.inv()*Kfr1*L0 + K0.inv()*Mfr1)
check("field-redefinition", "congruence shares hh kinetic projection", sp.simplify(Kfr1[0, 0] - d) == 0)
check("field-redefinition", "congruence shares vv mass projection", sp.simplify(Mfr1[1, 1] - s) == 0)
check("field-redefinition", "normalized tangent is a commutator", sp.simplify(Lfr1 - (L0*R - R*L0)) == sp.zeros(2))
check("field-redefinition", "trace derivative vanishes", sp.simplify(sp.trace(Lfr1)) == 0)
check("field-redefinition", "determinant derivative vanishes", sp.simplify((L0.adjugate()*Lfr1).trace()) == 0)

S = sp.eye(2) + t*R
Kfr = sp.simplify(S.T*K0*S)
Mfr = sp.simplify(S.T*M0*S)
Lfr = sp.simplify(Kfr.inv()*Mfr)
Dfr = sp.factor(sp.trace(Lfr)**2 - 4*Lfr.det())
check("field-redefinition", "finite congruence dynamics is similar", sp.simplify(Lfr - S.inv()*L0*S) == sp.zeros(2))
check("field-redefinition", "finite congruence discriminant is fixed", sp.simplify(Dfr - a**2*b**2) == 0)
check("planted", "two completions generically disagree spectrally", sp.simplify(Ddir1.subs({a: 2, b: 3, d: 5, s: 7})) != 0)
check("planted", "known projections do not fix hv kinetic response", sp.simplify(Kfr1[0, 1].diff(yr)) == a)
check("planted", "known projections do not fix hv mass response", sp.simplify(Mfr1[0, 1].diff(xr)) == -a*b)

artifact = (ROOT / "explorations/conditional-build/selected-k118-rsap-tt-full-moving-d3-owner-sufficiency-and-action-layer-gate-2026-08-15.md").read_text()
registry = json.loads((ROOT / "lab/process/selected-k118-rsap-tt-full-moving-d3-owner-sufficiency-and-action-layer-gate.json").read_text())
current = (ROOT / "CURRENT-STATE.yaml").read_text()
roadmap = (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8-sig")
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
check("repo", "artifact names all four action layers", all(name in artifact for name in ("I_sc", "I1B", "I2B", "I_II")))
check("repo", "registry records four-dimensional ambiguity", registry["pencil_ambiguity"]["remaining_dimension"] == 4)
check("repo", "registry denies a selected third-derivative identification", registry["action_layers"]["third_derivative_identification_selected"] is False)
check("repo", "current question has advanced through K120 to scalar-bridge selection", "scalar bridge" in current.lower() and "two-jet" in current.lower())
check("repo", "roadmap preserves K118 beneath current K120", "K120" in roadmap[:3500] and "K118" in roadmap and "action layer" in roadmap.lower())
check("repo", "context blocks direct owner assembly", "K118" in context[:7000] and "four" in context[:7000].lower())
check("repo", "research status records K118", "K118 TT full-moving D3" in status)
check("repo", "K117 carries K118 successor notice", "K118 ACTION-LAYER CORRECTION" in k117)
check("repo", "reverse scaffold routes K119 to layer selection", registry["reverse_scaffold"]["next_swings"][0] == "K119_ACTION_LAYER_AND_SCALAR_LIFT_SELECTION")

failures = [item for item in CHECKS if not item[2]]
print(f"\nTOTAL {len(CHECKS)}  FAILURES {len(failures)}")
raise SystemExit(1 if failures else 0)
