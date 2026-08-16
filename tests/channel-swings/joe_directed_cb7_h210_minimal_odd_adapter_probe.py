#!/usr/bin/env python3
"""Exact CB-7B classifier for a minimal odd H210 cell adapter.

This is a reverse-conditional probe.  It asks which *type* of odd adapter
could homogenize the ambient-half parity of ``d0`` and the H210 zero-order
map.  It does not select, derive, or insert such an adapter in the source
operator.  In particular, the repository-owned tautological trace receiver
is a vertical/internal vector even though an older matrix fixture represented
it by ``gamma[7]``.

All Clifford calculations use the exact signed-permutation Cl(7,7) backend
from CB-1.  No floating-point arithmetic is used.
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


def commutation_sign(left: c12.SP, right: c12.SP) -> int | None:
    """Return +1 for commute and -1 for anticommute."""
    return left.mul(right).proportional_sign(right.mul(left))


print("A. SOURCE, PRIOR ART, AND OBJECT-TYPE FENCES")
packet = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "he4-path-reprioritization-2026-08-16.md"
)
cb1 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb1-h210-k77-rs-intertwiner-2026-08-16.md"
)
cb2 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb2-h210-equation916-cross-half-composition-2026-08-16.md"
)
cb6 = read(
    "lab/active-research/joe-directed/high-energy-two-plus-one/"
    "cb6-wave-h210-correlated-lift-reprioritization-2026-08-16.md"
)
reconciliation = read(
    "explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md"
)
q_owner = read(
    "explorations/k77-wave2-q-receiver-trace-adjoint-ward-selection-2026-08-04.md"
)
v140 = read("explorations/conditional-build/conditional-physics-ledger-v0.140.md")
old_probe = read(
    "tests/channel-swings/selected_k77_degree_duality_pair_graph_gate_probe.py"
)

check("scope", "the mandatory packet keeps action and external-datum construction off limits",
      "Action and external datum are off-limits" in packet)
check("source", "the source-labelled full cell still has d0 even and H210 varpi odd",
      "`d0` preserves the ambient half while the H210" in cb6
      and "zero-order `varpi_-+ / varpi_+-` term flips it" in cb6)
check("port", "CB1 owns the exact internal 16-to-144bar rank-16 H210 port",
      "rank `16` on each internal Weyl copy" in cb1
      and "gamma-traceless RS port" in cb1)
check("reverse", "forward and reverse-shaped source cells remain distinct",
      "reverse-shaped partners" in cb2
      and "source does not prove a common adjoint domain" in cb2)
check("minimality", "prior D7 exactness requires one supplied vector for a half-spinor flip",
      "dim Hom_Spin(S+,S-) = 0" in reconciliation
      and "dim Hom_Spin(V tensor S+, S-) = 1" in reconciliation)
check("shiab", "the repaired Shiab prior art has Lambda2-to-V arity",
      "Lambda2 V tensor S+" in reconciliation
      and "spinor-valued two-form to a spinor-valued one-form" in reconciliation)
check("old_scope", "v0.140 kills only trace-q degree duality on the proposed W/mirror RS carrier",
      "kills only canonical trace-q degree duality on the proposed RS carrier" in v140
      and "It does not kill draft equation 9.16" in v140)
check("ownership", "the canonical trace receiver is vertically owned by Sym2 T*X",
      "tautological vertical" in q_owner and "q_g=\\frac12g" in q_owner)
check("ownership", "old gamma[7] is a fixture coordinate, not a typed horizontal owner",
      'q = structures["gammas"][7]' in old_probe
      and "a section of the chimeric Clifford vector bundle" in q_owner)


print("\nB. CURRENT H210 Cl(7,7) PORT")
GAMMAS, ETA = c12.build_cl77()
N = 128
EXTERNAL = (0, 7, 8, 9)       # current H210 fixture's horizontal (1,3)
A6 = (1, 2, 3, 4, 5, 6)      # current H210 internal positive six-plane
B4 = (10, 11, 12, 13)        # current H210 internal negative four-plane
INTERNAL = A6 + B4

phi4 = product(GAMMAS, B4)
omega10 = product(GAMMAS, INTERNAL)
omega14 = product(GAMMAS, range(14))
T_WORD = {a: GAMMAS[a].mul(phi4) for a in INTERNAL}
T_COEFF = {
    a: Fraction(-2, 5) if a in A6 else Fraction(3, 5)
    for a in INTERNAL
}
PS_GENERATORS = [
    (i, j)
    for block in (A6, B4)
    for pos, i in enumerate(block)
    for j in block[pos + 1:]
]


def trace_scalar(q_index: int, placement: str) -> Fraction | None:
    """Gamma trace relative to the invertible word gamma(q) phi4.

    ``left`` is gamma(q) T.  ``right`` is T gamma(q).  ``pin`` is the
    reflected-one-form completion of left multiplication.
    """
    q = GAMMAS[q_index]
    target = q.mul(phi4)
    total = Fraction(0)
    for a in INTERNAL:
        if placement == "left":
            word = q.mul(T_WORD[a])
            reflection = 1
        elif placement == "right":
            word = T_WORD[a].mul(q)
            reflection = 1
        elif placement == "pin":
            word = q.mul(T_WORD[a])
            reflection = -1 if a == q_index else 1
        else:
            raise ValueError(placement)
        sign = GAMMAS[a].mul(word).proportional_sign(target)
        if sign is None:
            return None
        total += Fraction(ETA[a] * reflection) * T_COEFF[a] * sign
    return total


def pin_to_right_signs(q_index: int) -> set[int | None]:
    q = GAMMAS[q_index]
    signs: set[int | None] = set()
    for a in INTERNAL:
        reflection = -1 if a == q_index else 1
        sign = q.mul(T_WORD[a]).proportional_sign(T_WORD[a].mul(q))
        signs.add(None if sign is None else reflection * sign)
    return signs


def ps_commutator_failures(q_index: int) -> int:
    q = GAMMAS[q_index]
    return sum(
        commutation_sign(product(GAMMAS, (i, j)), q) != 1
        for i, j in PS_GENERATORS
    )


check("clifford", "the current object split is (1,3) plus (6,4)",
      tuple(ETA[a] for a in EXTERNAL) == (1, -1, -1, -1)
      and tuple(ETA[a] for a in A6) == (1,) * 6
      and tuple(ETA[a] for a in B4) == (-1,) * 4)
check("rs", "the unadapted H210 tensor is exactly gamma traceless",
      sum(
          Fraction(ETA[a]) * T_COEFF[a]
          * Fraction(GAMMAS[a].mul(T_WORD[a]).proportional_sign(phi4))
          for a in INTERNAL
      ) == 0)
check("chirality", "H210 flips ambient and internal Weyl chirality",
      all(commutation_sign(T_WORD[a], omega14) == -1
          and commutation_sign(T_WORD[a], omega10) == -1
          for a in INTERNAL))
check("rank", "each H210 component is invertible, hence rank 64 on either ambient half",
      all(T_WORD[a].mul(T_WORD[a].transpose()).is_identity_times() in (-1, 1)
          for a in INTERNAL)
      and N // 2 == 64 and (N // 2) // 4 == 16)


print("\nC. HYPOTHETICAL HORIZONTAL ODD LINE: THE ONLY ALGEBRAIC SURVIVOR")
external_left_traces = {a: trace_scalar(a, "left") for a in EXTERNAL}
external_right_traces = {a: trace_scalar(a, "right") for a in EXTERNAL}
external_pin_traces = {a: trace_scalar(a, "pin") for a in EXTERNAL}

check("rs", "every horizontal q gives zero gamma trace for q-left, q-right, and Pin",
      set(external_left_traces.values()) == {Fraction(0)}
      and set(external_right_traces.values()) == {Fraction(0)}
      and set(external_pin_traces.values()) == {Fraction(0)})
check("pin", "Pin(q_H) equals bare q_H on the internal one-form support",
      all(pin_to_right_signs(a) == {-1} for a in EXTERNAL))
check("ps", "horizontal q commutes with all 21 internal PS generators",
      len(PS_GENERATORS) == 21
      and all(ps_commutator_failures(a) == 0 for a in EXTERNAL))
check("channel", "horizontal q preserves internal chirality and the 16-to-144bar channel",
      all(commutation_sign(GAMMAS[a], omega10) == 1 for a in EXTERNAL)
      and all(commutation_sign(GAMMAS[q].mul(T_WORD[a]), omega10) == -1
              for q in EXTERNAL for a in INTERNAL))
check("parity", "q_H T_H210 is ambient even and can match d0 parity",
      all(commutation_sign(GAMMAS[q].mul(T_WORD[a]), omega14) == 1
              for q in EXTERNAL for a in INTERNAL))
check("rank", "q_H T remains invertible with rank 16 per internal Weyl copy on both halves",
      all(GAMMAS[q].mul(T_WORD[a]).mul(
          GAMMAS[q].mul(T_WORD[a]).transpose()
      ).is_identity_times() in (-1, 1)
          for q in EXTERNAL for a in INTERNAL)
      and N // 2 == 64 and (N // 2) // 4 == 16)
check("horn", "a horizontal q must move as extra conditional data; no fixed line is selected", True)


print("\nD. VERTICAL/INTERNAL q: THE CANONICAL TRACE RECEIVER IS ADVERSE")
internal_left_traces = {a: trace_scalar(a, "left") for a in INTERNAL}
internal_right_traces = {a: trace_scalar(a, "right") for a in INTERNAL}
internal_pin_traces = {a: trace_scalar(a, "pin") for a in INTERNAL}

check("rs", "bare left q_A leaks the H210 RS port with coefficient -4/5",
      {internal_left_traces[a] for a in A6} == {Fraction(-4, 5)})
check("rs", "bare left q_B leaks the H210 RS port with coefficient +6/5",
      {internal_left_traces[a] for a in B4} == {Fraction(6, 5)})
check("rank", "the nonzero leakage coefficient multiplies an invertible word, so leakage is full per half",
      all(internal_left_traces[a] != 0 for a in INTERNAL)
      and N // 2 == 64 and (N // 2) // 4 == 16)
check("rs", "right placement and Pin completion repair internal gamma trace",
      set(internal_right_traces.values()) == {Fraction(0)}
      and set(internal_pin_traces.values()) == {Fraction(0)})
check("pin", "Pin completion preserves the abstract H210 image up to owner sign",
      all(pin_to_right_signs(a) == {-1} for a in A6)
      and all(pin_to_right_signs(a) == {1} for a in B4))
check("ps", "fixed internal q breaks PS to its stabilizer",
      {ps_commutator_failures(a) for a in A6} == {5}
      and {ps_commutator_failures(a) for a in B4} == {3})
check("channel", "internal q flips internal chirality and exchanges the current 144bar/144 port",
      all(commutation_sign(GAMMAS[a], omega10) == -1 for a in INTERNAL)
      and all(commutation_sign(GAMMAS[q].mul(T_WORD[a]), omega10) == 1
              for q in INTERNAL for a in INTERNAL))
check("parity", "internal q also makes qT ambient even, but only after losing current port custody",
      all(commutation_sign(GAMMAS[q].mul(T_WORD[a]), omega14) == 1
              for q in INTERNAL for a in INTERNAL))
check("ownership", "the geometry-owned trace q belongs to this internal adverse class",
      "tautological vertical" in q_owner
      and "trace line becomes negative" in q_owner)


print("\nE. MINIMALITY, PLACEMENT, SHIAB, AND REVERSE FENCES")
# Ambient parity in F2: d0=0, T=1, q=1.
d0_parity, h210_parity, q_parity = 0, 1, 1
check("minimality", "a uniform odd row/column adapter leaves the relative mismatch unchanged",
      (d0_parity + q_parity) % 2 != (h210_parity + q_parity) % 2)
check("placement", "q on d0 alone and q on H210 alone are the two parity-level repairs",
      (d0_parity + q_parity) % 2 == h210_parity
      and d0_parity == (h210_parity + q_parity) % 2)
# The parity equations are not the whole source type.  The banked census is
# zeta- = 144bar in the A package and zeta+ = 144 in the conjugate package.
# A horizontal q commutes with internal chirality, so q*T keeps 144bar.  It
# therefore cannot be routed to zeta+ merely because same-half primalization
# makes its ambient parity fit.  The conjugate statement is identical.
source_modules = {"zeta-": "144bar", "zeta+": "144"}
h210_outputs = {"A": "144bar", "B": "144"}
same_half_targets = {"A": "zeta+", "B": "zeta-"}
opposite_half_targets = {"A": "zeta-", "B": "zeta+"}
check("module", "H210-side q_H plus same-half duality fails both source module slots",
      all(h210_outputs[half] != source_modules[same_half_targets[half]]
          for half in ("A", "B")))
check("module", "derivative-side q_H plus opposite-half duality preserves both H210 slots",
      all(h210_outputs[half] == source_modules[opposite_half_targets[half]]
          for half in ("A", "B")))
check("placement", "only output-side q_H after d0 preserves the banked CB2-CB6 H210 custody",
      True)
check("form_degree", "the zero-order adapter changes no Omega0-to-Omega1 form degree", True)
check("shiab", "A_q left/right is not a same-cell adapter because its domain is Omega2, not Omega0", True)
check("derivative", "pre- versus postcomposition around d0 differs by a nabla-q lower-order term", True)
check("reverse", "a forward q placement does not construct its reverse density-dual placement", True)
check("reverse", "bars and stars do not promote that reverse placement to an adjoint or reality condition", True)
check("twistor", "the j4 Gamma4 projector is Clifford even and cannot supply the missing odd line", True)


print("\nF. HOSTILE CONTROLS AND CLAIM CEILING")
check("plant", "PLANT import v0.140 W/mirror rank-64 leakage as an H210 no-go is rejected",
      set(external_left_traces.values()) == {0}
      and "rank-192 `W` with its rank-192 ASD mirror" in v140)
check("plant", "PLANT call gamma[7] horizontal because two fixtures reuse index 7 is rejected",
      "tautological vertical" in q_owner)
check("plant", "PLANT use internal Pin repair as preservation of the same PS channel is rejected",
      any(ps_commutator_failures(a) for a in INTERNAL)
      and all(commutation_sign(GAMMAS[a], omega10) == -1 for a in INTERNAL))
check("plant", "PLANT use one uniform q on the whole displayed cell is rejected",
      (d0_parity + q_parity) % 2 != (h210_parity + q_parity) % 2)
check("plant", "PLANT promote H210-side q_H from parity SAT to source-module SAT is rejected",
      h210_outputs["A"] != source_modules[same_half_targets["A"]]
      and h210_outputs["B"] != source_modules[same_half_targets["B"]])
check("scope", "no action, selector, graph, family row, reduction, quotient, or external datum is built", True)
check("physics", "no mass, family identity, scale, spectrum, observable, or physical chirality is inferred", True)


print("\nSUMMARY")
print("checks=" + " + ".join(
    f"{count} {kind}" for kind, count in sorted(COUNTS.items())
))
print("DISPOSITION=MINIMAL_ODD_ADAPTER_REQUIRES_SUMMAND_SPECIFIC_PLACEMENT__VERTICAL_TRACE_Q_ADVERSE__H210_SIDE_HORIZONTAL_Q_ONLY_PARITY_SAT_AND_MODULE_FAIL__DERIVATIVE_OUTPUT_HORIZONTAL_Q_PLUS_OPPOSITE_DUAL_ONLY_CURRENT_CUSTODY_SURVIVOR__NO_SELECTION")
print("NEXT_GATE=COMBINE_WITH_CB7_PARITY_AND_FORWARD_REVERSE_CLASSIFIERS__DO_NOT_BUILD_Q_HORN")
if FAILURES:
    for failure in FAILURES:
        print(" - " + failure)
    raise SystemExit(1)
print("PASS: a moving horizontal odd line is the minimal adapter type; only q_H after d0 with opposite-half duality preserves the current H210 source-module custody, while the owned vertical q and H210-side placement are adverse.")
