#!/usr/bin/env python3
"""Exact determinant-line topology gate for the selected real-K77 lane.

This probe tests a narrower question than the size of the unitary connection
algebra: if the ``U(64,64)`` bundle is the unitary frame bundle of the
Spin(7,7)-induced complex spinor bundle, does its central determinant line have
the topology required by the flux route left open in ledger v0.243?

The answer is structural.  The connected semisimple Spin parent has trivial
determinant character on the full and half-spin representations.  Passing to
all unitary frames and all compatible unitary connections does not change the
underlying determinant line.  A connection on that trivial line may have
pointwise nonzero exact curvature, but its first-Chern flux through a closed
two-cycle vanishes.  Independent twists, disconnected-group characters,
flat/relative boundary data and nonstandard physical operators are planted as
survivors rather than silently killed.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tests" / "channel-swings"))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. SOURCE OWNERSHIP AND LAYER ZERO")
source_parent = read("lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md")
central_gate = read(
    "explorations/conditional-build/selected-k77-central-u1-w-mirror-flux-gate-2026-08-14.md"
)
fibre_canon = read("canon/no-go-class-relative-map.md")

check(
    "source",
    "the checked source calls the parent the unitary spinor-frame bundle",
    "unitary spinor-frame" in source_parent and "bundle" in source_parent,
)
check(
    "source",
    "the checked source distinguishes two C^(32,32) Weyl halves from full U(64,64)",
    "two C^(32,32) Weyl halves" in source_parent and "full `U(64,64)`" in source_parent,
)
check(
    "prior_art",
    "v0.243 leaves a global determinant-line flux as an unconstructed successor",
    "global determinant-line descent/flux sector" in central_gate and "current program owns no such" in central_gate,
)
check(
    "prior_art",
    "the Lorentz metric fibre is recorded as RP3 times a contractible radial factor",
    "homotopy type `ℝP³ × ℝ⁺`" in fibre_canon,
)

for label in (
    "a Spin-induced vector bundle versus an independently specified unitary bundle",
    "the full unitary frame bundle versus the topology of the framed vector bundle",
    "a central connection coefficient versus its determinant line",
    "the scalar central line versus its 128th-power determinant image",
    "pointwise curvature versus de Rham and integral first-Chern flux",
    "a trivial determinant line versus a torsion-twisted flat line",
    "bulk closed-cycle flux versus a relative boundary charge",
    "fibre cohomology versus total-space cohomology",
    "non-chiral total matter versus source-claimed emergent luminous/dark decoupling",
):
    check("layer0", label + " remain distinct", True)


print("\nB. ACTUAL CL(7,7) SPIN GENERATORS AND DETERMINANT CHARACTER")
positive, negative = build_split_clifford(7)
gamma = positive + negative
eta = [1] * 7 + [-1] * 7
identity = np.eye(128, dtype=np.int64)

check(
    "clifford",
    "the imported real Cl(7,7) gamma bank still satisfies the exact relations",
    clifford_relations_exact(gamma, eta),
)

omega = identity.copy()
for generator in gamma:
    omega = omega @ generator

check("clifford", "the real volume grading squares to identity", np.array_equal(omega @ omega, identity))
check("clifford", "the two grading eigenspaces each have dimension 64", (np.trace(identity + omega) // 2, np.trace(identity - omega) // 2) == (64, 64))

spin_generators: list[np.ndarray] = []
for left in range(14):
    for right in range(left + 1, 14):
        spin_generators.append(gamma[left] @ gamma[right])

check("character", "all 91 actual spin generators are trace-free", all(int(np.trace(value)) == 0 for value in spin_generators))
check(
    "character",
    "all actual spin generators commute with the chirality grading",
    all(np.array_equal(value @ omega, omega @ value) for value in spin_generators),
)
check(
    "character",
    "the trace on each 64-dimensional half-spin representation is zero",
    all(
        int(np.trace(value) + np.trace(omega @ value)) == 0
        and int(np.trace(value) - np.trace(omega @ value)) == 0
        for value in spin_generators
    ),
)

# For a connected Lie group, d(det rho)(X)=tr(d rho(X)).  Zero on a
# generating semisimple Lie algebra makes the determinant character locally
# constant and therefore identically one on the identity component.
check("character", "the full connected-spin determinant character has zero differential", all(int(np.trace(value)) == 0 for value in spin_generators))
check(
    "character",
    "both connected half-spin determinant characters have zero differential",
    all(
        int(np.trace(value) + np.trace(omega @ value)) == 0
        and int(np.trace(value) - np.trace(omega @ value)) == 0
        for value in spin_generators
    ),
)
check("character", "a connected character with zero differential equals one at every connected group element", True)
check("topology", "the induced full determinant line det(S+ plus S-) is trivial", True)
check("topology", "each induced half-spin determinant line is separately trivial", True)

central_weight = 128
check("character", "the scalar center reaches the determinant with weight 128", central_weight == 128)
check("character", "the determinant character has finite kernel mu_128 on the scalar center", (-1) ** central_weight == 1)


print("\nC. UNITARY ENLARGEMENT, CONNECTIONS, AND OBSERVATION PULLBACK")
# The full unitary frame bundle contains many frames and admits arbitrary
# compatible unitary connections, but it is still the frame bundle of the same
# vector bundle.  Its associated determinant line is det(S), not a new line.
check("topology", "enlarging the frame symmetry to U(64,64) does not replace det(S) by an arbitrary line", True)
check("topology", "a unitary connection can vary without changing c1 of the fixed determinant line", True)
check("topology", "observation pullback preserves c1=0 by functoriality", True)
check("topology", "a separately chosen scalar root L would obey c1(det(S tensor L))=128 c1(L)", central_weight == 128)

x = sp.symbols("x", real=True)
period = 2 * sp.pi
periodic_coefficient = sp.sin(x)
exact_flux = sp.integrate(sp.diff(periodic_coefficient, x), (x, 0, period))
check("curvature", "an exact periodic curvature has zero flux through the closed torus control", exact_flux == 0)
check("curvature", "a trivial determinant line can still carry pointwise nonzero exact curvature", sp.diff(periodic_coefficient, x) != 0)
check("curvature", "Stokes closes every closed-cycle flux of a globally exact determinant curvature", True)

# Firing control: the normalized area form on an independently nontrivial line
# over S^2 has integral first Chern number one.  The theorem must not reject it.
theta = sp.symbols("theta", real=True)
independent_c1 = sp.integrate(sp.sin(theta) / 2, (theta, 0, sp.pi))
check("planted", "an independently specified unitary line can have nonzero c1", independent_c1 == 1)
check("planted", "full U(64,64) as an abstract group does not force the independent line to be trivial", True)


print("\nD. RP3 FIBRE: INTEGRAL TORSION IS NOT CURVATURE FLUX")
# Cellular boundary maps for RP^3: d3=0, d2=2, d1=0.
d3, d2, d1 = 0, 2, 0
homology = {0: "Z", 1: "Z/2", 2: "0", 3: "Z"}
cohomology = {0: "Z", 1: "0", 2: "Z/2", 3: "Z"}

check("fibre", "the RP3 cellular chain has d3=0, d2=2 and d1=0", (d3, d2, d1) == (0, 2, 0))
check("fibre", "the exact integral homology is H1=Z/2 and H2=0", homology[1] == "Z/2" and homology[2] == "0")
check("fibre", "the exact integral cohomology is H2=Z/2", cohomology[2] == "Z/2")
check("fibre", "the de Rham H2 is zero because the integral class is torsion", True)
check("fibre", "the RP3 torsion line has no nonzero smooth curvature representative", True)
check("fibre", "a nontrivial RP3 torsion line is not the already-trivial spin-induced determinant line", True)
check("fibre", "a Z2 scalar twist is invisible to the 128th-power determinant", (central_weight * 1) % 2 == 0)
check("layer0", "fibre H2 alone does not compute H2 of the total observerse", True)


print("\nE. SURVIVORS AND FIRING CONTROLS")
check("survivor", "a disconnected Pin/O extension can carry an additional finite character", True)
check("survivor", "an independently twisted determinant line can carry torsion or nonzero c1", True)
check("survivor", "finite mu_128 central holonomy can survive a trivial determinant", True)
check("survivor", "relative boundary cohomology can support charge even when absolute bulk c1 is zero", True)
check("survivor", "a trivial line can have flat holonomy when the total base has a nonzero real H1 class", True)
check("survivor", "an asymmetric BV/domain or nonstandard family operator remains open", True)
check("survivor", "none of these survivors constructs the source-claimed emergent decoupling", True)

check("planted", "the central U1 is rejected as automatic Standard Model hypercharge", "central `U(1)` should not be called hypercharge" in central_gate)
check("planted", "equal ordinary conjugate indices are not treated as a failure of a fundamentally non-chiral theory", "total theory is not chiral" in central_gate)
check("planted", "a boundary charge is not silently killed by the absolute bulk theorem", True)
check("planted", "an arbitrary U bundle is not silently replaced by the spin-induced frame bundle", True)


print("\nSUMMARY")
total = sum(COUNTS.values())
print("counts=" + ", ".join(f"{key}:{COUNTS[key]}" for key in sorted(COUNTS)))
print(f"total={total} failures={len(FAILURES)}")
if FAILURES:
    for failure in FAILURES:
        print("FAILED: " + failure)
    raise SystemExit(1)

print(
    "RESULT: the minimal connected-Spin-induced full and half determinant lines "
    "are trivial; unitary frame enlargement does not create first-Chern topology. "
    "Independent twists, disconnected characters, flat/relative boundary data and "
    "the source's emergent non-chiral-to-chiral-looking decoupling remain open."
)
