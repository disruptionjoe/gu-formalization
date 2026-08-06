---
artifact_type: selected_action_curvature_graph_completion
created: 2026-08-06
status: CONSTANT_TORSION_GRAPH_CURVATURE_EXACT__OFF_GRAPH_DBT_AND_GLOBAL_REDUCTION_OPEN
lane: "1"
functional_channels: [BUILD, COMPOSE, SOURCE, VERIFY]
source_return: SOURCE-CONFIRMS_AND_SOURCE-SILENT
ledger_rows: [LT-GR1, LT-GR2b, LT-GR5, LT-GR6, LT-SM8]
scripts:
  - tests/channel-swings/selected_action_curvature_graph_six_versus_four_probe.py
registry: lab/process/selected-action-curvature-graph-six-versus-four.json
---

# Selected-action curvature graph: the six-versus-four test

## Result first

The selected `I1B` curvature term does exactly the right thing to the six
nongauge null directions exposed by v0.33—on the source-native
constant-augmented-torsion graph.

The Bianchi-selected `comm/symi/symi` Shiab is already known to act as
`-2 Einstein_14` on algebraic Riemann curvature. Pairing that response with
the tautological `Phi1` gives exactly twelve times scalar curvature. On the
normalized nonzero stationary radial branch `t*=-1/312`, the curvature gain
is therefore

\[
12t_*=-\frac1{26}\ne0.
\]

For metric-induced purely horizontal curvature, the graph-restricted second
variation is consequently a nonzero multiple of the four-dimensional
Fierz--Pauli/linearized-Einstein symbol. Combined with the v0.33 zero-jet
source Hessian, exact rational computation gives

```text
timelike: rank 30, nullity 4 = gauge exactly
spacelike: rank 30, nullity 4 = gauge exactly
null: rank 28, nullity 6 = gauge 4 + physical transverse 2
```

Thus all six zero-jet nongauge directions are lifted off the characteristic
cone. On the cone, two survive for the correct reason: they are the plus and
cross massless gravitational polarizations.

This closes the graph-restricted curvature part of the six-versus-four gate.
It does not totalize the off-graph `d_B T` torsion block, construct the global
observation receiver, or establish the common Green/BV/BFV domain.

## Plain English

The last wave found that the simplest part of the action could not distinguish
six real metric changes from keeping the augmented torsion constant. That was
not automatically a flaw; it told us what the curvature part had to supply.

The curvature term supplies precisely those missing equations. Away from the
light cone, the only remaining zero directions are coordinate changes. On
the light cone, two additional zero directions remain, and they are exactly
the two gravitational-wave polarizations. So the geometry did not merely fit
six arbitrary missing numbers: it produced the standard gauge-versus-wave
split with no added coefficient or datum.

## Layer 0

| phrase | exact object | not identified with |
| --- | --- | --- |
| constant-torsion graph | `varpi=B_LC(g)+T*`, so `T` stays fixed under metric motion | full independent `(g,varpi)` carrier |
| graph curvature | purely horizontal Riemann curvature induced by `B_LC(g)` | arbitrary ambient algebraic curvature |
| selected contraction | repository-selected `comm/symi/symi` Shiab on the Riemann image | a source-published unique selector |
| curvature Hessian | moving-contraction/density Einstein--Hilbert second variation on the graph | curvature value with metric frozen |
| nonnull kernel | four principal diffeomorphism directions | four physical zero modes |
| null extra kernel | plus/cross characteristic polarizations | Ward failure or a fifth booked quotient |

## Source and repository collision

The source owns the gauge-rotated Levi-Civita connection in the contorsion
slot, the augmented-torsion difference and the first-order action. It also
describes curvature contraction toward an Einstein-like one-form. The source
does not publish the selected product row, the exact trace factor, the graph
restriction, the observer receiver or a global domain.

The repository supplies two exact ingredients not attributed to Weinstein:

1. Bianchi plus nonvacuity selects `comm/symi/symi` among the eight displayed
   product rows and proves its Riemann response is `-2 Einstein_14`.
2. The selected radial stationary equation gives `t*=-kappa_1/312`.

Disposition:

```text
SOURCE-CONFIRMS: two-connection/Levi-Civita graph and first-order action arena
SOURCE-SILENT:   selected coefficient theorem, graph Hessian, observation
                 receiver, off-graph domain, BV/BFV and physical completion
```

## Exact coefficient and ranks

For an algebraic curvature tensor `R`,

\[
S_{sel}(R)=-2G_{14}(R),\qquad
\langle\Phi_1,S_{sel}(R)\rangle=12\,\mathrm{Scal}_{14}(R).
\]

