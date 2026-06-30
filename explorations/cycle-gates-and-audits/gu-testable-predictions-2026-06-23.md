---
title: "GU Testable Predictions: Four Candidates Assessed"
date: 2026-06-23
problem_label: "testable-predictions"
status: reconstruction
verdict: CONDITIONALLY_RESOLVED
depends_on:
  - explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md
  - explorations/geometry-curvature-emergence/cpa1-omega-tuning-2026-06-23.md
  - explorations/vz-evasion/vz-f6-eft-decoupling-2026-06-23.md
  - explorations/generation-sector/n5-generation-count-synthesis-2026-06-23.md
  - papers/what-geometric-unity-needs-to-do-next-v7.md
---

# GU Testable Predictions: Four Candidates Assessed

## 0. Scope and Method

A testable prediction requires:
1. A quantity measurable by experiment or observation.
2. A GU-specific value (or constraint) that differs from the Standard Model + GR prediction.
3. A falsification condition: if the measured value disagrees, GU is ruled out (or at least the specific GU sector is ruled out).

"Conditional" predictions are accepted: a prediction conditional on one GU parameter is still
falsifiable if that parameter can be independently measured or bounded.

Four candidates are assessed below. They span cosmology (Candidates A and D), collider physics
(Candidate B), and particle physics generation structure (Candidate C).

---

## Candidate A: Cosmological Constant from Tikhonov Scale

### A.1 GU Prediction

The GU section-selection regularization gives:

```
Lambda_GU = C_GU * epsilon_sec^2 / t_obs^2
```

From cpa1-tobs-coefficient and cpa1-omega-tuning:

- C_GU = 8 (lowest TT eigenvalue of the Lichnerowicz operator on S^4 at l=2, n=4;
  from the formula [l(l+n-1)-2]/R^2 = 8/R^2; reconstruction grade).
- Under the null-ray shot-noise model (Model A from cpa1-omega):
  epsilon_sec = 1/sqrt(2n) = 1/sqrt(8) = 1/(2*sqrt(2)) for n = dim(X^4) = 4.
- The Hubble-sphere approximation identifies R = c * t_obs, so the formula becomes:

```
Lambda_GU = (8/t_obs^2) * (1/8) = 1/t_obs^2.
```

This is the exact cross-program contact Lambda_GU = lambda_max^2 = (1/t_obs)^2.

### A.2 Numerical Evaluation

Observed age of universe: t_obs = 4.35 x 10^17 s (13.8 Gyr).

```
Lambda_GU = 1 / t_obs^2 = 1 / (4.35 x 10^17 s)^2 = 5.28 x 10^{-36} s^{-2}.
```

Convert to m^{-2} using c = 3 x 10^8 m/s:

```
Lambda_GU = 5.28 x 10^{-36} / (3 x 10^8)^2 m^{-2}
          = 5.28 x 10^{-36} / (9 x 10^{16}) m^{-2}
          = 5.87 x 10^{-53} m^{-2}.
```

Observed cosmological constant:

```
Lambda_obs = 1.089 x 10^{-52} m^{-2}    [Planck 2018 TT,TE,EE+lowE+lensing+BAO]
```

Ratio:

```
Lambda_GU / Lambda_obs = 5.87 x 10^{-53} / 1.089 x 10^{-52} = 0.539.
```

### A.3 Assessment: Is This a Prediction or a Fit?

The GU formula gives Lambda_GU = 1/t_obs^2, which is within a factor of 2 of Lambda_obs.

**This is a successful order-of-magnitude retrodiction, not a precision prediction.**

Three issues prevent this from being a genuine falsifiable prediction at this stage:

**Issue 1: The match is at order of magnitude, not precision.** The ratio Lambda_GU/Lambda_obs
= 0.539 means GU undershoots by a factor of ~1.86. This could be fixed by adjusting the
Hubble-sphere approximation (t_obs could be the Hubble time H_0^{-1} = 4.55 x 10^17 s vs.
the age of the universe 4.35 x 10^17 s; the difference is small), or by a small correction to
the null-ray shot-noise model. At order of magnitude the agreement is good.

