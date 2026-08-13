---
title: "RB4 moving observer/Cartan family and source-indicated complex--Cartan flag"
status: active_research
doc_type: construction_result
created: 2026-07-30
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-RB4
run: lab/evidence/predecessor-records/rb4-observer-cartan-moving-family.md
probe: tests/channel-swings/rb4_observer_cartan_moving_family_probe.py
grade: "EXACT FINITE GEOMETRY / ACTION OWNERSHIP OPEN. The native trace-reversed Sym2 fibre, base-induced W4(u) Cartan projector, complement, orientations, Clifford frame, volumes, conditional Phi family, internal moving-t family, and optional moving-J family are constructed and tested with powered frozen controls. The observer-only map u->J is exactly obstructed by the fixed-u SO(3) stabilizer and a planted path-dependence control. Source inspection supports, but does not prove, a dynamical complex--Cartan flag interpretation. No epsilon_IG-to-flag map, flag Euler equation, stable orbit, SM determinant-one reduction, retained mode, mass, cosmological value, index, or count is constructed."
canon_verdict_change: none
outcome: "MOVING-u-CARTAN-EXACT; u-TO-J-REFUTED; COMPLEX-CARTAN-FLAG-DYNAMIC-CANDIDATE; OWNERSHIP-OPEN"
---

# RB4 moving observer/Cartan family

## Result first

RB4 resolves the kinematic part of the fixed-Cartan gap and sharpens the
remaining action problem:

```text
TRACE-REVERSED (6,4) FIBRE:                       NATIVE / REQUIRED
u -> W4(u) CARTAN PROJECTOR:                     CONSTRUCTED EXACTLY
JOINT BASE-LORENTZ/CLIFFORD/Phi TRANSPORT:       CONSTRUCTED EXACTLY
FIXED-u Spin(3) STABILIZER:                      EXACT
FROZEN PROJECTOR/SOLDERING/VOLUMES:              REFUTED BY CONTROLS
INTERNAL Spin(4) WITH MOVING t:                  CONSTRUCTED CONDITIONALLY
INTERNAL Spin(4) WITH CANONICAL FIXED t:         ONLY Spin(3) SURVIVES
COMPATIBLE J ON (6,4):                           EXISTS AS A FAMILY
COMPATIBLE J ON RAW (7,3):                       OBSTRUCTED
OBSERVER-ONLY MAP u -> J:                        REFUTED
FULL CARTAN/J/epsilon_IG ACTION OWNERSHIP:       OPEN
```

The minimal object missing from RB3b is the vertical Cartan involution
\(\Theta_\chi\), equivalently its negative-plane projector

\[
\Theta_\chi^2=1,
\qquad
P_W=\frac{1-\Theta_\chi}{2},
\qquad
V_{6,4}=A_6\oplus W_4.
\]

A unit timelike observer \(u\) supplies one exact program-geometric family:

\[
W_4(u)
=
\mathbb R\,\widehat h_{\rm tr}
\oplus
\left(u^\flat\odot u^\perp\right).
\]

The executable calculation proves that this is a negative four-plane, its
orthogonal complement is a positive six-plane, and the full conditional
RB3b construction transforms covariantly when the projector, complement,
orientations, Clifford frame, volume elements, trace argument, and field
argument are moved together. This turns the previous fixed-frame algebra
into an exact moving **base-induced Cartan family**.

It does not yet turn it into a physical compactification or a source-owned
field. The observer family is three-dimensional, while the full vertical
Cartan space is

\[
O(6,4)/(O(6)\times O(4)),
\qquad
\dim=24.
\]

Nor does \(u\) supply the complex structure in Weinstein's source language.
At fixed \(u\), a spatial \(SO(3)\) rotation leaves
\(u,P_W,\widehat h_{\rm tr}\) fixed while moving the chosen \(J\) by
\(1.790325043\). Thus the apparent joint \(J\)-transport is a
**framed-observer** construction and does not descend to a map \(u\mapsto
J\).

The most economical full candidate exposed by the source is instead a
compatible complex--Cartan flag

\[
\mathfrak f=(J,\Theta_\chi;t),
\]

with

\[
J^2=-1,
\quad
J^{\dagger_G}=-J,
\quad
[J,\Theta_\chi]=0,
\quad
\Theta_\chi t=-t.
\]

