---
title: "The GU source action: necessary-conditions box, the two-level escape, and why the obstruction is causality-required"
date: 2026-06-27
status: exploration
doc_type: exploration
verdict: speculation   # keystone run: tightest box + named obstruction + a proposed unification; NO claim promoted
method: "keystone workflow (Constrain -> Survey -> Attempt -> adversarial Kill); minimal no-ghost candidate built + tested on the explicit Cl(9,5) rep, killed 3 ways; computation independently re-run in the main loop"
computable_anchor: explorations/rs_source_candidate_projected_differential_scratch.py  (reproduces 343.73, 58.72, 215.85; new facts 1.6e-14->169.19, t*=-1/6)
bears_on:
  - the unwritten GU RS/IG SOURCE ACTION (root blocker: shiab selector + generation count + RS-BRST + dark-energy)
  - Velo-Zwanziger no-go (canon/no-go-class-relative-map.md)
---

# The GU source action — what the keystone run pinned down

The source action stays unwritten (as expected: it is genuine missing physics, not a formalization gap).
But the keystone run did three real things: it **boxed** the action in precise operator conditions, it
**proved on the explicit rep** that a ghost outside the equivariant family is mandatory, and it surfaced a
**unification** — the central obstruction is not a defect to remove; it is *required for causality*.

## 1. The headline: the obstruction `[Π_RS, M_D] ≠ 0` is causality-required

The "clean, no-ghost" stabilization of the RS sector would require **CONSTRAINT-PRESERVATION**:
`Γ · d_RS,-1 = 0`, equivalently `[Π_RS, M_D] = 0` (the γ-trace constraint projector commutes with the
twisted Dirac symbol). The repo already proved the operator identity
`[Π_RS, M] = 0  ⟺  M preserves ker(Γ)  ⟺  ker(Γ) is an M-invariant (block-diagonal) sub-module`
(`shiab-codiff-obstruction-commutator-2026-06-26.md`). So `[Π_RS, M_D] = 0` means the RS sector
**decouples** — it propagates as a *standalone* γ-traceless module, not mixing with the spin-1/2 sector.

But that is **exactly the configuration GU's Velo-Zwanziger evasion forbids.** From
`canon/no-go-class-relative-map.md`: GU evades VZ precisely because *"RS does not decouple into a standalone
field"* (F6, CONDITIONALLY_RESOLVED, line 365), and *"the minimal-coupling functor forgets the
Clifford-module embedding R⊂E (the B/C datum) and treats R as a standalone matter field; the VZ class is
image(φ_mc), and GU lies in the domain but not the image"* (line 377). The VZ no-go's hypothesis VZ-H1 is a
**standalone** RS Lagrangian with an externally-imposed γ-trace condition.

Chaining these:
> **`[Π_RS, M_D] = 0` (clean no-ghost quotient)  ⟺  ker(Γ) dynamics-invariant  ⟺  RS decoupled / standalone
> ⟹ GU enters the VZ class (image φ_mc) ⟹ Velo-Zwanziger acausality (GU has no guardian).**

So the machine-measured obstruction `‖[Π_RS, M_D]‖ = 58.72 ≠ 0` is **not a bug to fix** — it is the
non-decoupling (the B/C Dirac-DeRham embedding) that *keeps GU causal*. A clean ghost-free RS subspace would
be acausal. **This unifies two previously-separate open problems: the RS-BRST stabilization gap and the
Velo-Zwanziger no-go are the same constraint** — the ghost is mandatory because the alternative is acausal.

> **Status: a strong STRUCTURAL ARGUMENT, not a proven theorem.** The load-bearing step is the identification
> `[Π_RS,M_D]=0  ⟺  RS standalone (VZ-H1)`. Its two premises are both in-repo (the shiab-codiff operator
> identity + the VZ-row non-decoupling evasion), and they were produced *adversarially* (by killers trying to
> refute the candidate, not to build this claim). It should be independently checked at the level of VZ
> characteristics before promotion. The standard VZ pathology (constraint–propagator inconsistency under
> minimal coupling, §2.5 line 311) is a *downstream* property of the standalone field, distinct from
> `[Π_RS,M_D]` itself; the bridge is decoupling, not that one commutator.

## 2. The in-rep proof that the ghost must be non-equivariant (the two-level escape)

The minimal no-ghost candidate `d_RS,-1^phys := Π_RS ∘ d_A` (the orthogonal-projector / penalty form) was
built to satisfy CONSTRAINT-PRESERVATION and tested on the verified Cl(9,5)=M(64,H) rep
(`rs_source_candidate_projected_differential_scratch.py`, re-run in the main loop, all anchors reproduced):

- It annihilates the obstruction **at gradient level**: `‖Γ · Π_RS d_A(gauge)‖ = 1.6e-14 ≈ 0`
  (vs naive `80.61`). **But this is a tautology** (`Γ·Π_RS ≡ 0` for *any* operator post-composed with
  `Π_RS`) — zero physical content, as the consistency killer flagged.
