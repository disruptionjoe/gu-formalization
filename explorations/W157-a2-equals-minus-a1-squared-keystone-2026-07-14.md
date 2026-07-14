---
artifact_type: exploration
status: exploration (W157; TEAM KEYSTONE-A2; five personas inline, one worker, no sub-agents; deterministic keystone test with W126/W130 positive controls)
created: 2026-07-14
wave: W157
label: W157
posture: coherence-first (Joe 2026-07-14); exploration grade; conditional register; honest grading
title: "W157 -- THE KEYSTONE settled. Is a2 = -(a1)^2 (the tachyon = R^2-channel shadow of attractive gravity) STRUCTURAL or a COINCIDENCE? VERDICT: COINCIDENCE (MSS-slice-basis + a0=2 normalization artifact). COMPUTED, decisive: the identity holds ONLY for the MSS-slice-reduced coefficient a2_MSS = -1/9 (Ric^2 -> R^2/4); the PHYSICAL scalaron coefficient that actually sets the tachyon mass -- W130's covariant c_R = a2s + a3s/3 = -4/9 (Ric^2 -> R^2/3; GB topological; C^2 the spin-2 channel) -- BREAKS the identity by a factor of 4 (-4/9 != -(1/3)^2 = -1/9). The same theory in the correct covariant basis is the breaking family member. Confirmed by three more computed facts: (T2) the identity is not scale invariant -- for ANY tachyon (a2<0) the normalization N* = -a2/a1^2 makes it hold, so it is a convention available to every tachyon; (T3) in the shape family alpha|II|^2+beta|H|^2 it holds at beta=0 but FAILS at the other GU-named point beta/alpha=2; (T5) route iii yields no structural proof -- the conformal weight forces the degree-2 ceiling (c_3=c_4=..=0) but the relation <II_1,II_1>=-4<II_0,II_1>^2 is inhomogeneous (degree 2 = degree 4) so no weight law can force it. WHAT SURVIVES: only the SIGN a2/a1<0 (tachyonic iff attractive), normalization- and basis-invariant. CONSEQUENCE: the keystone conversion of debit-1 FAILS; the tachyon stays an independent debit; the convergent story (W156) does NOT clear bar (b) by this route; the load returns to the AF/AS fork (W128) and gradient saturation (W126)."
hypothesis: "W156 worklist item D1, the #1 keystone: W156 graded a2 = -(a1)^2 a STRUCTURAL-CANDIDATE (exact; scale-mode invariant per W153 T1; non-automatic) but not proven structural. Settle it with the W126/W130 exact machinery across the natural deformation families (signature/codimension; the alpha|II|^2+beta|H|^2 shape mix; the conformal-weight/homogeneity route; the factorization/roots route)."
grade: "exploration / conditional register throughout. COMPUTED (deterministic, tests/W157_a2_equals_minus_a1_squared_keystone.py, 19/19 exit 0, W126 + W130 positive controls first). The verdict COINCIDENCE is a DEMOTION of the W156 STRUCTURAL-CANDIDATE grade, established by exact sympy identities, not asserted. LOAD-BEARING imports (CITED, not re-derived): W126 (the slice decomposition (a0,a1,a2s,a3s)=(2,1/3,8/9,-4), the exact degree-2 collapse c_3=c_4=..=0, P(u)=-64u^2-8u+2, the |II|^2 and |H|^2 Route-1 machinery reused verbatim-parametrized); W130 (the covariant basis map c_R = a2s + a3s/3 = -4/9, the GB-freedom cancellation, f_0^2 = 1/(6 c_R), the physical scalaron sits on c_R not the slice value); W128 (the AF/AS fork); W156 (the STRUCTURAL-CANDIDATE grade now demoted). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change; the count is unchanged; H59/H61a OPEN; the E2 AF/AS fork carried, not closed. HONEST RESIDUAL: whether the surviving SIGN (c_R<0 forced by a1>0) is itself structural is NOT settled here -- it is the next question, and it is a WEAKER claim than the exact-magnitude keystone that W155/W156 personas 6/10 leaned on."
construction: "program-native where the objects are GU's (the induced |II|^2 action, the MSS conformal slice, the covariant R^2 / Weyl / GB channel split, the (9,5) ambient). Standard-field where the machinery binds any construction (the f(R) scalaron-mass dependence on the R^2 coupling, the 4D identity Ric^2 = C^2/2 + ... relating the slice /4 and covariant /3 reductions, conformal-weight homogeneity, the Gram-matrix reading of a quadratic form). Every analogy PORTED and labelled; none asserted of GU. Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md."
depends_on:
  - explorations/W126-beyond4th-vacuum-lift-2026-07-13.md
  - explorations/W130-native-graviton-oneloop-block-2026-07-14.md
  - explorations/W128-reuter-branch-scalaron-native-2026-07-14.md
  - explorations/W155-ten-divergent-personas-tachyon-2026-07-14.md
  - explorations/W156-coherent-full-story-2026-07-14.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W157_a2_equals_minus_a1_squared_keystone.py
