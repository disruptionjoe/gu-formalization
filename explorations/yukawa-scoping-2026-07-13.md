---
artifact_type: exploration
status: exploration
created: 2026-07-13
hypothesis: H28
title: "H28 Yukawa scoping -- does the built structure grade fermion masses? VERDICT: SILENT on hierarchy (with one named texture hook and one new small no-go). The equivariant Yukawa channel table is COMPLETE and rigid (one channel per Lambda^k / allowed chirality block; scalar Dirac-Yukawa channel exists, cross-chirality, dim 1); the derived Z/3 acts NON-trivially (9->3 texture cut, 1+2 block); but NO built object grades magnitudes -- the three surviving couplings are free, and the order-3 rho=(0,2,1) charges are provably FN-STERILE (a mod-3 flavon grades only entries invariance already kills). All mass hierarchy is source-action-gated."
grade: "COMPUTED (exact rep theory on the verified Cl(9,5)=M(64,H) rep, MOVE-4 method, checksum-controlled, 20/20 asserts exit 0) / ARGUED (the reduced-level texture rides the H38 identification of the generation triplet with Lambda^2_+; the FN reading of rho as charges is a candidate assignment, not a built coupling). Scoping-tier, one wave, no arc. No canon movement, no count movement, no verdict movement. SILENT is the honest primary outcome."
construction: "program-native throughout: spinors are the Cl(9,5) 128-dim Dirac module (canon shiab-existence-cl95); the generation triplet is the DERIVED Z/3 on 3 = dim Lambda^2_+(R^4) (H38); carrier B and rho=(0,2,1) per canon gamma-traceless-38 / order3-equivariant-rho. Standard-field fork noted where it matters (charges-add transpose bilinear vs charges-subtract Krein pairing -- BOTH computed)."
depends_on:
  - canon/shiab-existence-cl95.md
  - canon/order3-equivariant-rho-RESULTS.md
  - canon/gamma-traceless-38-adjudication-RESULTS.md
  - canon/carrier-dirac-mass-capstone-RESULTS.md
  - explorations/wave15/H38-z3-chiral-selector-2026-07-11.md
  - explorations/wave16/H39-sourceaction-kclass-2026-07-11.md
  - explorations/H64-mass-selection-first-swing-2026-07-11.md
  - tests/chase/MOVE-4/move4_spinor_square_forms.py
scripts:
  - tests/yukawa-scoping/yukawa_trilinear_channels.py
---

# H28 -- Yukawa / fermion-mass scoping: what the built structure supplies, and what it provably does not

Test: `tests/yukawa-scoping/yukawa_trilinear_channels.py` (deterministic, fixed seed, exact;
20/20 asserts, exit 0). One bounded wave; a fast honest SILENT was pre-declared as a fully valid
outcome, and SILENT (on hierarchy) is what the computation returns.

Run as a 5-persona inline team (one worker, sequential): (1) representation theorist;
(2) flavor physicist; (3) model-building skeptic; (4) K-theory/torsion mathematician;
(5) honesty auditor.

## Scoping question and prior state

Fermions live in the 128-dim Dirac spinors of Cl(9,5) = M(64,H). Known before this wave:
the same-chirality Majorana SCALAR mass channel is provably absent from the equivariant family
(SHIAB-05: dim Hom(S+ (x) S+, Lambda^0) = 0); the carrier Dirac mass is allowed, vectorlike,
value action-gated (carrier-mass capstone); the mass VALUES are free and the family-breaking is
a doublet spurion (H64); the generation carrier binary is A (-42, rho (0,0,0)) vs B (-38, rho
(0,2,1), the unique index-changing carrier), count located at {1,3} (H39). What was NOT known
at computed grade: the complete trilinear Yukawa channel inventory, whether the derived Z/3
acts non-trivially on any such channel, and whether the order-3 spectral labels can grade
magnitudes (a Froggatt-Nielsen-type engine).

---

## Persona 1 -- Representation theorist: the complete channel table [COMPUTED]

