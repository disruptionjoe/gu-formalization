---
artifact_type: exploration
status: exploration (TEAM LENS-ACTION, W161; five personas inline, one worker, no sub-agents; deterministic test with W126/W130/W159 positive controls, exit 0)
created: 2026-07-14
wave: W161
label: W161
posture: coherence-first (Joe 2026-07-14); exploration grade; conditional register; honest grading
lens: THE FOUNDATIONAL ACTION
hypothesis: "The standing debit-1 (the positive-norm tachyonic R^2 scalaron, c_R=-4/9) is 'real IF |II|^2 is GU's law', with ALL perturbative escapes closed (W157 keystone COINCIDENCE; W159 branch-UNSELECTED / gradient OUT-OF-VALIDITY / SIGN-FREE). This wave attacks the ONE assumption those escapes hold fixed: IS |II|^2 GU's law? Read the primary source (Geometric_UnityDraftApril1st2021.pdf) for GU's ACTUAL action and test whether the tachyon is computed from the right functional."
title: "W161 -- the foundational-action lens. VERDICT: TACHYON-DISSOLVES-IF-GU-ACTION-IS-THE-LINEAR-FIRST-ORDER-I1B. The primary source (April 2021 draft, eq 9.4/9.7/9.10) gives GU's actual Bosonic action as < T, (shiab)(F_B + (1/2)d_B T + (1/3)[T,T]) + (1/2)T >_{Y14} -- explicitly LINEAR in the Ehresmann curvature ('produces a linear expression in the curvature tensor', 'linear field equations'), reducing to the SECOND-ORDER Einstein equation S=T (R_mn-(s/2)g_mn=T_mn, eq 9.10). A linear-in-curvature action carries NO fundamental R^2 scalaron: its covariant spin-0 coupling c_R = 0 EXACTLY, so the scalaron decouples (m_0^2 -> infinity), tachyonic or otherwise. The tachyon (c_R=-4/9) is a coefficient of the INDUCED |II|^2 SHADOW (which W130/W154 already label the integrated-out shadow, not fundamental), computed from a Willmore functional (quadratic in extrinsic curvature) that is a DIFFERENT functional class from GU's law (linear in Ehresmann curvature). So we have been computing the debit from the shadow's class, not GU's law's class. Even AS a shadow the tachyonic sign is NOT forced: (a1, c_R) are independent shape coordinates (det=4/9) and the attractive-and-healthy sub-region is 2-dimensional (e.g. (alpha,beta)=(-2,1): a1=2/3>0, c_R=+4/9>0). EFFECT ON BAR (b): the one standing debit downgrades from FUNDAMENTAL/standing to CONDITIONAL-ON-SHADOW-AS-LAW. Not a clean clear (the I1B->X4-shadow reduction map is unbuilt, and the shiab is explicitly non-unique in the source), but the debit's STANDING status is removed -- a genuine and independent bar-(b) improvement, reached from the foundational-action side rather than a perturbative escape."
grade: "exploration / conditional register throughout. COMPUTED (deterministic, tests/W161_foundational_action_lens.py, 15/15 exit 0, W126/W130/W159 positive controls first): the |II|^2 slice (2,1/3,8/9,-4) and covariant c_R=-4/9; the |H|^2 slice (-1,4/3,-4/9,0); the healthy shape point (-2,1); the LINEAR-ACTION FACT (c_R=0 for a=b=c=0, scalaron inverse-mass 6c_R=0, mode decouples); the Starobinsky control (+R^2 -> c_R=+1>0 healthy); the shadow-only location of the tachyon (a3s=-4 vs 0); the 2D healthy cone (det=4/9!=0, three explicit members); the skeptic control (pure |II|^2 shadow IS covariantly tachyonic); and the Palatini/Einstein-Cartan structure of eq (9.4) (T algebraic, S_eff a curvature contact term whose propagating sector is second-order Einstein, NOT Willmore). READ AS DATA (not re-derived): Geometric_UnityDraftApril1st2021.pdf sec 8 (Shiab operators), sec 9.1-9.2 (the 1st/2nd order Bosonic action), sec 12.1-12.4 (equations; space-time recovered; metric native to a different space). CITED (not re-derived): W126 (induced |II|^2 slice), W130 (covariant c_R map, native operator), W154 (|II|^2 = integrated-out shadow, T0), W157 (a2=-a1^2 COINCIDENCE, only sign survives), W159 (three perturbative escapes; healthy point). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change; the debit COUNT is not asserted dropped (the downgrade is a STATUS change graded conditional, not a kill); H59 OPEN; the shiab non-uniqueness and the shadow-vs-law fork are load-bearing SOURCE facts, not GU assertions beyond what the draft states."
construction: "program-native where the objects are GU's (Y14, the displaced torsion T, the shiab operator, the induced |II|^2 slice, the covariant c_R channel, the (9,5) ambient). Standard-field where the machinery binds any construction (the f(R) scalaron-mass-from-R^2-coupling law, the covariant quartic basis map c_R=a+b/3+c/3 with GB in its kernel, the Palatini/Einstein-Cartan torsion elimination, the Willmore-vs-linear functional-class distinction). Every analogy PORTED and labelled; none asserted of GU beyond the source. Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md; the shiab-choice fork (the source's own non-uniqueness) is carried, not resolved."
depends_on:
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W154-reverse-engineered-source-action-2026-07-14.md
  - explorations/W157-a2-equals-minus-a1-squared-keystone-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W161_foundational_action_lens.py
