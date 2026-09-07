---
title: "K140 thermodynamic, Schur-response, and charge-conjugation wave"
status: active_research
doc_type: conditional_boundary_response_identifiability_local_thermodynamic_scaling_coulomb_obstruction_and_charge_conjugation_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned classification for K139's supplied signed point control that complete complex on-shell boundary response identifies the finite Hermitian extension under a full-row-rank channel condition, physical box normalization gives volume-uniform local point-boundary estimates and a continuum coefficient limit, the raw one-dimensional Coulomb/Gauss relative bound fails uniformly on separated neutral pairs, and charge conjugation conditionally fixes the symmetric sea-charge origin and relates particle/hole couplings without selecting their magnitudes, the free operator/time orientation or W; no common infinite-volume interacting operator, scattering/NESS/current, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k140-thermodynamic-schur-response-charge-conjugation-wave.json
probe: tests/channel-swings/k140_thermodynamic_schur_response_charge_conjugation_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K140 thermodynamic, Schur-response, and charge-conjugation wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on K139's repository-owned signed point control. It
turns the unspecified “complete Schur datum” into an exact response-
identifiability condition, separates the thermodynamic behavior of the local
point boundary map from the raw one-dimensional Coulomb/Gauss form, and asks
what charge conjugation selects after a gapped signed free operator and time
orientation have already been supplied. It does not supply measured response
data, an infinite-volume interacting operator, or a source/GU action.

```gu-typed-objects
result: a full-row-rank complete complex on-shell boundary response recovers W; L^-1/2 box normalization makes the local signed point coefficient volume uniform, while separated neutral pairs obstruct a volume-uniform raw Coulomb/free-energy bound; relative to a supplied C-odd gapped free operator, charge conjugation fixes a symmetric sea-charge origin and relates particle/hole couplings but does not select the imported operator, magnitudes or W
carrier: the K139 C9 impurity and C512 Klein module coupled to thirty-six particle/hole point channels, first in a circle of length L and then at the coefficient-level continuum limit; neutral two-particle Gauss controls are tested separately LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive particle/hole Fock Hilbert pairing and finite-dimensional Hermitian Schur boundary pairing; charge conjugation is antiunitary on the supplied gapped one-particle carrier ON=repository_signed_point_control
real_structure: antiunitary C satisfies C D C^-1=-D, exchanges positive and negative spectral halves, conjugates particle/hole coefficients and makes the symmetrically normal-ordered charge odd
grading: matrix units are even, Klein/CAR fields are odd and defect monomials are even; the thermodynamic coefficient bound uses the same Neumann word grading as K139
action_owner: repository-construction -- the signed free operator, time orientation, polarization, charge conjugation, channel map, response datum, sea convention, couplings, W, Coulomb law and volume state are not selected by Weinstein's source or a GU action
target: complete Schur-response identifiability, local point thermodynamic scaling, raw Coulomb/Gauss nonuniformity and conditional charge-conjugation selection boundary MAP-TYPE=not-a-map
```

## Inline preflight bookend

K139 leaves two superficially similar but mathematically different questions:
whether the local point interaction has volume-uniform coefficients and whether
the raw Coulomb/Gauss addition is uniformly controlled by free energy. It also
names a complete Schur boundary datum without specifying what experimental or
operator response would recover it. These are the first discriminators. A
source-action search is wrong-direction here because the admitted reverse
scaffold asks what data and dynamics an eventual action must own.

Mechanism retrieval found K138's affine Hermitian `W` family and
three-parameter rook commutant, K139's finite-volume Neumann chart and its
explicitly volume-dependent Coulomb constant, and no prior full-channel
response inversion, physical box normalization theorem, separated-neutral-
pair obstruction, or charge-conjugation classification of the remaining
imports. No correction-registry entry supersedes the inputs.

The route census covered boundary triples and Weyl functions, finite-rank
inverse scattering, channel observability, analytic continuation, box-to-line
Riemann sums, point-evaluation normalization, one-dimensional Gauss law,
screening and confinement alternatives, spectral polarization, antiunitary
charge conjugation, Shale--Stinespring implementability, source ownership and
hostile scope review. A pole-only route is underdetermined. Complete complex
response is algebraically decisive under a rank condition. A broad scattering
construction is premature because no common interacting infinite-volume
operator is yet owned. Exact computation checks finite response inversion,
Riemann-sum behavior and the neutral-pair witness; it is not the analytic
proof.

## 1. Complete boundary response identifies the finite extension

