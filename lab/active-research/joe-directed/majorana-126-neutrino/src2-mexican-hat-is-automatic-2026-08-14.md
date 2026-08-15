---
artifact_type: exploration
status: exploration
doc_type: source-mechanism-gate
created: 2026-08-14
work_item: SRC-2
channel: majorana_126_neutrino_mechanism
title: "SRC-2: Eric's Mexican hat is AUTOMATIC. The cross-term mass form M[(mu,B),(nu,C)] = F0^{mu nu A} f_{ABC} is symmetric and exactly TRACELESS for ANY background curvature, because f_{ABB} = 0 and F0^{mu mu A} = 0. Symmetric plus traceless plus nonzero forces eigenvalues of both signs, so a tachyonic direction exists whenever F0 != 0 -- no sign condition is needed at all, which is STRONGER than the source's own 'if your curvature is negative'. The same tracelessness is double-edged: the symmetric point is never stable and the breaking is unselective."
grade: "EXACT integer arithmetic for every load-bearing claim: the Cartan three-form, its total antisymmetry, the k/p selection rule, and the symmetry, tracelessness and non-vanishing of M. 21/21. One eigenvalue COUNT is float and is explicitly labelled non-load-bearing. NOT: a full effective potential, a boundedness proof, a vacuum, a mass scale, or any claim-status movement."
disposition: MEXICAN_HAT_AUTOMATIC_FOR_ANY_NONZERO_BACKGROUND_CURVATURE__NO_SIGN_CONDITION_REQUIRED__MASS_FORM_EXACTLY_TRACELESS__SYMMETRIC_POINT_NEVER_STABLE__BREAKING_UNSELECTIVE__BOUNDEDNESS_OPEN
canon_verdict_change: none
steering_effect: unchanged
canonical_effect: pending_integration
depends_on:
  - lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md
  - lab/active-research/joe-directed/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md
  - papers/drafts/Transcript into the impossible.md
scripts:
  - tests/channel-swings/joe_directed_curvature_mexican_hat_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `SOURCE_NATIVE_ROUTE`.

# SRC-2 — the Mexican hat is automatic

## What was tested

SRC-1 extracted the source mechanism verbatim (primary transcript `00:43:04`):
the quadratic term in `||F||^2` is the unperturbed curvature contracted with
`a^a`, and *"if your curvature is negative, now you start to get a Mexican hat
potential."* The mass form for the constant mode is therefore

```text
M[(mu,B),(nu,C)] = F0^{mu nu A} f_{ABC},
```

with `f_{ABC} = B(T_A,[T_B,T_C])` the Cartan three-form of `so(6,4)`. The
composite index `(mu,B)` has dimension `10 x 45 = 450` — **exactly the
Lorentz-scalar content of `$` that MJ-2 and BD-2 identified**, which is a
non-trivial consistency check between the source reading and the earlier gates.

## Result

`M` is symmetric because `f` and `F0` are *each* antisymmetric, so the exchange
`(mu,B) <-> (nu,C)` flips both signs. And it is **exactly traceless**, for a
reason that has nothing to do with the choice of background:

- `f[A,B,B] = 0` for every `A,B` — verified over all `45 x 45` pairs;
- `F0^{mu mu A} = 0` for every `mu,A` by antisymmetry of the form indices.

> **A nonzero symmetric traceless form always has both a positive and a
> negative eigenvalue. So a tachyonic direction exists whenever `F0 != 0`.**

**No sign condition is required.** This is *stronger* than the source's own
statement: Eric conditions the Mexican hat on the curvature being negative,
but tracelessness makes it automatic for any nonzero background curvature
whatsoever. On the exhibited background, `tr(M) = 0` and `tr(M^2) = 1920`
exactly.

**Selection rule, computed:** `f_{ABC}` vanishes unless the number of `p`
indices is `0` or `2` — a direct consequence of `[k,k] ⊆ k`, `[k,p] ⊆ p`,
`[p,p] ⊆ k` together with `B(k,p) = 0`. Both allowed classes occur, so the rule
is not vacuous. Consequently a **purely `p`-valued background curvature
produces no `k-k` and no `p-p` blocks at all** — it couples `k` to `p` only.

## Why this cuts both ways

This is the first result in this channel that **supports** the source rather
than obstructing it. The mechanism does what Eric says, and does it more
generically than he claims. But the same tracelessness that makes it work is a
problem:

1. **The symmetric point is never stable.** For *any* nonzero background
   curvature there is a tachyonic direction. There is no regime, anywhere, in
   which the unbroken configuration sits at a minimum.
2. **The breaking is unselective.** Tracelessness forces the negative and
   positive directions to balance; on the exhibited background the split is
   `60 / 60` out of `450` *(float illustration, non-load-bearing)*. Nothing in
   the mass form prefers the Standard Model direction, which is the same gap
   PV-1 found from the orbit side: available breaking directions never reduce
   to exactly the SM.

So the mechanism supplies **breaking** generously and supplies **selection**
not at all. That is a sharper and more useful statement of the difficulty than
"the VEV is unselected", because it is now a property of the mass form rather
than an absence of information.

## Claim ceiling

**Constant modes only, and cross term only.** `M` is the `<F0, a^a>` mass form.
It is not the full effective potential: the quartic `||a^a||^2` and the `||da||^2`
kinetic term are not analysed, and no vacuum, mass scale, or breaking pattern is
computed.

**Boundedness is open and is the honest next question.** A tachyonic direction
gives a Mexican hat only if the quartic stabilises it. Along directions where
`[a,a] = 0` the quartic degenerates, and whether every negative direction of `M`
is stabilised is not established here. **This artifact does not claim the
potential is bounded below.**

**Float discipline:** the `60/60` eigenvalue count is floating point and is
labelled non-load-bearing in the probe. Every verdict above rests on exact
integer identities — tracelessness, symmetry, `tr(M^2) > 0`, and the selection
rule.

**Not claimed:** that this mechanism produces the observed spectrum, that it
gives neutrinos mass, or that it rescues anything the MJ/PV/BD/SG4 arc closed.
Those gates targeted the standard SO(10) VEV route, which SRC-1 showed the
source disavows; this gate tests the source's actual mechanism and finds its
first step works.

## Next gate

SRC-3: **boundedness.** Does the quartic `||a^a||^2` stabilise every negative
direction of `M`, or are there directions with `Q < 0` and `[a,a] = 0` where the
potential runs away? That is exactly decidable with the machinery now built, and
it is the difference between "GU breaks symmetry automatically" and "GU is
unstable".

Selection stays inside this channel. Repository-wide GU priority is unchanged,
the superposition / source-residual workstream is untouched, and no ledger,
canon, or current-state surface moves.