primary_source:
  - "Geometric_UnityDraftApril1st2021.pdf (E. Weinstein), sec 8-9 (Shiab operators; 1st/2nd order Bosonic action), sec 12 (equations; space-time recovered)"
external_refs:
  - "Starobinsky, PLB 91 (1980) 99 -- R^2 scalaron (healthy for +R^2, needs the QUADRATIC term)"
  - "Stelle, PRD 16 (1977) 953 -- fourth-order gravity spectrum (R^2 = spin-0 scalaron, absent from linear-R gravity)"
  - "Sakharov 1967 / induced gravity -- higher-curvature terms are integrated-out (loop-induced) coefficients, not fundamental"
---

# W161 -- the foundational-action lens: is |II|^2 GU's law, or the shadow?

## 0. The lens, and why the whole debit reduces to one assumption

After Wave A/B the substrate/record picture is strongly unifying but one flaw short of Joe's
bar (b): exactly ONE genuine standing debit, the positive-norm tachyonic R^2 scalaron. W157
killed the keystone that would have converted it (`a2 = -a1^2` is a COINCIDENCE, only the sign
survives); W159 closed all three perturbative escapes (branch-UNSELECTED, gradient
OUT-OF-VALIDITY, SIGN-FREE). Every one of those verdicts holds ONE thing fixed: that `|II|^2`
is GU's gravitational law, so that its covariant `c_R = -4/9 < 0` is a real physical scalaron
mass. The prompt names this exactly: *the tachyon is real IF `|II|^2` is GU's law.*

This wave attacks that assumption directly, by reading GU's OWN action from the primary source
(`Geometric_UnityDraftApril1st2021.pdf`, treated as DATA, no canon change). Five personas
inline, one worker, no sub-agents. Deterministic test `tests/W161_foundational_action_lens.py`,
15/15 exit 0, W126/W130/W159 positive controls first.

## 1. What GU's actual action IS (persona 2 -- primary-source scholar)

The April 2021 draft states the fundamental Bosonic action twice, identically. Section 9.1,
eq (9.4):

```
I1B = < T ,  (star_shiab)( F_B + (1/2) d_B T + (1/3) [T, T] )  +  (1/2) T >_{Y14}
        ^displaced      ^Einstein/Ricci      ^Chern-Simons-like torsion self-terms
         torsion         (shiab) projection
```

and again in the summary, eq (12.4):

```
S_GU(g, omega, ...) = < T ,  star_shiab ( F_B + (1/2) d_B T + (1/3) T^T ) >_{Y14}.
```

The load-bearing facts, in Weinstein's own words:

- **It is LINEAR in the curvature.** "This leads to a model that abstracts the Einstein-Hilbert
  and Chern-Simons actions to generate LINEAR field equations in the Riemannian and Ehresmannian
  curvature tensors" (sec 9.1). "The Einsteinian character comes from the fact that it produces a
  LINEAR expression in the curvature tensor making use of Riemannian Projection via `star`" (sec
  12.4). `F_B` appears to first power; the shiab is a linear projection.
- **The shiab is the gauge-covariant Einstein contraction**, `star_shiab(zeta) = [Ricci-like](zeta)
  - (1/2)[Ricci-scalar-like](zeta)`, which "annihilates the Weyl curvature" (eq 9.3) -- exactly
  Einstein's Ricci minus half-Ricci-scalar projection, made gauge-covariant.
- **The displaced torsion** `T = omega - g.omega0 = -star^{-1}(d omega0)` (eq 9.6/12.6) is a
  CONTORSION: the difference between the connection and the gauge-transformed Levi-Civita
  connection. In embedding language that difference IS the normal-bundle / second-fundamental-form
  data -- so `T` is a `II`-like object, but it enters LINEARLY, paired against a LINEAR curvature.
