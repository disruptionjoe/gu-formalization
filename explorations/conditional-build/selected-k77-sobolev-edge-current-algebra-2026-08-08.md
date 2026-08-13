---
artifact_type: construction_and_composition_result
created: 2026-08-08
status: COMPACT_BOUNDARY_STRONG_SOBOLEV_EDGE_REDUCTION_EXACT_CONDITIONALLY_ON_NONEMPTY_EDGE_TORSOR__CHARGED_CURRENT_ALGEBRA_EXACT__ODD_BFV_COMMON_DOMAIN_AND_PHYSICAL_SELECTION_OPEN
channels: [SOURCE, COMPOSE, BUILD, VERIFY]
ledger_rows: [LT-GR1, LT-GR2b, LT-GR3, LT-GR5, LT-GR6]
canon_verdict_change: none
---

# Selected K77 Sobolev edge reduction and charged current algebra

## Result in plain English

The finite boundary geometry from v0.102 has an honest infinite-dimensional
completion on a compact 13-dimensional boundary—but only after the momentum
is typed as a continuous dual, not as another field of the same regularity.

Put the gauge and edge frames in `H^8`, the connection/distortion in `H^7`,
and the cotangent momentum in `H^-7`. The canonical symplectic map is then
strong: it and its inverse are bounded uniformly across Fourier modes. The
edge dressing remains a submersion, and its kernel is exactly the residual
gauge orbit. On every nonempty edge-torsor stratum, the reduced space is the
dressed `H^7 x H^-7` cotangent pair with its canonical real vertical
polarization.

The obvious same-regularity alternative `H^7 x H^7` fails this test. Every
finite cutoff has full rank, but the inverse norm grows like
`(1+n^2)^7`; in the continuum the form is weak. This is a real analytic
distinction that no finite rank calculation could decide.

The charged horn also completes on `H^7 x H^-7`. Its classical charges form
the expected nonabelian current algebra with zero central term for the
selected ultralocal canonical form. The same vertical polarization exists on
both horns, so neither completion nor polarization selects gauge reduction
over charged physical symmetry.

This is not yet full BFV. There are no ghosts, BFV charge, master equation,
bulk common Green/Krein domain, quantum contour or measure. Nonemptiness and
topological classification of the global edge torsor also remain open.

## 1. Layer 0

| phrase | object here | kept distinct from |
| --- | --- | --- |
| boundary | compact 13-manifold bounding a `Y^14` region | 3-dimensional boundary of observed `X^4` |
| Sobolev topology | auxiliary positive Hilbert topology; compact choices equivalent | physical positive energy or K77 Krein form |
| same regularity | `H^7 x H^7`, weak canonical pairing | strong cotangent `H^7 x H^-7` |
| functional reduction | ordinary even presymplectic quotient | graded odd BFV/BRST theory |
| polarization | real vertical cotangent polarization | complex contour, state selection or measure |
| current algebra | classical algebra of `H^8` adjoint-bundle sections | quantum centrally extended algebra/anomaly |
| global edge field | section of a declared edge torsor | a global trivialization of the principal bundle |

An auxiliary Riemannian metric is used only to define Sobolev norms. On a
compact manifold different smooth choices give equivalent topologies; it is
not booked as a physical datum and does not replace the indefinite K77/Krein
pairing.

## 2. Source and prior-art return

Weinstein supplies the tilted bulk grammar and acknowledges that the upstairs
theory has unresolved boundary debt. He does not specify a Sobolev completion,
edge torsor, polarization, current algebra or BFV charge.

```text
SOURCE-CONFIRMS:
  tilted bulk double action and unresolved boundary problem.

SOURCE-SILENT:
  Sobolev topology, edge-torsor existence, polarization, current algebra,
  odd BFV/BRST charge and common analytic domain.
```

The repository's earlier PW2C Abelian `s^2=0` result is prior art only as a
finite comparator and explicitly says it is not a BV action. The full-20
campaign separately requires a declared Sobolev BV manifold and common closed
domain. Neither is silently promoted here.

## 3. The analytic fork finite ranks cannot see

Let `B^13` be a compact smooth boundary component and choose integer
`r=8>13/2+1`. Then

```text
gauge/edge frame: H^8
connection/distortion: H^(r-1) = H^7
cotangent momentum: (H^7)* = H^-7
```

The derivative term in `q_A0(g)` loses one order, so the full tilted cocycle
lands in `H^7`. Multiplication by `H^8` gauge/edge frames is continuous on
both `H^7` and `H^-7`.

For a Fourier mode `n`, the normalized singular value of the `L2` musical map

```text
H^7 -> (H^7)* = H^-7
```

is `(1+n^2)^-7`. It is nonzero at every finite cutoff but tends to zero, so
the inverse is unbounded. `H^7 x H^7` therefore has only a weak canonical
form.

On `H^7 x H^-7`, the canonical musical map