external_refs:
  - "Starobinsky, PLB 91 (1980) 99 -- R^2 scalaron (healthy for +R^2)"
  - "Stelle, PRD 16 (1977) 953 -- fourth-order gravity spectrum (R^2 = spin-0, C^2 = spin-2)"
  - "De Felice & Tsujikawa, Living Rev. Rel. 13 (2010) 3 -- f(R) scalaron mass set by the R^2 coupling"
---

# W157 -- the keystone: is a2 = -(a1)^2 structural or a coincidence?

## 0. The keystone, and why the whole bar-(b) verdict reduces to it

W156 closed the substrate/record arc with a single hinge (its Section 2C): the convergent
full story is strongly unifying but carries three standing debits, and **exactly one
computation** stands between it and Joe's bar (b). That computation is this one. If
`a2 = -(a1)^2` is STRUCTURAL (forced by the `|II|^2` functional's structure, not GU's specific
numbers) then the tachyon is not an independent defect: it is the R^2-channel image of
ATTRACTIVE gravity, you cannot have `a1 > 0` without `a2 < 0`, and debit-1 converts from a
flaw into a now-understood consequence. That single conversion drops the flaw count by one
while preserving the unification, which clears bar (b) and plausibly bar (a). If it is a
COINCIDENCE, the tachyon stays an independent debit and the escape routes carry the load.

W156 graded it STRUCTURAL-CANDIDATE: exact (`-1/9 = -(1/3)^2`), scale-mode invariant (W153
T1, the conformal record-count mode), reducible to a clean coefficient relation
(`w2 = -w1^2` in `P(u) = -64u^2 - 8u + 2`), and non-automatic (a generic tachyonic `a2`
fails it) -- but NOT proven structural (no first-principles `|II|^2` symmetry or
family-invariance). This wave settles the grade.

**Five personas inline, one worker, no sub-agents.** Deterministic test
`tests/W157_a2_equals_minus_a1_squared_keystone.py`, 19/19 exit 0, W126 + W130 positive
controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| Gravity functional | induced `\|II\|^2` on the conformal family; W126 Route-1 machinery reused verbatim, parametrized by signature and shape-mix | The pinned construction; every coefficient below is the W126 object, not a re-derivation. |
| **Which R^2 coefficient is "a2"** | BOTH computed and distinguished: the MSS-slice value `a2_MSS = a2s + a3s/4 = -1/9` AND the covariant scalaron coupling `c_R = a2s + a3s/3 = -4/9` (W130) | This fork is the whole answer. The identity holds for the first and breaks for the second; the physical scalaron mass rides the second. |
| Shape mix | `alpha\|II\|^2 + beta\|H\|^2`, both from Route-1 | Route ii: is the identity preserved along the wave-35 family or pinned to `beta=0`? |
| Signature | base `eta` swept over (1,3),(0,4),(2,2),(4,0) | Route i: does the identity or the tachyon sign depend on the (9,5) indefiniteness? (Answer: neither -- signature-blind.) |
| Normalization | the `a0 = 2` flat-section pin vs a free overall `N` | The identity is not `N`-invariant; this is half the coincidence. |