The factor twelve is computed directly in the exact `Cl(7,7)` exterior
backend: on the scalar-curvature fixture the pairing is `2184`, the scalar is
`182`, and their ratio is `12`.

On the constant-torsion graph, metric-induced curvature has no mixed vertical
compensation. Its ambient scalar equals the horizontal four-dimensional
scalar, so the second variation is `(-1/26) C_k`, where `C_k` is the
Fierz--Pauli symbol. Its ranks are six for timelike and spacelike covectors
and four for null covectors. It annihilates the rank-four metric
diffeomorphism symbol on all three orbits.

In source coordinates, v0.33's zero-jet Hessian is congruent to
`diag(0_10,K_24)` after changing from `delta varpi` to
`delta T=delta varpi-L delta g`. Adding graph curvature gives

\[
\operatorname{diag}((-1/26)C_k,K_{24}).
\]

Because `K_24` is nondegenerate, the total ranks are the sums `6+24=30`
off cone and `4+24=28` on cone. The null kernel is exhausted by the four
gauge columns plus the graph lifts of

\[
h_+=dx^1\odot dx^1-dx^2\odot dx^2,
\qquad h_\times=dx^1\odot dx^2.
\]

## Why the ambient-kernel no-go survives

The prior no-factor theorem allows arbitrary ambient algebraic curvature and
constructs mixed horizontal/vertical curvature whose ambient Ricci vanishes
while its horizontal restriction has arbitrary observed Einstein output.
That proves no post-Shiab adapter can recover observed gravity on the full
declared carrier.

This wave restricts to a smaller action image: curvature actually induced by
the horizontal Levi-Civita connection along the constant-torsion graph. It
contains no compensating vertical curvature. The selected contraction is
faithful enough on that image even though it is not faithful on all ambient
curvature. The no-go is preserved; its domain does not kill this route.

## Mandatory symplectic reading

Off characteristic, the graph-restricted Hessian kernel equals the gauge
image, which is the exact symbol condition needed before reduced covariant
phase-space construction. On the null cone, exactness must fail by two
directions: erasing them would erase the graviton characteristics. This is a
principal even complex, not yet the reduced covariant phase space. Boundary
charges, odd generators, the Green current and the unrestricted BFV quotient
remain open.

## Corrected queue

1. Construct the off-graph `d_B T` torsion principal block and its cross terms
   on the full independent `(g,varpi)` carrier; distinguish its physical
   characteristic kernel from extra constraint failure.
2. Compose the exact graph result with the observation equation receiver and
   prove no conormal leakage on the actual action image.
3. Establish a common closed Krein/Green domain, odd BV and unrestricted BFV
   while retaining the two null gravitational characteristics.
4. Keep `I2B <-> ||II||^2` separate until its owner map is constructed.

## Ledger v0.34

```text
Ledger v0.34 — 82/82 active target rows mapped (100%)
33 SAME · 19 DIFFERS · 24 NEEDS · 6 OVER-DETERMINED
Residue — 84 continuous + >=19 function-valued + 9 forks
Quotients ranked — 4 scoped
```

Five distances move. Verdicts, reason kinds, revival triggers, residue,
quotient count and P1/P2/P3 remain unchanged. The two null representatives
upgrade action ownership of an already-known characteristic pattern; they do
not add a fifth quotient.

## Seven-axis disposition

- **Layer 0:** graph curvature, arbitrary ambient curvature, observed
  Einstein target and full source carrier are separated.
- **L1 syntactic:** selected curvature coefficient and three symbol complexes
  are explicit.
- **L2 type:** metric-induced curvature lands in the horizontal Riemann image
  on which the selected contraction is nonzero.
- **L3 algebraic:** trace ratio, gains, ranks and kernel spans are exact.
- **L4 geometric:** local constant-torsion graph is exact; global bundle and
  observation descent remain open.
- **L5 variational/symplectic:** graph-restricted moving Einstein--Hilbert
  Hessian and gauge/characteristic split are exact; reduced BV/BFV is open.
- **L6 analytic:** no common closed Green/Krein domain is claimed.
- **L7 physical:** two standard massless tensor characteristics are located,
  but no full Einstein equation, Q1, cosmology or unitarity claim is promoted.

## Constraint fence

```text
new fields: 0
new coefficients: 0
new selectors: 0
new quotients: 0
P1/P2/P3 consumed: 0
```

Curt remains formally separate inside the Eric lane. No third lane, canon
verdict, claim status or public posture is promoted.
