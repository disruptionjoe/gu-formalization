---
title: "W135: the issuance-structure taxonomy and the measured rate. If dark energy is energy issued into the geometry from outside (source action as transducer), which issuance schedules are physically distinct, what rho_DE(a) / w(z) does each imply, which survive the repo's verified BAO + theta_star machinery, and what is the measured rate for the survivors?"
status: exploration
grade: exploration (hypothesis generation first, kills second; every verdict computed, nothing promoted)
date: 2026-07-14
test: tests/W135_issuance_structure_taxonomy.py (34 checks, exit 0)
depends_on:
  - tests/wave46/H46C_theta_star_cmb_calibration.py (theta_star calibration, imported verbatim)
  - tests/wave29/H46_de_raw_bao_likelihood.py (raw DESI DR2 BAO likelihood, imported verbatim)
  - explorations/W129-oq2-m2-band-sweep-de-exclusion-2026-07-14.md (LCDM-mimic band verdict, binding)
binding_constraints:
  - "B2 rate-identity FALSE: no coupling-rate identity asserted (path4 adversary + thread B)"
  - "H36 mu_DW identification FALSIFIED (H50/H52): rho = c_L mu_DW^4 never used to pin the rate"
  - "W129: everything the band allows is an LCDM mimic, |w0 + 1| < ~0.1"
---

# W135: the issuance-structure taxonomy and the measured rate

## 0. Posture and scope

This wave PROPOSES structures first, then kills rigorously. The working idea, held at
exploration grade throughout: dark energy is the visible signature of energy issued
into the geometry from outside, with the GU source action as the transducer. Different
issuance schedules give different cosmologies; each schedule is written as an explicit
source term, scored on the repository's verified data machinery, and either killed or
bounded. Nothing here is asserted as a GU prediction. The falsified priors are binding:
no coupling-rate identity (B2 FALSE), no mu_DW-scale pinning (H36 FALSIFIED), and the
W129 verdict that every band-allowed amplitude is an LCDM mimic is used as a
cross-check on the kill criterion, not re-litigated.

Tri-repo note. The issuance CONCEPT is native to the temporal-issuance repository;
this repository (GU formalization) owns the boundary and source-term mathematics that
would have to realize any surviving schedule (the object the source action must
supply is computed below for every structure). Identity claims across the repositories
remain gated; nothing in this page asserts that any temporal-issuance quantity IS a GU
quantity.

## 1. The two accounting conventions (the theorist's first result)

Everything downstream depends on stating what "issuance rate" means. There are two
inequivalent readings, and the null structure separates them.

Convention A (covariant source). Issuance is the source term Q in the sourced
continuity equation

    rho' + 3 H (1 + w) rho = Q        (rho' = d rho / dt)

for a vacuum-like carrier (w = -1), so rho' = Q exactly. Covariantly this is
nabla_mu T_DE^{mu nu} = Q u^nu. Q is precisely the object the source action must
supply, and the Bianchi identity makes it expensive: nabla_mu G^{mu nu} = 0 forces the
TOTAL stress tensor to be conserved, so a nonzero Q requires a compensating current
(an interacting-dark-sector transfer, a unimodular-gravity integration function with
d Lambda / dt tied to Q, or a genuinely external flux, which is where the transducer
reading lives). In exact FLRW the only tensor structure available is Q^nu = Q u^nu in
the comoving frame; any spatial component breaks isotropy, and derivative couplings
(momentum transfer) act on perturbations, which this page does not model. That is the
tensor-structure statement: at background level the source action must supply exactly
one scalar function Q(t), no more freedom exists.

Convention B (bookkeeping). Issuance is dE_c/dt where E_c = rho a^3 is the dark
energy in a comoving volume. For a w = -1 fluid dE_c/dt = 3 H rho a^3 even when
Q = 0: the growth is pressure work (p = -rho).

