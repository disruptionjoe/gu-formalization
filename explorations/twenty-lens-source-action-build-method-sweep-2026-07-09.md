---
artifact_type: exploration
status: exploration
created: 2026-07-09
title: "Twenty divergent lenses on how to build the unbuilt object (the K3 family-index N / source action) -- method-selection sweep"
grade: "GENERATION ONLY. A divergent-lens ideation pass to select the best BUILD METHOD for the RS K3 family-index crux. Produces no number, moves no verdict/canon/public-posture. Per repo discipline: sweeps generate; only compute->verify decides. One computed probe is spun out separately (canon/families-e-invariant-order3-monodromy-RESULTS.md)."
depends_on:
  - canon/rs-function-space-framework-SPEC.md
  - canon/source-action-family-index-interface-SPEC.md
  - canon/rs-boundary-eta-2primary-RESULTS.md
  - absorbed/gu-source-action/DEAD-ENDS.md
  - explorations/sequential-goals-2026-07-09/SYNTHESIS-sequential-goals-2026-07-09.md
scripts:
  - tests/rs-function-space/family_generation_arena_probe.py
---

# Twenty lenses on how to build the unbuilt object

The object, in its current sharpened form: a **families-pushforward index `N`** of the twisted
Rarita-Schwinger operator over the metric fiber `GL(4,R)/O(3,1)`, K3-fibered, with pass bar
**`N != 0 mod 3` WITHOUT importing `chi(K3)=24`** (`source-action-family-index-interface-SPEC.md`).
Bulk and boundary terms are DONE and both 2-primary; the K3 family pushforward (STEP 3, obligations 3-5)
is the open crux. This sweep asks 20 divergent ways to build it, then selects a method.

## The 20 lenses (method + risk)

**Topological-index cluster**
1. **Atiyah-Singer families** -- `N = int_fiber ch(sigma_RS) Todd(T_vert)`; mod-3 lives in `ch2(T_vert)`. *Risk: ch2 on K3 ties to chi,sigma -> the disguised-24 trap.*
2. **K-theory / KK pushforward** -- symbol class in `K^0`, Gysin pushforward, hunt Z/3 in torsion. *Risk: the integer index kills torsion (Hom(Z/3,Z)=0); need K-theory-with-coefficients.*
3. **Exact-CAS characteristic classes** -- sympy: ch, Todd, A-hat as exact polynomials over the family, extract mod-3, let symbols expose chi-smuggling. *Risk: honesty enforcer, not an idea; needs the bundle as input.*

**3-primary-native cluster (the only routes whose home natively contains a 3)**
4. **Adams e-invariant / J-homomorphism** -- count lives in `Im J_3 = Z/24`, `e_R=1/12` order-3 already in hand; build the FAMILIES e-invariant of the RS boundary framing. *Deepest route. Risk: Q/Z-valued; needs a families lift to an integer.*
5. **tmf / elliptic cohomology** -- K3 -> Witten genus; `pi_3 tmf = Z/24` sees `Z/8 (+) Z/3` directly. *Risk: heavy; flagged LOCATE->FORCE lever.*
6. **Equivariant / Spin(8)-triality** -- read Z/3 as triality center / SU(3)_family, index in `R(SU(3))`. *Risk: real group torsion but stranded selector-side / frame-trivial.*
7. **K3-CFT / moonshine** -- read N off the boundary K3 sigma-model; Mathieu moonshine carries 3-torsion. *Risk: speculative bridge; central charge may be 2-primary.*

**Build-the-missing-differential cluster (attack the Krein-isometry wall)**
8. **BV/BRST cohomology** -- `N` = ghost-graded Euler char of the BV complex; the stabilized action IS the differential. *Risk: `(S,S)=0` doesn't close on the symbol algebra (s^2~103) -- the known incompleteness.*
9. **Non-isometric Seiberg-Witten** -- rebuild the SW action explicitly NON-Krein-isometric (isometric => zero net chiral, proven). *Risk: gauge/BRST consistency may not exist; where a real discovery OR a real no-go hides.*
10. **Velo-Zwanziger / dressed obstruction** -- keep the DRESSED commutator nonzero (never the bare one -- acausality trap), derive N from the causal RS propagator index. *Risk: VZ sector unbuilt, not finite-dim representable.*

**Regularization / verification cluster**
11. **Lattice / discretized** -- triangulate a K3-family, index = finite matrix signature. *Risk: torsion is a delicate continuum limit.*
12. **Lean/mathlib** -- formalize the families-index statement so no chi-import is hand-waved. *Risk: mathlib lacks families-APS; huge -- but kills the theater critique.*
13. **Spectral-flow / parametrized** -- vary coupling `t`, track index jumps. *Risk: the auxiliary-t route is exactly what STEP 2 replaced with the a-priori connection.*

