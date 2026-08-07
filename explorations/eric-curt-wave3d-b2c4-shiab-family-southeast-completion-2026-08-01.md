---
title: "Eric/Curt Wave 3D-B2C4: Shiab-family selector and southeast completion"
status: active_research
doc_type: construction_result
created: 2026-08-01
lane: "1"
work_item: ECW3D-B2C4-SHIAB-FAMILY-BIANCHI-ADJOINT-AND-CONSTRAINT-SELECTOR
registry: lab/process/eric-curt-wave3d-b2c4-shiab-family-southeast-completion.json
probe: tests/channel-swings/eric_curt_wave3d_b2c4_shiab_family_southeast_completion_probe.py
grade: "EXACT active-Cl(9,5) principal-symbol construction. A correctly typed two-sided/Ward plus native-Krein filter removes the contract Shiab channel and leaves two real chiral wedge weights. The displayed zero-southeast rolled matrix still has the rank-128 square-zero Jordan obstruction, but the source explicitly admits nonzero southeast versions. In the frozen unit-K/unit-C normalization, the complete spatial Clifford identities leave a two-real-parameter nonzero family with 12 w_plus ell_minus+11=12 w_minus ell_plus+11=0. The four sign choices form only a normalized slice. Every tested survivor is time-noncharacteristic, semisimple, positive-right-H symmetrizable, and retains all physical nu and raw observation without quotient. The source does not select this spinorial Ward condition, reciprocal 11/12 invariant, or normalization; covariant action, Green, domain, and physical recovery remain open."
claim_status_change: false
canon_change: false
public_posture_change: false
---

# Wave 3D-B2C4 — Shiab-family selector and southeast completion

## Plain-English result

This swing found a real construction, not another way of restating the
obstruction.

The prior source-shaped matrix failed because its chosen Shiab block and its
zero lower-right corner left a rank-128 Jordan defect. This swing opened both
choices the manuscript itself leaves open:

1. the full natural Shiab family; and
2. the explicitly admitted possibility that the southeast block is nonzero.

Two independent pre-PDE conditions select the same Shiab channel. The pure
grade-three wedge/Rarita--Schwinger channel is divergence-free at principal
symbol and self-adjoint for the active Krein form. The grade-one contract
channel is neither. This removes the two contract coefficients but still
leaves one real wedge weight on each chirality.

The wedge choice alone does **not** cure the PDE. With the southeast block
kept at zero, the same rank-128 square-zero Jordan part remains.

The smallest first-order southeast class then gives a sharp completion. In
the frozen normalization of the source's `d` and `d*` blocks, exact spatial
Clifford relations force

\[
w_+w_-\ne0,
\qquad
12w_+\ell_-+11=0,
\qquad
12w_-\ell_++11=0.
\]

Thus

\[
\boxed{\ell_+=-\frac{11}{12w_-},\qquad
       \ell_-=-\frac{11}{12w_+}.}
\]

This leaves a two-real-parameter nonzero family. The four sign choices are a
normalized slice, not the complete solution. Every tested unequal and
normalized witness has an invertible time symbol, exact real semisimple
light-cone propagation, a positive right-`H` symmetrizer, all 128 physical
zero-form spinors, and all 640 raw observed components. Nothing is
quotiented.

This is the first source-guided alternative in this sequence that repairs the
full physical rolled symbol rather than deleting the bad modes.

The honest boundary is equally important: the draft permits a nonzero
southeast block but does not give this coefficient, and its missing historical
Bianchi calculation was bosonic. The wedge selector and reciprocal `11/12`
completion relation are repo constructions. The next wave must derive them
and select or explain their continuous normalization from the covariant
action, not merely from the desired principal-symbol identities.

## 1. What was frozen before PDE inspection

The active geometry is the trace-reversed Frobenius-fibre port

\[
(3,1)+(6,4)=(9,5),
\qquad
\mathrm{Cl}(9,5)=M(64,\mathbb H).
\]

Let

\[
K(k)=k\otimes 1,
\qquad
C_g(k)=\iota_{k^\sharp},
\qquad
C_g(k)K(k)=q(k)1.
\]

The repo's complete right-`H` natural spinorial Shiab family has coordinates

\[
(c_+,w_+,c_-,w_-)\in\mathbb R^4
\]

in the chiral contract/wedge basis. Composing with the exterior symbol gives

