"""GU attention priority: Condorcet ranking over the science-advisory council's five archetypes.

PURPOSE. This is the ranking ENGINE for the GU work card (JoeOps WI-068). Joe does not read the card; when
he has attention to give to GU, he wants a prioritized list of what to work on. That list is produced by a
Condorcet vote across the five council archetypes over the current hypothesis/next-move set
(explorations/science-advisory-council-full-picture-2026-07-11.md).

Condorcet is the PRIMARY ranking mode: item X outranks item Y if a MAJORITY of the five archetypes prefer X
to Y. When a strict Condorcet order exists it is used; when there is a cycle (Condorcet paradox) we fall back
to Copeland scores (count of pairwise wins minus losses), which always yields a full order and agrees with the
Condorcet winner when one exists. This makes ties and cycles explicit rather than hidden.

RE-RANKING AFTER A SWING (lightweight, per Joe's spec). After a significant swing toward one hypothesis:
  - if the swing RESOLVED it (cleared/killed): set its ballot rank to 'done' in every archetype (drop it), OR
    remove it from ITEMS; re-run.
  - if the swing STRENGTHENED/WEAKENED it: nudge its position up/down in the 1-2 archetypes whose stated
    values that swing served, and re-run. Do NOT re-elicit all five from scratch -- only move what moved.
The re-rank is just: edit BALLOTS below, run `python attention/gu_priority_condorcet.py`, paste the output
list onto the card. Cheap and reproducible by design.

Run: python attention/gu_priority_condorcet.py
"""
from __future__ import annotations

from itertools import combinations

