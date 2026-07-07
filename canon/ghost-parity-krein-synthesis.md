---
title: "Ghost parity, Krein structure, and the generation count: a GU / Turok-Bateman synthesis"
status: active
doc_type: synthesis
created: 2026-06-28
depends_on: [papers/drafts/prepublish-review-tracker.md]
supersedes: [canon/multiplicity-theorem.md]  # provenance: this successor corrects/replaces the superseded predecessor; not a load-bearing dependency on its (retired) claim
external_ref: "Turok & Bateman, quadratic-gravity / Krein-space generalized Born rule (TOE interview, June 2026)"
---

# Ghost parity, Krein structure, and the generation count

> **UPDATE (2026-07-06 big swing + viability gauntlet; approved by Joe in chat 2026-07-07).** Two
> statements below are corrected by machine-checked results
> (`explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md`,
> `explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md`):
> (1) The closing speculation that the open condition `[P_ghost, S] = 0` is "plausibly met if GU's
> source action is quadratic-gravity-like" is WEAKENED TO NEAR-CLOSED: on the 192-dim triplet sector
> every GU-native core is PT-unbroken yet spectrally sign-blind (every eigenspace exactly K-balanced),
> so a dynamics-DERIVED C-operator/parity never arises (R3, SUSTAINED x2), and the conformal member of
> the quadratic class inherits the fiber and Kramers walls unchanged (R4). The condition itself is
> sharpened: S must be Krein-diagonalizable with real SIMPLE spectrum — at spectral degeneracies
> (GU's three-generation target regime) C exists but is non-unique (R1 verifiers), so derivedness
> does not transfer even where the mechanisms agree.
> (2) The reading "the same ghost parity ... turns GU's vectorlike self-dual triplet into three
> physical chiral generations" is FENCED by a new theorem: {K, chi} = 0 forces Re tr(chi Pi_+) = 0
> for EVERY admissible C (R3; independently re-derived by two verifiers), and every GU-native
> ghost-parity-even condensate channel is exactly isospectral across the parity — mirrors and
> generations gap together (V1, theorem over the enumerated native algebra). The split into 3
> positive-norm + 3 ghost states survives as a CONSISTENCY statement only; it is NOT a chirality
> selection, and the mirror-selective datum is an import. The count stays OPEN.
> Positive addition (V2, SUSTAINED x2): the Krein form K itself implements the Cartan involution of
> so(9,5) (residual 0.0e+00) and equals the ghost parity on the triplet — the consistency structure,
> the gauge-sector rescue, and the Krein geometry are one Z2 at kinematic grade.

> **CORRECTION (A0 audit, 2026-06-28).** Any framing below of the Krein / Hilbert-positivity move as an
> inside-class shadow or inside-class richer datum is RETRACTED. By the Weyl unitarian trick a
> finite-dimensional representation of a compact group always carries an invariant positive-definite form,
> so the indefinite Krein form exists only because the internal gauge group is taken NON-COMPACT (SO(5,5),
> not SO(10)). Dropping Hilbert positivity is therefore logically equivalent to negating Distler-Garibaldi
> assumption DG-A3 (compact internal G): it is a SCOPE-EXIT, not an inside-class enrichment. The
> machine-checked results (the consistent positive-norm sector, the chiral no-go, the cross-chirality of K)
> are unaffected; only the classification is corrected, now consistent with
> `canon/no-go-class-relative-map.md` (EVASION BY SCOPE EXIT, with DG-A3 now in the violated list).

## One-paragraph statement

GU's Rarita-Schwinger matter module is an indefinite-metric (Krein) space, not a Hilbert space, because
it is built on `Cl(p,q)` with `q > 0` timelike directions. The self-dual `SU(2)+` family symmetry (the
rank-3 `Lambda^2_+` of any 4-base, GU-forced geometry) puts the Standard-Model generation into a
multiplicity-3 triplet that survives the gamma-trace (this is the H1 kill: it refutes the earlier
"a count of 3 must be imported" thesis). That triplet is vectorlike: three generations plus three mirrors.
But under GU's *intrinsic* Krein metric the triplet is maximally neutral -- exact signature `(+96, -96)`
in every `p+q=14` signature tested -- so each generation is bound to its mirror in a **hyperbolic (null)
pair**. This is precisely the structure that Turok and Bateman's generalized Born rule is built to
quantize: a discrete **ghost parity** `Z2` resolves each hyperbolic pair into one positive-norm physical
state and one negative-norm ghost, and the projector form of the Born rule then yields positive
probabilities with the ghosts consistently removed. **Applied to GU, the same ghost parity that Turok
needs for positivity is the one that turns GU's vectorlike self-dual triplet into three physical chiral
generations.** The chirality/mirror problem of GU's matter sector and the positivity problem of indefinite
-metric quantum gravity are the same problem, with the same `Z2` as their joint resolution.

## What is established (machine-checked, exact)

Scripts: `tests/generation-sector/h1_selfdual_family_kill.py`,
`tests/generation-sector/ghost_parity_krein.py`. All guarded by the structure of `ker(Gamma)`.

1. **The matter module is a Krein space.** The `so(p,q)`-invariant inner product on `V (x) S` is the
   indefinite form `K = eta_V (x) beta_S`, where `beta_S` is the spinor Krein metric (product of the
   spacelike gammas; `beta_S` Hermitian, `beta_S^2 = I`, and `beta_S sigma + sigma^dagger beta_S = 0` for
   every `so(p,q)` generator `sigma` -- pseudo-anti-Hermiticity, residual `0.0e+00`). On the full
   `1792`-dim `V (x) S`, `K` has signature `(+896, -896)`.

2. **The self-dual triplet exists and carries the generation** (H1). `ker(Gamma) = 1664` decomposes under
   the self-dual `SU(2)+` as `640` singlets `+ 416` doublets `+ 64` TRIPLETS; the `192`-dim triplet sector
   carries the pure `Spin(10)` generation spinor (Casimir `-11.25 = 16/16bar` exactly).

3. **The triplet is a neutral / hyperbolic Krein subspace.** Restricted to the triplet sector, `K` has
   signature exactly `(+96, -96, 0)` in `(9,5)`, `(7,7)`, and `(14,0)`. Each chirality half is totally
   null; the form is purely the cross-pairing between a generation and its mirror. So the `96` states
   organize as `96` hyperbolic (generation, mirror) pairs. (`96 = 3 (SU(2)+ triplet) x 2 (SU(2)-) x 16`
   per chirality.)

4. **No algebraic parity chiralizes it on its own** (the H1d result). The net chiral asymmetry of the
   triplet is `0` in every signature, real and quaternionic. A net chiral count is an index, identically
   zero at the representation-theory level; it can become nonzero only through base-manifold topology
   (a Dirac index) or a ghost-parity-preserving dynamics that selects the physical half of each pair.

## The Turok-Bateman mechanism, applied

A hyperbolic pair has null basis `{u, v}` with `<u,v> != 0`; the combinations `u +/- v` have norms
`+/- 2<u,v>` -- one positive-norm (physical), one negative-norm (ghost). A **ghost parity** `Z2` (the
symmetry swapping `u <-> v`, i.e. generation `<->` mirror) canonically labels physical vs ghost as its
even / odd eigenspaces. Turok and Bateman's projector Born rule -- project onto the initial physical
subspace, evolve with `S`, project onto the final physical subspace, evolve with `S^dagger`, trace --
then returns probabilities that are positive and sum to one *even though individual norms are indefinite*,
provided the ghost parity is a symmetry of the dynamics (`[P_ghost, S] = 0`).

Applied to GU: the `96` hyperbolic pairs resolve, under such a ghost parity, into a positive-norm
physical sector (the three chiral generations, with their `SU(2)-` and gauge structure) and a negative
-norm ghost sector (the three mirrors), the latter removed consistently by the projector Born rule. The
generation count `3` is then a *physical* count in the Turok-Bateman sense, not a vectorlike artifact.

## What is open (the honest boundary)

- **GU has no built dynamics / source action.** Everything above is kinematic: the Krein structure and the
  hyperbolic pairing are exact, and a ghost-parity `Z2` swapping the null halves *exists* as a linear map.
  But whether it is a **symmetry of GU's dynamics** (the condition `[P_ghost, S] = 0` that Turok-Bateman
  positivity requires) cannot be checked, because GU supplies no `S`-matrix. This is the same gap as the
  unbuilt RS/IG source action.
