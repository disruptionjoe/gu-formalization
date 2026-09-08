---
title: "K144 explicit screened Friedrichs threshold wave"
status: active_research
doc_type: conditional_explicit_screened_one_excitation_spectrum_threshold_and_projected_scattering_result
created: 2026-09-07
date: 2026-09-07
claim_ceiling: exact repository-owned theorem for one explicitly fixed positive self-inclusive vacuum-plus-one-excitation signed-rook Friedrichs benchmark that its thirty-six channels split into nine scalar bright blocks and twenty-seven free combinations, its complete point spectrum is the ninefold bound energy zero, its sole threshold has full impurity rank and a vacuous dark compression, its bright impurity response has square-root onset and t^-3/2 compact-cutoff decay, and finite-rank resolvent comparison gives complete wave operators only on this projected carrier; no complete interacting Fock residual census, many-body Mourre/Moller/Ruelle or NESS theorem, physical selector, smooth unreduced parent, Weinstein/source/GU action, Born derivation, prediction or confirmation follows
manifest: lab/process/k144-explicit-screened-friedrichs-threshold-wave.json
probe: tests/channel-swings/k144_explicit_screened_friedrichs_threshold_probe.py
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# K144 explicit screened Friedrichs threshold wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: INTERNAL_STRUCTURAL_ONLY.

Scope: this packet fixes and completely solves one repository-supplied
vacuum-plus-one-excitation Friedrichs projection of K139--K143's signed rook
control. It is a nonzero-coupling threshold benchmark, not an invariant sector
of the complete number-changing Fock Hamiltonian and not a physical parameter
selection. Its exact scattering statement binds only this projected linear
model.

```gu-typed-objects
result: one fixed positive self-inclusive screened signed-rook Friedrichs benchmark decomposes into nine scalar bright blocks plus twenty-seven free continua, has exactly nine bound states at energy zero and absolutely continuous spectrum [5/4,infinity), has no dark impurity threshold denominator or impurity-local threshold pole, and has complete one-excitation wave operators while the interacting Fock lift remains open
carrier: C9 impurity direct-sum L2(R;C36) vacuum-plus-one-excitation projection of the positive signed-rook control LAYER=observed CHIRALITY=S-FULL-DIRAC
pairing: standard positive direct-sum Hilbert pairing; the thirty-six continuum channels use dp and the point normalization (2 pi)^(-1/2) ON=repository_projected_signed_point_control
real_structure: K140's supplied positive particle/hole real structure is retained; equal particle/hole parameters are chosen for the benchmark and are not selected by charge conjugation or a source action
grading: impurity states are even, particle/hole channel labels retain the signed CAR ancestry, and the projected carrier contains only the vacuum/discrete and one-continuum summands
action_owner: repository-construction -- m=kappa=|q|=|g_plus|=|g_minus|=1, the positive screened convention, subtraction energy zero and W=0 are fixed benchmark data, not Weinstein/source/GU-owned values
target: complete projected bound/continuous spectrum, threshold Gamma matrix, dark compression, bright local decay and exact one-excitation scattering boundary MAP-TYPE=intertwiner
```

## Inline preflight bookend

K143 left a numerical-looking gate, but the first useful fixed family should
remove rather than hide algebra. The selected family keeps all thirty-six
signed endpoint channels nonzero, chooses equal masses and couplings, and uses
the positive screened self energy. Rook endpoint orthogonality then makes the
complete channel decomposition exact before any root search.

Object retrieval found K139's endpoint contraction, K140's finite Schur
response, K142's point-density threshold law and K143's `Gamma_tau`/dark-
denominator rule. It found no earlier artifact fixing these parameters or
solving the resulting spectrum. No correction-registry entry supersedes those
inputs. The route census covered direct finite-rank reduction, Weyl-function
monotonicity, certified roots, threshold expansions, limiting absorption,
local decay, trace-class scattering, Pauli-restricted residual channels,
many-body Mourre theory and source ownership. Exact block reduction dominates
a numerical diagonalization; certified root isolation is the fallback only if
the scalar sign identity fails.

## 1. Freeze the family and its exact scope

Work on

```text
H_1 = C^9 direct-sum L2(R;C^36).                       (1)
```

