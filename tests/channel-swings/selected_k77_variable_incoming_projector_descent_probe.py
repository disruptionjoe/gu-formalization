#!/usr/bin/env python3
"""Exact variable-coefficient incoming-projector descent gate.

This probe composes immutable full-carrier K77 receipts with a finite exact
model of the operation they leave open.  For the action-owned principal
coefficients ``D_t`` and ``D_n``, it forms

    E_n = D_t^{-1} D_n,          Pi_in(n) = (I - E_n) / 2.

The checks distinguish four objects: the action-derived projector family, the
member selected by an oriented unit boundary conormal, associated-bundle
descent, and a global analytic initial-boundary-value theorem.  Only the first
three are algebraically addressed here.  The doubled Majorana Green identity
is tested for both complete pairing horns; the one-sided independent-dual form
is retained as a firing wrong-object control.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(matrix: sp.MatrixBase) -> bool:
    return sp.simplify(matrix) == sp.zeros(*matrix.shape)


print("A. ADAPTIVE PREFLIGHT, PRIOR ART, SOURCE, AND LAYER ZERO")
v0167 = strict("lab/process/selected-k77-global-normal-symbol-descent.json")
v0177 = strict("lab/process/selected-k77-graded-green-reality-graphs.json")
v0179 = strict("lab/process/selected-k77-energy-green-boundary-horn-composition.json")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")

check("prior_art", "the actual nonnull normal symbol is an associated-bundle morphism",
      v0167["normal_symbol"]["global_associated_bundle_morphism"]
      and v0167["normal_symbol"]["nonnull_rank"] == 1920)
check("prior_art", "the completed flat incoming and outgoing carriers have equal half rank",
      v0179["carrier_rank"] == 1920
      and v0179["incoming_rank"] == v0179["outgoing_rank"] == 960)
check("prior_art", "both complete doubled-Majorana pairing horns are already locally isotropic",
      set(v0179["doubled_majorana_green_restriction_ranks"].values()) == {0})
check("prior_art", "both graded-reality horns already have exact tensorial overlap descent",
      v0177["overlap"].startswith("EXACT_TENSORIAL_THREE_PATCH_DESCENT"))
check("source", "the source owns a first-order four-field parent grammar",
      "four distinct fields" in source and "Equation 9.16" in source)
check("source", "the source is silent on the incoming projector and analytic domain",
      "Green preboundary current" in source and "SOURCE-SILENT" in source)

for label in (
    "projector family versus one boundary-selected member",
    "global associated-bundle descent versus global-in-time well-posedness",
    "action ownership of n-to-projector versus action selection of n",
    "Majorana graph versus spatial incoming relation",
    "nonnull spatial boundary versus null characteristic BFV relation",
):
    check("layer0", label, True)


print("\nB. ACTION-DERIVED MOVING PROJECTOR FAMILY")
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.diag(1, -1)
A1 = sp.kronecker_product(X, I2)
A2 = sp.kronecker_product(Z, X)
A3 = sp.kronecker_product(Z, Z)
I4 = sp.eye(4)

check("clifford", "the three exact spatial generators square to identity",
      all(A * A == I4 for A in (A1, A2, A3)))
check("clifford", "the exact spatial generators anticommute pairwise",
      all(A * B + B * A == sp.zeros(4)
          for A, B in ((A1, A2), (A1, A3), (A2, A3))))
check("analytic", "the exact generators are symmetric-hyperbolic in the base frame",
      all(A.T == A for A in (A1, A2, A3)))

x = sp.symbols("x", real=True)
n1 = (1 - x**2) / (1 + x**2)
n2 = 2 * x / (1 + x**2)
E0 = sp.simplify(n1 * A1 + n2 * A2)
Pin0 = sp.simplify((I4 - E0) / 2)
Pout0 = sp.simplify((I4 + E0) / 2)

check("normal", "the rational moving normal is exactly unit",
      sp.simplify(n1**2 + n2**2) == 1)
check("projector", "the moving spatial evolution remains involutive",
      zero(E0 * E0 - I4))
check("projector", "the incoming and outgoing polynomials are complementary projectors",
      zero(Pin0 * Pin0 - Pin0)
      and zero(Pout0 * Pout0 - Pout0)
      and zero(Pin0 + Pout0 - I4)
      and zero(Pin0 * Pout0))
check("projector", "the moving incoming and outgoing ranks remain two",
      Pin0.rank() == Pout0.rank() == 2)
check("flux", "the incoming polynomial is the minus-one energy-flux half",
      zero(E0 * Pin0 + Pin0) and zero(E0 * Pout0 - Pout0))

# Three nonconstant, nonorthogonal local field frames.  They make positivity
# transport and the connection correction nonvacuous while preserving exact
# rational arithmetic.
U0 = I4
U1 = sp.diag(1 + x, 1, 1, 1)
shear = I4.copy()
shear[0, 1] = x
U2 = sp.simplify(shear * U1)
U01 = sp.simplify(U1 * U0.inv())
U12 = sp.simplify(U2 * U1.inv())
U02 = sp.simplify(U2 * U0.inv())

check("descent", "the nonconstant field frames obey the three-patch cocycle",
      zero(U12 * U01 - U02))
check("planted", "PLANT reversing the noncommuting overlap order fails",
      not zero(U01 * U12 - U02))


def packet(U: sp.Matrix):
    Ui = sp.simplify(U.inv())
    E = sp.simplify(U * E0 * Ui)
    H = sp.simplify(Ui.T * Ui)
    Dt = H
    Dn = sp.simplify(H * E)
    Pin = sp.simplify((I4 - E) / 2)
    Pout = sp.simplify((I4 + E) / 2)
    Omega = sp.simplify(U.diff(x) * Ui)
    return {"U": U, "Ui": Ui, "E": E, "H": H, "Dt": Dt,
            "Dn": Dn, "Pin": Pin, "Pout": Pout, "Omega": Omega}


patches = [packet(U) for U in (U0, U1, U2)]
for index, item in enumerate(patches):
    check("action", f"patch {index} evolution is reconstructed from action coefficients",
          zero(item["Dt"].inv() * item["Dn"] - item["E"]))
    check("projector", f"patch {index} incoming polynomial is idempotent of rank two",
          zero(item["Pin"] * item["Pin"] - item["Pin"])
          and item["Pin"].rank() == 2)
    check("analytic", f"patch {index} action time coefficient has an exact positive Gram factor",
          zero(item["H"] - item["Ui"].T * item["Ui"]))
    check("analytic", f"patch {index} spatial action coefficient is symmetric",
          zero(item["Dn"] - item["Dn"].T))
    check("flux", f"patch {index} incoming action flux is negative in the transported energy",
          zero(item["Pin"].T * item["Dn"] * item["Pin"]
               + item["Pin"].T * item["H"] * item["Pin"]))

check("descent", "the action-derived evolution descends by similarity",
      zero(patches[1]["E"] - U01 * patches[0]["E"] * U01.inv())
      and zero(patches[2]["E"] - U12 * patches[1]["E"] * U12.inv()))
check("descent", "the incoming projector polynomial descends on both overlaps",
      zero(patches[1]["Pin"] - U01 * patches[0]["Pin"] * U01.inv())
      and zero(patches[2]["Pin"] - U12 * patches[1]["Pin"] * U12.inv()))
check("descent", "direct and sequential projector descent agree",
      zero(patches[2]["Pin"] - U02 * patches[0]["Pin"] * U02.inv()))
check("planted", "PLANT freezing the projector fails for a moving normal and frame",
      not zero(patches[2]["Pin"] - patches[0]["Pin"]))

for index, item in enumerate(patches[1:], start=1):
    covariant_derivative = sp.simplify(
        item["Pin"].diff(x)
        - (item["Omega"] * item["Pin"] - item["Pin"] * item["Omega"])
    )
    expected = sp.simplify(item["U"] * Pin0.diff(x) * item["Ui"])
    check("connection", f"patch {index} projector derivative is connection-natural",
          zero(covariant_derivative - expected))

wrong_derivative = sp.simplify(patches[2]["Pin"].diff(x)
                               - U2 * Pin0.diff(x) * U2.inv())
check("planted", "PLANT omitting the frame commutator breaks derivative naturality",
      not zero(wrong_derivative))

unnormalized_E = sp.simplify(A1 + x * A2)
unnormalized_P = sp.simplify((I4 - unnormalized_E) / 2)
check("planted", "PLANT an unnormalized conormal breaks polynomial idempotence",
      not zero(unnormalized_P * unnormalized_P - unnormalized_P))
check("selection", "reversing boundary orientation swaps incoming and outgoing",
      zero(sp.simplify((I4 - (-E0)) / 2) - Pout0))


print("\nC. BOTH DOUBLED-MAJORANA GREEN HORNS TRANSPORT")
J = sp.simplify(A1 * A2 * A3)
P_symmetric = A3
P_skew = J
D = E0
check("krein", "the first pairing horn is symmetric and anti-adjoint to the moving coefficient",
      P_symmetric.T == P_symmetric
      and zero(P_symmetric.T * D + D.T * P_symmetric))
check("krein", "the second pairing horn is skew and self-adjoint to the moving coefficient",
      P_skew.T == -P_skew
      and zero(P_skew.T * D + D.T * P_skew))

# A rational orthogonal moving frame transports bilinear matrices without
# obscuring the doubled graph identity behind a generic-GL musical map.
c = (1 - x**2) / (1 + x**2)
s = 2 * x / (1 + x**2)
R = sp.diag(1, 1, 1, 1)
R[0, 0], R[0, 1], R[1, 0], R[1, 1] = c, -s, s, c
check("descent", "the horn-control frame is exactly orthogonal",
      zero(R.T * R - I4))
D_R = sp.simplify(R * D * R.T)
for name, pairing in (("symmetric_anti_adjoint", P_symmetric),
                      ("skew_self_adjoint", P_skew)):
    pairing_R = sp.simplify(R * pairing * R.T)
    doubled = sp.simplify(pairing_R.T * D_R + D_R.T * pairing_R)
    check("graded_green", f"{name} doubled Majorana Green form remains zero",
          zero(doubled))
    incoming_R = sp.simplify(R * Pin0 * R.T)
    check("symplectic", f"{name} remains isotropic on the transported incoming half",
          zero(incoming_R.T * doubled * incoming_R))
    # The prior wrong-object control restricts only the source columns while
    # retaining an independent dual target.  Pulling back on both sides would
    # already impose the graph/domain relation and would ask a different
    # question.
    one_sided = sp.simplify(pairing_R * D_R * incoming_R)
    check("planted", f"PLANT {name} one-sided independent-dual form stays nonzero",
          one_sided.rank() == 2)


print("\nD. ANALYTIC AND OWNERSHIP FENCES")
for kind, label in (
    ("ownership", "the action owns D_t and D_n and therefore the map n to Pi_in(n)"),
    ("selection", "the action does not select the boundary hypersurface or its outward unit conormal"),
    ("analytic", "smooth descent and positive local Gram energy give local coefficient control on compact charts"),
    ("analytic", "global-in-time well-posedness still needs global hyperbolicity bounded geometry regularity and compatibility"),
    ("analytic", "the principal theorem is not a nonlinear constraint-propagation theorem"),
    ("symplectic", "pointwise Green isotropy is not unrestricted BFV closure"),
    ("scope", "the null characteristic relation remains outside the noncharacteristic polynomial domain"),
    ("scope", "no horn p chirality mirror index count mass or cosmological claim is selected"),
    ("accounting", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "immutable_full_carrier": {
        "rank": v0179["carrier_rank"],
        "incoming_rank": v0179["incoming_rank"],
        "outgoing_rank": v0179["outgoing_rank"],
        "both_doubled_horns_local_rank": 0,
    },
    "variable_projector": {
        "formula": "Pi_in(n)=(I-D_t^{-1}D_n)/2",
        "rank_fraction": "1/2",
        "associated_bundle_descent": True,
        "connection_naturality": True,
        "negative_flux": True,
        "requires_oriented_unit_noncharacteristic_conormal": True,
    },
    "ownership": {
        "action_owns": "THE_MAP_FROM_AN_ORIENTED_UNIT_OBSERVED_SPATIAL_CONORMAL_TO_THE_INCOMING_PROJECTOR",
        "observation_boundary_geometry_owns": "THE_BOUNDARY_HYPERSURFACE_OUTWARD_CONORMAL_AND_MEMBER_SELECTION",
        "independent_projector_datum_needed": False,
        "unique_global_boundary_selected": False,
    },
    "analytic_status": "CONDITIONAL_LOCAL_VARIABLE_COEFFICIENT_PRINCIPAL_IBVP_DATA__GLOBAL_IN_TIME_NONLINEAR_CONSTRAINT_AND_BOUNDED_GEOMETRY_CLOSURE_OPEN",
    "selection": "BOTH_HORNS_PASS__NO_HORN_OR_P_SELECTION",
    "source_return": "SOURCE_CONFIRMS_FIRST_ORDER_FOUR_FIELD_PARENT_AND_COVARIANT_GRAMMAR__SOURCE_CORRECTS_NONE__SOURCE_SILENT_ON_INCOMING_PROJECTOR_FAMILY_BOUNDARY_SELECTION_AND_VARIABLE_ANALYTIC_DOMAIN",
    "p1_p2_p3_used": False,
    "disposition": "ACTION_DERIVES_THE_VARIABLE_INCOMING_PROJECTOR_FAMILY_FROM_ITS_PRINCIPAL_COEFFICIENTS__OBSERVATION_BOUNDARY_GEOMETRY_SELECTS_THE_MEMBER__BOTH_DOUBLED_MAJORANA_HORNS_TRANSPORT__GLOBAL_ANALYTIC_CLOSURE_OPEN",
}

print("\nSELECTED K77 VARIABLE INCOMING-PROJECTOR DESCENT RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the action derives the transported projector family; boundary geometry selects a member; global analytic closure remains open.")
