---
title: "K143 periodic screened Mosco, HVZ, and dark-rank wave"
status: active_research
doc_type: conditional_periodic_screened_strong_resolvent_hvz_threshold_and_dark_channel_rank_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned theorem for K142's supplied positive particle/hole control that the periodic massive Yukawa forms converge on compact finite-particle cores, their uniform relativistic local-exclusion bound and finite signed IBC chart give Mosco convergence and hence strong-resolvent convergence to the direct common-carrier screened Hamiltonian, while a translating seam pair blocks uniform kernel or relative-form convergence and no norm-resolvent upgrade follows; independently, geometric Fock localization gives the essential-spectrum threshold union from residual bound energies plus escaping rest masses subject to conserved-sector compatibility, and the signed three-by-three rook endpoint matrix has rank nine for equal nonzero particle/hole couplings although the 36-to-9 channel map has a 27-dimensional kinematic kernel; threshold resonances still require residual finite-matrix tests, and no uniform propagation, Moller/Ruelle completeness, NESS/current, physical extension or screening selector, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k143-periodic-screened-mosco-hvz-dark-rank-wave.json
probe: tests/channel-swings/k143_periodic_screened_mosco_hvz_dark_rank_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K143 periodic screened Mosco, HVZ, and dark-rank wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet remains on K139--K142's repository-supplied positive
particle/hole point control. It adds the periodic massive screened forms to
K141's common-carrier approximation and classifies their exact convergence
topology. Separately it identifies the geometric many-body threshold set and
the finite endpoint ranks of the complete signed rook control. It does not
select the polarization, extension, couplings, screening mass, charge sector
or state and does not reconstruct a source/GU action.

```gu-typed-objects
result: periodic screened forms Mosco-converge through the finite signed IBC chart and therefore converge in strong resolvent, with a seam witness blocking uniform relative-form convergence; geometric localization gives residual-bound-energy plus escaping-mass HVZ thresholds, and the equal nonzero signed rook endpoint matrix is full rank despite a 27-dimensional kinematic channel kernel
carrier: C9 impurity and C512 Klein module tensored with antisymmetric Fock space over L2(R;C36), using K141's momentum-cell common-carrier extensions and K139's finite signed boundary chart LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive particle/hole Fock Hilbert pairing and finite-dimensional Hermitian boundary pairing; positive periodic and line screened forms use the Green kernels of -d_x^2+kappa^2 ON=repository_signed_point_control
real_structure: K140's supplied positive particle/hole real structure and charge-conjugation relation are retained; neither Mosco convergence, HVZ localization nor endpoint rank selects them
grading: matrix units are even, Klein/CAR fields are odd, defect monomials are even, fermion number grades the form bounds, and asymptotic channels are graded by escaping particle/hole multiplicity and any retained conserved charge
action_owner: repository-construction -- the signed free operator, time orientation, polarization, charges, couplings, W, kappa, Gauss law, sector and state are not selected by Weinstein's source or a GU action
target: periodic screened strong-resolvent limit, geometric many-body threshold set and signed rook endpoint/dark-channel rank classification MAP-TYPE=intertwiner
```

## Inline preflight bookend

K142 leaves two independent high-effect branches. The first asks whether its
direct line screened form is actually reached by periodic boxes through the
singular point domain. The second asks which many-body thresholds and dark
directions obstruct promoting K142's first-channel decay to scattering. They
use different instruments: periodic Green kernels, Mosco recovery/liminf and
boundary-coordinate transport for the first; geometric Fock localization and
finite endpoint linear algebra for the second.

