---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "RS-S2, the NO-GO twin of the twisted-Rarita-Schwinger generation-count swing (run independently of S1). HONEST OUTCOME: the located-carrier bridge is REFUTED at native scope, and the refutation is sharper than 'the count is external' -- it is a 3-INERTNESS theorem. On the GU-forced (2-adic-spine) base, every relative/equivariant/rank invariant built from the Cl(9,5) RS-sector data is (Leg A) a SIGNED invariant that is identically 0 by the achirality wall {K,chi}=0 (net index, relative index, net chiral rank; machine-checked with a K-commuting control giving net=+96), or (Leg B) the UNSIGNED twisted index whose mod-3 class ind == m^2 d' + sigma is CARRIER-3-INERT: every natively selected twist m (breaking line O(-1), quadratic O(-2), coset anticanonical O(5)) has m^2 == 1 (mod 3), so the located carrier's own twist contributes the TRIVIAL residue and the mod-3 value is carried entirely by the section degree d' (unbuilt dynamics) and base signature sigma (external), both DISJOINT from the RP^3 carrier; section-independent 3-divisibility <=> 3|m AND 3|sigma (a DOUBLE import; Rokhlin: sigma==0 mod 48), or (Leg C) a rank invariant whose only factor of 3 is the homotopy-FIXED multiplicity dim(Lambda^2_+)=3, with Hom(Z/3,Z)=0 blocking the class<->count identification. The category error is confirmed for sector-interior data. conjecture_signal = KILL of the located-carrier bridge; the surviving escape (the double external import 3|m cubic coupling + 3|sigma spacetime) is external-only, outside 'constructible from RS-sector data on a GU-forced base', and does NOT pass through the located carrier e_R=1/12."
grade: "exploration / component legs THEOREM at their stated scopes. Leg A: THEOREM (finite-dimensional; Theorem 2 of the paper re-instantiated as dim pi_+(P) - dim pi_-(P) = 0 for the reference physical subspace and 4 random K-isometric images, residual K-isometry 3.4e-11, all nets exactly 0; K-commuting control net=96 discriminates). Leg B: THEOREM (symbolic, exact sympy): 12k / 24k even-index formulas reproduced, ind_full = 12k + 16 m^2 d' - 2 sigma even for all inputs, ind == m^2 d' + sigma (mod 3) verified over 200 random integer inputs, 3-divisibility-for-all-sections <=> 3|m swept over m in 0..8, every selected m has m^2==1 mod 3, discriminating control m=3 (unselected core anticanonical) has m^2==0; base 2-adicity charge-q eta 2-primary swept q in [-4..5]. Leg C: THEOREM (arithmetic): Hom(Z/3,Z)=0 enumerated, sector ranks factored (only 192=2^6*3 carries a 3, the fixed multiplicity), net chiral rank 0 with unbalanced-grading control net=8, equivariant leaf reduces to Leg B (torus selects no Chern class, 35 realizable weight tuples). ROUTE VERDICT: KILL of the native/carrier-controlled 3-transfer; the double-external-import escape survives and is named, outside scope, disjoint from the carrier. Target-import guard at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, hardcoded as an answer, or divided by; every printed 3 carries provenance (modulus of the divisibility question; measured multiplicity dim Lambda^2_+=3; unselected core anticanonical m=3 as a control). Anchors reproduced first (rank Gamma=128, ker=1664, triplet (+96,-96,0), {K,chi}=0). All counts stated as 'mechanism/base M forces c', never 'GU forces c'. Internal tier: not independently replicated or peer-reviewed; run independently of the S1 promote twin, no coordination."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-06/VG-V7-cp2-equivariant-payoff.md
  - explorations/big-swing-2026-07-06/VG-V2-fourth-seat-gauge-sector.md
  - explorations/big-swing-2026-07-06/BIG-SWING-CONFORMAL-CLASS-BLOCKED.md
  - tests/generation-sector/ghost_parity_krein.py
scripts:
  - tests/big-swing/rs_s2_relative_index_nogo.py
---

# RS-S2: the no-go twin -- is the twisted-RS generation count provably not-forceable from sector data?

**The swing.** The frozen paper's Section 9 states the only open bridge: the generation count cannot BE
the absolute torsion class (`Hom(Z/3, Z) = 0` kills that); it can only arise from a **relative,
equivariant, or rank** invariant -- integer-by-construction, geometry-dependent -- which is exactly the
unbuilt twisted Rarita-Schwinger index. The PROMOTE-OR-KILL conjecture: does that relative index exist
on GU geometry and reduce mod 3 to the located carrier (the `RP^3`-spine framing `e_R = 1/12`, a genuine
order-3 class)?

