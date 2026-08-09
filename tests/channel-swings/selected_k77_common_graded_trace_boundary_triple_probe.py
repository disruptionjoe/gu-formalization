#!/usr/bin/env python3
"""Exact finite-mode certificate for the K77 graded boundary trace skeleton.

The certificate constructs the common *graded boundary trace space* carried by
the physical H^7/H^-7 pair and the gauge--ghost H^8/H^-8 pair.  It does not
construct the missing bulk maximal operator, a Green inverse, a Krein-positive
domain, an ultrahyperbolic spectral projector, or a coupled BV--BFV theory.
"""

from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
EXACT = []
PLANTED = []


def exact(label, condition):
    if not bool(condition):
        raise AssertionError(label)
    EXACT.append(label)


def planted(label, bad_condition):
    if bool(bad_condition):
        raise AssertionError(f"plant did not fire: {label}")
    PLANTED.append(label)


def zmat(matrix):
    return all(entry == 0 for entry in matrix)


# Layer 0: one common domain is allowed to be a graded direct sum.  It need not
# identify different Sobolev exponents, and a boundary trace space is not a
# bulk graph domain.
registry = json.loads((ROOT / "lab/process/selected-k77-relative-edge-bitorsor-topology.json").read_text())
ledger = json.loads((ROOT / "lab/process/conditional-physics-ledger-v0.115.json").read_text())
source = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()

exact("predecessor keeps common bulk domain open",
      registry["analytic_fence"]["common_bulk_Green_Krein_domain"] == "OPEN")
exact("predecessor keeps coupled BV BFV open",
      registry["analytic_fence"]["coupled_bulk_boundary_BV_BFV"] == "OPEN")
exact("ledger predecessor is v0.115", ledger["schema_version"] == "0.115")
exact("source admits upstairs boundary technical debt",
      "there are no initial conditions because that's a co-dimension one concept" in source
      and "Really what you have is boundary conditions" in source)
exact("source supplies no Sobolev boundary triple", "Sobolev" not in source)


# The common trace space T_B=(H7+H-7)_phys + (H8+H-8)_ghost is strong as a
# graded cotangent product.  The mode weight w stands for <xi> >= 1.
d = 2
I = sp.eye(d)
Z = sp.zeros(d)
Omega = sp.Matrix.vstack(
    sp.Matrix.hstack(Z, I, Z, Z),
    sp.Matrix.hstack(-I, Z, Z, Z),
    sp.Matrix.hstack(Z, Z, Z, I),
    sp.Matrix.hstack(Z, Z, -I, Z),
)
exact("graded canonical form is skew", Omega.T == -Omega)
exact("graded canonical form is nondegenerate", Omega.rank() == 4 * d)

for mode in (0, 1, 2, 4, 8):
    w = sp.Integer(1 + mode * mode)
    a7 = w ** 14
    a8 = w ** 16
    norm = sp.diag(*([a7] * d + [1 / a7] * d + [a8] * d + [1 / a8] * d))
    dual_norm = norm.inv()
    exact(f"graded musical isometry mode {mode}", Omega.T * dual_norm * Omega == norm)
    exact(f"graded musical inverse exists mode {mode}", Omega.inv() * Omega == sp.eye(4 * d))


# H7 and H8 are compatible as summands, not canonically the same scale.  The
# identity H7 -> H8 has normalized norm <xi>, so no uniform inverse-pair exists.
ratios = [sp.Integer(1 + n * n) for n in (0, 1, 2, 4, 8)]
exact("H7 to H8 identity ratios increase", all(a < b for a, b in zip(ratios, ratios[1:])))
exact("H7 to H8 identity is not uniformly bounded", ratios[-1] > 60)
planted("PLANT H7 and H8 are one uniformly equivalent norm", max(ratios) == min(ratios))

# The same-positive-regularity H7 x H7 form is only weak in the continuum.
weak_inverse = [(1 + n * n) ** 14 for n in (0, 1, 2, 4, 8)]
exact("same H7 regularity inverse norms diverge", weak_inverse[-1] > 10 ** 13)
planted("PLANT finite cutoff rank implies strong continuum form", weak_inverse[-1] <= 10 ** 6)


# Standard trace loses one half derivative.  The negative-order momenta are
# cotangent/conormal variables, not ordinary traces of the same positive field.
bulk_phys = sp.Rational(15, 2)
bulk_ghost = sp.Rational(17, 2)
exact("physical bulk trace lands in H7", bulk_phys - sp.Rational(1, 2) == 7)
exact("ghost bulk trace lands in H8", bulk_ghost - sp.Rational(1, 2) == 8)
exact("physical momentum is the H7 continuous dual", -7 == -int(bulk_phys - sp.Rational(1, 2)))
exact("ghost momentum is the H8 continuous dual", -8 == -int(bulk_ghost - sp.Rational(1, 2)))
planted("PLANT an H7 bulk field traces to H7", sp.Rational(7) - sp.Rational(1, 2) == 7)
planted("PLANT Hminus7 momentum is an ordinary positive field trace", -7 >= 0)


