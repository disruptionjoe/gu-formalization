---
title: "H3 Outcome D' to GU Bridge: Transfer from Finite SBP Parity Cocycles to Flat Z/2Z Gauge-Local-System"
date: 2026-06-23
problem_label: "h3-outcome-d-prime-gu-bridge"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
---

# H3 Outcome D' to GU Bridge: Transfer from Finite SBP Parity Cocycles to Flat Z/2Z Gauge-Local-System

## 1. Problem Statement

**What is being computed.** The cech_sheaf_fixture in temporal-issuance returned Outcome D':
under odd-SBP polarity-flip parity plus the no-anticipation constraint (NAC), the transition
values are derived as c(I_plus) = +1 and c(I_minus) = -1, giving holonomy -1. The nontrivial
cocycle is forced from axiom-configuration conditions, not stipulated externally. The CHSH
finite-cycle transfer also gives loop product -1.

Outcome D' is a finite-schema derivation path. The question is whether this result can be
transferred to the GU/T63 flat Z/2Z gauge-local-system statement: the signed-readout /
finality-presheaf isomorphism of T63's Holonomy Theorem.

**Three bridge conditions** (from the prompt):

- **C1 (type-bridge):** The SBP parity cocycle maps to a flat Z/2Z gauge connection on the
  GU observer bundle.
- **C2 (Cech-sheaf fixture):** The temporal-issuance Cech cohomology class equals the GU
  finality-presheaf obstruction class.
- **C3 (GU transport):** The holonomy -1 around spacelike-separated patches matches the GU
  causal structure.

**Prior resolutions:**

- C1 was RESOLVED in `taf-h3-c1-type-bridge-2026-06-23.md` (reconstruction) — the type-
  bridge between Z/2Z gauge data and TaF finality presheaf sections is a canonical
  isomorphism of Cech complexes; H^1(P, Z/2Z_gauge) ~= H^1(P, F_finality) naturally in P.

- C3 was RESOLVED in `taf-h3-c3-spacelike-overlap-2026-06-23.md` (reconstruction) — the
  Cech cover lives on observable space Y_spin, not spacetime; spacelike loops in Z/2Z have
  trivial holonomy; finality data on spacelike-separated patches is compatible by no-signaling.

**Remaining open condition:** C2 — whether Outcome D' from the temporal-issuance fixture is
the same class as the GU finality-presheaf obstruction class. This synthesis file attempts
that transfer.

**Output:** H3 CONDITIONALLY_RESOLVED if all three bridge conditions hold after synthesis;
OPEN with explicit per-condition failure analysis otherwise.

---

## 2. Established Context

**Prior files (all at reconstruction grade or better):**

- `taf-h3-contact-2026-06-23.md` (CONDITIONALLY_RESOLVED): W-H3 established; BC-1 through
  BC-3 structural parallels; six falsification conditions.

- `n3-cech-fixture-specification-2026-06-23.md` (CONDITIONALLY_RESOLVED): Full fixture
  specification with two-patch S^1 cover, Ax_+/Ax_- schemas, NAC, Outcome A/B/C/D/D'
  taxonomy, eleven test conditions TC-1 through TC-11.

- `taf-h3-c1-type-bridge-2026-06-23.md` (RESOLVED): Canonical isomorphism
  H^1(P, Z/2Z_gauge) ~= H^1(P, F_finality) established at reconstruction grade. Poset
  structure alignment confirmed; failure condition (edges vs. vertices) does not apply.

- `taf-h3-c3-spacelike-overlap-2026-06-23.md` (RESOLVED): Spacelike-separation does not
  create incompatible finality data; Z/2Z holonomy of spacelike loops is trivially +1.

- `DERIVATION-PROGRESS.md` entry h3-cech-sheaf-fixture-execution: The fixture returned
  Outcome D' — c(I_plus) = +1, c(I_minus) = -1, holonomy -1, both values derived_from_C
  under odd-SBP polarity-flip parity plus NAC. Control cases recover A, B, and C. The CHSH
  finite-cycle transfer gives loop product -1.

- `signed-readout-oq2d-gu-contact-2026-06-23.md` (CONDITIONALLY_RESOLVED): G_R^{GU} = 24-
  node bipartite graph (16 spin-1/2 + 8 RS), no edges, all weights +1 (monotone, R_- = 0);
  T^{GU} = affine gauge-field space (connected, contractible).

