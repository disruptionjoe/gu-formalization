---
title: "K2273 Positive nonlinear pulses and moment-qualified energy"
status: active_research
doc_type: exploration
created: "2026-10-29"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional supplied model only; no source or canonical verdict
scripts:
  - tests/channel-swings/k2273_positive_control_energy_probe.py
---

# K2273 Positive nonlinear pulses and moment-qualified energy

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or borders a conventional particle-physics comparator. Any result about a standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126` Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-mass route binds only that named model. It is not evidence for or against Weinstein's source-native mechanism without an explicit typed bridge. Read `lab/methods/source-native-comparator-routing.md` and follow its source-native pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: K2273 Positive nonlinear pulses and moment-qualified energy
carrier: ordinary finite-mode bosonic Fock space and finite neutral records LAYER=toy CHIRALITY=N/A
pairing: positive complex Hilbert inner product and spectral measure ON=declared_carrier
real_structure: real coefficients and complex Hilbert adjoint where applicable
grading: no native chirality or Clifford grading transported
action_owner: repository-construction -- supplied conditional model
target: positive pulse compilation and energy continuity under explicit moments MAP-TYPE=intertwiner
```

## Result and scope

Every signed primitive in [K2270](k2270-untruncated-detector-control-2026-10-29.md)'s nonlinear conserving alphabet can be replaced by a finite list of positive instantaneous generators, preserving its whole-Fock unitary up to a harmless scalar phase. Integer spectral periodicity removes negative Kerr and cross-Kerr pulses. Explicit number moments then price mean/RMS control energy and qualify what channel error says about free-energy error.

The positive shifted-hopping trick is ALREADY in [K2225](k2225-positive-drift-detector-control-2026-10-28.md); it is reused here. The new endpoint is its extension to the full nonlinear universal alphabet and composition with K2272's prepared stock and higher-moment estimates. This is supplied ordinary positive Fock space, not native GU physicalization. SC-META-53 stays UNCERTAIN, ledger0.263 and LT-SM8/LT-GR6b unchanged. There is no affordability, autonomous clock, reservoir renewal, source-spectrum resolution or novel control theorem claim.

## 1. Integer spectra remove the negative nonlinear generators

In units hbar=1, each

    D in {n_i,n_i²,n_i n_j,P_l,n_i P_l}

is nonnegative selfadjoint with integer spectrum; P_l is a neutral coordinate projector. For any real signed area theta, choose r in [0,2pi) congruent to theta modulo2pi. Spectral calculus gives

    exp(-i r D)=exp(-i theta D)                         (1)

on the WHOLE Fock space. Neither a cutoff nor a uniform bounded operator norm is needed. The hypothesis is about the actual normalized spectrum: an uncalibrated coefficient or a half-integer spectrum cannot be silently reduced modulo2pi. Negative small angles may require almost2pi of positive area; this is an explicit extra duration/precision burden.

For X_ij=a_i†a_j+a_j†a_i, N_ij=n_i+n_j, its one-particle eigenvalues ±1 imply

    0<=B=N_ij+sgn(theta)X_ij<=2N_ij.

A positive pulse of area |theta| under B followed by positive onsite n_i,n_j pulses each of area r_N=(-|theta|) mod2pi gives exactly exp(-i theta X_ij), because N_ij and X_ij commute. This reuses K2225; omitting phase repair fails across different total-charge sectors.

For a normalized neutral adjacent flip Y with spectrum in {-1,0,1}, I+sgn(theta)Y>=0. A positive area |theta| produces exp(-i theta Y) times exp(-i|theta|), a global phase on the FULL neutral space. Applying the identity only to the flipped two-dimensional block would instead give a relative spectator phase and require repair. The identity here is genuinely the full identity.

Thus each primitive is replaced exactly before any approximation analysis. The reconstructed finite compiler, its low-sector error and complete recorded-channel target survive unchanged. Replacing every signed pulse does not certify a new global diamond approximation; the old finite comparison sector and input bounds remain. All generators have selfadjoint charge-block realizations as in K2270.

## 2. Positive pulses, added duration and retained drift

For any positive replacement B of area r>=0 and duration T>0 choose

    g(t)=2r/T sin²(pi t/T), 0<=t<=T.

Extend by zero. It is C1 at both endpoints and implements exp(-irB). Its peak, slope and total variation are

    max g=2r/T, max |g'|=2pi r/T², integral |g'|=4r/T. (2)

Zero-area pulses are omitted. A prescribed peak coefficient gmax and envelope slew smax can be met by

    T>=max(2r/gmax, sqrt(2pi r/smax)).                  (3)

Use the ACTUAL replacement list for total time and its old compiler accuracy allocation. There is no claim this enormous list is economical. Diagonal corrections each cost less than2pi; a hopping pulse requires at most three such sequential components including the original |theta| positive hopping area. Neutral flips require one component plus a tracked global phase.

The common free drift omega Ntot commutes with every conserving replacement. It therefore accumulates omega*T_new, not the old signed schedule's duration. Retain it in an explicitly calibrated rotating-frame comparison or repair its known phase with positive periodic number pulses. For an explicit laboratory repair, apply a common onsite number control to all modes for T_c after the other pulses of total duration T_new. Choose

    T_c>=max(4pi/gmax,2pi/sqrt(smax)),
    r=(-omega(T_new+T_c)) mod2pi in [0,2pi).

