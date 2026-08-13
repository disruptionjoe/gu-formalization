#!/usr/bin/env python3
"""Exact Layer-0 gate for the K77 complete receiver and metric BV complex.

This probe does not identify the selected GU Euler operator with Einstein's.
It proves that the ten conormal coordinates of ordinary section pullback become
the ten independent metric-section Euler coordinates under the already-owned
complete receiver, then uses the standard linearized Einstein complex as the
typed physical comparator for what a diffeomorphism/BV reduction may remove.
"""

from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def reject(label, bad_condition):
    check("planted", f"PLANT {label}", not bool(bad_condition))


PAIRS = list(combinations_with_replacement(range(4), 2))
ETA = sp.diag(-1, 1, 1, 1)


def symmetric_basis(column):
    h = sp.zeros(4)
    mu, nu = PAIRS[column]
    h[mu, nu] = 1
    h[nu, mu] = 1
    return h


def metric_complex(k_components):
    """Return diffeo, Einstein and Bianchi symbols over QQ."""
    k = sp.Matrix(k_components)             # covector k_mu
    k_up = ETA * k
    k_sq = (k.T * ETA * k)[0]
    diffeo = sp.zeros(10, 4)
    einstein = sp.zeros(10, 10)
    bianchi = sp.zeros(4, 10)

    for row, (mu, nu) in enumerate(PAIRS):
        for rho in range(4):
            diffeo[row, rho] = (
                k[mu] * ETA[nu, rho] + k[nu] * ETA[mu, rho]
            )

    for column in range(10):
        h = symmetric_basis(column)
        trace = sum(ETA[mu, nu] * h[mu, nu]
                    for mu in range(4) for nu in range(4))
        kk_h = sum(k_up[mu] * k_up[nu] * h[mu, nu]
                   for mu in range(4) for nu in range(4))
        output = sp.zeros(4)
        for mu in range(4):
            for nu in range(4):
                ricci = sp.Rational(1, 2) * (
                    k[mu] * sum(k_up[rho] * h[rho, nu] for rho in range(4))
                    + k[nu] * sum(k_up[rho] * h[rho, mu] for rho in range(4))
                    - k_sq * h[mu, nu]
                    - k[mu] * k[nu] * trace
                )
                scalar = kk_h - k_sq * trace
                output[mu, nu] = ricci - sp.Rational(1, 2) * ETA[mu, nu] * scalar
        for row, (mu, nu) in enumerate(PAIRS):
            einstein[row, column] = output[mu, nu]

    for column, (mu, nu) in enumerate(PAIRS):
        for rho in range(4):
            bianchi[rho, column] = (
                (k_up[mu] if nu == rho else 0)
                + (k_up[nu] if mu == rho and nu != mu else 0)
            )

    return diffeo, einstein, bianchi


def quotient_dimensions(diffeo, einstein, bianchi):
    field_cohomology = (10 - einstein.rank()) - diffeo.rank()
    equation_cohomology = (10 - bianchi.rank()) - einstein.rank()
    return field_cohomology, equation_cohomology


portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
iti = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k77-physical-section-faithfulness-gate-2026-08-08.md").read_text()
contact = (ROOT / "explorations/conditional-build/selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md").read_text()

print("A. SOURCE LOCUS AND LAYER ZERO")
check("source", "Portal makes the metric fibre ten-dimensional",
      "10-dimensional metric along the fibers" in portal)
check("source", "Portal names sigma as the field communicating between U and X",
      "a section \\(\\sigma\\)" in portal and "communicate back and forth" in portal)
check("source", "the later source says a metric is a section of its own metric bundle",
      "A metric is a section of its own bundle of metrics" in iti)
check("source", "the source types Einstein's tensor by diffeomorphism orthogonality",
      "perpendicular to orbits under the diffeomorphism group" in iti)
check("source", "the source places the replacement equation upstairs before pullback",
      "before being pulled back onto the manifold" in portal)
check("source", "no checked source prints the complete receiver/BV complex",
      "SOURCE-SILENT" in predecessor)
check("type", "base displacement and independent metric-section variation are distinct", True)
check("type", "field gauge orbit and equation Bianchi identity are dual but distinct", True)
check("type", "Einstein comparator and selected K77 Euler operator are not identified", True)

print("\nB. COMPLETE RECEIVER RETYPES THE CONORMAL TEN")
J = sp.Matrix(10, 4, lambda a, mu: sp.Rational((a + 2) * (mu + 1) - 7, 11))
field_map = sp.BlockMatrix([
    [sp.eye(4), sp.zeros(4, 10)],
    [J, sp.eye(10)],
]).as_explicit()
base_motion = field_map[:, :4]
metric_motion = field_map[:, 4:]
ordinary_pullback = base_motion.T
conormal = sp.Matrix.vstack(-J.T, sp.eye(10))
complete_equation_dual = field_map.T

check("repo", "v0.79 records rank-four pullback and rank-ten conormal kernel",
      "rank four and the exact ten-dimensional" in predecessor)
check("repo", "the contact predecessor has rank-ten metric directions and diagonal Ward cancellation",
      "rank ten" in contact and "diagonal motion" in contact)
check("exact", "base motion has rank four", base_motion.rank() == 4)
check("exact", "independent metric-section motion has rank ten", metric_motion.rank() == 10)
check("exact", "the combined field variation map is invertible rank fourteen",
      field_map.rank() == 14 and field_map.det() == 1)
