---
title: "V15-1 physical-signature transfer audit"
status: complete-bounded-audit
doc_type: review-packet
created: 2026-07-23
scope: "Located, Not Forced v2.15; no manuscript integration"
source_revision: bbd985fe65371c3292b25b66fe2413bf5d1f1492
evidence:
  - tests/lorentzian-transfer/physical_signature_transfer_audit.py
  - tests/lorentzian-transfer/V15-1-receipt.json
  - tests/lorentzian-transfer/README.md
---

# V15-1 physical-signature transfer audit

## Disposition

The compact/complexified carrier calculation does not transfer as one
unchanged physical-real-form packet.

- One Lorentzian complex Hodge-star half has complex dimension `192` and two
  total-chirality blocks of dimension `96`. Thus the complex rank and
  complexified branching survive.
- That `192`-space is not preserved by the physical quaternionic conjugation.
  Conjugation exchanges it with the opposite Hodge-star half.
- The program-native invariant Krein form restricts to zero on each individual
  Lorentzian half. Therefore compact `(96,96)` is not the Krein signature of
  one physical Lorentzian `192`-space.
- Adjoining the conjugate half gives a complex `384`-dimensional
  real-form-stable carrier. The two halves are Krein-null and pair
  nondegenerately; the closure has signature `(192,192)`.
- The compact class-C Hom-space packet `(2,2,2,2,0)` is fork-specific. The
  selected Lorentzian complex half gives `(2,2,0,0,0)` and the stable closure
  gives `(4,4,4,4,0)`.
- The qualitative antilinear no-swap verdict survives only when “chirality”
  means total 14-dimensional chirality: all four equivariant antilinear
  intertwiners on the closure preserve it. Physical conjugation swaps the base
  and internal chirality factors separately and exchanges the selected
  self-dual half with its conjugate.

This does not reverse the tested representation-theoretic C1-C5 part of the
central bounded class-C conclusion: no equivariant total-chirality-swapping
linear or antilinear map appears on the stable physical-real-form carrier, and
the conjugate doubling introduces no odd-primary selector in those Hom-space
generators. Physical C6 characteristic classes were not reconstructed, so full
physical class-C transfer remains open. The audit does change the exact carrier
premises and forbids transferring the compact `(96,96)` theorem instance or
the phrase “antilinear maps preserve chirality” without qualification.

No canonical manuscript, status table, queue, Lane state, Lean file, or
existing test was edited.

## Fork discipline

This audit keeps two independent forks explicit.

### Indefinite/Krein versus positive-Hilbert

The construction uses the program-native invariant form

`K = eta_base tensor beta_S`

on the Clifford-Rarita-Schwinger carrier. It does not replace `K` with a
positive-definite identity form. As a discriminating control, the executable
test verifies that the positive identity has Lorentz-boost invariance defect
about `3.92e+01`; it is not the same invariant object. Consequently:

- failure of a positive-Hilbert default to be Lorentz invariant does not kill
  the program-native Krein construction; and
- failure of the compact `(96,96)` restriction to survive on one Lorentzian
  complex half does not establish a positive-Hilbert no-go.

### Compact/complexified versus physical real form

The baseline and reconstruction are:

| object | base/internal split | selected object | physical conjugation | Krein restriction |
| --- | --- | --- | --- | --- |
| compact selected | `(4,0)+(5,5)` | one `su(2)+` Casimir-8 sector, complex dim `192` | endomorphism of the selected carrier | nondegenerate `(96,96)` |
| Lorentz complex half | `(3,1)+(6,4)` | one `star=+i` Casimir-8 sector, complex dim `192` | maps out to the `star=-i` half | zero |
| Lorentz stable closure | `(3,1)+(6,4)` | `star=+i` plus `star=-i`, complex dim `384` | closed; quaternionic `J^2=-1` | nondegenerate `(192,192)` |

The Lorentzian half is constructed directly from the real
`so(3,1)+so(6,4)` generators and the complex Hodge-star eigenalgebra. No
dimension or signature is inferred by Wick-rotation analogy.

## Assumptions and construction choice

1. The total real Clifford algebra remains `Cl(9,5)=M(64,H)`; only the
   `4+10` signature partition changes.
2. All displayed carrier dimensions are complex dimensions in the same
   128-complex-dimensional Clifford realization used by the current census.
3. Indices `0,1,2,3` are the base. The compact model takes all four spacelike
   and five internal directions timelike. The physical model moves one
   timelike direction to base index `3`, giving `(3,1)+(6,4)`.
4. In the compact model the self-dual generators are the real combinations
   `M01+M23`, `M02-M13`, and `M12+M03`. In the Lorentzian model the two
   Hodge-star eigenspaces replace the boost terms by `+i` or `-i`. Their
   quadratic Casimir has eigenvalues `0,3,8`; the Casimir-8 space is selected.
