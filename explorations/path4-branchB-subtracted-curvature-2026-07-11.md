# Path 4 -- Branch B (thread B1): the O(M^0) intrinsic curvature we SUBTRACT

**Wave:** Path-4 "forced family-invariant" hunt (blind multi-branch). This is Branch B only.
**Status:** exploration-grade; deterministic test `tests/W62_path4_B_subtracted_curvature.py` (exit 0, 10/10 PASS).
**Construction used (GEOMETER-VS-PHYSICS-OBJECTS.md metric row):** the gimmel/DeWitt **metric-on-metrics**
on `Y^14 = Met(X^4)` -- horizontal tautological block `g`, **trace-reversed Frobenius** vertical fiber
`(7,3)->(6,4)`. NOT the single spacetime metric `g`. The object under test lives on the fiber geometry, so the
metric-on-metrics is the correct and load-bearing construction.

5-persona team run INLINE (sequential, one context). No canon / RESEARCH-STATUS / claim-status / verdict change.

---

## The candidate

The base of the GU gravity construction is `Y^14 = Met(X^4)` with the DeWitt/gimmel metric. That space is
**intrinsically curved**, so the **constant section** `s0(x) = (x, eta)` (the section that picks out THE
spacetime metric) is **not totally geodesic**: its vertical second fundamental form is nonzero even at zero
field. That nonzero O(M^0) piece is currently **subtracted as a background reference** in the `|II|^2 / R^Y`
gravity computations (H24 excludes it from the `s^1` kinetic sign; H25 separates it out at `t^0`; H51 names it
the DeWitt coefficient). Branch B asks: is subtracting it legitimate, and if kept, does it predict a **forced,
family-invariant** dark-energy contribution -- distinct from the `mu_DW`-scaled DeWitt-Lambda (a free scale)?

---

## Persona 1 -- Differential-geometry specialist: IDENTIFY and COMPUTE the O(M^0) term

For the constant section (`g = eta`, `partial g = 0`) the vertical SFF reduces (ii-s-coordinate-formula sec 6.1)
to the pure DeWitt vertical Christoffel:

```
B^V_{mu nu, ab} = -(1/2) ( eta_{a(mu} eta_{nu)b} - (1/2) eta_{ab} eta_{mu nu} )   (symmetrization weight 1/2)
```

Exact (sympy) properties, all O(M^0), no field / no derivative / no fitted input:

- **Nonzero** -- `Met(X^4)` is intrinsically curved; the constant slice is not totally geodesic. (This IS the
  subtracted piece.)
- **Fiber-trace `T_{mu nu} = eta^{ab} B^V_{mu nu,ab} = (1/2) eta_{mu nu}`** -- exactly proportional to the
  metric. An induced base stress `~ eta_{mu nu}` is the defining algebraic form of a **vacuum / cosmological-
  constant** stress. General dimension: coefficient `= (n-2)/4` (a consequence of `n=4`, vanishes at `n=2`;
  not imported).
- **Mean curvature `H_{ab} = eta^{mu nu} B^V_{mu nu,ab} = (1/2) eta_{ab}`** -- pure-trace normal, the Lambda
  direction.
- **Constant shape-energy densities** `|H|^2_V = -1`, `|II|^2_V = 2` (DeWitt vertical norm), **x-independent**.
  A spatially constant density integrated as `int sqrt(g) * const` **is** a cosmological-constant term.
- **Equivalent horizontal form:** the pure-horizontal ambient sectional curvature of the gimmel metric,
  `-3/16` (non-doubled) / **`-3/8`** (A-oracle doubled basis) `= c_L`, the DeWitt cosmological coefficient
  (H24 1a, H51 Q1). Negative and constant.

**Identification:** the subtracted O(M^0) term is the **DeWitt-Lambda** -- a genuine, `Lambda`-shaped vacuum-
energy contribution forced to be PRESENT by the curvature of the space of metrics.

## Persona 2 -- Referee: forced-vs-convention, novel-vs-known

