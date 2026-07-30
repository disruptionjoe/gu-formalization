---
title: "RB3 moving soldering, actual-Sym2 trace coordinate, and bridge discriminator"
status: active_research
doc_type: construction_result
created: 2026-07-30
lane: "1"
work_item: RB3-MOVING-SOLDERING-SPINZERO
run: lab/process/runs/GUH-20260730T215838Z-rb3-moving-shiab-dual-track/run-plan.md
probe: tests/channel-swings/rb3_moving_soldering_spinzero_probe.py
grade: "UNFRAMED MOVING CLIFFORD-PLANE ORBIT LOCALLY CONSTRUCTED / FRAMED-ASSOCIATED-BUNDLE AND GLOBAL REDUCTION CONDITIONAL / A0-INDUCED CONNECTION BRANCH CONSTRUCTED BUT NOT IDENTIFIED WITH N1 GAMMA / TRACE COORDINATE CONSTRUCTED / PHYSICAL FULL-20 INSERTION BLOCKED. The native 128-complex-dimensional fixture constructs a full-Sp direction outside Spin(9,5), executes moving P_R and chirality controls, and rejects their frozen versions; other projector and slot transports remain formula-level. The connected plane stabilizer is Spin_0(9,5), giving an 8165-dimensional orbit. The existing A0 plus a reductive projection supplies one economical lift-independent connection candidate with first-order epsilon dependence, but its Green form and identity with the N1 bridge connection are unbuilt. The actual-Sym2 primal and adjoint-valued dual trace projectors are exact. The missing physical insertion is widehat c_{rho,20}(tau tensor Phi_trace); its first unresolved factor is explicit rho_S(Phi_trace), and its full-20 lift is separately missing. A homogeneous chain-rule proxy proves the RB2 relative-response polynomial is not identically zero, but the literal Q_F/P_R/A0-current/Green join remains open. No VEV, mass, cosmological value, index, count, or preferred bridge is selected."
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# RB3 moving soldering, actual-Sym2 trace coordinate, and bridge discriminator

## Result first

RB3 returns:

```text
MOVING-CLIFFORD-PLANE: LOCALLY CONSTRUCTED
CONNECTED STABILIZER: Spin_0(9,5), dim 91
MOVING ORBIT: dim 8256-91 = 8165
A0-INDUCED CONNECTION CANDIDATE: locally lift-independent; identity with N1 Gamma open
ACTUAL-SYM2 TRACE COORDINATE: CONSTRUCTED
PHYSICAL FULL-20 INSERTION: MISSING
FIRST UNRESOLVED FACTOR: rho_S(Phi_trace)
CONSTRAINT SURPLUS: UNCOMPUTABLE FIRST AT rho_S(Phi_trace)
BRIDGES: BOTH SURVIVE HOMOGENEOUS CHAIN-RULE PROXY
LITERAL MOVING Q_F/P_R/A0/GREEN JOIN: OPEN
GLOBAL H REDUCTION: CONDITIONAL
NO VEV, MASS, COSMOLOGICAL VALUE, INDEX, OR COUNT
```

This is not a rediscovery that a soldering field or source datum is needed.
The moving Clifford-plane orbit, one local connection candidate, the unique
actual-\(\operatorname{Sym}^2\) trace coordinate, and a chain-rule
discriminator proxy between the two RB2 actions are now explicit. Writing
them exposed the next missing object at a much sharper level: not “the
Higgs,” “the source,” or “the external datum,” but the physical insertion

\[
\widehat{\mathfrak c}_{\rho,20}
(\tau\otimes\Phi_{\rm tr}).
\]

Its first unresolved factor is the explicit native spinor matrix
\(\rho_S(\Phi_{\rm tr})\). The lift of that factor to the full-20 carrier is
a separate missing arrow.

## Plain English

The fixed fourteen-dimensional Clifford geometry really can move inside the
large \(Sp(32,32;\mathbb H)\) group. We built an explicit motion that is
allowed by the quaternionic and indefinite structure, preserves all
Clifford relations, and nevertheless moves eleven of the fourteen old
Clifford directions out of their original plane. Freezing \(P_R\) or
chirality fails strongly; simultaneously moving \(P_R\) restores the tested
RR covariance. Transport of \(P_0,\rho,Y\), and every thin slot is presently
a formula-level requirement rather than an executed native placement.

That construction revealed an important fork. A point of the orbit
does not by itself give the connection used in the distortion
\(\theta=A-\Gamma-U\). Different local lifts of the same orbit point produce
different bare Maurer--Cartan terms. The already supplied \(A_0\) supplies
one economical reductive connection candidate without a new local datum.
It is not forced: a Levi--Civita/spin connection derived from a soldering
jet or an independent \(H\)-connection remains a rival. First-order
\(\epsilon_{\rm IG}\) dependence creates a Green/boundary **obligation**;
the Green form itself is still unbuilt.

