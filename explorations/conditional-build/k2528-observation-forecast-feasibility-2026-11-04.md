---
title: "K2528 Observation forecast feasibility and high-redshift anchor repair"
status: active_research
doc_type: exploration
created: "2026-11-04"
classification: CONVENTIONAL_COMPARATOR
target_claim: NONE-NOT-A-KILL
claim_ceiling: specified forecast versus sufficient conditional certificate; no empirical or native GU exclusion
scripts:
  - tests/channel-swings/k2528_observation_forecast_feasibility_probe.py
---

# K2528 Observation forecast versus the actual decision criterion

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
result: K2528
carrier: specified high-redshift spectroscopic forecast and conditional common-momentum radial FLRW test emitters LAYER=toy CHIRALITY=N/A
pairing: proper-time spectral velocity differences and jointly calibrated reduced-distance differences ON=declared_carrier
real_structure: positive real expansion, real subluminal velocities and one shared calibration
grading: forecast marginal standard deviation, simultaneous band, source motion and native dynamics remain distinct
action_owner: repository-construction -- K2367 sourced metric action; no native connection-action identification
target: feasibility of the existing sufficient weak test and shifted-domain repair MAP-TYPE=evaluation
```

## 1. A specified configuration, not an achieved experiment

[Marques, Martins and Alves, 2023, section2 equations2–3](https://arxiv.org/pdf/2305.01446) forecast a twenty-year ANDES experiment with six quasars in each effective bin z=2,2.5,3,3.5,4.5 and S/N3000 per0.0125-Angstrom pixel. Their statistical error prescription is

    sigma_v=1.35 (3000/2370)^(-1) (6/30)^(-1/2)
                   ((1+z)/5)^(-lambda) cm/s,
    lambda=1.7 below z=4, 0.9 above z=4.

It yields 5.683145,4.372997,3.484921,2.852552,2.188731 cm/s. These are forecast marginal statistical errors, not measured continuous joint bands. [The ANDES team paper,2024, sections5–6](https://pmc.ncbi.nlm.nih.gov/articles/PMC11413136/) describes long-term cm/s calibration stability as a goal requiring further research. This dated specification is the tested configuration; no claim about subsequently achieved instrument performance is needed.

[K2526](k2526-geodesic-emitter-drift-repair-2026-11-02.md) requires low-redshift coverage, same-momentum radial geodesic emitters, reciprocity, an absolute distance anchor and simultaneous calibration/motion/curve bands. Its envelope covers observed X=1+z through[1,3/2]. The forecast bins start at X=3; even p=1/100 maps that endpoint to y=3/sqrt(1.06)>2.9, outside the certified y<=36/25 interval. Ly-alpha absorption-line drift does not provide the same moving emitter/candle distance population. The primary forecast supplies no joint distance uncertainty, motion certification or continuous interpolation bound. Its marginal sigmas cannot be turned into those missing inputs by assuming independent errors.

Consequently this configuration does not instantiate the existing certificate. This rejects an attempted use of the certificate, not the quadratic action, all observational tests or GU. SC-COS-50/51/54 ASSERTS, LT-GR2e and ledger0.263 remain unchanged.

## 2. Units expose the sufficient bound's cost

For the spectroscopic convention delta_v=c delta_z/(1+z),

    Q_phys=dot_z/(1+z)=dot_v/c,
    Q_dimensionless=Q_phys/H_ref,
    sigma_Q=sigma_v/(c T H_ref).

No extra(1+z) divisor belongs in the last line. K2522's finite-baseline remainders and K2524's common calibration still apply; this conversion alone supplies neither. For the explicitly illustrative H_ref=70km/s/Mpc and20 Julian years, c T H_ref=42.92419513cm/s. This H_ref is an imported unit example, not a derived or measured calibration for the action.

The inherited exact sufficient oscillation R*=7.11777130738e-11 corresponds to3.055246e-9cm/s. Even a perfectly flat nominal curve leaves uniform E_v<=1.527623e-9cm/s in osc(Qhat)+2E_Q<=R*. Forecast statistical scales exceed that illustrative per-point budget by roughly1.43–3.72billion. This is not a necessary instrumental sensitivity, a confidence calculation or an impossibility theorem: the certificate is conservative and sigma is not E. The coverage/tracer/input mismatch already prevents application without this numerical comparison.

## 3. Executed repair: use a high-redshift distance difference

An origin integral is unnecessary if two calibrated reduced distances are actually supplied. Keep K2526's same-p radial-geodesic class and define

    D_p(X)=sqrt(1+2pX), y_p(X)=X/D_p(X),
    DeltaC_p=L_b/D_p(X_b)-L_a/D_p(X_a)>0,
    L_i=D_L(X_i)/X_i,
    Q(X_p(y))=q-H(y)/y.

The SAME lightcone gives DeltaC_p=int_ya^yb dy/H(y), including both anchor correlations and Doppler factors. Let R=osc Q on the entire common observed interval and h_a=H(y_a)/y_a>0. Then H(y)<=y(h_a+R), so

    h_a>=log(y_b/y_a)/DeltaC_p-R.                    (1)

Choose X_a=3, X_b=9/2, p in[0,1/100]. Their ratio is

    y_b/y_a=(3/2)sqrt((1+6p)/(1+9p))>29/20>36/25.   (2)

The ratio decreases in p; at its right endpoint its squared excess over(29/20)^2 is3731/43600>0. Thus, if the full joint anchor band proves DeltaC_p<=1 in the fixed clock/distance units for EVERY trial p, h_a>=9/29-R, since log(29/20)>=9/29. Require 0<=R<9/29 before dividing by this lower bound. Set a=y_a, u=y/a, C=a h_a and htilde(u)=H(au)/C. Then on1<=u<=36/25,

    |htilde(u)-u| <= (36/25)R/(9/29-R).              (3)

The same R* from K2526 makes(3) at most the inherited K2522 eta*. This is a new domain/anchor composition using the existing certificate, not new precision from repeated algebra.

### Why the actual weak action test transfers

Write s=3log y, sigma=3log u. Then ds=d sigma and exp(s)=a^3 exp(sigma). Substituting H=C htilde in all FOUR K2522 weak columns and dividing by C^(3/2) preserves their form with ONE shared triple

    alpha'=alpha/C^2, rho'=rho/C^4, q0'=q0 a^3/C^4. (4)

Translate the test windows to sigma; their first two s derivatives equal their sigma derivatives and endpoint support remains compact. The all-coefficient exclusion applies to(4), so no native units or source parameter are secretly fitted per window. Positive and negative results still concern only the declared metric-action class.

The repair removes the low-origin coverage requirement but does not make the ANDES forecast sufficient. It requires continuous Q across[3,4.5], a compatible source population, and two absolute, jointly calibrated distance anchors; these are not supplied. DeltaC is a difference: independent fractional anchor error assumptions can substantially underprice its uncertainty. A shared multiplicative ruler error scales DeltaC rather than cancelling. A uniform calibration shift in Q cancels its oscillation. These two nuisance modes are different.

## 4. Missing information survives exact samples and anchors

The bare between-node bump is already K2522/K2526 evidence. A stronger control preserves an exact distance anchor as well. At p=0 choose nonzero smooth psi compactly supported in(1,1.5), set f(y)=y psi'(y), and choose small A with1+A f>0. Define

    H_A(y)=y/(1+A f(y)), Q_A(y)=A f(y)/(1+A f(y)).

The source observer has H_A(1)=1, so Q_A=1-H_A/y is a valid comoving drift curve. Every high-z sample equals the coasting values, and

    integral_1^1.5 dy/H_A=log(1.5)+A[psi(1.5)-psi(1)]
                         =log(1.5).

Yet Q_A is nonconstant and its oscillation can exceed R*. Thus even an exact low-z distance anchor added to perfect high-z point data fails to supply the old continuous bound. This is a kinematic information counterexample, NOT a claim that either history solves the metric action. The same construction inside a gap between finitely many high-z nodes preserves the high-z difference anchor: a finite sample plus exact DeltaC still needs regularity. The probe uses a piecewise polynomial bump with enough endpoint vanishing for the displayed smooth finite-order controls; the written proof allows a C-infinity compact bump.

## 5. Consequence and reproducibility

The concrete configuration fails to establish the existing test; the shifted two-anchor construction closes one domain gap without hiding the remaining precision, tracer or joint-band inputs. The next observation result should be a directly measured finite-observable residual with a justified joint likelihood/band or a sharper weak certificate whose gain can close the observed scale gap. Another sufficient-bound decimal is not observational progress. Compare that work with the actual coupled-action response in[K2529](k2529-native-displacement-response-2026-11-04.md).

The probe checks exact domain bounds, transformed weak columns, anchor-preserving counterprofiles and rational sufficient-bound composition. Floating forecast errors and physical-unit examples are separately labeled numerical evidence. Dependency hashes/report equality establish provenance, not continuum theorems. No source register, ledger, canon, empirical or native GU verdict changes; no external-expert, proof-assistant or novelty certification.