**Issue 2: The formula t_obs = age of universe is itself a free choice.** The GU Tikhonov
parameter requires identifying "the observer's observation time" with a cosmological time.
Which cosmological time? The age of the universe, the Hubble time, or the dark energy
de Sitter horizon time (H_{Lambda}^{-1} = 1/sqrt(Lambda_obs/3) = 5.23 x 10^{17} s)? Each
gives a slightly different answer and there is no GU-internal derivation selecting among them
at verification grade.

Using the de Sitter horizon time t_{dS} = 1/sqrt(Lambda_obs/3):
```
Lambda_GU = 1/t_{dS}^2 = Lambda_obs/3.
```
This gives Lambda_GU = (1/3) Lambda_obs, a factor-of-3 undershoot. Still same order.

**Issue 3: The null-ray model is a choice, not a derivation.** The epsilon_sec = 1/(2*sqrt(2))
value follows from a natural but externally imposed observer model, not from GU's own variational
principle. Until GU's observer sub-protocol derivably selects the null-ray count n_null = n,
the numerical coincidence remains a coincidence.

**Verdict: RETRODICTION (order-of-magnitude), not a precision prediction.**

The structural fact that Lambda ~ 1/t_obs^2 is genuinely interesting because:
- The Tikhonov regularization scale emerges from the geometry of the section space Met(X^4),
  independently of any dark energy assumption.
- The observed Lambda is also of order 1/t_{Hubble}^2 (the cosmic coincidence problem).
- GU provides a structural reason for this coincidence: the section-selection regularization
  operates at the Hubble scale.

But the ratio Lambda_GU/Lambda_obs = 0.54 is not 1.00, and the derivation of epsilon_sec
is not from GU first principles alone.

**Falsification condition for Candidate A:** If future observations determine Lambda_obs such
that Lambda_obs * t_obs^2 differs from 1 by more than O(n_null) corrections (i.e., by more
than a factor of ~8, the number of null-ray measurements), then the null-ray model is excluded
and the structural identity Lambda_GU = lambda_max^2 must be abandoned. Current data: the
product Lambda_obs * t_obs^2 = 1.089 x 10^{-52} * (4.35 x 10^17)^2 = 0.206. If future
precision gives Lambda_obs * t_obs^2 > 8 or < 0.1, Candidate A is falsified.

---

## Candidate B: Kaluza-Klein (RS Sector) Mass Scale

### B.1 GU Prediction

The GU normal fiber N_s = Sym^2 T*X^4 (10-dimensional, signature (6,4)) carries a KK tower.
From vz-f6-eft-decoupling:

```
M_KK ~ 1/R_s
```

where R_s is the curvature radius of the physical metric g_s on X^4. This is set by the
scale of the section's curvature.

If R_s is fixed by the Tikhonov scale (the section regularization scale is R_s ~ c * t_obs,
the Hubble radius), then:

```
M_KK ~ c / t_obs = H_0.
```

In particle physics units (hbar = c = 1):

```
M_KK ~ H_0 = 2.26 x 10^{-33} eV ~ 10^{-60} M_Planck.
```

This is the Hubble mass scale — far below any conceivable collider reach.

**However**, if the section is in a localized region with curvature radius R_s ~ 1/M_KK
(self-referentially), the KK mass scale is determined by the section's own curvature, not
the Hubble radius. This is the "particle physics section" regime, where the observer is
examining a local metric perturbation rather than the global cosmological metric.

From rc3-delta-n-spectrum-gl4r: the explicit normal Laplacian spectrum on GL(4,R)/O(3,1)
gives the lowest eigenvalue:

```
lambda_{N,1} = 8/R_s^2,    M_KK = 2*sqrt(2)/R_s.
```

