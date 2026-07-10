---
title: "The -38 gamma-traceless question, ADJUDICATED: the honest geometric Rarita-Schwinger operator is elliptic with ind Q = -38 = 19*sigma/8 (published: Homma-Semmelmann Prop 3.1(i), fetched verbatim; in-house exact symbol-homotopy certificate), and its order-3 Nikulin rho classes are (0,2,1)/3 NONZERO. It differs from the pinned ghost-subtracted gravitino complex (-42 = 21*sigma/8, classes (0,0,0)) by exactly two reversed-chirality spin-1/2 units. The generation-arena order-3 verdict is now a named binary riding SG4. NEW OBJECT + GATE MOVED; located-not-forced HARDENED."
status: staged
doc_type: results
created: 2026-07-10
grade: "COMPUTED / exact (legs 106/96/580/155 asserts; referees 60/60/158/52 checks; all exit 0, re-run in-repo serially). Adversarially verified: 16-agent campaign, 4 legs x 2 hostile referees each, 0 refuted; referees used different arithmetic (sympy cyclotomics / Q(i*sqrt3) vs Q(zeta) pairs; Pauli vs quaternionic Clifford reps), a lift-free holomorphic-Lefschetz route, an exhaustive 729-config class-law check, and re-extracted the cited literature from the fetched PDFs themselves (pypdf, not trusting cached .txt). Literature anchors FETCHED and verified verbatim: Homma-Semmelmann arXiv:1804.10602 (eq (11), Prop 3.1(i), Remark 3.6, Prop 4.6 Ex.1), Baer-Mazzeo (ellipticity, chirality-reversal splitting, RS(K3)=38 sharp), Bilal eq (11.47). AGW primary (Nucl. Phys. B234) paywalled/unfetched; convention-A physics attribution rides two verified secondaries. Internal tier (caveat (e)). No CANON.md promotion; external publication pauses for Joe."
depends_on:
  - canon/order3-equivariant-rho-RESULTS.md
  - canon/rs-function-space-framework-SPEC.md
  - canon/families-e-invariant-order3-monodromy-RESULTS.md
  - absorbed/gu-source-action/DEAD-ENDS.md
scripts:
  - tests/rs-function-space/rho-38-adjudication/legA_symbol_homotopy.py
  - tests/rs-function-space/rho-38-adjudication/legB_index_bookkeeping.py
  - tests/rs-function-space/rho-38-adjudication/legC_equivariant_rho.py
  - tests/rs-function-space/rho-38-adjudication/legD_identification.py
  - tests/rs-function-space/rho-38-adjudication/referee_legA.py
  - tests/rs-function-space/rho-38-adjudication/referee_legB.py
  - tests/rs-function-space/rho-38-adjudication/referee_legC.py
  - tests/rs-function-space/rho-38-adjudication/referee_legD.py
---

# The -38 adjudication: two published carriers, one open identification

The prior campaign (`order3-equivariant-rho-RESULTS.md`) left one named verification target: the
"fourth convention" with index -38. This campaign adjudicated it. **It is not a convention. It is
the honest geometric gamma-traceless Rarita-Schwinger operator** -- elliptic, published
(Homma-Semmelmann; Baer-Mazzeo), a genuinely different K-class from the pinned ghost-subtracted
gravitino complex -- and its order-3 equivariant rho is NONZERO.

## The adjudicated mathematics

**1. Ellipticity + block-diagonalization (LEG-A, exact).** In the explicit Spin(4) Clifford model,
the compressed gamma-traceless symbol satisfies `det sigma_Q = (1/4) q^3` exactly (basis-independent
content: singular values `q x4, q/4 x2` = Weitzenboeck factors `1, ((n-2)/n)^2`), so `Q` is
elliptic. The straight-line contraction of the off-diagonal blocks stays elliptic on all of [0,1]:
`det sigma_t = f(t) q^4` with `f(t)/f(0) = (1/16)[1 + 3(1-t)^2]^2`, root-free (exact polynomial
identity; Sturm count 0; negative-control bad path degenerates at t=1, so the certificate is
non-vacuous; referee showed path-robustness across three paths). The embedded rank-2 block is the
REVERSED-chirality Dirac symbol scaled by `(2-n)/n = -1/2` -- the chirality reversal is published
verbatim in Baer-Mazzeo (`TM (x) Sigma^{+-} = iota(Sigma^{-+}) (+) Sigma-hat^{+-}`). Everything is
g-equivariant for the order-3 lift (symbolic-t identity).

**2. The index (LEG-B, two independent routes).** Additivity gives
`ind Q = ind(D tensor T_C) - ind(reversed D) = -40 - (-2) = -38 = 19*sigma/8 = -19*A-hat` --
and this exact additivity is INDEPENDENTLY PUBLISHED: Homma-Semmelmann eq (11)
(`ind Q = A-hat(TM)(ch(TM_C)+1)[M] = ind D_TM + ind D`) and Prop 3.1(i)
(`n=4: ind Q = -19 A-hat = 19/8 sigma`), fetched and verified verbatim. So `-38` does not ride the
in-house homotopy alone. The full convention table (all exact, no chi import):

