---
title: "Channel swing CH-COSMO: magnitude-mode projector attack, scale bracket, sign-as-orientation"
status: active_research
doc_type: exploration
created: 2026-07-19
directed_by: "Joe direct chat, 2026-07-19 (deep research swing on CH-COSMO)"
axiom: lab/process/boundary-adapter-standing-axiom.md
extends:
  - explorations/adapter-assumed-four-leg-swing-2026-07-19.md
  - explorations/five-leg-swing-2026-07-19.md
inputs:
  - lab/process/source-object-interface-contract.md
  - lab/process/integration-readiness-scorecard.md
  - lab/process/recovery-no-go-defense-register.json
  - explorations/assembly-archaeology-recovered-parameters-2026-07-19.md
  - explorations/transcript-reread-distortion-vacuum-field-2026-07-19.md
  - canon/theta-field-flrw-dark-energy-eos.md
  - explorations/wave46/H46C-theta-star-gu-cmb-calibration-2026-07-13.md
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md
  - explorations/W226-harden-de-tripwire-squeeze-data-2026-07-14.md
  - explorations/pred-norm-rank-2026-07-15.md
  - explorations/conformal-factor-mode-gauge-status-2026-07-11.md
scripts:
  - tests/channel-swings/ch_cosmo_magnitude_mode_probe.py
claim_status_change: none
---

# Channel swing CH-COSMO (2026-07-19)

CH-COSMO is the scorecard's weakest leg (Q1: NO — no physical scalar projector has
ever been exhibited; RECOVERY-NOGO-COSMO-SCALAR is a bounded no-go with a seven-item
missing list). This swing attacks Q1 directly under the standing axiom and H-COSMO
(the scalar channel is the magnitude mode of the C10 distortion VEV, H-GR'
curvature-conditioned), extracts the empirical bracket the frozen Lane 2 rows already
imply for the adapter's absolute-scale item, and works the sign question with no
inherited historical value (archaeology item 9: both prior signs came from the
hardcoded `d ln rho/dz = 3` vs `4.229` bug — the sign is OPEN).

Personas run inline in one context: GR perturbation theorist (Section 1), cosmologist
(Section 2), data analyst (frozen-row extraction, Sections 2-3). Receipt:
`tests/channel-swings/ch_cosmo_magnitude_mode_probe.py`, exit 0, 32/32 checks.

## 1. The Q1 attack: candidate projector and observable map, constructed