Method: exact computation on the verified 128-dim rep, same machinery and checksums as
SHIAB-05 / MOVE-4 (Jordan-Wigner gammas; trace-orthonormal Clifford words; block nullspace
solves; per-degree parity; closure/equivariance residuals ~1e-14 for k <= 3).

**The table is complete and rigid.** A Yukawa-type trilinear S^eps (x) S^delta (x) H needs an
equivariant map S (x) S -> H*. Since the invariant bilinear C : S ~ S* is equivariant and
invertible per block (computed: normalized smallest singular values O(1)), the channel space is
Hom(S (x) S*, H) = the multiplicity of H in End(S) -- and End(S) decomposes EXACTLY as
(+)_k Lambda^k(V_14) with multiplicity 1 each (Lambda^7: 1+1), hard checksum
sum_k C(14,k) = 16384 = 128^2 with zero residuals. Consequences, each machine-checked:

| Higgs carrier | dim Hom (channel count) | chirality blocks |
|---|---|---|
| Lambda^0 (scalar) | **1** | **OPPOSITE only (S+ x S-)** -- the Dirac-Yukawa channel |
| Lambda^1 (vector, 14) | 1 | SAME chirality (not a Lorentz scalar) |
| Lambda^2 (91, gauge-curvature sector) | 1 | OPPOSITE |
| Lambda^k, k odd / even | 1 each (k=7: 2) | SAME / OPPOSITE |
| Lambda^0 on S+ x S+ (Majorana scalar) | **0** (SHIAB-05, reproduced as control) | -- |
| **any non-form carrier** (e.g. Sym^2_0 V, dim 104) | **0** (new small no-go) | -- |

Two structural facts worth naming:

1. **The scalar Yukawa channel exists, is unique, and is cross-chirality only.** A Dirac-type
   Yukawa (psi_+ , chi_- , scalar Higgs) is inside the equivariant family, with NO freedom in
   its spinor structure (dim 1). Nothing about its coefficient is fixed.
2. **CHANNEL-FORBIDDEN (new, small): no non-form Higgs carrier has any Yukawa channel.** The
   16384 checksum saturates End(S) by forms, so a carrier in e.g. Sym^2_0(V) (a
   "graviton-like" or distortion-tensor-valued Higgs) has dim Hom = 0 at the Spin(9,5) level.
   Same epistemic class as SHIAB-05, and exact.
3. **Transpose structure:** C^T maps the (+-) solution to the (-+) solution (overlap 1.000000).
   So a Dirac pairing psi_+^T C chi_- carries NO transpose-symmetry constraint -- the
   generation Yukawa matrix is not forced (anti)symmetric. (Load-bearing for Persona 2: no
   forced degeneracy.)

## Persona 2 -- Flavor physicist: what a hierarchy mechanism needs vs what is here

A real hierarchy mechanism needs at least one of: (i) a graded symmetry with a small order
parameter (Froggatt-Nielsen: charges + flavon + epsilon = vev/M); (ii) texture zeros from a
symmetry, with hierarchy from the zeros' pattern under seesaw/rank effects; (iii) rank-1
dominance (one generation coupled at leading order, others radiatively/higher-dim).

What the built structure supplies, computed on the derived Z/3 (order-3 element of SU(2)+,
eigenvalues {1, zeta, zeta^2}, fixed axis = democratic (1,1,1)/sqrt3 -- all reproduced):

- **Texture, yes (the HOOK):** Z/3-invariance cuts the 9-dim generation-Yukawa space to
  **3 dimensions** with support {(0,0), (1,2), (2,1)} in the Z/3 eigenbasis (charges-add /
  transpose-bilinear fork, which is the built C channel). This is a genuine **1+2 BLOCK
  texture**: the sector-0 (democratic-axis) generation decouples in the coupling graph from
  the cross-paired {1,2} sectors. Construction fork carried: the charges-subtract (Krein
  sesquilinear) fork gives instead a DIAGONAL texture, dim 3, no pairing structure. Both
  computed; which one the physical Yukawa uses is a source-action question.
