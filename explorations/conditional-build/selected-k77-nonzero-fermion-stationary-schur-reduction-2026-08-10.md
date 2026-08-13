---
artifact_type: exact_nonzero_fermion_stationary_schur_reduction
created: 2026-08-10
status: MAXIMAL_OFFDIAGONAL_RANK_REDUCES_STATIONARITY_TO_64_BY_64_EFFECTIVE_MAP__SOUTHEAST_ZERO_NOT_A_STATIONARY_MODE__PLAIN_CONJUGATE_REALITY_NO_MIRROR_SELECTOR__ACTUAL_VARPI_IMAGE_REALITY_DOMAIN_AND_BV_OPEN
source_return: SOURCE_CONFIRMS_DRAFT916_BLOCK_GRAMMAR_INDEPENDENT_BARRED_FIELDS_AND_SOUTHEAST_FORK__SOURCE_SILENT_MAXIMAL_RANK_EFFECTIVE_MAP_NONZERO_STATIONARY_CONFIGURATION_REALITY_DOMAIN_BV_INDEX_AND_COUNT
ledger_rows: [RA-D4, RA-F1, RA-F2, RA-G2, LT-SM3, AC-F1]
canon_verdict_change: none
---

# Selected K77 nonzero-fermion stationary Schur reduction

## Result in plain English

We now know the smallest equation the missing fermion construction must solve.
The source-displayed candidate has the block shape

```text
D = [ A  B ]
    [ C  0 ]
```

on spinor-valued one-forms plus spinor-valued zero-forms. If `B` is injective
and `C` is surjective, a stationary field `(x,y)` must first have `x in ker C`.
The remaining equation asks whether `A x` vanishes after quotienting by the
image of `B`. Thus the whole kernel is controlled exactly by

```text
S_A : ker C -> coker B,
      x |-> [A x].
```

The map `(x,y) -> x` is then an isomorphism `ker D ~= ker S_A`; `y` is the
unique solution of `B y = -A x`. This is not a heuristic Schur complement. It
is an exact quotient theorem, checked on rational fixtures with residual ranks
two, one and zero.

For the desired K77 one-form sector the prior exact decomposition has
`p=192` one-form and `q=128` zero-form dimensions. On the **maximal-
offdiagonal-rank horn**, the apparently 320-dimensional stationary question
therefore reduces to a `64 x 64` effective map. The same is true for the
192-dimensional anti-self-dual mirror.

Two useful negatives follow.

1. The southeast zero does **not** automatically produce a nonzero stationary
   fermion. A generic effective `64 x 64` map is invertible. A stationary mode
   requires an actual rank-loss equation supplied by the source coefficients.
2. If the desired and mirror effective maps are related only by ordinary
   coefficient conjugation, their ranks and nullities are identical. Plain
   conjugation-compatible reality cannot select one of them. A source-derived
   conjugation-breaking/order parameter, a different real structure, or a
   BV/domain asymmetry would have to do that work.

These are construction constraints, not a new no-go on GU. The actual
`varpi`-coefficient image, the source reality map, maximal rank of the real
off-diagonal blocks, the global domain and the BV quotient remain unbuilt.

## Layer 0

| phrase | object here | not the same as |
| --- | --- | --- |
| source matrix | the candidate block grammar transcribed from draft 9.16 | a globally defined closed operator |
| southeast zero | the displayed lower-right block | an automatically nonzero kernel |
| stationary kernel | finite solutions of the assembled linear field equation | characteristic kernel of the principal symbol |
| nonzero fermion configuration | a solution of the odd classical field equation | a Lorentz-invariant fermion vacuum expectation value |
| effective residual | `ker C -> coker B` under full off-diagonal rank | BV cohomology or a physical quotient |
| 64 | dimension `192-128` of the residual source problem | generation count `3` |
| mirror reality | ordinary coefficient conjugation in the exact fixture | the unbuilt source `C`-reality/Krein placement |
| zero mode | vector in a finite kernel | a closed-domain normalizable mode |
| Fredholm index | future kernel-minus-cokernel invariant of a closed operator | finite kernel nullity |
| count | future physical identification of an index/cohomology | any block multiplicity |

## Exact theorem

Let `X` have dimension `p`, `Y` dimension `q`, and

```text
A : X -> X,  B : Y -> X,  C : X -> Y,
D(x,y) = (A x + B y, C x).
```

Assume `rank B = rank C = q`. Choose `N : ker C -> X` and a full-rank quotient
coordinate `L : X -> coker B`, so `C N=0` and `L B=0`. Define

```text
S_A = L A N.
```

If `D(x,y)=0`, then `x=N u` and `S_A u=0`. Conversely, `S_A u=0` means
`A N u` lies in `im B`; injectivity of `B` gives a unique `y` with
`B y=-A N u`. Therefore

```text
ker D ~= ker S_A,
dim ker D = dim ker S_A,
S_A has size (p-q) x (p-q).
```