## 2. Persona 1 -- differential geometer: the conformal weight cannot force it (route iii)

The cleanest possible "structural" proof would be a homogeneity/weight argument that fixes
`w2/w1^2 = -1` independent of the numbers. It does not exist, and here is exactly why.

The scale collapse (W126 result 1) makes `W = |II|^2` on the potential slice a function of the
single scale-covariant variable `sigma = e^{-2p} s` only. On the MSS slice `sigma = u eta`,
`W(u) = w0 + w1 u + w2 u^2`. The conformal weight of `|II|^2` forces the **degree-2 ceiling**:
`c_3 = c_4 = ... = 0` exactly (this is what W126 proved, and it is a genuine homogeneity
consequence -- `II` on this slice is affine in `sigma`, so `|II|^2` is quadratic). That is the
real structural content the weight delivers, and it is why the potential is exactly quadratic.

But the three coefficients are the three Gram scalars of the affine decomposition
`II = II_0 + u II_1`:

```
w0 = <II_0, II_0> = 2        w1 = 2<II_0, II_1> = -8        w2 = <II_1, II_1> = -64
```

(recovered exactly from `P(u)`, test T5a). The identity `w2 = -w1^2` reads

```
<II_1, II_1>  =  -4 <II_0, II_1>^2 .
```

The left side is **degree 2** in the `II`'s; the right side is **degree 4**. The relation is
therefore **inhomogeneous** under `II -> lambda II` (LHS scales as `lambda^2`, RHS as
`lambda^4`, test T5c). A conformal-weight / homogeneity law relates SAME-weight quantities; it
can never equate a quadratic Gram scalar to the square of another quadratic Gram scalar. So
route iii -- the cleanest structural-proof target -- **provably cannot close**. The weight fixes
the degree, not the `w2/w1^2` ratio. This is the first honest negative: there is no symmetry to
exhibit because the relation is not of a symmetry-forceable type.

## 3. Persona 2 -- the W126/W130 machinery specialist: the basis kill (routes i, iv)

**The decisive computation.** The headline `-1/9 = -(1/3)^2` uses the MSS-slice-reduced R^2
coefficient. But "the tachyon" is a statement about the scalaron MASS, and in fourth-order
gravity the scalaron (spin-0) mass is set by the coefficient of `R^2` in the COVARIANT
Lagrangian, because the Gauss-Bonnet term is topological in 4D and `C^2` is the spin-2 channel
(Stelle 1977). W130 computed that covariant coefficient exactly, resolving the slice ambiguity:

```
slice basis (W126):   W = a0 + a1 R + a2s R^2 + a3s Ric^2 ,  (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4)
MSS reduction:        Ric^2 -> R^2/4   =>   a2_MSS = a2s + a3s/4 = 8/9 - 1   = -1/9
covariant (W130):     Ric^2 -> R^2/3   =>   c_R    = a2s + a3s/3 = 8/9 - 4/3 = -4/9   (GB freedom cancels)
```

(PC1-PC3 reproduce all three exactly.) Now test the identity in each basis (T1):

```
MSS-slice coefficient:   a2_MSS = -1/9 = -(1/3)^2 = -(a1)^2      HOLDS
covariant coefficient:   c_R    = -4/9,  -(a1)^2 = -1/9          FAILS by a factor of 4
                         c_R / a1 = -4/3,  but -a1 = -1/3         (would need -1/3 to hold)
```

The physical scalaron coefficient -- the one W130 feeds into `f_0^2 = 1/(6 c_R)` and hence into
the tachyon mass -- **breaks `a2 = -a1^2`**. The identity lives only on the `/4` MSS reduction,
not the `/3` physical one (T1c). The breaking "family member" is not even a deformation: it is
the SAME induced action read in the correct covariant basis. This is the cleanest possible kill.