- `n3-h3-cech-holonomy-2026-06-23.md` (OPEN with C1, C2, C3 as gates): H3 anatomy; T63
  high-confidence entries are H3-independent; medium-confidence entries require H3.

---

## 3. Bridge Condition C1 Re-Assessment: Type-Bridge After Outcome D'

### 3.1 What Outcome D' Adds to C1

The C1 file established the abstract isomorphism: Z/2Z gauge data on the record poset P
and TaF finality presheaf sections over P are the same type of Cech H^1 data. The C1
argument was structural — it showed the Cech complexes are isomorphic without specifying
which cohomology CLASS the finality data lands in.

Outcome D' adds the class level: the specific SBP parity-flip configuration forces the
Mobius class (holonomy -1), not the trivial class. Outcome D' is therefore a class-level
statement within the isomorphism already established by C1.

**C1 status under Outcome D': RESOLVED (inherited).** The type-bridge is the isomorphism
of complexes established in C1. Outcome D' provides the input data (odd-SBP parity, NAC)
that selects the nontrivial class within that isomorphism. No new obstacle arises.

### 3.2 The Smooth-vs-Combinatorial Lifting Question (FC4 from C1)

C1 identified one open question: whether the combinatorial Z/2Z data lifts to smooth flat
Z/2Z gauge connections on the GU observer bundle (Y_spin over X^4).

**Outcome D' sharpens this.** The fixture produces a combinatorial class: c(I_plus) = +1,
c(I_minus) = -1 as specific values in {+1,-1}. To transfer this to GU, we need:

(L1) A map from SBP schema configurations to GU observer bundle sections sigma_alpha(X_alpha).
(L2) A map from odd-SBP parity data to the flat Z/2Z gauge connection on the GU bundle.
(L3) Continuity: the smooth structure on Y_spin is compatible with the combinatorial class.

**L1 assessment.** GU observer sections sigma: X^4 -> Y^14 are smooth maps selecting a
Lorentzian metric on X^4. SBP (schema-level binary parity) encodes whether the source
schema at a record has odd or even finality-class parity. The correspondence:

```
SBP parity class = {even (+1), odd (-1)}
GU gauge holonomy = {trivial (+1), Mobius (-1)} in pi_0(Flat(P, Z/2Z))
```

The two-element sets are canonically identified. Under the C1 type-bridge, a SBP schema
configuration determining the parity of finality assignments maps to a section of the
finality presheaf F over the record poset P, which maps to a Z/2Z Cech class via the C1
isomorphism, which maps to a flat Z/2Z connection on the GU observer bundle via the
identification of the nerve of {U_r} with the CHSH S^1 cover.

**L2 assessment.** Odd-SBP parity under NAC forces c(I_minus) = -1 (the fixture result).
In GU language: the flat Z/2Z connection on the CHSH cover has transition function -1 on
the overlap near theta = pi. The holonomy of the full S^1 loop is c(I_plus) * c(I_minus) =
(+1) * (-1) = -1. This is the Mobius flat bundle, the generator of H^1(S^1, Z/2Z) = Z/2Z.

The transition value c(I_minus) = -1 from TI admissibility maps exactly to the generator
of H^1(Y_spin, Z/2Z) via the CHSH Cech cover structure established in T63.

**L3 assessment.** The flat Z/2Z bundle on S^1 is discrete data (a holonomy homomorphism
pi_1(S^1) = Z -> Z/2Z); it has no smooth structure beyond the underlying topology. The
Cech class from Outcome D' is combinatorial; it lifts to the smooth setting automatically
because flat Z/2Z bundles on S^1 are classified by pi_1(S^1) -> Z/2Z, and any combinatorial
Cech class determines such a homomorphism (no continuity obstruction for discrete-valued
bundles).

**C1 lifting conclusion: RESOLVED.** The smooth-vs-combinatorial gap (FC4 from C1) does
not apply to flat Z/2Z connections: discrete-valued flat bundles have no smooth lifting
obstruction. The Mobius class from Outcome D' lifts immediately to the smooth GU bundle.

---

## 4. Bridge Condition C2: Cech-Sheaf Fixture Outcome D' as the GU Obstruction Class

### 4.1 The C2 Question Precisely Stated

