---
artifact_type: exploration
created: 2026-07-06
title: "VG-SA: Mannheim primary-source intake (rung 0) — gamma splits into an action-fixed local part and a curvature-datum cosmological part (pass-1 kill condition 2 adjudicates SPLIT, not fired-as-stated); kappa is a sourced moment integral, not an integration constant; q0=-0.37 is a fitted constant with no w(z) anywhere in the primaries; CC cancellation is a two-sector identity conditional on gamma_theta=-1 critical scaling; RH-neutrino and lensing-sign claims stay episode-only/unverified"
grade: "EXTRACTION (rung-0 source intake; no claim movement). The only computable content — the papers' internal numerical relations — passes 9 cross-checks plus a scrambled control at exit 0. Per-claim verdicts below use CHECKED / STILL-UNVERIFIED; the house computational enum does not apply to an extraction route and is not claimed."
depends_on:
  - explorations/persona-and-dialectic/all-persona-tri-theory-combination-steelman-hegelian-2026-07-06.md
  - explorations/big-swing-2026-07-06/SYNTHESIS-CONJECTURE-tri-theory-2026-07-06.md
  - explorations/persona-and-dialectic/conformal-class-steelman-hegelian-2026-07-06.md
  - explorations/generation-sector/mannheim-conformal-gravity-source-action-intake-2026-07-06.md
  - explorations/big-swing-2026-07-06/CROSS-EXAM-weinstein-turok-mannheim-first-principles.md
scripts:
  - tests/big-swing/vg_sa_mannheim_source_arithmetic.py
---

# VG-SA: Mannheim primary sources, read at last (rung 0 of the adjudication ladder)

## 0. Scope, method, and sourcing

Route SA of the 2026-07-06 gauntlet: primary-source intake on the three Mannheim papers the
federation docs lean on, executing rung 0 of the steelman's adjudication ladder (Section 6.3).
Method: the full LaTeX sources were downloaded from arXiv (`arxiv.org/e-print/<id>`) and read
directly — every quote below is verbatim from the `.tex` files, with Mannheim's own equation
labels. This is stronger than abstract-grade or ar5iv-truncated reading; nothing below is from
memory unless flagged.

| tag | paper | source file read |
|---|---|---|
| **P1** | arXiv:1101.2186, *Making the Case for Conformal Gravity*, Found. Phys. 42, 388 (2012) | `mexico4fp.tex`, 977 lines, full |
| **P2** | arXiv:1011.3495, Mannheim & O'Brien, *Impact of a global quadratic potential on galactic rotation curves*, PRL 106, 121101 (2011) | `fitting5.tex`, 1856 lines, full |
| **P3** | arXiv:1610.08907, *Mass Generation, the Cosmological Constant Problem, Conformal Symmetry, and the Higgs Boson*, Prog. Part. Nucl. Phys. 94, 125 (2017) | `ppnphiggs2.tex`, 3054 lines, full |
| **MK89** | Mannheim & Kazanas, ApJ 342, 635 (1989) | NOT read directly (predates arXiv). Content extracted via P1/P2 self-summaries, flagged `[MK89 via self-summary]` throughout |

Numerical fidelity receipt: `tests/big-swing/vg_sa_mannheim_source_arithmetic.py` recomputes
every numerical relation the papers assert between the extracted constants (kappa vs
(100 Mpc)^-2; gamma_0/kappa = 3.21e23 cm; (beta*/gamma*)^1/2 ~ 1e23 cm; gamma_0 = 2 sqrt(-K);
N*gamma* vs gamma_0 order; ~100 kpc max galaxy size; q0 in [-1,0]; the 111-galaxy subsample
sum; monotonicity of the (M190) luminosity distance), all pass, and a kappa-scrambled control
fails the same battery. Exit 0.

Posture: extraction only. No sympathy, no hostility, no claim movement, no credibility
transfer. A separate big-swing workflow (R1-R4) is running; nothing here cites its outcomes.

---

