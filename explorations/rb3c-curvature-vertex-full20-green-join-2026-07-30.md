---
title: "RB3c typed curvature vertex, full-20 Krein completion, and finite Green/Q join"
status: active_research
doc_type: construction_result
created: 2026-07-30
lane: "1"
work_item: RB3C-CURVATURE-VERTEX-FULL20-GREEN-JOIN
run: lab/process/runs/GUH-20260730T232344Z-rb3b-trace-vertex-grade3/run-plan.md
probe: tests/channel-swings/rb3c_curvature_vertex_full20_green_probe.py
grade: "W125/N4a CURVATURE MAP RETYPED S->R / ONE DIAGONAL-G2 S<->R KREIN-ADJOINT COMPLETION CONSTRUCTED / ONE MATRIX-DERIVED Q_F AMPLITUDE JOINED TO A PLANTED ABELIANIZED 1D GREEN/CHAIN-RULE FIXTURE. The written right-P_R sandwich is dimensionally invalid for the owned W125 map. Closing T_b with its native Krein reverse is an additional right-H, K-self-adjoint full-20 completion choice, not yet an implementation of W125's physical field embedding. The G2-plus-R pairing is nondegenerate; the completed vertex itself has rank 256 and kernel 1664. DeWitt versus raw-Frobenius signature/Hodge signs pass as an independent compatibility control but are not used by the executed polynomial Green fixture. No full Q_F 12-form, D_A^coad current, common epsilon_IG map, Y14 formal adjoint/domain/boundary, density variation, full-Sp covariance, polarization selection, or JD-versus-total bridge selection is constructed."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# RB3c typed curvature vertex, full-20 Krein completion, and finite Green/Q join

## Result first

This swing corrects the first map's type, constructs one additional finite
Krein completion, and tests one matrix-derived current amplitude in a
bounded Green/chain-rule fixture. It does not yet remove the full
curvature-current or physical-field-placement placeholders.

The owned W125/N4a curvature vertex is

\[
T_b:S\longrightarrow
R=\ker\Gamma\subset V^*\otimes S,
\qquad
\dim_\mathbb C S=128,\quad
\dim_\mathbb C R=1664.
\]

Its matrix before choosing an \(R\) basis has shape \(1792\times128\).
It is not an endomorphism of \(R\). Consequently, the written expression

\[
P_R\,T_b\,P_R
\]

is dimensionally invalid: the right \(P_R\) expects a vector-spinor, while
\(T_b\) expects a spinor.

Keeping the actual type produces a constructive adjacent completion. Let

\[
T_b^\times=K_S^{-1}T_b^\dagger K_{VS}.
\]

Then

\[
\boxed{
\mathcal V_b=
\begin{pmatrix}
0&T_b^\times\\
T_b&0
\end{pmatrix}}
\]

on
\(E_{20}=S\oplus(V^*\otimes S)=S\oplus I\oplus R\)
is right-\(\mathbb H\)-linear and Krein-self-adjoint. It maps
\(S\leftrightarrow R\) and annihilates \(I\) in the reverse direction.
It has rank \(256\) and kernel dimension \(1664\); the operator is therefore
highly degenerate.
For the diagonal
\(G_2=\operatorname{diag}(1,1/14)\) member already present in the
repository, the **pairing**
\(K_G=G_2\oplus K_R\) is nondegenerate with signature \((960,960)\).
This completion is not yet the W125 source action: its physical
\(S\oplus R\) field embedding has not been selected.

The same executable fixture then places this vertex next to:

1. an independent native trace-reversed \((9,5)\) Hodge-sign control;
2. one finite \(SO(3)/SO(2)\)-type realization of the
   \(A_0\)-connection linearization and candidate formal adjoint;
3. one matrix-derived scalar amplitude for a single \(Q_F\) component; and
4. a planted abelianized \(1/12/13\)-form polynomial Green fixture,
   including an endpoint boundary term.

In a synchronized one-parameter fixture, the finite derivative is reproduced
by the sum of the connection and moving-amplitude responses. Freezing the
amplitude or dropping the planted endpoint term changes the answer. No common
\(\epsilon_{\rm IG}\) map is yet shown to generate both movers.

