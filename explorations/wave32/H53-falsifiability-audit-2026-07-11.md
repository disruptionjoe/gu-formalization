# H53 (Wave 32) -- Falsifiability audit of the GU reconstruction program

**Object.** GU just made its first parameter-linked prediction and had it conditionally FALSIFIED. The
chain: everything empirical gates on ONE scale `mu_DW` (H49); the only PRINCIPLED identification of
`mu_DW` -- H36, DeWitt-Lambda = the observed dark-energy scale -- gives a sub-mm Stelle-Yukawa deviation
at `lambda = 60-74 um` (`c_L = 3/8` exact, H50/H51) that is EXCLUDED by short-range gravity, so H36 is
conditionally falsified. Scale-HUNTING (finding another `mu_DW` that "works") is p-hacking and is
OFF-LIMITS. The sharp Popperian question: does GU make ANY falsifiable prediction WITHOUT a forced
`mu_DW`, or is it decoupled-and-unfalsifiable until the (unbuilt) source action forces the scale?

**Discipline.** Adversarial, honest, Popperian -- not a defense of GU. (b) DECOUPLED and (c)
UNFALSIFIABLE are honest, valuable outcomes; a scale-independent prediction is NOT manufactured to
rescue GU. Personas run INLINE. Reproducible: `python tests/wave32/H53_falsifiability_audit.py`
(exit 0). COMPUTED vs ARGUED labeled throughout. Tree left dirty.

---

## Q1 -- THE SECTOR x SCALE-DEPENDENCE TABLE

Every place GU could touch data or make a falsifiable statement, classified as: **needs-free-scale**
(requires the unforced `mu_DW`, or free `f0`; the deviation is hideable by tuning that parameter),
**scale-independent PROPERTY** (a `mu_DW`-invariant structural fact), **settled** (passed/failed), or
**gated on the unbuilt source action** (not observable now).

| # | Sector | Status | Free param | Grade | Reason |
|---|---|---|---|---|---|
| 1 | PPN / solar-system (H10) | needs-free-scale | `mu_DW` | COMPUTED | Passes as an exp-suppressed Yukawa; requires `mu_DW > ~1e-17 eV`, cleared by ~45 orders at natural `M_Pl`. Deviation hideable; adds no binding constraint. |
| 2 | sub-mm Stelle-Yukawa, GIVEN H36 (H50/H51) | **settled-FAIL** | `mu_DW` forced = meV | COMPUTED | H36 forces `mu_DW = 2.3 meV` -> `lambda = 60-74 um` at `alpha = 1/3`, EXCLUDED by Kapner/Lee/Tan by an O(1)-robust factor. Self-falsifies the H36 identification. |
| 3 | sub-mm Stelle-Yukawa, WITHOUT H36 (H49) | needs-free-scale | `mu_DW` | ARGUED | Drop H36 and `mu_DW` is free again; the sole live window (`mu_DW ~ meV`) is a knife-edge; at `M_Pl` the range is `~1e-35 m`, decoupled. |
| 4 | GW extra polarizations / dispersion / propagator pole (H49) | needs-free-scale | `mu_DW` | COMPUTED | Massive spin-2 Compton frequency `~1e12 Hz` at the lab floor, `~1e27 Hz` at `M_Pl`; unexcited above the lab floor by any astrophysical source -> not observable. |
| 5 | 4th-order action ORDER / DOF count 7-vs-2 (H49/H45) | **scale-independent PROPERTY** | -- | COMPUTED | `box^2` present under BOTH GU branches, none in Bianconi/GR; **7 propagating DOF** is a `mu_DW`-invariant PROPERTY. But NOT an accessible observable unless the `~mu_DW`-mass modes are excited (Q2). |
| 6 | dark energy, CPL projection (H43/H44) | **settled-FAIL** | `f0` | COMPUTED | GU's `(w0,wa)` CPL locus excluded by DESI DR2 headline contour `~3.2 sigma`, robust to `M^2`, ansatz, backreaction. Falsified AS A CPL FIT. |
| 7 | dark energy, raw BAO distances (H46) | needs-free-scale | `f0` | COMPUTED | MARGINAL: excluded only at canonical-`f0` + CMB-fixed amplitude (`dchi2 = +21.6`); shape-marginalized competitive-to-better (`dchi2 = -3.2`); `f0` free (H42). |
| 8 | generation count `{1,3}` (H38/H40) | gated on source action | source-action carrier | COMPUTED | Located-not-forced; `{1,3}` not pinned to 3. WOULD be a scale-independent qualitative prediction IFF forced to 3, but forcing is source-action-gated. |
| 9 | fermion masses / Yukawas | gated on source action | source action | ARGUED | No source action -> no mass spectrum emitted; nothing to test now. |
| 10 | `|II|^2`-vs-`|H|^2` branch (H45/H49) | gated on source action | P2 (source-action norm choice) | ARGUED | The `|H|^2` branch = pure Mannheim-Kazanas conformal gravity, killed SCALE-INDEPENDENTLY by Horne/Hobson-Lasenby + the Jordan tree-ghost. But GU is FAVORED `|II|^2` (the *evading* branch), and P2 is gated on the source action. |
| 11 | class Lambda-magnitude no-go (H49) | **settled-FAIL (scope-kill)** | -- | COMPUTED | A scale-free two-metric action supplies only O(1) ratios; cannot contain `Lambda/M_Pl^4 ~ 1e-123`. The "Lambda emerges" HEADLINE is dead for GU and Bianconi alike -- a scope-kill of an overclaim, not of the theory. |

