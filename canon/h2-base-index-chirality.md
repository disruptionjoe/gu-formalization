---
title: "H2 result: base-topology index, the parity of the GU generation count, and the Lorentzian-complexification tension"
status: active
doc_type: result
created: 2026-06-28
depends_on:
  - canon/leg3-closure-and-spinor-2smoothness.md
  - canon/ghost-parity-krein-synthesis.md
  - canon/no-go-quaternionic-parity-generation-sector.md
supersedes:
  - canon/multiplicity-theorem.md  # provenance: this successor corrects/replaces the superseded predecessor; not a load-bearing dependency on its (retired) claim
tests:
  - tests/generation-sector/t1a_kinematic_chirality_kill.py
  - tests/generation-sector/h1_selfdual_family_kill.py
  - tests/generation-sector/leg3_family_embedding_enumeration.py
  - tests/generation-sector/step9_selfdual_connection_index.py
---

# H2: base-topology index, the parity of the generation count, and the Lorentzian complexification

## Scope and standing of the claims

This resolves H2 (the Lorentzian-complexification tension) and the open chiral question handed up by H1/T1a:
T1a established that **kinematics** gives net chirality 0 on the generation triplet (the `so(p,q)`-invariant
Krein form is purely cross-chirality, `||K(+,+)|| , ||K(-,-)|| ~ 1e-14`, so every positive-norm subspace is
exactly 50/50 and net chirality `= 0` in `(9,5)`, `(7,7)`, `(14,0)`). The one escape T1a left open was a
**base-manifold Dirac index**: gauge the GU-native family `su(2)` by an instanton on the 4-base `X^4` and let
Atiyah-Singer supply a net chiral count. This document closes that escape.

Two boundaries are kept honest throughout:

- The **kinematic / representation-theoretic facts** invoked (the H1 self-dual decomposition, the T1a Krein
  signature, the leg-3 family enumeration, the `so(p,q)`-connection vanishing of C-05/`step9`) are
  machine-checked and exact on this repo's `Cl(9,5) = M(64,H)` representation.
- The **index-theory layer** (Atiyah-Singer zero-mode counting, Dynkin indices, the reality/Kramers parity
  argument, Rokhlin) is standard mathematics *applied* to that fixed representation content. It is
  analytically careful, not a new machine-checked GU computation. Where it is decisive it is over-determined
  by independent arguments; that redundancy is the robustness test.

Nothing here asserts GU is vindicated or refuted. The result splits cleanly into a *multiplicity* statement
(native, strengthened) and a *net-chirality* statement (not internally forced).

This document **confirms the headline verdict** that the net chiral 3 is not GU-internally forced, but it
**corrects three sub-claims** of the original anchored reasoning that the adversarial review refuted:

1. "The generation is in the triplet, **not** the doublet" -- FALSE. The generation is *simultaneously* a
   triplet of `su(2)+` and a doublet of `su(2)-`.
2. "The **only** base route to exactly 3 is the fundamental/doublet with instanton number **k = 3**" --
   FALSE. The anti-self-dual `su(2)-` doublet route reaches exactly 3 at the **minimal** charge `k = 1`.
3. "The self-dual route gives even counts, so GU-native base topology is even, never odd 3" -- correct only
   for the `su(2)+` **adjoint** route, and must be scoped to it. Even-ness is a property of the *real/adjoint*
   channel, not of GU-native base topology in general.

The corrected verdict is *stronger and more honest*, and lands the firewall in the same place by a different,
sharper argument.

## 1. The base-topology index, exactly

The object is the Atiyah-Singer index of the Dirac operator on a compact Euclidean 4-base `X`, coupled to a
gauge bundle `V_R` carrying the family representation `R`:

```
ind(D_R) = integral_X [ -dim(R) * p_1(X)/24  +  ch_2(V_R) ],   ch_2(V_R) = -(1/8 pi^2) tr_R(F^F).
```