Here \(t\) is the canonical trace line. \(J\) and \(\Theta_\chi\) are
candidate dynamical order parameters, not derived structures. The Cartan
part carries the \(Spin(6)\times Spin(4)\) route; the complex part carries
the \(U(3,2)\) route. Their compact intersection is
\(U(3)\times U(2)\). Reaching the Standard Model group
\(S(U(3)\times U(2))\), with only one \(U(1)\), still requires an explicit
determinant-one, unimodular, or complex-volume condition.

The existing \(\epsilon_{\rm IG}\) can transport a chosen flag and its
Clifford plane. The present N1 action does not yet define a map from
\(\epsilon_{\rm IG}\), \(s\), \(A\), or \(\theta\) that selects the flag,
and it contains none of the resulting flag-variation terms. A fixed flag
inserted now would therefore be an uncharged continuous spurion.

The best working branch is source-selected dynamics, not immediate external
declaration: derive \(\Theta_\chi\) and \(J\) as spectral/polar data of an
existing distortion, curvature, Hessian, or spinless gauge-potential field,
then propagate their variations through N1. The source suggests this
direction but does not supply the construction.

## Plain English

Trace reversal gives exactly the kind of ten-dimensional space Weinstein
needs. It has six positive and four negative directions, and the trace of
the metric is one of the negative directions.

To use that as a Pati--Salam-like split, however, the theory has to say
which four-dimensional negative plane is the physical one. Choosing a
timelike observer on spacetime does give such a plane in a clean,
covariant way. If the observer moves under a Lorentz boost, the four-plane,
the Clifford matrices, and the proposed four-component field all move
together and the equations retain their form. Freezing any of them breaks
the construction. That part now works.

But covariance is not the same thing as physical redundancy. An
Einstein-aether model is also covariant when its preferred timelike vector
is transformed, while the chosen vector still changes observable
propagation. We have not yet proved that the observer/Cartan choice is pure
gauge.

The transcript clue adds something genuinely useful. Weinstein appears to
say: take the one distinguished direction in metric space, apply a complex
structure, and ask where it goes. Mathematically that is naturally

\[
t\longmapsto Jt.
\]

Because of trace reversal, both \(t\) and \(Jt\) are negative and
orthogonal. The new direction is exactly the kind of axis that can break
Lorentz symmetry. The repo's earlier result that no \(J\) is canonical is
therefore not a refutation of this reading. It types \(J\) as the
symmetry-breaking field.

The hostile result is that \(J\) does not come for free with the observer.
Even after fixing \(u\), there is an eight-dimensional family of compatible
choices. The action has to select one, treat it as gauge, or pay for it as
external data.

This gives a much tighter build target than “find a source action.” Build
one moving flag that must simultaneously:

- produce the \(6+4\) Pati--Salam split;
- produce the \(3+2\) complex chain;
- remove the extra \(U(1)\);
- carry the trace-based four-component vertex;
- survive Krein, BV, causal, gravity/cosmology, and right-\(\mathbb H\)
  constraints; and
- keep the index/count datum separate.

That is a heavily overdetermined fit. If it closes, it is informative even
though the construction was reverse engineered.

## 1. Layer 0

### 1.1 Objects separated

| phrase | RB4 object | not identified with it |
| --- | --- | --- |
| metric section | \(s:X\to\operatorname{Met}_{3,1}(X)\) | a timelike observer vector |
| observer | \(u\in SO^+(3,1)/SO(3)\) | a full vertical Cartan point |
| trace direction | canonical DeWitt-negative \(t=\widehat h_{\rm tr}\) | an internally rotated spurion \(\tau\ne t\) |
| base-induced Cartan | \(P_W(u)\), one three-dimensional family of maximal negative four-planes | the full 24-dimensional Cartan family |
| compatible complex structure | \(J\in O(6,4)/U(3,2)\) | \(u\), \(P_W\), or a canonical fibre tensor |
| complex trace axis | \(Jt\), a vertical symmetric tensor | a base observer until a typed eigenline map is built |
| internal \(Spin(4)\) | rotations inside a selected \(W_4\) | base Lorentz boosts |
| moving Clifford plane | the orbit carried by \(\epsilon_{\rm IG}\) | a selected Cartan point or selected \(J\) |
| physical compactification | a gauge quotient or selected stable orbit | mathematical existence of a maximal compact |
| P1/P2 | the already-typed vertical-symbol orientation line | \(\chi\), \(u\), \(J\), or a continuous modulus |
| P3 | the separate relative real-\(KO\) input | any dimension, block count, or orbit component |

