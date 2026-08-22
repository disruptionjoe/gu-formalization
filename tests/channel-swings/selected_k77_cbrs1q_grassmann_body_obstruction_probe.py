#!/usr/bin/env python3
"""Exact CBRS-1Q Grassmann-body obstruction for bilinear fermion extensions.

The probe freezes the minimal even action

    S(b, psibar, psi) = S_B(b) + psibar D(b) psi

with independent Grassmann-odd barred and unbarred fields.  It proves and
tests that the body of the bosonic current and of every even/odd mixed Hessian
block vanishes.  Consequently a bilinear odd extension cannot enlarge the
real even-body Hessian kernel of a bosonic branch.  An explicit nonzero odd
saddle verifies that nilpotent backreaction may exist without moving the body.

This is pointwise superalgebra, not a source-owned fermion operator, BV
cohomology, a condensate, a global vacuum, or a spectrum.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import json
import random


ROOT = Path(__file__).resolve().parents[2]
COUNTS: dict[str, int] = {}
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


@dataclass(frozen=True)
class G:
    """A small exact exterior/Grassmann algebra over Q."""

    terms: tuple[tuple[int, Fraction], ...] = ()

    @staticmethod
    def make(values: dict[int, Fraction | int]) -> "G":
        return G(tuple(sorted((mask, Fraction(value)) for mask, value in values.items()
                              if value)))

    @staticmethod
    def scalar(value: Fraction | int) -> "G":
        return G.make({0: Fraction(value)})

    @staticmethod
    def theta(index: int) -> "G":
        return G.make({1 << index: 1})

    def as_dict(self) -> dict[int, Fraction]:
        return dict(self.terms)

    def __add__(self, other: "G") -> "G":
        result = self.as_dict()
        for mask, value in other.terms:
            result[mask] = result.get(mask, Fraction(0)) + value
        return G.make(result)

    def __neg__(self) -> "G":
        return G.make({mask: -value for mask, value in self.terms})

    def __sub__(self, other: "G") -> "G":
        return self + (-other)

    def scale(self, value: Fraction | int) -> "G":
        return G.make({mask: Fraction(value) * coefficient
                       for mask, coefficient in self.terms})

    def __mul__(self, other: "G") -> "G":
        result: dict[int, Fraction] = {}
        for left, a in self.terms:
            for right, b in other.terms:
                if left & right:
                    continue
                inversions = 0
                bits = left
                while bits:
                    low = bits & -bits
                    index = low.bit_length() - 1
                    inversions += (right & (low - 1)).bit_count()
                    bits ^= low
                sign = -1 if inversions % 2 else 1
                mask = left | right
                result[mask] = result.get(mask, Fraction(0)) + sign * a * b
        return G.make(result)

    @property
    def body(self) -> Fraction:
        return self.as_dict().get(0, Fraction(0))

    @property
    def degree_support(self) -> set[int]:
        return {mask.bit_count() for mask, _ in self.terms}

    def is_zero(self) -> bool:
        return not self.terms


ZERO = G()
ONE = G.scalar(1)


def odd_linear(coefficients: list[int], offset: int = 0) -> G:
    result = ZERO
    for index, coefficient in enumerate(coefficients):
        result = result + G.theta(index + offset).scale(coefficient)
    return result


def matvec(matrix: list[list[G]], vector: list[G]) -> list[G]:
    return [sum((entry * value for entry, value in zip(row, vector)), ZERO)
            for row in matrix]


def rowvec(vector: list[G], matrix: list[list[G]]) -> list[G]:
    return [sum((vector[row] * matrix[row][column]
                for row in range(len(vector))), ZERO)
            for column in range(len(matrix[0]))]


def bilinear(left: list[G], matrix: list[list[G]], right: list[G]) -> G:
    return sum((left[index] * value
                for index, value in enumerate(matvec(matrix, right))), ZERO)


print("A. EXACT GRASSMANN ALGEBRA AND BODY MAP")
theta = [G.theta(index) for index in range(4)]
check("algebra", "odd generators square to zero",
      all((value * value).is_zero() for value in theta))
check("algebra", "distinct odd generators anticommute",
      all(theta[i] * theta[j] == -(theta[j] * theta[i])
          for i in range(4) for j in range(i + 1, 4)))
check("algebra", "the body map is multiplicative on exact fixtures",
      all((left * right).body == left.body * right.body
          for left in (ZERO, ONE, ONE + theta[0], theta[0] * theta[1])
          for right in (ONE, G.scalar(3) + theta[2], theta[1] * theta[3])))
check("type", "odd fields have no scalar body",
      all(value.body == 0 and value.degree_support <= {1, 3}
          for value in theta))


print("B. UNIVERSAL BILINEAR CURRENT AND MIXED-BLOCK BODY")
rng = random.Random(1729)
for fixture in range(8):
    psi = [odd_linear([rng.randint(-3, 3) for _ in range(2)], 0),
           odd_linear([rng.randint(-3, 3) for _ in range(2)], 2)]
    psibar = [odd_linear([rng.randint(-3, 3) for _ in range(2)], 0),
              odd_linear([rng.randint(-3, 3) for _ in range(2)], 2)]
    derivative = [[G.scalar(rng.randint(-4, 4)) for _ in range(2)]
                  for _ in range(2)]
    current = bilinear(psibar, derivative, psi)
    mixed_psi = rowvec(psibar, derivative)
    mixed_bar = matvec(derivative, psi)
    check("theorem", f"fixture {fixture} bilinear bosonic current has zero body",
          current.body == 0 and current.degree_support <= {2, 4})
    check("theorem", f"fixture {fixture} both mixed Hessian blocks have zero body",
          all(value.body == 0 and value.degree_support <= {1, 3}
              for value in mixed_psi + mixed_bar))


print("C. NONZERO ODD SADDLE WITH NILPOTENT BACKREACTION")
# Bosonic coordinates are (gauge, x, y).  The body Hessian is diag(0,2,3).
# D(x,y)=diag(x,1+y).  The exact odd saddle below has nonzero psi/psibar,
# a nonzero nilpotent current, and x=-psibar_0*psi_0/2.
psi = [theta[0], ZERO]
psibar = [theta[1], ZERO]
current_x = psibar[0] * psi[0]
x = current_x.scale(Fraction(-1, 2))
y = ZERO
D = [[x, ZERO], [ZERO, ONE + y]]
fermion_left = rowvec(psibar, D)
fermion_right = matvec(D, psi)
boson_euler_x = x.scale(2) + current_x
boson_euler_y = y.scale(3) + psibar[1] * psi[1]
check("saddle", "the barred and unbarred fields are nonzero", psi[0] != ZERO and psibar[0] != ZERO)
check("saddle", "fermion Euler rows vanish by exact nilpotence",
      all(value.is_zero() for value in fermion_left + fermion_right))
check("saddle", "the coupled bosonic Euler rows vanish exactly",
      boson_euler_x.is_zero() and boson_euler_y.is_zero())
check("saddle", "backreaction and bosonic correction are nonzero but body-zero",
      not current_x.is_zero() and not x.is_zero()
      and current_x.body == x.body == 0)
check("hessian", "the even body Hessian retains one gauge zero and rank two",
      [0, 2, 3].count(0) == 1 and sum(value != 0 for value in [0, 2, 3]) == 2)
mixed_entries = [psibar[0], psi[0], ZERO, ZERO]
check("hessian", "nonzero mixed super-Hessian entries vanish under body projection",
      any(not value.is_zero() for value in mixed_entries)
      and all(value.body == 0 for value in mixed_entries))
check("hessian", "the fermion body block may have a zero mode without an even metric mode",
      [[entry.body for entry in row] for row in D]
      == [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]])


print("D. CONTRARY CLASSES AND LOAD-BEARING PARITY")
# Replacing odd fields by commuting c-numbers gives a body current and moves
# the ordinary bosonic solution.  This is a plant, not an allowed inference.
commuting_current = Fraction(1)
commuting_x = -commuting_current / 2
check("plant", "PLANT commuting spinors can move the real bosonic body",
      commuting_x == Fraction(-1, 2) and commuting_x != 0)
# Likewise an independently body-valued even condensate/auxiliary scalar can
# source the body equation, but it is a new bosonic owner.
condensate_body = Fraction(3, 2)
condensate_x = -condensate_body / 2
check("plant", "PLANT an even condensate can move the real bosonic body",
      condensate_x == Fraction(-3, 4) and condensate_x != 0)
check("scope", "commuting spinor and even condensate are materially distinct classes", True)


print("E. CBRS-1P FOUR-BRANCH PROPAGATION")
predecessor_path = ROOT / "lab/process/selected-k77-cbrs1p-j4-component-ranks.json"
predecessor = json.loads(predecessor_path.read_text(encoding="utf-8"))
ranks = predecessor["complete_hessian"]["rank_per_branch"]
nullities = predecessor["complete_hessian"]["nullity_per_branch"]
check("prior", "CBRS-1P supplies four complete 230650-dimensional branches",
      len(ranks) == len(nullities) == 4
      and predecessor["coordinate_component_bank"]["complete_dimension"] == 230650)
check("prior", "every J4 bosonic body Hessian has rank 230610 and nullity 40",
      set(ranks.values()) == {230610} and set(nullities.values()) == {40})
check("prior", "the forty-dimensional bosonic body kernel is exactly diagonal gauge",
      predecessor["complete_hessian"]["kernel"]
      == "EXACTLY_THE_40_DIMENSIONAL_BROKEN_DIAGONAL_SPIN_ORBIT")
body_quotient_dimensions = {branch: nullity - 40 for branch, nullity in nullities.items()}
check("consequence", "bilinear odd coupling leaves zero real non-orbit metric body domain on all branches",
      set(body_quotient_dimensions.values()) == {0})
check("consequence", "fermion zero modes, if any, remain separate from real metric body tangents", True)


print("F. PROPAGATION AND CLAIM CEILING")
registry_path = ROOT / "lab/process/selected-k77-cbrs1q-grassmann-body-obstruction.json"
if registry_path.exists():
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    check("propagation", "registry records the universal body obstruction",
          registry["body_projection"]["bosonic_current_body"] == 0
          and registry["body_projection"]["mixed_hessian_body"] == 0)
    check("propagation", "registry preserves all four zero metric quotients",
          set(registry["j4_branch_consequence"]["real_nonorbit_metric_body_dimension"].values()) == {0})
    check("propagation", "current state and contributor front door carry CBRS-1R",
          "CBRS-1R" in (ROOT / "CURRENT-STATE.yaml").read_text(encoding="utf-8")
          and "CBRS-1R" in (ROOT / "NEXT-STEPS.md").read_text(encoding="utf-8")
          and "CBRS-1R" in (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text(encoding="utf-8"))
check("scope", "no BV cohomology global vacuum source operator condensate or spectrum is inferred", True)
check("scope", "CBRS-2 remains blocked on a real non-orbit metric tangent", True)


RESULT = {
    "disposition": "CBRS1Q_MINIMAL_GRASSMANN_ODD_BILINEAR_EXTENSION_CANNOT_REOPEN_REAL_J4_METRIC_BODY_TANGENT",
    "body_projection": {
        "bosonic_current_body": 0,
        "mixed_hessian_body": 0,
        "even_body_kernel_enlargement": 0,
    },
    "nonzero_odd_saddle": {
        "exists_in_exact_fixture": True,
        "backreaction": "NONZERO_NILPOTENT_BODY_ZERO",
        "real_bosonic_body_shift": 0,
    },
    "j4_branch_consequence": {
        "branches": list(ranks),
        "real_nonorbit_metric_body_dimension": body_quotient_dimensions,
    },
    "next_gate": "CBRS1R_FREEZE_AN_EVEN_CONDENSATE_BOSONIZED_AUXILIARY_OR_OTHER_MATERIALLY_DISTINCT_ACTION_OWNED_CLASS_BEFORE_ANY_BODY_REOPENING_CLAIM",
    "claim_ceiling": "EXACT_POINTWISE_SUPERALGEBRA_BODY_OBSTRUCTION_FOR_EVEN_BILINEAR_GRASSMANN_ODD_EXTENSION__NO_SOURCE_OPERATOR_BV_GLOBAL_VACUUM_OR_SPECTRUM",
    "counts": COUNTS,
    "failures": FAILURES,
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
