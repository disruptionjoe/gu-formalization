---
title: "K141 infinite-volume local point and screened Gauss wave"
status: active_research
doc_type: conditional_common_fock_thermodynamic_signed_point_operator_and_screened_gauss_boundary_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned theorem for K140's supplied positive particle/hole control that normalized momentum-cell extensions place all circle models on one continuum antisymmetric Fock carrier, the free operators and resolvent-dressed signed point data converge there, and K139's matched boundary-transform construction consequently has a thermodynamic norm-resolvent limit at fixed finite couplings and fixed finite Hermitian extension coordinate; a massive one-dimensional screened Gauss kernel changes the separated-pair energy from linear growth to q^2(1-exp(-kappa R))/(2 kappa), defeating that witness, but no all-sector screened-Fock relative bound, screening-mass selector, Moller/Ruelle completeness, NESS/current, smooth unreduced parent, Weinstein/source/GU owner, Born derivation, prediction or confirmation follows
manifest: lab/process/k141-infinite-volume-local-point-screened-gauss-wave.json
probe: tests/channel-swings/k141_infinite_volume_local_point_screened_gauss_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K141 infinite-volume local point and screened Gauss wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) 126
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> lab/methods/source-native-comparator-routing.md and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet stays on K139--K140's repository-supplied positive
particle/hole point control. It constructs a common carrier for its changing
circle volumes and takes the local renormalized defect to infinite volume. It
also tests one named massive screened Gauss law against K140's neutral-pair
witness. It does not select the polarization, extension, couplings, screening
mass or physical state and does not reconstruct a source/GU action.

```gu-typed-objects
result: normalized momentum-cell extensions put the signed point models on one continuum Fock carrier and converge in norm resolvent at fixed supplied polarization, couplings and finite extension coordinate; the massive screened Gauss pair energy saturates, while an all-sector screened-Fock bound remains unproved
carrier: C9 impurity and C512 Klein module tensored with antisymmetric Fock space over L2(R;C36), with each circle lattice embedded as normalized momentum-step functions LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive particle/hole Fock Hilbert pairing and finite-dimensional Hermitian boundary pairing; the screened charge form uses the positive Green kernel of -d_x^2+kappa^2 ON=repository_signed_point_control
real_structure: the supplied positive particle/hole real structure and charge-conjugation relation from K140 are retained; neither the common embedding nor screening selects them
grading: matrix units are even, Klein/CAR fields are odd, defect monomials are even, and fermion number grades the free-relative estimates
action_owner: repository-construction -- the signed free operator, time orientation, polarization, couplings, W, screening mass kappa, Gauss law and state are not selected by Weinstein's source or a GU action
target: common-Hilbert thermodynamic norm-resolvent limit for the local signed point defect plus a massive-screened separated-pair test and all-sector boundary MAP-TYPE=intertwiner
```

## Inline preflight bookend

K140 proves the correct `L^-1/2` coefficient scaling but explicitly stops
before identifying the varying box Hilbert spaces. Its other live branch asks
whether a named screened or local-neutral Gauss representation survives the
neutral-pair test. Those two questions are compatible: the first is an
operator-convergence problem in momentum space, while the second is an exact
Green-kernel discriminator in position space.

Mechanism retrieval found K139's cutoff-uniform Neumann inverse and matched
subtraction theorem, K140's volume-uniform resolvent coefficient, and no prior
common-carrier or screened-pair result. The route census covered
step-function/Galerkin embeddings, generalized resolvent convergence,
second-quantized relative bounds, IBC boundary transforms, Mosco convergence,
joint ultraviolet/volume limits, Yukawa Green functions, local neutrality,
one-dimensional fermionic stability, scattering and source ownership. A
position-box exhaustion obscures the point normalization. The momentum-cell
extension makes it exact and leaves only bounded multiplier errors. For the
Gauss branch, solving the massive Green problem is decisive before attempting
an all-sector many-body estimate. Computation checks the cell and kernel
identities; it is not the proof.

## 1. One continuum carrier contains every normalized box model

Let `delta=2 pi/L` and partition the momentum line into

```text
I_(n,delta)=[n delta,(n+1)delta),
V_delta=span{delta^-1/2 1_(I_(n,delta)): n in Z}
          subset L2(R).                                (1)
```

