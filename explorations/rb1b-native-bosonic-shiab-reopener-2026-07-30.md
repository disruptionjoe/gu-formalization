---
title: "RB1b native bosonic-Shiab reopener: parity kill and full-adjoint grade-flip"
status: active_research
doc_type: construction_result
created: 2026-07-30
lane: "1"
work_item: RB1B-NATIVE-BOSONIC-SHIAB-REOPENER
run: lab/process/runs/GUH-20260730T215838Z-rb3-moving-shiab-dual-track/run-plan.md
probe: tests/channel-swings/rb1b_native_bosonic_shiab_probe.py
grade: "PREREGISTERED FULL-SPIN SAME-LAMBDA2 RICCI ROUTE KILLED BY EXACT CENTRAL PARITY. An algebraic Spin(9,5)-equivariant map from curvature in Lambda2 tensor Lambda2 to a one-form spin adjoint in V tensor Lambda2 is zero; a general Ricci contraction lands in V* tensor V*, becoming Sym2 only with algebraic-Riemann/Levi--Civita hypotheses. The result also applies to stabilizers containing the same parity element, but not to every smaller stabilizer. A local framed epsilon-soldered full-adjoint grade-flipping formula is emitted as a conditional adjacent candidate. A finite Sp(1,1) quaternionic/Krein source-shaped architecture fixture passes degree, right-H, reality, moving-epsilon covariance, and fixed-curvature epsilon-response checks; it does not implement the native Clifford grade flip. A planted U(2,2) comparator passes covariance but fails right-H. One nondegenerate fixture gives a cyclic/transgression counterexample with relative gap 0.444, so the candidate does not clear RB1 and does not enter RB2."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# RB1b native bosonic-Shiab reopener

## Result first

```text
FULL-SPIN-SAME-LAMBDA2-RICCI: KILLED BY EXACT PARITY
EPSILON-SOLDERED-FULL-ADJOINT-GRADE-FLIP: CONDITIONAL CANDIDATE EMITTED
SOURCE-SHAPED DEGREE / RIGHT-H / REALITY / COVARIANCE: COHERENT IN FINITE FIXTURE
NATIVE CLIFFORD GRADE FLIP: UNTESTED
CYCLIC / TRANSGRESSION IDENTITY: NOT IMPLIED; ONE COUNTEREXAMPLE
RB1 REENTRY: NO
RB2 SOURCE RECORD: UNCHANGED AND BLOCKED
```

The registered side quest produced a decisive answer at its stated full-spin
symmetry grade. The proposed Ricci--Einstein route cannot fill the required
same-\(\Lambda^2\) spin-connection covector slot, even if the curvature
projection and invariant pairing are perfect. The failure is
representation-theoretic, not a missing coefficient. It does not rule out an
arbitrarily smaller stabilizer that supplies an odd invariant tensor; that
would be a different, charged construction.

Writing the failed construction also exposed a better neighboring geometry.
Clifford multiplication by the moving soldering form can send
spin-curvature into an odd Clifford grade of the **full**
\(\mathfrak{sp}(32,32;\mathbb H)\) adjoint. That candidate has the right
form degree and native covariance architecture. It has not yet earned
action status because the native grade-three carrier and the cyclic/Bianchi
identities required by RB2 remain unproved.

## Plain English

The failed idea tried to turn a curvature two-form into a connection
one-form using only full-\(\operatorname{Spin}(9,5)\)-invariant Ricci
contraction, the metric, the volume form, and the diagonal soldering frame.
That cannot work in the same spin-connection sector. The input carries an
even number of vector indices; the required output carries an odd number.
The full-spin invariant tensors used by this route have even parity, so there
is nowhere for the missing odd index to come from.

There are two honest escapes:

1. let the output move into an odd Clifford grade of the full GU gauge
   algebra; or
2. supply an actually odd object or differential operator.

The first escape is more native to the present construction and is now
written explicitly. The second would add an observer vector/normal or raise
the action's differential order, so it cannot be smuggled in as the
existing orientation bit.

