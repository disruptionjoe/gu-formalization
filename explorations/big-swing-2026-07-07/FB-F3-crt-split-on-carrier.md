---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "FB-F3 (the CRT Z/8 (+) Z/3 split read ON THE ACTUAL framed-bordism carrier): is the Z/3 summand of pi_3^s=Z/24 reachable at all by a SECTOR-CONSTRUCTIBLE invariant, or does the achirality wall + 2-adicity force everything into Z/8 even in framed bordism? HONEST OUTCOME: GATED, sharpened. The decisive readout is a TRICHOTOMY of reachability, machine-verified via an EXPLICIT, roundtrip-validated CRT iso Z/24 -> Z/8 x Z/3 (24 = 2^3*3 factored by sympy, gcd(8,3)=1, idempotents e8=9/e3=16, bijective over all 24 classes; the 24 is |Im J_3|=denom(B_2/4), Bernoulli/homotopy provenance kept DISTINCT from chi(K3)=24): (1) the FRACTIONAL Adams e-invariant carrier e_R=1/12 has Q/Z-primary decomposition 3/4 (2-primary) + 1/3 (3-primary, NONZERO order 3), and its framed-bordism class = e_R*24 = 2 projects to (2,2) -- NONZERO in BOTH summands, so the achirality wall does NOT wall the e-invariant carrier into Z/8; the Z/3 summand IS genuinely reached by the carrier, but ONLY as the fraction 1/3, which by Hom(Z/3,Z)=0 is a torsion datum, never an integer; (2) every SIGNED sector index is 0 by the measured achirality {K,chi}=5.2e-14 (net 96-96=0 on the 128-carrier), projecting to CRT (0,0) -- contributing to NEITHER summand; (3) the UNSIGNED twisted index ind_full=12k+16 m^2 d'-2 sigma has Z/3-component == m^2 d' + sigma, and every native selected twist m in {1,2,5} has m^2==1 (mod 3), so the carrier's own twist is 3-INERT and the Z/3-component is carried ENTIRELY by external (d' unbuilt dynamics, sigma external signature), disjoint from the RP^3 carrier; a carrier-controlled integer Z/3-charge needs the DOUBLE external import 3|m AND 3|sigma, which no native twist supplies. CONCLUSION: the Z/3 summand is reachable by the FRACTIONAL carrier (1/3) and by EXTERNAL integers, but by NO carrier-native sector-constructible INTEGER index. This CONFIRMS the Section-9 category error ONE LEVEL UP from Hom(Z/3,Z)=0: not 'Z/3 is unreachable', but 'the carrier reaches Z/3 only as 1/3, and every integer that reaches Z/3 is external or the still-unbuilt relative/equivariant twisted-RS index whose nonzero geometry-dependent bulk cancels 1/12 mod Z'. conjecture_signal = GATED, with a KILL sub-finding on the native-integer branch (consistent with RS-S2). Controls (discriminating): pure Z/3 classes (8,16) project to (0,nonzero), pure Z/8 classes (3,9) to (nonzero,0), a sigma=1 twisted index reaches Z/3 via the external sigma, a scrambled unbalanced grading gives net!=0. PROMOTE-or-KILL stays on the single unbuilt object."
grade: "CONSISTENT_UNCOMPUTED (route verdict GATED); component legs at THEOREM grade at their stated scopes. The CRT iso is a machine-certified theorem (explicit projection + idempotent inverse, roundtrip over ALL 24 classes, bijective; the split derived from the sympy factorization 24=2^3*3, not asserted). The carrier class 2 = e_R*24 and its projection (2,2) are exact; the Q/Z-primary decomposition 1/12 = 3/4 + 1/3 is exact CRT-of-Q/Z arithmetic (reconstruction check 3/4+1/3=13/12==1/12 mod Z). The signed-index net-0 is MEASURED on the actual 128-dim Cl(9,5) carrier ({K,chi}=5.2e-14, net 96-96=0) with a K-commuting control (net=96) and a scrambled unbalanced control (net=4). The twisted-index mod-3 reduction and its agreement with the CRT Z/3-projection are verified over 300 random integer inputs; the carrier 3-inertness m^2==1 mod 3 is measured per native twist; the 3|m sweep over m in 0..8 is exact. FROM-MEMORY flags: the Kirby-Melvin p_1=4 framing normalization for e_R (mitigated by the agreeing class-2/24 Adams route); the Adams image-of-J theorem |Im J_{4s-1}|=denom(B_2s/4s) (STANDARD, applied not re-proved); the RS-S2/h2 twisted-index formula ind_full=12k+16 m^2 d'-2 sigma (recomputed here from the CP^2 twist, inherited from VG-V7/h2 canon). TARGET-IMPORT GUARD at maximum strictness: no element of {3,8,24,chi(K3)=24,Ahat=3,rank_H=4,ind_H=8} assumed, inserted, hardcoded as an answer, or divided by to GET an answer; the two 24s (|Im J| via Bernoulli vs chi(K3) via Betti) kept provenance-distinct; every 3 measured with its chain printed (24=2^3*3 factored; the carrier class 2 measured from e_R; m^2 mod 3 measured per twist; 8,16 as pure-Z/3 controls; 3,9 as pure-Z/8 controls). Every count stated as 'mechanism/carrier M forces c', never 'GU forces c'. Internal tier: computed + self-adversarial (measured achirality, roundtrip-validated CRT, discriminating controls), not externally replicated or peer-reviewed."
depends_on:
  - papers/candidates/located-not-forced/located-not-forced-generation-count-2026-06-29.md
  - canon/h2-base-index-chirality.md
  - explorations/big-swing-2026-07-07/RS-S4-base-forcing-bismut-cheeger.md
  - explorations/big-swing-2026-07-07/RS-S2-relative-index-nogo.md