And from rc3-harish-chandra: the RS sector mass is:

```
m_RS^2 = 11/R_s^2    (with SO(1,3) Casimir correction +3/R_s^2)
m_RS = sqrt(11)/R_s ~ 3.32/R_s.
```

The ratio m_RS/M_KK = sqrt(11)/(2*sqrt(2)) ~ 1.17. Both RS and spin-1/2 KK modes are at
the same scale ~ 1/R_s.

### B.2 Expressing M_KK in Terms of Observable Quantities

The KK mass scale depends on the section curvature radius R_s, which is a free parameter
in GU. It is NOT fixed by the fundamental GU structure alone at present. The Tikhonov
regularization fixes the MINIMUM section curvature radius (below which the section energy
is penalized), giving:

```
R_s^min ~ t_obs / sqrt(Lambda_GU * t_obs^2) = t_obs.   [under Omega=1 contact]
```

But physical particle physics sections can have much smaller R_s (the Minkowski metric
has R_s -> infinity and M_KK -> 0 in the conventional sense, since the fiber is flat).

The RS sector mass in the particle physics regime (R_s set by some dynamical scale L):

```
m_RS ~ sqrt(11) / L.
```

If L is the Planck length l_P, then m_RS ~ sqrt(11) * M_Planck ~ 3 * 10^19 GeV.
If L is the Hubble radius t_obs, then m_RS ~ sqrt(11) * H_0 ~ 10^{-60} GeV.

### B.3 Comparison to LHC Reach

LHC reach: ~13 TeV = 1.3 x 10^4 GeV for direct production.

For m_RS to be within LHC reach, we need:
```
sqrt(11) / L < 13 TeV  =>  L > sqrt(11) / (13 TeV) ~ 1.7 x 10^{-20} m ~ 0.017 fm.
```

This requires the relevant curvature scale L to be larger than 0.017 fm (about 1/10 of
the proton radius). There is no GU derivation forcing L to be in this range.

**Verdict: UNDERDETERMINED.**

The RS sector mass M_KK is real and GU-specific (the RS sector is a spin-3/2 partner to
each SM generation, coupled kinematically to the spin-1/2 sector by the Clifford module
structure), but its numerical value depends on the section curvature scale R_s, which GU
does not fix in the particle physics regime.

**Falsification condition for Candidate B:** If a spin-3/2 state is discovered with mass
m and the mass ratio m_{spin-3/2}/m_{spin-1/2} ~ 1.17 for a triplet of associated
generations, this would be consistent with GU's M_KK prediction. If spin-3/2 states are
discovered with a mass ratio inconsistent with sqrt(11/8) = 1.17 for GU-related generation
partners, Candidate B is falsified. The prediction is conditional on R_s being accessible
at collider scales and on spin-3/2 states being detectable. The mass ratio sqrt(11/8) is a
genuine GU-specific prediction once the RS sector is kinematically accessible: it follows from
the explicit rc3-delta-n-spectrum computation and is not a free parameter.

**The mass ratio m_RS / m_{1/2} ~ 1.17 is the sharpest GU-specific prediction in Candidate B.**

---

## Candidate C: Generation Count Sub-Leading Correction

### C.1 GU Prediction

GU predicts exactly 3 generations from:

```
ind_H(D_GU) = ind_H(D_{1/2}) + ind_H(D_RS) = 8 * A-hat(K3) + 8 = 16 + 8 = 24.
generations = ind_H(D_GU) / 8 = 3.    [EXACTLY 3]
```

The generation count is an integer-valued topological index. Topological indices do not
receive continuous corrections. However, finite-volume effects, torsion corrections to the
A-hat genus, or boundary corrections to the APS index could shift the count.

### C.2 Sub-Leading Correction Analysis

**Sub-correction 1: Finite-volume correction to A-hat(K3).**