## 1. Layer-0 parity obstruction

On the honest spin-connection sector,

\[
\mathfrak{spin}(9,5)_\mathbb C\simeq\Lambda^2V^*.
\]

After identifying the density-dual \(\Omega^{13}\) output with its
pre-density primal \(\Omega^1\) carrier, an algebraic map would require

\[
\operatorname{Hom}_{\operatorname{Spin}(9,5)_\mathbb C}
\left(
\Lambda^2V^*\otimes\Lambda^2V^*,
V^*\otimes\Lambda^2V^*
\right).
\]

This Hom space is zero. A lift of
\(-I\in SO(14,\mathbb C)\) acts as

\[
+1
\quad\text{on}\quad
\Lambda^2V^*\otimes\Lambda^2V^*,
\]

and as

\[
-1
\quad\text{on}\quad
V^*\otimes\Lambda^2V^*.
\]

For an intertwiner \(T\),

\[
T=(-1)\,T\,(+1)^{-1}=-T,
\]

so \(T=0\).

An unrestricted Ricci-type contraction instead lands in

\[
V^*\otimes V^*,
\]

which has dimension \(196\). It lands in \(S^2V^*\), of dimension \(105\),
only after algebraic-Riemann or Levi--Civita symmetries are imposed. The
desired pre-density connection covector instead has carrier

\[
V^*\otimes\Lambda^2V^*
\]

of dimension \(14\cdot91=1274\). This is not a numerical near miss.

An invariant adjoint pairing only identifies an already correct adjoint
with its dual. It cannot change the zero Hom space. The diagonal coframe
lies in \(V^*\otimes V\), which is parity-even under the diagonal spin
action, so it also cannot supply the missing odd factor while retaining a
\(\Lambda^2\) internal target.

This kills the preregistered full-\(\operatorname{Spin}(9,5)\),
same-\(\Lambda^2\) Ricci--Einstein construction. The same proof applies to
any stabilizer containing the lift of \(-I\). A smaller stabilizer without
that parity element could admit an odd invariant, but the stabilizer or
invariant would then be a charged part of the construction. The result does
not kill the two RB2 bridge actions.

## 2. Why the full adjoint changes the question

The native quaternionic algebra decomposes by Clifford grade as

\[
\mathfrak{sp}(32,32;\mathbb H)
\simeq
\Lambda^2\oplus\Lambda^3\oplus\Lambda^6\oplus\Lambda^7
\oplus\Lambda^{10}\oplus\Lambda^{11}\oplus\Lambda^{14}.
\]

The grade list is not inferred from the dimension sum. In the native
Clifford fixture every generating gamma is Krein-self-adjoint, so Krein
adjunction acts on grade \(k\) by the reversion sign
\((-1)^{k(k-1)/2}\). The skew grades are exactly
\(2,3,6,7,10,11,14\). Their dimensions are

\[
91+364+3003+3432+1001+364+1=8256.
\]

Multiplication by a Clifford one-form sends grade two to grades one and
three:

\[
\Lambda^1\cdot\Lambda^2
\subset
\Lambda^1\oplus\Lambda^3.
\]

Projection to the native adjoint discards grade one and can retain grade
three. The relevant carrier now has the parity

\[
\Lambda^2V^*\otimes\Lambda^2V^*
\longrightarrow
V^*\otimes\Lambda^3V^*,
\]

and both sides have central character \(+1\). The exact same-sector
obstruction is gone because the target has changed.

This is a Layer-0 fork: a grade-three full-\(Sp\) connection covector is not
a Ricci tensor and not a grade-two spin connection.

## 3. Source-shaped grade-flipping candidate

Let

\[
S=\mathbb H^{64},\qquad
\mathfrak g=\mathfrak{sp}(32,32;\mathbb H)
\subset\operatorname{End}_{\mathbb H}(S).
\]

With Krein adjoint \(\ddagger\), define on right-\(\mathbb H\)-linear
endomorphisms

