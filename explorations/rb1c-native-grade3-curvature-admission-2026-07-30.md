---
title: "RB1c native grade-three curvature admission and trace-line cyclic gate"
status: active_research
doc_type: construction_result
created: 2026-07-30
lane: "1"
work_item: RB1C-NATIVE-GRADE3-CURVATURE-ADMISSION
run: lab/process/runs/GUH-20260730T232344Z-rb3b-trace-vertex-grade3/run-plan.md
probe: tests/channel-swings/rb1c_native_grade3_curvature_probe.py
grade: "NATIVE FULL-ADJOINT GRADE-THREE MAP EXECUTED / GENERIC NON-RIEMANNIAN RESPONSE NONZERO / POINTWISE LEVI-CIVITA SOURCE ROLE KILLED ON ALL ALGEBRAIC-RIEMANN IRREPS / DEWITT TRACE-LINE ADAPTER REOPENS A CARRIER BUT FAILS THE RB2 CYCLIC IDENTITY / CANONICAL POLARIZATION SURVIVES ONLY AS A DIFFERENT TWO-INPUT EULER-COVECTOR GEOMETRY. Trace reversal changes the ambient Hodge class and supplies the negative trace gamma. The unadapted source has norm 25.2982 on the generic control; independent scalar, traceless-Ricci, and Weyl regressions prove the projected source vanishes on the complete 3185-dimensional algebraic-Riemann representation, while powered raw controls remain nonzero (scalar norm 82.2679). The trace adapter is native and nonzero on the scalar plant at 78.2304, yet six deterministic seeded full-adjoint cyclic gaps are order one and a four-ordering repair family has full sampled rank. Exact polarization is symmetric and derivative-correct, and one finite moving-data covariance proxy passes, but a planted zero-polarized-curvature pair produces a nonzero Euler covector, ruling out representation by one linear S(Lambda2) map in that fixture. No RB1/RB2 reentry."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# RB1c native grade-three curvature admission

## Result first

The adjacent full-\(Sp(32,32;\mathbb H)\) grade-three source proposed by
RB1b is now executed in the actual trace-reversed \((9,5)\) geometry.

It is a real, nonvacuous map on generic non-Riemannian full-adjoint
curvature:

\[
\left\|\mathscr S_3(F_{\rm generic})\right\|=25.2982.
\]

Its output has degree \(13\), is Krein-skew, and is
right-\(\mathbb H\)-linear. But the grade-three projection removes the
entire pointwise Levi--Civita algebraic-Riemann representation. Independent
scalar, traceless-Ricci, and Weyl plants exhaust its
\(1+104+3080=3185\) dimensions. On all three, the projected first piece,
second piece, and full source vanish. Powered raw controls show that this is
not vacuous input; for the scalar plant,

\[
\left\|\mathscr S_{\rm raw}(F_{\rm scalar})\right\|=82.2679,
\]

while

\[
\mathscr S_3(F_{\rm scalar})
=
\mathscr S_3(F_{\rm Ric_0})
=
\mathscr S_3(F_{\rm Weyl})
=0.
\]

So this route does not supply the desired Ricci/Einstein source on the
Levi--Civita stratum. The generic non-Riemannian map remains mathematically
live; those are different claims.

The DeWitt trace line creates a genuine adjacent construction:

\[
\mathscr S_{\rm tr}(F)
=
\pi_{\mathfrak{sp}}\!
\left(c(t_{\rm tr})\mathscr S_{\rm raw}(F)\right).
\]

It reopens the scalar-curvature carrier with norm \(78.2304\) and passes
native reality. However, it fails the cyclic/transgression identity needed
to insert it into the existing RB1/RB2 source action. A bounded
left/right-ordering family does not repair the failure.

Canonical symmetric polarization of the cubic functional does satisfy the
derivative identity, and one finite moving-data native-covariance proxy
passes. That is useful, but it is a different two-input Euler-covector
geometry. A planted algebraic factorization counterexample proves that it
cannot be represented by one linear curvature-to-source map of the form
RB1/RB2 currently assumes in that fixture.

The disposition is therefore:

```text
generic full-adjoint grade-three map: LIVE
torsion-free Ricci/Einstein source role: KILLED AT BIANCHI BOUNDARY
trace-line carrier reopener: CONSTRUCTED
trace-line RB2 cyclic gate: FAILED
canonical polarization: LIVE AS A DIFFERENT EULER GEOMETRY
RB1/RB2 reentry as written: NO
```

## Plain English