- **Spectrum grading, no.** The three surviving couplings {y00, y12, y21} are free complex
  numbers. Singular values = {|y00|, |y12|, |y21|} exactly (witness (1,2,5) reproduced to
  1e-12): **no forced degeneracy** (T3: no transpose symmetry, so y12 and y21 independent;
  the H64 degenerate pair arises only under the OPTIONAL symmetric restriction y12 = y21) and
  **no forced ordering or ratio**. Top >> charm,up is "1+2-shaped" only in the coupling-graph
  sense; the structure does not make the distinguished generation heavy, light, or split.
  **PATTERN-COMPATIBLE (block level), NOT PREDICTED** -- and note the data do not show the
  degenerate-pair sub-texture at all (H64: mu/tau split by 17x), so even pattern-compatibility
  is at the weakest level.
- **FN engine, provably no (the sharp new negative):** see Persona 4.

Rank-1 dominance: the texture does contain a natural rank-1 candidate (y00 alone on the
democratic axis), but nothing suppresses y12, y21 relative to it. Not supplied.

## Persona 3 -- Model-building skeptic: attack every hook (the W60 discipline)

- **"The 1+2 texture predicts the fermion pattern."** No. (a) The 3 sectors are Z/3 GRADING
  slots, not flavor eigenstates -- identifying sector 0 with "the top quark" (or any physical
  generation) is exactly the frame-indices-are-spin / answer-as-premise trap (W60): the map
  from Z/3 sectors to physical flavors is itself source-action data. (b) The texture is
  GENERIC to any Z/3 family symmetry (Curie/genericity, verbatim the H64 caveat) -- it is
  standard Z/3 flavor structure, not a GU signature. (c) The fork matters: the Krein fork
  gives a plain diagonal texture with no distinguished generation at all.
- **"The scalar channel's uniqueness is deep."** It is exact but standard: End(S) = forms is
  textbook Clifford theory; the content is that the repo now has it as a checksum-controlled
  certificate covering ALL candidate carriers at once, not channel-by-channel.
- **"rho = (0,2,1) distinguishes the generations, so B carries a hierarchy seed."** The rho
  classes are Q/Z spectral labels of the Z/3 SECTORS of carrier B, and they are non-uniform
  (0, 2/3, 1/3 distinct) -- the sectors are genuinely spectrally distinguishable. But a label
  is not a coupling: turning labels into magnitudes needs an FN-type engine, and Persona 4
  shows the mod-3 arithmetic makes that engine impossible with these charges. The hook
  survives only as a LABEL, not as a grading.
- **Answer-as-premise audit of the whole wave:** the only "3" used is dim Lambda^2_+(R^4)
  (derived, H38); no mass, ratio, angle, or generation assignment was imported; the FN
  positive control uses deliberately NON-derived integer charges and is labeled a control.

## Persona 4 -- Mathematician (K-theory/torsion): does order-3 constrain TEXTURE or only count?

**Result: the order-3 structure constrains the texture's SUPPORT, and provably cannot
constrain its MAGNITUDES.** Two computed statements:

1. **Support:** the Z/3-invariant subspace of the 9-dim Yukawa space is exactly 3-dim with the
   {(0,0),(1,2),(2,1)} support (charges-add fork). This is the full reach of the order-3
   symmetry on the channel: a selection rule, i.e. texture ZEROS, not values.
2. **FN sterility (the new no-go-grade arithmetic):** read carrier B's rho = (0,2,1) as Z/3
   FN charges q. The FN exponent matrix n_ij = (q_i + q_j) mod 3 vanishes EXACTLY on the
   invariant entries -- and this is not special to (0,2,1): for ALL 27 assignments
   q in (Z/3)^3, every invariant entry has exponent 0 (tautologically: invariant = charge sum
   0 = ungraded). So **a mod-3 flavon can only grade entries that invariance already sets to
   zero; the surviving couplings are structurally ungradable.** Numeric confirmation: singular
   values of Y(eps) tend to three O(1) limits as eps -> 0 (smallest/largest ratio stays O(1)),
   while the integer-charge control q = (0,1,3) (NOT available in the built structure -- Z/3
   charges are only defined mod 3) produces a genuine hierarchy (ratio -> 1e-8 at eps = 1e-3).
   A Froggatt-Nielsen hierarchy engine requires charges valued beyond Z/3 -- i.e. a symmetry
   the built structure does not contain.

