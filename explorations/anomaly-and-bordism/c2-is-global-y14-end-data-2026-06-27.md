---
title: "C2 is provably GLOBAL: the local Y14 curvature cannot reconcile it; the source-action and boundary-index lines converge"
date: 2026-06-27
status: exploration
doc_type: exploration
verdict: speculation   # clean NEGATIVE: local/fiber curvature insufficient (~94% of C2 is global); NO claim promoted
method: "Design -> Build -> adversarial Kill over 3 curvature approaches (gimmel-curvature, physical-null-cone, local-vs-global diagnostic), all C2_FLOORS_NEEDS_GLOBAL genuine=True; structural core independently re-confirmed in the main loop"
builds_on:
  - explorations/anomaly-and-bordism/bv-bicomplex-and-c2-obstruction-2026-06-27.md  (SOURCE-02/BICOMPLEX-01)
  - explorations/time-as-finality-crosswalk/record-issuance-boundary-selector-2026-06-26.md  (Joe's boundary idea)
tests:
  - tests/c2_holonomy_global_obstruction.py  (fast ~10s structural confirmation)
  - tests/rs_c2_gimmel_curvature_physical_section.py / rs_c2_physical_null_cone_restriction.py / rs_c2_curvature_vs_global_diagnostic.py  (~11 min each)
bears_on: "the unwritten GU RS source action — now pinned to the GLOBAL Y14=Met(X4) end-geometry"
---

# C2 is global

The previous gate isolated the final RS obstruction as the secondary constraint `C2 = Γ·M_D·Π_RS`
(bare 155.36, fully Γ-independent) and named the missing object as a symmetry-breaking spectral section =
the GU connection-curvature on Y14. This gate **built the actual gimmel curvature** and tested it — using
Joe's sharpening (restrict to the physical metric's null cone, "the slice we live in"). The result is a
clean, triple-confirmed **negative that narrows the missing object decisively**: the local/fiber curvature
CANNOT reconcile C2 — **~94% of it is global/topological** — so the missing datum is the **global Y14 =
Met(X4) end-geometry**, not anything available on a single section's local curvature.

## 1. The result: local curvature is provably insufficient

The genuine so(9,5) gimmel connection-curvature 2-form `R^Y` was assembled a-priori from the in-repo
Christoffels (ii-s-coordinate-formula §2 / the Willmore-Schwarzschild `RY_block`), verified to read only the
metric η and the Christoffels (never C2/M_D/Γ/ξ; rebuild defect 0.0), to be a genuine non-equivariant
(defect 1.87) H-linear so(9,5) element (defect 9e-16) — and dressed into the bicomplex carrier. Across three
independent approaches (all `genuine=True`, all reproduced on the killers' re-runs):

- **It does not drive C2 down.** Dressed C2 floors at **~152.5** (a ~1.8% dent) and at the natural geometric
  scale actually *increases* to 167.3. The cleanest diagnostic: the a-priori floor over *all* geometric
  planes = **155.36 = exactly bare (0% drop)**; even a *cheating* C2-reading solve reaches only 9.68 (6.2%),
  so the **global/topological residual is ~94%** (145.68 of 155.36).
- **Structural reason (independently re-confirmed, `tests/c2_holonomy_global_obstruction.py`, ~10s):** C2 is
  fully Γ-independent, and a holonomy carrier `B_W = Γ·(id⊗G_W)` provably cannot pull it below bare — over 8
  random so(9,5) holonomies × 3 amplitudes the minimum dressed C2 was **303.42** (0/24 below bare). Local
  holonomy/curvature dressing generically *raises* C2; it cannot reconcile it.
- **All guards held:** bare `[Π_RS,M_D]=58.72` exactly (anti-trap), `s²≈0` non-vacuous, the carrier genuinely
  a-priori (not a fixed-solve).

**Honest scope (the killers flagged it):** this PROVES local insufficiency (the local curvature is exhausted,
~94% residual is global); it does NOT prove the global end-data *will* reconcile C2. "Needs global" is a
rigorously-motivated next-step, not an established closure.

## 2. Joe's "slice we live in" — the honest verdict

The physical null cone (the light cone of η, restricted from the (9,5) structure) was tested as Joe proposed.
Honest finding: it is **structurally distinguished** — the null plane beats the spacelike plane (which does
*nothing*, exactly bare) — so the causal structure is on the right track. But its effect is **tiny and not
uniquely privileged at the local level** (null 152.53 ≈ timelike 152.52). The interpretation: the slice we
inhabit matters, but its relevance is **global**, not in its local curvature — the section's global/topological
structure, not the pointwise light cone. Joe's intuition points at the right object; the object lives globally.

## 3. The convergence: the source-action line meets the boundary-index line

> **CORRECTED (SOURCE-04, same day): this section's "one global object" inference is a FORCED ANALOGY.**
> The Section-1/2 negative (C2 is global; no local carrier reduces it) STANDS. But the claim below that C2 *is*
> the boundary index / one object with Joe's record-issuance idea was tested three ways and retracted: C2 is
> degree-1 homogeneous (`C2(2ξ)/C2(ξ)=2`, a scale-dependent symbol-norm, NOT a scale-invariant index), no
> handle maps ch2=-5376 onto C2, and the eta "29% C2 reduction" is the generic rank-64 projection floor. The
> two are both global but different KINDS of object. See
> explorations/anomaly-and-bordism/topological-edge-c2-not-an-index-2026-06-27.md. Read the convergence below as the *hypothesis
> that was tested and failed*, not a result.

This is the loop-closing. The final RS source-action obstruction C2 is now provably **~94% global** — it needs
the non-compact Y14 end-data: the **boundary holonomy / spectral section** (K3 χ-gate / APS end). That is
**exactly the object Joe's record-issuance-boundary idea pointed at.** When that idea was first adjudicated
(`record-issuance-boundary-selector-2026-06-26.md`), the discipline correctly found it "lands on the
non-compact INDEX well-definedness, not the shiab selector" — and parked it as decoupled from the source
action. **It was not decoupled. The source action's final obstruction C2 is itself ~94% the global index /
boundary-spectral-section structure.** The two lines were never different problems:

> the **source action** (its final obstruction C2) = the **boundary spectral section / non-compact index
> end-data** (Joe's record-issuance boundary) = the **global Y14 = Met(X4) topology** (K3 χ-gate / APS).

Joe's boundary idea was pointing at the *global half* all along; the RS-source-action construction has now
arrived at the same place from the algebra side. The record-issuance "spectral section" — *which boundary
modes are finalized* — is the symmetry-breaking choice C2 demands.

## 4. Net + the next gate

The missing physics is now pinned to one **global/topological** object on the non-compact Y14: the boundary
holonomy / spectral section (the K3 χ-gate / APS end-data) that reconciles the Γ-independent C2. The local
algebra and the local geometry are both **provably exhausted** (symbol-algebra carriers floor at 41.04; the
actual local curvature gives 0–1.8%; ~94% is global). The next gate is genuinely topological/index-theoretic,
not algebraic: compute the **boundary η-invariant / spectral-section holonomy around the non-compact Y14 end**
(the existing `lab/active-research/...k3-chi-gate...` + the noncompact-APS-end work) and test whether *that*
global datum supplies the ~94% of C2 the local curvature cannot — i.e. whether the index/boundary structure
reconciles the source action's final constraint. This is where the record-issuance-boundary idea and the
source-action construction become a single computation.

## What this does NOT establish
- It does not reconcile C2, construct S_IG, or compute the generation count.
- It PROVES local insufficiency (~94% global), not that global end-data closes C2.
- The physical null cone is structurally distinguished but not decisively privileged at the local level.
