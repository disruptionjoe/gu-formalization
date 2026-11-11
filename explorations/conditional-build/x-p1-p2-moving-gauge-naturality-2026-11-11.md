---
title: "X-P1-P2: moving gauge covariance is not fixed-arrow compatibility"
status: exploration
doc_type: structural-result
created: "2026-11-11"
program_target: X-P1-P2
tier: T2
expected_delta: "Resolve the full-gauge transfer premise of the fixed Gamma/j commutant argument."
actual_delta: "Constrained: equivariant orbit maps are isotropy intertwiners; fixed diagram compatibility is an additional equation, not a consequence of covariance. Density-dual and connection transport are kept explicit."
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
canon_verdict_change: none
---

# Covariance transports a diagram; it does not make every map its symmetry

**Result.** On a specified transitive background orbit G/H, equivariant
linear and antilinear bundle maps are classified by the isotropy H
intertwiners. A moving gamma-trace/inclusion diagram can be covariant
without every covariant endomorphism preserving its arrows. Therefore the
[fixed-arrow commutant theorem](x-p1-p2-multiplicity-weld-2026-11-11.md)
applies to two coflips of the **same specified diagram**, not to arbitrary
covariant coflips of the field bundle. This closes the proposed automatic
covariance-to-fixed-arrow inference at its precise scope. `X-P1-P2` stays
constrained; no C action or universal weld is certified.

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Identify the exact gauge-to-fixed-diagram transfer requirement.
actual_delta: Orbit-isotropy classification, source-typed countercontrol and density-dual transport supplied.

```gu-typed-objects
result: moving-gauge-naturality
carrier: associated field bundles over a specified homogeneous background orbit LAYER=UNTYPED CHIRALITY=N/A
pairing: density-valued bilinear or Hermitian pairing, distinguished from a fibre endomorphism ON=declared_carrier
real_structure: antilinear fibre maps with separately specified square and base map
grading: zero-form versus one-form field provenance, not observed family count
action_owner: repository-construction -- structural bundle category, no field action
target: equivariant map and fixed diagram compatibility MAP-TYPE=intertwiner
```

## 1. Source and prior-result custody

The [rendered section-9 extraction](../../lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md)
places independent barred/unbarred fields in Omega0(S) and Omega1(S), with
S the full Dirac bundle. Its rho(epsilon) wrappers are a covariance ansatz;
they do not prove global descent or identify the active real-K77 transition
group. The chosen induced tensor action below is a precisely declared
geometric control, not a newly source-certified representation of the full
inhomogeneous extension.

Earlier [super-IG work](../misc/super-ig-algebra-construction-2026-06-23.md)
already distinguishes fixed Clifford insertion from full gauge equivariance;
its later correction preserves the mixed rolled-carrier bracket and its
remaining real-form/action limitations. The
[moving-parent reduction](selected-k77-moving-parent-bundle-observation-reduction-2026-08-10.md)
already transports moving projectors. We reuse those facts. The new consumer
is the November fixed-Gamma/j weld and its precise morphism requirement.

## 2. Complete orbit classification, including antilinear maps

Let G be a Lie group, H a closed subgroup and V,W finite complex H modules.
On `E=G×_H V`, `F=G×_H W` over G/H, every smooth G-equivariant
fibrewise linear map covering the identity is uniquely

`[g,v] -> [g,A v]`, with `A rho_V(h)=rho_W(h) A` for all h in H.

Proof: restriction to the identity coset gives A, equivariance gives its
values everywhere, and independence of the coset representative is exactly
the displayed H equation. Conversely that equation makes the formula
well-defined and smooth. For an antilinear map `v -> U conjugate(v)`, the
equation becomes `U conjugate(rho_V(h))=rho_W(h) U`. No commutation with
all of G on one frozen fibre follows. This is an elementary associated-bundle
fact, not a novelty claim or a certification that the entire GU background
space is one smooth orbit. Singular or multiple orbits require separate treatment.

A collection of arrows, including Gamma, j and a symbol D, is another
equivariant object. A morphism of this diagram must additionally satisfy
`A_t Gamma=Gamma' A_s`, and similarly for every other arrow. Merely being
an equivariant map of its vertex bundles does not impose those equations.

In a trivialized orbit control, let `Gamma_b:E_b->S_b` and `j_b:S_b->E_b`
with `Gamma_b j_b=I`. If g takes b to gb, covariance reads

`Gamma_gb=R_S(g) Gamma_b R_E(g)^-1`,
`j_gb=R_E(g) j_b R_S(g)^-1`.

Consequently `P_R(gb)=R_E(g) P_R(b) R_E(g)^-1` for
`P_R=I-j Gamma`, and `R_E(g) ker Gamma_b=ker Gamma_gb`.
This is transport between objects. Stabilization of the same kernel is a
separate condition, weaker even than preserving both named Gamma and j.
The relevant fixed-background group is the stabilizer of **all** supplied
background structures, not just the gauge group label.

## 3. Source-typed finite countercontrol and its limit

Take `F=S ⊕ (V*⊗S)` and explicitly choose ordinary vertical gauge action
`R_g=diag(g,I_V*⊗g)`. It preserves form degree. The endomorphism
`T=P_0-P_1` is therefore gauge invariant. Extend Gamma from the one-form
block into the zero-form block, and j in the reverse direction. Then

