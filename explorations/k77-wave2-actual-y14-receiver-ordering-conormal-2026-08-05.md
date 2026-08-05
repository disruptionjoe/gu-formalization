---
title: "K77 Wave 2: actual-Y14 receiver ordering and conormal obstruction"
date: 2026-08-05
lane: 1
status: PARTIAL_WITH_NAMED_MOVEMENT
named_gate: K77_ACTUAL_Y14_EULER_RECEIVER_FAITHFUL_MODULE_AND_COMMON_GREEN_DOMAIN
fork_assumed: SIGNATURE-AMBIENT
fork_horn: K77
search_space_dim: "0 selector parameters in the ordinary section-pullback class; direct degree map and primalize-then-restrict map fixed"
free_object_delta: 0
residue_touched: "K77-W2-ACTUAL-Y14-RECEIVER:T3"
fork_stack_acknowledged: "This wave instantiates the prior receiver theorem on a local K77 Met(X) graph using the trace-reversed fibre metric. It adds no signature selector, preserves the K95 carrier/primalizer/transition re-port cost, and does not treat Eric/Curt guidance as an identity theorem."
probe: tests/channel-swings/k77_wave2_actual_y14_receiver_ordering_probe.py
registry: lab/process/k77-wave2-actual-y14-receiver-ordering-conormal.json
grade: "Exact local fibrewise theorem. Direct pullback of the density-dual 13-form Euler row to X4 is zero; primalize-then-restrict has rank four and a complete rank-ten conormal kernel. A metric horizontal right inverse exists for a nondegenerate section graph, but faithfulness requires the actual source-action Euler image to lie in it, a genuine defect/density reduction varied on X, or a typed ten-component normal receiver. None of those complete receivers or a common analytic Green domain is yet built."
---

# K77 Wave 2 actual-Y14 receiver ordering and conormal obstruction

## Result in one paragraph

The previous abstract observation theorem is now instantiated far enough on
`Y=Met(X)` to expose the real receiver fork.  The source translation equation
is a 13-form density dual on fourteen dimensions.  Pulling that form directly
to a four-dimensional section gives zero identically.  If it is first
primalized by the K77 Hodge/Krein map to an upstairs connection one-form, then
restricted to the section, the receiver has rank four and an unavoidable
rank-ten conormal kernel.  The trace-reversed metric supplies a canonical
horizontal right inverse at every nondegenerate section graph, but the action
must still prove that its Euler image lies in that horizontal subspace.  Within
this ordinary post-primalization receiver class, the other honest option is to
retain ten normal equation components.  A third theory-level route already
exists in the prior build: localize or reduce the **action** by a genuine
codimension-ten defect/density operation and vary that reduced action.  This
is not a GU kill: it converts “actual receiver” into three precise construction
routes rather than allowing a dimensionally impossible pullback.

## 1. Why this gate ran

The predecessor proved that observed nilpotence detects the upstairs action
Euler row only modulo

\[
\ker(\rho_X\,\sharp_X\,O_E).
\]

It deliberately left `O_E` abstract.  Instantiating it as a section operation
immediately raises a degree question that must precede every rank or Ward
calculation:

> Is the observed object the pullback of the 13-form Euler residual, or the
> pullback of the one-form obtained after Hodge/Krein primalization?

Those operations are not interchangeable.

## 2. Pre-wave accounting

- `fork_assumed: SIGNATURE-AMBIENT`, horn `(7,7)`.
- The mostly-minus Lorentz convention gives horizontal inertia `(1,3)`; the
  trace-reversed symmetric-metric fibre has inertia `(6,4)`; their adapted
  sum has inertia `(7,7)`.
- `search_space_dim: 0 selector parameters`.  Ordinary pullback and the
  inherited invertible primalizer are fixed classes, so the entire kernel is
  computed rather than searching projectors.
- `free_object_delta: 0`.  No normal constraint, receiver, connection or datum
  is admitted.
- `residue_touched: K77-W2-ACTUAL-Y14-RECEIVER:T2` at opening.

The open fork stack remains explicit: transferring a signature-sensitive
metric/primalizer statement to K95 requires a carrier, primalizer and
transition re-port.  The degree and rank bounds themselves do not depend on
the signature horn.

## 3. Layer 0: four different operations