scripts:
  - tests/big-swing/fb_f3_crt_split_on_carrier.py
---

# FB-F3: the CRT split Z/24 = Z/8 (+) Z/3, read on the actual framed-bordism carrier

**The swing.** The RS-index swing (2026-07-07) narrowed the located-not-forced count to ONE remaining
carrier: the paper's Section 9 / conjecture-D **framed-bordism** object. The GU-forced `RP^3 = L(2;1)`
spine, with its self-dual `Lambda^2_+` tangential framing, escapes the 2-adic cohomology wall
(`H^2(RP^3;Z) = Z/2`) into **framed bordism** `pi_3^s = Z/24`. By CRT, `Z/24 = Z/8 (+) Z/3` into disjoint,
non-interacting summands. A homotopy-theoretic (odd) generation count, if it exists, must live in the
`Z/3` summand, read by the Adams `e`-invariant via the image of `J`, with `e_R = 1/12`.

**Route F3 asks:** *is the `Z/3` summand reachable at all by a sector-constructible invariant, or does the
achirality wall (`{K,chi}=0`) plus base 2-adicity force everything into the `Z/8` (2-primary) summand even
in framed bordism?*

**Honest outcome: GATED, sharpened into a reachability trichotomy.** The `Z/3` summand **is** reachable --
but by exactly two objects, and neither is a carrier-native integer index: the **fractional** carrier
`e_R = 1/12` (3-primary part `1/3`) and **external** imports (`3|m` AND `3|sigma`). No sector-constructible
**integer** invariant has a carrier-native nonzero `Z/3`-component. This confirms the Section-9 category
error **one level up** from `Hom(Z/3, Z) = 0`.

All numbers below are printed by `tests/big-swing/fb_f3_crt_split_on_carrier.py` (run from repo root,
exit 0). Anchors reproduced first on the verified `Cl(9,5)` carrier: `rank(Gamma) = 128`,
`dim ker = 1664`, triplet Krein `(+96, -96, 0)`, and the measured achirality `{K, chi} = 5.2e-14`.

---

## 1. The CRT iso, built explicitly and validated (not asserted)

`pi_3^s = Z/24` because `|Im J_3| = denom(B_2/4) = denom(1/24) = 24` (Adams image-of-`J` / Bernoulli --
**homotopy** provenance, kept distinct from `chi(K3) = 24`, which is a Betti-sum rank). The split is
**derived** from the sympy factorization `24 = 2^3 * 3`: the coprime prime-power parts are `8` (2-primary)
and `3` (3-primary), `gcd(8, 3) = 1`, so `Z/24 ~= Z/8 (+) Z/3`.

The projection `x -> (x mod 8, x mod 3)` and its CRT inverse (idempotents `e8 = 9 = (1 mod 8, 0 mod 3)`,
`e3 = 16 = (0 mod 8, 1 mod 3)`) are built explicitly and **roundtrip-validated over all 24 classes**
(bijective, `invert(project(x)) == x` for every `x`). This is the machinery every subsequent readout uses,
certified as a theorem before use.

---

## 2. The carrier reaches `Z/3` -- but fractionally