- **The physical / ghost assignment is not canonical without that symmetry.** Kinematically the split of
  each hyperbolic pair into physical `+` ghost is basis-dependent; the ghost parity is exactly the extra
  datum that fixes it. So "three physical generations" is contingent on GU's dynamics realizing the ghost
  parity, not derived from kinematics alone. This coincides with the H1d / families-index finding: the
  chiral selection is the missing ingredient, and it is precisely what a ghost-parity-preserving dynamics
  (or, equivalently, a topological index) would provide.
- **The bare "3".** The clean `3` is the `SU(2)+` triplet multiplicity. The full triplet sector also
  carries an `SU(2)-` doublet and the `16/16bar` pair; extracting exactly three Standard-Model generations
  (and not `6`) is part of what the ghost-parity projection must accomplish, and is not yet shown in
  detail.

## Why this matters for the program

This relocates and sharpens the "firewall / external source" question that has run through the project.
The source object GU is missing is no longer an abstract "boundary that supplies the prime 3." It now has
a concrete specification: **a ghost-parity-preserving dynamics on GU's matter Krein space**, of exactly
the Turok-Bateman type, whose ghost parity selects three physical generations from the self-dual triplet's
hyperbolic pairs. The count is not imported from outside; it is latent in GU's own self-dual geometry
(the `Lambda^2_+` triplet) and made physical by the quantization rule. Two independent four-dimensional
"theory of everything" programs -- GU's geometry and Turok-Bateman's Krein-space quantization -- meet at
the same `Z2`.

