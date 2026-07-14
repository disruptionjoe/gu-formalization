# The Generation Number is Located, Not Forced: A Class-Wide No-Go and the SU(2)+ Reduction

**Draft, 2026-07-11; revised 2026-07-13 (prior-art fixes from `review/prior-art-sweep-2026-07-13.md` folded in;
claim-to-test verification map added, see `VERIFICATION.md` in this folder). GU-INDEPENDENT: the results below are
about the generation-counting problem in any framework that selects the count by a
topological/representation-theoretic invariant; Geometric Unity appears only as the source of one named (unclosed)
escape route. External publication is Joe-gated (no arXiv, no submission in scope here). Every quantitative claim
ties to a reproducible test in `tests/` (W55-W60, all exit 0; re-run 2026-07-13, all exit 0).**

## Abstract

Why are there exactly three fermion generations? We ask a sharper, answerable question: can the count be FORCED
from first principles, and if not, exactly what is missing? Attacking the problem through five independent
constructions of "what the count is" -- an Atiyah-Singer index, an anomaly-inflow boundary invariant, a
cobordism/K-theory class, a 3-primary homotopy-torsion class, and an adversarial no-go -- we prove a **class-wide
no-go**: the generation number is not forced by first-principles topological selectors. It is a mod-3 torsion
datum, forced into `{1, 3}` and 3-primary (two, four, and higher counts are excluded by the self-dual 2-form
structure of the 4-manifold; the ceiling `3 = dim Lambda^2_+(R^4)`), but the value 3 over 1 is not forced: the
sterile one-generation solution is anomaly-free and admissible. The constructions converge on a single escape
hatch -- promoting the discrete self-dual `Z/3` to the continuous `SU(2)_+` (the chiral half of the local frame
group). We then close that hatch as a first-principles route: `SU(2)_+` is indeed gauged, but gauging never
forces its matter into the adjoint, so it does not force the generation multiplet to be `Lambda^2_+`. Forcing 3
is provably equivalent to identifying the family bundle with the self-dual frame adjoint -- an identification of
spin with flavor that first principles do not supply. The result turns "located, not forced" from an intuition
into a theorem, and pinpoints the exact new input any derivation of 3 must add.

## 1. Introduction