On the spin-zero side, there is now an exact geometric scalar coordinate:
the trace line in the actual symmetric-metric fibre. It is not yet a Higgs
or a mass. Its coefficient still lies in the gauge adjoint, and the
spinor representation matrix that would start telling us how it acts has
not been supplied explicitly. Even after that, its full-20 lift remains to
be built. Those are the first exact construction targets.

Finally, the two surviving action choices have an exact relative
\(\epsilon_{\rm IG}\) chain-rule formula. One homogeneous matrix fixture is
nonzero, proving the proxy polynomial is not identically zero. The fixture
does not yet combine literal \(Q_F\), moving \(P_R\), the \(A_0\)-induced
connection, density, and boundary terms.

## 1. Layer-0 register

The following objects remain separate:

| object | constructed status |
| --- | --- |
| unframed Clifford plane \(G/H_{\rm Cl}\) | local orbit constructed |
| soldering map \(TY\to\operatorname{End}_{\mathbb H}S\) | constructed locally when the orbit is paired with the vector-frame/soldering isometry |
| bridge connection required by N1 | still a fork |
| \(A_0\)-induced reductive \(\Gamma^{A_0}_{\epsilon}\) | one locally constructed candidate; identity with N1 \(\Gamma\) unresolved |
| actual-\(\operatorname{Sym}^2\) trace coordinate | constructed |
| adjoint coefficient \(\Phi_{\rm tr}\) | constructed as an output coordinate |
| explicit \(\rho_S(\Phi_{\rm tr})\) on the native spinor | first unresolved factor |
| full-20 insertion \(\widehat{\mathfrak c}_{\rho,20}(\tau\otimes\Phi_{\rm tr})\) | missing physical object |
| Yukawa/Higgs placement | unbuilt downstream |
| supplied or dynamical VEV | neither supplied nor solved |
| four-dimensional cosmological Euler response | unbuilt downstream |

The trace coordinate is not \(R/4\), a gauge singlet, a Standard Model Higgs
representation, a VEV, or a generation label.

## 2. Moving Clifford-plane orbit

Let

\[
G=Sp(32,32;\mathbb H),\qquad
S=\mathbb H^{64},
\]

and let \(c_0(V_{9,5})\subset\operatorname{End}_{\mathbb H}(S)\) be the
reference Clifford fourteen-plane. Its moving orbit is

\[
\mathcal O_{\rm Cl}=G/H_{\rm Cl}.
\]

The connected normalizer is exactly

\[
H_{\rm Cl}^0=\operatorname{Spin}_0(9,5).
\]

The proof is short. If \(X\in\mathfrak{sp}(32,32;\mathbb H)\) satisfies
\([X,c_0(V)]\subset c_0(V)\), differentiating the Clifford relations forces
the induced action on \(V\) to lie in \(\mathfrak{so}(9,5)\). Subtract its
spin lift. The remainder commutes with
\(\mathrm{Cl}(9,5)=M(64,\mathbb H)\), so within the right-\(\mathbb H\)-linear
endomorphisms it is a real scalar. Krein skewness kills that scalar.

Thus

\[
\dim G=64(2\cdot64+1)=8256,\qquad
\dim H_{\rm Cl}=91,
\]

and

\[
\dim\mathcal O_{\rm Cl}=8165.
\]

This is not yet the final N1 stabilizer. Preserving the written \(4+10\)
split reduces the evident spin stabilizer to
\(\operatorname{Spin}(3,1)\times\operatorname{Spin}(6,4)\), dimension \(51\).
The actual symmetric-metric image uses the six-dimensional
\(\operatorname{Spin}(3,1)\) action. \(P_0,\rho,Y\), end data, and active
action tensors can reduce the stabilizer further.

### Framed-local transport formulas

For a chosen local representative **and vector frame** \(g\),

\[
c_g(v)=g\,c_0(v)\,g^{-1}.
\]

On the vector-spinor carrier \(R_g=1_V\otimes g\),

\[
P_{I,g}=R_gP_{I,0}R_g^{-1},\qquad
P_{R,g}=R_gP_{R,0}R_g^{-1}.
\]