It does not select the diagonal \(G_2\) member, the overall curvature
coefficient \(\lambda_F\), the \(J_D\)-only versus total-current bridge, or
the \(A_0\)-induced connection over its still-live rivals.

## Plain English

The curvature coupling was being treated like a square operator acting
inside the gamma-traceless vector-spinors. It is actually a rectangular map:
it takes an ordinary spinor and produces a gamma-traceless vector-spinor.
That distinction matters. One of the projectors written around it was on
the wrong side and could never compose.

The adjacent completion is natural in an indefinite theory: pair the forward
rectangular map with its Krein reverse. Together they form one off-diagonal,
right-\(\mathbb H\), Krein-self-adjoint operator on the complete
20-component carrier. The surrounding pairing is nondegenerate; the
operator is not.

This is enough to emit one scalar bilinear amplitude and stress-test a
candidate chain rule. In the test, an \(A_0\)-connection fixture and a
Clifford-conjugation fixture move with the same parameter. Both derivative
pieces are visible, as is the endpoint term of a planted polynomial Green
identity. The test does not yet prove that one physical
\(\epsilon_{\rm IG}\) field causes both motions or construct the full
fourteen-dimensional current.

Trace reversal still passes an important compatibility control: it gives the
program-native \((9,5)\) Hodge signs, while raw Frobenius reverses them. The
executed one-dimensional polynomial Green calculation does not apply either
Hodge operator, so this run does not claim that trace reversal selects or
changes that finite result.

## 1. Layer 0: the map is rectangular

For one adjoint-valued curvature two-form coefficient \(b\), W125 constructs
the contract/wedge combination

\[
T_b
=
\operatorname{contract}(b)
-\frac16\operatorname{wedge}(b).
\]

The coefficient is not fitted. The native gamma-trace equation gives

\[
t_*=-\frac16
\]

exactly. In the executable fixture,

\[
\Gamma T_b=0
\]

before applying \(P_R\), while deleting the wedge term produces gamma-trace
norm \(11.313708\) and a nontrivial projection shift \(3.023716\).

The objects called “curvature vertex” must therefore remain separated:

| object | type |
| --- | --- |
| \(T_b\) | \(S\to R\subset V^*\otimes S\) |
| \(T_b^\times\) | \(V^*\otimes S\to S\); restricts to \(R\to S\) and kills \(I\) |
| \(\mathcal V_b\) | \(E_{20}\to E_{20}\), off-diagonal \(S\leftrightarrow R\) |
| \(q_b(Z)\) | one scalar amplitude \(\frac12\operatorname{Re}\langle Z,\mathcal V_bZ\rangle\) |
| \(Q_F\) | target density-dual 12-form; only one amplitude is emitted here |
| \(J_F\) | target \(D_A^{\rm coad}Q_F\); not constructed by this fixture |

The invalid \(P_RT_bP_R\) sandwich compared different members of this
table. The adjacent completion does not reinterpret \(T_b\) as \(R\to R\)
or by itself select how W125's physical field occupies \(S\oplus R\).

## 2. Native full-20 completion

The vector-spinor Krein form is

\[
K_{VS}=\eta_{9,5}\otimes K_S.
\]

With the native indefinite adjoint,

\[
T_b^\times=K_S^{-1}T_b^\dagger K_{VS},
\]

the finite fixture verifies

\[
\langle Z_{VS},T_bZ_S\rangle_{K_{VS}}
=
\langle T_b^\times Z_{VS},Z_S\rangle_{K_S}.
\]

Both directions are right-\(\mathbb H\)-linear. The completed operator
\(\mathcal V_b\) is \(K_E\)-self-adjoint, has only \(S\leftrightarrow R\)
blocks, and satisfies \(T_b^\times I=0\).

For the tested diagonal member of the repository's \(G_2\) family:

| carrier | signature |
| --- | ---: |
| \(S\) | \((64,64)\) |
| \(I=\operatorname{im}\Gamma\) | \((64,64)\) |
| \(R=\ker\Gamma\) | \((832,832)\) |
| \(E_{20}\) | \((960,960)\) |

