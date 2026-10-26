---
title: "K2099: Finite-band massive memory transfer with full-Fock control"
status: active_research
doc_type: exploration
created: "2026-10-26"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional mathematics; no local apparatus, source selection, GU verdict, novelty or external certification
scripts:
  - tests/channel-swings/k2099_finite_band_massive_memory_probe.py
---

# K2099: Finite-band massive memory transfer with full-Fock control

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
result: conditional operational theorem with supplied representation and controls
carrier: free massive sea excitation CAR and finite memory with ordinary tensor reference LAYER=toy CHIRALITY=S-FULL-DIRAC
pairing: positive Hilbert metric ON=declared_complex_completion
real_structure: CAR adjoint and explicit particle-hole split, not source-selected reality
grading: fermion parity with energy sign and charge kept distinct
action_owner: repository-construction -- supplied free dynamics and smeared controls
target: conditional operational state and instrument constraints MAP-TYPE=intertwiner
```

[Conditional mathematics accepted after independent internal specialist review and exact finite controls. No external or proof-assistant certification.]

## Source and Layer0 boundary

SC-OP-04 ASSERTS candidate four-field operator grammar; SC-OP-05 and
SC-META-53 remain UNCERTAIN; SC-META-56 DISAVOWS a mandatory odd action.
These supplied positive CAR models are not source operator9.16. K2021 already
constructs local R0/R1 but does not source-select these dynamics, observations
or states. LT-SM8/LT-GR6b retain action/observation/quotient/positivity debts.
Source-register, physics-ledger and canon verdicts remain unchanged. No new
substrate pathway or source mechanism is asserted. The results supply scoped
reverse-scaffold constraints and conditional mathematical constructions.


## 1. An actual massive spectral model with supplied smeared control

Supply the positive-energy excitation space of the free massive Dirac sea,
with self-adjoint h>=m>0, m>0, and absolutely continuous massive dispersion.
A hole sector, when used, is a separate conjugate excitation summand. Fix a
normalized f in the spectral subspace [a,b], m<=a<b<infinity, and a single
fermionic memory d. Set

    omega=<f,hf>, P=|f><f|, Q=I-P,
    r=(h-omega)f, sigma=||r||,
    H=(h direct-sum omega)+g(|f><d|+|d><f|), g>0.       (1)

The coupling is a supplied bounded, rank-two one-particle perturbation; it
selects a spectral wavepacket, not a point or bounded spatial laboratory.
Its CAR lift is an even number-conserving bounded coupling of norm g.
This is a Hamiltonian on a massive continuum, not K2096's chiral Markov
boundary equation. It does not derive a local field-to-memory interaction.

Define V=|r><f|+|f><r| and h_ref=h-V on Dom h. Bounded perturbation makes
h_ref self-adjoint. Since h_ref f=omega f and f is in Dom h, P reduces h_ref;
its Q restriction is self-adjoint on Q Dom h. Thus

    h_ref=omega P + QhQ,
    H_ref=(h_ref direct-sum omega)+g(|f><d|+h.c).        (2)

Equation(2) is an exact comparison operator, not an implemented modification.
It leaves the orthogonal field modes under QhQ and on (f,d) evolves as
exp(-it omega)[cos(gt)I-i sin(gt)X]. At T=pi/(2g) it is a swap with phase
-i exp(-i omega T). Number phases must be tracked or corrected by explicitly
supplied register rotations. It is not an unsigned tensor SWAP on all Fock
occupations: exterior powers fix the doubly occupied sign.

## 2. Uniform full-Fock bound and stronger selected-input bound

For sigma>0, V has precisely two nonzero eigenvalues +sigma,-sigma, with
normalized directions proportional to f+r/sigma and f-r/sigma. Consequently

    ||dGamma(V)||=sigma.                               (3)

Indeed occupations of these two eigenmodes give energies 0,+sigma,-sigma,0;
all other occupations are spectators. For sigma=0 the assertion is immediate.
This bounded Fock perturbation means the two self-adjoint second-quantized
Hamiltonians have a common domain and differ by dGamma(V). Duhamel yields

    ||exp(-it dGamma(H))-exp(-it dGamma(H_ref))||
          <= min(2,|t| sigma).                         (4)

No mean excitation-number bound is required. With Tdiamond denoting half the
diamond norm of a channel difference, unitary dilation and trace contraction
then give Tdiamond<=min(1,|t|sigma), including arbitrary ordinary tensor
references, arbitrary spectator occupation and any subsequent common channel.
A one-particle norm bound alone would not establish(4); the two signed
finite-rank eigenvalues are the essential extra fact.

There is a sharper capture estimate for the selected one-excitation input f
and an empty memory. Along the reference trajectory the f amplitude is
exp(-i omega s)cos(gs), and V annihilates d, so

    ||(exp(-iTH)-exp(-iTH_ref))f||
       <=sigma integral_0^T |cos(gs)| ds=sigma/g.
    p_capture >= max(0,1-(sigma/g)^2).                  (5)

Project the actual output onto the field complement of the ideal memory
output to obtain the second line. This improvement is not a replacement for
the arbitrary-spectator full-Fock bound(4). The spectral variance satisfies
sigma²<= (b-a)²/4: (E-a)(b-E)>=0 implies variance <=(omega-a)(b-omega).
Thus narrowing the energy band can suppress both errors at fixed g. In the
absolutely continuous continuum sigma=0 cannot occur for nonzero f; a discrete
eigenmode is an explicit countercontrol where exact swap is possible.

## 3. Followthrough: speed, detuning and positivity are different limits

For time-dependent coupling g(t), any field drift and memory energy commuting
with memory number, and any initial joint normal state with empty memory,
let p(t)=<n_d>. Splitting the density into empty/occupied memory blocks and
using ||a(f)||=1 gives

    |p'|<=2 |g(t)| sqrt(p(1-p)).
    p(t)<=sin²(integral_0^t |g(s)|ds)
        whenever integral_0^t |g(s)|ds<=pi/2.           (6)

The block trace-norm inequality follows from positivity by writing the
cross block as A^(1/2) K B^(1/2), ||K||<=1. Integrating the arcsine inequality
by continuity covers p=0. References and field correlations do not remove
this speed constraint. A coherent resonant isolated mode saturates it.
This pi/2 area law differs from the logarithmic Markov budget in K2096
because the supplied dynamical models differ.

Detuning is not spectral spread. For an exact discrete mode with energy
omega+Delta and memory energy omega, the exact population transfer is

    p(t)=g²/(g²+Delta²/4) sin²(t sqrt(g²+Delta²/4)).      (7)

Its maximum over time is g²/(g²+Delta²/4). A zero-width mode therefore does not guarantee perfect transfer unless the
memory is matched. The construction(1) deliberately sets its energy to the
mean; that is an imported control choice.

If the instantaneous one-particle Hamiltonian must remain nonnegative, the
exact Schur-complement criterion is

    g² <f,h^(-1)f> <= omega.                            (8)

Complete the quadratic form in the field coordinate, using bounded h^(-1).
Since omega>=m and <f,h^(-1)f><=1/m, g<=m is sufficient. Large g cannot be
used without checking(8). Narrow spectral spread at fixed g<=m supplies an
honest small-error regime. Number conservation alone does not prove positive
instantaneous energy. No external switching/reset work or ground-state
selection is computed here.

## 4. Spatial and source limits

Finite massive energy band bounds momentum support. The position Fourier
transform of a compact-momentum L2 spinor is real analytic (compact support
also makes it L1 and permits every derivative). If it vanished outside a
bounded spatial region it would vanish on an open set, hence everywhere.
Therefore a nonzero exactly finite-band f is not compactly spatial supported.
Positive-energy filtering is also nonlocal. The supplied rank-one coupling
cannot be called a causally local apparatus from its bounded norm. Time-dependent
local transport, approximate spectral filtering and distributed control remain
possible; no all-apparatus exclusion follows. K2094's multiplier limit is
reused rather than applied to an arbitrary time-ordered propagator.

A quantitative spatial cost follows for dispersion E(p)=sqrt(v²|p|²+m²),
using Fourier normalization (2pi)^(-3/2). The spectral shell has volume

    Vp=4pi/(3v³) [(b²-m²)^(3/2)-(a²-m²)^(3/2)].
    integral_A ||f(x)||² dx <=min(1, |A| Vp/(2pi)³).     (9)

Fourier Cauchy-Schwarz bounds the vector norm pointwise by
sqrt(Vp)/(2pi)^(3/2); no spin multiplicity factor is needed. For a fixed
bounded central energy, narrowing the band drives Vp to zero, forcing spatial
delocalization. Thus a smaller sufficient variance error is purchased with
less possible concentration in a fixed region. This is a kinematic bound,
not a lower bound on all local detector errors or proof that the variance
estimate is sharp in every continuum model.

## 5. Evidence and next condition

The universal estimates are written proofs. The exact probe checks a
three-level matrix with sigma=3/5, its residual's full exterior-power lift, a genuine
finite-band variance, the Schur boundary and an exact detuned two-level control.
Input faults change the coupling, residual, memory energy or spectral values;
no mutation changes a theorem assertion into its negation. Finite controls do
not prove the domain or continuum claims. Independent internal review is
required; no novelty or external certification is claimed. The next physical
construction must replace the spectral rank-one control by an explicit local
interaction and quantify its approximation at the same record/coherence bar.

Adjacent prior art: [Bertoni et al., travelling-wavepacket quantum-dot capture,
Physical Review B73,125334 (2006)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.73.125334).
That semiconductor model is not a proof of(1)-(8) for a relativistic sea; the
present argument is direct finite-rank perturbation theory.
