---
artifact_type: exploration
created: 2026-08-05
title: "Pre-contract Wave 0C: the spinor cure line is identical but not the whole SA-C2 object; the two Shiabs meet on a trace-reversed Riemann restriction; scale blindness has a precise boundary"
grade: "EXACT finite-dimensional typing and irreducible-coordinate theorem plus primary-source collision. Full-domain bundle descent, moving fields, action equality and observed physics remain open."
named_gate: PRECONTRACT-0C-TYPED-IDENTITY-AND-THEOREM-SCOPE
gate_before: SAME_OBJECT_CLAIM_OVERBROAD__TWO_SHIABS_RELATION_UNTYPED__SCALE_BLINDNESS_SCOPE_INFORMAL
gate_after: SPINOR_LINE_IDENTITY_EXACT__FULL_SA_C2_IDENTITY_REJECTED__RIEMANN_TRACE_REVERSAL_ADAPTER_CONSTRUCTED__FULL_ADAPTER_OPEN__SCALE_THEOREM_SCOPED
route_disposition: USE_RIEMANN_ACTION_SQUARE_AS_ADAPTER_SEED__DO_NOT_SPEND_BUILD_ON_CONGRUENCE_INVARIANT_SCALE_SELECTORS
source_collision: SOURCE-CORRECTS
fork_assumed: none
search_space_dim: "4 real spinor-channel coordinates plus 2 irreducible Riemann response coordinates"
free_object_delta: 0
residue_touched:
  - "LT-SM3b:T3"
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
---

# Pre-contract Wave 0C: identity and theorem scope

## Result first

Three questions now have separate answers.

1. **Same object, narrowly:** SHIAB-04's gamma-traceless spinor selector and
   W125's T3 vertex are exactly the same projective element
   `contract-(1/6)wedge`, equivalently `wedge-6 contract` up to `-6`.
2. **Not the whole cure:** SA-C2 also contains a `g=1` projector and points to
   an unbuilt Porrati–Rahman analytic completion. Those are not maps
   `Omega²(S)->Omega¹(S)`. Calling the entire cure “the same object” is false.
3. **The two Shiabs can meet, but only after adapters:** the spinor map and the
   adjoint degree-13 map have a natural common action codomain. On algebraic
   Riemann curvature, Clifford contraction gives Ricci while the selected
   adjoint Shiab gives Einstein. Exact trace reversal converts one into the
   other. This constructs a Riemann-restricted adapter seed, not a full-domain
   identity.

The scale theorem is also now bounded exactly: it kills every condition
invariant under the blockwise congruence group that moves the desired ratio.
It does not kill vacuum stationarity with competing homogeneities, flux or
spectral quantization, boundary/domain data, anomaly conditions that genuinely
break the action, dimensional transmutation, or an openly fitted external
scale.

## 1. Exact identity of the spinor line

Use the real coordinate basis

`(contract_+-, wedge_+-, contract_-+, wedge_-+)`.

The canon reconstruction is `C=(1,0,1,0)`. Let `W=(0,1,0,1)`. W125 T3 is

`T3 = C-(1/6)W = (1,-1/6,1,-1/6)`.

SHIAB-04's named line is

`W-6C = (-6,1,-6,1) = -6 T3`.

They are therefore the same nonzero projective element, with no convention or
normalization ambiguity.

The gamma-trace functional on each block has row `(1,6)`. It kills T3 exactly
and does not kill the pure contraction. On the four-real-coordinate family the
two block constraints have rank two, so their kernel is two-dimensional. After
projectivizing an overall scale, one chiral-block ratio remains. Only an
additional equal-block tie makes the projective point unique; the action
coupling normalization remains separate. Thus the earlier accounting phrase
“residual 3 -> 0” was too strong. What is exact is:

```text
4 real channel coordinates -> 2 real gamma-traceless coordinates
-> 1 projective chiral-tie coordinate after overall normalization
-> one projective point only if equal block weights are separately imposed
```

## 2. Layer 0 on SA-C2

| item | type | relation to T3 |
| --- | --- | --- |
| T3 spinor vertex | `Omega²(ad) x S -> Omega¹(S)` pointwise, or `Omega²(S)->Omega¹(S)` after action | identical to the gamma-traceless line |
| `Pi_kerGamma` cure | endomorphism of `Omega¹(S)` | different domain and role |
| Porrati–Rahman completion | field-strength-dependent nonminimal vertex in a different physical setting | structural template only; not constructed in GU |
| adjoint Shiab | `Omega²(ad)->Omega¹³(ad)` | different coefficient bundle and degree shift |

The identity therefore attaches to the **T3 facet**, not all of SA-C2.