Setting (toy grade, sympy, FLRW cosmic time): `s*(theta)` modeled as a symmetric
rank-2 tensor; the FLRW-symmetric restriction of the H-GR' branch-(a)
curvature-locked VEV is the most general form the background symmetry allows,
`theta_bar_{mu nu} = alpha(t) u_mu u_nu + beta(t) h_{mu nu}` (u = cosmic time
direction, h = spatial metric). The magnitude is the fiber-Frobenius norm
`|theta|^2 = g^{ma} g^{nb} theta_{mn} theta_{ab} = alpha^2 + 3 beta^2` — GU-native in
type (the transcript's own Frobenius fiber metric), not a standard SVT variable.

### 1.1 The projector exists and its output is automatically scalar (A1)

The candidate projector is the Frobenius contraction with the VEV:

```
delta|theta| = <theta_bar, delta theta>_Frob / |theta_bar|
```

Computed: the output is `alpha * dtheta_00 + (beta/a^2) * tr(dtheta_ij)` — it contains
ONLY helicity-0 components. Every helicity +-1 (vector) and +-2 (tensor) component of
the fluctuation drops out of the projector identically, by the structure of the
FLRW-symmetric contraction. This is the first time the repo has an explicit candidate
for the no-go's "physical scalar projector" slot rather than a name.

### 1.2 Gauge status: exactly ONE slicing scalar survives (A2) — the key finding

The load-bearing subtlety: `|theta|^2` depends on the metric too, so the honest
perturbation of the magnitude must carry the metric fluctuation along with the theta
fluctuation. Doing that, the gauge shift of the full perturbed `|theta|^2_g` under an
arbitrary linearized diffeomorphism `xi = (T, grad S + V)` is EXACTLY

```
delta_gauge |theta|^2 = T * d|theta_bar|^2/dt
```

— verified symbolically. The spatial-scalar gauge `S` and the vector gauge `V` drop
identically. So delta|theta| is gauge-covariant as a scalar with a SINGLE residual
dependence: the time slicing. Consequences:

- A **uniform-|theta| slicing** (choose T to cancel the shift) exists wherever
  `d|theta_bar|/dt != 0` — which the H-GR' hypothesis supplies for free, since a
  curvature-conditioned VEV on FLRW evolves with the background. The degenerate
  frozen-VEV case (`|theta_bar|` exactly constant) is a named condition, not silently
  assumed.
- The adapter's boundary gauge-fixing demand for CH-COSMO is therefore ONE typed
  item: a single time-slicing scalar fixed at the boundary. Not a family of
  conditions — one datum. This goes to the adapter demand ledger.
- Equivalently a Bardeen-style gauge-invariant combination with one metric scalar can
  be formed; the slicing datum and the invariant combination are the same content in
  two presentations.

### 1.3 Residue discharge: which residues discharge structurally, which do not (A3, A4)

The no-go's missing list has seven items. This swing splits them into two classes:

**Discharge by representation theory (no C10 action needed).** At fixed wavevector k
the little group is SO(2); every component of any tensor fluctuation carries a pure
helicity phase `e^{i m phi}` (verified for all 10 rank-2 components), so an
FLRW-invariant quadratic action can only pair helicities summing to zero. Scalar-vector
and scalar-tensor cross terms are NOT invariant (exhibited explicitly) and cannot
appear. Hence: **the vector and tensor residues discharge from the scalar equation at
quadratic order for ANY FLRW-symmetric action** — Schur/superselection, not an import
of standard SVT dynamics (the forbidden shortcut is importing standard SVT variables
or equations as GU evidence; a symmetry theorem about arbitrary actions is neither).
Conditionality named: this holds iff C10's branch-(a) VEV admits an FLRW-symmetric
restriction at all — which waits on CH-GR.

**The honest surviving residue (C10-dependent).** The helicity-0 block is
multi-scalar: 4 theta-scalars + 4 metric-scalars at fixed k; the projector picks one
ray; gauge removes two directions; generically >= 1 dynamical orthogonal scalar (plus
constraints) remains. Representation theory CANNOT force its decoupling (same
helicity). The closed-scalar-truncation question therefore reduces to a
finite, named computation on the C10 action: (i) the scalar-block mixing
coefficients between the magnitude ray and the orthogonal scalars must vanish or be
constraint-eliminated, and (ii) the kinetic normalization `Z_theta > 0` must be
emitted. These are exactly two of the quantities the old packets named as
never-emitted (`scalar_theta_mode, Z_theta, C_Rtheta, xi_eff`).

**Net Q1 movement.** The no-go's seven-item missing list compresses to two
C10-dependent items plus one typed adapter demand:

| no-go missing item | status after this swing |
|---|---|
| physical scalar projector | candidate CONSTRUCTED (Frobenius/VEV contraction), toy grade |
| gauge-invariant observable map | gauge-covariant with ONE slicing residue; boundary-fixable (typed adapter demand) |
| vector residues | discharge by SO(2) superselection (conditional on FLRW-symmetric VEV) |
| tensor residues | same |
| gauge residues | reduced to the single slicing scalar |
| block-diagonal SVT quadratic action | scalar block still open: mixing coefficients (C10) |
| source/connection/boundary residues | inside the scalar block: same C10 computation + boundary datum |

This does not clear the no-go (nothing here is source-owned; the C10 action does not
exist), and no register state moves. It converts "no projector has ever been
exhibited" into "a projector candidate exists whose failure modes are two named
computations on C10."

### 1.4 Relation to W78 (conformal-mode scalar)

W78 proved GU's induced-|II|^2 gravity sector already carries a physical propagating
scalar (the R^2 scalaron, PHYSICAL not gauge, positive-norm tachyon at flat space).
That mode lives in the METRIC scalar block of Section 1.3's count — meaning the
scalar-block diagonalization must handle the scalaron-magnitude mixing too. This is a
sharpening, not a new obstacle: the same C10 mixing computation covers it, and a
magnitude/scalaron mixing angle would be a computable output, not an unknown unknown.

## 2. The empirical bracket for the adapter's absolute-scale item

Frozen rows only (H46C, DARK-ENERGY-05/06 + W129, W226); the Lane 2 DE-AMP audit is
NOT re-run. The adapter item splits into a two-sided TOTAL and a one-sided SPLIT:

**Total scale (two-sided, pinned).** The CMB-calibrated amplitude leg pins the total
DE density: `rho_DE^(1/4) ~ 2.2-2.3 meV`, i.e. `rho_DE ~ 7e-121 M_Pl_red^4 ~
1e-123 M_Pl^4` (the familiar 10^-122 +- 1 in Planck units, convention-dependent).
GU's OWN theta-star calibration (H46C: H0_GU = 63.75, amplitude +5.66% over Planck,
a +5.7 sigma_A internal tension at f0 > 0) shifts this by ~10% — invisible at bracket
resolution. **The adapter's absolute normalization is not free within many orders of
magnitude: it is empirically a point at ~(2.24 meV)^4, known to better than 10%.**

