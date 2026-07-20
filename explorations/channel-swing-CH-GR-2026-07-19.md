---
title: "Channel swing CH-GR: C10 formalized to a computed cancellation identity; branch space collapses to one"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (deep research swing, CH-GR channel)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/adapter-assumed-four-leg-swing-2026-07-19.md
  - explorations/five-leg-swing-2026-07-19.md
inputs:
  - explorations/transcript-reread-distortion-vacuum-field-2026-07-19.md
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md
  - explorations/construction-space-gr-r0-lemma-c9-c3-2026-07-19.md
  - lab/process/source-object-interface-contract.md
test: tests/channel-swings/ch_gr_vev_stress_probe.py
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Channel swing CH-GR: the distortion VEV computed

Assignment: take C10 (distortion vacuum field) as far as honest formalization
allows under the standing axiom, compute the VEV stress for the three H-GR'
sub-branches, check the C2 scale law, draft the CH-GR parameter card, and
sharpen the kill tests. All of that is done, with a runnable probe:
`tests/channel-swings/ch_gr_vev_stress_probe.py` (exit 0, 20/20 checks).

## Headline

**Branch (a) — curvature-locked anisotropic — is LIVE and computes to an
exact cancellation identity.** In the weak-field symbol frame the C10
distortion VEV's quadratic stress carries a NONZERO trace-free
`Q^TF(B)`-slot component at `O(M^2)` (the first live nonzero trace-free
candidate in the whole GR construction space), and it cancels the computed
`Q^TF(B)` residual EXACTLY with one frozen pure number (`kappa^2 = 1`) and
one sign bit (`sigma = +1`), on Schwarzschild AND on the Kerr
frame-dragging background with the SAME frozen coefficient. Branches (b)
homogeneous and (c) gradient-dominated are computed DEAD. The C10 branch
space is no longer hypothetical: it is a computed 3-element list with one
survivor.

## 1. The typed home for theta

Transcript anchors ([00:22:26]-[00:25:56]): theta is the **distortion** —
"any connection minus the gauge-transformed Levi-Civita" — with "great
equivariance properties" (adjoint-valued under the tau_+ double quotient),
and it "replaces lambda times the metric": "it's not lambda times the
metric. It's a field."

Program-native typing (construction fork: GU-native, not standard-field):

- **Bundle home.** On `Y14 = Met(X4)` with physical section
  `g: X4 -> Y14`, theta lives in the **vertical-Christoffel / second
  fundamental form slot**: `theta in Gamma(Sym^2 T*X4 (x) V)` with
  `V = S^2 T*X4` the vertical bundle of `Met(X4)` pulled back along the
  section — components `theta_{mu nu}{}^{ab}`, symmetric in `(mu,nu)`,
  valued in the metric-fiber directions. This is exactly the type of a
  connection DIFFERENCE on the section (the willmore reconciliation
  identified the algebraic-slice SFF as the genuine DeWitt vertical
  Christoffel `Gamma^{ab}_{mu nu}` — a distortion in the transcript's
  literal sense: the failure of the section's connection to match the
  gauge-transformed reference). The upstream `ad`-typing over Spin(9,5)
  remains reconstruction-grade; the weak-field symbol home above is what
  the computation uses and is convention-honest.
- **The slot that replaces `Lambda*g`.** Not theta itself: the vacuum term
  occupying the old `Lambda g_mn` slot is the **canonical quadratic stress
  bilinear of theta**, `S_mn = sigma * <theta_{m.}, theta_{n.}>_eta`
  (all internal slots contracted with eta). `Lambda g` was the
  metric-proportional degenerate case; the general S is not
  metric-proportional — which is precisely why C10 escapes the C3 kill.

## 2. The computation (all machine-checked, exit 0)

**The structural identity the probe rides on.** The gate's own residual
decomposes as `Q = t1 - t2` with `t1 = (1/2) hmean . bhat` and
`hmean_ab = box(h_ab)`. On a harmonic-gauge linearized-VACUUM background
`box(h) = 0` (PC1), so `t1 = 0` (PC2) and

```
Q^TF(B) = -[t2]^TF   exactly (PC4),
```

