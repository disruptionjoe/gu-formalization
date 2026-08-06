---
artifact_type: construction_result
created: 2026-08-05
status: ZERO_FIELD_SCALAR_HESSIAN_ENLARGEMENT_MISTYPED__EVERY_SCALAR_PARITY_HAS_A_CONTINUUM_ODD_CHANNEL__Q1_POLE_CONDITIONAL_ON_UNBUILT_ONSHELL_NUMERATOR
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-SILENT
ledger_rows: [LT-GR2b, LT-GR3, LT-GR5, LT-SM8]
scripts:
  - tests/channel-swings/selected_cubic_qft_threshold_numerator_probe.py
  - tests/channel-swings/selected_cubic_qft_threshold_numerator_independent.sage
registry: lab/process/selected-cubic-qft-threshold-and-numerator-gate.json
---

# Selected-cubic continuum threshold and on-shell numerator gate

## Result first

The recorded next gate was partly mistyped. Adding the scalar fluctuation to
the previous zero-field Hessian does not produce a larger interacting metric.
For

\[
 V_3=c\theta(q_0+q_m)^2,
\]

the complete Hessian in `(q0,qm,theta)` vanishes at the zero-field point. At
`q0=qm=0` and fixed `theta_bar`, only the already-built two-by-two TT block
`2c theta_bar vv^T` survives. Scalar mixing in the Hessian begins only on a
nonzero TT background. Repeating the spectral matrix calculation with an
extra zero row would have looked like progress while asking the same question.

The first genuinely new state-space test is the continuum odd-channel
homological equation. Carrying all three monomials produces an unexpectedly
tight kinematic result:

- if `theta` is Krein-even, the mixed vertex `theta q0 qm` is odd. Because
  `q0` is massless, whichever of the two positive-mass species `theta` and
  `qm` is heavier can transition to the lighter plus `q0`. For unequal masses
  a real energy denominator therefore vanishes; equal masses are the soft
  zero-momentum boundary.
- if `theta` is Krein-odd, `theta q0^2` and `theta qm^2` are odd. A positive-
  mass `theta` is automatically above the two-massless threshold through
  `theta q0^2`.

Thus neither scalar sign supplies a generic subthreshold escape. This is a
stronger and correctly typed continuation of the classical parity failure.
It is **not yet a QFT `C`-operator no-go**, because W179's generator is

\[
 Q_1\sim {-2N(k)\over D(k)},
\]

and the August action has not yet supplied the momentum-dependent numerator
`N(k)` on the resonance shell. The fixed-background coefficient `c != 0` at a
chosen TT symbol does not prove `N|_{D=0} != 0`. Gauge/BV reduction, a soft
identity, or equation-of-motion redundancy can make `N` divisible by `D`, in
which case the apparent pole cancels exactly.

The result therefore moves the frontier to one precise object: derive the
complete selected momentum-space cubic on the even-BV quotient and restrict
its odd numerator to the two exact shells below. A nonzero restriction gives
a first-order continuum obstruction. A vanishing restriction gives a
constructive cancellation and permits the next `Q1`/domain step.

P1/P2/P3 remain unused. Curt remains formally separate inside the Eric lane,
and the conjunctive third-lane gate remains unpromoted.

## Plain English

The last result made the two gravity modes positive while the extra scalar was
held fixed. Letting that scalar wiggle does not alter the small-oscillation
matrix at the vacuum; a cubic interaction has no second derivative there.

The real next issue is particle production. Whichever sign we try for the
scalar, the interaction contains a negative-grade process involving the
ordinary massless graviton. The energy bookkeeping allows that process to go
on shell. But an allowed process can still have zero amplitude. We have now
located the exact calculation that decides it: compute the actual momentum-
dependent vertex and see whether it vanishes on the allowed shell.

## 1. Layer 0

| phrase | object here | not identified with |
| --- | --- | --- |
| scalar fluctuation | the third classical field in the complete Hessian | a scalar one-particle state before the trace mode and domain are diagonalized |
| background `C` | fundamental symmetry of the fixed-`theta_bar` TT Hessian | a Fock-space metric including scalar quanta |
| odd vertex | cubic monomial with total negative Krein parity | a proved nonzero physical decay amplitude |
| threshold | real zero of a free energy denominator | a physical-sheet pole or failed total unitarity |
| numerator | selected momentum-space vertex after observation and BV reduction | the constant off-shell coefficient `c` at one TT symbol |
| scalar mass | pole of the trace equation on the stable-sign branch | the distinct massive spin-two partner |
| Q1 exists | first homological equation has a regular solution | all-orders `C`, common domain, loops or renormalization |