The grade-three idea was not empty. It detects extra curvature that a
generic large gauge connection can carry beyond ordinary Levi--Civita
geometry. But when the curvature obeys the familiar Riemann symmetries and
Bianchi identity, the part this map can see disappears pointwise across
the scalar, traceless-Ricci, and Weyl sectors.
That makes it a possible detector or source for non-Riemannian distortion,
not the missing ordinary Einstein source.

Multiplying by the trace direction changes the answer. This is only
available because trace reversal makes that direction negative and native
to the \((9,5)\) Clifford algebra. The adapted map sees ordinary constant
curvature. Unfortunately, seeing it is not enough: varying the proposed
cubic action does not produce the current that the source-action formula
assumes. The mismatch survives diverse full-adjoint tests and a held-out
fixture.

There is one constructive escape. If the cubic form is fully symmetrized,
its derivative works automatically. But the resulting Euler covector depends on
two inputs separately, not only on their combined curvature. Adopting it
would change the source-action geometry rather than complete the existing
one.

## 1. Layer 0: three maps, not one

RB1c keeps these objects separate:

| map | meaning | status |
| --- | --- | --- |
| \(\mathscr S_3\) | native projection of RB1b's grade-flipping linear curvature map | generic response live; Riemann source role fails |
| \(\mathscr S_{\rm tr}\) | trace-gamma adapter followed by native projection | carrier live; cyclic gate fails |
| \(T_{\rm pol}\) | full symmetric polarization of the cubic functional | exact derivative; different two-input Euler-covector geometry |

The first two are linear in curvature. The third is a symmetric trilinear
functional and its associated two-input Euler covector. A derivative identity
for the third cannot be credited to either linear map without a factorization
proof.

## 2. Trace reversal is load-bearing

For the actual symmetric metric fibre,

\[
(7,3)_{\rm raw}
\longrightarrow
(6,4)_{\rm DeWitt},
\qquad
(10,4)_{\rm total}
\longrightarrow
(9,5)_{\rm total}.
\]

The primal trace tensor is

\[
h_{\rm tr}=-g/4.
\]

In the repository's orthonormal DeWitt frame, it has the single coordinate
\(-1/2\) on the negative trace line. The corresponding unit Clifford
generator obeys

\[
c(t_{\rm tr})^2=-1.
\]

This changes the Hodge square on degrees \(2\) and \(12\):

\[
*^2_{\rm raw}=+1,
\qquad
*^2_{\rm DeWitt}=-1.
\]

The probe executes both Hodge algebras and requires the hostile raw
comparator to produce the opposite sign.

## 3. The two linear source candidates

With the moving Clifford one- and two-forms \(\Phi_1,\Phi_2\), define

\[
\mathscr S_{\rm raw}(F)
=
\Phi_1\wedge *F
-\frac12*
\left[
\Phi_1\wedge*
\left(\Phi_2\wedge*F\right)
\right].
\]

The RB1b candidate is

\[
\mathscr S_3(F)
=
\pi_{\mathfrak{sp}}\mathscr S_{\rm raw}(F).
\]

The pointwise Clifford reductions are

\[
\gamma^aF_{ab}
=
\frac12\operatorname{Ric}_{bd}\gamma^d
\]

and

\[
\gamma^{ab}F_{ab}
\quad\hbox{is purely scalar}.
\]

The possible grade-three remainder in the first identity is killed by the
first Bianchi identity. In the second identity, Bianchi kills grade four
and Ricci symmetry kills grade two. The source's Hodge-normalized
two-gamma contraction is likewise scalar, so the native grade-three
projection kills it. The executable scalar, traceless-Ricci, and Weyl
fixtures independently verify these identities and exhaust the complete
algebraic-Riemann representation. Nonzero raw scalar and traceless-Ricci
controls prove the zero is caused by the projection rather than vacuous
input.

The adjacent trace-relative map is

\[
\boxed{
\mathscr S_{\rm tr}(F)
=
\pi_{\mathfrak{sp}}
\left[c(t_{\rm tr})\mathscr S_{\rm raw}(F)\right].
}
\]

It changes the carrier and the visible stabilizer. It is not Weinstein's
written source map and cannot inherit its cyclic identity by name. On the
scalar-curvature fixture it is nonzero, Krein-skew, and
right-\(\mathbb H\)-linear.

## 4. The cyclic gate fails

For either linear source \(S\), consider

\[
I_S(\theta)
=
\left\langle
\theta,S(\theta\wedge\theta)
\right\rangle .
\]

Its exact derivative is

\[
\delta I_S
=
\left\langle\delta\theta,S(\theta^2)\right\rangle
+
\left\langle
\theta,
S(\delta\theta\wedge\theta+\theta\wedge\delta\theta)
\right\rangle .
\]

