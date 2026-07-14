---
title: "Track 2 (H47 declare-and-build) -- the conditional theory GU-given-S: declared postulates and its NUMBERS (graviton sector + raw dark-energy curves + one-page ledger)"
artifact_type: exploration
status: exploration
created: 2026-07-13
track: 2
depends_on:
  - "tests/track2/T2A_graviton_sector_numbers.py"
  - "tests/track2/T2B_dark_energy_curves.py"
  - "explorations/two-track-persona-sweep-2026-07-11/SYNTHESIS.md"
  - "explorations/wave7/H25-II-first-variation-2026-07-11.md"
  - "explorations/wave10/H27-soldering-palatini-2026-07-11.md"
  - "explorations/wave22/H10-ppn-weak-field-2026-07-11.md"
  - "explorations/wave30/H50-mudw-de-scale-prediction-2026-07-11.md"
  - "explorations/wave31/H51-dewitt-coefficient-cL-2026-07-11.md"
  - "explorations/wave18/H34-predictive-content-audit-2026-07-11.md"
  - "explorations/wave20/H43-de-shape-falsifier-2026-07-11.md"
  - "explorations/wave25/H44-de-backreacted-background-2026-07-11.md"
  - "GEOMETER-VS-PHYSICS-OBJECTS.md"
verdict: >
  BUILT (conditional-theorem form throughout). The Track-2 declare-and-build move is executed:
  the honest leans are DECLARED as stated postulates S = {S1..S7} and the resulting conditional
  theory's numbers are emitted, tests exit 0. Graviton sector (given S): alpha = 1/3 fixed,
  lambda(mu_DW) = hbar c / (sqrt(m2_eff) mu_DW) with m2_eff in [5/6, 5/4]; gamma - 1 =
  -(2/3) e^{-m2 r}; the H36 point (mu_DW = DE scale) is ALREADY FALSIFIED (lambda in
  [60.0, 73.6] um excluded at alpha = 1/3), so the conditional theory does NOT adopt H36; the
  allowed window is mu_DW >= ~3.4-4.8 meV (argued sub-mm edge; boundary not digitized) with no
  experimental upper edge; inside the window GU-given-S predicts EXACT GR at LIGO (massless pole
  exactly massless; massive companion 9+ orders above the excitable band). Dark energy (given S):
  the CPL (w0,wa) comparison is falsified up front (H43/H44); the raw non-CPL w(z) and H(z)
  curves at declared shape M^2 = 8 H0^2 with free amplitude f0 are tabulated over z in [0,2]
  (DESI full-likelihood is Team 2's parallel deliverable, not duplicated). Strict H34 counting:
  free parameters remain {f0, M2(band-declared), B_i, mu_DW}; zero unconditional predictions are
  claimed; every emitted number is labeled PREDICTION-given-S / FIT / BOUND. Nothing in this
  document asserts S; "X given S" is a prediction of GU-given-S, never of GU. No canon change.
---

# Track 2 -- the conditional theory GU-given-S and its numbers

**Firewall (binding, repo-ratified; two-track SYNTHESIS sec 6).** Everything below is a
conditional theorem. It never asserts its antecedent. "X given S" is a prediction of
**GU-given-S**, not of GU. This branch reports up to the unconditional Track-1 posture and does
not change it. Any quotation of a number from this page without the given-S clause is a
misquotation.

**Priority correction honored (SYNTHESIS sec 5/7).** The generation count is NOT built here: it
is decoupled from the physics legs, source-action-gated, and likely under-determined even under
a declared carrier (the worst first deliverable). The first deliverables are the
graviton-sector numbers and the raw-H(z) dark-energy curve.

Reproduction: `python -u tests/track2/T2A_graviton_sector_numbers.py` (exit 0, 8/8) and
`python -u tests/track2/T2B_dark_energy_curves.py` (exit 0, 4/4).

---

## 1. The declared postulate set S (stated, never asserted)

Each postulate is an honest lean elsewhere graded in the repo; here it is DECLARED. The
construction column follows the GEOMETER-VS-PHYSICS-OBJECTS discipline (identify which
construction, and why).

| # | Postulate (declared) | Construction used | Repo status of the lean |
|---|---|---|---|
| S1 | Ambient signature (9,5); the 5 times force the indefinite Krein form, not a Hilbert space | program-native (Branch 5) | settled-native fork (do not kill for multi-time) |
| S2 | Gravity functional = the full norm `|II|^2` of the embedding X^4 -> Y^14 (Gauss: `|II|^2 = |H|^2 - R^X`; EH induced, not added); the OQ2-A functional choice is hereby declared | program-native (induced, not added) | H15/H49 structural lean; pure `|H|^2` dies on rotation curves |
| S3 | Soldering: `A = spin-lift(grad^gimmel)`; theta pinned to the second-fundamental-form locus | program-native projector | H27: **genuine postulate, NOT dynamically forced** (Palatini test; codim 8165) |
| S4 | `mu_DW` is a free dimensionful scale (the gimmel geometry fixes ratios only) | program-native (ratio-only, H24) | structurally free; NOT identified with the DE scale (H36 is refused, sec 3) |
| S5 | Carrier B: the gamma-trace-constrained (causal) RS field space is the source-action field-space declaration | program-native (H40) | declared for completeness of S; **exercised nowhere in this page's numbers** (count decoupled) |
| S6 | Geometric posture: Krein keep-and-grade ghost clearance `[P,S]=0` at tree level; `Sp(32,32;H)`; two metrics (base + gimmel fiber) | program-native (table rows 1-3, 8) | settled-native forks; loop-level `[P,S]=0` stays OPEN and is NOT declared |
| S7 | DE sector: DE = constant DeWitt-Lambda + KG theta field with shape `M^2 = 8 H0^2` (BC_1 ground eigenvalue on GL(4,R)/O(3,1), reconstruction-grade), slow-roll IC at z = 30; amplitude `f0` free | program-native eigenvalue (RC3) | reconstruction-grade (F6 Iwasawa check open); H43 scanned the whole band, verdict insensitive |

Explicitly NOT declared: H36 (`mu_DW` = DE scale) -- already falsified (sec 3); loop-level
`[P,S]=0` -- open; any digitized alpha = 1/3 exclusion boundary -- would be invented.

## 2. Persona pass 1 -- effective-field theorist: the conditional Lagrangian, cited

Given S1-S6, the assembled spin-2 sector, every ingredient repo-established:

```
S_grav[given S]  ~  mu_DW^2 R^X  +  Weyl^2  +  c_L mu_DW^4         (no R^2 term)
TT operator:  box(box + m2^2),   m2^2 = m2_eff mu_DW^2,   m2_eff = 1/2 + C_RY in [5/6, 5/4]
```

- `|II|^2 = |H|^2 - R^X`, induced EH, Stelle-type `R + Weyl^2`: H15 (wave 3), S2.
- `C_RY > 0` computed two independent ways; `m2_eff in [5/6, 5/4]`: H25 (wave 7).
- No `R^2` term -> the scalar mode decouples (`m0 -> infinity`): H10 (wave 22).
- DeWitt Lambda = background density `c_L mu_DW^4`, `c_L = 3/8` exact; TT `s^0` coefficient = 0
  exactly (massless pole exactly massless): H51 (wave 31).
- Tree-level Krein clearance `[P,S]=0`: H23/canon ghost-parity synthesis, S6.
- Conditionality: the whole assembly stands on S3 (H27: the soldering is a genuine postulate).

Given S7, the DE sector: `w_DE = (-1 + f w_theta)/(1 + f)`, `f = rho_theta/rho_L`, KG theta on
the self-consistently backreacted FLRW background (H44 solver).

**Gaps flagged, not invented** (inventing is out of scope): (g1) the matter coupling of the
massive spin-2 beyond the linearized Stelle 1978 solution (H10 imports `Phi, Psi` and
cross-checks the vDVZ endpoint; a from-scratch GU linearization with sources does not exist);
(g2) loop-level `[P,S]=0` (unitarity beyond tree; generic-Stelle-shared); (g3) the O(1)
background-vs-TT normalization band of `c_L` (`[3/8, 2]`, H51 limit 4); (g4) the `m2_eff`
method band `[5/6, 5/4]` (normalization-gated, H25); (g5) a GU derivation of `B_i` and the
absolute `mu_DW` (the source-action bottleneck, untouched); (g6) realistic GW source modeling
for the massive companion (bounded instead via the excitability threshold).

## 3. Persona pass 2 -- phenomenologist: the numbers (all "given S")

All computed in `tests/track2/T2A_graviton_sector_numbers.py`; published bounds comparison-only.

**Yukawa correction** (strength FIXED, range a function of the free scale):

```
V(r) = -(GM/r) [1 + (1/3) e^{-r/lambda}],   alpha = 1/3 (vDVZ trace factor, not tunable)
lambda(mu_DW) = hbar c / (sqrt(m2_eff) mu_DW),  m2_eff in [5/6, 5/4]
  mu_DW = 2.3 meV  -> lambda in [76.7, 94.0] um     (the H36 point, c_L = 1)
  mu_DW = 2.94 meV -> lambda in [60.0, 73.6] um     (H36 with computed c_L = 3/8) -- EXCLUDED
  mu_DW = 1 eV     -> lambda in [0.18, 0.22] um
  mu_DW = M_Pl     -> lambda ~ 1.5e-35 m            (natural H24 default; unobservable)
```

**PPN profile and Cassini:** `gamma(r) - 1 = -(2/3) e^{-m2 r}` (H10; endpoints vDVZ 1/2 and GR
1 cross-checked there). Cassini `|gamma - 1| < 2.3e-5` gives `m2 r > 10.27`, i.e.
`mu_DW > 1.5e-17 eV` (1 AU) or `> 2.0e-15 eV` (1.6 R_sun). Reproduces H10; NOT binding.

**Sub-mm (the binding channel):** the H36 identification predicts `alpha = 1/3` at
`lambda in [60.0, 73.6] um`, which sits above the argued alpha = 1/3 exclusion boundary
(~45-52 um; Lee 2020 / Tan 2020 / Kapner 2007, boundary argued not digitized): **falsified**
(H50/H51, margin O(1)). Therefore the conditional theory keeps `mu_DW` free (S4) and the

**allowed mu_DW window** is:

```
mu_DW  >=  ~3.4 meV (weakest defensible corner: boundary 52 um, m2_eff = 5/4)
           to ~4.8 meV (strictest corner: boundary 45 um, m2_eff = 5/6)
no experimental upper edge (EFT validity only, up to ~M_Pl; the natural M_Pl default
sits ~30 orders inside the window)
```

Honest spread note: H50 quoted an argued floor of ~3.0-3.6 meV; the T2A recomputation from the
same boundary band and the same formula gives 3.4-4.8 meV. Both are ARGUED-grade until the
alpha = 1/3 curve is digitized (the named H51 residual); the discrepancy is inside the
un-digitized-boundary uncertainty and is reported, not smoothed over.

Ladder caveat (ARGUED, named as such): "the floor is the ONLY open edge" uses the standard
fifth-force compilations (torsion-balance through planetary/PPN ranges all bound
`|alpha| << 1/3` for lambda above ~50 um). The mm-to-0.1-AU segment is cited from standard
compilations, not digitized in-repo; the Cassini segment IS computed here.

**GW channel (LIGO):** given S, the massless pole is EXACTLY massless (H51: TT `s^0 = 0`
exactly) -> luminal tensor modes, zero dispersion, two polarizations. The massive spin-2
companion is radiated only if `omega > m2`, i.e. `mu_DW < 9.3e-12 eV` (f <= 2048 Hz) -- nine
orders below the allowed window floor. So **GU-given-S predicts exact GR radiation at LIGO**;
a confirmed GW dispersion, extra polarization, or non-luminal tensor speed falsifies
GU-given-S. LIGO's graviton-mass bound (~1.3e-23 eV, GWTC-3) binds the massless pole, which is
exactly massless: satisfied identically, no new `mu_DW` constraint from this channel.

**Dark energy (given S7; T2B):** stated up front: the CPL `(w0,wa)` comparison is FALSIFIED
(H43: 3.20 sigma global closest on fixed LCDM; H44: 3.22 sigma fully backreacted; every rescue
route spent). The surviving object is the RAW non-CPL expansion history (mimics DESI-CPL
distances to ~1%, canon DARK-ENERGY-03; distance-model scope only). T2B tabulates, on the
self-consistent backreacted background at declared `M^2 = 8 H0^2`:

| z | w_DE (f0=0.05) | w_DE (f0=0.125) | w_DE (f0=0.5) | H/H0 (f0=0.125) | H/H_LCDM - 1 (f0=0.125) |
|---|---|---|---|---|---|
| 0.00 | -0.935 | -0.853 | -0.595 | 1.000 | +0.00% |
| 0.25 | -0.919 | -0.833 | -0.640 | 1.174 | +2.97% |
| 0.50 | -0.925 | -0.855 | -0.722 | 1.377 | +4.13% |
| 0.75 | -0.938 | -0.884 | -0.790 | 1.604 | +4.12% |
| 1.00 | -0.952 | -0.910 | -0.841 | 1.855 | +3.63% |
| 1.25 | -0.962 | -0.930 | -0.879 | 2.130 | +3.03% |
| 1.50 | -0.970 | -0.946 | -0.907 | 2.427 | +2.48% |
| 1.75 | -0.977 | -0.958 | -0.927 | 2.744 | +2.02% |
| 2.00 | -0.981 | -0.966 | -0.942 | 3.081 | +1.64% |

Shape (given S, any f0 > 0): non-CPL, shallow peak near z ~ 0.25, `w -> -1` at high z; exact
LCDM as f0 -> 0. `f0` is a FIT. The DESI DR2 BAO full-likelihood confrontation of these curves
is Team 2's parallel deliverable; this page deliberately emits the curves and stops.

## 4. Persona pass 3 -- computational engineer: tests and independent routes

- `tests/track2/T2A_graviton_sector_numbers.py` -- exit 0, 8/8 PASS. Independent routes:
  hbar*c from two constant sets (rel 3e-10); lambda conversion two unit paths; Cassini
  threshold closed-form vs bisection (agree to 1e-9); reproduction asserts against H50
  ([76.74, 93.98] um), H51 ([60.0, 73.6] um), H10 (1.4e-17 / 1.5e-17 eV).
- `tests/track2/T2B_dark_energy_curves.py` -- exit 0, 4/4 PASS. Solver core reproduced from
  H44 (attributed); guards: f0 -> 0 reduces to LCDM (3.5e-6); canonical (w0,wa) reproduces H44
  to 1e-4; **independent integrator** (adaptive Radau vs fixed-step RK4) agrees on w(z) to
  1.7e-8; canonical w(z) samples reproduce H44 Q1 to < 5e-3.

## 5. Persona pass 4 -- hostile referee: fit-in-disguise audit (H34 strict count)

Free parameters of the conditional theory (unchanged from H34): **f0, M2, B_i, mu_DW**.
Declaring S does not reduce the count; it converts leans into named antecedents. Strict labels:

- `alpha = 1/3`: PREDICTION-given-S (no knob; the vDVZ trace structure of the S2/S3 operator).
- `lambda(mu_DW)`, `m2(mu_DW)`: neither -- a one-parameter FAMILY (mu_DW free). Any specific
  lambda quoted as "the prediction" would be a fit in disguise; refused.
- `gamma - 1 = -(2/3) e^{-m2 r}`: PREDICTION-given-S as a profile SHAPE (the -2/3 coefficient
  and single-Yukawa form are knob-free); the deviation MAGNITUDE at given r rides mu_DW.
- `mu_DW >= ~3.4-4.8 meV`: BOUND (data-derived, argued edge).
- H36 lambda in [60.0, 73.6] um: was the one genuine parameter-linked prediction; FALSIFIED.
  Refusing to re-declare H36 after its falsification is exactly what keeps this page from
  being a fit in disguise.
- Exact GR at LIGO: PREDICTION-given-S (window-conditional but knob-free inside the window).
- w(z), H(z) tables: FIT-family (f0 free). The knob-free residue is the SHAPE class
  (non-CPL, shallow-peak, w -> -1 damping) at declared M^2; its CPL projection is already
  falsified, honestly displayed in the same breath.
- Unconditional predictions of GU (not GU-given-S) emitted here: **zero** (H34 stands).

## 6. Persona pass 5 -- honesty/firewall auditor

Checked: (i) every numbered claim in secs 2-3 carries the given-S clause or a
FIT/BOUND label; (ii) the verdict block states the conditional form and the non-assertion of S;
(iii) the falsifications (H36 sub-mm; CPL shape) are stated up front, in the same sections as
the surviving numbers, not appendixed; (iv) S5 (carrier B) is declared but flagged as exercised
nowhere here, so no count claim can be laundered through this page; (v) the un-digitized
alpha = 1/3 boundary and the fifth-force-ladder segment are named ARGUED, and the H50-vs-T2A
floor discrepancy is displayed rather than harmonized; (vi) quoting any line as "GU predicts X"
fails, because every X is bound to S in the sentence that carries the number. PASS.

## 7. The one-page conditional-theory ledger

| # | Number / curve | Value (given S) | Label | Experiment that touches it | Current bound / status |
|---|---|---|---|---|---|
| 1 | Yukawa strength alpha | 1/3 exactly | PREDICTION-given-S | any Yukawa search that reaches the range | tested jointly with lambda (rows 2-3) |
| 2 | Yukawa range lambda | hbar c/(sqrt(m2_eff) mu_DW), m2_eff in [5/6,5/4] | family (mu_DW free) | Eot-Wash / HUST sub-mm | alpha=1/3 excluded for lambda >~ 45-52 um (argued edge) |
| 3 | H36 point: lambda at mu_DW = DE scale | [60.0, 73.6] um (c_L = 3/8) | FALSIFIED (was PREDICTION-given-S+H36) | Lee 2020, Tan 2020, Kapner 2007 | excluded at alpha = 1/3, margin O(1) |
| 4 | Allowed mu_DW window | >= ~3.4-4.8 meV; no upper edge | BOUND | sub-mm (binding), Cassini (weaker by ~14 orders) | Cassini floor 1.5e-17 eV; sub-mm floor meV-scale |
| 5 | PPN profile | gamma-1 = -(2/3) e^{-m2 r} | PREDICTION-given-S (shape) | Cassini conjunction | \|gamma-1\| < 2.3e-5 -> m2 r > 10.27 |
| 6 | Ghost mass m2 | sqrt(m2_eff) mu_DW; Planckian at natural mu_DW | family (mu_DW free) | none directly (decoupled if heavy) | -- |
| 7 | GW dispersion / extra polarizations at LIGO | NONE (exact GR) inside the window | PREDICTION-given-S | LIGO/Virgo/KAGRA | massless-pole mass bound 1.3e-23 eV satisfied identically; excitable region 9 orders below window |
| 8 | DeWitt vacuum density | c_L mu_DW^4, c_L = 3/8 (band [3/8, 2]) | family (mu_DW free) | cosmology only via H36-type identification (refused) | -- |
| 9 | w(z), z in [0,2] | sec 3 table; non-CPL, shallow peak z~0.25, -> -1 | FIT-family (f0 free; shape given S7) | DESI DR2 BAO (raw distances) | CPL projection FALSIFIED (H43/H44); raw H(z) within ~1% of DESI-CPL distances; full likelihood = Team 2 |
| 10 | H(z)/H0, z in [0,2] | sec 3 table; +O(f0)% above LCDM at mid-z | FIT-family (f0 free) | DESI DR2 BAO / CMB | same scope as row 9 |
| 11 | Generation count | NOT EMITTED | -- (decoupled, gated, under-determined) | -- | deliberately excluded per priority correction |

**What would kill this conditional theory (one sentence).** GU-given-S dies if any of: an
alpha ~ 1/3 Yukawa is POSITIVELY detected at a range inconsistent with a single mu_DW that
also satisfies every other channel, LIGO confirms tensor dispersion / extra polarizations /
non-luminal speed, the raw-H(z) DESI DR2 full likelihood (Team 2) rejects the f0-family at the
distance level, or loop-level `[P,S]=0` fails (Krein clearance breaks beyond tree) -- and
independently of data, a forced build landing theta off the spin-lift locus falsifies S3 and
collapses the antecedent itself.

---

*Filed 2026-07-13. Track 2 branch deliverable; exploration-grade; no canon change; reports up
to Track 1. Reproducible: `python -u tests/track2/T2A_graviton_sector_numbers.py` (exit 0) and
`python -u tests/track2/T2B_dark_energy_curves.py` (exit 0). Five personas run inline in one
session (EFT assembler, phenomenologist, computational engineer, hostile referee,
honesty/firewall auditor). The count is not built here by design.*