This is also an arena fork. Weinstein describes quantum GU as native to
`Y^14` and classical physics as observed on `X^4`. The present calculation is
an observed-sector continuum gate. Identifying it with the complete native
quantum operator still requires observation descent and a common domain.

## 2. Divergent specialist preassessment

| lens | demand | effect |
| --- | --- | --- |
| variational geometry | differentiate the full cubic before enlarging the Hessian | exposed the zero-field block decoupling |
| Krein QFT | sort monomials by total grade before solving for `Q1` | produced different odd banks for the two scalar signs |
| scattering kinematics | include every orientation of a Hermitian vertex | found the heavier-to-lighter-plus-massless channel |
| scalar-tensor theory | derive, do not name, the scalar pole | gave `mu^2=a kappa/(3 beta^2)` on the stable branch |
| higher-derivative gravity | keep spin zero and spin two distinct | forbids importing the two-identical-graviton W179 label |
| BV/BRST | evaluate the physical numerator after quotient | prevents denominator-only overclaim |
| microlocal analysis | separate characteristic shells from operator domains | leaves Green/Fock closure open |
| symplectic geometry | descend the vertex through the covariant presymplectic constraint quotient | makes physical Hamiltonian support, not an unreduced density, the numerator target |
| source criticism | ask whether Weinstein supplies this prescription | `SOURCE-SILENT`; observed/native arena warning retained |
| exact-computation engineering | independent symbolic routes and omissions | SymPy and Sage reconstruct the atlas |
| hostile synthesis | attack both overclaim and superseded-object defense | numerator and three-species fences are load-bearing |

Two preregistered implementation controls fired. The primary probe initially
used structural rather than simplified polynomial matrix equality, and the
independent Sage route declared its rational function field incorrectly. Both
were repaired before reading a verdict; neither changed the mathematics.

## 3. Why the scalar-enlarged Hessian is not the next interaction

Exact differentiation gives

\[
 D^2V_3=
 \begin{pmatrix}
 2c\theta&2c\theta&2c(q_0+q_m)\\
 2c\theta&2c\theta&2c(q_0+q_m)\\
 2c(q_0+q_m)&2c(q_0+q_m)&0
 \end{pmatrix}. \tag{1}
\]

At `(q0,qm,theta)=(0,0,0)`, (1) is zero. At `q0=qm=0` with fixed
`theta_bar`, it is

\[
 \begin{pmatrix}
 2c\bar\theta&2c\bar\theta&0\\
 2c\bar\theta&2c\bar\theta&0\\
 0&0&0
 \end{pmatrix}, \tag{2}
\]

whose only nonzero block is exactly the predecessor's `u vv^T`, with
`u=2c theta_bar`. The mixed scalar entries are proportional to `q0+qm` and
appear only on a nonzero TT background. Consequently the fixed-background
`C(u)` remains valid in its stated scope, but appending a scalar zero row does
not test the interaction.

## 4. Complete parity support

Take `p(q0)=+1`, `p(qm)=-1` and `p(theta)=s`. Then

| monomial | parity |
| --- | ---: |
| `theta q0^2` | `s` |
| `theta q0 qm` | `-s` |
| `theta qm^2` | `s` |

For `s=+1`, only the mixed monomial is odd. For `s=-1`, both diagonal
monomials are odd. Omitting the mixed term falsely clears even `theta`;
omitting the diagonal terms falsely clears odd `theta`. Both false reductions
are planted failures in the certificate.

## 5. The selected masses

The TT construction gives

\[
 M^2={124\over117}\alpha_{II}\kappa_1. \tag{3}
\]

The scalar trace equation at zero vacuum source is

\[
 aR+{3\beta^2\over\kappa}\Box R=0.
\]

On the convention where `Box R=-mu^2 R`, its stable positive-mass branch has

\[
 \mu^2={a\kappa\over3\beta^2}, \qquad
 {M^2\over\mu^2}={124\alpha_{II}\kappa_1\beta^2\over39a\kappa}. \tag{4}
\]

Equation (4) does not select an ordering: the two masses use distinct open
coefficient combinations. A tachyonic or zero coefficient horn is outside the
positive-mass threshold theorem and has its own earlier instability burden.

## 6. Exact continuum threshold atlas

For a parent of mass `A`, a daughter of mass `B<A`, and a massless daughter,
the parent rest-frame momentum is

\[
 |k|={A^2-B^2\over2A}>0. \tag{5}
\]

It obeys `A=sqrt(k^2+B^2)+|k|` exactly. Hence:

| scalar grade | odd selected channel | real denominator zero |
| --- | --- | --- |
| even | `theta q0 qm` | for `M>mu`, `qm -> theta+q0`; for `mu>M`, `theta -> qm+q0` |
| even, `M=mu` | same | only at the soft point `|k|=0`; IR/numerator analysis required |
| odd, `mu>0` | `theta q0^2` | `theta -> q0+q0` at `|k|=mu/2` |
| odd, `mu=0` | same | collinear/soft massless locus; numerator and IR domain required |
| odd | `theta qm^2` | additional shell when `mu>=2M`; not needed for the generic result |

