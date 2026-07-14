# Staging Notes: generation-number-boundary-odd-primary

**Candidate:** `generation-number-boundary-odd-primary-2026-07-11.md`

## Scope

GU-independent structural packet for the fermion generation-count problem. The candidate combines two claims:

1. A primary-partition no-go: in the stable arena `pi_3^s = Z/24 = Z/8 (+) Z/3`, invariants valued in a
   finite 2-group or in a torsion-free abelian group vanish on the 3-primary summand, so 2-primary/free tools
   cannot force an odd generation count.
2. A boundary-localization claim: closed cross-chirality/Krein or compact-lattice settings conserve net
   chirality at zero, while a nonzero count must be supplied by boundary/anomaly-inflow data.

The resulting orientation is deliberately conditional: a topological generation count, if it exists, must live
in an odd-primary boundary invariant. The note does not claim three generations, does not promote GU, and does
not move any claim status or paper status.

## Honest grade

**Mixed structural-candidate grade.** The primary-partition lemma is theorem-grade elementary algebra and is
checked by `tests/family-puzzle/primary_partition_lemma.py`. The finite-dimensional no-net-chirality proposition
is theorem-grade at its stated finite-dimensional scope, and the domain-wall/Nielsen-Ninomiya analogy is
computationally exercised by `tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py`.

The census of standard family-number tools, the finite-dimensional Krein / compact-BZ correspondence, and the
novelty/prior-art positioning remain source-verification and exposition obligations. The candidate is staged as
a bounded research packet, not as a ready publication or as a derivation of the generation count.

## Light staging gate (per `papers/candidates/README.md`)

1. Title matches the theorem-grade core: PASS. "Boundary Quantity in the Odd-Primary Summand" states the
   localization/no-go result and does not claim a value of 3.
2. No retracted or downgraded wording: PASS WITH OPEN GAPS. The candidate states the theorem-grade algebra,
   separates the census as source-verification pending, and names the finite-dimensional/lattice correspondence
   as a gap rather than a single formal theorem.
3. External citations resolve: PENDING. The packet names Adams, Garcia-Etxebarria-Montero, Wan-Wang-Yau,
   Nielsen-Ninomiya, Callan-Harvey, and Kaplan, but the Section 2 census and Section 5 novelty comparison still
   explicitly require primary-source verification.
4. Sharpest open issue acknowledged in-text: PASS. The status section names source verification, the precise
   finite-dimensional/lattice correspondence, novelty confirmation, and figure work before submission.
5. Overlap with other staged candidates: DELINEATED. `generation-number-located-not-forced/` carries the
   class-wide forcing no-go plus `{1,3}` and SU(2)+ reduction; `located-not-forced/` carries the 2-primary
   Clifford RS obstruction. This candidate is the boundary/odd-primary localization packet feeding those later
   forcing and obstruction results.

## Open items (ranked)

1. Verify every Section 2 census value group and 3-primary-reach statement against primary sources, then cite
   each one explicitly.
2. State the finite-dimensional Krein / compact-BZ / domain-wall correspondence at the right formal strength so
   the analogy is neither underclaimed nor silently promoted to an identity.
3. Complete the prior-art comparison for the inverse-reading plus boundary-localization novelty claim.
4. Add the two named figures only after the paper text and source citations are stable.

## Before posting

Keep this as a staged candidate until the source census and novelty comparison are closed. Any submission,
upload, DOI/tag/release action, publication move, or public-posture change remains Joe-gated.
