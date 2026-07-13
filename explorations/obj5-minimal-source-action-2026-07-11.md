---
artifact_type: exploration
status: exploration (5-persona inline team; FIRST construction of the minimal source-action skeleton)
created: 2026-07-11
objective: 5
title: "Objective 5 -- the MINIMAL internally-consistent GU-native source-action SKELETON (first construction, NOT a reproduction of physics). Build the one unbuilt object (the falsifiability keystone) far enough to ANSWER the seven decisive questions: fields+symmetries, what is varied, the EOM, where observer-relativity enters mathematically, the chiral-index result, UV-preservation, and explicit failure tests. VERDICT: a consistent SKELETON exists -- defined DOF (theta, A=spin-lift(grad^gimmel), RS carrier B=ker Gamma), complete IG+Krein transformation laws, a consistent variational EOM (d_A star theta = source, with a UNIQUE causal RS cure g=1 that is so(9,5)-equivariant and therefore CANNOT pick the carrier), one nontrivial derived consequence (causality forces the cure, not the carrier -- first JOINT confirmation of H40), and five explicit failure tests all checked absent. The chiral index is honestly located-{1,3}, NOT forced-nonzero. The UV structure (4-derivative renormalizable Stelle + HORN-K Krein ghost parity + AF/AS) is preserved. The shape-dimension-1 residual (beta/alpha gravity ratio + two scales mu_DW, alpha) stays FREE -- that is the arena/value structure and it is EXPECTED. This is NOT the finished source action."
grade: "COMPUTED (exact, on the repo's verified Cl(9,5)=M(64,H) rep -- tests/W102_obj5_source_action.py, 20/20 PASS, exit 0): the RS carrier B projector (rank 1664 = ker Gamma); the spin-lift so(9,5) homomorphism (residual 0 on a spanning set + Jacobi); the non-compact gauge group beta_S signature (+64,-64); the soldering codim 8165; the built VZ leakage C2=155.3625 and the cure law leakage(g)=(1-g)C2 with unique root g=1; the cure's so(9,5)-equivariance (residual 0 -> closes on both carriers); the order-3 SO(3) eigenstructure on Lambda^2_+ and the residue trap (-42%3=0, -38%3=1); the two-invariant gravity Hessian ranks (10 vs 1); the Krein self-adjointness K M_D = M_D^dag K (residual 0). ARGUED (structural / recorded from prior waves): that the C2 leakage is a genuine Y14 acausality (H40, cited); AF/AS of f_2/EH (H60, recorded RG sign); the arena/value non-circular partition (H62); the B-lean of the final constrain-vs-gauge bit (H39/H40); the m2_eff -> beta/alpha band map (H24/H25/H48). Reconstruction-tier, internal. NO canon promotion; the generation count stays OPEN {1,3}; SG4 unchanged; GU is neither killed nor forced by this construction."
depends_on:
  - tests/W102_obj5_source_action.py
  - explorations/wave8/H23-source-action-construction-2026-07-11.md
  - explorations/wave17/H40-terminal-sourceaction-2026-07-11.md
  - explorations/wave34/source-action-landscape-scan-2026-07-11.md
  - explorations/wave35/source-action-carve-2026-07-11.md
  - explorations/H62-arena-value-partition-firmup-2026-07-11.md
  - canon/carrier-bit-decision-campaign-RESULTS.md
scripts:
  - tests/W102_obj5_source_action.py
---

# Objective 5 -- the minimal GU-native source-action skeleton (first construction)

**What this is.** The whole GU arc has collapsed onto ONE unbuilt object -- the source action, where
selection, observation, chirality, and generation structure enter. It is the falsifiability keystone and
it has never been built. This note makes the **first concrete construction**: a minimal, internally
consistent **skeleton** with defined degrees of freedom, complete transformation laws, a consistent
variational equation of motion, at least one nontrivial derived consequence, and explicit failure tests.

**What this is NOT.** It is not a reproduction of physics, not a finished source action, and it does not
resolve the generation count. The shape-dimension-1 residual (the gravity ratio `beta/alpha` + two free
scales) stays free -- that is the arena/value structure and it is *expected*. Every load-bearing positive
claim is an exact matrix identity on the verified `Cl(9,5)=M(64,H)` representation
(`tests/W102_obj5_source_action.py`, 20/20 PASS, exit 0) or is labelled ARGUED/recorded.