| operation | degree/result | disposition |
| --- | --- | --- |
| `s*:Omega13(Y)->Omega13(X)` | zero because `dim X=4` | exact, not the physical receiver |
| `Omega13(Y,E*) --R_Y--> Omega1(Y,E) --s*--> Omega1(X,s*E)` | potentially nonzero | live receiver candidate |
| `pi_!:Omega13(Y)->Omega3(X)` for ten-dimensional fibres | degree three | different object; support/normalization also required |
| horizontal plus normal coefficient decoder | four tangent plus ten normal components | algebraically faithful; physical owner unbuilt |
| codimension-ten defect/density reduction, then variation | a new four-dimensional Euler system | prior N3 supplies a moving-defect derivative; full weld still open |

The word “pullback” in the public descriptions primarily concerns fields and
spinors.  It does not license the first row as an equation receiver.

The mandatory source collision is recorded in
[`gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md`](../lab/sources/gu-actual-y14-receiver-ordering-source-reinspection-2026-08-05.md):

| source row | disposition |
| --- | --- |
| observerse section and field pullback | `SOURCE-CONFIRMS` |
| `10+4` decomposition and trace reversal | `SOURCE-CONFIRMS` |
| contracted curvature/Euler object described as a one-form | `SOURCE-GUIDES` |
| explicit primalize-before-observe formula | `SOURCE-SILENT` |
| action-image horizontality | `SOURCE-SILENT` |
| normal receiver/common Green domain | `SOURCE-SILENT` |

## 4. Exact local K77 section geometry

At a point of `Y=Met(X)`, choose adapted coordinates

\[
T_sY\cong T_xX\oplus \operatorname{Sym}^2T_x^*X,
\qquad \dim=4+10.
\]

With mostly-minus

\[
g_X=\operatorname{diag}(1,-1,-1,-1),
\]

the vertical trace-reversed Frobenius form is

\[
G_{\rm v}(h,k)
=\operatorname{tr}(g^{-1}h g^{-1}k)
-\frac12\operatorname{tr}(g^{-1}h)\operatorname{tr}(g^{-1}k).
\]

The exact probe verifies:

| form | inertia |
| --- | --- |
| raw vertical Frobenius | `(7,3)` |
| trace-reversed vertical | `(6,4)` |
| horizontal plus trace-reversed vertical | `(7,7)` |

This is precisely where the trace reversal matters.  Omitting it gives the
wrong total inertia.

For a nontrivial rational local section graph with first jet

\[
L=ds=\begin{bmatrix}I_4\\J\end{bmatrix},
\qquad J\in\operatorname{Mat}_{10\times4}(\mathbb Q),
\]

the probe chooses rank-four `J` and verifies that

\[
g_s=L^T G_Y L
\]

is nondegenerate.  This is a local fibrewise witness, not a theorem that an
arbitrary `X` has a global Lorentz observation section.

## 5. The degree-zero result

The pullback of covectors is

\[
O=s^*=L^T:T_s^*Y\longrightarrow T_x^*X.
\]

On 13-forms it induces

\[
\Lambda^{13}O:
\Lambda^{13}T_s^*Y\longrightarrow\Lambda^{13}T_x^*X=0.
\]

The exact exterior-power matrix has shape `0 x 14` and rank zero.  Therefore
direct pullback of the source Euler 13-form cannot be the nontrivial observed
connection equation.

This does **not** say that the source Euler equation is zero or meaningless.
It says that the form must be converted or pushed forward before comparison
with a four-dimensional equation.

## 6. Primalize first: the rank-ten obstruction

Let

\[
R_Y:E_Y^!\longrightarrow E_Y
\]

be the inherited nondegenerate K77 Hodge/Krein/density primalizer.  In the
oriented coefficient fixture the probe represents it by the invertible
gimmel musical matrix.  Since `R_Y` is invertible,

\[
\operatorname{rank}(O R_Y)=\operatorname{rank}(O)=4,
\qquad
\dim\ker(O R_Y)=10.
\]

The result is independent of the particular invertible coordinate
representation of the primalizer.

The complete kernel after primalization is the conormal bundle of the section.
For the graph above,

\[
N=
\begin{bmatrix}-J^T\\I_{10}\end{bmatrix},
\qquad
ON=0,
\qquad
\operatorname{rank}N=10.
\]

