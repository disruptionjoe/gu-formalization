---
title: "Type II_1 Selector Candidate: C3/D4 Generation Projection Audit"
date: "2026-06-24"
status: exploration
verdict: "NO_VIABLE_EXPLANATORY_SELECTOR_FOUND; C3/D4 IS A TOY COUNT SELECTOR ONLY"
owner: "Second-Wave Worker 3"
depends_on:
  - "explorations/type-ii1-spectral/type-ii1-construction-or-nogo-gate-2026-06-24.md"
  - "explorations/type-ii1-spectral/type-ii1-finite-control-selector-attempt-2026-06-23.md"
  - "explorations/type-ii1-spectral/type-ii1-finite-control-specialist-pass-2026-06-23.md"
  - "explorations/type-ii1-spectral/type-ii1-sm-checklist-tightening-2026-06-23.md"
  - "lab/specifications/type-ii1-spectral-sm/connes-finite-control-checklist.md"
  - "lab/specifications/type-ii1-spectral-sm/type-ii1-extension-requirements.md"
---

# Type II_1 Selector Candidate: C3/D4 Generation Projection Audit

## Verdict

No viable explanatory selector was found.

The narrowest plausible construction is a C3/D4 generation-count selector:
choose a finite-index subfactor with an intrinsic threefold standard-invariant
feature, then use its three equal Markov-trace projections or bimodule summands
as generation labels. The best concrete model is an index-3 group-subfactor /
D4-principal-graph picture.

This candidate passes a very weak toy test:

```text
after choosing an index-3/C3/D4 subfactor, the standard invariant supplies
three canonically named, equal-dimension summands, up to permutation.
```

It fails the construction-or-no-go gate as an explanatory Type II_1 selector:

```text
the choice "C3" or "index 3" already inserts the desired count, and the
Connes-Chamseddine finite algebra/module must still be tensor-attached by hand.
```

So the candidate selects at most a threefold label set. It does not select the
SM algebra, the SM representation content, or three physical generations without
an added `Phi_CC` that deliberately forgets the C3/D4 charge and maps each sector
to the same finite CC generation module.

This does not close the Type II_1 lane as a semifinite hosting construction. It
does narrow the subfactor-generation lane: a future positive result must do more
than exhibit a triple point or an order-3 group action.

## Gate Being Tested

The previous gate asked for an explicit object

```text
(N subset M, tau, p_1, p_2, p_3, Phi_CC)
```

with:

- `M` a II_1 factor;
- `N subset M` a finite-index subfactor, or a declared replacement;
- `p_1,p_2,p_3` mutually orthogonal, Murray-von Neumann equivalent projections
  or bimodule summands with equal `tau`-dimension;
- the `p_i` obtained from the standard invariant rather than chosen by hand;
- `Phi_CC` sending the Type II_1 data to finite Connes-Chamseddine control data;
- at least one SM-relevant finite-control datum selected beyond merely embedding
  the finite CC triple.

Since full algebra selection remains too hard, this note tests only generation
selection.

## Candidate Selector Definition

Call the candidate `S_C3/D4`.

### Data

Choose an outer action of `C3` on a II_1 factor `R`, and form either of the
standard equivalent-looking finite-index pictures:

```text
N = R^C3 subset R
```

or

```text
N = R subset M = R crossed_product C3.
```

In the hyperfinite case this is the familiar amenable test object. A
non-hyperfinite or non-embeddable replacement would have to be specified
separately; nothing in this note constructs one.

The index is:

```text
[M : N] = 3.
```

The standard-invariant/principal-graph reading is the D4-style triple-point
reading: the first nontrivial branching has three equal arms or, in the group
picture, three character-sector labels.

### Projection Model

In the crossed-product presentation `M = R crossed_product C3`, let `u_g` be
the canonical group unitaries and let `omega = exp(2*pi*i/3)`. The group algebra
`L(C3)` contains three Fourier idempotents:

```text
e_k = (1/3) * sum_{g=0}^{2} omega^(-kg) u_g,       k = 0,1,2.
```

They satisfy:

```text
e_k^2 = e_k
e_k^* = e_k
e_i e_j = 0 for i != j
sum_k e_k = 1
tau(e_k) = 1/3
```

Since `M` is a II_1 factor, equal trace implies Murray-von Neumann equivalence
inside `M`:

```text
e_0 ~ e_1 ~ e_2.
```

So the formal projection candidate is:

```text
p_i = e_i.
```

In the D4 principal-graph presentation, replace the `e_i` by the three minimal
central idempotents in the relevant finite-dimensional relative commutant
corresponding to the three D4 arms. Their Markov traces are equal by graph
symmetry/Perron-Frobenius weighting. This produces a canonical unordered triple
of equal-weight sector projections in the Jones tower.

### Shadow Functor Attempt

Let `K_SM` denote one finite CC generation module, with the usual finite algebra
action of:

```text
A_F = C oplus H oplus M_3(C).
```

The only available `Phi_CC` is a collapse map of the following form:

```text
Phi_CC(N subset M, tau, p_i; A_F, K_SM, D_F, J_F, gamma_F)
  = (A_F,
     (K_SM tensor C^3) plus particle/antiparticle doubling,
     D_F with generation blocks,
     J_F,
     gamma_F;
     SU(3) x SU(2) x U(1) / Z_6)
```

where the C3/D4 sector label `i` is read as the generation label and then
forgotten by the observer-facing Connes channel.

This is the critical weakness: `Phi_CC` does not arise from the subfactor data
alone. It imports `A_F`, the one-generation CC module, and the rule "send each
of the three sectors to an identical SM generation."

## Pass/Fail Audit Against the Gate

| Gate item | Result | Reason |
|---|---|---|
| `M` is a II_1 factor | PASS in the hyperfinite/group-subfactor test model | `R crossed_product C3` is again a II_1 factor for an outer finite-group action. |
| `N subset M` finite index | PASS | The chosen group-subfactor has index 3. |
| Three orthogonal projections/summands | PASS in the crossed-product model; PARTIAL in principal-graph-only model | Fourier idempotents give actual projections in `M`; D4 arms give sector idempotents in the Jones tower/relative commutants. |
| Equal `tau` or Markov-trace dimension | PASS | `tau(e_i)=1/3`; D4 arm weights are equal by the triple symmetry. |
| Murray-von Neumann equivalence | PASS for `e_i` as projections in the factor; PARTIAL for D4 sectors | Equal-trace projections in a II_1 factor are equivalent, but the equivalences are not canonical. D4 sector labels may be equal-weight without being equivalent as bimodule sectors. |
| Canonically obtained rather than chosen by hand | PARTIAL/FAIL | The projections are canonical after choosing C3/index 3/D4. But that choice already contains the count 3. |
| `Phi_CC` explicit | PARTIAL | A collapse functor can be written, but only after supplying `A_F`, one SM generation module, and a rule identifying the three sector labels with generations. |
| Selects SM algebra `A_F` | FAIL | `A_F = C oplus H oplus M_3(C)` is still external. |
| Selects SM representation list | FAIL | The 16 Weyl fermions per generation still come from the finite CC module or the GU/Pati-Salam branching, not from the subfactor. |
| Selects three generations beyond CC hand insertion | WEAK PARTIAL | It selects a canonical threefold label set only because an order-3/index-3 object was chosen. It does not prove that three is forced by Type II_1 spectral data. |
| Non-embeddable contribution | FAIL | The clean model is hyperfinite/amenable. No non-embeddable separation is used. |

## Does It Select Anything?

Yes, but only in a weak and possibly tautological sense.

It selects:

```text
an unordered triple of equal trace sector labels,
given an index-3/C3/D4 finite-index inclusion.
```

It does not select:

```text
the SM finite algebra;
the one-generation SM bimodule;
the hypercharge assignments;
the compact SM gauge group;
the physical interpretation of the three labels as generations.
```

The construction is therefore better than choosing arbitrary projections
`p_1,p_2,p_3` in a diffuse II_1 factor, because the projections come from a named
standard-invariant feature. But it is not yet better than inserting the number
three at the level of the subfactor choice.

The anti-smuggling test is simple:

```text
replace C3 by Cn.
```