With the Dynkin normalization `tr_R(F^2) = 2 T(R) tr_fund(F^2)` and `integral ch_2(V_fund) = k` (the
*definition* of the instanton charge), the gauge piece is the standard

```
ind_gauge(D_R) = 2 * T(R) * k.
```

Dynkin indices for `su(2)` spin-`j`, `T(j) = (1/3) j(j+1)(2j+1)`, normalized `T(1/2) = 1/2`:

| `j` | rep (dim) | `T(R)` | `2 T(R)` | gauge index `2 T k` |
| --- | --- | --- | --- | --- |
| 1/2 | doublet (2) | 1/2 | **1** | `k` |
| 1 | **adjoint/triplet (3)** | **2** | **4** | `4k` |
| 3/2 | quartet (4) | 5 | 10 | `10k` |
| 2 | quintet (5) | 10 | 20 | `20k` |
| 5/2 | sextet (6) | 35/2 | 35 | `35k` |

Two textbook anchors fix the normalization: fundamental `T = 1/2` gives `ind = k` ('t Hooft, one left zero
mode per doublet per instanton); adjoint `T = 2` gives `ind = 4k` (gaugino counting `2N` for `SU(N)`, `N=2`).
A vanishing theorem (Weitzenbock) lets the index be read as a *net chiral* count: for a (anti-)self-dual
connection one Weyl operator has no zero modes, so the `2 T(R) k` modes share one chirality and the index *is*
the chiral asymmetry, with no cancellation.

**Correction to the earlier "unique odd channel" phrasing.** The precise statement is *not* "the doublet is
the unique irrep with odd `2T`" (`j = 5/2` also has `2T = 35`). The load-bearing fact is the **parity by
spin type**: every **integer-spin** (vector/tensor) irrep has `2T(R)` divisible by 4 (`{4, 20, 56, ...}`),
so an integer-spin family channel gives an index divisible by 4 for *any* `k`. Oddness is available only in
**half-integer-spin** channels with `2T` odd, of which the **fundamental doublet** (`2T = 1`) is the one that
appears here. The generation's `su(2)+` carrier is the integer-spin adjoint; its `su(2)-` carrier is the
half-integer-spin doublet. Both facts matter below.

## 2. The family rep the generation actually occupies (corrected)

The GU-native joint content of the generation sector is machine-checked
(`h1_selfdual_family_kill.py`, `leg3_family_embedding_enumeration.py`,
`ghost-parity-krein-synthesis.md` item 2-3):

```
(3)_{su(2)+}  (x)  (2)_{su(2)-}  (x)  (16 + 16bar)_{Spin(10)}      (192-dim triplet sector = 3 * 2 * 32).
```

So the generation is **a triplet of the self-dual `su(2)+` AND a doublet of the anti-self-dual `su(2)-`,
simultaneously**. The earlier clause "the generation is in the triplet, not the doublet" is deleted: it is in
both, because `so(4) = su(2)+ (+) su(2)-` and the generation transforms under each factor. This is the central
rep-assignment correction; it is what opens the second base route in section 4.

The leg-3 enumeration gives the full 16-dim generation multiplicity space under each native `su(2)`:

| family `su(2)` | multiplicity content | odd piece |
| --- | --- | --- |
| self-dual `su(2)+` | `2(j=0) + 4(j=1/2) + 2(j=1)` | triplet `j=1` |
| anti-self-dual `su(2)-` | `2(j=0) + 4(j=1/2) + 2(j=1)` (parity image) | triplet `j=1` |
| diagonal / vector `su(2)` | `4(j=1/2) + 2(j=3/2)` | none (all 2-smooth) |

The multiplicity-3 (the odd object H1 found) is the `Lambda^2_+` triplet -- the unique odd-multiplicity route,
since the spinor channels are power-of-2 (M3 lemma) and the diagonal `su(2)` has no odd piece, and `su(3)`
cannot embed (`dim 8 > 6`).

## 3. The self-dual `su(2)+` route is even -- and *why* it is robustly even

