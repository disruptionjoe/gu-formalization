---
title: "LT-GR8 forward track, step one: typing the K77-to-observed-3+1 carrier and boundary map"
status: active_research
doc_type: exact_typing_and_boundary_census_result
created: "2026-08-22"
directed_by: "Joe direct chat, 2026-08-22 (execute the admitted LT-GR8 typing swing)"
registry: lab/process/selected-k77-ltgr8-observed-boundary-carrier-typing.json
probe: tests/channel-swings/selected_k77_ltgr8_observed_boundary_carrier_typing_probe.py
grade: "EXACT FINITE METRIC-ONLY TYPING AND BOUNDARY-TYPE CENSUS; NO BACKGROUND, NO HORIZON EXISTENCE, NO ENTROPY OR TEMPERATURE OBJECT, NO STATE SPACE, NO CBRS-2 ADVANCE, NO GU VERDICT"
target_claim: ledger row LT-GR8 (verdict NEEDS unchanged); this artifact types the missing bridge's carrier and boundary components and certifies which boundary objects are post-observation-only under metric-only typing
canon_verdict_change: none
---

# LT-GR8 forward track, step one: typing the K77-to-observed-3+1 carrier and boundary map

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

`GU-COMPARATOR-ROUTING-CLASSIFICATION: BRIDGE_OR_SEMANTIC_BOUNDARY`

Scope: this artifact executes the licensed first step of the LT-GR8 forward
track — "type the K77-to-observed-3+1 carrier and boundary map" — at typing
grade only. The bordered comparator is the Jacobson horizon-thermodynamics
family (EXT-J95); mechanism commitment and confirmation credit remain NONE.
Notation is declared plus-first (positives first) throughout, matching the
author's one-equation display `TY^{7,7} = TX^{1,3} + N^{6,4}`
(PD-SOURCE-NOTATION).

```gu-typed-objects
result: metric-only typing of the observation-side carrier split, the null-hypersurface conormal lift, the characteristic-cone descent asymmetry, the causal-orientation non-lift, and the six-way boundary-type census for the LT-GR8 bridge
carrier: T_(s(x))Y^14 = H + V with q = q_H + q_V, sig(q_H)=(1,3), sig(q_V)=(6,4), plus-first LAYER=ambient+observed BRIDGE=section-restriction CHIRALITY=N/A
pairing: the ambient chimeric quadratic form and its dual, block-diagonal over the observed section split ON=finite-tangent-witnesses
real_structure: real; no spinor, Krein, or complex-structure claim is made here
grading: none used; all statements are degree-zero finite quadratic-form facts
action_owner: N/A -- no action term, boundary law, entropy density, temperature, ensemble or measure is selected or constructed; K104's released-source census (no physical boundary law) is inherited, not modified
target: LT-GR8's composite missing bridge, carrier and boundary components MAP-TYPE=UNTYPED -- the artifact separately types restriction, pullback, conormal lift and a non-lift
```

## Result first

Four exact metric-only facts, each machine-checked over exact rationals by the
probe, fix what the LT-GR8 bridge's boundary component IS and where it can
live:

- **T-1 (restriction).** The ambient form restricted to the horizontal
  (observed) subspace is the observed Lorentzian form: the ambient null cone
  meets `H` exactly in the observed null cone.
- **T-2 (null-hypersurface conormal lift).** The dual form is block-diagonal,
  so a hypersurface conormal lifted from the observed side with zero vertical
  component is ambient-characteristic exactly when it is observed-null. The
  bundle preimage of an observed null hypersurface is therefore
  ambient-characteristic: this single boundary-map component exists at
  metric-only typing grade.
- **T-3 (descent asymmetry).** The ambient characteristic cone is a
  13-dimensional quadric cone; the lifted-from-observed subfamily is
  3-dimensional. Ambient characteristic data does not descend to observed
  null data without the observation map: the lift direction exists, the
  descent direction is not metric-only.
- **T-4 (causal-orientation non-lift).** In the observed `(1,3)` form the
  positive (timelike) set has exactly two components — the sign of the
  positive-axis coordinate never vanishes on it — and this future/past datum
  is what a causal horizon, Rindler wedge, or Clausius sign requires. In the
  ambient `(7,7)` form the positive set is connected: an explicit exact
  rational path joins a positive horizontal vector to its negative through
  everywhere-positive vectors using one positive vertical direction. So the
  observed future/past distinction is not the restriction of any locally
  constant ambient datum: **under metric-only typing, causal orientation —
  and with it every causal boundary object — exists only after observation.**

T-4 upgrades the council's default placement ("the Jacobson benchmark
primarily belongs after the K77 observation map in the physical observed
`3+1` system") from a protocol choice to an exact kinematic certificate, with
a stated ceiling: the certificate binds the metric alone. Any ambient
causal-orientation owner would be genuinely new structure (a distinguished
vector field, polarization, or domain selection) and would need a
source/action owner; the released-source census supplies none (K104).

## Carrier typing (assembled, with receipts)

