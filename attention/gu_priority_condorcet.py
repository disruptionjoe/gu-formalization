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
    # LOCKED; the SOLE live escape is L7 = the (9,5)/(7,7) signature = H19. The whole count collapses onto H19.
    "H19": "THE SINGLE COUNT HINGE (L7, the only unlocked axis): settle whether GU's Y14 is the native (9,5)/H-class [count PROVABLY located, H37] or (7,7)/R-class [J^2=+1: the odd rank-3 becomes admissible -> count possibly FORCED]. H37 reduced the ENTIRE generation-count question to this one signature choice. The sole decider is a term LINEAR in g (the base-pullback/observerse structure). [heterodox]",
    "H30": "Elevate the gravity conditional theorem to REFEREE grade: state the soldering as a clean axiom, prove tree-level clearance rigorously from it. Turns an assembled argument into a stated theorem. [heterodox]",
    # STANDING RULE (Joe, 2026-07-11): the GU council proposes RESEARCH ADVANCEMENT of this repo only.
    # Do NOT suggest external-review / submission-prep / methodology-paper / "shipping" items (Joe is aware of
    # those; they are not the advancement of the research). H31 (flagship review-ready) and H32 (methodology
    # paper) DROPPED per this rule. H6 (finish the GU-independent family-puzzle THEOREM) is kept as a research
    # result, not a shipping task.
    "H6": "Finish the GU-INDEPENDENT family-puzzle result ('forces odd count => nonzero 3-Sylow image'): sharpen the predictive proposition + verify the census vs primary sources. A real theorem, credible regardless of GU's fate. [commercial]",
    "H34": "Predictive-content AUDIT of the whole flagship: which 'clears' are genuine PREDICTIONS vs free-parameter FITS (like f0)? The honest measure of what GU predicts vs merely houses -- what a skeptic does first. [philosopher]",
    "H5": "Geometry-first vs INFORMATION-first showdown: is GU's geometric primitive right, or is entropic/information-first (Bianconi +Lambda) the correct frame? The one lens that reframes the whole program. [philosopher]",
    "H20": "The UNIFIED even/odd action: does |II|^2-on-Y14 split as gravity(even) + matter(odd) -- Weinstein's 'square and square-root'? If yes, the C2/fermion wall and gravity are ONE structure and the count may drop out. Highest upside. [wild]",
    "H35": "The SECTION-FUNCTOR reframe: make the 'one residual' a single functorial identity (conjugate SMs, shared theta, alpha_W<->f0 as naturality). Turns 'routes to one object' from slogan into theorem. [wild]",
    "H36": "The OBSERVERSE / issuance connection: the O(M^0) DeWitt-Lambda = the dark-energy scale = the issuance/non-collapse rate. Connect the DeWitt curvature to observerse-non-collapse -- the paper only this program can write. [wild]",
}

# --- five council ballots: strict preference order, best first ---
# "PUSH FURTHER" vote (2026-07-11): each archetype ranks the pooled 14 ideas; their own top-3 lead, the rest
# ranked by their values. Expect the fermion/C2 wall (H29) and the cheap falsification bars (H10/H26) to lead.
# Re-rank after Wave 13 (H37 NO-GO). The count is proven located within built (9,5); the whole count question
# collapses onto the single signature hinge H19 (L7, the only unlocked axis) -> H19 rises to the count top.
# Remaining independent frontiers: H10 (PPN), H26 (loop), H34 (predictive audit), H20 (unified action).
BALLOTS = {
    "orthodox":            ["H10", "H26", "H28", "H19", "H34", "H30", "H6", "H20", "H5", "H35", "H36"],
    "heterodox_rigorous":  ["H19", "H30", "H20", "H35", "H28", "H26", "H34", "H10", "H5", "H36", "H6"],
    "commercial":          ["H6", "H10", "H19", "H30", "H34", "H26", "H28", "H20", "H5", "H35", "H36"],
    "philosopher":         ["H19", "H34", "H5", "H10", "H26", "H30", "H20", "H28", "H35", "H36", "H6"],
    "wild_frontier":       ["H20", "H35", "H36", "H19", "H5", "H34", "H30", "H28", "H26", "H10", "H6"],
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
