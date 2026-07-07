---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "RS-S1 (route S1, BUILD the relative twisted-RS index): the paper's Section-9 escape from Hom(Z/3,Z)=0 -- 'an integer count needs a RELATIVE / EQUIVARIANT / RANK invariant, = the twisted-RS index' -- is CONSTRUCTED as all three named types and each FAILS natively for a distinct, computed reason. HONEST OUTCOME: KILL of the native-construction branch. TYPE 1 (RELATIVE, ind_twisted - ind_untwisted): integer-by-construction YES and Hom-safe YES (an index difference, never a class-to-Z map), but ind_rel = 16 m^2 d' is divisible by 16 (2-PRIMARY, can never be an odd chiral 3), and for every natively selected twist m^2 == 1 (mod 3) so its mod-3 residue is the section degree d' ALONE -- a section-degree import (leg 5(ii)), or the base-signature import on K3 (sigma=-16 == 2 mod 3); never FORCED to the carrier's Z/3 by GU geometry, and the boundary<->bulk bridge (Bismut-Cheeger) is the gated unbuilt object. TYPE 2 (EQUIVARIANT, character-valued in the free Z-module R(G)): integer YES and Hom-safe YES (a Z/3 would come from an order-3 ACTION, the legitimate non-Hom route), but the only family group that acts on the coset is the torus U(1)+ (order-3 character sum_a zeta^a = 0 on C^3, = 1+zeta of norm 1 on C^2 -- a torus selects no Chern class); SU(2)+ DOES act on the carrier multiplicity space but its order-3 Lefschetz number on the leg-3 content 2(0)+4(1/2)+2(1) is 6 (EVEN, == 0 mod 3); a genuine Z/3-VALUED index needs a Z/3 deck group, and the native spine RP^3 = L(2;1) is deck Z/2 (reduced eta 2-adic, denominators powers of 2, 3-primary part 0) while L(3;1,1) (denominator 3) is an IMPORT where SM/16 boundary data still gives 0 by color triality (R2). TYPE 3 (RANK / multiplicity): integer 3 YES natively (measured: Casimir top 8.0 <=> j=1, dim 192 = 3*2*32) but it is a MULTIPLICITY with net chiral count tr(chi_t) = 0 (vectorlike) -- a representation dimension, not a chiral generation index; it IS the carrier's own multiplicity, not a mod-3 reduction of e_R. The three pinned constraints reinforce as independent walls: (1) Cartan=Krein=ghost-parity, {theta,chi}=0 forces the chiral index net-0 on the physical sector (achirality); (2) the tr(Q5 Phi^2) alignment residual is one SIGN bit, and the index sees m only through m^2, so the sign is mod-3-INVISIBLE; (3) every native base is 2-adic and every selected m^2 == 1 mod 3, CP^2's O(3) a certified double import. Every route is 2-primary, net-0, or a wrong-type (multiplicity) integer -- exactly the KILL condition. The only nonzero-mod-3 readings are imports (section degree d', base signature, cubic 3|m coupling, L(3) deck group) that ARE the paper's already-named gate, unchanged."
grade: "KILL (native-construction branch of the twisted-RS relative/equivariant/rank index), containing THEOREM-grade sub-results at their stated scopes: (i) TYPE 1 relative-index arithmetic exact-symbolic (ind_rel = 16 m^2 d', divisible by 16; mod-3 residue = section-degree d' for every selected m^2 == 1); (ii) TYPE 2 equivariant character values exact (U(1)+ order-3 character 0 / 1+zeta; SU(2)+ order-3 Lefschetz 6 on the leg-3 content) plus the APS/Donnelly lens reduced-eta reused from R2 (L(2;1) denominators [4] 3-free, L(3;1,1) denominators [3]); (iii) TYPE 3 rank measured on the carrier (multiplicity 3, net chiral tr(chi_t) = -6.7e-15); (iv) constraint (1) achirality Re tr(chi Pi_+) = -2.9e-15 from {theta,chi} = 0 machine-instantiated on the 192-dim triplet. Scope: kinematic / index-arithmetic, conditional on the h2-canon index formula and the VG-V5/V7 coset assignment; the actual twisted Dirac operator on X^4 needs the unbuilt section (enters only through d', which cannot repair 3 not-divides m or supply the carrier's Z/3). Anchors reproduced first: beta_S residual 0.0e+00 over all 91 generators; rank(Gamma) = 128, dim ker = 1664; triplet dim 192, su(2)+ Casimir top 8.0, Krein signature (+96, -96, 0); ghost parity P^2 = I, {P, chi} = 0. Target-import guard at maximum strictness: no element of {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} assumed, inserted, hardcoded, or divided by; every 3 carries printed provenance (multiplicity from Casimir + dim; U(1)+ 3 = count of distinct measured weights; m^2 == 1 arithmetic of measured charges; mod 3 = modulus of the divisibility question only; Dynkin /3 and Hirzebruch p1 = 3 sigma library math). Controls with power: random 192-subspace fails the vectorlike net-0 (tr chi = +0.12); order-2 SU(2)+ character differs from order-3; the section degree d' sweeps all of Z/3 (mod-3 value unforced). Single carrier signature (9,5). Not externally replicated or peer-reviewed."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-06/VG-V7-cp2-equivariant-payoff.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - explorations/big-swing-2026-07-07/A1-native-potential-alignment.md
  - tests/big-swing/R2_lens_dai_freed_eta.py
  - Lean/GUFormalization/K3IndexArithmetic.lean
