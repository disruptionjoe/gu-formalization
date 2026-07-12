#!/usr/bin/env python3
r"""
W55 / Path-2 Wave-2 Target 2 -- two-loop CLOP pinch pre-gate for the Lee-Wick / fakeon family.

Target 2 from the Path-2 wave-1 synthesis asks whether the removal-based family (Lee-Wick / fakeon)
is stable beyond the one-loop proof-of-concept. Branch D (W51) showed that the Stelle spin-2 ghost
admits the Lee-Wick treatment at one loop: the pole leaves the real axis as a complex-conjugate pair
and the GOW cut on real external states carries no negative ghost contribution.

This file does NOT compute a full two-loop gravity amplitude. It turns the named obstruction into a
deterministic gate:

  * A single Lee-Wick pole is off the real s-axis, so the one-loop ghost cut is empty.
  * At two-loop order, a mixed pair of conjugate Lee-Wick resonances has threshold

        s_mix = (m_+ + m_-)^2 = (2 M)^2

    exactly on the real external-energy axis. Same-sign thresholds (m_+ + m_+)^2 and
    (m_- + m_-)^2 stay off-axis.
  * Therefore the mixed threshold is the CLOP pinch candidate. Scalar Lee-Wick/GOW has a known
    prescription for this kind of threshold in the narrow, non-derivative setting; broad derivative
    gravity does not automatically inherit that theorem.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md discipline):
  * "The ghost": Lee-Wick complex-pole resonance, not GU-native keep-and-grade Krein positivity and
    not positive-Hilbert removal. This is the Family-2 construction Target 2 is testing.
  * "The cutting rules": CLOP/GOW deformed contour around complex-conjugate poles, not ordinary
    real-axis Cutkosky cutting through a stable ghost.
  * "The obstruction": a two-resonance mixed threshold / contour pinch candidate. This is a
    prescription-stability question, not a positivity verdict.

VERDICT (gate only): TARGET2_OPEN_WITH_PINCH_TARGET. The mixed threshold is unavoidable and real, so
the next valid Target 2 swing is a genuine two-loop tensor discontinuity / contour computation near
s = 4 M^2. No H59, GU, canon, claim-status, or public-posture verdict changes.

Reproducible: python tests/W55_path2_target2_clop_pinches.py
"""
from __future__ import annotations

from dataclasses import dataclass

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


@dataclass(frozen=True)
class LeeWickCase:
    name: str
    mass: float
    gamma_over_m: float
    derivative_power: int
    tensor_numerator: bool
    scalar_clop_theorem_available: bool

    @property
    def gamma(self) -> float:
        return self.gamma_over_m * self.mass

    @property
    def m_plus(self) -> complex:
        return complex(self.mass, +0.5 * self.gamma)

    @property
    def m_minus(self) -> complex:
        return complex(self.mass, -0.5 * self.gamma)

    @property
    def s_pole_plus(self) -> complex:
        # Same normalization as W51: the pole in s=p^2 is off-axis by M*Gamma.
        return complex(self.mass * self.mass, self.mass * self.gamma)


def threshold(a: complex, b: complex) -> complex:
    return (a + b) ** 2


def mixed_threshold(case: LeeWickCase) -> complex:
    return threshold(case.m_plus, case.m_minus)


def same_threshold_plus(case: LeeWickCase) -> complex:
    return threshold(case.m_plus, case.m_plus)


def same_threshold_minus(case: LeeWickCase) -> complex:
    return threshold(case.m_minus, case.m_minus)


def inherited_scalar_clop_gate(case: LeeWickCase) -> bool:
    """Sufficient gate for inheriting the scalar Lee-Wick/GOW contour theorem.

    This is intentionally conservative. Failing it is not a kill; it means Target 2 still needs the
    actual two-loop contour/discontinuity computation for this case.
    """
    return (
        case.scalar_clop_theorem_available
        and case.gamma_over_m <= 0.10
        and case.derivative_power == 0
        and not case.tensor_numerator
    )


def pinch_weight_proxy(case: LeeWickCase) -> float:
    """A non-verdict proxy for numerator severity at the mixed threshold.

    Derivative gravitational vertices weight the pinched region by powers of s. This does not prove
    a pinch; it only shows that derivative numerators amplify rather than erase the candidate region.
    """
    s_mix = mixed_threshold(case).real
    return s_mix ** case.derivative_power


log("=" * 96)
log("W55 / PATH-2 WAVE-2 TARGET 2 -- TWO-LOOP CLOP PINCH PRE-GATE")
log("=" * 96)

scalar = LeeWickCase(
    name="narrow scalar Lee-Wick reference",
    mass=1.0,
    gamma_over_m=0.01,
    derivative_power=0,
    tensor_numerator=False,
    scalar_clop_theorem_available=True,
)
gravity = LeeWickCase(
    name="broad derivative-coupled gravitational resonance",
    mass=1.0,
    gamma_over_m=1.0,
    derivative_power=4,
    tensor_numerator=True,
    scalar_clop_theorem_available=False,
)

log("")
log("1. One-loop pole location versus two-resonance thresholds")
log(f"   scalar  s_pole+ = {scalar.s_pole_plus}")
log(f"   gravity s_pole+ = {gravity.s_pole_plus}")