The map

```text
J_delta e_n=delta^-1/2 1_(I_(n,delta))                 (2)
```

is an isometry from the circle momentum space `l2(Z)` onto `V_delta`. A
normalized point coefficient `L^-1/2` becomes

```text
L^-1/2 delta^-1/2=(2 pi)^-1/2                          (3)
```

on every cell. Thus K140's normalization is exactly the continuum Fourier
normalization, not merely asymptotic.

Put `omega(p)=sqrt(m^2+p^2)` and

```text
omega_delta(p)=omega(n delta), p in I_(n,delta).       (4)
```

Multiplication by `omega_delta` leaves both `V_delta` and its orthogonal
complement invariant, and its restriction to `V_delta` is exactly the circle
dispersion. Since `omega` is one-Lipschitz,

```text
||omega_delta-omega||_infinity <= delta.               (5)
```

Extending the circle model by the free spectator Fock space over
`V_delta^perp` therefore places every volume on the single carrier

```text
H=C9 tensor C512 tensor F_a(L2(R;C36)).                (6)
```

This extension is transparent: under the fermionic exponential law it is the
original box model tensored with decoupled free spectators. It is not a claim
that the unextended changing Hilbert spaces are literally identical.

## 2. The free and boundary data converge on all Fock sectors

Let `H_(0,delta)=dGamma(omega_delta)` and `H_0=dGamma(omega)`, including the
fixed finite impurity term. On the `r`-particle sector, (5) gives

```text
|H_(0,delta)-H_0| <= r delta <= (delta/m) dGamma(omega).
                                                               (7)
```

After one common finite lower shift, the scalar resolvent identity applied on
the joint momentum representation makes (7) uniform in `r`. Hence

```text
||(H_(0,delta)+a)^-1-(H_0+a)^-1|| -> 0.               (8)
```

The resolvent-dressed point coefficient on the common carrier is

```text
h_(delta,lambda)(p)
  =(2 pi)^-1/2(omega_delta(p)+lambda)^-1,               (9)
h_lambda(p)=(2 pi)^-1/2(omega(p)+lambda)^-1.
```

Equations (5), (9) and an integrable `p^-2` square majorant give
`h_(delta,lambda)->h_lambda` in `L2(R)`. Fermionic creation and annihilation
by an `L2` vector are bounded with that vector norm. Every finite
edge/polarity sum in K139's boundary map therefore satisfies

```text
G_(delta,lambda) -> G_lambda in operator norm.         (10)
```

K140's uniform large-`lambda` estimate chooses one chart with
`sup_delta ||G_(delta,lambda)||=q<1`, so the Neumann inverses obey

```text
(1-G_(delta,lambda))^-1 -> (1-G_lambda)^-1             (11)
```

in norm. The same argument with the standard factor two works on the
particle-number graph after enlarging the compensated auxiliary shift.

## 3. The local signed point defect has a thermodynamic operator limit

Use a physical momentum cutoff `Lambda` and match at each `delta` the K139
endpoint subtraction

```text
c_(delta,Lambda)(lambda)
 =delta/(2 pi) sum_(|n delta|<=Lambda)
       (omega(n delta)+lambda)^-1.                     (12)
```

The divergent logarithm is common. Subtracted contraction differences have a
uniform `p^-2` tail, so Riemann sums converge and the ultraviolet remainder is
uniform as `delta->0`. The point-annihilation trace is bounded from the free
operator graph because its graph-dual coefficient is proportional to
`omega^-1 in L2(R)`. Its step version converges by (5); the four signed
exchange blocks do likewise. Every higher bidirected word carries another
`G_delta` and is dominated by the common geometric series `sum_j q^j`.

Consequently the regular pullbacks at a fixed renormalized finite Hermitian
boundary coordinate `W` satisfy

```text
||(K_delta-K)(H_0+a)^-1|| -> 0,                        (13)
```

after the common shift. Combining (11), (13) and K139's exact inverse
factorization gives self-adjoint operators

```text
H_delta^pol,W -> H_infinity^pol,W                      (14)
```

in norm resolvent on (6), with
`Dom(H_infinity^pol,W)=(1-G_lambda)^-1 Dom(H_0)`. The
uniform `p^-2` tails also allow `Lambda->infinity` and `delta->0` along any
cofinal path after matched subtraction; the sequential construction is not an
order-of-limits artifact.