- **The escape reappears one level up**: `‖[Π_RS, M_D]‖ = 58.72 ≠ 0` and
  `‖(I−Π_RS) M_D Π_RS(gauge)‖ = 169.19 ≠ 0`. The Dirac symbol carries the projected gauge mode straight
  back off ker(Γ). So **projection alone never closes the complex** — and since `Π_RS ∘ d_A` is a composite
  of two Spin(9,5)-equivariant maps, it lies in the exact equivariant class SHIAB-04 proved cannot close
  (closure-Gram eigenvalues O(1e5–1e6), no null direction). **The compensating ghost symbol `σ_c(ξ)` must
  live OUTSIDE the equivariant family**, and the candidate localizes precisely where it must act: the
  `[Π_RS, M_D] = 58.72` mixing.
- H-linearity holds exactly (`‖J²+I‖ = ‖[J,Cl]‖ = ‖Π_RS J − J·conj(Π_RS)‖ = 0`), so rank_H stays well-defined.

**New exact fact (RT-TRACE-DICHOTOMY, computed):** canon shiab `(1,0,1,0)` is γ-traceFUL
(`‖Γ·shiab_contract‖ = 215.85 ≠ 0`); the **unique** γ-traceless (constraint-preserving) coupling is
`contract + t·wedge` with `t* = −1/6` (residual `0.0` to machine precision), i.e. proportional to
`wedge − 6·contract` — **not** `(1,0,1,0)`. So **constraint-preservation and GU's written canon shiab are
jointly unsatisfiable**: any constraint-preserving source action must *revise* the `(1,0,1,0)` formula. (This
is consistent with, and sharpens, the earlier γ-trace selector result.)

## 3. The pinned SHAPE of the missing object

The three independent kills (all refuted the candidate, by design — `survives = 0`) converge on one
specification. A valid GU RS/IG source action must be:

- a **BV action `S_IG^susy`** satisfying the classical master equation `(S,S) = 0` (≡ BRST nilpotency `s²=0`),
- whose off-shell **Noether-second-theorem identity** `δ₂ ∘ d_RS,-1 = 0` (i.e. `D_A^* E_RS = 0`) *forces*
  the physical projector as a derived consequence of a genuine gauge invariance — rather than imposing
  `Π_RS` by hand (the candidate's fatal non-canonicity),
- with the γ-trace constraint realized **cohomologically** (the off-surface escape `(I−Π_RS)(M_D+σ_c)Π_RS`
  is *ghost-exact*, via a **non-equivariant** compensator `σ_c(ξ)`), not as a clean ker(Γ) subspace,
- carrying a **Velo-Zwanziger guardian** (a local-SUSY / super-IG completion) so VZ stays evaded *while the
  constraints propagate* — which §1 shows is the same requirement.

## 4. Survey verdict: only one candidate mechanism, and it is unconstructed

No known higher-spin mechanism supplies `S_IG` from GU's stated data:
- **Fang–Fronsdal** gives only the kinetic+gauge skeleton (= `d_RS,-1`) and is destabilized the instant it is
  coupled to Sp(64) or Y14 curvature — the field-theory shadow of `[Π_RS, c·d*] ≠ 0` (the 73.48/343.73 object).
- **Stueckelberg/BRST** supplies the *ghost machinery* (nilpotent `s`, the `q = 1−a` count, `Π_RS^phys` as
  BRST cohomology) but not the GU-specific datum that fixes the slice or `q` — and GU is constitutionally
  anti-gauge-fixing.
- **Vasiliev** is machine-shown genuinely distinct and non-absorbing: `hs(λ)` has no `M(64,H)` truncation and
  needs AdS / Λ<0 that GU lacks.
- **The only mechanism** that consistently couples spin-3/2 to gauge+gravity with finite field content, could
  close *both* VZ and Johnson–Sudarshan, *and* emit the data the BRST/rank chain needs (`d_RS,-1`, the slice,
  `q`, hence `Π_RS^phys`) is a **local-SUSY / super-IG guardian** — exactly Weinstein's author-disclaimed
  ("Caveat Emptor") super-inhomogeneous-gauge direction. It is unconstructed.

## 5. Net

The source action is still unwritten, but it is no longer a black box: its **shape is pinned** (a
non-equivariant BV ghost from a local-SUSY completion, with the γ-trace constraint cohomological), its
**single most decisive missing piece is named** (the compensator `σ_c(ξ)` outside the equivariant family +
the master-equation certificate), and the central obstruction has a **physical reason to exist** (causality).
The next concrete move toward it is to *construct a candidate non-equivariant `σ_c(ξ)`* and test
`(I−Π_RS)(M_D+σ_c)Π_RS = 0` with `s² = 0` on the explicit rep — the first genuinely new degree of freedom the
whole selector hunt has been unable to reach from inside the equivariant family.

## What this does NOT establish
- It does not construct `S_IG^susy`, the ghost count `q`, or make `rank_H(Π_RS·E_+·Π_RS)` computable.
- The §1 VZ-causality unification is a structural argument pending an independent VZ-characteristic check.
- The generation count, anomaly global leg, and dark-energy structural leg all remain gated on this object.