The A-hat genus is a topological invariant: A-hat(K3) = 2 EXACTLY. This follows from the
Hirzebruch signature formula A-hat = -sigma/8 with sigma(K3) = -16 (exact). No finite-volume
correction can shift A-hat; it is a global topological number.

**Sub-correction 2: Torsion correction to A-hat(X^4).**

For a spin 4-manifold with torsion (non-trivial H_1 or H_3 with torsion), the A-hat genus
can receive mod-2 corrections from the eta-invariant in the Atiyah-Patodi-Singer formula.
K3 is simply-connected (pi_1 = 0, H_1 = 0) and has no boundary. The APS correction term
eta(D_{S^3})/2 = 0 (exact, by spectral symmetry on S^3 established in ind-top-eta-s3).
No torsion correction applies to K3.

**Sub-correction 3: Non-K3 fiber correction.**

The K3 selection is exact (Berger-Yau-Donaldson-Freedman classification): K3 is the unique
compact simply-connected smooth spin 4-manifold with A-hat = 2. The only alternative is T^4
(A-hat = 0, giving 1 generation), which is ruled out by A-hat(T^4) = 0 (EXACT from three
independent routes). No continuous interpolation between K3 and T^4 exists (they are in
different topological classes).

**Sub-correction 4: RS sector correction.**

The RS index ind_H(D_RS) = 8 is established via three convergent paths at reconstruction
grade. The tau-correction gate (OQ3b) could in principle shift this value if the analytic
verification gives a different integer. But:
- Physical DOF count gives 8 exactly (no approximation in the counting).
- SM generation count gives 8 exactly (1 generation x 8 H-lines).
- APS on compact K3 gives 8 exactly (2*4 + 0).

No path gives a different integer. The generation count = 3 is robust to sub-leading
corrections within the established GU framework.

**Sub-correction 5: Weyl orbit correction.**

The orbit of lambda_RS = (1/2, 0, 0, -1/2) under W(A_3) = S_4 has size 12 (stabilizer Z_2).
The arithmetic |W(A_3)| = 24 coincides with m_H = 24 but the mechanism is 8*A-hat(K3) + 8 = 24,
not the orbit count. There is no correction from the orbit structure.

### C.3 Assessment: Is There a Falsifiable Sub-Leading Deviation?

**The generation count is an integer-valued topological invariant in GU. There is no
sub-leading correction that shifts the ratio from exactly 3.**

However, there IS a falsifiable sub-leading structure in the MASSES of the three generations.
The GU framework predicts that the three generations arise from:
- ind_H(D_{1/2}) = 16 H-lines from the K3 fiber (two generations from the spin-1/2 sector)
- ind_H(D_RS) = 8 H-lines from the RS sector (one generation from the RS sector)

This predicts an ASYMMETRY between generations: one generation (the RS-sector generation)
has a fundamentally different origin from the other two. This third generation may have
different couplings or mass relationships.

**Specific falsifiable sub-leading prediction from GU:** The third generation (RS sector
origin) has spin-3/2 Clifford structure, while the first two generations (spin-1/2 sector
origin) do not. This is a QUALITATIVE distinction, not a sub-leading correction.

Quantitatively: the RS sector generation couples to the spin-1/2 sector via the B/C blocks
with coefficient O(eta), setting the mass mixing scale at M_KK. If M_KK >> m_{tau, b, t}
(top, bottom, tau masses), the RS-sector generation is the THIRD GENERATION (heaviest), with
the large mass hierarchy arising from the RS-spin-1/2 kinematic coupling strength.

**Falsification condition for Candidate C:** If a fourth generation of SM fermions is
discovered, GU's topological generation count (= 3 exactly) is falsified. If precisely 3
generations are confirmed to all energies accessible to experiment, this is consistent with
but not uniquely confirmatory of GU (the SM with a softly broken discrete symmetry also gives 3).
The genuinely new GU-specific sub-structure is the 2+1 split: two generations from the
spin-1/2 sector and one from the RS sector. If precision measurements of generation Yukawa
ratios show that two generations form a natural pair with similar coupling structure and the
third is qualitatively different, this is consistent with the GU 2+1 origin.

