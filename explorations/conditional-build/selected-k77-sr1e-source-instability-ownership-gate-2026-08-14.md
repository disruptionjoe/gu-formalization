---
title: "Selected-K77 SR-1E source-instability ownership gate"
status: active_research
doc_type: exact_interface_type_gate
created: "2026-08-14"
registry: lab/process/selected-k77-sr1e-source-instability-ownership-gate.json
probe: tests/channel-swings/selected_k77_sr1e_source_instability_ownership_gate_probe.py
grade: "EXACT CARRIER/VARIATIONAL INTERFACE GATE; SOURCE INSTABILITY DOES NOT YET INSTANTIATE A CANONICAL POINT/FIRST-JET BRANCH"
canon_verdict_change: none
---

# Selected-K77 SR-1E source-instability ownership gate

## Result first

The source Mexican-hat result is genuine new evidence for branch generation,
but it does **not** yet construct the distinct canonical point/first-jet branch
required by `SR-1E`.

The source result owns a symmetric traceless quadratic mass form on constant
modes,

```text
M[(mu,B),(nu,C)] = F0^(mu nu A) f_ABC,
dim = 10 x dim so(6,4) = 10 x 45 = 450.
```

For every nonzero background curvature, `M` has both signs, so some tachyonic
direction exists. That is an exact instability theorem. The selected-K77
canonical branch, however, lives at point grade in

```text
Omega^1(Y14, so(7,7)),
dim = 14 x 91 = 1274,
```

before its first jet is supplied. The dimensions differ by `824`; the groups,
base directions and object roles differ as well. The source packet itself
records the spin-zero representation/placement map as absent. No source-owned
equivariant map from the `450`-dimensional constant-mode carrier to the
labelled `1274`-dimensional K77 point carrier is presently serialized.

Even after such a carrier map, a negative Hessian direction is not a nonlinear
critical point. Along a selected line with

```text
V(a) = lambda a^2 + q a^4,
```

one needs `lambda<0`, a stabilising `q>0`, and the nonzero critical amplitude
`a^2=-lambda/(2q)`. Fresh SRC-3 evidence now decides the declared norm-square
route: the unique Ad-invariant/DeWitt pairing has an explicit `K=-4<0` ray, so
that potential is unbounded below. This remains conditional because SG4 does
not declare the actual quadratic form and the full Shiab/eddy action may add a
repair. The mass-form result alone proves no vacuum or breaking pattern.
Symmetry, tracelessness and nonzeroness cannot select a fixed line: exact
two-dimensional controls with `diag(-1,1)` and `[[0,1],[1,0]]` obey the same
theorem but have different negative directions.

Thus the new evidence supplies `EXISTENCE_OF_AN_INSTABILITY_DIRECTION`, not
`SELECTED_CANONICAL_NONLINEAR_POINT_FIRST_JET`. It cannot reopen the killed
SR-1C fibre, but it sharpens SR-1E from a broad branch search to one explicit
six-object bridge contract.

## Minimum bridge contract

A source-instability route may enter SR-1E only after one packet owns all of:

1. an exact equivariant carrier map from the source `450D` constant modes to
   the selected K77 `1274D` point-`T` carrier;
2. one exact source-owned negative line or orbit, not a basis-chosen floating
   eigenvector;
3. the full-action nonlinear potential restricted to that same line or orbit,
   including an exact repair of the SRC-3 negative quartic ray or an explicit
   alternative to the undeclared norm-square;
4. a nonzero exact critical amplitude from the restricted Euler equation;
5. a labelled canonical-`B_Z` compatible first-jet lift satisfying inherited
   Bianchi rows; and
6. point translation, `j1E_T`, `j1E_B`, primitive epsilon and total
   fixed-`varpi` metric rows recomputed on that one carrier.

The first kill/switch condition is now precise. If no equivariant carrier map
exists, the source instability is disjoint from selected K77. If the map
exists but the full action leaves a nonpositive or degenerate quartic, the
route is unstable rather than a Mexican-hat vacuum. If a stable critical orbit
exists but no source-owned selector chooses it, the branch remains
noncanonical and cannot instantiate VRS-5.

## Scope and consequence

This is `TYPE-MISSING`, not a no-go for source symmetry breaking. The automatic
instability may still generate the needed branch after the six objects above
are constructed, but the declared norm-square route is now killed unless the
full GU action repairs the exact negative quartic ray. It also does not absorb
the Joe-directed Majorana channel; repository-wide priority remains unchanged.

`SR-1` remains `BACKGROUND-MISSING`; `SR-2` and `VRS-6` remain blocked. No
ledger, canon, residue, quotient datum or public posture changes. No physical
cohomology, superposition law, Born rule, spectrum, Standard Model selection or
empirical prediction follows.

Reproduce with:

```bash
python3 tests/channel-swings/selected_k77_sr1e_source_instability_ownership_gate_probe.py
```

The exact/interface probe passes `45/45`.
