---
artifact_type: construction_result
created: 2026-08-05
status: FREE_SPECTRAL_PARITY_FAILS_FIRST_ACTION_OWNED_CUBIC__INTERACTING_C_OPERATOR_REMAINS_OPEN__ALL_FINITE_LOCAL_ZERO_MODE_COMPLETIONS_NOSCREEN_OR_UNSOLVABLE__NORMALIZED_GLOBAL_PROJECTOR_SCREENS_CONDITIONALLY_WITH_DOMAIN_MEASURE_DATUM
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CORRECTS
ledger_rows: [LT-GR2b, LT-GR2c, LT-GR2d, LT-GR3, LT-GR5, LT-SM8]
scripts:
  - tests/channel-swings/first_interaction_krein_global_zero_mode_probe.py
  - tests/channel-swings/first_interaction_krein_global_zero_mode_independent.sage
registry: lab/process/first-interaction-krein-global-zero-mode.json
---

# First-interaction Krein grading and global zero-mode horn

## Result first

The preceding gate contained two different problems under one name. Source
reinspection corrects the first: GU's super-IG burden is an algebraic odd
extension whose bracket lands in the linear connection sector. Weinstein
expressly declines an action as a prerequisite for doing GU. Bracket,
equivariance, Jacobi, real form and global descent remain open; an odd action,
odd Noether identity and odd BV complex are not source-required by default.

The physical positivity problem belongs instead to the nonlinear interacting
metric/distortion theory. Its first exact result is adverse but sharply scoped.
The finite free TT pencil has the positive spectral majorant constructed in
the predecessor. The already-written scalar horn

\[
 I_{\rm sc}=\int\sqrt{-g}\left[(a+\beta\theta)R
        +{\kappa\over2}\theta^2-\rho\right]
\]

contains at constant `theta` the TT cubic vertex

\[
 V_3=c\,\theta h^2,
 \qquad c\ne0. \tag{1}
\]

In the `P`-eigenbasis, the observed metric coordinate is
`h=q_0+q_m`, with `q_0` even and `q_m` odd. Hence

\[
 V_3=c\theta(q_0^2+2q_0q_m+q_m^2). \tag{2}
\]

If `theta` is even, the mixed term is odd. If `theta` is odd, both diagonal
terms are odd. No multiplicative sign assigned to this scalar extends the
free spectral involution through (2). This kills that smallest extension of
the free `P`; it does not kill a nonlinear field-mixing or nonlocal interacting
`C`-operator.

The cosmology horn also becomes exact at the right level. Any finite local
completion of the trace equation has the form

\[
 K(\Box)R=2\rho,\qquad
 K(s)=a+c_1s+\cdots+c_Ns^N. \tag{3}
\]

On the constant mode, all derivatives vanish. If `a` is nonzero, then
`R=2rho/a` and the susceptibility is nonzero. If `a=0`, a nonzero constant
source violates the zero-mode solvability condition. Thus additional finite
local derivatives cannot turn tracking into constant-shift screening.

The smallest exact global horn uses a normalized functional `ell` with
`ell(1)=1`,

\[
 \Pi_0 f=1\,\ell(f),\qquad Q=1-\Pi_0, \tag{4}
\]

and couples the response only to `Q rho`. Then
`Q(rho+delta)=Q rho` for every constant `delta`. On a finite connected
transitive model with its invariant positive measure, (4) is the unique
self-adjoint rank-one projection onto constants and the construction has zero
free parameters after the domain and measure are supplied.

That last clause is the boundary and the opportunity. On a noncompact
Lorentzian spacetime there is no normalized translation-invariant volume
functional. One must supply or derive a compact domain, observer window,
state/weight, boundary prescription or another global completion. The wave
therefore identifies the missing object's type without pretending to have
derived it. It is not identified with the existing unknown `P2_datum`, and
P1/P2/P3 remain unused.

## Plain English

The free two-mode gravity system could be made positive by calling the usual
graviton even and its new partner odd. The first real interaction spoils that
simple rule: one part of the interaction wants the extra scalar even, while
another part wants it odd. The viable next question is whether the interacting
theory builds a more sophisticated positive inner product. Repeating the free
two-by-two calculation cannot answer it.

For dark energy, adding more local derivatives cannot make a constant vacuum
energy disappear, because derivatives do not see constants. A global
operation can: subtract the average before the source enters the curvature
equation. But “the average” only exists after saying over what domain and with
what measure. That domain/measure choice is now a concrete candidate for the
missing external information the source action needs.

## 1. Layer 0

