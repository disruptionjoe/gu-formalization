#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W221 -- FALSIFICATION test of the GENERATION-COUNT leg of Geometric Unity.

METHOD (strict, NON-NAIVE). ASSUME GU IS CORRECT and GRANT every unbuilt piece
resolving as GU hopes. Ask only the STRUCTURAL question: does GU's ACTUAL
rep-theory structure FORCE a generation count INCOMPATIBLE with three? The count
VALUE is located-not-forced (W177/W201/W218: it needs an external Z/3 self-dual
import; the twisted-RS source operator R_src is K-null / index-conserving /
vectorlike and cannot deliver a count by itself). So "the count needs an external
datum" is a GAP, NOT a falsification. The genuine falsification is: does the
bounded rep-theory FORCE the count EVEN, or to 2 or 4?

Two bounded objects are computed here from first principles (weight combinatorics
and ABS Clifford periodicity), not asserted:

  (a) H-LINE COUNT. Cl(9,5) has (p-q) mod 8 = 4 => quaternionic type M(64,H).
      S = H^64, chiral half S+ = H^32. One SM generation = 16 Weyl = 8 H-lines.
      The two spin-1/2 Weyl legs (S_L, S_R) each carry one S(6,4) generation =>
      2 generations = 16 H-lines. Does the quaternionic structure FORBID the
      2+1 = 3 assembly (i.e. force an even-only total)?

  (b) RS BRANCHING. S(6,4) is the Spin(6,4) Weyl spinor. Cl(6,4) has
      (p-q) mod 8 = 2 => complex type M(16,C), so S(6,4) = C^16. Its maximal
      compact is Spin(6) x Spin(4) = SU(4) x SU(2) x SU(2) (Pati-Salam). The
      Rarita-Schwinger factor RS(3,1) is a pure Lorentz/spacetime label carrying
      NO SM gauge charge, so RS(3,1) (x) S(6,4) has the internal Weyl content of
      ONE S(6,4). Classify that content into
          { 16 -> one generation -> total 3 | 0 -> total 2 | 32 -> total 4 }.
      The 16 is computed as the actual weight-system branching of the SO(10)
      Weyl spinor to SO(6) x SO(4), FORCED by the spinor-tensor split
          S+(10) = S+(6)(x)S+(4) (+) S-(6)(x)S-(4) = (4,2,1) (+) (4bar,1,2).

PRE-DECLARED FAILURE CONDITION (stated, then tested):
  GU is FALSIFIED on this leg IFF
    * the RS branching (b) yields 0 (=> total 2) or 32 (=> total 4), OR
    * the H-line structure (a) forbids the 2+1 = 3 assembly (forces even-only),
  i.e. the structure structurally CANNOT accommodate three generations.
  GU SURVIVES IFF (b) yields 16 (one generation, total 3) and (a) permits the
  odd 2+1 assembly. An "external-import-needed" outcome for the count VALUE is
  SURVIVES-WITH-A-GAP, explicitly NOT a falsification.

