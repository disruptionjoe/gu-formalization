---
title: "K1899: Active scalar pulses and the free-energy domain"
status: active_research
doc_type: exploration
created: "2026-10-21"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
claim_ceiling: conditional massive rank-four R3 scalar-pulse theorem; free excitation energy is not renormalized stress energy or a GU observable
scripts:
  - tests/channel-swings/k1899_active_pulse_energy.py
  - tests/channel-swings/k1899_active_pulse_energy_probe.py
---

# K1899: Active scalar pulses and the free-energy domain

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
result: active-time particle count is finite but free excitation energy has a logarithmic ultraviolet divergence when the spatial gradient is nonzero
carrier: rank-four massive Dirac target on R3 LAYER=toy CHIRALITY=N/A
pairing: positive complex L2 and free polarized CAR sea ON=conditional_Dirac_target
real_structure: Hermitian Clifford matrices and real scalar multiplication potential
grading: free positive-negative spectral splitting and CAR parity
action_owner: repository-construction -- supplied smooth compact external scalar potential
target: weighted off-diagonal evolution and its endpoint dressing MAP-TYPE=intertwiner
```

## 1. The question and answer

Use exactly [K1897](k1897-smooth-pulse-energy-2026-10-21.md)'s
h=c(D.p+mu M), c=1/24, mu>0, E=|h|, Q=sign h, P_±=(1±Q)/2.
The four Hermitian matrices obey the Clifford relations, with trace of the
identity four. V is real scalar C_c^infinity(R x R3), and U(t,a) solves
 i partial_t U=(h+V)U, with a before the pulse. The fixed free sea is P_-.
Let Pi_L be the Fourier multiplier 1_(|p|<=L), and define

```
J_m(t;L) = (1/4)||Pi_L E^(m/2)[Q,U(t,a)]||_HS^2.
```

This is the sum of positive particle and hole excitation moments, with a
cutoff on the outgoing momentum; m=1 is positive free excitation energy.
For every fixed t with ||grad V(t)||_2>0,

```
J_0(t;infinity) < infinity,
J_1(t;L)/log L -> ||grad V(t)||_2^2/(12 pi^2 c).       (1)
```

More generally J_m is finite for 0<=m<1 and infinite for m>=1 at such a t.
At an instant with V(t)=0 as a spatial function, J_1 is finite, even if a
time derivative of V is nonzero. Once the pulse and all its jets vanish,
K1897 gives every finite moment. The latter theorem is retained unchanged.
Thus Fock implementability/normality does NOT imply finite free energy during
the pulse. Equation(1) is an all-order statement in the specified smooth
external-potential model, not an inference from a divergent Born coefficient.

The energy here is not a renormalized stress-energy tensor, the energy of
h+V, or a gauge-invariant calorimetric observable. We make no claim about
those quantities. It is a positive unbounded observable in a fixed free sea.
No GU identification follows. SC-META-53 remains UNCERTAIN; SC-OP-04 ASSERTS
candidate operator grammar and SC-MAS-01/SC-CHI-02 ASSERT a stylized R/4 toy.
LT-SM8, LT-GR6b, AC-F1, all source and canon verdicts remain unchanged.

## 2. Endpoint normal form: the missing term in the scattering argument

Apply the established finite-order unitary regularization of
[Langmann--Mickelsson, Lemma2.12 and (2.13)](https://arxiv.org/pdf/hep-th/9509034).
Write its product of finitely many changes of variables as T(t), with
U=T(t) U_reg(t,a), T(a)=I. Choose enough iterations that
[Q,A_reg] has localized symbol order -p with p>m/2+3/2.
K1897's weighted Duhamel estimate then gives
E^(m/2)[Q,U_reg] Hilbert--Schmidt on every finite interval. This argument
needs no vanishing final endpoint. Only identifying U with U_reg would need it.

All symbols used here are classical symbols with rapid spatial decay for
the interaction-dependent terms, including their derivatives. Scalar smooth
compact V, massive elliptic E and finite iterations preserve this class;
regularize the homogeneous formulas smoothly near p=0. Low momenta and
localized smoothing remainders are Hilbert--Schmidt with all finite weights.
A symbol of order -q becomes Hilbert--Schmidt after weight s when q>s+3/2;
spatial decay is essential on R3. The same Sobolev-boundedness estimates hold
for T, T^-1 and U_reg. These are the precise symbol/ideal hypotheses reused
from K1897, not a conclusion from negative order alone.

The first generator and its principal homogeneous term are

```
alpha = -(E^-1[Q,V]+[Q,V]E^-1)/8,
alpha_-2(x,p) = i D.v_perp/(4 c r^2),
r=|p|, n=p/r, v=grad V(t,x), v_perp=v-n(n.v).          (2)
```

Indeed q_0=D.n and [Q,V]_-1=-i D.v_perp/r in Kohn--Nirenberg
quantization (p=-i partial). The scalar nature of V is crucial: its leading
matrix commutator vanishes. Later generators have order at most -3.
Consequently T-I has order -2, with (2) as its leading symbol, and

```
[Q,T]_-2 = i (D.n)(D.v_perp)/(2 c r^2),
tr([Q,T]_-2* [Q,T]_-2) = |v_perp|^2/(c^2 r^4).       (3)
```

The mass contributes only to lower orders. Formula(3) uses anticommutation
of perpendicular Clifford vectors and tr I=4; it is not a dimension-only
transfer from an unrelated representation.

## 3. Exact decomposition prevents an all-order cancellation

The identity

```
[Q,U]=[Q,T]U_reg + T[Q,U_reg]                         (4)
```

separates the bad endpoint from a weighted Hilbert--Schmidt remainder.
For m=1 set F=E^(1/2)[Q,T] and
R=E^(1/2)T[Q,U_reg]. R is HS because
E^(1/2)T E^(-1/2) is bounded (mu>0). Right multiplication by U_reg
preserves the HS norm, even with Pi_L on the left. Thus

```
||Pi_L F U_reg||_HS = ||Pi_L F||_HS,
| ||Pi_L(FU_reg+R)||_HS^2 - ||Pi_L F||_HS^2 |
 <= 2 ||Pi_L F||_HS ||R||_HS + ||R||_HS^2.            (5)
