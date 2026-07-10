---
artifact_type: exploration
status: exploration
created: 2026-07-09
title: "SG5 -- three disjoint homes for the prime 3: import-channel independence"
grade: "COMPUTED (exact finite-abelian-group arithmetic). GU-independent structural result. Internal, single implementation. No verdict/canon/posture change."
depends_on:
  - explorations/big-swing-2026-07-07/BIG-SWING-RS-INDEX-STILL-GATED.md
  - explorations/big-swing-2026-07-07/RS-S3-double-duty-base-selection.md
  - explorations/sequential-goals-2026-07-09/SG2-price-sigma-mod3-import.md
scripts:
  - tests/big-swing/sg5_import_channel_independence.py
---

# SG5 -- closing the arithmetic-level double-duty hope

## The swing

After the native-construction escape branch was closed (BIG-SWING-RS-INDEX), the only surviving route
to an odd count is a **double external import**: `3 | m` (cubic Yukawa) **and** `3 | sigma` (base
signature), both disjoint from the located carrier `e_R = 1/12`. Route S3 killed the "double-duty"
hope (that one source action supplies the base selector) at the **source-action level**. This goal
closes the same hope at the **arithmetic/cohomological level**.

## What was computed (`tests/big-swing/sg5_import_channel_independence.py`, exit 0)

The prime 3 appears in three homes: **H1** base signature `sigma in Z`; **H2** cubic coupling
`m in Z`; **H3** located carrier `e_R = 1/12 in Q/Z <= pi_3^s = Z/24` (its 3-part is the `Z/3` in
`Z/24 = Z/8 (+) Z/3`). Exact finite-group arithmetic shows:

1. `Hom(Z/24, Z) = 0` -- the carrier induces no integer, so **H3 cannot supply H1's `sigma`**.
2. `pi_3^s = Z/8 (+) Z/3`; the S3 mirror-hiding selector lives in the order-8 `Z/8`, and
   `Hom(Z/8, Z/3) = 0`, so the selector cannot reach the 3-part -- **S3's kill reconfirmed
   arithmetically**, and H3's 3-part is isolated.
3. **Carrier 3-inertness:** every natively selected twist has `m^2 == 1 (mod 3)`, so H3 supplies
   neither the `m`-factor (H2) nor the `sigma`-factor (H1); `3|m` and `3|sigma` are logically
   independent divisibility events.
4. **Joint realizability = full product:** with the carrier fixed at `e_R = 1/12`, the residues
   `(sigma mod 3, m mod 3)` realize the entire `Z/3 x Z/3` with no forbidden combination -> H1, H2
   independent given H3.
5. **No double-duty homomorphism:** every linking Hom vanishes
   (`Hom(Z/24,Z) = Hom(Z/3,Z) = Hom(Z/8,Z/3) = Hom(Z/2,Z/3) = 0`), so no single GU datum links two
   homes.

## Verdict

**The prime 3 has three structurally independent homes.** The surviving escape (`3|m AND 3|sigma`) is
**two independent external choices**, neither derivable from the located carrier nor from each other
by any GU-forced map. This **closes the arithmetic-level double-duty hope** (S3 closed the
source-action-level one), leaving the escape as a genuine external supply of two independent data --
consistent with the firewall-boundary reading. This is an exact, GU-independent result (holds
regardless of GU's correctness). No target imported; generation count stays OPEN (located, not forced).
