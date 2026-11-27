---
status: exploration
doc_type: structural-result
created: '2026-11-27'
tier: T2
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
matrix_or_ledger_effect: Evidence only; no verdict change.
title: Full metric-space product lifting is detected on an observation section
program_target: X-P1-P2
expected_delta: Resolve the explicitly open full-Y determinant-root extension while retaining integral
  fibre torsion.
actual_delta: Every compatible normal H reduction on full Y lifts to the direct product iff its restriction
  to a metric section does. For closed spin Lorentz bases some liftable reduction exists iff signature
  is divisible48.
class_covered: Connected oriented spin4 base admitting a Lorentz metric section, full unoriented-time
  Y=Met(3,1)(X), native normal6,4 bundle, prescribed normal Spin and optional H=S(U3xU2) reduction. Fixed-H
  criterion includes all integral torsion; some-H existence allows free positive J/volume and assumes
  closed X.
premises:
- explorations/conditional-build/global-normal-complex-reduction-2026-11-24.md
- explorations/conditional-build/normal-special-unitary-existence-2026-11-25.md
- explorations/conditional-build/normal-sm-characteristic-constraints-2026-11-27.md
- lab/sources/source-claim-register.yaml#SC-GEO-03
- lab/sources/source-claim-register.yaml#SC-GRP-03
source_bridge:
  status: conditional
  reason: The full metric carrier and optional normal SU reduction are source supplied; closedness, product
    lift and physical gauge identification are not required by source.
kill_condition: A nonzero admissible fibre determinant class or failed prescribed-Spin extension cancels
  this upstairs extension; the owned section theorem remains.
classification: SOURCE_NATIVE_ROUTE
---

# No extra determinant-root obstruction upstairs

Basis: `c083eefcb2c6196f3a686596aeb2c596c2bdb42a`.

```yaml
program_target: X-P1-P2
tier: T2
expected_delta: Resolve the explicitly open full-Y determinant-root extension while retaining integral
  fibre torsion.
actual_delta: Every compatible normal H reduction on full Y lifts to the direct product iff its restriction
  to a metric section does. For closed spin Lorentz bases some liftable reduction exists iff signature
  is divisible48.
```

```gu-typed-objects
result: full-Y fixed-reduction lift criterion and some-reduction existence
carrier: native vertical normal N=P6+Q4 over full Y=Met(3,1)(X), complex E3_R=P and E2_R=Q LAYER=ambient+observed BRIDGE=metric-section-restriction CHIRALITY=N/A
pairing: trace-reversed normal metric signature6,4; integral degree-two cohomology ON=declared_carrier
real_structure: oriented spin base and prescribed total normal Spin; optional special-unitary normal reduction
grading: positive6/negative4 normal factors, not physical fermion grading
action_owner: repository-construction of geometric theorem; no action or physical gauge selected
target: restriction detection of geometric central-cover lift MAP-TYPE=intertwiner
```

> **GU-COMPARATOR-ROUTING — scope before inference.** The native geometric
> bundles are not independently chosen physical gauge bundles. Read
> [routing](../../lab/methods/source-native-comparator-routing.md).
> No chirality/count, physical current or connection is derived.

## Decision delta and source relevance

The recently accepted
`explorations/conditional-build/normal-sm-characteristic-constraints-2026-11-27.md`
Section3 explicitly leaves **product-lift extension over all of Y** open.
Its last section again lists global-Y lift as unmodeled. This is distinct
from the already-proved quotient existence on Y and product-lift criterion
on the four-dimensional observation section.

SC-GEO-03 (2021 draft p17) supplies Y=Met(X); SC-GRP-02 (p24-25,
equation3.32) puts the structure bundle upstairs; SC-GRP-03 (p29,
equation4.6 and adjacent text) permits the normal compact/complex
intersection, optionally special-unitary. These provide the actual carrier
and reduction category. They do **not** require the optional direct-product
lift, closed X, or identify the geometric bundles with physical gauge data.
Thus the result is a positive conditional all-Y upgrade, not a
source or GU exclusion.

## Theorem

Let X be a connected smooth oriented spin four-manifold admitting a Lorentz
metric section s, and let pi:Y=Met_(3,1)(X)->X be the full unoriented-time
metric bundle. Use the owned trace-reversed normal bundle with negative
rank-four factor Q and its prescribed total normal Spin lift. For every
compatible full-Y normal H=S(U(3)xU(2)) reduction, write E2 for its negative
complex rank-two bundle, E3 for its positive rank-three bundle, and
`d=c1(E2)=-c1(E3)`.

1. There is a unique d0 in H²(X;Z) such that `d=pi*d0`; it is `s*d` and is
   even, including integral torsion.
2. This **specified** H reduction lifts to SU3xSU2xU1 over Y if and only if
   its restriction along s does. Equivalently, `d0 in 6 H²(X;Z)`.
3. If X is closed, some full-Y product-liftable H reduction compatible with
   the prescribed normal Spin lift exists if and only if `48 | signature(X)`.
   This existence statement permits choosing the positive complex structure
   and determinant volume. It does not assert liftability of every reduction.

On the time-oriented cover the fibre is S³ and pi* is an isomorphism in H²,
so the sixth-root criterion is detected by the unique base class. Restriction
along a section gives that class only when a lifted/time-oriented section is
supplied; an arbitrary unoriented-time section need not lift.

## Proof: retain the noncontractible fibre and its torsion

The owned global-normal-complex-reduction report, Section2, deforms Y onto
P(TX), with fibre RP³. Let L be its tautological timelike real line and put

    a=w1(L),  x=beta(a)=c1(L tensor C).

