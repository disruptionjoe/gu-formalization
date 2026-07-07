---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "FB-F1 (BUILD the twisted operator on the framed-bordism carrier -- the constructive object RS-S4 left UNBUILT). HONEST OUTCOME: KILL of the constructive route on the located carrier, and a CONFIRMED category error one level up from Hom(Z/3,Z)=0. On the GU-forced RP^3 = L(2;1) spine with the self-dual Lambda^2_+ tangential framing (e_R = 1/12, the order-3 class in the Z/3 summand of pi_3^s = Z/24 = Z/8 (+) Z/3, CRT-derived from denom(B_2/4)=24), we BUILD the twisted Dirac reduced eta (APS/Donnelly spectral sum) and enumerate EVERY GU-admissible twist: the flat deck-group Z/2 lines (chars a in {0,1}), the flat family SU(2)+ bundles (Hom(Z/2,SU(2)) = {hol +I, hol -I}), the self-dual Lambda^2_+ adjoint (Ad of each holonomy), and the bulk section degrees d'. MEASURED RESULT: every twist eta_E is 2-ADIC (v_3(den)=0, because pi_1(L(2;1))=Z/2 is coprime to 3; L(2;1) built eta = (-1/8,+1/8), sum 0), so the twisted APS eta-index I(E) = bulk(0) - (e_R + eta_E) has 3-adic valuation FIXED at v_3 = -1 for EVERY twist -- it is NEVER an integer -- and its Z/3 (3-primary Q/Z) component is FROZEN at the nonzero fraction 2/3, identical across all six twists: the Z/2 deck acts ONLY on the 2-primary sector and cannot manufacture, cancel, or integerize the Z/3 content of e_R. The self-dual Lambda^2_+ adjoint is in fact 3-inert twice over: Ad(-I)=I (central), so even the nontrivial family holonomy gives the trivial adjoint bundle 3*[char 0], eta = 0. Integerness and Z/3-content are MUTUALLY EXCLUSIVE on this carrier (the trivial-framing control gives integer 0 with zero Z/3 content; the 1/12 and 1/24 framings give fractional with nonzero Z/3 content). DISCRIMINATING CONTROL: the SAME machinery on L(3;1) (deck Z/3, NOT GU-forced -- RS-S1: the native spine is L(2;1) not L(3;1)) DOES integerize a 3-adic framing with Z/3 content (built rho_a = (0,1/3,1/3), 3-adic; a rank-2 flat Z/3 twist gives eta=2/3, framing 1/3 + 2/3 = 1 in Z) -- so the mechanism EXISTS, on the wrong carrier; the obstruction is precisely the deck-group order 2 of the GU-forced spine. SCRAMBLED-TWIST CONTROL: 2000 random 2-adic twist etas, zero integerize -1/12; isolating the 3-primary sector on framing f=1/3, no 2-adic twist integerizes but a (deck-unavailable) 3-adic twist does -- pinning 3-adicity as the load-bearing block. The bulk integer index (closed AS index 12k + 16 m^2 d' - 2 sigma) is integer-BY-CONSTRUCTION but 3-INERT: every selected twist has m^2 == 1 (mod 3), so its Z/3 content is external (d', sigma), disjoint from e_R (RS-S2 reproduced). conjecture_signal = KILL of the constructive route on the located carrier: e_R = 1/12 is provably WITHOUT an integer-index preimage constructible from any GU-admissible twist on the GU-forced L(2;1) carrier. Conjecture D, as it NAMES the located carrier, is refuted by construction. The only surviving escape is the RS-S2 double external import (3|m cubic coupling + 3|sigma spacetime), which is off-carrier and does not route through e_R, so it does not rescue conjecture D as stated."
grade: "CONSISTENT_UNCOMPUTED promoted to KILL (of the constructive-on-carrier branch); component results THEOREM at their stated scopes. THEOREM (F1 p-adic): for every flat twist E on L(2;1) (deck Z/2), eta_E is 2-adic (MEASURED: all rho_a denominators powers of 2; built via the APS/Donnelly spectral sum validated by sum_a xi_a = 0 against the S^3 cover), so v_3(I(E)) = min(v_3(1/12), v_3(eta_E)) = -1 always => never integer; Z/3 component frozen at 2/3 across all six enumerated twists. DISCRIMINATING CONTROL is a genuine measurement (L(3;1), deck Z/3, integerizes; 3-adic eta present, v_3=-2). FROM-MEMORY flags: the Kirby-Melvin p_1=4 framing normalization for e_R (mitigated by the agreeing independent Adams class-2/24 route, both = 1/12); the L(p;1) reduced-eta Donnelly/APS closed form (standard, reproduced and internally validated by sum_a xi_a = 0); eta(S^6)=0 / A-hat[S^6]=0 transparency inherited from RS-S4 (structural: no degree-6 Pontryagin number). Anchors reproduced first on the verified Cl(9,5) carrier: rank(Gamma)=128, dim ker=1664, triplet Krein (+96,-96,0), 12k index; pi_3^s=Z/24 CRT split DERIVED from denom(B_2/4)=24 (factor 24=8*3, gcd=1), not asserted. TARGET-IMPORT GUARD at maximum strictness: {3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4, ind_H=8} never assumed, inserted, hardcoded as an answer, or divided by; every 3 MEASURED with printed provenance (24=8*3 a CRT fact about the Bernoulli denominator; e_R=1/12 measured two ways; the Z/3 component 1/3 computed via partial-fraction/CRT decomposition of e_R mod Z). e-INVARIANT / Hom(Z/3,Z)=0 discipline held throughout: e_R is Q/Z-valued, never identified with an integer; the only integer exhibited (the closed AS index) is proven 3-inert. Every count stated 'mechanism/carrier M forces c'. Internal tier: computed + self-adversarial (three discriminating controls), not independently replicated or peer-reviewed; run as the constructive twin of the RS-S4 GATED thread."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-07/RS-S4-base-forcing-bismut-cheeger.md
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
scripts:
  - tests/big-swing/fb_f1_twisted_operator_build.py