\[
A_c(k)=K(k)\Gamma-1\otimes c(k)
\]

and

\[
(A_w(k)\zeta)_a
=\eta_{aa}\,c(e_a\wedge k\wedge e_v)\zeta_v.
\]

No characteristic projector, Jordan eigenspace, external datum, southeast
coefficient, or positive metric was used to define these maps.

## 2. The Shiab-family result

Both natural channels obey

\[
A_c(k)K(k)=A_w(k)K(k)=0.
\]

This is only `k wedge k=0`; it does not select a channel and is not an
off-shell BV identity for the complete physical operator.

The discriminating left compositions are

\[
C_g(k)A_c(k)=q(k)\Gamma-c(k)C_g(k)\ne0
\]

and

\[
\boxed{C_g(k)A_w(k)=0.}
\]

The second identity is total antisymmetry:

\[
k^a\gamma_{abc}k^b\zeta^c=0.
\]

It selects the wedge line in each chiral block. Independently, with

\[
\beta=e_0e_1\cdots e_8,
\qquad
H_1=\eta\otimes\beta,
\]

the wedge channel is Krein-self-adjoint and the contract channel is not. The
two filters therefore agree:

\[
c_+=c_-=0,
\qquad
(w_+,w_-)\in\mathbb R^2.
\]

They do not tie the two chiral weights. Right-`H` preserves each chirality,
and the Krein form pairs opposite chiralities in exactly the way that makes
each odd wedge block separately self-adjoint. A chiral tie must come from the
action, charge-conjugation convention, or another independently typed rule.

### Layer-0 warning about “Bianchi”

The manuscript's unavailable historical Bianchi selector concerns the
bosonic adjoint-valued Shiab family. The present identity is a spinorial
principal-symbol divergence/Ward analogue. It is mathematically natural and
source-motivated, but it is not recovered authorial proof.

## 3. Why the zero-southeast version still fails

For

\[
D_0(k)=
\begin{pmatrix}
A_w(k)&K(k)\\
C_g(k)&0
\end{pmatrix},
\]

the continuous Lorentz time remains noncharacteristic when both chiral wedge
weights are nonzero. Nevertheless, for a unit section-spatial covector,

\[
N_\xi=E_\xi^2-1,
\qquad
\operatorname{rank}N_\xi=128,
\qquad
N_\xi^2=0,
\qquad
N_\xi\ne0.
\]

So changing the Shiab channel alone does not solve B2C3. The source-displayed
zero southeast corner remains weakly, not strongly, hyperbolic.

A one-sided chiral wedge is worse: its time symbol has nullity `832`. Both
chiral blocks are required before a one-time section evolution exists.

## 4. The rational southeast completion

The draft immediately notes that other versions can have a nonzero southeast
block. Freeze the smallest active-real first-order class

\[
L(k)=c(k)(\ell_+P_++\ell_-P_-)
\]

and the complete rolled symbol

\[
D(k)=
\begin{pmatrix}
A_w(k)(w_+P_++w_-P_-)&K(k)\\
C_g(k)&L(k)
\end{pmatrix}.
\]

Requiring the three admitted spatial evolution matrices to form a Clifford
triple,

\[
E_i^2=1,
\qquad
E_iE_j+E_jE_i=0\quad(i\ne j),
\]

gives the necessary and sufficient relations

\[
w_+w_-\ne0,
\qquad
\ell_+=-\frac{11}{12w_-},
\qquad
\ell_-=-\frac{11}{12w_+}.
\]

The necessity is not an interpolation from the tested points. In one chiral
sector, let `w` be the wedge weight and `ell` the southeast weight. Exact
Clifford reduction gives

\[
D(dt)\text{ invertible}\iff w\ne0,
\]

\[
E_x^2-1
=\left(\ell+\frac{11}{12w}\right)N_x(w),
\qquad
N_x(w)\ne0,
\qquad
N_x(w)^2=0.
\]

Thus semisimplicity forces and is forced by `12 w ell+11=0`. The full chiral
pencil splits into the pairs `(zeta+,nu-)` with `(w+,ell-)` and
`(zeta-,nu+)` with `(w-,ell+)`, producing the two crossed equations above.
The same reduction for any unit spatial covector gives `E(xi)^2=1`; spatial
polarization then gives the cross anticommutators.

