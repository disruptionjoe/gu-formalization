---
title: "Source-native versus conventional-comparator routing"
status: active_method
doc_type: mandatory_semantic_and_inference_boundary
created: "2026-08-14"
registry: lab/process/source-native-comparator-routing-registry.json
audit: process_gates/source_native_comparator_routing_audit.py
---

# Source-native versus conventional-comparator routing

## Mandatory rule

A result about a conventional particle-physics construction binds only the
construction it actually tested. It does **not** become evidence for or against
Weinstein's differently constructed GU mechanism merely because both objects
are called “Higgs,” “generation,” “chirality,” “Majorana mass,” “symmetry
breaking,” or “gauge-boson mass.”

The recurring conventional models below are not the operative GU models. They
remain useful as controls, comparisons and bridge targets, but their failure
must be reported as `CONVENTIONAL_ROUTE_EXCLUDED` or, where appropriate,
`STANDARD_TRANSLATION_INVALID`.

They may not be summarized as “GU became more adverse,” used to change a
hypothesis vote, or promoted into the next GU task unless an artifact proves a
typed bridge from the source-native carrier, action and reduction to the
comparator's carrier, action and observable.

## The four recurring forks

### 1. Ordinary family index or net chirality versus Weinstein's `2+1`

The comparator is three repeated four-dimensional chiral spin-1/2 families
derived from an ordinary compact family index, anomaly count or net chiral
index. Weinstein's stated target is different: the total theory remains
non-chiral, while the observed low-curvature split is meant to arise through
an asymmetric `2+1` construction involving two true-family sectors, an
effective imposter/remainder sector, observation pullback and still-open
BV/boundary/domain descent.

An ordinary index obstruction is therefore not a generation obstruction for
the GU-native route. A standard net-chirality calculation is not a chirality
no-go for a balanced bulk whose observed sectors may separate only after
observation and reduction.

Read first:

- `CURRENT-STATE.yaml`, the paragraph beginning “Weinstein's total theory
  remains explicitly non-chiral”;
- `lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md`;
- `explorations/signature-chirality-conjugation-check-2026-08-13.md`; and
- `explorations/chirality-grading-and-77-rerun-2026-08-03.md`.

### 2. Standard Higgs/VEV versus the connection-curvature mechanism

The comparator is a separate four-dimensional scalar Higgs—including a
standard SO(10) `126` VEV—with an independently supplied Mexican-hat potential
and Yukawa coupling. Weinstein explicitly describes a different mechanism:
there is “no Higgs” as a separate primitive; an `ad`-valued connection
perturbation `a in Omega^1(ad)` enters `||F||^2`, background curvature supplies
the quadratic sign, and `a wedge a` supplies the quartic.

> [!CAUTION]
> **Withdrawn clause — this paragraph previously ended “…and vertical
> connection components may appear as four-dimensional scalars after
> reduction.” That clause is (a) not source-attested and (b) refuted.**
>
> **Not source-attested.** The three preceding clauses are verified verbatim
> against the primary transcript at `[00:42:42]`–`[00:43:04]` (see
> `lab/active-research/joe-directed/majorana-126-neutrino/src1-...`). The
> fourth is not in that passage, and it restates the Kaluza–Klein reduction the
> source **explicitly disavows**: *“It’s not extra dimensions. It’s not Kaluza
> Klein. The space that is four dimensional births its own 14 dimensional
> ambient space.”* Attributing it to Weinstein inside a mandatory boundary was
> the error.
>
> **Refuted.** The observation reduction is a **contraction, not a projection**
> — `(s^*omega)_mu = omega_mu + omega_(ab) d_mu g_ab`, surjective onto `T*X` —
> so an ad-valued one-form descends to a **one-form**, not to scalars (`MD-1`,
> 67/67). `LA-8` (78/78) then ran both horns of the open `SOLDERED-AD` fork to
> a number: the sector is `45` under the inert horn and exactly `1` under the
> soldered horn, against the `450` this clause implied, and **both horns carry
> zero doublets**. The fork being open does not rescue the clause.
>
> This is recorded rather than silently deleted because the clause sat in a
> `mandatory_semantic_and_inference_boundary` for agents to read, and every
> reader of it re-imported the refuted step — the exact failure mode this
> document exists to prevent, occurring inside the document itself.

Thus absence, repulsion or nonselection of a conventional `126` VEV excludes
that comparator only. It does not adjudicate the curvature-induced connection
mechanism.

Read first:

- `explorations/layer0-pass-on-the-two-higgs-objects-2026-07-29.md`;
- `explorations/vertical-vev-chirality-bridge-2026-07-29.md`;
- `lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md`; and
- `lab/active-research/joe-directed/majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md`.

### 3. VEV-only breaking versus observation plus the later action layer

The comparator asks a conventional VEV to perform the complete reduction to
the Standard Model and give every unwanted vector a mass. GU assigns part of
the reduction to observation—the selection of four-dimensional geometry
inside the larger arena—and separately requires the later
Yang--Mills--Higgs/connection layer. A stabilizer or vector-mass calculation
that omits either half is not a test of the composed source-native mechanism.

Read first:

- `lab/active-research/pati-salam-chain-verification.md`;
- `explorations/layer0-pass-on-the-two-higgs-objects-2026-07-29.md`; and
- `lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md`.

### 4. Standard Majorana/anomaly/unification diagnostics versus native owners

The standard `126` Yukawa, anomaly cancellation as a family selector,
ordinary perturbative coupling unification and familiar baryon-number tests
are admissible comparators. None is automatically the owner of Weinstein's
claimed mechanism. Before applying one, identify the source claim, carrier,
action term, observation map and physical observable that make it relevant.
Absent that bridge, retain the calculation as a scoped control.

## Required artifact notice

Every live artifact that contains or directly borders one of these comparators
must repeat this notice near its top:

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

The notice is deliberately uniform so agents and audits can find it. An
artifact may then state whether it is a `CONVENTIONAL_COMPARATOR`, a
`SOURCE_NATIVE_ROUTE`, or a `BRIDGE_OR_SEMANTIC_BOUNDARY`.

The registry and audit stamp every current high-risk working artifact. Canon,
published papers, primary-source transcripts and archives are not rewritten to
retrofit this method; `AGENTS.md` applies this boundary whenever an agent reads,
cites or reuses those historical surfaces. Any new work derived from them must
carry the notice and classification.

## Bridge burden

A bridge is not a shared informal role. It must type, at minimum:

1. the two carriers and their real structures;
2. the map induced by observation/reduction;
3. the action term or variational owner on both sides;
4. the quotient, boundary and analytic domain if physical modes are claimed;
5. the observable whose value is being transported; and
6. why the comparator's failure condition pulls back to the GU-native object.

Without those six items, the comparator remains scientifically useful but
logically non-adjudicating.

## Summary grammar

Allowed:

```text
The standard 126-VEV route is excluded. Weinstein's curvature-induced
connection route is a distinct object and remains governed by its own gates.
```

Forbidden:

```text
GU's Higgs mechanism is excluded.
Particle physics became more adverse.
The family-index failure counts against Weinstein's 2+1 claim.
```

The forbidden sentences become available only after a bridge satisfying the
burden above has been constructed and checked.
