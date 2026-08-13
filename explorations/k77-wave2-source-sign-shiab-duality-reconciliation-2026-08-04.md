---
title: "K77 Wave 2: source-sign, Shiab-parity, and degree-duality reconciliation"
status: active_research
doc_type: exploration
created: 2026-08-04
gate: RENDEZVOUS-ACTION-CURRENT-RIESZ-SUPERIG-WARD
result: "PARTIAL__NATIVE_EVEN_SHIAB_HOM0__DEGREE_REALITY_SAT_REQUIRES_ONE_ODD_COVECTOR__EXACT_Q_REPAIRS_BUILT__OWNERSHIP_ADJOINT_WARD_OPEN"
canon_verdict_change: none
---

# K77 source-sign / Shiab / duality reconciliation

## Result first

The three-way fork from the preceding D916 swing has collapsed to one sharply
typed missing object.

1. **A source-native ambient-chirality-even Shiab middle map does not exist**
   in the natural `Spin(7,7)` invariant-tensor class.  An independent exact
   Sage `D7` character computation gives

   ```text
   dim Hom(Lambda2 V tensor S+, V tensor S+) = 0
   dim Hom(Lambda2 V tensor S+, V tensor S-) = 2.
   ```

   The two natural middle contractions are therefore both chirality-odd.

2. **A barred-row duality depending only on output form degree still has no
   solution.**  But the more generous degree-sensitive reality problem—acting
   on both barred rows and unbarred columns—has exactly two sign solutions,
   related by a global sign.  The provisional assertion that the whole
   degree-dependent branch was dead was too strong.  The surviving sign
   assignment requires a real map flipping half-spinors between the zero- and
   one-form sectors.

3. **No released primary source corrects the section-11.2 signs.**  Weinstein's
   2025 explanation confirms contraction `2 -> 1`, Hodge star, and southeast
   zero, then explicitly calls the improved cyclic `D^2` object unreleased.
   That is `SOURCE-SILENT`, not a license to rewrite equation 9.16.

4. **The smallest chirality-flipping realization is one additional moving odd
   covector `q`.**  Clifford multiplication supplies the unique vector-supplied
   half-spinor flip, and both

   \[
   A_q^L(\xi)=\gamma(q)A(\xi),\qquad
   A_q^R(\xi)=A(\xi)\gamma(q)
   \]

   are exact, nonzero, linearly independent, ambient-`J` even, preserve the
   preceding wedge adjacency, and descend when `q`, `xi`, the form indices,
   and spinors move together.  Holding `q` fixed breaks covariance.

So the degree-reality branch and the modified-Shiab branch converge: both need
the same `q`-type object.  This is real construction progress, but not yet
confirmation.  If `q` is free, the current fit has negative constraint
surplus; if geometry already owns `q`, its source and action variation still
have to be shown.  P1 can choose `q` versus `-q` only after a timelike line and
normalization exist—it cannot manufacture the line.  No identification with
P1, P2, or P3 is made here.

The exact executable result is:

```text
7 source + 15 type + 22 exact + 5 planted = 49 PASS
```

Wave 2 remains partial.  Wave 3 does not open.

## Layer 0: what the signs belong to

| object | type in this swing |
| --- | --- |
| `zeta+/-`, `nu+/-` in draft section 11.2 | ambient half-spinor bundle labels |
| barred fields in equation 9.16 | independent Berezin row fields, not yet vector representatives |
| row primalizer / Krein pairing | converts a density-dual row to a vector arrow only after a convention is chosen |
| `G=(-1)^form J` | coherent auxiliary grading of the prior rival, not the source glyph meaning |
| source-native middle symbol | `Lambda2 V* tensor S -> V* tensor S`, built from invariant tensors |
| `q` repair | an additional moving odd covector, not epsilon conjugation itself |
| observation timelike orientation | can choose a sign on an already-existing timelike line, not supply the line |
| physical chirality | an effective four-dimensional statement, held out |

This prevents two tempting but false shortcuts.  First, a source bilinear is
not already a square endomorphism.  Second, conjugating `Phi1` and `J` by the
same `epsilon` preserves their relative oddness; the gauge rotation is not an
extra vector index.

## Primary-source collision

### What the 2021 draft fixes