| carrier | K-twist | index on K3 | density | mod 3 | order-3 rho classes | published gate |
|---|---|---|---|---|---|---|
| **A: ghost-subtracted gravitino** | `T_C - 1C` | **-42** | `21 sigma/8 = 7 p1/8` | 0 | **(0, 0, 0)** | AGW/Bilal eq (11.47); HS Remark 3.6 (Witten's ghost subtraction) |
| **B: geometric gamma-traceless Q** | `T_C + 1C` | **-38** | `19 sigma/8 = 19 p1/24` | 1 | **(0, 2, 1) NONZERO** | Homma-Semmelmann Prop 3.1(i); Baer-Mazzeo |
| bare twist (control) | `T_C` | -40 | `5 p1/6` | 2 | (0, 1, 2) | none |
| double subtraction (control) | `T_C - 2C` | -44 | `11 p1/12` | 1 | (0, 2, 1) | none |

Fork = `2 * ind(D) = 4`; `[B] - [A] = 2([S+]-[S-])` -- exactly two spin-1/2 units.

**3. The equivariant rho of the geometric operator (LEG-C, exact Q(zeta)).** Multiplier
`c_B = tr(g|T_C) + 1 = -1` at all 6 Nikulin fixed points (NOT 0 mod 3 -- carrier A's structural
kill `c_A = -3` is absent). `ind_phi(Q) = -2` by FOUR routes (equivariant additivity, nu-multiplier,
direct Atiyah-Bott, Hodge trace). Kernel `ker^-(Q) = {0: 14, 1/3: 12, 2/3: 12}`, `ker^+ = 0` --
matching Homma-Semmelmann's published `dim ker Q = 2 h^{1,1} - 2 = 38` on K3 (two copies of
primitive harmonic (1,1)-forms), equivariantly `2 x (7 + 6 zeta + 6 zeta^2)`. Result:
`eta = rho = (0, +2/3, -2/3)`, **mod-Z classes (0, 2, 1)/3 -- NONZERO**, with the classes
additionally kernel-independent (disk fixed-point route from local data + the exhaustively verified
class law `rho_k == -(k/3) ind mod Z`, checked over all 729 phase configs). Exact identity across
carriers: `rho_B = rho_A + 2 rho_Dirac` at every level (K-theory, index, multiplier, eta, class).

**4. Where the order-3 class lives (LEG-D).** Entirely in the orientation of the rank-2 spin-1/2
slot completing `D tensor T_C` to a spin-3/2 package: the twisted Dirac class `(0,1,2)/3` and the
Dirac class `(0,1,2)/3` are both order-3 live; **ghost SUBTRACTION cancels them exactly (carrier A,
class (0,0,0)); geometric reversed-chirality ADDITION doubles them (carrier B, class (0,2,1))**.
Z/24 arena: Dirac `(0,16,8)`, A `(0,0,0)`, B `(0,8,16)`.

## What is refuted, what is re-scoped

- **REFUTED (one sentence of the prior RESULTS):** "the index and the mod-Z class are stable under
  the gamma-traceless repackaging." False as written -- the geometric operator is a different
  published K-class, not a repackaging; both index and class move. APS-III deformation invariance is
  untouched; it does not apply across distinct K-classes. Correction note applied in place.
- **RE-SCOPED (the prior 2-primary verdict):** true of, and only of, the ghost-subtracted carrier A.
  Nothing in this campaign touches that arithmetic.
- **DEAD (the freeze rationale):** "the `T_C - 1C` pin is uniquely selected by the established
  gate" no longer discriminates -- BOTH carriers now pass a distinct established published gate
  (`21 sigma/8` physics vs `19 sigma/8` mathematics). Selection authority moved to SG4.
- **Probe scoping:** `family_generation_arena_probe.py`'s "every honest number == 0 mod 3" sweep is
  carrier-A-scoped (note added); the fiberwise `-38 != 0 mod 3` is NOT a pass of the families
  criterion (that requires the unbuilt fibered geometry).

## The single strongest honest statement

> The geometric gamma-traceless Rarita-Schwinger operator on K3 is elliptic, its index is
> `-38 = 19 sigma/8` (in-house exact symbol certificate + published HS Prop 3.1(i), two independent
> routes), and its order-3 Nikulin equivariant rho classes are `(0,2,1)/3` -- NONZERO; it differs
> from the pinned ghost-subtracted gravitino complex (`-42`, classes `(0,0,0)`) by exactly two
> reversed-chirality spin-1/2 units, and which of the two is the GU generation-arena carrier is an
> operator-identification question (SG4) that arithmetic provably cannot decide.

## The named binary (the new frontier shape)