The separator: the cosmological constant (structure (a)) has Q = 0 identically. Its
Convention-B "rate" is pure pressure work. So only deviations from w = -1 evidence a
genuine Convention-A issuance, and W129 already bounds those deviations to
|w0 + 1| < ~0.1 on the admissible band. Both rates are reported in Section 4.

## 2. The taxonomy: schedules, exact signatures, source terms

Each structure below is defined by its schedule, solved exactly (closed form where it
exists, self-consistent fixed-point otherwise), and written as the source term Q the
source action would have to supply. w_eff(a) = -1 - (1/3) d ln rho / d ln a
throughout.

### (a) Fixed per comoving volume (the null structure)

rho = rho_L = const; dE_c/dt = 3 H rho_L a^3, proportional to d(a^3)/dt. w = -1
exactly; Q = 0 identically (verified numerically to < 1e-8). The unique schedule that
holds the density fixed: any schedule not locked to the volume growth rate CANNOT hold
w = -1 over a finite interval (this is why every other structure below has a
signature). A constant comoving stock (zero issuance, S = 0) is exactly dust.

### (b1) Fixed per time, per comoving volume (Bitcoin-like drip from zero)

d(rho a^3)/dt = S = const for t >= t_i, zero stock at t_i.

    rho(a) = S (t - t_i) / a^3
    w(a)   = -S / (3 H rho a^3)          (exact)
    Q(a)   = S / a^3 - 3 H rho

Mimic condition: w = -1 today needs S = 3 H0 rho_L, i.e. t0 - t_i = 1/(3 H0), a
turn-on at z_i ~ 0.3. But then there is no dark energy at z > 0.3 and the distances
fail; with an early turn-on the ramp w -> -1/(3 H t) ~ -1/2 in the matter era fails
instead. The window is squeezed from both sides.

### (b2-pure) Fixed per time, per proper volume, from zero stock

rho' = Q = s = const, rho(t_i) = 0, so rho = s (t - t_i) and

    |w0 + 1| = 1 / (3 H0 (t0 - t_i)) >= 1 / (3 H0 t0) ~ 0.35   for ANY start time.

A parameter-free phantom floor: the structure cannot enter the W129 mimic band at all.

### (b2) Fixed per time, per proper volume, stock plus drip (THE RATE STRUCTURE)

rho(t) = rho_0 - s (t0 - t) (clipped at zero in the far past); one parameter, the
rate s itself. w = -1 - s / (3 H rho): phantom side for s > 0 (issuance), thawing
side for s < 0 (withdrawal). Q = s exactly. The s -> 0 limit is the null structure.
This is the structure that turns the data into a two-sided measurement of the
covariant rate.

### (c1) Holographic, Hubble cutoff: rho = C H^2

Self-consistency forces rho_DE / rho_m = const: w_eff = 0 exactly, no acceleration
ever (the Hsu structure). Structurally dead before any fit.

### (c2) Issuance per horizon-area change, integrated: rho = C~ H

Energy per Hubble volume proportional to horizon area gives rho proportional to H.
Zero free parameters after flatness: E = [C~ + sqrt(C~^2 + 4 (Om a^-3 + Or(a^-4 - 1)))]/2
with C~ = 1 - Om. Q = C~ dH/dt = -(3/2) C~ H^2 (1 + w_tot) < 0: despite the name,
this "issuance" structure is a WITHDRAWAL (the horizon area change is negative-definite
in dH). Late-time de Sitter attractor E -> C~, but the approach is slow.

### (c3) Holographic, future event horizon (Li): rho = 3 c^2 M_p^2 / R_h^2

dOm_de/dx = Om_de (1 - Om_de)(1 + 2 sqrt(Om_de)/c); w = -1/3 - (2/3) sqrt(Om_de)/c.
One parameter c; w0 = -1 needs c ~ 0.83.

### (d) Halving / stepped schedules