The rendered draft fixes the equation-9.16 row/column incidence, the
section-11.2 ambient half-spinor bundles, the simple invariant-`Phi_r` Shiab
workshop, and the candidate rather than unique status of the displayed
operator.  It says the historical preferred Shiab calculation cannot be
located.

For a natural map from a spinor-valued two-form to a spinor-valued one-form,
there are three exposed vector slots: two input form indices and one output
index.  Metrics contract indices in pairs and the fourteen-index orientation
tensor changes the count by an even number.  Therefore the number of Clifford
vector factors is odd.  Every such map anticommutes with ambient chirality.

### What the 2025 transcript adds

At `02:38:12--02:42:55`, Weinstein describes rolling the connection-twisted
de Rham sequence and cutting it to `0 -> 1 -> 13 -> 14`.  The middle operation
contracts a two-form back to a one-form and then stars it.  He connects the
southeast zero to a possible seesaw mechanism.

At `02:44:06--02:45:13`, he describes a new cyclic `D^2` construction but says
he has never released it and recalls its entries tentatively.  This supports
continued construction; it does not supply a released sign correction.

Source disposition:

| question | disposition |
| --- | --- |
| contraction `2 -> 1` then star | `SOURCE-CONFIRMS` |
| southeast-zero importance | `SOURCE-CONFIRMS` |
| section-11.2 ambient signs | `SOURCE-STATES` |
| correction/relabel of those signs | `SOURCE-SILENT` |
| exact improved cyclic operator | `SOURCE-UNRELEASED` |

## Branch 1: source-native ambient-even Shiab

The invariant-tensor parity argument already predicts a zero.  Sage 10.9
independently verifies it in the complexified `D7` representation ring:

```text
D = WeylCharacterRing("D7", style="coroots")
V  = D(fundamental_weight_1)
S+ = D(fundamental_weight_6)
S- = D(fundamental_weight_7)

<Lambda2(V) tensor S+, V tensor S+> = 0
<Lambda2(V) tensor S+, V tensor S-> = 2
```

The real K77 matrix witness constructs the one-gamma and three-gamma maps and
checks that every block anticommutes with `J`.  Complex Hom-dimension zero
implies real Hom-dimension zero for the even target.  This kills only the
source-native natural invariant-tensor mechanism.  It does not kill a map
using an extra moving tensor or reduced observation geometry.

## Branch 2: degree-sensitive duality/reality

Let `r1,r0` convert barred one- and zero-form row labels to vector-output
representatives and `c1,c0` convert the unbarred column sectors.  The displayed
derivative cells join equal source signs, so the three parity conditions are

```text
r1*c1 = parity(Phi d) = -1
r1*c0 = parity(d)     = +1
r0*c1 = parity(-d*)   = +1.
```

If only barred rows may change, the first two equations contradict.  If both
rows and columns may carry degree-sensitive reality, the exact solutions are

```text
(r1,r0,c1,c0) = (-s,+s,+s,-s),  s in {+1,-1}.
```

This was the swing's important self-correction.  The sign system is soluble;
the natural realization is not free.  It requires `c0=-c1`, hence a genuine
chirality-flipping map between degree sectors.  Sage gives

```text
dim Hom_Spin(S+,S-) = 0
dim Hom_Spin(V tensor S+, S-) = 1.
```

Thus a bare degree relabel is not a bundle map, while one supplied vector or
covector produces exactly the missing intertwiner.

An operator-cell-dependent matcher can trivially assign the three requested
parities.  It uses three bits for three conditions, has zero surplus, and is
retained only as a planted negative control.

## Branch 3: released sign correction

No released primary locator inspected here changes the equation-9.16
incidence or section-11.2 half-spinor bundles.  The correct status is
`SOURCE-SILENT`, not `REFUTED`: a future released correction could still alter
the source-identification question.

## Constructive escape: one moving odd covector

For the native one-gamma symbol

\[
A(\xi)_a{}^c=\delta_a^c\gamma(\xi)-\xi_a\gamma^c,
\]

introduce `q in V*` and define left/right repairs as above.  Because both
`gamma(q)` and `A(xi)` are `J` odd, their products are `J` even.  The exact
fixture verifies:

- both repaired families are nonzero and independent;
- `A_q(xi) B(xi)=0`, so the rolled principal adjacency survives;
- an even Clifford transition moving two axes transports the repaired symbol
  exactly when `q` moves;
- the fixed-`q` plant fails; and
- the zero-`q` plant erases the middle symbol.

There are two equivalent architectural placements still to compare:

1. put `gamma(q)` into a degree-reality/primalizer map; or
2. put it into the Shiab middle block as `A_q^L` or `A_q^R`.

They must be compared inside the same full action because moving
`gamma(q)` through the Krein pairing and covariant derivative changes formal
adjoints, `dq` terms, and the connection/`q` currents.

## Constraint surplus and datum boundary

If `q` is freely chosen pointwise, it has thirteen projective parameters.  The
left/right span adds one projective coefficient.  At this gate, even parity and
rolled adjacency are identities across the whole family, not equations
selecting those fourteen parameters.  The current selecting-constraint rank is
zero, so the provisional surplus is `-14`.

That does **not** justify abandoning the repair.  It means the construction is
an instrument whose information content must come from downstream independent
constraints: ownership by the geometry, the full multi-index adjoint, common
current/Ward variation, source zero-order blocks, and global descent.

The earlier observer-Cartan construction supplies a candidate *shape*: a
future unit timelike line/vector on the Lorentz observation slice.  But:

- a time orientation chooses one of two directions on an existing line;
- it does not select the line inside the Lorentz four-plane;
- normalization uses a selected metric; and
- an `X`-side observer vector is not automatically a global covector on `Y`.

Therefore P1 is not consumed here.  P2 remains untyped, though this swing emits
a precise receiver hypothesis for its later gate: a globally compatible odd
line/covector or soldering direction whose orientation may share P1.

## Divergent specialist pre-assessment

The ten inline lenses are recorded in the Runtime plan.  Their main shared
prediction was that tensor-valence parity should decide the native Shiab branch
before matrix brute force, while source archaeology should keep the unreleased
cyclic operator from being used as a correction.  The prediction succeeded.
The duality lens's initial row-only model was incomplete and was repaired in
hostile review by allowing degree-sensitive column reality as well.

## Hostile review and material correction

The review returned

```text
REPAIRED_PARTIAL__THREE_BRANCHES_CONVERGE_ON_ONE_Q_TYPE_RECEIVER
```

The material correction was not numerical.  The first draft said
“degree-dependent duality is killed.”  That was true only for barred-row
duality.  Once the column reality maps were typed, two algebraic solutions
appeared.  The Sage half-spinor Hom calculation then showed why those solutions
still require the same extra vector/covector as the Shiab repair.

The review also refused four promotions:

- `q` is not `epsilon` merely because both move;
- `q` is not P1, P2, or P3;
- exact principal-symbol descent is not the full adjoint/current/Ward action;
- the seesaw source analogy is not a mass or neutrino prediction.

## Seven axes plus Layer 0

| level | disposition |
| --- | --- |
| Layer 0 | bilinear, duality, vector arrow, ambient chirality, total grading, and `q` separated |
| L1 | source locators and released/unreleased grades pinned |
| L2 | exact real K77 maps plus exact `D7` Hom multiplicities |
| L3 | finite moving-transition witness only; actual `Y14` ownership open |
| L4 | no statistical or phenomenological fit claimed |
| L5 | no physical chirality, particle, mass, or family inference |
| L6 | hostile review completed with one material scope repair |
| L7 | runnable exact probe and successor-aware scope audit required |

## Honest boundary and next gate

This swing closes the original three-way ambiguity to one missing type.  It
does not close Wave 2 because `q` has no accepted owner and its two placements
have not been varied in the full action.

The next named build is

```text
K77_D916_Q_RECEIVER_OWNERSHIP_ADJOINT_WARD_SELECTION
```

It must:

1. test whether `q` is already supplied by the actual moving
   observation/soldering/augmented-torsion geometry or is genuinely new datum;
2. compare degree-reality, left-Shiab, and right-Shiab placements;
3. derive the full `dq`, connection, fermion, and `q` currents with the
   multi-index Krein adjoint;
4. use those independent equations to rank/select the placement coefficients;
5. check full-source-group descent or name the exact stabilizer reduction; and
6. keep Wave 3 closed unless that common action actually exists.