**Route S2 attempts the negative.** Prove: *no relative / equivariant / rank invariant constructible
from the `Cl(p,q)` RS-sector data reduces mod 3 to a nonzero, carrier-controlled class on a GU-forced
base* -- i.e. the category error is confirmed and the result is "located, provably-not-forceable from
sector-interior data." (Run independently of the S1 promote twin; no coordination.)

**Honest outcome: KILL of the located-carrier bridge, sharper than "the count is external."** The
refutation is not merely that an internal invariant fails to be nonzero mod 3 -- it is that the located
carrier is **3-INERT**: its own twist contributes the trivial residue `m^2 == 1 (mod 3)` to every
twisted index, so the carrier can never be the object the mod-3 class tracks. The one surviving route to
a nonzero mod-3 class is a **double external import** (`3 | m` via a non-native cubic-in-VEV coupling AND
`3 | sigma` via an imported spacetime of signature divisible by 3), which is outside "constructible from
RS-sector data on a GU-forced base" and, crucially, **does not pass through the located carrier**.

All numbers below are printed by `tests/big-swing/rs_s2_relative_index_nogo.py` (run from repo root,
exit 0).

---

## 0. Anchors (reproduced first, on the verified carrier)

Verbatim Jordan-Wigner recipe of `ghost_parity_krein.py` / VG-V2 (timelike `{4..8}`, so `(9,5)`):

| anchor | value | required |
|---|---|---|
| `beta_S` pseudo-anti-Hermiticity, max over all 91 `so(9,5)` generators | `0.0e+00` | ~0 |
| `rank(Gamma)` / `dim ker(Gamma)` | **128 / 1664** | 128 / 1664 |
| triplet dim / `su(2)+` Casimir top | **192 / 8.0** | 192 / top |
| triplet Krein signature | **(+96, -96, 0)** | (+96, -96, 0) |
| `{K, chi}` on the triplet (K purely cross-chirality) | **5.2e-14** | 0 |
| `tr(chi)` on the triplet (net chiral index) | **-6.7e-15** | 0 |

---

## 1. Leg A -- the achirality wall fences every SIGNED invariant to 0 (constraint 1)

Constraint (1) of the week (VG-V2): the Krein form `K` **is** the Cartan involution on the module, and
on the triplet it equals the ghost parity `P_ghost = sign(K_t)`. It is purely cross-chirality:
`{K, chi} = 0` (measured `5.2e-14`). This is the hypothesis of the achirality theorem
(`BIG-SWING-CONFORMAL-CLASS-BLOCKED`): `{K, chi} = 0 => Re tr(chi Pi_+) = 0`, and of the paper's
Theorem 2 (index conservation).

**The extension performed here.** The signed invariant classes are all read off the same structure. A
*physical subspace* `P` (maximal `K`-positive, dim 96) is, by Theorem 2's own proof, the graph of an
isomorphism `W_+ -> W_-`, so it projects isomorphically onto **both** chirality eigenspaces:

- **(i) net chiral index of `P`:** `dim pi_+(P) - dim pi_-(P) = 96 - 96 = 0` (computed by SVD-rank of
  the chirality-projected orthonormal basis).
- **(iii) K-isometric images:** 4 random `K`-isometries `U = exp(t * K S)`, `S` anti-Hermitian (so `U`
  is a genuine `K`-isometry, residual `||U^dag K U - K|| = 3.4e-11`), each map `P` to a physical
  subspace with `(dim pi_+, dim pi_-) = (96, 96)`, net `= 0`.
- **(ii) relative index:** `ind(O_1) - ind(O_0) = 0 - 0 = 0` for any two admissible operators.

**Control (discriminating).** A `K`-**commuting** grading `chi' = sign(K)` makes `W'_+` `K`-definite, so
the `K`-positive physical subspace lies wholly in `W'_+`: net' `= 96 - 0 = 96 != 0`. The cross-chirality
hypothesis `{K, chi} = 0` is load-bearing; the net-0 is not a tautology.

**Leg A verdict.** Every signed invariant (net chiral index, relative index, net chiral rank) built from
an admissible (`K`-self-adjoint, cross-chirality-graded) operator is **identically 0**, hence `== 0
(mod 3)`. The whole signed family is fenced. THEOREM (finite-dimensional).

---

## 2. Leg B -- the UNSIGNED twisted index is CARRIER-3-INERT (constraint 3)

