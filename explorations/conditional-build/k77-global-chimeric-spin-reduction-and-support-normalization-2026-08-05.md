---
artifact_type: construction_result
created: 2026-08-05
status: K77_GLOBAL_FULL_CHIMERIC_CLIFFORD_REDUCTION_CONSTRUCTED_FROM_ADMITTED_X_SPIN_AND_SOURCE_P_H__SOURCE_GUIDED_INDEPENDENT_X_SUPPORT_HORN_SELECTED_WITH_ZERO_NEW_SUPPORT_PARAMETERS__EXISTING_RELATIVE_ACTION_NORMALIZATION_NONLINEAR_BV_AND_NULL_GREEN_DOMAIN_OPEN
lane: "1"
functional_channels: [BUILD, SOURCE, COMPOSE, VERIFY]
ledger_rows: [LT-GR1b, LT-GR2c, LT-GR2d, LT-SM8]
fork_assumed: SIGNATURE_AMBIENT_K77__ORIENTED_TIME_ORIENTED_LORENTZ_COMPONENT__ADMITTED_X_SPIN_STRUCTURE
search_space_dim: "global reduction has zero new choices after the admitted X spin structure and source epsilon are fixed; source-guided support horn adds zero profile/trivialization parameters; lambda_def remains an unresolved alias fork: existing kappa1/source_norm or one additional real"
free_object_delta: "zero new fields, zero new spin bits, zero new projectors and zero new support profiles in the selected horn"
source_return: SOURCE-CORRECTS
scripts:
  - tests/channel-swings/k77_global_chimeric_spin_reduction_probe.py
  - tests/channel-swings/k77_global_chimeric_spin_reduction_independent.sage
registry: lab/process/k77-global-chimeric-spin-reduction-and-support-normalization.json
---

# K77 global chimeric-spin reduction and support normalization

## Result first

The full global Clifford soldering reduction required by the K77 rank-ten
gravitational receiver is **constructed** on the GU substrate already in the
repository. It does not require a new dynamical field or a second external
datum.

The construction uses exactly the starting data Weinstein names:

1. the active spin structure on the four-manifold (X);
2. the tautological Lorentz metric over (Y=operatorname{Met}_{1,3}(X));
3. the chimeric bundle

   \[
   C=\operatorname{Sym}^2(\pi^*T^*X)\oplus\pi^*T^*X;
   \]
4. the source-defined principal bundle (P_H), which is the unitary/Krein
   spinor-frame extension of (C), not an independent gauge bundle; and
5. source (epsilon), a global gauge transformation/nonlinear sigma field.

The resulting reference Clifford map and its moved family are

\[
 \gamma_0:C\longrightarrow\operatorname{ad}(P_H),
 \qquad
 \boxed{\gamma_\epsilon=\operatorname{Ad}(\epsilon^{-1})\gamma_0}. \tag{1}
\]

Equation (1) is a full labelled fourteen-frame. It is not merely the image
plane. The global split (C=V\oplus H^*) remains attached to its domain, so
the predecessor's vertical projection and rank-ten receiver are globally
typed.

This corrects the prior source return. The primary source is not silent about
ownership: it builds (P_H) from the chimeric spinors, says the adjoint bundle
looks like the Clifford algebra, and explicitly rotates the invariant
(Phi) by (epsilon). What the source does not supply is the characteristic-
class/lift proof below. The decisive return is therefore
`SOURCE-CORRECTS`, not `SOURCE-SILENT`.

The bulk/defect result is narrower. The source-guided nonduplicating support
horn is selected:

\[
 \boxed{S=S_Y^{\rm ED}+S_Y^{\rm YMH}+S_X^{\rm independent}}. \tag{2}
\]

An independently typed (X)-density pushes forward canonically as a current;
it needs no normal-density trivialization or transverse profile. Thus the
selected horn adds **zero new support fields, transverse profiles or
normal-density trivializations**. But covariance does not fix the relative
action/source normalization, and this wave does not yet prove whether that
coefficient is the already-counted `kappa_1`/`source_norm` or one additional
real. Nonlinear BV/CME and the null/Green domain also
remain open. This wave therefore advances `LT-GR2c` without claiming a
physical Einstein equation, dark-energy magnitude or cosmology.