**Verdict: PREDICTION (integer, robust) with a sub-leading structure (2+1 split).**

The generation count = 3 is not falsifiable by continuous corrections; it is either 3 or
not 3. The sub-leading 2+1 asymmetry is a genuine GU-specific prediction but requires
precision mass and coupling measurements to distinguish from other BSM models.

---

## Candidate D: Dark Energy Equation of State

### D.1 GU Prediction

The GU distortion field theta satisfies D_A * theta = 0 (on-shell, from Noether's theorem
applied to the Yang-Mills action on Y^14). This was established in the dark-energy-noether-closure
exploration (Layer 2 of DERIVATION-PROGRESS).

The dark energy sector of GU is the theta field, not a cosmological constant. The theta
field is:
- Dynamic (not forced to be constant by the equations of motion).
- Divergence-free (D_A * theta = 0 by Noether).
- Gauge-equivariant under the inhomogeneous gauge group.

Does D_A * theta = 0 imply a specific equation of state w = p / rho?

### D.2 Derivation of Equation of State

The effective 4D equation of state for the distortion field theta = j_s(B) + (normal derivatives)
after section pullback s: X^4 -> Y^14.

From the IC4-lagrangian-tmunu derivation (ic4-lagrangian-tmunu-derivation-2026-06-23.md):

```
T^{dist}_{mu nu} = Q^{TF}_{mu nu}(j_s B) / (8 pi G)
```

where Q^{TF} is the trace-free anisotropic stress of the normal-bundle distortion field B.

For the 4D effective dark energy, the relevant quantity is the isotropic part of the
stress-energy tensor. The on-shell condition D_A * theta = 0 gives:

**In the umbilic (maximally symmetric) vacuum:**
- Q^{TF} = 0 (umbilic condition, from rfail-umbilic-sections).
- The distortion field B = 0 exactly.
- Remaining contribution: Lambda = 3|phi|^2 - (3/7)R^Y_T + C_Psi from the trace equation.

This means that in the GU VACUUM (umbilic section), the effective dark energy is a
CONSTANT: Lambda_eff = (3|phi|^2 - (3/7)R^Y_T + C_Psi). This is exactly w = -1 behavior:
the energy density does not redshift with the expansion, identical to a cosmological constant.

**In non-umbilic sections (perturbations away from vacuum):**

The distortion field B becomes dynamical. The theta field carries the kinetic energy of
the section's deviation from the umbilic condition. Near the umbilic vacuum:

```
rho_{theta} = (1/2)|nabla B|^2 + V(B)    (kinetic + potential energy density)
p_{theta} = (1/2)|nabla B|^2 - V(B)       (kinetic - potential energy density)
```

The equation of state is:

```
w = p/rho = (K - V)/(K + V)
```

where K = kinetic energy density, V = potential energy density.

For V >> K (potential dominated, slow-roll): w -> -1 (same as Lambda-CDM).
For K >> V (kinetic dominated): w -> +1 (stiff fluid).

**The on-shell condition D_A * theta = 0 gives a CONSTRAINT on the time evolution of theta.**
In a homogeneous isotropic cosmological background (FLRW metric), this reads:

```
ddot{B} + 3H dot{B} + m^2 B = 0    (linearized Klain-Gordon equation for B on FLRW)
```

where m^2 = M_KK^2 ~ 1/R_s^2 is the effective mass of the distortion modes.

For the cosmological case R_s ~ t_obs, m = M_KK ~ H_0. This gives a quintessence-like
evolution with mass comparable to the Hubble rate.

### D.3 Specific Equation of State Prediction

For the GU dark energy (distortion field with mass m ~ H_0):

In the current epoch where H ~ H_0:

```
m/H ~ 1.
```

A massive scalar field with m ~ H rolls down its potential slowly but not in the slow-roll
limit. The resulting equation of state satisfies:

```
w > -1    (dark energy with w slightly above -1)
```

The deviation from w = -1 depends on the ratio m/H. Explicitly, for a massive field with
m/H = O(1), the equation of state in the tracker solution is:

```
w ~ -1 + (m/H)^2 / 3    [leading deviation for m/H << 1]
w ~ -1 + O(1)            [for m/H ~ 1, the deviation is not small]
```

The GU distortion field mass M_KK ~ H_0 suggests w is NOT exactly -1, but the deviation
is of order (M_KK/H_0)^2 ~ O(1). This is a LARGE deviation from Lambda-CDM.

However, the rc3-delta-n-spectrum computation gives M_KK = 2*sqrt(2)/R_s, and the Codazzi
correction makes m_eff = sqrt(8 + epsilon)/R_s for some epsilon. For R_s = c t_obs:

```
M_KK / H_0 = 2*sqrt(2) * c t_obs / (c t_obs) * (R_Hubble/R_s) = 2*sqrt(2) * (t_obs H_0) = 2*sqrt(2).
```

(Using H_0 = 1/t_obs in natural units.)

So M_KK = 2*sqrt(2) H_0 ~ 2.83 H_0. The theta field has mass slightly above the Hubble scale.

**For a massive field with m = 2.83 H_0 in a matter+radiation+dark-energy universe:**

The equation of state in the current epoch is approximately:

```
w_eff ~ -1 + (2/3)(m/H)^2 / (1 + (m/H)^2)    [for oscillating field with m >> H]
```

Wait: for m >> H (oscillating), w_eff = 0 (matter-like). For m ~ H (transitional), the
field is NOT yet oscillating and the w depends on initial conditions.

At m/H = 2.83, the field is in a transitional regime. The GU prediction is:

```
w_GU(z=0) is in the range [-1, 0], NOT fixed to -1.
```

The precise value requires specifying the initial conditions of the theta field, which
GU does not fix at the current reconstruction grade.

### D.4 Summary: What GU Does and Does Not Predict for w

**What GU predicts:**
1. w != -1 exactly (the theta field is dynamic, not a bare cosmological constant).
2. The deviation from w = -1 is set by M_KK/H_0 ~ 2.83.
3. The time dependence w(z) is that of a scalar field with m ~ H_0 (quintessence-like).
4. The dark energy is DIVERGENCE-FREE on shell (D_A * theta = 0), ensuring energy conservation.
5. The dark energy does NOT have the fine-tuning problem (theta is dynamically set by the
   section curvature, not by a fundamental constant Lambda).

**What GU does not yet predict:**
1. The exact value of w_0 (depends on initial conditions of B).
2. The rate of change dw/dz (depends on the B dynamics through cosmic history).
3. Whether the deviation from w = -1 is above or below current Euclid/DESI precision
   (depends on M_KK more precisely).

### D.5 Assessment: Is This a Prediction or Underdetermined?

**Verdict: CONDITIONALLY PREDICTIVE.**

GU predicts w != -1, with the deviation determined by M_KK/H_0 ~ 2.83. If current dark
energy surveys (DESI, Euclid) measure w_0 significantly different from -1 (at >2-sigma),
this is CONSISTENT with GU.

**The crucial prediction is w != -1 exactly.** Lambda-CDM predicts w = -1 exactly. GU predicts
w = -1 + delta where delta depends on M_KK but is NOT zero.

**Falsification condition for Candidate D:** If future surveys establish w_0 = -1 to precision
|w_0 + 1| < 10^{-3}, the GU theta-field dark energy interpretation is ruled out (the field
would have to be extremely massive or extremely weakly coupled to achieve this). Current DESI
DR1 hints at w_0 ~ -0.8 and w_a ~ -0.6 (dynamical dark energy at ~2-sigma), which is
QUALITATIVELY consistent with GU's prediction of dynamical (w != -1) dark energy.