\[
\pi_{\mathfrak g}(X)=\frac12(X-X^\ddagger),
\qquad
\kappa_{\mathfrak g}(X,Y)
=\operatorname{ReTr}_{\mathbb H}(XY).
\]

The displayed projection is only a Krein-skew projection in the ambient
complex matrix model. It is a projection to the native
\(\mathfrak{sp}(32,32;\mathbb H)\) real form when its input is already
right-\(\mathbb H\)-linear.

For a reference Clifford embedding, the source-inspired soldering tensors
are schematically

\[
\Phi_1^0=\sum_a e^a\otimes c_0(e_a),
\]

\[
\Phi_2^0
=\frac12\sum_{a,b}e^a\wedge e^b
\otimes c_0(e_a)c_0(e_b),
\]

with normalization still conditional. Move them by

\[
\Phi_i(\epsilon)
=\operatorname{Ad}_{\epsilon^{-1}}\Phi_i^0.
\]

This is a local framed formula. Relative to the RB3 convention
\(c_g=\operatorname{Ad}_g c_0\), its source-field convention is
\(\epsilon_{\rm source}=g_{\rm RB3}^{-1}\). Under a lift change
\(g\mapsto gh\), the vector frame must co-transform; descent to the
associated bundle is not yet constructed.

The candidate is

\[
\begin{aligned}
\mathscr S_\epsilon^{\rm raw}(F)
=\pi_{\mathfrak g}\Big(
&\Phi_1(\epsilon)\wedge *_G F\\
&-\frac12 *_G\big[
\Phi_1(\epsilon)\wedge *_G(
\Phi_2(\epsilon)\wedge *_G F)
\big]
\Big).
\end{aligned}
\]

The density-dual map is

\[
\widehat{\mathscr S}^{\rm bos}_\epsilon
=
\kappa_{\mathfrak g}^{\flat}
\circ\mathscr S_\epsilon^{\rm raw}:
\Omega^2(\mathfrak g)
\longrightarrow
\Omega^{13}(\mathfrak g^*).
\]

The Hodge stars inside the trace-subtraction expression are structural.
There is no additional final Hodge after
\(\kappa_{\mathfrak g}^{\flat}\). Such an extra star returns the output to
degree one and repeats RB2's double-Hodge error.

For signature \((9,5)\),

\[
*_G^2|_{\Omega^k}
=(-1)^{k(14-k)+5}.
\]

It is \(-1\) on degrees \(2,12\) and \(+1\) on degrees \(1,13\).

## 4. Moving covariance and epsilon response

With

\[
F\mapsto\operatorname{Ad}_uF,\qquad
\epsilon\mapsto\epsilon u^{-1},
\]

the soldering tensors satisfy

\[
\Phi_i(\epsilon u^{-1})
=\operatorname{Ad}_u\Phi_i(\epsilon),
\]

and therefore

\[
\mathscr S_{\epsilon u^{-1}}(\operatorname{Ad}_uF)
=\operatorname{Ad}_u\mathscr S_\epsilon(F).
\]

Every coefficient lies in
\(\operatorname{End}_{\mathbb H}(S)\), so the construction is
right-\(\mathbb H\)-linear. The real reduced trace supplies a real
indefinite action pairing.

For \(\chi=\epsilon^{-1}\delta\epsilon\),

\[
\delta\Phi_i=[\Phi_i,\chi].
\]

Holding \(F,G,K,\kappa\), the real-form projection, and the local frame fixed,

\[
\begin{aligned}
D_\epsilon\mathscr S[\delta\epsilon](F)
=\pi_{\mathfrak g}\Big(
&[\Phi_1,\chi]\wedge *F\\
-\frac12 *\{&
[\Phi_1,\chi]\wedge*(\Phi_2\wedge*F)
+\Phi_1\wedge*([\Phi_2,\chi]\wedge*F)
\}\Big).
\end{aligned}
\]

If the moving soldering also moves the metric, Krein form, density, or
real-form projection, their derivatives must be added. A zero epsilon
response is not available by default.