The number of fermion generations, three, is among the sharpest unexplained facts in particle physics. A body of
work has *located* the count without *deriving* it: it is odd-primary / 3-primary rather than an integer index
(the relevant homotopy is `Z/3 subset pi_3^s = Z/24`), and it is a boundary / anomaly-inflow quantity
(Nielsen-Ninomiya; Callan-Harvey; Kaplan; the cobordism analyses of Garcia-Etxebarria-Montero, arXiv:1808.00009,
and Wan-Wang, arXiv:1910.14668; the 2026 conditional-uniqueness result of Wan-Wang-Yau, arXiv:2605.26202). A
separate literature *does* force the count, but always from added structure: `N_gen = |chi|/2` once a Calabi-Yau
compactification is chosen (Candelas-Horowitz-Strominger-Witten 1985), `N_gen = 3` from 6d anomaly cancellation
given two universal extra dimensions (Dobrescu-Poppitz, hep-ph/0102010), from 331-type gauge extensions, or from
gauging baryon triality (Garcia-Etxebarria-Montero's `Z/9` result). What has been missing is a precise statement
of whether "located, not forced" is a limitation of
particular tools or a theorem, and of exactly what extra input would force the value.

We answer both. The question decomposes into three decidable sub-questions:
- **Q-force:** does a construction FORCE a specific count (3), or only CONSTRAIN it (odd / 3-primary / `<= 3`)?
- **Q-extra:** if it only constrains, what is the minimal extra input that pins 3, and is it a first-principles
  condition or a free choice?
- **Q-nogo:** can one prove no first-principles selector of a given kind forces 3, and is the no-go
  construction-specific or class-wide?

We run five independent, mutually blind constructions of "what the count is," on the principle (validated below)
that a no-go in one construction need not transfer to another: the integer-index construction famously cannot
reach the count, but a torsion construction can. Only a wave that runs all of them blind can distinguish "this
tool fails" from "every tool fails."

## 2. Setup

**The arena.** Two facts anchor everything. First, `3 = dim Lambda^2_+(R^4)`: the self-dual 2-forms on the
oriented 4-manifold form a 3-dimensional space, the adjoint of `SU(2)_+`, the self-dual (chiral) half of the
frame group `SO(4) = SU(2)_+ x SU(2)_-` (`Spin(4) = SU(2) x SU(2)`). Second, the relevant homotopy summand is
`Z/3 subset pi_3^s = Z/24 = Z/8 (+) Z/3`: the 3-Sylow part, where an integer index cannot land.

**The five constructions** (each a rival answer to "what is the count"):
- **A -- Atiyah-Singer index / Dirac** (net chirality as an integer index).
- **B -- anomaly inflow** (a boundary-localized invariant, Callan-Harvey / Kaplan).
- **C -- K-theory / cobordism** (a torsion bordism class, Garcia-Etxebarria-Montero / Wan-Wang).
- **D -- 3-primary homotopy torsion** (a torsion class in `pi_3^s`, acting on `Lambda^2_+`).
- **E -- adversarial no-go** (an obstruction to forcing).

**The construction-fork principle.** These constructions are not interchangeable. The prior "family-puzzle"
result is exactly the statement that an integer-index construction provably cannot reach a `Z/3` torsion class
(`Hom(Z/3, Z) = 0`): the answer's reachability depends on which construction one uses. Running blind prevents
defaulting to the index picture (where the count famously cannot be forced) and missing whether a torsion picture
reaches it.

## 3. Result 1: a class-wide no-go

The four constructive branches, blind to one another, converge on the same obstruction, each from its own side
(`tests/W55-W58`):

- **Index (A):** the integer Dirac index constrains the count (`= 0 mod 3` on closed spin 4-manifolds, via
  `p_1 = 3 sigma`) but cannot force it (`Hom(Z/3, Z) = 0`). Torsion-valued indices (the reduced eta / Adams
  e-invariant, order 3; mod-3k Freed-Melrose) reach the `Z/3` arena but produce a class, not the integer 3.
- **Anomaly inflow (B):** inflow locates and quantizes but does not force; the boundary invariant is Z-valued (a
  free bulk winding/level choice), and the one forced first-principles condition -- anomaly-freedom -- lands in
  the 2-primary arena, coprime to 3.
- **Cobordism (C):** the group is `Omega^Spin_5(BG)`, framing channel `pi_3^s = Z/24`, 3-primary summand `Z/3`.
  The structure forces the modulus 3 (the arena is `Z/3`, `3 = |Z/3| = dim Lambda^2_+`) but not the value 3; the
  anomaly is a homomorphism, hence constrains only mod an order, and the Standard-Model per-generation Dai-Freed
  anomaly vanishes. That generation-blindness is a known computation, not a finding of this branch: it follows
  from the bordism groups of Davighi-Gripaios-Lohitsiri (arXiv:1910.11277, for arbitrary fermion content across
  all four SM gauge-group quotients) and from Garcia-Etxebarria-Montero and Wan-Wang; we use only its 3-primary
  corollary `Omega^Spin_5(BG_SM) (x) Z_(3) = 0`. Scope: this holds for `G_SM` with plain spin structure. In the
  `Spin x_{Z2} Z4` refinement the `Z/16` anomaly DOES count fermions mod 16 (generation-sensitive), but it is
  2-primary, coprime to the 3-primary arena where the count lives, which sharpens rather than weakens the point.
  No-go via `Aut(Z/3) = Z/2`, `Hom(Z/3, Z) = 0`, and linearity.
- **Homotopy torsion (D), the reachable construction:** the order-3 element acts on `Lambda^2_+ = R^3` as an
  element of `SO(3) = SU(2)_+`, splitting `R^3 = ` (fixed axis, dim 1) `(+)` (rotated pair, dim 2). The realized
  rank is odd, hence in `{1, 3}`. So the torsion bounds (ceiling 3) but does not force: the rank-1 fixed axis is
  admissible.

**The adversarial branch (E) closes this into a theorem** (`tests/W59`): a residual-freedom result -- the rank-1
solution (the `SO(3)` fixed axis) is admissible whenever rank-3 is, and no first-principles condition
(equivariance, reality, self-adjointness, oddness, anomaly-freedom) separates `{1, 3}`. It is class-wide over all
four constructions, with a uniform reason: **the count is a torsion (mod-3) datum with no canonical integer
value, realized as an invariant subspace whose odd choices `{1, 3}` nothing separates.** It survives its own
steelman: the condition that would force 3 (faithfulness/maximality, excluding the sterile axis) is not
first-principles -- a sterile trivial self-dual direction is consistent and anomaly-free (rank 1 cancels all
anomalies), and the mod-3 Dai-Freed arena is empty (`Omega^Spin_5(BG_SM) (x) Z_(3) = 0`).

## 4. Result 2: what IS forced

The no-go is not "nothing is forced." The constructive branches force a sharp, non-trivial positive statement:
- the count is **3-primary** (it lives in `Z/3`, defined mod 3);
- the **ceiling is exactly 3** `= dim Lambda^2_+(R^4)`;
- **oddness excludes 2**; the realized count is in `{1, 3}`.

So **the number of generations is forced to be 1 or 3, and 3-primary.** Counts of 2, 4, 5, ... are excluded by
the self-dual 2-form structure of the 4-base. This answers "why not 2, why not 4, why 3-primary" while leaving
exactly one thing open: 3 versus the sterile 1.

Two scope notes on this bound. First, the oddness premise (a net chirality is an odd datum) is imported from a
prior leg of this program, not re-derived here; without it the invariant ranks are `{0, 1, 2, 3}` and the forced
content is the 3-primary/ceiling statement alone. Second, the closest published result, Wang (arXiv:2312.14928),
derives `N_f in 3Z` in exactly this arena (`pi_3^s = Z/24`, the 3-Sylow), which EXCLUDES `N_f = 1`. There is no
contradiction: Wang's conclusion requires his postulates (topological robustness of the 16-Weyl family and the
`c_- = 0 mod 24` modular-invariance condition), which are precisely non-first-principles extra input by the
standard of this paper. Our `{1, 3}` admits the sterile 1 because we do not assume them.