The prior RB3b phrase “candidate type for the unknown P2/X-sector datum” is
withdrawn. P2 is already typed as the phase/orientation of the vertical
projected Rarita--Schwinger symbol and is conditionally welded with P1 into
one flat real orientation line. A continuous Cartan or complex-structure
field is a different object.

### 1.2 Cartan existence versus physical selection

The symmetric space

\[
\mathcal C_{6,4}
=O(6,4)/(O(6)\times O(4))
\]

is the space of Cartan involutions, maximal negative four-planes, or
positive majorants of the DeWitt form. It is contractible componentwise, so
the continuous Cartan choice has no intrinsic topological charge. That
settles existence, not physical status.

A field taking values in a contractible space can still be:

1. a Stückelberg/gauge coordinate;
2. a dynamical order parameter;
3. a supplied aether/modulus.

Only the first has zero physical cost automatically. The second has no
external-datum cost only after its action and Euler equation are built. The
third is a new section-valued continuous datum.

The compatible-complex-structure space is different:

\[
\mathcal J_{6,4}=O(6,4)/U(3,2),
\qquad
\dim=20.
\]

It has multiple components and nontrivial compact-reduction freedom. It is
not made contractible by the observer reduction. Any discrete component,
orientation, or complex-volume identification with P1/P2 requires an
explicit map of base spaces and holonomies; shared cardinality is not an
identity.

## 2. The exact base-induced Cartan family

Let \(g(u,u)=-1\) and define

\[
q_a{}^b=\delta_a{}^b+u_a u^b.
\]

For \(k\in\operatorname{Sym}^2T^*X\), the DeWitt-orthogonal projection is

\[
(P_W(u)k)_{ab}
=
\frac14\operatorname{tr}_g(k)g_{ab}
-2u_{(a}q_{b)}{}^c k_{cd}u^d.
\]

The image is

\[
W_4(u)
=
\mathbb R\,\widehat h_{\rm tr}
\oplus
(u^\flat\odot u^\perp),
\]

and the executable signatures are

```text
G_DW on W4(u):       (0 positive, 4 negative)
G_DW on W4(u)^perp:  (6 positive, 0 negative)
raw Frobenius fibre: (7 positive, 3 negative)
```

Set

\[
\Theta_u=1-2P_W(u).
\]

Then

\[
\Theta_u^2=1,
\qquad
\Theta_u^{\dagger_G}=\Theta_u,
\qquad
H_u(v,w)=G_{\rm DW}(v,\Theta_uw)
\]

is positive definite. This is an actual Cartan involution of the
trace-reversed fibre.

For the convention \(h\mapsto\Lambda^Th\Lambda\) and
\(u\mapsto\Lambda^{-1}u\), the finite probe gives

\[
P_W(\Lambda^{-1}u)
=
\operatorname{Sym}^2(\Lambda)P_W(u)
\operatorname{Sym}^2(\Lambda)^{-1}
\]

with defect \(3.33\times10^{-16}\).

The hostile controls have power:

```text
frozen P_W under a boost:             1.940205721
frozen Clifford/soldering frame:      4.857134150
frozen Cartan volumes in Phi:         7.760822882
```

The fixed-\(u\) spatial \(Spin(3)\) stabilizer preserves \(P_W\) exactly.

## 3. Joint Clifford and RB3b transport

Let \(A_6=W_4^\perp\), and let \(\omega_A,\omega_W\) be their oriented
Clifford volumes. The conditional RB3b field is

\[
\Phi_t^\lambda(w)
=
\mathcal P_t^-
\left[
\omega_Wc(w)+\lambda\omega_Ac(w)
\right],
\]

where

\[
\mathcal P_t^-(B)
=\frac12\left(B-c(t)Bc(t)^{-1}\right).
\]

The unique induced \(so(6,4)\) spin lift transports every vertical Clifford
generator and preserves the native Clifford relations. When

\[
(P_W,P_A,\omega_W,\omega_A,c,t,w)
\]

all move together, the finite \(\Phi\)-covariance defect is
\(1.11\times10^{-15}\).

This is the exact moving-family replacement for RB3b's fixed-frame
calculation. It does not choose a physical orbit, a retained mode, or a
vacuum.