The solution is a two-real-parameter nonzero family. Three unequal-weight
witnesses `(1,2)`, `(-2,3)`, and `(0.5,0.75)` pass the complete matrix gate.
The four normalized sign witnesses are

| `w+` | `w-` | `ell+` | `ell-` | branch |
| ---: | ---: | ---: | ---: | --- |
| `+1` | `+1` | `-11/12` | `-11/12` | tied |
| `-1` | `-1` | `+11/12` | `+11/12` | overall-sign partner |
| `+1` | `-1` | `+11/12` | `-11/12` | coflip |
| `-1` | `+1` | `-11/12` | `+11/12` | overall-sign partner |

A unit-`K`/unit-`C_g` chiral similarity rescales `w+` and `w-` inversely, so
the product `p=w+w-` remains invariant. On the normalized sign slice,
simultaneous sign reversal pairs the two tied signs and the two coflip signs.
For the fixed source action, however, arbitrary magnitudes have not been
proved equivalent: the continuous normalization and the sign of `p` remain
action burdens, not yet an external datum.

For the tied representative,

\[
\boxed{
D_{\rm tie}(k)=
\begin{pmatrix}
A_w(k)&K(k)\\
C_g(k)&-\frac{11}{12}c(k)
\end{pmatrix}.}
\]

The nearby planted value `10/12` fails `E_y^2=1` with defect `1/12`. Thus the
rational coefficient is not a broad numerical basin.

## 5. PDE and observation result

Every normalized and unequal-weight witness tested satisfies, to the exact
matrix-representation tolerance,

\[
E_i^2=1,
\qquad
\{E_i,E_j\}=0.
\]

Therefore for every section-spatial covector

\[
E(\xi)^2=|\xi|^2 1.
\]

The characteristic roots are real and semisimple. On the unit sphere,

\[
H(\xi)=1+E(\xi)^\dagger E(\xi)
\]

is positive and obeys

\[
H(\xi)E(\xi)=E(\xi)^\dagger H(\xi).
\]

It is also right-`H` compatible. Coordinate and normalized `(1,2,3)`
directions give the same bounds

\[
1.0294976\lesssim H(\xi)\lesssim34.901058.
\]

This positive majorant is a derived PDE symmetrizer, not the native indefinite
Krein form.

No quotient or constraint restriction is used. The raw observation map
retains rank `640 = 4*128 + 128`, and the physical `nu` projection retains
rank 128.

## 6. Three specialist lenses, kept separate

### Affine/cohomological lens

The wedge channel is the unique projective member of the natural family that
produces the two-sided symbol sequence

\[
S\xrightarrow{K}T^*Y\otimes S
\xrightarrow{A_w}T^*Y\otimes S
\xrightarrow{C_g}S.
\]

This is a Ward-admissible RS symbol. It becomes gauge/BV only if a distinct
ghost and a covariant action-derived Noether identity are built.

### Krein/PDE lens

The two-sided wedge with zero southeast still fails. The rational southeast
completion instead gives a full Clifford evolution, an explicit positive
right-`H` symmetrizer, and no initial-data quotient. This is the highest-value
route because it repairs dynamics while retaining source-labeled matter.

### Axiom/source lens

The source confirms the family, the rolled matrix, and that nonzero southeast
versions exist. It only intends Bianchi/orbit-perpendicular action
compatibility; it does not supply the spinorial selector, active `(9,5)`
adjoint theorem, chiral tie, reciprocal `11/12` relation, or normalization.
The physical formal-adjoint test must
ultimately include Hodge/density, Grassmann/charge conjugation, lower-order
terms, Green flux, and domain—not only this principal matrix.

## 7. Source collision

| source locator | disposition | consequence |
| --- | --- | --- |
| 2021 draft Section 8.1--8.2, PDF pp. 41--43 | `SOURCE-CONFIRMS` a Shiab family and historical Bianchi/highest-weight selection intent; calculation unavailable | family search is required; no unique author-selected member |
| 2021 draft equations 9.16--9.18, PDF pp. 48--49 | `SOURCE-CONFIRMS` the physical `Omega1(S)+Omega0(S)` rolled matrix | `zeta` and `nu` remain physical fields |
| draft note following 9.16 | `SOURCE-CORRECTS` the claim that every version has a zero southeast block | a nonzero southeast rival is source-admitted |
| spinorial `C_g A_w=0`, active Krein selector, reciprocal `11/12` relation, normalization, and PDE completion | `SOURCE-SILENT` | repo-derived construction, not attributed to Weinstein |