**The generation-arena order-3 verdict is one bit riding SG4:** when the GU source action's
gravitino sector is built, either its quadratic form ghost-subtracts (BRST; carrier A) => the arena
is 2-primary and located-not-forced holds as before -- or it geometrically completes (carrier B) =>
the arena carries the nonzero order-3 class `(0,2,1)/3 = 2 x class(Dirac)`. In-repo tension a
hostile reader will press: GU's own RS-BRST packet reports MissingCarrierError and the ghost-parity
no-go says GU ghost parity cannot chiralize -- which SMELLS like an argument for carrier B; treating
that smell as a verdict would be story-shopping and stays blocked. Both steelmen intact.

**Steelman-ledger update (2026-07-10, transcript-tier):** re-reading the UCSD transcript against
this adjudication upgrades the carrier-B steelman from "in-repo smell" to **author-stated
mechanism, three independent ways**: [00:39:18] GU's third generation comes from the RS product
rule with the spin-1/2 term ADDED as physical matter (carrier B's arithmetic shape); [00:36:13]
"really two plus one; the third family is an imposter" -- the imposter IS the added spin-1/2 slot
this adjudication proved carries all the order-3 content; [00:41:48] the Velo-Zwanziger answer
implies ungauged spin-3/2 MATTER, and ghost subtraction exists only for gauged gravitini. Still
evidence, not verdict -- the bit rides the unbuilt action's quadratic form (SG4). Full reading:
`explorations/transcript-carrier-b-evidence-2026-07-10.md`.

**Decision-campaign update (2026-07-10, later same day; 0 legs refuted):** the carrier-bit decision
campaign (`canon/carrier-bit-decision-campaign-RESULTS.md`) ruled: (i) **the bit provably cannot be
decided by symbol arithmetic** -- the 343.73 obstruction is re-derived as an exact MUTUAL-EXCLUSION
certificate: on the gamma-trace-constrained field space no linear nilpotent ghost extension exists
(off the null cone), on the full field space a ghost-subtracted 4-term BRST complex exists exactly;
the carriers are mutually exclusive field-space DECLARATIONS, evidence for neither. (ii) No fetched
no-go theorem forces gauging on GU-as-stated (massless / global-SUSY hypotheses fail), none forbids
it (graded-IG upstairs door live); the ungauged massive carrier is published-viable inside a named
window (Einstein backgrounds -- K3 qualifies; Porrati-Rahman's causality cure IS the ker(Gamma)
constraint defining carrier B). (iii) The `-19` density is published for a NON-gauged spin-3/2
system in BOTH registers (HS math; PTZ PRD 106 (2022) physics: `-19 = -21 + 2` for Adler's RSA,
field content = spin-3/2 + ADDED spin-1/2, GU's stated shape). (iv) Referee corrections to the
steelman count above: L158 also carries transcript-tier support for the A-door, so the honest count
is **three B-passages vs one ambiguous A-passage**, and `-21` is equally published -- the real
asymmetry is GU-LICENSE, not publication. Net: **B-tilt at GU-commitments + published-theorem
grade; bit stays on SG4, escape routes enumerated and priced.**

## Honest limits

1. **SG4 MISSING-CARRIER (the live gate):** A-vs-B is not decidable from geometry or literature;
   this campaign computes both and selects neither. Nothing licenses replacing `-42` in canon, and
   nothing licenses extending A's 2-primary verdict to B.
2. **Equivariant globalization:** only the NON-equivariant additivity is published; the order-3
   equivariant version rides in-house flat-model certificates plus Spin(4)-naturality (two
   independent Clifford models agree; still models). Counterweight: the homotopy-free Atiyah-Bott
   route on Q reaches `ind_phi(Q) = -2` directly.
3. **Eta-level reals of B** (`(0, +2/3, -2/3)`, `h = (14,12,12)`) ride the pinned suspension
   conventions and the HS kernel identification (equivariance by naturality, not machine-checked);
   only the mod-Z classes are at adjudication grade. **B2 semantic note:** the computed rho is the
   SUSPENDED fiber operator's on `T_phi`; the intrinsic 5d RS operator is a different bundle (unlike
   the Dirac case) -- a separate computation if ever named.
4. **AGW primary unfetched** (paywalled); carrier-A attribution rides two verbatim-verified
   secondaries (Bilal eq (11.47); HS Remark 3.6 quoting Witten).

## Classification

**NEW OBJECT + GATE MOVED; located-not-forced HARDENED.** Not a verdict flip: the pinned object's
2-primary verdict stands exactly as scoped. The campaign adjudicated a second, distinct, published
operator into the program and proved its order-3 class NONZERO; the old selection gate collapsed;
the order-3 content is now located with exact arithmetic precision (the +-1 orientation of one
spin-1/2 slot, worth exactly `2 x class(Dirac)`), and nothing forced a 3 -- the four candidate
residues span `(0,1,2,1)`, and a zero outcome (carrier A confirmed by SG4) remains fully live. No GU
verdict, no physics claim, no generation-count movement, no public-posture change.