## 4. Base Lorentz and internal \(Spin(4)\) do different jobs

Under the base Lorentz action:

- the canonical trace line \(t\) is fixed;
- the observer \(u\) moves;
- the full plane \(W_4(u)\) moves.

Under the selected internal \(Spin(4)\):

- \(W_4\) is preserved;
- a generic transformation moves \(t\) within \(W_4\).

The internal calculation gives:

```text
moving t,w Spin(4) covariance defect:       5.55e-17
fixed-t non-stabilizer residual:             3.188874624
fixed-t Spin(3) stabilizer residual:         0
```

Therefore a fixed canonical trace direction supplies only the
\(Spin(3)\)-equivariant branch. A full moving \(Spin(4)\) family exists only
if the object moved away from the trace line is explicitly carried as a
spurion or order parameter. It should then be denoted \(\tau\), because it
is no longer the canonical trace tensor \(t\).

Pointwise joint transport proves covariance of a family. It does not prove
that choosing a member is gauge or that noncompact physical modes have
disappeared.

## 5. Weinstein's complex-structure clue

The 2025 Into the Impossible transcript places the relevant statements in
one passage:

1. trace reverse the vertical Frobenius metric from \((7,3)\) to \((6,4)\);
2. use the \(Spin(6,4)\), \(SU(3,2)\), and compact-subgroup chains;
3. take the one distinguished dimension in metric space;
4. ask where a complex structure sends it, producing Lorentz breaking “in
   a certain sense”; and
5. “reduce maximal compact subgroups along the fibers.”

See
[`Transcript into the impossible.md`](../papers/drafts/Transcript%20into%20the%20impossible.md)
at timestamps `00:43:04--00:46:40`.

The coherent literal candidate is

\[
t\longmapsto n=Jt.
\]

For an orthogonal \(J\),

\[
G(t,Jt)=0,
\qquad
G(Jt,Jt)=G(t,t)<0.
\]

The probe confirms both identities. It also confirms:

- \((6,4)\) admits orthogonal complex structures;
- raw \((7,3)\) fails the even-even parity condition;
- joint \(O(6,4)\) transport preserves \(J^2=-1\) and
  \(J^{\dagger_G}=-J\);
- freezing \(J,t\) gives a \(Jt\) residual \(0.858628124\).

This is `SOURCE-BOUND`, not `SOURCE-EXPLICIT`. No primary source inspected
here writes \(J\) as a field, gives its action term, or derives its VEV.
The source's own VEV-location and preferred-projection gaps remain open.

### 5.1 Why \(J\) is not a function of \(u\)

An equivariant map

\[
SO^+(3,1)/SO(3)
\longrightarrow
O(6,4)/U(3,2)
\]

would require a seed \(J_0\) fixed by the \(SO(3)\) stabilizer of the seed
observer.

No such \(J_0\) exists. Under fixed-\(u\) \(SO(3)\), the real symmetric
fibre decomposes into blocks of dimensions

\[
2\oplus3\oplus5.
\]

A commuting real \(J\) would preserve the odd three-dimensional block,
where \(J^2=-1\) is impossible.

The executable hostile control makes the path ambiguity visible:

```text
spatial rotation changes u:                  0
spatial rotation changes P_W:                0
spatial rotation changes t:                  0
spatial rotation changes J:                  1.790325043
spatial rotation changes Jt:                 0.407134320
```

Two Lorentz transformations reaching the same observer therefore return
different \(J\)'s. The transported spatial frame was the hidden datum.

At fixed \(P_W\), the compatible \(J\)-family has local dimension

\[
\dim O(6)/U(3)+\dim O(4)/U(2)
=6+2=8.
\]

The probe obtains the same value as the nullity of the linearized
\(J^2=-1\), \(J^{\dagger_G}=-J\), and \([J,P_W]=0\) constraints. This is a
reduction-family dimension, not a physical count.

Even the single axis \(Jt\) retains an \(S^2\) choice inside
\(W_4\cap t^\perp\). This is consistent with symmetry breaking, not
canonicity.

## 6. The common flag and the extra-\(U(1)\) gate

The flag

\[
\mathfrak f=(J,\Theta;t)
\]

is the smallest current candidate that can place the two source group
chains in one object:

| flag piece | stabilizer / role |
| --- | --- |
| \(J\) | \(U(3,2)\), the complex real-form chain |
| \(\Theta\) | \(O(6)\times O(4)\), the compact \(6+4\) split |
| \([J,\Theta]=0\) | \(U(3)\times U(2)\), compatible compact intersection |
| unit complex volume / unimodularity | \(S(U(3)\times U(2))\), one \(U(1)\) |
| \(t\in W_4\) | trace-based RB3b field and possible \(Jt\) breaking axis |

Without the complex-volume or determinant-one condition, the compatible
flag leaves two \(U(1)\) factors. A Standard Model identification would
then owe an extra massless gauge field or an additional breaking
mechanism. This is the first falsification gate for the SM leg, not an
editorial normalization.

No claim is made here that the flag's stabilizer is already the physical
gauge group. The spin covers, global quotient, bundle topology, charge
normalization, and actual full-20 incidence remain to be built.

## 7. Variation

### 7.1 Base-induced projector

At fixed \(g\), let \(\xi=\delta u\in u^\perp\) and

\[
m_a=q_a{}^c k_{cd}u^d.
\]

Then

\[
\begin{aligned}
(D_uP_W[\xi]k)_{ab}
={}&-2\xi_{(a}m_{b)}-2u_{(a}\dot m_{b)},\\
\dot m_a
={}&(\xi_a u^c+u_a\xi^c)k_{cd}u^d
+q_a{}^c k_{cd}\xi^d.
\end{aligned}
\]

For the unrestricted Cartan orbit, write

\[
\delta P_W=[\Omega,P_W],
\qquad
\Omega^{\dagger_G}=-\Omega,
\]

with \(\Omega\) off-diagonal between \(A_6\) and \(W_4\). The \(u\)-formula
samples only the three induced-base-boost directions inside the full
24-dimensional orbit.

### 7.2 The RB3b field

Let

\[
T=c(t),
\qquad
B_\chi(w)=\omega_Wc(w)+\lambda\omega_Ac(w).
\]

Then

\[
\begin{aligned}
\delta\Phi
={}&
\mathcal P_t^-(\delta B)
-\frac12\delta T\,B\,T^{-1}
+\frac12TBT^{-1}\delta T\,T^{-1},\\
\delta B
={}&
(\delta\omega_W)c(w)
+\omega_W\left(\delta c(w)+c(\delta w)\right)\\
&+\lambda(\delta\omega_A)c(w)
+\lambda\omega_A\left(\delta c(w)+c(\delta w)\right).
\end{aligned}
\]

For \(w=P_W\bar w\),

\[
\delta w
=(\delta P_W)\bar w+P_W\delta\bar w.
\]

If the complete family is transported by the same spin lift
\(\widehat\Omega\), then

\[
\delta\Phi=[\widehat\Omega,\Phi].
\]

This identity is necessary for a pure-gauge reading. It is not sufficient:
the complete action and observable quotient must also be invariant.

### 7.3 Action response

For \(M_\chi=T\Phi_\chi\),

\[
\delta M_\chi
=(\delta T)\Phi_\chi+T\delta\Phi_\chi.
\]

The ambient full-20 term emits

\[
\boxed{
\delta_\chi S_{20}
=
\frac12\operatorname{Re}
\int_Y
[Z,\mathbb K_{\mathbf G}\,
\delta_\chi\widehat M_\chi Z].
}
\]

The two defect bilinear branches separately emit

\[
\delta_\chi S_{{\rm Yuk},K}
=
\operatorname{Re}
\int_X
\psi^\dagger K\,
\delta_\chi\widehat M_\chi Y_K\psi,
\]

\[
\delta_\chi S_{{\rm Yuk},C}
=
\frac12\operatorname{Re}
\int_X
\psi^TC\,
\delta_\chi\widehat M_\chi Y_C\psi
+\delta(\text{\(C\)-reality completion}).
\]

Every \(\chi\)-dependent \(P_0,K,C,Y\), slot embedding, retained-mode map,
Hodge operator, density, and domain must be differentiated as well.

If the flag is a composite

\[
\mathfrak f=\mathfrak f(\epsilon_{\rm IG},s,A,\theta),
\]

the existing Euler covectors gain

\[
\mathcal E_\epsilon
\mapsto
\mathcal E_\epsilon
+(D_\epsilon P_W)^!\mathcal E_P
+(D_\epsilon J)^!\mathcal E_J
+\cdots
\]

and the analogous section/connection terms. N1 currently contains none of
these because it defines no composite map.