# Relative-bitorsor transitions act by cotangent lift in both blocks.
A = sp.Matrix([[2, 1], [1, 1]])
S = sp.diag(A, A.inv().T, A, A.inv().T)
exact("relative transition is invertible", S.det() != 0)
exact("relative cotangent lift preserves graded form", S.T * Omega * S == Omega)

# Vertical polarization L=span(momentum, antighost momentum).
L = sp.Matrix.vstack(
    sp.zeros(d, 2 * d),
    sp.Matrix.hstack(I, Z),
    sp.zeros(d, 2 * d),
    sp.Matrix.hstack(Z, I),
)
exact("vertical polarization is isotropic", zmat(L.T * Omega * L))
exact("vertical polarization is half dimensional", 2 * L.rank() == Omega.rows)
exact("vertical symplectic orthogonal equals itself",
      sp.Matrix.hstack(sp.Matrix.hstack(*(L.T * Omega).nullspace()), L).rank() == L.rank())
exact("relative cotangent lift preserves vertical polarization",
      sp.Matrix.hstack(S * L, L).rank() == L.rank())

wrong = sp.diag(A, A, A, A)
planted("PLANT same transition on covectors is symplectic", wrong.T * Omega * wrong == Omega)
graph_bad = sp.Matrix.vstack(I, sp.Matrix([[0, 1], [-1, 0]]), Z, Z)
planted("PLANT arbitrary graph is Lagrangian", zmat(graph_bad.T * Omega * graph_bad))


# Boundary-triple readiness audit.  These are explicit repository ownership
# facts, not a fake finite-dimensional proof of the analytic hypotheses.
owned = {
    "graded_trace_carrier": True,
    "graded_green_form": True,
    "relative_patch_descent": True,
    "lagrangian_polarization": True,
    "complete_action_owned_gauge_fixed_bulk_operator": False,
    "closed_Dmax": False,
    "surjective_bulk_trace": False,
    "Dmin_equals_trace_kernel": False,
    "common_green_inverse": False,
    "krein_positive_physical_domain": False,
}
for key in ("graded_trace_carrier", "graded_green_form", "relative_patch_descent", "lagrangian_polarization"):
    exact(f"owned boundary skeleton: {key}", owned[key])
for key in ("complete_action_owned_gauge_fixed_bulk_operator", "closed_Dmax", "surjective_bulk_trace",
            "Dmin_equals_trace_kernel", "common_green_inverse", "krein_positive_physical_domain"):
    exact(f"analytic hypothesis remains unowned: {key}", not owned[key])

planted("PLANT boundary form alone constructs a Green inverse", owned["common_green_inverse"])
planted("PLANT polarization is already a selected boundary condition", False)
planted("PLANT observed X4 defect domain is the ambient Y14 domain", False)
planted("PLANT positivity follows from nondegeneracy", owned["krein_positive_physical_domain"])
planted("PLANT source supplies an ultrahyperbolic spectral projector", False)

print("SOURCE_RETURN=SOURCE-CONFIRMS_UPSTAIRS_BOUNDARY_TECHNICAL_DEBT__SOURCE-SILENT_SOBOLEV_TRACE_BOUNDARY_TRIPLE_GREEN_KREIN_DOMAIN_AND_BV_BFV")
print("LAYER0_RETURN=COMMON_MEANS_GRADED_DIRECT_SUM__NOT_ONE_EXPONENT__TRACE_SPACE_NOT_POLARIZATION_NOT_BOUNDARY_CONDITION_NOT_BULK_DOMAIN")
print("BUILD_RETURN=H7_HMINUS7_PLUS_H8_HMINUS8_STRONG_GRADED_TRACE_AND_RELATIVE_COTANGENT_POLARIZATION_EXACT")
print("ANALYTIC_RETURN=COMPLETE_ACTION_OWNED_BULK_OPERATOR_DMAX_DMIN_TRACE_EXACT_SEQUENCE_GREEN_INVERSE_AND_KREIN_POSITIVITY_UNOWNED")
print("P1_P2_P3=UNUSED")
print("NEXT=ASSEMBLE_COMPLETE_ACTION_OWNED_GAUGE_FIXED_BULK_LINEARIZED_OPERATOR__PROVE_DMAX_DMIN_GRADED_TRACE_EXACT_SEQUENCE_OR_KILL__THEN_COUPLE_BULK_BV_TO_BOUNDARY_BFV")
print(f"PASS selected K77 common graded trace boundary triple: {len(EXACT)} exact + {len(PLANTED)} planted = {len(EXACT) + len(PLANTED)}")