The one invariant that *can* be nonzero is the Atiyah-Singer twisted RS index. Reproduced exactly
(sympy), from the `h2` canon `12k` even-index formula plus the `CP^2` twist `O(m)` and the
gravitational term:

```
self-dual / anti-self-dual su(2)+ bundle:  2(0) + 4k + 2(4k)  = 12k    (EVEN)
diagonal / vector bundle:                  4k   + 2(10k)      = 24k    (EVEN)
full twisted index:  ind_full = 12k + 8 m^2 d - 2 sigma
X spin => d = 2d'  =>  ind_full = 12k + 16 m^2 d' - 2 sigma           (EVEN for all inputs)
MOD 3:   ind_full == m^2 d' + sigma   (mod 3)     [12 == 0, 16 == 1, -2 == 1]
```

(The mod-3 reduction is verified as `ind_full - (m^2 d' + sigma) == 0 (mod 3)` over 200 random integer
inputs; the 2-adic wall as every coefficient of `ind_full(spin)` even.)

**The 3-inertness theorem.** Section-independent 3-divisibility (`3 | ind_full` for all `d'`, `k`) holds
**iff `3 | m` AND `3 | sigma`** (`m^2 d' == 0` for all `d'` iff `m^2 == 0 (mod 3)` iff `3 | m`; then the
constant term forces `sigma == 0 (mod 3)`). Now insert the twist the located carrier actually couples
through -- the natively **selected** homogeneous line bundles of VG-V7's stabilizer-character arithmetic:

| natively selected twist | `m` | `m^2 (mod 3)` |
|---|---|---|
| breaking line `O(-1)` | 1 | **1** |
| quadratic condensate `O(-2)` | 2 | **1** |
| coset `D` own anticanonical `O(5)` | 5 | **1** |

Every selected `m` has `m^2 == 1 (mod 3)`. **The located carrier's own twist contributes the trivial
residue.** Hence `ind_full == d' + sigma (mod 3)`: the mod-3 value is carried **entirely** by the
section degree `d'` (an unbuilt-dynamics import) and the base signature `sigma` (an external import),
both **disjoint from the `RP^3` carrier**.

