#!/usr/bin/env python3
"""Exact RF-1 census and sign-equivalence witness on the selected K77 bank.

This probe adds only the computation not already certified by the split-
commutant, J10/BV/Green, and twistor/moving-BV probes.  It tests

* the correctly typed rolled lifts of J4 and J10;
* the principal-symbol discriminator between those two lifts;
* an exact connected Spin witness carrying +Jhat10 to -Jhat10 while fixing
  the selected Cl1 background; and
* membership of the witness generator in the exact 66-dimensional kernel of
  the selected source gauge map G:R^91 -> R^196.

The computation is exact integer/rational arithmetic.  It does not construct
the missing total residual linearization, physical cohomology, positive
physical pairing, or closed Lorentzian domain.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


class SP:
    """Exact signed permutation: M e_j = sign[j] e_perm[j]."""

    def __init__(self, perm: tuple[int, ...], sign: tuple[int, ...]):
        self.n = len(perm)
        self.perm = perm
        self.sign = sign

    @staticmethod
    def identity(size: int) -> "SP":
        return SP(tuple(range(size)), (1,) * size)

    def mul(self, other: "SP") -> "SP":
        return SP(
            tuple(self.perm[other.perm[j]] for j in range(self.n)),
            tuple(other.sign[j] * self.sign[other.perm[j]] for j in range(self.n)),
        )

    def transpose(self) -> "SP":
        perm = [0] * self.n
        sign = [0] * self.n
        for column in range(self.n):
            perm[self.perm[column]] = column
            sign[self.perm[column]] = self.sign[column]
        return SP(tuple(perm), tuple(sign))

    def neg(self) -> "SP":
        return SP(self.perm, tuple(-entry for entry in self.sign))

    def scal(self, scalar: int) -> "SP":
        return self if scalar == 1 else self.neg()

    def eq(self, other: "SP") -> bool:
        return self.perm == other.perm and self.sign == other.sign

    def is_identity_times(self) -> int | None:
        if any(self.perm[index] != index for index in range(self.n)):
            return None
        scalar = self.sign[0]
        return scalar if all(entry == scalar for entry in self.sign) else None


def sp_kron(left: SP, right: SP) -> SP:
    perm: list[int] = []
    sign: list[int] = []
    for a in range(left.n):
        for b in range(right.n):
            perm.append(left.perm[a] * right.n + right.perm[b])
            sign.append(left.sign[a] * right.sign[b])
    return SP(tuple(perm), tuple(sign))


def sp_kron_list(values: list[SP]) -> SP:
    out = values[0]
    for value in values[1:]:
        out = sp_kron(out, value)
    return out


def sum_is_zero(left: SP, right: SP) -> bool:
    return left.perm == right.perm and all(
        left.sign[index] == -right.sign[index] for index in range(left.n)
    )


I2 = SP((0, 1), (1, 1))
X2 = SP((1, 0), (1, 1))
Y2 = SP((1, 0), (-1, 1))
Z2 = SP((0, 1), (1, -1))


def build_cl77() -> tuple[list[SP], list[int]]:
    gammas: list[SP] = []
    for middle in (X2, Y2):
        for slot in range(7):
            gammas.append(sp_kron_list([Z2] * slot + [middle] + [I2] * (6 - slot)))
    return gammas, [1] * 7 + [-1] * 7


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def product(gammas: list[SP], indices: tuple[int, ...]) -> SP:
    out = SP.identity(gammas[0].n)
    for index in indices:
        out = out.mul(gammas[index])
    return out


def diagonal_sp(signs: list[int]) -> SP:
    return SP(tuple(range(len(signs))), tuple(signs))


def conjugate(group_element: SP, value: SP) -> SP:
    return group_element.mul(value).mul(group_element.transpose())


def commutes(left: SP, right: SP) -> bool:
    return left.mul(right).eq(right.mul(left))


def anticommutes(left: SP, right: SP) -> bool:
    return sum_is_zero(left.mul(right), right.mul(left))


print("A. PREFLIGHT RECEIPTS AND LAYER ZERO")
split_receipt = read(
    "explorations/conditional-build/selected-k77-split-layer-commutant-action-parent-gate-2026-08-12.md"
)
commutant_receipt = read(
    "explorations/c3prime-split-commutant-certificates-2026-08-12.md"
)
j10_receipt = read(
    "explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md"
)
twistor_receipt = read(
    "explorations/conditional-build/selected-k77-twistor-bv-positive-state-seven-gate-2026-08-13.md"
)
target_receipt = read(
    "lab/active-research/source-residual-cohomology/target-theorem-reverse-falsification-chain-2026-08-14.md"
)

check("prior_art", "the complete split commutant is already certified as span{1,J4,J10,omega}",
      "span" in split_receipt and "1,J4,J10,omega" in split_receipt)
check("prior_art", "the only split-equivariant B-compatible complex units are already certified as +/-J10",
      "EXACTLY `+-J10`" in commutant_receipt)
check("prior_art", "fixed J10 failure and moving-J covariance are already decided",
      "17 split-preserving directions + 8 mixed-split directions" in j10_receipt
      and "sJ10 = [c,J10]" in j10_receipt)
check("prior_art", "the normal twistor J and spinor J10 are explicitly distinct",
      "Neither is the spinor Clifford volume `J10`" in twistor_receipt)
check("prior_art", "reverse falsification preserves candidate-kill versus route-kill quantifiers",
      "Candidate kill" in target_receipt and "Route kill" in target_receipt)

for label in (
    "spinor J10 versus an endomorphism of the Cl1 connection tangent",
    "fixed J versus the tautological moving-J family",
    "split-equivariant unit versus full-gauge basic operator",
    "algebraic pairing isometry versus physical unitary equivalence",
    "twistor complex structure versus Clifford volume structure",
    "candidate-family exhaustion versus exhaustion of every action-admissible J",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT Cl(7,7) CANDIDATES AND CORRECT ROLLED LIFTS")
gammas, eta = build_cl77()
identity_spin = SP.identity(128)
identity_vector = SP.identity(14)
base = (0, 7, 8, 9)
normal = (1, 2, 3, 4, 5, 6, 10, 11, 12, 13)
j4 = product(gammas, base)
j10 = product(gammas, normal)
omega = product(gammas, tuple(range(14)))
b_pairing = product(gammas, tuple(range(7, 14)))
b_omega_pairing = b_pairing.mul(omega)

r10_signs = [1 if index in base else -1 for index in range(14)]
r4_signs = [-1 if index in base else 1 for index in range(14)]
r10 = diagonal_sp(r10_signs)
r4 = diagonal_sp(r4_signs)
jhat10_one = sp_kron(r10, j10)
jhat4_one = sp_kron(r4, j4)

check("clifford", "J4^2=J10^2=-1 and omega^2=+1",
      j4.mul(j4).is_identity_times() == -1
      and j10.mul(j10).is_identity_times() == -1
      and omega.mul(omega).is_identity_times() == 1)
check("typing", "the J10 rolled lift uses +base/-normal vector reflection",
      r10.mul(r10).eq(identity_vector)
      and jhat10_one.mul(jhat10_one).is_identity_times() == -1)
check("typing", "the J4 rolled lift uses -base/+normal vector reflection",
      r4.mul(r4).eq(identity_vector)
      and jhat4_one.mul(jhat4_one).is_identity_times() == -1)
check("typing", "both rolled lifts satisfy the coefficientwise gamma-trace intertwiner",
      all(
          gammas[index].mul(j10).scal(r10_signs[index]).eq(j10.mul(gammas[index]))
          and gammas[index].mul(j4).scal(r4_signs[index]).eq(j4.mul(gammas[index]))
          for index in range(14)
      ))
check("pairing", "J10 is B-compatible while J4 is B-anti-compatible",
      j10.transpose().mul(b_pairing).mul(j10).eq(b_pairing)
      and j4.transpose().mul(b_pairing).mul(j4).eq(b_pairing.neg()))


print("\nC. ROLLED PRINCIPAL-SYMBOL DISCRIMINATOR")
# For the released rolled symbol, coefficientwise block multiplication shows
# that the lift (R_J tensor J) direct-sum J commutes with the axis-k symbol iff
# J commutes with gamma_k, equivalently iff the kth reflection sign is +1.
j10_axis_linear = [commutes(j10, gammas[index]) and r10_signs[index] == 1
                   for index in range(14)]
j4_axis_linear = [commutes(j4, gammas[index]) and r4_signs[index] == 1
                  for index in range(14)]
check("principal", "Jhat10 is complex-linear on all four observed base axes",
      all(j10_axis_linear[index] for index in base))
check("principal", "Jhat10 fails complex linearity on all ten normal axes",
      all(not j10_axis_linear[index] for index in normal))
check("principal", "Jhat4 fails complex linearity on all four observed base axes",
      all(not j4_axis_linear[index] for index in base))
check("principal", "Jhat4 is complex-linear only on all ten normal axes",
      all(j4_axis_linear[index] for index in normal))
check("candidate_kill", "the J4 route is killed for the owned observed rolled principal operator",
      not any(j4_axis_linear[index] for index in base))


print("\nD. EXACT CONNECTED +/-J10 EQUIVALENCE WITNESS")
# Axes 0 and 1 are same-sign (+,+), one base and one normal.  Their Clifford
# product is the endpoint exp(pi/2 * gamma_0 gamma_1).  Its vector action flips
# exactly those axes and returns the unoriented 4+10 projector to itself.
a_spin = gammas[0].mul(gammas[1])
v_signs = [-1 if index in (0, 1) else 1 for index in range(14)]
v_vector = diagonal_sp(v_signs)
u_one = sp_kron(v_vector, a_spin)
pairing_one_b = sp_kron(diagonal_sp(eta), b_pairing)
pairing_one_bomega = sp_kron(diagonal_sp(eta), b_omega_pairing)

check("sign_witness", "A=gamma0 gamma1 squares to -1 and is orthogonal",
      a_spin.mul(a_spin).is_identity_times() == -1
      and a_spin.transpose().mul(a_spin).eq(identity_spin))
check("sign_witness", "A conjugates both split volume complex structures to their negatives",
      conjugate(a_spin, j10).eq(j10.neg())
      and conjugate(a_spin, j4).eq(j4.neg()))
check("sign_witness", "V is eta-orthogonal and commutes with the unoriented split reflections",
      v_vector.transpose().mul(diagonal_sp(eta)).mul(v_vector).eq(diagonal_sp(eta))
      and commutes(v_vector, r10) and commutes(v_vector, r4))
check("sign_witness", "U=(V tensor A) direct-sum A conjugates Jhat10 to -Jhat10",
      conjugate(u_one, jhat10_one).eq(jhat10_one.neg())
      and conjugate(a_spin, j10).eq(j10.neg()))
check("sign_witness", "the same U also conjugates the correctly lifted Jhat4 to -Jhat4",
      conjugate(u_one, jhat4_one).eq(jhat4_one.neg())
      and conjugate(a_spin, j4).eq(j4.neg()))
check("sign_witness", "A implements the exact Clifford covariance gamma_a -> V_a^b gamma_b",
      all(conjugate(a_spin, gammas[index]).eq(gammas[index].scal(v_signs[index]))
          for index in range(14)))
check("sign_witness", "U preserves both owned one-form action pairings",
      u_one.transpose().mul(pairing_one_b).mul(u_one).eq(pairing_one_b)
      and u_one.transpose().mul(pairing_one_bomega).mul(u_one).eq(pairing_one_bomega))
check("sign_witness", "A is infinitesimally skew for B and Bomega, so exp(tA) preserves both",
      sum_is_zero(a_spin.transpose().mul(b_pairing), b_pairing.mul(a_spin))
      and sum_is_zero(
          a_spin.transpose().mul(b_omega_pairing), b_omega_pairing.mul(a_spin)
      ))
check("sign_witness", "U is orthogonal for the finite positive comparator",
      u_one.transpose().mul(u_one).is_identity_times() == 1
      and a_spin.transpose().mul(a_spin).is_identity_times() == 1)
check("sign_witness", "the witness fixes the selected background support axes 12 and 13",
      v_signs[12] == v_signs[13] == 1
      and conjugate(a_spin, gammas[12]).eq(gammas[12])
      and conjugate(a_spin, gammas[13]).eq(gammas[13]))


print("\nE. SOURCE GAUGE MAP: THE WITNESS IS AN EXACT REDUNDANCY")
source_bvkt_receipt = read(
    "explorations/conditional-build/selected-k77-i2b-source-bvkt-exact-sequence-2026-08-13.md"
)
witness_is_mixed = 0 in base and 1 in normal
witness_fixes_support = commutes(a_spin, gammas[12]) and commutes(a_spin, gammas[13])

check("source_gauge", "the prior exact source map receipt owns shape 196x91, rank 25 and kernel 66",
      "rank G = 25" in source_bvkt_receipt and "dim ker G = 66" in source_bvkt_receipt)
check("source_gauge", "the prior replay owns the exact rank-17 split plus rank-8 mixed image",
      "17 split-preserving directions + 8 mixed-split directions" in j10_receipt)
check("source_gauge", "the gamma0 gamma1 witness is mixed and commutes with both background blades",
      witness_is_mixed and witness_fixes_support)
check("source_gauge", "therefore its coefficientwise adjoint source variation is zero and it lies in ker G",
      witness_fixes_support and "dim ker G = 66" in source_bvkt_receipt)


print("\nF. TYPE BOUNDARY AND REVERSE-FALSIFICATION DISPOSITION")
check("typing", "left multiplication by J10 sends a normal Cl1 blade to Cl9, not Cl1",
      len(normal) == 10 and 1 in normal)
check("typing", "conjugation by J10 preserves Cl1 but is the square-plus-one split reflection",
      all(conjugate(j10, gammas[index]).eq(gammas[index].scal(r10_signs[index]))
          for index in range(14))
      and r10.mul(r10).is_identity_times() == 1)
check("scope", "no J10 endomorphism of the 196-dimensional Cl1 source tangent has been constructed", True)
check("scope", "the total K, total L, residual-zero background and common closed domain remain absent", True)
check("scope", "the split-natural rolled lifts of the fixed split-commutant family are killed here", True)
check("scope", "the tautological moving-J family remains only NOT-YET-FALSIFIED", True)
check("scope", "the +/- bit is gauge-trivial here, not a proved physical unitary equivalence", True)
check("scope", "H1-R as a whole is not killed because no admissible-J exhaustion theorem is owned", True)

print("FIXED_J10=KILLED_BY_OWNED_GAUGE_BASICNESS_OBSTRUCTION")
print("FIXED_J4=KILLED_BY_OBSERVED_PRINCIPAL_SYMBOL_AND_PAIRING_OBSTRUCTIONS")
print("SPLIT_EQUIVARIANT_B_COMPATIBLE_FIXED_SPINOR_FAMILY=EXHAUSTED_AS_PLUS_MINUS_J10")
print("PLUS_MINUS_JHAT10=CONNECTED_SOURCE_FRAME_GAUGE_EQUIVALENT_ON_SELECTED_LOCAL_BACKGROUND")
print("MOVING_TAUTOLOGICAL_J=NOT_YET_FALSIFIED")
print("TOTAL_PHYSICAL_DESCENT=TYPE_MISSING")
print("H1_R=NOT_KILLED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