The key correction to a naive use of W179 is that the even-`theta` channel has
three unequal species. One must include both orientations of the same vertex.
There is no region called “subthreshold” merely because the massive TT partner
is lighter than the scalar; then the scalar is the decaying parent.

## 7. The numerator is now the decisive construction

W179's first equation is schematically

\[
 [H_0,Q_1]=-2A,\qquad Q_1(k)={-2N(k)\over D(k)}. \tag{6}
\]

The threshold atlas proves that `D=0` has real solutions. It does not prove a
pole. The exact negative control is elementary but decisive:

\[
 D=z,\quad N=g \Longrightarrow Q_1=-2g/z,
\]

while

\[
 D=z,\quad N=gz \Longrightarrow Q_1=-2g. \tag{7}
\]

Thus the next construction must derive the complete momentum-dependent
numerators

```text
N_even(theta,q0,qm) restricted to the mixed massive/massless shell
N_odd(theta,q0,q0) restricted to the two-massless shell
```

from the selected `Y^14` action, observation map and even-BV quotient. The
constant-background statement `c != 0` is insufficient because it was read at
a fixed TT symbol before on-shell quotienting. A field redefinition or Ward
identity may make the physical numerator proportional to `D`.

The symplectic form adds a second non-negotiable check. The cubic Hamiltonian
must define a nonzero vector field on the reduced covariant phase space. If its
differential lies in the characteristic kernel of the presymplectic form, or
is an exact boundary generator after quotienting, the unreduced vertex does
not create a physical odd transition even when its free energy denominator
vanishes. This is the symplectic version of the numerator gate, not a separate
escape hatch.

## 8. Seven-axis audit

| layer | disposition |
| --- | --- |
| Layer 0 | background Hessian, Fock `C`, continuum `Q1`, numerator and physical sheet separated |
| L1 source | `SOURCE-SILENT`; `Y^14` quantum versus observed `X^4` distinction retained |
| L2 algebra | complete Hessian, parity table, mass ratio and rest-frame thresholds exact |
| L3 geometry | selected reduced cubic owned; native momentum vertex and observation descent open |
| L4 variation | scalar trace pole derived; complete cubic Euler/Legendre vertex not yet assembled |
| L5 covariance/BV | ordinary TT quotient inherited; on-shell Ward/BV/presymplectic numerator open |
| L6 analytic | real denominator shells exact; IR, Green/Fock domain and physical sheet open |
| L7 physics | generic kinematic opportunity for odd production; actual amplitude and unitarity undecided |

## 9. Constraint and ledger effect

No new coefficient or datum was added. The mass comparison introduces no new
freedom; it exposes an existing dimensionless combination. The numerator is a
missing construction, not a free parameter to fit.

The ledger denominator, verdict counts, global residue and four ranked scoped
quotients remain unchanged. Four row distances move:

| row | retained verdict/kind | new distance |
| --- | --- | --- |
| `LT-GR2b` | `SAME/DERIVED_PARTIAL` | derive the selected on-shell cubic numerator and its native/observed descent |
| `LT-GR3` | `DIFFERS/STRUCTURAL_DIFFERENCE` | evaluate the odd numerator on the exact massless resonance shells, then run physical-sheet H59 |
| `LT-GR5` | `DIFFERS/STRUCTURAL_DIFFERENCE` | complete augmented-torsion cubic bank and common BV/Green/Fock domain |
| `LT-SM8` | `NEEDS/PROVEN_UNSUPPLYABLE` | a full interacting even-BV/Fock metric remains open; no scalar sign clears Q1 kinematics |

## 10. Next gate

Construct the full selected cubic momentum vertex before another positivity
matrix:

1. expand the complete action, including moving normalized trace, Shiab,
   augmented torsion and scalar-distortion terms, to cubic order;
2. diagonalize the scalar, massless TT and massive TT external legs on the
   same Krein/BV domain;
3. derive `N_even` and `N_odd` with all derivative and compensator terms;
4. restrict them exactly to the shells in the table;
5. if nonzero, solve the physical-sheet/self-energy horn; if zero, construct
   the regular `Q1` quotient and continue to `Q2`;
6. independently continue super-IG global descent and the covariant normalized
   observer-functional action horn.

## Non-claims

No interacting `C`, Q1 pole, physical-sheet instability, decay width, loop
unitarity, common Fock domain, native `Y^14` quantum identification,
cosmological prediction, external-datum consumption, canon movement, Lane
promotion or public-posture movement is claimed.