**Tally (COMPUTED):** 4 needs-free-scale, 3 settled, 3 gated-on-source-action, 1 scale-independent
PROPERTY. **Zero standing scale-independent OBSERVABLE predictions.** Every row is one of: hideable by a
free parameter, already settled, gated on the unbuilt source action, or a structural property that is
not an accessible observable.

**Two rows deserve emphasis because they look like scale-independent falsifiers and are not:**

- **Row 10 (the `|H|^2` branch).** Horne/Hobson-Lasenby "no genuine flat rotation curves" is a genuinely
  scale-INDEPENDENT, `mu_DW`-independent refutation -- but it only bites the `|H|^2` branch (pure
  conformal `gamma*r` gravity with no Einstein-Hilbert scale). GU is favored `|II|^2` (H45, P1 proven,
  P2 open), where the Einstein-Hilbert term makes the Bach sector a *short-range* massive spin-2 and the
  `gamma*r` mechanism is simply absent -- so the scale-independent kill EVADES on the favored branch. It
  fires only if the source action resolves P2 to `|H|^2`. A scale-independent falsifier that is itself
  source-action-gated.
- **Row 8 (the count).** `3` forced would be a clean scale-independent qualitative prediction. But the
  build gives `{1,3}` (H40 residue trap: net-3 has carrier-A's residue 0; the order-3 datum cannot
  certify a chiral 3). Located, not forced -- source-action-gated.

## Q2 -- IS THERE A SCALE-INDEPENDENT QUALITATIVE PREDICTION? (the decisive one)

The spin-2 action ORDER -- GU's 4th-order `box^2 = -4 Bach` vs GR/Bianconi's 2nd-order Einstein -- was
flagged as robust to the signature binary and needing no source action (H49). Is it ALSO robust to
`mu_DW`, and does it give a qualitative deviation no tuning can hide?

**The answer splits cleanly into PROPERTY vs OBSERVABLE, and the distinction is the whole verdict.**

**As a PROPERTY: YES, scale-independent [COMPUTED].** GU's graviton is genuinely 4th-order. The `box^2`
Bach term is present under BOTH GU branches (H45 Q2); Bianconi/GR carry none. The pole structure is two
poles (a massless graviton + a massive spin-2 companion at `p^2 = -m2^2`) for ANY `mu_DW > 0`; the DOF
count is **7 propagating DOF (2 massless + 5 massive spin-2), 5 more than GR's 2** -- an integer that
does not depend on `mu_DW`. As a statement about the Lagrangian, GU is NOT GR: it is a distinct theory,
and this distinction is `mu_DW`-invariant. **GU is therefore falsifiable IN PRINCIPLE.**

**As an OBSERVABLE: NO, scale-HIDEABLE [ARGUED from a COMPUTED scaling].** The massive companion has mass
`m2 = sqrt(m2_eff) * mu_DW`. Every observable GU-minus-GR effect -- the extra polarization admixture, the
GW dispersion, the Yukawa correction to the static potential -- is the leading effect of integrating out a
heavy field of mass `m2`, and scales as `(E/m2)^2` at accessible probe energy `E`. As `mu_DW -> M_Pl`,
`m2 -> M_Pl`, and `(E/m2)^2 -> 0` at EVERY fixed accessible `E`. Computed magnitudes (test PART 2):

| probe energy `E` | dev at `mu_DW = meV` | dev at `mu_DW = 1e6 eV` | dev at `mu_DW = M_Pl` |
|---|---|---|---|
| LIGO `~100 Hz` (`E ~ 4e-13 eV`) | `2.3e-20` | `2.0e-37` | `1.4e-81` |
| lab sub-mm (`E ~ meV`) | `7.3e-1` | `6.3e-18` | `4.4e-62` |