**Dynamical/constant split (one-sided).** The magnitude-mode fraction
`f0 = rho_B / rho_Lambda_eff` is bounded above, never below:

- canonical (M^2 = 8, BC_1): `f0 in [0, 0.027]` (3-sigma-equivalent, W129 band row);
- A_1 (M^2 = 7): `f0 in [0, 0.039]`;
- softest band point (S^3, M^2 = 3): `f0 in [0, 0.208]`;
- every DESI-signal-reproducing amplitude `f0_CPL` (0.17 / 0.23 / 1.63) is excluded
  band-wide at `dchi^2 >= +33.5`; every allowed point is an LCDM mimic
  (`|w0+1| < 0.1`).

In initial-amplitude terms (canon Result 2 mapping `f0 = 0.125 <-> B_i ~ 0.98 M_Pl`,
`f0 ~ B_i^2`): `B_i in [0, ~0.46 M_Pl]` canonical, `[0, ~1.26 M_Pl]` at the softest
band point.

**One-sided ceiling (W226, monitor).** F1 fires only if an admissible dataset excludes
`w_a/(w_0+1) > -3.5` at 2-sigma (forcing `B_i > 3 M_Pl`). Tightest current 2-sigma
least-negative edge: -2.39 (DESY5); live margin **+1.11**. Not fired; no floor exists.
The allowed bracket sits strictly inside the ceiling — the frozen rows are mutually
consistent.

**Reading for the interface contract.** The adapter's scale item is one number pinned
to ~(2.24 meV)^4 plus a split degree of freedom bracketed one-sidedly at <= 2.7%
(canonical). PRED-NORM-RANK stands: GU cannot fix this internally (rank-3 rescaling
freedom, invariant quotient dimension 4); the bracket is what the DATA hand the
adapter, not what GU derives.

## 3. The sign question: an indirect, relational orientation observable

No historical sign is inherited: both prior sign computations (the +1.17 and -1.80
ratio readings) traced to the hardcoded `d ln rho/dz = 3` (real 4.229) bug
(DARK-ENERGY-03); the current re-verified global-fit values are LCDM-amplitude-
degenerate. The data-facing sign is OPEN.

The sharp version of "the DE sign ties to the transmitted Z/2" (H-REC):

- In the two-component construction with STANDARD energy sign, `rho_B >= 0` forces
  `w_0 = -1 + 1.39 f0 >= -1`: the magnitude mode can only push to the quintessence
  side of w = -1. If the transmitted orientation flips the mode's effective energy
  sign (the same flip that selects the Krein physical sector), the flipped class
  pushes to the phantom side. Then **sgn(w_0 + 1) is an indirect orientation
  observable**.
- What a sign measurement WOULD tell — three conditions, all named: (i) `f0 != 0`
  (a detected deviation from w = -1; the LCDM limit is orientation-SILENT); (ii) a
  DERIVED, field-redefinition-stable co-variance between the orientation and the
  mode's energy sign (a C10-level task; without it a sign is just a coefficient);
  (iii) a second-sector reference (Krein sector or record arrow), because the Z/2 is
  relational — what the measurement reads is the RELATIVE orientation between the
  cosmological sector and the reference sector, i.e. it tests H-REC's co-flip
  consistency. That is exactly what an orientation observable can do, and a mismatch
  would kill the sign-link hypothesis (not the orientation itself).
- What it would NOT tell: no absolute orientation (there is no orientation-free
  standard of "which side is which"); no discrimination between "orientation" and an
  independent sign posit unless (ii) is derived; nothing at all if f0 = 0.
- Locality consistency (new, worth keeping): w(z) is a GLOBAL background observable.
  A cosmological sign read is a global read, so it does NOT contradict the
  local-unreadability of the topologically stored bit (H-QM/p2c storage) — it is the
  kind of access the storage mechanism permits. The DE sign is currently the only
  candidate GLOBAL READOUT CHANNEL for payload item 1 anywhere on the board.
- Flag for Lane 2 (per archaeology item 9): when the DE amplitude audit next runs,
  the sign of any detected deviation doubles as the orientation-consistency datum.

## 4. Draft CH-COSMO parameter card

Conditional under `A_boundary`; adopts DE-AMP-DIAGNOSTIC and DE-F1-TRIPWIRE as its
data-facing legs (five-leg swing) rather than duplicating them.

**Sector construction parameters (GU-internal; C10 must emit):**

