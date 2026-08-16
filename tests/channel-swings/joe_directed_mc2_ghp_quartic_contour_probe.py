#!/usr/bin/env python3
"""MC-2 exact phase/contour classifier for the SRC-3/SRC-4 potential.

This probe declares only the formal Euclidean horn

    Z_Gamma = integral_Gamma exp(-V(z)) dz.

It does not assert that GU is Euclidean, choose Gamma, modify the source real
structure, or construct a physical domain.  It decides what a *uniform straight
phase* z = exp(i theta) x can and cannot do to the banked degree-two, degree-three
and degree-four terms.

Run:
    python3 tests/channel-swings/joe_directed_mc2_ghp_quartic_contour_probe.py
    python3 tests/channel-swings/joe_directed_mc2_ghp_quartic_contour_probe.py --self-test
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
MUTATION = ""
if len(sys.argv) > 1 and sys.argv[1].startswith("--mutate="):
    MUTATION = sys.argv[1].split("=", 1)[1]

CHECKS: list[tuple[str, bool]] = []


def check(label: str, condition: object) -> None:
    CHECKS.append((label, bool(condition)))


@dataclass(frozen=True)
class RootPhase:
    """The exact root of unity exp(2 pi i * exponent / order)."""

    order: int
    exponent: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "exponent", self.exponent % self.order)

    def power(self, degree: int) -> "RootPhase":
        return RootPhase(self.order, self.exponent * degree)

    def is_one(self) -> bool:
        return self.exponent == 0

    def is_minus_one(self) -> bool:
        return self.order % 2 == 0 and self.exponent == self.order // 2

    def is_real(self) -> bool:
        return self.is_one() or self.is_minus_one()

    def is_pure_imaginary(self) -> bool:
        return self.order % 4 == 0 and self.exponent in (
            self.order // 4,
            3 * self.order // 4,
        )

    def rational_real_part(self) -> Fraction:
        """Return cos(2*pi*exponent/order) when its exact value is rational."""
        angle = Fraction(self.exponent, self.order) % 1
        values = {
            Fraction(0): Fraction(1),
            Fraction(1, 6): Fraction(1, 2),
            Fraction(1, 4): Fraction(0),
            Fraction(1, 3): Fraction(-1, 2),
            Fraction(1, 2): Fraction(-1),
            Fraction(2, 3): Fraction(-1, 2),
            Fraction(3, 4): Fraction(0),
            Fraction(5, 6): Fraction(1, 2),
        }
        if angle not in values:
            raise ValueError(f"cosine is not rational at angle fraction {angle}")
        value = values[angle]
        if MUTATION == "pi6-quadratic-realpart-wrong" and angle == Fraction(1, 6):
            return -value
        return value


ONE = RootPhase(1, 0)
I = RootPhase(4, 1)
E_PI_4 = RootPhase(8, 1)
E_PI_6 = RootPhase(12, 1)


print("A. EXACT DEGREE-PHASE ALGEBRA")

iz_quartic = I.power(4)
if MUTATION == "iz-flips-quartic":
    iz_quartic = RootPhase(2, 1)
check("z -> i z leaves every quartic coefficient unchanged", iz_quartic.is_one())
check("z -> i z flips a quadratic coefficient", I.power(2).is_minus_one())
check("z -> i z rotates a cubic coefficient by -i", I.power(3).is_pure_imaginary())
check("degree-six control: z -> i z flips an even term with degree 2 mod 4", I.power(6).is_minus_one())

pi4_d2 = E_PI_4.power(2)
if MUTATION == "pi4-preserves-bilinear":
    pi4_d2 = ONE
check("theta=pi/4 flips a quartic coefficient", E_PI_4.power(4).is_minus_one())
check("theta=pi/4 makes every bilinear quadratic/kinetic coefficient imaginary", pi4_d2.is_pure_imaginary())
check("theta=pi/4 rotates degrees 1,2,3,4 by distinct phases",
      len({E_PI_4.power(d).exponent for d in (1, 2, 3, 4)}) == 4)


print("\nB. SRC-3 PRE-REDUCTION K+/- CONTRADICTION")

def executable_receipt(relative: str) -> tuple[int, str]:
    run = subprocess.run(
        [sys.executable, str(ROOT / relative)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    return run.returncode, run.stdout


src3_rc, src3_receipt = executable_receipt(
    "tests/channel-swings/joe_directed_potential_boundedness_probe.py"
)
cg1_rc, cg1_receipt = executable_receipt(
    "tests/channel-swings/joe_directed_coset_versus_gauge_probe.py"
)
src3_negative_match = re.search(r"BRANCH A explicit ray: K\(v\) = (-?\d+)", src3_receipt)
src3_positive_match = re.search(r"same bracket with one timelike internal leg: (-?\d+)", src3_receipt)
cg1_pre_match = re.search(
    r"SRC-3 ray under \(Killing, eta\): spacelike (-?\d+), mixed (-?\d+)",
    cg1_receipt,
)
cg1_post_match = re.search(
    r"same ray under \(B_theta, eta_plus\): spacelike (-?\d+), mixed (-?\d+)",
    cg1_receipt,
)

check("upstream SRC-3 executable receipt passes", src3_rc == 0)
check("upstream CG-1 executable receipt passes", cg1_rc == 0)
check("SRC-3 receipt exposes both exact ray coefficients",
      src3_negative_match is not None and src3_positive_match is not None)
check("CG-1 receipt exposes exact pre/post pairing coefficients",
      cg1_pre_match is not None and cg1_post_match is not None)

K_MINUS = int(src3_negative_match.group(1)) if src3_negative_match else 0
K_PLUS = int(src3_positive_match.group(1)) if src3_positive_match else 0
CG1_PRE = tuple(map(int, cg1_pre_match.groups())) if cg1_pre_match else ()
CG1_POST = tuple(map(int, cg1_post_match.groups())) if cg1_post_match else ()
check("SRC-3 and CG-1 independently agree on the pre-reduction -4/+4 pair",
      (K_MINUS, K_PLUS) == CG1_PRE == (-4, 4))
check("CG-1 banks the post-reduction +4/+4 control", CG1_POST == (4, 4))

if MUTATION == "drop-positive-ray":
    K_PLUS = -4


def required_cosine_sign(coefficient: int) -> int:
    """For Re(K exp(4i theta))>0, return the required sign of cos(4theta)."""
    assert coefficient != 0
    return 1 if coefficient > 0 else -1


requirements = {required_cosine_sign(K_MINUS), required_cosine_sign(K_PLUS)}
check("SRC-3 live controls retain one negative and one positive quartic ray",
      (K_MINUS, K_PLUS) == (-4, 4))
check("the negative ray requires cos(4 theta)<0", required_cosine_sign(K_MINUS) == -1)
check("the positive ray requires cos(4 theta)>0", required_cosine_sign(K_PLUS) == 1)
check("no uniform scalar phase makes both pre-reduction quartic rays damp",
      requirements == {-1, 1})
check("theta=pi/4 repairs K=-4 only by turning K=+4 negative",
      (-K_MINUS, -K_PLUS) == (4, -4))

# For the isolated negative ray, the four exact wedge centres are odd*pi/4.
centres = [RootPhase(8, k) for k in (1, 3, 5, 7)]
boundaries = [RootPhase(16, k) for k in (1, 3, 5, 7, 9, 11, 13, 15)]
check("all four isolated-ray decay-wedge centres flip the quartic sign",
      all(phase.power(4).is_minus_one() for phase in centres))
check("the eight wedge boundaries have purely imaginary quartic phase and zero damping",
      all(phase.power(4).is_pure_imaginary() for phase in boundaries))


print("\nC. ORIGINAL REALITY AND SOURCE GRAMMAR")

# The line exp(i theta) R is preserved by ordinary conjugation exactly when
# exp(-2 i theta) is real.  Then exp(4 i theta)=1, so an invariant straight
# line cannot flip a negative quartic.
def conjugation_preserves_line(phase: RootPhase) -> bool:
    return RootPhase(phase.order, -2 * phase.exponent).is_real()


pi4_reality = conjugation_preserves_line(E_PI_4)
if MUTATION == "source-line-pi4-real":
    pi4_reality = True
check("the pi/4 line is not preserved by the original conjugation", not pi4_reality)
check("the real line is preserved by the original conjugation", conjugation_preserves_line(ONE))
check("the imaginary line is preserved by the original conjugation", conjugation_preserves_line(I))
check("both original-reality-preserving cardinal lines leave a quartic unchanged",
      ONE.power(4).is_one() and I.power(4).is_one())
check("a pi/4 slice needs a modified antilinear reality rather than the source one",
      (not conjugation_preserves_line(E_PI_4)) and E_PI_4.power(4).is_minus_one())

# Bracket closure of exp(i theta) g_R would require exp(2i theta) g_R to equal
# exp(i theta) g_R by a real scalar, hence exp(i theta) itself must be real.
check("the pi/4 rotated real form is not closed under the original real Lie bracket",
      not E_PI_4.is_real())
check("the unrotated source real form passes the bracket-closure control", ONE.is_real())


print("\nD. CUBIC STRAIGHT-LINE CEILING")

# Along a straight line, the real leading cubic coefficient at -infinity is
# the negative of the coefficient at +infinity.  Strict damping at both ends
# is impossible.  If it is zero, lower even degree must supply damping.
A_PLUS = 7
A_MINUS = -A_PLUS
if MUTATION == "cubic-same-end-sign":
    A_MINUS = A_PLUS
check("a nonzero real cubic has opposite leading signs at the two ends of a straight line",
      A_PLUS == -A_MINUS and A_PLUS != 0)
check("strict cubic damping at both ends of one straight line is impossible",
      not (A_PLUS > 0 and A_MINUS > 0))
check("theta=pi/6 makes a real cubic purely imaginary", E_PI_6.power(3).is_pure_imaginary())
pi6_quadratic_real_part = E_PI_6.power(2).rational_real_part()
check("theta=pi/6 derives exact quadratic real part cos(pi/3)=1/2 from the phase",
      pi6_quadratic_real_part == Fraction(1, 2))
check("the pi/6 cubic control is conditional on a coercive quadratic",
      E_PI_6.power(3).is_pure_imaginary() and pi6_quadratic_real_part > 0)


print("\nE. POST-REDUCTION AND GHP CONTROLS")

POST_K = 4
if MUTATION == "post-real-negative":
    POST_K = -4
check("post-reduction positive quartic damps on the unrotated real line", POST_K > 0)
check("a pi/4 rotation would make that post-reduction positive quartic divergent", -POST_K < 0)
check("negative-quadratic GHP control is repaired by z -> i z",
      (-1) * (-1) == 1)
check("negative-quartic target differs from the GHP control because i^4=+1",
      I.power(2).is_minus_one() and I.power(4).is_one())

# A quartic-flat subspace controlled by an indefinite quadratic has the same
# uniform-phase contradiction, now with cos(2 theta).
quadratic_requirements = {
    required_cosine_sign(-3),
    required_cosine_sign(5),
}
check("an indefinite quadratic on quartic-flat rays also defeats one uniform phase",
      quadratic_requirements == {-1, 1})
check("under the declared positive-composite horn, the post-reduction real line needs no repair",
      POST_K > 0 and required_cosine_sign(5) == 1)


print("\nF. SOURCE CUSTODY AND CLAIM CEILING")

artifact = (ROOT / "lab/active-research/joe-directed/metric-cone-boundedness/"
            "mc2-ghp-contour-does-not-repair-indefinite-quartic-2026-08-16.md").read_text(
                encoding="utf-8"
            )
for phrase in (
    "FORMAL-EUCLIDEAN-CYCLE",
    "NO_SOURCE_REALITY_PRESERVING_UNIFORM_PHASE_REPAIR",
    "NO_FULL_PRE_REDUCTION_UNIFORM_COERCIVITY",
    "DOES_NOT_PROVE_THAT_NO_COMPLEX_THIMBLE_EXISTS",
    "TYPE_MISSING[INTEGRATION_CYCLE]",
    "TYPE_MISSING[EUCLIDEANIZATION]",
    "TYPE_MISSING[PHYSICAL_DOMAIN]",
    "SOURCE_NATIVE_ROUTE",
):
    check("artifact carries required scope phrase: " + phrase, phrase in artifact)

check("artifact distinguishes formal pointwise sign from a legitimate contour",
      "Pointwise sign is not a contour" in artifact)
check("artifact keeps non-straight Picard-Lefschetz cycles open",
      "Picard--Lefschetz" in artifact and "not excluded" in artifact)
check("artifact preserves the post-reduction pairing horn",
      "POST-E2-POS" in artifact and "PRE-E2-INDEF" in artifact)
check("artifact cites both W78 and W122 only as scope prior art",
      "W78" in artifact and "W122" in artifact and "scope prior art" in artifact)


def finish() -> int:
    failures = [label for label, ok in CHECKS if not ok]
    for label, ok in CHECKS:
        print(f"{'PASS' if ok else 'FAIL'}: {label}")
    print(f"\nMC-2: {len(CHECKS) - len(failures)}/{len(CHECKS)} checks pass")
    if failures:
        return 1
    print("RESULT: no source-reality-preserving uniform phase repairs SRC-3's full indefinite quartic;")
    print("        z->iz leaves quartics unchanged, while non-straight thimbles remain unselected and open.")
    return 0


if "--self-test" in sys.argv:
    mutations = (
        "iz-flips-quartic",
        "drop-positive-ray",
        "pi4-preserves-bilinear",
        "source-line-pi4-real",
        "cubic-same-end-sign",
        "pi6-quadratic-realpart-wrong",
        "post-real-negative",
    )
    script = Path(__file__).resolve()
    rejected = 0
    for mutation in mutations:
        run = subprocess.run(
            [sys.executable, str(script), f"--mutate={mutation}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if run.returncode != 0:
            rejected += 1
        print(f"{'PASS' if run.returncode != 0 else 'FAIL'} MUTANT: {mutation}")
    print(f"SELF-TEST: {rejected}/{len(mutations)} mutants rejected")
    raise SystemExit(0 if rejected == len(mutations) else 1)

raise SystemExit(finish())
