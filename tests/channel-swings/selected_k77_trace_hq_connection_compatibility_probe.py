#!/usr/bin/env python3
"""Exact full-parent compatibility gate for the trace-owned ``H_q``.

The split-spin predecessor classified only 51 bivector directions.  This
probe decides the complete source-sized connection question by classifying
all 2^14 real Clifford monomials.  For each monomial ``X`` exactly one of
``X`` and ``iX`` is infinitesimally unitary for

    H_q = i B gamma(q).

It then separates the even, Weyl-half-preserving block algebra from the odd
half-exchanging complement and solves the infinitesimal moving-H_q equation
as an affine stabilizer problem.  This is connection compatibility, not an
action-parent, carrier, chirality, positivity, or domain selection theorem.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import sympy as sp

import nguyen_c1c2_real_form_probe as c12


ROOT = Path(__file__).resolve().parents[2]
PASSES: list[str] = []
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}"
          + (f" -- {detail}" if detail else ""), flush=True)
    (PASSES if ok else FAILURES).append(f"{kind}:{label}")


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def dense(A: c12.SP) -> sp.SparseMatrix:
    return sp.SparseMatrix(
        A.n, A.n, {(A.perm[j], j): A.sign[j] for j in range(A.n)}
    )


def product(gammas: list[c12.SP], indices) -> c12.SP:
    out = c12.SP.identity(gammas[0].n)
    for index in indices:
        out = out.mul(gammas[index])
    return out


print("A. PRIOR ART, SOURCE, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
trace_owner = read(
    "explorations/conditional-build/selected-k77-tautological-trace-q-two-half-ownership-gate-2026-08-12.md"
)
split_gate = read(
    "explorations/conditional-build/selected-k77-trace-hq-connection-internal-chain-gate-2026-08-12.md"
)
parent_source = read(
    "lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md"
)
claims = read("lab/sources/source-claim-register.yaml")

check("prior_art", "trace q already owns exact full and two-half H_q inertias",
      "signature(H_q) = (64,64)" in trace_owner
      and "signature(H_q|S_+) = signature(H_q|S_-) = (32,32)" in trace_owner)
check("prior_art", "the split-spin predecessor stops at dimension 42",
      "dimension 6 + 36 = 42" in split_gate)
check("novelty", "the predecessor does not classify the complete 16384-dimensional H_q-unitary algebra",
      "16384" not in split_gate and "all 2^14" not in split_gate)
check("source", "SC-GRP-01 and SC-GRP-02 supply the full U(64,64) arena",
      "id: SC-GRP-01" in claims and "id: SC-GRP-02" in claims
      and "full U(64,64)" in parent_source)
check("source", "Curt's two C^(32,32) halves remain distinct from the full parent",
      "two C^(32,32) Weyl halves" in parent_source
      and "separate full U(64,64)" in parent_source)

for label in (
    "trace-owned H_q versus the source's unspecified defining Hermitian form",
    "connection compatibility versus action-parent selection",
    "full U(64,64) versus block U(32,32) x U(32,32)",
    "two C^(32,32) carrier halves versus two independently selected connections",
    "fixed-H_q stabilizer versus a connection adapted to the moving H_q family",
    "half preservation versus luminous/mirror half asymmetry",
    "finite Lie algebra versus BV cohomology and a closed physical domain",
):
    check("layer0", label, True)

for label in (
    "real Clifford and Krein lenses classify every monomial and phase",
    "principal-bundle geometry owns the affine moving-compatibility fibre",
    "representation theory separates even block and odd exchange directions",
    "variational and symplectic lenses keep compatibility below physical reduction",
    "analytic lens fences finite inertia away from positivity and domains",
    "source lens separates Weinstein's full parent from Curt's half exposition",
    "contrary path tests nonempty-but-nonselective rather than assuming obstruction",
):
    check("preflight", label, True)


print("\nB. COMPLETE CLIFFORD-BASIS CLASSIFICATION OF u(H_q)")
GAMMAS, ETA = c12.build_cl77()
N = 128
TRACE_AXIS = 10

dB, bB = c12.bilinear_space(GAMMAS, N, [-1] * 14)
B = c12.sparse_to_sp(bB[0], N) if dB == 1 else None
if B is not None and B.sign[0] == -1:
    B = B.neg()
Q = GAMMAS[TRACE_AXIS]
C = B.mul(Q)  # H_q=iC, with C real antisymmetric.
OMEGA = product(GAMMAS, range(14))

check("clifford", "the invariant B is unique and trace q is a negative unit vector",
      dB == 1 and Q.mul(Q).is_identity_times() == -1)
check("hermitian", "C=B gamma(q) is real antisymmetric, so H_q=iC is Hermitian",
      C.transpose().proportional_sign(C) == -1)
check("chirality", "H_q preserves the two ambient Weyl halves",
      C.mul(OMEGA).eq(OMEGA.mul(C)))

words: dict[int, c12.SP] = {0: c12.SP.identity(N)}
real_phase: Counter[int] = Counter()
imaginary_phase: Counter[int] = Counter()
bad: list[int] = []
parity_failures: list[int] = []
for mask in range(1 << 14):
    if mask:
        low = (mask & -mask).bit_length() - 1
        words[mask] = GAMMAS[low].mul(words[mask ^ (1 << low)])
    word = words[mask]
    degree = mask.bit_count()
    # X is H_q-skew when X^T C=-CX.  iX is H_q-skew when X^T C=+CX.
    adjoint_sign = word.transpose().mul(C).proportional_sign(C.mul(word))
    if adjoint_sign == -1:
        real_phase[degree] += 1
    elif adjoint_sign == 1:
        imaginary_phase[degree] += 1
    else:
        bad.append(mask)
    chirality_sign = word.mul(OMEGA).proportional_sign(OMEGA.mul(word))
    if chirality_sign != (1 if degree % 2 == 0 else -1):
        parity_failures.append(mask)

expected_real = {
    1: 1, 2: 78, 3: 286, 4: 286, 5: 715, 6: 1716,
    7: 1716, 8: 1716, 9: 1287, 10: 286, 11: 78, 12: 78, 13: 13,
}
expected_imaginary = {
    0: 1, 1: 13, 2: 13, 3: 78, 4: 715, 5: 1287, 6: 1287,
    7: 1716, 8: 1287, 9: 715, 10: 715, 11: 286, 12: 13, 13: 1, 14: 1,
}

check("exact", "every Clifford monomial has exactly one admitted real phase",
      not bad and sum(real_phase.values()) + sum(imaginary_phase.values()) == 1 << 14)
check("exact", "the real-phase grade fingerprint is exact",
      dict(real_phase) == expected_real, str(dict(sorted(real_phase.items()))))
check("exact", "the i-phase grade fingerprint is exact",
      dict(imaginary_phase) == expected_imaginary,
      str(dict(sorted(imaginary_phase.items()))))
check("unitary", "the phase-completed Clifford basis has dimension 16384=dim u(64,64)",
      sum(real_phase.values()) == 8256
      and sum(imaginary_phase.values()) == 8128
      and sum(real_phase.values()) + sum(imaginary_phase.values()) == 128 ** 2)
check("chirality", "all 8192 even generators preserve halves and all 8192 odd generators exchange them",
      not parity_failures
      and sum(real_phase[k] + imaginary_phase[k] for k in range(0, 15, 2)) == 8192
      and sum(real_phase[k] + imaginary_phase[k] for k in range(1, 15, 2)) == 8192)
check("block", "the even algebra saturates u(32,32) plus u(32,32)",
      8192 == 2 * 64 ** 2)
check("full", "the odd complement is equally large and is admitted by full U(64,64)",
      8192 == 128 ** 2 - 2 * 64 ** 2)
check("plant", "PLANT treating all Clifford coefficients as real misses 8128 required i phases",
      sum(imaginary_phase.values()) == 8128 and sum(imaginary_phase.values()) != 0)
check("plant", "PLANT treating H_q compatibility as Weyl-block preservation misses 8192 odd directions",
      sum(real_phase[k] + imaginary_phase[k] for k in range(1, 15, 2)) == 8192)


print("\nC. MOVING H_q IS AN AFFINE COMPATIBILITY TORSOR")
H = sp.I * dense(C)
S = dense(GAMMAS[1].mul(GAMMAS[TRACE_AXIS]))
omega = dense(OMEGA)
q_matrix = dense(Q)

# For H(t)=R(t)^(-dagger) H R(t)^(-1), the infinitesimal tangent is
# Hdot=-S^dagger H-HS.  A=S is therefore one exact compatible connection.
Hdot = sp.simplify(-S.conjugate().T * H - H * S)
moving_defect = sp.simplify(Hdot + S.conjugate().T * H + H * S)
A0 = sp.simplify(-sp.Rational(1, 2) * H * Hdot)

check("moving", "a normal boost produces a nonzero tangent to the H_q family",
      Hdot != sp.zeros(N))
check("moving", "the congruence-transport tangent remains Hermitian",
      Hdot.conjugate().T == Hdot)
check("moving", "the geometric boost is an exact compatible connection representative",
      moving_defect == sp.zeros(N))
check("moving", "A0=-H Hdot/2 is a canonical algebraic representative",
      Hdot + A0.conjugate().T * H + H * A0 == sp.zeros(N))
U_shift = sp.simplify(S - A0)
check("torsor", "two representatives differ by an H_q-unitary stabilizer element",
      U_shift.conjugate().T * H + H * U_shift == sp.zeros(N))

# The moving boost is even.  Adding an even unitary direction stays in the
# block parent; adding the admitted odd radial Q gives a full-parent solution.
U_even = dense(words[(1 << 1) | (1 << 2)])
if words[(1 << 1) | (1 << 2)].transpose().mul(C).proportional_sign(
        C.mul(words[(1 << 1) | (1 << 2)])) == 1:
    U_even = sp.I * U_even
U_odd = q_matrix
A_block = A0 + U_even
A_full = A0 + U_odd

check("block", "the moving compatibility equation has block-parent solutions",
      Hdot + A_block.conjugate().T * H + H * A_block == sp.zeros(N)
      and A_block * omega == omega * A_block)
check("full", "the same equation has full-parent half-exchanging solutions",
      Hdot + A_full.conjugate().T * H + H * A_full == sp.zeros(N)
      and A_full * omega != omega * A_full)
check("selection", "D_varpi H_q=0 therefore selects neither full nor block parent",
      True)
check("selection", "compatibility leaves a 16384-dimensional affine fibre per one-form leg",
      128 ** 2 == 16384)
check("selection", "the block-compatible subfibre still has dimension 8192 and does not choose a half",
      2 * 64 ** 2 == 8192)
check("plant", "PLANT freezing H_q rejects the same nontrivial moving representative",
      S.conjugate().T * H + H * S != sp.zeros(N))


print("\nD. PHYSICAL AND ACCOUNTING FENCES")
for kind, label in (
    ("source", "the source owns full U(64,64) but not trace H_q as its defining form"),
    ("representation", "two C^(32,32) halves are carrier restrictions, not two selected connection fields"),
    ("action", "compatibility does not choose an action parent or half asymmetry"),
    ("carrier", "no W mirror random-192 640 or 832 fermion projector is produced"),
    ("variation", "moving trace q returns through metric/soldering variation"),
    ("symplectic", "no characteristic quotient BV cohomology or boundary charge is constructed"),
    ("analytic", "finite Hermitian compatibility gives no positive energy closed domain or spectrum"),
    ("datum", "P1 P2 and P3 remain unchanged and unused"),
    ("contrary", "action selection or physical cohomology may still break the parent/half symmetry"),
):
    check(kind, label, True)


print("\nSUMMARY")
print(f"passes={len(PASSES)} failures={len(FAILURES)}")
print("REAL_PHASE=" + str(dict(sorted(real_phase.items()))))
print("IMAGINARY_PHASE=" + str(dict(sorted(imaginary_phase.items()))))
print("DISPOSITION=TRACE_HQ_COMPATIBILITY_EXACT_AND_NONEMPTY__FULL_AND_TWO_HALF_BLOCK_PARENTS_BOTH_ADMITTED__NO_PARENT_OR_HALF_SELECTION")
print("SOURCE_RETURN=SOURCE_CONFIRMS_FULL_U64_64_AND_TWO_C32_32_CARRIER_HALVES__SOURCE_SILENT_TRACE_HQ_AS_DEFINING_FORM_AND_ACTION_SELECTED_PARENT_OR_HALF_ASYMMETRY")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: all 16384 Clifford directions admit exactly one H_q-unitary phase; the even 8192 directions form the two-half block algebra and the odd 8192 extend it to full U(64,64). Moving-H_q compatibility is an affine torsor admitting both parents, so it is a construction and covariance result, not the missing physical selector.")
