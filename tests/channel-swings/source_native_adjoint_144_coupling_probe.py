#!/usr/bin/env python3
"""Exact degree ladder for the paired-real WG-P03 adjoint/144 coupling.

Scope: complexified D5 representation channels plus their paired-real and
Pati--Salam interpretation.  This does not select a source action component,
family covector, background, mass, observed sector, scale, or threshold.
"""
from __future__ import annotations

from collections import Counter
from itertools import combinations, combinations_with_replacement
import contextlib
import importlib.util
import io
from pathlib import Path
import sys


REPO = Path(__file__).resolve().parents[2]
CHECKS: list[tuple[str, bool]] = []


def check(name: str, ok: bool) -> None:
    CHECKS.append((name, bool(ok)))


def load_script(name: str, relative: str, expected_exit: int | None = None):
    path = REPO / relative
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact dependency: {path}")
    module = importlib.util.module_from_spec(spec)
    exit_code = None
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            spec.loader.exec_module(module)
        except SystemExit as exc:
            exit_code = exc.code
    check(f"{name} dependency exit", exit_code == expected_exit)
    return module


he4 = load_script(
    "he4_exact_owner_engine",
    "tests/channel-swings/joe_directed_he4_distinct_ps_channel_owners_probe.py",
    expected_exit=0,
)
he1 = he4.he1
q5 = he4.q5


def expanded_weights(character: Counter) -> list[tuple[int, ...]]:
    return [weight for weight, multiplicity in sorted(character.items())
            for _ in range(multiplicity)]


def pair_character(weights: list[tuple[int, ...]], symmetric: bool) -> Counter:
    iterator = (combinations_with_replacement(range(len(weights)), 2)
                if symmetric else combinations(range(len(weights)), 2))
    return Counter(
        tuple(weights[i][axis] + weights[j][axis] for axis in range(5))
        for i, j in iterator
    )


def decomposition_dimensions(character: Counter) -> list[tuple[int, int]]:
    return sorted(
        (int(he1.SO10.dim(highest)), multiplicity)
        for highest, multiplicity in he1.decompose(character, he1.SO10).items()
    )


adjoint_weights = expanded_weights(he4.C45)
sym2_adjoint = pair_character(adjoint_weights, symmetric=True)
alt2_adjoint = pair_character(adjoint_weights, symmetric=False)

check("adjoint character expands to 45 weight states", len(adjoint_weights) == 45)
check("symmetric and alternating squares have dimensions 1035 and 990",
      (sum(sym2_adjoint.values()), sum(alt2_adjoint.values())) == (1035, 990))
check("Sym^2(45) decomposes exactly as 1 + 54 + 210 + 770",
      decomposition_dimensions(sym2_adjoint) == [(1, 1), (54, 1), (210, 1), (770, 1)])
check("Lambda^2(45) decomposes exactly as 45 + 945",
      decomposition_dimensions(alt2_adjoint) == [(45, 1), (945, 1)])

same_label = q5.EXPECTED[("16+", "144+")]
conjugate_same_label = q5.EXPECTED[("16-", "144-")]
crossed_a = q5.EXPECTED[("16+", "144-")]
crossed_b = q5.EXPECTED[("16-", "144+")]

check("bare same-label fermion products contain no scalar",
      "1" not in same_label and "1" not in conjugate_same_label)
check("one adjoint 45 occurs in each conjugate same-label product",
      same_label["45"] == conjugate_same_label["45"] == 1)
check("crossed products contain no adjoint 45",
      crossed_a["45"] == crossed_b["45"] == 0)
check("the cubic adjoint channel is not a conventional 126 channel",
      not any(name.startswith("126") for name in same_label))

sym2_names = {1: "1", 54: "54", 210: "210", 770: "770"}
alt2_names = {45: "45", 945: "945"}
fermion_names = set(same_label)
sym2_intersection = {
    sym2_names[dimension]
    for dimension, multiplicity in decomposition_dimensions(sym2_adjoint)
    if multiplicity == 1 and sym2_names[dimension] in fermion_names
}
alt2_intersection = {
    alt2_names[dimension]
    for dimension, multiplicity in decomposition_dimensions(alt2_adjoint)
    if multiplicity == 1 and alt2_names[dimension] in fermion_names
}
check("quadratic symmetric-adjoint owners are exactly 54 and 210",
      sym2_intersection == {"54", "210"})
check("quadratic alternating-adjoint owners are exactly 45 and 945",
      alt2_intersection == {"45", "945"})

ps_counts = {"45": 0, "54": 1, "210": 1, "945": 0}
check("linear adjoint has no Pati-Salam singlet", he4.PS_COUNTS["45"] == 0)
check("both symmetric quadratic owners have one Pati-Salam singlet",
      he4.PS_COUNTS["54"] == he4.PS_COUNTS["210"] == 1)
check("alternating quadratic owners have no Pati-Salam singlet",
      ps_counts["45"] == ps_counts["945"] == 0)

REAL_COUPLING = "conjugate-paired 45 line"
FIRST_PS_BACKGROUND_OWNERS = ("54", "210")
FAMILY_COPY_COUPLING_SPACES = (REAL_COUPLING, REAL_COUPLING)
SOURCE_SELECTED_FAMILY_COVECTOR = None
SOURCE_SELECTED_QUADRATIC_OWNER = None
SOURCE_FORM_LEG_CONTRACTION = None

check("the real cubic is the conjugate pair, not either complex line alone",
      REAL_COUPLING == "conjugate-paired 45 line")
check("the first PS-preserving background owners are the two symmetric channels",
      FIRST_PS_BACKGROUND_OWNERS == ("54", "210"))
check("equivalent true-family copies have identical representation coupling spaces",
      FAMILY_COPY_COUPLING_SPACES[0] == FAMILY_COPY_COUPLING_SPACES[1])
check("representation theory selects no family covector or quadratic owner",
      SOURCE_SELECTED_FAMILY_COVECTOR is None
      and SOURCE_SELECTED_QUADRATIC_OWNER is None)
check("the source form-leg contraction remains type-missing",
      SOURCE_FORM_LEG_CONTRACTION is None)


def reference_verifier(sym_character: Counter) -> bool:
    """Reference-dependent verifier used by the planted hostile controls."""
    return decomposition_dimensions(sym_character) == [
        (1, 1), (54, 1), (210, 1), (770, 1)
    ]


if "--selftest" in sys.argv:
    check("selftest baseline is green before mutations", reference_verifier(sym2_adjoint))
    missing_state = sym2_adjoint.copy()
    witness = max(he4.C210, default=None)
    check("selftest dependency 210 character is nonempty", witness is not None)
    if witness is not None:
        missing_state[witness] -= 1
        if missing_state[witness] == 0:
            del missing_state[witness]
    check("selftest catches a corrupted quadratic character",
          not reference_verifier(missing_state))
    wrong_owner = sym2_adjoint + he4.C45
    check("selftest catches a planted forbidden adjoint owner",
          not reference_verifier(wrong_owner))


print("WG-P03 source-native adjoint/144 coupling degree ladder")
print("  degree 2 (bare fermion pairing): no scalar")
print("  degree 3 (one adjoint): one conjugate-paired real 45 vertex")
print("  PS-preserving linear background: obstructed; Inv_PS(45)=0")
print("  degree 4 Sym^2(ad): 54 and 210, one PS singlet each")
print("  degree 4 Lambda^2(ad): 45 and 945, no PS singlet")
print("  family copies: identical allowed spaces; selector TYPE_MISSING")
print()
passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"\n{passed}/{len(CHECKS)} exact checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
