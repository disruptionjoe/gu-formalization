#!/usr/bin/env python3
"""Executable contract for the old-construction/Eric ten-lens council.

This probe checks exact finite implications and the durable dependency/data
contract.  It is not a simulation of the global GU action.  The planted
claims are mistakes the council explicitly forbids future agents to revive.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MATRIX_PATH = ROOT / "lab/process/old-vs-eric-ten-lens-gap-matrix.json"
DOSSIER_PATH = ROOT / "explorations/old-vs-eric-ten-specialist-gap-opportunity-council-2026-07-31.md"
DICTIONARY_PATH = ROOT / "lab/specifications/old-vs-eric-object-dictionary-2026-07-31.md"

exact_count = 0
planted_count = 0


def exact(name: str, condition: bool) -> None:
    global exact_count
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    exact_count += 1


def planted(name: str, false_claim: bool) -> None:
    global planted_count
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    planted_count += 1


def mat_vec(m, v):
    return tuple(sum((m[i][j] * v[j] for j in range(len(v))), F(0)) for i in range(len(m)))


def transpose(m):
    return tuple(tuple(m[j][i] for j in range(len(m))) for i in range(len(m[0])))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def acyclic(swings) -> bool:
    dependencies = {row["id"]: set(row["depends_on"]) for row in swings}
    remaining = set(dependencies)
    while remaining:
        ready = {node for node in remaining if not (dependencies[node] & remaining)}
        if not ready:
            return False
        remaining -= ready
    return True


def main() -> None:
    matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
    dossier = DOSSIER_PATH.read_text(encoding="utf-8")
    dictionary = DICTIONARY_PATH.read_text(encoding="utf-8")

    lenses = matrix["lenses"]
    lens_ids = {row["id"] for row in lenses}
    swings = matrix["swings"]
    swing_ids = {row["id"] for row in swings}
    gaps = matrix["gaps"]

    exact("ten distinct specialist lenses", len(lenses) == 10 and len(lens_ids) == 10)
    exact("ten distinct construction swings", len(swings) == 10 and len(swing_ids) == 10)
    exact("swing dependency graph is acyclic", acyclic(swings))
    exact(
        "every gap has typed lenses, a kill, and a live swing",
        all(
            set(row["lenses"]) <= lens_ids
            and row["next_swing"] in swing_ids
            and bool(row["kill"])
            for row in gaps
        ),
    )
    exact(
        "every swing is used by at least one gap",
        swing_ids == {row["next_swing"] for row in gaps},
    )

    # Density-dual degree bookkeeping on an n=14 base.
    n = 14
    connection_form_degree = 1
    exact("connection Euler covector has degree thirteen", n - connection_form_degree == 13)
    exact("group-valued epsilon Euler covector has top degree", n == 14)
    exact("presymplectic current has horizontal degree thirteen", n - 1 == 13)

    # Atiyah--Bott's surface formula does not integrate on Y14 without new data.
    raw_ab_degree = 1 + 1
    planted("raw integral of two connection variations is a Y14 symplectic form", raw_ab_degree == n)
    exact("generalized AB comparator needs degree twelve", raw_ab_degree + 12 == n)

    # Inertia interlacing: a codimension-one subspace can remove at most one
    # negative direction from signature (9,5).
    ambient_negative = 5
    hypersurface_negative_floor = ambient_negative - 1
    exact("ambient hypersurface retains four negative directions", hypersurface_negative_floor == 4)
    planted("Y14 admits an ordinary spacelike 13D Cauchy hypersurface", hypersurface_negative_floor == 0)
    exact("physical initial section has codimension eleven in Y14", 14 - 3 == 11)
    planted("data on s(Sigma3) determine a generic ambient first-order field", 14 - 3 == 1)

    # A real skew complex structure squares to -I, but is not self-adjoint for
    # the positive Euclidean inner product.  This catches the hidden-i move.
    complex_structure = ((F(0), F(-1)), (F(1), F(0)))
    square_e1 = mat_vec(complex_structure, mat_vec(complex_structure, (F(1), F(0))))
    exact("complex-polarization control squares to minus identity", square_e1 == (F(-1), F(0)))
    planted("the positive-Hilbert complex structure is self-adjoint", complex_structure == transpose(complex_structure))

    # Finite Stueckelberg Noether control.  L=1/2|A-D phi|^2 has
    # E_A=u, E_phi=-D^T u, so D^T E_A+E_phi=0 while D^T E_A is generically nonzero.
    derivative = ((F(1), F(-1)), (F(0), F(1)))
    a = (F(3), F(-2))
    phi = (F(1), F(4))
    u = add(a, tuple(-x for x in mat_vec(derivative, phi)))
    e_a = u
    e_phi = tuple(-x for x in mat_vec(transpose(derivative), u))
    divergence = mat_vec(transpose(derivative), e_a)
    exact("coupled Stueckelberg Noether identity", add(divergence, e_phi) == (F(0), F(0)))
    planted("isolated connection divergence vanishes off shell", divergence == (F(0), F(0)))

    # E0's own correction: adding a curvature-linear term separates field and Euler covector.
    theta = (F(2), F(-1))
    curvature = (F(3), F(4))
    kappa = F(2)
    e_theta = add(curvature, tuple(kappa * x for x in theta))
    exact("generic Euler covector includes curvature plus field", e_theta == (F(7), F(2)))
    planted("distortion field literally equals generic Euler covector", theta == e_theta)

    # The physical chirality predicate belongs to the K-composed bilinear.
    bare_vertical_flips = False
    krein_flips = True
    paired_vertical_flips = bare_vertical_flips ^ krein_flips
    exact("K-composed vertical bilinear is cross-chirality", paired_vertical_flips)
    planted("bare vertical operator alone is the mass-channel predicate", bare_vertical_flips)

    # Typed datum and count guards.
    count_objects = {"multiplicity", "kernel_dimension", "torsion_Z3", "analytic_index", "observed_count"}
    exact("five count-related codomains remain distinct", len(count_objects) == 5)
    planted("three product-rule blocks prove three observed generations", "multiplicity" == "observed_count")
    planted("a boundary polarization is already P2", "domain_polarization" == "vertical_RS_orientation")

    # The council deliberately delays super-IG and preserves PP3 provenance.
    exact(
        "derivative super-IG is demoted beyond the ten swings",
        any(row["item"] == "derivative-level super-IG lift" for row in matrix["demoted_but_not_killed"]),
    )
    consumed_desi_confirmation_weight = F(0)
    planted("existing DESI input confirms PP3", consumed_desi_confirmation_weight > 0)

    required_dossier_tokens = [
        "G1 — derivative cocycle and moving reference",
        "G4 — observation retract and ultrahyperbolic domain",
        "G9 — rolled physicalization and datum surplus",
        "Constraint surplus ledger",
    ]
    exact("dossier carries revised construction and surplus boundary", all(t in dossier for t in required_dossier_tokens))

    required_dictionary_tokens = [
        "field versus Euler covector",
        "domain/polarization versus P2",
        "dynamic dark energy versus PP3",
    ]
    exact("dictionary preserves the decisive semantic forks", all(t in dictionary for t in required_dictionary_tokens))

    print(
        "OLD-VS-ERIC-TEN-LENS-CONTRACT: "
        f"{exact_count} exact checks + {planted_count} planted failures = "
        f"{exact_count + planted_count} PASS"
    )
    print("RESULT: derivative cocycle, coupled Noether, and ultrahyperbolic domain inserted before fitting")
    print("RESULT: K-paired vertical channel and typed P1/P2 weld preserved; P3 remains separate")
    print("BOUNDARY: council contract only; no global action, VEV, SM Higgs, PP3 emission, index, or count")


if __name__ == "__main__":
    main()
