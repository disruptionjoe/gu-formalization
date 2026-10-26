---
title: "K2087: Thermal measurement energy without infinite subtraction"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no source-state selection, GU verdict or external certification
scripts:
  - tests/channel-swings/k2087_relative_measurement_energy.py
  - tests/channel-swings/k2087_relative_measurement_energy_probe.py
---

# K2087: Thermal measurement energy without infinite subtraction

Classification: `INTERNAL_STRUCTURAL_ONLY`.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

```gu-typed-objects
result: bounded relative energy, exact coarse cost and thermal positivity
carrier: supplied massive complex Dirac1408 CAR on R3 LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: fixed positive Hilbert metric and gauge-invariant quasifree input ON=declared_complex_completion
real_structure: inherited b antiunitary with b squared minus identity and b H b inverse equals minus H
grading: fermion parity, charge and energy signs are separate
action_owner: repository-construction -- imported free massive dynamics and stated operational additions
target: operational state and measurement constraints MAP-TYPE=intertwiner
```

[Conditional mathematical result; accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Scope and inherited evidence

SC-OP-04 ASSERTS candidate four-independent-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS an odd-action prerequisite.
These calculations use the supplied positive massive CAR completion, not the source
operator (9.16). LT-SM8/GR6b, source-register, physics-ledger and canon verdicts remain
unchanged. K2021 already supplies local R0/R1; source selection and interacting
observation/action/quotient are still separate. No novelty or external certification
is claimed. The operational demands are reverse-scaffold constraints, not predictions.

## 1. Define the energy change intrinsically

[K2086](k2086-ground-state-selection-2026-10-26.md) has finite thermal energy
density, but infinite total energy on R3. Its state need not be a vector in the sea
representation. Subtracting two infinite expectations of a Hamiltonian is invalid.
Let d denote the CAR dynamics derivation with convention d(A)=[G,A] (the usual
star derivation is i*d). For normalized f in Dom H, n=a*(f)a(f) is in its domain,
||d(n)||<=2||Hf||. For any projection E in this domain define

    D_E = E d(E)+(1-E)d(1-E) = (2E-1)d(E).             (1)

The projection identity gives (2E-1)d(E)=-d(E)(2E-1), while d(E)*=-d(E).
Thus D_E is a bounded self-adjoint CAR element. Its expectation exists in EVERY
state. Whenever finite Hamiltonian expectations exist it equals the nonselective
Lueders energy difference EGE+(1-E)G(1-E)-G. Equation(1), not subtraction,
defines relative free-dynamics energy in the infinite thermal system. It is not
thermodynamic free energy, total apparatus work, or heat paid for a record.

## 2. Exact single-mode formula and sign

Let the stationary input be gauge-invariant quasifree with C=c(H), 0<=C<=1.
Put R=|f><f|. The output covariance of the number Lueders channel is

    C'=RCR+(1-R)C(1-R),
    Delta C=-RC(1-R)-(1-R)CR.                         (2)

For example, the channel is the equal mixture of identity and conjugation by
1-2n, whose one-particle reflection is 1-2R; averaging proves(2).
The output need NOT be quasifree: only its two-point function is stated.
Since C preserves Dom H, H Delta C is finite rank and trace class. Directly,

    Delta_f = omega(D_n) = Tr(H Delta C)
            = 2(nu*h-k),
    nu=<f,Cf>, h=<f,Hf>, k=<f,CHf>.                  (3)

The trace is of a finite-rank difference, not a subtraction of total energies.
For the spectral probability measure mu_f of H and thermal
c(x)=1/(1+exp(beta*x)), beta>=0, this becomes

    Delta_f = integral integral (x-y)(c(y)-c(x)) dmu_f(x)dmu_f(y) >=0. (4)

Monotonicity makes the integrand nonnegative. Absolute integrability follows
from its bound |x|+|y| and f in Dom H. For beta>0 it is strictly positive unless
mu_f is supported at one energy. The free Dirac operator on R3 has no eigenvalues,
so every nonzero normalized f in Dom H has positive cost. At beta=0 cost is zero.
For a general inverted population the cost can be negative; no all-state
positivity is inferred from boundedness. Equation(1) also gives the sharper
uniform bound |Delta_f|<=2||Hf||.

## 3. Coarse paired measurement versus a refined substitute

Use K2082's two orthogonal H-reducing multiplicity sectors with block-diagonal C,
f and bf in the separate sectors. This condition includes Hf and Hbf; merely
<f,Cbf>=0 is insufficient. Write n=n_f, N_b=n_bf, E=1-(1-n)N_b. Let D_n and D_Nb be
as in(1). Splitting the free derivation across the sectors gives the identity

    D_E = D_n N_b + (1-n)D_Nb.                          (5)

It can also be verified by expanding the double commutator [E,[G,E]]. Products
factor in the INITIAL quasifree block-product state. In general,

    omega(D_E)=<N_b> Delta_f+(1-<n>) Delta_bf.          (6)

If additionally bCb^-1=1-C and bHb^-1=-H, then <N_b>=1-nu and
Delta_bf=Delta_f (apply(3): h_b=-h, k_b=k-h). Therefore

    Delta_coarse=2(1-nu)Delta_f,
    Delta_refined=2Delta_f.                         (7)

The refined channel separately measures both occupations and forgets the record.
Its cost is different and its extra coherence loss remains observable.
For thermal beta>=0, 0<=Delta_coarse<=Delta_refined. The projection commutator
bound ||d(E)||<=4||Hf|| gives |Delta_coarse|<=4||Hf|| independently of thermal
volume or representation. K2080's ||Hf||<=201m/100 therefore gives <=201m/25.
This is a coarse uniform bound, not a low-noise or sharp temperature estimate.

Equal defect means by themselves do NOT prove(7). Take equal weights in energies
1,2 and partner energies -1,-2, with occupations respectively 1/5,1/10,7/10,1.
Both defect means are3/20, but Delta_f=1/20 and Delta_bf=3/20. Equation(6)
gives17/100, while falsely applying(7) gives17/200. This stationary monotone
nonthermal input lacks the required particle-hole complement.

## 4. Zero-temperature check and useful operational consequence

In the sea, let e_+=<f,H P f>, e_-=-<f,H Q f>, nu=<f,Qf>. Then(3) yields

    Delta_f=2(nu*e_+ +(1-nu)*e_-),
    Delta_coarse=4(1-nu)(nu*e_+ +(1-nu)*e_-).         (8)

This recovers positivity and sharpens the previous generic commutator estimate
for a specified mode. If nu<=tau^2 and ||Hf||<=M, Cauchy-Schwarz gives
e_-<=M sqrt(nu), e_+<=M sqrt(1-nu). Thus
Delta_coarse<=4M(tau^2+tau), in the stated paired sea input. No thermal
small-noise bound is obtained by blindly replacing nu with a cutoff error.

The finite exact probe constructs full Fock density matrices, both channels and
Hamiltonian energy differences. It separately computes(3), the thermal pair
integral, and the unequal-cost counterexample. This verifies finite algebra and
counterexamples; the domain/relative-energy argument above carries R3.
Next optimize a specified temperature/localization/readout budget, or supply an
actual apparatus whose work and measurement channel can be compared with these
relative-energy costs. No apparatus cost follows from(1).