**Cheap-decisive cluster**
14. **Anomaly inflow** -- compute the boundary anomaly the bulk must cancel, infer N by matching. *Risk: anomaly is Green-Schwarz 2-primary; likely misses the count.*
15. **Minimal-viable falsificationist** -- smallest computation that could find ANY honest `N != 0 mod 3`; bounded failure is itself the result. *Risk: absence of evidence.*
16. **Adversarial red-team** -- assume `N != 0 mod 3` impossible, prove the families pushforward is always 2-primary. *If it proves: settled no-go. If it fails: shows where 3 enters.*

**Reframe cluster**
17. **CRT-native / odd-localization** -- never ask for an integer; build a Z/8 (selector) and a Z/3 (carrier) invariant, compute only the Z/3 via odd-torsion localization. *Respects Hom(Z/3,Z)=0. Risk: yields a class, not a count -- may be the honest answer.*
18. **SPT / tenfold-way** -- RS sector as an SPT; the antilinear selector is class CII; AZ classification gives torsion natively. *Risk: the SPT invariant is the selector (2-primary), not the carrier.*
19. **TQFT / Dai-Freed functor** -- family index as a bordism-category functor; "external by structure" = a boundary-condition datum. *Risk: makes the firewall rigorous but likely confirms external.*
20. **Firewall-native** -- take the firewall-boundary hypothesis as primary; build N as an explicit external APS/Dai-Freed spectral section, compute the MINIMAL external structure needed. *Risk: locates, does not force.*

## Synthesis

**Strong convergence (7 lenses: 4,5,6,7,17 + honesty 3,16).** An ordinary integer index `N in Z` CANNOT
carry the count: the AS-integer is provably 2-primary and `Hom(Z/3,Z)=0` kills the Z/3. The right object
is a **Z/24-valued (framed-bordism / tmf) families invariant**; the count lives only in its Z/3 summand.
The Adams e-invariant (4) is deepest because `e_R=1/12` is already computed and located.

**The real fork (genuine disagreement).** The build-the-differential cluster (8,9,10) dissents:
- *e-invariant / tmf / CRT camp*: the correct object is a torsion class; building it rigorously LOCATES
  the 3 and most likely confirms it has no integer image (located-not-forced, proven at families level).
  Cheap, decisive, honest.
- *BV / non-isometric-SW camp*: locating is not building; the count becomes a NUMBER only by building the
  non-Krein-isometric stabilized action (attack the wall head-on), accepting this is theory-COMPLETION,
  not derivation from GU.

That is the located-vs-forced question, now a METHOD choice: rigorously locate (torsion invariant) vs
force by completion (non-isometric BV action).

## Recommended method

Run the **e-invariant / Z/24 route first**: it is the only method that (a) natively carries the 3,
(b) is cheap and decisive, and (c) tells you whether the expensive completion route is even needed.

> Build a **families framed-bordism invariant over the compact-reduced K3 fiber, computed in Z/24 via
> the Adams e-invariant of the RS boundary framing -- firewall on (no chi-import) -- cross-checked by
> exact-CAS characteristic classes (#3) and stress-tested by the adversarial 2-primary-collapse
> theorem (#16).**

Two independent lenses (16 red-team, 17 CRT) predict the likely outcome: the invariant lands in the
`Z/8` summand or gives a `Z/3` class with no integer image -- i.e. it CONFIRMS located-not-forced,
rigorously, at the families level, far more cheaply than building the BV action. The non-isometric BV
action (9) is the correct SECOND move, reserved for the single outcome (`N != 0 mod 3` honest) that
would demand it.

**Decisive first computation:** the reduced eta / e-invariant of the RS boundary over a one-parameter
K3 family, read as a `Z/24` class -- three decisive outcomes (Z/3-part lifts to integer => forcing on
the table; lands in Z/8 => 2-primary; Z/3 class with no integer image => located, provably not forced).
Spun out and run in `canon/families-e-invariant-order3-monodromy-RESULTS.md`.

## Boundary

Generation only. No number is fitted here; no verdict, canon, or public posture moves. The recommended
method's firewall (`N != 0 mod 3` WITHOUT `chi=24`, `/8`, `A-hat=3`, or `contractible => 1`) is
inherited verbatim from `absorbed/gu-source-action/DEAD-ENDS.md`. Pauses for Joe on any promotion.
