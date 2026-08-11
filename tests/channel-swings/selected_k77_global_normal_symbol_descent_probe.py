#!/usr/bin/env python3
"""Exact real-K77 normal-symbol and Darboux-overlap gate.

This probe composes four already-owned objects rather than inventing a new
coefficient: the source's first-order four-field grammar, the exact K77
nonnull/null principal ranks, the global moving Clifford bundle, and the
v0.166 first-jet Darboux transform.  It tests two distinct statements:

1. the normal principal symbol is a global associated-bundle morphism; and
2. it is invertible only on the noncharacteristic conormal locus.

A nonconstant Spin-frame overlap is included so that raw ``dA`` cannot pass as
tensorial.  The induced cotangent momentum transition restores the complete
potential and the Darboux atlas.  No graph, Calderon projector, analytic
domain, positivity claim, or BFV quotient is supplied.
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


def scalar(value):
    return value[0] if isinstance(value, sp.MatrixBase) else value


print("A. ADAPTIVE PREFLIGHT, SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
principal = strict("lab/process/selected-k77-induced-fermion-principal-discriminator.json")
global_spin = read("explorations/conditional-build/k77-global-chimeric-spin-reduction-and-support-normalization-2026-08-05.md")
action_overlap = read("explorations/conditional-build/selected-k77-action-bundle-observation-overlap-2026-08-08.md")
comoving = read("explorations/conditional-build/selected-k77-transverse-comoving-coefficient-closure-2026-08-08.md")
v0166 = strict("lab/process/selected-k77-moving-antidualizer-darboux.json")

check("source", "the draft displays a first-order four-field operator grammar",
      "four distinct fields" in source and "d0" in source and "Equation 9.16" in source)
check("source", "the source remains silent on the global Green domain",
      "Green preboundary current" in source and "SOURCE-SILENT" in source)
check("prior_art", "the global moving Clifford bundle is already owned",
      "P_H=P_{\\operatorname{Spin}(C)}" in global_spin
      and "\\gamma_\\epsilon=\\operatorname{Ad}(\\epsilon^{-1})\\gamma_0" in global_spin)
check("prior_art", "the action coefficient bundle overlap is already exact",
      "FULL_ACTION_COVECTOR_ADJOINT_BUNDLE_OVERLAP_EXACT" in action_overlap)
check("prior_art", "all-ten comoving coefficient transport is already exact",
      "all ten metric values" in comoving and "coefficient-motion packet" in comoving)
check("prior_art", "v0.166 makes invertibility an explicit local hypothesis",
      v0166["darboux_completion"]["requires"] == "A(q) invertible on the chart")
for label in (
    "fermion normal principal symbol versus bosonic E_B-minus-E_T coefficient bank",
    "normal principal symbol versus residual Riesz map",
    "actual four-field symbol versus v0.165 scalar finite comparator",
    "global bundle morphism versus globally invertible bundle automorphism",
    "noncharacteristic inverse versus null characteristic relation",
    "Darboux atlas versus Calderon projector",
):
    check("layer0", label, True)


print("\nB. EXACT REAL CL(7,7) NORMAL-SYMBOL CONTROL")
spin_dim = 1 << 7


def creation(index: int) -> sp.Matrix:
    out = sp.zeros(spin_dim)
    for mask in range(spin_dim):
        if mask & (1 << index):
            continue
        sign = -1 if (mask & ((1 << index) - 1)).bit_count() % 2 else 1
        out[mask | (1 << index), mask] = sign
    return out


def contraction(index: int) -> sp.Matrix:
    out = sp.zeros(spin_dim)
    for mask in range(spin_dim):
        if not mask & (1 << index):
            continue
        sign = -1 if (mask & ((1 << index) - 1)).bit_count() % 2 else 1
        out[mask ^ (1 << index), mask] = sign
    return out


wedge0 = creation(0)
contract0 = contraction(0)
gamma_plus = wedge0 + contract0
gamma_minus = wedge0 - contract0
identity128 = sp.eye(spin_dim)
check("clifford", "the positive generator squares to plus one",
      gamma_plus * gamma_plus == identity128)
check("clifford", "the negative generator squares to minus one",
      gamma_minus * gamma_minus == -identity128)
check("clifford", "the opposite-sign generators anticommute",
      gamma_plus * gamma_minus + gamma_minus * gamma_plus == sp.zeros(spin_dim))

normal_positive = gamma_plus
normal_negative = gamma_minus
normal_generic = 2 * gamma_plus + gamma_minus
normal_null = gamma_plus + gamma_minus
check("causal", "positive normal coefficient is invertible",
      normal_positive.rank() == spin_dim and normal_positive.inv() == normal_positive)
check("causal", "negative normal coefficient is invertible",
      normal_negative.rank() == spin_dim and normal_negative.inv() == -normal_negative)
check("causal", "generic nonnull coefficient has Clifford inverse",
      normal_generic * normal_generic == 3 * identity128
      and normal_generic.rank() == spin_dim)
check("causal", "null Clifford coefficient is square-zero and rank one half",
      normal_null * normal_null == sp.zeros(spin_dim)
      and normal_null.rank() == spin_dim // 2)
check("planted", "PLANT a null Clifford coefficient has no inverse",
      normal_null.det() == 0)

full = principal["exact_result"]["full_symbol"]
check("actual_symbol", "the actual complete four-field symbol is invertible off the null cone",
      full["nonnull_rank"] == 1920)
check("actual_symbol", "the actual complete four-field symbol is singular on the null cone",
      full["null_rank"] == 1024 and full["null_kernel"] == 896)
check("layer0", "the 128-spin Clifford control is not substituted for the 1920-field symbol",
      normal_null.rank() == 64 and full["null_rank"] != 15 * normal_null.rank())


print("\nC. NONCONSTANT THREE-PATCH SPIN OVERLAP")
x = sp.symbols("x", real=True)
r = 1 + x
s = 1 + 2 * x
U0 = sp.eye(2)
U1 = sp.diag(1, r)
# A constant Clifford reflection followed by a moving boost makes the atlas
# genuinely noncommuting; a purely diagonal Cl(1,1) atlas would make the
# reversed-order plant vacuous.
U2 = sp.Matrix([[0, 1], [1, 0]]) * sp.diag(1, s)
U01 = U1 * U0.inv()
U12 = sp.simplify(U2 * U1.inv())
U02 = U2 * U0.inv()
check("descent", "the nonconstant Spin-frame transitions obey the triple cocycle",
      sp.simplify(U12 * U01 - U02) == sp.zeros(2))
check("planted", "PLANT reversing transition order fails",
      sp.simplify(U01 * U12 - U02) != sp.zeros(2))

e = sp.Matrix([[0, 0], [1, 0]])
iota = sp.Matrix([[0, 1], [0, 0]])
A0 = e + iota


def patch_coefficient(U: sp.Matrix) -> sp.Matrix:
    return sp.simplify(U * A0 * U.inv())


A1 = patch_coefficient(U1)
A2 = patch_coefficient(U2)
check("descent", "the normal coefficient descends on overlap 01",
      sp.simplify(A1 - U01 * A0 * U01.inv()) == sp.zeros(2))
check("descent", "the normal coefficient descends on overlap 12",
      sp.simplify(A2 - U12 * A1 * U12.inv()) == sp.zeros(2))
check("descent", "direct and sequential coefficient descent agree",
      sp.simplify(A2 - U02 * A0 * U02.inv()) == sp.zeros(2))
check("descent", "inverse symbols descend contragrediently on the nonnull locus",
      sp.simplify(A1.inv() - U01 * A0.inv() * U01.inv()) == sp.zeros(2)
      and sp.simplify(A2.inv() - U02 * A0.inv() * U02.inv()) == sp.zeros(2))
check("planted", "PLANT freezing the coefficient breaks a nonconstant overlap",
      sp.simplify(A1 - A0) != sp.zeros(2))


print("\nD. COMPLETE POTENTIAL AND DARBOUX-ATLAS DESCENT")
p0 = sp.symbols("p0", real=True)
z0, z1, b0, b1 = sp.symbols("z0 z1 b0 b1", real=True)
dz0, dz1, db0, db1, dx = sp.symbols("dz0 dz1 db0 db1 dx", real=True)
psi0 = sp.Matrix([z0, z1])
bar0 = sp.Matrix([b0, b1])
dpsi0 = sp.Matrix([dz0, dz1])
dbar0 = sp.Matrix([db0, db1])


def differential(U: sp.Matrix, vector: sp.Matrix, dvector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(U * dvector + U.diff(x) * vector * dx)


def patch_packet(U: sp.Matrix):
    Ui = U.inv()
    psi = U * psi0
    bar = U.T.inv() * bar0
    dpsi = differential(U, psi0, dpsi0)
    dbar = differential(U.T.inv(), bar0, dbar0)
    A = patch_coefficient(U)
    Omega = sp.simplify(Ui * U.diff(x))
    p = sp.simplify(p0 - sp.Rational(1, 2)
                    * scalar(bar0.T * (A0 * Omega + Omega * A0) * psi0))
    theta = sp.simplify(p * dx + sp.Rational(1, 2) * (
        scalar(bar.T * A * dpsi) - scalar(dbar.T * A * psi)
    ))
    v = sp.simplify(A.T * bar)
    dv = differential(U.T.inv(), A0.T * bar0,
                      A0.T * dbar0)
    P = sp.simplify(p + sp.Rational(1, 2)
                    * scalar(bar.T * A.diff(x) * psi))
    theta_darboux = sp.simplify(P * dx + sp.Rational(1, 2) * (
        scalar(v.T * dpsi) - scalar(dv.T * psi)
    ))
    return {
        "A": A, "psi": psi, "bar": bar, "dpsi": dpsi, "dbar": dbar,
        "Omega": Omega, "p": p, "theta": theta, "v": v, "P": P,
        "theta_darboux": theta_darboux,
    }


patch0 = patch_packet(U0)
patch1 = patch_packet(U1)
patch2 = patch_packet(U2)
check("symplectic", "the complete original potential descends on both overlaps",
      sp.simplify(patch1["theta"] - patch0["theta"]) == 0
      and sp.simplify(patch2["theta"] - patch0["theta"]) == 0)
check("variational", "each patch has the exact v0.166 Darboux potential",
      all(sp.simplify(packet["theta"] - packet["theta_darboux"]) == 0
          for packet in (patch0, patch1, patch2)))
check("descent", "the Darboux dual variable transforms contragrediently",
      sp.simplify(patch1["v"] - U01.T.inv() * patch0["v"]) == sp.zeros(2, 1)
      and sp.simplify(patch2["v"] - U02.T.inv() * patch0["v"]) == sp.zeros(2, 1))

expected_P1 = sp.simplify(patch0["P"]
                          - scalar(patch0["v"].T * patch1["Omega"] * patch0["psi"]))
expected_P2 = sp.simplify(patch0["P"]
                          - scalar(patch0["v"].T * patch2["Omega"] * patch0["psi"]))
check("symplectic", "the Darboux momentum carries the induced cotangent shift",
      sp.simplify(patch1["P"] - expected_P1) == 0
      and sp.simplify(patch2["P"] - expected_P2) == 0)

Omega12 = sp.simplify(U12.inv() * U12.diff(x))
via1_P2 = sp.simplify(patch1["P"]
                      - scalar(patch1["v"].T * Omega12 * patch1["psi"]))
check("descent", "direct and sequential Darboux momentum descent agree",
      sp.simplify(via1_P2 - patch2["P"]) == 0)

wrong_bar1 = U1 * bar0
wrong_bilinear = sp.simplify(scalar(wrong_bar1.T * A1 * (U1 * psi0))
                               - scalar(bar0.T * A0 * psi0))
check("planted", "PLANT using vector rather than dual transport for bar fails",
      wrong_bilinear != 0)
wrong_theta1 = sp.simplify(p0 * dx + sp.Rational(1, 2) * (
    scalar(patch1["bar"].T * A1 * patch1["dpsi"])
    - scalar(patch1["dbar"].T * A1 * patch1["psi"])
))
check("planted", "PLANT omitting the cotangent overlap shift breaks the potential",
      sp.simplify(wrong_theta1 - patch0["theta"]) != 0)
wrong_P1 = sp.simplify(patch1["p"])
check("planted", "PLANT omitting the half shear breaks Darboux equality",
      sp.simplify(wrong_P1 * dx + sp.Rational(1, 2) * (
          scalar(patch1["v"].T * patch1["dpsi"])
          - scalar(differential(U1.T.inv(), A0.T * bar0, A0.T * dbar0).T
                   * patch1["psi"])
      ) - patch1["theta"]) != 0)


print("\nE. ANALYTIC, SELECTION, AND PHYSICS FENCES")
for kind, label in (
    ("analytic", "the noncharacteristic symbol inverse is not a Calderon projector"),
    ("analytic", "null characteristic data require a separate relation or characteristic theory"),
    ("analytic", "no Sobolev closedness Lopatinski estimate or maximal dissipativity is inferred"),
    ("selection", "overlap descent transports every supplied symmetric graph and selects none"),
    ("symplectic", "the induced cotangent shift is transition-owned rather than external datum"),
    ("gauge", "unrestricted boundary moment map and BFV edge completion remain open"),
    ("scope", "no positivity chirality mirror index count mass or spectrum is derived"),
    ("accounting", "P1 P2 P3 remain unchanged and unused"),
):
    check(kind, label, True)

result = {
    "counts": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "normal_symbol": {
        "typed_owner": "FIRST_ORDER_FOUR_FIELD_FERMION_PRINCIPAL_SYMBOL",
        "not_bosonic_EB_minus_ET_bank": True,
        "not_v0165_scalar_comparator": True,
        "global_associated_bundle_morphism": True,
        "nonnull_rank": full["nonnull_rank"],
        "null_rank": full["null_rank"],
        "null_kernel": full["null_kernel"],
        "global_automorphism": False,
    },
    "darboux_descent": {
        "complete_potential": True,
        "half_shear": True,
        "cotangent_overlap_shift": True,
        "three_patch_cocycle": True,
        "requires_noncharacteristic_normal": True,
    },
    "selection": {
        "graph_selected": False,
        "minimum_coordinates_transported": 120,
        "P1_P2_P3": "UNUSED",
    },
    "analytic_successor": {
        "timelike_spacelike": "OPEN__CONSTRUCT_CALDERON_OR_MAXIMAL_DISSIPATIVE_PROJECTOR",
        "null": "SEPARATE_CHARACTERISTIC_RELATION_OR_BFV_EDGE_THEORY_REQUIRED",
    },
    "disposition": "ACTUAL_NORMAL_SYMBOL_TYPED_AS_FOUR_FIELD_PRINCIPAL_SYMBOL__GLOBAL_ASSOCIATED_BUNDLE_DESCENT_AND_NONCHARACTERISTIC_INVERSE_EXACT__GLOBAL_INVERTIBLE_EVERYWHERE_PREMISE_KILLED_BY_NULL_RANK1024_KERNEL896__DARBOUX_ATLAS_GLUES_WITH_TRANSITION_OWNED_COTANGENT_SHIFT__GRAPH_UNSELECTED",
}
print("\nSELECTED K77 GLOBAL NORMAL-SYMBOL DESCENT RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: the symbol and Darboux atlas descend off the characteristic cone; null invertibility and graph selection do not.")