Object retrieval found K141's common momentum-cell carrier, K142's uniform
all-sector screened bound and finite `L2 intersect L4` boundary-mode split,
and K139's exact signed endpoint matrix. It found no prior periodic screened
form transport or full signed-rook rank census. Mosco convergence is used only
for its standard strong-resolvent consequence; the distinction from norm-
resolvent convergence is kept explicit. The fermionic HVZ literature is a
method anchor for geometric localization on Fock space, not a substitute for
checking the present point chart and screened cross terms
([arXiv:1211.4965](https://arxiv.org/abs/1211.4965)). No canonical correction
supersedes K139--K142.

The route census covered periodic image sums and Fourier multipliers, compact
core recovery, weak lower semicontinuity, finite boundary-coordinate changes,
strong versus norm resolvent topology, translating seam witnesses, massive
Fock localization, residual cluster spectra, superselection compatibility,
rook endpoint matrices, channel-map kernels, dark threshold Schur complements,
Mourre regularity, high-energy estimates and source ownership. A global
operator-norm comparison is rejected before computation because periodic
topology remains visible to states translating with the seam. Computation is
restricted to exact kernel identities, convergence witnesses and finite graph
ranks; it is not the Mosco or HVZ proof.

## 1. The periodic Yukawa form has the correct local limit

Let the centered circle have length `L`, let `d_L(x)` be circular distance to
zero, and put

```text
Y_(kappa,L)(x)
 =sum_(n in Z) exp(-kappa|x+nL|)/(2 kappa)
 =cosh(kappa(L/2-d_L(x)))/(2 kappa sinh(kappa L/2))
 =L^-1 sum_(r in Z) exp(2 pi i r x/L)/((2 pi r/L)^2+kappa^2). (1)
```

It is positive, has exact circle integral `kappa^-2`, and

```text
Y_(kappa,L)(0)=coth(kappa L/2)/(2 kappa)
              ->1/(2 kappa).                          (2)
```

For every fixed `R`, the image sum gives

```text
sup_(|x|<=R)|Y_(kappa,L)(x)-Y_kappa(x)|
 <= exp(-kappa(L-R))/(kappa(1-exp(-kappa L)))          (3)
```

once `L>2R`. Thus the periodic positive field energy and its diagonal self
term converge on antisymmetric finite-particle wave functions whose position
support stays in one fixed compact set. Smooth compactly supported regular
coordinates, together with the finitely many K142 boundary modes, form a core
after applying K139's bounded inverse boundary chart.

K142's local-number proof is uniform in volume. Periodizing the kernel only
adds exponentially weighted neighboring cells, so for the same finite species
count `F=36`, mass gap and bounded charges,

```text
0 <= E_(kappa,L)
   <= C F q_*^2(kappa^-2 T_L+kappa^-1 N),              (4)
```

with one `L`-independent constant for all sufficiently large boxes. The
periodic normal-ordering subtraction uses
`q_alpha^2 Y_(kappa,L)(0)/2` and converges to K142's
`q_alpha^2/(4 kappa)` term. A common lower shift therefore controls the
positive and normally ordered families.

## 2. Mosco convergence survives the signed IBC chart

Work first in K139's regular coordinate `phi`. For the Mosco recovery
condition, approximate any limiting form vector in the graph/form norm by the
compact finite-particle core, then use K141's momentum-cell projections. On
each fixed core vector, (3), the Riemann-sum free/point convergence and the
finite boundary-mode convergence make every term converge.

For the weak liminf condition, take a weakly convergent sequence with bounded
shifted form energy. The mass gap and (4) bound particle number and local
kinetic energy. Localize to a fixed compact region and finite particle
truncation, pass to the limit there using positivity and local compactness,
then let the localization radius and truncation grow. Cross-boundary Yukawa
terms vanish exponentially and discarded positive field energy can only
increase the liminf. For the normally ordered family the convergent linear
self term is restored after the common lower shift.

Let `U_L=1-G_L` and `U=1-G` be the compensated signed boundary charts.
K141 proves `U_L^(-1)->U^(-1)` in operator norm and on the particle-number
graph, while K142 proves that the finite singular modes remain in the screened
form domain. Consequently recovery sequences and weak-liminf sequences
transport in both directions without losing boundedness. The pulled-back
periodic screened forms therefore Mosco-converge to K142's line form:

```text
q_(kappa,L,W)  --Mosco-->  q_(kappa,infinity,W).       (5)
```

After the common lower shift, (5) gives

```text
(H_(kappa,L,W)+a)^(-1) psi
   ->(H_(kappa,infinity,W)+a)^(-1) psi                 (6)
```

for every carrier vector `psi`: strong-resolvent convergence of both the
self-inclusive positive and normally ordered screened Hamiltonians.

## 3. The periodic seam forbids a norm upgrade from these estimates

The convergence is not uniform on the unit form ball. Put two fixed-width
wave packets at `-L/2+r/2` and `L/2-r/2`, with fixed `r>0`. Their free energy
and particle number are independent of `L`. On the circle their separation is
`r`, so the cross kernel tends to `Y_kappa(r)>0`; on the line their separation
is `L-r`, so the cross kernel tends to zero. Thus

```text
sup_(bounded free-form vectors)
 |E_(kappa,L)-E_kappa|  not->0.                        (7)
```

The packets escape weakly to zero, so (7) does not contradict the localized
Mosco argument. It does show exactly why K141's norm-resolvent proof for a
local defect cannot simply absorb the periodic interaction: the torus seam is
invisible pointwise and visible in the global supremum. K143 therefore proves
strong-resolvent convergence and an obstruction to the available relative-
form/norm-resolvent route. It does not claim an abstract impossibility theorem
for every differently identified or modified finite-volume approximation.

## 4. Geometric localization gives the many-body threshold set

Fix any conserved total label `Q` actually carried by the selected control;
if no such superselection is imposed, take the union over `Q`. Let
`E_j(Q-q(n))` be a discrete bound energy of the residual localized Hamiltonian
after an escaping cluster with multiplicities `n=(n_alpha)` and total label
`q(n)` is removed. Let `m_alpha>0` be the corresponding particle/hole rest
masses. The geometric threshold set is

```text
T_Q=closure{E_j(Q-q(n))+sum_alpha n_alpha m_alpha:
            sum_alpha n_alpha>=1, compatible(Q,n,j)}. (8)
```

Because every escaping relativistic particle has continuous energy
`[m_alpha,infinity)`, the essential spectrum is the union of the attached
half-lines,

```text
sigma_ess(H_Q)
 =closure union_(tau in T_Q)[tau,infinity)
 =[Sigma_Q,infinity),   Sigma_Q=inf T_Q.               (9)
```

The localization hypotheses are present on this supplied control: the point
defect is fixed at the origin and its resolvent-dressed boundary vectors are
`L2`; the Yukawa cross-cluster interaction vanishes exponentially; the mass
gap controls escaping multiplicity below a fixed energy; finite CAR species
and K142's form estimate control localization errors. The upper inclusion is
constructed by a residual bound vector times translated antisymmetric wave
packets. The lower inclusion follows by partitioning into a compact localized
cluster and at least one escaping massive particle, with point and screened
cross terms tending to zero.

Equation (9) is a complete structural HVZ formula, not a numerical threshold
list. The values of `E_j`, the compatible `Q` sectors and even the lowest
channel depend on the supplied `W`, couplings, charges and `kappa`. Higher
thresholds in (8) remain relevant to Mourre estimates even though their
half-lines overlap in (9).

## 5. The signed rook is boundary-full-rank but channel-dark

For every oriented rook edge `e=(u,v)`, `u<v`, K139 uses
`B_e=|v><u| tensor kappa_e`. The coefficient of the divergent endpoint Weyl
term is

```text
D_g=sum_e(|g_(e,+)|^2 |v><v|+|g_(e,-)|^2 |u><u|)
   =diag(d_0,...,d_8),                                 (10)
```

where

```text
d_x=sum_(e upper at x)|g_(e,+)|^2
    +sum_(e lower at x)|g_(e,-)|^2.                   (11)
```

Hence

```text
rank D_g=#{x:d_x>0},
ker D_g=span{|x>:d_x=0}.                              (12)
```

The three-by-three rook graph has degree four at every vertex. Equal nonzero
particle and hole couplings give `D_g=4g^2 I_9`, rank nine and no dark impurity
direction. The one-way particle-only endpoint matrix has rank eight and dark
vertex `0`; the hole-only matrix has rank eight and dark vertex `8`.

There are nevertheless 36 signed species endpoint columns. If `Gamma` is the
`9 by 36` endpoint channel map with `Gamma Gamma*=D_g`, equal nonzero signed
couplings give

```text
rank Gamma=9,        dim ker Gamma=36-9=27.            (13)
```

Those 27 combinations are kinematically invisible to the leading impurity
endpoint map and retain free-channel behavior. They are not dark impurity
directions and do not contradict K142's full-rank impurity-local
`t^-3/2` law.

At a many-body threshold `tau`, residual-state matrix elements and Pauli
availability replace `Gamma` by a finite channel matrix `Gamma_tau`. Define
`D_tau=Gamma_tau Gamma_tau*` and let `P_0` project onto `ker D_tau`. The exact
rank census remains

```text
rank D_tau=rank Gamma_tau,
dark impurity space=ker D_tau.                         (14)
```

On the range of `D_tau`, K142's inverse-square-root Weyl singularity is
inverted. On the dark space, a threshold eigenvalue or resonance is excluded
only if the finite compressed threshold denominator

```text
P_0[W_eff(tau)-M_reg(tau)]P_0                          (15)
```

is invertible after the ordinary Schur reduction against the bright range.
The repository supplies neither all residual bound vectors nor selected
`W,kappa,g`, so (14)--(15) are the complete computable census rule, not a
claim that every many-body threshold is bright or resonance-free.

## Inline postflight bookend

- **Strongest advance:** periodic positive and normally ordered screened forms
  reach K142's direct common-carrier Hamiltonians in strong resolvent through
  the finite signed IBC chart.
- **Strongest topology boundary:** a translating seam pair keeps an order-one
  periodic-versus-line interaction difference on a bounded free-form family.
  The available argument cannot promote Mosco convergence to norm resolvent.
- **Strongest independent advance:** geometric localization identifies every
  essential-spectrum channel by residual bound energy plus escaping rest
  masses, with the exact conserved-sector compatibility left visible.
- **Strongest rank result:** equal nonzero signed rook couplings give a full
  rank-nine impurity endpoint matrix, while the 36-channel endpoint map still
  has a 27-dimensional kinematic kernel.
- **Strongest overclaim:** “HVZ plus full endpoint rank proves scattering or
  NESS.” Refused. Threshold resonances, Mourre regularity, uniform weighted
  bounds, high energy, asymptotic completeness and state preparation remain.
- **Strongest contrary construction:** deleting one polarity restores an
  explicit dark impurity vertex; at a residual threshold, Pauli or selection
  zeros can similarly lower `rank Gamma_tau` even when the vacuum endpoint
  matrix is full rank.
- **Weakest reproducibility seam:** the structural threshold formula requires
  the selected control's local compactness and conserved-label decomposition.
  A different point extension or sector rule must recheck those hypotheses.

The companion probe checks the periodic image/closed/Fourier normalizations,
compact convergence and seam witness, the complete rook graph and signed/
one-way endpoint ranks, the 36-to-9 channel nullity, sample threshold unions,
and the manifest claim boundary under baseline-first hostile mutations. No
uniform weighted propagation, Moller/Ruelle completeness, interacting NESS,
microscopic current, physical `W` or `kappa`, smooth unreduced connection/BRST
parent, Weinstein/source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Next condition

For scattering, compute `Gamma_tau` and the compressed denominator (15) for
every residual bound state of one explicitly fixed `W,kappa,g` control, then
prove a Mourre/weighted-resolvent estimate uniformly away from and through the
surviving threshold set, including high energy. Only after threshold
eigenvalues and resonances are excluded or projected may the program attempt
Moller/Ruelle completeness and then a separate return-to-NESS/current theorem.
For thermodynamic approximation, norm-resolvent convergence would require a
topology-changing identification or boundary modification that defeats the
seam witness; the natural periodic family proved here supplies strong
resolvent only. Physical and source/GU selection remain independent.

## Reproduction

```bash
python3 tests/channel-swings/k143_periodic_screened_mosco_hvz_dark_rank_probe.py
python3 tests/channel-swings/k143_periodic_screened_mosco_hvz_dark_rank_probe.py --selftest
```