Equation (14) is the common interacting infinite-volume operator K140 left
open, but only for the **local signed point defect** on the supplied positive
polarization, at fixed finite couplings and fixed finite `W`. It does not
include K139's raw unscreened Coulomb form and does not physically select any
of those inputs.

## 4. A massive screened Gauss law defeats the separated-pair witness

Take the named one-dimensional screened equation

```text
(-d_x^2+kappa^2) phi=rho,       kappa>0,               (15)
```

whose positive Green kernel is

```text
Y_kappa(x-y)=exp(-kappa|x-y|)/(2 kappa).                (16)
```

For point charges `rho_R=q delta_0-q delta_R`, the field energy is

```text
E_kappa(R)
 =1/2 <rho_R,Y_kappa*rho_R>
 =q^2/(2 kappa)(1-exp(-kappa R)).                      (17)
```

It is monotone but uniformly bounded by `q^2/(2 kappa)`, whereas K140's
massless limit grows as `q^2 R/2`. For identical fixed-shape probability
profiles, the Fourier multiplier is multiplied by `|eta_hat(k)|^2<=1`, so
the same point-pair value is an upper bound. The separated-neutral-pair
witness therefore does **not** obstruct this massive screened
representation.

This is a genuine route switch, not a thermodynamic Gauss completion. The
positive many-charge kernel gives the elementary Fock estimate

```text
0 <= E_kappa <= q_max^2 N^2/(4 kappa),                 (18)
```

but `N^2` is not bounded by the massive free energy using only
`N<=m^-1 H_0`. Closing a volume-uniform all-sector form bound requires an
additional one-dimensional fermionic density/stability estimate on the
specific thirty-six-species carrier, including its self-energy and normal-
ordering convention. That estimate is not proved here. Nor does the
repository select `kappa`: sending `kappa` to zero recovers K140's obstruction.

## Inline postflight bookend

- **Strongest advance:** the supplied signed point control now has one common
  continuum Fock carrier and a norm-resolvent thermodynamic limit of its local
  renormalized defect.
- **Strongest exact route switch:** the massive screened Green kernel changes
  the neutral-pair energy from linear growth to a bounded saturation law.
- **Strongest boundary:** the pair result does not itself establish an
  all-sector screened Fock form bound; the available elementary estimate is
  quadratic in particle number.
- **Strongest overclaim:** “K141 constructs the physical infinite-volume GU
  Hamiltonian and therefore opens NESS.” Refused. The operator is a supplied
  repository control with unselected polarization, `W`, couplings and state;
  screening is not yet included in the all-sector operator.
- **Strongest contrary route:** a relativistic one-dimensional Lieb--Thirring
  or local-number estimate may close the screened all-sector form and can be
  pursued next. Conversely, removing the screening mass restores the
  separated-pair obstruction.
- **Weakest reproducibility seam:** (14) compares common-carrier extensions,
  not bare resolvents on unidentified changing spaces. The spectator
  complement and fixed renormalization coordinate must remain explicit.

The companion probe checks the exact cell normalization, dispersion and
resolvent convergence, point-vector convergence, screened saturation law and
manifest claim boundary with baseline-first hostile mutations. No
Moller/Ruelle completeness, asymptotic completeness, interacting NESS,
microscopic current, smooth unreduced connection/BRST parent,
Weinstein/source/GU action, Born rule, held-out score, prediction,
confirmation, canon, paper, release or public-posture move follows.

## Next condition

Prove or refute the missing thirty-six-species relativistic fermionic
density/local-number estimate needed to add the massive screened Gauss form to
`H_infinity^pol,W` uniformly over Fock space. In parallel, establish spectral
threshold and local-decay estimates for the local operator (14). Only those
results can decide whether a screened interacting Hamiltonian and then
Moller/Ruelle wave operators are available. Physical selection still requires
an actual response datum or action principle, and a source/GU action must
independently own the free operator, time orientation, polarization, charges,
couplings, domain and state.

## Reproduction

```bash
python3 tests/channel-swings/k141_infinite_volume_local_point_screened_gauss_probe.py
python3 tests/channel-swings/k141_infinite_volume_local_point_screened_gauss_probe.py --selftest
```