## 5. Result 3: the SU(2)+ reduction (the escape hatch, closed as a first-principles route)

Branches D and E independently name the single escape: promote the discrete order-3 element to the continuous
`SO(3) = SU(2)_+`. Under the connected group, `Lambda^2_+ = R^3` is irreducible, so any nonzero matter content
forces rank `= 3 = dim adjoint SU(2)_+`. We test whether that promotion is first-principles (`tests/W60`), by two
independent derivations that agree:

- **Representation theory:** `SU(2)_+` *is* a genuine continuous gauged symmetry -- it is the self-dual half of
  the local frame group, gauged by the spin connection. But **gauging a group never forces its matter into the
  adjoint.** `Rep(SU(2))` contains an irrep of every dimension; the trivial singlet (rank 1) and the adjoint
  (rank 3) are both admissible. Schur's lemma forces rank 3 *only given* the premise C1 -- that the generation
  multiplet is the `SU(2)_+`-equivariant adjoint bundle `Lambda^2_+` -- which is the answer inserted as a
  hypothesis.
- **Consistency / anomaly:** the sterile `SU(2)_+`-singlet sector survives gauging: it is anomaly-free
  (one generation cancels all anomalies) and the mod-3 Dai-Freed arena is empty. So gauging `SU(2)_+` does not
  obstruct the sterile solution.

The decisive obstruction is physical and sharp: **the frame `SU(2)_+` acts on SPIN, whereas the generation label
is a Lorentz-SCALAR (flavor).** The frame group therefore acts trivially on generations unless spin is identified
with flavor by hand. Promoting `Z/3 -> SU(2)_+` *relocates* the sterile axis (from an internal `Z/3` subspace to
an external `SU(2)_+` singlet); it does not forbid it. Hence:

**Forcing the generation number to 3 is provably equivalent to identifying the family bundle with the self-dual
frame adjoint -- an identification of spin with flavor that first principles do not supply.**

One named, unclosed route remains, and we flag it honestly rather than lean on it: a graded/"guardian" structure
(in Geometric Unity, the "super-IG" sector) in which the supercharge closes on the spin connection
(`{Q, Q} ~ Omega^1(ad)`) could make the family bundle frame-covariant and adjoint-valued natively, closing C1
and forcing 3. This route is named, not closed: in Geometric Unity such a structure was examined and found *not*
to be a spacetime symmetry, so it is a long shot (`tests/W60` records it as unestablished, an explicit assert),
and in any framework it is the precise extra input a derivation of 3 must supply.

## 6. Synthesis and honest scope

The three results cohere: the count is forced into `{1, 3}` and 3-primary (Result 2); it cannot be forced to 3
by any first-principles topological selector (Result 1); and forcing 3 is exactly the spin-flavor identification
C1, which the standard structure does not provide (Result 3). "Located, not forced" is thereby a theorem, with
the residual freedom reduced to one precisely-named condition.

What this is, and is not:
- It is **not** a derivation of three generations (that needs C1 closed).
- It **is** a correctly-scoped no-go on a famous problem -- a proof that the standard topological tools cannot
  force the count, and an exact identification of the single missing input -- and it is independent of any
  particular unified theory.
