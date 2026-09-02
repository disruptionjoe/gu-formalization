---
title: "A Residual Abelian Direction Under the Declared Geometric Unity Field Content"
author: "Joseph Hernandez"
status: draft
document_role: draft
operational_state: working
claim_verdict: conditional_exact
updated_at: "2026-09-02"
---

# A Residual Abelian Direction Under the Declared Geometric Unity Field Content

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Comparator classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

```gu-typed-objects
result: DECLARED-CONTENT-EXTRA-VECTOR-OBSTRUCTION
carrier: declared so(6,4) gauge directions with adjoint-45 and 10 tensor 45 scalar weight supports
pairing: no positive state or Born pairing is asserted; physical-vector realization is a separate premise
real_structure: real so(6,4) with compact k=so(6)+so(4) and complexified D5 weights for the census
grading: Cartan involution k(+1) plus p(-1); no observation grading beyond this split is inferred
action_owner: none; a gauge-kinetic/physical-realization term is not derived here
target: MAP-TYPE conditional composition from frozen declared content and admitted removal routes to a residual abelian gauge direction
```

## Abstract

Four existing exact packets can be composed into a binary result. Under a
single frozen premise set, the declared internal carriers and the available
Standard-Model-preserving adjoint orbits do not reduce the compact gauge
algebra to the twelve Standard Model directions. Observation removes the
24-dimensional noncompact complement but leaves nine non-Standard-Model
compact directions. The best available orbit leaves dimension 13, and the
declared content supplies no charged Standard-Model singlet, shifting
zero-form, anomaly or nonabelian residual factor that closes the remaining
abelian mass route. Therefore at least one extra abelian gauge direction
survives. Calling it a physical vector requires an additional, explicit
gauge-kinetic/physical-realization premise. This is a conditional exclusion
inside the frozen declared grammar, not a universal statement about possible
unreleased completions.

## Frozen premises

Let the following propositions be the complete antecedent:

1. **Declared carrier closure.** The internal algebra and field carriers are
   exactly those enumerated by PV-1/MV-2: the adjoint 45 and the declared
   `10 tensor 45` scalar support, with no undeclared 126 or other completion.
2. **Observation map.** Observation is the displayed Cartan reduction
   `so(6,4)=k+p`, with `dim(k)=21` and `dim(p)=24`; it can remove the `p`
   directions but is not an additional operation on directions inside `k`.
3. **Orbit completeness.** Standard-Model-preserving adjoint vacua range over
   the full two-dimensional centralizer used in PV-1.
4. **Mass-route completeness relative to declared content.** The admitted
   routes are Higgs, Stückelberg, Green–Schwarz and confinement, with their
   required owners typed as in MV-2.
5. **Residual identification.** The minimum residual is an abelian Cartan
   direction.
6. **Physical-vector premise, when that conclusion is wanted.** The residual
   direction owns a nondegenerate gauge-kinetic/physical realization. This
   premise is not supplied by the preceding representation theory.

## Theorem

**Declared-content residual-direction theorem.** Under premises 1–5, every
admitted removal or mass route leaves at least one non-Standard-Model abelian
gauge direction. Under premises 1–6, that surviving direction is an extra
physical vector. Without premise 6, only the gauge-direction conclusion is
licensed.

## Proof

The compact/noncompact decomposition has dimensions

`45 = 21 + 24`.

The Standard Model algebra has dimension `8+3+1=12` and lies inside the
21-dimensional compact Pati–Salam algebra. Observation therefore reaches the
24 directions of `p` but leaves nine non-Standard-Model directions inside
`k`. It cannot by itself remove the compact surplus.

An exact D5 root census of the entire two-dimensional Standard-Model-
preserving adjoint orbit space has unbroken dimensions

`{13, 15, 19, 25}`.

Thus no available adjoint orbit has unbroken dimension 12; the generic best
case is the Standard Model plus one abelian direction. The familiar
`(10bar,1,3)` route to dimension 12 belongs to a 126 and is excluded by premise
1 rather than silently added to the carrier.

It remains to ask whether the final direction can acquire a mass by another
declared mechanism. An independent weight-support enumeration finds no
Standard-Model singlet with nonzero residual `B-L` charge in the adjoint 45 or
the declared `10 tensor 45`, so the Higgs route has no owner. No shifting
zero-form is declared, so the Stückelberg route has no owner. Linear, cubic
and mixed `Y^2(B-L)` anomaly sums vanish on the chiral 16, so anomaly
cancellation supplies no Green–Schwarz necessity or owner. The residual
factor is abelian, so the named nonabelian confinement route does not apply.
These exhaust premise 4. At least one abelian gauge direction therefore
survives. Premise 6 is exactly what upgrades that algebraic conclusion to a
physical-vector conclusion. ∎

## Hostile reopeners

The result is deliberately easy to defeat with the right new information.
Any one of the following reopens it: a declared charged singlet such as the
missing 126 component; an action-owned shifting zero-form; an anomaly-owned
Green–Schwarz coupling; a nonabelian residual factor with a confinement
mechanism; an observation map that acts on the relevant compact direction; a
previously omitted orbit; or an authenticated carrier completion. Removing
only premise 6 does not undo the residual gauge direction—it blocks the claim
that the direction is a propagated physical particle.

The executable selftest plants each mutation separately and requires the
corresponding conclusion to fail closed.

## What this settles—and what it does not

This package settles the prior open composition seam: within one frozen
declared-content model, PV-1, PV-2 and MV-2 do form a binary exclusion rather
than a list of suggestive residuals. It strengthens the internal result from
“each route has a problem” to “the enumerated routes jointly leave an abelian
direction.”

It does **not** show that all formulations or future completions of Geometric
Unity contain an observable massless photon. It does not derive a source-owned
action, gauge kinetic term, coupling strength, detector response, cosmological
abundance or experimental prediction. MV-1's empirical fifth-force and
cosmology comparisons are consequently not load-bearing in this theorem.

## Reproduction

Run:

```sh
python3 papers/drafts/declared-content-extra-vector-obstruction/reproduce_all.py
```

The integrated certificate independently recomputes the D5 roots, all orbit
strata, the observation count, declared scalar weight supports and anomaly
sums. It then executes the baseline before eight hostile premise mutations.
