---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "Big swing VG-V7 (T2' payoff: equivariant m-selection + twisted-index arithmetic): V5's open invoice 5(i)/(iii) is PAID and the answer is NEGATIVE. The family SU(2)+ cannot act on the breaking coset at all (Euclidean base kills the coset -- trace-reversed (9,1), p odd; Lorentzian base kills the equivariance -- no compatible J commutes with the SO(3) image, exact isotypic obstruction), so equivariance selects nothing; the structure that DOES select is the coset's own homogeneity, and it selects AGAINST the payoff: the breaking line transforms in the tautological O(-1), |m| = 1 (quadratic coupling 2, degree-r coupling r), the coset D's own anticanonical is O(5) -- 3-FREE -- and the celebrated 3h class is only the anticanonical of the compact core CP^2, which nothing measured selects. Twisted-index arithmetic (exact): ind_full == m^2 d' + sigma (mod 3); section-independent 3-divisibility <=> 3|m AND 3|sigma (<=> sigma == 0 mod 48 with Rokhlin); every natively selected m has m^2 == 1 (mod 3), so the coset contributes NOTHING mod 3 beyond the free imports (d', sigma). C-07 confrontation: the twist direction is J_quat-ODD on the 192-dim triplet ({M,J} = 0 at 1.5e-13, ||[M,J]|| = 2||M||) -- the Kramers hypothesis fails exactly as V5 predicted, but the even/vectorlike CONCLUSION re-arises by a different quaternionic mechanism (+-weight pairing + Kramers-even zero slice): slices 64/64/64, Krein (32,32) each, tr P = tr chi = 0 on every slice. HONEST OUTCOME: KILL for the NATIVE transfer of the coset 3 into the generation index; the O(3) coupling is certified an IMPORT (a double one: 3|m coupling AND 3|sigma base topology)."
grade: "exploration / component legs THEOREM at their stated scopes ((a1) exact isotypic obstruction + exact (1,1) Gram + scan floors with passing controls; (a2) exact adapted J_ad in Q(sqrt(3)) with exact zero-matrix identities and exact integer weights; (a3) exact stabilizer-character and localization arithmetic with (2,1)/(4,2)/CP^1/CP^3 controls; (b) exact sympy index arithmetic; (c) machine-checked on the 192-dim triplet with exact quaternionic structure C bar(C) = -I at 0.0e+00 and random controls). ROUTE VERDICT: KILL of the native/equivariant 3-transfer branch of T2' -- kinematic scope, conditional on V5 premises alpha (J-canonicity, refuted separately by V3's commutant scan) and beta (condensate valued in the line space); the import branch (an unforced O(3) = cubic-in-VEV coupling PLUS sigma == 0 mod 48) remains live as an explicit double invoice, and leg V5-5(ii) (an actual section; unbuilt dynamics) can only supply d', never 3|m. Target-import guard at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, or divided by; every printed 3 carries printed provenance; anchors reproduced first; all counts stated as 'mechanism M forces c'."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V5-breaking-coset-topology.md
  - explorations/big-swing-2026-07-06/VG-V1-condensate-ghost-parity-scan.md
  - explorations/big-swing-2026-07-06/VG-V3-j-commutant-conformal-native.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - canon/h2-base-index-chirality.md
  - canon/ghost-parity-krein-synthesis.md
scripts:
  - tests/big-swing/vg_v7_cp2_equivariant_payoff.py
---

# VG-V7: the T2' payoff computation — does the coset's 3 reach the generation index?

**The leg.** VG-V5 left the breaking-coset route CONSISTENT_UNCOMPUTED with a precise invoice
(V5 §5): (i) equivariant m-selection — which homogeneous line bundle O(m) does the breaking
direction transform in? m = ±3 would make the 3-divisibility canonical, any other m makes it an
import; (ii) an actual section f (unbuilt dynamics); (iii) the C-07 twisted check. The verifiers
enlarged the invoice: the payoff needs **3 | m AND 3 | sigma**. This route pays items (i) and
(iii) and does the full divisibility arithmetic for (ii)'s remaining free parameter.

**Honest outcome in one line:** the invoice is paid and the answer is negative — the m-selection,
now actually performed, returns |m| = 1 (the tautological line), not 3; the coset's own
anticanonical is O(5), not O(3); and the mod-3 arithmetic then makes the coset's contribution to
the generation count exactly zero beyond the already-free imports.

All numbers below are printed by `tests/big-swing/vg_v7_cp2_equivariant_payoff.py`
(run from repo root, exit 0).

