---
artifact_type: exploration_result
created: 2026-08-08
status: BASE_CHAIN_IS_HINGE_FREE__THE_SINGLE_OPEN_STEP_IS_THE_RS_TWIST__NAIVE_CLOSURE_REFUSED_AS_SIGNATURE_CROSSING
grade: "LOCATION result plus a refused inference. The identification of tau with
  tau_RS is read from the filed b-parametrix and generation-sector artifacts. The
  invariant count under a Riemannian reading is exact representation theory; it is
  reported and then REFUSED as the answer, because the reading crosses signature."
canon_verdict_change: none
priority_change: none
row_change: none
residue_touched: []
follows:
  - explorations/holonomy-kernel-route-2026-08-08.md
---

# Where the hinge enters the window chain

## The question

Does the holonomy route to `ker D_tang != 0` — and therefore the whole
window-index chain — depend on the "2+1 with an imposter" hinge?

## The answer: no, except at exactly one step, and that step is the hinge

```text
holonomy on X^4, parallel spinors from Hol(K3) = SU(2)      BASE side, hinge-free
Gamma^r invertibility, indicial family, window separation   BASE side, hinge-free
------------------------------------------------------------------------------
"does the tau twist admit a parallel section?"              tau = tau_RS
                                                            = 4 D(1/2,0) + 4 D(0,1/2)
                                                            = the RS sector
                                                            = where the imposter
                                                              and the 384 cousin live
```

The base-side chain is **independent of the 2+1 line**. The two meet at exactly
one point: the RS twist.

That is worth knowing in both directions. The window-index argument is not a
re-derivation of the generation-count result — it comes from the base and the
count line comes from the internal sector. And they are not fully independent
either: they share a single junction, and that junction is the hinge.

## The naive closure, computed and refused

Reading `D(1/2,0)` and `D(0,1/2)` as the Riemannian `S^+`, `S^-` of `Spin(4)`:

```text
Hol = SU(2)_- :  tau_RS -> 4 S^+ + 4 S^-  gives  4*2 + 4*0 = 8 invariants
Hol = SU(2)_+ :  tau_RS -> 4 S^+ + 4 S^-  gives  4*0 + 4*2 = 8 invariants
```

Either way **8 parallel sections**, which would satisfy the open condition, hence
`ker D_tang != 0`, hence `delta = 0` is an indicial root, hence the two natural
windows are separated, hence **the count question is malformed and the row
closes**.

**This is refused as the answer.** The reading identifies the **Lorentzian**
`D(1/2,0)` of `SL(2,C) = Spin(3,1)` with the **Riemannian** `S^+` of `Spin(4)`.
Those are different objects related by complexification, and this session's own
complexification result showed that **signature is not a complex invariant** —
over `C` every nondegenerate symmetric form is equivalent to the identity, so the
identification destroys precisely the datum it would need to carry.

It is the signature-crossing move the repository's Layer-0 discipline forbids
without an explicit map, and it has the same shape as the false `[verified]`
convexity claim corrected earlier today. Taking it would have closed a headline
row on an unlicensed identification.

## Honest status

The remaining condition reduces to: **does `tau_RS`, restricted to `Hol(X^4)`,
contain the trivial representation?**

- Under a naive Riemannian reading: yes, with multiplicity 8.
- That reading is unlicensed. What is owed first is the explicit map between the
  Lorentzian `SO_0(3,1)` representation content of `tau_RS` and whatever acts on
  the Riemannian `X^4` spin bundle — including which real form and which
  chirality convention survives the passage.

Note the structure of the obstruction: the chain was blocked by a broken index
formula, routed around it via holonomy, and now terminates on a **signature
typing** question. That is the same object that `SIGNATURE-AMBIENT` leaves open at
stack depth 10, arriving from a completely different direction.

## Fences

- The invariant counts are exact representation theory *for the Riemannian
  reading*. They are not a result about GU.
- Nothing here closes the count row, and nothing here should be cited as evidence
  that it closes.
- The location result — that the base chain is hinge-free and meets the 2+1 line
  at exactly the RS twist — does not depend on the refused inference and stands
  on its own.