**Controls (discriminating, not blind).**
- The **unselected** core anticanonical `O(3)` has `m^2 = 9 == 0 (mod 3)` -- which *would* change the
  residue (to `ind == sigma`). The arithmetic sees the twist; it is not blind. (Provenance of the `3`:
  the exact stabilizer weight ratio `-6/-2` of the compact-core `CP^2` anticanonical, VG-V7 a3 -- **not**
  the breaking-direction rep, **not** the coset's own anticanonical, which is `O(5)`, 3-free.)
- Even at that unselected `m = 3`, `ind == sigma (mod 3)`: `3 | ind` **still** needs the second import
  `3 | sigma`. The escape is a **double** import, never one leg alone.

**Base 2-adicity.** The GU-forced metric-fiber spine `RP^3 = L(2;1)` has `H^2(RP^3; Z) = Z/2` (2-torsion,
3-free, standard topology); the charge-`q` reduced Dirac `eta = (2q^2 - 4q + 1)/8` is 2-primary
(denominator a power of two) for every integer `q` (swept `q in [-4..5]`). GU-forced base data carries
no 3-torsion; `3 | sigma` is an imported spacetime datum, not a spine datum, and in any case is a
**different** manifold's invariant from the carrier's `RP^3`.

**Leg B verdict.** The located carrier `e_R = 1/12` is provably **3-INERT** (`m^2 == 1 (mod 3)` for every
natively selected twist). The twisted index's mod-3 class is import-carried and disjoint from the
carrier. THEOREM (symbolic, exact).

---

## 3. Leg C -- `Hom(Z/3, Z) = 0` made rigorous; the invariant taxonomy exhausted

**(c1)** Every homomorphism `phi: Z/3 -> Z` is zero: `0 = phi(0) = phi(1+1+1) = 3 phi(1) => phi(1) = 0`
(enumerated over `phi(1) in [-5..5]`). The **absolute** torsion class yields no integer -- the paper's
Section-9 category error, machine-explicit. Any integer count must be relative, equivariant, or rank.

**(c2) The taxonomy is exhausted, and every leaf is 2-primary / net-0 / import-carried:**

- **RELATIVE** -> Leg A (difference of net-0 indices `= 0`) or Leg B (twist arithmetic).
- **EQUIVARIANT** -> `U(1)+` localization: `O(m) = taut^(-m) (x) chi_c` carries an equivariant structure
  for **every** `m` (fixed-point weights `-m a_i + c` well-defined; 35 realizable weight tuples over a
  small `(m,c)` grid) -- a torus selects no Chern class (VG-V7 a2). The equivariant index's **integer**
  values (at the identity) reduce to the ordinary twisted index = Leg B; its non-integer **character**
  values are not counts (the `Hom` guard). No new mod-3 route.
- **RANK** -> the sector's ranks factor as `128 = 2^7`, `1664 = 2^7 . 13`, `640 = 2^7 . 5`,
  `832 = 2^6 . 13`, `192 = 2^6 . 3`. The **only** factor of 3 is in the triplet dimension `192`, and that
  3 is the **homotopy-fixed multiplicity** `dim(Lambda^2_+) = 3` -- identical for a one-generation or a
  five-generation universe (located, not forcing). The **net** chiral rank is `96 - 96 = 0` (Leg A).
  Control: an unbalanced `Z2` grading (`rank_+ = 100`) gives net `= 2(100) - 192 = 8 != 0` -- the net-0
  is the measured cross-chirality balance, not automatic. And `Hom(Z/3, Z) = 0` blocks the
  class<->count identification for the absolute rank regardless.

**Leg C verdict.** The taxonomy has no un-visited leaf. Every relative/equivariant/rank invariant on
sector data is net-0, carrier-3-inert, or an unforced import. THEOREM (arithmetic).

---

## 4. The theorem, stated exactly, with its scope and escape hatch

> **RS-S2 no-go (native scope).** Let `I` be any relative, equivariant, or rank invariant constructed
> from the `Cl(9,5)` gamma-traceless RS-sector data (the `j=1` triplet with its cross-chirality Krein
> form `K`, the family `su(2)+` action, the twisted-index data with a **natively selected** homogeneous
> twist `O(m)`), evaluated on the GU-forced base (the 2-adic metric-fiber spine `RP^3`). Then the mod-3
> reduction of `I` is **not** a nonzero, carrier-controlled class: either `I = 0` identically (every
> signed invariant, by the achirality wall `{K, chi} = 0`), or `I mod 3` is carried entirely by external
> imports `(d', sigma)` disjoint from the located carrier (every unsigned twisted index, because every
> selected `m` has `m^2 == 1 (mod 3)`), or `I` is an absolute rank whose only factor of 3 is the
> homotopy-fixed multiplicity `dim(Lambda^2_+) = 3`, which `Hom(Z/3, Z) = 0` forbids from being a count.

**Invariant classes covered:** signed indices and relative indices of admissible (`K`-self-adjoint,
cross-chirality-graded) operators; ordinary and equivariant twisted RS indices with a natively selected
homogeneous twist; absolute and net rank invariants of the sector's isotypic decomposition.

**Where the escape hatch is (named exactly).** A nonzero mod-3 class survives *only* through a **double
external import**: `3 | m` (a non-native **cubic-in-VEV** coupling, `3 | r`, that no measured object
supplies) **AND** `3 | sigma` (an imported spacetime of signature divisible by 3; with Rokhlin,
`sigma == 0 mod 48`). Both legs are outside "constructible from RS-sector data on a GU-forced base," and
neither passes through the located carrier `e_R = 1/12` -- the `3 | m` leg is a dynamical coupling degree
and the `3 | sigma` leg is a *different manifold's* signature. This is exactly the paper's pre-existing
"external by structure" route, now **sharpened**: not only is the count external, the located order-3
carrier is provably 3-inert, so even the external route cannot be routed *through* the carrier.

---

## 5. Verdict, kill-condition mapping, and standing

| leg | result | grade |
|---|---|---|
| A -- achirality wall on signed invariants | net index / relative index / net rank all `= 0`; K-commuting control net `= 96` | THEOREM (finite-dim) |
| B -- twisted-index mod-3 arithmetic | `ind == m^2 d' + sigma (mod 3)`; every selected `m` has `m^2 == 1`; carrier 3-INERT; base 2-adic | THEOREM (symbolic) |
| C -- `Hom(Z/3,Z)=0` + taxonomy | absolute class gives no integer; rank leaf's only 3 is fixed `dim Lambda^2_+`; net rank 0 | THEOREM (arithmetic) |
| **route** | **the located-carrier -> integer-3 bridge is refuted at native scope; the carrier is 3-inert** | **KILL (native-transfer branch)** |

**Against the standing conjecture (paper Section 9).** "Does the relative index reduce mod 3 to the
located carrier?" -- the answer is **no**: the carrier contributes `m^2 == 1 (mod 3)`, the trivial
residue, to every RS-sector invariant. The mod-3 class it would have to control is instead controlled by
disjoint external imports. The conjecture, as it names the located carrier, is dead.

**Consistency with canon.** Nothing here moves the `12k` / `24k` arithmetic, the `(+96, -96, 0)` anchors,
the consistency-not-chirality pattern, or the VG-V7 selection table; Leg A re-instantiates the paper's
Theorem 2 as a dimension count, Leg B re-uses the VG-V7 index arithmetic, Leg C re-uses the VG-V7
localization and the paper's `Hom(Z/3,Z)=0`. The S2 contribution is the **3-inertness reading**: the
carrier's twist is the trivial mod-3 residue, so "located, not forced" hardens to "located, and provably
not forceable through the located object."

**conjecture_signal = KILL** of the located-carrier bridge. The surviving escape (double external
import) is real, named, external-only, and disjoint from the carrier -- it does not rescue the conjecture.

---

## 6. Honest gaps carried

1. **Native scope.** The 3-inertness is proven for the **natively selected** twists (breaking line,
   quadratic condensate, coset anticanonical `O(5)`). A dynamical Yukawa could couple through any `O(m)`;
   that is exactly the priced import branch (`3 | m` cubic coupling), not a gap in the enumeration logic.
2. **Leg B is arithmetic, not the built operator.** The honest twisted Dirac operator on `X^4` still
   needs the unbuilt section (the source action). Leg B settles the mod-3 *arithmetic* for every `m`;
   Leg A settles the signed *kinematics* on the carrier. The value on the true `Y14` bundle remains the
   paper's one open residual -- unchanged, and unchanged in verdict.
3. **`sigma` is spacetime, not spine.** The `3 | sigma` escape imports a four-manifold of signature
   divisible by 3; it is not GU-forced and is a *different* manifold from the carrier's `RP^3`. Whether
   the physical base has `3 | sigma` is a genuine external open question -- but it does not connect to
   `e_R = 1/12`.
4. **Single carrier signature `(9,5)`** for Leg A (as in VG-V1/V7); `(7,7) = M(128, R)` is unprobed here.
5. **Internal tier.** Computed, adversarially self-reviewed within the same process; not independently
   replicated or peer-reviewed. Run independently of the S1 promote twin, no coordination.

## 7. Governance

Exploration-grade; **no canon promotion, and no edit to the frozen paper.** A promote/kill outcome is a
**PROPOSAL** for the paper's Section 9 that pauses for the maintainer: the proposed sharpening is that
the located order-3 carrier is **3-inert** in every RS-sector relative/equivariant/rank invariant
(`m^2 == 1 (mod 3)` for every natively selected twist), so the `order-3-class -> integer-3` bridge is
refuted at native scope and the only surviving route is a double external import disjoint from the
carrier. The generation-count verdict is unchanged: **OPEN** (external by structure; now with the carrier
bridge specifically closed). Any verdict/status flip pauses for Joe.

---

## 2026-07-09 honesty-alignment note (SG3)

The BIG-SWING-RS-INDEX synthesizer (2026-07-07) already downgraded this route from "all three legs
THEOREM / universal no-go" to **PARTIAL**: the decisive Leg-B mod-3 sweep is circular (the swept
difference `ind_full - (m^2 d' + sigma) = 15 m^2 d' + 12k - 3 sigma` has every coefficient divisible
by 3, so "200 random inputs pass" verifies `0 == 0`), and the twisted-index formula was asserted, not
derived. The sequential-goals SG3 certificate
(`tests/big-swing/sg3_s2_mod3_tautology_audit.py`, doc
`explorations/sequential-goals-2026-07-09/SG3-s2-mod3-tautology-audit.md`) discharges the constructive
horn of the synthesizer's next-step #3: it exhibits the tautology symbolically, **derives**
`ind == m^2 d' + sigma (mod 3)` coefficient-by-coefficient, and replaces the circular sweep with an
exact-polynomial mutant-discriminating test.

**Read the "component legs THEOREM" language in this doc's frontmatter and body as native-scope**, per
the claim-status-consistency rule: what is established is "the located-carrier bridge is not established
and is arithmetically implausible via native data," NOT a universal no-go over all
relative/equivariant/rank invariants. The underlying content (the mod-3 reduction, carrier 3-inertness,
the double-import structure) survives and is now derived. No scientific verdict changes: the
generation-count verdict stays OPEN (located, not forced).