1. Branch: H-GR' sub-branch (a) curvature-locked VEV, FLRW-symmetric restriction
   `theta_bar = alpha(t) u u + beta(t) h` (two background functions, not free:
   determined by the C10 response kernel given the background).
2. `M^2` (magnitude-mode mass, units H0^2): admissible set {3, 7, 8} (S^3/A_1/BC_1)
   + continuum threshold 20.25; canonical 8 at reconstruction grade; OQ2 open.
3. `Z_theta > 0` (kinetic normalization of the magnitude mode) — never emitted;
   required output.
4. Scalar-block mixing coefficients (magnitude ray vs orthogonal theta-scalars,
   metric scalars incl. the W78 scalaron, connection scalars): must vanish or be
   constraint-eliminated — THE closure computation.
5. `xi_eff` (non-minimal coupling): currently assumed 0; must be emitted or justified.
6. Phase `phi_0 ~ 50 deg` (numerically resolved, reconstruction grade).
   NOT parameters: `f0`, `B_i` — fits until derived; listing them as construction
   parameters would repeat the DE-04-era mistake.

**Adapter parameters (typed demands, to the demand ledger):**

- A1. Absolute normalization scale (shared payload item 3): pinned
  `~(2.24 meV)^4 ~ 1e-123 M_Pl^4` (two-sided, <10%); split freedom
  `f0 in [0, 0.027]` canonical (band: to 0.208), one-sided.
- A2. Boundary gauge-fixing: ONE time-slicing scalar at the boundary
  (uniform-|theta| slicing; valid where `d|theta_bar|/dt != 0`; frozen-VEV
  degenerate case needs a fallback datum — named condition).
- A3. Sign linkage (shared payload item 1, the Z/2): enters ONLY if the
  energy-sign co-variance is derived from C10; no historical sign value inherited.

**Kills (pre-registered):**

- K1. If C10's FLRW restriction forces `alpha = -beta * (metric proportion)` (VEV
  metric-proportional), the magnitude mode is pure trace and dies C3-style.
- K2. If no C10 coupling choice discharges the scalar-block mixing (or `Z_theta <= 0`
  for all branches), H-COSMO fails independent of H-GR (the four-leg swing's
  pre-registered ending).
- K3. F1 fires (2-sigma edge below -3.5): amplitude ceiling breached, `B_i > 3 M_Pl`
  unphysical — construction-level kill via the existing tripwire.
- K4. Sign-link kill: with f0 != 0 detected AND co-variance derived, a measured
  sgn(w_0+1) inconsistent with the reference sector's orientation kills the
  H-REC sign identification for this channel.

## 5. Proposed scorecard row (proposal only; the scorecard file is not edited here)

- **Q1: NO -> PARTIAL (proposed).** A candidate projector is now CONSTRUCTED (toy
  grade, receipt): fiber-Frobenius contraction with the VEV, output automatically
  helicity-0; gauge residue is exactly one slicing scalar (boundary-fixable, typed
  adapter demand); vector/tensor residues discharge representation-theoretically for
  ANY FLRW-symmetric action. Not YES: no C10 action exists; the surviving residue
  (multi-scalar helicity-0 mixing + Z_theta) is C10-dependent; nothing is
  source-owned. Still derivative of CH-GR, but no longer empty-handed.
- **Q2: PARTIAL (strengthened).** Construction-side boundaries now itemized:
  `Z_theta > 0`; scalar-block mixing discharge; `d|theta_bar|/dt != 0`
  (slicing nondegeneracy); FLRW-compatibility of branch (a); scalaron-magnitude
  mixing handled in the same computation.
- **Q3: PARTIAL -> strong PARTIAL.** The scale item now has an actual bracket:
  total pinned ~(2.24 meV)^4 (two-sided, <10%); split one-sided f0 <= 0.027
  canonical; F1 margin +1.11. Remaining Q3 gap: whether the adapter transmits the
  split (f0) or only the total, and the A2 slicing datum's exact type.
- **Gaps to card-freeze (unchanged critical path):** C10 formalization (CH-GR);
  then the scalar-block mixing + Z_theta computation (Section 1.3) is the single
  decisive CH-COSMO calculation; sign co-variance derivation rides on the same
  formalization.

## Boundary

All conditional constructions under the standing axiom, toy grade where computed.
The no-go register entry RECOVERY-NOGO-COSMO-SCALAR is not cleared, reopened, or
edited; the scorecard row change is a PROPOSAL recorded here, not applied. No claim
status, canon verdict, or public posture moves. Frozen data rows are cited, not
re-audited (Lane 2 owns the audit). Receipt:
`tests/channel-swings/ch_cosmo_magnitude_mode_probe.py` (sympy, deterministic,
exit 0, 32/32).