The same framed formula applies to \(\Gamma_{\rm tr}\), \(j\), chirality,
chiral projectors, and the thin carrier slots. Under \(g\mapsto gh\), the
\(\operatorname{Spin}(9,5)\) element rotates the vector labels. These
objects descend only when the vector frame/soldering isometry co-transforms
by the inverse \(SO(9,5)\) action. The executable native fixture directly
tests \(P_R\) and chirality; \(P_I\) follows algebraically from \(1-P_R\);
\(P_0,\rho,Y\), and all thin-slot lifts remain formula-level.
Infinitesimally,
with \(X=\dot g g^{-1}\),

\[
\delta c=[X,c],\qquad
\delta P_R=[1\otimes X,P_R].
\]

For a fixed adjoint coefficient,

\[
\delta_\epsilon c_\rho(v)
=
\sum_a[X,c(\nu^a)]\,\rho(\Phi_a).
\]

Under simultaneous gauge transport of \(\Phi\), the full insertion
transforms by conjugation.

The native \(K\) pairing remains fixed. In the checked basis,
\(C_+=-KC_J\). \(K\)-unitarity plus right-\(\mathbb H\)-linearity therefore
preserves the skew \(C_+\) branch throughout the full native group. The
symmetric \(C_-\) branch is not preserved by the explicit generic
full-\(G\) motion; it must move by congruence or debit a smaller stabilizer.
The two branches therefore cannot be collapsed.

## 3. Exact native hostile motion

The executable fixture uses the repository's signed
\(128\times128\) Jordan--Wigner matrices and

\[
X=\gamma_0\gamma_1\gamma_2,\qquad
g(t)=\cos t\,1+\sin t\,X.
\]

It verifies

\[
X^2=-1,\qquad
X^\dagger K+KX=0,\qquad
XC_J=C_J\overline X.
\]

So \(g(t)\) is an honest native quaternionic \(K\)-unitary subgroup. \(X\)
has Clifford grade three, not spin grade two. It commutes with
\(\gamma_0,\gamma_1,\gamma_2\); for each of the other eleven gammas,
\([X,\gamma_a]\) has normalized residual one within numerical tolerance
against the old
fourteen-plane.

The deterministic control gives:

```text
frozen-P_R motion ratio                 0.315443
written RR primitive fixed-Z derivative 30.521455
simultaneously transported derivative  -5.329e-09
```

The RR number is a control using the already written
\(P_Rc(v)P_R\) primitive. It proves the projector-response channel is live.
It is not relabelled as the literal twelve-form \(Q_F\). For the actual
\(Q_F\), the moving response must include every occurrence of
\(P_R,V_b,K_E\), and the density policy.

## 4. An \(A_0\)-induced connection candidate

A point in \(G/H_{\rm Cl}\) is an unframed Clifford plane. A local lift is
defined only modulo \(g\mapsto gh\), \(h:Y\to H_{\rm Cl}\). The bare term
\(-dg\,g^{-1}\) changes by an \(h\)-connection term and does not descend.

One economical construction uses the already supplied \(A_0\). With the reductive
\(\mathfrak g=\mathfrak h\oplus\mathfrak m\) projection,

\[
B_0=g^{-1}A_0g+g^{-1}dg,\qquad
\omega=\operatorname{pr}_{\mathfrak h}B_0,
\]

\[
\Gamma^{A_0}_{\epsilon}
=g\omega g^{-1}-dg\,g^{-1}
=A_0-g\operatorname{pr}_{\mathfrak m}(B_0)g^{-1}.
\]

The transformation

\[
\omega\mapsto h^{-1}\omega h+h^{-1}dh
\]

cancels the lift ambiguity. A pointwise
\(\mathfrak{so}(3)/\mathfrak{so}(2)\) Lie-algebra control rejects the bare
Maurer--Cartan expression and verifies this candidate expression.

The candidate dependency overlay is:

```text
abstract N1 object: Gamma_conn(epsilon_IG), still unresolved
candidate branch:   Gamma_conn^A0(epsilon_IG,d epsilon_IG,A0,pr_spin)
```

The \(\epsilon_{\rm IG}\) variation is first order and therefore requires a
Green/boundary owner. `G_Gamma` remains unbuilt until the formal adjoint and
boundary form are written. \(A_0\) participates in the candidate's
background response. RB2 checks homogeneous constant-gauge covariance on
this branch; it does not prove a local Ward identity.

Locally, this adds no external datum. Globally, an \(H_{\rm Cl}\) reduction
must exist. The clean no-new-datum construction is

\[
P_G=Q_{\rm Spin}(Y)\times_{\operatorname{Spin}(9,5)}G,
\]

using the inherited spin frame bundle. If the supplied \(G\)-bundle is
arbitrary, reduction existence is an obstruction determined by that bundle.
Choosing the reduction is the \(\epsilon\) field itself. A separate global
sector is an additional datum only if the variational or boundary setup
independently fixes one; it is never silently relabelled as P1/P2 or P3.

