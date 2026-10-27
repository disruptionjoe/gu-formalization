---
title: "K2137: Continuum record response and finite field-energy budgets"
status: active_research
doc_type: exploration
created: "2026-10-27"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: fixed-code continuum bounds for K2136; no full-Fock operator norm convergence or total work bound
scripts:
  - tests/channel-swings/k2137_point_probe_energy_continuum_probe.py
---

# K2137: Continuum record response and finite field-energy budgets

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

```gu-typed-objects
result: Continuum record response and finite field-energy budgets
carrier: K2136 massive scalar Fock space and fixed vacuum-one-photon code with arbitrary references LAYER=toy CHIRALITY=N/A
pairing: positive Hilbert norm and free field energy ON=declared_carrier
real_structure: complex operator adjoint
grading: boson occupation; no source grading
action_owner: repository-construction -- supplied K2136 point-memory dynamics and fixed finite code
target: UV limit full recorded channel and field energy MAP-TYPE=intertwiner
```

## 1. Consume the point model in explicit continuum budgets

K2136's rectangular pulse already has a finite-energy non-Gaussian record.
Here we freeze m>0, λ=m, T=1/m, derive a certified response floor and cutoff
error, then replace the abrupt pulse by a triangular one to obtain finite
second energy moment. This is a dependent resource result for the SAME
point-local massive scalar and memory, not another independent physical model.
No source, ledger, canon, total-work or physical-parity claim changes.

## 2. Rectangular pulse: no ultraviolet energy divergence

With p=k/m and ζ=(1-exp(iω/m))f, direct substitution gives

    A=||ζ||²=(1/(2π))∫R
       [1-cos(sqrt(1+p²))]/(1+p²)^(3/2) dp,
    11/(48πsqrt2)<=A<=2/π,
    Eζ<=m.                                         (1)

For the lower bound restrict |p|<=1. On1<=x<=sqrt2,
1-cos x>=x²/2-x⁴/24>=11/24, and (1+p²)^(-3/2)>=1/(2sqrt2).
The upper bound uses1-cos<=2 and ∫(1+p²)^(-3/2)dp=2.
Thus the fixed code u=ζ/sqrt A has recorded one-photon/vacuum contrast

    2A exp(-2A)>=(11/(24πsqrt2))exp(-4/π)>0,
    mean output energy<=m(1+48πsqrt2/11).             (2)

These are conservative certified bounds, not optimal response or energy.
They establish a fixed nonzero contrast with finite field-energy cost in the
unregulated model. Mean energy does not bound its variance: for the abrupt
pulse ∫ω²|ζ|² has a logarithmic ultraviolet divergence for nonzero duration,
because its large-k integrand is a positive oscillatory1/|k| tail. This is
explicitly outside the finite-second-moment assertion below.

## 3. Full recorded fixed-code cutoff convergence

Let f_Λ=1_(|k|<=Λ)f, ζ_Λ the corresponding displacement. Direct tail integration
using ω>=|k| gives

    ||f-f_Λ||²<=λ²/(4πΛ²),
    ||ζ-ζ_Λ||²<=λ²/(πΛ²),
    Eζ-Eζ_Λ<=2λ²/(πΛ).                              (3)

These bounds hold for all m,λ,T and Λ>0 for a rectangular pulse. Disjoint
momentum supports make the Weyl cross phase between ζ_Λ and δ=ζ-ζ_Λ zero.
On the fixed vacuum/one-photon code V, the anti-Hermitian displacement generator
Qδ=a*(δ)-a(δ) satisfies ||Qδ V||<=sqrt3||δ||: its images of Ω and1_u have
opposite number parity, and ||Qδ1_u||²=||δ||²+2|<δ,u>|²<=3||δ||².
The spectral inequality |exp(ix)-1|<=|x| gives

    ||(D(δ)-I)V||<=sqrt3||δ||.

Use the same controlled-memory Stinespring isometry and same record channel
on both sides. Purification and trace contraction yield

    (1/2)||J_V-J_Λ,V||_diamond
        <=min(1,sqrt(3/π)|λ|/Λ).                    (4)

The output is the FULL field plus record with arbitrary reference, not just
its probabilities. The exact code remains fixed as Λ varies. Its one-photon
wavefunction need not be band limited; the cutoff leaves high modes freely
evolving. The common free output rotation cancels in channel comparison.
This is not full-Fock operator-norm convergence. For any nonzero δ, the
spectrum of its quadrature is R, so ||D(δ)-I||=2. Neither (4) nor strong
convergence gives exact causality of a momentum regulator; locality belongs
to the unregulated retarded solution proved in K2136.

