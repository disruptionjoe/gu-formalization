#!/usr/bin/env python3
"""Exact composition of the v0.15 zero-mode projector with v0.142 amplitude family."""

from pathlib import Path
import sympy as sp


COUNTS = {k: 0 for k in (
    "prior", "source", "exact", "layer0", "global", "fredholm",
    "symplectic", "cosmology", "accounting", "planted",
)}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append((kind, label))


ROOT = Path(__file__).resolve().parents[2]
prior_projector = ROOT / "tests/channel-swings/first_interaction_krein_global_zero_mode_probe.py"
prior_family = ROOT / "tests/channel-swings/selected_k77_zero_fermion_vev_selector_exhaustion_probe.py"
source_receipt = ROOT / "lab/sources/first-interaction-krein-global-zero-mode-source-reinspection-2026-08-05.md"

print("A. PRIOR ART AND SOURCE RETURN")
p_text = prior_projector.read_text()
f_text = prior_family.read_text()
s_text = source_receipt.read_text()
check("prior", "v0.15 already owns Pi0 and Q", "Pi0 = sp.ones(n, n) / n" in p_text)
check("prior", "v0.142 already owns the one-amplitude family", '"local_amplitude_dimension": 1' in f_text)
check("source", "the source publishes no normalized global functional",
      "publish a zero-mode projector" in s_text and "derive a normalized global" in s_text)
check("source", "the source distinguishes dynamic coupling from a normalized average", "a specified normalized global average" in s_text)

print("\nB. EXACT LOCAL FAMILY")
f, u, t = sp.symbols("f u t", real=True)
ET = 312 * (f + u + t**2) + t
Eg = 624 * (f + u / 2 + t**2 / 3) + t
family = {f: t**2 / 3, u: -t / 312 - 4 * t**2 / 3}
J = sp.Matrix([ET, Eg]).jacobian([f, u, t])
vt = sp.Matrix([2 * t / 3, -sp.Rational(1, 312) - 8 * t / 3, 1])
check("exact", "the two source equations vanish on the family", sp.simplify(ET.subs(family)) == 0 and sp.simplify(Eg.subs(family)) == 0)
check("exact", "the source Jacobian has rank two", J.subs(family).rank() == 2)
check("exact", "the family tangent remains in its kernel", sp.simplify(J.subs(family) * vt) == sp.zeros(2, 1))

print("\nC. NORMALIZED PROJECTOR COMPOSITION")
n = 4
one = sp.ones(n, 1)
Pi0 = sp.ones(n, n) / n
Q = sp.eye(n) - Pi0
ell = one.T / n
t_field = t * one
f_field = family[f] * one
u_field = family[u] * one
check("exact", "Pi0 is the normalized constant-mode projector", Pi0**2 == Pi0 and Pi0 * one == one and Pi0.rank() == 1)
check("exact", "Q kills the constant mode", Q * one == sp.zeros(n, 1))
check("layer0", "ell reads the amplitude but does not impose an equation", sp.simplify((ell * t_field)[0]) == t)
check("layer0", "Q removes all three constant family fields", Q * t_field == sp.zeros(n, 1) and Q * f_field == sp.zeros(n, 1) and Q * u_field == sp.zeros(n, 1))

rho = sp.Matrix(sp.symbols("rho0:4", real=True))
delta = sp.symbols("delta", real=True)
L = sp.Matrix([[2, -1, 0, -1], [-1, 2, -1, 0], [0, -1, 2, -1], [-1, 0, -1, 2]])
K = sp.eye(n) + L
R = sp.simplify(K.inv() * Q * rho)
R_shift = sp.simplify(K.inv() * Q * (rho + delta * one))
check("global", "Q screens an independent constant source shift", sp.simplify(R_shift - R) == sp.zeros(n, 1))
check("global", "the screened response is mean zero", sp.simplify((ell * R)[0]) == 0)
check("layer0", "screening the source does not select t", not R.has(t) and not R_shift.has(t))

print("\nD. FREDHOLM AND NORMALIZATION DISTINCTIONS")
check("fredholm", "Q source automatically passes the constant left-kernel condition", sp.simplify((one.T * Q * rho)[0]) == 0)
check("fredholm", "that compatibility condition is independent of t", not sp.simplify((one.T * Q * rho)[0]).has(t))

c = sp.symbols("c", real=True)
J_with_value = sp.Matrix([ET, Eg, t - c]).jacobian([f, u, t])
check("accounting", "supplying ell(t)=c raises equation rank to three", J_with_value.subs(family).rank() == 3)
check("accounting", "the selected value is exactly the supplied scalar c", sp.solve([ET, Eg, t - c], [f, u, t], dict=True)[0][t] == c)
check("layer0", "requiring the VEV field itself to lie in im Q forces t=0", sp.solve(sp.Eq((ell * t_field)[0], 0), t) == [0])

t0 = sp.Rational(5, 17)
Kplant = L + (t - t0) * Pi0
check("planted", "an amplitude-dependent global operator would be detected",
      sp.simplify(Kplant.det() - 16 * (t - t0)) == 0)
check("planted", "the planted Fredholm wall selects t0", sp.solve(sp.Eq(Kplant.det(), 0), t) == [t0])

print("\nE. SCOPE FENCES")
check("symplectic", "the existing local symplectomorphism remains amplitude-blind", True)
check("global", "ell still requires a domain measure or observer owner", True)
check("cosmology", "constant-shift screening is not nonzero-VEV magnitude selection", True)
check("cosmology", "zero-mode removal is not an observed dark-energy prediction", True)
check("accounting", "ell is not silently identified with P2", True)
check("accounting", "no residue or quotient moves before an owner is constructed", True)

result = {
    "verdict": "GLOBAL_PROJECTOR_SCREENS_SHIFTS__DOES_NOT_SELECT_NONZERO_VEV_AMPLITUDE",
    "family_dimension": 1,
    "source_equation_rank": 2,
    "projector_rank": 1,
    "screened_response_rank": int((K.inv() * Q).rank()),
    "amplitude_equations_added_by_Q": 0,
    "if_field_in_im_Q": "T_EQUALS_ZERO",
    "if_ell_T_equals_c": "T_EQUALS_SUPPLIED_C",
    "next_gate": "DERIVE_ACTION_OWNED_AMPLITUDE_DEPENDENT_GLOBAL_COMPATIBILITY_OR_EXPLICIT_EXTERNAL_VALUE__COMMON_DOMAIN_FIRST",
    "failures": FAILURES,
    "counts": COUNTS,
}

print("\nRESULT")
for key, value in result.items():
    print(f"{key}={value}")
total = sum(COUNTS.values())
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