If the curvature is \(F_{B(\epsilon)}\) for a connection depending on the
moving soldering, the additional term
\(D_F\mathscr S_\epsilon[\delta_\epsilon F_B]\) must also be added. The
formula and executable fixture in this section hold \(F\) fixed.

## 5. Finite quaternionic/Krein architecture fixture

The executable probe uses a four-dimensional
\(Sp(1,1)\) analogue on \(\mathbb H^2\simeq\mathbb C^4\), with random
right-\(\mathbb H\)-linear \(\Phi_1,\Phi_2\) matrices. This tests the
three-Hodge/source-shaped architecture, not the native
fourteen-dimensional selector or the Clifford grade flip.

It obtains:

```text
native covariance residual                 4.180e-16
epsilon finite-difference residual          3.225e-10
wrong epsilon-law residual                  1.402
native output right-H defect                <1e-10
imaginary action trace                      0
extra final Hodge output degree             1
```

A deliberately non-quaternionic \(U(2,2)\)-type group element still passes
homogeneous covariance with residual \(3.723\times10^{-16}\), but its output
has right-\(\mathbb H\) defect \(0.3609\). This proves that covariance alone
would admit the wrong real form.

## 6. Why this still does not clear RB1

RB2's source exactness requires more than covariance and reality. In
particular, the cubic term needs the appropriate cyclic identity:

\[
\int\kappa\big(
\alpha\wedge\mathscr S_\epsilon(\beta\wedge\gamma)
\big)
\]

must have the permutations and adjointness that generate the \(3b\)
variation coefficient. It also needs compatible
\(D_B\Phi_i=0\), \(D_BG=0\), \(D_BK=0\), a self-adjoint
\(\pi_{\mathfrak g}\), and the correct Green flux.

One nondegenerate finite fixture compares the cubic finite difference with
the cyclic prediction:

```text
finite derivative   0.131155
cyclic prediction   0.0729469
relative gap        0.444
```

Thus covariance, right-\(\mathbb H\), and action reality do not logically
force the transgression identity. This one counterexample does not prove
that every native fourteen-dimensional \(\Phi_1/\Phi_2\) choice fails it.

The candidate therefore remains:

```text
CONDITIONAL-PRE-RB1
```

It cannot update the RB1 map register or rerun RB2 until:

1. the grade-three output is admitted as part of the same full-\(Sp\)
   connection Euler covector;
2. the native fourteen-dimensional \(\Phi_1/\Phi_2\) normalizations and
   projection are explicit; and
3. the cyclic/Bianchi and Green identities pass.

## 7. If the target must remain grade two

The missing odd factor must be supplied honestly. Two examples are:

\[
n\in\Gamma(V),\qquad
\widehat{\mathscr S}_n(F)
=\kappa^\flat *_G(\iota_nF),
\]

or a first-order operator whose symbol supplies a covector, schematically

\[
\kappa^\flat *_G D_B^*F.
\]

The first adds an observer normal/coorientation field and must be charged
as a new external coordinate unless dynamically constructed. The second
changes the action's differential order. Neither the P1 orientation line
nor the diagonal coframe is an unpaired vector, so neither silently pays
this cost.

## 8. Disposition and next source swing

The preregistered route is killed at its stated symmetry grade:

```text
full-Spin same-Lambda2 Ricci--Einstein: KILLED
```

The adjacent route is emitted:

```text
epsilon-soldered full-adjoint grade flip: CONDITIONAL
```

The next source-action swing should not repeat the full-spin
same-\(\Lambda^2\) Ricci calculation. It should first decide the full-adjoint
carrier question and then compute the native cyclic identity:

1. branch \(\mathfrak{sp}(32,32;\mathbb H)\) by Clifford grade at the
   action's \(A\)-Euler target;
2. install the exact fourteen-dimensional \(\Phi_1,\Phi_2,\pi_{\mathfrak g}\);
3. compute the trilinear cyclic form on the admitted grades;
4. derive the epsilon and Green responses; and
5. only if those pass, return through RB1 and rerun RB2.

