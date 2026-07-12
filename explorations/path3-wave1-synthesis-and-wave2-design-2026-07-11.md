# Path 3 wave 1 -- orchestrator synthesis + wave 2 design

Five blind branches attacked "can the generation count be FORCED from first principles?" from five rival
constructions of what the count IS (A Atiyah-Singer index, B anomaly inflow, C K-theory/cobordism, D 3-primary
homotopy torsion, E adversarial no-go), mutually blind. Tests W55-W59 all exit 0. This is the synthesis, the
cross-test, and the single sharp wave-2 target the wave produced.

## 1. The high-level picture: a class-wide NO-GO, seen four ways, machine-checked

The wave landed the pre-registered "E proves a class-wide no-go" outcome -- and the four constructive branches
independently converged on the SAME no-go from their own sides, which is what makes it strong rather than one
team's opinion. **"Located, not forced" is now a theorem.** The number of fermion generations is not forced by
first-principles topological selectors; it is a mod-3 torsion datum with an irreducible {1,3} residual.

The single mechanism, seen four ways:
- **A (index):** the integer Dirac index CONSTRAINS the count (`= 0 mod 3` on closed spin 4-manifolds, via
  `p_1 = 3 sigma`) but cannot FORCE it -- `Hom(Z/3, Z) = 0`. Torsion-valued indices (the reduced eta / Adams
  e-invariant `e_KO = 1/3`, order 3; mod-3k Freed-Melrose) genuinely REACH the `Z/3` arena, but reaching locates
  the class, it does not produce the integer 3.
- **B (anomaly inflow):** inflow LOCATES and quantizes but does not force -- the boundary invariant is Z-valued
  (a free bulk winding/level/Chern choice), and the one forced first-principles condition, anomaly-freedom, lands
  in the 2-primary arena, coprime to 3. Class-wide no-go for the standard (integer/parity) inflow invariant.
- **C (cobordism):** the relevant group is `Omega^Spin_5(BG)`, framing channel `= pi_3^s = Z/24 = Z/8 (+) Z/3`;
  the 3-primary summand is `Z/3`. The group structure forces the MODULUS 3 (the arena is `Z/3`, and
  `3 = |Z/3| = dim Lambda^2_+(R^4)`) but NOT the value 3; the anomaly is a homomorphism (Freed-Hopkins), so it
  can only constrain mod an order, and the SM per-generation Dai-Freed anomaly vanishes (generation-blind).
  Class-wide no-go via `Aut(Z/3)=Z/2` (no canonical generator), `Hom(Z/3,Z)=0`, and linearity.
- **D (homotopy torsion, the REACHABLE construction):** `3 = dim Lambda^2_+(R^4)`, and the `Z/3 subset pi_3^s`
  order-3 element acts on `Lambda^2_+ = R^3` as an element of `SO(3) = SU(2)_+`, splitting `R^3 = ` (fixed axis,
  dim 1) `(+)` (rotated pair, dim 2). Realized rank is in `{1,3}` (oddness selects the odd-dim invariant
  subspaces). So the torsion BOUNDS (ceiling 3) but does not force -- the rank-1 fixed axis stays admissible.

**E (adversarial) closes it into a theorem.** A residual-freedom theorem (machine-checked): the rank-1 solution
(the `SO(3)` fixed axis) is admissible whenever rank-3 is, and no first-principles condition (equivariance,
reality, self-adjointness, oddness, anomaly-freedom) separates `{1,3}`. Class-wide across all four constructions,
with a uniform reason: **the count is a torsion (mod-3) datum with no canonical integer value, realized as an
invariant subspace whose odd choices `{1,3}` nothing separates.** E survives its own steelman: the condition that
WOULD force 3 (faithfulness/maximality -- use all of `Lambda^2_+`, exclude the sterile axis) is not
first-principles, because a sterile trivial self-dual direction is consistent and anomaly-free (rank 1 cancels
all anomalies) and the mod-3 Dai-Freed arena is empty (`Omega^Spin_5(BG_SM) (x) Z_(3) = 0`).

## 2. What IS forced (the strongest provable positive statement)

The no-go is not "nothing is forced." Assembling the constructive branches, the forced content is sharp and
non-trivial:
- **The count is 3-PRIMARY** -- it lives in `Z/3`, i.e. it is defined mod 3 (C, the arena is forced).
- **The ceiling is exactly 3** `= dim Lambda^2_+(R^4)` (D, forced linear algebra).
- **Oddness excludes 2** -- the realized rank is odd, so the count is in `{1, 3}` (D).
- Therefore: **the number of generations is forced to be 1 or 3, and 3-primary.** Two, four, five... are excluded
  by the self-dual 2-form structure of the 4-base. What is NOT forced is 3-over-1: the sterile one-generation
  solution is admissible.

