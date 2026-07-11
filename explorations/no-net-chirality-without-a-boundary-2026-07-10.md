# No net chirality without a boundary: the generation no-go is Nielsen-Ninomiya; the count is a boundary anomaly-inflow quantity

2026-07-10. GU-INDEPENDENT result, hardened from the session's computed pieces. Canon-candidate.
States the one frame-independent thing that gained ground this session as a clean standalone principle,
with each part's rigor labeled honestly. Highest scientific yield of the campaign, lowest risk (does not
depend on GU being right).

## The principle

**No net chirality without a boundary.** Let `S` be a real Clifford/spinor matter sector carrying an
invariant indefinite (Krein) pairing `K` that is purely cross-chirality on the physical multiplet -- i.e.
`K` pairs the two chirality eigenspaces `W_+`, `W_-` as complementary `K`-Lagrangians, net signature
`(+n, -n)`. Then a NONZERO net chiral count is impossible from any closed/internal structure and can only
be a BOUNDARY / anomaly-inflow quantity. Three parts:

**(a) Finite-dimensional (rigorous).** Every `K`-isometric linear operator on `S` conserves the net
chiral index at zero. *Proof:* a physical subspace `P` (maximal `K`-positive, `dim n`) meets each
`K`-Lagrangian `W_\pm` only at 0, so `P` projects isomorphically onto both -- it is the graph of an
isomorphism `W_+ -> W_-`, hence chirality-balanced, `chi(P)=0`; a `K`-isometry maps physical subspaces to
physical subspaces, so `chi(UP)=0`. Elementary finite-dimensional linear algebra -- no Fredholm theory.
[This is the located-not-forced paper's Theorem 2; machine- and symbolically-verified.]

**(b) Lattice (rigorous, standard).** For a translation-invariant lattice Dirac operator on a compact
Brillouin torus, the same conclusion is **Nielsen-Ninomiya**: the net chirality summed over the BZ
vanishes (fermion doubling -- a right-mover is forced to arrive with a left-mover). Computed:
`tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py` (1D naive fermion: zeros at `k=0` (+1) and
`k=pi` (-1), net 0).

**(c) The escape is a boundary (computed, toy).** A nonzero net chiral count arises only from a structure
with a boundary: a domain wall / gapless edge carries net chirality equal to the bulk topological (Chern)
invariant, while the closed system stays net-zero -- **anomaly inflow** (Callan-Harvey; Kaplan
domain-wall fermions; Jackiw-Rebbi). Computed: Chern strip -- single edge net chirality `= bulk Chern =
+/-1`, closed strip net `0`, trivial bulk `0/0`.

## The unifying statement

**Net chirality vanishes on any closed (compact / internally `K`-isometric) structure; a nonzero chiral
count is necessarily a boundary / anomaly-inflow quantity.** Parts (a) and (b) are the same *principle* in
two categories (finite-dimensional Krein vs compact-BZ lattice); part (c) is the shared escape. The
fermion-generation no-go -- "no interior operator forces an odd count; the count is external by
structure" -- is an INSTANCE of this principle, with the generation count identified as a **boundary
anomaly-inflow quantity**.

## Honest scope (what is and isn't a formal theorem)

- (a) is a rigorous finite-dimensional theorem; (b) is standard (Nielsen-Ninomiya 1981); (c) is computed
  at toy grade (a 2-band Chern strip), illustrating the standard bulk-boundary correspondence.
- The statement that (a) and (b) are "the same theorem" is a structural **correspondence** -- the same
  obstruction (net chirality zero on a closed structure) realized in two different mathematical settings
  -- NOT a single formal theorem subsuming both. The durable, GU-independent content is the **principle**
  ("no net chirality without a boundary"), of which both are instances.
- No claim that any construction DOES produce the physical count 3; the `order-3-class -> integer-3`
  bridge stays open. This principle says WHERE the count must live (a boundary), not its value.

## Why it is useful to the world (family puzzle)

Combined with the CRT map (`family-puzzle-CRT-map-which-tools-can-work-2026-07-10.md`), this pins the
generation number to two coordinates: it lives (i) at a **boundary** (anomaly inflow), not in any bulk /
internal construction, and (ii) in the **3-primary** summand, not the 2-primary one. So it tells the
field, GU-independently, exactly where to look: **equivariant boundary spectral invariants (Dai-Freed /
eta-invariants on the compactification boundary) in the odd-torsion summand** -- and equally, which entire
classes of approach (bulk index/anomaly theory; any 2-primary or free-integer invariant) are dead ends
for forcing an odd generation count. That is a genuine, falsifiable orientation for a real open problem,
independent of whether GU is correct.

## Grade

GU-independent. (a) theorem-grade, (b) standard, (c) toy/computed. The unifying principle and the
family-puzzle orientation are the contribution. No claim/canon-ledger movement; the generation count
stays OPEN; SG4 unchanged. Assembles: paper Theorem 2 + `nn_domain_wall_records_as_rows.py` +
the CRT map + the located-not-forced "external by structure" result.