**Signature/codimension (route i) is degenerate.** Sweeping the base signature over
(1,3),(0,4),(2,2),(4,0) returns the SAME `(a0,a1,a2s,a3s) = (2,1/3,8/9,-4)` every time (T4):
the conformal-graph `|II|^2` on this slice is signature-blind (each `eta` pairs with an
`eta^{-1}` in the contractions, `eta_ii^2 = 1` cancels). So the signature family does not deform
the numbers -- it can neither confirm nor refute the identity. It does, however, **refute one
tempting structural story**: the tachyon `c_R = -4/9 < 0` is NOT a Krein/(9,5)-indefiniteness
effect -- it persists in Euclidean (4,0). The tachyon sign is an algebraic property of the
conformal-graph construction, robust across signature, not a signature artifact.

## 4. Persona 3 -- number theorist: the factorization and the roots (route iv)

`W(u) = -64u^2 - 8u + 2 = -2(8u - 1)(4u + 1)`, roots `u = 1/8, -1/4`; equivalently
`F(R) = -(1/9)(R - 6)(R + 3)`, roots `R = 6, -3`. Is `a2 = -a1^2` an arithmetic identity the
roots force? The product and sum of the `u`-roots give `w0/w2 = (1/8)(-1/4) = -1/32` and
`-w1/w2 = 1/8 - 1/4 = -1/8`. The identity `w2 = -w1^2` is `-64 = -64`; in root language it is
`w2 = -(w2(r_+ + r_-))^2`, i.e. `w2 = -w2^2 (r_+ + r_-)^2`, i.e. `1 = -w2 (r_+ + r_-)^2 =
-(-64)(1/64) = 1`. It checks -- but it is a relation between `w2` (a MAGNITUDE, hence
normalization-carrying) and the root sum, not a pure statement about the root RATIO. The roots
`{6, -3}` have ratio `-2` (a clean rational, part of the prime-3/`3:2:1` leitmotif, W130), and
THAT ratio is normalization-invariant -- but the ratio `-2` is not `a2 = -a1^2`; it is the
weaker `a0/a1 = 6`, `a2_MSS/a1 = -1/3` data. The arithmetic that is invariant (the root ratio,
the sign) is not the arithmetic the keystone needs (the magnitude lock). Number theory confirms
the identity is exact at GU's point and confirms it carries a normalization factor; it does not
find it forced.

## 5. Persona 4 -- symbolic engineer: what the test pins (T2, the normalization)

`tests/W157_...py`, 19 checks, exit 0, exact sympy, positive controls first (PC1-PC5 reproduce
W126's `(2,1/3,8/9,-4)`, `P(u)=-64u^2-8u+2`, and W130's `c_R=-4/9`; the shape family and
signature sweeps reuse the verbatim Route-1 machinery, parametrized). The normalization result
(T2) is the second half of the coincidence and the engineer's sharpest pin:

- Under an overall action rescale `W -> N W`, all of `a0,a1,a2` scale by `N`, so `a2 = -a1^2`
  becomes `N a2 = -(N a1)^2 = -N^2 a1^2`, i.e. `a2 = -N a1^2`. It holds only at `N = 1` -- the
  `a0 = 2` flat-section pin. **Not scale invariant** (T2a).
- For ANY tachyonic theory (`a2 < 0, a1 != 0`), the choice `N* = -a2/a1^2 > 0` makes
  `a2 = -a1^2` hold. Demonstrated on the covariant coefficients: `N* = -(-4/9)/(1/3)^2 = 4`,
  and `4 c_R = -16/9 = -(4 a1)^2 = -(4/3)^2`. So the identity is a normalization CONVENTION
  available to EVERY tachyon, not a constraint on any of them (T2b).
- The only scale-invariant content is the SIGN `a2/a1 < 0` (T2c): `-1/3` in the slice basis,
  `-4/3` in the covariant basis -- the magnitude is basis-dependent, only the sign is shared.

So `w2 = -w1^2` being "exact" (W156 S1) and "reducible to a coefficient relation" (S3/S4) is
real but non-load-bearing: exactness at a pinned normalization is what a normalization
convention looks like. W153 T1 scale-mode invariance (S5) is invariance under the conformal
factor `p`, a DIFFERENT scaling than the action normalization `N` -- it does not rescue the
identity, because `N` is the free scaling and the identity is not `N`-invariant.