scripts:
  - tests/big-swing/rs_s1_relative_index_construct.py
---

# RS-S1: build the relative twisted-Rarita-Schwinger index, and read whether it delivers a forced integer

**The swing (paper Section 9).** The frozen paper closes on one open bridge. A nonzero class in `Z/3`
is information *mod 3*, not the integer 3; and `Hom(Z/3, Z) = 0` forbids any homomorphism from the
absolute torsion class to a torsion-free integer count. So the paper concedes the count **cannot be**
the absolute torsion class, and states the only escape:

> An integer count, if one exists, ... can only arise from a **relative, equivariant, or rank**
> invariant -- integer-valued by construction yet geometry-dependent -- which is exactly what the
> unbuilt twisted Rarita-Schwinger index is. The conjecture is thus better stated as: does that
> relative index exist on GU's 14-manifold and reduce mod 3 to the located carrier?

Route S1 is the **build-it** attempt: construct each of the three named invariant types explicitly, on
GU-admissible bases, and read the decisive question. This is PROMOTE-or-KILL on that conjecture.

**Honest outcome in one line.** All three types are constructible and each is integer-by-construction
and `Hom(Z/3,Z)=0`-safe -- but each fails the decisive test natively, for a *distinct, computed*
reason: the **relative** index is 2-primary (divisible by 16, mod-3 residue is a section-degree
import), the **equivariant** index is net-0 (the only acting family group is a torus; its order-3
character is 0; a genuine `Z/3` needs an imported `L(3)` deck group), and the **rank** invariant is a
vectorlike multiplicity (integer 3, but net chiral count 0 -- a representation dimension, not a chiral
index). **KILL of the native-construction branch.**

All numbers below are printed by `tests/big-swing/rs_s1_relative_index_construct.py` (run from repo
root, exit 0). The carrier, the twisted-index arithmetic, the lens eta, and the achirality wall are
**reused**, not re-derived: this route assembles the paper's own machinery against the paper's own
proposed escape.

---

## 0. Anchors (reproduced first)

Verbatim Jordan-Wigner carrier of `ghost_parity_krein.py` / VG-V7:

| anchor | value | required |
|---|---|---|
| `beta_S` pseudo-anti-Hermiticity, max over all 91 `so(9,5)` generators | **0.0e+00** | ~0 |
| `rank(Gamma)` / `dim ker(Gamma)` | **128 / 1664** | 128 / 1664 |
| triplet dim / `su(2)+` Casimir top / Krein signature | **192 / 8.0 / (+96, -96, 0)** | as canon |
| ghost parity `P = sign(K_t)`: `\|\|P^2 - I\|\|`, `\|\|{P, chi}\|\|`, `tr chi_t` | **3.4e-14, 5.3e-14, -6.7e-15** | ~0 |

Shared substrate (h2-canon / VG-V7 §5, reproduced symbolically): the full 16-dim multiplicity bundle
`[2(j=0) + 4(j=1/2) + 2(j=1)]` twisted by `O(m)` over a spin 4-base, gravitational term included, has

```
ind_full = 12k + 8 m^2 d - 2 sigma  ;  X spin (d = 2d') => 16 m^2 d' + 12k - 2 sigma  (EVEN always)
MOD 3:   ind_full == m^2 d' + sigma  (mod 3)     [12 == 0, 16 == 1, -2 == 1]
```

Dynkin anchors `T(1/2) = 1/2`, `T(1) = 2`. The `/3` inside `T(j)` is library math anchored by
`T(1/2) = 1/2`, not the target 3.

---

## 1. TYPE 1 -- the RELATIVE index `ind(D_twisted) - ind(D_untwisted)`