dE_c/dt = S_0 2^{-floor((t - t_i)/Dt)} for t >= t_i. E_c piecewise linear in t; w(z)
has kinks at each halving; total issued converges to 2 S_0 Dt, after which rho decays
as dust (w -> 0). Q = S(t)/a^3 - 3 H rho, a stepped function.

### (e) PID-regulated setpoint (the control theorist's structure)

A controller holds rho at a setpoint rho_* with finite gain:

    rho' = Kp (rho_* - rho) + Ki int (rho_* - rho) dt + Kd (rho_* - rho)'
    Q    = the right-hand side (the controller output IS the source term)

Zeroth order (any stable gain, transient decayed): rho = rho_* = Lambda. The
PID structure at zeroth order IS the cosmological constant, consistent with the W129
LCDM-mimic verdict by construction. First order, P-only, initial offset eps at t_i:

    rho(t)      = rho_* (1 + eps e^{-Kp (t - t_i)})
    delta w(z)  = + (Kp / 3H) eps e^{-Kp (t - t_i)} / (1 + eps e^{-Kp (t - t_i)})

an exponentially decaying w(z) transient. EDE resemblance, honestly labeled: the shape
(a localized extra-density transient that decays away) is qualitatively the early-dark-
energy phenomenology, but real EDE lives at z ~ 3000 and this window is z <= 30; the
resemblance is structural, not quantitative. Transfer function (disturbance d to
density response):

    delta rho(s) / d(s) = s / ((1 + Kd) s^2 + Kp s + Ki)

Poles s = [-Kp +/- sqrt(Kp^2 - 4 Ki (1 + Kd))] / (2 (1 + Kd)). Stable iff Kp, Ki >= 0
(Kd > -1); Ki > 0 removes steady-state error (the setpoint is reached exactly);
UNDERDAMPED, with w(z) ringing at frequency omega_d = sqrt(4 Ki (1 + Kd) - Kp^2) /
(2 (1 + Kd)), iff Kp^2 < 4 Ki (1 + Kd).

## 3. Data confrontation (verified machinery, imported verbatim)

Pipeline per structure: solve the self-consistent background on a 3000-point ln a grid
to z_star; calibrate h by the H46C theta_star procedure (solve theta_star(h; model) =
Planck 1.04110 with omega_m h^2 = 0.1430 fixed; A3 ratio-correction against the LCDM
pipeline control; ALL theta_star roots scored and the best kept, so no kill rests on
root selection); score the calibrated H(z) on the raw DESI DR2 BAO likelihood (full
13x13 covariance). Kill criterion: dchi^2 > 9 vs LCDM (3-sigma-equivalent, 1 dof)
everywhere in parameter space. Structures for which NO h in [0.30, 1.50] reproduces
the measured acoustic angle are DEAD-BY-THETA_STAR, an explicit physical verdict.

Positive controls (all pass): structure (a) through the generic pipeline reproduces
Planck theta_star (residual +2.3e-4), the calibrated h (0.67280, the shared pipeline
systematic divided out per A3), and the verified LCDM BAO row chi^2 = 30.680 at the
verbatim H46 configuration; the imported backreacted machinery reproduces H46C's
M^2 = 8 row (52.26 / 30.68, dAIC +21.58). theta_star validity guard: rho_DE/rho_m at
z = 30 is < 2.1e-4 for every ALIVE structure; the HDE scan violates it at the 1e-2
level, recorded and irrelevant at its exclusion margin.

### The taxonomy table (chi^2_LCDM = 30.11 at the calibrated baseline; dAIC = dchi^2 + 2k)