For an independently varied flag, stationarity is the projected orbit
equation

\[
\Pi_{\mathfrak{so}/\mathfrak h}
\left(
[P_W,\mathcal E_P]
+[J,\mathcal E_J]
+\cdots
\right)=0.
\]

At \(Z=0\), fermion bilinears alone cannot select the bosonic vacuum. A
claimed dynamical reduction needs a bosonic kinetic/potential or constraint
term that remains active in that stratum.

## 8. Source-action ownership

### 8.1 What the source supplies

The source-native first-order bosonic action contains an
\(\epsilon\)-dependent contraction and completed curvature:

\[
I_1^B
=
\left\langle
T_\omega,
*
\left[
\odot_\omega
\left(
F_{B_\omega}
+\frac12d_{B_\omega}T_\omega
+\frac13[T_\omega,T_\omega]
\right)
+\frac{\kappa_1}{2}T_\omega
\right]
\right\rangle.
\]

The public explanation also says that expanding a curvature norm gives a
kinetic term, quartic self-interaction, and a background-curvature
quadratic term capable of producing a Mexican-hat potential. It identifies
minimal and Yukawa coupling as the same geometric kind of operation.

These are valuable design constraints. They do not yet construct the flag.
The source variation held \(\epsilon\) fixed in the displayed
translation-direction calculation, and the source explicitly leaves the
VEV location and preferred projection unresolved.

### 8.2 Lowest-debit construction route

Do not append a free matrix \(J\), a free projector \(P_W\), and an
arbitrary quartic potential. Instead search the existing varied fields for:

1. a \(G\)-self-adjoint vertical endomorphism \(H\) whose separated
   rank-four spectral sector defines
   \[
   P_W=\mathbf1_{\rm selected\ rank\,4}(H);
   \]
2. a \(G\)-skew invertible endomorphism \(Q\) whose polar normalization
   defines
   \[
   J=Q(-Q^2)^{-1/2};
   \]
3. a unit complex-volume section imposing the determinant-one condition;
4. a source-derived nonzero background on which the spectral gaps and
   polar normalization exist.

Candidate owners are the distortion, its curvature, the mixed
vertical-connection sector, the moving section Hessian, and the source's
spinless gauge-potential component. Each gives a concrete derivative through
standard spectral-projector and polar-decomposition calculus.

The trace mode alone cannot generate the claimed Yang--Mills quartic. For
the decomposable coefficient \(\tau\otimes\Phi\),

\[
(\tau\otimes\Phi)\wedge(\tau\otimes\Phi)=0.
\]

Mixed vertical modes or background curvature are mandatory. This prevents
the curvature-potential story from being declared merely because the trace
carrier exists.

### 8.3 Current classification

| class | status |
| --- | --- |
| composite of existing fields | `OPEN`: no map to \(P_W,J,\Omega_{\mathbb C}\) yet |
| pure gauge / compensator | `OPEN`: pointwise covariance passes; observable and BV quotient untested |
| dynamical order parameter | `SOURCE-BOUND / BEST WORKING BRANCH`: VEV and Lorentz-breaking language support it; action equation absent |
| new external continuous datum | `CURRENT FALLBACK`: this is what a frozen flag would be |

Thus RB4 does not add a third datum to the ledger. It identifies the exact
construction whose success would avoid adding one and the exact fallback
cost if it fails.

## 9. Interaction with the compactification no-go

The prior compact-reduction audit remains in force: mathematical
maximal-compact conjugacy does not physically select a positive sector, and
the native Krein form is not itself a Cartan involution.

W240/W243 distinguish two cases:

- chirality-safe neutral, adjoint, maximal-compact, and
  charged-extremal order parameters cannot produce the desired ambient
  compact good-stable;
- a non-extremal timelike vector can have a compact stabilizer, but that
  route was not previously realized by a GU-native condensate.

The base observer \(u\) is precisely of the non-extremal timelike orbit
type, so the \(u\mapsto P_W(u)\) construction is mathematically meaningful.
It selects a vertical Cartan **seed** from the actual symmetric-tensor
geometry. It does not by itself evade the ambient
\(Sp(32,32;\mathbb H)\) no-go or construct a physical positive Hilbert
sector.