- Native carrier: `Y^14` with the chimeric metric; over an observed section
  value the tangent splits `H + V` with `sig(q_H) = (1,3)`,
  `sig(q_V) = (6,4)`, total `(7,7)`; the fibre form is base-sign independent
  (`PD-SIGNATURE-PARITY`, `tests/signature_fork_equivariance_defect.py`), and
  the author's eq. (12.19) is the one-notation display
  (`lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md`).
- Observed carrier: `X^4` with the section-induced Lorentzian `(1,3)` form.
- Observation map: pullback along the section `s` (a metric `g`),
  `s^*: Omega^1(Y) -> Omega^1(X)` — a contraction, not a projection, and
  surjective onto `T^*X` (`MD-1`, 67/67;
  `lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md`).
- Analytic domain: the ambient operator is first-order ultrahyperbolic; the
  Cauchy problem is ill-posed by default and any domain must be supplied, not
  assumed (`PD-ULTRAHYPERBOLIC-DOMAIN`).

## Boundary-type census (the W151 separations, typed)

The ledger's required separations name six boundary types. Under metric-only
typing:

| boundary type | observed-side object | ambient-side status | owner status |
| --- | --- | --- | --- |
| local Rindler horizon | causal: null hypersurface + future/past choice + boost flow | conormal lifts (T-2); orientation does not (T-4): POST-OBSERVATION ONLY | needs an observed background; instantiation blocked on CBRS-1 |
| cosmological horizon | causal, global | same as above, plus global observed structure | same |
| York / quasilocal ensemble boundary | imposed timelike boundary + ensemble | not causal-native; an imposed-boundary system is a different system (source pack) | action boundary term MISSING — released source supplies no physical boundary law (K104) |
| analytic operator-domain boundary | n/a (ambient object) | ambient-native NEED: nonlocal-constraint remedy class, codimension-one only | distinct from every causal type; do not identify (PD-ULTRAHYPERBOLIC-DOMAIN) |
| BV--BFV boundary | action-owned boundary data | boundary law unowned; full-G equivariance cannot select the fixed balanced zero level (K104, K103 routes unselected) | MISSING OWNER |
| capability / measurement boundary | records/measurement object (W151) | proposed typed bridge only; identity with any causal horizon outruns evidence (W151 correction) | UNPROVED BRIDGE |

No two rows may be identified without a constructed map satisfying the
six-item bridge burden of `lab/methods/source-native-comparator-routing.md`.

## Missing-owner ledger for the LT-GR8 packet

Against the seven components of LT-GR8's revival trigger:

1. **Causal boundary** — typed here: post-observation-only (T-4); its lift
   half exists (T-2). Instantiation needs an actual observed background:
   blocked on CBRS-1.
2. **Canonical reduction / constraints** — CBRS-2; dependency-blocked.
3. **Entropy density with frozen normalization** — MISSING OWNER: no
   physical state space or positive pairing exists (K106/K107, conditional).
4. **Temperature or KMS state** — MISSING OWNER: requires a state and a flow;
   blocked behind the same positivity burden.
5. **Stress-energy flux** — PARTIAL: native Hilbert-stress maps exist at
   reconstruction grade; the observed-side composition through `s^*` is
   untyped.
6. **Equilibrium or entropy-production law** — MISSING OWNER: the released
   source names the ultrahyperbolic boundary problem but supplies no physical
   boundary law (K104).
7. **Held-out consequence** — RESERVED-AT-PACKET-TIME: none frozen; freezing
   one before target comparison is the no-retuning protocol's requirement.

## Route selection and hostile review

The census ran a Lorentzian-geometry lens (which causal objects require an
orientation datum), a quadratic-forms/linear-algebra lens (block restriction,
dual-form lift, cone dimensions, connectedness witnesses — all exact over the
rationals), a PDE/domain lens (characteristic versus causal versus analytic
domain boundaries kept distinct), a comparator-routing semanticist lens (the
Jacobson family stays a scoped comparator; no forbidden summary grammar), and
a hostile claim-ceiling lens. The hostile pass pressed two attacks. First,
"T-4 kills ambient physics": it does not — it is a metric-only statement, and
an action- or source-owned selector could still supply ambient structure; the
certificate only prices that selector as a missing owner rather than a free
default. Second, "this is CBRS-2 by another name": it is not — no background,
region, constraint, reduction, state space, or physical selection is
constructed; every physical component above is typed as missing or blocked,
none is discharged.

The strongest overclaim would read T-2 as "GU has a horizon": T-2 lifts
conormal nullness only, and a horizon additionally needs the orientation and
dynamical data typed as post-observation or missing. The weakest propagation
seam is a future artifact quietly treating an ambient characteristic surface
as a causal boundary; the probe pins the census rows and the T-4 witnesses
together.

No scientific ledger verdict, canon, source ownership, prediction credit, or
public posture changes. LT-GR8 remains `NEEDS`/`MISSING_CONSTRUCTION`; a
conditional evidence delta records the typed refinement for canonical
Progress disposition.