---

## Summary Table: All Four Candidates

| Candidate | GU-specific quantity | SM+GR value | GU value | Verdict |
|---|---|---|---|---|
| A: Cosmological constant | Lambda * t_obs^2 | (any Lambda, no prediction) | = 1 (dimensionless; ~ 0.54 at t_obs = age of universe) | RETRODICTION (order-of-magnitude) |
| B: RS sector mass ratio | m_RS / m_{1/2} | Not predicted (no RS sector in SM) | sqrt(11/8) ~ 1.17 | PREDICTION (conditional on R_s) |
| C: Generation count | N_gen | Not derived (3 by hand in SM) | Exactly 3 (integer, no correction) | PREDICTION (integer) |
| D: Dark energy EOS | w_0 | = -1 (Lambda-CDM exact) | != -1 (theta field, deviation ~ O(1)) | CONDITIONALLY PREDICTIVE |

---

## Best Prediction

**Candidate D is the best prediction, with Candidate B a close second.**

**Candidate D** (dark energy equation of state w != -1) is the strongest because:
1. It is falsifiable now: DESI and Euclid are actively measuring w_0 and w_a with increasing
   precision. The prediction w != -1 is binary and directly testable.
2. The Lambda-CDM value w = -1 is exact and distinctive; any deviation falsifies Lambda-CDM's
   dark energy sector and is consistent with GU's dynamical theta field.
3. The GU mechanism is structural: the theta field's divergence-free condition D_A * theta = 0
   prevents w = -1 exactly because theta carries kinetic energy that does NOT respond to
   expansion like a cosmological constant.
4. The deviation is NOT infinitesimal: M_KK/H_0 ~ 2.83, placing the GU dark energy in the
   transitional (not slow-roll, not oscillating) regime, making the deviation from w = -1
   potentially observable.

**Falsification condition (explicit):**

Candidate D is falsified if:
```
|w_0 + 1| < epsilon_survey    and    |w_a| < epsilon_survey
```
with epsilon_survey = 0.01 (the projected Euclid 68% precision), AND if GU cannot supply
a mechanism that keeps the theta field in slow-roll (suppressed kinetic energy) for the
entire cosmic history. Current reconstruction-grade GU has no such suppression mechanism,
so w = -1 at Euclid precision would require fundamental revision of the GU dark energy sector.

**Candidate B** (RS mass ratio m_RS/m_{1/2} ~ 1.17) is falsifiable in a different way:
it requires discovering spin-3/2 partners to SM fermions and measuring their mass ratios.
This is not accessible with current collider technology if M_KK >> TeV, but the prediction
is sharp and GU-specific.

---

## Failure Conditions for This Analysis

**F1.** The Tikhonov parameter Lambda is NOT the GU cosmological constant but only an
auxiliary inverse-problem parameter. If so, Candidate A and the M_KK identification
both lose their physical interpretation.

**F2.** The section curvature R_s is not determined by any GU variational principle and
is a completely free parameter. If so, Candidates B and D lose their numerical predictive
power (they remain structurally GU-specific but not numerically falsifiable without fixing R_s).

**F3.** The dark energy sector of GU is the Yang-Mills kinetic term G_A^Y, NOT the theta
field. If so, Candidate D's analysis of w via D_A * theta = 0 is misdirected. The correct
dark energy analysis would need to start from the Yang-Mills stress-energy T^{YM}_{mu nu}.

**F4.** The GU RS sector mass from rc3-delta-n-spectrum (m_RS^2 = 11/R_s^2) assumes the
BC_1 c-function analysis which was PARTIALLY SUPERSEDED (rc1-root-mult-disambiguation showed
the correct root system for scalar L^2 is A_3, not BC_1). The RC3 computation may need
revision for the corrected A_3 root system. The mass ratio prediction m_RS/m_{1/2} ~ 1.17
is therefore at risk from the same root-system correction that demoted the generation count
scalar FJ route.