Simultaneous equal onsite sin² envelopes with area r obey each onsite peak/slew bound by (2), and their sum is the common Ntot control. Total drift plus repair is an integer2pi rotation. This uses allowed simultaneous onsite controls; a strict single-site-at-a-time restriction would require a different duration account. The new completion is finite under any positive supplied gmax,smax, but may increase total time substantially. Nonuniform unknown drift or implementation errors retain their separate K2270 projected analysis.

## 3. Which energetic quantities require which moments

Set G=Ntot+1. The replacement B commutes strongly with G and

    0<=B<=c_B G², B²<=c_B²G⁴,                         (4)

with c_B=1 for diagonal D and c_B=2 sufficient for shifted hopping and full-identity neutral flips. These inequalities follow shell by shell; they do not raise an arbitrary noncommuting operator inequality to a power. Ideal conserving dynamics preserve EVERY number moment.

For a state family with Tr(G²rho_t)<=M2 and Tr(G⁴rho_t)<=M4, (2)-(4) imply

    expected control energy <=2r c_B M2/T,
    RMS control energy <=2r c_B sqrt(M4)/T,
    |Tr(rho_t partial_t H_control)|<=2pi r c_B M2/T²,
    integral |Tr(rho_t partial_t H_control)|dt<=4r c_B M2/T. (5)

Sum the final bound over actual pulses. Multiply energies/work by hbar when restoring units. These are mean switching exchanges and energy moments in the declared model, not total engineering or thermodynamic costs. The conserved common-drift free energy contributes separately. Positive generators are still unbounded, so a peak coefficient is not a state-independent peak power.

Actual perturbations preserve these bounds only with additional evidence: exact total-number conservation, or a common-domain form estimate i[H_actual(t),G^p]<=kappa_p(t)G^p with justified differentiation and Gronwall, yielding Mp(t)<=Mp(0) exp(integral kappa_p). K2270's low-sector eta alone does NOT imply this. Its tiny-leakage-to-arbitrarily-high-energy counterexample remains valid.

A concrete normalized distribution p_n=6/[n(n+1)(n+2)(n+3)] for n>=1 has total mass1/3, with remaining mass2/3 at0. Its second number moment is finite but its fourth moment diverges. Thus finite mean Kerr energy does not imply finite RMS Kerr energy. A first-moment-only input bound is weaker still. K2272's coherent stock has finite explicit moments, but the input and adaptive controller moments require separate bounds. In particular (8) of K2272 alone does not assert (5) for an arbitrary adaptive process.

## 4. Sharp energy continuity under a UNIFORM moment budget

Let A>=0 be a positive observable, p>1, delta=D(rho,sigma) and

    Mp=max(Tr A^p rho,Tr A^p sigma)<infinity.

Measure A. The resulting probability laws have total variation at most delta. The positive and negative parts of their difference each have mass at most delta and are dominated by the corresponding original law. If the mean difference is positive, discard its negative contribution and apply Hölder to the positive part; reverse the roles if negative. Therefore

    |Tr A(rho-sigma)|<=Mp^(1/p) delta^(1-1/p).          (6)

There is no factor two. It is sharp: rho=(1-delta)|0><0|+delta|M><M| and sigma=|0><0| for A=N give Mp=delta M^p and equality. This example also proves that trace closeness without a UNIFORM Mp bound controls no unbounded-energy difference.

For free energy hbar omega N, p=2 gives hbar omega sqrt(M2 delta), where M2 bounds N² of BOTH compared states. Nonuniform finite-mode positive frequencies permit H0^p<=(hbar omega_max)^p N^p since these observables commute. This is not an assertion about noncommuting Hamiltonian forms. A channel bound can be inserted into (6) only after establishing both actual and ideal output moments, including any retained stock in the chosen A. Existence of finite moments separately at each mu is insufficient: K2272's mu grows rapidly, so Mp(delta) can overwhelm the improving channel error.

## 5. A finite-moment replacement for the lost capacity bound

For ONE vacuum detector input, one coherent stock of mean mu, no other charged donors and actual number-conserving dynamics with neutral fresh ancillas, the actual reference satisfies E(N_ref²)<=mu²+mu because N_ref<=Ntot and total-number moments are conserved. The ideal original coherent reference has the same second-moment bound. K2253's bounded field witness is

    mu_J=(64/25)[1-(16/25)^J], J>=1.

If epsilon_S is the actual field trace error and delta_B is reference marginal restoration error, positivity and charge conservation give mean reference loss at least [mu_J-2J epsilon_S]_+. Applying (6) to reference number therefore yields

    delta_B >= [mu_J-2J epsilon_S]_+²/(mu²+mu).        (7)

For J=1, mu_J=576/625. This is an untruncated, moment-based restoration obstruction, replacing neither the original finite-capacity theorem nor its hypotheses. Exact target and exact reference restoration remain incompatible. Equation (7) is not licensed for arbitrary nonconserving perturbations or controllers that import another charged resource. Its very small value at mu=10^28 is consistent with K2272's approximation; no optimality is claimed.

## Verification and next independent requirement

The probe checks actual integer/half-integer spectra, full finite charge-shell hopping matrices, missing phase and spectator-identity faults, exact pulse integrals and moment/tail arithmetic, plus saturation of (6). Universal spectral calculus, domain propagation and measure-theoretic continuity are written internally reviewed proofs, distinct from finite controls. No external-expert, Lean, hardware, novelty or remote-CI certification.

This removes negative nonlinear generators as an ideal-dynamics obstacle and supplies an honest energetic inference rule. It leaves the giant compiler, control calibration, phase source, finite clock, physical supply and output-moment conditions visible. The next useful implementation test must fix an affordable alphabet/time/precision/resource budget and prove its channel AND energetic errors together; another formal controllability extension cannot settle that question.
