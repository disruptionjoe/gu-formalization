---
title: "K2330 Microscopic Kerr approximation over the complete readout"
status: active_research
doc_type: exploration
created: "2026-10-30"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no empirical, hardware or native GU acceptance
scripts:
  - tests/channel-swings/k2330_microscopic_kerr_validity_probe.py
---

# K2330 Microscopic Kerr approximation over the complete readout

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `CONVENTIONAL_COMPARATOR`.

```gu-typed-objects
result: K2330
carrier: finite total-excitation Jaynes-Cummings cavity, reference mode and neutral register LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and full-channel trace distance ON=declared_carrier
real_structure: real covariance or complex adjoint as explicitly declared
grading: total excitation including the two-level atom and its dressed branches
action_owner: repository-construction -- supplied rotating-wave Jaynes-Cummings model and explicitly priced controls/noise
target: finite-shell spectral approximation, accumulated compiler error and dressed-control interface MAP-TYPE=evaluation
```

## Result and scope

[K2328](k2328-local-neutral-readout-compiler-2026-10-30.md) assumes an exactly quadratic Kerr spectrum and independently supplied controls. A specific microscopic rotating-wave model exposes what that assumption costs: its exact lower dressed spectrum is not quadratic, a small dispersive parameter alone does not certify a long compiler, and bare optical control and loss operators do not become ideal dressed number/hopping operators automatically. We derive uniform error certificates, finite-difference lower bounds for all quadratic fits, and an explicit dressed-channel comparison. We also identify an exact-frequency repair that needs a new control analysis.