**Construction.** Subtract the untwisted (`m = 0`) absolute index from the twisted one, so the common
gravitational and instanton absolute parts cancel and only the twist-channel zero-mode difference
survives:

```
ind_untwisted (m=0) = 12k - 2 sigma
ind_relative        = ind_twisted - ind_untwisted = 16 m^2 d'
```

- **Q1 integer-by-construction: YES.** A difference of two integer indices; a Z-linear form in
  `(m^2, d')`.
- **Q2 not `Hom(Z/3,Z)=0`: YES.** It never evaluates a torsion class into `Z`; it counts an honest
  zero-mode difference. This is the legitimate *relative* route the paper names.

**Why it fails the decisive test -- two independent reasons, both computed.**

1. **2-primary wall.** `ind_rel = 16 m^2 d'` is divisible by 16 for every `(m, d')`. A quantity
   divisible by 16 can **never be an odd chiral count**, so never the odd 3. The 2-primary meta-theorem
   of the paper reasserts on the relative invariant.
2. **The mod-3 residue is an import.** Every natively selected twist charge has `m^2 == 1 (mod 3)`
   (VG-V7: breaking line `O(-1)` `m=1`, quadratic `O(-2)` `m=2`, coset anticanonical `O(5)` `m=5`), so
   `ind_rel == d' (mod 3)`: the mod-3 residue is carried **entirely by the section degree `d'`**, which
   is the unbuilt-dynamics import (leg 5(ii)). As `d'` ranges over `Z` the residue sweeps `{0,1,2}`
   freely -- it is not pinned by GU geometry.

**On GU-admissible bases.** The located carrier `e_R = 1/12` sits on the `RP^3 = L(2;1)` metric-fiber
spine, in the `p_1/48` *framing* channel (homotopy-fixed), not in the closed-base `sigma`/twist channel
the relative index measures. On the control `K3` (`sigma = -16 == 2 mod 3`) a nonzero mod-3 residue does
exist -- but via the *base signature* `sigma`, an imported datum, and `chi(K3) = 24` is a forbidden
target and `K3` is not the GU-native spine. `CP^2` (`sigma = 1`, odd) is not spin and hosts no RS index.
The bridge that would relate the boundary-spine carrier to a bulk closed-base index -- Bismut-Cheeger
fibered-boundary -- is precisely the gated, unbuilt object.

**Verdict: 2-PRIMARY / IMPORT.** Integer yes, but even (`/16`), and its mod-3 content is a
section-degree or base-signature import; never a forced odd chiral 3 matching `e_R`.

---

## 2. TYPE 2 -- the EQUIVARIANT index (character-valued in `R(G)`)

**Construction.** An equivariant index lives in the representation ring `R(G)`, a **free Z-module**:
integer-by-construction on every weight, and torsion-free, so not `Hom(Z/3,Z)=0`. The legitimate way a
`Z/3` enters is by evaluating at a group element `g` of **order 3** (Atiyah-Segal / Atiyah-Bott
localization): the value lands in `Z[zeta_3]` and reduces mod `(1 - zeta_3)`. This is 3-torsion from a
`Z/3` **action**, never from the forbidden map. So the question is genuinely: is there a GU-native
order-3 action, and is its equivariant index nonzero mod 3?

**(a) The family group that acts on the coset is the torus `U(1)+`** (VG-V7 (a1): full `SU(2)+` cannot
act on the breaking coset in either signature). Exact weights `C^3 : a = (0,1,2)`, `C^2 : b = (0,1)`.
Character at the order-3 element `g` (`g^3 = 1`, `zeta = e^{2 pi i/3}`):

```
positive part  sum_a zeta^a = 0.000     (the regular-representation vanishing)
negative part  sum_b zeta^b = 1 + zeta,  |1 + zeta|^2 = 1   (algebraic integer of norm 1, NOT the integer 3)
```

A torus never selects a Chern class, and here its order-3 character is `0` (net) or a unit `1 + zeta` --
no nonzero integer-3 mod-3 class.

**(b) `SU(2)+` does act on the carrier's 16-dim multiplicity space** `[2(0) + 4(1/2) + 2(1)]`. Its
order-3 element (rotation by `2 pi/3`) has Lefschetz number

```
j=0: chi=+1 x2 = +2 ;  j=1/2: chi=+1 x4 = +4 ;  j=1: chi=0 x2 = 0  =>  total = 6  (EVEN, == 0 mod 3)
```

The native family action's order-3 index is 6 -- even, and `== 0 (mod 3)`. **Control:** the order-2
element (`pi`) gives a different character, so the order-3 mod-3 vanishing is a real measurement, not a
generic identity.

