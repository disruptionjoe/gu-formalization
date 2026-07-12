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
    "H10": "PPN / weak-field-with-MATTER test (light bending, perihelion): does GU's fourth-order/Stelle gravity pass the real solar-system bars (known trouble for 4th-order theories)? Cheap, decisive, needs NO source action. [orthodox]",
    "H26": "Loop-level ghost unitarity: does the Krein [P,S]=0 (holds at tree, H23) survive renormalization? The generic-Stelle killer -- decides whether 'conditional theorem' means anything quantum. [orthodox]",
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
    "H43": "THE DE-SHAPE FALSIFIER (the sharpest cheap kill-or-credit, promoted by Wave 19): the source-first (w0,wa) LOCUS misses DESI at EVERY amplitude f0 (closest 3.47 sigma; joint 4.19 sigma at f0=0.125) -- so freeing f0 CANNOT rescue GU's dark energy. Is that locus ROBUST or an artifact of the OQ2 M^2 / two-component reconstruction ansatz? Resolve OQ2 A_3-vs-BC_1 (which shifts M^2=8H0^2 and the whole locus). If the shape HOLDS under a firmed-up M^2, GU's dark energy is FALSIFIED independent of amplitude -- the strongest clean negative on the board and exactly the kill-or-credit the audit calls for. Cheap, decisive, needs no source-action build. [orthodox/philosopher]",
    "H5": "GEOMETRY-first vs INFORMATION-first showdown (Bianconi 'Gravity from entropy', arXiv:2408.14391, PRD 111 066001): SAME skeleton as GU -- two metrics (spacetime g + a matter-INDUCED metric) related by an action, yielding an emergent small positive Lambda. The fork is WHICH functional relates them: GU's |II|^2/Willmore (geometric) vs Bianconi's quantum relative entropy S(g||G) (information). Concrete discriminators: (1) GU is 4th-order + ghost (Krein-cleared, Bateman-Turok) while Bianconi is 2nd-order + ghost-free by construction; (2) Wave 19 sharpened the key asymmetry -- GU leaves the emergent-Lambda AMPLITUDE free (f0 needs the unbuilt source action), where Bianconi PINS Lambda from the G-field; (3) Bianconi's Dirac-Kahler 2-form matter vs GU's 3=dim Lambda^2_+ self-dual 2-forms. Map the two functionals, name what would decide it. Reframes the whole program. Research advancement (not shipping). [philosopher/wild]",
    "H20": "The UNIFIED even/odd action: does |II|^2-on-Y14 split as gravity(even) + matter(odd) -- Weinstein's 'square and square-root'? If yes, the C2/fermion wall and gravity are ONE structure and the count may drop out. Highest upside. [wild]",
    "H35": "The SECTION-FUNCTOR reframe: make the 'one residual' a single functorial identity (conjugate SMs, shared theta, alpha_W<->f0 as naturality). Turns 'routes to one object' from slogan into theorem. [wild]",
    "H36": "The OBSERVERSE / issuance connection: the O(M^0) DeWitt-Lambda = the dark-energy scale = the issuance/non-collapse rate. Connect the DeWitt curvature to observerse-non-collapse -- the paper only this program can write. [wild]",
}

# --- five council ballots: strict preference order, best first ---
# "PUSH FURTHER" vote (2026-07-11): each archetype ranks the pooled 14 ideas; their own top-3 lead, the rest
# ranked by their values. Expect the fermion/C2 wall (H29) and the cheap falsification bars (H10/H26) to lead.
# GENERATIVE re-rank after Wave 19 (H42 RESOLVED = NO-TEST-YET). f0 is not source-first derivable now, but the
# DE LOCUS misses DESI at EVERY amplitude (freeing f0 does not rescue it; joint 4.19 sigma) -- promoting the DE
# SHAPE test (H43) as the sharpest cheap kill-or-credit: if the (w0,wa) locus holds under a firmed-up OQ2 M^2,
# GU's dark energy is falsified independent of amplitude. Joe surfaced Bianconi (arXiv:2408.14391) -> H5 is now
# CONCRETE and coupled (the f0 gate is exactly the geometry-vs-information amplitude-determinacy asymmetry).
# Council: H43 leads (a real clean falsification is the highest-value outcome the audit calls for); H5 rises
# (concrete rival, Joe-surfaced, reframes the core); H41 the amplitude unblock; H10/H26 the other cheap bars.
BALLOTS = {
    "orthodox":            ["H43", "H10", "H26", "H28", "H41", "H30", "H6", "H5", "H20", "H35", "H36"],
    "heterodox_rigorous":  ["H43", "H41", "H30", "H5", "H26", "H20", "H35", "H28", "H10", "H36", "H6"],
    "commercial":          ["H6", "H43", "H10", "H26", "H5", "H41", "H30", "H28", "H20", "H35", "H36"],
    "philosopher":         ["H43", "H5", "H10", "H26", "H41", "H30", "H20", "H28", "H35", "H36", "H6"],
    "wild_frontier":       ["H5", "H41", "H43", "H20", "H35", "H36", "H30", "H28", "H26", "H10", "H6"],
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