5. The selected space must be gamma-traceless and invariant under all six
   base and forty-five internal real-form generators. Both are hard-checked.
6. The physical antilinear structure is constructed from the six imaginary
   Clifford generators. It commutes with `Cl(9,5)`, squares to `-1`, and is
   checked on the computed carrier rather than assumed from a table.
7. The class-C comparison covers the representation-theoretic generator
   spaces C1-C5: linear commutants, invariant bilinear and sesquilinear forms,
   equivariant antilinear intertwiners, and equivariant cross-total-chirality
   linear maps. It does not reconstruct C6 characteristic classes on the true
   physical bundle.

## Executable results

The direct matrix construction produced:

| claim | compact selected | Lorentz complex half | Lorentz stable closure | disposition |
| --- | ---: | ---: | ---: | --- |
| carrier dimension | `192` | `192` | `384` | `192` survives per complex half, not as a conjugation-stable packet |
| total-chirality blocks | `96+96` | `96+96` | `192+192` | per-half complex split survives |
| Krein restriction | `(96,96)` | rank `0` | `(192,192)` | compact `(96,96)` does not transfer |
| C1-C5 dimensions | `(2,2,2,2,0)` | `(2,2,0,0,0)` | `(4,4,4,4,0)` | compact tuple does not transfer |
| equivariant antilinear total-chirality type | all preserve | no antilinear endomorphism | all preserve | qualitative total-chirality no-swap transfers to closure |

All Hom bases have residuals between `1.2e-13` and `2.7e-11`, with the next
normal-matrix eigenvalue between about `3.3e+01` and `2.3e+02`. The
Casimir, gamma-trace, and covariance residuals are at most `3.4e-12`,
`8.1e-13`, and `7.2e-13`, respectively.

The exact real-even-algebra fork is also reproduced:

- `Cl^0(5,5)=M(16,R)+M(16,R)`: the two internal Weyl `16`s are separately
  real/self-conjugate in the compact baseline real form.
- `Cl^0(6,4)=M(16,C)`: the two physical internal Weyl `16`s form a
  complex-conjugate pair.

This is why the word “chirality” cannot remain untyped. The physical
conjugation:

- preserves total 14d chirality;
- swaps base Lorentz chirality;
- swaps internal `16`/`16bar` chirality; and
- exchanges the selected self-dual and anti-self-dual Lorentzian halves.

## Claim-by-claim transfer

### `192`

**Survives after complexification, with a real-form caveat.** Each Lorentzian
Hodge-star half has complex dimension `192`, is gamma-traceless, and is
invariant under the physical real Lie algebra. It is a legitimate complex
Lorentz representation. It is not closed under the program's physical
quaternionic conjugation; the smallest carrier closed under that conjugation
inside this reconstruction has complex dimension `384`.

The claim “there is a complex rank-192 Lorentzian half” is verified. The claim
“the physical-real-form carrier is the same 192-space” remains a
reconstruction premise and is false if closure under the exhibited physical
conjugation is required.

### `(3,2,16)+(3,2,16bar)`

**Survives as complexified branching notation for one half.** Up to the
orientation choice naming the two Lorentz factors, the selected half is

`(3_SD,2_ASD,16_+) + (3_SD,2_ASD,16_-)`.

Its physical conjugate is

`(2_SD,3_ASD,16_-) + (2_SD,3_ASD,16_+)`.

Thus the dimensions and the `3 x 2 x (16+16)` complex branching survive.
The compact notation suppresses that the physical conjugation simultaneously
exchanges the two Lorentz factors and the internal Weyl factors. Treating the
first line alone as a real physical carrier is still a premise.

### `(96,96)`

**Compact/complexified only in the stated 192-dimensional form.** On one
Lorentzian complex half the program-native Krein form is identically zero, not
signature `(96,96)`. The two Lorentzian halves are complementary Krein-null
spaces. Their closure has signature `(192,192)`.

Therefore the current finite Krein intersection theorem remains valid on its
compact 192-dimensional premise packet, and its abstract linear-algebra form
can be instantiated on a `(192,192)` closure after the relevant grading is
typed. It cannot be advertised as already proved on the physical Lorentzian
192-space.

### `(2,2,2,2,0)`

**Compact/complexified only.** The executable C1-C5 census gives:

- compact selected carrier: `(2,2,2,2,0)`;
- one Lorentzian complex half: `(2,2,0,0,0)`;
- Lorentzian stable closure: `(4,4,4,4,0)`.

This is not disagreement between two routes computing the same object. It is
the expected discriminator among three non-isomorphic fork objects. In
particular, one complex half has invariant bilinear forms but no invariant
sesquilinear form or equivariant antilinear endomorphism; those structures
pair it with its conjugate and reappear on the closure.

The fifth entry remains zero in all three constructions: no equivariant
linear map swaps total 14d chirality.

