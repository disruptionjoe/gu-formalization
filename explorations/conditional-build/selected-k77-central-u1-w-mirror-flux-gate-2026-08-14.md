---
artifact_type: exact_lie_invariant_and_conditional_index_result
created: 2026-08-14
status: CENTRAL_U1_SUPPLIES_A_CANDIDATE_BOSONIC_W_MIRROR_LEG__LOCAL_REAL_ACTION_CANNOT_SELECT_FLUX_SIGN__FOUR_DIMENSIONAL_ORDINARY_DIRAC_INDEX_DOES_NOT_SPLIT_CONJUGATES
source_return: SOURCE_CONFIRMS_FULL_U6464_CONNECTION_ARENA_AND_GAUGE_HIGGS_LIKE_VARPI_ASSIGNMENT__SOURCE_SILENT_CENTRAL_FLUX_SECTOR_PHYSICAL_IDENTITY_AND_SELECTION
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 central-`U(1)` W/mirror flux gate

## Result first

The full source-sized unitary parent contains a canonical one-dimensional
center, and the exact anti-linear W/mirror exchange makes that center odd.  It
therefore supplies the first honest candidate for the missing **bosonic leg**
of the W/mirror involution:

```text
z = i Identity,        tau(z) = -z,
A_c = a z,             tau(A_c) = -A_c,
F_c = d a z,           tau(F_c) = -F_c.
```

This is not the same as treating the two source carrier halves as two Higgs
doublets or two independent connection fields.  In the block-preserving
`U(32,32) x U(32,32)` subgroup there are two center lines `z_+` and `z_-`.
The exchange acts by

```text
tau(z_+) = -z_-,       tau(z_-) = -z_+.
```

Consequently their diagonal combination is odd and their relative combination
is even.  Once half-exchanging directions are admitted, only the diagonal line
commutes with the full `U(64,64)` parent.  The relative line is not a second
full-parent center.

The route then divides cleanly:

1. The central connection coefficient `a` is not gauge invariant; it shifts by
   an exact one-form.
2. Its abelian curvature `F_c` is gauge invariant and conjugation odd.
3. Every local real scalar action invariant under the exchange has even total
   degree in `F_c`.  Hence any nonzero stationary central-curvature solution
   occurs with its `-F_c` conjugate and the local action selects neither sign.
4. A nonzero first Chern/flux class could make the two sectors globally
   gauge-inequivalent.  That is a real path, not a constructed GU outcome: the
   current program owns no such global bundle sector, flux-selection law or
   relevant Fredholm domain.

There is also an important dimensional qualification.  On a hypothetical
compact spin fourteen-manifold, the ordinary line-twisted Dirac index obeys

```text
index(D tensor L^{-1}) = - index(D tensor L),
```

because every degree-fourteen term in `exp(c1(L)) Ahat(TY)` contains an odd
power of `c1`.  On an ordinary observed four-manifold, however, the same index
contains only `c1^2/2` plus the gravitational term and is invariant under
`L <-> L^{-1}`.  The simplest central-flux twist therefore does **not** split
the ordinary four-dimensional W/mirror indices.  A family index, nonstandard
physical operator, internal pushforward or asymmetric BV/domain construction
would be a new route and remains open.

## Plain English

We found a place in the large GU connection where matter and mirror matter can
couple with opposite sign: the common phase direction at the center of the
unitary group.  Its magnetic-like field strength changes sign when matter is
exchanged with its mirror.  If the universe carried a nonzero topological flux
in that direction, the two conjugate backgrounds could be genuinely different
rather than gauge copies.

But the geometry tested here does not choose such a flux or choose its sign.
A real symmetric action assigns the same value to `+flux` and `-flux`.  The
equal ordinary four-dimensional indices are compatible with Weinstein's
stated claim that the total theory is not chiral.  They do, however, show that
this ordinary line-bundle index cannot by itself explain the claimed
low-curvature separation into luminous and dark chiral-looking sectors.  So
this is a legitimate structural route to a non-fixed global background, not
yet the source's emergent-decoupling mechanism.

## Exact center theorem

The probe uses a faithful `2+2` multiplicity-space model.  This loses no center
information: the complexification of the block algebra is

```text
M_n(C) + M_n(C),
```

whose commutant has dimension two, while the complexification of the full
parent is `M_(2n)(C)`, whose commutant has dimension one.  The exact solver
reproduces both dimensions.  A half-exchanging anti-Hermitian direction
commutes with the diagonal center and has a nonzero commutator with the
relative center, so the distinction fires rather than being inserted by
definition.

For half fluxes `(n_+,n_-)`, conjugation gives

```text
(n_+,n_-) -> (-n_-,-n_+).
```

Thus `n_+ + n_-` is odd and `n_+ - n_-` is even.  The full parent retains the
odd diagonal channel; the even relative channel belongs only to the block
parent unless more structure is declared.