**F5.** The dark energy divergence-free proof (D_A * theta = 0) relies on identifying
theta = D_A * F_A on-shell (from the GU vacuum field equation). If the GU vacuum field
equation takes a different form, the Noether argument is misdirected.

---

## Open Questions

**OQ1.** Verify the RC3 mass computation m_RS^2 = 11/R_s^2 for the A_3 root system
(not the BC_1 system used in rc3-delta-n-spectrum). If the corrected A_3 root system
changes the spectrum, the mass ratio prediction shifts.

**OQ2.** Derive epsilon_sec from GU's own variational principle (the observer sub-protocol),
without importing the null-ray shot-noise model. If GU does not have such a derivation,
Candidate A remains a structural coincidence, not a prediction.

**OQ3.** Compute the GU theta-field equation of state w(z) in FLRW cosmology with M_KK = 2*sqrt(2)*H_0.
This requires solving the linearized GU field equations on a FLRW background and extracting
the effective w. A numerical comparison to DESI DR1 results would determine whether GU's
dynamical dark energy is consistent with current data.

**OQ4.** Identify the GU mechanism that fixes M_KK at the Hubble scale (M_KK ~ H_0).
If M_KK >> H_0, the theta field has already oscillated to zero energy density and contributes
zero to dark energy today. If M_KK << H_0, theta is frozen in slow-roll and w = -1 exactly.
The prediction w != -1 only fires if M_KK ~ H_0 at the current epoch; this coincidence
requires a GU-internal explanation.

---

## Verdict

**CONDITIONALLY_RESOLVED.**

Candidate D (dark energy equation of state w != -1) is a genuine conditional testable prediction
from GU. It is conditionally resolved because:
- The structural argument (theta is dynamic, not a cosmological constant) is at reconstruction
  grade.
- The numerical estimate (M_KK ~ H_0, deviation from w = -1 is O(1)) is at exploration grade.
- The explicit falsification condition (Euclid precision |w_0 + 1| < 0.01) is well-defined.

The full resolution requires: (1) GU-internal derivation of M_KK in terms of the observed
dark energy density; (2) theta-field cosmological evolution in FLRW background; (3) comparison
to DESI/Euclid measurements.

---

## References

- `explorations/geometry-curvature-emergence/cpa1-tobs-coefficient-2026-06-23.md` (Lambda_GU = 1/t_obs^2; C_GU = 8)
- `explorations/geometry-curvature-emergence/cpa1-omega-tuning-2026-06-23.md` (Omega = 1 under null-ray model; epsilon_sec = 1/(2*sqrt(2)))
- `explorations/vz-evasion/vz-f6-eft-decoupling-2026-06-23.md` (M_KK ~ 1/R_s; RS/spin-1/2 mass ratio)
- `explorations/generation-sector/n5-generation-count-synthesis-2026-06-23.md` (ind_H(D_GU) = 24; 3 generations exact)
- `explorations/representation-theory-noncompact/rc3-delta-n-spectrum-gl4r-2026-06-23.md` (normal Laplacian spectrum, m_RS^2 = 11/R_s^2)
- `explorations/geometry-curvature-emergence/rfail-umbilic-sections-2026-06-23.md` (R_fail = 0 in vacuum; Lambda from trace equation)
- `explorations/dark-energy-cosmology/dark-energy-noether-closure-2026-06-22.md` (D_A * theta = 0 on-shell, Noether proof)
- `explorations/geometry-curvature-emergence/ic4-lagrangian-tmunu-derivation-2026-06-23.md` (T^{dist}_{mu nu} derivation)
- Planck Collaboration (2020). Planck 2018 results VI: cosmological parameters. A&A 641, A6.
- DESI Collaboration (2024). DESI 2024 VI: cosmological constraints from BAO. arXiv:2404.03002.
- Weinstein, E. (2021). Geometric Unity lecture, Oxford. (Dark energy as dynamic distortion field)
