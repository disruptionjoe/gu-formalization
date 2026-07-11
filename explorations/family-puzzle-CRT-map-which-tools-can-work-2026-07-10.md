# The family puzzle, mapped: which topological tools CAN force the generation number (and which can't)

2026-07-10. GU-INDEPENDENT synthesis, world-facing. Turns the campaign's theorem-grade two-primary /
CRT-two-arena result into a PREDICTIVE MAP for the generation-number ("why 3 families?") problem: it
sorts the field's tools into those that can possibly force an odd count and those that are arithmetically
incapable, and points to the under-explored tool class that can. Useful to anyone working the family
puzzle, regardless of GU.

## The organizing fact (elementary, checkable)

A topological generation count, if it exists, is an ODD integer. The relevant stable arena is
`pi_3^s = Z/24 = Z/8 (+) Z/3` (Chinese Remainder Theorem; `|Im J_3| = denom(B_2/4) = 24`, Adams). By CRT
the 2-primary summand `Z/8` and the 3-primary summand `Z/3` are DISJOINT and non-interacting:
`Hom(Z/8, Z/3) = Hom(Z/3, Z/8) = 0`, and `Hom(Z/3, Z) = 0` (no torsion-to-free map). Consequence: any
invariant valued in a finite 2-group or a torsion-free integer index is arithmetically INCAPABLE of
carrying the odd (3-primary) part -- it can locate a slot but never force an odd count.

## The map (each tool by its primary character -> can it force an odd count?)

| Tool used on the family puzzle | value group | primary character | can force odd count? |
|---|---|---|---|
| per-generation anomaly cancellation | `Z` (free integer) | torsion-free | **NO** (`Hom(Z/3,Z)=0`) |
| ordinary Dirac / Atiyah-Singer index | `Z` (free) | torsion-free | **NO** |
| mod-2 Witten anomaly, Rokhlin (16), Kervaire, spinor-dim `2^k` | `Z/2`, `Z/16`, `2^k` | 2-primary | **NO** (`gcd(3,2^k)=1`) |
| cross-chirality Krein signature | `Z` (free) | torsion-free | **NO** |
| **Adams e-invariant / J-homomorphism** (`e_KO`) | `Z/24` | **reaches `Z/3`** | **YES** (`e_KO(8nu)=1/3`) |
| **Garcia-Etxebarria-Montero `Z/9` anomaly** | `Z/9` | **3-primary** | **YES** (forces `N_gen in 3Z`) |
| **Wan-Wang-Yau beyond-cohomology `p_1` part** | isolates `n=2,3` | 3-primary reach | **YES** |
| **equivariant Spin/KO G-index (order-3 rho)** | `Z/3`-valued | **3-primary** | **YES** (under-explored) |

## The predictive content (the useful part)

**The literature's success/failure pattern is EXPLAINED and PREDICTED by primary character:** every tool
that has ever constrained the generation number (GEM's `Z/9`, WWY's Pontryagin split, the e-invariant)
reaches the 3-primary summand; every tool that fails (per-generation anomaly, ordinary index, all mod-`2^k`
classes) is 2-primary or free. This is not a coincidence -- it is CRT. So the map makes a falsifiable
prediction about FUTURE approaches:

> A topological approach to the generation number can succeed ONLY IF its invariant reaches the
> 3-primary (odd-torsion) summand. Any 2-primary or free-integer construction is a dead end for forcing
> an odd count, no matter how natural -- it can locate the slot but not fill it.

## The under-explored viable tool (where to look)

The map singles out one 3-primary-reaching tool that the family-puzzle literature has barely used:
**equivariant Spin/KO invariants (the G-index / order-3 symplectic-automorphism rho).** This campaign's
exhaustiveness result showed the equivariant Nikulin `rho = (0,2,1)/3` genuinely reaches the odd torsion
that ordinary (non-equivariant) KO/Spin/Pin cannot. So the concrete research direction the map recommends
is: **look for a generation-count mechanism in equivariant (finite-group) spectral invariants on the
compactification geometry**, not in ordinary index/anomaly theory -- because only the equivariant/3-primary
tools are arithmetically able to carry an odd count.

## Grade / boundary

GU-independent. The arithmetic (CRT disjointness, `Hom` vanishings, the primary decompositions) is
elementary and checkable; the literature classification is best-effort but each entry is a standard
result. The predictive claim ("only 3-primary-reaching tools can force an odd count") is a genuine,
falsifiable meta-statement about the family puzzle. It does NOT claim any tool DOES force 3 (GU's own
order-3 -> integer-3 bridge stays open). The useful output is the MAP: it tells the field which entire
classes of approach are dead ends and which one class is worth pursuing. No claim/canon movement.