```

The leading symbol of F has order -3/2. Its remainder is order -5/2,
and cross terms have finite phase-space integral. To justify the outgoing
cutoff without pretending it commutes with spatial multiplication, express F
in RIGHT quantization: its kernel is
(2pi)^-3 integral exp(i(x-y).p) f_R(y,p) dp.
Fourier transformation in x and Plancherel give the exact identity

```
||Pi_L F||_HS^2=(2pi)^-3 integral_(|p|<=L) dp dy tr(f_R* f_R).
```

Changing left to right quantization preserves the principal symbol and
lowers the difference by one order. From(3), its leading squared norm is
|v_perp|^2/(c r^3). Since
integral_S2 |v-n(n.v)|^2 dn = (8pi/3)|v|^2,

```
(1/4)||Pi_L F||_HS^2
 = ||grad V(t)||_2^2/(12 pi^2 c) log L + O(1).         (6)
```

Equations(5),(6) give(1), with an O(sqrt(log L)) possible error from this
norm estimate. We do NOT assert an O(1) remainder for the full energy.
No finite weighted-HS regularized term can cancel the leading logarithm.
For 0<=m<1 the radial integral is integral_1^infinity r^(m-2)dr,
which converges. For m>=1 use E>=c mu to transfer the energy divergence
upward. If V(t)=0, the first generator vanishes at that instant, so T-I
starts at order -3, and the m=1 weighted ideal test now converges.

## 4. Independent Born check and controls

The exact projector overlap is
tr(P_+(p)P_-(q))=1-(p.q+mu^2)/(E_p E_q), where E_p=sqrt(p^2+mu^2)
without the factor c. For fixed k=p-q and p=r n,

```
tr(P_+(p)P_-(p-k)) = |k_perp|^2/(2 r^2)+O(r^-3).
```

Integrating the first-order amplitude in time by parts, with zero initial
endpoint, gives its leading active-time term Vhat(t,k)/[c(E_p+E_q)].
Adding particle and hole energy gives the radial density
|Vhat(t,k)|^2 |k_perp|^2/(4c r^3), with convolution factor(2pi)^-3.
Angular integration/Parseval reproduces(1)'s coefficient. This is an
independent perturbative check; (4)--(6) carry the all-order conclusion.
The vanishing-gradient control removes the leading term, and switching the
pulse fully off removes all endpoint terms. A compact nonzero spatial
potential cannot have zero gradient everywhere.

For V=a g(t) exp(-|x|^2/(2l^2)) (Schwartz spatial extension of the same
proof), ||grad V||_2^2=(3/2)pi^(3/2) a^2 g(t)^2 l. Its logarithmic
coefficient is a^2 g(t)^2 l/(8 sqrt(pi)c), or 3a^2g(t)^2l/sqrt(pi)
when c=1/24. This is an explicit diagnostic, not a finite raw energy budget.

## 5. Released consequences: mixtures and dressed measurements

A binary +/- pulse has the same positive coefficient on both paths; it
cannot cancel the divergence by mean-zero potential. For any finite or
compact-amplitude mixture the leading coefficient is the expectation of
||grad V(t)||_2^2/(12pi^2c), with uniform finite-order remainder bounds.
A positive-probability set of nonconstant active profiles therefore has
infinite mean raw free energy. This does not reverse K1897's finite final
energy or exact finite-duration neutral decoherence construction.

A direct consuming condition follows: within this smooth compact scalar class,
finite raw free energy at EVERY time is possible only for V=0. At each time
(1) would force grad V=0, and spatial compactness forces the constant to zero.
A nonzero smooth pulse has an open time interval of nonconstant profiles, so
the raw energy is infinite there, not merely at an isolated switching instant.
This excludes that additional all-time requirement in this fixed free-sea
model; it does not prohibit the finite final-energy construction or change a
source claim. Switching more smoothly cannot remove this active endpoint term.

The unitary dressing provides a precise possible change of measurement:
use Q_T=TQT*, E_T=TET*, and measure the evolved state relative to these
operators. Its excitation moments are those of U_reg and can be finite to
any specified order by choosing sufficient regularization depth. This is
not a unique physical prescription: different depths/dressings give different
observables, and pseudodifferential T is generally spatially nonlocal. No
local detector, renormalized stress tensor, unchanged locality of dressed
observables, or GU-selected vacuum is supplied by this construction.
T itself is implementable (order-2 off-diagonal HS), consistently with
[Deckert--Merkl](https://arxiv.org/abs/1505.06039)'s free Fock implementability
for scalar potentials with zero spatial electromagnetic components.

A strongly continuous unitary path can leave and later reenter the form
domain of an unbounded positive energy observable. There is no conservation
law for the fixed free energy under a prescribed time-dependent drive.
These facts remove the apparent conflict between finite particle count,
infinite intermediate energy and finite final energy without subtracting
positive infinities or claiming an interacting quantum vacuum construction.

## 6. Verification and remaining frontier

Producer: exact Clifford matrices, perpendicular symbol, angular integral,
weighted radial thresholds and Gaussian coefficient. Separate probe: exact
projector high-momentum expansion and Born denominator/particle-hole factors,
plus mathematical coefficient mutations, dependency pins and report checks.
Finite controls do not certify pseudodifferential estimates; the continuum
argument is (2)--(6) under the stated localized symbol hypotheses.
Hostile review targets endpoint versus scattering, left/right quantization,
all-order versus Born, scalar versus matrix potential, and raw versus dressed
energy. No external review, formal proof or novelty is claimed.

The active-time free-energy question is answered in this model. A physical
energy measurement or quantitative final-energy cost still requires a specified
observable and pulse. The native full20/K-C/accessibility adapter and the
three-wall, noncanonical-rotation and scalar optimizer alternatives remain
separate. Infinite raw free energy is not a GU falsification or a universal
obstruction to causal finite-energy noise.
