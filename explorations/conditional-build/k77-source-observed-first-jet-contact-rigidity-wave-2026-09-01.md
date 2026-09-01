---
title: "K77 source-observed first-jet substitution rigidity wave"
status: active_research
doc_type: reverse_scaffold_source_observed_first_jet_bridge_result
date: 2026-09-01
claim_ceiling: exact one-axis off-shell rigidity for regular first-jet substitutions between positive first-order kinetic Lagrangians modulo first-jet boundary terms; no full-carrier, indefinite, singular, higher-jet, nonlocal, auxiliary-field, on-shell or gauge-reduced equivalence
manifest: lab/process/k77-source-observed-first-jet-contact-rigidity-wave.json
probe: tests/channel-swings/k77_source_observed_first_jet_contact_rigidity_probe.py
---

# K77 source-observed first-jet substitution rigidity wave

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`

```gu-typed-objects
result: regular first-jet substitution rigidity for a positive one-axis kinetic term
carrier: one real source field t and one real observed field q on a one-dimensional base LAYER=conditional CHIRALITY=N/A
pairing: positive repository-owned source kinetic coefficient h(t) and a first-order observed target modulo a first-jet boundary term
real_structure: real C2 substitutions Phi(q,v), with v=dq/dx, tested on the full second-jet space (q,v,a)
grading: jet order through two; no gauge, BRST or BV quotient is supplied
action_owner: source owns only the I1B cubic transgression grammar; h, the target action and enlarged bridge test are repository-derived
target: existence of an off-shell variational bridge t=Phi(q,dq/dx) that avoids the prior point-map normal form MAP-TYPE=classification
```

## The enlarged map class

Freeze one base coordinate `x` and write

```text
L_src(t,t_x)=(1/2)h(t)t_x^2-P(t),       h(t)>0,
L_tgt(q,q_x)=K(q,q_x)-Q(q).                         (1)
```

Allow a regular local first-jet substitution

```text
t=Phi(q,v),       v=q_x,       a=q_xx.              (2)
```

The comparison is off shell on the full second-jet space and may differ by a
first-jet boundary term `D_x B(q,v)`. This is the smallest explicit
derivative-dependent horn left by the point-map packets: it enlarges the map
without importing a nonlocal kernel, extra field or equation-of-motion
identity.

## Acceleration-square rigidity

Differentiating (2) gives

```text
t_x=Phi_q v+Phi_v a.                                (3)
```

Therefore the pulled-back source kinetic term has polynomial dependence

```text
(1/2)h(Phi)(Phi_q v+Phi_v a)^2
 = (1/2)h(Phi)Phi_v^2 a^2
   +h(Phi)Phi_q Phi_v v a
   +(1/2)h(Phi)Phi_q^2 v^2.                         (4)
```

The first-order target contains no `a`. A first-jet boundary term is

```text
D_x B(q,v)=B_q v+B_v a,                             (5)
```

which is at most linear in `a`. Exact equality for every second jet thus
forces the `a^2` coefficient to vanish:

```text
h(Phi)Phi_v^2=0.                                    (6)
```

Positivity of `h` gives `Phi_v=0`. Every regular bridge in this frozen class
is consequently a point transformation `t=phi(q)`, and the previous geodesic
normal form applies:

```text
F(phi(q))=plus-or-minus sqrt(mu) q,
F(t)=integral_0^t sqrt(h(s)) ds.                    (7)
```

The first-jet enlargement therefore supplies no new coefficient freedom under
these assumptions. This is stronger than simply choosing a derivative-free
ansatz: derivative dependence was admitted and then removed by the off-shell
highest-jet coefficient.

## Exact assumption boundary

Equation (6) is an order argument, not a universal field-redefinition theorem.
It uses all of the following:

- one base direction with a positive nondegenerate kinetic coefficient;
- a regular finite first-jet substitution;
- off-shell equality on the full second-jet space;
- a first-order target and a boundary term depending on first jets only; and
- no auxiliary fields whose elimination could cancel the highest-jet square.

An indefinite multidimensional contraction can have null highest-jet symbols;
a singular map can evade division by `h`; a higher-jet or nonlocal boundary
functional can alter derivative order; and an on-shell or gauge-reduced
equivalence need not be a polynomial identity on free second jets. None of
those classes is decided here.

## Hostile review and ceiling

The strongest overstatement would extend the one-axis positive-symbol result
to the full rank-1920 carrier. The contrary cases above block that extension.
The strongest apparent escape is a nonzero `Phi_v`; equation (4) shows that it
necessarily leaves an uncancellable positive acceleration square inside the
frozen class. The weakest reproducibility seam is allowing an unspecified
higher-jet boundary functional after the result and still calling the target
first order.

The packet is repository-derived and conditional. It does not provide the
source-owned full-carrier metric, gauge quotient, physical domain or actual
bridge. It earns no source-action, physical-state, prediction, confirmation,
held-out or GU-verdict credit.

## Next condition

Freeze an independently owned full-carrier principal symbol, gauge complex and
domain, then repeat the highest-jet test for all tensor directions. Otherwise
advance only with a fully specified singular, auxiliary-field, higher-jet,
nonlocal, on-shell or gauge-reduced map whose induced operators are fixed
before comparison with the target.