# --- the candidate hypotheses / next moves (the council's decision set) ---
# RESOLVED in Wave 1 / Wave 10 (2026-07-11), dropped from the live set:
#   H1 -> gravity CLEARS in the Bach branch (Bach tensor of exact Schwarzschild = 0 all orders; Kerr
#         Ricci-flat), REDUCED to the conformal-invariance datum. tests/wave1/H1_bach_flat_exact_vacua.py.
#   H3 -> DESI verified vs arXiv:2503.14738 (recall was correct; GU ~3-4 sigma on wa, a standing FALSIFIER);
#         the theta INT gravity over-determination WEAKENS under the corrected M^2/r^6 residual (f0 not
#         pinned by gravity). tests/wave1/H3_desi_verified_and_intersection.py.
#   H27 -> the soldering is PROVABLY a genuine postulate: Palatini variation of |theta|^2 does NOT force
#          pi onto the spin-lift; the conditional theorem is the final state within the built structure.
#          tests/wave10/H27_soldering_palatini.py.
ITEMS = {
    # Wave 5: H21 PROVEN (s*(theta)=II_s off-shell, fork does NOT re-open) + H16 CONTESTED-CORNER (antigravity
    # kill retired). BOTH collapse gravity's residual onto ONE object: A = spin-lift(grad^gimmel) = the source
    # action. Gravity is HARD-clear MODULO that object. -> H23 (attempt it) + H24 (the R^Y firm-up).
    # H23 RESOLVED (Wave 8) -> PARTIAL: the spin-lift is canonical AS A MAP + the Krein [P,S]=0 holds (ghost
    # clears structurally); but the SOLDERING (pinning theta to the spin-lift image, codim-8165) is NOT forced
    # -- a single honest postulate. Gauge group sharpened to NON-COMPACT Sp(32,32;H). Gravity = a CONDITIONAL
    # THEOREM (tree-level Stelle-clear, positive decoupled ghost) modulo {the soldering postulate + mu_DW}.
    # H27 RESOLVED (Wave 10) -> the soldering is a genuine postulate, not an unclosed forcing gap; drop it
    # from the live decision set and let attention move to the next unresolved item.
    # --- "PUSH FURTHER" decision set (2026-07-11): each archetype's top-3 next ideas, pooled + deduped.
    # Gravity is a proven conditional theorem; DE is a soft tension; both route to the one unbuilt source
    # action; the fermion/C2 wall (where the count lives) is untouched. ---
    # PARALLEL BATCH (Waves 20-23, 2026-07-11) -- four independent probes fanned out at once:
    # H10 RESOLVED (Wave 22, tests/wave22): PPN GATED-ON-mu_DW, effectively PASSES. GU = R^X+Weyl^2+Lambda has
    #   no R^2 -> pure Einstein-Weyl (massless graviton + one massive spin-2); gamma-1=-(2/3)e^{-m2 r} Yukawa-
    #   suppressed; Cassini needs mu_DW > ~1e-17 eV, natural M_Pl clears it by ~45 orders. A real 4th-order-
    #   gravity falsifier, PASSED. Dropped from the live set (next object mu_DW = existing H24/H25 BAR 2).
    # H26 RESOLVED (Wave 23, tests/wave23): loop ghost unitarity OPEN. The [P,S]=0 COMMUTATION leg is proven
    #   radiatively stable (P is an EXHIBITED group symmetry: Cartan involution = conj by eta in O(9,5); beta_S
    #   in Sp(32,32;H); every so(9,5)-covariant vertex commutes exactly, inherited to all loops). But loop
    #   POSITIVITY (weak ghost symmetry tr(C^dag C)=0, broken by IR regulators) needs an S-matrix -> the source
    #   action (H41). A missing OBJECT, not a missing calc. Routes to H41; dropped from the live set.
    "H28": "Fermion masses / Yukawas: the SM is cleared only at GAUGE-GROUP grade. Does GU predict the mass hierarchy + mixings, or just the algebra? Where unification programs historically die. [orthodox]",
    # H29 (Wave 12) NARROWED + H37 (Wave 13) NO-GO -> the count is PROVABLY located-not-forced within the built
    # (9,5) structure (fermion analog of H27). Seven-axis map (L0-L7): L0 baseline + L1-L6 selector-side all
    # LOCKED; L7 = the (9,5)/(7,7) signature was flagged as the sole live escape (= the old H19).
    # H19 RESOLVED (Wave 14, tests/wave14/H19_seven_seven_branch.py, exit 0): adopting (7,7) is LIVE-BUT-NON-
    # DERIVING. It lifts the Kramers 2-primary VETO (odd ranks 1,3,5,7 become admissible) but is STRUCTURALLY
    # INCAPABLE of supplying the count: the signature is a 2-primary datum (Z/8), the 3 lives in the orthogonal
    # Z/3 arena, |Hom(Z/8,Z/3)|=1 (zero map). The triplet carrier is neutral Krein (net index 0) in BOTH sigs.
    # So the count does NOT collapse onto the signature; (7,7) trades a false constraint for MORE freedom and is
    # NOT recommended. H19 drops from the live set. The count's REAL decider is signature-INDEPENDENT -> H38.
    # H38 RESOLVED (Wave 15, tests/wave15/H38_z3_chiral_selector.py, exit 0, 11/11) = NARROWED. A DERIVED Z/3 IS
    # present in the built (9,5) matter sector (the order-3 subgroup of the self-dual SU(2)+ on the 192=3x64
    # triplet; the 3 = dim Lambda^2_+(R^4), forced by the 4-base, not imported, not ambient triality). But
    # ghost parity [P,S]=0 is 2-primary and index-PRESERVING (chiral index fixed=0 for every ghost-parity S) ->
    # it PERMITS the vectorlike 3+3, cannot SELECT a chiral 3. H38=H26 only on the unitarity leg (shared Z2);
    # the count leg W is Z/3, arena-orthogonal (gcd(2,3)=1). The count decider must be 3-primary AND
    # index-CHANGING (non-Krein-unitary) -> that is a SOURCE-ACTION K-class selection, not a ghost-parity
    # condition. H38 drops from the live set; the count's real decider is H39.
    # H39 RESOLVED (Wave 16, tests/wave16/H39_sourceaction_kclass.py, exit 0, 14/14) = NARROWED to a
    # conditional-theorem TWIN of gravity. Carrier B (index -38, rho (0,2,1)) is the UNIQUE index-changing
    # carrier -> any count-selector must be B; but which carrier the source action NAMES is a field-space
    # declaration arithmetic cannot force (gamma-trace-constrained -> B; full field space + BRST -> A), GU
    # commitments B-lean. The count is odd/nonzero with a DERIVED ceiling dim Lambda^2_+=3, realized rank in
    # {1,3}, not pinned (a net index 3 has residue 0 = A's, so no residue certifies 3). NEW (Q3): selecting the
    # count does NOT break gravity's [P,S]=0 -- arena-orthogonal (gcd(2,3)=1) and self-adjoint != index 0
    # (K3 Dirac witness). So gravity's soldering (H27) AND the count's K-class (H39) are COHERENT field-space
    # declarations of the SAME source action. Both reduce to ONE forced build -> H40.
    # H40 RESOLVED (Wave 17, tests/wave17/H40_terminal_sourceaction.py, exit 0, 14/14) = NARROWED, the
    # maximally-hardened terminal state. The Porrati-Rahman causal window IS a genuine structural forcing (the
    # built C2=155.36 leakage is a real VZ acausality on curved Y14, degree-1 -> cure DEMANDED), collapsing the
    # 4-corner residual to the 2 causal cures {A,B} -- one bit removed. But BOTH are causal, so the final
    # constrain(B)-vs-gauge(A) bit stays a B-LEANING LEAN, not forced. Count STAYS {1,3} (order-3 acts on
    # Lambda^2_+ as SO(3): fixed axis + rotated pair; net index 3 = residue 0 = carrier A's, so no order-3 datum
    # certifies 3 -- the "forces 3" temptation checked and REFUSED). Soldering(even) and gamma-trace(odd) are
    # two independent declarations, unifiable under one geometric-posture meta-postulate. The program is ONE
    # forced build from complete, but the build needs an UNBUILT input: the causal-cure term -> H41.
    "H41": "THE SOURCE-ACTION CAUSAL-CURE TERM (the terminal build, the one unbuilt input): construct the RS non-minimal / field-space-defining coupling that cures GU's built VZ acausality (the minimal Dirac symbol leaks, C2=155.36, degree-1 -> genuine acausality on curved Y14). Wave 17 proved causality FORCES a cure (killing 2 of 4 carrier corners -> {A,B} both causal) but not the final constrain(B)-vs-gauge(A) bit. The cure term is NOT in the built action; building it WITHOUT p-hacking the carrier is the single terminal object that would close the source action (and with it both gravity's soldering and the count's K-class). Honest ceiling: even built, the count stays odd rank in {1,3}, not pinned to 3. The hardest object on the board -- a genuine higher-spin construction, not a quick swing. [heterodox/wild]",
    "H30": "Elevate the gravity conditional theorem to REFEREE grade: state the soldering as a clean axiom, prove tree-level clearance rigorously from it. Turns an assembled argument into a stated theorem. [heterodox]",
    # STANDING RULE (Joe, 2026-07-11): the GU council proposes RESEARCH ADVANCEMENT of this repo only.
    # Do NOT suggest external-review / submission-prep / methodology-paper / "shipping" items (Joe is aware of
    # those; they are not the advancement of the research). H31 (flagship review-ready) and H32 (methodology
    # paper) DROPPED per this rule. H6 (finish the GU-independent family-puzzle THEOREM) is kept as a research
    # result, not a shipping task.
    "H6": "Finish the GU-INDEPENDENT family-puzzle result ('forces odd count => nonzero 3-Sylow image'): sharpen the predictive proposition + verify the census vs primary sources. A real theorem, credible regardless of GU's fate. [commercial]",
    # H34 RESOLVED (Wave 18, tests/wave18/H34_parameter_count.py, exit 0, 13/13) = the honest ledger. Strict
    # count: PREDICTIONS zero; FITS 4 free params (f0, M2, B_i, mu_DW); the asset is the one-residual
    # COMPRESSION (a structural map, not a prediction); DESI is the sole data-touch (+2.55 sigma on wa, soft
    # only because f0 is free); "ACCOMMODATES" is honest, even conservative. Signal: run the CHEAP FALSIFIERS
    # before more synthesis; H41 is demoted in URGENCY (only pays off if forced). The sharpest new move -> H42.
    # H42 RESOLVED (Wave 19, tests/wave19/H42_f0_prereg.py, exit 0, 5/5) = NO-TEST-YET. f0 is NOT source-first
    # derivable now (DERIVABLE-ONLY-AFTER-H41: the amplitude ratio depends on two unbuilt inputs B_i + mu_DW;
    # the geometry fixes only the SHAPE M^2=8H0^2, not the amplitude; the f0=1/8 back-fit was raised and
    # REFUSED). It stays a FIT. But the sharper finding: the source-first (w0,wa) LOCUS misses DESI at EVERY f0
    # (closest 3.47 sigma; joint tension 4.19 sigma at canonical f0) -- freeing the amplitude does NOT rescue
    # the fit; the shape tracks ACROSS the DESI degeneracy. So the DESI tension is deeper than "soft", latent-
    # falsifier-grade, gated only by the reconstruction-grade OQ2 M^2/ansatz -> the sharpened cheap move is the
    # DE SHAPE test, H43. (The amplitude unblock stays H41.)
    # H43 RESOLVED (Wave 20, tests/wave20): DE-shape FALSIFIED -- the first hard negative. GU's source-first
    #   (w0,wa) locus misses DESI's headline CPL contour robustly: NO admissible M^2 (BC_1=8, A_1=7, S^3=3,
    #   threshold=20.25) and NO point in the free (M^2,f0) plane rotates it in (global closest 3.20 sigma); the
    #   1-component ansatz misses too (3.18 sigma). It is a SHAPE/DIRECTION miss, exhausting f0 + OQ2 + ansatz.
    #   HONEST SCOPE: falsifies the (w0,wa) CPL comparison DESI reports, NOT the raw H(z) (GU's non-CPL w(z)
    #   reaches ~1% RMS on distances, near BAO). One untested escape: a self-consistent theta-backreacted
    #   background (currently LCDM) -> H44.
    # H5 RESOLVED (Wave 21, tests/wave21): geometry-vs-information (Bianconi) = DISTINCT PRIMITIVES (rel-entropy
    #   is the 2nd-order Kubo-Mori supermetric; |II|^2 is order-4). KEY CORRECTION: NEITHER frame pins Lambda's
    #   magnitude (Bianconi's Lambda is a subtracted input constant) -- the asserted determinacy asymmetry is
    #   FALSE. Bianconi cleaner on order/ghosts; GU's 4th-order buys the Weyl sector. The real decider is the
    #   SPIN-2/WEYL sector, and the pivotal internal object is the |H|^2-vs-|II|^2 binary -> H45.
    # SECOND PARALLEL BATCH + persona-council coherence assessment (Waves 24-26, 2026-07-11):
    # H44 RESOLVED (Wave 25): DE = FALSIFIED-FULL-STOP at the (w0,wa) CPL level. The self-consistent
    #   theta-backreacted background (backreaction real, +3.6% on H at z~1) shifts the locus AMPLITUDE not its
    #   DIRECTION -- closest 3.22 sigma vs H43's 3.20. Every DE-rescue route (f0, OQ2, components, IC,
    #   background) spent. Scope unchanged: CPL falsified, raw H(z) not independently killed (GU ~1.3% on
    #   distances) -> the one remaining DE object is the raw-likelihood test, H46.
    # H45 RESOLVED (Wave 24): |H|^2-vs-|II|^2 STILL-OPEN, favored |II|^2 (H21 fixed the object theta not the
    #   action NORM P2). GU has the Weyl sector under BOTH branches (Bianconi has none) -> the spin-2/Bach
    #   discriminator is ROBUST to the binary. Lambda +positive under |II|^2. The source action settles P2 +
    #   mu_DW + H26 positivity + the H21 bundle = QUADRUPLY-motivated keystone.
    # H20 RESOLVED (Wave 26): SPLITS-BUT-RELABELS. The Clifford omega-parity DOES split gravity(even, the 91
    #   bivectors) from matter(odd, c(xi)); one first-order D generates both kinetic operators (Weinstein's
    #   first-order-then-square, made precise) -- BUT it removes 0 of 4 unforced choices (relabels them, does
    #   not force them). The elegant-shortcut hope is ELIMINATED.
    # COUNCIL COHERENCE SYNTHESIS (full persona pass + the batch): the coherence gap IS the missing keystone
    #   (the source action); H20 proved there is NO elegant bypass; everything (P2, mu_DW, soldering, K-class,
    #   loop positivity, count) routes to it. THE LOCAL MINIMUM: the program keeps NARROWING onto a keystone
    #   that cannot be FORCED (signature doesn't force it, causality forces only the cure not the carrier, the
    #   even/odd grading is cosmetic). THE ESCAPE: stop narrowing; DECLARE the honest lean and build the
    #   CONDITIONAL theory to get testable predictions -> H47.
    "H46": "THE DE RAW-LIKELIHOOD TEST (the last DE decider, cheap): H44 falsified GU dark energy FULL-STOP at DESI's (w0,wa) CPL level. The ONLY comparison that falsification does not settle is the raw expansion history -- fit the backreacted GU H(z) to the ACTUAL DESI DR2 BAO table + a CMB Omega_m prior (not the CPL proxy), where GU's non-CPL w(z) mimics DESI distances to ~1.3%. Either GU's dark energy is genuinely dead (raw-likelihood also fails) or GU makes a DISTINCT non-CPL prediction the CPL summary mismeasures (a real, if narrow, result). Cheap, decisive, closes the DE sector either way. [orthodox/philosopher]",
    "H47": "DECLARE-AND-BUILD THE CONDITIONAL THEORY (the escape from the local minimum): the program has narrowed everything onto the source action, which H20 proved cannot be reached by an elegant shortcut and Waves 16/17 proved cannot be FORCED (only leaned, B-carrier). STOP narrowing. DECLARE the honest lean as explicit stated postulates -- (9,5) signature, |II|^2 norm, B-carrier K-class, the geometric-posture soldering -- and BUILD the CONDITIONAL theory, then DERIVE its concrete predictions (the count pinned to 1 or 3; the fermion/Yukawa structure; the raw-H(z) DE; PPN already passes) and TEST them. Converts GU from 'zero predictions, conditional on an unbuilt object' into a concrete conditional theory with N testable predictions -- exactly what the audit (H34) said is missing and what the DE falsification showed the program CAN do. Honest: everything labeled conditional-on-the-declared-postulates (like gravity's conditional theorem); this is disciplined declaration, NOT p-hacking the carrier. [heterodox/commercial/philosopher/wild]",
    "H35": "The SECTION-FUNCTOR reframe: make the 'one residual' a single functorial identity (conjugate SMs, shared theta, alpha_W<->f0 as naturality). Turns 'routes to one object' from slogan into theorem. [wild]",
    "H36": "The OBSERVERSE / issuance connection: the O(M^0) DeWitt-Lambda = the dark-energy scale = the issuance/non-collapse rate. Connect the DeWitt curvature to observerse-non-collapse -- the paper only this program can write. [wild]",
}

