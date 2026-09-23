---
title: "Residual-vector kinetic-realization first gate"
status: exploration
doc_type: construction_result
created: "2026-09-23"
target_claim: "P8 of DECLARED-CONTENT-EXTRA-VECTOR-OBSTRUCTION"
claim_verdict: conditional_exact
operational_state: verified
---

# Residual-vector kinetic-realization first gate

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact uses the
> conventional D5 / Pati–Salam Cartan comparator to test one declared-content
> premise. It is not evidence for or against Weinstein's source-native mechanism
> without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` before reuse.

Comparator classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: RESIDUAL-VECTOR-KINETIC-REALIZATION-GATE
carrier: compact D5 Cartan plane spanned by declared hypercharge Y and B-L comparator generators LAYER=toy CHIRALITY=N/A
pairing: exact trace over all forty D5 roots ON=compact_D5_Cartan_plane; candidate algebraic Yang-Mills Cartan form only
real_structure: compact real Cartan coordinates with rational generator entries
grading: packet fundamental zeta_F=1, packet induced zeta_F=0, and source two-layer reading kept distinct
action_owner: comparator; no observed source-owned gauge kinetic bilinear is selected
target: first rank/radical evaluation inside supplied premise P8 MAP-TYPE=evaluation
```

## Target and scope

The target is deliberately smaller than “derive a physical vector.” The
declared-content theorem already proves that an abelian gauge direction remains
under premises P1–P7. P8 separately supplies a nondegenerate physical
gauge-kinetic realization. This gate asks only whether the natural compact D5
root-trace form becomes degenerate on the residual direction after its mixing
with the admitted hypercharge direction.

The result binds the frozen comparator model and the packet's fundamental
Yang–Mills candidate. It does not select the source action, observation map,
physical quotient, domain, Green pairing, coupling or propagating particle.

## Exact calculation

Enumerating the forty roots `±e_i ±e_j` of D5 gives, without invoking a
pre-tabulated Killing form,

`sum_alpha alpha tensor alpha = 16 I_5`.

Use the declared Cartan coordinates

`Y=(-1/6,-1/6,-1/6,1/4,1/4)` and
`B-L=(-1/3,-1/3,-1/3,0,0)`.

The exact root-trace Gram matrix in basis `(Y,B-L)` is

`[[10/3, 8/3], [8/3, 16/3]]`,

with determinant `32/3`. It therefore has rank two. Orthogonalizing the
residual direction gives

`X=(B-L)-(4/5)Y=(-1/5,-1/5,-1/5,-1/5,-1/5)`,

and exactly `<X,Y>=0`, `<X,X>=16/5`.

Thus a radical or kinetic-mixing escape does not remove the residual direction
on this candidate compact Cartan form. This is a positive answer only to the
first algebraic rank/radical gate.

## Horn-specific disposition

- On the packet's fundamental horn `zeta_F=1`, the written Yang–Mills candidate
  is nondegenerate on the `Y` plus residual plane. P8 still does not follow:
  the trace form has not been descended through an observed action-owned gauge
  quotient and paired with a physical Green operator.
- On the packet's induced horn `zeta_F=0`, the repository supplies neither an
  admissible regulator nor a source-owned induced kinetic form. The D5 Gram
  cannot substitute for that missing object, so no rank test is licensed there.
- The source two-layer `I^B_2=||Upsilon^B_omega||^2` reading is a third typed
  architecture, not silently one of the packet's two horns. It needs its own
  action bridge before this calculation can be transported.

## Consequence and claim ceiling

P8 remains `supplied_not_derived`. The next cheapest discriminator is not
another Cartan census. It is to match the existing corrected observation
projection to a named action-owned constraint/gauge image and Green pairing,
then test nondegeneracy on the resulting closed quotient. The still-missing
owners are: the actual kinetic bilinear; observation descent; gauge/constraint
quotient and domain; real or Krein Green pairing; and only then normalization.

No source register row, physics ledger row, canon, paper status, public surface
or physical claim changes. RA-G4 and LT-SM1a/b remain open with a sharper first
gate: the simple radical escape fails on the fundamental candidate, while the
physical-realization chain remains unbuilt.

## Reproduction

```sh
python3 tests/channel-swings/residual_vector_kinetic_realization_gate.py
python3 tests/channel-swings/residual_vector_kinetic_realization_gate_probe.py
```