```text
(delta Theta, delta P) -> (-delta P, delta Theta)
```

is an isometry into the continuous dual with bounded inverse mode by mode.
This is the strong completion.

Main exact probe: `59/59 PASS`. Independent Sage/QQ: `22/22 PASS`.

## 4. Edge dressing and the topological fence

On a declared edge-torsor stratum, use the v0.102 dressing

\[
Q=u\Theta u^{-1},\qquad \Pi=uPu^{-1}.
\]

Its derivative is a split surjection: at `u=1`, arbitrary variations of
`Q,Pi` come from variations of `Theta,P`. If a tangent vector lies in its
kernel, `xi=u^{-1}delta u` uniquely reconstructs

\[
\delta\Theta=[\Theta,\xi],\qquad
\delta P=[P,\xi],\qquad
\delta u=u\xi.
\]

Thus the kernel is exactly the residual `H^8` gauge orbit, and the quotient is
the dressed strong cotangent pair. Exact one-site and three-site certificates
give ranks `8/12` and `24/36`, with kernels/orbits `4` and `12`.

This statement is conditional on the relevant edge-torsor section space being
nonempty. v0.102 proves the patch law, not global triviality or existence of a
section in every topological sector. The theorem is therefore stratum-wise,
not a claim that all K77 boundary bundles admit one common edge field.

## 5. Charged horn and polarization

For `xi,eta` in the `H^8` gauge algebra, the charged-horn Hamiltonian is

\[
\mu_\xi=\langle P,[\Theta,\xi]\rangle.
\]

With the selected canonical form,

\[
\{\mu_\xi,\mu_\eta\}=-\mu_{[\xi,\eta]}
\]

in the executable sign convention. The central remainder is exactly zero at
one site and for direct sums. This is a classical result for the current
selected form; derivative boundary counterterms, quantization and regularized
anomalies are not covered.

The ordinary vertical polarization is Lagrangian and preserved by the
cotangent-lifted adjoint action. The edge quotient inherits it, but the charged
horn has the same polarization. It therefore supplies no physical selector.

## 6. What closes and what remains

Closes conditionally:

- strong versus weak Sobolev completion of the selected boundary form;
- compact-boundary `H^8/H^7/H^-7` tilted action;
- stratum-wise strong edge reduction and exact gauge kernel;
- classical charged current algebra with zero central term;
- real vertical polarization on both horns.

Remains:

- nonemptiness and topology of all global edge-torsor sectors;
- noncompact, cornered, null and mixed-signature boundary completions;
- preservation of the `H^7/H^-7` trace spaces by a common bulk Green/Krein
  domain and evolution;
- odd BFV fields, BRST charge, CME and cohomology;
- contour, determinant, measure, reflection positivity and quantum anomaly;
- physical choice between edge gauge and charged boundary symmetry;
- source selection among Spin-native, two-half and full-unitary action parents.

## 7. Specialist and hostile review

- **Symplectic geometry:** the dual-regularity cotangent form is strong; the
  same-regularity form is only weak. The edge kernel theorem then extends by
  submersion, not by finite-rank analogy.
- **Functional analysis:** `r=8` is the least integer above the declared
  13-dimensional multiplication/derivative threshold. It is a regularity
  class, not a fitted coupling.
- **Gauge geometry:** associated-bundle patching does not prove that every edge
  torsor has a global section.
- **Variational PDE:** no bulk operator domain or boundary condition is chosen;
  preservation of the trace spaces remains load-bearing.
- **Complex/path-integral:** real vertical polarization is not a contour or
  measure, and zero classical central term is not anomaly cancellation.
- **Representation theory:** the theorem is on the conditional Spin-native
  parent. Two `U(32,32)` halves and full `U(64,64)` still require expanded
  carriers.
- **Constraint accounting:** the fifth scoped quotient is strengthened from
  finite local to conditional compact-boundary functional scope; it is not
  counted twice. No datum or coefficient is added.

Hostile verdict:
`COMPACT_BOUNDARY_STRONG_SOBOLEV_REDUCTION_SURVIVES_CONDITIONALLY__FULL_BFV_GLOBAL_EDGE_EXISTENCE_AND_PHYSICAL_SELECTION_REJECTED`.

## 8. Progress and next gate

```text
Ledger v0.103 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional action-parent range 84..86
Scoped quotients 5 (the fifth now has conditional compact-boundary scope)

headline_delta: none
frontier_conditions_closed: 4
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

No verdict, residue, datum, canon or public posture changes.

Next:

`COMMON_GREEN_KREIN_DOMAIN_COMPATIBILITY_WITH_H7_HMINUS7_BOUNDARY_TRACES__THEN_ODD_BFV_BRST_CHARGE_AND_CME__KEEP_CHARGED_HORN_AND_EDGE_TORSOR_TOPOLOGY_OPEN`.