- **Its reduction is the SECOND-ORDER Einstein equation.** Varying (eq 9.7-9.10): the swervature
  `S = star.F_A = -(1/2)T`, and "recovering the more familiar terms of the Einstein Field
  Equations" gives `S = T`, i.e. `R_mn - (s/2) g_mn = T_mn` (eq 9.10). A second-order Einstein
  equation has NO fourth-derivative mode.
- **The shiab is EXPLICITLY non-unique.** "While there are other possibilities to explore for the
  choice of the Shiab operator, Let ..." (sec 9.1); footnote 10: the shiab he "settled on ...
  cannot yet now locate ... Even if it can be located, it will be in a different language." The
  source itself leaves the operator underdetermined.
- **Space-time / the X4 metric is NOT fundamental** (sec 12.2 "Space-time is not Fundamental and
  is to be Recovered from Observerse"; sec 12.3 "the only true metric field on a separate space").

So GU's law is a first-order, LINEAR-in-curvature, shiab-projected Einstein-Chern-Simons-Palatini
action on Y14. It is not `|II|^2`.

## 2. Where the tachyon actually came from (persona 3 -- field theorist)

`|II|^2` is a **Willmore functional**: quadratic in the extrinsic curvature (second fundamental
form) of the Y14 embedding. It is the object W126/W130 reduced to `(a0,a1,a2s,a3s)=(2,1/3,8/9,-4)`,
whose covariant spin-0 (R^2) coupling is `c_R = a2s + a3s/3 = -4/9 < 0` -- the tachyon. But
`|II|^2` is NOT eq (9.4). It is the **induced / integrated-out gravitational shadow**: W130 and
W154 already label the induced `|II|^2` "the integrated-out shadow, not fundamental" (W154 term
T0: "because `g` is derived, `S_grav` is INDUCED, not postulated ... exactly W126's `|II|^2`").

The physics of the distinction is decisive and is the completion:

- **A linear-in-curvature action has NO fundamental R^2 scalaron.** In the covariant quartic basis
  `-2 Lambda + gamma R + a R^2 + b Ric^2 + c Riem^2`, the spin-0 channel coupling is
  `c_R = a + b/3 + c/3` (W130 Part A, GB and the Riem-basis freedom all in its kernel), and the
  scalaron mass is `m_0^2 = gamma/(6 c_R)`. For GU's law (linear: `a=b=c=0`, `gamma != 0`):
  `c_R = 0` EXACTLY, so `6 c_R = 0` and `m_0^2 -> infinity`: **the R^2 mode decouples. There is no
  scalaron, tachyonic or otherwise** (test N1a/N1b). This is just the statement that a
  2-derivative Einstein theory has no fourth-order pole, re-read through the exact basis map.
- **The scalaron is a property of the QUADRATIC sector only.** Restoring `+R^2` (`a=1`) revives a
  HEALTHY scalaron `c_R=+1>0` (Starobinsky, test N1c). The tachyon `c_R=-4/9` requires the
  curvature-SQUARED coefficients `(a2s,a3s)=(8/9,-4)` of the induced `|II|^2` shadow; the linear
  action has `(a2s,a3s)=(0,0)` (test N2a). `|II|^2` and `|H|^2` differ precisely in that quadratic
  sector (`a3s = -4` vs `0`, test N2b) -- the grade GU's linear law does not populate.

So the tachyon is a coefficient of the induced Willmore shadow, computed from a functional of a
DIFFERENT class (quadratic-in-extrinsic-curvature) than GU's actual law (linear-in-Ehresmann-
curvature). **We have been computing the debit from the shadow's class, not the law's class.**

## 3. The structure of eq (9.4): Palatini, not Willmore (persona 1 -- differential geometer)