**(c) A genuine `Z/3`-valued index needs a `Z/3` deck group on the base.** Reusing the APS/Donnelly
reduced-eta `rho_a = xi_a - xi_0` on `L(p;1,1)` (from `R2_lens_dai_freed_eta.py`):

```
p = 2 (RP^3 = L(2;1), native spine): rho_a = [0, 1/4]   denominators [4]  -> POWERS OF 2, 3-FREE
p = 3 (L(3;1,1), IMPORT):            rho_a = [0, 1/3, 1/3] denominators [3] -> factor 3, a mod-3 phase lives
```

The native spine is deck `Z/2`: its reduced eta is 2-adic (denominators powers of 2, 3-primary part 0).
A `Z/3`-valued index requires the imported `L(3;1,1)` -- and even there, SM / `16` boundary data gives
mod-3 phase 0 by color triality (R2, canon: the mod-3 arena is empty).

**Verdict: NET-0 / IMPORT.** Integer yes, `Hom`-safe yes, but the only native action is a torus (order-3
character 0) or `SU(2)+` (order-3 Lefschetz 6, even); a nonzero `Z/3` needs an imported deck group.

---

## 3. TYPE 3 -- the RANK invariant (multiplicity of the native self-dual triplet)

**Construction.** A rank / multiplicity is a vector-space dimension: integer-by-construction, and not a
torsion class, so trivially `Hom`-safe. The native self-dual triplet has multiplicity **3** -- measured,
not inserted: `su(2)+` Casimir top eigenvalue `8.0 <=> j = 1`, and `dim 192 = 3 (spin-1) x 2 (su(2)-) x
32 (16 + 16bar)`.

**Why it fails.** It is a **multiplicity, not a net chiral count**. The net chiral index on the triplet
is `tr(chi_t) = -6.7e-15 = 0`: the sector is vectorlike, the rank-3 does not break the `(+96, -96)`
Krein balance. It is the carrier's *own* multiplicity, not a mod-3 reduction of `e_R`. This is exactly
the multiplicity-vs-index distinction of the paper's Section 3: a representation dimension and an
operator index are not one number computed two ways. **Control:** a random 192-subspace has
`tr(chi) = +0.12`, so the exact net-0 is measured structure, not generic.

**Verdict: WRONG-TYPE (net-0 chirally).** The one route that natively yields the integer 3 -- and it is
the vectorlike multiplicity, category-different from a chiral generation count.

---

## 4. The three pinned constraints as independent walls

1. **Cartan = Krein = ghost-parity `Z2` (VG-V2).** On the triplet `theta_t = P_ghost = sign(K_t)`, and
   `{theta, chi} = 0` (chirality-odd). The physical projector `Pi_+ = (I + theta)/2` gives
   `Re tr(chi Pi_+) = -2.9e-15 = 0`: **every chirality-graded index is net-0 on the physical sector**
   (the achirality theorem of BIG-SWING-CONFORMAL, instantiated here). This is an independent reason
   Types 1-2 give 0 -- not a separate assumption but the same Krein cross-chirality.
2. **`tr(Q5 Phi^2)` alignment (A1/A2/A4, 2026-07-07).** The residual is one **sign bit** on the twist
   charge `m`. The index depends on `m` only through `m^2`, so `sign(m)` is **mod-3-invisible**: `m` and
   `-m` give identical mod-3 residues. Resolving the alignment sign cannot flip any mod-3 verdict.
3. **Base 3-torsion (VG-V7).** Native spine `RP^3 = L(2;1)` deck `Z/2` (2-adic); `K3` `sigma = -16 == 0
   mod 16` (Rokhlin, 2-adic; `chi(K3) = 24` forbidden); `CP^2` `sigma = 1` odd (non-spin). Every
   natively selected twist has `m^2 == 1 (mod 3)`; the coset's own anticanonical is `O(5)` (3-free);
   `CP^2`'s `O(3)` is a certified **double** import (`3 | m` cubic-in-VEV coupling AND `3 | sigma` base
   topology).

---

## 5. Decisive readout

`e_R = 1/12` (order 12 in `Q/Z`); its 3-primary part is `4 e_R = 1/3` (order 3) -- the target `Z/3`
class.

| type | integer-by-construction | `Hom(Z/3,Z)=0`-safe | native mod-3 result | verdict |
|---|---|---|---|---|
| **RELATIVE** `16 m^2 d'` | yes (index diff) | yes | even (`/16`); residue `= d'` (section import) | 2-PRIMARY / IMPORT |
| **EQUIVARIANT** char in `R(G)` | yes (free Z-module) | yes | torus char 0; `SU(2)+` order-3 = 6 (even); `Z/3` needs `L(3)` | NET-0 / IMPORT |
| **RANK** multiplicity 3 | yes (dimension) | yes | net chiral `tr(chi) = 0` (vectorlike) | WRONG-TYPE |