Moreover the compactifying Cartan involution is \(Z_2\)-odd relative to the
existing noncompact grading in W240. A source-selected flag therefore
cannot be called chirality-preserving. This may be compatible with the
source's high-curvature Dirac coupling and low-curvature Weyl decoupling,
but that relationship must be built. It cannot be inferred from the common
word “chirality.”

## 10. Seven-axis and five-leg disposition

| axis | RB4 disposition |
| --- | --- |
| Layer 0 | base observer, Cartan involution, complex structure, trace axis, ambient compactifier, and P1/P2 line remain separately typed |
| L1 substrate | unchanged smooth bulk-plus-defect \(P\to Y,s(X)\); a flag must be composite, varied, or charged |
| L2 observer | \(u\mapsto P_W(u)\) exact; \(u\mapsto J\) refuted; preferred-frame status unresolved |
| L3 pairing | native DeWitt/Krein and separate \(K/C\) branches retained; positive majorant is \(\Theta\)-dependent |
| L4 causal order | ambient \((9,5)\) and Lorentzian shadow retained; moving covariance is not physical Lorentz invariance |
| L5 emergence | a selected flag would be ordinary symmetry breaking/order-parameter dynamics, not an RG claim |
| L6 coordination | pure gauge requires a Noether/BV identity; dynamical flag requires an Euler equation; no observer-feedback claim |
| L7 positivity | no positive-Hilbert replacement; physical probability/superselection remains open |

| physics leg | RB4 carry and next kill |
| --- | --- |
| SM/Yukawa/provenance | common flag is a concrete Pati--Salam/complex-chain carrier; kill SM if the determinant-one condition, zero-order \(P_0/\rho/Y_K/Y_C/C\)-reality placement, or retained mode fails |
| quantum/Krein/BV | move every pairing/projector/ghost owner; kill pure gauge if a joint-orbit dependence survives the quotient; keep \(K\) and \(C\) distinct |
| gravity/cosmology | trace reversal and native Hodge signs remain load-bearing; include flag stress, section motion, full Gauss \(H^2+R^Y_{\rm tan}\), and mixed trace modes |
| UV/causality | move the Clifford plane through \(\epsilon_{\rm IG}\) or restrict honestly; rerun \(g=1\), principal/subprincipal, and common-cone tests |
| P3/index/count | require right-\(\mathbb H\) compatibility and a uniform closed domain; no flag dimension, component, support block, or VEV is a count |

## 11. Kill conditions

1. Kill “\(\chi=P2\)”; P2 is already a \(Z_2\) vertical-symbol orientation.
2. Kill “the Krein metric selects the Cartan split”; an indefinite metric
   is not a Cartan involution or positive majorant.
3. Kill “full Cartan reduction” if only the three observer-\(u\)
   directions are varied.
4. Kill \(u\mapsto J\); the fixed-\(u\) stabilizer obstruction is exact.
5. Kill \(Jt\mapsto u\) unless the source forces the symmetric tensor
   \(Jt\) to have a unique timelike eigenline.
6. Kill full internal \(Spin(4)\) if the trace direction is frozen while
   non-stabilizer transformations are claimed.
7. Kill a Pati--Salam/SM promotion if only the fixed-\(t\) Spin(3) image
   survives.
8. Kill the SM group if the flag stops at \(U(3)\times U(2)\) without a
   determinant-one/complex-volume condition.
9. Kill dynamic selection if the bosonic vacuum action is independent of
   the flag.
10. Kill a trace-only Yang--Mills quartic; the decomposable trace
    one-form wedges with itself to zero.
11. Kill “derived from \(\epsilon_{\rm IG}\)” until the equivariant
    orbit-to-flag map and its stabilizer descent are explicit.
12. Kill pure gauge if the gauge-quotiented action, Hessian, or observables
    retain flag dependence.
13. Kill the dynamical branch if its projected Euler equation breaks
    right-\(\mathbb H\), \(K/C\) reality, BV covariance, \(g=1\) causal
    closure, gravity/cosmology, or P3 compatibility.
14. Read no count from four components, eight \(J\)-moduli, 44 supported
    blocks, a \(2+1\) decomposition, or any transcript phrase.

## 12. Next highest-information swing

Run one \(\epsilon_{\rm IG}\)-flag stabilizer and Hessian construction:

1. Type the actual soldering orbit
   \[
   \mathcal O_\epsilon
   =Sp(32,32;\mathbb H)/H_\epsilon.
   \]
