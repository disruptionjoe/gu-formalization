---
artifact_type: exploration_result
created: 2026-08-08
status: NO_CONVENTION_INDEPENDENT_SELECTOR_EXISTS__SIGMA_IS_NOT_THE_SELECTOR__RETYPING_OBJECTION_DOES_NOT_SURVIVE
grade: "EXACT for the causal-cone identity, which is the load-bearing check: the
  timelike sets coincide exactly on 4000 sampled vectors and the reason is a
  one-line algebraic identity, not a statistical result. The enumeration of
  candidate selectors is an argument over a named list and is not a proof that no
  selector exists anywhere."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/signature-ambient-is-a-sign-convention-2026-08-08.md
---

# Nothing convention-independent selects the base sign — and `sigma` is not the selector

## The objection being tested

The previous artifact argued `SIGNATURE-AMBIENT` reduces to the base sign
convention, and named the strongest objection itself: *is there any
convention-independent structure — time orientation, causal ordering, an
orientation datum — that selects `g` over `-g`?* It flagged `sigma = U7 = w_1` of
the orientation double cover of `L_time` as exactly such a candidate.

**The objection does not survive, and `sigma` is the clearest casualty.**

## The load-bearing check: the causal cone is the same set

```text
timelike under g,  convention g(v,v) < 0 : 724 of 4000 sampled vectors
timelike under -g, convention g(v,v) > 0 : 724 of 4000
the two sets are IDENTICAL : True
```

This is not a statistical coincidence. `g(v,v) < 0` and `(-g)(v,v) > 0` are the
**same inequality**. The timelike cone is one set of vectors described twice.

**Therefore `L_time` is the same bundle on both horns, and `w_1(L_time) = sigma =
U7` is the same class.** `sigma` is convention-*independent*, which is a good
property for a datum to have — and precisely why it **cannot** be the selector.

## The other candidates

| candidate | selects? | why |
|---|---|---|
| causal cone / time orientation / `w_1(L_time)` | **no** | the cone is the same set; `sigma` is the same class |
| spacetime orientation (volume form) | **no** | `det(g) = det(-g) = -1` in even dimension |
| the DeWitt fibre form `G` | **no** | `G(-g) = G(g)` exactly, residual `0.00e+00` |
| anything defined by the **sign** of `g(v,v)` | yes, but circularly | e.g. "the spatial block is positive definite" **is** the convention restated |

Every convention-independent structure on the list fails to select. Every
structure that does select is itself a sign choice.

## What this does to the retyping proposal

It removes the objection that was holding it back. The previous artifact declined
to retype `SIGNATURE-AMBIENT` partly because a convention-independent selector
might exist; the strongest named candidate is now shown not to be one.

**What still stands in the way, and it is not small:**

1. The registry states these two rows are **distinct**, and that statement is
   deliberate. It should be attacked on its own terms, not overridden by a
   third-party argument.
2. This enumeration covers a **named list**. It is not a theorem that no selector
   exists — a structure nobody has named could select, and the honest form of the
   result is "no known convention-independent structure selects".
3. Retyping the highest-fan-out fork in the registry is verdict-adjacent and needs
   the hostile field-specialist review of the standing 2026-08-03 rule.

So this artifact strengthens the case and does not close it. That distinction is
the point.

## The consequence if it is eventually accepted

`sigma` becomes more interesting, not less. It is convention-independent, so it
survives the retyping untouched — and it stays exactly what the repository already
says it is: an **external** `Z/2` that GU cannot own. What changes is that it can
no longer be hoped to double as the signature selector, which removes one of the
places its "quadruple duty" might have been extended to a fifth.

And the fork, if retyped, is settled for the source by `REAL-CLIFFORD-FORM` at
`Cl(7,7)`, i.e. base `(1,3)` — with the physical consequences (spinor reality,
Majorana availability, the Kramers wall) tracked as a consequence list rather than
as an open question.

## Fences

- The causal-cone identity is exact algebra; the 4000-vector sample is an
  illustration of it, not its warrant.
- The candidate enumeration is a named list, not an exhaustiveness theorem.
- Nothing in the registry, ledger or canon is changed by this artifact. The
  retyping remains proposed and unexecuted.
