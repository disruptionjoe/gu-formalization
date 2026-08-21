---
title: "Selected-K77 CBRS-1D coupled grade-two connection/T first-jet rigidity"
status: active_research
doc_type: exact_class_obstruction
created: "2026-08-21"
registry: lab/process/selected-k77-cbrs1d-coupled-grade2-connection-jet.json
probe: tests/channel-swings/selected_k77_cbrs1d_coupled_grade2_connection_jet_probe.py
grade: "EXACT ONE-INCIDENCE COUPLED GRADE-TWO FIRST-JET CLASS KILL; NOT A FULL GRADE-TWO OR FULL CLIFFORD THEOREM"
target_claim: NONE-NOT-A-KILL
source_return: SOURCE_CONFIRMS_TWO_CONNECTION_MOVING_SHIAB_PRIMITIVE_EPSILON_AND_METX_GRAMMAR__REPO_DERIVES_AND_KILLS_THIS_FROZEN_COUPLED_INCIDENCE__SOURCE_SILENT_ON_THE_CLASS
canon_verdict_change: none
---

# Selected-K77 CBRS-1D coupled grade-two connection/T first-jet rigidity

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `lab/methods/source-native-comparator-routing.md` and follow its source-native
> pointers before reusing this result.

Classification: `INTERNAL_STRUCTURAL_ONLY`

```gu-typed-objects
result: CBRS-1D lexicographically first coupled grade-two connection/T one-axis jet rigidity and metric-trace class kill
carrier: Omega1_base_tensor_span{B_s_gamma01,T_s_gamma01} at the K77 anisotropic point LAYER=ambient CHIRALITY=N/A
pairing: K77 Clifford scalar-density pairing ON=Omega1_Cl77
real_structure: K77 real Spin(7,7) grade-two connection inside the u(64,64) comparator
grading: exterior form degree and Clifford grade
action_owner: repository-construction
target: coupled field prolongation primitive-epsilon covector and intrinsic metric covector MAP-TYPE=evaluation
```

## Result first

The lexicographically first honest grade-two successor to CBRS-1C is rigid
once the connection owner is included. Keep the anisotropic point

```text
(a,b)=(-13/96,1/48)
```

and one labelled base axis. In form slot zero, let `p` multiply the first real
Spin blade `gamma_0 gamma_1` in the connection and let `q` multiply the same
blade in `T`. The exact selected action restricts to

```text
I(p,q) = 221/55296 - p q/24 + 17 q^2/36.
```

Both first derivatives vanish at `(p,q)=(0,0)`. The first prolongation of the
coupled field equations is therefore

```text
[   0    -1/24 ] [p'] = [0]
[ -1/24   17/18] [q']   [0].
```

Its determinant is `-1/576`, so the only on-shell one-axis jet in this frozen
coupled incidence is

```text
p'=q'=0.
```

This cross term is load-bearing. Dropping the connection-to-`T` coupling
creates a false connection zero mode. Conversely, a lone `T` jet fires the
connection equation and a lone connection jet fires the `T` equation. CBRS-1D
therefore repairs the type error identified by CBRS-1C rather than repeating a
lone coefficient test.

## Complete covector cross-check

The exact symbolic adjoint was split into independent `E_B` and `E_T`
covectors. It covers the complete `14 x 16,384` real pointwise `T` bank plus
the `14 x 91` real Spin-connection bank, `230,650` admitted pointwise
directions before restriction. Differentiating both covectors with respect to
`p` and `q` gives support counts

```text
p -> E_B: 12     p -> E_T: 13
q -> E_B: 13     q -> E_T: 13.
```

Projection back to the selected cells reproduces the same `2 x 2` matrix
exactly. The result is therefore not an interpolation-only or reduced-action
shortcut.

## Primitive epsilon and held-out metric return

At the anisotropic point, the exact momentum `E_B-E_T` has fourteen one-cell
rows, all in Clifford grade one. Its restriction to the Spin grade-two
connection owner is zero. The moving-Shiab primitive-epsilon return vanishes
on all 91 Spin generators. Since coupled field rigidity forces the admitted
one-axis momentum derivative to zero, both source-owned terms in

```text
E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S
```

vanish on this carrier.

CC-01 remains binding. At fixed `varpi`, the intrinsic metric equation is

```text
E_g = rho I + (D_g B_Z)^! (E_B-E_T).
```

The on-shell coupled jet is zero, so the graph-adjoint return is zero. The
held-out density remains `221/55296` and the normalized metric row remains

```text
(-221/27648,0,0,0,221/27648,0,0,221/27648,0,221/27648).
```

It is nonzero. This selected coupled incidence closes before second jets,
full Hessian, stabilizer, `mu6`, `J`/Higgs, photon, extra-`U(1)`, or
gravitational-spectrum work is admissible.

## Prior-art and source fence

CBRS-1A through CBRS-1C froze the anisotropic point and killed the `a/b`,
grade-zero, and representative grade-one derivative modules. They explicitly
left grade two open because a lone `T` cell would omit the connection owner.
The August 9 moving-epsilon work already owns the general `D_B eta` and
moving-Shiab grammar; this result consumes that grammar rather than claiming
it anew.

The released source supplies the two-connection action, moving Shiab,
primitive-epsilon, and `MET(X)` argument structure. It does not supply this
anisotropic CBRS carrier, reduced polynomial, exact matrix, or class verdict.

## Hostile return and exact successor

- **Strongest overclaim:** one lexicographically first incidence is not the
  full `14 x 91` grade-two incidence module.
- **Strongest contrary construction:** the first off-incidence control, form
  slot two with the same `gamma_0 gamma_1` blade, has restricted matrix
  `diag(0,-1)`. Its connection column is flat. That direction is retained and
  must be classified by the gauge orbit, primitive epsilon, and metric graph.
- **Strongest mistyping:** `p` is a connection coefficient; it is not itself
  the primitive-epsilon gauge parameter or an endpoint charge.
- **Weakest propagation seam:** zero metric-graph return follows from the
  rigid selected jet, not from a universal factorization across all grade-two
  incidences.

CBRS-1 remains active at `CBRS-1E`. Before any second jet, classify the
symmetry-inequivalent grade-two incidence orbits, beginning with the exact
off-incidence flat connection control. Decide which flat columns are gauge
or primitive-epsilon characteristics and whether any surviving quotient class
has a nonzero metric-graph image.

No ledger verdict, source ownership, canon, residue, quotient datum, or public
posture changes. No physical vacuum, cohomology, particle assignment,
prediction, or confirmation follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_cbrs1d_coupled_grade2_connection_jet_probe.py
```

The exact probe passes `43/43`.