At natural `mu_DW ~ M_Pl` the massive-mode range is `~1.8e-35 m` (sub-nuclear), so the 5 extra DOF are
never excited by any accessible source and GU reduces OBSERVATIONALLY to GR's 2 DOF. **`mu_DW -> M_Pl`
pushes every deviation below detectability at all accessible scales.**

> **Q2 verdict:** the 4th-order content is a scale-independent PROPERTY (COMPUTED: the DOF count and
> action order are `mu_DW`-invariant, GU differs from GR at the level of the action) but a
> scale-HIDEABLE OBSERVABLE (COMPUTED scaling: every deviation is `(E/m2)^2`-suppressible and vanishes
> as `mu_DW -> M_Pl`). **There is NO scale-independent qualitative OBSERVABLE that no tuning can hide.**
> GU is falsifiable-in-principle but scale-hideable-in-practice: at natural `mu_DW` it is empirically
> indistinguishable from GR at all accessible scales.

This is the honest answer, and it does not rescue (a). The property-vs-observable gap is exactly the gap
between "a distinct theory on paper" and "a standing falsifiable prediction."

## Q3 -- THE POPPERIAN VERDICT

**(b) DECOUPLED-IN-PRACTICE, which for a free-scale framework is operationally (c)
CONSISTENT-BUT-UNFALSIFIABLE as it stands.** NOT (a).

- **Not (a).** There is no scale-independent qualitative OBSERVABLE prediction that no tuning can hide
  (Q2). The one scale-independent thing -- the 4th-order order / 7-DOF count -- is a property of the
  action, not an accessible observable; its every empirical footprint is `(E/m2)^2`-suppressible.
- **(b) DECOUPLED-IN-PRACTICE.** GU is falsifiable only if `mu_DW` happens to land in an accessible
  window. Every empirical channel (PPN, sub-mm Yukawa, GW polarizations/dispersion, dark energy) is
  gated on the free `mu_DW` (or free `f0`). At natural `mu_DW ~ M_Pl` all deviations decouple; only the
  knife-edge `mu_DW ~ meV` window is live -- and that window, when reached via the one principled route
  (H36), is FALSIFIED. `mu_DW` is a free parameter, so as it stands GU is effectively unfalsifiable.
- **(c) framework-not-theory.** Equivalently: GU is a consistent framework, not yet a standing theory,
  until the source action forces the scale.

**The demonstrated predictive CAPACITY matters and is stated plainly.** The H36 channel (DeWitt-Lambda =
observed DE) *was* computed to the end and emitted a falsifiable number (`lambda = 60-74 um`, `alpha =
1/3`), which was then EXCLUDED. That self-falsification proves GU is **not vacuous** -- it CAN emit
falsifiable numbers, exactly what a real prediction is supposed to risk. But the one candidate
self-falsified, leaving **ZERO standing predictions**. Capacity demonstrated; standing predictions zero.

## Q4 -- IS THE SOURCE ACTION THE FALSIFIABILITY KEYSTONE?

**YES.** GU's very falsifiability rests on H41. Every empirical channel is gated on the free scale
`mu_DW` (or `f0`); no scale-independent OBSERVABLE exists to carry falsifiability on its own; and the ONE
object that would force `mu_DW` -- turning the whole decoupled apparatus into a standing prediction (or a
clean kill) -- is the source action (H41). H41 was already the COHERENCE keystone (it fixes the gauge
vacuum, the soldering, the norm choice P2, the count carrier, the loop-positivity S-matrix). This audit
shows it is ALSO the **falsifiability keystone**: GU's scientific status as a testable theory, not just
its internal coherence, rests on building it.