| phrase | object here | not identified with |
| --- | --- | --- |
| super-IG | algebraic odd module and symmetric bracket into connection one-forms | an asserted odd action symmetry or BV differential |
| free spectral grading | linear involution `P` on the two-field TT pencil | the interacting `C`-operator |
| first interaction | constant-`theta`, off-shell TT Hessian of the written `(a+beta theta)R` horn | every cubic vertex of the ambient K77 action |
| local completion | a finite polynomial in covariant derivatives with fixed zero-order coefficient | a global constraint or nonlocal inverse |
| screening | invariance under an independent constant shift of `rho` | two fields merely tracking the same input |
| global average | a normalized functional on a specified domain/measure space | a canonically available average on noncompact Lorentzian `X` |
| datum candidate | type `ell: functions -> R`, `ell(1)=1`, with covariance/positivity/domain duties | current `P2_datum` without an identification theorem |

## 2. Divergent specialist preassessment

| lens | efficient demand | effect on construction |
| --- | --- | --- |
| variational GR | derive the cubic from the established TT Hessian | used the coefficient replacement `a -> a+beta theta` |
| Krein operator theory | test extension of `P`, not positivity in the abstract | all three parity monomials tested |
| BV/BRST | do not turn the super-IG bracket into a differential | even physical quotient kept separate |
| supergeometry | retain the actual algebraic descent burden | bracket/Jacobi/real form/global descent remain open |
| representation theory | test the full parity support | diagonal and mixed terms both retained |
| hyperbolic PDE | separate a zero-mode obstruction from characteristics | theorem limited to the constant mode |
| global analysis | state the domain and normalized functional | `ell` exposed as an owner, not notation |
| cosmology | perturb by an independent vacuum shift | tracking and screening remain distinct |
| source criticism | find the argument before pricing it | odd-action target corrected; new mechanisms unattributed |
| exact-computation engineering | use two exact routes and planted omissions | SymPy and Sage agree; truncation plants fail |

Pre-registered kill conditions fired twice before interpretation. A prose
matcher for the super-IG burden expected the wrong exact phrase, and the Sage
route initially compared a factorization object to a field element. Both were
repaired; neither altered the mathematical outcome.

## 3. Exact first-interaction obstruction

For one TT polarization, the predecessor's free matrices are

\[
 K=\begin{pmatrix}\alpha&1\\1&0\end{pmatrix},\qquad
 M=\begin{pmatrix}0&0\\0&b\end{pmatrix},\qquad L=K^{-1}M.
\]

For `m^2=alpha b !=0`,

\[
 P=1+{2L\over m^2}
  =\begin{pmatrix}1&2/\alpha\\0&-1\end{pmatrix}. \tag{5}
\]

The exact probe rechecks `P^2=1`, `[P,L]=0`, and `P^T K=KP`. Its eigenvectors
are

\[
 u_0=(1,0),\qquad u_m=(1,-\alpha),
\]

and the metric projection `(1,0)` evaluates to one on both. Therefore
`h=q_0+q_m` exactly.

At constant `theta`, the TT Hessian of the written scalar horn is obtained by
the already-established replacement of the Einstein coefficient
`a -> a+beta theta`. Its term linear in `theta` is (1), with nonzero
`c` whenever `beta` and the chosen nonzero TT symbol are nonzero. Under the
two possible scalar signs:

\[
 V_3(Pq,+\theta)-V_3(q,\theta)
   =-4c\theta q_0q_m,
\]

\[
 V_3(Pq,-\theta)-V_3(q,\theta)
   =-2c\theta(q_0^2+q_m^2). \tag{6}
\]

Neither vanishes. Omitting the mixed term falsely makes even `theta` pass;
omitting the diagonal terms falsely makes odd `theta` pass. Both plants are
in the executable certificate.

### Scope

Equation (6) proves no extension of the form

```text
(q0, qm, theta) -> (q0, -qm, plus_or_minus theta)
```

preserves this vertex. It does not classify general involutions that mix all
scalar/distortion fields, nonlinear field-dependent gradings, or the
nonlocal interacting `C` discussed by the repository's keep-and-grade lane.
The W132 exact identity still applies: a free positive subspace is unitary
only when the odd production block vanishes; the remaining route is an
interacting positive metric whose existence and locality must be constructed.

## 4. Finite local zero-mode theorem

Let `D` be any differential operator with `D 1=0`. For a finite polynomial

\[
 K(D)=a+\sum_{j=1}^N c_jD^j,
\]

one has `K(D)1=a1`. Therefore a constant source `2rho 1` has:

- `R=(2rho/a)1` if `a !=0`, with susceptibility `2/a`; or
- no solution satisfying the self-adjoint kernel compatibility condition if
  `a=0` and `rho !=0`.

This includes the predecessor's
`aR+(3 beta^2/kappa) Box R=2rho` and every finite higher-derivative extension
with the same local constant mode. Boundary conditions can remove or fix the
zero mode, but then they are part of the global data rather than a stronger
local equation.

The exact finite witness uses the connected four-cycle Laplacian `Delta` and
checks