Here \(G_2\) governs the \(S/I\) copy pairing, while \(K_R\) is the separately
fixed native pairing on \(R\). This proves existence of one nondegenerate
**pairing** compatible with the completion. It does not make
\(\mathcal V_b\) nondegenerate, select that point from the
four-real-parameter \(G_2\) family, or fix the overall \(\lambda_F\).

## 3. Independent trace-reversal compatibility control

The complete target current must eventually use the actual symmetric-metric
fibre:

\[
\operatorname{Sym}^2T^*X:
\quad
(7,3)_{\rm raw}
\longrightarrow
(6,4)_{\rm DeWitt}.
\]

After adding the base \((3,1)\), the native ambient signature is \((9,5)\),
not \((10,4)\). Therefore

\[
*^2=+1 \text{ on degrees }1,13,
\qquad
*^2=-1 \text{ on degrees }2,12.
\]

The raw-Frobenius control reverses both signs. The probe also checks the
linear musical identity

\[
G_{\rm DW}(-g/4,k)=\tfrac14\operatorname{tr}_g(k),
\]

whereas raw Frobenius returns its negative. A quadratic-only control would
not have detected this. These are necessary ambient compatibility checks.
The finite Green fixture below uses exterior reorder signs and a planted
one-dimensional polynomial profile; it does not apply the DeWitt Hodge/Riesz
map. Thus the trace reversal is not a demonstrated cause of that fixture's
numerical response.

## 4. Finite realization of the candidate \(A_0\) Green formula

At the identity lift, write

\[
A_0=\omega+\beta,\qquad
\omega\in\mathfrak h,\quad
\beta\in\mathfrak m,\quad
\xi=g^{-1}\delta g\in\mathfrak m.
\]

For the local candidate, the formal bundle-level formulas proposed for
later construction are

\[
\Gamma_{\epsilon}^{A_0}
=
A_0-g\,\operatorname{pr}_{\mathfrak m}
\bigl(g^{-1}A_0g+g^{-1}dg\bigr)g^{-1},
\]

the exact linearization is

\[
L_{A_0}\xi
=
-D_\omega\xi
+\operatorname{pr}_{\mathfrak h}[\beta,\xi].
\]

Its formal adjoint in the invariant pairing is

\[
L_{A_0}^{!}(\eta_{\mathfrak m}+\eta_{\mathfrak h})
=
\operatorname{pr}_{\mathfrak m}
\left(
D_\omega\eta_{\mathfrak m}
+[\eta_{\mathfrak h},\beta]
\right),
\]

with boundary owner

\[
\mathfrak G_{A_0}(\eta,\xi)
=
-\int_{\partial Y}
\langle\eta_{\mathfrak m},\xi\rangle.
\]

Finite differencing a compact \(3\times3\) symmetric-pair realization of
the connection agrees with \(L_{A_0}\) to
\(2.52\times10^{-11}\). In that one-dimensional polynomial fixture,
the left, bulk, and boundary values are respectively

\[
-0.382939467,\qquad
0.481060533,\qquad
-0.864000000.
\]

Removing either the \(\beta\)-adjoint term or the endpoint term breaks the
finite identity. This constructs one realization/check of the candidate
formal-adjoint and Green formula. It does not construct the actual
\(Y^{14}\) domain, density/Hodge operator, boundary conditions, or physical
boundary geometry, and does not prove that this branch is the connection
meant by N1.

## 5. One \(Q_F\) amplitude in an abelianized chain-rule fixture

For one fixed adjoint coefficient \(b\) and one fixed full-20 field \(Z\),
the native matrices emit the scalar amplitude

\[
b\wedge\widehat Q_F
=
\frac{\lambda_F}{2}
\operatorname{Re}
\langle Z,\mathcal V_b Z\rangle_{K_E}\,\mu_G.
\]

The fixture sets \(\lambda_F=1\) only to test the map. It keeps
\(T_b\), its final \(P_R\), \(K_E\), fixed \(Z\), fixed \(b/\rho_h\), and a
unit density explicit. It does not vary the density or volume form. At the
reference point it obtains

