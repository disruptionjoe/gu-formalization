---
artifact_type: conditional_build_real_form_correction
created: 2026-08-12
status: TRACE_HQ_CONTACT_RANK120_OF_160__COKERNEL_RANK40__SCALAR_COMPLETION_POINTWISE_REALIZABLE
canon_verdict_change: none
---

# Selected K77 I2B trace-Hq normal-contact correction

## Result

V0.220 used the grade-only `B`-skew Clifford bank as the source real form and
therefore reported rank eight per normal. That was the wrong embedded real
form for the source-sized unitary carrier already established by v0.194.

The operative Hermitian form is

```text
H_q = i B gamma(q_g),        q_g = g/2.
```

It has inertia `(64,64)` on the full complex carrier and `(32,32)` on each
Weyl half. Applying the exact `H_q`-skew phase rule to every one of the 32
matching grade-two supports gives

```text
rank per normal = 12 of 16,
total rank = 120 of 160,
cokernel rank = 40.
```

The old `B`-skew rank is eight and the observer-time `H_u` rank is ten, so the
three real-form embeddings are observably different controls, not alternate
descriptions of one matrix. In the corrected trace-`H_q` image the scalar
completion used by v0.219 is pointwise source-realizable. Its on-shell value is
still not selected: that requires the coupled Euler normal prolongation on a
stationary background, plus gauge, domain and state conditions.

## Two halves and the H homonym

The source-level carrier statement is

```text
C^(32,32)_+ + C^(32,32)_-.
```

The product `U(32,32) x U(32,32)` is the subgroup preserving those two halves;
it is not the primary carrier statement and does not by itself assert two
independent connection fields. All supports in this contact are Clifford
grade two, hence even, so the rank-120 contact preserves both halves and lies
in that block-preserving algebra. Full `U(64,64)` half exchange is unnecessary
for this particular contact.

There are also two unrelated uses of `H` in the repository:

- `H_q` is the full Hermitian form above, with restrictions to both Weyl
  halves; and
- the generation hinge satisfies `H^- = X(S^+)`, `H^+ = X(S^-)` because `X`
  reverses chirality.

They must not be identified. The superscript on the hinge records its target
Rarita--Schwinger chirality; it does not denote the negative restriction of
the Hermitian form.

## Exact module result

The corrected per-normal image has pivot coordinates

```text
(0,1,2,4,5,6,8,9,10,12,13,14),
```

and the cokernel has basis coordinates `(3,7,11,15)`. The actual fixed-observer
`SO(3)` action on all sixteen sparse response tensors is trivial, so the local
cokernel is four trivial copies under that derived group. V0.219's synthetic
`1+3` action was not induced by the response bank.

The 16-response truncation is not closed under the complete trace-q normal
stabilizer. Therefore the rank-40 local cokernel is not yet a global associated
subbundle. It is also not the recurring rank-128 fermionic leakage module:
dimension and carrier type both disagree.

## What changes and what does not

Append-corrected:

- v0.220 rank `80/160` becomes rank `120/160`;
- the cokernel rank becomes `40`, not `80`;
- scalar destroy/create contact is pointwise source-realizable; and
- the recurring-rank-128 identification is refuted at this grade.

Unchanged:

- the source owns the off-shell normal-contact operator, not its on-shell
  value;
- `D_varpi H_q=0` and global two-half reduction remain open;
- coupled Euler prolongation, stationary background, global module closure,
  Green/BFV/domain and physical spectrum remain open; and
- the 120 source-image coordinates are not booked as a coupling, P1, P2, P3
  or new datum.

The main exact probe passes `46/46`, with the old real form, observer real form,
`kappa=0`, synthetic-module and fixed-frame/global plants all firing.

## Next gate

Derive the complete coupled Euler normal prolongation on a stationary
trace-`H_q` background. Intersect its allowed contact with the rank-120 source
image, then test the resulting physical image against the existing contact
discriminant. Build the full stabilizer orbit before naming a global cokernel
bundle.
