# N2a/N4a intersection and the finite N3 construction handoff

**Date:** 2026-07-30
**Frozen N1 construction hash:**
`1efdffd34e3ad5358fed16c08cda9ecf681df676e817560bf36b436d79658ffb`
**Executable certificate:**
`tests/channel-swings/n2a_n4a_intersection_probe.py`

## Result first

The two parallel screens turn the next source-action step into a finite
construction problem.

N2a constructs the native bare \(K\Gamma(\alpha_h)\) and
\(C_{\varepsilon,\tau}\Gamma(\alpha_h)\) spinor kernels on the four frozen
actual-\(\operatorname{Sym}^2T^*X\) representatives. The zero representative
is killed. Trace, spacelike-traceless, and null insertions are nonzero. Of
those, only the trace representative preserves all six generators of the
fixed-background Lorentz algebra. This is a screen of bare kernels and
representatives, not yet a verdict on the total N1 bilinear:

\[
\begin{aligned}
\mathcal M_K
&=
P_0^\dagger
\bigl[K\,\mathfrak c_\rho(v[\Phi])\,Y_K\bigr]P_0,\\
\mathcal M_C
&=
P_0^T
\bigl[C_{\varepsilon,\tau}\,
      \mathfrak c_\rho(v[\Phi])\,Y_C\bigr]P_0.
\end{aligned}
\]

Those are different Layer-0 objects. The first is sesquilinear and uses the
Krein pairing; the second is complex bilinear and uses Grassmann transpose.
Their full \(P_0\), gauge/provenance, reality-completion, and 20-slot
placement maps are the first two N3 discriminators.

N4a computes the ordinary Levi--Civita contribution to the
gamma-traceless physical-\(R\) curvature defect, under
\(\nabla\Gamma=\nabla P_R=0\):

\[
\mathcal C^{LC}_{RR}
=
\frac12 P_R\!\left(\operatorname{Ric}^{0}_{bd}\gamma^d\right).
\]

The scalar-curvature and Weyl components are annihilated exactly; only
traceless Ricci survives. The previous W177 qualitative nonzero/full-rank obstruction
survives, while its mixed-raised/lowered-gamma norm is superseded by the
corrected value \(15.66992510\). The separately constructed
\(\rho(P_{\rm IG})\) matrix is only a pointwise Spin-compatible witness.
Full \(\operatorname{Sp}(32,32;\mathbb H)\) covariance remains unproved
until the vector/soldering action, gamma action, and \(P_R\) are explicitly
intertwined.

The useful intersection is:

> The only nonzero fully Lorentz-preserving representative in the N2a
> four-stratum screen is trace-type, whereas the N4a Levi--Civita obstruction
> is traceless-Ricci-type. They are not one direct algebraic channel.

This is not a contradiction and does not kill the trace branch. The trace
branch can still participate in a coupled equation producing traceless Ricci
through derivatives, fermion stress, the trace-free second fundamental form,
IG curvature, or the coupled source equations. It means N3 must calculate
those maps rather than identify the two representations by name or dimension.

No new source coefficient or external-datum freedom was added. The P1/P2/P3
packet remains held fixed, and its index/count value remains held out.

## Layer 0

| shared term | object used here | object not identified with it |
| --- | --- | --- |
| \(K\) bilinear | \(P_0^\dagger K\mathfrak c_\rho(v[\Phi])Y_KP_0\), sesquilinear | \(P_0^TC\mathfrak c_\rho(v[\Phi])Y_CP_0\) |
| \(C\) bilinear | complex-bilinear odd-field kernel with Grassmann transpose and a reality completion | a Krein expectation value or a physical mass |
| trace orbit | scalar line in the actual \(\operatorname{Sym}^2T^*X\) fibre screen | \(\operatorname{Ric}^0\in\operatorname{Sym}^2_0T^*X\) |
| LC defect | \(P_R(\operatorname{Ric}^0_{bd}\gamma^d)/2\) under metric/Clifford compatibility | scalar curvature, Weyl curvature, or an arbitrary endomorphism-valued two-form |
| IG witness | pointwise Spin-compatible \(\rho(P_{\rm IG})\) matrix with the same matrix source/target | a proved full-\(\operatorname{Sp}\)-equivariant Hom arrow, \(F_A\), or \(\Omega^{IG}\) |
| BV incidence | 36 typed, 712 rejected, and 362 map-deferred word-shape statuses in the supplied partial incidence graph | an equivariant Hom rank, EOM factorization, or CME solution |
| count | no count object is computed in this wave | Clifford rank, orbit number, block multiplicity, or generation number |