## 6. Persona 5 -- adversarial skeptic: steelman STRUCTURAL, then the shape family (route ii)

The steelman for STRUCTURAL was: the identity is exact, non-automatic (a generic `a2` fails it,
W156 S6), and survives the one deformation W153 could compute. If it ALSO survived the shape
family `alpha|II|^2 + beta|H|^2`, that family-invariance would BE the structural proof W156
asked for. So compute it (T3). Route-1 gives both pieces on the MSS slice:

```
|II|^2 :  -64 u^2 -  8 u + 2         |H|^2 :  -256 u^2 - 32 u - 1
```

Form `alpha|II|^2 + beta|H|^2`, extract `a1(alpha,beta), a2(alpha,beta)`, and evaluate the
identity residual `a2 + a1^2`:

```
a2 + a1^2  =  (alpha^2 - alpha + 16 beta^2 - 4 beta + 8 alpha beta) / 9 .
```

This is a nontrivial conic in `(alpha, beta)` -- it vanishes on a CURVE, not identically (T3b).
It vanishes at `beta = 0` (the pure-`|II|^2` GU representative, the positive control T3a) but is
NONZERO (`= 8`) at the OTHER GU-named shape point `beta/alpha = 2` (the W136 bulk-flat
consequence, T3c). So the identity is a codimension-1 point property of the shape family, pinned
to the `beta = 0` representative, NOT a family-wide identity. The steelman's best hope --
family-invariance -- fails: the identity is not preserved along the natural deformation. The
skeptic's steelman for STRUCTURAL collapses; the COINCIDENCE reading is what the family shows.

Honest note (no overclaim): the skeptic did NOT find a signature-family member that breaks the
identity, because the signature family is degenerate (Section 3). The breaks are real and come
from the basis choice (Section 3) and the shape mix (this section) and the normalization
(Section 5) -- three independent deformations, each of which the identity fails to survive.

## 7. Synthesis -- the verdict

**VERDICT: COINCIDENCE.** The exact magnitude identity `a2 = -(a1)^2` is a joint artifact of
(1) the MSS-slice reduction basis (`Ric^2 -> R^2/4`) and (2) the `a0 = 2` flat-section
normalization. It is NOT structural. Three independent computed deformations each break it:

1. **Basis (decisive, T1).** The physical scalaron coefficient is W130's covariant
   `c_R = -4/9`, not the MSS-slice `-1/9`. `c_R != -(a1)^2` by a factor of 4. The coefficient
   that sets the tachyon mass breaks the identity; the same action in the correct covariant
   basis is the breaking family member.
2. **Normalization (T2, T5).** Not scale invariant; holds only at `N=1`; reproducible by
   `N* = -a2/a1^2` for ANY tachyon. Geometrically the relation `<II_1,II_1> = -4<II_0,II_1>^2`
   is inhomogeneous (degree 2 = degree 4), so no conformal-weight law can force it (route iii
   provably cannot close).
3. **Shape family (T3).** The identity locus is a codim-1 curve; it holds at `beta=0` but fails
   at the GU-named `beta/alpha=2`.

**What survives as structural:** ONLY the SIGN, `a2/a1 < 0` (tachyonic iff attractive),
normalization- and basis-invariant (`-1/3` slice, `-4/3` covariant, both negative), and --
per the degenerate signature sweep -- robust across signature (so not a (9,5) artifact either).
The tachyon is CORRELATED in sign with attractive gravity. It is NOT the literal square-shadow
of the Einstein coefficient; the exact `= a1^2` magnitude that W155/W156 personas 6 and 10
leaned on was an artifact.

**Consequence for debit-1 and bar (b).** The keystone conversion FAILS. Debit-1 (the tachyon)
does NOT become a now-understood consequence via the exact-magnitude argument; it stays an
INDEPENDENT debit. The flaw count does not drop, so the W156 convergent story does NOT clear
bar (b) by this route. The load returns to the two genuine escapes named in W156/W155: the
AF-vs-AS branch fork (W128) and gradient-sector saturation (W126). The W156 grade
STRUCTURAL-CANDIDATE is **demoted to COINCIDENCE**.

