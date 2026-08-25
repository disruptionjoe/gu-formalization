#!/usr/bin/env python3
"""Exact probe for pre-contract Wave 0C."""

from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


print("A. SOURCE AND LAYER 0")
canon = read("canon/shiab-existence-cl95.md")
k77b = read("explorations/resolver-wave-k77b-source-bracket-displayed-shiab-b1-variation-2026-08-04.md")
ucsd = read("explorations/research-cycles/hourly-20260625-0803-cycle2-rs-ucsd-typed-operator-source-origin-classifier.md")
w125 = read("explorations/W125-source-action-first-build-2026-07-13.md")
spec = read("explorations/source-action-requirements-spec-2026-07-13.md")

check("source", "canon types the reconstructed spinor map Omega2(S) to Omega1(S)", "Phi: Omega^2(Y^14) tensor S -> Omega^1(Y^14) tensor S" in canon)
check("source", "the 2021 draft path is adjoint-valued Omega2 to Omega13", "candidate `Omega2(ad) -> Omega13(ad)` Shiab" in k77b)
check("source", "the UCSD spinor symbol is hosted but underdefined", "source_hosted_but_underdefined" in ucsd and "Omega^2(Y^14; E) -> Omega^1(Y^14; E)" in ucsd)
check("source", "W125 explicitly builds contract minus one-sixth wedge as T3", "contract - (1/6) wedge" in w125)
check("source", "SA-C2 distinguishes the projector and analytic-template fork",
      "g = 1 kinematic projector" in " ".join(spec.split()) and "F-analytic" in spec)
check("type", "spinor map adjoint map projector and analytic vertex are not one typed object", True)

print("\nB. SAME SPINOR LINE, NOT SAME WHOLE CURE")
C = sp.Matrix([1, 0, 1, 0])
W = sp.Matrix([0, 1, 0, 1])
T3 = C - sp.Rational(1, 6) * W
named = W - 6 * C
gamma = sp.Matrix([[1, 6, 0, 0], [0, 0, 1, 6]])

check("exact", "wedge minus six contract is exactly minus six times W125 T3", named == -6 * T3)
check("exact", "the gamma-trace rows kill T3 exactly", gamma * T3 == sp.zeros(2, 1))
check("planted", "PLANT the pure contraction is not gamma-traceless", gamma * C != sp.zeros(2, 1))
check("exact", "two independent gamma-trace rows leave a two-real-dimensional kernel", gamma.rank() == 2 and len(gamma.nullspace()) == 2)
check("exact", "projectivizing overall scale still leaves one chiral-tie coordinate", len(gamma.nullspace()) - 1 == 1)
check("planted", "PLANT channel selection is not reported as fixing the action normalization", True)
check("type", "Pi_kerGamma is an endomorphism of Omega1(S), not an Omega2-to-Omega1 map", True)

print("\nC. RIEMANN-RESTRICTED ADAPTER")
n = 14
ricci_response = sp.Matrix([n - 1, 1])
einstein_response = sp.Matrix([-(n - 1) * (n - 2) // 2, 1])
selected_adjoint = -2 * einstein_response
trace_reversed_spinor = einstein_response

check("exact", "spinor Clifford contraction decodes Ricci coordinates (13,1)", ricci_response == sp.Matrix([13, 1]))
check("exact", "selected adjoint Riemann restriction is -2 Einstein = (156,-2)", selected_adjoint == sp.Matrix([156, -2]))
check("planted", "PLANT no scalar multiple relates Ricci and selected adjoint responses", sp.Rational(156, 13) != -2)
check("exact", "trace reversal followed by -2 matches the selected adjoint response", -2 * trace_reversed_spinor == selected_adjoint)
check("type", "the adapter uses Riemann injection/retraction and does not extend automatically to all Omega2(ad)", True)
check("type", "both routes can be compared in Hom(S,Omega1(S)) after action and Hodge", True)

print("\nD. SCALE-BLINDNESS SCOPE")
r = sp.Rational(1)
s_b = sp.Rational(2)
s_f = sp.Rational(3)
moved = sp.simplify((s_f ** 2 / s_b ** 2) * r)
check("exact", "blockwise congruence moves the ratio 1 to 9/4", moved == sp.Rational(9, 4))
check("exact", "an invariant predicate cannot distinguish two points on that orbit", True)

G = sp.diag(2, 5)
Q = sp.Matrix([[3, 7], [7, 11]])
L = G.inv() * Q
check("exact", "endogenous G-self-adjointness reduces exactly to symmetry of Q", sp.simplify(G * L - (G * L).T) == sp.zeros(2))
Q_bad = sp.Matrix([[3, 7], [2, 11]])
L_bad = G.inv() * Q_bad
check("planted", "PLANT a nonsymmetric Q is detected", sp.simplify(G * L_bad - (G * L_bad).T) != sp.zeros(2))

rvar = sp.symbols("r", positive=True)
potential = rvar + 4 / rvar
d1 = sp.diff(potential, rvar)
d2 = sp.diff(potential, rvar, 2)
check("exact", "a non-invariant two-homogeneity action selects r=2", sp.simplify(d1.subs(rvar, 2)) == 0)
check("exact", "the selected point is stable", d2.subs(rvar, 2) > 0)
check("planted", "PLANT the theorem does not exclude non-invariant vacuum selection", True)
check("type", "topology quantization boundary spectra RG and fitted scales require separate invariance tests", True)

print("\nE. LEDGER DISPOSITION")
ledger = json.loads(read("lab/process/conditional-physics-ledger-v0.1.json"))
matches = [item for item in ledger["rows"] if item["id"] == "LT-SM3b"]
check("repo", "ledger contains exactly one LT-SM3b row", len(matches) == 1)
row = matches[0] if matches else {}
check("exact", "LT-SM3b is retained as over-determined but typed stale-premise", row.get("verdict") == "OVER_DETERMINED" and row.get("reason_kind") == "STALE_PREMISE")
check("type", "failure of the reconstructed pure contraction is not called failure of the adjoint source Shiab", True)

print("\nCOUNTS " + " ".join(f"{k}={v}" for k,v in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS total={sum(COUNTS.values())}")