This is a synthesis and a research direction, not a completed derivation. The kinematic facts are exact;
the dynamical completion is the open frontier and is identical to GU's long-standing missing source action.

## Distler-Garibaldi: a candidate inside-the-class evasion (new seventh axis)

The CapacityOS no-go-map (`work/drafts/wrk-376-gu-no-go-map/no-go-map.md`, cross-built against the
six-axis protocol `wrk-375-gu-six-axis`) singles out **Distler-Garibaldi as the stress case**: every
published evasion (E8xE8 heterotic, SO(3,11) GraviGUT, K(E10) Kac-Moody) *leaves the single-group class*,
and "there is no known richer-substrate datum that lives inside single-E8 representation theory and
reproduces three SM generations." The six-axis protocol "has no clean axis-drop" for it because its
assumptions sit below L1 (a specific finite-dim group and representation type). This is the map's declared
falsification surface for the whole no-go framework.

The Krein / ghost-parity result is a candidate evasion of a kind the map did not have: it stays **inside
the single-group class** and drops a different, hidden assumption.

- **It does NOT change the category.** We keep the single finite-dim reconstruction (`Spin(14)` /
  `Cl(p,q)`); no product group, no bundle, no Kac-Moody extension.
- **It does NOT contradict Distler-Garibaldi's representation-theoretic conclusion.** The matter rep is
  genuinely vectorlike (the self-dual triplet is real / mirror-paired; net chiral asymmetry 0 in every
  signature). That is exactly the Distler-Garibaldi mirror obstruction, reproduced.
- **It drops Distler-Garibaldi's hidden positivity assumption.** Distler-Garibaldi assumption (5) --
  "chirality means `V_{2,1}` is complex as a `G`-representation" -- presupposes the fermion state space is
  a positive-definite Hilbert space, so chirality must be a property of the full `G`-rep. GU's matter
  module is a **Krein space**; chirality is instead a property of the **physical (positive-norm,
  ghost-parity-even) subspace**, which can be chiral even when the full `G`-rep is real / vectorlike. The
  three mirrors are negative-norm ghosts, not physical mirror fermions.

**The forgetful operation** is therefore not a category collapse (the map's `phi_singleE8`) but a metric
forgetting: `phi_Hilbert : (Krein module, ghost parity Z2) -> (underlying real G-rep, positive-definite
metric)`. Distler-Garibaldi computes on the image of `phi_Hilbert`; the datum it forgets is the Krein
metric and its ghost parity. This is a genuine *shadow*, not a category change -- which is precisely what
the no-go-map said did not exist for Distler-Garibaldi.

**Six-axis placement: a new axis.** This evasion is not L1-L6 as currently menued. It is a **state-space
metric / positivity axis** (Hilbert vs Krein, with ghost parity), or equivalently a sharpening of Leg 3
(pairing) to carry the inner-product *signature* and not only the channel. It is the first candidate that
evades Distler-Garibaldi without leaving the single-group class.

**First falsification test (the honest open condition).** Does GU's eventual dynamics (the unbuilt source
action) realize the ghost parity as a symmetry, `[P_ghost, S] = 0`? Turok-Bateman positivity requires
exactly this. If GU's dynamics cannot preserve the ghost parity, the physical-chiral-three reading
collapses back to vectorlike and the evasion fails. This test is plausibly met if GU's source action is
quadratic-gravity-like (higher-derivative), since that is the dynamics for which Turok-Bateman built the
ghost parity in the first place -- which is why the quadratic-gravity question and this evasion are the
same question seen from the gravity and the matter side.

Status: a typed candidate, kinematically exact and dynamically open. It does not prove Distler-Garibaldi
is evaded; it identifies the precise new axis (positivity) and the precise test (ghost-parity-preserving
dynamics), and it converts the no-go-map's hardest stress case from "no inside-the-class datum exists" to
"here is one inside-the-class datum; its dynamical realization is the open question."