## Local invariant ring

For a simultaneous sign action `F_c -> -F_c`, invariant scalar polynomials have
even total degree.  The probe verifies the one-coordinate restriction through
degree seven and its odd covariant complement.  This restriction is enough to
decide sign selection: along every line through the curvature space, an
invariant potential is even and its Euler derivative is odd.  Therefore a
stationary point at `F_c` implies one at `-F_c`.

The curvature itself is the first gauge-invariant conjugation-odd **covariant**;
it is not a scalar invariant that a symmetric action can use to choose a sign.
A linear term becomes invariant only after supplying another conjugation-odd
coefficient.  The firing control constructs exactly that product, making its
extra-owner cost explicit rather than silently importing it.

## Conditional index calculation

Let `c=c1(L)`.  The degree-fourteen part of `exp(c) Ahat(TY)` has the form

```text
A0 c^7/7! + A4 c^5/5! + A8 c^3/3! + A12 c.
```

It is odd under `c -> -c`.  This is an actual characteristic-class identity,
but applying it to GU would require at least:

- a global central line bundle and nonzero class;
- a compact or otherwise Fredholm fourteen-dimensional problem;
- an action/domain selecting an admissible sector;
- an identification of the relevant physical fermion operator;
- observation or pushforward showing how the upstairs class controls the
  four-dimensional carrier.

The ordinary four-dimensional comparator is

```text
A0 c^2/2 + A4,
```

which is even.  This is not a strike against GU's non-chiral total theory.  It
kills only the naive statement that opposite central line-bundle twists,
through the ordinary 4D Dirac index alone, explain the luminous/dark
decoupling asserted by the source.

## Layer 0

| Object | Decided here | Not decided |
| --- | --- | --- |
| two `C^(32,32)` halves | two carrier blocks | two connection fields or two Higgs doublets |
| block-parent center | two lines, diagonal odd and relative even | action selection of the block parent |
| full-parent center | one diagonal conjugation-odd line | Standard Model hypercharge |
| central potential | transforms inhomogeneously | gauge-invariant observable |
| central curvature | gauge-invariant and conjugation odd | scalar action selector |
| nonzero flux | would label a global conjugate sector | source/action construction or selection |
| compact 14D twisted index | changes sign conditionally | actual noncompact `Y^14` Fredholm index |
| ordinary 4D twisted index | conjugation even, consistent with a non-chiral total theory | luminous/dark decoupling via a family index or nonstandard GU operator |
| paired stationary sectors | forced by an invariant local action | selection of one physical vacuum |

The central `U(1)` should not be called hypercharge merely because both are
abelian.  The reduction, normalization, charges, observation descent and
anomaly ledger would all have to be constructed.

## Adaptive specialist close

- **Lie/invariant theory — ACTUAL MATH, very high:** the center dimensions and
  conjugation eigenspaces are decided wholesale; no large connection search is
  needed.
- **Category/Layer 0 — ACTUAL MATH, very high:** generator, potential,
  curvature, flux, index and selected vacuum are six distinct objects.
- **Gauge/cohomology — ACTUAL MATH, high:** curvature is the first local odd
  covariant; a nonzero Chern class is a global successor, not a local field
  value.
- **Index theory — ACTUAL MATH, very high:** the 14D sign flip and 4D equality
  follow from degree parity; neither supplies a GU Fredholm operator.
- **Variational bicomplex — ACTUAL MATH, high:** an invariant local action has
  paired Euler solutions and cannot select the sign without another odd owner.
- **Symplectic/BFV — ACTUAL MATH, high:** flux sectors or boundary charges can
  survive gauge reduction only after the global bundle and boundary complex
  are specified.
- **Analytic/PDE — ACTUAL MATH, high:** no harmonic representative, stability,
  Green operator or closed domain is constructed.
- **Source criticism — ACTUAL MATH, high:** the source owns the full connection
  arena but is silent on this center's physical identity, nonzero flux and
  selection.

## Progress and next gate

```text
Ledger v0.243 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
Frontier closed: smallest full-parent central bosonic involution and local sign-selection ring
Frontier remaining: global determinant-line descent/flux sector, full stationarity, or asymmetric BV/domain
```

The next bounded gate is to construct the determinant/central line of the
source-full connection globally, pull it through the observation map, and ask
whether any nonzero class or boundary charge survives on the actual physical
domain.  Preregister two kills: ordinary four-dimensional Dirac index equality
does not count as the claimed luminous/dark decoupling, and a freely chosen
flux sector does not count as action selection.  If no owned global sector survives, move to the already-
named asymmetric BV/BFV or analytic-domain route rather than another local
W/mirror Hessian.

No field, coupling, flux, datum, residue coordinate, quotient count, P1/P2/P3
use, canon verdict or public posture changes.  The exact probe passes `48/48`,
including four firing controls.
