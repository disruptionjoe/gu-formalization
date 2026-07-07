---
artifact_type: exploration
status: exploration
created: 2026-07-07
title: "MP-M3 count-matching + anomaly: two DETERMINED structural predictions of the gapped mirror sector. (a) COUNT-MATCHING (THEOREM): both Krein halves carry the IDENTICAL 3 x 2 x 16 structure -- su(2)+ triplet {-2,0,+2}x32 and su(2)- doublet x48 MEASURED equal on the P-even (physical) AND P-odd (mirror) 96s, internal so(5) Casimir uniform on both -- so N_mirror(families) = N_visible(families): the dark/mirror sector has EXACTLY as many families as the visible sector (the absolute number 3-vs-6 stays OPEN; only the matching is fixed). (b) ANOMALY (THEOREM): all four SM gauge-anomaly coefficients of the physical half VANISH -- SU(3)^3=0, SU(2)^2U(1)=0, U(1)^3=tr(Y^3)=0, grav^2U(1)=tr(Y)=0 -- forced by the umbrella fact that Spin(10) is anomaly-SAFE (full so(10) cubic tensor A^{abc}=0 on the 16); the gapped mirror is the exact CPT/anomaly-conjugate (16bar), so gapping it is anomaly-consistent and the mechanism CANNOT break gauge consistency. Carrier-native corroboration in (14,0): tr(Y)=tr(Y^3)=0 on both 96-halves of the actual 192-dim carrier. The absolute scale mu=phi stays DYNAMICS-GATED."
grade: "THEOREM (both results). Count-matching: exact measured equality of the su(2)+ x su(2)- x internal-16 decomposition on the two Krein halves (no assumption; the '3' is read from the su(2)+ Cartan multiplicity on each half). Anomaly-freedom: the four SM coefficients are computed from the derived Spin(10) -> SU(3)xSU(2)xU(1) structure and all vanish, umbrella'd by the vanishing full so(10) cubic anomaly tensor on the 16 (Spin(10) has no symmetric cubic Casimir); corroborated directly on the 192-dim carrier for U(1)^3 and grav^2-U(1) on BOTH halves. Controls have power: the su(3) fundamental reads A=d^118/2!=0 and its conjugate the exact negative; tr(Y^2)!=0. SM identification of the 16 as one generation is standard GUT physics, flagged FROM-MEMORY. No absolute-mass claim; mu is dynamics-gated. Count 3-vs-6 stays OPEN -- only the matching between halves is determined."
depends_on:
  - explorations/big-swing-2026-07-06/VG-V8-t5-map-attempt.md
  - explorations/big-swing-2026-07-07/BIG-SWING-ALIGNMENT-PHASE-NOT-TUNING.md
  - explorations/big-swing-2026-07-07/MP-M2-dark-vs-visible.md
  - canon/ghost-parity-krein-synthesis.md
  - papers/drafts/Transcript into the impossible.md
scripts:
  - tests/big-swing/mp_m3_count_and_anomaly.py
---

# MP-M3 -- Count-matching and anomaly consequences of the gapped mirror sector

**The swing.** V8 + the A-series established, at kinematic grade, that the condensate
`phi*Pi_mirror` (`Pi_mirror = (I - K|_W)/2`) gaps all 96 mirror states at mass `~ mu` while
keeping all 96 generation states massless, `[M, P_ghost] = 0`, on the physical sector
`96 = 3 x 2 x 16`. That is an internal-consistency result. This route makes it face outward and
EXTRACTS two falsifiable/structural predictions of the gapped mirror sector:
**(a)** does the mechanism yield `N_mirror = N_generation` (does the dark sector have the same
family count as the visible one)? and **(b)** does gapping the mirror leave an anomaly-free chiral
Standard Model, with the mirror the exact anomaly-conjugate that makes the removal consistent?

Script: `tests/big-swing/mp_m3_count_and_anomaly.py` (exit 0; every number below is printed by it).
Machinery reused verbatim from the verified carrier recipe (`vg_v8_t5_map_attempt.py` /
`ghost_parity_krein.py`) and the Spin(10) construction of `mp_m2_dark_vs_visible.py`.

## 0. Anchors (reproduced before any claim)

(9,5) carrier, timelike `{4..8}`: `rank(Gamma) = 128`, `dim ker = 1664`, triplet dim `192`,
triplet Krein signature `(+96, -96, 0)`, and `P_ghost = -Q5` on `W` (residual `3.7e-14`). The
physical half is the `K`-positive 96, the mirror half the `K`-negative 96. (14,0) reproduces its
own anchor set (rank 128, ker 1664, triplet 192, Krein `(+96, -96)`) for the carrier-native
anomaly corroboration in Section 5.

## 1. (a) Count-matching: N_mirror = N_generation (THEOREM, measured)

The family structure is **measured on both Krein halves**, not assumed. The "3" is read as the
`su(2)+` Cartan multiplicity of each half:

| half | su(2)+ (family) weights | su(2)- weights | internal so(5) Casimir |
|---|---|---|---|
| PHYSICAL (P-even) 96 | `{-2, 0, +2} x 32` (triplet, "the 3") | `{-1, +1} x 48` (doublet) | uniform `2.500` |
| MIRROR (P-odd) 96 | `{-2, 0, +2} x 32` (triplet, "the 3") | `{-1, +1} x 48` (doublet) | uniform `2.500` |

Both halves are `3 x 2 x 16 = 96` with **identical** decompositions: the `su(2)+` family triplet
is a `3` on each side, the `su(2)-` doublet a `2` on each side, and the internal `so(5)_s (+)
so(5)_t` Casimir is a single isotype (one 16) with the SAME value on both. So:

> **DETERMINED (structural prediction).** `N_mirror(families) = N_visible(families)`. The
> dark/mirror sector has **exactly as many families as the visible sector**. The Krein split
> pairs each visible family with one mirror family; there is no family-count asymmetry across the
> physical/ghost line.

**Honest scope.** This determines the *matching*, not the *number*. The absolute family count
(3 vs 6 -- the `su(2)+` triplet is a clean 3, but the physical sector also carries the `su(2)-`
doublet, so whether the visible family count is 3 or 6 is the count question canon leaves OPEN)
is untouched. What M3 adds is that whatever that number is, the mirror sector carries the same one.

## 2. The 16 of Spin(10) and the SM embedding (DERIVED, reused from M2)

The internal matter factor is the `16` of `Spin(10)`, built independently as the `+`-chirality
spinor of `Cl(10)` from five fermionic oscillators (`{Gamma_a, Gamma_b} = 2 delta_ab` at
`0.0e+00`; chirality `Gamma_11` splits the 32-dim Fock space into `16` and `16bar`). The SM
embedding `SU(3)_c x SU(2)_L x U(1)_Y` is fixed inside `Spin(10)` (color on oscillators `{0,1,2}`,
weak on `{3,4}`); hypercharge `Y = sum_k y_k (n_k - 1/2)`, `y = (-1/3,-1/3,-1/3,+1/2,+1/2)`, and
`Q = T3 + Y` is a pure output. `Y` commutes with all `SU(3)_c` and `SU(2)_L` generators
(`9.6e-17`), i.e. it is a legitimate SM `U(1)`. The bridge to the carrier (M2, reused): the
carrier's internal factor IS this same irrep (the `16`), so its Cartan/anomaly spectrum is the
carrier's -- `su(2)+` (family) and `su(2)-` are separate tensor factors on which the gauge group
acts trivially.

## 3. (b) The four SM anomaly coefficients vanish (THEOREM)

Computed on the physical `16`, DERIVED from the structure above:

| anomaly | quantity | value |
|---|---|---|
| `SU(3)^3` | color cubic tensor `A^{abc}` of the 16 (2 quark triplets `-` `u^c` `-` `d^c`) | `0.0e+00` |
| `SU(2)^2 U(1)` | `tr_16({T^a_L, T^b_L} Y)` (`sum_doublets Y`) | `4.4e-16` |
| `U(1)^3` | `tr_16(Y^3)` | `1.1e-16` |
| `grav^2 U(1)` | `tr_16(Y)` | `-2.2e-16` |

**The umbrella.** All four are forced by one fact: the **full `so(10)` symmetric cubic anomaly
tensor `A^{abc} = tr(T^a {T^b, T^c})` vanishes on the 16 for every triple of the 45 generators**
(`max|A^{abc}| = 0.0e+00`). `Spin(10)` has no symmetric cubic Casimir (`d`-symbol identically
zero), so `A^{abc} = 0` for any representation, and hence every subgroup anomaly -- including all
four SM coefficients -- is zero. **The physical half is anomaly-free BECAUSE the unifying gauge
group is `Spin(10)`.** This is the standard GUT reason `SO(10)` models are automatically
anomaly-free; the identification of the `16` as one SM generation is flagged FROM-MEMORY.

**Controls have power.** The identical anomaly routine on the `su(3)` FUNDAMENTAL (a single chiral
color triplet) reads `A^{abc} = d^{abc}/2` with `max ~ 0.289 = 1/(2 sqrt 3)` (the routine *can*
see an anomaly), and on its conjugate `3bar` the EXACT negative (`A_conj = -A`). The quadratic
Dynkin index `tr_16(Y^2) = 3.333 != 0` (Y acts nontrivially). So the 16's vanishing cubic is
content, not a blind spot.

## 4. (c) The mirror is the exact anomaly-conjugate; gapping is consistent (THEOREM)

The gapped mirror half is the `16bar` -- the CONJUGATE representation of the physical `16`
(opposite chirality `Gamma_11`). Its four coefficients vanish too (`A_color = 0.0e+00`,
`tr(Y^3) = 1.1e-16`, `tr(Y) = 0.0e+00`), and its cubic anomaly tensor is the EXACT negative of the
physical half's -- verified with teeth on the anomalous `su(3)` control (`3bar = -3`). The full
vectorlike `16 (+) 16bar` has identically zero anomaly (`tr_32(Y^3) = 2.2e-16`).