C2 asks: is the Cech cohomology class produced by the temporal-issuance fixture equal to
the GU finality-presheaf obstruction class?

Concretely:

- **Fixture class**: The Cech 1-cocycle from Outcome D' assigns c_L = c(I_plus) = +1 and
  c_R = c(I_minus) = -1 on the two overlap components of the S^1 cover. This represents
  the nontrivial class in H^1(S^1, Z/2Z) = Z/2Z.

- **GU obstruction class**: The T63 Holonomy Theorem asserts the non-trivial class in
  H^1(Y_spin, Z/2Z) corresponds to quantum contextuality (CHSH violation). The generator
  is the Mobius bundle on S^1 (viewing the CHSH observable cycle as S^1).

- **The question**: Are these two classes equal in H^1(S^1, Z/2Z) = Z/2Z?

### 4.2 The Equality Argument

H^1(S^1, Z/2Z) = Z/2Z has exactly two elements: the trivial class and the Mobius class.
Outcome D' produces a nontrivial class (c_L * c_R = -1). The Mobius class is the unique
nontrivial class. Therefore:

```
[Outcome D' fixture class] = [Mobius class] = [GU T63 nontrivial class]
```

in H^1(S^1, Z/2Z) = Z/2Z.

This is a tautological equality: there is only one nontrivial class in Z/2Z. The fixture
class is nontrivial; the GU class is nontrivial; they are equal.

**C2 status: RESOLVED** at reconstruction grade. The Cech class from Outcome D' equals
the GU finality-presheaf obstruction class because both are the unique nontrivial class in
H^1(S^1, Z/2Z) = Z/2Z. The group structure forces equality once both classes are shown to
be nontrivial.

### 4.3 The Non-Tautological Content of C2

A skeptic could object: the "equality" is trivial (it follows from both being the only
nontrivial Z/2Z class) and therefore does not constitute a genuine bridge. The non-trivial
content is:

1. **Derivation vs. stipulation**: Outcome D' shows the nontrivial class is DERIVED from
   admissibility axioms (odd-SBP parity + NAC), not stipulated as an external input. The
   GU T63 class is the contextuality obstruction class (non-derivable from local hidden
   variable assignments). The C2 bridge says: TI admissibility independently derives the
   class that GU T63 identifies as the contextuality obstruction. This is a substantive
   structural claim, not a tautology.

2. **Forcing mechanism matches**: The forcing mechanism in TI is NAC + odd-SBP parity.
   The forcing mechanism in GU T63 is the CHSH inequality (quantum violation forces
   holonomy = -1 for any local-realistic assignment to fail). Both mechanisms produce
   the same class by the same route: the nontrivial class arises because no consistent
   global section exists.

3. **The bridge is the identification of these two forcing mechanisms.** TI admissibility
   forces the nontrivial class via no-anticipation; CHSH forces the nontrivial class via
   no-local-hidden-variable. The C2 bridge is the claim that these are the same forcing
   in different language: no-anticipation in schema space = no-local-hidden-variable in
   observable space.

**Assessment of non-tautological content.** The identification of NAC + odd-SBP parity
with no-local-hidden-variable is a substantive claim. It is supported by:

- The formal parallel: both conditions express that no global consistent assignment exists
  on the two-patch cover (NAC: no schema extension consistent with both patches; CHSH:
  no hidden variable assignment consistent with all four settings).
- The Cech machinery: in both cases, the obstruction to a global section is the same
  H^1 class.
- The T63 architecture: T63 is precisely the theorem asserting that TaF finality obstructions
  correspond to CHSH contextuality obstructions. Outcome D' provides the fixture evidence
  for this correspondence at the schema level.

**Residual gap.** The identification NAC + odd-SBP = no-LHV is structural-parallel at
reconstruction grade. A verified proof would require showing that the TI schema-consistency
condition (C_TaF admissibility) is equivalent to a Bell-locality condition as a theorem,
not a structural analogy. This is the C2 gap that remains at exploration grade.

### 4.4 C2 Status Summary