## 3. A typed bridge between the two Shiabs

For `F in Omega²(ad P)` and a spinor `s`, both maps can be sent to
`Hom(S,Omega¹(S))`:

```text
spinor path:  F -> (s |-> Phi_S(rho(F)s))
adjoint path: F -> (s |-> rho(* Shiab_ad(F))s)
```

This makes equality a meaningful question. It does not make it true.

On the algebraic-Riemann spin image in dimension fourteen:

- the Clifford/Bianchi contraction on the spinor path decodes to `Ric`;
- the selected adjoint row decodes to `-2 G_14`.

In scalar/traceless-Ricci coordinates their responses are

```text
spinor Ricci path:       (13, 1)
adjoint selected path:   (156, -2)
```

No scalar multiple relates these pairs. But trace reversal sends

`Ric -> Ric-(1/2)Scal g`, hence `(13,1) -> (-78,1)`, and multiplication by
`-2` gives `(156,-2)` exactly. Therefore

```text
Shiab_ad | Riemann
  = -2 * encode * trace_reverse * decode * Phi_S * action
```

at the declared fixed-frame Riemann-restriction grade.

This is the first explicit adapter candidate between the two repo Shiabs. It
does **not** extend automatically to arbitrary `Omega²(ad)` inputs: the
Riemann injection/retraction, algebraic and differential Bianchi conditions,
moving soldering, Hodge/Krein owners, full action pairing and bundle descent
are extra structure. Restriction does not determine a unique full-domain map.

## 4. What this does to LT-SM3b

The conflict is real on the reconstructed spinor family: pure contraction is
gamma-traceful and the constraint-preserving line excludes it. But the phrase
“GU's written Shiab `(1,0,1,0)`” is a stale source premise. The 2021 written
map is adjoint-valued and degree 13; the pure spinor contraction is a later
UCSD-motivated reconstruction whose source-forced selection remains open.

The ledger disposition is therefore:

```text
LT-SM3b: OVER_DETERMINED / STALE_PREMISE
scope: canon spinor reconstruction treated as Eric's uniquely written map
distance: keep the exact gamma-traceless T3 line, separate it from the adjoint
          Shiab, and extend the Riemann adapter through the action
revival: a primary source or full-domain theorem proving the pure contraction
         must occupy the constraint-preserving spinor slot
```

This does not restore the pure contraction. It stops its failure from being
misreported as a failure of the source's adjoint Shiab.

## 5. Exact scope of the scale-blindness theorem

Let a block metric be `G=diag(c_b I_b,c_f I_f)` and let
`S=diag(s_b I_b,s_f I_f)` act by congruence. Then

`c_f/c_b -> (s_f²/s_b²)(c_f/c_b)`.

The group moves the desired ratio. Any predicate `P(G,...)` invariant under
this action is constant along that orbit and cannot select the ratio. This
includes the DC-H2 reciprocity and endogenous self-adjointness conditions,
because `G(G^-1 Q)=Q` reduces them to symmetry of `Q`, with `G` absent.

### Excluded supplier class

- symmetry or reciprocity of the pairing;
- self-adjointness defined by the same unfixed `G`;
- rank, inertia and representation-type conditions preserved by the full
  blockwise congruence action;
- any anomaly or equivariance condition **only when** its actual formula is
  invariant under that action.

### Not excluded

- an action/vacuum equation with terms of different homogeneity in the ratio;
- flux, index or lattice quantization that is not congruence-invariant;
- a fixed spectral value or boundary/asymptotic domain;
- renormalization-group dimensional transmutation;
- a source term using an independently normalized measure or reference;
- an external fitted scale, honestly priced as a fit;
- topology by itself only if a constructed map makes the scale discrete.

The exact counterexample to the overbroad reading is the positive potential

`V(r)=r+4/r`, `r>0`.

Its stationary equation is `1-4/r²=0`, selecting `r=2` with positive second
derivative. The equation is not blockwise-congruence invariant; its two
coefficients supply the missing comparative normalization. The theorem never
forbade it. It says the price cannot be hidden in a symmetry word.

## 6. Construction handoff

The best next object is now more precise:

1. use the Riemann action square as the seed adapter between spinor and adjoint
   Shiabs;
2. extend it to the source-owned curvature/torsion domain with moving Hodge,
   pairing and soldering;
3. compose it with the observed equation receiver exposed by 0B;
4. require the resulting full variational square to commute;
5. use only non-congruence-invariant mechanisms when trying to select the
   remaining horizontal/vertical scale.

This is compositional construction that directly specifies the next Build
target; it is not another search for the already-known need for a source action.