where `t2_mn = sum_p eta^pp <bhat_{mp}, bhat_{pn}>` is precisely the
canonical quadratic stress of a field locked to `bhat` with the identity
kernel. In words: **the Willmore-type residual IS (minus) the quadratic
stress of the second fundamental form** — so a vacuum field whose VEV locks
to the SFF is the canonical canceller. H-GR' predicted "a
fixed-point/backreaction identity, not a coincidence of coefficients"; the
computation confirms exactly that shape.

**Branch (a) curvature-locked anisotropic** — `theta_vac = kappa * bhat`:

- A1: trace-free `Q^TF`-slot component NONZERO at `O(M^2)`. **This answers
  the C10 first question: YES.**
- A2: stress is `O(M^2)` exactly — linear cheap-read clears preserved.
- A3: `Q^TF + sigma kappa^2 [t2]^TF = (sigma kappa^2 - 1)[t2]^TF`:
  EXACT cancellation at the single constant `sigma kappa^2 = 1`.
- A4: wrong orientation `sigma = -1` admits NO real kappa (residual factor
  `-(1+kappa^2)`) — **the cancellation sign is a hard Z/2 datum**, exactly
  the structure the four-leg swing hypothesized.
- A5: right orientation forces `kappa^2 = 1` — one frozen pure number.
- A6-A8: the SAME identity with the SAME frozen coefficient holds on the
  Kerr frame-dragging background (`box(h) = 0` there too). The identity is
  a property of the harmonic-gauge linearized-vacuum CLASS, not a
  Schwarzschild fit.

**Branch (b) homogeneous** — computed DEAD, both sub-cases: isotropic
homogeneous stress is metric-proportional (zero trace-free part — the
C10-image of the C3 kill, confirmed as prediction, not re-run as
resurrection; C3 stays `R0_FAIL` untouched); frozen-direction homogeneous
(`theta_m = v u_m`) has a nonzero trace-free part but a CONSTANT profile no
constant coefficient can match to the `M^2/r^6` residual (B3: off-diagonal
residual components have no stress partner at all).

**Branch (c) gradient-dominated** — computed DEAD: the natural harmonic
response `phi = M/r` gives stress falloff `M^2/r^4` vs the residual's
`M^2/r^6` (required coefficient `32/3` vs `32/15` across components — not
constant); the falloff-tuned `phi = M/r^2` is (i) NOT harmonic
(`box(phi) = 2M/r^4` — needs a source, violating vacuum support) and
(ii) still tensor-mismatched (required coefficient `24` vs `24/5`).

**Honesty on the branch-(a) result — why this is not a target-shaped
import, and what remains unearned.** The kill lemma warned that a tensor
shaped as `-Q^TF` is a target import "unless derived before target
confrontation." Three things distinguish this result from that trap, and
one thing does not:

1. The ansatz is the simplest equivariant linear response (identity kernel
   on `bhat`), not a componentwise fit; that its stress lands proportional
   to `Q^TF` is a computed consequence of `t1 = 0`, which is itself a
   structural fact of the harmonic-gauge linearized-vacuum class.
2. It is background-robust (Schwarzschild + Kerr-drag, same coefficient).
3. It makes falsifiable side-predictions (the sign gate A4; the kernel
   purity D1/D2; the t1-sector behavior on non-vacuum backgrounds — see
   Section 5).
4. BUT: `kappa^2 = 1` was solved FROM the cancellation demand, i.e., read
   off target-side. So the coefficient is NOT yet source-owned. The
   demonstrated content is existence + uniqueness + maximal sharpness of
   the demand: the adapter must deliver `sigma = +1` and `kappa^2 = 1`
   with source-side provenance, frozen before target use. Until then the
   grade ceiling is conditional (`R0_COND`-shaped), exactly as the
   standing axiom's working mode intends.

Other caveats, stated plainly: the stress bilinear form is the canonical
one, posited rather than derived from the unbuilt action (an action-level
demand, DEM-GR-3 below); the identity is established in the gate's frozen
convention (coordinate second-derivative `bhat`, harmonic gauge) and its
gauge/convention covariance is the sharpest open kill (K2 below); the
willmore reconciliation's principled-II convention gives the same `M/r^3`,
`M^2/r^6` orders, so the frames are consistent at order level, but the
OQ2-A convention binary still sits under everything.

## 3. The C2 scale law check