## 1. HOW gamma is fixed (adjudicates pass-1 kill condition 2)

### 1.1 The two-component structure: CHECKED, exactly as the federation docs carry it

The linear coefficient is genuinely two things added together. P1 Section 9 ("The dark matter
problem"):

Local part — a star sources, per unit solar mass (P1 eq. M59):

> "Given (M57), we see that a star would put out a weak gravity potential
> V*(r) = -beta* c^2/r + gamma* c^2 r / 2 per unit solar mass."

summed over the N* stars of a galaxy into the N*gamma* term of the rotation formula
(P1 eq. M60, M68). Cosmological part — added on top (P1 eq. M65, M67):

> "v^2_TOT/R = v^2_LOC/R + gamma_0 c^2/2 - kappa c^2 R"

with asymptotic limit (P1 eq. M68): `v^2_TOT/R -> N*beta*c^2/R^2 + N*gamma*c^2/2 + gamma_0
c^2/2 - kappa c^2 R`. Same formula as P2 eq. (23)-(24) and P3 eq. (M188). Universal values
(P1 M66/M69, P2 eq. 22, P3 M189, identical across all three):

> gamma* = 5.42e-41 cm^-1, gamma_0 = 3.06e-30 cm^-1, kappa = 9.54e-54 cm^-2
> (P3 adds beta* = 1.48e5 cm)

So: **CHECKED** — the linear coefficient has a local per-galaxy-mass component N*gamma* PLUS a
cosmological gamma_0, exactly the "gamma decomposed per-unit-mass" structure the steelman's
Section 4.6 attributed to Mannheim's fitting practice from memory.

### 1.2 Which equations produce each part — the answer that splits the kill condition

**The local gamma* factors through the action.** P1 eq. (M56)-(M58): in the static spherically
symmetric geometry the Bach equations reduce exactly to `nabla^4 B = (3/4 alpha_g B)(T^0_0 -
T^r_r) = f(r)`, and matching interior to exterior fixes

> "2 beta = (1/6) Int_0^{r0} dr' r'^4 f(r'),   gamma = -(1/2) Int_0^{r0} dr' r'^2 f(r')"  (M58)

The action coupling alpha_g sits inside f(r). This is selection through the Weyl^2 action's
field equations, quantitatively. `[MK89 via self-summary: P1 attributes the exact solution
(M55)-(M57) to Mannheim & Kazanas 1989.]`

**The cosmological gamma_0 does NOT arrive through the Bach particular integral.** P1 Section 9
is explicit that the homogeneous background lives in the complementary function:

> "The inhomogeneities contribute to the particular integral solution to (M11) given in (M62)
> (both nabla^4 B(r) and f(r) non-zero), while the homogeneous background contributes to the
> complementary function (both nabla^4 B(r) and f(r) zero)."

Because the RW background is conformal to flat, "the Weyl tensor vanishes identically in such
a geometry" and W^munu = 0 there — the Bach equation on the background degenerates to
T^munu_M = 0. gamma_0 then arrives by a **coordinate transformation of the comoving RW metric
to static coordinates** (P1 eq. M63-M64, transformation attributed to MK89):

> "Recognizing (M64) to be conformal to a topologically open RW metric with 3-curvature
> K = -gamma_0^2/4 ... in the rest frame of a galaxy the negative K global cosmology found in
> [Mannheim2006] acts like a universal linear potential with cosmological strength
> gamma_0/2 = (-K)^(1/2)."

P2 gives the fuller version and volunteers a frame caveat the federation docs did not have:
the general transformation yields K = -gamma_0^2/4 - k (two static scales from one RW scale),
and (P2, verbatim):

> "the decomposition of just one RW scale (viz. K) into two static scales (gamma_0 and k) is
> artificial, and it is not meaningful to keep both gamma_0 and k."

Mannheim retains the gamma_0-only representation because it covers the full static coordinate
domain ("the coordinate r would then be able to run all the way to infinity ... with nothing
being able to become complex"), whereas the k-only representation covers only an r <= k^(-1/2)
patch. So the linear-vs-quadratic split of the cosmological piece is a representation choice
justified by coordinate-domain coverage — Mannheim's own text, not a hostile reading.

What fixes the VALUE of gamma_0: the magnitude of K. K < 0 is argued dynamically (P1: the
nontrivial vanishing of T^munu_M on the background requires negative gravitational energy
density, i.e. negative 3-curvature, citing Mannheim2006), but the number 3.06e-30 cm^-1 is
FIT — first to 11 rotation curves (P1, citing Mannheim1997), held fixed thereafter. P1 does
call it "a derived gamma_0 = 2(-K)^(1/2)" in the MOND comparison — derived in the sense of
"expressed through the cosmological curvature," not computed from alpha_g.

### 1.3 Adjudication of pass-1 kill condition 2

The pass-1 doc (`conformal-class-steelman-hegelian-2026-07-06.md`, S2 antithesis blow 2)
claimed from memory:

> "The linear coefficient gamma is fixed by matching the local solution to the cosmological
> background THROUGH THE BACH EQUATIONS of the Weyl^2 action (from memory) — the selection
> factors through the action."

**Verdict: SPLIT — corrected, not confirmed as stated.**

- gamma* (local): selection DOES factor through the action. (M58) is Bach-equation matching to
  the local source with alpha_g explicit. The action clause of the Ext_S kill condition fires
  for this component.
- gamma_0 (cosmological): selection does NOT factor through the Bach particular integral. It is
  a complementary-function datum — the static-frame representation of the background spatial
  curvature K, whose sign is dynamically argued but whose value is observationally fitted, and
  whose linear form is a representation choice Mannheim himself calls part of an "artificial"
  decomposition. Typed in federation vocabulary: gamma_0 is a **continuous boundary/background
  datum supplied to, not derived from, the local action problem**. This is exactly the
  exterior-sourcing shape the tri-theory docs assign Mannheim, and it survives primary-source
  contact — for the cosmological component only.

Consequence for the standing absorber entry: the "gamma selection factors through the action,
kill branch (b) fires by inspection" sentence needs the split — branch (b) fires for gamma*,
does not fire for gamma_0. The interface object the federation cares about (the exterior
datum) is gamma_0, and it is curvature-datum-typed, not action-typed.

---

## 2. What sources the kappa term: CHECKED, with one correction to the steelman

P1 Section 9:

> "These inhomogeneities would typically be clusters and superclusters and would be associated
> with distance scales between 1 Mpc and 100 Mpc or so. ... the inhomogeneities would
> contribute constant and quadratic terms multiplied by integrals that are evaluated between
> end points such as r_clus that do not depend on the galaxy of interest, to thus be
> constants."

with (P1, after eq. M68):

> "kappa = (1/3c^2) Int_{r_clus}^{infinity} dr' r' h(r')"

i.e. kappa is the **particular-integral moment of the exterior inhomogeneity distribution**
(the r-to-infinity integrals of the fourth-order Green's function, P1 eq. M62 / P2 eq. E9-E10:
"it is only inhomogeneities that contribute to the third integral in equation (E10)"). P1's
summary footnote: "kappa is a matter fluctuation moment integral." P2's abstract types the
detection: "we are thus able to both detect the presence of a global de Sitter-like component
and provide a specific value for its strength." Fitted value kappa = 9.54e-54 cm^-2 ~
(100 Mpc)^-2 (P1 M69; arithmetic verified in the script, ratio 0.908).

**Correction registered:** the tri-theory steelman Section 3.4 says "Mannheim's gamma_0 and
kappa are integration constants of the fourth-order exterior equations." Half right. gamma_0
is complementary-function-typed (an integration-constant-like background datum). kappa is NOT
an integration constant — it is a **sourced moment integral over the actual exterior matter
distribution** (Weyl-tensor-carrying inhomogeneities, nonzero f(r)), i.e. it factors through
the Bach equations' particular integral with a physical source. The two exterior constants
have opposite typing: gamma_0 = geometry/frame datum, kappa = sourced-field datum. Any
federation leg (T2', T5') that treats "(gamma_0, kappa)" as one homogeneous class of exterior
data should carry this asymmetry.

---

## 3. q0 = -0.37: what the primaries actually assert (and what they never mention)

P3 eq. (M190) gives the closed-form Hubble-plot function:

> "d_L(z) = -(c/H_0) (1+z)^2/q_0 (1 - [1 + q_0 - q_0/(1+z)^2]^(1/2))"

and (P3, verbatim):

> "in the conformal theory the structure of the cosmological evolution equations is such that
> q_0 is constrained to lie in the interval -1 <= q_0 <= 0 no matter what the magnitudes of
> the parameters in I_M(conf). Fits given in [Mannheim2006] ... are found to lead to the value
> q_0 = -0.37 ... As constructed, the conformal theory is naturally accelerating at all epochs
> (which is why it required no fine tuning in the first place) while in contrast, the standard
> paradigm is fine tuned to only be accelerating at late epochs. Consequently, at redshifts
> above one or so the conformal theory and standard theory Hubble plot expectations start to
> differ, and ... begin to do so quite markedly by a redshift of two or so."

Extraction verdict on the "quasi-static or dynamical w(z)?" question:

- **q0 = -0.37 is CHECKED** as a fitted constant (fit made in Mannheim2006, reproduced in P3
  Fig. "accelerating"). The cross-exam's "q0 ~ -0.37, per the episode extract" is now
  paper-verified.
- **The string "w(z)" and any equation-of-state function appear NOWHERE in the three
  primaries.** The fit is a one-parameter closed-form d_L(z) in the current-era deceleration
  parameter. The steelman's label "his quasi-static q0 ~ -0.37 (from memory)" is right that no
  dynamical w(z) is offered, but slightly mis-shaped: (M190) is presented as following from the
  exact conformal evolution equations (with negative lambda and negative k), not as a
  quasi-static approximation. The theory's own stated discriminator against LambdaCDM is
  **permanent acceleration** (all epochs, divergence at z >~ 1-2), not thawing/evolving w. Any
  sky-program leg that wants "w(z) must be dynamical, against Mannheim" should restate the
  target as: against Mannheim's PERMANENT-acceleration, single-q0 Hubble plot — a sharper and
  checked formulation. (The DESI-era observational claims in the steelman remain from-memory,
  outside these three papers.)

---

## 4. The zero-point / CC cancellation: the actual stated logic, end to end

The mechanism, assembled strictly from P1 Sections 6-8 and P3 Sections 9.2-9.5 (all quotes
verbatim):

1. **The gravitational equation of motion IS a vanishing condition on total energy-momentum.**
   P1 eq. (M11): `-4 alpha_g W^munu + T^munu_M = 0`; P3 writes it as T^munu_UNIV =
   T^munu_GRAV + T^munu_M = 0. "For gravity the equation of motion is expressly a condition on
   the energy-momentum tensor itself ... one cannot consistently set T^munu_GRAV = 0 since it
   has a non-vanishing zero-point contribution. Hence one must instead set T^munu_GRAV +
   T^munu_M = 0." (P3 footnote.)
2. **Divergences cancel between sectors, not within one.** P1 (M31)/(M32), P3 (M183)/(M184):
   the identity splits into (T_GRAV)_DIV + (T_M)_DIV = 0 and (T_GRAV)_FIN + (T_M)_FIN = 0.
   "With (M31) we see that all gravitational and matter field infinities cancel each other
   identically, with (T_GRAV)_DIV and (T_M)_DIV regulating each other." Bosonic graviton
   zero-point against fermionic matter zero-point: "in essence in conformal gravity the
   graviton itself performs the task that a bosonic superpartner of the fermion does in the
   supersymmetry case" (P3).
3. **Gravity has no stand-alone quantization; the matter source fixes it.** P3: "gravity is
   quantized entirely by virtue of it being coupled to a matter source that is quantized";
   Z(k) = 1 forced in the unbroken massless case (P3 M177), and generally "2Z(k) + M - N = 0"
   for M massless gauge bosons and N two-component fermions, "with gravity adjusting to
   whatever its source is." No matter source => Z(k) = 0, no graviton quantization at all
   (P3 footnote). There is "no intrinsic classical gravity at all, with gravity being produced
   entirely by quantum effects" — expansion in powers of hbar, no hbar^0 term.
4. **The cancellation survives the symmetry breaking that mints scales.** P3 (M178)-(M182):
   after dynamical breaking at the critical point, Z(k) readjusts (M182) and "the zero-point
   vacuum energy density in the gravity sector identically cancels both the quartic divergence
   and the induced finite cosmological constant term in the matter sector." Footnote: "Since
   symmetry breaking is an infrared, long range order, effect, the mutual cancellation ... is
   not affected." This is the paper's stated answer to why broken conformal symmetry keeps the
   protection broken supersymmetry loses.
5. **The trace anomalies are claimed to cancel between sectors.** P1 footnote to (M31)/(M32) and
   P3 footnote: "the gravity sector and matter sector trace anomalies thus have to cancel each
   other identically order by order in perturbation theory, with T^munu_UNIV being anomaly
   free." The stated ground is stationarity, not a conformal Ward identity.
6. **Conditionality — the mechanism is NOT generic.** It requires the matter sector at a
   critical RG point with gamma_theta(alpha) = -1 (dynamical dimension of psi-bar-psi reduced
   from 3 to 2) and the four-fermion term: "the four-fermion interaction plays a double role —
   it is needed to generate a dynamical Higgs boson and is needed to cancel vacuum energy
   density infinities that couple to gravity" (P3). And both sectors must be renormalizable for
   the identity to persist order by order.
7. **What cosmology then measures.** P3: astrophysics uses the infinity-free particle equation
   (M184); "Cosmology thus only sees the change in the vacuum energy density due to adding in
   positive energy modes and does not see the full negative energy mode vacuum energy density
   itself" — the S_0 entering cosmology is the mode-difference expectation, "an altogether
   smaller quantity."

Extraction note for the federation: the stated logic is a **two-sector cancellation identity
enforced by the equation of motion**, conditional on (i) conformal both-sector actions,
(ii) renormalizability of both sectors, (iii) critical scaling gamma_theta = -1 with a
four-fermion term. It is not a symmetry-protection argument in the SUSY sense and it is not
claimed to hold for a stand-alone Weyl^2 theory. Items (i)-(iii) are Mannheim's own stated
load-bearing conditions, quoted, not our gloss.

---

## 5. Composite Higgs and right-handed neutrinos

### 5.1 Composite Higgs: CHECKED, with the mechanism now on record

P3's whole architecture (Sections 5-8): the Higgs field is either "a q-number elementary field
... or it is generated as a dynamical bound state, with the field in a dynamically induced
Higgs potential then being the c-number matrix element <S|psi-bar psi|S>, a dynamical bilinear
fermion condensate" (P3 Section 5.1). The dynamical route: NJL as mean field, then
Johnson-Baker-Willey QED at the Gell-Mann-Low eigenvalue with gamma_theta(alpha) = -1, where
the four-fermion interaction becomes renormalizable via anomalous dimension d_theta = 2 and
generates dynamical Goldstone and Higgs states. P3 Summary, verbatim:

> "(i) a bound state Higgs boson has no hierarchy problem, (ii) when the Higgs boson is a bound
> state, the same dynamics that fixes its mass as the position of the pole in a
> fermion-antifermion scattering amplitude also fixes its coupling to the fermions as the
> residue at the pole, (iii,iv) when the Higgs generation mechanism involves the four-fermion
> interaction then on coupling to conformal gravity one can resolve both the cosmological
> constant problem and the zero-point problem."

P3 exhibits the dynamical Higgs as a RESONANCE above threshold: `q_0 = (1.48 - 0.02i)
(M mu)^(1/2), q^2 = (2.19 - 0.05i) M mu` — poles off the real axis, width dynamical. P3's
candidate "theory of everything" action (M209): `I_UNIV = J_D + I_W + I_YM + I_FF`, conformal
everywhere, "all mass ... generated in the vacuum by dynamical symmetry breaking," with quark
and lepton mass matrices "potentially calculable" (footnote) but expressly "for the future" —
i.e. **P3 makes no generation-count claim of any kind.** Relevant to the federation: even the
friendliest conformal-breaking primary offers no discrete/countable structure in the
condensate channel; the count invoice (T2') gets no help here.

Nuance across papers: P1 (2011, pre-discovery) says the Ginzburg-Landau order parameter "would
not be observable in an accelerator" (P1 Section 3); P3 (2016, post-discovery) presents the
125 GeV boson as compatible with a dynamical bound state. Evolution of position, on record.

### 5.2 Right-handed neutrinos: NOT in these papers as claimed — STILL-UNVERIFIED

The ONLY right-handed-neutrino statement in all 5,887 lines of the three sources is one
footnote (P3, Section 8):

> "in an actual application to weak interactions one would have to take the weak interaction to
> have a chiral SU(2)_L x SU(2)_R x U(1) structure of the type described in e.g. [Mannheim1980]
> ... in analog to Cooper pairing, in [Mannheim1980] it was shown that right-handed neutrino
> pairing would break the SU(2)_R sector."

The intake doc's episode-derived claim "right-handed neutrinos needed for parity/conformal
compatibility" is **not stated in P1, P2, or P3**. It may live in Mannheim1980 or the episode
only. Marked STILL-UNVERIFIED; anyone leaning on it must fetch Mannheim (1980) or the episode
transcript.

---

## 6. What Mannheim himself says about lensing in these papers

All three primaries treat lensing as OPEN work, none reports a conformal lensing success, and
none engages the sign dispute head-on:

- **P1** (Summary): "much more still needs to be done: anisotropy of the cosmic microwave
  background, large scale structure, cluster dynamics and lensing by clusters (especially in
  light of the recently found global -kappa c^2 R term in (M67) and (M68))."
- **P2**: "for lensing we need to use equation (E9) for points exterior to the cluster, and in
  both cases we need to include the global effect due to all of the other clusters in the
  Universe. Since previous applications of conformal gravity to clusters (velocity dispersions,
  X-rays in clusters, and lensing [Walker1994, Edery1998, Pireaux2004a, Pireaux2004b,
  Sultana2010]) did not include this global effect, studies of its possible impact ... could be
  instructive." — i.e. Mannheim's own position is that ALL prior conformal lensing analyses
  (including the hostile ones) omitted the global kappa/gamma_0 terms.
- **P3**: "two of the most urgent issues are gravitational lensing and fluctuations in the
  cosmic microwave background. For lensing the impact of the recently identified kappa term
  needs to be worked out since one is dealing with light coming in from a non-asymptotically
  flat background."

This CHECKS the intake doc's episode caveat ("lensing must be RECOMPUTED for
non-asymptotically-flat geometries") as a genuine paper-level position, not just podcast talk.
It does NOT check the steelman 4.6 claim that "the lensing sign ... already fired: null
geodesics in the Mannheim-Kazanas exterior give deflection ~ -(gamma)r/2 (Edery-Paranjape
1998, from memory)": Edery1998 is cited in P2's reference list as a lensing study, but no
deflection formula or sign appears in any of the three primaries. The adverse-sign claim
remains STILL-UNVERIFIED at rung 0 and needs Edery-Paranjape itself (plus Yoon 2013 and
Hobson-Lasenby 2021 for the other two objections, none of which these primaries engage —
P2's "artificial decomposition" passage in Section 1.2 above is however directly relevant
raw material for the Hobson-Lasenby frame question).

---

## 7. Claim ledger: CHECKED vs STILL-UNVERIFIED vs CORRECTED

Every Mannheim-touching claim in the intake/cross-exam/steelman docs, adjudicated:

| # | claim (doc) | verdict |
|---|---|---|
| 1 | Action I_W = -alpha_g Int d^4x sqrt(-g) C_lmnk C^lmnk, alpha_g dimensionless, unique local-conformal pure-metric action, fourth-order Bach equations (intake) | **CHECKED** (P1 eq. M9 + Section 3: "the unique gravitational action that is invariant under the local transformation g -> e^{2 alpha(x)} g"; EOM M11) |
| 2 | Extra solutions beyond Einstein (Ricci derivatives vanish without Ricci vanishing) (intake) | **CHECKED** (P3 Section 10.1: "the vanishing of W^munu can be achieved without the vanishing of the Ricci tensor itself"; Schwarzschild recovered as exact vacuum solution) |
| 3 | V(r) ~ -GM/r + (1/2) gamma_0 c^2 r; later quadratic -(1/2) kappa c^2 r^2 from inhomogeneities (intake) | **CHECKED with refinement** — the linear term is N*gamma* + gamma_0, not gamma_0 alone (P1 M59-M68); quadratic sourcing confirmed (Section 2 above) |
| 4 | gamma_0 = 3.06e-30 cm^-1, kappa = 9.54e-54 cm^-2, universal not per-galaxy (intake) | **CHECKED** (P1 M66/M69, P2 eq. 22, P3 M189; "needing to be universal and not have any dependence on a given galaxy at all") |
| 5 | 111-138 galaxy fits, only M/L free (intake) | **CHECKED, numbers pinned**: P2 fits 111 (18+30+20+21+22, script-verified); P1 quotes the extended 138-galaxy program; P3 quotes 141. "The only parameter that can vary from one galaxy to the next is the galactic disk mass to light ratio" (P1). The task label "1011.3495 = 138-galaxy fits" is off by paper: 138 belongs to the companion program P1 cites, P2 itself is 111 |
| 6 | Opposing signs of linear/quadratic bound galaxy sizes (intake) | **CHECKED** (P1: no bound orbits beyond gamma_0/kappa = 3.21e23 cm, script-verified; "global physics thus imposing a natural limit on the size of galaxies") |
| 7 | q0 = -0.37 fitted; -1 <= q0 <= 0 structural (intake "per episode"; cross-exam) | **CHECKED** (P3 M190 context; fit from Mannheim2006) — upgraded from episode-grade to paper-grade |
| 8 | No inflation needed / negative spatial curvature; cyclic non-singular universes (intake, episode) | **PARTIAL**: negative-K cosmology, no cosmological dark matter, no fine-tuning — CHECKED (P1 Section 9, P3). The words "inflation" and "cyclic" appear NOWHERE in the three primaries — those remain episode-only, STILL-UNVERIFIED |
| 9 | Zero-point energies of gravity and matter cancel; induced CC cancelled on breaking (intake) | **CHECKED and mechanism now on record** (Section 4 above; P3 M178-M184) |
| 10 | No fundamental graviton / gravity quantized solely through coupling to quantized matter (intake) | **CHECKED in substance** (P3: Z(k) fixed by source, Z=0 absent matter, "no intrinsic classical gravity"). The phrase "zero-norm graviton states" appears nowhere in the three primaries — that wording stays episode-only |
| 11 | Composite Higgs (fermion-antifermion condensate) (intake) | **CHECKED** (Section 5.1 above) |
| 12 | Right-handed neutrinos needed for parity/conformal compatibility (intake, episode) | **STILL-UNVERIFIED** — only the SU(2)_R-pairing footnote exists in the primaries (Section 5.2) |
| 13 | Lensing must be recomputed for non-asymptotically-flat background (intake) | **CHECKED** (P3 verbatim; P2 adds that all prior conformal lensing studies omitted the global terms) |
| 14 | "gamma fixed ... through the Bach equations — selection factors through the action" (pass-1 kill condition 2) | **CORRECTED: SPLIT** (Section 1.3) — gamma* yes, gamma_0 no; gamma_0 is a curvature/frame datum whose value is fitted |
| 15 | "gamma_0 and kappa are integration constants of the fourth-order exterior equations" (steelman 3.4) | **CORRECTED** (Section 2) — gamma_0 complementary-function-typed; kappa is a sourced particular-integral moment, not an integration constant |
| 16 | "quasi-static q0 ~ -0.37"; "w(z) must be dynamical, against his ..." (steelman 3.4/4.6) | **CORRECTED in shape** (Section 3) — q0 checked; but no w(z) exists in the primaries to be quasi-static ABOUT; Mannheim's own discriminator is permanent acceleration diverging from LCDM at z >~ 1-2 |
| 17 | Edery-Paranjape adverse lensing sign ~ -(gamma) r/2 (steelman 4.6, from memory) | **STILL-UNVERIFIED** at rung 0 — not present in these primaries; requires Edery-Paranjape 1998 directly (likewise Yoon 2013, Hobson-Lasenby 2021) |
| 18 | Bender-Mannheim PT quantization dissolves the fourth-order ghost (intake) | **CHECKED as claim-of-record** (P1 Section 5 asserts it, citing Bender2008a/b): "Bender and Mannheim have recently shown that one can find a realization of the theory that is unitary." Whether the mechanism works, and its relation to ghost parity, is the R1 workflow's question — gate only, no outcome cited |
| 19 | MK89 content (exact vacuum solution; RW-to-static transformation) | **CHECKED via self-summary only** — P1 (M55-M58, M63) and P2 both attribute these to Mannheim & Kazanas 1989; MK89 itself unread. Flagged throughout |

---

## 8. What this intake hands the federation legs (typed, no claim movement)

- **T2' (index-in-the-breaking):** worse for the synthesis than the from-memory version. The
  exterior data are not merely continuous — the cleanest one (gamma_0) is a FRAME-REPRESENTED
  curvature datum Mannheim himself calls part of an artificial decomposition, and the
  friendliest breaking primary (P3) offers no discrete structure in the condensate channel and
  no generation count anywhere. Nothing in rung 0 pays, or even denominates, the 3-torsion
  invoice.
- **T5' (VEV map):** the condensate is now precisely typed at source: <S|psi-bar psi|S> at a
  gamma_theta = -1 critical point, mass switched ON by forming (P3) — the decreased-VEV vs
  formed-condensate sign tension carried by the steelman is confirmed as real at the Mannheim
  end, verbatim.
- **T9'/R1 gates:** the CC-cancellation identity (Section 4) is conditional on two-sector
  renormalizability and the anomaly-cancellation footnote — a concrete UV clause any
  federation positivity-locus story inherits. Stated as gate input only.
- **SKY':** the one-condensate lock's Mannheim-side target should be restated per Sections 1-3:
  per-mass gamma* (action-typed) vs universal gamma_0 (curvature-typed) vs kappa (moment-typed),
  permanent acceleration rather than thawing w(z), and a lensing story Mannheim himself marks
  unfinished pending the global terms.

## 9. Honest limits of this route

Full-text reading of three primaries plus a numerical fidelity script; no independent
derivation checks (the (M58) integrals, the (M63) transformation, and the Z(k) computations
were transcribed, not re-derived); MK89, Mannheim1980, Mannheim2006, Bender-Mannheim 2008, and
the entire critical literature (Edery-Paranjape, Yoon, Hobson-Lasenby, Flanagan) remain
unread — the last four are named rung-0 residue. Single-process caution applies: the same
process that wrote the federation docs performed this extraction; the quotes are verbatim and
grep-reproducible from the arXiv e-print sources, which is the strongest independence this
route can offer.
