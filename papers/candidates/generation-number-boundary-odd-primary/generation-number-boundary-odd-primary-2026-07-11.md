# The Fermion Generation Number Is a Boundary Quantity in the Odd-Primary Summand

**Draft-of-record, started 2026-07-11. A GU-INDEPENDENT result (combines top-5 items #1 + #2).** This
paper does NOT claim three generations. It proves a structural no-go + localization for the family
puzzle: any topological generation count must live (i) in the odd-primary summand of the relevant stable
arena, and (ii) at a boundary (as an anomaly-inflow quantity) -- and it partitions the standard toolkit
by which invariants can possibly force it. Every theorem-grade step is independent of Geometric Unity;
GU appears only as the motivating sector, clearly marked.

## Abstract

We give two structural facts about a topological fermion generation number and combine them. **(I) A
primary-partition no-go.** In the stable arena `pi_3^s = Z/24 = Z/8 (+) Z/3` (Adams: `|Im J_3| =
denom(B_2/4) = 24`), the two summands are CRT-disjoint. We prove (elementary) that any invariant valued
in a finite 2-group or in a torsion-free abelian group vanishes on the 3-primary summand; hence a
2-primary or free invariant is *arithmetically incapable* of forcing an odd generation count. A census
shows the standard family-number tools partition exactly: the Dirac/Atiyah-Singer index, per-generation
anomaly cancellation, and all mod-`2^k` classes are 2-primary/free (cannot force an odd count), while the
Adams `e`-invariant, the Garcia-Etxebarria-Montero `Z/9` anomaly, the Wan-Wang-Yau beyond-cohomology
part, and equivariant Spin/KO `G`-indices reach the 3-primary summand (can). **(II) No net chirality
without a boundary.** On a closed structure with a purely cross-chirality invariant (Krein) form, every
symmetry-respecting operator conserves the net chiral index at zero -- the finite-dimensional shadow of
the Nielsen-Ninomiya no-go -- so a nonzero net count is necessarily a *boundary* anomaly-inflow quantity
(a domain-wall / edge mode). Combined: **a topological generation count, if it exists, is a boundary
quantity in the odd-primary summand.** This yields a falsifiable orientation for the family puzzle:
forcing an odd count requires a 3-primary-reaching *equivariant boundary* invariant (Dai-Freed / eta in
the odd-torsion summand); the whole 2-primary bulk toolkit is a dead end.

## 1. The primary-partition lemma (rigorous spine)

**Lemma.** *Let `G` be a finite cyclic group with `3 | |G|`, and `S_3 <= G` its 3-Sylow subgroup. If `H`
is a finite 2-group or a torsion-free abelian group, then every homomorphism `phi: G -> H` vanishes on
`S_3`.*

*Proof.* `phi|_{S_3}` factors through `Hom(S_3, H)`. If `H` is a finite 2-group of order `2^k`, then
`|Hom(Z/3^a, Z/2^k)| = gcd(3^a, 2^k) = 1`, so the only map is 0. If `H` is torsion-free, a finite
subgroup maps to a finite subgroup of `H`, which is trivial; so `phi(S_3) = 0`. QED.

Applied to `pi_3^s = Z/24`: the order-3 elements `{8, 16}` (the summand `Z/3`) are killed by every
2-primary or free invariant. Verified computationally: `tests/family-puzzle/primary_partition_lemma.py`
(exit 0).

## 2. The census (each entry a standard result -- TO VERIFY vs primary sources)

| Tool | value group | 3-Sylow reach | can force odd count? |
|---|---|---|---|
| Dirac / Atiyah-Singer index | `Z` | trivial | no |
| per-generation anomaly cancellation | `Z` | trivial | no |
| mod-2 Witten anomaly | `Z/2` | trivial | no |
| Rokhlin invariant | `Z/16` | trivial | no |
| spinor 2-smoothness (`dim 2^k`) | `2^k` | trivial | no |
| Adams `e`-invariant / `J`-homomorphism | `Z/24` | `Z/3` | **yes** |
| Garcia-Etxebarria-Montero anomaly | `Z/9` | `Z/9` | **yes** |
| Wan-Wang-Yau beyond-cohomology `p_1` | (3-primary) | nonzero | **yes** |
| equivariant Spin/KO `G`-index (order-3) | `Z/3` | `Z/3` | **yes** |

The tools that *have* constrained the generation number in the literature are exactly the
3-primary-reaching ones. [GAP: verify each value group against primary sources; cite.]

## 3. No net chirality without a boundary

**Proposition (finite-dimensional).** *Let a matter sector carry a purely cross-chirality invariant Krein
form `K` (signature `(+n,-n)`, pairing the chirality eigenspaces `W_+, W_-` as complementary
`K`-Lagrangians). Then every `K`-isometric linear operator conserves the net chiral index at zero.*
*Proof.* A maximal `K`-positive subspace `P` meets each `K`-null `W_\pm` only at 0, so projects
isomorphically onto both -- it is the graph of an isomorphism `W_+ -> W_-`, hence chirality-balanced,
`chi(P)=0`; a `K`-isometry preserves this. QED. (Machine + symbolically verified.)

This is the finite-dimensional shadow of **Nielsen-Ninomiya**: on a compact Brillouin torus, net
chirality summed over the zone vanishes (fermion doubling). The escape in both settings is a **boundary**:
a domain wall / gapless edge carries net chirality equal to the bulk topological (Chern) invariant, the
closed system staying net-zero -- anomaly inflow (Callan-Harvey; Kaplan domain-wall fermions). Computed:
`tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py`. [GAP: the cross-setting identification
(finite-dim Krein <-> compact-BZ lattice) is a structural correspondence, not one formal theorem -- state
the shared principle precisely.]

## 4. The combined statement and the falsifiable prediction

Sections 1-2 place a topological count in the odd-primary summand; Section 3 places it at a boundary.
**Therefore a topological fermion generation count, if it exists, is a boundary anomaly-inflow quantity
valued in the odd-primary (3-primary) summand.** Falsifiable orientation for the family puzzle:

> A topological approach can force an odd generation count ONLY IF its invariant is (a) 3-primary-reaching
> and (b) an equivariant *boundary* invariant. The entire 2-primary bulk toolkit (Dirac index, mod-`2^k`
> classes, per-generation anomaly) is arithmetically incapable, no matter how natural.

This predicts *which* future approaches can possibly work (equivariant Spin/KO `G`-indices; Dai-Freed /
eta invariants in the odd-torsion summand) and which are dead ends.

## 5. Relation to prior art

Constraining the family number from topology has precedent -- Garcia-Etxebarria-Montero (`Z/9 -> N_gen in
3Z`), Wang (framed/string bordism `Z/24`), Wan-Wang-Yau (cohomology-vs-Pontryagin split isolating `n=3`).
Our contribution is the **inverse reading**: the *no-go* structure (2-primary tools are blind to the
3-primary count) + the *boundary localization*, which together partition the toolkit and predict
viability. We claim no novelty for the bare `24 = 8 x 3` factorization. [GAP: full literature comparison;
confirm the inverse-reading + boundary-localization novelty.]

## 6. What is not claimed

No claim of three generations; `order-3-class -> integer-3` stays open (`Hom(Z/3,Z)=0`: an integer needs a
relative/equivariant index). GU appears only as motivation; every theorem-grade step is GU-independent.

## Status / open gaps to close before submission

1. Verify the Section-2 census value groups against primary sources (cite each).
2. State the Section-3 shared principle precisely (the finite-dim/lattice correspondence).
3. Confirm the Section-5 novelty claim with a full literature search.
4. Two figures: the primary-partition table; the domain-wall net-chirality (bulk 0, edge ±1).

Grade: Lemma (Section 1) rigorous + computed; census computed, source-verification pending; Proposition
(Section 3) rigorous finite-dim + standard N-N; the combined statement and prediction are the
contribution. Target venue: hep-th / math-ph. External publication Joe-gated.