Gauge the GU-native self-dual family `su(2)+` by a charge-`k` self-dual instanton on `X^4`, leaving `su(2)-`
flat. Two independent statements, and a third value-level check, all give even:

**(a) Per-irrep (Atiyah-Singer value).** The generation's `su(2)+` carrier is the integer-spin **adjoint**
(`T = 2`), index `4k` -- divisible by 4.

**(b) Over the full multiplicity bundle.** Summing the index over the whole 16-dim generation multiplicity
space (not just the triplet piece) gives, from the leg-3 decomposition `2(j=0)+4(j=1/2)+2(j=1)`:

```
ind = 2*(0) + 4*(k) + 2*(4k) = 12k     (self-dual su(2)+ gauged).
```

Even for every `k`. (The earlier "`8k`" attribution -- "`4k` triplet `x 2` `su(2)-` spectator" -- was loose
bookkeeping: the triplet already appears with multiplicity 2 under `su(2)+` alone, and the honest full-bundle
index is `12k`. Even-ness is unaffected; the factor attribution is corrected.)

**(c) Reality / Kramers parity -- the value-independent backbone (the robust reason).** The even-ness does not
actually depend on the value `4k` or on `k` being an integer. In 4 Euclidean dimensions `Spin(4) = SU(2)xSU(2)`
and each Weyl bundle `S_+` is quaternionic: an antilinear `j_S : S_+ -> S_+` with `j_S^2 = -1`, chirality
preserving. If the family rep `R` is **real** (`j_R^2 = +1`, the case for the adjoint/triplet), then
`J = j_S (x) j_R` obeys `J^2 = (-1)(+1) = -1`, commutes with `D` for any real connection, and preserves
chirality. Each kernel `ker D_+`, `ker D_-` is then quaternionic, hence of even complex dimension, so
`index = dim ker D_+ - dim ker D_- ` is **even -- for any metric, any connection, any charge, self-dual or
not**. This is the base-side analogue of the internal quaternionic no-go (C-07, `J_quat`, `J^2=-1` forces even
signatures) and the topological twin of T1a's kinematic cross-chirality Krein form.

This argument is *stronger* than the `4k` formula in one decisive way the bare formula misses: it closes the
**`SO(3)` fractional-instanton** escape. If the adjoint bundle is an `SO(3)` bundle that does not lift to
`SU(2)`, fractional `p_1` could naively evade the integer `4k`; but the Kramers argument needs only that the
adjoint is *real* and `S_+` is quaternionic, so the index stays even regardless of fractional charge.

**(d) Gravitational term.** The untwisted Dirac index is `Ahat[X] = -sign(X)/8`, and Rokhlin gives
`sign(X) ≡ 0 (mod 16)`, so `Ahat[X]` is even and `dim(R) * Ahat[X] = 3 * (even)` is even: the odd `dim(R)=3`
of the triplet **cannot** inject oddness through the gravitational channel. (Rokhlin is the clean compact-base
statement; on the non-compact `Y14`/APS setting the local-density version carries the same conclusion, and
argument (c) does not need Rokhlin at all.)

**Scoping note (the correction the adversaries forced).** Statement "even, never odd 3" is true and robust
**for the self-dual `su(2)+` adjoint route specifically**. It is NOT a property of GU-native base topology in
general, because the Kramers argument is confined to **real** reps. The pseudoreal `su(2)-` doublet
(`j_R^2 = -1`, so `J^2 = +1`, no Kramers constraint) escapes it -- and that is exactly the channel of section 4.

## 4. Does ANY GU-native base route force an odd 3? No -- but the honest reason is sharper than "even"

There is a second equally-native base route the original enumeration missed: the generation is also a
**doublet of the anti-self-dual `su(2)-`**. Gauge `su(2)-` by a charge-`k_-` anti-self-dual instanton, leaving
`su(2)+` flat.

- The pseudoreal `(2)_{su(2)-}` doublet has index `k_-` (`T = 1/2`).
- The native `su(2)+` triplet multiplicity 3 rides as a flat spectator.
- Restricted to the `(3,2)` generation piece: `net = 3 * k_-`, which is **odd** and equals exactly **3 at the
  minimal charge `k_- = 1`**.