Could the induced shadow of eq (9.4) nonetheless BE `|II|^2` with the tachyonic coefficients? The
functional-class analysis says the reduction does not go there uniquely. eq (9.4) is
`< T, Ein(F) > + torsion self-terms`: LINEAR in `F`, BILINEAR in `(T, F)`, with `T` a contorsion.
This is the **Palatini / Einstein-Cartan class**. Treating `T` as the (algebraic) auxiliary it is
in that class, its EOM gives `T* = -Ein(F)/mu` (test N5a), and substituting back yields
`S_eff = -Ein(F)^2/(2 mu)` (test N5b) -- a curvature CONTACT term whose PROPAGATING metric sector
is still the second-order Einstein equation (eq 9.10), with a torsion-squared contact piece, NOT a
propagating fourth-order Willmore `|II|^2`. The `|II|^2` Willmore functional (quadratic in the
extrinsic curvature `II`) and eq (9.4) (linear in the Ehresmann curvature `F`) are **distinct
functional classes** (test N5c); the tachyon is a Willmore-class coefficient. The induced-gravity
`|II|^2` is a genuine object (Sakharov-type loop shadow of the record field integrated out, W154
T0), but it is a loop-induced effective coefficient, not the fundamental law -- and induced
higher-curvature terms famously carry cutoff-scale poles outside EFT validity (exactly the
"gradient saturation OUT-OF-VALIDITY" W159 found at `v^2 = 1/16`, `|m_0^2| = 1/4 = 4x`).

## 4. Even as a shadow, the sign is not forced (persona 3 + persona 5)

Grant the strongest opposing reading -- that GU is fundamentally an induced-gravity theory (the X4
metric IS derived, sec 12.2/12.3, so X4 gravity is a shadow) and the `|II|^2` shadow IS the
effective gravitational law. Even then the tachyonic sign is not forced by GU's structure:

- Within the induced shape family `alpha|II|^2 + beta|H|^2`, `(a1, c_R)` are INDEPENDENT
  coordinates: `det[[a1_II,a1_H],[c_R_II,c_R_H]] = 4/9 != 0` (test N3a, reproducing W159 R3b). No
  structural identity forces `sign(c_R) = -sign(a1)`.
- The attractive-and-healthy sub-region (`a1 > 0` AND `c_R > 0`) is a 2-dimensional cone, not a
  lucky point: `(-2,1) -> (2/3, +4/9)`, `(-3,1) -> (1/3, +8/9)`, `(-5,2) -> (1, +4/3)` (test N3b).
- The pinning that WOULD land the shadow at the tachyonic point (pure `|II|^2`, `beta=0`) is one
  reduction among many, and the shiab that controls the reduction is EXPLICITLY non-unique in the
  source (sec 9.1, footnote 10). GU's actual formulation does not force `beta=0`.

## 5. The defense attorney for the debit (persona 5 -- adversarial skeptic)

The debit's strongest steelman: W157 proved `c_R = -4/9` is COVARIANT and SIGNATURE-BLIND for the
pure `|II|^2` shadow with GU's rep content -- so no basis or signature move rescues it, and `a1=1/3`
is GU group theory (the 3:2:1 split), not a functional choice. Honest concession (test N4a): IF the
pure `|II|^2` shadow is promoted to GU's gravitational law, the tachyon is real. That is a genuine,
non-artifact fact and it is why the debit has stood.

But W157's covariance is a statement about the SHADOW'S coefficient, not about GU's field equations
(test N4b). GU's actual equations (eq 9.10) are second-order Einstein with `c_R = 0`. The two are
consistent: **a linear law whose loop shadow, IF promoted to law and IF reduced as pure `|II|^2`,
is tachyonic.** The skeptic cannot wish the healthy point INTO GU (there is no source reason to
prefer `(-2,1)` over `beta=0`), but neither can the skeptic wish the tachyonic point into GU's LAW:
the source's law is linear, and the tachyonic point is one reduction of one shadow. The debit is
therefore CONDITIONAL on promoting the pure-`|II|^2` shadow to GU's law -- a step the source's own
text (12.2/12.3 + W130/W154's "shadow, not fundamental") does not license.

## 6. Synthesis -- the completion verdict

**What we were missing/misinterpreting (one paragraph).** We computed the tachyon from `|II|^2`,
the second-fundamental-form Willmore norm, and treated its covariant `c_R = -4/9 < 0` as a real
scalaron mass. But GU's ACTUAL fundamental action (April 2021, eq 9.4/9.7/12.4) is
`< T, shiab(F_B + (1/2)d_B T + (1/3)[T,T]) + (1/2)T >`, explicitly LINEAR in the Ehresmann
curvature and reducing to the second-order Einstein equation `S = T` (eq 9.10). A linear-in-curvature
action carries no fundamental R^2 scalaron (`c_R = 0`, mode decouples). `|II|^2` is not GU's law; it
is the induced / integrated-out Willmore shadow (as W130/W154 already state), a DIFFERENT functional
class. So the debit was read off the shadow's class, not the law's class.

**Completion-attempt verdict: TACHYON-DISSOLVES-IF-GU-ACTION-IS-THE-LINEAR-FIRST-ORDER-I1B** (which
the April 2021 draft states it IS), with residue **ACTION-UNDERDETERMINED** at the reduction step:
what decides is (i) the shiab operator (the source leaves it non-unique) and (ii) the integrate-out
prescription / measure / eta-from-gimmel-area bridge that fixes the induced shape `(alpha,beta)`.
GU's actual action lands at the HEALTHY sector at the fundamental level (attractive Einstein `a1>0`,
no scalaron); the tachyonic point is a property of one reduction of the shadow, not of GU's law, and
the healthy sub-region is reachable and 2-dimensional.