The exact probe verifies the theorem on `4+2` fixtures with residual
nullities `0,1,2`, and on `3+2` fixtures with nullities `0,1`. A planted
independent mirror changes the nullity, proving that the conjugation relation—
not dimension alone—is the load-bearing equality.

## K77 instantiation and its fence

The prior exact principal discriminator records:

| sector | one-form | zero-form | total | characteristic rank/kernel |
| --- | ---: | ---: | ---: | ---: |
| desired `W_sd192` | 192 | 128 | 320 | 224 / 96 |
| mirror `asd192` | 192 | 128 | 320 | 224 / 96 |

Only the dimensions and the equality of the already-built principal
fingerprints are imported here. The characteristic rank `224` does **not**
prove that the stationary operator's separate zero-order `B` and `C` have
maximal rank. Consequently `64 x 64` is the exact residual size on the
maximal-rank horn, not yet the rank of an assembled source operator.

The full `U(64,64)` source parent, moving-Spin parent and two-`U(32,32)`-halves
parent share the principal derivative fingerprint. They can populate `A`,
`B`, `C` and the reality map differently. This wave therefore does not select
among them.

## Southeast-nonzero rival

The source extraction explicitly keeps a separately parameterized nonzero
southeast block `E`. If `E` is invertible, the appropriate ordinary Schur
object is `A-B E^{-1} C`, not `ker C -> coker B`. An exact planted fixture has
an invertible southeast-zero candidate and a two-dimensional kernel after
turning on `E=I`. The rival can change the answer and cannot be folded into
the displayed zero candidate.

## Ten efficient specialist lenses

1. **Exact linear algebra — ACTUAL MATH, very high.** The quotient proof is complete under the two stated rank hypotheses and replaces a 320-dimensional opaque solve by one residual determinant/rank problem.
2. **Representation theory — ACTUAL MATH, high.** The 192/128 typing is exact, but representation equivariance may force `B` or `C` away from maximal rank; compute the actual source intertwiners next.
3. **Real Clifford theory — ACTUAL MATH, high.** K77 fixes the real carrier but does not determine which lower-order parent or reality map populates the residual block.
4. **Analytic operator theory — ACTUAL MATH, very high.** Finite nullity is not a normalizable zero mode until a closed Krein/Green domain is built.
5. **Hyperbolic PDE — ACTUAL MATH, high.** A stationary zero mode and a characteristic mode answer different questions; the existing 96-dimensional null-symbol kernel cannot be substituted here.
6. **Variational calculus — ACTUAL MATH, high.** `D Psi=0` is the fermion Euler equation, but a coupled saddle additionally requires the bosonic equation with the quadratic fermion current.
7. **Symplectic/BV--BFV — ACTUAL MATH, high.** `ker S_A` precedes gauge reduction; only the reduced cohomology on a compatible boundary domain can become a physical carrier.
8. **Constraint-rank geometry — ACTUAL MATH, very high.** `det S_A=0` is the first explicit selection condition; it must be action-derived or priced as a new constraint/datum.
9. **Source criticism — ACTUAL MATH, high.** The draft supplies the block grammar and southeast fork, not maximal rank, the residual theorem, reality, domain or count.
10. **Fermion/Higgs phenomenology — ACTUAL MATH, medium.** A nonzero odd classical solution is not automatically a fermion condensate or Higgs vacuum; the source's `varpi` Higgs/Yukawa assignment must be connected without violating fermion parity.

## Progress and next gate

```text
Ledger v0.155 — 82/82 mapped (100%)
32 SAME · 19 DIFFERS · 26 NEEDS · 5 OVER-DETERMINED
Residue 84; conditional parent range remains 84..86
Scoped quotients 5

headline_delta: none
frontier_conditions_closed: 2
frontier_conditions_opened: 1
remaining_named_conditions: 3
```

Closed: the correct finite stationary reduction and the plain-conjugation
no-selector result. Newly opened: construct the actual source-owned effective
map rather than search the full block blindly. Remaining: establish the ranks
of actual `B/C`, populate `S_W(varpi*)` on a coupled bosonic stationary branch,
and build the source reality plus BV/Green domain.

The efficient next gate is
`ACTUAL_DRAFT916_VARPI_EFFECTIVE_MAP_WITH_THREE_PARENT_ABLATIONS`: compute the
real `B`, `C` ranks and the induced desired/mirror effective maps on the
already-built stationary bosonic branches for full `U(64,64)`, moving Spin and
two `U(32,32)` halves. Only if a rank loss survives should the campaign pay for
the coupled nonzero-fermion bosonic Euler equation and global domain.

No datum, P1/P2/P3 assignment, residue, quotient, verdict, canon or public
posture moves. Exact pinned-SymPy probe: `30 exact + 9 planted + 9 source/
prior-art/Layer-0/type = 48/48 PASS`.