The RB2 cyclic shortcut would replace this with

\[
3\left\langle\delta\theta,S(\theta^2)\right\rangle.
\]

Central finite differences reproduce the exact derivative with maximum
relative residual \(1.745\times10^{-9}\). On six deterministic seeded
full-adjoint fixtures, the relative gaps from the cyclic shortcut are:

| source | six gaps |
| --- | --- |
| \(\mathscr S_3\) | \(0.642,0.876,0.991,0.543,1.057,0.633\) |
| \(\mathscr S_{\rm tr}\) | \(1.121,0.655,0.716,0.383,0.837,0.739\) |

A four-column repair family—left/right trace multiplication applied to the
first/second source pieces—has sampled rank four, with singular values

\[
(30.133,24.758,4.345,1.899).
\]

Thus it contains no sampled nonzero universal cyclic combination. The
least-singular training combination also fails the held-out
fixture with residual \(4.98728\).

### Correction to the first-pass restricted fixture

The initial grade-\(2/3\)-restricted test suite had tiny gaps,
\(10^{-7}\) to \(4\times10^{-5}\), and its ordering matrix had rank three
with normalized null vector

\[
(1,1,1,1).
\]

That did **not** support the earlier label “restricted grade-\(2/3\)
cyclic failure.” The saved probe records the correction rather than hiding
it. A held-out restricted fixture rejects that apparent null with residual
\(-0.12249\), showing it was a special training relation, not a universal
repair. The order-one full-adjoint fixtures are the powered failure result.

## 5. The constructive adjacent geometry: full polarization

Define

\[
B(x,y,z)
=
\left\langle x,\mathscr S_{\rm tr}(y\wedge z)\right\rangle
\]

and its canonical symmetric polarization

\[
T_{\rm pol}(x,y,z)
=
\frac1{6}\sum_{\sigma\in S_3}
B(x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)}).
\]

Then

\[
\delta I_{\rm pol}(\theta)
=3T_{\rm pol}(\delta\theta,\theta,\theta)
\]

by construction. The finite fixture verifies:

- nonzero response;
- permutation symmetry;
- derivative residual \(1.745\times10^{-9}\); and
- homogeneous covariance under a native right-\(\mathbb H\),
  \(K\)-unitary rotor.

But this Euler covector does not factor through one polarized curvature. A planted
pair \(y,z\) has

\[
\frac12(y\wedge z+z\wedge y)=0,
\]

while \(T_{\rm pol}(x,y,z)\) is nonzero for multiple planted \(x\).
Therefore no single linear

\[
\mathscr S:\Lambda^2\longrightarrow\Omega^{13}(\mathfrak g^*)
\]

can represent this polarized Euler covector in the tested fixture.

This is the useful fork: either retain the existing one-curvature source
architecture and reject this candidate, or explicitly reopen RB1 with a
two-input/polarized Euler geometry and rederive its covariance, Green,
BV, and datum ledger. The latter is a new swing, not an automatic repair.

## 6. Seven-axis and next-step disposition

| candidate | L0 | L1 substrate | L2 observer | L3 pairing | L4 causal order | L5 emergence | L6 loop | L7 positivity | first falsification |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \(\mathscr S_3\) | generic full-adjoint versus complete pointwise algebraic-Riemann curvature separated | smooth native \(Sp(32,32;\mathbb H)\) adjoint | no new observer | native invariant/Krein projection | \((9,5)\) Hodge | no RG claim | none | indefinite | scalar/Ricci\(_0\)/Weyl Clifford reduction |
| \(\mathscr S_{\rm tr}\) | trace adapter named as a new map | trace-stabilized native stratum | trace line supplied by geometry | same | trace-reversed Hodge | none | none | indefinite | six-fixture cyclic gate |
| \(T_{\rm pol}\) | two-input Euler-covector geometry, not a linear source map | same finite native carrier | same | symmetrized trilinear pairing | same | none | one finite moving-data covariance proxy | indefinite | factorization/complete-action test |

The efficient next move is not to tune more left/right coefficients in the
failed four-ordering family. Keep \(\mathscr S_3\) as a possible
non-Riemannian distortion diagnostic. Advance the already-passing typed
curvature vertex/current from RB3c. Reopen the polarized geometry only if
the full Euler system generates an independent need for a two-input source
map.

No global action, Ward identity, VEV, mass, stationary solution, nonlinear
CME, domain, anomaly, index, generation count, or cosmological prediction
is claimed.

## Reproduction

Run:

```bash
python3 -B tests/channel-swings/rb1c_native_grade3_curvature_probe.py
```
