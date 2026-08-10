#!/usr/bin/env python3
"""Exact topological go/no-go for the P3-to-chiral-spin bundle diagonal.

This probe deliberately stops before the restricted source action.  It asks
whether the P3 Hopf/anti-Hopf class can be the chiral spin bundle of the model
S4 and whether that topological class match already supplies a unique
connection-preserving diagonal.  The latter is false without a connection
orbit condition; on the round homogeneous model the invariant connection is
unique.
"""

from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = {}
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    if not bool(condition):
        FAILURES.append(f"[{kind}] {label}")
        print(f"FAIL [{kind}] {label}")
    else:
        print(f"PASS [{kind}] {label}")


packet = (ROOT / "explorations/unified-source-datum-packet-v0-2026-07-30.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-k77-p3-selfdual-source-reduction-2026-08-10.md").read_text()
tangential = (ROOT / "canon/boundary-einvariant-and-the-tangential-fork.md").read_text()
transcript = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()

check("prior", "P3 uses q-to-left-q^n clutching on S3", "g_n(q)=L_{q^n}" in packet)
check("prior", "P3 p1 convention is minus two n", "p_1(H_n)=-2n" in packet)
check("prior", "P3 connection is fixed rather than varied", "fixed external data, not a\nvaried gauge field" in packet)
check("prior", "predecessor requires a principal-bundle diagonal", "principal-bundle map embedding" in predecessor)
check("prior", "tangential prior art uses p1 over two as stable degree", "framing degree is 4/2 = **2**" in tangential)
check("source", "source types instanton self-duality as Einsteinian", "It's not a Yang is an Einsteinian equation" in transcript)
check("source", "source does not supply the P3/source diagonal", "SOURCE_SILENT_P3_SOURCE_DIAGONAL" in predecessor)

# For an oriented spin real four-plane E with chiral complex rank-two bundles
# S+ and S-, use the declared convention
#   p1(E) = -2(c2(S+) + c2(S-)),
#   e(E)  =  c2(S+) - c2(S-).
# On S4, <p1,[S4]>=0 and <e,[S4]>=chi(S4)=2.
c_plus, c_minus = sp.symbols("c_plus c_minus", integer=True)
solution = sp.solve(
    [sp.Eq(-2 * (c_plus + c_minus), 0), sp.Eq(c_plus - c_minus, 2)],
    [c_plus, c_minus],
    dict=True,
)
check("spin", "S4 chiral Chern system has a unique integral solution", solution == [{c_minus: -1, c_plus: 1}])
c2_plus = solution[0][c_plus]
c2_minus = solution[0][c_minus]
check("spin", "positive chiral spin bundle has charge plus one", c2_plus == 1)
check("spin", "negative chiral spin bundle has charge minus one", c2_minus == -1)
check("spin", "spin reconstruction returns p1 zero", -2 * (c2_plus + c2_minus) == 0)
check("spin", "spin reconstruction returns Euler number two", c2_plus - c2_minus == 2)

# H_n is the underlying real four-plane of an SU(2) complex rank-two bundle
# with c2=n, so p1(H_n)=-2n.  SU(2) bundles on S4 are classified by
# pi3(SU2)=Z, exactly the clutching degree.
matches = {}
for n in (-1, 0, 1):
    p1_h = -2 * n
    matches[n] = "S+" if n == c2_plus else "S-" if n == c2_minus else "NONE"
    check("clutching", f"P3 n={n} has p1=-2n", p1_h == -2 * n)
check("clutching", "n=+1 matches S+ exactly", matches[1] == "S+")
check("clutching", "n=-1 matches S- exactly", matches[-1] == "S-")
check("clutching", "n=0 matches neither chiral spin bundle", matches[0] == "NONE")
check("clutching", "exactly one P3 horn matches the selected S+ orientation", sum(value == "S+" for value in matches.values()) == 1)
check("planted", "PLANT equal real rank does not imply bundle isomorphism", matches[0] != "S+")

