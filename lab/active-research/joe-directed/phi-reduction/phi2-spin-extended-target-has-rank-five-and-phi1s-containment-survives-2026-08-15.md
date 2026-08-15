---
artifact_type: exploration
status: exploration
doc_type: construction-delta
created: 2026-08-15
work_item: PHI-2
channel: conditional_ledger_advancement
ledger_base: lab/process/conditional-physics-ledger-v0.258.json
axis: ANOMALY_CONSISTENCY
rows: [AC-C2, AC-D1, AC-D2, AC-D3, AC-D4, AC-D5, AC-E1]
delta_kind: VERSIONLESS_DELTA__NOT_A_LEDGER_EDIT
target_claim: "NONE — no GU source claim is targeted, attacked or defended. The object BUILT is the spin-extended 4D anomaly target lattice `Z^6_ext = Z^6 ⊗ Z^5_spin = Z^30` that PHI-1 §7.3 named as its own weakest seam and left unbuilt, together with the extended condition system on it and the extended reduction `phi_ext : Z^15 → Z^30`. The objects ADJUDICATED are (i) PHI-1's own seam statement — that `D1..D5` on `Z^6` are not the complete 4D conditions for a spectrum with charged spin-3/2, that 'the rank result survives', and that AC-1's `(3,4,5)`/`(-21,-20,-19)` rescalings are what has to be wired in; and (ii) PHI-1's decision `phi(ker M) ⊆ L ⟺ v ∈ L`, re-run on the extended target. The carrier bit is CARRIED AS A FORK and is NOT adjudicated."
grade: "EXACT throughout: exact Chern-root expansion in sympy with the degree-4 part decomposed against `(p1, e)` and the decomposition verified by subtraction, `fractions.Fraction` and integer linear algebra over Q, sympy Rational, Smith normal form on integer matrices, integer weight-multiset representation decomposition inherited from PHI-1. No float is load-bearing anywhere; `assert_no_float` sweeps the result dict. 121/121, exit 0, via `tests/channel-swings/joe_directed_phi2_spin_extended_target_lattice.py`, which IMPORTS `tests/channel-swings/joe_directed_anomaly_cancellation_probe.py` (AC-1's own `anomaly_coeffs`, never reimplemented) and `tests/channel-swings/joe_directed_phi_reduction_construction.py` (PHI-1, which in turn imports CB-C). Certificate splits as 83 [E] exact results, 19 [C] controls that must fire, 19 [R] reproductions of filed owners (AC-1's spin-1/2 coefficients and the whole `(3,4,5)`/`(-21,-20,-19)` carrier table; PHI-1's `k = (-1)^p`, five Lorentz types, `T(ker M) = Z^5`, rank-10 kernel; LA-3's rank 4 and `f5`; CB-C's `W` in the row space). FAILURE PATH EXERCISED: six planted mutations (`twist`, `euler`, `no-mixed-rescale`, `witness`, `decomp`, `gauge-blind`) each run to exit 1 through the check harness. NOT: a source action, a decision of the carrier bit, a decision of the SOLDERED-AD fork, a supply of `v`, a chirality-production mechanism, a generation count, a ledger edit, or any verdict movement."
disposition: SPIN_EXTENDED_TARGET_BUILT__CONDITION_SYSTEM_HAS_RANK_5_NOT_LA3S_4__LA3_RELATION_BROKEN_WITH_EXACT_RESIDUAL_MINUS_216_H_TENSOR_F5__L_EXT_HAS_RANK_25_AND_IS_STRICTLY_LARGER_THAN_L_TENSOR_Z5_WITH_AN_ALL_NONNEGATIVE_WITNESS_WHOSE_SPIN_HALF_PROJECTION_IS_SU3_CUBED_ANOMALOUS__PHI1_RANK_ONE_DOES_NOT_SURVIVE_RANK_PHI_EXT_IS_3__PHI1_ZERO_BIT_RESULT_SURVIVES__PHI1_CONTAINMENT_SURVIVES_VERBATIM_v_IN_L_FOR_EVERY_CARRIER_AND_UNDER_ARBITRARY_HIGHER_SPIN_COEFFICIENTS__BECAUSE_THE_p0_DEPOSIT_IS_A_PURE_SPIN_HALF_SLOT_AND_GAUGE_BLINDNESS_PUTS_THE_SAME_v_IN_EVERY_SLOT__GAUGE_BLINDNESS_IS_NOW_VERDICT_LOAD_BEARING_NOT_ONLY_RANK_LOAD_BEARING__CARRIER_BIT_NOT_ADJUDICATED__ZERO_ROWS_ADVANCE
canon_verdict_change: none
priority_change: none
steering_effect: unchanged
canonical_effect: pending_integration
rows_touched: [AC-C2, AC-D1, AC-D2, AC-D3, AC-D4, AC-D5, AC-E1]
rows_advanced: 0
grants_retyped: []
depends_on:
  - lab/active-research/joe-directed/phi-reduction/phi1-the-reduction-is-rank-one-and-the-14d-kernel-contributes-zero-bits-2026-08-15.md
  - lab/active-research/joe-directed/anomaly-cancellation/ac1-rs-content-cannot-obstruct-and-anomalies-cannot-select-2026-08-14.md
  - lab/active-research/joe-directed/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md
  - lab/active-research/joe-directed/ledger-advancement/la5-anomaly-axis-is-seven-handles-not-twenty-six-2026-08-15.md
  - lab/active-research/joe-directed/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md
  - lab/active-research/joe-directed/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md
  - explorations/conditional-build/cb-c-anomaly-conditions-2026-08-05.md
  - canon/carrier-bit-decision-campaign-RESULTS.md
  - canon/gamma-traceless-38-adjudication-RESULTS.md
  - lab/methods/source-native-comparator-routing.md
