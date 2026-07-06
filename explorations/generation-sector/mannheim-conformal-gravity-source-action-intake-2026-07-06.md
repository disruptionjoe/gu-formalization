---
title: "Intake: Mannheim conformal gravity as a candidate class for the missing source action"
date: "2026-07-06"
status: exploration
doc_type: external_intake
owned_path: "explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md"
depends_on:
  - "canon/ghost-parity-krein-synthesis.md"
external_ref: "Philip Mannheim, 'The Story of Conformal Gravity' (Curt Jaimungal, Theories of Everything, 2026), https://youtu.be/rNXNHYvS7zU"
---

# Intake: Mannheim conformal gravity and the ghost-parity frontier

Light intake extract from a TOE podcast episode (same input class as the Turok-Bateman interview that
seeded `canon/ghost-parity-krein-synthesis.md`). No claim movement; this note records why the episode
lands on this repo's live frontier and what a follow-up exploration would check.

## What the source says

Philip Mannheim (UConn, program running since 1972) presents conformal (Weyl) gravity: the pure
Weyl-tensor-squared action — reconstruction-grade recollection: `S = -alpha_g \int C_{munurhosigma}
C^{munurhosigma} sqrt(-g) d^4x`, the unique conformally invariant pure-metric action in 4D, with
fourth-order (Bach) field equations. Headline claims in the episode:

- renormalizable and (he argues) unitary quantum gravity;
- the fourth-order ghost is dissolved by the Bender-Mannheim PT-symmetric quantization of the
  Pais-Uhlenbeck oscillator (PRL 2008): the Hamiltonian is non-Hermitian but PT-symmetric, and with the
  PT inner product there are no negative-norm states;
- dark matter reinterpreted as the gravitational pull of the rest of the universe (exterior/cosmological
  sourcing of a linear potential term); 138 galaxy rotation curves fit with universal parameters;
- side topics: composite vs elementary Higgs, speculation on wavefunction collapse.

Facts above are from the episode page plus assistant recollection of the literature; primary sources are
NOT yet checked against this note. Treat as pointer-grade.

## Why it lands on the live frontier here

`canon/ghost-parity-krein-synthesis.md` leaves one named open condition: GU's unbuilt source action must
realize the ghost parity as a symmetry of the dynamics (`[P_ghost, S] = 0`), and the file states this
"is plausibly met if GU's source action is quadratic-gravity-like (higher-derivative), since that is the
dynamics for which Turok-Bateman built the ghost parity."

Conformal gravity is the maximally symmetric member of exactly that class. And the Bender-Mannheim PT
move is the original ghost-resolution for fourth-order dynamics — the direct ancestor/sibling of the
Turok-Bateman Krein-space projector Born rule the canon synthesis is built on. So the episode is not
topically adjacent; it is the 50-year worked example of "higher-derivative gravity + indefinite-norm
sector rendered physical by a discrete structure of the quantization."

## Candidate follow-up exploration (not yet run)

1. Compare Bender-Mannheim PT quantization vs Turok-Bateman ghost parity as candidate
   ghost-parity-preserving dynamics for GU's Krein matter module: are they the same mechanism in
   different dress (PT operator vs `Z2` swap of null halves), or materially different?
2. Ask whether a Weyl^2-type term is a viable shape for GU's missing source action, given GU's
   symmetries; conformal invariance is NOT obviously a GU symmetry, so the fit is class-level
   (higher-derivative + Krein + discrete rescue), not identity.
3. Inherit the stress tests: the PT-quantization critiques and the conformal-gravity phenomenology
   disputes (e.g. lensing-sign objections to the linear potential) are a real literature; if the PT
   mechanism has a known failure mode at the full nonlinear/field-theory level, the ghost-parity
   frontier here inherits that risk and should log it.

## Refined episode extract (added 2026-07-06, Joe-supplied secondary extract; still pointer-grade)

Joe supplied a detailed secondary extract of the episode the same day. Sharpened details worth carrying
(all pending primary-source verification):

- Action confirmed: `I_W = -alpha_g \int d^4x sqrt(-g) C_{lmnk} C^{lmnk}`, alpha_g dimensionless;
  variation gives the fourth-order **Bach equations**. Einstein solutions recovered in limits, but the
  theory admits EXTRA solutions (derivatives of Ricci can vanish without Ricci vanishing).
- Mannheim-Kazanas 1989 exact vacuum solution: `V(r) ~ -GM/r + (1/2) gamma_0 c^2 r`, plus in later
  analyses a quadratic `-(1/2) kappa c^2 r^2` from cosmic inhomogeneities; universal constants
  `gamma_0 ~ 3.06e-30 cm^-1`, `kappa ~ 9.54e-54 cm^-2`, fixed globally, not per galaxy. 111-138 galaxy
  rotation curves fit with only mass-to-light ratios free. Opposing signs of the linear/quadratic terms
  naturally bound galaxy sizes.
- Cosmology: fitted deceleration parameter ~ -0.37; no inflation needed (negative spatial curvature);
  cyclic non-singular universes possible; zero-point energies of gravity and matter sectors claimed to
  cancel, with the CC term induced by dynamical mass generation cancelled on symmetry breaking.
- Quantum claims: **no fundamental graviton** (gravity quantized solely through coupling to quantized
  matter; zero-norm / non-propagating graviton states); renormalizable via conformal symmetry + RG fixed
  points; composite Higgs (fermion-antifermion bound state); right-handed neutrinos needed for
  parity/conformal compatibility.
- Caveat he states himself: lensing must be RECOMPUTED for non-asymptotically-flat geometries — the
  standard lensing-sign objection lands on asymptotically-flat intuitions.
- Additional primary papers beyond the two in external_refs: **arXiv:1011.3495** (138-galaxy rotation
  curve fits with the linear+quadratic potential) and **arXiv:1610.08907** (mass generation, CC problem,
  conformal symmetry, Higgs).

## Guards

- GU is not conformal gravity. No identification is proposed; only class membership of the candidate
  source action.
- No claim movement, no canon change, no ledger entry from this intake.
- The refined extract above is a secondary source (episode summary), not a primary-source check.
- Anything promoted out of this note must first check primary sources (Mannheim-Kazanas 1989 exterior
  solution; Bender-Mannheim 2008; Mannheim-O'Brien / arXiv:1011.3495 rotation-curve fits;
  arXiv:1610.08907; published critiques).