Let the finite impurity space be `K=C^9`, let `M(z)` be the known Weyl matrix
of the fixed point-channel construction, and let `W=W*` be K138's finite
extension coordinate. At a regular boundary value `E+i0`, write

```text
R_W(E)=(W-M(E+i0))^-1.                                  (1)
```

If `C(E): H_ch(E)->K` is the known on-shell channel map, the complete complex
channel response has the standard finite-rank form

```text
S_W(E)=I-2 pi i C(E)* R_W(E) C(E).                      (2)
```

Assume `C(E)` has full row rank nine. Then
`G(E)=C(E)C(E)*` is invertible, and the measured response determines

```text
R_W(E)=G(E)^-1 C(E) [(I-S_W(E))/(2 pi i)]
         C(E)* G(E)^-1,                                (3)
W=M(E+i0)+R_W(E)^-1.                                   (4)
```

Thus one complete complex response matrix at one nonpole energy is
algebraically sufficient when `M` and `C` are already known. An open energy
interval is the honest robust condition: it avoids isolated poles and rank
drops, tests energy consistency, and supplies redundancy against incomplete
data. This sharpens K138's statement that one scalar pole is insufficient.

Full row rank is load bearing. If `C` is rank deficient, (2) directly supplies
only the compressed resolvent on the channel-visible subspace. A decoupled
Hermitian change on an invisible impurity direction leaves the full response
unchanged. Particular restricted `W` families may remain identifiable, but
there is no unconditional recovery theorem for all Hermitian `W`.

Equations (2)--(4) are a **selection interface**, not a physical selection.
The repository contains neither measured infinite-volume response data for
this model nor a source-owned action that fixes `M`, `C` and `S_W` together.

## 2. The local signed point coefficient is volume uniform

Put the massive point control on a circle of length `L`, with orthonormal
modes `L^-1/2 exp(i p_n x)` and

```text
p_n=2 pi n/L,
omega(p)=sqrt(m^2+p^2),
h_L(lambda)^2=(1/L) sum_(n in Z)(omega(p_n)+lambda)^-2. (5)
```

The factor `L^-1/2` is the physical box normalization of point evaluation. It
was absent from the unit-circle notation because `L` was fixed. For the even,
positive, decreasing function
`f_lambda(p)=(omega(p)+lambda)^-2`, the integral test gives, for `L>=1`,

```text
h_L(lambda)^2
 <= f_lambda(0)+(1/pi) integral_0^infinity f_lambda(p) dp. (6)
```

The right side is finite, independent of `L`, and tends to zero as
`lambda->infinity`. Consequently K139's bound becomes

```text
sup_(L>=1,N) ||G_(L,N,lambda)||
 <= M sum_(e,s)|g_(e,s)| sup_(L>=1) h_L(lambda),        (7)
```

and one auxiliary shift gives a common Neumann margin for every large volume
at fixed finite couplings. The shift remains a compensated boundary-chart
coordinate, not a physical weak-coupling condition.

Standard Riemann-sum convergence gives

```text
h_L(lambda)^2 -> (1/(2 pi)) integral_R
                    dp/(sqrt(m^2+p^2)+lambda)^2.       (8)
```

The matched endpoint counterterm is

```text
c_(L,Lambda)(lambda)=(1/L) sum_(|p_n|<=Lambda)
                         (omega(p_n)+lambda)^-1.       (9)
```

It retains the expected ultraviolet logarithm as `Lambda->infinity`, while
subtracted differences have an integrable `p^-2` tail. Thus the local point
boundary and renormalized Schur coefficients have the right volume scaling.
Equations (5)--(9) are not yet convergence of interacting operators on one
identified infinite-volume Hilbert space: embeddings, domains and the
interaction limit still have to be constructed.

## 3. Raw one-dimensional Coulomb/Gauss control is not volume uniform

The raw Gauss form behaves differently. Put charges `+q` and `-q` in fixed-
shape wave packets centered a distance `R` apart, far from the box boundary.
In one spatial dimension, Gauss law makes the electric field equal to `q`
between the packets and zero outside, up to the fixed edge-smearing error.
Hence

```text
Coul(R)=(1/2) integral |E_R(x)|^2 dx
       =(q^2/2)R+O(1).                                 (10)
```

Translation leaves the free massive energy of the two fixed-shape packets
unchanged. Therefore no constants `a,b` independent of `L` and `R` can satisfy

```text
Coul_L <= a H_0+b                                      (11)
```

