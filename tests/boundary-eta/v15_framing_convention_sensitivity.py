#!/usr/bin/env python3
"""V15-5 exact arithmetic for the framed RP^3 convention chain.

This certificate does not derive the GU-specific identification

    Lambda^2_+ twist = natural tangential framing on RP^3.

It takes that reconstruction-grade identification as a declared premise and
checks the resulting characteristic-class, stabilization, Adams, and CRT
arithmetic.  It also separates:

* viable sign conventions for the same oriented framed-cycle data;
* factor-of-two misnormalizations, retained as sensitivity diagnostics; and
* different objects/premise failures (a shifted framing or gauge coefficient).

No floating point and no third-party packages are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd


MODULUS = 24
P1_MAGNITUDE = 4
STABILIZATION_FACTOR = 2
ADAMS_GENERATOR = Fraction(1, 24)


def additive_order_mod(value: int, modulus: int) -> int:
    """Additive order of value in Z/modulus."""
    return modulus // gcd(modulus, value % modulus)


def additive_order_qz(value: Fraction) -> int:
    """Additive order of a rational value in Q/Z."""
    return value.denominator


def mod_one(value: Fraction) -> Fraction:
    """Canonical representative of a rational class in Q/Z."""
    return Fraction(value.numerator % value.denominator, value.denominator)


def crt_coordinates(value: int) -> tuple[int, int]:
    """Z/24 -> Z/8 x Z/3."""
    return value % 8, value % 3


def project_two_primary(value: int) -> int:
    """CRT projection to the subgroup Z/8 inside Z/24.

    The idempotent 9 is 1 mod 8 and 0 mod 3.
    """
    return (9 * value) % MODULUS


def project_three_primary(value: int) -> int:
    """CRT projection to the subgroup Z/3 inside Z/24.

    The idempotent 16 is 0 mod 8 and 1 mod 3.
    """
    return (16 * value) % MODULUS


def verify_crt_projectors() -> None:
    """Exhaustively verify the exact CRT projector identities."""
    for value in range(MODULUS):
        two = project_two_primary(value)
        three = project_three_primary(value)
        assert (two + three) % MODULUS == value
        assert project_two_primary(two) == two
        assert project_three_primary(three) == three
        assert project_three_primary(two) == 0
        assert project_two_primary(three) == 0
        assert crt_coordinates(two)[1] == 0
        assert crt_coordinates(three)[0] == 0


@dataclass(frozen=True)
class Outcome:
    degree: int
    z24_class: int
    e_signed: Fraction
    e_mod_one: Fraction
    crt: tuple[int, int]
    two_primary_class: int
    three_primary_class: int
    full_order: int
    qz_order: int
    three_primary_order: int
    has_nonzero_three_primary: bool


def outcome_from_degree(degree: int) -> Outcome:
    """Apply J, Adams e_R, and CRT to an integral stable-framing degree."""
    z24_class = degree % MODULUS
    e_signed = degree * ADAMS_GENERATOR
    e_mod_one = mod_one(e_signed)
    two = project_two_primary(z24_class)
    three = project_three_primary(z24_class)
    return Outcome(
        degree=degree,
        z24_class=z24_class,
        e_signed=e_signed,
        e_mod_one=e_mod_one,
        crt=crt_coordinates(z24_class),
        two_primary_class=two,
        three_primary_class=three,
        full_order=additive_order_mod(z24_class, MODULUS),
        qz_order=additive_order_qz(e_mod_one),
        three_primary_order=additive_order_mod(three, MODULUS),
        has_nonzero_three_primary=(three != 0),
    )


def print_outcome(prefix: str, result: Outcome) -> None:
    print(
        f"{prefix:<31} "
        f"d={result.degree:+3d}  "
        f"class={result.z24_class:>2d}  "
        f"e_R={str(result.e_signed):>5} "
        f"(mod 1 {str(result.e_mod_one):>5})  "
        f"CRT={result.crt}  "
        f"P2={result.two_primary_class:>2d}  "
        f"P3={result.three_primary_class:>2d}  "
        f"orders(full,e,P3)="
        f"({result.full_order},{result.qz_order},{result.three_primary_order})"
    )


@dataclass(frozen=True)
class SensitivityBranch:
    name: str
    factor_from_canonical: Fraction
    branch_type: str
    viable_same_cycle_convention: bool
    expected_three_primary: bool


def integral_degree(factor: Fraction, sign: int) -> int:
    degree = Fraction(sign * 2) * factor
    assert degree.denominator == 1, (factor, degree)
    return degree.numerator


def check_canonical_chain() -> None:
    print("V15-5 FRAMED RP^3 CONVENTION AND SENSITIVITY CERTIFICATE")
    print("=" * 96)
    print("Declared geometric input:")
    print("  M = RP^3 = L(2;1), natural fiber-preserving/right-handed Lie framing;")
    print("  orientation is the boundary orientation of the Euler +2 disk-bundle filling.")
    print("  GU dependency: Lambda^2_+ is identified with this exact tangential framing.")
    print()
    print("Sourced normalization chain:")
    print("  charge-one adjoint clutching generator in pi_3(SO(3)): rho = +/-1")
    print("  p1[W,M] = +/-4; (p1/2)[W,M] = +/-2")
    print("  stabilization pi_3(SO(3))->pi_3(SO): rho |-> 2 sigma")
    print("  Adams: nu=J(sigma), e_R(nu)=1/24")
    print()

    verify_crt_projectors()

    canonical: dict[int, Outcome] = {}
    for sign in (1, -1):
        p1_number = sign * P1_MAGNITUDE
        half_p1_degree = p1_number // 2
        stabilized_degree = sign * STABILIZATION_FACTOR
        assert p1_number % 2 == 0
        assert half_p1_degree == stabilized_degree

        result = outcome_from_degree(stabilized_degree)
        canonical[sign] = result
        print_outcome("canonical sign +1" if sign == 1 else "canonical sign -1", result)

        assert result.e_signed == sign * Fraction(1, 12)
        assert result.z24_class == (sign * 2) % MODULUS
        assert result.full_order == 12
        assert result.qz_order == 12
        assert result.three_primary_order == 3
        assert result.has_nonzero_three_primary

    assert canonical[1].crt == (2, 2)
    assert canonical[-1].crt == (6, 1)
    assert canonical[1].three_primary_class == 8
    assert canonical[-1].three_primary_class == 16
    print("  PASS: both signs have full order 12; only P3 has order 3, and P3 is nonzero.")
    print()


def check_sign_sources() -> None:
    """Every orientation/generator sign combination reduces to the two signs."""
    outcomes: dict[int, int] = {1: 0, -1: 0}
    for orientation_sign in (1, -1):
        for clutching_sign in (1, -1):
            for stable_generator_sign in (1, -1):
                for adams_sign in (1, -1):
                    net = (
                        orientation_sign
                        * clutching_sign
                        * stable_generator_sign
                        * adams_sign
                    )
                    result = outcome_from_degree(net * 2)
                    outcomes[net] += 1
                    assert result.full_order == 12
                    assert result.three_primary_order == 3
                    assert result.has_nonzero_three_primary
    assert outcomes == {1: 8, -1: 8}
    print("Sign-source audit:")
    print("  orientation, clutching/self-duality, stable-generator, and Adams-sign choices")
    print("  give 8 copies of +2 and 8 copies of -2; all preserve nonzero order-3 P3.")
    print()


def check_factor_sensitivity() -> None:
    branches = (
        SensitivityBranch(
            "canonical x2 / p1-over-2",
            Fraction(1),
            "sourced normalization",
            True,
            True,
        ),
        SensitivityBranch(
            "omit stabilization x2",
            Fraction(1, 2),
            "diagnostic: contradicts sourced x2",
            False,
            True,
        ),
        SensitivityBranch(
            "use p1 as stable degree",
            Fraction(2),
            "diagnostic: double-counts x2",
            False,
            True,
        ),
        SensitivityBranch(
            "multiply by adjoint rank 3",
            Fraction(3),
            "invalid: rank is not a framing convention",
            False,
            False,
        ),
        SensitivityBranch(
            "gauge/coefficient, no framing",
            Fraction(0),
            "different object / GU premise failure",
            False,
            False,
        ),
    )

    print("Factor and construction sensitivity (each row asserted for both signs):")
    viable_erasing: list[str] = []
    for branch in branches:
        signed_results = [
            outcome_from_degree(integral_degree(branch.factor_from_canonical, sign))
            for sign in (1, -1)
        ]
        for result in signed_results:
            assert (
                result.has_nonzero_three_primary
                == branch.expected_three_primary
            ), branch.name
        if (
            branch.viable_same_cycle_convention
            and not all(r.has_nonzero_three_primary for r in signed_results)
        ):
            viable_erasing.append(branch.name)

        plus, minus = signed_results
        status = "PRESERVES P3" if plus.has_nonzero_three_primary else "ERASES P3"
        print(
            f"  {branch.name:<30} "
            f"d=({plus.degree:+d},{minus.degree:+d}) "
            f"class=({plus.z24_class},{minus.z24_class}) "
            f"full-order=({plus.full_order},{minus.full_order}) "
            f"{status}; {branch.branch_type}"
        )

    assert not viable_erasing, viable_erasing
    print("  PASS: no viable convention for the same framed cycle erases P3.")
    print("  NOTE: rank-3 multiplication and the gauge/no-framing branch erase P3, but")
    print("        neither is a convention for the same oriented framed cycle.")
    print()


def check_changed_framing_object() -> None:
    """Show the sensitivity to changing, rather than renaming, the framing."""
    print("Different-framed-cycle sensitivity:")
    print("  A stable-framing shift k changes d=2 to d=2+k; this changes the object.")
    erasing_shifts: list[int] = []
    for shift in range(-3, 4):
        result = outcome_from_degree(2 + shift)
        if not result.has_nonzero_three_primary:
            erasing_shifts.append(shift)
        print(
            f"    k={shift:+d}: d={result.degree:+d}, class={result.z24_class:>2d}, "
            f"P3={result.three_primary_class:>2d}, "
            f"{'NONZERO' if result.has_nonzero_three_primary else 'ZERO'}"
        )
    assert erasing_shifts == [-2, 1]
    print("  Exact rule: P3 vanishes iff 2+k == 0 (mod 3), i.e. k == 1 (mod 3).")
    print("  This is why the exact GU-to-natural-framing identification is a premise;")
    print("  arbitrary tangentiality without the framing class is insufficient.")
    print()


def main() -> None:
    check_canonical_chain()
    check_sign_sources()
    check_factor_sensitivity()
    check_changed_framing_object()
    print("STOP CHECK: NOT TRIGGERED by any viable sign/factor convention for the same cycle.")
    print("Premise guard: select gauge/no-framing or shift the natural framing by k=1 mod 3,")
    print("and the nonzero 3-primary manuscript claim must stop.")
    print("VERDICT: PASS_WITH_DECLARED_GU_TANGENTIAL_IDENTIFICATION_PREMISE")


if __name__ == "__main__":
    main()