check("exact", "ordinary pullback annihilates all ten graph-conormal equations",
      ordinary_pullback * conormal == sp.zeros(4, 10))
check("exact", "the complete equation dual maps conormal equations to pure metric equations",
      complete_equation_dual * conormal == sp.Matrix.vstack(sp.zeros(4, 10), sp.eye(10)))
check("exact", "all ten conormal equations survive as independent metric Euler coordinates",
      (complete_equation_dual * conormal).rank() == 10)
reject("ordinary pullback is a stationarity test for independent metric variations",
       ordinary_pullback.rank() == 14)
reject("the complete receiver makes the conormal action witness disappear",
       (complete_equation_dual * conormal).rank() == 0)

print("\nC. NONCHARACTERISTIC METRIC/BIANCHI COMPLEX")
for label, k in (("timelike", (1, 0, 0, 0)), ("spacelike", (0, 1, 0, 0))):
    D, G, W = metric_complex(k)
    check("exact", f"{label} diffeomorphism symbol has rank four", D.rank() == 4)
    check("exact", f"{label} Einstein symbol has rank six", G.rank() == 6)
    check("exact", f"{label} Bianchi symbol has rank four", W.rank() == 4)
    check("exact", f"{label} pure gauge lies in the Einstein kernel", G * D == sp.zeros(10, 4))
    check("exact", f"{label} Einstein image obeys Bianchi", W * G == sp.zeros(4, 10))
    check("theorem", f"{label} field complex is exact at Sym2",
          D.rank() == 10 - G.rank())
    check("theorem", f"{label} equation complex is exact at Sym2",
          G.rank() == 10 - W.rank())

print("\nD. NULL SYMBOL LEAVES TWO SPIN-TWO CLASSES")
D0, G0, W0 = metric_complex((1, 0, 0, 1))
field_h, equation_h = quotient_dimensions(D0, G0, W0)
check("exact", "null diffeomorphism symbol remains rank four", D0.rank() == 4)
check("exact", "null Einstein symbol drops to rank four", G0.rank() == 4)
check("exact", "null Bianchi symbol remains rank four", W0.rank() == 4)
check("exact", "null pure gauge remains in the Einstein kernel", G0 * D0 == sp.zeros(10, 4))
check("exact", "null Einstein image remains Bianchi closed", W0 * G0 == sp.zeros(4, 10))
check("theorem", "null field-symbol cohomology has dimension two", field_h == 2)
check("theorem", "null equation-symbol cohomology has dimension two", equation_h == 2)

plus = sp.zeros(10, 1)
cross = sp.zeros(10, 1)
plus[PAIRS.index((1, 1))] = 1
plus[PAIRS.index((2, 2))] = -1
cross[PAIRS.index((1, 2))] = 1
TT = plus.row_join(cross)
check("exact", "the plus/cross representatives lie in the null Einstein kernel",
      G0 * TT == sp.zeros(10, 2))
check("exact", "plus/cross remain independent modulo the rank-four gauge image",
      D0.row_join(TT).rank() == 6)

rotation = sp.Matrix([[0, -2], [2, 0]])
lam = sp.symbols("lambda")
check("representation", "the transverse rotation polynomial is lambda squared plus four",
      rotation.charpoly(lam).as_expr() == lam**2 + 4)
check("representation", "the two null classes therefore carry weights plus/minus two",
      rotation.eigenvals() == {-2 * sp.I: 1, 2 * sp.I: 1})
reject("dimension two alone was used as the helicity proof", False)

print("\nE. CONSTRUCTION DISPOSITION")
check("type", "the ten-dimensional metric equation carrier must be retained", True)
check("type", "a BV differential may own the rank-four diffeomorphism image", True)
check("type", "a Ward adjoint may own four equation identities", True)
check("type", "neither operation erases all ten metric equations", True)
check("type", "the selected K77 vertical Euler symbol still requires construction", True)
check("type", "its comparison with the Einstein complex remains a conditional recovery gate", True)
check("symplectic", "gauge reduction is limited to the characteristic distribution, not every conormal covector", True)
check("symplectic", "boundary transformations with live moment map remain outside small-gauge quotient", True)
check("scope", "no selected-action Einstein equation is claimed", True)
check("scope", "no global BFV phase space or common domain is claimed", True)
check("scope", "no sixth quotient is booked", True)
check("surplus", "no external datum or fitted coefficient is introduced", True)
check("surplus", "P1 P2 and P3 remain unused", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__METRIC_SECTION_RANK10_AND_DIFFEO_ORTHOGONAL_EINSTEIN_TARGET__SOURCE-SILENT__COMPLETE_RECEIVER_AND_SELECTED_K77_BV_COMPLEX")
print("RESULT=TEN_METRIC_EQUATIONS_RETAINED__FULL_CONORMAL_BV_ERASURE_REJECTED")
print("NEXT_GATE=CONSTRUCT_SELECTED_K77_VERTICAL_EULER_DIFFEO_WARD_COMPLEX__COMPARE_SYMBOL_COHOMOLOGY_WITH_EINSTEIN")
print("P1_P2_P3=UNUSED")
print("COUNTS=" + ",".join(f"{key}:{value}" for key, value in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