Recovered constraint (archaeology item 8): `C2(2xi)/C2(xi) = 2` exactly —
any compensator/source structure must reproduce this scale covariance.

Computed reading: the law is a **kernel-purity constraint**. A compensator
symbol built from a SCALE-FREE (constant) response kernel is exactly
homogeneous and reproduces the factor 2 (D1); a kernel carrying any
internal dimensionful parameter (toy: `kappa/(1 + L^2 |xi|^2)`) violates
the exact law (D2). Consequences for CH-GR:

- The curvature-locked branch (a) passes NATURALLY: its kernel is the
  identity with a pure-number coefficient — no internal scale to spoil the
  exact factor 2. A curvature-conditioned VEV response kernel of the
  branch-(a) type therefore scales correctly, and this is a real
  discriminator, not a formality: it FORBIDS massive/resonant response
  kernels (any `theta = K(box) bhat` with a mass scale in K is dead by the
  C2 law before any target computation).
- Dimensional bookkeeping of kappa (connection-difference vs curvature
  units) is convention-dependent and lands on the same OQ2-A/gimmel
  normalization datum as `c_W`; the C2 law pins the INVARIANT content:
  whatever the convention, the frozen coefficient must be a pure number in
  gimmel units. Recorded as part of DEM-GR-2, not silently assumed.

## 4. CH-GR parameter card (draft for card-freeze)

### (a) Sector construction parameters — GR inside GU-type geometry

| # | Parameter | Value / status | Provenance |
|---|---|---|---|
| G1 | Arena | `Y14 = Met(X4)`, physical section `g: X4 -> Y14`; weak-field symbol frame `eta + h`, harmonic gauge | frozen repo convention; gate script |
| G2 | Field content | distortion `theta in Gamma(Sym^2 T*X4 (x) S^2 T*X4)` (vertical-Christoffel/SFF slot); transcript-typed adjoint equivariance upstream | Section 1; transcript [00:22:26]+ |
| G3 | Vacuum law | curvature-locked VEV `theta_vac = kappa * bhat(B)` — H-GR' branch (a), the unique computed survivor | probe A1-A8, B1-B3, C1-C4 |
| G4 | Vacuum-term slot | canonical quadratic stress `S = sigma kappa^2 t2` replacing `Lambda g` | Section 1-2 |
| G5 | Cancellation identity | `Q^TF + S^TF = (sigma kappa^2 - 1)[t2]^TF = 0` on harmonic-gauge linearized vacuum | probe PC4/A3 |
| G6 | Coefficient | `kappa^2 = 1` (pure number; scale-free forced by C2 law) | probe A5, D1/D2 |
| G7 | Sign | `sigma = +1` in gate conventions; binary, no real-kappa escape if wrong | probe A4 |
| G8 | Cheap-read preservation | stress exactly `O(M^2)`; no linear theta-metric vacuum coupling permitted in the action | probe A2/PC5; K4 |
| G9 | Convention datum | OQ2-A functional binary + gimmel normalization (shared with `c_W`, `alpha_W`) | willmore reconciliation |

### (b) Adapter parameters — what must come through the boundary

Adapter demand ledger entries (typed, per the standing axiom rule 4; to be
routed to the interface-contract ledger by the parent):

- **DEM-GR-1 (Z/2 sign).** `sigma = +1`: the sign with which the theta
  stress enters the vacuum field equation — an action-level orientation of
  the Krein-indefinite fiber. Type: one global Z/2, loop-coherent,
  plausibly IDENTICAL to the bar-b Krein bit (H-QM/H-REC item 1 of the
  payload). The identification is a hypothesis with a named kill (K1), not
  computed here.
- **DEM-GR-2 (frozen pure number).** `kappa^2 = 1`, dimensionless in
  gimmel units, scale-free (C2 law), delivered with source-side provenance
  and frozen BEFORE target use. The value is now known; the PROVENANCE is
  the missing piece — this is the sharpest possible form of the demand.
- **DEM-GR-3 (action structure).** The source action must (i) produce the
  canonical stress bilinear as theta's stress form, (ii) make
  divergence-freeness Noether-forced via equivariance (transcript:
  "equivariance is what leads to divergence free" — same pattern as the
  B.2 `delta_2 . d_RS,-1 = 0` identity), (iii) contain no linear
  theta-metric coupling in the vacuum sector (K4), and (iv) respect the
  non-equivariant-compensator and cohomological-realization constraints
  recovered from the 2026-06-27 spec (B.3/B.4).