2. Test at the seed whether \(H_\epsilon\) fixes a complete target flag
   \[
   \mathcal O_\epsilon
   \longrightarrow
   (P_W,J,t,\Omega_{\mathbb C}).
   \]
   Failure means \(\epsilon_{\rm IG}\) cannot own the flag.
3. In parallel, construct the source-derived spectral candidates \(H,Q\)
   from distortion/curvature/spinless-connection data and compare their
   projectors/polar factors to the target flag.
4. Insert the survivor into the source-completed action and compute
   \[
   \delta_{P,J,\Omega,\epsilon,s,A}S
   \]
   including every zero-order full-20, Hodge, density, section, and
   retained-mode term.
5. Compute the gauge-quotiented flag Hessian:
   - all flag directions gauge \(\Rightarrow\) compensator, no new datum;
   - nondegenerate admissible orbit \(\Rightarrow\) dynamical selection;
   - residual non-gauge zero modes \(\Rightarrow\) modulus/aether;
   - no map/equation \(\Rightarrow\) external continuous flag.
6. Test the complex-volume/unimodularity condition and reject an extra
   \(U(1)\).
7. Rerun the five-leg suite and compare any residual flag-loop orientation
   with \(L_\sigma\) only through an explicit \(w_1\)/holonomy map.

This single swing decides the remaining ownership trilemma while advancing
the source action itself. It does not circle back to rediscover that an
action and datum are needed.

## Validation

Passing:

```text
python3 -B tests/channel-swings/rb4_observer_cartan_moving_family_probe.py
python3 -B tests/channel-swings/rb3b_trace_reversed_bidoublet_full20_probe.py
uv run --with-requirements requirements.txt python -B tests/big-swing/vg_v3_j_commutant_conformal_native.py
uv run --with-requirements requirements.txt python -B tests/W240_z2even_compact_image_nogo.py
uv run --with-requirements requirements.txt python -B tests/W243_charged_corridor_closure.py
```

The native RB4 probe uses deterministic finite matrices and powered
negative controls. The VG-V3 and W240/W243 reruns required the repository
dependency environment for SciPy.

No stationary solution, source-derived flag, physical compactification,
Standard Model identification, mass, cosmological prediction, anomaly
closure, domain, index, or generation count is claimed.

## 13. RB5 ownership disposition

RB5 executes the stabilizer/Hessian swing requested above and corrects the
first ownership possibility. The sentence above saying that one swing would
“decide the remaining ownership trilemma” was too strong: RB5 decides the
coarse \(\epsilon_{\rm plane}\) route, but the refined dynamical and
source-spectral routes remain conditional.

The explicit RB3 finite-local realization is the coarse unframed
Clifford-plane quotient

\[
\epsilon_{\rm plane}
\in
\Gamma\!\left(
P_G/\operatorname{Spin}_0(9,5)
\right).
\]

It cannot equivariantly descend to the complete flag. Its stabilizer moves
even the prerequisite \(V_{3,1}\oplus V_{6,4}\) split: \(51\) of the
\(91\) \(\mathfrak{so}(9,5)\) generators preserve that split and \(40\)
move it. The full vector commutant is scalar. A local-lift change inside the
same Clifford-plane coset moves a supplied vertical projector, so transporting
one chosen seed flag is lift-dependent.

The corresponding global associated bundle/reduction remains conditional;
RB5 does not promote the local orbit calculation to a globally existing
field.

The valid construction direction is

\[
P_G/L_{\rm flag}
\longrightarrow
P_G/\operatorname{Spin}_0(9,5).
\]

The existing Clifford-plane transport and \(A_0\)-induced connection may be
pulled back through this forgetful map. They do not select the refinement:
the connection candidate factors through the coarse quotient and its
derivative vanishes along the flag-refinement fibre.

RB5 also constructs the complete **conditional** spectral/polar calculus

\[
H\mapsto P_-,
\qquad
Q\mapsto Q(-Q^2)^{-1/2},
\]

with exact covariance, first derivatives, and powered failure controls.
No current source field has a target-free typed adapter to the required
\(H,Q\), so the result is a construction preflight rather than source
ownership. The physical Hessian remains ineligible before a source composite,
stationary background, full coupled BV complex, retained-mode closure, and
domain.

See
[`rb5-epsilon-flag-ownership-spectral-hessian-2026-07-30.md`](rb5-epsilon-flag-ownership-spectral-hessian-2026-07-30.md).