# --- five council ballots: strict preference order, best first ---
# "PUSH FURTHER" vote (2026-07-11): each archetype ranks the pooled 14 ideas; their own top-3 lead, the rest
# ranked by their values. Expect the fermion/C2 wall (H29) and the cheap falsification bars (H10/H26) to lead.
# GENERATIVE re-rank after the SECOND batch + the persona-council coherence assessment (Waves 24-26: H45
# favored-|II|^2-but-gated, H20 SPLITS-BUT-RELABELS, H44 DE FALSIFIED-FULL-STOP). The synthesis is decisive:
# the source action is the keystone everything routes to, H20 killed the elegant-shortcut hope, and the LOCAL
# MINIMUM is narrowing onto a keystone that cannot be forced. Two new objects: H46 (the last DE decider, the
# raw-likelihood test) and H47 (the ESCAPE: declare the honest lean + build the CONDITIONAL theory to get
# testable predictions -- the audit's missing predictions, disciplined-declaration not p-hacking). Council
# converges hard on H47 as the escape from the local minimum; H46 the cheap DE closer; H41 the keystone the
# conditional build instantiates. Do NOT count another narrowing pass as progress (the council's explicit warning).
BALLOTS = {
    "orthodox":            ["H46", "H47", "H28", "H30", "H41", "H6", "H35", "H36"],
    "heterodox_rigorous":  ["H47", "H41", "H46", "H30", "H35", "H28", "H36", "H6"],
    "commercial":          ["H47", "H6", "H46", "H41", "H30", "H28", "H35", "H36"],
    "philosopher":         ["H47", "H46", "H41", "H30", "H28", "H35", "H36", "H6"],
    "wild_frontier":       ["H47", "H41", "H46", "H36", "H35", "H30", "H28", "H6"],
}