`T Gamma_ext=Gamma_ext`, `Gamma_ext T=-Gamma_ext`,
`T j_ext=-j_ext`, `j_ext T=j_ext`.

Thus this invariant T fails both fixed-arrow equations. The probe realizes
this on a two-dimensional spinor and two covector components, with actual
noncommuting moving gamma matrices and normalized Gamma j=I. The example
is a control on the declared bundle grammar, not a C Lagrangian or a
counterexample to the earlier theorem. A nonzero off-diagonal symbol
coupling the zero- and one-form fields also rejects T as its symmetry.

If C0 and C1 are invertible antilinear maps to the **same mirror diagram**,
their ratio `T=C0^-1 C1` is an automorphism of that diagram. Conversely
such automorphisms give the possible ratios. When both cover the identity
and C0²=epsilon I, the common-square condition is `tau(T)T=I`,
`tau(T)=C0 T C0^-1`. A nontrivial involution of the background base
requires the two base points to be retained in this formula. Hence the
previous sixteen-variable sparse graph classification remains applicable
exactly after diagram compatibility is established. Gauge covariance alone
does not supply it, and the form-degree control does not disprove it for
actual same-operator coflips.

The failure persists even after adding square and isometry. As a separate
algebraic control take G=GL3(R) on C3, background
`Gamma=E01`, `j=E10`, `K=I`. The simultaneous stabilizer is
`H={diag(a,a,b):a,b in {+1,-1}}`: commuting with the two matrix units
first forces diag(a,a,b), and preserving K then forces these signs.
Both conjugation C0 and `C1=diag(1,-1,1) C0` are H-equivariant,
square to I, and preserve K. They extend to covariant fields on G/H by
the orbit theorem. Yet C1 fails both arrow equations. This shows that
covariance plus square plus isometry still does not imply arrow compatibility.
Moving by a real nonorthogonal shear transports K by inverse congruence;
freezing K would change the question. This is not a GU gauge-group assignment.

## 4. Released follow-through: density dual and local connection

For ordinary vertical gauge transformations fix a density mu and write a
Hermitian pairing as `u† P_b v mu`. Covariance means

`P_gb=R_g^{-dagger} P_b R_g^{-1}`.

For a bilinear pairing with independently transforming barred fields, use
the respective dual inverse and transpose instead; do not identify the
bars with Hermitian adjoints without a reality condition. A diffeomorphism
also transports mu and covectors. If `P_b` and `K_b` obey the same
Hermitian density-dual law, then `X_b=K_b^-1 P_b` obeys
`X_gb=R_g X_b R_g^-1`. At a fixed background this puts X in the
isotropy commutant. It does **not** make X commute with every diagram
arrow or make P proportional to K. The previous common-adjoint condition
is still needed. Distinct positive weights on the two form-degree summands
give an explicit covariant nonproportional pairing control.

There is an exact local differential counterpart. With column convention
`nabla=d+A`, `psi'=R psi`, covariance requires

`A'=R A R^-1-(dR)R^-1`.

For a moving endomorphism Q'=R Q R^-1, direct differentiation gives
`dQ'+[A',Q']=R(dQ+[A,Q])R^-1`. Omitting the inhomogeneous
term fails for a nonconstant R even if the pointwise orbit formulas are
correct. The probe tests a nonconstant polynomial shear with nontrivial A
and Q, then rejects the omitted-term control. This supplies a reproducible
local transport identity, not a global holonomy or parallelism proof. The
affine compensation is standard and already used in the
[moving split-structure calculation](selected-k77-moving-split-structure-action-selection-gate-2026-08-12.md);
its application here is a transfer check, not a new connection theorem.

Finally the source's additional connection translation is not automatically
gauge redundancy. The
[native BV image result](selected-k77-i2b-source-gauge-bv-image-2026-08-13.md)
has `delta T=alpha-D_A zeta`, with zero T-image on the tilted graph
`alpha=D_A zeta`. Treating every alpha as a pure gauge direction would
erase physical tangents. No extra invariance equation for the fermion
diagram is inferred from that translation label.

## 5. Effect and verification

The full-gauge successor is resolved as a conditional classification and
explicit transfer requirement: first identify the background orbit and
actual diagram morphisms; then apply the fixed-arrow theorem. The density
and connection checks close the immediate pointwise-to-local bookkeeping
consequences. Global naturality, permitted symbol support strata, coflip
existence, and the physical class-C realization remain separate.

The [Green-domain result](p3-green-form-symmetry-domain-2026-11-11.md)
then tests the same fixed J on an admissible boundary space. Covariance of a
moving family of J's does not by itself prove symmetry of one chosen domain. These two results
compose without identifying a selfadjoint ordinary index with native 2+1.

[Exact controls](../../tests/program-focus/x_p1_p2_moving_gauge_naturality_probe.py)
and [evidence](../../lab/process/x-p1-p2-moving-gauge-naturality.json) support
the written proofs; finite matrices do not certify universal GU covariance.
SC-GEO-55 retains ASSERTS for gauge-rotated-Levi-Civita displacement;
SC-GEN-54 retains ASSERTS for the supercharge-extension count claim, whose
physical map is not supplied here. SC-CHI-01/51 retain ASSERTS for the
nonchiral-total/effective split. Source, physics ledger, class C and canon
remain unchanged. No action witness, universal datum floor, Lean proof or
external-expert certification is claimed.
