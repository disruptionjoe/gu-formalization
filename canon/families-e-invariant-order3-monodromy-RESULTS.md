---
title: "Families e-invariant over a one-parameter K3 family: the decisive first computation from the twenty-lens build-method sweep. Result: 2-primary on ALL honest data (incl. the new order-3 Nikulin-monodromy Lefschetz invariant); the Z/3 route is gated on the unbuilt fine equivariant rho -- located-not-forced confirmed at the families level, no fabrication."
status: staged
doc_type: results
created: 2026-07-09
grade: "COMPUTED / exact (rational arithmetic, 12 checks, exit 0). Target-import-safe (firewall {24,3} enforced). Internal tier (caveat (e)). No CANON.md promotion, no verdict/public-posture change. Pauses for Joe."
depends_on:
  - explorations/twenty-lens-source-action-build-method-sweep-2026-07-09.md
  - canon/rs-function-space-framework-SPEC.md
  - canon/source-action-family-index-interface-SPEC.md
  - canon/rs-boundary-eta-2primary-RESULTS.md
  - absorbed/gu-source-action/DEAD-ENDS.md
scripts:
  - tests/rs-function-space/families_e_invariant_order3_monodromy.py
---

# Families e-invariant over a one-parameter K3 family (the sweep's decisive first computation)

The twenty-lens build-method sweep selected the **Adams e-invariant / Z/24 route** (lens 4, hardened by
the CRT lens 17 and the adversarial lens 16) as the right FIRST build for the RS K3 family-index crux,
because it is the only method whose home (`pi_3^s = Z/24 = Z/8 (+) Z/3`) natively contains the order-3
generation arena, and it is cheap and decisive. This is that computation.

Method: read the families e-invariant as a `Z/24` class, `e = N/24`; the count can only live in the
`Z/3`-part `N mod 3`. Firewall (`DEAD-ENDS.md`): no value may be manufactured from `chi(K3)=24`, the
`/8` normalization, `A-hat=3`, or `contractible-fiber => 1`.

## Result (`families_e_invariant_order3_monodromy.py`, 12 checks, exit 0)

| object | Z/24 class N | CRT (Z/8, Z/3) | reading |
|---|---|---|---|
| **boundary-spine framing** `e_R = p1/48 = 1/12` | **2** | (2, **2**) | a REAL located order-3 object -- but a boundary FRAMING datum, not a families index |
| bulk `I_3/2[K3] = 21 sigma/8` | -42 -> 6 | (6, 0) | 2-primary |
| twist-by-16 RS index | -672 -> 0 | (0, 0) | 2-primary |
| `ch2(S_X)[K3]` honest | -5376 -> 0 | (0, 0) | 2-primary |
| RS boundary APS eta (STEP 2) | 0 | (0, 0) | 2-primary |
| **NEW: order-3 Nikulin monodromy Lefschetz** `L(phi)=6` | 6 -> 6 | (6, **0**) | **2-primary -- even the order-3 clutching's topological invariant is 0 mod 3** |
| fine equivariant rho of the order-3 monodromy | -- | -- | **BLOCKED_NEEDS_SPEC (not fabricated)** *(UPDATE 2026-07-10: COMPUTED at geometric-benchmark grade -- Dirac rho carries a genuine nonzero Z/3 class (0,1,2)/3; RS rho is 2-primary, class (0,0,0), structurally (twist character -3 == 0 mod 3). "Not computable from existing data" was over-conservative: the benchmark IS computable via Donnelly + Nikulin + Hodge. The GU-operator-identity caveat stays open. See `canon/order3-equivariant-rho-RESULTS.md`.)* |

## The new datum and why it matters

A one-parameter K3 family is a mapping torus of a monodromy `phi`. Only an **order-3** monodromy can
possibly source the `Z/3` arena, and such automorphisms EXIST: a Nikulin order-3 symplectic automorphism
of K3 has exactly **6 fixed points** (Nikulin 1979; Garbagnati-Sarti 2007), invariant lattice rank **10**,
coinvariant rank **12** *(CORRECTION 2026-07-10: this line originally said "invariant 14, coinvariant 8" --
that is the ORDER-2 Nikulin package; the Lefschetz gate `L = 2 + r - s/2 = 6` with `r + s = 22` forces
`(r,s) = (10,12)` (coinvariant = Coxeter-Todd `K12`); caught and machine-verified by the order-3 rho
campaign, `tests/rs-function-space/order3-rho/`. The error was not load-bearing here -- only `L = 6` was
used.)*. Its topological families invariant -- the Lefschetz number `L(phi) = #Fix = 6` --
is itself **`0 mod 3`**. So the one clutching that could reach the generation arena still lands
2-primary at the topological level.

The ONLY object that could carry a nonzero `Z/3` families e-invariant is the **fine SPECTRAL
(rho / eta, not topological) equivariant invariant** of the order-3 action -- the APS-III rho of the
mapping torus. It is not computable from existing data; it requires the geometric GU K3-fibered
source-action operator, which is unbuilt (`absorbed/gu-source-action`, SG4 MISSING-CARRIER on the
indefinite `GL(4,R)/O(3,1)` fiber). Per this repo's discipline it is marked **BLOCKED, not fabricated**.

## Verdict

`FAMILIES_E_INVARIANT_2_PRIMARY_ON_ALL_HONEST_DATA__Z3_ROUTE_GATED_ON_UNBUILT_ORDER3_RHO`.

- A real order-3 object exists at the **boundary framing** (`e_R = 1/12`, `Z/3`-part 2) -- **located**.
- But **every honest FAMILIES number is `0 mod 3`**, including the new order-3-monodromy Lefschetz
  invariant. No families INDEX reaches the `Z/3` generation arena on the honest geometry.
- The single escape is the fine equivariant rho of an order-3 monodromy = an **external order-3 spectral
  section** GU does not supply -- exactly the **firewall-boundary hypothesis**, now sharpened to ONE
  computable target (that rho, once the source-action operator is built).

This is the sweep's predicted decisive outcome, computed rather than asserted: **located-not-forced is
confirmed at the families level**, and the remaining gap is localized to a single, well-posed, firewall-
guarded spectral object. It also tells us the expensive completion route (lens 9, the non-Krein-isometric
BV action) is **not yet warranted**: nothing honest reaches `Z/3`, so there is nothing for a forcing
action to match until the order-3 rho is built and shown nonzero.

## Boundary

Computed / exact, target-import-safe, internal tier. No CANON.md promotion, no verdict, canon, or
public-posture movement; the generation count stays OPEN (located, not forced). Pauses for Joe on any
promotion. The next build step, if taken, is the order-3 equivariant rho -- which still waits on the
source-action operator (`SG4` MISSING-CARRIER), i.e. it does not shortcut the unbuilt geometry.