Here beta is the integral Bockstein from `0->Z --2--> Z -> Z2->0`.
Thus 2x=0, and x restricts to the nonzero class in H²(RP³;Z)=Z2.

The degree-two integral Serre filtration gives

    0 -> pi*H²(X;Z) -> H²(Y;Z) -> Z2 -> 0.

There is no (1,1) term because H¹(RP³;Z)=0. The fibre H² local system is
trivial since its group Z2 has no nontrivial automorphism. The only possible
outgoing differential on its degree-two generator is d3; the globally
defined x restricts to that generator, so d3 is zero. The globally defined
order-two x splits the extension. Consequently there is no hidden Z4
extension even if H²(X;Z) has 2- or 4-torsion.

For a splitting aligned with the actual section, use

    x_s=x-pi*(s*x),
    H²(Y;Z)=pi*H²(X;Z) direct-sum Z2<x_s>,  s*x_s=0.

The unadjusted x need not pull back to zero: a Lorentz metric need not be
time-oriented. No time orientation is smuggled into the splitting.

The owned native splitting gives

    Q ~= L* tensor pi*T*X.

The rank-four line-twist formula is

    w2(Q)=pi*w2(TX)+3a pi*w1(TX)+6a²=0.

For every compatible complex E2, `rho2(d)=w2(Q)=0`. The coefficient exact
sequence therefore gives d=2u for an **integral** u. Doubling annihilates
the Z2<x_s> summand, so d is uniquely pi*d0 with d0 even. This uses no
division in cohomology and loses no base torsion.

The existing central-cover theorem applies on any such base: the covering
map `(A,B,z)->(z²A,z^-3B)` has kernel mu6, and a specified H bundle lifts
exactly when det(E3) has an integral sixth root. Write any u as
`pi*u0+epsilon x_s`. Then `6u=pi*(6u0)`. Since pi* is injective,

    pi*d0 in 6H²(Y;Z) iff d0 in 6H²(X;Z).

This proves the fixed-reduction claim, including torsion. Fibre torsion can
neither create a new obstruction for an admissible determinant nor repair
a failed base sixth-root condition.

## Proof of the some-reduction statement

Necessity follows by restriction and the already-owned closed-section
signature criterion. For sufficiency take signature=48m and the already
constructed negative J0 on Q0=s*Q with `c1(Q0,J0)=d0=-6ell`; the section
theorem supplies such a J0 for the prescribed restricted Spin structure.
Let L0=s*L. There is a real bundle isomorphism

    Q ~= pi*Q0 tensor (L tensor pi*L0).

Pull back J0 and tensor with this real line. Its complexification has
first Chern class alpha of order at most two, so the resulting complex
rank-two bundle has

    c1=pi*d0+2alpha=pi*d0.

Make this complex structure orthogonal for the actual definite negative
metric by the usual metric-compatible deformation; the procedure may be
chosen to fix the section, where J0 is already orthogonal. It changes no
characteristic class.

Now apply the **owned prescribed-Spin extension theorem**
`normal-special-unitary-existence-2026-11-25.md`: keeping this full-Y negative
J, the positive J and determinant volume can be chosen compatibly with the
specified total Spin lift. Its fibre is S7 and the first obstruction is in
degree8; Y has homotopy dimension at most7. The resulting determinant class
is `-pi*d0=6pi*ell`, so a pulled-back line representing ell supplies the
sixth root. No new action, gauge connection or native matrix is constructed.

This does not claim extension of an independently prescribed positive J,
volume, preserved connection, boundary/end data or whole fixed H reduction
on X. Those are different relative/fixed-data problems. The fixed-full-Y
theorem above only tests a reduction that is already supplied.

## Controls and inference limits

The degree-two computation is integral. A global order-two class splits the
Serre extension; a hidden Z4 extension is therefore not assumed away. The
unadjusted tautological Bockstein need not vanish on the chosen section.
On T4×RP3 the fibre Bockstein is nonzero and not sixth-divisible, but it cannot
be the determinant class of this spin negative bundle because it is not even.
A section class d0=2e with e primitive still fails the sixth-root test upstairs;
fibre torsion cannot repair it. The signature−48 positive example extends;
the signature−16 quotient-without-product example remains unchanged.

This theorem does not divide degree-four cohomology by2 and makes no new
all-Y second-Chern claim. It does not preserve an independently fixed positive
J, volume, connection or boundary data. Its closed examples still fail the
stronger literal2021 unique-Spin requirement; the source does not require
closedness. Chosen/active Spin and unique Spin remain distinct.

- **ESTABLISHED:** the specified upstairs lift is detected by any admitted
  section; some closed-base liftability has exactly the owned48-divisibility
  criterion. No extra fibre determinant obstruction remains in this class.
- **RULED OUT:** treating fibre Z2 alone as a new obstruction for an admissible
  even determinant, or as a repair for a failed base sixth root.
- **NOT MODELED / UNDETERMINED:** physical gauge identification, prescribed
  connections or positive J/volume, relative/end data and source necessity of
  closedness or the product group. The fullU alternative remains.

The probe checks exact split-group/torsion arithmetic and countercontrols,
not the topology or smooth extension theorem. Those are written and reviewed.
The existing finite signature arithmetic is reused; no new Lean claim or
world-novelty claim is made. Standard Serre filtration, Bockstein and
central-cover tools are composed on the owned native bundles.
Choice budget stays10/4/net6/0; no new physical choice is adopted.