## Plain English

The last wave had built the correct ten-dimensional receiver but had to say,
“this works if the whole fourteen-dimensional Clifford frame exists globally.”
That “if” is now discharged.

The reason is simple once the source documents are put beside the topology.
GU does not first invent an unrelated giant gauge bundle and then hope the
fourteen geometric directions fit inside it. It builds the giant bundle from
the spinors of those fourteen chimeric directions. The Clifford directions
therefore come with the bundle. Weinstein's epsilon field then rotates the
whole labelled frame. The only global precondition is the spin structure on
the original four-manifold, and he explicitly lists that as starting data.

There is still a real action problem. We now know how the geometry talks to
the gravitational receiver everywhere, but a fourteen-dimensional action and
a four-dimensional defect action can still be weighted relative to each
other. The clean construction is to keep one bulk action and add only terms
that are genuinely defined on the observed four-dimensional section. This
does not need a fake transverse thickness. It also does not magically choose
the remaining physical coupling, solve the master equation or establish a
well-posed null evolution.

## 1. Layer 0

| object | object used here | not identified with |
| --- | --- | --- |
| spin of (TY) | a lift for the tangent bundle of the observerse | spin of the chimeric bundle (C) |
| spin of (C) | a lift of the ((7,7)) orthonormal frames of (C) | mere vanishing of (w_2(TY)) |
| admitted spin datum | the active spin structure on (X) named by Weinstein | a new free fibre (mathbb Z/2) selected in this wave |
| induced (C)-spin lift | the lift functorially induced from the supplied (X)-spin structure | every possible spin structure on (C) |
| (P_H) | the source's chimeric-spinor unitary/Krein frame extension | an arbitrary independent (U(64,64)) gauge bundle |
| source (epsilon) | a gauge transformation/nonlinear sigma field | the map (gamma_\epsilon) itself |
| (gamma_\epsilon) | the dependent full Clifford frame (\operatorname{Ad}(\epsilon^{-1})\gamma_0) | an unframed homogeneous-space point |
| selected support | one bulk action plus independently typed (X)-density terms | a localized second copy of the bulk density |
| relative normalization | an existing action/source coefficient | a normal-density profile or new P1/P2/P3 datum |

This separation is load-bearing. Source (epsilon) and `epsilon_IG` were
previously kept distinct for good reason. The resolution is not to rename
them. It is to construct `epsilon_IG` as the dependent map (gamma_\epsilon)
from source (epsilon) and the global reference Clifford map.

## 2. Pre-assessment lenses and kill conditions

| lens | preregistered danger | result |
| --- | --- | --- |
| characteristic classes | (Y)-spin may be substituted for (C)-spin | both are typed; (w_2(C)=\pi^*w_2(TX)) is recomputed directly |
| spin geometry | (w_2=0) may be called a canonical lift | the supplied (X)-spin structure constructs a particular induced lift |
| principal bundles | (P_H) may be treated as independent | the source and draft map define it from chimeric spinors |
| Clifford/Krein algebra | real K77 may silently become quaternionic K95 | exact `Cl(7,7)=M128(R)` and (U(64,64)) complexification are retained |
| equivariance | a moved image plane may be called a soldering frame | equation (1) moves all fourteen labelled inputs |
| stratified action | a same-stratum projector may be used as a density theorem | support horns are ranked independently |
| dimensional engineering | a coordinate `length^10` may be called invariant | the invariant object is the normal-density line |
| variational geometry | support choice may be mistaken for coupling selection | the existing relative coefficient remains free |
| epistemic breadth | the repo may already own the needed global object | the source definition of (P_H) and the canon spin theorem change the gate |

The pass condition was stricter than (w_2(C)=0): construct the particular
lift, identify the actual (P_H), prove grade-one lands in
(operatorname{ad}(P_H)), and transport the full frame. All four pass.

