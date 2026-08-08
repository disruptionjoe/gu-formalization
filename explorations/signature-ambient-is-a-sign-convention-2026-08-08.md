---
artifact_type: exploration_result
created: 2026-08-08
status: SIGNATURE_AMBIENT_REDUCES_TO_THE_BASE_SIGN_CONVENTION__RETYPING_PROPOSED_NOT_EXECUTED
grade: "EXACT. The invariance of the DeWitt fibre form under g -> -g is computed
  with residual 0.00e+00 and has a two-line reason. The arithmetic combining base
  and fibre signatures is trivial. The RETYPING that follows is a proposal and is
  NOT executed here: it would take a depth-10 fork off the board and requires
  hostile field-specialist review under the standing 2026-08-03 rule."
run_id: GUH-20260808T060000Z-register-side-track
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/where-the-hinge-enters-2026-08-08.md
---

# `SIGNATURE-AMBIENT` is the base sign convention

## Computed

```text
base  g = diag(1,1,1,-1)    signature (3,1)
base -g = diag(-1,-1,-1,1)  signature (1,3)

DeWitt fibre form G(g)   signature (6,4)
DeWitt fibre form G(-g)  signature (6,4)
G(-g) = G(g) exactly,  residual 0.00e+00

base (3,1) + fibre (6,4)  =>  ambient (9,5)  =>  Cl(9,5) = M(64,H), quaternionic
base (1,3) + fibre (6,4)  =>  ambient (7,7)  =>  Cl(7,7) = M(128,R), real
```

**Reason, two lines.** `A_i = g^{-1} B_i`, so `g -> -g` sends `A_i -> -A_i`. Both
`tr(A_i A_j)` and `tr(A_i) tr(A_j)` are **even** in `A`, so
`G_ij = tr(A_iA_j) - (1/2) tr(A_i)tr(A_j)` is invariant. The fibre does not flip;
the base does; the ambient is their sum.

## What follows

`g` and `-g` describe **the same Lorentzian geometry**. The causal cones are the
same set of vectors; only the labels "timelike" and "spacelike" exchange. So the
two horns of `SIGNATURE-AMBIENT` are **not two geometries**. They are one geometry
under two sign conventions.

**Therefore the fork as posed — "(9,5) or (7,7)?" — has no convention-independent
answer.** There is nothing about the geometry that selects one.

The registry already records the input to this: *"the fibre is (6,4) both ways"*.
It does not draw the consequence, and no file in `canon/` records it either.

## Why this is not "the fork does not matter"

The convention is **not free**, because `Cl(3,1) = M(2,H)` and `Cl(1,3) = M(4,R)`
are genuinely different algebras with different spinor reality types. Majorana
conditions available in one are unavailable in the other. That is exactly why the
repository's own notes record that the Kramers wall is `(9,5)`-only and that
`(7,7)` removes the halving.

So the correct reading is: **a convention with physical consequences**. It cannot
be chosen arbitrarily; it must be chosen consistently with whatever the physics
demands, and every reality-type statement in the program is downstream of it.

## The retyping this suggests, proposed and NOT executed

Once the fork is seen as a convention, the ill-posed question splits into two
well-posed ones:

1. **Which convention does the source compute in?** That is `REAL-CLIFFORD-FORM`,
   and it is **SETTLED at `Cl(7,7)`** — which by the arithmetic above corresponds
   to base `(1,3)`.
2. **What depends on the convention?** Spinor reality type, Majorana availability,
   the Kramers wall, every `dim_H` restatement.

If that split is accepted, `SIGNATURE-AMBIENT` retypes from **open,
UNDER-DETERMINED, stack depth 10 over threshold** to **a convention, settled for
the source by `REAL-CLIFFORD-FORM`, with a tracked consequence list**.

That would remove the largest live structural exposure in the program.

**It is not executed here, deliberately.** Three reasons. It is a verdict-adjacent
change on the highest-fan-out fork in the registry and requires the hostile
field-specialist review of the standing 2026-08-03 rule. The registry explicitly
states these two rows are distinct, and overriding that on one session's argument
would be exactly the unlicensed move refused an hour ago on the `tau_RS`
identification. And this session has already produced one confident false claim.

## The strongest objection, stated for whoever reviews it

The registry's distinction may be doing real work: `REAL-CLIFFORD-FORM` asks what
the **source computes in**, which is a fact about Weinstein's arithmetic, while
`SIGNATURE-AMBIENT` asks what the **geometry is**. If the geometry genuinely had a
convention-independent signature, the two would be separate questions and this
artifact's argument would be wrong.

The computation above says the geometry does **not** have one. But a reviewer
should attack precisely there: is there any convention-independent structure —
time orientation, a causal ordering, an orientation datum — that selects `g` over
`-g`? Note `sigma = U7 = w_1` of the orientation double cover of `L_time` is
exactly a candidate, and it is an **external** datum. If the selection is external,
the fork is settled by an import rather than by GU, which is a different closure
and arguably a more interesting one.

## Fences

- The invariance computation is exact and is the only computation here.
- The retyping is a **proposal**. Nothing in the registry, ledger or canon is
  changed by this artifact.
- Nothing here says the convention is physically irrelevant. It says the geometry
  does not select it, which is a different and weaker claim.