The same crossed-product construction gives `n` equal Fourier projections. Unless
the spectral-triple axioms, order-one condition, anomaly constraints, or a
Connes-channel theorem force `n = 3`, the construction has not explained the
generation count. It has only moved the hand insertion from "three CC copies" to
"choose the C3/index-3 standard invariant."

## Why D4/C3 Still Fails as the Narrow Selector

The D4/C3 object is the best narrow candidate because it has the right kind of
mathematical discreteness:

- finite index;
- finite standard invariant;
- a named threefold feature;
- equal trace weights;
- an internal symmetry or dual action that can permute the three projections in
  the algebraic model.

But it misses the load-bearing physical requirement. A generation in the CC
shadow is not just a projection of trace `1/3`. It is a full copy of the
one-generation fermion bimodule, with the same SM gauge representation package
and anomaly cancellation.

The C3/D4 data supplies no functorial reason that each sector should carry
exactly that same `A_F`-bimodule. If the finite CC module is tensored onto each
sector, the selector has only labeled three inserted copies.

There is also a mild equivalence problem. Equal trace projections in a II_1
factor are Murray-von Neumann equivalent, but this is a diffuse-factor fact, not
a generation theorem. In the principal-graph reading, the three D4 arms are
equal-weight sector labels; they need not be equivalent bimodule summands in the
strong sense needed for three identical SM generations. Equality of dimension is
not equality of representation content.

## Consequence for the Type II_1 Lane

This result does not demote the entire Type II_1 lane below the previous gate.
The lane still supports a semifinite host for the CC triple, and the sign/real
structure obstructions are not presently decisive.

It does demote the current subfactor-generation idea from "candidate selector"
to:

```text
candidate count-label mechanism, pending a non-smuggling theorem.
```

The strongest honest statement is:

> A C3/D4 finite-index inclusion can provide a canonical threefold sector label
> set with equal trace. It cannot, by itself, make those labels into three SM
> generations.

## Concrete Next Computation

The next worker should not search for another graph with a visible `3` until the
C3/D4 toy model is either upgraded or formally rejected. The concrete proof
obligation is:

```text
For the index-3/D4 subfactor, compute the three arm idempotents in the Jones
tower, their Markov traces, their Connes-fusion classes, and their image under
any proposed Phi_CC.
```

Decision rule:

1. If the three arm sectors are not equivalent, and `Phi_CC` maps them to three
   identical SM generations only by forgetting their inequivalence, then the
   selector fails as explanatory.
2. If the sectors are equivalent only because the ambient II_1 factor has equal
   trace projection equivalence, then the selector still fails; diffuse
   equivalence is too cheap.
3. If a canonical standard-invariant automorphism gives a transitive orbit of
   three sector idempotents, and a functorial Connes-channel construction sends
   that orbit to exactly three identical copies of the one-generation CC module
   while preserving `J`, `gamma`, `D`, order-one, and anomaly cancellation, then
   the generation selector can be upgraded to conditional pass.

The minimal deliverable should be a four-column ledger:

| object | computed from subfactor alone? | equal dimension? | CC-shadow interpretation |
|---|---|---|---|
| three D4/C3 idempotents | yes/no | value | one generation each, or merely labels |
| equivalences among them | yes/no | canonical/noncanonical | preserves identical SM content? |
| `Phi_CC` on each sector | no external CC data? | same/different | anomaly-free SM generation? |
| replacement `Cn` test | why not `n != 3`? | varies with n | falsifies selection if arbitrary |

Until that ledger is filled, the selector finding is negative.

## Bottom Line

The narrowest plausible Type II_1 generation selector is the C3/D4
standard-invariant candidate. It gives a clean toy triple of equal projections or
sector idempotents, but it does not yet select generations in the SM sense.

The present verdict is therefore:

```text
NO VIABLE EXPLANATORY SELECTOR FOUND.
```

The Type II_1 path remains open as a construction/hosting lane, but its
generation-selection claim now has a very specific burden: prove that the
standard invariant determines not only a threefold count, but three equivalent
copies of the one-generation CC finite-control datum under a non-ad-hoc
`Phi_CC`.