- Grades: the mathematical cores (the `Hom`/Schur/`{1,3}`/residual-freedom statements) are theorem-grade and
  checked by deterministic computation against standard, citable mathematics; the framework-facing legs (whether
  a given physical theory's generation sector is the torsion class in question) are argued at reconstruction
  grade, not proven.

## 7. Relation to prior work

- **Location of the count in the 3-primary / mod-3 arena.** Garcia-Etxebarria-Montero (arXiv:1808.00009) show
  that gauging baryon triality (a discrete `Z/3` beyond `G_SM`, with `Omega^Spin_5(BZ_3) = Z/9`) yields a `Z/9`
  Dai-Freed anomaly cancelling only for generation numbers divisible by 3. Wang (arXiv:2312.14928) derives
  `N_f in 3Z` from framed/string-bordism (`Z_24`) and `c_- = 0 mod 24` modular-invariance constraints.
  Wan-Wang-Yau (arXiv:2605.26202) single out `N_c = N_f = 3` as the unique solution given odd colour number, a
  `Z_{N_c}` colour symmetry extension, and TQFT replacement of missing sterile neutrinos. Each forces the count
  only given a further condition (a gauged discrete symmetry; topological robustness of the 16-Weyl family; the
  extension ansatz): instances, in our language, of extra input closing the residual freedom. In particular our
  `{1, 3}` bound admits the sterile `N_f = 1` solution precisely because we do not assume them. Delta: we prove
  the location is a *no-go for forcing*, not merely a locating statement, and we add the `{1, 3}` bound and the
  `SU(2)_+` reduction.
- **Generation-blindness of the SM anomaly (known, used, not claimed).** Freedom of the four SM gauge-group
  quotients from global anomalies for arbitrary fermion content, hence for any generation number, was
  established by Davighi-Gripaios-Lohitsiri (arXiv:1910.11277) via `Omega^Spin_5(B(G_SM/Gamma_n))`, and by
  Garcia-Etxebarria-Montero and Wan-Wang (arXiv:1910.14668) in the Dai-Freed / cobordism setting; we use only
  the 3-primary corollary `Omega^Spin_5(BG_SM) (x) Z_(3) = 0`. In the `Spin x_{Z2} Z4` refinement the `Z/16`
  anomaly does count fermions mod 16 (arXiv:1808.00009; Wang-Wen, arXiv:1809.11171): a generation-sensitive but
  2-primary constraint, coprime to the 3-primary arena where the count lives.
- **Topology DOES force the count once compactification data is chosen.** `N_gen = |chi|/2` for Calabi-Yau
  compactifications (Candelas-Horowitz-Strominger-Witten, Nucl. Phys. B258 (1985) 46) and Kaluza-Klein index
  counting (Witten 1983). Our no-go is the statement that the choice of internal manifold and bundle is itself
  the non-canonical extra input: no such selector is supplied by first principles. Likewise 6d anomaly
  cancellation (Dobrescu-Poppitz, hep-ph/0102010; bordism refinement Davighi-Lohitsiri, arXiv:2012.11693) and
  331-type gauge extensions (Pisano-Pleitez; Frampton) force 3 at the cost of assuming the enlarged arena.
- **Frame-chirality-as-internal-quantum-number has been proposed, not derived.** Graviweak / graviGUT
  unification identifies the self-dual `SU(2)` with weak isospin and obtains one family from `SO(3,11)`
  (Nesti-Percacci, arXiv:0706.3307, arXiv:0909.4537; cf. Woit, arXiv:2104.05099, where the generation number is
  explicitly left unexplained), and spinorial family unification posits families inside enlarged spin
  representations (BenTov-Zee, arXiv:1505.04312; arXiv:1706.03116; Mankoc-Borstnik). Our Result 3 explains the
  pattern: forcing 3 is equivalent to such an identification, which is why these constructions must insert it as
  a premise. A precedent for a rigorous no-go about generation embedding is Distler-Garibaldi (arXiv:0905.2658)
  for `E8`.
- **Algebraic derivations of 3** from 3x3 octonionic / triality structure (Dubois-Violette, arXiv:1604.01247;
  Todorov-Dubois-Violette; Boyle, arXiv:2006.16265; Furey-Hughes, arXiv:2409.17948) select the count from a
  chosen algebra rather than from `Lambda^2_+`; the algebra choice is again extra input in our sense.
- **The odd-primary / Hom-obstruction ("family-puzzle") result:** the prior in-repo theorem that a selector
  forcing a 3-primary count needs nonzero 3-Sylow image (`Hom(Z/3, Z) = 0`; `Hom(Z/3, Z/2^k) = 0`; Toda / Adams
  / von Staudt-Clausen inputs). Delta: that theorem is Leg 1 of the present no-go (the unreachable
  constructions); this paper adds Leg 2 (the residual `{1, 3}` freedom in the REACHABLE torsion constructions),
  the class-wide synthesis, and the `SU(2)_+` reduction, closing the gap the family-puzzle result explicitly
  left open ("does not derive the integer 3").
- **Anomaly inflow / no net chirality without a boundary:** Nielsen-Ninomiya (Nucl. Phys. B185 (1981) 20);
  Callan-Harvey (Nucl. Phys. B250 (1985) 427); Kaplan (Phys. Lett. B288 (1992) 342). Delta: we show inflow
  quantizes but does not force, and that its forced content is 2-primary.
- **Cobordism classification of anomalies:** Freed-Hopkins (arXiv:1604.06527). Delta: we use it to prove the
  anomaly is a homomorphism, hence constrains the count only mod an order.

## 8. Status / open gaps

1. **DONE:** the five-construction no-go, the `{1, 3}` forced content, and the `SU(2)_+` reduction are
   reproducible in-repo (`tests/W55-W60`, all exit 0), each carrying its honest grade.
2. **The single open input:** close (or refute) C1 -- the spin-flavor identification / a genuine anomaly
   forbidding the sterile axis. This is the exact new physics any derivation of 3 must add.
3. **Target framing:** the natural paper is this trio -- the no-go, the `{1, 3}` bound, and the `SU(2)_+`
   reduction -- as a GU-independent structural contribution to the generations problem.

Grade: structural result at honest grade; the mathematical cores are theorem-grade and computation-checked; no
derivation of the value 3 is claimed. Target: hep-th / math-ph. External publication Joe-gated (NOT in scope
here: no arXiv, no submission).