---

# FB-F1: build the twisted operator on the framed-bordism carrier

**The swing.** The frozen `located-not-forced` paper (Section 9 / conjecture D) leaves one open bridge:

> `order-3-class -> integer-3`.

The order-3 class is the framed-bordism Adams `e`-invariant `e_R = 1/12`, carried by the self-dual
`Lambda^2_+` tangential framing on the GU-forced `RP^3 = L(2;1)` spine of the metric fiber, living in the
`Z/3` summand of `pi_3^s = Z/24 = Z/8 (+) Z/3`. `RS-S4` computed the **untwisted** transparent-fiber APS
index `= -1/12` (fractional) and stopped **GATED** because the **twisted** operator -- the object that could
supply a nonzero, geometry-dependent bulk and integerize the boundary defect -- was never built.

**Route F1 builds it.** On `L(2;1)` with the self-dual framing, we build the twisted Dirac reduced `eta`
(the APS/Donnelly spectral sum, reused from `R2_lens_dai_freed_eta.py`) and enumerate **every**
GU-admissible twist, asking the decisive question: **does any GU-admissible twist promote the fractional
`-1/12` to an INTEGER with nonzero `Z/3` content?**

**Honest outcome: KILL of the constructive route on the located carrier, and a confirmed category error
one level up from `Hom(Z/3, Z) = 0`.**

All numbers below are printed by `tests/big-swing/fb_f1_twisted_operator_build.py` (run from repo root,
exit 0). Anchors reproduced first on the verified `Cl(9,5) = M(64,H)` carrier: `rank(Gamma) = 128`,
`dim ker(Gamma) = 1664`, triplet Krein `(+96, -96, 0)`, the `h2` canon full-bundle index
`2(0) + 4(k) + 2(4k) = 12k`. The two-arena split is **derived, not asserted**: `|Im J_3| = denom(B_2/4) =
denom(1/24) = 24`, factored `24 = 8 * 3` with `gcd(8, 3) = 1`, so by CRT `pi_3^s = Z/24 = Z/8 (+) Z/3`;
the located class `2` in `Z/24` maps to `(2 mod 8, 2 mod 3) = (2, 2)`, `Z/3` image `2 != 0` (genuine `Z/3`
content). This `24` is a homotopy-group order (Bernoulli denominator), kept **provenance-distinct** from
`chi(K3) = 24`.

---