**The honest residual (the one thing NOT settled, stated as the next computation).** The
surviving sign fact -- is `c_R < 0` (tachyon) FORCED by `a1 > 0` (attraction) in the covariant
induced action? -- is a WEAKER claim than the exact-magnitude keystone, and it is NOT settled
here. The signature sweep shows `c_R = -4/9 < 0` is robust (signature-blind), which is
suggestive, but "robust across the deformations we can compute" is the same evidential tier
that `a2 = -a1^2` itself enjoyed before this wave demoted it. So the sign's structural status
should be graded SIGN-CANDIDATE, not asserted. Concretely: does `c_R = a2s + a3s/3 < 0` follow
from `a1 > 0` by an identity of the conformal-graph `II` construction (e.g. a forced relation
between `a3s` and `a1`), independent of the specific rationals? That is the residual
computation, and it is strictly weaker leverage on bar (b) than the keystone was, because even
if the sign is structural it delivers only "the tachyon is correlated with attraction," not
"the tachyon is the same number as attraction" -- a correlation converts a debit to a feature
far less cleanly than an identity would.

## 8. The (a1, a2) family-sweep table (the RETURN data)

| family parameter | a1 | a2 (as used) | a2 = -a1^2 ? | notes |
|---|---|---|---|---|
| GU point, MSS-slice basis | 1/3 | -1/9 (`a2s + a3s/4`) | **YES** | the headline; positive control |
| GU point, covariant basis (W130) | 1/3 | **-4/9** (`c_R = a2s + a3s/3`) | **NO** (-4/9 vs -1/9) | the physical scalaron coeff; DECISIVE break |
| shape `beta/alpha = 0` (pure \|II\|^2) | 1/3 | -1/9 | YES | GU representative |
| shape `beta/alpha = 2` (W136 bulk-flat) | -- | -- | **NO** (`a2+a1^2 = 8`) | other GU-named point; break |
| signature (1,3),(0,4),(2,2),(4,0) | 1/3 | -1/9 / c_R=-4/9 | slice YES / cov NO | signature-blind (degenerate family) |
| overall normalization `N` | `N/3` | `-N/9` | only at `N=1` | `a2 = -N a1^2`; convention |
| ANY tachyon, `N* = -a2/a1^2` | `a1` | `a2` | YES by construction | proves it is a convention |

Scale-invariant content across ALL rows: `sign(a2/a1) < 0` (tachyonic iff attractive). The
magnitude `|a2/a1|` is basis-dependent (`1/3` slice, `4/3` covariant) and never a structural
constant.

## 9. Gates and honest limits

- Exploration grade; conditional register throughout. Nothing asserts GU, asserts a vacuum, or
  changes any verdict. The result is a DEMOTION of a prior exploration-grade candidate grade
  (W156 STRUCTURAL-CANDIDATE -> COINCIDENCE), established by exact computation with W126 + W130
  positive controls, not asserted.
- W138 battery honored: the verdict binds to GU-specific objects (the W126 slice coefficients,
  the W130 covariant map, the shape family, the `a0=2` pin). The one tempting structural story
  the geometry FORBIDS is recorded (the (9,5)-indefiniteness origin of the tachyon: refuted by
  the signature-blindness, T4).
- Tri-repo gating held: record/finality/capability semantics stay pointers to
  temporal-issuance / time-as-finality / TaF; GU owns the induced-action math only; no
  cross-repo identity asserted.
- No canon / RESEARCH-STATUS / claim-status / verdict / posture change; the debit count is
  unchanged (the keystone did NOT drop it); H59/H61a OPEN; the E2 AF/AS fork carried, not
  closed. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by Team KEYSTONE-A2 (W157). Coherence-first, the #1 keystone of the
substrate-arc worklist. Five personas inline in one worker (differential geometer,
W126/W130 machinery specialist, number theorist, symbolic engineer, adversarial skeptic); no
sub-agents. Reproducible: `python -u tests/W157_a2_equals_minus_a1_squared_keystone.py`
(19/19, exit 0; W126 + W130 positive controls first). Exploration grade; conditional register;
no canon movement.*