check(
    "P1  a single Lee-Wick pole is off the real s-axis, so the one-loop real-axis ghost cut is empty "
    "(Branch D's one-loop mechanism)",
    abs(scalar.s_pole_plus.imag) > TOL and abs(gravity.s_pole_plus.imag) > TOL,
    f"Im scalar pole={scalar.s_pole_plus.imag:.3g}; Im gravity pole={gravity.s_pole_plus.imag:.3g}",
)

for case in (scalar, gravity):
    s_pm = mixed_threshold(case)
    s_pp = same_threshold_plus(case)
    s_mm = same_threshold_minus(case)
    log("")
    log(f"   {case.name}:")
    log(f"     m+ = {case.m_plus}, m- = {case.m_minus}")
    log(f"     s(++): {s_pp}")
    log(f"     s(--): {s_mm}")
    log(f"     s(+-): {s_pm}")

    check(
        f"T1  {case.name}: same-sign Lee-Wick thresholds stay off the real axis",
        abs(s_pp.imag) > TOL and abs(s_mm.imag) > TOL and abs(s_pp.imag + s_mm.imag) < TOL,
        f"Im s(++)={s_pp.imag:.3g}, Im s(--)={s_mm.imag:.3g}",
    )
    check(
        f"T2  {case.name}: the mixed conjugate threshold s(+-)=(m+ + m-)^2 is EXACTLY real",
        abs(s_pm.imag) < TOL and abs(s_pm.real - 4.0 * case.mass * case.mass) < TOL,
        f"s(+-)={s_pm.real:.6g}+{s_pm.imag:.3g}i",
    )

log("")
log("2. Width does not move the mixed threshold off the real axis")
for ratio in (0.001, 0.05, 0.5, 1.0, 2.0):
    c = LeeWickCase(
        name=f"gamma/M={ratio}",
        mass=1.0,
        gamma_over_m=ratio,
        derivative_power=0,
        tensor_numerator=False,
        scalar_clop_theorem_available=False,
    )
    check(
        f"W{ratio:g}  mixed threshold remains real even when Gamma/M changes",
        abs(mixed_threshold(c).imag) < TOL and abs(mixed_threshold(c).real - 4.0) < TOL,
        f"s_mix={mixed_threshold(c)}",
    )

log("")
log("3. Scalar-inheritance gate versus gravitational Target-2 gate")
check(
    "G1  narrow scalar Lee-Wick reference satisfies the conservative scalar CLOP inheritance gate",
    inherited_scalar_clop_gate(scalar),
    "narrow width, no derivative numerator, scalar theorem available",
)
check(
    "G2  broad derivative-coupled gravity FAILS the scalar-inheritance gate: this is not a kill, but "
    "it blocks automatic reuse of the scalar all-orders proof",
    not inherited_scalar_clop_gate(gravity),
    "broad width + derivative tensor numerator + no gravity-specific CLOP theorem",
)

scalar_weight = pinch_weight_proxy(scalar)
gravity_weight = pinch_weight_proxy(gravity)
check(
    "G3  derivative gravitational numerators amplify the mixed-threshold region in the proxy model; "
    "they do not remove the pinch candidate",
    gravity_weight > scalar_weight,
    f"proxy weight scalar={scalar_weight:.3g}, gravity={gravity_weight:.3g}",
)

log("")
log("4. Counterterm and prescription guards")
shifted = LeeWickCase(
    name="real mass counterterm",
    mass=1.3,
    gamma_over_m=gravity.gamma_over_m,
    derivative_power=gravity.derivative_power,
    tensor_numerator=gravity.tensor_numerator,
    scalar_clop_theorem_available=False,
)
check(
    "C1  a real mass counterterm moves the real location of the mixed threshold but cannot give it an "
    "imaginary contour margin",
    abs(mixed_threshold(shifted).imag) < TOL and mixed_threshold(shifted).real > mixed_threshold(gravity).real,
    f"s_mix shifted={mixed_threshold(shifted)}",
)

TARGET2_SETTLED = False
PINCH_CANDIDATE_IDENTIFIED = True
NEXT_COMPUTATION_IS_TWO_LOOP_TENSOR_CONTOUR = True
check(
    "H1  honesty guard: the gate identifies the real mixed conjugate-pole threshold and scalar-inheritance "
    "failure, but it does NOT settle Target 2 or H59",
    (not TARGET2_SETTLED) and PINCH_CANDIDATE_IDENTIFIED and NEXT_COMPUTATION_IS_TWO_LOOP_TENSOR_CONTOUR,
    "status = TARGET2_OPEN_WITH_PINCH_TARGET",
)

log("")
log("=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W55 Target-2 CLOP pinch checks failed"

log("")
log("VERDICT (gate only): TARGET2_OPEN_WITH_PINCH_TARGET.")
log("  The one-loop Lee-Wick pole is off-axis, but a two-resonance mixed conjugate-pole threshold")
log("  lies exactly on the real external-energy axis at s=4M^2. This is the CLOP pinch candidate.")
log("  Same-sign thresholds are off-axis; width changes do not move the mixed threshold away.")
log("  Narrow scalar Lee-Wick inherits the known CLOP/GOW theorem. Broad derivative-coupled gravity")
log("  does not automatically inherit it; the next valid Target 2 work is a two-loop tensor")
log("  discontinuity / contour computation near the mixed threshold. H59 remains OPEN.")
raise SystemExit(0)