| structure | k | best chi^2 | dchi^2 | dAIC | w0 (best) | source term Q | verdict | allowed region |
|---|---|---|---|---|---|---|---|---|
| (a) fixed per comoving volume | 0 | 30.11 | 0 | 0 | -1.000 | 0 identically | ALIVE (null) | all: it is the baseline |
| (b1) per-time, comoving, from zero | 1 | 47.87 | +17.8 | +19.8 | -0.544 | S/a^3 - 3 H rho | DEAD | none (z_i <= 0.2 cannot even calibrate theta_star) |
| (b2-pure) per-time, proper, from zero | 1 | 113.69 | +83.6 | +85.6 | -1.305 | s | DEAD | none (analytic floor \|w0+1\| >= 0.35) |
| (b2) stock + drip | 1 | 21.73 | -8.4 | -6.4 | -1.094 | s | ALIVE (bounded) | s in [-0.116, +0.446] H0 rho_crit |
| (c1) rho = C H^2 | 0 | 6566.8 | +6537 | +6537 | 0.0 | C d(H^2)/dt | DEAD (structural + data) | none |
| (c2) rho = C~ H | 0 | 580.4 | +550 | +550 | -0.689 | C~ dH/dt < 0 | DEAD | none (no parameters) |
| (c3) event-horizon HDE | 1 | 67.6 | +37.5 | +39.5 | -1.474 | from the Om_de flow | DEAD | none in c in [0.5, 1.5] |
| (d) halving schedule | 2 | 51.0 | +20.9 | +24.9 | -0.511 | stepped S(t)/a^3 - 3 H rho | DEAD | none on the (z_i, Dt) grid |
| (e) PID setpoint | 2 | 17.54 | -12.6 | -8.6 | ~ -1 today | controller output | ALIVE (bounded) | 21/30 of grid; excluded = positive-offset corner eps >= +0.5 |

Notes per row, honest and complete:

- (b1) is squeezed exactly as derived: recent turn-on (z_i <= 0.2) cannot reproduce
  theta_star at any h (DEAD-BY-THETA_STAR); early turn-on fails the BAO shape
  (w ~ -0.5 ramp); the best compromise (z_i = 1.5) still loses by dchi^2 = +17.8.
- (b2-pure)'s kill is the cleanest in the taxonomy: a parameter-free analytic floor
  (|w0 + 1| >= 1/(3 H0 t0) ~ 0.35, grid minimum 0.305) that the W129 mimic band
  excludes by construction. Fixed-per-time issuance that built ALL of the present
  dark energy is dead, full stop; only a drip on top of a pre-existing stock lives.
- (c3): the entire scanned c range loses by >= +37.5; w0(c) matches the analytic HDE
  law at every point (machinery cross-check). Consistent with the known literature
  tension of event-horizon HDE against combined BAO + CMB distance data.
- (d): the halving signature (kinks in w(z), verified: max inter-grid-point |dw| of
  order 1) is invisible to BAO at the distance level (relative second difference of
  D_M ~ 2e-6): DISTANCES ARE DOUBLE INTEGRALS OF rho, so steps smear. What kills the
  halving schedules is not the steps but the same secular drift that kills (b1): the
  issued total converges and the remnant decays like dust. A halving schedule could
  only be detected by w(z)-resolving probes (binned SNe w(z)); BAO/CMB alone see only
  the smoothed drift. Best point (z_i = 2, Dt = 1/H0) still +20.9.
- (e): the allowed region is everything except the positive-offset corner. Two
  computed findings, one of which corrected this team's own pre-stated expectation:
  (1) "fast gain is always safe" is FALSE in H0 units: with z_i = 30 the transient is
  only ~0.15/H0 old at z = 2, so even Kp = 10 H0 leaves a visible w(z) transient in
  the DESI window; the boundary is set by the offset sign and size, not the gain
  (every excluded point has eps >= +0.5; every |eps| <= 0.2 point is allowed at every
  gain scanned, Kp in [0.1, 10] H0). (2) Negative offsets (density rising toward the
  setpoint, w < -1 transient) fit BETTER than LCDM, best dchi^2 = -12.6 at
  (Kp, eps) = (3 H0, -0.5). The underdamped PI point (Kp = 1, Ki = 4 H0^2,
  zeta = 0.25) is excluded at +34.9 for eps = 0.5: ringing at these gains moves too
  much density inside the window.