## 3. Characteristic classes of the chimeric bundle

Let (E=\pi^*TX) over the oriented, time-oriented Lorentz component of (Y).
As a real vector bundle,

\[
 C=\operatorname{Sym}^2 E^*\oplus E^*.
\]

Under the splitting principle write the four formal mod-two roots of (E) as
(x_1,\ldots,x_4). The ten roots of (\operatorname{Sym}^2E) are four zero
diagonal roots (2x_i=0) and the six mixed roots (x_i+x_j). Exact expansion
gives

\[
 w_1(\operatorname{Sym}^2E)=w_1(E),\qquad
 w_2(\operatorname{Sym}^2E)=w_1(E)^2. \tag{3}
\]

The Whitney formula then gives, without first assuming orientability,

\[
\begin{aligned}
 w_1(C)
 &=w_1(\operatorname{Sym}^2E)+w_1(E)=0,\\
 w_2(C)
 &=w_1(E)^2+w_2(E)+w_1(E)^2=w_2(E).
\end{aligned} \tag{4}
\]

Thus

\[
 \boxed{w_1(C)=0,\qquad w_2(C)=\pi^*w_2(TX)}. \tag{5}
\]

This agrees with, but is not the same computation as, the canon theorem
(w_2(TY)=\pi^*w_2(TX)). It also prevents an overclaim: (C) is not
unconditionally spin over a non-spin base. It is spin in the GU branch because
an active spin structure on (X) is supplied.

Both the Python F2 polynomial route and an independent Sage polynomial-ring
route certify (3)--(5).

## 4. The induced global Spin(7,7) lift

The pointwise Lorentz metric (g_y) on (E_y) is tautological over (Y).
Restrict the supplied topological spin structure on (X) to the tautological
oriented/time-oriented orthonormal-frame reduction over (Y). This produces
a principal

\[
 \widetilde Q\longrightarrow Y
\]

with structure group (\operatorname{Spin}_0(1,3)).

The Lorentz group acts on
(\operatorname{Sym}^2E^*\oplus E^*) and preserves its chimeric metric. The
trace-reversed Frobenius block has exact inertia ((6,4)); the horizontal dual
block uses ((1,3)). Therefore the representation is

\[
 r_C:SO_0(1,3)\longrightarrow SO_0(7,7). \tag{6}
\]

Because (\operatorname{Spin}_0(1,3)\cong SL(2,\mathbb C)) is simply
connected, (r_C\circ\lambda) has a unique identity-preserving lift

\[
 \widetilde r_C:\operatorname{Spin}_0(1,3)
 \longrightarrow\operatorname{Spin}_0(7,7). \tag{7}
\]

The induced bundle

\[
 P_{\operatorname{Spin}(C)}
 =\widetilde Q\times_{\widetilde r_C}\operatorname{Spin}_0(7,7) \tag{8}
\]

is a global spin structure on (C). It is canonical **relative to the supplied
spin structure on (X)**. The set of all possible spin structures on (C)
may be larger; no claim of absolute uniqueness is made or needed.

## 5. From the spin lift to the actual (P_H)

For split signature,

\[
 \operatorname{Cl}(7,7)\cong M_{128}(\mathbb R).
\]

Let (S_{\mathbb R}) be its faithful real rank-128 module. The exact integer
certificate constructs fourteen signed-permutation gamma matrices and an
invariant symmetric spinor form (B) with

\[
 B^2=1,\qquad \operatorname{tr}B=0,
 \qquad \operatorname{sig}B=(64,64). \tag{9}
\]

Every grade-one matrix is (B)-skew:

\[
 \gamma(c)^TB+B\gamma(c)=0. \tag{10}
\]

Consequently complexification gives

\[
 \gamma(C)\subset\mathfrak{so}(64,64)
 \subset\mathfrak u(64,64). \tag{11}
\]

This is exactly the source real/complex relation. The source first builds the
spinors of (C), then their unitary structure bundle, and later calls that
principal bundle (P_H). In precise associated-bundle notation the relevant
extension is