- **DEM-GR-4 (B.5 global objects, pass-through).** (i) families
  pushforward over `GL(4,R)/O(3,1)` — globalizes the vertical typing of G2
  beyond the symbol frame; (ii) the Y14-end boundary holonomy/spectral
  section — the natural HABITAT for DEM-GR-1's Z/2 (lineage:
  DEP-NATIVE-SOURCE-DATUM, now at p2c); (iii) the BV-to-boundary-Dirac
  map — ties theta's compensator sector to the C2 obstruction that the
  scale law constrains.
- **Branch selection: NO LONGER a payload item (proposed).** The four-leg
  swing budgeted "1 branch/sector selection" for CH-GR. Branches (b) and
  (c) are now computed dead; branch (a) is FORCED within the computed
  space. The adapter need not select the branch — it must only realize it.
  (Bounded honestly: forced within the three predeclared H-GR' families;
  a kernel-family exhaustion sweep beyond linear-local response is not
  claimed.)

## 5. Kill tests, sharpened

Killed-selector ledger respected: none of the eleven dead routes
(shiab=codifferential, gamma-trace, seesaw, folded-complex, PO1,
conditional-expectation, Kostant, observer-slice-as-index, record-issuance
=selector, ch2=24, C3 scalar-isotropic) were re-run. Branch (b1) is the
C10-image of the C3 kill, computed as a confirmation inside C10's own
branch list; C3's grade is untouched.

- **K1 — joint sign-consistency kill (CH-GR x CH-QM, decisive for the
  payload).** Once CH-QM's finite graded-quotient toy fixes the
  orientation convention for the bar-b bit, check whether the SAME
  orientation that yields the positive physical sector delivers
  `sigma = +1` in the GR slot. If the two are forced OPPOSITE, then either
  the H-REC one-orientation identification dies (N -> 5) or branch (a)
  dies. Executable as soon as the CH-QM toy exists; the GR side of the
  check is already frozen in the probe (A4/A5).
- **K2 — gauge/convention kill (the sharpest open threat to this result).**
  The identity `Q^TF = -[t2]^TF` was established in harmonic gauge with
  the gate's `bhat` convention. Mechanical spec for an hourly: (i) apply a
  pure-gauge shift `h -> h + d(xi)` with `xi` chosen so `box(h) != 0`
  (breaking harmonicity while fixing the same physical solution);
  (ii) recompute `t1, t2, Q^TF`; (iii) check whether the curvature-locked
  stress with the SAME `kappa^2 = 1` still cancels, or whether a
  gauge-covariant completion of the kernel exists (candidate: lock theta
  to the gauge-invariant linearized Riemann slot instead of raw `bhat`).
  If no gauge-covariant completion exists, the cancellation was a frame
  artifact and C10-GR closes honestly (given (b)/(c) already dead). This
  is the predeclared next computation.
- **K3 — scale kill (computed, standing).** Any source-side delivery of
  kappa carrying an internal dimensionful parameter is dead on arrival by
  the exact `C2(2xi)/C2(xi) = 2` law (probe D2). This kills
  massive/resonant response kernels as a class, before target use.
- **K4 — linear-slot kill.** Any candidate action with a linear
  theta-metric coupling in the vacuum sector injects an `O(M)` residual
  and breaks the Schwarzschild/Kerr linear cheap-read clears (probe
  A2/PC5 pin the quadratic purity). Symbol-level check on any proposed
  `S_IG`: reject if `delta S / delta g` contains a theta-linear vacuum
  term.
- **K5 — matter-background discriminator (new, prediction-shaped).** On
  NON-vacuum backgrounds `box(h) != 0`, the `t1` block switches on and the
  identity generalizes to `Q^TF = [t1 - t2]^TF` while the curvature-locked
  stress supplies only the `t2` part — so branch (a) PREDICTS a
  `t1`-shaped uncancelled remainder exactly where standard stress-energy
  occupies the slot. If a computation instead finds the vacuum
  cancellation persisting unmodified on matter backgrounds, the
  construction is cancelling too much (Einstein-dynamics-in-disguise
  territory) and fails the no-target-import discipline. This gives CH-GR
  a two-sided test, and hands CH-COSMO its opening move: on FLRW,
  `t1 != 0`, and the magnitude mode of the same VEV rides the `t1` sector
  — the response is NOT killed by branch (b)'s death because FLRW is not
  vacuum.