## 5. Exact actual-\(\operatorname{Sym}^2\) trace coordinate

For the four-dimensional metric fibre, let

\[
h_{\rm tr}=-\frac14g,\qquad
\tau(k)=\frac14\operatorname{tr}_g(k)
=G_{\rm DW}(h_{\rm tr},k).
\]

Then

\[
\tau(h_{\rm tr})=-\frac14.
\]

For a vertical covector
\(v\in(\operatorname{Sym}^2T^*X)^*\otimes\operatorname{ad}P\), define

\[
\Phi_{\rm tr}(v)=-4v(h_{\rm tr}),\qquad
i_{\rm tr}(\Phi)=\tau\otimes\Phi,
\]

\[
p_{\rm tr}=i_{\rm tr}\circ\Phi_{\rm tr}.
\]

The probe separately verifies the primal tensor projector
\(h\mapsto-4\tau(h)h_{\rm tr}\) and the adjoint-valued dual projector:

\[
p_{\rm tr}^2=p_{\rm tr}.
\]

Solving all six Lorentz invariance equations on the ten-dimensional actual
symmetric-metric fibre gives a one-dimensional invariant subspace. The
trace Clifford insertion is nonzero and has rank \(128\). This is the
unique nonzero fixed Lorentz-scalar stratum found by the actual-fibre
screen.

Its target is still \(\operatorname{ad}P\). A four-dimensional Lorentz
scalar is not automatically a gauge singlet.

## 6. The full-20 placement attempt

Writing the zero-order operator exposes the arrow order:

\[
p_{\rm tr}
\longrightarrow
\Phi_{\rm tr}
\longrightarrow
\rho_S(\Phi_{\rm tr})
\longrightarrow
\widehat{\mathfrak c}_{\rho,20}(\tau\otimes\Phi_{\rm tr})
\longrightarrow
P_0^\dagger K\,\widehat{\mathfrak c}_{\rho,20}Y_KP_0
\]

and separately

\[
p_{\rm tr}
\longrightarrow
\Phi_{\rm tr}
\longrightarrow
\rho_S(\Phi_{\rm tr})
\longrightarrow
\widehat{\mathfrak c}_{\rho,20}(\tau\otimes\Phi_{\rm tr})
\longrightarrow
P_0^TC\,\widehat{\mathfrak c}_{\rho,20}Y_CP_0
+\text{reality completion}.
\]

The missing physical object is

\[
\widehat{\mathfrak c}_{\rho,20}
(\tau\otimes\Phi_{\rm tr}).
\]

Its first unresolved factor is an explicit native spinor matrix
\(\rho_S(\Phi_{\rm tr})\), including branching relative to the carried
stabilizer and imported Standard Model subgroup/selector. RB3 does not
solve the repository's separate SM-selector gap. Even with \(P_0=1\), the
lift from the spinor endomorphism to \(E_{20}\) remains missing.
Downstream co-blockers are:

1. native \(P_0\) defect embeddings;
2. \(Y_K/Y_C\) incidence across all twenty slots, especially the \(X\)
   sector;
3. total \(K\)-adjoint versus \(C\)-natural reality completion;
4. the coflip action on \(\rho(\Phi)Y\); and
5. right-\(\mathbb H\) compatibility needed before extending by the P3
   factor.

The existing \(M_3(\mathbb C)\) provenance matrices do not define these
maps and cannot be renamed generation matrices.

The observer-complex computation derives

\[
4+4+8+4+4+8+8+8+20=68
\]

vertical incidences, and the frozen observer schema retains twenty slots and
136 directed incidence cells. That demonstrates pipeline power only. It is
not a fitted physical placement.

The constraint surplus is therefore

```text
SURPLUS-UNCOMPUTABLE-FIRST-rho_S(Phi_trace)
```

It must later be computed from matrix ranks after quotienting gauge,
normalization, field-redefinition, and supplied-VEV freedom. Nine prose
requirements are not nine independent constraints.

## 7. Gravity and cosmology interface

N1 already contains the ambient quadratic distortion term

\[
\frac1{2\kappa}\int_Y\kappa_{\mathfrak g}(\theta,*\theta).
\]

If the source \(T_\omega\), repository vertical coefficient, and the trace
of \(\theta\) are proved to be the same object, this term supplies an
ambient quadratic response. That Layer-0 identification and the map into
the four-dimensional section Euler equation are still unbuilt.

There are two useful controls:

- for semisimple full \(G\),
  \(\operatorname{Hom}_G(\operatorname{ad},\mathbf1)=0\), so a nontrivial
  adjoint coefficient has no full-gauge-invariant **linear** cosmological
  readout;
- on the covariantly constant decomposable trace-only stratum
  \(a=\tau\otimes\Phi\), \(a\wedge a=0\), so ambient Yang--Mills alone
  supplies no Mexican-hat quartic on that one-mode control.

Neither statement kills quadratic invariants, background-curvature
couplings, multimode connections, soldered terms, or an explicitly written
potential.

## 8. Moving bridge discriminator formula and proxy

The two RB2 actions differ by

\[
\Delta S
=S_{\rm total}-S_{\rm JD}
=-\widehat J_F[\theta].
\]

Along a moving-soldering tangent \(X\),

\[
(\Delta E_\epsilon)[X]
=
\widehat J_F[\delta_\epsilon\Gamma[X]]
-
(\mathrm d_{\mathcal F,\epsilon}\widehat J_F[X])[\theta].
\]

The second term is the moving-current/projector response missing from the
fixed-geometry slice. For the literal \(Q_F\), it must include the
corresponding \(P_R,V_b,K_E\), density, bulk, and boundary responses.

The executable homogeneous matrix proxy uses
\(\Gamma(t)=g(t)\Gamma_0g(t)^{-1}\) and an anticommutator current. It checks
the chain-rule sign, detects a frozen-current response, and obtains:

```text
analytic  -0.0372917
finite    -0.0372917
```

The same fixture with the odd field set to zero vanishes. The nonzero value
proves this proxy polynomial is not identically zero. It is not the
\(A_0\)-induced connection and does not execute literal \(Q_F\), moving
\(P_R\), density, or Green terms. It is a candidate discriminator, not a
selection or a complete moving Euler equation.

## 9. Five-leg and datum ledger

| leg | RB3 disposition |
| --- | --- |
| Standard Model / Yukawa | trace coordinate constructed; physical insertion missing; first unresolved factor is explicit \(\rho_S(\Phi_{\rm tr})\), relative to carried/imported SM subgroup |
| quantum / Krein / BV | \(K,C_+,C_-\) remain separate; \(C_-\) moves or reduces symmetry; native Ward/CME held |
| gravity / dark energy | ambient \(\theta^2\) response carried conditionally; four-dimensional cosmological map unbuilt |
| index / count | P3 stays external; eventual placement must be right-\(\mathbb H\)-linear; no readout |
| UV / causality | principal Clifford symbol conjugate/carried; moving subprincipal and domain untested |

The datum ledger remains:

\[
\text{one P1/P2 orientation line}
\quad+\quad
\text{external P3 relative-}KO\text{ datum}.
\]

No VEV was supplied. A future supplied VEV must be charged by the dimension
of its orbit/moduli. A dynamically selected VEV is not a fit parameter, but
it requires the completed Euler equation.

## 10. Next dependency-correct swing

RB3 is split:

- moving geometry is locally constructed and can feed the later moving
  defect calculus;
- the shared physical spin-zero placement has not earned RB3-go.

The next main construction should therefore remain at the RB3 placement
boundary:

1. construct explicit native \(\rho_S(\Phi_{\rm tr})\);
2. build its lift into
   \(\widehat{\mathfrak c}_{\rho,20}(\tau\otimes\Phi_{\rm tr})\);
3. branch it under the explicit stabilizer and carried/imported Standard
   Model subgroup/selector;
4. place it through native \(P_0\), all twenty provenance/\(X\) slots, and
   separate \(Y_K/Y_C\) reality spaces;
5. test right-\(\mathbb H\), P1/P2 coflip, and the ambient-to-section
   cosmology map; and
6. join literal moving \(Q_F/P_R\) to a selected connection branch and
   construct its Green form;
7. only then compute constraint surplus and decide whether RB4 may consume
   the placement.

The parallel source-action track is recorded separately. Its failed
full-\(\operatorname{Spin}(9,5)\), same-\(\Lambda^2\) Ricci--Einstein route
does not kill either N1 bridge.

## Reproduction and nonclaims

Run:

```bash
python3 tests/channel-swings/rb3_moving_soldering_spinzero_probe.py
python3 tests/channel-swings/rb1_source_repo_current_musical_probe.py
python3 tests/channel-swings/rb2_source_action_exactness_probe.py
```

This result claims no global orbit bundle for an arbitrary \(G\)-bundle,
complete native Ward identity, Diff closure, nonlinear CME, physical
domain, positivity rule, stationary solution, VEV, mass, cosmological
constant, anomaly, P3 pushforward, index, or generation count.
