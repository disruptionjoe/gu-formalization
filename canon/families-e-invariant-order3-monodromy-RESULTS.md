---
title: "K3-family controls: listed bulk residues vanish mod 3; fine Nikulin rho is computed for A and B with different outcomes; native transfer open"
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

## Construction scope correction — Joe approved, 2026-11-20

Authority: `joe_direct_chat_2026_11_20_b`; wording correction, with existing
status and grade retained. The Nikulin order-3 **ghost-subtracted** benchmark A
has index -42 and zero rho class. The **geometric gamma-traceless** benchmark B
has index -38 and nonzero classes (0,2,1)/3. The source-native **Krein-graded**
complex remains unidentified at this invariant: retaining ghosts does not
specify their index grading or trace. A/B is a comparison, not an exhaustive
classification of source constructions. Neither residue supplies an integer
family count. Statements below about a binary or sole decider are restricted
to their declared comparison; they do not require building the source action
before testing defined structural subfamilies. Paper and released bytes are
unchanged. See the [approved-scope audit](../explorations/conditional-build/native-complex-order3-fork-2026-11-20.md)
and [follow-up benchmark and map test](../explorations/conditional-build/krein-order3-observation-label-2026-11-20.md).

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
| ghost-subtracted A bulk `I_3/2[K3] = 21 sigma/8` | -42 -> 6 | (6, 0) | 2-primary |
| twist-by-16 A index | -672 -> 0 | (0, 0) | 2-primary |
| `ch2(S_X)[K3]` honest | -5376 -> 0 | (0, 0) | 2-primary |
| RS boundary APS eta (STEP 2) | 0 | (0, 0) | 2-primary |
| **NEW: order-3 Nikulin monodromy Lefschetz** `L(phi)=6` | 6 -> 6 | (6, **0**) | **2-primary -- even the order-3 clutching's topological invariant is 0 mod 3** |
| fine equivariant rho, computed benchmarks | A: zero; B: nonzero | A:(0,0,0); B:(0,2,1)/3 in Q/Z | Dirac also nonzero; see order3 and gamma-traceless records. Native transfer open. |

## The new datum and why it matters

A one-parameter K3 family is a mapping torus of a monodromy `phi`. An **order-3** monodromy is a concrete candidate for the `Z/3` arena; such automorphisms EXIST: a Nikulin order-3 symplectic automorphism
of K3 has exactly **6 fixed points** (Nikulin 1979; Garbagnati-Sarti 2007), invariant lattice rank **10**,
coinvariant rank **12** *(CORRECTION 2026-07-10: this line originally said "invariant 14, coinvariant 8" --
that is the ORDER-2 Nikulin package; the Lefschetz gate `L = 2 + r - s/2 = 6` with `r + s = 22` forces
`(r,s) = (10,12)` (coinvariant = Coxeter-Todd `K12`); caught and machine-verified by the order-3 rho
campaign, `tests/rs-function-space/order3-rho/`. The error was not load-bearing here -- only `L = 6` was
used.)*. Its topological families invariant -- the Lefschetz number `L(phi) = #Fix = 6` --
is itself **`0 mod 3`**. This particular Lefschetz number has zero mod-3 residue; it does not
determine the fine spectral invariant.

The historical fine-rho gap was closed for published benchmarks on July10:
A has zero order-3 rho, while Dirac and B have nonzero classes. The earlier
claim that computing any such object required the GU source action was too
strong. Source-native transfer is still open.

## Current scoped verdict

- The listed A-derived bulk controls and the Lefschetz control vanish mod3.
- Boundary framing, Dirac rho and geometric-Q rho supply distinct located
  order-3 data. They are not interchangeable invariants.
- No calculation here identifies a physical integer family count or selects
  the source-native graded complex. The historical all-data-zero verdict is
  superseded by this construction-specific statement.

## Boundary

Computed / exact, target-import-safe, internal tier. No CANON.md promotion, no verdict, canon, or
public-posture movement; the generation count stays OPEN (located, not forced). Pauses for Joe on any
promotion. The benchmark rho computations are complete for A and B; native identification and
count transfer remain open without restricting all research to a source-action build.