scripts:
  - tests/channel-swings/joe_directed_phi2_spin_extended_target_lattice.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact is built
> entirely inside a conventional particle-physics comparator: the 4D
> Standard-Model perturbative gauge-anomaly conditions, the lattice
> `L = Z·(15 of SU(5)) ⊕ Z·(nu^c)`, and the ordinary index-density prescription
> for higher-spin anomaly coefficients. Those are **fork-1** objects
> (`lab/methods/source-native-comparator-routing.md`, "Ordinary family index or
> net chirality versus Weinstein's `2+1`"). Every result below binds only that
> named model. It is **not** evidence for or against Weinstein's differently
> constructed source-native mechanism without an explicit typed bridge, and the
> ordinary-index arena is precisely the one the routing document warns is not
> the GU-native one.
> Classification: **`BRIDGE_OR_SEMANTIC_BOUNDARY`.**

# PHI-2 — the spin-extended target has rank five, and PHI-1's containment survives it

**Blunt statement first.** I built the extension. It is not scoped, it is
constructed and decided: the target lattice is `Z^30`, the extended condition
system has **rank 5** where LA-3's spin-1/2 system had rank 4, the extended
anomaly-free lattice has **rank 25** and is strictly larger than "SU(5)-complete
in every spin slot", and there is an explicit all-non-negative spectrum that is
anomaly-free on the extended system while its spin-1/2 projection is
`SU(3)^3`-anomalous. So PHI-1's seam was real.

And then: **PHI-1's containment survives it verbatim.**
`phi_ext(ker M) ⊆ L_ext ⟺ v ∈ L`, for every horn of the carrier bit, with or
without the Euler channel, and under arbitrary spin coefficients on the three
higher-spin slots. One thing of PHI-1's does *not* survive: `rank(phi) ≤ 1` was
a spin-1/2-projection artefact, and `rank(phi_ext) = 3`.

**Zero rows advance.** What moves is that PHI-1's corrected condition string is
now known to be robust against the exact objection PHI-1 raised against itself,
and that gauge-blindness has been promoted from *rank*-load-bearing to
*verdict*-load-bearing.

---

## 0. Prior art, swept by mechanism, and what this file does not re-claim

| already owned | by | what PHI-2 does with it |
|---|---|---|
| the twist → degree-6 anomaly map, its factorisation into `(spin coefficient) × (group invariant)` with zero residue, and the whole `(3,4,5)` / `(−21,−20,−19)` carrier table | AC-1, `tests/channel-swings/joe_directed_anomaly_cancellation_probe.py` | **imported and called**, never reimplemented. The carrier table is **reproduced** as three points of the new lattice. |
| the `−21/−20/−19` and `−42/−40/−38` column at literature-fetched grade (PTZ, Homma–Semmelmann, Bilal), and carrier B = the gamma-traceless field space | `canon/carrier-bit-decision-campaign-RESULTS.md`, `canon/gamma-traceless-38-adjudication-RESULTS.md` | **carried as a fork, not adjudicated.** The identification "carrier B ↔ the gamma-trace-constrained field space" is canon's, not new here. |
| the exact `sl(2,C)⊕sl(2,C)` decomposition of `Λ^p T*X4 ⊗ (1/2,0)`, the five occurring Lorentz types, `k_p = (−1)^p`, `T(ker M) = Z^5`, `phi = v ⊗ k` | PHI-1 | **imported**; the five types become the five spin slots and `k` is recovered as the spin-1/2 projection of the extended map |
| the 14D system (`12×15`, rank 5, `ker M` rank 10), `W` in the row space | CB-C, via PHI-1 | **imported**, never re-derived |
| 4D rank 4, the relation `2D1 − 27D2 − 36D3 − 9D4 + 9D5 = 0`, `L` rank 2 and saturated | LA-3 | **reproduced**, then shown to be broken by the extension |
| charge conventions on doubled integer weights | MJ-5, via AC-1 | inherited |

Nothing below claims novelty for any row of that table. In particular the
`(3,4,5)` / `(−21,−20,−19)` numbers are **AC-1's**, and the reading of carrier B
as the gamma-traceless field space is **canon's**.

---

## 1. PREFLIGHT — PHI-1's seam, re-derived independently, and what moved

PHI-1 §7.3 states the seam exactly:

> "The spin-1/2 projection discards charged `(1,1/2)`, `(3/2,0)`, `(1/2,1)`
> content carrying the same internal numbers. `Z^6` has no spin slot, so
> `D1..D5` on `Z^6` are NOT the complete 4D conditions for a spectrum with
> charged spin-3/2. The rank result survives; the target lattice would need
> extending. AC-1 already has the exact RS rescalings (`3,4,5` /
> `−21,−20,−19`) to wire in."

Re-derived from AC-1's and PHI-1's own tables before building anything.
**Three things moved.**

**(i) "The rank result survives" is false as stated, and harmless.** The rank
result is a statement about a map into a target. Change the target and the map
changes: `phi_ext : Z^15 → Z^30` has **rank 3**, because `Λ^1` and `Λ^3` deposit
identically and the two `p = 2` higher-spin slots deposit identically, giving
`Im K = {(a,b,b,c,c)}`. What survives is the *use* PHI-1 made of the rank —
LA-5's bound `rank ≤ rank(L)` — because the bound moves with the target too:
`rank(L_ext) = 25`. So the bound is even less discriminating than PHI-1 found,
and PHI-1's headline "the reduction is rank one" must be read as *"the
spin-1/2-projected reduction is rank one"*. Filed as a scope correction to
PHI-1's title, not a defect in its computation.

**(ii) "AC-1 already has the exact RS rescalings to wire in" is two-thirds
true.** `(3,4,5)` and `(−21,−20,−19)` are the three carrier readings of the
**`p = 1` slot only** — the vector-spinor `Λ^1 T*X4 ⊗ S^+` and its two field-space
declarations. They say nothing about the `p = 2` higher-spin content
`(3/2,0) ⊕ (1/2,1)`, which needs gauge ratios `2` and `3` and mixed ratios `−22`
and `−21`. That is checkable directly against AC-1's own table, which has one
twist family, `T_C + q`. So the seam under-counted what had to be supplied by
exactly the two slots that carry the word "spin-3/2" in its own sentence.
Deriving those two entries is the actual new work in §2.

**(iii) The seam's worry does not propagate, and the reason was available
before computing.** "`D1..D5` on `Z^6` are not the complete conditions" is true
(§4 exhibits a witness). But the criterion `phi(ker M) ⊆ L` is not evaluated on
all of `Z^30` — it is evaluated on `phi_ext(Z^15)`, and gauge-blindness (PHI-1
§2.1, which is `M`'s own assumption) forces that image to be a **pure tensor**
`v ⊗ Im K`. On a pure tensor every extended condition evaluates as
`(scalar) × (spin-1/2 condition on v)`. Predicted before the build; confirmed
in §5. This is the whole answer, and it is structural rather than numerical.

Everything else re-derives unchanged: the five Lorentz types, `k = (−1)^p`,
`T(ker M) = Z^5` with Smith divisors all 1, `L` rank 2 and saturated, the 4D
system rank 4 with the LA-3 relation.

### Preflight lenses, run inline

- **Index theory / characteristic classes.** Only *bundle-valued* fields have a
  canonical twist. An irreducible Lorentz type is not a bundle until you name
  one, so any twist assigned to `(3/2,0)` or `(1/2,1)` is derived by subtraction
  and must be checked for consistency. This lens predicted, before computing,
  that the `Λ^2_±` split would drag in the **Euler class** — because `Λ^2_±` are
  the only 4D-specific (non-stable) pieces in the list. It did: `ch(Λ^2_±) =
  3 + p1 ± 2e`. Carried as an explicit fork in §3, shown irrelevant to the
  verdict in §5.
- **Representation theory (`sl2 ⊕ sl2`).** A subtraction-derived assignment has
  exactly one internal check available: for each form degree, the type
  contributions must re-sum to the `Λ^p` twist. Set up as a mandatory closure
  test before any conclusion; it is §2's five `p`-rows and it is what certifies
  the `2` and `3` entries.
- **Lattice theory / saturation.** The question is an image-of-sublattice
  question again, so saturation will be load-bearing again — and the new
  question is whether the image is a *pure tensor* in `Z^6 ⊗ Z^5`. Flagged
  before the build; it is the mechanism, §5.
- **Anomaly-channel bookkeeping.** `D1..D4` are four components of the *single*
  symmetric cubic `Tr_R X^3`; `D5` is the *different* channel `p1 Tr_R X`. AC-1's
  factorisation says the two classes carry different spin coefficients.
  Therefore **any** linear relation whose support crosses the two classes must
  break under the extension — and LA-3's relation does exactly that. This lens
  predicted the rank rise `4 → 5` before it was computed.
- **Adversarial / red-team.** Two attacks set up in advance and built as live
  controls, not prose: (a) the observation might deposit *different* internal
  content in the higher-spin slots — the solder horn, §6.3, which is the only
  construction that changes the verdict; (b) the `p = 0` generator might not be
  load-bearing — controlled by degenerating the other two generators, §5.
- **Fork hygiene / ledger accounting.** The carrier bit must not be silently
  decided by the shape of the construction. Set up in advance as a hard
  requirement: express all three carriers as **points of the same lattice**
  rather than as three different condition systems. That is what §2 does, and it
  is why the fork can be reported rather than resolved.

---

## 2. THE CONSTRUCTION — five spin slots and their twists

### 2.1 The slots

PHI-1's exact weight-multiset decomposition of `Λ^p T*X4 ⊗ (1/2,0)` produces
five Lorentz types and no others:

```
   p=0   (1/2,0)
   p=1   (1,1/2) + (0,1/2)
   p=2   (3/2,0) + (1/2,0) + (1/2,1)
   p=3   (1,1/2) + (0,1/2)
   p=4   (1/2,0)
```

The extended target is
`Z^6_ext := Z^6 ⊗ Z^5_spin = Z^30`, with coordinates `n_{i,s}` indexed by an SM
constituent `i ∈ {Q, u^c, d^c, L, e^c, ν^c}` and a Lorentz type
`s ∈ {(1/2,0), (0,1/2), (1,1/2), (3/2,0), (1/2,1)}`. The three types PHI-1's
seam named are exactly the three that carry a `p1` in their twist.

### 2.2 The twists, derived by subtraction

`ch(Λ^p T_C)` is computed exactly from the Chern roots `{±x1, ±x2}`, with the
degree-4 part resolved against `(p1, e)`, `p1 = x1²+x2²`, `e = x1x2`:

```
   ch(Lambda^0 T_C) = 1              ch(Lambda^3 T_C) = 4 + p1
   ch(Lambda^1 T_C) = 4 + p1         ch(Lambda^4 T_C) = 1
   ch(Lambda^2 T_C) = 6 + 2 p1       ch(Lambda^2_+)  = 3 + p1 + 2e
                                     ch(Lambda^2_-)  = 3 + p1 - 2e
```

No `Λ^p T_C` carries an Euler term; the two halves of `Λ^2` do, with opposite
sign. Each irreducible type's twist then follows by subtraction inside the
decomposition, with `S^-` entering as the virtual twist `−1` (same gauge rep,
opposite chirality, so all five odd functionals `D1..D5` flip sign):

| type | realised as | twist | `t0` | gauge ratio `g` | mixed ratio `m` | Euler `e` |
|---|---|---|---|---|---|---|
| `(1/2,0)` | `S^+` | `1` | 1 | **1** | **1** | 0 |
| `(0,1/2)` | `S^-` | `−1` | −1 | **−1** | **−1** | 0 |
| `(1,1/2)` | `Λ^1 ⊗ S^+ ⊖ (0,1/2)` | `T_C + 1` | 5 | **5** | **−19** | 0 |
| `(3/2,0)` | `Λ^2_+ ⊗ S^+ ⊖ (1/2,0)` | `Λ^2_+ − 1` | 2 | **2** | **−22** | **+2** |
| `(1/2,1)` | `Λ^2_- ⊗ S^+` | `Λ^2_-` | 3 | **3** | **−21** | **−2** |

Ratios computed by calling **AC-1's own `anomaly_coeffs`**, with AC-1's residue
check (no 4D pure-gravitational term) re-run for every row.

Two things are worth naming precisely.

**The `(1,1/2)` row is AC-1's carrier B, reproduced.** `(5, −19)` is exactly
the `T_C + 1` / gamma-traceless entry. That is not a new identification —
`canon/carrier-bit-decision-campaign-RESULTS.md` already reads carrier B as the
gamma-trace-constrained field space, and PTZ's `−19 = −20 + 1` is the same
arithmetic in the other sign convention. What this construction adds is only
that the three carriers become three *points* of `Z^30`:

```
   carrier A (ghost-subtracted, T_C - 1)   w = (-1, 1, 1, 0, 0)   g.w = 3   m.w = -21
   bare      (vector-spinor,   T_C    )   w = ( 0, 1, 1, 0, 0)   g.w = 4   m.w = -20
   carrier B (gamma-traceless, T_C + 1)   w = ( 0, 0, 1, 0, 0)   g.w = 5   m.w = -19
```

so the fork is a choice of which lattice point the `p = 1` deposit is, not a
choice of condition system. **The bit is not adjudicated here.** The observation
itself deposits the reducible bundle `Λ^1 T*X4 ⊗ s^*S`, i.e. the bare row; A and
B are declarations about the field space imposed on it, which is SG4's object.

**The `(3/2,0)` and `(1/2,1)` rows are the new entries.** `2` and `3` in the
gauge channel, `−22` and `−21` in the mixed channel. They pass the only
available internal check: for every `p`, the type ratios re-sum to the `Λ^p`
twist —

```
   p :        0     1     2     3     4
   gauge :    1     4     6     4     1     = C(4,p)
   mixed :    1   -20   -42   -20     1
   euler :    0     0     0     0     0     (the two Euler terms cancel at p = 2)
```

and the closure is non-trivial: `(3/2,0) + (1/2,1)` alone give `(5, −43, 0)`,
which is `Λ^2` minus its spin-1/2 piece.

### 2.3 The exact mechanism, in one line

```
        m  =  g  -  24 . h ,        h = (0, 0, 1, 1, 1) = the higher-spin indicator
```

`g_s = t0` and `m_s = t0 − 24 t1`, and `t1 = 1` on exactly the three higher-spin
slots. The `24` is the `Â`-genus denominator. Everything in §3 is a consequence
of this single identity.

---

## 3. THE EXTENDED CONDITION SYSTEM, AND ITS RANK

AC-1's factorisation theorem is used as a theorem: the degree-6 anomaly splits
channel by channel into `(spin coefficient) × (group invariant)` with zero
residue. `D1..D4` are four components of the one symmetric cubic `Tr_R X^3`, so
they rescale by `g`; `D5 = grav²-U(1)_Y` is the mixed `p1 Tr_R X` channel, so it
rescales by `m`. Writing `f_a` for LA-3's five functionals on `Z^6`:

```
        D_a^ext  =  g (x) f_a   (a = 1..4)          D_5^ext  =  m (x) f_5
```

a `5 × 30` integer/rational system.

> **RANK 5.** LA-3's spin-1/2 system had rank 4. The extension adds exactly one
> independent condition.

**LA-3's relation is broken, with an exact residual.**

```
   2 D1^ext - 27 D2^ext - 36 D3^ext - 9 D4^ext + 9 D5^ext
        =  9 (m - g) (x) f5  =  -216 . h (x) f5     ( != 0 )
```

and it survives *exactly* on the spin-1/2 sublattice, where `h = 0`. So LA-3's
degeneracy was never a fact about the anomaly channels; it was a fact about a
spectrum in which every field has the same spin coefficient. Control with power:
setting `m := g` — pretending the mixed channel does not rescale — returns rank 4
and restores the relation, so the rank rise is bought entirely by `m ≠ g`.

**The Euler fork, carried explicitly.** If `e ∧ Tr F` is admitted as a sixth 4D
channel, the coefficient vector is `(0,0,0,2,−2)`, it is not in `span(g, m)`, and
the rank is **6**, with `L_ext` of rank 24. Whether that 6-form descends to a
genuine 4D anomaly is **not settled here**. It is carried as a fork because §5
shows the verdict does not depend on it.

---

## 4. THE EXTENDED ANOMALY-FREE LATTICE — and PHI-1's seam, confirmed with an object

Write `V_g(n) = Σ_s g_s n_{·,s} ∈ Z^6` and `N_H(n) = Σ_{s ∈ higher} n_{·,s} ∈ Z^6`.
Then, proved by **row-space identity** rather than by sampling:

```
        L_ext  =  { n in Z^30 :  V_g(n) in L    AND    f5 . N_H(n) = 0 }
                  rank 25   ( rank 24 if the Euler channel is admitted )
```

So the one condition the extension adds is exactly: **the total charged
higher-spin content must have vanishing `grav²-U(1)_Y`.** That is the physical
reading of the rank going `4 → 5`.

`L_ext` is strictly larger than `L ⊗ Z^5` — "SU(5)-complete in every spin slot".
The witness is explicit and every multiplicity is **non-negative**:

```
        two u^c, two d^c, two e^c        as spin-1/2  (1/2,0)
        one Q,   one L                   as charged   (3/2,0)
```

`V_g = 2·(15 of SU(5)) ∈ L`; `f5 · V_m = 0`; the Euler channel also vanishes on
it. Its spin-1/2 projection is `(0,2,2,0,2,0)`, which is **not** in `L` — its
`SU(3)^3` anomaly is `D1 = −4`.

> **PHI-1's seam is confirmed with an object.** `D1..D5` on `Z^6` really are not
> the complete 4D conditions once charged spin-3/2 is present: there is an
> honest, all-non-negative, extended-anomaly-free spectrum whose spin-1/2
> shadow is badly anomalous.

Controls fire: deleting the `(3/2,0)` lepton doublet breaks it; moving the two
charged `(3/2,0)` fields down into spin-1/2 breaks it.

---

## 5. THE EXTENDED REDUCTION, AND THE VERDICT

The observation deposits `Λ^p T*X4 ⊗ s^*S` for `p = 0..4`, so

```
        phi_ext  =  v (x) K ,     K : Z^15 -> Z^5_spin  the decomposition matrix

        K_{(1/2,0)} = x0 + x2 + x4      K_{(3/2,0)} = x2
        K_{(0,1/2)} = x1 + x3           K_{(1/2,1)} = x2
        K_{(1,1/2)} = x1 + x3
```

`rank(phi_ext) = 3` for every `v ≠ 0`; `Im K = {(a,b,b,c,c)}`, saturated. Its
spin-1/2 projection is `(+1,−1,+1,−1,+1)` — PHI-1's `k`, recovered. Its
`g`-weighting is `C(4,p) = (1,4,6,4,1)`; its `m`-weighting is
`(1,−20,−42,−20,1)`; its Euler weighting is **identically zero**, because the
reduction deposits `(3/2,0)` and `(1/2,1)` with equal multiplicity.

**The zero-bit result survives.** `T(ker M) = Z^5` is a statement about `M` and
the truncation, untouched by the target. It has a sharper corollary worth
recording: *since `T` is onto, no nonzero functional supported on the observed
slots `p = 0..4` can annihilate `ker M`.* Verified for both `(1,4,6,4,1)` and
`(1,−20,−42,−20,1)`, in contrast to CB-C's `W` and PHI-1's `k''`, whose support
reaches `p ≥ 5`. Hence

```
        phi_ext(ker M)  =  phi_ext(Z^15)  =  v (x) Im K
```

— 14D anomaly cancellation still contributes **exactly zero bits** to the 4D
verdict through the observation.

**And the containment survives.** Evaluating `L_ext` on the pure tensor
`v ⊗ w`:

```
        v (x) w  in  L_ext    <==>    (g.w) v in L    and    (m.w) (f5 . v) = 0
```

On the `p = 0` generator `w = (1,0,0,0,0)` this reads `v ∈ L` outright, because
that slot is pure spin-1/2 with `g = 1`. And `v ∈ L ⟹ f5·v = 0`, so every other
generator's condition is then automatic. Therefore

```
        phi_ext(ker M) subset L_ext     <==>     v in L
                                        <==>     the observed 4D content is SU(5)-complete
```

Verified exhaustively over `[−3,3]^6`, with the same positive witnesses (`16`,
`15`, `15 + 7ν^c`, `4×16`) and the same firing controls (a lone `Q`,
`(1,1,1,1,0,0)`, a `16` minus one `d^c`) that PHI-1 used, plus:

- the verdict is identical for **all three carriers** (`g·w = 3, 4, 5`);
- identical **with the Euler channel admitted**;
- identical under **all 1029 perturbed higher-spin coefficient assignments**
  swept — because the `p = 0` slot's coefficient is `1` by definition of
  spin-1/2 and cannot be perturbed away.

Control with power, so this is not vacuous: delete the `p = 0` generator *and*
tune the higher-spin gauge coefficients to annihilate the two survivors, and
`v = (2,1,0,0,0,0) ∉ L` passes. The collapse to `v ∈ L` is genuinely bought by
the `p = 0` slot.

---

## 6. THE FORKS, AND WHAT EACH DOES TO THE ANSWER

### 6.1 The carrier bit — both branches carried, verdict invariant

| | `g·w` | `m·w` | rank of the extended system | `L_ext` | containment |
|---|---|---|---|---|---|
| carrier A (`T_C − 1`, ghost-subtracted) | 3 | −21 | 5 | rank 25 | `v ∈ L` |
| bare (`T_C`, the bundle the observation deposits) | 4 | −20 | 5 | rank 25 | `v ∈ L` |
| carrier B (`T_C + 1`, gamma-traceless) | 5 | −19 | 5 | rank 25 | `v ∈ L` |

The carrier bit changes **which point of `Z^30`** the `p = 1` deposit is. It does
not change the rank, the lattice, or the verdict. This is the reduction-level
analogue of AC-1's "anomalies cannot select the carrier bit", by a different
mechanism: AC-1's zero came from vanishing group invariants on the `16`; here it
comes from the `p = 0` slot forcing `v ∈ L` before the RS slot is consulted.
**Neither is a decision of the bit, and `SG4` remains the sole decider.**

`AC-C2` also survives every carrier: the extended doublet count is
`(g·w) · 4 n_Q` for `v ∈ L`, divisible by 4 in all three cases; and it fails for
`v ∉ L` (a `16` minus its lepton doublet gives `3` on the `p = 0` deposit and `9`
on carrier A's, neither divisible by 4).

### 6.2 The Euler channel — undecided, and shown not to matter

Admitting `e ∧ Tr F` raises the rank to 6 and drops `L_ext` to rank 24. It does
not touch the verdict, because the reduction's Euler weighting is identically
zero: the two `p = 2` higher-spin slots are deposited with equal multiplicity and
their Euler coefficients are `+2` and `−2`. This is the **exact missing datum**
of the extension, and it is named rather than guessed: *whether the Euler class
term in `ch(Λ^2_±)` contributes an admissible 4D anomaly channel*. Everything
that depends on it is reported on both branches.

### 6.3 Velo–Zwanziger — upstream of this file, and orthogonal to it

Whether a *charged* spin-3/2 field propagates causally at all is the repo's open
VZ fork (`explorations/vz-evasion/`, `canon/carrier-bit-decision-campaign-RESULTS.md`
LEG-3: the published VZ-escape fork *coincides* with the carrier fork). If the
answer is no, the three new slots are unphysical and `Z^30` is a formal object.
The verdict is `v ∈ L` either way, so PHI-2 neither needs nor supplies a VZ
resolution.

---

## 7. POSTFLIGHT

**Postflight lenses, run inline: index theory / characteristic classes;
representation theory; lattice theory and saturation; anomaly-channel
bookkeeping; adversarial red-team; fork hygiene and ledger accounting.**

### 7.1 Strongest overclaim available, and why it is refused

*"The complete 4D anomaly conditions are now built, they have rank 5, and PHI-1's
`v ∈ L` survives them — so `AC-D1..D5`'s residual condition is closed and the
higher-spin worry is dead."*

Refused on four counts, in descending order of severity.

1. **The prescription is inherited, not established.** Every number in §2 rests
   on "a 4D field valued in `Λ^p T*X ⊗ S^+ ⊗ F` has anomaly
   `[Â ch(Λ^p T_C) ch_F]_6`". That is AC-1's own assumption — it is how AC-1
   twists the RS field by `T_C + q` — and it is inherited here, not re-derived.
   For `p = 1` it has a published anchor. For `p ≥ 2` it does not: `(3/2,0)` and
   `(1/2,1)` fields carry constraints and ghosts of their own and **no ghost
   scheme is declared for them anywhere in this repo or in this file**. My `t0 = 2`
   and `t0 = 3` are the unconstrained-bundle readings, i.e. the analogue of the
   *bare* carrier, not of A or B. The `p = 2` slots therefore have their own
   undeclared carrier bit.
2. **What is scheme-dependent, and what is not.** The verdict `v ∈ L` is
   scheme-independent — proved, not sampled, and swept over 1029 perturbed
   assignments. `L_ext` and the §4 witness are **not**: shift `t0` on a
   higher-spin slot and both change. So "the extended lattice is `rank 25` and
   `L_ext = {V_g ∈ L, f5·N_H = 0}`" is a result *about the bare-scheme
   extension*, and must be quoted with that qualifier.
3. **"Rank 5" and "zero bits" must be stated together.** The extension adds one
   independent condition **on the target lattice**, and simultaneously adds
   **zero bits to the verdict through the reduction**. Quoting the first without
   the second reads as a strengthening of the anomaly axis; it is not one.
4. **Nothing here supplies `v`.** As in PHI-1, the 14D half is complete and the
   4D half is a grant owned by the representation axis. The extension changed the
   target of the map, not the fact that its only free parameter is `U1`/`EMB`'s
   object.

A fifth, weaker overclaim also refused: this file does **not** show that
charged spin-3/2 is harmless in GU. It shows that *on the pullback horn, with
gauge-blindness, the anomaly criterion does not see it*. Those are different
statements, and §6.3 is where the difference lives.

### 7.2 Strongest contrary construction, built

Not described — built, as a live control. **Break gauge-blindness.** Let the
observation deposit internal content `v` in the spin-1/2 slots and a *different*
`v'` in the higher-spin slots. Then the image is no longer a pure tensor, the
`p = 2` generator reads `v + 5v' ∈ L`, and the criterion becomes

```
        v in L   AND   v' in L        ( strictly stronger )
```

verified: `containment(v = 16, v_high = Q) = False`, and `= True` when the two
agree. This is the **decisive finding of the extension**, and it is a
strengthening of the stakes rather than of the result: in PHI-1's `Z^6` arena,
denying gauge-blindness only changed the *rank* (its §2.1 control reaches rank 5);
on the extended target it changes the **verdict**. So the `SOLDERED-AD` fork —
already open, already named by MD-1 and LA-8 — is now verdict-load-bearing for
`AC-D1..D5` in a way it was not before this file.

Why the horn is nonetheless not available *here*: gauge-blindness of the form
index is `M`'s own assumption (PHI-1 §2.1, verified over all 15 columns — the
Casimir `Y` occurs only in `ch(S)`), so a reduction that denies it does not get a
different `phi_ext`; it loses `ker M`, and with it the question.

The second contrary — the disavowed KK horn — is unchanged from PHI-1 and is not
re-run: it empties the 4D spectrum, and an empty spectrum has no spin content to
extend.

### 7.3 Weakest seam

**The `p = 2` slots have an undeclared ghost scheme, and `L_ext` depends on it.**
This is the same defect one level up that PHI-1's seam was one level down.
PHI-1 discarded higher-spin content entirely; PHI-2 admits it with the
*unconstrained-bundle* twist and no declared constraint structure. The exact
missing datum is: **for a 4D field valued in `Λ^2_± T*X ⊗ S^+`, what is the
ghost/constraint subtraction?** For `p = 1` the repo has three answers and calls
the choice the carrier bit; for `p = 2` it has none, and this file supplies the
bare one and sweeps the neighbourhood rather than deriving it. The sweep is what
makes the verdict safe; it does not make `L_ext` safe.

Second seam, smaller and named in §6.2: whether `e ∧ Tr F` is an admissible 4D
anomaly channel. Both branches reported; rank 5 vs 6, `L_ext` 25 vs 24, verdict
unchanged.

Third seam, inherited verbatim from PHI-1 §7.2 and not improved here: the arena.
`Z^6` is the SM **constituent** lattice, `Z^30` is that tensored with a 4D
Lorentz-type basis. If the true 4D content has exotics, the arena moves again.
LA-3's own arena-extension controls already show one exotic `Y = 1/2` singlet
restores rank 5 in the spin-1/2 arena. The arena is a fork-1 comparator choice
and it is not derived.

---

## 8. WHAT MOVES FOR THE SEVEN ROWS

**Zero verdict advances.** Stated first so nothing below reads as a promotion.

| row | after PHI-1 | after PHI-2 |
|---|---|---|
| `AC-D1..D5` | corrected `distance`: *"none after the internal SM content `v` of the observed 4D spinor is fixed, and `v` is SU(5)-complete"* | **unchanged, and now robust.** PHI-1 flagged that its own correction might not survive a target that carries charged spin-3/2. It does: the criterion is still exactly `v ∈ L`, for every carrier, with or without the Euler channel, under arbitrary higher-spin coefficients. The revival trigger still fires iff `v ∉ L`. |
| `AC-C2` | reconfirmed with the divisibility-by-4 sharpening | **unchanged.** Extended doublet count is `(g·w)·4n_Q`; divisible by 4 for every carrier; fails outside `L`. |
| `AC-E1` | untouched | **untouched.** PHI-2 is a statement about the perturbative lattice and supplies nothing toward the global/Dai–Freed recomputation. |

**The structural consequence.** PHI-1 removed `U4`'s anomaly-relevant half as an
independent grant atom by showing it is a function of `U1`/`EMB`. PHI-2 does not
restore it — but it does show that the *other* half of `U4`, the
gauge-blindness/soldering question, is now verdict-load-bearing rather than
merely rank-load-bearing for these rows. That is a re-weighting of an existing
open fork, not a new grant and not a verdict.

---

## 9. CERTIFICATE

`tests/channel-swings/joe_directed_phi2_spin_extended_target_lattice.py` —
**121/121, exit 0.**

```
   [E] 83   exact results
   [C] 19   controls that must fire
   [R] 19   reproductions of filed owners
```

Reproductions: AC-1 (its probe re-run clean under import, exit 0; spin-1/2
coefficients `1/6` and `−1/24`; zero degree-6 residue; `ch(T_C) = 4 + p1`; the
whole `(3,4,5)` / `(−21,−20,−19)` carrier table); PHI-1 (its probe re-run clean
under import, exit 0; `k_p = (−1)^p`; the five Lorentz types; the three
higher-spin types; `ker M` rank 10; `T(ker M) = Z^5` with Smith divisors all 1);
LA-3 (rank 4 on `Z^6`; `f5 = (1,−2,1,−1,1,0)`; the relation still holding on
`Z^6`); CB-C (`W = Σ_p x_p C(14,p)` in the row space of `M`).

Exactness: exact Chern-root expansion with the degree-4 part resolved against
`(p1, e)` by exact polynomial coefficient extraction; `fractions.Fraction` and
integer arithmetic over `Q`; sympy `Rational`; Smith normal form on integer
matrices. `assert_no_float` sweeps the result dict. No float is load-bearing
anywhere. AC-1's `anomaly_coeffs` is **called**, not reimplemented.

**Failure path exercised — six planted mutations, each exits 1 through the check
harness:**

| `--mutate=` | plants | fires |
|---|---|---|
| `twist` | `(3/2,0)` gets `t0 = 3` instead of `2` | 9 checks |
| `euler` | flips the sign of `ch(Λ^2_-)`'s Euler term | 7 checks |
| `no-mixed-rescale` | sets `m := g` (the mixed channel does not rescale) | 8 checks |
| `witness` | corrupts the §4 exotic witness | 3 checks |
| `decomp` | drops `(3/2,0)` from the `p = 2` decomposition | 4 checks |
| `gauge-blind` | asserts the soldered map gives the same verdict | 1 check |

---

## 10. WHAT THIS DOES NOT SUPPLY

No source action. No decision of the carrier bit — all three carriers are
carried as three points of `Z^30` and all three give the same verdict, which is
evidence that anomalies cannot select, not a selection. No decision of the
`SOLDERED-AD` fork; §7.2 raises its stakes and leaves it open. No ghost scheme
for the `p ≥ 2` slots; §7.3 names that as the missing datum. No resolution of the
Velo–Zwanziger question. No supply of `v`. No chirality-production mechanism, no
generation count, no real-form statement. No ledger edit and no verdict movement.
No claim about the global/Dai–Freed sector. The 14D system is imported, AC-1's
anomaly machinery is imported, and LA-3's 4D lattice is reproduced; none of the
three is re-claimed here.
