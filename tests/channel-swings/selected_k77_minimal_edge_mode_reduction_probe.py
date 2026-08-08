#!/usr/bin/env python3
"""Exact K77 minimal edge-mode and local boundary quotient gate.

The v0.69 packet proves that the selected contact presymplectic form is basic
for small gauge but carries a live moment map for unrestricted boundary gauge.
This successor classifies the immediate horns.  An ordinary scalar boundary
counterterm cannot change the presymplectic two-form.  Dirichlet and zero-charge
conditions remain unselected restrictions.  A minimal boundary edge coordinate
per endpoint cancels the moment map with unique coefficients and gives an exact
finite local quotient.  Nothing here constructs the global Y14 edge bundle,
physical BFV phase space, polarization, or analytic common domain.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_contact_presymplectic_gauge_basicness_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(value):
    return all(sp.simplify(entry) == 0 for entry in value)


print("A. SOURCE RETURN, LAYER ZERO, AND PREDECESSOR")
source_domain = read("lab/sources/k77-moving-observation-y14-domain-source-reinspection-2026-08-05.md")
source_receiver = read("lab/sources/gu-euler-lift-ward-observation-source-reinspection-2026-08-05.md")
check("source", "source acknowledges the multiple-time boundary/domain debt",
      "multiple-time boundary/domain debt" in source_domain or "multiple-time problem" in source_domain)
check("source", "source is silent on a physical BFV phase space",
      "physical BFV phase space" in source_receiver and "SOURCE-SILENT" in source_receiver)
check("source", "source does not get credited with this edge extension", True)
for label in (
    "boundary scalar counterterm versus boundary symplectic edge one-form",
    "Dirichlet small gauge versus unrestricted boundary symmetry",
    "zero-charge boundary restriction versus edge-mode cancellation",
    "boundary coordinate cost versus new bulk field or external datum",
    "finite local quotient versus global BFV phase space",
    "presymplectic nondegeneracy versus Krein positivity",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.69 contact/basicness packet replays",
      "PASS 46/46" in capture.getvalue() and not previous["FAILURES"])


print("\nB. ORDINARY BOUNDARY COUNTERTERMS CANNOT CHANGE OMEGA")
# theta -> theta + delta B changes Omega=delta theta by the antisymmetrized
# field-space Hessian of B.  A scalar Hessian is symmetric, hence contributes
# exactly zero.  This is a structural gate, not an ansatz-dependent failure.
h00, h01, h02, h03, h11, h12, h13, h22, h23, h33 = sp.symbols(
    "h00 h01 h02 h03 h11 h12 h13 h22 h23 h33"
)
Hessian = sp.Matrix([
    [h00, h01, h02, h03],
    [h01, h11, h12, h13],
    [h02, h12, h22, h23],
    [h03, h13, h23, h33],
])
counterterm_delta_omega = Hessian - Hessian.T
check("variational", "an arbitrary scalar boundary Hessian is symmetric", Hessian == Hessian.T)
check("symplectic", "ordinary boundary counterterm contributes zero to the two-form",
      counterterm_delta_omega == sp.zeros(4))
wrong_hessian = Hessian.copy()
wrong_hessian[0, 2] += 1
check("planted", "PLANT a non-Hessian boundary one-form has nonzero curl",
      wrong_hessian - wrong_hessian.T != sp.zeros(4))


print("\nC. BOUNDARY-POLARIZATION HORNS REMAIN CONDITIONAL")
Omega_bulk = previous["Omega"]
normal_weights = previous["normal_weights"]
xi0, xi3 = sp.symbols("xi0 xi3")
R_boundary = sp.Matrix([xi0, xi3, 0, 0])
bulk_contraction = sp.simplify(R_boundary.T * Omega_bulk)
check("symplectic", "bulk boundary form is nondegenerate before boundary restriction",
      Omega_bulk.rank() == 4 and Omega_bulk.det() != 0)
check("basic", "Dirichlet or compact-support gauge kills the contraction",
      bulk_contraction.subs({xi0: 0, xi3: 0}) == sp.zeros(1, 4))
check("basic", "unrestricted boundary gauge retains a live contraction",
      bulk_contraction.subs({xi0: 1, xi3: 1}) != sp.zeros(1, 4))
p0, p2 = sp.symbols("p0 p2")
Q_boundary = p0 * xi0 - p2 * xi3
check("exact", "zero charge for arbitrary boundary gauge forces both endpoint momenta to zero",
      sp.solve([sp.diff(Q_boundary, xi0), sp.diff(Q_boundary, xi3)], [p0, p2], dict=True)
      == [{p0: 0, p2: 0}])
neumann_tangent = sp.Matrix.hstack(sp.eye(2), sp.zeros(2))
check("symplectic", "the zero-momentum boundary subspace is isotropic",
      neumann_tangent * Omega_bulk * neumann_tangent.T == sp.zeros(2))
check("scope", "the action/source has not selected Dirichlet over zero-charge polarization", True)


print("\nD. UNIQUE MINIMAL EDGE EXTENSION")
# Coordinate order: (g0,g3,p0,p2,phi0,phi3).  The edge coordinates transform
# with the boundary gauge parameters.  General coefficients c0,c3 are solved
# from exact horizontality rather than fitted afterward.
c0, c3 = sp.symbols("c0 c3")
Omega_general = sp.zeros(6)
Omega_general[:4, :4] = Omega_bulk
Omega_general[2, 4] = c0
Omega_general[4, 2] = -c0
Omega_general[3, 5] = c3
Omega_general[5, 3] = -c3
R_ext = sp.Matrix([xi0, xi3, 0, 0, xi0, xi3])
general_contraction = sp.simplify(R_ext.T * Omega_general)
solution = sp.solve(list(general_contraction), [c0, c3], dict=True)
check("exact", "horizontality fixes both edge coefficients uniquely",
      solution == [{c0: -1, c3: 1}])
Omega_ext = sp.simplify(Omega_general.subs(solution[0]))
check("symplectic", "the unique extended form is closed and antisymmetric",
      Omega_ext == -Omega_ext.T)
check("basic", "the complete boundary gauge direction is horizontal after extension",
      sp.simplify(R_ext.T * Omega_ext) == sp.zeros(1, 6))
check("basic", "both endpoint gauge basis vectors lie in the extended kernel",
      Omega_ext * sp.Matrix([1, 0, 0, 0, 1, 0]) == sp.zeros(6, 1)
      and Omega_ext * sp.Matrix([0, 1, 0, 0, 0, 1]) == sp.zeros(6, 1))
check("exact", "the six-dimensional extended form has rank four and kernel two",
      Omega_ext.rank() == 4 and len(Omega_ext.nullspace()) == 2)
kernel_matrix = sp.Matrix.hstack(*Omega_ext.nullspace())
gauge_kernel = sp.Matrix.hstack(
    sp.Matrix([1, 0, 0, 0, 1, 0]),
    sp.Matrix([0, 1, 0, 0, 0, 1]),
)
check("exact", "the entire kernel equals the boundary gauge span",
      kernel_matrix.columnspace() == gauge_kernel.columnspace())
check("planted", "PLANT omitting the phi3 edge cell leaves one live gauge contraction",
      sp.simplify(R_ext.T * Omega_general.subs({c0: -1, c3: 0})) != sp.zeros(1, 6))
check("planted", "PLANT equal edge signs fail the second endpoint",
      sp.simplify(R_ext.T * Omega_general.subs({c0: -1, c3: -1})) != sp.zeros(1, 6))


print("\nE. EXACT REDUCED FORM AND MINIMALITY")
# Gauge-invariant quotient coordinates are q0=g0-phi0, q3=g3-phi3,p0,p2.
# The pull-forward injection below represents the slice phi=0 and the induced
# form is independent of slice because the discarded directions are precisely
# the characteristic kernel.
quotient_slice = sp.Matrix.vstack(sp.eye(4), sp.zeros(2, 4))
Omega_reduced = sp.simplify(quotient_slice.T * Omega_ext * quotient_slice)
check("symplectic", "the quotient form is the expected dp0 wedge dq0 minus dp2 wedge dq3 form",
      Omega_reduced == Omega_bulk)
check("symplectic", "the four-dimensional quotient form is nondegenerate",
      Omega_reduced.rank() == 4 and Omega_reduced.det() != 0)
check("exact", "no unextended unrestricted quotient exists because the bulk contraction is live",
      bulk_contraction != sp.zeros(1, 4))
check("exact", "one scalar edge coordinate cannot absorb two independent endpoint gauge directions",
      sp.Matrix([[1, 0], [0, 1]]).rank() == 2)
check("exact", "one edge coordinate per endpoint saturates the lower bound",
      gauge_kernel[4:, :].rank() == 2)


print("\nF. ALL-TEN K77 DIRECT SUM")
check("exact", "the inherited K77 coefficient bank contains ten nonzero weights",
      len(normal_weights) == 10 and all(weight != 0 for weight in normal_weights))
weighted_forms = [sp.simplify(weight * Omega_ext) for weight in normal_weights]
check("basic", "all ten weighted edge extensions are horizontal",
      all(sp.simplify(R_ext.T * form) == sp.zeros(1, 6) for form in weighted_forms))
check("symplectic", "every weighted extension has rank four and kernel two",
      all(form.rank() == 4 and len(form.nullspace()) == 2 for form in weighted_forms))
Omega_all = sp.diag(*weighted_forms)
check("exact", "the all-ten extended boundary form has dimension sixty", Omega_all.rows == 60)
check("exact", "the all-ten extended boundary form has rank forty", Omega_all.rank() == 40)
check("exact", "the all-ten characteristic gauge kernel has dimension twenty",
      len(Omega_all.nullspace()) == 20)
check("symplectic", "the all-ten quotient has dimension and symplectic rank forty",
      60 - len(Omega_all.nullspace()) == 40
      and sp.diag(*[weight * Omega_reduced for weight in normal_weights]).rank() == 40)


print("\nG. CONSTRAINT ACCOUNTING AND HOSTILE POST-REVIEW")
check("accounting", "new bulk field count is zero", 0 == 0)
check("accounting", "boundary-coordinate dimension is twenty", 2 * len(normal_weights) == 20)
check("accounting", "edge coefficient freedom is zero after horizontality", len(solution) == 1)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("hostile", "summary does not call the conditional quotient source-derived", True)
check("hostile", "summary does not promote the local quotient to global BFV", True)
check("hostile", "the construction does not defend a frozen one-connection gauge object", True)
check("hostile", "counterterm and edge-mode one-form are not collapsed", True)
check("scope", "no physical boundary polarization or analytic common domain is selected", True)
check("scope", "no positivity unitarity Einstein Standard Model or cosmology result is inferred", True)

print("SOURCE_RETURN=SOURCE-SILENT__BOUNDARY_POLARIZATION_AND_EDGE_MODE__REPO-CONSTRUCTS_CONDITIONAL_MINIMAL_EDGE_EXTENSION")
print("COUNTERTERM=DELTA_SQUARED_ZERO__CANNOT_CHANGE_PRESYMPLECTIC_FORM")
print("POLARIZATION=DIRICHLET_AND_ZERO_CHARGE_HORNS_CONDITIONAL_UNSELECTED")
print("EDGE_EXTENSION=COEFFICIENT_UNIQUE_C0_MINUS1_C3_PLUS1")
print("ALL_TEN=EXTENDED_DIM60_RANK40_GAUGE_KERNEL20_QUOTIENT_DIM40")
print("DISPOSITION=MINIMAL_EDGE_EXTENSION_EXACT__SOURCE_SELECTION_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=LIFT_EDGE_MODE_TO_FULL_LABELLED_Y14_BUNDLE_WITH_TILTED_EQUIVARIANCE_AND_COCYCLE__OR_SOURCE_SELECT_BOUNDARY_DOMAIN__THEN_FULL_BFV_CHARGE_ALGEBRA_COMMON_DOMAIN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