No source action, VEV, mass, cosmological constant, anomaly, index, or count
is promoted by this side track.

## Reproduction

Run:

```bash
python3 tests/channel-swings/rb1b_native_bosonic_shiab_probe.py
```

## 2026-07-30 appended RB1c native disposition

[`rb1c-native-grade3-curvature-admission-2026-07-30.md`](rb1c-native-grade3-curvature-admission-2026-07-30.md)
executes the native fourteen-dimensional grade flip that remained untested
above. The later result supersedes only the conditional grade-admission and
cyclicity rows; the central-parity kill of the same-\(\Lambda^2\) route is
unchanged.

The native projected map is nonzero on a generic non-Riemannian
full-adjoint curvature, with norm \(25.2982\), and has the required degree,
Krein reality, and right-\(\mathbb H\) type. On a powered
constant-curvature Riemann/Bianchi fixture, the raw expression has norm
\(1238.21\) but its native grade-three projection is exactly zero. Thus it
does not re-enter as a torsion-free Ricci/Einstein source, while remaining a
live non-Riemannian distortion map.

Trace reversal supplies an adjacent smaller-stabilizer map:

\[
\mathscr S_{\rm tr}(F)
=
\pi_{\mathfrak{sp}}
\left[c(t_{\rm tr})\mathscr S_{\rm raw}(F)\right].
\]

It reopens constant curvature with norm \(1193.17\) and passes native
reality, but fails the RB2 cyclic current identity on six preregistered
full-adjoint fixtures. A four-ordering repair family has full sampled rank,
and its least-singular combination fails the held-out fixture. The earlier
restricted grade-\(2/3\) near-pass is explicitly corrected: its apparent
\((1,1,1,1)\) null relation is rejected held out and cannot be promoted.

Canonical symmetric polarization gives a nonzero covariant derivative-correct
Euler current. A planted pair with zero polarized curvature still gives a
nonzero polarized current, so it cannot be represented by one linear
curvature-to-source map in the tested fixture. It is a different two-input
Euler geometry and would have to reopen RB1 from its action definition.

```text
full-adjoint grade-three map on generic curvature: LIVE
torsion-free Ricci/Einstein source role: KILLED AT BIANCHI BOUNDARY
DeWitt trace-line adapter: CARRIER LIVE / CYCLIC GATE FAILED
canonical polarization: LIVE DIFFERENT GEOMETRY
RB1/RB2 reentry as written: NO
```

## 2026-07-30 hostile closure correction to the RB1c append

The constant-curvature-only wording above is superseded by the completed
pointwise Levi--Civita closure. The probe now executes independent scalar,
traceless-Ricci, and Weyl plants. Clifford reduction proves

\[
\gamma^aF_{ab}=\frac12\operatorname{Ric}_{bd}\gamma^d,
\qquad
\gamma^{ab}F_{ab}\ \text{is purely scalar},
\]

with the first Bianchi identity killing the possible grade-three/four
remainders and Ricci symmetry killing grade two. The three irreps exhaust
the \(3185\)-dimensional algebraic-Riemann representation, and the native
grade-three source vanishes on all of it. Powered raw controls remain
nonzero; the corrected scalar raw norm is \(82.2679\), not \(1238.21\).
The DeWitt trace adapter has corrected scalar-plant norm \(78.2304\), not
\(1193.17\).

The six order-one cyclic fixtures are deterministic seeded fixtures, not
preregistered fixtures. The covariance evidence for the polarized branch
is one finite moving-data homogeneous proxy, not a theorem. Its
factorization failure is a planted algebraic counterexample, and the
surviving object is a two-input Euler covector rather than a new
source-valued linear current.

```text
generic non-Riemannian grade-three response: LIVE
all pointwise algebraic-Riemann irreps: PROJECTED SOURCE ZERO
DeWitt trace adapter: CARRIER REOPENED / CYCLIC GATE FAILED
polarization: DIFFERENT TWO-INPUT EULER-COVECTOR GEOMETRY
RB1/RB2 reentry as written: NO
```