## 6. Proposed scorecard row (CH-GR) — for the scorecard owner; not applied here

- **Q1: PARTIAL -> YES (conditional).** A formalized construction now
  EXISTS and computes: C10 branch (a) in the weak-field symbol frame, with
  an exact cancellation identity, background-robust across the
  harmonic-gauge linearized-vacuum class. Gaps: gauge-covariance (K2),
  action-level derivation (DEM-GR-3), nonlinear/exact-background
  extension.
- **Q2: YES (stands, strengthened).** The requirement set is unchanged and
  now has a computed branch-space collapse (3 -> 1) plus a new
  kernel-purity boundary from the C2 law (K3) and a two-sided
  matter-background condition (K5).
- **Q3: PARTIAL -> YES (candidate freeze).** The adapter range for CH-GR
  is now concretely stated: one Z/2 sign (value known: `sigma = +1`), one
  frozen pure number (value known: `kappa^2 = 1`), the DEM-GR-3 action
  structure, and the B.5 pass-throughs. What is missing is not the RANGE
  but the source-side provenance — exactly the p2c instance question.
  Gaps: sigma-Krein identity unproven (K1), kernel-family exhaustion
  beyond linear-local response not swept, K2 pending.

## 7. What this does to the N <= 4 payload question

- The four-leg payload budgeted for CH-GR: "1 branch selection + 1 frozen
  coefficient (possibly Z/2-linked)." After this swing: the branch
  selection item is plausibly DELETED (forced by computation), and the
  Z/2-linkage of the sign is now a computed hard gate (A4) rather than a
  plausibility. CH-GR's net demand: the SHARED Z/2 (payload item 1) + one
  pure number whose value is already known.
- If K1 lands positive (one orientation serving Krein sign, cancellation
  sign, and arrow), the payload pressure moves from N <= 4 toward
  **N = 3** (orientation; absolute scale; subgroup datum) — with the
  caveat that the archaeology's J_quat question still decides whether
  generations force a fifth item. If K1 lands negative, N -> 5 pressure.
  K1 is therefore now decisive on BOTH ends and should ride in CH-QM's
  finite toy build as a required output, not an optional check.
- The empty-intersection ending remains live per the P0 pre-registration:
  K2 failing with no covariant completion would close C10-GR and return
  the GR track to C9-only, which is the honest falsification-shaped path.

## Persona pass (inline, three voices, condensed)

- *Differential geometer:* the honest typing is the vertical-Christoffel
  slot, and the t1/t2 split is the real content — the identity is a
  statement about harmonic-gauge linearized vacuum, so K2
  (gauge covariance) is not optional polish, it is the theorem/artifact
  boundary. Locking theta to the gauge-invariant curvature slot is the
  natural covariant completion candidate.
- *Condensed-matter theorist:* this is strain-locked order-parameter
  response — the condensate rides the background strain (curvature), the
  uniform condensate (branch b) carries no shear stress, and the sign gate
  is which Krein well the condensate sits in. The two-sided K5 test is the
  analog of checking the response vanishes where it must, not just fires
  where you want.
- *Numerical engineer:* the probe verifies `t1 = 0` rather than brute
  simplifying `t2` products, so it runs in seconds and extends cheaply;
  K2's gauge-shifted rerun is the same machinery with one extra `d(xi)`
  term and is mechanically executable by an hourly today.

## Boundary

Everything here is conditional construction under the standing axiom.
`claim_status_change: none`; no map/canon/scorecard file was edited; the
scorecard row in Section 6 and the payload-item deletion in Section 4b are
PROPOSALS for their owners. The branch-(a) result is weak-field,
convention-frozen, and coefficient-unprovenanced until a p2c instance
delivers DEM-GR-1/2 — the honest grade ceiling is conditional. Adapter
demands are recorded and work CONTINUED per the axiom; nothing here stops
on "needs the adapter."