So the claim "the only base route to 3 needs `k = 3` in the fundamental" is **refuted**: the cheapest base
route to exactly 3 is a *charge-1* anti-self-dual instanton, with the odd factor 3 supplied for free by the
GU-native `Lambda^2_+` triplet multiplicity. This is a *softer* import than `k=3`, and the paper should rebut
it directly rather than only rebutting `k=3`.

Two honest qualifiers keep the firewall standing, and they are what make this still **not** a GU-forced 3:

1. **It still imports a nonzero topological charge.** GU forces no instanton number. With `k_- = 0` the count
   is 0. Every metric `so(p,q)` connection -- including the natural self-dual one carrying the geometric "3"
   of `Lambda^2_+` -- gives generation index identically 0 (C-05/`step9`: all 91 `so(9,5)` generators plus the
   3 self-dual ones preserve the particle-hole symmetry `C = J_quat * G`, forcing a `±`-symmetric spectrum,
   `sig = 0`). The only families home GU's signature `p-q=4` points at is the metric-fiber base
   `GL(4,R)/O(3,1) ~ RP^3`, whose `H^2(RP^3;Z) = Z_2` is 2-torsion, hence 3-free. So the charge `k_- = 1` is
   external data, not GU-supplied.

2. **The clean odd 3 also requires a sub-sector truncation.** Computed honestly over the *full* 16-dim
   multiplicity bundle, gauging `su(2)-` gives `2(0) + 4(k_-) + 2(4k_-) = 12 k_-` -- **even**, identical in
   form to the self-dual case. The odd `3 = 3 k_-` appears only when one isolates the `(3,2)` generation
   sub-sector and discards the singlet/extra-doublet/triplet remainder of the multiplicity bundle. So the
   route reaches 3 via *(import `k_- = 1`)* **and** *(sub-sector truncation)*, not by a GU-internal datum.

**The full-bundle even-ness is uniform across all three native `su(2)` choices** (from the leg-3
decompositions, gauging any single family `su(2)` at charge `k`):

```
self-dual su(2)+   :  2(0) + 4(k)  + 2(4k)   = 12k
anti-self-dual su(2)-:  2(0) + 4(k)  + 2(4k)   = 12k
diagonal / vector  :  4(k)  + 2(10k)          = 24k
```

All even. The per-irrep `4k` (triplet) is one summand; the full multiplicity-space index is even regardless.

**Mod-2 / global-anomaly check.** The Witten `Z_2` mod-2 index is nontrivial only for **pseudoreal** reps
(the doublet), where it registers parity, and is identically 0 for the **adjoint**; in neither case does it
produce the integer 3 -- it only ever yields a parity. So no odd-from-adjoint and no "3" from a mod-2 effect.

**Conclusion of the route hunt.** No GU-native base route forces an odd 3. The self-dual/adjoint and the
full-bundle counts are even (robust by reality/Kramers + Rokhlin + value `4k`/`12k`). The odd `3` is reachable
only off the adjoint route, through the pseudoreal `su(2)-` doublet, and only with **(i)** an imported
instanton charge (cheapest `k_- = 1`) **and** **(ii)** truncation to the `(3,2)` generation sub-sector. Both
are imports. The firewall stands as "import a unit of (anti-self-dual) flux," not as "even-only" and not as
"needs `k=3`."

## 5. The multiplicity-vs-index resolution, stated as the crux

The integer 3 plays *two different roles* and is never both at once:

- When `su(2)+` is left **ungauged**, the 3 is the **dimension** of the flat triplet multiplicity space
  (`Lambda^2_+`) -- a representation dimension, a vectorlike `3 + 3bar`. This is H1's native object.
- Once `su(2)+` (or `su(2)-`) is **gauged** by a base instanton, that same 3 is no longer a flat dimension; it
  is folded into an **index** (`4k`/`12k`, even). The chiral count is then the index, not the dimension.