---

## 0. Anchors (reproduced first)

Carrier (verbatim recipe of `ghost_parity_krein.py` / VG-V2): `beta_S` pseudo-anti-Hermiticity
residual **0.0e+00** over all 91 generators; rank(Gamma) = **128**, dim ker = **1664**; triplet
sector dim **192**, su(2)+ Casimir top **8.0**, Krein signature **(+96, −96, 0)**; ghost parity
P = sign(K_t) with ‖P²−I‖ = 3.4e−14, ‖{P, chi}‖ = 5.3e−14.

Fiber chain (V5/V3): Frobenius **(7,3)** → trace-reversed **(6,4)** → compatible J → Hermitian
**(3,2)** (residual 6.0e−16). Euclidean control: (10,0) → **(9,1)**.

## 1. (a1) The equivariance dichotomy — the family SU(2)+ never acts on the coset

**Euclidean horn — the family acts, the coset is absent.** On a Euclidean base su(2)+ is an
honest real symmetry of the fiber: Sym²(R⁴) decomposes under it as **3 triplets + 1 singlet**
(measured Casimir: eigenvalue 8.0 × 9, 0.0 × 1 — H1's native multiplicity-3 echo, used in no
downstream formula). But the Euclidean trace-reversed fiber form is **(9,1)**: p odd, no
compatible complex structure exists (V3 Section-A theorem), and the scan control confirms it
(floor 4.000 over 10 starts). **D does not exist over a Euclidean base.**

**Lorentzian horn — the coset exists, the family does not act on it.** Hodge-* on
Lambda²(R^{1,3}) squares to **−I** (measured; Euclidean control +I), so su(2)+ acts on the real
10-dim fiber only through its **SO(3) rotation image**. Under SO(3), V10 = **1+1+3+5** (measured
Casimir multiplicities 0×2, 2×3, 6×5); the commutant has dim **6**; and the obstruction is exact:

- every commutant element restricted to the 3-dim and 5-dim isotypics is a **real scalar**
  (max ‖X|_iso − cI‖ = 3.5e−16 over the whole commutant), and a scalar c with c² = −1 does not
  exist over R — so **no compatible J commutes with the SO(3) image** (multiplicity-one,
  real-type, odd-dimensional isotypics: a two-line theorem, machine-instantiated);
- independently, the 2-dim trivial isotypic {h_tt, spatial trace} has **exact** G-Gram
  [[1/2, 3/2], [3/2, −3/2]], det = −3 < 0: signature **(1,1)** — both odd, no J there either;
- optimizer scan over the commutant: floor **28.34** over 25 starts (exact lower bound 8 = 3+5,
  the measured odd isotypic dims); CONTROL: the same scan over the commutant of the Cartan L3
  alone reaches **3.5e−20** — the wall is the full SO(3), not the machinery.

**Dichotomy verdict: the SU(2)+-equivariant coset does not exist in either signature.** Euclidean
kills the coset; Lorentzian kills the equivariance. Full-family equivariance cannot select m
because it cannot be formulated. "Which orbits of CP² are SU(2)+-invariant" — none: SU(2)+ has no
holomorphic action on any CP²_J; it moves J itself. (This is V3's step-4 EMPTY, sharpened from
"no GU-native J" to "no family-equivariant complex coset at all".)

## 2. (a2) The maximal acting family subgroup U(1)+ and its exact weights — THEOREM

The Cartan U(1)+ ⊂ SO(3) does act: an adapted compatible **J_ad is constructed exactly** (sympy,
entries in Q(√3)) — rotation pairs on the exact zero-weight block (positive pair G-norm 1/2,
negative pair −6, all cross-pairings exactly 0) plus J = rho(L3)/w on the weight planes. The
three defining identities are **exact zero matrices**: J_ad² = −I, J_adᵀ G J_ad = G,
[J_ad, rho(L3)] = 0. Hermitian signature **(3,2)** (residual 6.1e−16): the adapted coset is the
same C^(3,2).

Exact U(1)+ weights (integers, from rho(L3) = w·J_ad on each plane):

```
positive part C^3:  a = (0, 1, 2)      negative part C^2:  b = (0, 1)
```