def prefers(ballot, x, y):
    return ballot.index(x) < ballot.index(y)


def pairwise_margin(items):
    """margin[(x,y)] = (# archetypes preferring x to y) - (# preferring y to x)."""
    margin = {}
    for x, y in combinations(items, 2):
        sx = sum(1 for b in BALLOTS.values() if prefers(b, x, y))
        sy = len(BALLOTS) - sx
        margin[(x, y)] = sx - sy
        margin[(y, x)] = sy - sx
    return margin


def copeland(items, margin):
    """Copeland score: pairwise wins minus losses. Full order; agrees with Condorcet winner if one exists."""
    score = {i: 0 for i in items}
    for x, y in combinations(items, 2):
        m = margin[(x, y)]
        if m > 0:
            score[x] += 1; score[y] -= 1
        elif m < 0:
            score[y] += 1; score[x] -= 1
    return score


def condorcet_winner(items, margin):
    for x in items:
        if all(margin[(x, y)] > 0 for y in items if y != x):
            return x
    return None


def main():
    items = list(ITEMS)
    margin = pairwise_margin(items)
    cw = condorcet_winner(items, margin)
    score = copeland(items, margin)
    # rank by Copeland, break ties by average ballot position (lower = better)
    def avg_pos(i):
        return sum(b.index(i) for b in BALLOTS.values()) / len(BALLOTS)
    order = sorted(items, key=lambda i: (-score[i], avg_pos(i)))

    print("=" * 78)
    print("GU ATTENTION PRIORITY  --  Condorcet over the 5-archetype council")
    print("=" * 78)
    print(f"Condorcet winner: {cw if cw else 'NONE (cycle) -> Copeland order below is authoritative'}\n")
    print("Prioritized list (what to hand Joe when he has GU attention):\n")
    for rank, i in enumerate(order, 1):
        print(f"  {rank}. [{i}]  Copeland {score[i]:+d}  (avg ballot pos {avg_pos(i):.1f})")
        print(f"       {ITEMS[i]}")
    print("\n" + "-" * 78)
    print("Per-archetype #1 picks:")
    for a, b in BALLOTS.items():
        print(f"  {a:20s} -> {b[0]}")
    # a couple of decisive pairwise checks for transparency
    print("\nKey pairwise margins (positive = row beats col across the 5 archetypes):")
    top = order[:4]
    hdr = "        " + "".join(f"{j:>6}" for j in top)
    print(hdr)
    for x in top:
        row = "".join(f"{margin[(x, y)]:+6d}" if x != y else "     ." for y in top)
        print(f"  {x:>5} {row}")
    return order


if __name__ == "__main__":
    main()