### The evolving-DE pull, honestly labeled

Both survivors that beat LCDM ((b2) at s* = +0.2, dAIC = -6.4; (e) at negative
offset, dAIC = -8.6) do it the same way: dark energy density LOWER in the past,
rising toward today (a w < -1 transient). This is the known DESI DR2 evolving-DE
preference expressed in issuance variables, NOT a GU discovery and NOT a detection of
issuance: (i) SNe are not integrated (the same named residual as W129 and H46C);
(ii) the preference is 2-3 sigma-equivalent, the conventional not-decisive band edge;
(iii) W129 showed the GU theta-sector family specifically CANNOT reach this signal,
and nothing here changes that verdict. What IS new: if the pull is real, its sign is
POSITIVE ISSUANCE (energy entering, not leaving), and its magnitude is the O(1) rate
below. That is the hypothesis-generating output, built to be killed by SNe
integration.

## 4. The measured rate

### Convention B (the bookkeeping rate; structure (a), exact)

    dE/dt per proper volume today:   q_B = 3 H0 rho_L = 3.435e-27 W/m^3
    dE/dt per Hubble volume:         P   = 3.727e+52 W
    Planck luminosity:               c^5/G = 3.628e+52 W

    P / (c^5/G) = 1.0273        exact identity: P = (3/2) Omega_L c^5/G

THE O(1) FLAG: the bookkeeping issuance rate per Hubble volume is one Planck
luminosity to 3 percent. Honest caveats, in order of importance: (i) the exact form is
(3/2) Omega_L c^5/G, so the O(1)-ness is structural (c^5/G is the unique GR rate
scale and Omega_L is O(1) in the coincidence era), while the NEAR-UNITY value is
partly the numerical accident Omega_L ~ 2/3; (ii) for structure (a) the COVARIANT
rate is zero, so this number is pressure work, not transduction; (iii) any
"the universe issues at exactly one Planck power" reading is therefore a coincidence-
era statement, not an invariant.

### The dimensionless ladder (which ratio is O(1)?)

    q_B / (H0^3 M_Pl_red^2) = 9 Omega_L = 6.16      O(1). THE RATE, in natural units.
    q_B / H0^4              = 1.8e+121              not O(1) (the usual 122-order gap)
    rho_L^(1/4) = 2.240 meV vs the mu_DW floor [3.4, 4.7] meV: ratio in [0.48, 0.66].
      Comparison ONLY: the H36 identification rho = c_L mu_DW^4 is FALSIFIED
      (H50/H52) and is not used anywhere in this page.

So the hypothesis-generating unit is H0^3 M_Pl^2 (equivalently c^5/G per Hubble
volume): the issuance rate density is O(1) in exactly one natural unit, and it is the
same unit in which the b2 measurement below lands.

### Convention A (the covariant rate; structure (b2), measured)

    allowed (3-sigma-equivalent vs LCDM):  s in [-0.116, +0.446] H0 rho_crit
                                             = [-1.94e-28, +7.46e-28] W/m^3
                                             = [-0.057, +0.217] q_B
    best fit (exploration grade):          s* = +0.20 H0 rho_crit = +3.3e-28 W/m^3
                                             = +0.10 q_B
    in the ladder unit:                    Q*/(H0^3 M_Pl_red^2) = +0.60;  |Q| < 1.34

The measured covariant issuance rate is CONSISTENT WITH ZERO, two-sided, bounded at
about a fifth of the pressure-work rate; the best-fit value is positive (issuance,
not withdrawal) at O(0.1-1) in the Planck-ladder unit, and it is exactly the DESI
evolving-DE pull. If SNe integration kills the pull, the rate is zero and the null
structure stands alone; if it survives, the first physical-units measurement of a
covariant dark-energy issuance rate is the number above.

### PID allowed gain / timescale region

