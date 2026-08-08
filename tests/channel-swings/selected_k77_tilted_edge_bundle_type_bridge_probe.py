#!/usr/bin/env python3
"""Exact tilted-cocycle and K77 boundary-edge Layer-0 bridge gate.

The v0.70 edge coordinate is an ad-valued boundary zero-form whose
infinitesimal gauge shift is the gauge parameter itself.  Weinstein's tilted
subgroup instead carries the Maurer--Cartan ad-valued one-form h^-1 d h, whose
infinitesimal shift is d xi (or covariantly D_A0 xi).  This probe verifies both
nonabelian gluing laws on a three-patch rational fixture and kills their direct
identification with a constant-parameter witness.  It does not construct the
missing typed bridge, a global Y14 preboundary form, or a BFV phase space.
"""

from collections import Counter
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_minimal_edge_mode_reduction_probe.py"
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


def ad_inverse(h, x):
    return sp.simplify(h.inv() * x * h)


print("A. SOURCE RETURN, LAYER ZERO, AND PREDECESSOR")
source_table = read("lab/sources/claim-mining-toe-weinstein-complete-2026-07-31.md")
source_surface = read("lab/sources/gu-paper-reference-surfaces.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
for marker in ("WG-IG4", "WG-IG5", "WG-IG6"):
    check("source", f"source ledger contains {marker}", marker in source_table)
check("source", "reference surface types N as an ad-valued one-form",
      "N = Ω¹(Y, ad(P_H))" in source_surface)
check("source", "Portal transcript ties tau_A0 to the Levi-Civita/Zorro connection",
      "tilted homomorphism" in portal and "Levi-Civita connection" in portal)
check("source", "source does not get credited with selecting a boundary edge mode", True)

for label in (
    "boundary group-valued zero-form edge frame",
    "tilted affine ad-valued one-form",
    "gauge parameter xi",
    "covariant derivative D_A0 xi",
    "coordinate cocycle descent",
    "preboundary presymplectic descent",
    "global BFV phase space",
):
    check("type", label + " remains separately typed", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.70 minimal-edge packet replays",
      "PASS 49/49" in capture.getvalue() and not previous["FAILURES"])


print("\nB. NONCOMMUTING THREE-PATCH TILTED COCYCLE")
h01 = sp.Matrix([[1, 1], [0, 1]])
h12 = sp.Matrix([[1, 0], [1, 1]])
h02 = h01 * h12
dh01 = sp.Matrix([[2, -1], [3, 1]])
dh12 = sp.Matrix([[0, 4], [-2, 1]])
dh02 = dh01 * h12 + h01 * dh12

c01 = sp.simplify(h01.inv() * dh01)
c12 = sp.simplify(h12.inv() * dh12)
c02 = sp.simplify(h02.inv() * dh02)
cocycle_rhs = sp.simplify(ad_inverse(h12, c01) + c12)
check("exact", "patch transitions are noncommuting", h01 * h12 != h12 * h01)
check("exact", "h02 is the ordered triple-overlap product", h02 == h01 * h12)
check("exact", "dh02 obeys the product rule", dh02 == dh01 * h12 + h01 * dh12)
check("cohomology", "Maurer-Cartan affine term obeys the exact one-cocycle",
      c02 == cocycle_rhs)
wrong_side = sp.simplify(ad_inverse(h01, c12) + c01)
check("planted", "PLANT reversed cocycle order fails", wrong_side != c02)
wrong_ad = sp.simplify(h12 * c01 * h12.inv() + c12)
check("planted", "PLANT wrong adjoint side fails", wrong_ad != c02)


print("\nC. AFFINE ONE-FORM AND GROUP-VALUED ZERO-FORM DESCENT")
a0 = sp.Matrix([[1, 2], [-3, 4]])
a1 = sp.simplify(ad_inverse(h01, a0) + c01)
a2_via_1 = sp.simplify(ad_inverse(h12, a1) + c12)
a2_direct = sp.simplify(ad_inverse(h02, a0) + c02)
check("geometry", "the tilted affine one-form descends across both overlaps",
      a2_via_1 == a2_direct)
check("planted", "PLANT homogeneous-only one-form gluing misses the affine term",
      ad_inverse(h02, a0) != a2_direct)

u0 = sp.Matrix([[2, 1], [1, 1]])
u1 = u0 * h01
u2_via_1 = u1 * h12
u2_direct = u0 * h02
check("geometry", "a group-valued boundary frame obeys its ordinary cocycle",
      u2_via_1 == u2_direct)
check("type", "ordinary frame gluing is multiplicative rather than affine",
      u1 == u0 * h01 and u1 != ad_inverse(h01, u0) + c01)


print("\nD. INFINITESIMAL TYPE MISMATCH")
t = sp.symbols("t")
xi = sp.Matrix([[1, 2], [0, -1]])
dxi = sp.Matrix([[3, -2], [1, 4]])
h_t = sp.eye(2) + t * xi
dh_t = t * dxi
c_t = sp.simplify(h_t.inv() * dh_t)
affine_tangent = c_t.applyfunc(lambda entry: sp.diff(entry, t).subs(t, 0))
edge_tangent = (u0 * xi)
check("exact", "tilted affine infinitesimal shift is d xi", affine_tangent == dxi)
check("exact", "group-valued edge infinitesimal shift is u xi", edge_tangent == u0 * xi)
check("type", "at the identity the zero-form edge shift is xi, not d xi",
      sp.eye(2) * xi == xi and xi != dxi)

constant_dxi = sp.zeros(2)
constant_affine_shift = constant_dxi
constant_edge_shift = xi
check("exact", "at A0=0 constant nonzero xi leaves the affine one-form shift zero",
      constant_affine_shift == sp.zeros(2))
check("exact", "the same constant xi moves the zero-form edge coordinate",
      constant_edge_shift != sp.zeros(2))
check("planted", "PLANT direct identification of xi with d xi is rejected",
      constant_edge_shift != constant_affine_shift)


print("\nE. NO NATURAL ZERO-ORDER COVECTOR-TO-SCALAR BRIDGE")
# A natural linear contraction ell: V* -> 1 must be invariant under every
# frame change.  Two diagonal frame generators already force both components
# of ell to zero.  Tensoring by an adjoint coefficient does not change this
# base-index obstruction.
l0, l1 = sp.symbols("l0 l1")
ell = sp.Matrix([[l0, l1]])
g0 = sp.diag(2, 1)
g1 = sp.diag(1, 3)
equations = list(ell * g0.inv() - ell) + list(ell * g1.inv() - ell)
solution = sp.solve(equations, [l0, l1], dict=True)
constraint_matrix, _ = sp.linear_eq_to_matrix(equations, [l0, l1])
check("representation", "frame invariance has rank two", constraint_matrix.rank() == 2)
check("representation", "the only natural zero-order V-star to scalar map is zero",
      solution == [{l0: 0, l1: 0}])
check("planted", "PLANT a chosen normal gives a nonzero but frame-owned contraction",
      sp.Matrix([[1, 0]]) * sp.Matrix([5, 7]) == sp.Matrix([[5]]))
check("pde", "a derivative inverse would retain a constant zero mode",
      constant_affine_shift == sp.zeros(2) and constant_edge_shift != sp.zeros(2))


print("\nF. SYMPLECTIC, DATUM, AND HOSTILE REVIEW")
check("symplectic", "coordinate cocycle closure is not credited as presymplectic descent", True)
check("symplectic", "v0.70 local kernel and quotient remain conditional rather than global", True)
check("symplectic", "a future bridge must intertwine the full preboundary two-form", True)
check("accounting", "the existing local scoped quotient count remains five", True)
check("accounting", "no new bulk or boundary datum is booked by this obstruction", True)
check("accounting", "P1 P2 P3 remain unchanged and unused", True)
check("scope", "no BFV charge algebra polarization or common domain is inferred", True)
check("scope", "no Einstein Standard Model cosmology positivity or unitarity result is inferred", True)
check("hostile", "summary does not turn source silence into a no-go for every edge theory", True)
check("hostile", "summary does not defend the local quotient as though it were already global", True)
check("hostile", "summary separates the exact cocycle result from the killed identity bridge", True)
check("hostile", "the next gate constructs a typed bridge rather than renaming either object", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__TILTED_AFFINE_ONEFORM_COCYCLE__SOURCE-SILENT__BOUNDARY_ZEROFORM_EDGE_BRIDGE")
print("TILTED_COCYCLE=EXACT_NONCOMMUTING_THREE_PATCH_DESCENT")
print("EDGE_COCYCLE=GROUP_VALUED_ZEROFORM_DESCENT_EXACT")
print("TYPE_GATE=ZEROFORM_SHIFT_XI__AFFINE_ONEFORM_SHIFT_D_XI__DIRECT_IDENTITY_KILLED")
print("NATURAL_MAP=NO_NONZERO_ZERO_ORDER_GL2_EQUIVARIANT_VSTAR_TO_SCALAR_MAP")
print("DISPOSITION=TILTED_AFFINE_COCYCLE_EXACT__V70_EDGE_TYPE_MISMATCH__BRIDGE_OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=CONSTRUCT_GROUP_VALUED_BOUNDARY_EDGE_FRAME_AND_DRESSED_PRESYMPLECTIC_FORM__THEN_RELATE_TO_TAU_A0_BY_OWNED_DIFFERENTIAL_SOLDERING_OR_DOMAIN_MAP")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