So the order-3/K-class structure grades the COUNT arena (index-changing, H39) and the texture
SUPPORT, and is arithmetically incapable of grading mass magnitudes. This is the same
"arena reaches the form, never the value" shape as H62/H64, now proved at the channel level.

## Persona 5 -- Honesty auditor: final verdict, not exceeding the computations

### Verdict per scoping question

1. **Equivariant Yukawa channels:** COMPLETE TABLE [COMPUTED]. One channel per
   (Lambda^k, allowed chirality block); scalar Dirac-Yukawa channel exists (dim 1,
   cross-chirality only); Majorana scalar FORBIDDEN (SHIAB-05 control reproduced); any
   non-form Higgs carrier FORBIDDEN (checksum saturation -- new small no-go).
2. **Order-3 action on channels:** NON-TRIVIAL [COMPUTED] -- the derived Z/3 cuts 9 -> 3 with
   the 1+2 block texture (charges-add fork; diagonal on the Krein fork). This is a HOOK at
   the texture/selection-rule level only.
3. **1+2 texture:** YES at coupling-graph level, **PATTERN-COMPATIBLE, NOT PREDICTED**; no
   spectral 1+2 (no forced degeneracy, ordering, or ratio); the sector-to-flavor map is
   unsupplied; generic to any Z/3, not GU-specific.
4. **Overall: SILENT on hierarchy, with one named hook and one new no-go.**
   - **SILENT:** no built object grades Yukawa magnitudes. All three surviving couplings are
     free source-action data. The one candidate grading structure (rho = (0,2,1) as FN
     charges) is provably sterile: mod-3 charges cannot grade the invariant entries -- for
     ANY charge assignment. The honest failure mode named in the brief is confirmed: mass
     structure is source-action-gated like everything else.
   - **HOOK-EXISTS (texture only), named object:** the Z/3-invariant Yukawa texture -- the
     3-dim invariant subspace {y00, y12, y21} of (generation-triplet)^2 tensored with the
     unique equivariant scalar channel, with sector 0 decoupled from the cross-paired {1,2}.
   - **CHANNEL-FORBIDDEN (new):** non-form Higgs carriers (e.g. Sym^2_0 V) have no Yukawa
     channel; Majorana scalar remains forbidden (prior).

### What the source action must supply (per outcome)

- Under SILENT (the standing state): (i) the Higgs-carrier identification (must be some
  Lambda^k; k=0 for a mass-type Yukawa) and its vev; (ii) the entire hierarchy -- three free
  complex couplings (or a flavor symmetry LARGER than the built Z/3, with charges beyond
  mod 3, plus a flavon and small parameter, if hierarchy is to be mechanized); (iii) the
  sector-to-flavor assignment; (iv) the pair-splitting/breaking spurion (H64); (v) the
  Majorana spurion if same-chirality masses are wanted (SHIAB-05).
- If the hook is engaged (source action realizes the charges-add fork with a Z/3-neutral
  scalar): the texture zeros come for free, but every magnitude above still must be supplied.
- Under the new no-go: the source action simply cannot put the Higgs in a non-form carrier;
  this PREVENTS a class of would-be constructions rather than demanding anything.

### Honest limits

- The reduced-level texture computation lives on the 3-dim generation space with the derived
  Z/3 (H38); it rides the identification of the generation index with the Lambda^2_+ triplet.
  The full fibered Yukawa on Y14 with generation structure woven in is not built here (it
  needs the source action).
- The FN sterility statement is arithmetic about mod-3 charges; a source action could import a
  larger flavor group with unreduced charges -- that is precisely "the source action supplies
  the hierarchy," not an evasion of the no-go.
- Nothing here moves canon, the count ({1,3}, located-not-forced), SG4, or any verdict.
  Scoping wave, one wave, closed.