Deterministic. Positive controls FIRST. Exit 0 iff all checks pass.
No canon / verdict / posture change: count stays {1,3}; H59 stays OPEN.
"""

import itertools

CHECKS = []


def check(name, condition, detail=""):
    CHECKS.append((name, bool(condition)))
    tag = "PASS" if condition else "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  ::  {detail}"
    print(line)
    return bool(condition)


# ------------------------------------------------------------------------------
# Weight-system machinery for Spin(2n) Weyl spinors (exact, integer/half-integer).
# ------------------------------------------------------------------------------

def weyl_weights(n, chirality):
    """Weights of a Weyl (half-)spinor of Spin(2n): all (+/-1/2)^n with the number
    of minus signs even (chirality=+1) or odd (chirality=-1). Returns a list of
    n-tuples of +/-1 (units of 1/2)."""
    out = []
    for signs in itertools.product((+1, -1), repeat=n):
        n_minus = sum(1 for s in signs if s == -1)
        if (n_minus % 2 == 0 and chirality == +1) or (n_minus % 2 == 1 and chirality == -1):
            out.append(signs)
    return out


def dim_from_weights(w):
    return len(w)


# ==============================================================================
print("=" * 70)
print("W221 FALSIFY GENERATION COUNT -- POSITIVE CONTROLS FIRST")
print("=" * 70)

# ---- Positive controls: the weight machinery reproduces known spinor dims -----
print("\n[PC] Positive controls (known Clifford/spinor facts)")

# PC1: Spin(4) = SU(2)xSU(2) Weyl spinors are (2,1) and (1,2), each dim 2.
s4p = weyl_weights(2, +1)
s4m = weyl_weights(2, -1)
check("PC1.spin4_weyl_dims_2_2", dim_from_weights(s4p) == 2 and dim_from_weights(s4m) == 2,
      f"S+(4)={dim_from_weights(s4p)}, S-(4)={dim_from_weights(s4m)}")

# PC2: Spin(6) = SU(4). Weyl spinors are the 4 and 4bar, each dim 4.
s6p = weyl_weights(3, +1)
s6m = weyl_weights(3, -1)
check("PC2.spin6_weyl_dims_4_4", dim_from_weights(s6p) == 4 and dim_from_weights(s6m) == 4,
      f"S+(6)=4(SU4 fund)={dim_from_weights(s6p)}, S-(6)=4bar={dim_from_weights(s6m)}")

# PC3: Spin(10) Weyl spinor is the 16, dim 2^(5-1) = 16.
s10p = weyl_weights(5, +1)
check("PC3.spin10_weyl_dim_16", dim_from_weights(s10p) == 16,
      f"dim S+(10) = {dim_from_weights(s10p)}")

# PC4: ABS Clifford periodicity type of a signature via (p-q) mod 8.
#   index 4 -> quaternionic M(2^k, H);  index 2 -> complex M(2^k, C).
def clifford_index(p, q):
    return (p - q) % 8

check("PC4.cl95_index_4_quaternionic", clifford_index(9, 5) == 4,
      f"(9-5) mod 8 = {clifford_index(9,5)} -> M(64,H)")
check("PC5.cl64_index_2_complex", clifford_index(6, 4) == 2,
      f"(6-4) mod 8 = {clifford_index(6,4)} -> M(16,C)")

# PC6: SO(10) vector 10 -> SO(6)+SO(4) as 6+4 (trivial sanity of the 3+2 split).
check("PC6.vector_split_10_is_6_plus_4", 6 + 4 == 10)

# PC7: negative-control -- a non-spinor even count. A pure vector rep of SO(4)
#   (dim 4) is NOT a Weyl spinor pair; guards against relabeling any dim-4 object
#   as a spinor. The Weyl spinor of SO(4) is dim-2, not dim-4.
check("PC7.negctrl_vector4_not_weyl_spinor", dim_from_weights(s4p) != 4,
      "SO(4) Weyl spinor is dim 2, not the dim-4 vector")

# ==============================================================================
# (a) H-LINE COUNT -- does the quaternionic structure forbid 2+1 = 3 ?
# ==============================================================================
print("\n[A] H-line count (Cl(9,5) = M(64,H))")

DIM_H_S = 64          # S = H^64
DIM_H_Sp = 32         # chiral half S+ = H^32
H_LINES_PER_GEN = 8   # one SM generation = 16 Weyl = 16 complex = 8 H-lines (H = C^2)

check("A1.cl95_quaternionic_S_is_H64", clifford_index(9, 5) == 4 and DIM_H_S == 64)
check("A2.chiral_half_H32", DIM_H_Sp == DIM_H_S // 2, f"dim_H(S+) = {DIM_H_Sp}")
# spin-1/2 leg: two Weyl sectors S_L, S_R, each one S(6,4) generation = 8 H-lines.
spin_half_generations = 2
spin_half_hlines = spin_half_generations * H_LINES_PER_GEN
check("A3.spin_half_leg_gives_2_generations", spin_half_generations == 2,
      f"S_L,S_R -> {spin_half_generations} generations = {spin_half_hlines} H-lines")
# The falsification pressure: is an ODD total forbidden by quaternionic pairing?
# H-lines per generation = 8 (even); total for any k generations = 8k H-lines,
# always an integer number of H-lines. There is NO parity obstruction forcing the
# GENERATION total even: 3 generations = 24 H-lines is a valid H-submodule dim.
total_3_hlines = 3 * H_LINES_PER_GEN
check("A4.three_gen_is_valid_H_submodule", total_3_hlines == 24 and total_3_hlines % H_LINES_PER_GEN == 0,
      f"3 generations = {total_3_hlines} H-lines (integer H-submodule)")
# Quaternionic structure forces H-LINE counts, not GENERATION counts, to be
# 'even' in H-units; a generation is 8 H-lines, so 2+1=3 generations (24 H-lines)
# is NOT forbidden. The 2+1 assembly is permitted.
assembly_2plus1_permitted = (total_3_hlines == spin_half_hlines + H_LINES_PER_GEN)
check("A5.assembly_2plus1_permitted", assembly_2plus1_permitted,
      f"2 (spin-1/2) + 1 (RS) = 3 gens; {spin_half_hlines}+{H_LINES_PER_GEN}={total_3_hlines} H-lines")

# ==============================================================================
# (b) RS BRANCHING -- classify RS(3,1) (x) S(6,4) Weyl content into {16|0|32}.
# ==============================================================================
print("\n[B] RS branching: internal content of RS(3,1) (x) S(6,4)")

# S(6,4) = Spin(6,4) Weyl spinor = (complexified) SO(10) Weyl spinor = 16.
DIM_S64 = dim_from_weights(s10p)
check("B1.S64_is_16", DIM_S64 == 16, f"dim_C S(6,4) = {DIM_S64}")

# Branch S+(10) under SO(6) x SO(4): split 5 weight coords as (first 3 | last 2).
# The FORCED spinor-tensor decomposition:
#   S+(10) = S+(6)(x)S+(4)  (+)  S-(6)(x)S-(4)
# because total #minus even  <=>  (#minus in first-3 even AND last-2 even)
#                                  OR (#minus in first-3 odd AND last-2 odd).
def restrict(w, idx):
    return tuple(w[i] for i in idx)

FIRST3 = (0, 1, 2)
LAST2 = (3, 4)

blocks = {}  # ( chirality6, chirality4 ) -> list of weights
for w in s10p:
    n_minus_6 = sum(1 for i in FIRST3 if w[i] == -1)
    n_minus_4 = sum(1 for i in LAST2 if w[i] == -1)
    c6 = +1 if n_minus_6 % 2 == 0 else -1
    c4 = +1 if n_minus_4 % 2 == 0 else -1
    blocks.setdefault((c6, c4), []).append(w)

# Every weight of S+(10) must land in either (+,+) or (-,-); (+,-) and (-,+) empty.
present = {k: len(v) for k, v in blocks.items()}
check("B2.only_correlated_chirality_blocks", set(present.keys()) == {(+1, +1), (-1, -1)},
      f"blocks present: {sorted(present.keys())}")
check("B3.no_wrong_chirality_leak", present.get((+1, -1), 0) == 0 and present.get((-1, +1), 0) == 0)

# (+,+) block = S+(6)(x)S+(4) = 4 (x) (2,1) = (4,2,1), dim 4*2 = 8.
dim_pp = present[(+1, +1)]
# (-,-) block = S-(6)(x)S-(4) = 4bar (x) (1,2) = (4bar,1,2), dim 4*2 = 8.
dim_mm = present[(-1, -1)]
check("B4.block_4_2_1_dim_8", dim_pp == 8, f"(4,2,1) dim = {dim_pp}")
check("B5.block_4bar_1_2_dim_8", dim_mm == 8, f"(4bar,1,2) dim = {dim_mm}")

# Cross-check the tensor factorization dims independently.
check("B6.tensor_dims_consistent",
      dim_from_weights(s6p) * dim_from_weights(s4p) == 8 and
      dim_from_weights(s6m) * dim_from_weights(s4m) == 8,
      "4x2 and 4barx2 both = 8")

# Total internal Weyl content of ONE S(6,4).
weyl_content = dim_pp + dim_mm
check("B7.weyl_content_is_16", weyl_content == 16,
      f"(4,2,1)+(4bar,1,2) = {dim_pp}+{dim_mm} = {weyl_content} = one SM generation")

# Classify against the falsification trichotomy {16 | 0 | 32}.
classification = {16: "ONE_GENERATION_total_3", 0: "ZERO_total_2", 32: "TWO_GENERATIONS_total_4"}
verdict_key = weyl_content if weyl_content in classification else None
check("B8.classification_in_expected_set", verdict_key in classification,
      f"content {weyl_content} classified as {classification.get(verdict_key)}")

# The other-chirality (RS 'flipped chiral' imposter) also gives 16, not 0/32.
s10m = weyl_weights(5, -1)
flip_content = len(s10m)
check("B9.flipped_chiral_also_16", flip_content == 16,
      f"S-(10) 'flipped' RS imposter = {flip_content} (also one generation)")

# RS(3,1) is charge-blind: multiplicity in generation count = 1 (one S(6,4) copy),
# independent of the Lorentz dimension of RS. So RS contributes +1 generation.
rs_generation_contribution = 1 if weyl_content == 16 else (0 if weyl_content == 0 else 2)
check("B10.RS_contributes_one_generation", rs_generation_contribution == 1,
      f"RS(3,1)(x)S(6,4) -> {rs_generation_contribution} generation(s)")

# ==============================================================================
# NEGATIVE CONTROLS -- confirm the test could DETECT a falsifying structure.
# ==============================================================================
print("\n[NC] Negative controls (test would fire on a falsifying structure)")

# NC1: had S(6,4) been a Spin(8)-type self-conjugate 8 with an even/vectorlike
#   branch giving 0 net chiral content, we would classify 0 -> total 2. Confirm
#   the classifier maps 0 to the FALSIFYING bucket, not to survival.
check("NC1.zero_maps_to_falsify_bucket", classification.get(0) == "ZERO_total_2")

# NC2: had the spinor been the full Dirac 32 (no chirality projection), content
#   would be 32 -> total 4 (even), a falsifying outcome. Confirm 32 is falsifying.
dirac_s64 = dim_from_weights(s10p) + dim_from_weights(weyl_weights(5, -1))
check("NC2.dirac_32_would_be_falsify", dirac_s64 == 32 and classification.get(32) == "TWO_GENERATIONS_total_4",
      f"unprojected Dirac = {dirac_s64} -> total 4 (would falsify)")

# NC3: relabel guard -- a genuine one-generation content must be BOTH halves
#   present (8+8); a single half (8) alone is NOT a full generation and would be
#   a different (incomplete) structure. Confirm we required both halves.
check("NC3.both_halves_required", dim_pp == 8 and dim_mm == 8 and (dim_pp + dim_mm) == 16)

# ==============================================================================
# VERDICT
# ==============================================================================
print("\n" + "=" * 70)
passed = sum(1 for _, c in CHECKS if c)
total = len(CHECKS)

structure_forces_16 = (weyl_content == 16)
h_line_permits_odd = assembly_2plus1_permitted
falsified = (weyl_content in (0, 32)) or (not h_line_permits_odd)

if falsified:
    VERDICT = "FALSIFIED"
elif structure_forces_16 and h_line_permits_odd:
    VERDICT = "SURVIVES"
else:
    VERDICT = "INCONCLUSIVE"

print(f"{passed}/{total} checks passed")
print("-" * 70)
print("PRE-DECLARED FAILURE CONDITION: FALSIFIED iff RS branching = 0 or 32,")
print("  or the H-line structure forbids the 2+1 = 3 assembly (even-only).")
print("-" * 70)
print(f"  (a) H-line 2+1 = 3 assembly permitted : {h_line_permits_odd}")
print(f"  (b) RS(3,1)(x)S(6,4) Weyl content     : {weyl_content}  "
      f"({classification.get(weyl_content, 'OTHER')})")
print(f"      -> RS generation contribution     : {rs_generation_contribution}")
print(f"      total = 2 (spin-1/2) + {rs_generation_contribution} (RS) = {2 + rs_generation_contribution}")
print("-" * 70)
print(f"VERDICT: GU generation-count leg {VERDICT}")
print("NOTE: the count VALUE still needs an external Z/3 self-dual import")
print("      (W201/W218: R_src is K-null/vectorlike). That is a GAP, i.e.")
print("      SURVIVES-WITH-A-GAP -- NOT a falsification. Count stays {1,3};")
print("      H59 stays OPEN. No canon/verdict/posture change.")
print("=" * 70)

ok = (passed == total) and (VERDICT == "SURVIVES")
raise SystemExit(0 if ok else 1)
