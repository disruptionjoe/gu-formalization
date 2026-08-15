---
artifact_type: exploration
status: exploration
doc_type: exhaustive-mechanism-closure-gate
created: 2026-08-14
work_item: MV-2
channel: photon_and_extra_vector_spectrum
title: "MV-2: all four ways an abelian gauge field can gain mass are closed for GU-as-declared. Higgs (no B-L-charged SM singlet, MJ-5), Stueckelberg (declared content transforms homogeneously, and the inhomogeneous gauge group's translations shift degree 1 where degree 0 is needed), Green-Schwarz (U(1)_{B-L} is anomaly-free, so there is no anomaly for a 2-form to cancel, AC-1), and confinement (B-L is a Cartan direction). Also STRENGTHENS MJ-5: $ has no SM-singlet component at all, which makes MJ-5's own $ check vacuously true."
grade: "EXACT rational weight arithmetic, 27/27, with three firing non-vacuity controls. The mechanism enumeration is a standard field-theory classification, not a novel one; what is GU-native is testing each against the declared content. NOT: a statement about SG4's completion, a dynamical claim, or any claim-status movement."
disposition: ALL_FOUR_ABELIAN_MASS_ROUTES_CLOSED_IN_DECLARED_CONTENT__STUECKELBERG_FAILS_ON_HOMOGENEITY_AND_DEGREE__GREEN_SCHWARZ_FAILS_ON_ANOMALY_FREEDOM__MJ5_DOLLAR_CHECK_WAS_VACUOUS_AND_IS_STRENGTHENED
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/massless-vector-cosmology/
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - lab/active-research/joe-directed/anomaly-cancellation/
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md
scripts:
  - tests/channel-swings/joe_directed_stueckelberg_probe.py
---

# MV-2 — every abelian mass route is closed

## Why this gate

MV-1 left exactly one extra massless gauge boson in GU-as-declared — the
gauged `U(1)_{B-L}` — excluded by equivalence-principle tests at roughly 24
orders in the coupling. Every prior gate (MJ-2, MJ-5, PV-1, SG4-1) tested only
the **Higgs** route. An abelian gauge boson has other ways to become massive
that need no Higgs, no charged scalar and **no 126**, and MJ-2's zero
multiplicity is silent on them. MV-1 named this as the cheapest thing GU could
declare to dissolve four gates at once. It does not work.

## Result — the enumeration is exhaustive and every branch closes

| route | requirement | status in GU-as-declared |
|---|---|---|
| **(a) Higgs** | scalar with `B-L != 0` taking a VEV | **closed** — no SM singlet with `B-L != 0` in `eps` or `$` (MJ-5, re-derived) |
| **(b) Stückelberg** | 0-form shifting inhomogeneously | **closed** — twice over, see below |
| **(c) Green–Schwarz** | the `U(1)` must **be** anomalous | **closed** — `B-L` cubic and mixed traces vanish exactly (AC-1, re-derived) |
| **(d) Confinement** | non-abelian self-coupling | **closed** — `B-L` is a Cartan direction |

**(b) closes for two independent reasons.** First, **homogeneity**: fields in a
linear representation transform as `delta phi = rho(alpha) phi`, and for an
abelian generator `X` the adjoint action on the component along `X` is
`[X,X] = 0`. Verified on weights: every SM-singlet component of the declared
content is exactly `B-L`-neutral, hence *inert*, not shifted. A Stückelberg
field must shift by the gauge parameter, which no linear representation does.

Second, **degree**. GU's inhomogeneous gauge group is a semidirect product
whose translation part is valued in ad-valued **one**-forms — the source is
explicit ("this whole thing is gonna live in ad valued one forms... taking a
semi direct product"). So the translations shift degree-1 objects. Massing a
1-form gauge field requires a shifting **degree-0** object. The degrees do not
match. What those translations *could* Stückelberg is a **2-form** gauge
symmetry, which is a different object entirely.

**(c) is closed by a result from a different route.** AC-1's cross-channel
deliverable — all thirteen SM and `B-L` traces vanish exactly — is precisely
the condition that forbids Green–Schwarz here: with no anomaly, there is
nothing for a 2-form to cancel. The `B-L` cubic and mixed-gravitational traces
over the 16 are re-derived here as an independent control, with a firing
teeth-check (the same cubic on half the 16 does *not* vanish).

## A correction to MJ-5

The non-vacuity controls caught a defect in my own earlier gate.

> **`$` has no SM-singlet component at all** — not merely none carrying
> `B-L`. So **MJ-5's check "`$` has no SM-singlet with `B-L != 0`" is
> vacuously true.**

The correct and stronger statement is that **`$` cannot take an SM-preserving
VEV in any direction whatsoever**. Structural reason, verified: an SM singlet
requires colour `(0,0,0)` with zero weak part, i.e. the zero weight, and
`10 (x) 45` never contains it because a single `+-e_i` can never cancel a
two-entry root. By contrast `eps` genuinely does have SM singlets, so the
`eps` branch of MJ-5 is sound and non-vacuous.

MJ-5's conclusion is unaffected and in fact strengthened; only the grounds for
the `$` half change. This is recorded rather than silently patched because a
vacuously-passing check is exactly the defect `certificate_shape_audit` exists
to flag, and it survived into a committed artifact.

## Claim ceiling

**The four-way enumeration is standard field theory, not a novel
classification**, and no novelty is claimed for it. What is GU-native is
testing each branch against the declared content. The Green–Schwarz branch
rests on AC-1; the Higgs branch on MJ-5; both are cited and re-derived as
controls rather than re-claimed.

**Scoped to GU-as-declared.** Canon makes SG4 the open decider; a completion
declaring a `B-L`-charged SM singlet reopens (a), and a completion declaring a
genuine axionic 0-form reopens (b). SG4-1 already names exactly what (a) would
require: a 16 or a 126.

**Not claimed:** that GU is excluded — MV-1's own ceiling stands, and the
exclusion is of GU-as-declared, not of GU. Nor is anything claimed about
whether GU's connection sector actually gives these directions Yang–Mills
kinetic terms, which MV-1 flagged as load-bearing and imported.

## Consequence

The `U(1)_{B-L}` problem is now **structural rather than incidental**: it is
not that GU happens to lack the right field, but that *every* mechanism by
which an abelian gauge boson can become massive is closed simultaneously in the
declared content. Combined with MV-1's ~24-order equivalence-principle gap,
and with the fact that the same missing object underlies MJ-2, MJ-5, PV-1 and
CU-1, this is the fifth independent consequence of one absence.

Repository-wide GU priority is unchanged, the superposition / source-residual
workstream is untouched, and no ledger, canon, or current-state surface moves.
