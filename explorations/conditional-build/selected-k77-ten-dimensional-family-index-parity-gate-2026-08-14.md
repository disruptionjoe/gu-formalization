---
artifact_type: exact_conditional_family_index_parity_result
created: 2026-08-14
status: TEN_DIMENSIONAL_SPIN_FAMILY_IS_CONJUGATE_ODD__VIRTUAL_ASYMMETRY_EXACT__GU_FAMILY_OPERATOR_FLUX_DOMAIN_AND_SELECTION_UNBUILT
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
canon_verdict_change: none
---

# Selected K77 ten-dimensional family-index parity gate

## Result first

A genuine ten-dimensional spin-family pushforward would have exactly the
conjugation parity that the ordinary four-dimensional Dirac index lacks. Let

```text
pi:Y^14 -> X^4
```

be a **conditional** proper spin fibration with ten-dimensional fibres, let
`L` be a complex line on `Y`, and let `D_v` be the vertical spin Dirac family.
The family index formula gives

```text
ch Ind(D_v tensor L) = pi_!(Ahat(T_v Y) exp(c)),  c=c1(L).
```

For every Chern-character component,

```text
ch_j Ind(D_v tensor L^-1) = (-1)^(j+1) ch_j Ind(D_v tensor L).
```

Equivalently, rationally in K-theory,

```text
Ind(D_v tensor L^-1) = - conjugate(Ind(D_v tensor L)).
```

Thus the virtual rank changes sign, the degree-two component is unchanged,
the degree-four component changes sign, and the pattern alternates. This is a
real structural difference from the ordinary four-dimensional comparator,
whose line-twisted numerical index is conjugation-even.

The theorem does **not** construct the required GU fibration, vertical Dirac
operator, line bundle, nonzero flux, Fredholm domain, physical carrier,
boundary reduction or vacuum selection. The actual Spin-induced determinant
line remains trivial by the preceding gate. The result therefore identifies
the exact mathematical shape a nonstandard family-operator route would have,
but does not claim that GU owns or physically realizes it.

## Proof

Write the fibre dimension as `2m`, with `m=5`. A term

```text
c^r Ahat_(4s)
```

contributing after fibre integration to base degree `2j` must satisfy

```text
2r + 4s = 2m + 2j,
r + 2s = m + j.
```

Hence every contributing exponent has the same parity,

```text
r = m+j mod 2.
```

Replacing `L` by `L^-1` sends `c` to `-c`, so the complete degree-`2j`
component gains `(-1)^(m+j)`. Complex conjugation of a virtual complex bundle
acts on `ch_j` by `(-1)^j`. Therefore a `2m`-dimensional spin family obeys

```text
Ind(L^-1) = (-1)^m conjugate(Ind(L))
```

rationally. Ten-dimensional fibres have odd `m=5`, giving the minus sign.
The executable probe enumerates every allowed `(r,s)` through base degree
twelve and includes 8D, 12D and 14D controls.

## Layer 0

| Object | Decided here | Not decided |
| --- | --- | --- |
| 14D total-space numerical index | prior odd line-twist parity | GU Fredholm realization |
| 10D vertical family index | conjugate-odd virtual index | source ownership |
| virtual rank | flips under `L <-> L^-1` | particle multiplicity |
| `ch_1` | conjugation-even in the virtual family | nonzero selected determinant class |
| `ch_2` | conjugation-odd | luminous/dark observable |
| central line | conditional twist input | actual Spin-induced line remains trivial |
| rational Chern character | complete parity theorem | integral torsion |
| family operator | exact required mathematical type | physical domain, spectrum and cohomology |

The 4+10 split is used as a program-native dimension fork, not silently
retyped as a standard Kaluza--Klein compactification. A proper spin fibration
with compact/Fredholm fibres is additional structure.

## Broad route-changing lens census

- **Family index theory — exact:** fibre integration decides the full parity
  pattern without choosing Chern numbers.
- **Characteristic classes — exact:** mixed horizontal/vertical terms do not
  spoil the result because the degree equation fixes the parity of every
  contributing power of `c`.
- **K-theory/real structure — exact rationally:** the alternating component
  signs assemble as minus complex conjugation; torsion is outside the claim.
- **Representation theory — structural:** a virtual-index asymmetry is not a
  W/mirror carrier selection or a family multiplicity.
- **Analytic/PDE — open by ownership:** a proper vertical Fredholm family and
  closed domain are absent in the ambient ultrahyperbolic construction.
- **Gauge/BFV — open by ownership:** neither a nonzero central sector nor
  survival through physical gauge reduction is supplied.
- **Source criticism — high:** the source supplies the full connection arena
  and non-chiral total target, but not this family pushforward.
- **Philosophy of science — strict ceiling:** the theorem upgrades a route
  from vague to exact conditional mathematics without counting it as physics.

## Controls and hostile boundary

The strongest overclaim would be “GU now derives luminous matter without its
mirror.” False: the theorem is conditional on precisely the global and
analytic objects still missing.

The strongest contrary control is fibre dimension eight or twelve. There
`m` is even and the relation becomes conjugate-even, proving that the minus
sign is dimension-sensitive rather than inserted by definition. Fourteen
dimensions (`m=7`) reproduce the earlier odd numerical-index parity.

The weakest seam is integrality. Equality of rational Chern characters cannot
detect torsion in the index class. The result is therefore explicitly
rational unless a later integral K-theory argument supplies the missing lift.

## Progress and next gate

```text
Ledger v0.247 — 82/82 target rows mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue: 84 continuous + >=19 function-valued + 9 discrete forks
Tightness: T4x1 T3x3 T2x1 · scoped quotients: 5
Headline delta: none
```

The vague “family index” survivor is now an exact conditional construction
contract: build a proper ten-dimensional spin family, its vertical source-
owned operator and domain, and a nontrivial selected line sector; then test
whether the rational virtual asymmetry lifts integrally and descends through
observation/BFV to physical cohomology. Failure of any ownership or descent
condition stops the physical reading without weakening the theorem.

No field, flux, datum, residue coordinate, quotient count, generation count,
canon verdict or public posture changes. The exact probe passes `58/58`.
