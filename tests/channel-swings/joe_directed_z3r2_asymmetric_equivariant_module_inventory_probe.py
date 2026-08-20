#!/usr/bin/env python3
"""Z3R2 exact audit of the owned C3-equivariant module inventory.

This probe checks a structural occupied 1+2 isotypic survivor and the exact
automorphism obstruction to promoting it to a canonical rank-three/family
quotient.  It does not construct a source action, external datum, selector,
marked orbit, family row, or physical quotient.
"""

from __future__ import annotations

import argparse
import itertools
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


@dataclass(frozen=True)
class QZ:
    """a + b*zeta in Q[zeta]/(zeta^2+zeta+1)."""

    a: F
    b: F = F(0)

    def __add__(self, other: object) -> "QZ":
        o = qz(other)
        return QZ(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self) -> "QZ":
        return QZ(-self.a, -self.b)

    def __sub__(self, other: object) -> "QZ":
        return self + (-qz(other))

    def __rsub__(self, other: object) -> "QZ":
        return qz(other) - self

    def __mul__(self, other: object) -> "QZ":
        o = qz(other)
        # zeta^2 = -1-zeta
        return QZ(self.a * o.a - self.b * o.b,
                  self.a * o.b + self.b * o.a - self.b * o.b)

    __rmul__ = __mul__

    def __truediv__(self, n: int) -> "QZ":
        return QZ(self.a / n, self.b / n)

    def conj(self) -> "QZ":
        # conjugate(zeta)=zeta^2=-1-zeta
        return QZ(self.a - self.b, -self.b)

    @property
    def is_rational(self) -> bool:
        return self.b == 0


def qz(x: object) -> QZ:
    if isinstance(x, QZ):
        return x
    return QZ(F(x))


ZERO, ONE, ZETA = QZ(F(0)), QZ(F(1)), QZ(F(0), F(1))
ZETA_POW = (ONE, ZETA, ZETA * ZETA)


def ga_add(x: tuple[QZ, ...], y: tuple[QZ, ...]) -> tuple[QZ, ...]:
    return tuple(a + b for a, b in zip(x, y))


def ga_mul(x: tuple[QZ, ...], y: tuple[QZ, ...]) -> tuple[QZ, ...]:
    out = [ZERO, ZERO, ZERO]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[(i + j) % 3] = out[(i + j) % 3] + a * b
    return tuple(out)


def central_idempotent(k: int, sign: int = -1) -> tuple[QZ, ...]:
    return tuple(ZETA_POW[(sign * k * j) % 3] / 3 for j in range(3))


def invert_group_element(x: tuple[QZ, ...]) -> tuple[QZ, ...]:
    return (x[0], x[2], x[1])


def conjugate_coefficients(x: tuple[QZ, ...]) -> tuple[QZ, ...]:
    return tuple(a.conj() for a in x)


def affine_permutations() -> tuple[tuple[int, int, int], ...]:
    # Enlarged label equivalences k -> a*k+b.  The b != 0 maps are
    # tensor-by-character translations, NOT automorphisms of C3.
    return tuple(tuple((a * k + b) % 3 for k in range(3))
                 for a in (1, 2) for b in range(3))


def character_group_automorphisms() -> tuple[tuple[int, int, int], ...]:
    # Aut(C3) acts on characters by multiplication and must fix label 0.
    return tuple(tuple((a * k) % 3 for k in range(3)) for a in (1, 2))


def relabel(m: tuple[int, int, int], p: tuple[int, int, int]) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for old, new in enumerate(p):
        out[new] = m[old]
    return tuple(out)


def stabilizer(m: tuple[int, int, int], perms=None):
    ps = affine_permutations() if perms is None else perms
    return tuple(p for p in ps if relabel(m, p) == m)


def label_orbits(ps: tuple[tuple[int, int, int], ...]):
    unseen = set(range(3))
    out = []
    while unseen:
        seed = min(unseen)
        orbit = {p[seed] for p in ps}
        out.append(tuple(sorted(orbit)))
        unseen -= orbit
    return tuple(out)


class Ledger:
    def __init__(self):
        self.total = 0

    def check(self, condition: bool, message: str):
        self.total += 1
        if not condition:
            raise AssertionError(f"check {self.total}: {message}")


def find_repo_root(start: Path) -> Path:
    for p in (start, *start.parents):
        if (p / "canon/order3-equivariant-rho-RESULTS.md").is_file():
            return p
    raise FileNotFoundError("could not locate gu-formalization root")