Run as a **5-persona inline team** (one worker, sequential): (1) GEOMETER / GAUGE-THEORY SPECIALIST
builds it; (2) MATH REFEREE checks variational consistency; (3) ADVERSARY ("it is not internally
consistent / it imports the answer"); (4) CROSS-CHECKER against the Wave 34/35 landscape assessment and
the `|II|^2` results; (5) SYNTHESIZER.

---

## 1. GEOMETER / GAUGE-THEORY SPECIALIST -- the construction

### 1.1 Fields (the DOF)

The skeleton carries three field objects, all GU-native (no imports):

| field | object | role | verified |
|---|---|---|---|
| `theta = pi - Ad(eps^-1) B` | an `ad P`-valued **one-form** on `Y14` | the IG connection displacement; the **gravity field** | H23 |
| `A = spin-lift(grad^gimmel)` | the `so(9,5) -> End_H(S)` spin connection, `sigma_ab = 1/4[e_a,e_b]` | the covariant derivative `d_A` | 1b (residual 0) |
| `Psi in ker Gamma` | the **gamma-trace-constrained** Rarita-Schwinger field = **carrier B** | the matter / count sector | 1a (rank 1664) |

- **`A` is a genuine connection [CONSTRUCTED].** The spin-lift `sigma_ab = 1/4[e_a,e_b]` is an *exact*
  Lie-algebra homomorphism `so(9,5) -> End_H(S)` (check 1b: bracket residual `0.0e+00` on a spanning set
  of six generator pairs; Jacobi residual `0.0e+00` in F2). So `d_A` is a bona fide gauge-covariant
  derivative -- not a wished-for object.
- **`Psi` lives in a well-defined field space [CONSTRUCTED].** `Pi_RS` is an honest projector
  (`Pi^2 = Pi`, `Gamma Pi_RS = 0`, rank `1664 = ker Gamma`; check 1a). This is carrier B's field-space
  declaration made concrete.

### 1.2 Symmetries (complete transformation laws)

- **The inhomogeneous gauge group** `ISp = Sp(32,32;H) ltimes Omega^1(ad P)`: a gauge rotation `g` acting
  on the connection PLUS a shift by an `ad P`-valued one-form (Weinstein's "four-momentum becomes gauge
  potentials"). `theta` transforms as a connection *displacement* -- it is the affine (one-form) slot of
  the IG group, which is exactly why its EOM is a current law, not `theta = 0` (Section 2).
- **The gauge group is the NON-COMPACT real form `Sp(32,32;H) = u(32,32;H)` [CONSTRUCTED].** The spinor
  Krein metric `beta_S` = product of the 9 spacelike gammas is Hermitian, `beta_S^2 = I`, traceless, and
  has signature exactly `(+64,-64)` (check 1c, all residuals `0.0e+00`). `Spin(9,5)` is non-compact
  simple, so it cannot map nontrivially into compact `Sp(64)`; the connection preserves the *indefinite*
  `beta_S`. This is the Krein arena.
- **The Cartan / Krein parity `P = K = eta_V (x) beta_S`**, implementing the Cartan involution of
  `so(9,5)` (`+` on rotations, `-` on boosts; check 4b). `[P,S] = 0` is the Bateman-Turok hidden-ghost
  condition (Section 4).
- **The graded / super-IG extension (the `eps` sub-slot).** The A/B door: gauging the fermionic
  `eps` sub-slot of the inhomogeneous group is carrier A; leaving it as constrained matter is carrier B.
  GU-as-stated does **not** state this sub-slot, and its generic SUGRA form is amputated by GU's "no
  spacetime SUSY" commitment -- so this extension is present as a *door*, B-leaning, not a forced choice.

### 1.3 The action and what is VARIED

```
S  =  |theta|^2  +  <Psi, O(g_cure) Psi>_K            [schematic]
   =  |II_s|^2   +  (RS matter on ker Gamma)
```

- `|theta|^2 = |II_s|^2` is the **full second-fundamental-form norm** `|II|^2` (H21/H45), NOT `|H|^2`.
  `|H|^2` is pure Bach and dies to Ostrogradsky/rotation-curve; `|II|^2` gives the Stelle
  `box(box+m^2)` structure on the TT sector (Section 4).
- **What is varied:** `theta` (the gravity field) and `Psi` **restricted to the gamma-trace-constrained
  field space `ker Gamma`** -- i.e. the field-space declaration is *carrier B* (index `-38`). The
  restriction is the physical content: varying over the full space with a gauge invariance would be
  carrier A instead.

---

## 2. MATH REFEREE -- variational consistency (the EOM)

### 2.1 The gravity EOM: `d_A star theta = source`, not `theta = 0`

Because `theta` is the IG one-form (the gravity field), the first variation of `S = |theta|^2` gives a
**second-order current-conservation law**

```
d_A star theta  =  source        (H23)
```

**not** the algebraic `theta = 0`. The vacuum is *not* the soldered configuration -- driving `theta -> 0`
would re-hit the acausal-trap family. This is the correct variational structure for a connection-valued
gravity field, and it is what makes `theta` *be* the second fundamental form on-shell rather than trivially
vanishing.

### 2.2 The RS EOM: a UNIQUE causal cure [CONSTRUCTED]

The minimal Dirac symbol `M_D` leaks off the constraint surface: `C2 = ||Gamma M_D Pi_RS|| = 155.3625`
(check 2a) -- the Velo-Zwanziger acausal trigger is present *as built*. The cured operator

```
O(g)  =  (1-g) M_D  +  g (Pi M_D Pi),      leakage(g)  =  (1-g) * C2
```

(the projected term is killed by `Gamma Pi = 0`) has the **unique causal root `g = 1`** -- the full
`ker Gamma` projection (check 2b: `leak(0)=155.36`, `leak(1/2)=77.68=C2/2`, `leak(1)=6.3e-14=0`). This is
the Porrati-Rahman non-minimal completion, GU-incarnated: a non-minimal RS coupling that restores
constraint invertibility.

**Referee's variational verdict: CONSISTENT.** The EOM is well-posed, the cure is unique, and it is a
genuine (not hand-imposed-arbitrarily) consequence of demanding zero leakage -- one linear equation, one
root.

### 2.3 The nontrivial derived consequence

The cure `Pi` is built from `Gamma`, and **`Gamma` is `so(9,5)`-equivariant** (`Gamma J_i = sigma_i Gamma`,
residual `0.0e+00`, check 2c). Therefore `ker Gamma` (B) *and* the full space (A) are BOTH cure-compatible
submodules -- the causal cure **closes on both carriers**. Consequence, derived not assumed:

> **Causality forces the CURE (to the unique point `g=1`) but is provably BLIND to the A/B carrier bit.**
> The carrier is a *separate* axis, fixed (if at all) by count-selection, not by causality.

This is the **first joint confirmation** of H40's "forces the cure, not the carrier": earlier waves
imposed the constraints one at a time; here causality is imposed on the actual rep *with* the equivariance
structure, and the decoupling is exact. That is a real, nontrivial output of the construction.

---

## 3. ADVERSARY -- "it is not internally consistent / it imports the answer"

Four attacks, each answered on the rep:

- **"The chiral index is fabricated to be 3."** *No.* The order-3 subgroup of the self-dual `SU(2)_+`
  acts on `Lambda^2_+` (3-dim) as an SO(3) rotation: 1 fixed axis + a rotated pair (check 3a,
  `R^3=I`, eigenvalues `{1, omega, omega^2}`). The odd `Z/3`-equivariant ranks are `{1,3}`, but the
  **residue trap** (check 3b) shows a net index of exactly 3 has residue `0 mod 3` = carrier A's residue
  (`-42%3=0`, index-*preserving*), while carrier B is `-38%3=1` (index-*changing*). So no order-3 datum can
  read "3 generations" off B's content. The skeleton **does not** and **must not** certify 3 (failure test
  F4). The only exact `3` anywhere is `dim Lambda^2_+` (a ceiling, not a count). **The answer is NOT
  imported.**
- **"The Krein positivity is a fudge."** *No.* `M_D` is *exactly* Krein-self-adjoint,
  `K M_D = M_D^dag K` (residual `0.0e+00`, checks 4b/F3), and this holds for every covector `xi` -- it is a
  structural feature of any `so(9,5)`-covariant operator, not a tuned coincidence. (It is also *sign-blind*
  -- it clears the ghost, it does not select the count. That honesty is preserved.)
- **"The soldering is where you smuggle the geometry in."** *Conceded as a postulate, not smuggled.*
  `A = spin-lift(grad^gimmel)` is a codim-8165 pinning (check 1d: `8256 - 91 = 8165`) that GU's dynamics
  does not force -- it is a B-leaning postulate, explicitly flagged (Section 5, still-open). Wave 34
  collapsed it and the connection-map into ONE knob, so it is one honest declaration, not a hidden lever.
- **"The whole region might be empty (a hidden inconsistency)."** *No.* Failure test F5: the joint carve
  (causality + count-selection + positivity + Krein) is NONEMPTY -- all satisfiable on carrier B with the
  `ker Gamma` cure. EMPTY is actively falsified. GU is not killed here.

**Adversary's residual mark (carried):** the construction is a *skeleton*. The cure-basis size is a
modeling choice standing in for the unbuilt full higher-spin (Porrati-Rahman) coupling; the `Y14`
acausality of the leakage is cited (H40), not re-derived end-to-end; the guardian that would UV-complete
the interacting massive RS past the Rahman cutoff is unestablished. These are named in Section 6.

---

## 4. CROSS-CHECKER -- against Wave 34/35 landscape + the `|II|^2` results

- **Wave 35 carve verdict = FAMILY, shape-dimension 1.** This construction reproduces it exactly: cure
  FIXED (`g=1`), carrier FIXED to B (count-selection `-38%3=1`), and the gravity ratio `beta/alpha` a
  bounded 1-parameter residual + 2 free scales (check 5a). Nothing here contradicts the carve; the
  skeleton *instantiates* the carve's allowed region.
- **The `|II|^2` result (H45/H48).** The two O(4)-invariant 4-derivative gravity densities reproduce:
  `|II|^2` rank-10 Hessian, `|H|^2` rank-1 (check 4a). `S = |II|^2` -> Stelle `box(box+m^2)` on TT, with
  `m2_eff in [5/6,5/4]` (nonempty, `m^2 != 0`). The residual `beta/alpha` is precisely the live
  H45-full-`|II|^2` vs H48-conformal-`|II_0|^2` tension -- the shape-dim-1 freedom, unresolved by design.
- **Wave 34 Rahman cutoff.** The cross-check confirms the honest limit: guardian-free, the interacting
  massive RS is at best a finite-`Lambda` EFT (Rahman + Sagnotti-Taronna, GU's finite content). The
  skeleton does not claim UV-completeness of the *interacting* RS; it claims the *causal-cure* structure
  and the UV structure of the *gravity + free-RS* sector. That distinction is preserved.
- **The `C2 = 155.3625` anchor** reproduces to `1e-3` (check 2a), matching every prior wave. No drift.

**Cross-checker verdict: CONSISTENT with the entire prior landscape.** The construction is the landscape's
allowed region made into an explicit object; it introduces no new number and fits no target.

---

## 5. SYNTHESIZER -- the seven decisive answers

1. **Fields & symmetries [CONSTRUCTED].** `theta = pi - Ad(eps^-1)B` (IG one-form / gravity field);
   `A = spin-lift(grad^gimmel)`, an exact `so(9,5)` homomorphism into the non-compact `Sp(32,32;H)`;
   `Psi in ker Gamma` (carrier B, rank 1664). Symmetry: inhomogeneous gauge group
   `ISp = Sp(32,32;H) ltimes Omega^1`, Cartan/Krein parity `[P,S]=0`, and a graded/super-IG `eps`-slot
   door (B-leaning, not forced).

2. **What is varied [CONSTRUCTED].** The gamma-trace-constrained field space -> carrier B (index `-38`).
   Varying the full space with a fermionic gauge invariance would be carrier A instead; the declaration
   is the physics.

3. **The EOM [CONSTRUCTED].** `d_A star theta = source` (H23; not `theta = 0`); the RS cure
   `O(g) = (1-g)M_D + g Pi M_D Pi` with `leakage(g) = (1-g)C2` and the **unique causal root `g = 1`**.

4. **Where observer-relativity enters mathematically [ARGUED, H62].** As **value-selection =
   symmetry-breaking**. The ARENA (observer-*invariant*, forced) = the family shape, the causal cure,
   carrier B, and the count menu `{1,3}`. The VALUE (observer-*selected*, requires breaking a vacuum /
   frame / direction) = the `beta/alpha` gravity ratio, the scales `mu_DW, alpha`, and the 3-over-1 pick.
   The observer forces the arena and selects the value (check 5b; non-circular partition, characterization
   (c)). This is the mathematical seat of observer-relativity: the shape-dim-1 residual IS the
   observer-selected value slot.

5. **Chiral index [CONSTRUCTED, honest]: located-{1,3}, NOT forced-nonzero.** The residue trap forbids
   certifying a net 3; the only exact 3 is `dim Lambda^2_+` (a ceiling). The count stays OPEN; SG4 remains
   the single decider. **No nonzero chiral index is forced by this skeleton** -- reporting one would be the
   Wave 14/15/16 trap, and it is refused.

6. **UV preservation [CONSTRUCTED + ARGUED]: YES.** 4-derivative renormalizable Stelle
   (`|II|^2 -> box(box+m^2)`, `m^2 != 0`); HORN-K = the Krein / Bateman-Turok hidden-ghost parity
   `[P,S]=0` clears the Stelle ghost (exact, residual 0); AF in `f_2` + AS in the EH sector preserved,
   and the RS cure does not spoil `beta_f2` (H60, recorded). The UV structure already found survives the
   construction.

7. **Failure tests [CONSTRUCTED].** Five explicit conditions that would each kill the skeleton, all
   checked ABSENT: **F1** acausality (cured leakage `!= 0`); **F2** not-a-connection (Jacobi fails);
   **F3** ghost-not-cleared (`[P,S] != 0`); **F4** fabricated-count (certifying net-3 against the residue
   trap = importing the target); **F5** empty-region (the joint carve inconsistent -> GU killed).

### Built vs still-open (honest grading)

- **BUILT (exact, on the rep):** the field content and the connection; the non-compact gauge group and the
  Krein/Cartan structure; the RS carrier B field space; the variational EOM structure and the unique causal
  cure; the cure's carrier-blindness (the one nontrivial derived consequence); the residue trap and the
  located-{1,3} chiral index; the two-invariant gravity Hessian; the HORN-K ghost clearing; the five
  failure tests.
- **STILL OPEN (conjectural, expected):** the `beta/alpha` value + the two scales (the arena/value residual
  -- expected to stay free); the GU-internal **guardian** (super-IG / local SUSY) that would UV-complete the
  *interacting* massive RS past the Rahman cutoff; whether the soldering + the super-IG `eps`-slot is
  **forced** (still a B-leaning postulate, not a derivation); the AF/AS `f_2` sign is recorded from H60, not
  re-derived here.

---

## Honest limits (do not overclaim)

1. **This is a SKELETON, not the finished source action.** It has enough structure to answer the seven
   questions and to be internally consistent; it is not a full higher-spin construction. The cure-basis
   size stands in for the unbuilt Porrati-Rahman non-minimal coupling.
2. **No carrier is forced; no count is forced.** The A/B bit is B-leaning (H39/H40), not a theorem; the
   chiral index stays located-{1,3}. Nothing here manufactures "3 generations."
3. **The `Y14`-acausality of the leakage is cited (H40), not re-derived** on the full bundle. The leakage
   magnitude and its degree-1 homogeneity are exact; that it constitutes a genuine VZ acausality is the
   standard physics, cited.
4. **The arena/value partition is a MODEL of the outputs (H62)**, non-circular via the symmetry
   characterization but possibly generic (Curie), not proven GU-unique.
5. **No canon / RESEARCH-STATUS / claim-status / verdict movement.** The generation count stays OPEN; SG4
   unchanged; GU stays framework-not-theory. Exploration/analysis grade. No git commit.

## Not claimed

Not a finished source action; not a forcing of the carrier or the count; not a UV-completion of the
interacting massive RS; not a derivation of `beta/alpha` or any scale; not a canon promotion. A graded,
reproducible **first construction of the minimal consistent skeleton** of the one unbuilt object, with the
seven decisive questions answered and the shape-dim-1 residual honestly left free.

---

*Filed 2026-07-11 (Objective 5). Reproducible: `python -u tests/W102_obj5_source_action.py` (exit 0,
20/20 PASS). Exploration-grade; not promoted to canon. Adversarially graded: no forcing manufactured (the
causality forcing is of the cure, not the carrier), no target imported (the only 3 is `dim Lambda^2_+`; the
residue trap is made explicit and F4 forbids certifying 3), EMPTY actively falsified (F5), and the skeleton
is honestly marked a first swing with the arena/value residual left free.*