For every particle and hole channel fix

```text
m=1,  kappa=1,  |q|=1,  g_+=g_-=1.                   (2)
```

Use K142's positive self-inclusive screened convention. With at most one
matter excitation there is no pair term; the Yukawa field contributes only
the exact diagonal self energy `q^2/(4 kappa)=1/4`. Thus

```text
epsilon(p)=sqrt(1+p^2)+1/4,   tau_0=inf epsilon=5/4. (3)
```

Subtract the point self energy at `z_*=0` and set the resulting renormalized
Hermitian extension `W=0_9`. This choice defines the benchmark. It is not a
claim that zero is preferred physically or invariant under a change of
subtraction coordinate.

Let `Gamma:C^36->C^9` send each particle column for `e=(u,v)`, `u<v`, to
`|v>` and its hole column to `|u>`. Every rook vertex is incident to four
edges, different rows have disjoint column support, and therefore

```text
Gamma Gamma*=4 I_9,   rank Gamma=9,   dim ker Gamma=27. (4)
```

The normalized row vectors give nine orthogonal bright continuum
combinations. A channel unitary decomposes (1) into nine identical scalar
Friedrichs blocks and twenty-seven untouched free channel-label continua.
Because `epsilon(p)=epsilon(-p)`, point coupling reaches only the even momentum
branch inside each bright block; its odd branch is also free. The twenty-seven
label combinations are channel-dark, not impurity-dark; (4) has no dark
impurity vector.

## 2. The complete bound spectrum is exactly zero with multiplicity nine

The subtraction-normalized scalar Weyl function below `tau_0` is

```text
M(z)=integral_R dp/(2 pi)
     [1/(epsilon(p)-z)-1/epsilon(p)]
    =z integral_R dp/(2 pi epsilon(p)(epsilon(p)-z)). (5)
```

It is finite for real `z<5/4`, vanishes at zero, and has the sign of `z`.
Each bright block has scalar Schur denominator

```text
f(z)=-z-4M(z).                                        (6)
```

For `z<0`, both terms in (6) are positive. For `0<z<5/4`, both are
negative. Hence zero is the unique subthreshold root. Its eigenvector for
`u in C^9` has continuum tail

```text
psi_u(p)=-(2 pi)^(-1/2) Gamma* u/epsilon(p),           (7)
```

which is square integrable because `epsilon(p)^-1=O(|p|^-1)`. The root
therefore supplies nine genuine orthogonal bound states.

For `E>5/4`, the boundary value of (5) has strictly positive imaginary part
on every bright block. Thus (6) cannot vanish on the real continuum. The
twenty-seven free multiplication channels have no `L2` eigenvectors. The
explicit boundary formula also leaves no singular-continuous support. The
complete spectral census on (1) is

```text
sigma_p(H_1)={0}, multiplicity 9;
sigma_ac(H_1)=[5/4,infinity), 36 channel species,
              spectral multiplicity 72;
sigma_sc(H_1)=empty.                                  (8)
```

Equation (8) is not the spectrum of the complete screened Fock Hamiltonian.
The projection suppresses two-and-higher excitation residual clusters and is
not claimed invariant under the full number-changing defect.

## 3. The sole threshold is bright on the impurity and free in 27 channels

The residual bound spectrum has only `E_b=0`; all thirty-six one-particle
channels have the same screened threshold. K143's structural rule therefore
gives one threshold,

```text
tau=E_b+m+q^2/(4 kappa)=0+1+1/4=5/4,                 (9)
Gamma_tau=Gamma,  D_tau=4 I_9.                       (10)
```

Thus `ker D_tau={0}`. The compressed dark denominator is a zero-dimensional
operator, and its invertibility test is vacuous. There is no threshold
eigenvalue or impurity-local dark resonance. The separate `ker Gamma` still
contains twenty-seven exactly free continuum combinations, whose ordinary
one-dimensional branch point remains. Calling those combinations a dark
impurity denominator would reverse the map and repeat the distinction K143
made explicit.

## 4. Bright response is regularized, not the complete channel resolvent

For `E>5/4`, put `s=E-1/4`. The free point density and Weyl imaginary part are