## 1. The built operator: `L(2;1)` twisted Dirac eta is 2-adic; `L(3;1)` is 3-adic

The twisted Dirac operator on `L(p;1)`, coupled to a flat character `a`, has reduced `eta` given by the
APS/Donnelly spectral closed form (the `Z_p`-projected `S^3` Dirac spectrum),

```
xi_a = (1/p) sum_{j=1..p-1}  zeta^{a j} / (2i sin(pi j / p))^2,   zeta = e^{2 pi i / p},
```

real and rational, internally validated by `sum_a xi_a = 0` (the `p`-fold cover `S^3` has `eta = 0`). The
measured values:

| carrier | deck group | built `xi_a` | 3-adic reading |
| --- | --- | --- | --- |
| `L(2;1)` = `RP^3` (**GU-forced spine**) | `Z/2` | `(-1/8, +1/8)` | every denominator a power of 2: **2-adic** (`v_3(den) = 0`) |
| `L(3;1)` (**control, unforced**) | `Z/3` | `(-2/9, +1/9, +1/9)` | denominator `9 = 3^2` present: **3-adic** (`v_3 = -2`) |

The deck-group order **fixes the arithmetic**: `Z/2` deck `=>` 2-adic `eta`; `Z/3` deck `=>` 3-adic `eta`.
This is the whole story in one line, and it is measured, not recalled.

---

## 2. Every GU-admissible twist on the forced `L(2;1)` carrier

Flat bundles on `L(2;1)` are representations of `pi_1 = Z/2`; the twisted `eta` of
`E = (+)_a mult_a [char a]` is `eta_E = sum_a mult_a rho_a`, with `rho_a = xi_a - xi_0` the pure-gauge
Dai-Freed invariant (`rho_0 = 0`, `rho_1 = 1/4`). The twisted APS eta-index with the transparent bulk
(`A-hat[S^6] = 0`, inherited from RS-S4) is `I(E) = bulk(0) - (e_R + eta_E) = -(1/12 + eta_E)`.

The enumeration is exhaustive because `Z/2` has exactly two characters, and the only order-`<= 2` elements
of `SU(2)` are `+-I` (both central), so `Hom(Z/2, SU(2)) = {hol +I, hol -I}`:

| twist | decomposition | `eta_E` | `I(E)` | `v_3(I)` | integer? | `Z/3` comp |
| --- | --- | --- | --- | --- | --- | --- |
| trivial flat line `[char 0]` | `[0]` | `0` | `-1/12` | `-1` | no | `2/3` |
| nontrivial flat `Z/2` line `[char 1]` (deck sign) | `[1]` | `1/4` | `-1/3` | `-1` | no | `2/3` |
| flat `SU(2)+` family, `hol = +I` | `2[0]` | `0` | `-1/12` | `-1` | no | `2/3` |
| flat `SU(2)+` family, `hol = -I` (central) | `2[1]` | `1/2` | `-7/12` | `-1` | no | `2/3` |
| self-dual `Lambda^2_+` adjoint, `hol = +I` | `3[0]` | `0` | `-1/12` | `-1` | no | `2/3` |
| self-dual `Lambda^2_+` adjoint, `hol = -I` (`Ad(-I) = I`) | `3[0]` | `0` | `-1/12` | `-1` | no | `2/3` |

**Two measured facts carry the KILL:**

1. **`v_3(I(E)) = -1` for every twist.** Every `eta_E` is 2-adic (built from `rho_a` on the `Z/2` deck,
   `v_3(eta_E) >= 0`), so `v_3(I(E)) = min(v_3(1/12), v_3(eta_E)) = -1`. The `3` in `1/12` **survives every
   twist**. No twist gives an integer.

2. **The `Z/3` component is frozen at `2/3`.** Across all six twists the 3-primary component of `I(E)` in
   `Q/Z` (computed by partial-fraction/CRT decomposition) is identically `2/3` -- nonzero and fractional.
   The `Z/2` deck twists act **only on the 2-primary sector**; they cannot touch, cancel, or integerize the
   `Z/3` content of `e_R`.

The self-dual `Lambda^2_+` adjoint -- the twist the located carrier actually couples through -- is **3-inert
twice over**: because `Ad(-I) = I` (`-I` is central), *even the nontrivial family holonomy* yields the
**trivial** adjoint bundle `3[char 0]`, `eta = 0`. The carrier's own twist is the trivial residue.

