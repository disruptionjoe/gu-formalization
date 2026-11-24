---
title: Literal observation and the distributional functional dual
status: exploration
doc_type: structural-result
created: '2026-11-24'
program_target: X-P1-P2-P3
tier: T2
expected_delta: Identify what a barred-field dual of the actual thin observation must be before applying
  two-sided variational descent
actual_delta: The functional transpose of literal observation is i_*(Q^t beta), a supported current; it
  is neither a fiber transpose nor an automatically supplied smooth barred readout. Stronger Riesz duals
  and constrained domains remain explicit alternatives.
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# The dual of thin observation is not another smooth restriction

program_target: X-P1-P2-P3
tier: T2
expected_delta: Identify what a barred-field dual of the actual thin observation must be before applying two-sided variational descent
actual_delta: The functional transpose of literal observation is i_*(Q^t beta), a supported current; it is neither a fiber transpose nor an automatically supplied smooth barred readout. Stronger Riesz duals and constrained domains remain explicit alternatives.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`. Base revision
`b586e6e5b2f8064670685cf3809971222293db5f`; internally reviewed T2 structural result.
Primary target X-P1-P2-P3, secondary X-P1-P2. No source, ledger or packet kill.

```gu-typed-objects
result: Fiber-dual versus functional-dual observation and the supported barred-current requirement
carrier: fixed smooth codimension10 section i:S4→Y14, smooth source scalar/one-form spinors and their observed contraction LAYER=ambient+observed BRIDGE=literal-section-contraction CHIRALITY=S-FULL-DIRAC
pairing: algebraic independent row/column duality with explicit densities; optional supplied smooth nondegenerate bundle pairing, no reality or physical positivity assumption ON=declared_carrier
real_structure: complex linear transpose of independent bars; a separately specified conjugate dual has the same support result, without identifying source bars with adjoints
grading: field form degree, dual-current form degree and physical chirality kept distinct
action_owner: N/A -- duality identity for an existing observation; no source action, pairing selection or new domain built
target: actual barred-observation bridge for variational descent MAP-TYPE=restriction
```

## 1. Source boundary and the three different maps

The rendered source §9.3 extraction declares four independent smooth fields
nu,bar-nu∈Omega0(Y,S) and zeta,bar-zeta∈Omega1(Y,S). It supplies a candidate
operator display, not a unique density lift, global adjoint or common domain.
Its equations9.18–9.19 use form degrees13 and14 for Euler receivers; those
receivers must not be confused with the original barred field coordinates.
[Source extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md).

SC-CHI-01/04/52 concern effective observed separation, not universal exact
off-shell autonomous hidden and observed fields. The local two-cross-block
test in [determinant repair](determinant-repair-variation-2026-11-24.md) §4
explicitly assumes a supplied density-dual K and true barred dual splitting;
it also explicitly says those are not yet supplied for the completed source.
The existing metric-spin/fixed-density exterior subclass is a legitimate
conditional arena, not that missing source selection.

Write E for the ambient field bundle, O for the observed bundle and

    Q:i*E→O,                 q=Q i*:Gamma(Y,E)→Gamma(S,O).

Q is the actual zeroth-order section contraction. For the full source-shaped
local comparison it retains (P_H zeta,Gamma_Y zeta,nu). The following proof
uses only Q and its nonzero image; it is not an arbitrary projector.

Keep three maps separate:

- Q^t:O*→i*E* is the **fiber transpose** on the section. It does not extend
  a field into Y and includes no integration over normal directions.
- q^t is the **functional transpose** between test-section duals. It pushes
  an observed dual density into an ambient distributional dual density.
- A proposed barred observation bar-q on smooth ambient barred fields is
  another source/geometry map. It is not determined merely by writing Q^t
  or q^t; its direction, density and domain must be supplied.

Here t means linear transpose, not a Hilbert or Krein adjoint. Independent
barred variables permit this notation without imposing a reality condition.
A specified sesquilinear convention conjugates the coefficient as usual but
does not change the support or regularity argument.

## 2. Exact functional-transpose theorem

Take a compactly supported smooth observed dual density
beta∈Gamma_c(S,O*⊗Dens(S)), and define its functional on ambient test fields by

    ell_beta(u)=integral_S beta[Q(i*u)].

Then, by the definition of distributional pushforward,

    q^t beta = i_*(Q^t beta).                              (1)

This identity is coordinate-independent and makes no choice of ambient
extension. In coordinates (x,y) with S={y=0}, write beta=b(x) w_S(x) dx,
and let the ambient density be mu_Y=w_Y(x,y) dx dy. Equation(1), as an
ambient dual density, is

    Q(x)^t b(x) w_S(x) delta_0(y) dx dy.                   (2)

If one represents ambient barred coefficients through a supplied smooth
invertible pairing B and mu_Y, their generalized coefficient is

    B(x,0)^(-1) Q(x)^t b(x) [w_S(x)/w_Y(x,0)] delta_0(y).  (3)

B here maps barred coefficients to unbarred covectors; its inverse is not
silently the source's reality operation. Equations2–3 keep the measures and
coefficient identification explicit. Smooth nonzero scalar weights or
invertible frame/pairing transports change coefficients, not delta support.

**No smooth representative.** If Q^t beta is nonzero, no smooth ambient
barred field paired with a smooth nondegenerate density map can represent
ell_beta on ALL compactly supported ambient test fields. Indeed tests
supported off S force the smooth representing dual density to vanish off S.
Since S has empty interior, continuity makes it vanish everywhere. But a
nonzero Q^t beta is detected by a test field supported near a point of S,
contradiction. If Q is pointwise surjective, every nonzero beta is detected.
For a nonsurjective Q the exact condition is Q^t beta≠0, not beta≠0 alone.

For the plain horizontal one-form and scalar restriction slots, ordinary
form-current pushforward raises degree by the normal codimension: an observed
degree3 one-form dual becomes degree13, and an observed degree4 scalar dual
becomes degree14. The extra gamma-trace slot uses its own algebraic Q^t
coefficient map and must not be assigned degrees by this plain-form rule.
The density formulation(1) covers all slots without ambiguity. These outputs
are CURRENTS supported on S, not smooth forms supplied by the source's
receiver display. No new
family, chirality or gauge count follows from them.

## 3. Relation to the already-proved graph/domain constraint

A nonzero localized coefficient of (2) has the form f(x)delta_0(y). The
existing K2531 Fourier argument gives

    f(x)delta_0(y) ∈ H^(-s)_loc  iff s>5               (c=10),

in auxiliary isotropic positive chart norms. This threshold is reused,
not a new regularity result or a physical Hilbert-space assertion.
The stronger source-specific consequence is the identification of the
FUNCTIONAL barred dual with that supported object.

More directly, choose the germ-preserving cutoffs of
[observation graph domains](observation-graph-domain-2026-11-24.md), with
ell_beta(u)≠0. Then

    ||chi(y/epsilon)u||_(first-order graph)→0,
    ell_beta(chi(y/epsilon)u)=ell_beta(u)≠0.

Thus this nonzero dual functional is not continuous in the tested graph
topology. We do not identify a nonelliptic operator's graph dual with H^-1;
the cutoff argument proves the assertion without such an identification.
At-section normal jets or smooth determinant weights still do not help.
The theorem does not say that distributions are forbidden in a completed
GU construction; it says their use and analytic pairing require an explicit
bridge beyond smooth independent barred coordinates.

## 4. Countercontrols and legitimate changes of construction

**A smooth extension is dual to an average.** In a product chart with product
density, choose a smooth normal profile rho with integral1. Extending beta
as Q^t beta times rho(y) defines the transpose of

    q_rho u(x)=integral rho(y) Q(x)u(x,y) dy,              (4)

not literal q on unrestricted fields. A normal Taylor term y1² is zero
under literal restriction but generally nonzero under (4). This is the
precise difference; calling both maps “observation” does not identify them.
If Q or the density varies normally, its chosen extension and the density
factor enter (4) as well.

A normalized width-epsilon profile rho_epsilon=epsilon^-10 rho(y/epsilon)
has L2 norm epsilon^-5 ||rho||_L2. Hence smooth dual representatives at
finite width do not stay uniformly L2 bounded while approaching a nonzero
thin dual. K2543 already owns the related smearing/zero-width distinction.
No finite width, regulator or detector is selected here.

**Constrained-domain positive control.** On a supplied finite-volume normal
product Z, restrict ambient test fields to u(x,y)=v(x). The smooth constant
extension beta/Vol(Z) reproduces ell_beta on this restricted test space.
More generally, on the supplied profile subspace u(x,y)=psi(y)v(x),
psi(0)=1, any smooth dual profile phi with integral phi psi=1 does so. These
are equal functionals ONLY on the declared subspace, not on all ambient
fields. This is the same domain-sensitive escape exhibited by K2242; it
adds a tube-wide restriction/profile and is not a source-selected domain.

**A Sobolev Hilbert adjoint is another identification.** If a supplied stronger
Hilbert topology makes q bounded, its Hilbert adjoint is
q†=R_E^(-1) q^t R_O, where R_E and R_O are the Riesz maps of those
actual Hilbert spaces. Such maps can contain differential or nonlocal
regularizing operators; they are not the smooth zeroth-order pairing B in
(3). The resulting representative need not be delta-supported, although
its underlying functional transpose remains(1). This does not contradict
the theorem and must not be excluded by it. No such native Riesz/domain
choice is supplied by the printed bars or by an indefinite finite pairing.

**A section-supported action/measure.** If an already-supplied functional
is integrated on S, its barred variable may naturally be a section dual
without claiming a smooth ambient representative. Such a functional is a
different action/measure specification from an ambient smooth bilinear.
This alternative is not constructed or attributed to the source here.

These controls prevent a false universal statement that source observation
requires singular physical fermions. It is only the functional transpose of
literal unrestricted observation that has the supported-current form.

## 5. Consequence and next usable input

For a two-sided variational descent claim, supply (i) the actual density-
valued operator and pairing, (ii) the barred readout or its injected dual
carrier, and (iii) the common test/closed domains and measures. A fiberwise
orthogonal representative can support a local coefficient calculation; it
does not supply a smooth ambient functional transpose. Conversely, retaining
independent smooth barred fields and applying literal restriction to each is
a different specified pair of maps and must be tested as such.

The next calculation can therefore proceed on the **existing declared local
metric-spin/exterior subclass**, with both cross blocks evaluated there and
the result explicitly conditional. It cannot silently claim that the source
selected those dual data. The present theorem identifies the missing global
barred bridge without building a source action or reopening a blocked packet.
No physical ledger row moves: source effective2+1, native weak projector,
closed Fredholm realization and integer observable remain open.

## Verification ceiling

The companion exact probe checks a nontrivial fiber-transpose pairing,
normal-density conversion, finite-width readout versus evaluation, exact
Gaussian normalization and norm growth, and a constrained-profile positive
control. The Gaussian is a rapidly decreasing product fixture; the local
statement(1) is proved for compactly supported tests without depending on
that fixture. No numerical rank, chosen action or empirical prediction is
inferred. Independent T2 review accepted the result. Root replay passed24 controls and rejected both planted errors (density ratio and smearing/restriction confusion). See the [review](../../lab/process/hostile-reviews/2026-11-24-source-dual-grading-review.md).