That is a genuine, GU-independent sharpening of the generations problem: not "why 3" answered, but "why not 2,
not 4, and why 3-primary" answered, with the residual freedom pinned to a single, named, physical question.

## 3. The cross-test and the SINGLE escape hatch (the wave's convergent output)

Cross-testing E against A-D: E's residual-freedom obstruction covers all four constructions (index/anomaly can't
reach the arena; cobordism/homotopy reach it but hit the class-to-integer gap + the `{1,3}` subrep residual). But
D and E independently name the SAME, single escape hatch, and A/B/C's "torsion-refined" escapes all point at it
too:

**Promote the discrete order-3 element to the full CONTINUOUS `SO(3) = SU(2)_+`.** Under the connected group,
`R^3 = Lambda^2_+` is irreducible, so the only invariant subspaces are `{0, R^3}` -- any matter content then
forces rank `= 3 = dim Lambda^2_+ = dim adjoint SU(2)_+`, cleanly and first-principles. Equivalently (E's
framing): exhibit a genuine anomaly that FORBIDS the sterile rank-1 axis. These are the same condition from two
sides.

This is the crux, and it is a well-posed, decidable question: **`SU(2)_+` is the self-dual half of the 4D frame
rotation group `SO(4) = SU(2)_+ x SU(2)_-` -- the chiral half. So "is `SU(2)_+` a forced continuous gauge
symmetry acting on the generation space?" is asking whether the chiral/self-dual half of the local frame rotation
gauges the generation multiplet.** If yes, generations `= 3` is forced and `3 = dim` of the self-dual chiral
algebra. If only the discrete `Z/3` is forced, the count stays `{1,3}` and the no-go stands.

## 4. Where this sits against the blockbuster bar

- It is a real, GU-independent, machine-checked THEOREM on a famous problem: the generation number is not forced
  by first-principles topological selectors; it is a mod-3 torsion datum forced into `{1,3}`, and forcing 3 is
  provably equivalent to promoting the self-dual `Z/3` to a continuous `SU(2)_+` gauge symmetry.
- It is NOT "we derived 3" (that would need the escape hatch to close).
- Honest weight: comparable to the path-2 map, arguably a bit stronger -- the no-go is machine-checked and
  class-wide, it is directly on the generations problem, and it converts a suspected fact into a theorem while
  pinpointing the unique route to a positive. A clean "here is exactly why the standard tools cannot force 3, and
  here is the single thing that would" result.

## 5. Wave 2 design

The wave produced ONE sharp target; a second blind wave is NOT warranted (wave 1 already converged the no-go).

**Target 1 -- THE decisive swing: is `SU(2)_+` a forced continuous gauge symmetry?** Ask whether the self-dual
2-form bundle `Lambda^2_+` over the 4-base necessarily carries a *dynamical, continuous* `SU(2)_+` gauge symmetry
(whose irreducibility forces rank 3), or whether only its discrete order-3 subgroup is forced (leaving `{1,3}`).
Concretely: (a) is the self-dual `SU(2)_+` (the chiral half of `SO(4)`/`Spin(4)`) a gauge symmetry of the matter
sector, or a global/discrete symmetry? (b) equivalently, is there a first-principles anomaly or consistency
condition that forbids the sterile rank-1 axis (E's escape route)? (c) what minimal, honestly-first-principles
assumption closes it -- and is that assumption itself forced or a choice? This is GU-independent in statement
(4-manifold + self-dual gauge structure) though it touches GU's self-dual sector; run it as a SWING (one worker),
cross-shared with E's residual-freedom theorem and D's `SO(3)`-promotion criterion. HONEST PRE-REGISTRATION: the
likely outcome is that continuous `SU(2)_+` is a *stronger* assumption than the framework forces (so the count
stays `{1,3}` and the no-go is the final word), but if it IS forced, generations `= 3` is derived. Either way is
a clean terminus.

**Target 2 (follow-on) -- consolidate.** Whichever way Target 1 goes, the path-3 result (the `{1,3}` no-go +
the `SU(2)_+` reduction) is a standalone GU-independent paper, parallel to the path-2 consolidation.

## 6. Honest register
Wave 1 is exact linear algebra + standard topology across the board (A/C/D/E machine-checked theorem-grade on
their cores; B computed; the GU-facing legs graded reconstruction-tier). The no-go is solid; the `SU(2)_+`
escape is a precisely-stated open question, not a claim either way. No canon / RESEARCH-STATUS / claim-status /
verdict / posture changed; the generation count stays OPEN (now with a theorem-grade located-not-forced floor).