\[
 P_H=P_{\operatorname{Spin}(C)}
 \times_{\rho_H}U(64,64). \tag{12}
\]

Clifford multiplication is therefore a global bundle map

\[
 \gamma_0:C\longrightarrow\operatorname{ad}(P_H). \tag{13}
\]

If (P_H) had instead been an independent (U(64,64)) bundle, (13) would
require an additional isomorphism or reduction section. That is the correct
negative control, but it is not the source-defined GU object.

## 6. The moved full frame

The source uses

\[
 \epsilon\in\Gamma(\operatorname{Ad}P_H)
\]

both as a nonlinear sigma field and as the gauge transformation that rotates
the Clifford invariant (Phi). Hence (1) is globally defined. For every
(c,d\in C_y),

\[
 \{\gamma_\epsilon(c),\gamma_\epsilon(d)\}
 =\operatorname{Ad}(\epsilon^{-1})\{\gamma_0(c),\gamma_0(d)\}
 =2G_C(c,d)1. \tag{14}
\]

The full domain (C_y), including its labels and (V\oplus H^*) split, is
unchanged. Equation (14) thus supplies a full soldering isometry rather than
only a point of the orbit of fourteen-planes.

An exact integer Spin conjugation independently checks all 196 Clifford
relations after transport, preservation of (B), grade-one (B)-skewness,
and nondegeneracy of all fourteen transported directions.

Combining this with the predecessor yields a global conditional receiver

\[
 \sigma_\epsilon(v_T)
 =\operatorname{pr}_V\pi_1^\epsilon(v_T(g/2)) \tag{15}
\]

of exact rank ten with its already-built adjoint right inverse and orthogonal
projector.

## 7. Support horns and parameter accounting

Along the section (s:X\hookrightarrow Y), density lines satisfy

\[
 \mathcal D_Y|_X\cong\mathcal D_X\otimes\mathcal D_N. \tag{16}
\]

This immediately separates the horns.

| horn | density/support type | added support freedom | disposition |
| --- | --- | ---: | --- |
| one bulk plus independently typed (X) terms | (L_X\in\mathcal D_X), represented upstairs by the canonical current (s_!L_X) | 0 | **selected primary** |
| restrict or duplicate an ambient density | (s^*L_Y\in\mathcal D_X\otimes\mathcal D_N) | at least a section of (\mathcal D_N^*), or a transverse profile | live rival, not source-selected |
| pull back/localize the entire theory to (X) | replaces the source's upstairs (Y) dynamics | support operation plus changed equations | source-incompatible as the primary GU architecture |

For the first horn, (s_!L_X) is defined invariantly by

\[
 \langle s_!L_X,f\rangle=\int_X(f\circ s)L_X. \tag{17}
\]

No normal-frame trivialization, transverse thickness or `length^10` scalar is
needed. The current already carries the inverse normal-density type. This is
why (2) is the minimal nonduplicating support architecture.

The selected horn does **not** fix every coefficient. If

\[
 S=S_Y+\lambda_{\rm def}S_X,
\]

then gauge/diffeomorphism covariance holds for every
(\lambda_{\rm def}). The exact control is elementary:
(lambda_{\rm def}\cdot0=0). The receiver isometry fixes the carrier gain,
not the relative integration weight. The predecessor calls its coefficient
"inherited as unit" on the replacement horn, while the global inventory
separately carries `kappa_1` and an unresolved `source_norm`. No artifact yet
proves these are the same object. The correct accounting is therefore an
alias fork:

```text
lambda_def = existing kappa_1/source_norm
         OR lambda_def = one additional real.
```

The 83-real inventory remains a lower bound during this fork. This wave books
no extra real before the alias is adjudicated, adds one explicit open fork,
and does not describe `lambda_def` as already counted.

## 8. Constraint-surplus accounting