The trace/traceless firewall is exact:

\[
\pi_0(\lambda g)=0,
\qquad
\operatorname{tr}_g(\operatorname{Ric}^0)=0.
\]

It blocks a direct algebraic identification only. It does not block a
differential or equation-mediated coupling.

## Six N3 discriminator emissions

The joint N2a/N3/N4 handoff should produce six discriminator outputs in
dependency order. Items 1--2 are completed kernel inputs, items 3--5 are
Euler derivatives, and item 6 is derived from them; none is introduced as a
new field.

### 1. Total Krein kernel

\[
\mathcal M_K
=P_0^\dagger K\mathfrak c_\rho(v[\Phi])Y_KP_0.
\]

Supply its sesquilinear reality rule, exact gauge/provenance action, and
20-slot incidence. This decides whether the N2a bare \(K\)-branch reaches the
restricted source action.

### 2. Total charge-conjugation kernel

\[
\mathcal M_C
=P_0^TC_{\varepsilon,\tau}
  \mathfrak c_\rho(v[\Phi])Y_CP_0.
\]

Supply its Grassmann transpose, real-action completion, exact
gauge/provenance action, and 20-slot incidence. This decides the complete odd
kernel without importing the \(K\)-branch answer.

### 3. Fermion and vertical-connection Euler maps

\[
\bigl(\mathcal E_Z,\,
      \operatorname{res}^{(V,!)}_s\mathcal E_A^{V}\bigr).
\]

Include both the Yukawa current and the dual of the section-induced vertical
current. This is where the Standard-Model/Yukawa and Krein/BV legs first meet
the geometric source equation.

### 4. Section equation with trace split

\[
\mathcal E_s
=
\bigl(\operatorname{tr}_g\mathcal E_s,\,
      \mathcal E_s^0\bigr).
\]

Vary \(s_!\), not only the pulled-back coefficients, and include the induced
\(|II|^2\) terms. This computes whether the surviving trace orbit can
dynamically source the traceless-Ricci equation rather than pretending they
are the same representation.

### 5. IG parent and compatibility equations

\[
\bigl(
\mathcal E_{P_{\rm IG}},
\mathcal E_U,
\mathcal E_A^{IG},
\mathcal E_{\epsilon_{\rm IG}}
\bigr),
\]

together with

\[
[\nabla_A,\Gamma],\qquad
[\nabla_A,P_R],
\]

and the soldering/vector-equivariance residual. Keep
\(\Omega^{IG}\), \(F_A\), and \(P_{\rm IG}\) distinct. This either builds the
full-\(\operatorname{Sp}\)-covariant IG arrow or restricts the construction
honestly to the proved Spin-compatible stratum.

### 6. Physical-\(R\) Noether defect

\[
\Delta_R
=
P_R\,\mathcal H_{\rm packet}\,R_r\gamma,
\]

split into:

\[
\Delta_R^{LC,\operatorname{Ric}^0}
+\Delta_R^{IG}
+\Delta_R^{\rm compat}
+\Delta_R^{\rm source}.
\]

Only after this split exists should N4b ask whether
\(\Delta_R=M_R{}^a\mathcal E_a\) in the actual native-real-form Hom quotient.
If it factors, the frozen open-BV grammar can fix a correction coefficient.
If it does not, the finite residual eliminates only the tested
source/background stratum.