This decisive result therefore passes the Eric-lane source-collision gate
without turning source silence into evidence.

## 8. Layer 0 and seven-axis boundary

| shared phrase | object here | must not be identified with |
| --- | --- | --- |
| Bianchi selector | unavailable bosonic source calculation | spinorial `C_g A_w=0` proved here |
| Ward identity | principal two-sided symbol closure | covariant nonlinear Noether identity |
| wedge/RS channel | pure grade-three natural map | gamma-traceless `wedge-6 contract` selector |
| southeast block | first-order zero-form endomorphism | author-selected mass/Yukawa block |
| formal adjoint | active principal Krein symmetry | final density/Hodge/Green/domain adjoint |
| `nu` | physical zero-form spinor | gauge parameter or ghost |
| positive symmetrizer | derived one-time PDE majorant | native Krein form or quantum Hilbert space |
| coefficient family | continuous reciprocal family; normalized tied/coflip slice | P1 or an author-selected normalization |
| generation | observed chiral/index object | four coefficient witnesses or chiral blocks |

| axis | result |
| --- | --- |
| L1 algebra | full right-`H` contract/wedge family filtered; four rational southeast witnesses |
| L2 representation | both chiral wedge blocks required; continuous product/normalization and normalized tied/coflip sign remain |
| L3 geometry | active trace-reversed `(9,5)` explicit; draft `(7,7)` not identified |
| L4 dynamics | exact semisimple light-cone principal evolution and positive symmetrizer |
| L5 observation | raw rank 640 and physical `nu` rank 128 retained without quotient |
| L6 physics | physical carrier/action candidate only; covariant EL/Green/Noether/SM recovery open |
| L7 empirical | no mass, index, generation count, or prediction claimed |

## 9. External datum and non-regression

- P1/P2/P3 were not used and are not repriced.
- The continuous normalization and normalized tied/coflip sign are not P1.
  An orientation reading requires patch transport proving that reversal
  exchanges the sign branches, after the action fixes or quotients magnitude.
- P3 remains a later Fredholm/index twist and does not select the reciprocal
  `11/12` relation or a normalization.
- B2B remains a correct no-positive-symmetrizer result for isolated W131.
- B2C1's carrier-erasing quotient remains killed.
- B2C2A/B guided super-IG/RS differential work remains a separate route.
- B2C3 remains correct for the contract and zero-southeast candidates.
- The B2C2 full-Clifford completion remains a mathematical control.
- Curt's literal `(7,7)` pairing/domain/action port remains separate;
  `TG-1 AND TG-2 AND TG-3` is still false.
- No canon, claim status, public posture, Lane control, scheduler, or
  publication state changes.

The executable probe passes `36 exact + 13 planted = 49` checks.

## 10. Next gate

`ECW3D-B2C5-COVARIANT-SOUTHEAST-ACTION-AND-GREEN-WARD-CLOSURE`

1. Write the complete covariant fermion action with `A_w`, `K`, `C_g`, the
   southeast class, Hodge/density conversion, barred fields, Krein pairing,
   Grassmann signs, and charge-conjugation reality.
2. Vary it term by term. Require the Euler operator itself to select the
   wedge channel, reciprocal `11/12` relation, and any physical normalization;
   otherwise price the surviving continuous coefficient family as an action
   parameter rather than a derivation.
3. Covariantize `AK=0`, `C_gA=0`, and the Clifford-square identities. Compute
   their curvature, augmented-torsion, and distortion remainders exactly.
4. Test whether the bosonic Euler residual and Shiab/eddy completion cancel
   those remainders in a genuine coupled Ward identity.
5. Derive the Green current and a closed right-`H` section domain; prove the
   positive symmetrizer is compatible with patch descent and observation.
6. Only after the action and transport are explicit test whether magnitude is
   a field-normalization equivalence and whether the normalized tied/coflip
   sign is exchanged by orientation and can lawfully consume P1.

If the action does not generate the wedge/reciprocal-`11/12` structure and
control its normalization, keep this as an
exact hyperbolic control and return the coefficient debit to the source-action
ledger. If covariant curvature destroys the principal closure without a
bosonic cancellation, the no-quotient ordinary one-time route fails at that
precise coupled-action gate rather than at the earlier isolated W131 no-go.