This is a conditional analysis of the supplied Jaynes-Cummings (JC) model, itself an effective rotating-wave approximation. It is not a measured device, all-cavity impossibility, hardware-feasibility verdict, or native GU quantization. Source SC-ACT-01/GEO-55/COS-50/51/54 ASSERTS and SC-META-53 UNCERTAIN, ledger0.263 and earlier conditional results remain unchanged. Exact dressed k-body expansions are established prior art; see [Smith, Bhattacharya and Masiello](https://arxiv.org/abs/2103.07571). Our use is the finite-shell error account for this particular readout interface, not a novelty claim.

## Exact carrier and diagonalization

Set hbar=1, Delta>0 and g>0. In a cavity-rotating frame let

    H_JC=Delta |e><e|+g(a_P sigma_+ +a_P^dagger sigma_-).

The mediator atom is distinct from every neutral flag/register qubit. Controls used below preserve the mediator's bare g/e labels apart from the JC drift; arbitrary mediator sigma_x gates are not included. The reference mode R is protected in the ideal Hamiltonian. The conserved hard charge is Q=n_P+n_R+|e><e|<=N, not bare photon number. In the n>=1 pilot-plus-atom excitation block {|n,g>,|n−1,e>}, H_JC has matrix [[0,g sqrt(n)],[g sqrt(n),Delta]] and eigenvalues

    E_n=(Delta−sqrt(Delta²+4g²n))/2,
    E_n^+=(Delta+sqrt(Delta²+4g²n))/2.                       (1)

E_0=0. Define theta_n=(1/2)atan(2g sqrt(n)/Delta), c_n=cos theta_n, s_n=sin theta_n,

    |n,−>=c_n|n,g>−s_n|n−1,e>,
    |n,+>=s_n|n,g>+c_n|n−1,e>.

The direct-sum rotation U maps bare labels to these dressed vectors. On the complete Q<=N carrier,

    rho=||U−I||<=max theta_n<=g sqrt(N)/Delta.              (2)

This is a norm bound, not a claim that a physical encoding U has already been implemented.

## Uniform Taylor remainder and exact compensation

For x>=0, E''(x)=2g^4/(Delta²+4g²x)^(3/2) and E^(3)(x)=−12g^6/(Delta²+4g²x)^(5/2). Taylor's integral remainder gives

    E_n=−g² n/Delta+g^4 n²/Delta³+R_n,
    −2g^6 n³/Delta^5 <= R_n <= 0.                          (3)

To obtain H_K=chi n(n−1)/2, chi=2g^4/Delta³, add c_comp n with c_comp=g²/Delta−g^4/Delta³ and n=n_P+|e><e|. This joint cavity-and-atom frequency shift commutes exactly with H_JC. A cavity-only shift c_comp n_P is not this operator: it changes detuning and has dressed off-diagonal entries. Its mismatch must be separately controlled; no free exact linear correction is assumed.

On the lower branch after this specified compensation,

    ||H_exact−H_K||<=delta_N=2g^6 N³/Delta^5.               (4)

For duration T, Duhamel gives a unitary norm error<=T delta_N, and hence half-diamond distance of the induced unitary channels<=T delta_N (capped by1). A uniform spectral fit is a sufficient certificate; a large bound is not a proof that the physical error is large.

K2328's nominal Kerr revival is Tchi=2pi/chi=pi Delta³/g^4. Its residual phase is exp(-iR_n Tchi), rather than identity. One revival costs at most

    Tchi delta_N=2pi(g/Delta)²N³.                          (5)

M such pauses cost at most M times(5), and every active hopping/query interval contributes its duration to T in(4). Thus g sqrt(N)/Delta small does not by itself prove the compiler accurate. It can be made arbitrarily small while N³(g/Delta)² is large. This exposes a missing bound, not a universal no-revival theorem: phase wrapping, accidental finite commensurabilities, fitted coefficients and changed pulses remain possible.

## Lower bounds against every fitted affine or quadratic spectrum

For any h>=1 integer with2h<=N, the second finite difference has the integral representation integral_[0,h]^2 E''(u+v)du dv. Since affine fits have zero second difference, every affine fit on0..N has maximum energy error at least

    g^4 h²/[2(Delta²+8g²h)^(3/2)].                         (6)

Similarly, for3h<=N the third difference is integral_[0,h]^3 E^(3)(u+v+w)du dv dw<0. A quadratic fit has zero third difference and the coefficient absolute sum is8, hence every quadratic fit has maximum energy error at least

    3g^6 h³/[2(Delta²+12g²h)^(5/2)].                       (7)

These are energy-norm bounds, including arbitrary constant/linear shifts and a refitted Kerr coefficient. They are not channel-distance lower bounds at arbitrary times: phase wrapping matters. N<=2 permits an exact quadratic spectral interpolant, and N<=1 an affine one. Nonzero third difference on four populated levels settles the exact-quadratic question without a numerical fit or long simulation.

## Bare controls and microscopic loss on the same carrier

Let C(t) be a specified bounded bare control on Q<=N that preserves the lower/upper LABEL blocks before dressing; on lower labels it implements the intended K2328 control, and a stated upper-label extension completes it. Hopping between P and R and neutral-only gates have such a block extension. In the dressed representation the actual control is U^dagger C U, so

    ||U^dagger C U−C||<=2rho ||C||.                        (8)

This bounds both within-branch mismatch and offbranch leakage. The sharper accumulated contribution is integral||U^dagger C U−C||dt. Neutral-register-only gates commute with U exactly and contribute zero to that term; separating commuting controls permits replacing C by its noncommuting part in the upper bound. Their physical duration still contributes to spectral and noise errors. Compare on the whole carrier, choosing the ideal upper drift to equal its exact dressed value and retaining the exact compensation there. The ideal lower drift is H_K; starting in lower labels, ideal controls preserve it. Duhamel then gives

    e_H <= T delta_N+2rho integral_0^T ||C(t)||dt.          (9)

All actual controls must be included in C, including sensing, dispersive pauses, timing/phase controls and implemented compensation errors; the exactly commuting joint compensation is already in the drift. Additional perturbations add integral||Delta H||. If a physical desired control has not been specified with such an extension, (9) is not an implementation claim. A supplied exactly dressed controller could remove the conjugation term, but would be a different hardware assumption.

Bare encoding/readout versus dressed encoding adds at most rho for each endpoint channel comparison, hence at most2rho if both endpoints are changed. Physically realizing dressing is a separate cost, not a free reset operation.

For example the projected bare pilot number is

    <n,−|n_P|n,−>=n−s_n²,
    <n,+|n_P|n,−>=c_n s_n.

It is not the excitation label n. A physical dispersive pulse coupling to n_P therefore has both a number error and offbranch coupling. The photon annihilation operator obeys

    a_P|n,−>=alpha_n |n−1,−>+beta_n |n−1,+>,
    alpha_n=sqrt(n)c_n c_(n−1)+sqrt(n−1)s_n s_(n−1),
    beta_n=sqrt(n)c_n s_(n−1)−sqrt(n−1)s_n c_(n−1).        (10)

Set c_0=1,s_0=0. At n=1 the absent upper0 state has zero coefficient. For higher n the upper-branch term need not vanish. Also [n_P,H_JC]=g(a_P^dagger sigma_-−a_P sigma_+) is nonzero. Neither scalar no-jump attenuation gamma n nor a commutation assertion about a full nonlinear dissipator transfers from an ideal Kerr model.

A safe alternative compares the complete microscopic noisy channel to the ideal LOSSLESS instrument. With specified Markov cavity jump sqrt(kappa)a_P and atomic jump sqrt(Gamma)sigma_-, the hard-carrier half-diamond generator bounds are kappa N and Gamma. Duhamel and contractivity add

    e_noise <= (kappa N+Gamma)T.                          (11)

Reference loss or neutral noise adds its own bound. No transformed no-jump cancellation is needed. Total excitation decreases under these jumps and remains inside Q<=N; a pumping/leakage process would require a different carrier. Together with K2328's selective/echo/compiler error and full input error, (9)-(11) bound the complete recorded instrument, including false flags. There is no exact heralded survival or conditional-normalization claim.

## Follow-through: a sufficient region and an exact-frequency repair

Let T be the ACTUAL complete duration from the declared compiler, including integer-revival waits, routing, query and reset. The conditional comparison closes if

    e_input+e_K2328+e_endpoints+T delta_N
      +2rho integral||C||dt +(kappa N+Gamma)T
      +integral||Delta H||dt <= epsilon.                 (12)

Here chi is constrained to2g^4/Delta³; it is no longer independently tunable from g and Delta. Increasing Delta suppresses local remainder but increases Tchi as Delta³. The relative phase per revival scales as(g/Delta)²N³, and the noise per revival scales as(kappa N+Gamma)pi Delta³/g^4. Those opposite tendencies must be solved together on the SAME device. Equation(12) is sufficient, often very conservative; failing it does not establish infeasibility or an optimal noise floor. No measured rates or huge-N implementation is claimed.

A concrete repair preserves the microscopic model while abandoning the nominal quadratic drive. Define transition frequency omega_n=E_n−E_(n−1)+c_comp. Exact neighboring spacings are

    omega_(n+1)−omega_n=E_(n+1)−2E_n+E_(n−1)>0,
    >=2g^4/(Delta²+4g²N)^(3/2) for1<=n<N.                (13)

This follows from the positive second-derivative integral over the centered unit square. Hence the lower-to-lower transition frequencies on a finite shell are distinct, with nonuniform gaps. This is a necessary spectral ingredient; physical selective addressability still requires the full coupling and upper-branch collision analysis. Retuning each carrier to omega_n removes the wrong resonant frequency; it does not restore full Kerr revivals, ideal hopping matrix elements or branch-preserving jumps. A new averaging theorem using these exact frequencies, actual alpha_n matrix elements, upper-branch detunings, and physical idle phases is the next concrete repair. It must price possible spectral collisions with upper branches and other device modes. Adding an unconstrained ideal dressed gate is not that proof.

## Verification boundary

The probe checks characteristic polynomial, derivatives and compensation exactly; finite-difference annihilation and integral constants; explicit finite JC blocks, transformed number and annihilation matrices, noncommutation, and nominal-revival residuals. High-precision finite fixtures are numerical controls, not universal certificates. Changed coefficients/operators/gaps/compensation must fail clean evaluators; no boolean truth flag is a mutation. The written Taylor, finite-difference and Duhamel arguments supply general bounds. Independent specialist review must check the common carrier and full control/jump comparison, since spectrum-only checks cannot establish(12).

Next build the exact-frequency, dressed-matrix-element controller or instantiate a specific device's rates/noise and test(12). Do not repeat abstract controllability or treat a small dispersive parameter as the completed error account. Native curved field/receiver jets and the common analytic domain remain a separate construction.