The probe exhibits a nonzero `e_Y` for which

\[
\tau_Y=R_Ye_Y\ne0,
\qquad
O\tau_Y=0.
\]

No faithful coefficient representation *after* `O` can recover that lost
direction.  Coefficient-module faithfulness and geometric receiver
faithfulness are therefore sequential conditions, not rival repairs.

## 7. The conditional repair supplied by the geometry

When `g_s=L^T G_YL` is nondegenerate, the gimmel metric defines

\[
H=G_YL(L^TG_YL)^{-1}:T_x^*X\longrightarrow T_s^*Y.
\]

It obeys

\[
OH=I_4.
\]

Consequently

\[
P=HO,
\qquad Q=I-P

\]

are complementary projectors, and `im H` is inverse-gimmel-orthogonal to
`ker O`.  Section observation is faithful on `im H`.

This yields the exact action-specific sufficient condition

\[
Q\,R_Y\Upsilon_T=0
\quad\text{on the actual source-action Euler image}. \tag{AHR}
\]

If `(AHR)` holds, the ten conormal false-shell directions are absent from the
action image, and the predecessor's coefficient-faithfulness test becomes the
next receiver condition.

What is **not** proved is the load-bearing statement `(AHR)` itself.  The
metric constructs the split; it does not prove that the varied action lands in
one summand.  Imposing `(AHR)` because desired four-dimensional physics needs
it would repeat the target-selection error.  It must follow from the complete
Euler map, a source-owned constraint/BV differential, or an independent
geometric identity.

## 8. The honest alternative: retain the normal equations

The fourteen covectors in `[H,N]` form a basis.  Its inverse gives a full
receiver

\[
\mathcal O_{\rm full}
=\begin{bmatrix}O\\V_N\end{bmatrix},
\]

where the first four rows are ordinary section restriction and the last ten
rows recover the conormal coefficients.  The exact probe verifies that this
receiver is invertible and detects the hidden witness.

This construction proves that information loss is not inevitable if the
normal equations are retained.  It does **not** identify those ten components
as particles, Higgs slots, constraints, auxiliary fields, dark matter, or any
other physical content.  Their transformation law, action role, preboundary
pairing and observation semantics remain to be built.

Fibre integration is not an immediate substitute: a ten-dimensional
pushforward sends degree 13 to degree 3, and the metric fibres are noncompact,
so support and normalization become additional real obligations.

### 8.1 The third route: reduce the action honestly, then vary

The hostile pass caught an initially false exhaustiveness claim in this wave.
The theory is not limited to “horizontal Euler image” or “retain ten normal
components.”  One may instead construct a genuine map from the ambient action
to a four-dimensional action and derive its Euler system there.

This is not literal pullback of a 14-form.  A differential 14-form also pulls
back to zero on `X4`.  The reduction must be typed as one of:

- pairing the ambient density with the current of integration of `s(X)` or a
  codimension-ten Thom/delta current;
- an induced-density restriction that is explicitly **not** differential-form
  pullback; or
- a supported/renormalized fibre pushforward.

The prior N3 construction already gives a live starting point.  For a moving
defect `(s_t)_* ell_t`, it derived

\[
\left.\frac d{dt}\right|_0\langle(s_t)_*\ell_t,f\rangle
=\int_X\bigl[df_{s(x)}(V)\ell+f(s(x))\dot\ell\bigr],
\]

and, for a pulled-back connection,

\[
\delta_s(s^*A)
=s^*(\iota_VF_A)+D_{A_X}(s^*\iota_VA).
\]

Those normal section variations can carry information that ordinary
one-form restriction kills.  They do not yet prove that the complete source
action, Hodge/Krein pairing, defect density and all moving bundle maps form a
single variationally closed receiver.

This correction also exposes a stale typing problem in older reconstruction
surfaces that write `s^*(dvol_Y)` as a four-dimensional volume form.  Taken
literally as differential-form pullback, that expression is zero.  It may be
repairable as induced density on the section, but that density operation must
be named and varied; the old notation cannot be used as a proof.

## 9. Common Green domain boundary

For an operator `D` to preserve the horizontal observed image, the pointwise
finite condition is