The framed-bordism class of the `RP^3` spine is measured from the framing, not recalled:
`class = e_R * |Im J| = (1/12) * 24 = 2` (the `+/-2` of the paper's Section 8). Its CRT projection is

```
2  ->  (2 mod 8, 2 mod 3)  =  (2, 2)      NONZERO in BOTH summands.
```

So the achirality wall + 2-adicity do **not** force the `e`-invariant carrier into `Z/8`: the `Z/3` summand
is genuinely reached by the carrier. The `Q/Z`-primary decomposition of the `e`-invariant makes the shape
exact:

```
e_R = 1/12  =  3/4 (2-primary, order 4)  +  1/3 (3-primary, order 3).      (3/4 + 1/3 = 13/12 == 1/12 mod Z)
```

The 3-primary part `1/3` is **nonzero** -- the carrier carries a genuine order-3 datum in the `Z/3` summand.
But `1/3` is a **fraction** (a `Q/Z` torsion datum), and by `Hom(Z/3, Z) = 0` it is **never an integer**.
The carrier reaches `Z/3` only as the fraction `1/3`, not as a count. This is the swing's signature
discipline made quantitative: the `e`-invariant is `Q/Z`-valued; its `Z/3`-part is `1/3`, not the integer 3.

---

## 3. Every sector-constructible INTEGER invariant, CRT-projected onto `Z/3`

**(b.i) The SIGNED index is 0 by achirality.** On the actual 128-dim carrier, `{K, chi} = 5.2e-14` (K purely
cross-chirality), and the net chiral index of the maximal `K`-positive physical subspace is `96 - 96 = 0`
(measured by SVD-rank of the chirality-projected basis). CRT image: `(0, 0)` -- it contributes to **neither**
summand. Control: a `K`-commuting grading gives `net = 96`, and a scrambled **unbalanced** grading gives
`net = 4`; the net-0 is the load-bearing `{K,chi}=0` cross-chirality balance, not a rank tautology.

**(b.ii) The UNSIGNED twisted index is carrier-3-inert.** The Atiyah-Singer twisted RS index (h2 canon `12k`
bundle + `O(m)` twist + gravitational term, X spin) is

```
ind_full = 12k + 16 m^2 d' - 2 sigma,       Z/3-component == m^2 d' + sigma   (12==0, 16==1, -2==1 mod 3).
```

Verified over 300 random integer inputs, and the CRT `Z/3`-projection of the integer index (`reduce mod 24`,
then `mod 3`) agrees with `ind_full mod 3` in every case. The decisive fact:

| native selected twist | `m` | `m^2 (mod 3)` | `Z/3`-component |
| --- | --- | --- | --- |
| breaking line `O(-1)` | 1 | **1** | `d' + sigma` |
| quadratic condensate `O(-2)` | 2 | **1** | `d' + sigma` (`4d'+sigma`) |
| coset `D` anticanonical `O(5)` | 5 | **1** | `d' + sigma` (`25d'+sigma`) |

Every native twist has `m^2 == 1 (mod 3)`: the carrier's own twist is **3-inert**, so the `Z/3`-component is
carried **entirely** by `(d', sigma)` -- the section degree (unbuilt dynamics) and the base signature
(external) -- both **disjoint** from the `RP^3` carrier. A carrier-controlled `Z/3`-charge (nonzero for all
`d'`) requires `3|m` **and** `3|sigma` (double external import); no native selected twist supplies `3|m`.

---

## 4. Controls: the projection discriminates

- **Pure `Z/3` generators** (classes `8, 16 = 8*{1,2}`): project to `(0, 2)` and `(0, 1)` -- `Z/3` reached,
  `Z/8` zero. The projection **detects** `Z/3` charge.
- **Pure `Z/8` generators** (classes `3, 9`): project to `(3, 0)` and `(1, 0)` -- `Z/8` reached, `Z/3` zero.
  The projection **separates** the summands.
- **A `Z/3`-charged twisted index** (`sigma=1`, native `m=1`, `d'=0`): `ind_full = -2`, `Z/3`-component `= 1`
  -- nonzero, but via the **external** `sigma`. So the native/achiral 0 is a real measurement, not a blind
  zero.
- **A scrambled unbalanced grading:** `net = 4 != 0` -- the signed-index 0 is the measured `{K,chi}=0` fact.

---

## 5. The decisive readout (trichotomy) and conjecture signal

**Reachability of the `Z/3` summand of `pi_3^s = Z/24`, by object:**

| object | `Z/3`-reach | integer? | through the carrier? |
| --- | --- | --- | --- |
| fractional `e`-invariant `e_R = 1/12` | `1/3` (NONZERO) | **no** (fraction; `Hom(Z/3,Z)=0`) | yes (the carrier) |
| signed sector index (achirality) | `0` | yes (`=0`) | trivially (0) |
| unsigned twisted index, native `m` | `d' + sigma` | yes | **no** (`m^2==1` inert; external-carried) |
| carrier-controlled integer `Z/3`-charge | needs `3|m` AND `3|sigma` | yes | **no** (double external import) |

**So the `Z/3` summand IS reachable** -- by the fractional carrier (`1/3`) and by external integers -- **but by
NO carrier-native sector-constructible INTEGER index.** The achirality wall does not wall the `e`-invariant
carrier into `Z/8` (its class is `(2,2)`), yet no integer preimage of its `Z/3`-charge is sector-constructible:
the signed index is `0`, and the unsigned native twisted index's `Z/3`-charge is external-carried.

**This confirms the Section-9 category error ONE LEVEL UP from `Hom(Z/3, Z) = 0`.** The sharper statement is
not "the `Z/3` summand is unreachable" (it is reached, by `1/3`); it is: *the carrier reaches `Z/3` only as
the fraction `1/3`, and every integer that reaches `Z/3` is either external (`3|m` cubic coupling + `3|sigma`
signature) or the still-unbuilt relative/equivariant twisted-RS index whose nonzero geometry-dependent bulk
cancels `1/12` mod `Z`.*

**SIGNAL = GATED.**

- **KILL sub-finding (native-integer branch, consistent with RS-S2):** no sector-constructible **integer**
  invariant has a carrier-native nonzero `Z/3`-component. Signed -> `0`; unsigned native twisted ->
  external-carried; the double external import is disjoint from the carrier.
- **NOT a full KILL of conjecture D:** the `Z/3` summand is genuinely reached by the fractional carrier
  (`1/3`), and the ONLY object that could supply an **integer** preimage of that `1/3` is the unbuilt
  relative/equivariant twisted-RS index (the Section-9 / RS-S4 gate). PROMOTE-or-KILL stays on that one
  object.

---

## 6. Honest gaps carried

1. **From-memory analytic inputs (flagged in-script):** the Kirby-Melvin `p_1 = 4` framing normalization for
   `e_R` (mitigated by the agreeing class-2/24 Adams route); the Adams image-of-`J` order formula
   `|Im J_{4s-1}| = denom(B_2s/4s)` (standard, applied not re-proved); the RS-S2 / h2 twisted-index formula
   `ind_full = 12k + 16 m^2 d' - 2 sigma` (recomputed here from the `CP^2` twist, inherited from VG-V7 / h2
   canon).
2. **The framing identification** (GU's `Lambda^2_+` twist = the tangential `RP^3` framing carrying `e_R`) is
   reconstruction-grade, inherited from the paper's Section 7, not established here.
3. **Sector-constructible scope.** The trichotomy covers the signed index (achirality), the unsigned twisted
   index (native twist), and their CRT images. The unbuilt **relative/equivariant twisted-RS index** with a
   nonzero geometry-dependent bulk is exactly the object outside this scope -- and it is the surviving gate,
   not a gap in the enumeration.
4. **`sigma` and `d'` are external/unbuilt.** The `3|sigma` leg imports a different manifold's signature; the
   `d'` leg is the unbuilt source-action section. Neither passes through the located `RP^3` carrier.
5. **Internal tier only:** computed and self-adversarial (roundtrip-validated CRT, measured achirality,
   discriminating controls), not externally replicated or peer-reviewed.

## 7. Governance

Exploration-grade; **no edit to the frozen `located-not-forced` paper.** A promote/kill outcome is a
**PROPOSAL** for Section 9 that pauses for the maintainer. F3 returns **GATED**, so the proposed sharpening
is: record, under Section 9, that on the actual framed-bordism carrier the CRT `Z/3` summand is reachable by
the **fractional** `e`-invariant `1/3` and by **external** integer imports, but by **no** carrier-native
sector-constructible **integer** index -- confirming the category error one level up from `Hom(Z/3,Z)=0` and
collapsing the open bridge onto the single unbuilt relative/equivariant twisted-RS index (the RS-S4 gate).
The generation-count verdict is unchanged: **OPEN**.