Setpoint control with ANY stable gain and |offset| <= 0.2 is allowed (indistinguishable
from Lambda after the transient); offsets eps >= +0.5 are excluded for all
Kp >= 0.3 H0 (the transient is visible in the DESI window regardless of gain);
underdamped PI ringing at (Kp = 1 H0, Ki = 4 H0^2) is excluded at eps = 0.5. In
controller language: the data do not constrain the gain, they constrain the
initial-condition error the controller is allowed to have had at z = 30, to roughly
|eps| < 0.2-0.5 depending on sign (positive offsets die faster because extra density
in the window shrinks D_M where BAO is most constraining).

## 5. The skeptic's pass (kills and near-kills, stated plainly)

1. Anything already excluded by W129's mimic verdict dies here on schedule: (b2-pure)
   is the sharpest case (analytic floor outside the band, no parameters to tune).
2. The c-family is a graveyard: c1 structural, c2 zero-parameter miss by 550, c3 miss
   by 37 at its best. Holographic-flavored issuance in all three standard cutoffs is
   dead against this machinery.
3. The Planck-luminosity coincidence is seductive and should be treated as the
   caption says: (3/2) Omega_L c^5/G, an O(1)-by-construction number whose near-unity
   is Omega_L ~ 2/3. It generates a hypothesis (issuance saturates a Planck-power
   bound per Hubble volume); it does not evidence one.
4. The survivors' dAIC < 0 values are the DESI pull, not a discovery; SNe integration
   is the named killer and remains undone.
5. Nothing in this page identifies the issuance rate with any GU coupling (B2 FALSE
   honored) or with mu_DW^4 (H36 honored). The one plot-adjacent number that could be
   misread that way, rho_L^(1/4) = 2.24 meV vs the [3.4, 4.7] meV floor, is a ratio
   in [0.48, 0.66] and is labeled comparison-only.

## 6. What the source action must supply (the GU-side residue)

The surviving structures reduce the transducer requirement to one scalar function:

- Structure (a): Q = 0. No transducer needed at background level. If cosmology ends
  here, issuance is unfalsifiable at the background level and lives or dies on
  perturbations or on the other repositories' grounds.
- Structure (b2): Q = s, a CONSTANT proper-volume rate, |s| < 0.45 H0 rho_crit. The
  simplest possible transducer output: a constant. Bianchi then demands the
  compensating current; in unimodular language d Lambda/dt = -8 pi G s.
- Structure (e): Q = the controller output, which at P-only order is
  Q = Kp (rho_* - rho): the transducer must READ the local dark energy density and
  feed back. That is a qualitatively different (and much stronger) requirement than
  (b2): it needs a sensor, not just an emitter. Whether the source action's structure
  can even express a feedback term is a well-posed GU-side question this page leaves
  open (it is the natural next object after the SA-C4/SA-U1 layer).

## 7. Residuals (named)

- SNe integration (Pantheon+ or DES-SN5YR) into the same pipeline: the decisive
  kill-or-confirm for the evolving-DE pull carried by both survivors.
- A second BAO dataset (the same residual named by W129).
- Perturbation-level signatures of Q != 0 (growth, ISW): background-only here.
- The feedback-expressibility question for structure (e) in the source-action
  requirements (tests/spec-consistency).
- (d) halving detection forecast against binned-w(z) probes: the step signature is
  BAO-invisible (computed), so any future claim must come from SNe or redshift drift.

## 8. Verification ledger

tests/W135_issuance_structure_taxonomy.py: 34 checks, exit 0 (~3 min). Positive
controls first (theta_star reproduction, verified LCDM row 30.68 at the verbatim H46
configuration, H46C M^2 = 8 row 52.26/30.68/dAIC +21.58); all theta_star roots scored
so no kill rests on root selection; theta_star validity guard passed by every ALIVE
structure; both binding falsifications honored structurally. No canon, verdict, or
posture change proposed; W129 and H46C stand exactly as recorded.
