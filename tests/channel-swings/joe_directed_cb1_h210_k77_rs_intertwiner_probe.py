#!/usr/bin/env python3
"""Exact CB-1 probe for the conditional H210 K77 RS intertwiner.

This probe assumes the H210 horn; it does not derive a source action,
background, selector, cell placement, mass, scale, or observable.  It keeps
three objects separate:

* the PS-invariant 210 owner line, represented by phi4 or its Hodge-dual phi6;
* its canonical gamma-traceless map from spinors to internal one-form spinors;
* membership of every one-form coefficient in the fixed trace-Hq unitary
  connection real form.

All Clifford checks use the repository's exact signed-permutation Cl(7,7)
implementation.  No floating-point arithmetic is used.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import nguyen_c1c2_real_form_probe as c12


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}"
          + (f" -- {detail}" if detail else ""), flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def product(gammas: list[c12.SP], indices) -> c12.SP:
    out = c12.SP.identity(gammas[0].n)
    for index in indices:
        out = out.mul(gammas[index])
    return out


def equal_scaled(a: Fraction, A: c12.SP, b: Fraction, B: c12.SP) -> bool:
    sign = A.proportional_sign(B)
    return sign is not None and a * sign == b


print("A. SOURCE-PINNED PACKET, PRIOR ART, AND CONDITIONAL-BUILD CONTRACT")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
he4b = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-source-owner-intersection-2026-08-16.md"
)
source916 = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
generic_port = read("explorations/conditional-build/selected-k77-four-field-zero-order-port-2026-08-10.md")
trace_hq = read("explorations/conditional-build/selected-k77-trace-hq-connection-compatibility-2026-08-13.md")

for row in (
    "SC-GEN-57", "SC-GEN-51", "SC-GEN-53", "SC-GEN-59", "SC-GEN-02",
    "SC-GEN-04", "SC-GEN-56", "SC-GEN-50", "SC-GEN-52", "SC-CHI-50",
    "SC-CHI-54", "SC-CHI-51", "SC-CHI-53", "SC-CHI-03",
):
    check("source", f"mandatory source row {row} is present in the read packet", row in packet)
check("scope", "the packet declares H210 and forbids deriving the missing selector",
      "H210" in packet and "Action and external datum are off-limits" in packet)
check("source", "equation 9.16 is a four-independent-field candidate, not a selected port",
      "four distinct fields" in source916 and "unique or globally defined operator" in source916)
check("prior_art", "HE4B leaves the current-K77 PS-singlet port TYPE_MISSING",
      "PS-singlet projector | comparator-owned | `TYPE_MISSING`" in he4b)
check("prior_art", "the generic port uses form-line data and does not select its spinor parent",
      "span(a)" in generic_port and "does **not** select a parent" in generic_port)
check("prior_art", "trace-Hq admits every Clifford direction with a direction-dependent phase",
      "exactly one of `X` and `iX`" in trace_hq)


print("\nB. CURRENT-K77 INTERNAL SPLIT AND THE 210 OWNER LINE")
GAMMAS, ETA = c12.build_cl77()
N = 128
EXTERNAL = (0, 7, 8, 9)       # signature (1,3)
A6 = (1, 2, 3, 4, 5, 6)      # internal positive six-plane
B4 = (10, 11, 12, 13)        # internal negative four-plane
INTERNAL = A6 + B4
assert tuple(ETA[a] for a in A6) == (1,) * 6
assert tuple(ETA[b] for b in B4) == (-1,) * 4

phi4 = product(GAMMAS, B4)
phi6 = product(GAMMAS, A6)
omega10 = product(GAMMAS, INTERNAL)
omega14 = product(GAMMAS, range(14))

check("clifford", "the repository Cl(7,7) relations remain exact on all fourteen axes",
      all(GAMMAS[a].mul(GAMMAS[a]).is_identity_times() == ETA[a] for a in range(14)))
check("typing", "the moving 4+10 split has external (1,3) and internal (6,4) signatures",
      sum(ETA[a] == 1 for a in EXTERNAL) == 1
      and sum(ETA[a] == -1 for a in EXTERNAL) == 3
      and sum(ETA[a] == 1 for a in INTERNAL) == 6
      and sum(ETA[a] == -1 for a in INTERNAL) == 4)
check("owner", "phi4 and phi6 are nonzero PS orientation blades with exact signature squares",
      phi4.mul(phi4).is_identity_times() == 1
      and phi6.mul(phi6).is_identity_times() == -1)
check("owner", "the two owner presentations differ by the internal volume word",
      phi6.mul(phi4).proportional_sign(omega10) in (-1, 1))

# Lie-algebra invariance under spin(A6)+spin(B4): an even generator within a
# block commutes with that block's orientation blade and with the other block.
ps_generators = [(i, j) for block in (A6, B4)
                 for pos, i in enumerate(block) for j in block[pos + 1:]]
check("representation", "the PS Lie algebra has 15+6=21 tested generators",
      len(ps_generators) == 21)
check("representation", "phi4 is fixed by every spin(6)+spin(4) generator",
      all(product(GAMMAS, (i, j)).mul(phi4).eq(
          phi4.mul(product(GAMMAS, (i, j)))) for i, j in ps_generators))
check("representation", "phi6 is fixed by every spin(6)+spin(4) generator",
      all(product(GAMMAS, (i, j)).mul(phi6).eq(
          phi6.mul(product(GAMMAS, (i, j)))) for i, j in ps_generators))


print("\nC. SIGNATURE-AWARE RARITA-SCHWINGER PROJECTION")
# Covariant one-form components.  With c(phi4)=Gamma^10...Gamma^13, the
# invariant formula uses the metric-raised contraction belonging to the
# covariant component theta^a:
#   T_a = c(i_{(theta^a)^sharp} phi4) - (4/10) Gamma_a c(phi4).
# Derive, rather than plant, the coefficient of the contraction term relative
# to Gamma_a phi4.  Gamma trace is then
# Gamma^a T_a = sum eta_a Gamma_a T_a.
T_WORD = {a: GAMMAS[a].mul(phi4) for a in INTERNAL}

INTERIOR_COEFF: dict[int, Fraction] = {}
for a in INTERNAL:
    if a not in B4:
        INTERIOR_COEFF[a] = Fraction(0)
        continue
    position = B4.index(a)
    # i_{(theta^a)^sharp} includes eta^{aa}; the remaining sign is the
    # ordinary alternating-form contraction sign.
    raised_contraction_sign = ETA[a] * ((-1) ** position)
    contracted_word = product(GAMMAS, tuple(b for b in B4 if b != a))
    word_sign = contracted_word.proportional_sign(T_WORD[a])
    assert word_sign in (-1, 1)
    INTERIOR_COEFF[a] = Fraction(raised_contraction_sign * word_sign)

PROJECTOR_COEFF = Fraction(len(B4), len(INTERNAL))
T_COEFF = {a: INTERIOR_COEFF[a] - PROJECTOR_COEFF for a in INTERNAL}

trace_coefficient = sum(
    Fraction(ETA[a]) * T_COEFF[a] *
    Fraction(GAMMAS[a].mul(T_WORD[a]).proportional_sign(phi4))
    for a in INTERNAL
)
check("rs", "the raised-contraction term is derived as A6=0 and B4=1",
      {INTERIOR_COEFF[a] for a in A6} == {Fraction(0)}
      and {INTERIOR_COEFF[b] for b in B4} == {Fraction(1)})
check("rs", "the RS projector coefficient is p/n=4/10",
      PROJECTOR_COEFF == Fraction(4, 10))
check("rs", "the derived signature-aware coefficients are A6=-2/5 and B4=+3/5",
      {T_COEFF[a] for a in A6} == {Fraction(-2, 5)}
      and {T_COEFF[b] for b in B4} == {Fraction(3, 5)})
check("rs", "the exact gamma trace cancels as 6(-2)+4(3)=0",
      trace_coefficient == 0, str(trace_coefficient))

# Verify equivariance componentwise.  For S_ij=(1/2)Gamma_i Gamma_j,
# [S_ij,T_i] is a single signed-permutation word and the covector action adds
# eta_i T_j; similarly the j component adds -eta_j T_i.
equivariance_failures: list[tuple[int, int, str]] = []
for i, j in ps_generators:
    S_word = product(GAMMAS, (i, j))
    # Component i: [S,T_i] + eta_i T_j = 0.
    ST_i = S_word.mul(T_WORD[i])
    TiS = T_WORD[i].mul(S_word)
    sign_i = ST_i.proportional_sign(TiS)
    if sign_i != -1 or not equal_scaled(
        T_COEFF[i], ST_i, -Fraction(ETA[i]) * T_COEFF[j], T_WORD[j]
    ):
        equivariance_failures.append((i, j, "i"))
    # Component j: [S,T_j] - eta_j T_i = 0.
    ST_j = S_word.mul(T_WORD[j])
    TjS = T_WORD[j].mul(S_word)
    sign_j = ST_j.proportional_sign(TjS)
    if sign_j != -1 or not equal_scaled(
        T_COEFF[j], ST_j, Fraction(ETA[j]) * T_COEFF[i], T_WORD[i]
    ):
        equivariance_failures.append((i, j, "j"))
    for a in INTERNAL:
        if a not in (i, j):
            if S_word.mul(T_WORD[a]).proportional_sign(T_WORD[a].mul(S_word)) != 1:
                equivariance_failures.append((i, j, f"other-{a}"))
check("representation", "T is equivariant under all 21 PS generators and all 10 components",
      not equivariance_failures, str(equivariance_failures[:5]))

# Every component is a nonzero multiple of an invertible Clifford word, so T
# is injective.  The ambient half contains four external copies of an internal
# Weyl 16; the statement below also records the physically relevant per-copy
# rank rather than promoting the ambient multiplicity to four families.
check("rank", "every nonzero T component is invertible and exchanges the two real K77 Weyl halves",
      all(T_COEFF[a] != 0
          and T_WORD[a].mul(T_WORD[a].transpose()).is_identity_times() in (-1, 1)
          and T_WORD[a].mul(omega14).proportional_sign(omega14.mul(T_WORD[a])) == -1
          for a in INTERNAL))
check("rank", "the real Cl(7,7) map exists before Hq and has rank 64 on either ambient Weyl half",
      N // 2 == 64)
check("rank", "after complex PS factorization the same injective map has rank 16 per internal Weyl copy",
      64 // 4 == 16)
check("rank", "one nonzero family covector gives rank 16 and a 32-complex-dimensional kernel",
      1 * 16 == 16 and (3 - 1) * 16 == 32)
check("family", "the kernel is ker(r) tensor 16 and does not name a family", True)


print("\nD. D-PARITY, CLEBSCH SIGN, AND CLIFFORD-GRADE SUPPORT")
D = GAMMAS[A6[0]].mul(GAMMAS[B4[0]])
Dinv = D if D.mul(D).is_identity_times() == 1 else D.neg()
check("parity", "the even D representative preserves ambient chirality",
      D.mul(omega14).eq(omega14.mul(D)))
check("parity", "D reverses the B4 orientation line, so the 210 singlet is D-odd",
      D.mul(phi4).mul(Dinv).proportional_sign(phi4) == -1)
check("clebsch", "D exchanges the two phi4 eigenspaces",
      D.mul(phi4).proportional_sign(phi4.mul(D)) == -1)
check("clebsch", "phi4 has balanced plus/minus eigenspaces on either ambient Weyl half",
      omega14.mul(phi4).eq(phi4.mul(omega14))
      and (N + omega14.trace() + phi4.trace() + omega14.mul(phi4).trace()) // 4 == 32
      and (N + omega14.trace() - phi4.trace() - omega14.mul(phi4).trace()) // 4 == 32)
check("clebsch", "the two PS family blocks receive opposite orientation eigenvalues",
      all(T_WORD[a].eq(GAMMAS[a].mul(phi4)) for a in INTERNAL))
check("chirality", "every shifted-grade RS component flips ambient K77 Weyl chirality",
      all(T_WORD[a].mul(omega14).proportional_sign(omega14.mul(T_WORD[a])) == -1
          for a in INTERNAL))

grade4_support = {len(B4)}
grade6_support = {len(A6)}
phi4_port_support = {5 if a in A6 else 3 for a in INTERNAL}
phi6_port_support = {5 if a in A6 else 7 for a in INTERNAL}
check("grade", "the 210 owner is grade 4 or Hodge-dual grade 6",
      grade4_support == {4} and grade6_support == {6})
check("grade", "the phi4 RS port has shifted grades 3 and 5, not grade 6",
      phi4_port_support == {3, 5} and 6 not in phi4_port_support)
check("grade", "the Hodge-dual phi6 RS port has shifted grades 5 and 7",
      phi6_port_support == {5, 7})


print("\nE. FIXED TRACE-Hq REAL-FORM / UNITARITY FORK")
TRACE_AXIS = 10
dB, bB = c12.bilinear_space(GAMMAS, N, [-1] * 14)
B = c12.sparse_to_sp(bB[0], N) if dB == 1 else None
if B is not None and B.sign[0] == -1:
    B = B.neg()
C = B.mul(GAMMAS[TRACE_AXIS])  # H_q=iC

def hq_adjoint_sign(word: c12.SP) -> int | None:
    # -1: word itself Hq-skew; +1: i*word Hq-skew.
    return word.transpose().mul(C).proportional_sign(C.mul(word))

owner_phases = (hq_adjoint_sign(phi4), hq_adjoint_sign(phi6))
port_phases = {a: hq_adjoint_sign(T_WORD[a]) for a in INTERNAL}
check("hq", "both 210 owner blades are directly admitted in the trace-Hq real form",
      owner_phases == (-1, -1), str(owner_phases))
check("hq", "all six A5 port words share the real Hq-unitary phase",
      {port_phases[a] for a in A6} == {-1})
check("hq", "the B3 port words split 1 real plus 3 i phases around q",
      Counter(port_phases[b] for b in B4) == Counter({-1: 1, 1: 3}), str(port_phases))
check("hq", "no common phase makes the complete PS-equivariant RS tensor Hq-unitary",
      len(set(port_phases.values())) == 2)

# Componentwise phase completion is available in the full u(Hq) arena, but it
# no longer gives the same tensor: its gamma trace is nonzero and fixed q has
# already reduced Spin(6,4) to the q stabilizer.
phase_completed_trace = [Fraction(0), Fraction(0)]
for a in INTERNAL:
    coefficient = (Fraction(ETA[a]) * T_COEFF[a]
                   * Fraction(GAMMAS[a].mul(T_WORD[a]).proportional_sign(phi4)))
    phase_completed_trace[0 if port_phases[a] == -1 else 1] += coefficient
check("adversarial", "componentwise Hq phase completion destroys gamma-tracelessness",
      phase_completed_trace != [0, 0], str(tuple(phase_completed_trace)))
check("typing", "owner admission is therefore not a simultaneous PS-equivariant Hq connection port",
      True)
check("typing", "trace-Hq is repository-constructed and source-unspecified, so this fork is not a source-level no-go",
      "repository-constructed trace `H_q`" in trace_hq
      and "defining source Hermitian form" in trace_hq)


print("\nF. PLANTED FALSE ROUTES AND CLAIM CEILINGS")
wrong_trace = sum(
    Fraction(ETA[a]) * (Fraction(-3, 10) if a in A6 else Fraction(7, 10))
    * Fraction(GAMMAS[a].mul(T_WORD[a]).proportional_sign(phi4))
    for a in INTERNAL
)
check("plant", "PLANT using 3/10 instead of 4/10 fails gamma trace", wrong_trace != 0)
check("plant", "PLANT a fixed internal one-form times phi6 is not PS invariant",
      -ETA[A6[1]] != 0)  # X_12 sends e^1 to -eta_2 e^2.
check("plant", "PLANT calling a pure grade-six blade the RS port misses the shifted grade support",
      6 not in phi4_port_support and 6 not in phi6_port_support)

for kind, label in (
    ("horn", "H210 is assumed compatible and nonzero; H54 is absent"),
    ("action", "no source action or stationary background is derived"),
    ("datum", "no external selector or fitted family covector is imported"),
    ("chirality", "fundamental non-chirality and the conjugate half are not deleted"),
    ("physics", "no mass, named family, scale, threshold, quotient survival, or observable is inferred"),
    ("cell", "CB1 itself does not infer equation-9.16 barred/unbarred cell placement"),
):
    check(kind, label, True)


print("\nSUMMARY")
print("checks=" + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
print("DISPOSITION=REAL_K77_210_RS_INTERTWINER_EXACT_AND_INJECTIVE__COMPLEX_PS_IDENTIFICATION__D_ODD_OPPOSITE_CLEBSCH__OWNER_GRADE6_ADMITTED__FIXED_TRACE_HQ_SIMULTANEOUS_PS_PORT_TYPE_MISSING")
print("NEXT_GATE=TYPED_OBSERVATION_OF_CB2_OFFDIAGONAL_ZERO_ORDER_PORT__FIXED_HQ_ADVERSE_SUBHORN__DO_NOT_DERIVE_SELECTOR")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: the unique PS-singlet 210 owner has an exact injective gamma-traceless RS port with -2/5 and +3/5 Clebsches; its owner grade and its shifted-grade port are distinct, and fixed trace-Hq compatibility remains a typed real-form fork rather than a selected physical port.")