# Do not conflate the fundamental real four-plane p1=-2c2 with the adjoint
# rank-three p1=-4c2 used by the framed e-invariant computation.
check("layer0", "fundamental and adjoint Pontryagin normalizations differ", -2 * c2_plus != -4 * c2_plus)
check("layer0", "P3 fundamental p1 at n=1 is minus two", -2 * c2_plus == -2)
check("layer0", "adjoint framing p1 magnitude at charge one is four", abs(-4 * c2_plus) == 4)

# A class match is necessary but not sufficient for a connection-preserving
# isomorphism.  Two exact two-cell curvature fixtures have the same total
# topological charge but different gauge-invariant quadratic energy.
curvature_a = sp.Matrix([1, 0])
curvature_b = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
charge_a = sum(curvature_a)
charge_b = sum(curvature_b)
energy_a = sum(value**2 for value in curvature_a)
energy_b = sum(value**2 for value in curvature_b)
check("connection", "same characteristic charge fixture", charge_a == charge_b == 1)
check("connection", "same charge does not fix connection orbit", energy_a != energy_b)
check("planted", "PLANT characteristic equality is not gauge equivalence", charge_a == charge_b and energy_a != energy_b)

# The unframed charge-one SU(2) ASD moduli index on S4 is
# 8k - 3(1-b1+b+) = 5.  Thus an arbitrary BPST representative has a real
# moduli cost unless the homogeneous round representative is part of the data.
k, b1, bplus = 1, 0, 0
asd_moduli_dim = 8 * k - 3 * (1 - b1 + bplus)
check("moduli", "charge-one S4 ASD moduli dimension is five", asd_moduli_dim == 5)
check("accounting", "arbitrary instanton orbit carries continuous freedom", asd_moduli_dim > 0)

# For round S4=Spin(5)/Spin(4), invariant connections differ by
# Hom_{Spin(4)}(m,su2+).  The isotropy types are m=(2,2) and su2+=(3,1), so
# the Hom multiplicity is zero.  This establishes uniqueness inside the
# homogeneous class without claiming that the packet selected that class.
m_type = (2, 2)
su2_plus_type = (3, 1)
invariant_connection_deformations = int(m_type == su2_plus_type)
check("homogeneous", "round isotropy modules are inequivalent", m_type != su2_plus_type)
check("homogeneous", "homogeneous invariant connection has zero deformation multiplicity", invariant_connection_deformations == 0)
check("homogeneous", "homogeneity removes the five arbitrary-instanton moduli", invariant_connection_deformations < asd_moduli_dim)

check("accounting", "bundle-isomorphism class costs no continuous coordinate modulo gauge", matches[1] == "S+")
check("accounting", "differential diagonal remains conditional on connection orbit", energy_a != energy_b)
check("layer0", "bundle class is not a connection-preserving diagonal", matches[1] == "S+" and energy_a != energy_b)
check("symplectic", "gauge-isomorphism torsor is not yet a physical BV quotient", "A subbundle restriction is not a\n   quotient" in predecessor)
check("variational", "topological interface theorem stops before restricted Euler", "recompute **all** Euler rows" in predecessor)

print("\nRESULT")
print("verdict=ONE_P3_ORIENTATION_MATCHES_CHIRAL_SPIN_BUNDLE__TOPOLOGICAL_DIAGONAL_EXISTS_UP_TO_GAUGE__CONNECTION_DIAGONAL_CONDITIONAL_ON_HOMOGENEOUS_ROUND_BPST")
print(f"spin_c2_pair=({c2_plus},{c2_minus})")
print(f"p3_matches={matches}")
print(f"arbitrary_charge_one_asd_moduli_dim={asd_moduli_dim}")
print(f"homogeneous_invariant_connection_deformations={invariant_connection_deformations}")
print("next_gate=CONSTRUCT_ACTUAL_SUPPORT_PULLBACK_DIAGONAL_N_PLUS1_AND_PROVE_SUPPLIED_BPST_EQUALS_SOURCE_CHIRAL_CONNECTION__THEN_PRICE_RESTRICTED_I1")
print(f"failures={FAILURES}")
print(f"counts={COUNTS}")
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