| sub-condition | status | grade |
|---|---|---|
| Fixture class is nontrivial | RESOLVED | reconstruction (from Outcome D') |
| GU T63 class is nontrivial | RESOLVED | reconstruction (from T63 architecture) |
| Both classes equal in H^1(S^1,Z/2Z) | RESOLVED | verified (unique nontrivial element) |
| NAC + odd-SBP = no-LHV as theorem | OPEN | exploration grade |
| C_TaF equivalent to Bell-locality | OPEN | exploration grade |

C2 is CONDITIONALLY_RESOLVED: the class equality holds; the forcing-mechanism identification
is reconstruction-grade structural parallel, not verified theorem.

---

## 5. Bridge Condition C3 Re-Assessment: GU Causal Structure After Outcome D'

### 5.1 What Outcome D' Adds to C3

C3 was RESOLVED in the dedicated C3 file via two routes:
- Route A: Cech cover on observable space Y_spin; spacelike separation is a precondition
  for CHSH, not an obstacle.
- Route B: Z/2Z spacelike loops have holonomy (+1)^k = +1; nontrivial holonomy (-1)
  requires mixed traversal.

Outcome D' does not alter these arguments. What it adds is:

The CHSH finite-cycle transfer in the fixture also gives loop product -1. This confirms
that the fixture's S^1 two-patch setup is compatible with the four-context CHSH cover:
the two-patch holonomy c_L * c_R = -1 transfers to the full CHSH four-cycle as the same
nontrivial class.

**C3 under Outcome D': RESOLVED (inherited from prior file, strengthened by fixture CHSH
transfer).** The holonomy -1 around the GU causal structure (four-context CHSH cycle) is
consistent with the holonomy -1 in the two-patch S^1 fixture.

### 5.2 Explicit GU Causal Structure Check

From `signed-readout-oq2d-gu-contact-2026-06-23.md`: G_R^{GU} = 24-node bipartite graph
(16 spin-1/2 + 8 RS nodes), no causal edges between nodes (all weight +1, R_- = 0). The
GU causal structure in the signed-readout framework is monotone (all finality weights +1;
the GU ground state has no finality-sign conflicts).

The C3 question asks: does holonomy -1 match the GU causal structure? For G_R^{GU} being
a trivial monotone graph, the answer requires care:

- G_R^{GU} is the RECORD GRAPH (nodes = finalized generation modes). It is monotone because
  the GU Dirac operator ground state has no negative-weight finality assignments.
- The CHSH cover is the CONTEXTUALITY cover (CHSH experimental settings, four contexts).
- These are two separate structures. G_R^{GU} measures the GU monotone finality count;
  the CHSH cover measures quantum contextuality of observer correlations.

The holonomy -1 in the CHSH cover is not the holonomy of G_R^{GU} (which is trivially +1
for a monotone record graph). It is the holonomy of the OBSERVABLE SPACE cover under the
CHSH experiment setup.

**Reconciliation.** The T63 Holonomy Theorem is not a claim about G_R^{GU}; it is a claim
about the observable space Y_spin with its CHSH cover structure. The GU observer sections
sigma_alpha: X_alpha -> Y^14 define the observer domain; the CHSH cover lives on Y_spin
(the spin observerse), which is a different space. The C3 condition asks whether the GU
causal structure (the causal structure of Y^14 = Met(X^4)) is compatible with the CHSH
holonomy -1 — specifically, whether the null-cone causal structure of Y^14 is compatible
with a Z/2Z flat bundle of holonomy -1 on Y_spin.

**GU causal structure compatibility.** From VZ evasion results: the characteristic cone
of D_GU is the null cone of g_Y; no spacelike propagation. From C3 Route B: spacelike
loops in Z/2Z flat connections have trivial holonomy. Therefore the nontrivial holonomy
(-1) in the CHSH class requires a loop that includes null or timelike segments — which is
exactly the CHSH four-cycle (Alice's and Bob's measurements are connected via null/timelike
routes through the common past). The GU null-cone causal structure is COMPATIBLE with the
CHSH holonomy -1.

**C3 status: RESOLVED** (reconstruction grade, inherited and confirmed).

---

## 6. Synthesis: Transfer from Outcome D' to Full H3

### 6.1 What Outcome D' Achieves

Outcome D' provides:

1. A finite-schema instance in which TI admissibility (C_TaF + NAC) forces a nontrivial
   Z/2Z cocycle (c_L * c_R = -1).
2. Both transition values derived_from_C, not stipulated.
3. The CHSH finite-cycle transfer confirming the nontrivial class persists to the four-
   context cover.