## One campaign carry-through

The index/causality leg is not a seventh minimal discriminator for N2b/N4b.
It is a mandatory campaign carry:

\[
\sigma_{\rm principal/subprincipal}
\otimes \nu^*\widehat e_n .
\]

N3 must transport that twisted characteristic input with the packet so that
the source-action construction cannot later solve its local equations by
silently discarding P3 or changing the ultraviolet symbol. It is not yet an
index pushforward and no integer is read from it.

## Five-leg constraint ledger

| leg | construction now emitted | next falsifiable question |
| --- | --- | --- |
| Y — Standard Model/Yukawa | separate total \(K\) and \(C\) kernels; Yukawa contribution to \(\mathcal E_Z,\mathcal E_A^V\) | does either complete restricted kernel survive with the required channel and reality? |
| Q — Krein/BV | pairing-aware kernels, parent/connection Euler maps, and finite frozen grammar | does the full Noether defect factor through the N3 Euler ideal in the exact equivariant Hom space? |
| G — gravity/dark energy | exact LC \(\operatorname{Ric}^0/2\) map and trace/trace-free section split | do source stationarity and IG terms select an Einstein-compatible locus without a fitted free coefficient? |
| I — index/count | P3 twist carried with the principal/subprincipal packet | does a later proved domain and pushforward produce the held-out class without target coding? |
| U — UV/causality | compatibility residuals and unchanged principal symbol carried explicitly | does the completed source solution preserve hyperbolicity/Fredholm admissibility on its actual domain? |

The same candidate must answer all five rows. A locally successful Yukawa or
gravity term may not be retained by dropping the index twist, changing the
Krein pairing, or replacing the native principal symbol.

## Scoped kills, survives, and nonclaims

Killed in this wave:

- zero as a nontrivial vertical insertion;
- direct identification of the Lorentz trace orbit with the LC
  traceless-Ricci obstruction;
- scalar-curvature or Weyl-curvature attribution of the compatible LC
  physical-\(R\) obstruction;
- treating the pointwise Spin \(P_{\rm IG}\) witness as already
  full-\(\operatorname{Sp}\)-covariant;
- collapsing the \(K\) and \(C\) total kernels into one transpose formula;
- reporting the grammar ceiling or partial incidence counts as an open-BV
  Hom rank; and
- treating the twisted characteristic carry as a computed count.

Surviving conditional construction routes:

- the Lorentz-preserving trace branch through the complete \(K\) or \(C\)
  restricted kernel;
- a differential trace-to-\(\operatorname{Ric}^0\) source map generated by
  the section Euler equation;
- a source-selected Einstein locus;
- a fully intertwined IG cancellation/factorization channel;
- a finite open-BV correction whose coefficient is forced by exact
  N3-EOM factorization; and
- the unchanged P3-twisted analytic route once a global domain exists.

This handoff does **not** claim N2a `GO`, an N4b EOM factor, a physical mass,
a stationary source, a CME solution, a global domain, an index, or a
generation count.

## Efficient next sequence

1. Build the two total kernels in parallel but never identify their reality
   structures.
2. Differentiate the written N1 action once to obtain
   \(\mathcal E_Z\), \(\mathcal E_A^V\), and the trace/trace-free
   \(\mathcal E_s\).
3. Build or restrict the IG carrier by solving the gamma, projector, and
   soldering intertwining equations.
4. Assemble the four-piece \(\Delta_R\) and compute its exact EOM-jet
   quotient.
5. Run N2b on the complete kernels and N4b on that quotient.
6. Carry the unchanged P3-twisted symbol throughout; defer its numerical
   pushforward until the global domain is constructed.

That sequence extracts the maximum shared information from each variation:
the same Euler maps decide the bilinear survival question, the gravity/IG
obstruction, the allowable BV correction, and whether the source action
preserves the held-out index/causality route.