The original tension ("is the rank-3 object the count?") dissolves because *multiplicity* (a dimension) and
*net chiral count* (an index) are different invariants. The multiplicity-3 is GU-native; the chiral projection
turning vectorlike `3 + 3bar` into a net 3 is a separate datum (an index, or a ghost parity), and that datum
is even / absent on the GU-native side.

## 6. The Lorentzian-complexification tension (H2), resolved

In a Lorentzian `(3,1)` base, `*^2 = -1` on 2-forms, so `Lambda^2` does not split over `R`; over `C` it splits
into two **complex rank-3** conjugate pieces `Lambda^2_+ (+) Lambda^2_-`, the `sl(2,C)` self-dual / anti-self-
dual Weyl structure. The family group is `SL(2,C)`, not compact `SU(2)`. The tension: if this complex rank-3
is intrinsic to GU's *own* Lorentzian base, is the 3 then GU-forced, flipping the firewall?

The resolution separates the object from the count.

**At the object / multiplicity level: yes, and this strengthens H1.** The rank-3 self-dual Weyl bundle is
genuinely native to a Lorentzian 4-base; no import is needed for the *object* to exist. So H1's
multiplicity-3 is not a Euclidean artifact -- it is honest in GU's actual signature. Nguyen's
"rank-3-on-complexification" is real and native **as a structure**. This vindicates H1 at the multiplicity
level in Lorentzian signature, and removes the worry that the rank-3 had to be imported to even exist.

**At the count level: even-ness survives, for three reasons complexification does not touch.**

1. **Topology lives in the maximal compact.** `SL(2,C)` deformation-retracts onto `SU(2)`, so the instanton
   charge sits in `pi_3(SL(2,C)) = pi_3(SU(2)) = Z`: still an integer. The non-compact boosts are contractible
   and carry no topology. The complex-3 of `sl(2,C)` restricted to that `SU(2)` is the complexified real
   adjoint = spin-1, `T = 2`, index `4k`. Calling the group `SL(2,C)` instead of `SU(2)` changes nothing about
   the count.
2. **An index is intrinsically Euclidean/elliptic.** Atiyah-Singer requires an elliptic operator on a compact
   Riemannian manifold; the Lorentzian Dirac operator is hyperbolic and has no index theorem and no instanton
   number. Any well-defined net chiral count is computed after Wick rotation, where `sl(2,C) -> su(2)`,
   `k in Z`, and the Dynkin index is unchanged. Complexifying the *group* leaves the Dynkin index, the charge,
   and `2T(R)k` invariant; the adjoint of `sl(2,C)` is still 3-dimensional with `T = 2`. **Complexification
   cannot turn an even index odd.**
3. **Reality type is conserved.** Keeping the physical theory real forces `Lambda^2_+ (+) Lambda^2_- = 3 (+)
   3bar` (real rank 6); Wick rotation returns the real rank-3 adjoint, where the section-3 Kramers argument
   applies directly. Rokhlin is a property of the spin 4-base independent of the gauge bundle's reality and is
   unaffected.

**Where the genuine import actually lives (the honest Nguyen tie-in).** In Lorentzian signature `Lambda^2_+`
and `Lambda^2_-` are complex conjugates; keeping `Lambda^2_+` and discarding `Lambda^2_-` is a reality-breaking,
orientation-like `Z_2` choice -- precisely Nguyen's unannotated complexification step. So Nguyen's gap is
**confirmed and load-bearing**: there *is* an import, and it is exactly the reality-breaking needed to even
*define* a chiral split. But the import is **relocated and shrunk**: it is not the integer 3 and not "the
prime 3." The rank-3 object is native (H1, now in Lorentzian signature too). What is imported is the smaller
datum -- a `Z_2` chiral projection (which self-dual half) -- and that projection *by itself* still restricts to
the real adjoint of the compact form and yields an **even** count. To get an odd 3 one must *additionally*
import a nonzero topological charge (section 4). The mixed Euclidean construction (`su(2)+` and `su(2)-`
gauged independently) is available in exactly the same way, so complexification neither removes nor forces it.