> **DETERMINED.** The mirror sector is the exact CPT/anomaly-conjugate of the physical sector.
> Because the physical half is anomaly-free **on its own** (`Spin(10)` safe), gapping the mirror
> leaves a consistent chiral theory: **the mechanism cannot introduce a gauge anomaly.** The
> mirror is the vectorlike partner, Dirac-massable at any `mu` with zero anomaly cost -- which is
> *why* it can be uniformly gapped.

Had the GUT group possessed a cubic anomaly (e.g. `SU(5)`), anomaly-consistency would have imposed
a nontrivial constraint on which states the condensate may gap; the fact that it does not is a
determined consequence of the `Spin(10)` structure, not an assumption.

## 5. Carrier-native corroboration (14,0)

To show the anomaly-freedom is native to the 192-dim carrier and not only a property of the clean
Fock model, we work in the Riemannian internal signature (14,0), where the internal `so(10)` is
fully COMPACT and all 45 bivectors commute with `P_ghost` (they preserve the Krein halves). Five
internal Cartan bivectors `H_k = (i/2) g_{2k} g_{2k+1}` have eigenvalues `{-1/2, +1/2}` (the
`so(10)` spinor Cartan), mutually commute, and commute with `P_ghost`. Building `Y = sum_k y_k H_k`
with the same weights:

- `grav^2-U(1)`: `tr(Y) = 0` on BOTH the physical (`-8.3e-15`) and mirror (`8.3e-15`) 96-halves.
- `U(1)^3`: `tr(Y^3) = 0` on BOTH halves (`-1.2e-14`, `8.3e-15`).
- control: `tr(Y^2) = 20.0 != 0` on the physical 96 (the trace machinery has power).
- sampled `so(10)` cubic tensor on the physical 96 (400 random triples + 45 Cartan cubes):
  `max|A^{abc}| = 1.7e-14 ~ 0`.

So `U(1)^3` and `grav^2-U(1)` vanish directly on the actual carrier, on both halves -- the
anomaly-freedom is carrier-native.

## 6. What this settles / does not settle

**Settles (at stated scopes):**
1. **Count-matching (THEOREM):** `N_mirror(families) = N_visible(families)`; the two Krein halves
   carry the identical `3 x 2 x 16` structure. The dark sector has exactly as many families as the
   visible one.
2. **Anomaly-freedom (THEOREM):** the physical half is anomaly-free in all four SM channels,
   forced by `Spin(10)` safeness; verified on the Fock 16 and (for `U(1)^3`, `grav^2-U(1)`) on the
   carrier, both halves.
3. **Anomaly-consistent gapping (THEOREM):** the mirror is the exact anomaly-conjugate; removing
   it cannot break gauge consistency.

**Does not settle:**
- **The absolute family count 3-vs-6.** Only the matching between halves is determined; the number
  itself is the OPEN count question, untouched.
- **The absolute mirror mass scale `mu = phi`.** DYNAMICS-GATED; set by the unbuilt VEV/source
  action. No absolute-mass claim is made.
- **The orientation sign bit** (which half is physical). Discharged as unphysical by A3; not
  re-opened here.
- **Whether the mirror is dark or charged.** That is MP-M2's question (answer: CHARGED/COLORED, a
  heavy mirror generation). M3 adds only that this charged mirror generation is the exact
  anomaly-conjugate of the visible one.

## 7. Honest gaps

1. **The SM identification of the 16 is FROM-MEMORY.** That `Spin(10)` is anomaly-safe and that the
   `16` is one SM generation are standard GUT facts, flagged as physics knowledge, not re-derived
   from first principles here (though the four coefficients themselves ARE computed on the
   explicitly-built 16).
2. **The bridge (carrier internal factor = the 16).** The four Fock-model coefficients transfer to
   the carrier via the measured "internal factor is one 16" (uniform `so(5)` Casimir). Section 5
   corroborates two of the four directly on the carrier; `SU(3)^3` and `SU(2)^2-U(1)` are carrier-
   corroborated only through the sampled `so(10)` cubic tensor, not by an explicit carrier-level
   `SU(3)`/`SU(2)` embedding.
3. **Kinematic only.** No dynamics, no source action; `mu` is dynamics-gated and never predicted.
4. **The count stays OPEN.** Nothing here selects 3, selects a chirality, or resolves 3-vs-6; the
   determined content is the *matching* and the anomaly-consistency, not the absolute count.

## Governance

Exploration-grade; no canon promotion proposed. The determined structural predictions
(family-count matching across the Krein split; anomaly-freedom of the physical half forced by
`Spin(10)` safeness; the mirror as exact anomaly-conjugate) are candidates for the prediction table
of the second-paper (mirror-mechanism) frontier, flagged for Joe, not applied. Generation-count
verdict remains OPEN. Verification tier: internal, single-run to exit 0 with powered controls; no
external adversarial pass yet.