\[
 (a+c_1\Delta+c_2\Delta^2)1=a1
\]

coefficientwise. Setting `a=0` leaves rank three and a nonzero constant source
outside the image.

## 5. Conditional global horn and constraint surplus

On the same finite connected model,

\[
 \Pi_0={1\over4}{\bf1}{\bf1}^T,
 \qquad Q=I-\Pi_0. \tag{7}

The exact checks give

\[
 \Pi_0^2=\Pi_0,\quad \Pi_0^T=\Pi_0,\quad
 \operatorname{rank}\Pi_0=1,\quad Q1=0,
 \quad [Q,\Delta]=0. \tag{8}

For any invertible invariant response operator, for example
`K_g=I+Delta`, define the conditional linear horn

\[
 K_gR=Q\rho. \tag{9}

Then

\[
 R[\rho+\delta1]=R[\rho]
\]

exactly, while the response on the three-dimensional inhomogeneous subspace
is nonzero.

There are four raw weights in `ell`. Normalization plus the three independent
cyclic-equality constraints has rank four, leaving zero freedom. This is a
positive constraint surplus **after** the finite transitive domain and its
measure class have been supplied. The construction is therefore informative,
not dismissed as shaped-to-fit.

The actual missing datum is upstream of those constraints. A normalized
translation-invariant volume does not exist on noncompact Minkowski space:
equal singleton/translated-cell weights are either positive and sum to
infinity or zero and cannot normalize. A physical horn must derive or supply
one of:

1. a compact global observed domain;
2. a normalized observer window;
3. a state or weight on the observable algebra;
4. a boundary/asymptotic prescription; or
5. another GU-native global functional with a proved covariance law.

Equation (9) is thus the smallest successful conditional model and a type
specification for the external datum/source-action build. It is not yet the
ambient `Y14` Euler equation.

## 6. Seven-axis audit

| layer | result | boundary |
| --- | --- | --- |
| Layer 0 | super-IG/action/BV and free-`P`/interacting-`C` separated; local/global separated | no identification with P2 |
| L1 substrate | exact two-field TT pencil and finite connected zero-mode model | full ambient carrier open |
| L2 observer | written scalar horn supplies the TT cubic | only constant-`theta` observed TT grade |
| L3 pairing | free Krein form and self-adjoint finite projector exact | interacting positive metric open |
| L4 causal order | constant mode theorem independent of characteristic choice | global Lorentzian domain open |
| L5 emergence | simple free parity fails at first interaction; global projector screens | neither mechanism is source-derived |
| L6 coordination | source correction, action ownership and ledger types composed | super-IG global descent still open |
| L7 positivity | no free-sign extension; conditional finite positive average | QFT `C`, loops and type-III control open |

## 7. What changes and what does not

The wave changes the work order:

1. do not spend further waves extending the free two-by-two `P` by scalar
   signs;
2. construct the first perturbative interacting `C` or prove an obstruction
   for the full cubic vertex bank;
3. pursue super-IG separately as algebraic global descent;
4. treat local dark-energy derivative additions as closed for the constant
   mode; and
5. build or select the global functional before deriving FLRW predictions.

It does not change the 82-row denominator, verdict counts, global parameter
residue, canon, Lane count or public posture. It ranks one additional scoped
finite zero-mode quotient. P1/P2/P3 are unchanged and unused.

## 8. Next gate

```text
IN_PARALLEL:
  (A) CONSTRUCT_FIRST_PERTURBATIVE_INTERACTING_C_OPERATOR_OR_FULL_CUBIC_BANK_OBSTRUCTION
      ON_THE_EXISTING_EVEN_BV_PHYSICAL_CARRIER;
  (B) GLOBALIZE_THE_MIXED_SUPER_IG_BRACKET_TO_THE_ACTUAL_H_BUNDLE_WITH_REAL_FORM
      EQUIVARIANCE_JACOBI_AND_OBSERVATION_DESCENT;
  (C) DERIVE_OR_EXPLICITLY_SUPPLY_A_COVARIANT_NORMALIZED_OBSERVER_FUNCTIONAL
      AND_INSERT_ITS_PROJECTOR_INTO_ONE_ACTION_BEFORE_ANY_FLRW_WZ_CLAIM.
```

## 9. Reproduction

```sh
PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python \
  tests/channel-swings/first_interaction_krein_global_zero_mode_probe.py
DOT_SAGE=/private/tmp/gu-interaction-zero-mode-sage \
  /Applications/SageMath-10-9.app/Contents/Frameworks/Sage.framework/Versions/Current/venv/bin/sage \
  tests/channel-swings/first_interaction_krein_global_zero_mode_independent.sage
```

Primary certificate: `2 source + 3 repo + 27 exact + 7 type + 10 planted =
49/49 PASS`. Independent Sage/QQ reconstruction: `PASS`.