So Nguyen's complexification reading is **necessary but insufficient for the count**: necessary, because
without the `Z_2` reality-breaking there is no chiral asymmetry to speak of; insufficient, because on its own
it produces an even count, not the observed odd 3. The complexification does **not** flip the firewall verdict
at the net-chirality level.

## 7. What the observed chiral 3 ultimately requires

Neither GU-native route forces an odd chiral 3:

- **Kinematics (T1a):** purely cross-chirality Krein form, every physical subspace 50/50, net chirality 0. No
  ghost parity chiralizes it without dynamics.
- **GU-native base index:** even on every native channel and over the full multiplicity bundle (`4k` per
  triplet; `12k`/`12k`/`24k` over the bundle for self-dual / anti-self-dual / diagonal). Robustly even by the
  real-rep quaternionic-Kramers argument (closing even the `SO(3)` fractional escape), corroborated by Rokhlin
  and by the explicit values. The only odd-capable channel is the pseudoreal `su(2)-` doublet, and it yields 3
  only with an imported charge `k_- = 1` plus a sub-sector truncation.
- **Families index over the GU metric fiber `RP^3`:** valued in 2-torsion `H^2(RP^3) = Z_2`; 3-free.

Therefore the observed chiral 3 requires exactly one of:

1. an **imported topological charge** -- cheapest a charge-1 anti-self-dual instanton in the `su(2)-` doublet
   channel (times the native multiplicity 3), or a charge-3 fundamental; in every case external data GU does
   not force; or
2. **GU's unbuilt ghost-parity dynamics** -- a ghost-parity-preserving source action (`[P_ghost, S] = 0`,
   Turok-Bateman type) that selects the physical positive-norm half of each hyperbolic (generation, mirror)
   pair. This is *not* an index and lies outside the parity argument; it is the one open route that could
   select an odd physical count from the hyperbolic pairs, and it is identical to GU's long-standing missing
   source action.

## 8. Verdict, and how it lands the paper's net-chirality story

**Multiplicity level (confirmed, strengthened).** GU natively contains a 3-shaped object: the canonically
unique `Lambda^2_+` / `su(2)+` adjoint triplet multiplicity, robustly 3 (H1, leg-3 closure, M3 lemma). The
Lorentzian `sl(2,C)` complexification makes this rank-3 object honestly native in GU's *actual* signature, so
the multiplicity-3 claim is not a Euclidean artifact. This part of the paper's corrected claim stands and is
reinforced.

**Net-chirality level (confirmed -- the paper's original instinct holds).** GU does **not** force 3 chiral
generations from internal data. Every base-topology route to a net count is even on the GU-native side, and the
only ways to an odd net 3 are (a) an imported topological charge (cheapest a charge-1 anti-self-dual instanton,
with a sub-sector truncation) or (b) GU's unbuilt ghost-parity dynamics -- both imports. So the count-3 is not
GU-internally forced, exactly the paper's original instinct, while the multiplicity-3 IS native.

**Net correction to the anchored reasoning.** The headline survives; three sub-claims were refuted and are
corrected: the generation is a `(3,2)` of `su(2)+ x su(2)-` (not "triplet, not doublet"); the cheapest odd-3
import is a charge-1 anti-self-dual instanton (not `k=3`); and even-ness is a property of the *real/adjoint*
channel and the full multiplicity bundle (robust by reality/Kramers, scoped away from the pseudoreal doublet),
not of GU-native base topology as an undifferentiated whole. The corrected firewall is sharper: not "even,
never odd," but "every odd route imports a nonzero topological charge (or unbuilt ghost-parity dynamics); GU
forces none."

This neither vindicates nor refutes GU. It places the boundary exactly: GU supplies the *shape and
multiplicity* of one generation and a native 3-shaped object; the *net chiral number three* is a separate
invariant (an index or a ghost parity) that GU does not internally fix.