\[
q(0)=0.007437949,\qquad
\dot q=-0.006808802.
\]

The Clifford-conjugation fixture genuinely changes the generic projector.
Because the exact \(-1/6\) family already lies in \(\ker\Gamma\), however,

\[
(\delta P_R)T_b=0
\]

on this channel. The measured \(\dot q\) comes from the moved raw
contract/wedge/gamma map, not from a demonstrated projector-response term.
This does not permit \(P_R\) to be frozen on other images.

To test the intended algebra, the script then **plants**
\(\theta(x)=1+x^2\), a 12-form coefficient profile
\(q(x)=2x+x^3\), a unit density, and an endpoint boundary on an interval.
It works on a fixed-\(\mathfrak h\), \(A=0\) slice, so
\(D_AQ_F=dQ_F\). For the resulting comparator

\[
\Delta S=-J_F[\theta]
=-\int_Y\theta\wedge D_AQ_F,
\]

the \(14\)-dimensional reorder signs are

\[
(-1,+1,-1)
\]

for \(D\theta\wedge Q_F\), \(\theta\wedge DQ_F\), and the boundary term.
One scalar parameter synchronizes two otherwise unlinked motions: the
finite \(SO(3)\) \(A_0\)-connection realization and conjugation by
\(\exp(s\gamma_0\gamma_1\gamma_2)\). The finite derivative and analytic
chain rule agree:

\[
\frac{d}{ds}\Delta S\bigg|_{0}
=0.022717673
=
\underbrace{-0.006333215}_{\text{connection response}}
+
\underbrace{0.029050888}_{\text{moving-current response}}.
\]

The planted polynomial endpoint contribution is independently nonzero:

\[
\mathfrak G_{Q_F}=0.040852811
\]

in that deterministic fixture. Thus:

- freezing the typed current misses a nonzero term;
- dropping the Green flux changes the Euler response; and
- the direct and Green-expanded moving-\(Q_F\) terms agree.

These numbers are powered controls for a possible join, not physical
couplings or predictions. No common \(\epsilon_{\rm IG}\) map, simultaneous
gauge-covariance convention for fixed \(\rho_h\), full \(Q_F\) 12-form,
\(D_A^{\rm coad}Q_F\), nonabelian gauge transport, density variation, or
physical boundary has been constructed.

## 6. What changes and what remains open

The previous RB3 ledger changes as follows:

```text
T_GT/V_b full-20 type: S->R RETYPED
right P_R sandwich: REJECTED AS DIMENSIONALLY INVALID
one S<->R Krein-adjoint completion choice: CONSTRUCTED
one native-matrix Q_F amplitude: CONSTRUCTED
A0 formal-adjoint/Green formula: PASSES ONE 1D FINITE REALIZATION
synchronized connection/amplitude chain rule: PASSES ONE FIXTURE
physical S-plus-R field embedding: OPEN
full Q_F and D_A^coad current: OPEN
common epsilon_IG mover: OPEN
Y14 domain/density/Hodge/boundary geometry: OPEN
G2 polarization selection: OPEN
lambda_F normalization: OPEN
connection-branch selection: OPEN
JD versus total-current bridge selection: OPEN
```

The highest-information continuation is first to select or derive the
physical \(S\oplus R\) embedding that turns this completion into an actual
W125 action term, then construct the full \(Q_F\) form, common
\(\epsilon_{\rm IG}\) motion, \(D_A^{\rm coad}\) current, density/Hodge
response, and \(Y^{14}\) Green/domain data. Only then may both surviving RB2
Euler systems consume the map and use a held-out source-owned identity to
discriminate the bridge choices. If the full \(G_2\) family changes the
discriminator, its parameters must enter the same constraint-surplus ledger
as the trace-bidoublet parity/orientation choices.

No physical W125 field embedding, full current, common mover, full-\(Sp\)
covariance, \(Y^{14}\) boundary geometry, VEV, mass, stationary solution,
nonlinear CME, common domain, anomaly, index, generation count, or
cosmological value is claimed.

## Reproduction

Run:

```bash
python3 tests/channel-swings/rb3c_curvature_vertex_full20_green_probe.py
```
