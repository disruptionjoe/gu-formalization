---
artifact_type: exploration
status: exploration (toy computation + six-axis disposition; analysis grade)
created: 2026-07-10
title: "The Nielsen-Ninomiya lane executed: the generation-count terminus (Theorem 2 + external-by-structure) IS the lattice chiral no-go and its domain-wall escape; the records-as-rows frame supplies a candidate boundary (the autoregressive frontier). Toy-grade shadow exhibited; the six-axis smoothing-functor burden advanced, not discharged."
grade: "COMPUTED / toy (tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py, exit 0, 6/6 checks, deterministic). Standard condensed-matter physics (1D fermion doubling; 2-band Chern insulator strip; bulk-boundary correspondence) with discriminating controls. The physics is textbook and verified; the records-as-rows identification is an analysis-grade analogy, explicitly separated below. No canon, claim, or verdict movement; the generation count stays OPEN and rides SG4 as ever."
depends_on:
  - explorations/six-axis-examination-of-the-records-as-rows-reframe-2026-07-10.md
  - explorations/records-as-rows-spacetime-from-attention-2026-07-10.md
  - explorations/gu-as-neural-architecture-2026-07-10.md
  - canon/gu-forces-field-space-declaration-RESULTS.md
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
---

# The Nielsen-Ninomiya lane

The six-axis examination of the records-as-rows reframe named the **Nielsen-Ninomiya L3/L6 lane** as
"the cleanest target ... the disciplined next step, and the one that would move the reframe from frame to
candidate." Its disciplined burden: does the causal-masked attention tensor admit a **smoothing functor
to the Nielsen-Ninomiya lattice-fermion image** (a genuine evasion / shadow), or does it merely change
the unit (scope-exit)? This note executes that lane at toy grade.

## The load-bearing observation: the terminus and N-N are the same theorem

The located-not-forced paper's **Theorem 2** -- "every linear Krein-isometric operator conserves the net
chiral index at zero" (the cross-chirality `(+96,-96)` Krein form makes every physical subspace
chirality-balanced) -- is a **Nielsen-Ninomiya-shaped statement**: net chirality vanishes on a closed /
compact structure. And the paper's escape -- the count is **external by structure**, supplied by a
boundary / net-self-dual chiral background via anomaly inflow -- is structurally the **domain-wall
fermion** escape from N-N (Kaplan 1992; Jackiw-Rebbi 1976): a single chiral mode lives on the boundary of
an extra dimension while the bulk stays vectorlike. So "located, not forced" is the GU-sector instance of
the oldest lattice-chirality fact: *you cannot put a net chiral fermion on a closed lattice; it must come
from a boundary.* That identification is the real conceptual payoff, and it is independent of the
records-as-rows frame.

## The computable object (one toy, three statements)

A 2-band Chern-insulator lattice, `h(k) = (sin kx, sin ky, M + cos kx + cos ky)`, `H = h.sigma`, makes
all three statements a single computed object (`tests/nielsen-ninomiya/nn_domain_wall_records_as_rows.py`,
exit 0, deterministic, discriminating controls):

| statement | computation | result |
|---|---|---|
| **N-N doubling** (compact BZ) | 1D `E(k)=sin k`: zeros + chirality (dE/dk sign) at each | zeros at `k=0` (**+1**) and `k=pi` (**-1**), **net 0**; continuum `E(k)=k` control: 1 zero, net +1 |
| **bulk topology** | Berg-Luscher Chern number | `M=-1 -> C=+1` (topological); `M=-3 -> C=0` (trivial control) |
| **domain-wall escape** | Chern strip (periodic x, open y = walls vs vacuum), per-edge net chirality by overlap-tracked E=0 crossings | topological: top edge **+1**, bottom edge **-1**, **closed strip 0**; trivial: **0 / 0** |