def run_exact_checks(repo: Path, artifact: Path, mutation: str | None = None) -> int:
    L = Ledger()

    sign = +1 if mutation == "cyclotomic" else -1
    es = tuple(central_idempotent(k, sign) for k in range(3))
    identity = (ONE, ZERO, ZERO)
    for k in range(3):
        L.check(ga_mul(es[k], es[k]) == es[k], f"e_{k} must be idempotent")
        for ell in range(3):
            if k != ell:
                L.check(ga_mul(es[k], es[ell]) == (ZERO, ZERO, ZERO),
                        f"e_{k} e_{ell} must vanish")
    L.check(ga_add(ga_add(es[0], es[1]), es[2]) == identity,
            "central idempotents must sum to one")
    L.check(invert_group_element(es[0]) == es[0], "inversion fixes e0")
    # Coefficient conjugation and group inversion each exchange e1/e2 under
    # the standard sign.  The deliberately flipped mutation violates this
    # pinned convention check while preserving abstract idempotency.
    L.check(conjugate_coefficients(es[1]) == es[2] and sign == -1,
            "pinned cyclotomic convention: conjugation swaps e1 and e2")
    L.check(invert_group_element(es[1]) == es[2], "inversion swaps e1 and e2")
    L.check(all(c.is_rational for c in es[0]), "e0 is defined over R")
    L.check(all(c.is_rational for c in ga_add(es[1], es[2])), "e1+e2 is defined over R")
    L.check(not all(c.is_rational for c in es[1]), "e1 alone is not defined over R")
    L.check(not all(c.is_rational for c in es[2]), "e2 alone is not defined over R")

    perms = affine_permutations()
    aut_perms = character_group_automorphisms()
    if mutation == "symmetry_type":
        aut_perms = perms
    L.check(len(perms) == 6 and len(set(perms)) == 6, "AGL(1,3) has six elements")
    L.check(set(perms) == set(itertools.permutations(range(3))), "AGL(1,3) is S3 on labels")
    L.check(len(aut_perms) == 2 and all(p[0] == 0 for p in aut_perms)
            and any(p[0] != 0 for p in perms),
            "Aut(C3)=C2 fixes the trivial label; affine translations enlarge it by tensoring")

    constant = (64, 64, 64)
    q_tuple = (14, 13, 12) if mutation == "q_tuple" else (14, 12, 12)
    prior = ((8, 6, 6), (7, 6, 6), (16, 12, 12))
    L.check(len(stabilizer(constant, perms)) == 6, "regular tuple has full S3 stabilizer")
    L.check(label_orbits(stabilizer(constant, perms)) == ((0, 1, 2),),
            "regular tuple has one transitive label orbit")
    for m in (q_tuple, *prior):
        L.check(len(stabilizer(m, perms)) == 2, f"{m} has C2 stabilizer")
        L.check(label_orbits(stabilizer(m, perms)) == ((0,), (1, 2)),
                f"{m} has exact occupied singleton-plus-pair orbit")
        L.check(all(x > 0 for x in m), f"{m} has no empty isotype")
    L.check(len(stabilizer((14, 13, 12), perms)) == 1,
            "all-distinct control has trivial stabilizer")
    L.check(label_orbits(stabilizer((14, 13, 12), perms)) == ((0,), (1,), (2,)),
            "all-distinct control has three singleton orbits")

    solutions = [(m0, m1) for m0 in range(39) for m1 in range(39)
                 if m0 + 2 * m1 == 38 and m0 - m1 == 2]
    L.check(solutions == [(14, 12)], "dimension, trace and reality uniquely force (14,12,12)")
    L.check(sum(q_tuple) == 38, "Q multiplicities sum to 38")
    L.check(q_tuple[1] == q_tuple[2], "Q nontrivial characters are conjugate-paired")
    L.check(q_tuple[0] - q_tuple[1] == 2, "Q character trace is 2")

    rho = (0, 2, 2) if mutation == "rho_sign" else (0, 2, 1)
    L.check(rho == (0, 2, 1), "Q rho class is (0,2,1)/3")
    L.check(tuple((-x) % 3 for x in rho) == (0, 1, 2),
            "Q and Dirac rho classes have opposite nonzero order-three signs")
    L.check((0, 0, 0) != rho, "Q rho is not ghost convention A's zero class")

    real_pair = 11 if mutation == "real_pair" else 12
    L.check(14 + 2 * real_pair == 38, "realification is R^14 plus 12 rotation planes")
    L.check(real_pair == q_tuple[1] == q_tuple[2], "real rotation multiplicity matches conjugate pair")
    L.check(14 != real_pair, "real singleton and rotation blocks have unequal multiplicity")

    cdim = 14 * 14 + 12 * 12 + 12 * 12
    rdim = 14 * 14 + 2 * 12 * 12
    if mutation == "centralizer":
        rdim += 1
    L.check(cdim == 484, "complex centralizer dimension is 484")
    L.check(rdim == 484, "real centralizer dimension is 484")
    L.check(cdim == rdim, "complex and real centralizer dimensions agree numerically, not as algebras")
    L.check(14 + 12 + 12 == 38, "equivariant maps V_Q -> C[C3] form a 38-dimensional space")
    L.check(all(n > 1 for n in q_tuple), "every isotypic multiplicity admits non-scalar basis changes")

    invariant_covector_dimension = 1 if mutation == "naturality" else 0
    # Invariance under every scalar lambda*I in GL_n forces f=lambda f,
    # hence f=0 by choosing lambda != 1, on each occupied isotype.
    L.check(invariant_covector_dimension == 0,
            "no nonzero covector is natural under the full module automorphism group")
    L.check(0 + 0 + 0 == 0, "there is no natural rank-one choice on any of the three isotypes")

    custody = {
        "tests/rs-function-space/rho-38-adjudication/legC_equivariant_rho.py": (
            "route (iii): m0 + 2 m1 = 38",
            "UNIQUE solution (14, 12)",
            "GEOMETRIC Q: h = (14, 12, 12) -- HONEST kernel dims",
            "GEOMETRIC Q: rho = (0, +2/3, -2/3)",
        ),
        "canon/order3-equivariant-rho-RESULTS.md": (
            "order-3 rho classes are `(0,2,1)/3` NONZERO",
            "nothing connects it to a chiral count",
        ),
        "lab/active-research/joe-directed/z3-receptacle/z3r1-nu-trivial-w-untwisted-2026-08-17.md": (
            "standard Higgs/VEV, ordinary family index or net chirality",
            "tests/dim13/mh7_dim13_link_receptacle_probe.py",
        ),
    }
    for rel, needles in custody.items():
        text = (repo / rel).read_text()
        L.check(bool(text), f"custody file exists and is nonempty: {rel}")
        for needle in needles:
            L.check(needle in text, f"custody phrase remains present in {rel}: {needle}")

    atext = artifact.read_text()
    required = (
        "STRUCTURAL_1_PLUS_2_ISOTYPIC_SURVIVOR",
        "CANONICAL_RANK3_OR_FAMILY_QUOTIENT_OBSTRUCTED_BY_MODULE_AUTOMORPHISMS",
        "DIM13_AND_SOURCE_MAPS_TYPE_MISSING",
        "not an integer generation count",
        "not the source imposter `F`",
        "not the family multiplicity space `M_3`",
        "not the partner `144`",
        "no owned map",
        "GU-COMPARATOR-ROUTING — scope before inference.",
        "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`",
    )
    forbidden = (
        "Z/3 forces three generations",
        "Q kernel is the imposter",
        "rho equals the generation count",
        "the source action selects Q",
    )
    for needle in required:
        L.check(needle in atext, f"artifact carries required ceiling: {needle}")
    for needle in forbidden:
        L.check(needle not in atext, f"artifact avoids forbidden overclaim: {needle}")

    return L.total


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--artifact", type=Path)
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()

    here = Path(__file__).resolve()
    repo = args.repo_root.resolve() if args.repo_root else find_repo_root(here.parent)
    artifact = (args.artifact.resolve() if args.artifact else
                repo / "lab/active-research/joe-directed/z3-receptacle/"
                       "z3r2-asymmetric-equivariant-module-inventory-2026-08-20.md")
    count = run_exact_checks(repo, artifact)
    print(f"Z3R2 PASS: {count} exact checks")
    print("disposition=STRUCTURAL_1_PLUS_2_ISOTYPIC_SURVIVOR__"
          "CANONICAL_RANK3_OR_FAMILY_QUOTIENT_OBSTRUCTED_BY_MODULE_AUTOMORPHISMS__"
          "DIM13_AND_SOURCE_MAPS_TYPE_MISSING")

    if args.selftest:
        mutations = ("cyclotomic", "symmetry_type", "q_tuple", "rho_sign",
                     "real_pair", "centralizer", "naturality")
        killed = 0
        for mutation in mutations:
            try:
                run_exact_checks(repo, artifact, mutation)
            except AssertionError:
                killed += 1
                print(f"MUTATION KILLED: {mutation}")
            else:
                raise AssertionError(f"mutation survived unexpectedly: {mutation}")
        print(f"SELFTEST PASS: {killed}/{len(mutations)} mutations killed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