This converts the C2 fixture question from "is there any admissibility-forcing instance?"
to "the answer is yes, for odd-SBP parity + NAC configurations."

### 6.2 Transfer Chain: TI -> Cech -> GU

```
TI level:     odd-SBP parity + NAC
              => C_TaF admissibility forces c(I_plus)=+1, c(I_minus)=-1

Cech level:   c_L * c_R = -1
              => nontrivial class in H^1(S^1, Z/2Z) = Mobius bundle

C1 bridge:    H^1(P, Z/2Z_gauge) ~= H^1(P, F_finality) [C1, RESOLVED]
              => Mobius class = finality-presheaf gluing obstruction

C2 transfer:  Cech class from fixture = GU T63 nontrivial class
              [CONDITIONALLY_RESOLVED: class equality exact; forcing mechanism
               identification is reconstruction-grade structural parallel]

C3 transport: Holonomy -1 matches GU null-cone causal structure
              [RESOLVED: spacelike loops trivial; four-cycle requires null/timelike]

GU level:     The GU signed-readout / finality-presheaf isomorphism holds
              for the specific SBP-odd + NAC observer configuration
```

### 6.3 H3 Upgrade Assessment

**H3 in T63:** The TaF finality presheaf sections can be identified with flat Z/2Z-gauge
connections on GU observer sections, such that the Cech coboundary condition maps to the
holonomy computation on Y_spin.

**Status after bridge synthesis:**