| item | count |
| --- | ---: |
| new spin structures supplied | 0; the active (X)-spin datum is consumed |
| new gauge/soldering fields | 0; (gamma_\epsilon) is dependent on source (epsilon) |
| new Clifford-frame coefficients | 0 |
| new support profiles in selected horn | 0 |
| new support-normalization coefficients | 0 profiles/trivializations; 1 relative-coefficient alias fork |
| global bundle conditions checked | 4: (w_1), (w_2), lift, (P_H) ownership |
| exact fibre conditions checked | Clifford relations, split (B), grade-one adjoint landing, full-frame transport |
| existing relative action coefficient fixed | 0 |

This is positive information even though (lambda_{\rm def}) remains open.
The construction could have failed at (w_2(C)), at the group lift, at
(P_H) ownership or at the Krein adjoint inclusion. It failed at none of
them. The remaining possible parameter is precisely located instead of being hidden
inside “global reduction.”

## 9. Seven-axis disposition

| layer | result |
| --- | --- |
| Layer 0 | (TY)-spin, (C)-spin, induced lift, (P_H), source (epsilon), (gamma_\epsilon), support and coupling are separated |
| L1 substrate | oriented/time-oriented Lorentz component of (Y=\operatorname{Met}(X)), conditional on the admitted (X)-spin structure |
| L2 algebra | exact `Cl(7,7)=M128(R)`, (B)-skew grade one, (U(64,64)) extension and full-frame transport |
| L3 geometry | global induced Spin(7,7) bundle and global (gamma_\epsilon:C\to\operatorname{ad}(P_H)) constructed |
| L4 variation | selected stratified support architecture typed; relative action coefficient still open |
| L5 quotient | predecessor's local non-null rank-16 even-BV quotient retained; no new physical quotient |
| L6 analytic | nonlinear primitive BV, null characteristic and trace-compatible Green domain open |
| L7 physics | no Einstein, dark-energy magnitude, vacuum, observation or cosmology result claimed |

## 10. Source disposition

Decisive return: **`SOURCE-CORRECTS`**.

The correction is local and specific. The earlier source receipt correctly
said the sources do not print the predecessor's rank-ten receiver formula or
its action weld. It went too far in treating the global full reduction as
source-silent. The source does supply the bundle ownership and moving-
Clifford grammar:

- TOE 2025 `00:03:06`: the active spin structure is starting data;
- Portal 2020 `01:12:17--01:13:55`: (C) and its intrinsic metric;
- Portal `01:21:48--01:22:54`: chimeric spinors and their unitary structure
  bundle;
- Portal `01:33:22--01:35:41`: adjoint as Clifford/exterior algebra and
  invariant (Phi_i);
- Portal `01:35:41--01:37:34`: source (epsilon) rotates (Phi) by the
  adjoint action; and
- TOE `02:41:57`: the same chimeric-spinor (U(64,64)) structure.

The characteristic-class and lift argument remains this reconstruction's
mathematical contribution.

## 11. Held-open boundary and next gate

This wave does not establish:

- a source rule fixing the existing relative defect/action normalization;
- the term-by-term nonlinear even BV primitive ledger with all moving
  (epsilon), Shiab, Hodge, density, section and preboundary owners;
- nilpotency or the classical master equation on the actual full field space;
- constraint propagation at null covectors;
- a trace-compatible closed Krein/Green/BFV domain;
- positivity, a physical observation quotient, a vacuum branch, dark-energy
  magnitude or cosmology; or
- use of P1, P2 or P3.

The next gate is

```text
ASSEMBLE_GLOBAL_GAMMA_EPSILON_NONLINEAR_EVEN_BV_PRIMITIVE_OWNER_LEDGER__TEST_EXISTING_SOURCE_NORMALIZATION_ON_LAMBDA_DEF__AND_CONSTRUCT_NULL_TRACE_COMPATIBLE_KREIN_GREEN_DOMAIN
```

First adjudicate whether the existing source normalization fixes
(\lambda_{\rm def}). If it does not, append one real to the inventory rather
than hiding it as a support convention. The null/Green construction then decides
whether the predecessor's non-null rank-16 quotient extends to an admissible
physical domain.