**The bulk section degrees `d'`** feed the **closed** AS index `ind_full = 12k + 16 m^2 d' - 2 sigma`, an
integer **by construction** -- but it is 3-INERT: `ind_full == m^2 d' + sigma (mod 3)`, and every natively
selected twist (`m in {1, 2, 5}`: breaking line `O(-1)`, quadratic `O(-2)`, coset anticanonical `O(5)`) has
`m^2 == 1 (mod 3)`, so the integer's `Z/3` content is carried by `d'` (unbuilt) and `sigma` (external),
**disjoint from `e_R`** (RS-S2, reproduced). Integer-ness and `e_R`'s `Z/3` content live in structurally
disjoint places.

---

## 3. Controls (the KILL is a measurement, not a tautology)

**Control 1 -- discriminating (the mechanism exists, on the wrong carrier).** On `L(3;1)` (deck `Z/3`, which
GU does **not** force -- RS-S1 fixes the native spine as `L(2;1)`), the identical machinery gives built
`rho_a = (0, 1/3, 1/3)` (3-adic). A rank-2 flat `Z/3` twist gives `eta_E = 2/3`, and a 3-adic framing
`f = 1/3` (nonzero `Z/3` content) integerizes: `I = -(1/3 + 2/3) = -1 in Z`. So the `Z/3` integer preimage
**is reachable** -- but only on `L(3;1)`. The obstruction on `L(2;1)` is precisely the **deck-group order 2**,
not a failure of the construction.

**Control 2 -- scrambled twist.** 2000 random 2-adic "twist" `eta`s: **zero** integerize `-1/12`. Isolating
the 3-primary sector on framing `f = 1/3`, no 2-adic twist integerizes but a (deck-unavailable) 3-adic twist
does -- pinning **3-adicity** as the load-bearing block, and the `Z/2` deck supplies **only** 2-adic twists.

**Control 3 -- alternate framing.** The `3` lives in the framing's denominator, not tunable by twists:
`p_1 = 2` (`e_R = 1/24`) and `p_1 = 4` (`e_R = 1/12`) both stay fractional with nonzero `Z/3` content; only
the **trivial** framing (`e_R = 0`, no `Z/3` content) is an integer (`0`). Integer-ness and `Z/3` content are
**mutually exclusive** on this carrier: you get an integer exactly when there is no `Z/3` content to carry.

---

## 4. The theorem, and the confirmed category error

> **F1 no-go (constructive, on the GU-forced carrier).** Let `E` be any flat twist on `L(2;1)` (deck group
> `Z/2`): a deck-group line, a flat `SU(2)+` family bundle, or the self-dual `Lambda^2_+` adjoint. Its
> twisted Dirac reduced `eta` `eta_E` is 2-adic (`v_3(eta_E) >= 0`, measured; because `pi_1 = Z/2` is coprime
> to 3). Hence the twisted APS eta-index `I(E) = bulk(0) - (e_R + eta_E)` has `v_3(I(E)) = -1` -- it is never
> an integer -- and its `Z/3` component is frozen at the nonzero fraction `2/3` in `Q/Z` for every `E`.

**The category error, confirmed and sharpened.** `e_R = 1/12` is `Q/Z`-valued; its `Z/3` content (`= 1/3`) is
genuine mod-3 **information**. No operator **built** on the GU-forced `L(2;1)` carrier converts it to an
integer, because the carrier's deck symmetry has order 2, **coprime to 3**. This is one level up from
`Hom(Z/3, Z) = 0`: it is not merely that the absolute torsion class admits no class-to-integer map -- it is
that the constructive object the conjecture invokes (a twisted-RS index on the located carrier) provably
**cannot** manufacture the `Z/3` integer, for a structural reason (deck-group order). The only integer index
that exists on the carrier (the closed AS index) is 3-inert. So the answer to the swing's decisive question
is the second horn: **`e_R = 1/12` is provably without an integer-index preimage** constructible on the
GU-forced carrier.

---

## 5. Verdict and conjecture signal

**`conjecture_signal = KILL`** of the constructive route on the located carrier.

The framed-bordism carrier `e_R = 1/12` on the GU-forced `L(2;1)` spine has **no integer-index preimage
constructible from any GU-admissible twist** on that carrier. Every enumerated twist stays fractional
(`v_3 = -1`) with the `Z/3` component frozen at `2/3`; the `Z/2` deck group is coprime to 3 and cannot
manufacture the `Z/3`. Conjecture D, **as it names the located carrier**, is refuted by construction.

This converts the RS-S4 **GATED** verdict to **KILL** on the branch RS-S4 explicitly left open: RS-S4 could
not rule out that *some* built twisted-RS index might integerize `e_R`; F1 builds the operator with every
GU-admissible twist and shows none can, with a structural (p-adic / deck-order) reason and a discriminating
`L(3;1)` control proving the machinery is not blind.

**Surviving escape (named, off-carrier).** The only route to a nonzero mod-3 integer is the RS-S2 **double
external import** (`3 | m` via a non-native cubic-in-VEV coupling **and** `3 | sigma` via an imported
spacetime of signature divisible by 3). Both legs are outside "constructible from RS-sector data on a
GU-forced base," and **neither passes through the located carrier** `e_R = 1/12`. It does not rescue
conjecture D as stated.

**Consistency touchpoints (not forcing).** The reduction obstruction is sign-blind (enters as `m^2`), so the
alignment sign bit `tr(Q5 Phi^2)` lives elsewhere (A4); the Cartan = Krein = ghost-parity `Z/2` seat is
reproduced as `(+96, -96, 0)`; the `12k`/`24k` even-index arithmetic and the VG-V7 selection table are
untouched.

---

## Honest gaps carried

1. **Flat-twist scope.** F1 enumerates the **flat** twists genuinely available on the 3-manifold boundary
   `L(2;1)` (deck-group lines, flat `SU(2)+`, `Lambda^2_+` adjoint). A non-flat / bulk **relative** index over
   a 4-manifold `W` with `dW = L(2;1)` could carry a 3-adic bulk -- but its 3-content would come from `sigma`
   or `d'`, both external and disjoint from the carrier (RS-S2). The carrier itself is provably 3-inert for
   construction; the bulk route is the same off-carrier import already priced, so it does not route the `3`
   through `e_R`. This is the load-bearing boundary of the KILL: it is a KILL of the **carrier-routed**
   construction, not of the abstract existence of *some* off-carrier integer.