**No constructible relative / equivariant / rank invariant on a GU-admissible base is both a genuine
chiral count and reduces mod 3 to the located carrier without an import.** Every route is 2-primary,
net-0, or a wrong-type (multiplicity) integer -- exactly the KILL condition. The paper's proposed
integer home for the count -- the twisted-RS index built as a relative / equivariant / rank invariant --
does not, on GU-native geometry, deliver a forced integer chiral 3. The only nonzero mod-3 readings
require an import (section degree `d'`, base signature `sigma`, a cubic `3 | m` coupling, or an `L(3)`
deck group) -- exactly the gate the paper already names in Section 8 (leg 5(ii), the unbuilt source
action) and R2 (the empty mod-3 arena). No new forced integer was found; the existing gate is unchanged.

**CONJECTURE SIGNAL: KILL (native-construction branch).**

---

## 6. Proposed Section-9 edit (PAUSES for the maintainer; the frozen paper is NOT edited)

Section 9 currently states the escape as an open possibility:

> an integer count ... can only arise from a relative, equivariant, or rank invariant ... which is
> exactly what the unbuilt twisted Rarita-Schwinger index is. ... does that relative index exist on
> GU's 14-manifold and reduce mod 3 to the located carrier?

RS-S1 proposes appending (subject to Joe's review, exploration-grade, internal tier):

> *A build-it attempt (RS-S1, 2026-07-07) constructs each of the three named invariant types explicitly.
> Each is integer-by-construction and `Hom(Z/3,Z)=0`-safe, and each fails the mod-3-match natively for a
> distinct computed reason: the relative index `ind_tw - ind_untw = 16 m^2 d'` is divisible by 16
> (2-primary, never an odd chiral 3) with mod-3 residue equal to the section-degree import `d'` for
> every selected `m` (`m^2 == 1 mod 3`); the equivariant index is net-0 (the only family group acting on
> the coset is the torus `U(1)+`, whose order-3 character is 0, and `SU(2)+`'s order-3 Lefschetz number
> on the multiplicity space is 6, even -- a `Z/3`-valued index needs an imported `L(3)` deck group, the
> native spine being `L(2;1) = Z/2`); and the rank invariant is the vectorlike native multiplicity 3
> (`tr chi = 0`), a representation dimension rather than a chiral index. The three named invariant homes
> for the count do not, on GU-native geometry, supply a forced integer that reduces mod 3 to `e_R`; the
> only nonzero-mod-3 readings are the already-named imports (section degree, base signature, cubic
> coupling, `L(3)` deck group). This strengthens the conjecture's standing as located-not-forced: the
> escape route from `Hom(Z/3,Z)=0` exists in principle but is empty on GU-native data.*

Grade of the proposed edit: **KILL of the native branch** -- a sharpening of "located, not forced," not
a change to the OPEN generation-count verdict, which is untouched. Any status flip pauses for Joe.

---

## 7. Honest gaps carried

1. **Kinematic / index-arithmetic scope.** The relative-index arithmetic is conditional on the h2-canon
   index formula and the VG-V5/V7 coset assignment; the actual twisted Dirac operator on `X^4` needs the
   unbuilt section. That section enters only through `d'`, and no `d'` can repair `3 not-divides m` or
   supply the carrier's `Z/3` -- but the section itself is not built here (as in the whole program).
2. **The import branch remains live, as the paper already says.** RS-S1 kills the *native/forced*
   construction, not the existence of *some* invariant with imports. An imported cubic `3 | m` coupling
   plus `sigma == 0 (mod 48)`, or an imported `L(3)` deck group, could carry a `Z/3` -- these are exactly
   the paper's Section 8 / R2 gates, unchanged. This is a KILL of the build-it branch, not a
   theory-independent impossibility over all conceivable backgrounds.
3. **Single carrier signature `(9,5)`** for the achirality and rank measurements; the twisted-index
   arithmetic is symbolic and signature-free.
4. **The equivariant `Z/3` route is treated at the character / lens-eta level**, reusing R2's L(3)
   analysis; a full `SU(2)+`-and-`so(10)`-equivariant K-theory index on the actual `Y14` was not built
   (it presupposes the same unbuilt section and the non-convex-fiber pushforward, gated in Section 8).
5. **Internal tier.** Computed, adversarially self-reviewed, reused-machinery; not externally replicated
   or peer-reviewed.