```text
rho_0(E)=s/(pi sqrt(s^2-1)),
Im M(E+i0)=pi rho_0(E).                               (11)
```

Writing `E=5/4+delta`, both behave as `(2 delta)^-1/2` to leading order.
Below threshold,

```text
M(5/4-delta)~1/sqrt(2 delta).                         (12)
```

Consequently the inverse bright denominator vanishes as

```text
f(E+i0)^-1=O(sqrt(delta)),                            (13)
```

and the impurity-local spectral density has the same square-root onset.
Against a smooth compact energy cutoff, its Fourier transform is
`O(t^-3/2)` after the nine bound states are projected out.

This is a finite-dimensional point/impurity response estimate. The full
channel resolvent retains the free one-dimensional threshold branch in the
twenty-seven uncoupled combinations and continuum propagation terms. K144
does not claim a full weighted-channel limiting-absorption estimate uniformly
at the threshold.

## 5. Scattering closes exactly on this projection and nowhere else

The resolvent formula factors every interaction correction through the nine
impurity coordinates and nine resolvent-dressed continuum vectors. Relative
to the decoupled comparison, the resolvent difference therefore has rank at
most eighteen and is trace class at one nonreal spectral parameter. The
Kato--Rosenblum/resolvent-comparability theorem gives existence and
completeness of the two one-excitation wave operators on the absolutely
continuous subspace. The twenty-seven free combinations scatter trivially;
the nine bright combinations carry the scalar Friedrichs phase.

This is ordinary finite-rank Friedrichs scattering, not many-body Moller or
Ruelle asymptotic completeness. It supplies a positive control for the exact
`Gamma_tau` and threshold logic. A full-Fock lift must still compute the
interacting residual spectra, Pauli-restricted `Gamma_tau` at every threshold,
compressed denominators whenever rank falls, commutator regularity and
high-energy estimates.

## Inline postflight bookend

- **Strongest advance:** one fully fixed nonzero signed-rook screened family
  now has a complete bound, continuous and threshold census on its declared
  vacuum-plus-one-excitation carrier.
- **Strongest structural simplification:** disjoint endpoint-row support gives
  nine identical bright blocks and twenty-seven exactly free channel-label
  combinations; point coupling reaches only each bright block's even momentum
  branch, leaving its odd branch free.
- **Strongest threshold result:** the sole impurity threshold has rank nine,
  zero dark dimension and a vacuous compressed denominator; the bright
  impurity response vanishes like a square root rather than forming a pole.
- **Strongest scoped scattering result:** finite-rank resolvent comparison
  closes wave-operator completeness for this Friedrichs projection.
- **Strongest overclaim:** “the complete screened Fock model is asymptotically
  complete.” Refused. The projection is not an invariant full-Fock theorem
  and contains none of the higher residual cluster or Pauli data.
- **Strongest contrary construction:** remove one signed endpoint family or
  enter a Pauli-blocked residual state and `Gamma_tau` can lose rank, reviving
  a nonvacuous compressed dark denominator.
- **Weakest propagation seam:** impurity-local square-root onset does not make
  the full weighted channel resolvent uniform through a one-dimensional free
  branch point.

The companion probe checks the rook channel map, its exact Gram matrix and
rank/nullity, the Weyl sign/root law, bound-tail integrability, threshold
asymptotics, the complete threshold compression and every ownership boundary
under baseline-first hostile mutations.

## Next condition

Lift the calculation to the first genuinely invariant residual family of the
number-changing signed Fock model. Enumerate its bound states and Pauli-
available escape channels, compute each `Gamma_tau`, and apply the compressed
denominator test wherever its rank drops. Then prove the problem-matched
Mourre commutator and high-energy estimates on the continuous subspace before
claiming many-body Moller/Ruelle completeness. A separate open-system theorem
is still required for return to NESS and current. Physical and source/GU
selection of the free operator, polarization, charges, couplings, `W`,
`kappa`, domain and state remains independent.

## Reproduction

```bash
python3 tests/channel-swings/k144_explicit_screened_friedrichs_threshold_probe.py
python3 tests/channel-swings/k144_explicit_screened_friedrichs_threshold_probe.py --selftest
```