on the neutral two-particle sector: the left side grows linearly while the
right side stays bounded on the translated test family. K136--K139's
finite-volume all-sector estimate is correct, but its `C_L` must grow.

This is a route obstruction, not a universal no-go. It blocks carrying the
**raw unscreened one-dimensional Coulomb form** to the thermodynamic limit by
K139's uniform relative-form argument. Screening, a confining thermodynamic
representation, local-neutral clusters, another topology, subtraction of a
state-dependent bulk energy, or a different renormalized dynamics are not
excluded. The local point interaction can be volume uniform even though this
Gauss addition is not.

## 4. What charge conjugation selects conditionally

Let the supplied gapped signed one-particle operator satisfy

```text
C D C^-1=-D                                             (12)
```

for an antiunitary charge conjugation `C`, with zero outside the spectrum.
Then spectral calculus gives

```text
C P_+ C^-1=P_-,
P_+=1_(0,infinity)(D),  P_-=1_(-infinity,0)(D).         (13)
```

Relative to this already chosen `D` and time orientation, (13) canonically
pairs particles and holes. If the Fock vacuum and normal ordering are chosen
`C`-invariant, the charge operator is `C`-odd and its additive sea-charge
origin is forced to zero. Covariance of each edge defect relates the two
couplings by

```text
g_(e,-)=exp(i theta_e) conjugate(g_(e,+)),              (14)
```

where channel rephasing absorbs `theta_e`. Equal magnitudes reproduce K139's
rook endpoint datum `4|g|^2 I`. Charge conjugation also requires `W` to lie in
the corresponding real fixed subspace of the Hermitian extension family.

These are genuine reductions of arbitrary input, not complete selection.
Charge conjugation does not choose `D`, the time orientation, coupling
magnitudes, channel map, or a point in the `C`-fixed `W` family. More general
`C`-compatible polarizations exist; in infinite volume, Bogoliubov-related
choices are Fock-equivalent only under the Hilbert--Schmidt implementability
condition. The symmetry therefore cannot make every compatible sea convention
equivalent or source-owned.

## Inline postflight bookend

- **Strongest advance:** complete complex channel response now has an exact
  full-rank inversion formula for `W`; the formerly vague boundary datum is a
  reproducible identifiability condition.
- **Strongest thermodynamic result:** physical box normalization yields a
  volume-uniform local point-boundary coefficient and continuum integral.
- **Strongest negative result:** separated neutral pairs prove the raw
  one-dimensional Coulomb/free-energy relative bound cannot be volume uniform.
- **Strongest conditional selection:** charge conjugation fixes the symmetric
  sea-charge origin and relates particle/hole couplings only after the signed
  free operator, time orientation and invariant vacuum have been supplied.
- **Strongest overclaim:** “K140 constructs the infinite-volume physical GU
  Hamiltonian.” Refused. It constructs coefficient-level local estimates,
  an obstruction for one Coulomb route and a response interface with no data.
- **Strongest contrary route:** screening or a different thermodynamic
  representation may control Gauss energy, and a rank-deficient response may
  identify a specially restricted extension family. Neither possibility is
  excluded.
- **Weakest reproducibility seam:** the finite-circle unit convention can hide
  the `L^-1/2` point normalization; omitting it falsely manufactures volume
  growth in the local defect. Conversely, applying it does not normalize away
  the physical `q^2 R/2` electric-string energy.

The companion probe checks 42 exact structural/numerical controls and uses a
baseline-first hostile harness with 31 planted mutations. No common
infinite-volume interacting operator, Moller/Ruelle theory, return to NESS,
microscopic current, smooth unreduced connection/BRST parent,
Weinstein/source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Next condition

Construct a common infinite-volume Hilbert-space embedding and operator limit
for the **local** signed point defect using (5)--(9), without importing the raw
unscreened Coulomb form. In parallel, test a named screened/local-neutral or
confining Gauss thermodynamic representation against the separated-pair
witness. Only after one interacting infinite-volume operator is owned should
Moller/Ruelle or return-to-NESS work begin. A physical extension still needs
an actual full-rank response datum or an action principle, while a source/GU
action must independently own the free operator, time orientation,
polarization, charges, couplings, domain and state.

## Reproduction

```bash
python3 tests/channel-swings/k140_thermodynamic_schur_response_charge_conjugation_probe.py
python3 tests/channel-swings/k140_thermodynamic_schur_response_charge_conjugation_probe.py --selftest
```