| Component | Status | Grade |
|---|---|---|
| C1: Type-bridge (combinatorial -> smooth) | RESOLVED | reconstruction |
| C3: GU causal structure transport | RESOLVED | reconstruction |
| C2: Class equality (Outcome D' class = GU obstruction class) | RESOLVED | verified (Z/2Z uniqueness) |
| C2: Forcing mechanism identification (NAC+SBP = no-LHV) | CONDITIONALLY_RESOLVED | reconstruction |
| Full H3 (universal identity, all observer configurations) | OPEN | — |
| Conditional H3 (for SBP-odd + NAC configurations) | CONDITIONALLY_RESOLVED | reconstruction |

**Conclusion:** H3 is CONDITIONALLY_RESOLVED for the specific observer configuration
class (odd-SBP polarity-flip parity + NAC). The three bridge conditions hold at the
following grades:

- **C1: RESOLVED** — type-bridge established; smooth lifting obstacle absent for flat Z/2Z.
- **C2: CONDITIONALLY_RESOLVED** — class equality is exact (Z/2Z uniqueness); forcing
  mechanism identification is a structural parallel at reconstruction grade.
- **C3: RESOLVED** — GU null-cone causal structure compatible with CHSH holonomy -1.

The transfer from Outcome D' finite-schema cocycles to the GU/T63 flat Z/2Z gauge-local-
system statement succeeds at reconstruction grade for the conditional case. Full H3
(universal identity theorem for all GU observer sections, not just SBP-odd + NAC) remains
OPEN: it requires showing that the GU signed-readout framework always instantiates the
SBP-odd + NAC configuration or a structural equivalent.

---

## 7. The Conditionality Precisely Characterized

**What Outcome D' is NOT.**

Outcome D' is not a proof that all TI admissibility configurations produce the nontrivial
class. The fixture establishes:

```
[odd-SBP parity + NAC] => [c_L * c_R = -1]
```

Not:
```
[any C_TaF admissibility] => [c_L * c_R = -1]
```

The control cases show:
- Outcome A (no transition data): c_L, c_R both free.
- Outcome B (stipulated transitions): c_L, c_R from external input.
- Outcome C (forced trivial): c_L * c_R = +1 (trivial Cech class).

So TI admissibility does NOT always force the nontrivial class.

**What Outcome D' DOES establish.**

1. The nontrivial class is ACHIEVABLE from TI admissibility (without external input)
   for specific schema configurations. This rules out Outcome C as the universal result.

2. The GU observer configuration corresponding to SBP-odd + NAC is the specific physical
   configuration for which H3 holds. The natural question: what physical situation does
   SBP-odd + NAC correspond to in GU?

**Physical interpretation.** In the GU framework:

- NAC (no anticipation) = the GU observer section sigma: X^4 -> Y^14 does not contain
  information about spacelike-separated regions before causally accessing them. This is
  the GU manifestation of the no-signaling condition.

- Odd-SBP parity = the finality structure of the observer's records has an odd number of
  polarity flips around the relevant cycle. In terms of the CHSH experiment: the joint
  measurement correlations exhibit an odd number of contextuality-forcing transitions
  around the four-cycle. This is the signature of genuine quantum contextuality (not
  classical simulation).

**Combined:** NAC + odd-SBP parity is the GU characterization of a quantum-contextual
observer in the CHSH setting. H3 holds for quantum-contextual GU observers.

---

## 8. Remaining Gaps

### 8.1 Forcing Mechanism Gap (Gap 1)

**Status:** C2 forcing mechanism identification is OPEN at verified grade.

**Precise gap:** The claim that NAC + odd-SBP parity = CHSH no-LHV as a formal theorem is
not established. A verified proof would require:

(G1a) A formal map from TI schema consistency conditions to Bell-locality conditions.
(G1b) A theorem that the forcing mechanism in TI (C_TaF refusing consistent global
       sections under NAC + odd-SBP) is equivalent to the CHSH forcing mechanism (no
       local-hidden-variable assignment consistent with the four-cycle correlations).

Currently this is a structural parallel (both express non-existence of global sections)
but the equivalence theorem has not been proved.

### 8.2 Universality Gap (Gap 2)

**Status:** OPEN.

**Precise gap:** H3 as a GU identity theorem requires that the GU signed-readout framework
ALWAYS instantiates a configuration equivalent to SBP-odd + NAC, or that the signed-
readout record graph G_R^{GU} itself forces the nontrivial H^1 class.

But G_R^{GU} is MONOTONE (all weights +1, R_- = 0). A monotone record graph has:
- All local finality sections are globally consistent (no gluing obstruction).
- H^1(G_R^{GU}, Z/2Z) class = trivial (holonomy +1).

This appears to be a CONFLICT. The GU finality structure G_R^{GU} produces the trivial
Cech class, while T63 H3 requires the nontrivial class.

**Resolution of the apparent conflict.** The record graph G_R^{GU} and the CHSH Cech
cover are DIFFERENT STRUCTURES:

- G_R^{GU} = record graph for the GU generation count (24 finalized H-lines, monotone).
  Its trivial H^1 class means: the 24-generation result is globally consistent; there is
  no generation-counting contextuality.

- CHSH Cech cover = cover of the OBSERVABLE SPACE Y_spin for physical measurement settings.
  Its nontrivial H^1 class means: physical correlations on Y_spin cannot be explained by
  local hidden variables.

These are separate covers of separate spaces. G_R^{GU} is a cover of the GENERATION COUNT
poset; the CHSH cover is a cover of the OBSERVABLE MEASUREMENT SPACE. H3 concerns the
observable space cover, not the generation count poset.

**Consequence.** The apparent conflict dissolves: H3 (nontrivial class on Y_spin for CHSH
settings) is compatible with G_R^{GU} monotone (trivial class on generation poset). These
are not the same H^1 group.

**But the universality gap remains:** For H3 to be a GU identity theorem (not just a
conditional result), we need: for EVERY quantum-contextual observer with GU sections
sigma_alpha, the T63 CHSH cover of Y_spin produces the nontrivial H^1 class. This requires
a structural argument that the GU observer-section geometry forces odd-SBP + NAC for any
physical contextual observation. Not yet established.

### 8.3 Smooth-Structure Gap (Gap 3)

**Status:** OPEN but non-blocking.

**Precise gap:** The C1 type-bridge and the C2 class transfer are at the level of the
combinatorial record poset. The GU bundle geometry of Y_spin (a 14D pseudo-Riemannian
manifold) has much richer smooth structure. The flat Z/2Z bundle on S^1 is smooth (discrete
structure), but the identification of the CHSH S^1 with a geodesic loop in Y_spin has not
been made explicit.

**Assessment:** Non-blocking because flat Z/2Z bundles are determined by their topology
(pi_1 -> Z/2Z), and the smooth and topological structures coincide for flat discrete bundles.

---

## 9. Verdict and Grade

**Verdict: CONDITIONALLY_RESOLVED**

**Grade: reconstruction**

**Rationale:**

All three bridge conditions (C1, C2, C3) hold for the conditional case (SBP-odd + NAC
observer configurations):

- C1 RESOLVED: type-bridge is canonical isomorphism of Cech complexes; smooth lifting
  is automatic for flat Z/2Z bundles.
- C2 CONDITIONALLY_RESOLVED: class equality is exact by Z/2Z uniqueness; forcing
  mechanism identification is reconstruction-grade structural parallel.
- C3 RESOLVED: GU null-cone causal structure compatible with CHSH holonomy -1.

The transfer from Outcome D' finite-schema cocycles to the GU/T63 flat Z/2Z gauge-local-
system statement SUCCEEDS at reconstruction grade for the conditional case.

Full H3 as a universal GU identity theorem remains OPEN. The remaining gates are:

1. **Gap 1** (forcing mechanism): NAC + odd-SBP = CHSH no-LHV as verified theorem.
2. **Gap 2** (universality): GU observer-section geometry forces the SBP-odd + NAC
   configuration for all quantum-contextual observers on Y_spin.

If both gaps close, H3 upgrades to RESOLVED at verified grade.

---

## 10. Explicit Failure Conditions

**F1: The class equality (C2) is empty content.**

If the argument "both classes are nontrivial elements of Z/2Z, hence equal" is rejected
as insufficient (because the two nontrivial classes are in DIFFERENT H^1 groups for
different spaces), then C2 requires an explicit map between the groups.

Mitigation: The spaces are identified via the T63 architecture (the CHSH S^1 cover IS the
TI fixture S^1 cover, under the identification of CHSH observable settings with TI schema
extension contexts). If this identification is rejected, C2 requires a new argument.

**F2: Odd-SBP + NAC is not the GU physical configuration.**

If the GU observer sections are not quantum-contextual (i.e., the GU correlated measurement
outcomes satisfy CHSH inequalities), then the SBP-odd + NAC condition is never instantiated
in GU physics, and H3 holds vacuously (or not at all, depending on interpretation).

Assessment: this would require GU correlations to be locally reproducible, contradicting
the quantum field-theoretic character of the theory.

**F3: G_R^{GU} monotone conflicts with T63 nontrivial class.**

If the apparent conflict (G_R^{GU} gives trivial H^1, T63 requires nontrivial H^1) is not
resolved by distinguishing the two cover spaces, then either H3 or G_R^{GU} monotonicity
must be wrong.

Assessment: the conflict is resolved (§7.2 above) by noting the two covers are on separate
spaces. But if the GU signed-readout framework is revised to make G_R^{GU} the T63 cover
(collapsing the two structures), the conflict becomes genuine.

**F4: Smooth-structure gap blocks the full bundle identification.**

If the CHSH S^1 is not realizable as a smooth geodesic loop in Y_spin compatible with the
flat Z/2Z structure, the C1 smooth-lifting argument fails.

Assessment: non-blocking given flat Z/2Z bundles are topological, but worth checking.

**F5: Forcing mechanism identification fails as a theorem.**

If NAC + odd-SBP is provably NOT equivalent to CHSH no-LHV (e.g., if a TI schema
satisfying NAC + odd-SBP allows a local hidden variable model), then C2's forcing mechanism
identification is wrong and the bridge is structural analogy only.

Assessment: Gap 1 is the precise statement of F5 as an open gate.

---

## 11. Open Questions

**OQ-H3-1:** Prove or disprove NAC + odd-SBP <=> CHSH no-LHV as a formal theorem. This
is the Gap 1 upgrade gate. Approach: map TI schema consistency conditions to Bell
inequalities via a formal translation of "C_TaF admissibility" into "local realistic
model existence" and apply CHSH.

**OQ-H3-2:** Characterize the class of GU observer sections that instantiate SBP-odd +
NAC. Is this the full class of quantum-contextual observers, or a strict subset? This is
the Gap 2 universality gate.

**OQ-H3-3:** Is the CHSH S^1 a well-defined object in Y_spin? Explicit construction:
embed the CHSH four-context cycle as a null-geodesic loop in Y^14 and pull back the flat
Z/2Z bundle. This closes Gap 3.

**OQ-H3-4:** Does the Outcome D' CHSH finite-cycle transfer (loop product -1) directly
correspond to a CHSH inequality violation in GU? Establish the dictionary between the TI
finite-cycle product and the GU CHSH correlation E(a,b) + E(a,b') + E(a',b) - E(a',b').