\[
QDH=0.
\]

The probe constructs two exact operators with the same observed tangential
block:

- `D_good` satisfies `Q D_good H=0`;
- `D_bad` has a live normal block, so `Q D_bad H != 0`;
- nevertheless `O D_bad H = O D_good H`.

Thus matching the four-dimensional observed evolution cannot diagnose normal
leakage.  For the actual differential operator, `(AHR)` and `QDH=0` must hold
on a shared domain compatible with the Krein Green form, boundary conditions,
closure and the BV/constraint structure.  The finite algebra here supplies no
closability, maximal-dissipativity or ultrahyperbolic boundary theorem.

## 10. Divergent specialist preassessment

The ten inline lenses predicted the decisive features before computation:

1. differential geometry predicted a rank-ten conormal kernel;
2. the variational-bicomplex lens required primalization before a nontrivial
   section equation could be read;
3. pseudo-Riemannian geometry required the trace-reversed metric and a
   nondegenerate induced graph metric;
4. gauge/BV geometry warned that Ward tangency does not prove Euler
   horizontality;
5. Krein/operator theory separated a pointwise split from a common domain;
6. hyperbolic PDE required principal-symbol image invariance;
7. representation theory predicted that later faithfulness cannot repair
   earlier geometric erasure;
8. symplectic geometry required a pairing and quotient owner for retained
   normal data;
9. exact-computation engineering required both tangent and conormal witnesses;
10. the science-council lens required both summary-overreach and
    superseded-object review.

Nine predictions survived without change.  The science-council/proof-systems
lens found one material omission: the initial synthesis presented two receiver
routes as exhaustive even though the earlier moving-defect build already owns
a third, action-reduction route.  The hostile review and repairs
are recorded in
[`2026-08-05-k77-wave2-actual-y14-receiver-ordering-review.md`](../lab/process/hostile-reviews/2026-08-05-k77-wave2-actual-y14-receiver-ordering-review.md).

## 11. Seven axes plus Layer 0

| level | disposition |
| --- | --- |
| Layer 0 | direct `Omega13` pullback, primalize-then-restrict, fibre integration, defect/density reduction and enlarged receiver separated |
| L1 | source confirms field pullback and guides a one-form equation reading; ordering/horizontality silent |
| L2 | exact form-degree zero theorem, K77 inertia, rank-four receiver and rank-ten complete kernel |
| L3 | exact local `Met(X)` graph, metric right inverse and tangent/normal decoder; global section open |
| L4 | actual action ownership preserved; its Euler-image horizontality unproved |
| L5 | later coefficient faithfulness cannot repair conormal erasure; BV ownership open |
| L6 | finite invariant-image discriminator built; common closed Green domain open |
| L7 | no physical equation, particle, Standard Model, GR, dark-sector or cosmology row moves |

## 12. Accounting and next gate

| item | result |
| --- | --- |
| ordinary receiver selector parameters | `0` |
| direct `Omega13` receiver rank | `0` |
| primalize-then-restrict rank | `4` |
| conormal kernel rank | `10` |
| enlarged receiver rank | `14` |
| new free coefficients | `0` |
| `free_object_delta` | `0` |
| residue | `K77-W2-ACTUAL-Y14-RECEIVER:T3` |
| P1/P2/P3 | unchanged and unused |
| Wave 3 | closed |

The original compound gate is therefore **partially moved, not closed**.  The
actual receiver is no longer vague: its ordering and whole kernel are known.
The highest-information successor is

`K77_ACTION_DERIVED_HORIZONTAL_EULER_IMAGE_OR_DEFECT_VARIATIONAL_RECEIVER`.

Run it in this order:

1. substitute the complete source-owned translation Euler map and test `(AHR)`
   coefficientwise, including the fermionic adjoint contribution;
2. in parallel on the already-built N3 route, weld the ambient action to the
   moving codimension-ten defect/induced density and vary it before any
   observation claim;
3. if neither route retains the necessary equations, type the ten normal
   outputs under the active gauge group, variation and preboundary pairing
   rather than discarding them;
4. only after one receiver closes, build the common Krein/Green/BV domain on
   that selected image.

No stationarity, physical equation, mass, VEV, chirality, anomaly, index,
generation count, dark-energy or dark-matter result is claimed.