### Antilinear preserve/swap

**Preserve for total chirality; swap for the separated physical factors.**

- Compact selected carrier: both equivariant antilinear generators preserve
  total chirality, which aligns with internal chirality on that selected
  compact half.
- Lorentz complex half: there is no equivariant antilinear endomorphism. The
  physical antilinear structure maps it to its conjugate half.
- Lorentz stable closure: all four equivariant antilinear intertwiners
  preserve total 14d chirality. The exhibited physical conjugation swaps base
  and internal chirality separately.

Accordingly, the no-go “no equivariant antilinear **total-chirality** swap”
transfers to the bounded physical closure. The stronger reading “physical
conjugation preserves the internal `16`/`16bar` label” does not transfer.

## No-go transfer map

| statement | fork where established | transfers? |
| --- | --- | --- |
| positive identity is not Lorentz invariant | standard positive-Hilbert default on the finite Lorentz representation | no program-native kill; it only rejects silent Hilbert substitution |
| selected `192` has nondegenerate `(96,96)` Krein form | compact `(4,0)+(5,5)` | no; Lorentz half is null and closure is `(192,192)` |
| no equivariant total-chirality-swapping linear map | all three computed objects | yes, for C1-C5 |
| no equivariant total-chirality-swapping antilinear map | compact selected and Lorentz stable closure | yes, for the bounded closure |
| equivariant antilinear maps preserve internal chirality | compact `(5,5)` internal real form | no; physical `(6,4)` conjugation swaps the internal Weyl pair |
| one Lorentz complex half has no antilinear endomorphism | selected physical complex half | not a universal antilinear no-go; the map exists between conjugate halves |

## Reconstruction premises and residuals

The audit does not determine:

1. whether the true `Y14` source action selects one Lorentzian complex half,
   the conjugation-stable closure, or another representation;
2. whether a physical reality/quaternionic condition is imposed on the
   carrier and how it is compatible with the source action;
3. whether the action preserves the self-dual half, couples the two halves,
   or supplies a different grading;
4. which subspace, domain, or projector defines physical states in the
   program-native indefinite theory;
5. whether the C6 characteristic-class packet transfers to the physical
   bundle;
6. any Fredholm, hyperbolic-to-elliptic, or net-handedness index; or
7. any map from the located torsion class or complex rank three to the
   observed generation integer.

Those are reconstruction premises, not failed numerical checks.

## Manuscript and status-table consequences

V15-9 integration should make the following changes, without overstating this
audit:

1. Retain `192` and `(3,2,16)+(3,2,16bar)` only as a complexified
   per-Hodge-half calculation; state that physical conjugation closes it with
   the opposite half.
2. Do not attach `(96,96)` to the physical Lorentzian `192`-space. State that
   the per-half restriction is null and the computed stable closure is
   `(192,192)`.
3. Scope `(2,2,2,2,0)` to the compact/complexified carrier. If the physical
   fork is discussed, give `(2,2,0,0,0)` for one complex half and
   `(4,4,4,4,0)` for the stable closure.
4. Replace every unqualified antilinear “preserve/swap chirality” statement
   with the typed distinction among total, base, internal, and Hodge-half
   chirality.
5. Keep the finite Krein theorem and class-C conclusion conditional on their
   carrier premise. Do not claim the existing 192-dimensional theorem
   instance as a physical Lorentzian theorem.
6. Keep the true-`Y14` source-action, physical-state, and integer-count
   residuals open.

These are integration consequences, not edits made by this packet.

## Validation

Environment:

- source revision: `bbd985fe65371c3292b25b66fe2413bf5d1f1492`;
- Python `3.14.6`;
- NumPy `2.5.1`.

Command from the repository root:

```sh
../../../_local/venvs/research-compute/bin/python \
  tests/lorentzian-transfer/physical_signature_transfer_audit.py
```

Result:

```text
AUDIT PASS: 53/53 checks
```

The script recomputes all values and checks them against the machine-readable
receipt. Its controls include the compact signature, the null-half versus
hyperbolic-closure discriminator, exact real Clifford-even-algebra types,
physical-conjugation exchange, and failure of the positive identity under
Lorentz boosts.

## Stop-condition assessment

No central class-C/antilinear reversal was found:

- total-chirality cross-linear dimension remains zero;
- all closure antilinear intertwiners preserve total chirality; and
- no odd-primary selector is introduced in the computed C1-C5 Hom-space
  closure.

The exact compact tuple and Krein premise do change across the physical fork.
That is a mandatory manuscript-scope correction for V15-9, not a reason to
edit the manuscript during this audit. If “chirality” in the current central
verdict was intended to mean internal `16` versus `16bar` rather than total
14d chirality, then the verdict changes and must be returned to Joe before
integration; this packet supplies the discriminating evidence. Full physical
C6 transfer also remains open rather than silently inherited from the compact
packet.