The three are one fact. **(1) N-N**: the closed strip / compact BZ forces net chirality 0 (doubling) --
the lattice shadow of Theorem 2. **(2) Escape**: a *single* edge carries net chirality = the bulk Chern
number = +/-1 -- chirality as a boundary mode. **(3) Anomaly inflow**: the two edges are opposite, so
"chiral boundary + net-0 bulk" is the same statement -- the paper's "external by structure." The trivial
control (Chern 0, no edge mode) confirms the edge chirality is *sourced by the bulk topology*, not an
artifact of merely having a boundary.

## The records-as-rows reading (analysis grade -- explicitly separated)

Read the open `y`-direction as **time** (records accumulating, the row index) and the edge / domain wall
as the **autoregressive frontier** (the causal mask's edge, "the present"). Then the chiral edge mode is
chirality **issued at the frontier**: the temporal boundary carries the net chirality the closed bulk
cannot. This hands the records-as-rows frame a **concrete mechanism** for the "external" chirality the
generation-count terminus said had to come from outside the closed structure -- it comes from the
*temporal boundary*, by bulk-boundary correspondence. It also aligns with the Temporal-Issuance reading
(a genuinely new chiral mode is *issued*, not rearranged) and with the gu-as-neural-architecture note
(the count is a rank set over the sequence, not present in the frozen columns).

This layer is an **analogy**, not a theorem. The domain wall here is a boundary between two topological
phases of a specific lattice model; calling the autoregressive frontier "a domain wall in time" presumes
the records-as-rows premise (time as a genuine extra dimension with topological character), which is not
independently established.

## Six-axis disposition (precise)

Three honest layers:

1. **Solid (computed, standard).** N-N + domain-wall escape + anomaly inflow is one genuine object, and
   it is a real **shadow of the generation-count terminus** (Theorem 2 and its external-by-structure
   escape). This is not vacuous relabeling: the object is *in* N-N's category (a lattice Dirac operator
   with a boundary) and reproduces both N-N's image (net-0 bulk) and its known escape (chiral edge). The
   target structure the records-as-rows lane needs demonstrably EXISTS and is non-trivial.

2. **Advanced, not discharged (the functor burden).** The six-axis burden is to exhibit the smoothing
   functor *from an actual causal-masked attention / records object* to this lattice image. What is built
   here is the **target** (the lattice N-N object and its escape) and the argument that it has exactly the
   shape the frame needs. The **domain of the functor** -- a concrete attention/records object that maps
   onto the lattice Dirac operator -- is still asserted, not constructed. So the lane moves from
   "generative frame / scope-exit" toward "candidate," but the evasion is **not** completed.

3. **Scope-exit remainder.** Identifying the frontier-as-domain-wall with **GU's actual chiral field
   content** stays scope-exit: the mechanism is real and generic, but that GU's specific generation
   sector *is* this edge mode is unbuilt -- it rides SG4, exactly as the carrier bit does. The N-N lane
   does not route around SG4 any more than any other lane did; what it adds is a *named external
   mechanism* (a temporal domain wall) for the "external chirality" the terminus already required.

## Net

- **Real result:** the generation-count terminus is a Nielsen-Ninomiya no-go, and its external-by-structure
  escape is the domain-wall mechanism -- a genuine unification of "located, not forced" with the oldest
  lattice-chirality fact, computed as one object with controls.
- **Frame payoff:** records-as-rows supplies a concrete candidate boundary (the autoregressive frontier)
  for the external chirality, upgrading the L3/L6 lane from scope-exit toward candidate.
- **Still open:** the smoothing functor's domain (an actual records/attention object -> the lattice) and,
  as ever, whether GU's specific sector is this edge mode (SG4).
- **No movement:** canon, claims, verdicts, and the generation count are unchanged. Toy / analysis grade.

## Not claimed

Not a derivation of three (or any) generations, not a metric, not a proof that the records-as-rows
analogy is an identity, and not a completed six-axis evasion. A mechanism demonstration with
discriminating controls, plus the (defensible, frame-independent) observation that Theorem 2 is
N-N-shaped and its escape is the domain wall.