**Honest public register (until H41):** *a consistent, reconstruction-grade geometric FRAMEWORK -- not a
standing theory. It has a DEMONSTRATED but (so far self-falsifying) predictive channel (H36 -> sub-mm),
ZERO standing predictions, and every empirical channel gated on the free scale `mu_DW`. Its
falsifiability rests on building the source action (H41) that would force `mu_DW`.* Not "GU predicts X";
the honest verb remains ACCOMMODATES, now sharpened: accommodation plus a demonstrated, self-falsifying
predictive channel -- a framework with a working but empty predictive gun, not a standing theory.

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| sector table: 4 needs-free-scale / 3 settled / 3 gated / 1 scale-indep-property | **COMPUTED** (classification of cited prior results) | PART 1, test |
| 4th-order order / 7-DOF count is `mu_DW`-independent (PROPERTY) | **COMPUTED** | H49/H45; test PART 2a |
| GU-vs-GR deviation `~ (E/m2)^2`, `m2 = sqrt(m2_eff) mu_DW` -> 0 as `mu_DW -> M_Pl` | **COMPUTED** (scaling + magnitudes) | test PART 2b/2c |
| no scale-independent OBSERVABLE that no tuning can hide | **ARGUED** (from the COMPUTED `(E/m2)^2` scaling) | Q2 |
| H36-forced sub-mm prediction EXCLUDED (settled-FAIL) | COMPUTED (H50/H51, cited) | rows 2, H51 `c_L=3/8` |
| CPL projection falsified; raw BAO MARGINAL | COMPUTED (H43/H44/H46, cited) | rows 6, 7 |
| `|H|^2` scale-independent kill (Horne/HL) is source-action-gated; GU favored `|II|^2` | ARGUED (from COMPUTED H45/H49) | row 10 |
| verdict (b)/(c) DECOUPLED / framework-until-H41; NOT (a) | ARGUED (Popperian, from the table + Q2) | Q3 |
| H41 is the falsifiability keystone; falsifiability rests on it | ARGUED | Q4 |

## Honest limits

- **The `(E/m2)^2` decoupling is the generic heavy-field scaling, not a from-scratch GU nonlinear
  amplitude.** It is the correct leading behavior of integrating out a spin-2 of mass `m2` and is
  reproduced deterministically, but the exact O(1) prefactors of each observable (dispersion,
  polarization admixture) are not re-derived from GU's full `|II|^2` source action (unbuilt). The
  scale-hideability conclusion is robust to the prefactor; the exact magnitudes are illustrative.
- **"No scale-independent observable" is a demonstrated-absence, not a theorem of impossibility.** The
  audit swept every sector the repo has reached (PPN, sub-mm, GW, DE, count, masses, the two branches,
  the Lambda no-go). A future GU-internal result could in principle expose a `mu_DW`-independent
  observable; none exists in the built content. Reported as an absence found after adversarially looking.
- **The verdict is conditional on `mu_DW` being genuinely free.** That is the current status (H24/H25
  BAR 2: only dimensionless ratios are geometric; the magnitude is smuggled). If H41 forces `mu_DW`, the
  verdict changes -- to a standing prediction or a kill. That is precisely why H41 is the keystone.
- **Scale-hunting stayed off-limits.** No alternative `mu_DW` was proposed to move the sub-mm point into
  an allowed window; that would be p-hacking. The audit reports the decoupling, not a rescue.
- **All external bounds and the Bianconi comparison are DATA**, used in comparison only (Kapner/Lee/Tan,
  Cassini, GW170817, Horne, Hobson-Lasenby, DESI DR2). No target imported; no claim promoted to canon.
  Tree left dirty.

## RE-RANK signal

**DECOUPLED (falsifiable-in-principle, unfalsifiable-in-practice until H41 forces `mu_DW`).**

- **Q1 sector table:** zero standing scale-independent OBSERVABLE predictions. 4 needs-free-scale, 3
  settled (2 fails + 1 scope-kill), 3 gated-on-source-action, 1 scale-independent PROPERTY (not an
  observable).
- **Q2:** the 4th-order content is a scale-independent PROPERTY (COMPUTED) but a scale-HIDEABLE
  OBSERVABLE (COMPUTED scaling `(E/m2)^2 -> 0` as `mu_DW -> M_Pl`). No scale-independent qualitative
  observable exists that no tuning can hide. Do NOT read the robust action-order result as a standing
  prediction -- it is a property, decoupled at natural scale.
- **Q3 verdict:** (b) DECOUPLED-IN-PRACTICE / (c) CONSISTENT-BUT-UNFALSIFIABLE as it stands. NOT (a).
  Predictive capacity demonstrated (H36 channel), standing predictions zero.
- **Q4:** GU's falsifiability rests on H41. The source action is the FALSIFIABILITY keystone, not just
  the coherence keystone -- **quintuply motivated** (it forces `mu_DW`, resolves P2, fixes the count
  carrier, gates loop positivity, AND is the sole route to standing falsifiability). Unambiguous #1.
- **Honest public register:** a consistent framework with a demonstrated, self-falsifying predictive
  channel -- not a standing theory. Verb stays ACCOMMODATES.

---

*Filed 2026-07-11. Wave 32. Reproducible: `python tests/wave32/H53_falsifiability_audit.py` (exit 0).
Exploration-grade; not promoted to canon. Tree left dirty.*
