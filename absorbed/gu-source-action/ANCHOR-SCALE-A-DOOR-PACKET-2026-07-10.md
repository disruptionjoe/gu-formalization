---
title: "Anchor-Scale A-Door Packet"
status: exploration
doc_type: packet
date: "2026-07-10"
---

# Anchor-Scale A-Door Packet

## Scope

This is the second hourly-progress swing from `NEXT-STEPS.md`: test the unbroken graded-IG
scalar-spinor A-door against the actual Cl(9,5) representation anchors before attempting BV closure.

This packet does not build `S_IG` and does not change the generation-count verdict. The tracked source-action
test below is a lightweight necessary-condition gate. During this swing, the repo's tracked anchor-scale
exact legs under `tests/anchor-scale/` were also run serially; those corroborate a stronger finite-fiber
closure statement.

## Built Artifact

Executable fork:

- `lib/anchor_scale_a_door.py`
- `tests/test_anchor_scale_a_door.py`

Run:

```text
python tests/test_anchor_scale_a_door.py
```

## Result

Tracked lightweight-gate verdict:

```text
PARTIAL_PASS_BV_TAU_BLOCKED
```

What passes at anchor scale:

- the repo anchors remain fixed: bare commutator `58.7215`, `C2 = 155.3625`;
- `Gamma` has rank `128`, so `ker Gamma` has dimension `1664`;
- each non-null component scalar-spinor shift `S -> V tensor S` has full-rank gamma trace;
- those shifts have both a kernel component and a normal component, so they are not tangent to `ker Gamma`;
- the component shifts are compatible with the quaternionic/H-linear anchor;
- the spinor Krein form has signature `(64,64,0)` and the component pullbacks preserve that Krein structure.

What remains blocked:

- the null direction `e_0 + e_9` has gamma-trace rank `64`, so half of the component-shift scalar-spinor
  directions are tangent to `ker Gamma` there;
- therefore the derivative-level `tau_plus` choice and the BV/Koszul-Tate closure remain the construction
  wall;
- no anomaly, families-pushforward, security-budget selection, or generation-count claim follows.

## Active Exact Corroboration

The repo also contains exact anchor-scale legs under `tests/anchor-scale/`. I did not edit or move them, but
I ran the following checks serially:

| Check | Result |
|---|---|
| `python tests/anchor-scale/leg1_anchor_super_jacobi.py` | 64 checks passed; finite-fiber graded IG extension closes on the Cl(9,5) / `u(64,64)` anchor. |
| `python tests/anchor-scale/leg1_crosscheck.py` | 9 checks passed; corroborates the load-bearing noncentral kill and balanced central escape. |
| `python tests/anchor-scale/indep_verify.py` | 16 checks passed; independent gamma basis and engine confirm signature `(64,64)`, real-not-complex bilinear, noncentral kill, and balanced central closure. |
| `python tests/anchor-scale/leg2_krein_real_form.py` | 35 checks passed; real/Krein form survives without complexification; finite frozen `tau_plus` shadow preserves Krein reality. |

Read from those active checks: the toy B1 algebra does survive the honest finite anchor fiber more strongly
than the lightweight gate alone shows. The semisimple gauge-valued odd bracket is still killed; the new
anchor-scale feature is a balanced central `u(1)` escape. The real/Krein layer is decided at finite-fiber
level. The genuine derivative-level homomorphism remains blocked on the missing geometric data: the
connection on `Y`, the covariant first-order `d_aleph`, and the curvature identity tying
`F_aleph = d_aleph^2` to the base.

## Handoff

The next reasonable hourly progress point is:

```text
MINIMAL-BV-CLOSURE
```

That run should attempt the smallest non-equivariant, anti-trap compensator plus Koszul-Tate leg that could
force the gamma-trace constraint by Noether identity. The null-direction tau caveat above is an explicit
failure condition: if closure only works by ignoring it or by driving the bare commutator to zero, the
candidate fails.

Update after `MINIMAL-BV-KT-CLOSURE-PACKET-2026-07-10.md`: the finite-fiber BV/Koszul-Tate closure attempt
partially passed after projecting the gauge map into `ker Gamma`. The remaining blocker is source-derived
Noether/tau data that explains that projection rather than assuming it.