- **Forced that it EXISTS / its SHAPE:** YES. The curvature of `Met(X^4)` is not optional; the constant section
  is provably not totally geodesic (nonzero `B^V`; thread A3: the shape operators don't even commute). Its
  `Lambda`-shape (fiber-trace `~ eta`) is exact, not chosen.
- **Forced dimensionless COEFFICIENT `c_L` and SIGN:** YES, and **family-invariant**. `c_L` is the horizontal
  DeWitt sectional -- it is built from the background `eta` alone, in the **horizontal** sector, so it is blind
  to the residual gravity-shape ratio `beta/alpha` (which lives in the TANGENTIAL `|II|^2`-vs-`|H|^2` kinetic
  sector). Independent of `beta/alpha` and independent of the free scales' magnitudes.
- **Forced MAGNITUDE (the actual DE density):** **NO.** `rho_Lambda = c_L * mu_DW^4`. The dimensionful vacuum
  energy is set by the **free** DeWitt scale `mu_DW`. The ratio-only geometry (H24) fixes only dimensionless
  invariants; a `[mass^4]` density needs a `scale^4`, and `mu_DW` is the ONLY dimensionful scale in the
  construction. So the magnitude is a **fit, not a prediction**.
- **Novel:** "a curved geometry produces a cosmological constant" is not by itself novel or discriminating --
  every EFT carries a `Lambda` counterterm. The narrow novel-and-forced content is the *specific* geometric
  coefficient/sign and the cross-observable lock (below).

## Persona 3 -- Intra-team adversary (PRESENTS, does not veto)

Two attacks, both land partially:

1. **"It is a pure background/gauge choice; subtracting it is legitimate and it carries no physical content."**
   *Rebuttal (partial):* the term is a **FULL tensor**, not a trace (H21 Check 4b; test (b) here) -- it cannot
   be removed by a trace/gauge convention. It is a genuine geometric invariant of the metric-on-metrics, so
   "subtract it" is a *physical* choice about the vacuum energy, not a coordinate freedom. **BUT** the adversary
   is right that, as an EFT, you retain the standard freedom to add a `Lambda` counterterm of the opposite sign;
   the geometry forces the term to be PRESENT and computes its shape/sign/coefficient, but it does not forbid a
   counterterm. So "keeping it" is *physically meaningful* but not *un-cancellable*. **Strength: STRONG on
   "magnitude is a convention/counterterm-adjustable"; DEFEATED on "no physical content / pure gauge."**

2. **"Even if physical, its scale is the free `mu_DW`, so it is not a forced prediction."**
   *Rebuttal:* correct for the **magnitude**. This is the load-bearing trap and it holds: the DE **density** is
   `c_L * mu_DW^4` with `mu_DW` free. **Strength: DECISIVE against a forced DE-magnitude claim.** What survives
   is only the dimensionless coefficient/sign and the `mu_DW`-cancelling lock.

## Persona 4 -- Cross-checker: independent known-geometry limit

The curvature of `Met(M)` with the DeWitt supermetric is classically known: **Freed-Groisser (1989)** and
**Gil-Medrano-Michor (1991)** show `Met(M)` is fiberwise a symmetric space of **non-compact type**
(`GL(n,R)/O(n)`-like) with **non-positive sectional curvature**, and the constant sections are **not** totally
geodesic. This independently confirms, model-agnostically: (i) the O(M^0) SFF is nonzero (the subtracted term is
real), and (ii) the sectional curvature has a **definite (negative) sign** -- so the forced SIGN of `c_L` is a
known-geometry fact, not a GU artifact. The GU-specific normalization (`-3/16` / `-3/8`, and `|II|^2_V=2`) is
the model input; the *non-vanishing and the negative sign* are the model-independent Freed-Groisser /
Gil-Medrano-Michor limit. Cross-check **passes**.

## Persona 5 -- Synthesizer

### Graded verdict

- **Q-forced: SPLIT.** The **existence, `Lambda`-shape, sign, and dimensionless coefficient `c_L`** of the
  O(M^0) DeWitt-Lambda are **forced and family-invariant** (independent of `beta/alpha` and of the free-scale
  magnitudes). The **dark-energy MAGNITUDE** `rho_Lambda = c_L * mu_DW^4` is **NOT forced** -- it is set by the
  single free scale `mu_DW`. As a standalone DE-density prediction: **not forced (a fit).**
- **Q-novel: WEAK-as-DE-magnitude, NARROW-forced-residue.** "Geometry yields a `Lambda`" is not novel or
  discriminating (any EFT has one). The genuinely novel-and-forced residue is (a) the forced geometric
  *coefficient/sign* `c_L`, and (b) the **`mu_DW`-cancelling lock**: because the SAME `mu_DW` sets both
  `rho_Lambda` and the graviton mass `m2 = sqrt(m2_eff)*mu_DW`, the cross-observable ratio
  `lambda = hbar_c * c_L^{1/4} / (sqrt(m2_eff) * rho_Lambda^{1/4})` is `mu_DW`-independent -- a forced,
  family-invariant tie between the short-range Yukawa range and the DE density.
- **Q-disc: NO as a DE-magnitude; YES-but-EXCLUDED as the lock.** The magnitude discriminates nothing. The lock
  IS discriminating (it ties two observables by pure geometry, which no LCDM/GR/generic-EFT does), but it is the
  H50/H51 correlation, already found **excluded-at-frontier** under the H36 identification (`lambda ~ 60-74 um`
  at `alpha = 1/3`).

### The single strongest forced-and-novel statement (what Branch B can defend)

> The curvature of the space of metrics `Met(X^4)` **forces** a specific, `Lambda`-shaped O(M^0) vacuum-energy
> contribution to be present in **every** family member, with a **family-invariant** (`beta/alpha`-independent)
> dimensionless coefficient `c_L = 3/8` and a **definite (negative-sectional) sign** -- but its magnitude is
> `rho_Lambda = c_L * mu_DW^4`, fixed entirely by the one free scale `mu_DW`, so the dark-energy **density is a
> fit, not a forced prediction**. The only forced-and-novel *observable* content is the `mu_DW`-cancelling lock
> tying the DE density to the graviton-mass Yukawa range by pure geometric O(1) numbers -- which is the
> Branch-A correlation, and is already excluded-at-frontier.

### Honest bottom line (the anticipated trap, cleanly stated)

Branch B **does not** deliver an independent, forced, family-invariant dark-energy *magnitude*. It confirms the
trap: the subtracted term is **physical** (a genuine geometric invariant, not a gauge/trace artifact), so
"subtract it" is a physical vacuum-energy choice -- but its **scale is the free `mu_DW`**, and dimensional
analysis forecloses any `mu_DW`-independent magnitude because the ratio-only geometry has exactly one scale.
The forced content is the coefficient/sign (dimensionless) and the cross-observable lock, **not** a vacuum-
energy density. Branch B's positive contribution is (i) upgrading "subtracting the O(M^0) term" from "free
convention" to "physical background-energy choice with a forced, computed coefficient and sign," and (ii)
pinning that the DE-magnitude cannot be forced by geometry alone.

### Load-bearing assumption

The gimmel/DeWitt metric on `Y = Met(X^4)` (trace-reversed Frobenius fiber, tautological horizontal block) is
GU's intended metric-on-metrics, AND the ratio-only / scale-covariant property (H24) holds -- i.e. `mu_DW` is
the sole dimensionful scale. If a second, geometrically-forced scale existed, the magnitude conclusion would
change; none is known.

### Confidence

**HIGH** on the SPLIT verdict. The forced side (existence, shape, sign, `c_L`, family-invariance) rests on four
independent computed tests (thread B, thread A3, H24, H25/H51) plus the Freed-Groisser / Gil-Medrano-Michor
known-geometry cross-check. The not-forced side (magnitude = free `mu_DW`) rests on dimensional analysis plus
the H24 ratio-only result -- both robust. Residual O(1) freedom in the `c_L` normalization (band `3/16 .. 2`)
does not affect the SPLIT (it moves the lock's `lambda`, not the forced-vs-free boundary).

---

## COMPUTED vs ARGUED ledger

| claim | grade | evidence |
|---|---|---|
| O(M^0) term = constant-section vertical SFF, nonzero (not totally geodesic) | **COMPUTED** | test (a); thread B/A3 |
| fiber-trace `= (1/2) eta_mn`, coeff `(n-2)/4` (Lambda-shaped) | **COMPUTED** | test (a), exact sympy |
| `|H|^2_V=-1`, `|II|^2_V=2` constant densities | **COMPUTED** | test (a) |
| term is a FULL tensor, NOT a trace -> physical, not a gauge/trace convention | **COMPUTED** | test (b); H21 Check 4b |
| `c_L = 3/8` family-invariant, `beta/alpha`-independent (horizontal sector) | **COMPUTED** | H24 1a, H51 Q1; test (c) |
| magnitude `rho_Lambda = c_L*mu_DW^4` set by FREE `mu_DW` -> NOT forced | **COMPUTED/ARGUED** | test (c); H24 ratio-only + dim. analysis |
| `mu_DW`-cancelling lock `lambda ~ c_L^{1/4}/rho^{1/4}` is forced/family-invariant | **COMPUTED** | test (c); H50/H51 |
| the lock is discriminating but EXCLUDED-at-frontier under H36 | COMPUTED vs cited | H50/H51 (Lee/Tan/Kapner) |
| non-positive sectional / not-totally-geodesic (sign of `c_L`) | **COMPUTED + known-limit** | Freed-Groisser 1989; Gil-Medrano-Michor 1991 |

## Deliverables

- This file: `explorations/path4-branchB-subtracted-curvature-2026-07-11.md`
- Test: `tests/W62_path4_B_subtracted_curvature.py` (exit 0, 10/10 PASS)

*Exploration-grade; not promoted to canon. No canon / RESEARCH-STATUS / claim-status / verdict / posture change.
References for the known-geometry limit (comparison only): Freed & Groisser, "The basic geometry of the manifold
of Riemannian metrics" (1989); Gil-Medrano & Michor, "The Riemannian manifold of all Riemannian metrics" (1991).
Short-range-gravity bounds cited in H50/H51 only.*