2. **From-memory analytic inputs (flagged in-script):** the Kirby-Melvin `p_1 = 4` framing normalization for
   `e_R` (mitigated by the agreeing independent Adams class-2/24 route, both `= 1/12`); the `L(p;1)`
   reduced-eta Donnelly/APS closed form (standard, reproduced, internally validated by `sum_a xi_a = 0`); the
   `A-hat[S^6] = eta(S^6) = 0` transparency inherited from RS-S4 (structural).
3. **The framing identification** (GU's `Lambda^2_+` twist `=` the tangential `RP^3` framing carrying `e_R`)
   is reconstruction-grade, inherited from the paper's Section 7, not established here. F1 shows that *even
   granting* the identification, the constructive integerization fails.
4. **Internal tier only:** computed and self-adversarial (three discriminating controls: `L(3;1)`,
   scrambled-twist, alternate-framing), not independently replicated or peer-reviewed.

## Governance

Exploration-grade; **no edit to the frozen `located-not-forced` paper.** A promote/kill outcome is a
**PROPOSAL** for Section 9 that pauses for the maintainer. The proposed sharpening: the located order-3
carrier `e_R = 1/12` on the GU-forced `L(2;1)` spine has **no integer-index preimage constructible from any
GU-admissible twist** (every twist `eta` is 2-adic on the `Z/2` deck, so `v_3(I) = -1` and the `Z/3`
component is frozen at `2/3`), so the `order-3-class -> integer-3` bridge is **refuted by construction** on
the located carrier, converting RS-S4's GATED to KILL on that branch; the only surviving route is the RS-S2
double external import, off-carrier and disjoint from `e_R`. The generation-count verdict is unchanged:
**OPEN** (external by structure; now with the carrier's constructive bridge specifically closed). Any
verdict/status flip pauses for Joe.
