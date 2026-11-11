---
title: "BET-COSMOLOGY: fixed potentials, acoustic calibration and a nuisance-dependent survivor"
status: active_research
doc_type: exploration
created: "2026-11-11"
program_target: BET-COSMOLOGY
tier: T2
expected_delta: "First two fixed-potential acoustic/BAO tests; bound initial-time and calibration transfer."
actual_delta: "Cosine scalar retains a nonmimic diagnostic state after equal matter-prior profiling; central-input exclusion does not persist. Bet remains active, with no GU or full-CMB claim."
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: "Two speculative scalar actions and declared compressed data model only; no source or matrix inference."
scripts:
  - tests/program-focus/bet_cosmology_fixed_potentials_probe.py
---

# Fixed potentials, acoustic calibration and the matter-prior fork

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: BET-COSMOLOGY fixed potentials and calibrated scalar backgrounds
carrier: real scalar on flat four-dimensional Lorentzian FLRW with dust and radiation LAYER=toy CHIRALITY=N/A
pairing: positive scalar kinetic energy and positive survey covariance ON=declared_carrier
real_structure: real scalar, homogeneous initial position and momentum
grading: no native Clifford or chirality grading transferred
action_owner: repository-construction -- two SPECULATIVE canonical scalar actions
target: acoustic distance and thirteen compressed BAO distances MAP-TYPE=evaluation
```

## Native research bookends

- program_target: BET-COSMOLOGY
- tier: T2
- expected_delta: a common-calibration test of two fixed potentials, including early-history and nuisance controls.
- actual_delta: a nonmimic cosine state survives the compressed-prior diagnostic; the bet remains active without a full-CMB or source claim.

## Result and scope

Two **SPECULATIVE**, fixed-coefficient scalar potentials have acoustic-calibrated homogeneous states distinct from a cosmological constant. At central matter density both give worse DESI DR2 compressed BAO discrepancy than the equally calibrated ΛCDM control. But the cosine model's central difference does **not** persist above the bet's threshold after both models receive the same approximate Gaussian matter-density prior and nuisance profiling. Its numerical comparison is Δχ²≈4.13 with w(0)≈−0.845. This is a conditional diagnostic survivor, not an empirically allowed cosmology, full CMB calibration, source-derived scalar, or GU prediction.

The exponential comparison remains above threshold in these numerical tests. No all-initial-state, all-potential or bet closure follows. Finite root scans and floating-point optimization are not global certificates. The bet stays active. No lane-C result enters the constraint matrix or ledger.

**Preflight:** target BET-COSMOLOGY; T2; expected delta a first common-calibration confrontation of fixed structural potential shapes; kill condition the bet's Δχ²≥10 or |w0+1|<0.1 criterion, requiring its full scope and acceptance before closure. **Postflight actual delta:** a nuisance-sensitive nonmimic diagnostic state, an explicit physical-unit pipeline, and analytic acoustic/early-tail bounds; no kill.

## 1. Source boundary and prior work

SC-COS-50 **ASSERTS** a variable dark-energy term with the conditional “if it continues” DESI clause; SC-COS-51/52 **ASSERTS** an ad-valued one-form construction; SC-COS-54 **ASSERTS** a movable-field relation without specifying the action or which curvature field. SC-COS-02 **DISAVOWS** attribution of the phrase “dark energy” to the written 2021 draft. Read the full [source entries](../../lab/sources/source-claim-register.yaml). Neither a scalar potential nor its reduction from that one-form is supplied there. These scalar actions are admitted speculative comparators only. Calling them collective modes does not build that missing map.

The [canonical correction record](../../canon/theta-field-flrw-dark-energy-eos.md), DARK-ENERGY-02 through -06, already corrects the local-versus-fitted CPL sign, the uncalibrated distance amplitude and the original quadratic model's mass-band scope. H46C/W129 own that quadratic oscillator test. We do not repeat it or overturn its scoped results. [K2274](k2274-desi-fixed-family-test-2026-10-29.md) owns a different fixed metric-action/initial-data BAO bound and its slope escape. The present elementary scalar models are conventional research tools, not a novelty claim. Ledger0.263 LT-GR2b–e retain their complete mapping grades; LT-GR2e remains NEEDS.

## 2. Exactly what is frozen and calibrated

On the observed metric with signature (−,+,+,+), take

    S = integral sqrt(-g)[Mpl² R/2 - (∂phi)²/2 - V(phi)] + S_dust + S_radiation.

Mpl is the reduced Planck mass. Put x=phi/Mpl, p=phidot/(Mpl H100), H100=100 km s^-1 Mpc^-1 and U=V/(3 Mpl² H100²). Fix before outcomes

    omega_m=.1430,
    omega_r=2.4728e-5 (1+.2271*3.046), h_ref=.6736,
    U*=h_ref²-omega_m-omega_r,
    EXP: U(x)=U* exp(-sqrt(2) x),
    COS: U(x)=U* (1+cos x), f=Mpl.

There is no additive Λ and no potential coefficient or slope tuning. The reference normalization is explicitly imported, not predicted. It stays fixed when matter density is varied. The cosine has a periodic potential; the continuous shift symmetry is broken to discrete shifts. Its pi/2 control starts at an inflection point, not the hilltop.

At a_i=10^-6 set p_i=0 and calibrate only x_i against the acoustic angle. The exponential's field shift is physically degenerate with changing its amplitude, so this is an effective amplitude calibration with **no scale-prediction credit**; the fixed action is not claimed to force x_i. The cosine's initial angle changes energy and slope within its fixed action. There is no BAO adjustment of x_i or of potential coefficients. h is an output of the solution. It is never rescaled after solving the acoustic equation.

Use 100theta*=1.04110, r*=144.43 Mpc, z*=1089.92 and r_d=147.09 Mpc, the same Planck column as the earlier test. This is a **compressed acoustic-distance condition**, not a Planck temperature/polarization/lensing likelihood. The matter prior below likewise omits joint correlations. Standard redshift, flat optics, photon-baryon sound propagation and the applicability of DESI's compressed Gaussian BAO likelihood are assumptions.

EXP uses the endpoint bracket [-2,3]; COS uses [0,pi]. An endpoint-bracketed numerical root is the declared branch, independent of BAO. A 65-point cosine scan detects one sign-changing bracket, not a proof that all roots exist only there. The frozen hilltop is exactly constant energy 2U*; the minimum is the dust/radiation control. They provide independent endpoints.

## 3. Actual dynamics, not a separately fitted Hubble normalization

For N=log a,

    q=H²/H100²=omega_m e^(-3N)+omega_r e^(-4N)+p²/6+U(x),
    x_N=p/sqrt(q),
    p_N=-3p-3U_x/sqrt(q),
    rho_phi=p²/6+U,  rho_phi,N=-p²,
    q_N=-3omega_m e^(-3N)-4omega_r e^(-4N)-p².

The Klein–Gordon equation gives the first two equations; direct differentiation proves both last identities. This physical-unit parametrization avoids dividing by 1−x_N²/6 when enforcing Friedmann. The saved script checks the algebra symbolically and solves the actual system with DOP853 and an independent RK45 comparison.

    D_M(z)=(c/H100) integral_(-log(1+z))^0 e^(-N)/sqrt(q(N)) dN,
    D_H(z)=(c/H100)/sqrt(q(z)),
    D_V(z)=[z D_M(z)² D_H(z)]^(1/3),
    h=sqrt(q(0)), w=(p²/6-U)/(p²/6+U).

All thirteen BAO observations use one shared drag ruler. The full covariance, including each DM/DH anticorrelation and the final Ly-alpha DH-before-DM order, is retained. No CPL fit substitutes for these observables. No sigma or p-value is assigned to Δχ².

## 4. Potential-independent acoustic ordering and its limitation

At fixed present h, matter, radiation and positive scalar energy, conservation gives rho_phi(z)≥rho_phi(0) for every z≥0. Thus H_scalar(z)≥H_LCDM_same_h(z), so D_scalar(z*)≤D_LCDM_same_h(z*). The latter distance is strictly decreasing with h: its integrand denominator contains q_LCDM=omega_m(1+z)^3+omega_r(1+z)^4+h²−omega_m−omega_r. Hence equal **fixed** acoustic distance implies

    h_scalar <= h_LCDM,

strictly if rolling occurs on a set of positive measure along the integration interval. This proves why an upward-H0 repair is unavailable under these assumptions; it does not prove any BAO χ² threshold. Phantom kinetic sign, energy exchange, nonminimal gravity, changed optics or a changed early ruler invalidate the premise. No source-wide conclusion follows.

Canonical scalar perturbations have positive unit kinetic and gradient coefficients and principal c_s²=1; V'' can still produce a tachyonic mass term. EXP has V''>0; COS has V''<0 near its hilltop and can roll through the inflection. These statements exclude a local principal ghost/gradient problem in this declared model, not all instability, primordial-spectrum or CMB difficulties. Matter perturbations, initial perturbation state, lensing and recombination are not calculated here.

## 5. A full early-integral bound, despite possible early kination

A small scalar fraction at recombination alone would not bound its earlier history. In particular, extending a finite frozen initial condition backward need not remain frozen. For either smooth nonnegative potential,

    rho_N=-p²,  0<=p²<=6rho,
    rho(a)<=rho_i (a_i/a)^6  for 0<a<a_i,
    rho(a)<=rho_i            for a_i<=a.

The backward bound follows by integrating d log rho/dN≥−6 with the integration orientation reversed. Also |x_N|≤sqrt(6); rho is bounded on every finite backward N interval. Positive radiation and smooth potentials therefore permit continuation to every a>0, without asserting regularity at a=0.

Hold the recombination/drag scale factor fixed, and compare with the **same** dust/radiation background without scalar energy. Since c_s≤1/sqrt(3), q_b≥omega_r a^-4, and beta=a_i³ sqrt(rho_i/omega_r), the missing early contribution to the sound horizon obeys

    0 <= delta r_early
      <= c/(H100 sqrt(3omega_r))
         [a_i - sqrt(a_i²+beta²) + beta]
      <= c beta/(H100 sqrt(3omega_r)).

Indeed its integrand is bounded by c/(H100 sqrt(3omega_r)) times [1−a/sqrt(a²+beta²)], whose integral is the displayed expression. Pure stiff energy against radiation saturates the comparison algebra. This is a bound on an integrated deficit, **not** uniformly small early scalar density.

For a_i<=a<=a_event, epsilon=rho_i/[omega_m a_event^-3+omega_r a_event^-4] bounds rho/q_b. The inequality 1−(1+t)^(-1/2)<=t/2 gives delta r_late<=epsilon r_base/2. Use each event's own epsilon and the independently integrated no-scalar r_base. The saved report adds the early and late bounds for both events. These bounds do not cover changes in recombination/drag times, baryon physics, a primordial spectrum or BBN. They justify a small *background integral* correction only. Initial-time controls at 10^-5,10^-7 and10^-9 are numerical sensitivity tests, not a proof of a regular big-bang branch.

A conservative **analytic uniform raw-ruler bound** avoids reliance on a floating calibrated root. Across the stated initial brackets and matter scan, U*<1/3, EXP initial energy<(1/3)exp(2sqrt2)<7 and COS energy<2/3<7. Both event scale factors are <.001, omega_m>.13, omega_r>4e-5 and c/H100<3000 Mpc. Hence epsilon<7/(1.7e8), the raw baseline ruler is <274 Mpc, and the late deficit is <5.65e-6 Mpc. With a_i=1e-6 the tail is <1.2e-10 Mpc. Therefore the total raw fixed-event deficit is **<6e-6 Mpc** for every bracket state, including possible earlier kination. The elementary bound exp(3)<21 supplies the exponential estimate; exact rational square/ceiling checks support the remaining inequalities. This is a raw background-integral theorem. A ruler normalized to a Planck anchor needs its explicit normalization factor; no exact observational ruler or event time is inferred.

## 6. Central data and released nuisance successor

Primary inputs: [Planck 2018](https://arxiv.org/abs/1807.06209), [DESI DR2 BAO](https://arxiv.org/abs/2503.14738), and the immutable [mean](https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt)/[covariance](https://raw.githubusercontent.com/CobayaSampler/bao_data/bb0c1c9009dc76d1391300e169e8df38fd1096db/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt) inputs. These are the specified datasets, not a claim about the newest cosmological release. The already-owned H46 module supplies the numerical vector/covariance; its exact code digest is saved. Its old interpretation and approximate background solver are not imported.

Central compressed-calibration results (floating diagnostics):

| Model | h | w(0) | chi2_BAO | delta versus same calibrated LCDM |
|---|---:|---:|---:|---:|
| LCDM | 0.67279616 | -1 | 32.335870 | 0 |
| EXP | 0.62473664 | -0.72377179 | 77.224948 | 44.889078 |
| COS | 0.64681826 | -0.83119596 | 47.565014 | 15.229144 |

The absolute LCDM offset from h_ref is retained. An alternative target computed from the reference LCDM model is **re-solved**, with its own matched control, rather than correcting h afterward. Central differences remain approximately43.73/14.53 in that alternative convention.

The first finite matter scan placed both scalar minima on its lower boundary. The released successor extends n=(omega_m−.1430)/.0011 to [-6,3], adds n² to every model, and searches continuous interior numerical minima. The first ruler approximation is (omega_m/.1430)^(-1/4). The independent sensitivity calculation uses

    r_s(a_event)=c/(H100 sqrt3) integral_0^a_event
       da / sqrt[(omega_r+omega_m a)(1+3omega_b a/(4omega_gamma))],

with omega_b=.02237 and fixed z_drag=1059.94. Its ratios across omega_m are normalized to the same central Planck rulers; the absolute integral values are recorded. This is a dust plus massless-radiation approximation, not a massive-neutrino or recombination solver. No claim that shared approximations cancel to a proved order is made. Both models recalibrate their initial state at each nuisance point, and U* stays fixed.

Sound-integral-ratio numerical minima:

| Model | n | total chi2_BAO+n² | w(0) | delta total |
|---|---:|---:|---:|---:|
| LCDM | -2.224660 | 17.758982 | -1.00000000 | 0.000000 |
| EXP | -3.815895 | 39.277311 | -0.70965919 | 21.518329 |
| COS | -2.938140 | 21.888394 | -0.84467088 | 4.129412 |

The quarter-power sensitivity gives Δχ²≈21.92/4.28, consistent at this diagnostic level. COS is still nonmimic by the bet's |w0+1|≥0.1 criterion. Its favorable state pays a roughly three-standard-deviation penalty in this **approximate single Gaussian prior**. The full correlated CMB likelihood could change the comparison. The bounded optimizer and grid do not certify global minima, uniqueness or all allowed states. These results therefore do not establish the bet's complete CMB-consistent acceptance or its kill criterion.

## 7. Reproducibility, uncertainty and next condition

Run `python tests/program-focus/bet_cosmology_fixed_potentials_probe.py`. Use `--write-report` only to regenerate [the evidence](../../lab/process/bet-cosmology-fixed-potentials.json). The no-write replay compares all scientific fields, including nuisance minima, bounds, calibration and numerical controls, plus script/data hashes. Environment versions are recorded separately. Algebraic identities and the written analytic inequalities are proofs; ODE integration, quadrature, finite scans, bounded optimization and their tolerance checks are numerical evidence. The report separates supporting checks from contrary controls; the count is not a count of independently proved cosmologies.

The independent integrator agrees on the primary and optimized diagnostics. Controls expose uncalibrated starting points, lost covariance, wrong observation order, phantom energy-sign transfer and the false inference from small recombination fraction to uniformly small early density. No full CMB/SNe run, remote-CI, Lean or external certification is claimed. Specialist and hostile review independently inspected the argument and transfer assumptions.

For a residual with chi2=c, an additional whitened model-vector error of norm at most e changes it within [(sqrt(c)−e)_+²,(sqrt(c)+e)²]. For the central comparisons the saved equal-radius threshold follows from (sqrt(c_scalar)−e)²−(sqrt(c_LCDM)+e)²=10. This quantifies a **required** error bound, not a measured bound on omitted physics. Numerical integrator errors are far smaller; full physical calibration errors are not supplied by this computation.

The next cosmology condition is a fully specified perturbation/initial-state and early-physics treatment with a joint CMB likelihood (and then independent SNe), on these same fixed potentials and declared initial-state family, or a separately frozen structurally different action on a later bet turn. Do not tune either potential to BAO, declare full CMB agreement from theta*, repeat the old quadratic band test, or export this lane-C result into the matrix. Current program_focus governs subsequent work. The scalar-to-source one-form/action/observation bridge remains absent regardless of the cosmological outcome.