## 4. Triangular switching closes the second-moment gap

Set a=1/(2m), and take χ(t)=t/a on[0,a], (2a-t)/a on[a,2a], zero elsewhere.
The total variation is2, amplitude at most1. The time-dependent Hamiltonian
is the K2136 common closed form with λ replaced by λχ(t), lower bound
-λ²χ(t)²/(4m). Piecewise Lipschitz switching defines its unitary propagator;
one can construct it directly by cutoff Weyl evolution and form convergence.
Its sector-dependent displacement is

    ζχ(k)=-i λ h(k)/sqrt2 Fχ(ω(k)),
    Fχ(ω)=∫χ(t)exp(iωt)dt
          =-(exp(iωa)-1)²/(aω²)
          =a exp(iωa)sinc²(ωa/2).                   (5)

The time-ordering phase is the SAME for both memory sectors and cancels
from the instrument. Explicitly it is λ²/2 times the k integral of h² times
∫_0^T ds ∫_0^s dr χ(s)χ(r)sin(ω(s-r)). Integration by parts in r bounds
this double time integral by Cχ/ω, with
Cχ=||χ||₂²+||χ||₁(|χ(0)|+||χ' ||₁); for the triangle Cχ=8a/3.
Since ∫h²/ω=1/(2m), the phase converges absolutely after time integration;
its cutoff tail is at most λ²Cχ/(2πΛ). This avoids treating φ(δ0) as an operator at an instant.
The variable source is still supported on the one worldline segment;
retarded convolution in time proves the same causal domain. No spatial
smearing or finite-range detector current was introduced.

For λ=m, integration by parts gives |Fχ|<=2/ω, so Aχ<=2/π and Eχ<=m as before.
For |k|<=m, x=ωa/2 lies in[1/4,sqrt2/4]; sinc x>=1-x²/6>=47/48. Therefore

    Aχ>=(47/48)^4/(8πsqrt2)=:L>0,
    contrast>=2L exp(-4/π),
    mean output energy<=m(1+1/L).                    (6)

These deliberately loose constants use h²>=1/(2πm sqrt2) on that interval.
The extra ω^-2 from(5) gives |ζχ|²=O(|k|^-5), hence

    M2=∫ω²|ζχ|² dk < infinity.                       (7)

In particular uχ=ζχ/sqrt(Aχ) has a finite second energy moment.
For a coherent branch the second moment is Eχ²+M2; Weyl translation by ζχ
preserves the H_F operator domain, as follows from ωζχ in L2 and the relative
bound for its field operator. Thus all fixed0/1-code outputs, recorded or
unread, have finite second energy moment. More explicitly M2<=32m²/π at the frozen pulse. On a normalized fixed-code/
reference input, the square root of the output second energy moment is bounded
by sqrt(M2/Aχ)+sqrt(3M2)+Eχ: conjugating H_F by D(ζχ) adds
a*(ωζχ)+a(ωζχ)+Eχ, whose linear part has code norm at most sqrt(3M2).
Replacing Aχ by L and Eχ by m gives a finite explicit uniform code bound.
This is not a uniform bound over all input states and does not account for
controller or reset energy. The triangle is absolutely continuous and piecewise
C1; no C-infinity pulse or arbitrary higher-moment claim is made.
Using |Fχ|<=4/(aω²), the cutoff tails also obey

    ||ζχ-ζχ,Λ||²<=2λ²/(πa²Λ⁴),
    Eχ-Eχ,Λ<=8λ²/(3πa²Λ³),
    M2-M2,Λ<=4λ²/(πa²Λ²),
    (1/2)||Jχ,V-Jχ,Λ,V||_diamond
       <=min(1,sqrt(6/π)|λ|/(aΛ²)).                 (8)

The same fixed-code generator argument proves the last line. This is an
actual improved resource/convergence consequence, not a larger pass count.

## 5. Verification and next constraint

Symbolic checks reproduce the pulse transform, displacement tails, conservative
lower bounds and record/energy identities. Numerical quadrature is a transparent
sanity check only; universal bounds follow from the stated integrable majorants
and inequalities, independently reviewed internally. Faults alter pulse
normalization, Fourier powers and the energy measure rather than check predicates.
No exact causality is inferred from a numerical cutoff or finite grid.

A next substantial target is an actual parity-capable local interaction or an
autonomous controller with bounded total resources; the present non-Gaussian
scalar record does not supply either. The code's preparation/localization
constants also remain separate from the field-energy bounds. The native full
graph/raw tangent and independent thermal global inequalities remain alternatives.
All source polarities and physical-quotient debts retained by K2136 survive.