(signs are per-plane J-orientation choices; magnitudes canonical). **No weight is 3**; the 3
appears only as the COUNT of distinct positive weights = the number of isolated U(1)+ fixed
points on the core CP² = chi (V5's measured 3, reproduced as a fixed-point count).

Exact localization cross-check (fixed-point fiber weights, fit w_i = −m·a_i + c):

| bundle | fixed-point weights | fitted m |
|---|---|---|
| tautological O(−1) | (0, 1, 2) | **−1** |
| det T(core CP²) — anticanonical | (3, 0, −3) | **3** |
| det T(D) — anticanonical | (4, −1, −6) | **5** |

**U(1)+-equivariance forces no m**: every O(m) = taut^(−m) ⊗ chi_c carries an equivariant
structure (the weights −m·a_i + c are well-defined for every m, c). A torus never selects a Chern
class. Whatever selects must be the homogeneous structure — next section.

## 3. (a3) The m-selection itself: stabilizer-character arithmetic — THEOREM, and it selects against the payoff

D = SU(3,2)/S(U(1) × U(2,2)) (V5's measured assignment; su(3,2) basis dim **24 measured**).
The stabilizer h of the positive line Ce₁ is block-diagonal automatically (isometries preserving
a non-null line preserve its orthocomplement): dim h = **16**, dim [h,h] = **15**, so the
character lattice is **Z**, generated on the central Y = i·diag(4,−1,−1,−1,−1) (in h at 0.0e+00,
central at 0.0e+00, outside [h,h] at relative residual 1.00). Exact weight arithmetic
(O(m) fiber weight = −w_L·m; tautological O(−1) ↔ +w_L):

| object | weight data | homogeneous bundle |
|---|---|---|
| the breaking line itself (V5 premise beta) | line weight +4 | **O(−1), \|m\| = 1** |
| quadratic condensate v⊙v ∈ Sym²(line) | +8 | O(−2), \|m\| = 2 |
| degree-r monomial in the VEV | +4r | O(−r), \|m\| = r |
| anticanonical of the coset D (det T_D) | −20 = −4·**5** | **O(5)** |
| anticanonical of the compact core CP² | −6 = −2·**3** | **O(3)** |

Controls (same arithmetic, different measured input): C^(2,1) → ambient O(3) / core O(2);
C^(4,2) → ambient O(6) / core O(4). The machinery outputs p and p+q — the 3 is the measured
Hermitian p of V5's chain, the 5 is p+q; neither is inserted.

Three sharp consequences, each a correction of emphasis to how the V5 payoff was imagined:

1. **The mechanism "stabilizer character of the breaking direction" FORCES |m| = 1** (2 for a
   quadratic coupling, r for degree r). 3 | m fails for every natively selected coupling; only a
   **cubic-in-the-VEV** coupling (3 | r) would see the factor, and no native object supplies one.
2. **The coset's own anticanonical is O(5), which is 3-FREE.** The celebrated c₁ = 3h of V5 is
   the anticanonical of the **compact core CP²** (the maximal-compact orbit SU(3)/S(U(1)×U(2))),
   NOT of the homogeneous vacuum manifold D. The two differ by the normal bundle O(1)⊕O(1)
   (5 = 3 + 2, exact). So even "couple through the coset's canonical geometry" gives m = 5,
   m² ≡ 1 (mod 3).
3. **V5's flagged possibility "the condensate couples through O(3) = K^(−1)" is now certified an
   import**: O(3) is a compact-core datum that nothing measured selects — not the rep the
   breaking direction transforms in, not the coset's own canonical class, not an equivariance
   requirement (there is no equivariance).

**(a4) Carrier-side honesty.** V5 §5(i)'s literal form ("decompose the 1792-dim carrier under the
stabilizer") has no native home: the carrier's internal block is **(5,5)** (measured from eta_V),
not (6,4); any so(6,4) sub-block must borrow ≥ 1 of the 4 base directions (only 5 internal
spacelike exist), and a borrowed-index block fails to commute with the family su(2)+
(‖[σ₂₃, σ₃₉]‖ = 5.657). **The carrier cannot natively host both the (6,4) fiber chain and a
commuting family action** — a new sharp adverse datum; the fiber-level computation above is the
invoice's honest home.

## 4. (b) The twisted-index arithmetic — THEOREM (symbolic, exact)

Dynkin anchors reproduced (T(1/2) = 1/2, T(1) = 2). The twist enters only through rk·c₁(L)²/2
(cross term ch₁(V)·c₁(L) vanishes for every traceless su(2) channel — verifier finding,
reproduced symbolically). Full 16-dim multiplicity bundle [leg-3 content 2(0) + 4(k) + 2(4k)]:

```
ind_full = 12k + 8 m² d − 2σ ;   X spin ⇒ d = 2d' ⇒ ind_full = 12k + 16 m² d' − 2σ   (EVEN, always)
MOD 3:   ind_full ≡ m² d' + σ   (mod 3)        [12 ≡ 0, 16 ≡ 1, −2 ≡ 1]
```

**Exact divisibility condition:** 3 | ind_full for all sections (all d') and all k **iff
3 | m AND 3 | σ**. With Rokhlin (16 | σ on spin X): iff 3 | m and **σ ≡ 0 (mod 48)**. The
verifiers' enlarged invoice is now an exact arithmetic statement. Residue table (d' symbolic):

```
m≡0:  σ≡0: 0 | σ≡1: 1 | σ≡2: 2          — the (0,0) cell is the ONLY d'-independent zero
m≡1:  σ≡0: d' | σ≡1: d'+1 | σ≡2: d'+2
m≡2:  σ≡0: d' | σ≡1: d'+1 | σ≡2: d'+2
```

**Inserting the measured m's from (a):** m ∈ {±1 (breaking line), ±2 (quadratic), 5 (D's own
anticanonical)} all have **m² ≡ 1 (mod 3)**, so ind_full ≡ d' + σ (mod 3): the coset contributes
NOTHING mod 3 beyond the free imports (d', σ). Even the unselected core-anticanonical m = 3
leaves ind ≡ σ: the 3 | σ base-topology import remains on top. A residue-tuned import
(d' ≡ −σ mod 3) is possible for 3∤m but is a section-degree import, exactly like k in 12k.
The (3,2) sub-sector 3(k₋ + m²d) trap is flagged as in V5 (native multiplicity riding along, not
a coset-born 3).

## 5. (c) The C-07 confrontation on the 192-dim triplet — THEOREM (carrier scope)

Exact quaternionic structure by the C-07 regression rule: C = product of exactly the generators
with bar(e_a) = −e_a — the index set **measured** from this rep's reality signs
({1,3,4,6,8,9,11,13}, 8 generators, even; the C-07 script's {1,3,5,7,10,12} belongs to a
different rep convention). C is unitary at 0.0e+00, **C·bar(C) = −I at 0.0e+00** (J² = −1,
quaternionic, p − q = 4 mod 8), and e_a C = C·bar(e_a) at 0.0e+00 for all 14 generators.
The triplet is J-invariant (1.0e−13) and quaternionic (U_t·bar(U_t) = −I at 5.2e−14); a random
192-dim subspace FAILS the same check at 12.5 — the structure is not automatic.

The invoiced finite proxy: the su(2)+ weight operator composed with the scale/coset direction.
The scale direction degenerates to the identity on the triplet (‖etaV⊗1|_W − I‖ = 3.7e−14 — the
V1 adverse datum reproduced), so the composed core is M = i·J⁺₃|_W (Hermitian 8.2e−14,
K-self-adjoint 1.5e−13):

| operator | ‖[·, J]‖ | ‖{·, J}‖ | reading |
|---|---|---|---|
| NATIVE core A = J⁺₃\|_W (real) | 8.5e−14 | 45.25 | J-COMMUTES: C-07/Kramers hypothesis holds → even count |
| TWISTED core M = iA (∘ scale) | 45.25 = **2.000·‖M‖** | 1.5e−13 | J-ANTICOMMUTES: **the twist breaks J-commutation maximally** |
| random K-self-adjoint (control) | 1.42 | 1.41 | mixed parity, and ‖[·,P]‖ = 1.41 — the clean structure is measured, not generic |

So the answer to the C-07 fork question is: **the twist breaks J-commutation** — the twisted
generation operator is NOT GU-native in the C-07 sense, and the Kramers evenness argument does
not apply to it, exactly the escape-of-hypothesis V5 §6.3 predicted. But the confrontation cuts
both ways, and the machine shows the **conclusion re-arises by a different quaternionic
mechanism**: J-oddness maps the weight slice E_w isometrically onto E_{−w} (residual 2.6e−14) and
leaves E_0 J-invariant and quaternionic (U₀·bar(U₀) = −I at 2.2e−14 ⇒ dim E₀ even by Kramers).
Measured slice structure:

```
E_(−2): dim 64, Krein (+32, −32), tr P = 1e−14, tr chi = −3e−15
E_( 0): dim 64, Krein (+32, −32), tr P = 1e−14, tr chi = −2e−15     net signed count = 0
E_(+2): dim 64, Krein (+32, −32), tr P = 9e−15, tr chi = −6e−15
```

Every slice is **vectorlike**; the twisted core is ghost-parity even and chi-commuting
([M,P] = 1.5e−13, [M,chi] = 1.5e−13), hence mirror-blind by V1's intertwiner lemma. The twist
direction supplies **no kinematic asymmetry seed**. (Scope honesty: this is the kinematic proxy
spectrum on the carrier; the actual twisted Dirac index on X⁴ still needs the unbuilt section —
but its 3-divisibility was already settled negative in §4 for every selected m.)

## 6. Verdict, kill-condition mapping, and standing

| leg | result | grade |
|---|---|---|
| (a1) SU(2)+ equivariance on the coset | nonexistent in both signatures (Euclidean: no coset; Lorentzian: exact isotypic obstruction, scan floor 28.3 with passing controls) | THEOREM |
| (a2) maximal acting subgroup U(1)+ | exact J_ad (identities = exact zero matrices); weights (0,1,2)/(0,1); 3 fixed points = chi; forces no m | THEOREM |
| (a3) the m-selection | breaking line → O(−1), \|m\| = 1 (quadratic 2, degree-r r); K_D^(−1) = O(5); O(3) = core anticanonical only, unselected; controls pass | THEOREM |
| (b) twisted index | ind ≡ m²d′ + σ (mod 3); payoff ⟺ 3\|m ∧ σ ≡ 0 (48); every selected m has m² ≡ 1 | THEOREM (symbolic) |
| (c) C-07 twisted check | twist is J-odd (hypothesis escape confirmed); conclusion re-arises: all slices vectorlike, zero slice Kramers-even | THEOREM (carrier scope) |
| **route** | **the coset 3 does NOT reach the generation index natively** | **KILL (native-transfer branch)** |

**Against the standing conditions:**

- **V5's KC-2 clause "the integer never arrives":** now closed on the native side — through the
  equivariant/homogeneous channel the integer provably does not arrive. The coset's 3-divisible
  class exists (V5, unchanged) but is not the class the breaking direction couples through, and
  the class it does couple through (O(∓1)) is 3-inert in the index.
- **V5's KC-3 certification test:** performed; the stamp is **"import"**, not "canonical". The
  import is double: an unforced cubic-in-VEV / O(3) coupling AND σ ≡ 0 (mod 48) base topology.
- **Consistency with canon:** nothing here moves the 12k arithmetic, the (+96,−96,0) anchors, or
  the consistency-not-chirality pattern; (c) actually extends the pattern — even the channel that
  escapes the C-07 hypothesis is spectrally vectorlike on the carrier.

**What this buys the federation:** T2's payoff branch is now typed like T3's (V1): the native
machinery is self-consistent and self-blocking. The breaking coset supplies a 3-divisible class
the way the Krein module supplies mirror-splitting directions — present in the ambient geometry,
never in the GU-native coupling. Any future claim that "GU's breaking gives 3 generations via
the CP² twist" must now name its two imports explicitly: who orders the O(3) coupling, and who
orders σ ≡ 0 (mod 48).

## 7. Honest gaps carried

1. **Conditional scope:** everything is conditional on V5's premises alpha (a compatible J is
   canonically present — separately refuted at the fiber level by V3's commutant scan, which
   makes THIS route's negative even stronger: the J needed to even define D is itself unforced)
   and beta ("positive lines" as the vacuum manifold — a modeling choice, flagged in V5).
2. **Leg V5-5(ii) is still unbuilt** (an actual section f and its degree d): but it enters the
   arithmetic only through d′, and no value of d′ can repair 3∤m. The kill is of the native
   3-transfer, not of the (always-available) double-import route.
3. **"Natively selected couplings" = the enumerated list** (the line, its monomial powers, the
   two anticanonicals): a dynamical Yukawa structure could in principle couple through any O(m) —
   that is exactly the import branch, priced above, not a gap in the enumeration logic.
4. **The (c) leg is a kinematic proxy** (the weight operator on the carrier, scale direction
   degenerate): the honest twisted Dirac operator on X⁴ does not exist without a section. The
   proxy answers the C-07 fork question (J-commutation broken) and the asymmetry-seed question
   (none), not the index-value question — which (b) answers arithmetically.
5. **Sign conventions:** the U(1)+ weight signs are J-orientation choices (magnitudes canonical);
   m enters the index only as m².
6. **Single carrier signature (9,5)** for the (c) leg, as in V1.