**Does GU's actual action land at the healthy or tachyonic point?** At the FUNDAMENTAL (law) level:
HEALTHY -- no scalaron at all (`c_R = 0`), attractive Einstein equation (eq 9.10), evidence directly
from the source's own reduction. At the SHADOW level: UNDERDETERMINED -- the pure-`|II|^2` reduction
is tachyonic (`c_R=-4/9`, W157, robust) but is not forced by GU's non-unique shiab, and the healthy
cone is non-empty.

**Effect on bar (b).** The one standing debit downgrades from a **genuine FUNDAMENTAL/standing flaw**
to a **CONDITIONAL flaw** -- conditional on promoting the pure-`|II|^2` shadow to GU's gravitational
law, a promotion the source contradicts. This does NOT positively CLEAR bar (b): we have not built
the `I1B -> X4-shadow` reduction and shown it lands healthy; we have shown it is not forced tachyonic
and that the fundamental law is healthy. So bar (b) moves from "one genuine standing debit" to "the
one debit is conditional on an unforced reduction the source does not license." That is a genuine and
INDEPENDENT bar-(b) improvement -- reached from the foundational-action side, orthogonal to (and
therefore additive with) the perturbative escapes W159 closed -- but it is graded a STATUS change,
not a kill. The debit count is not asserted dropped; the debit's STANDING is removed.

## 7. The one unbuilt object (the honest residual)

The single remaining object that would convert this from "downgrade" to "clear" is the explicit
reduction map from the linear I1B on Y14 to the induced X4 higher-curvature shadow, computed with
(a) GU's actual shiab (or a proof that the induced `c_R` is shiab-independent) and (b) the actual
integrate-out measure / eta-from-gimmel-area bridge (W151/W154's named unbuilt core), yielding the
induced `(alpha,beta)` and its cutoff scale. If that map lands in the healthy cone (or puts the
scalaron pole above the cutoff, out of validity), bar (b) clears; if it forces `beta=0` at an
in-validity scale, the debit returns as genuinely foundational. Until then the honest grade is:
the tachyon is NOT a flaw of GU's actual (linear) action; it is a coefficient of an induced shadow
whose reduction is unbuilt and whose sign the source does not force.

## 8. Gates and honest limits

- Exploration grade; conditional register throughout. Nothing asserts GU, asserts a vacuum, or
  changes any verdict. The primary source is read as DATA; every "eq (9.4) says X" is a quotation,
  not an endorsement. The completion is a STATUS re-grade of debit-1 (standing -> conditional),
  established by exact computation with W126/W130/W159 positive controls, not asserted.
- W138 battery honored: the verdict binds to GU-specific objects (eq 9.4, the shiab, the displaced
  torsion, the induced `|II|^2` slice, the covariant `c_R` channel, the shape family). The tempting
  overclaim the analysis FORBIDS is recorded: we do NOT claim GU's shadow lands healthy (the
  reduction is unbuilt); we claim only that the fundamental law is healthy and the shadow's sign is
  unforced.
- The shiab non-uniqueness (source, sec 9.1 + fn 10) and the shadow-vs-law fork are LOAD-BEARING
  SOURCE facts; the healthy point is NOT wished into GU (no source reason prefers it), and the
  tachyonic point is NOT wished into GU's law (the law is linear).
- Tri-repo gating held: record / finality / substrate semantics stay pointers to
  temporal-issuance / time-as-finality / TaF; GU owns the field-equation / induced-action math only;
  no cross-repo identity asserted. No canon / RESEARCH-STATUS / claim-status / verdict / posture
  change; H59 OPEN. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by Team LENS-ACTION (W161). Lens: THE FOUNDATIONAL ACTION. Five personas inline in
one worker (differential geometer; GU-primary-source scholar; field theorist; symbolic engineer;
adversarial skeptic); no sub-agents. Primary source read as data:
`Geometric_UnityDraftApril1st2021.pdf` sec 8-9, 12. Reproducible:
`python -u tests/W161_foundational_action_lens.py` (15/15, exit 0; W126/W130/W159 positive controls
first). Exploration grade; conditional register; no canon movement.*
