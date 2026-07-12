---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: H59
branch: "Path-2 wave-2, Target 1 (cross-shared): the AF RG flow vs branch-E's exceptional locus"
title: "Does the asymptotically-free 4th-order (Stelle/agravity) RG flow reach branch-E's exceptional (Jordan / pole-collision) locus? VERDICT: BOUNDARY. In the spin-2 sector the AF trajectory is strictly PT-unbroken (grading well-defined, m2^2>0) at EVERY finite RG scale and touches the exceptional locus m2^2=0 ONLY at the free UV Gaussian fixed point (f_2^2=0, ghost decouples) -- proven two independent ways. Because the ghost mass is PROPORTIONAL to the AF coupling (m2^2=(1/2)f_2^2 M_Pl^2), asymptotic freedom drives m2^2 TOWARD the locus, so keep-and-grade gets an interior that PINCHES onto the locus at the UV endpoint (||C||->inf), NOT a clean interior-all-the-way-up. The spin-0 conformal mode sits at the wrong-sign UV fixed ratio f_0^2/f_2^2<0 (tachyonic M_0^2<0 = PT-broken) and PLAUSIBLY already sits past the locus -- the load-bearing open question."
grade: "exploration / spin-2 verdict PROVEN two ways (numeric RK4 of the imported W45 beta + analytic leading-log), on the STANDARD agravity mass convention; spin-0 CROSS graded PLAUSIBLE (physical-vs-gauge status of the wrong-sign conformal mode open). Deterministic test tests/W53_path2_target1_af_vs_locus.py, 10/10, imports the W45 BetaSystem (betas not re-derived). No canon / RESEARCH-STATUS / claim-status / verdict / posture changed. H59 remains OPEN."
depends_on:
  - explorations/path2-branchE-nogo-2026-07-11.md
  - explorations/path2-branchA-cutkosky-cut-2026-07-11.md
  - explorations/path2-branchD-leewick-2026-07-11.md
  - tests/W45_H57_stage1_beta_system.py
  - tests/W46_H57_stage2_fixed_point.py
  - tests/W47_H60_firm_af.py
scripts:
  - tests/W53_path2_target1_af_vs_locus.py
---

# Path-2 wave-2, Target 1 — does the AF flow reach branch-E's exceptional locus?

**Role.** The five-branch blind Path-2 wave reduced the whole keep-and-grade loop-positivity question to
one decidable computation (branch E, repair-3): *exhibit the RG flow of the fourth-order sector and
decide whether it ever reaches the exceptional (Jordan / pole-collision / m2→0) locus, on which — by the
repo's R1 two-line theorem — no positivity-compatible grading of any kind exists.* This target settles
that. It is **cross-shared, not blind**: it connects branch E (the locus), branches A/D (the pole
picture), and W45/46/47 (the AF flow).

The decisive stakes, restated:
- **STAYS-CLEAR** (AF trajectory stays PT-unbroken all the way to the UV FP) → the positivity-defining
  grading is RG-stable → keep-and-grade **works** for AF 4th-order gravity (strongest available proof).
- **CROSSES** (flow crosses the exceptional locus at finite RG time) → grading-based loop positivity
  **fails**; only the removal-based (fakeon/Lee-Wick) route — unitarity at a bounded causality cost —
  survives.
- **BOUNDARY** — the trajectory sits on / asymptotically touches the locus. This is what we find.

---

## 1. Branch-E's exceptional locus, made explicit for 4th-order gravity

**E's locus in the solvable skeleton (W52).** On the minimal 2×2 PT Hamiltonian
`H(a,b)=[[ia,b],[b,-ia]]` the positivity-defining grading is `eta_+=[[1,-ia/b],[ia/b,1]]` with
eigenvalues `1∓a/b`. The domain structure is exact:

- PT-unbroken (real spectrum, `eta_+>0`) ⇔ `|a|<b`;
- **exceptional locus `a=b`**: eigenvalues collide, `H` is a defective Jordan block,
  `lambda_min(eta_+)=1−a/b→0` — the positive grading **degenerates**;
- PT-broken `|a|>b`: imaginary spectrum, `eta_+` indefinite — positivity gone.

So the locus is the codim-1 surface where **two eigenvalues degenerate** (`lambda_min(eta_+)→0`).

**Its physical face (branches A, D): the spin-2 pole collision `m2^2 → 0`.** The Stelle/induced-`|II|^2`
spin-2 propagator (Branch A §1.1) is `D(p)=(1/m2^2)[1/p^2 − 1/(p^2−m2^2)]`: a healthy massless-graviton
pole at `p^2=0` (residue `+`) and the massive **ghost** pole at `p^2=m2^2` (residue `−`). These are the
two spin-2 "eigenvalues." They **collide when `m2^2 → 0`** — the massive ghost pole runs down onto the
massless graviton pole. That is a within-sector Jordan degeneration, exactly E's `a/b→1`, and E named it
explicitly as the physically distinguished, symmetry-enhanced degeneration in its repair-4:
*"the conformal / massless-spin-2-ghost limit `m2→0`, which is not a random point but a symmetry-enhanced
one the flow can be driven toward."*

Branch D gives the *other* face of the same locus: the one-loop self-energy pushes the ghost pole
**complex** (`m2^2 → complex`, Lee-Wick pair). That is a **loop-driven** route to non-real spectrum;
the RG running of the tree couplings is a **coupling-driven** route to the **real** Jordan collision
`m2^2→0`. This target computes the coupling-driven (RG) face; D's loop-driven face is complementary,
not competing.

**Construction fork (GEOMETER-VS-PHYSICS-OBJECTS.md), stated.** For "the exceptional locus" I use the
**physics face** (spin-2 pole collision `m2^2→0`, A/D) and cross-identify it with E's **program-native**
grading-degeneration (`a/b→1`, `lambda_min(eta_+)→0`). For "the ghost" I keep it (keep-and-grade
Krein/PT), grading-agnostic at the pole level as in Branch A. The positivity object attacked is the
**positive Born-rule inner product** (E's target), not pseudo-unitarity.

**E's locus condition, written on the couplings.** With the mass–coupling relation of §2:
```
  EXCEPTIONAL LOCUS (spin-2):   m2^2 = 0   ⇔   f_2^2 = 0   (M_Pl fixed).
  distance-to-locus:            d_locus(mu) ≡ m2^2 / M_Pl^2 = (1/2) f_2^2(mu)  ( >0 ⇔ PT-unbroken interior ).
```

---

## 2. The mass ↔ coupling relation, and the convention (the crux)

**Convention (Salvio–Strumia agravity, arXiv:1403.4226), stated explicitly.** Write the Weyl term as
`−(1/(2 f_2^2)) C_{μνρσ}^2`, so `f_2` is a coupling like the Yang–Mills `g` (it sits in the
*denominator*), and **asymptotic freedom is `f_2 → 0`**. In this normalization the massive spin-2 ghost
pole sits at
```
      m2^2 = (1/2) f_2^2 M_Pl^2                       ( ghost mass-squared PROPORTIONAL to f_2^2 ).
```
`M_Pl` is the dimensional-transmutation (Newton) scale — a **relevant** direction that is **fixed** along
the flow (W46 Q2e identifies `mu_DW = M_Pl`). This is the honest, load-bearing convention call, and it is
the standard one: it is the normalization in which AF *and* the ghost mass are both defined.

**The crux tension, resolved.** AF drives `f_2^2 → 0` in the UV. Since `m2^2 ∝ f_2^2` with `M_Pl` fixed,
the dimensionless distance-to-locus
```
      d_locus = m2^2 / M_Pl^2 = (1/2) f_2^2(mu)  ⟶ 0     as mu → ∞.
```
**The very property that gives asymptotic freedom (`f_2 → 0`) drives the ghost mass TOWARD the exceptional
point `m2^2 = 0`, not away.** E's repair-4 worry is realized *in direction*. (Measured instead against
the running scale, `m2^2/mu^2 = (1/2) f_2^2 M_Pl^2/mu^2 → 0` even faster — same conclusion.)

**Adversary — "did you pick the wrong convention?"** If the convention were *inverted* — i.e. the ghost
mass grew as `m2^2 ~ M_Pl^2/f_2^2` (ghost → infinitely heavy in the UV) — then `d_locus → ∞` and the flow
would move **away** from the locus (STAYS-CLEAR trivially). That is *not* the agravity convention: there,
the higher-derivative coefficient `1/f_2^2` diverging in the UV means the *massive* pole `m2^2 = f_2^2
M_Pl^2` goes to *zero*, not infinity. The standard convention is precisely the one that makes this a
**genuine tension** rather than a triviality, so the convention choice is load-bearing and is stated as
the assumption (§6).

---

## 3. Integrating the AF flow and evaluating the locus (two independent derivations)

The imported object is `W45.BetaSystem` (betas **not** re-derived): `beta_{f2^2} = −kappa f_2^4 b_2`,
`b_2 = 133/10 + c_RS_weyl = 14.717 > 0` at the RS anchor. `f_0^2` does not enter `beta_{f2^2}`.

### (i) Numeric — RK4 of the imported beta from IR to deep UV
Seed `f_2^2(0)=0.8` (⇒ `d_locus=0.40`), integrate `t=ln mu` to `t=4000` (RK4, 4×10^5 steps):

| `t` | `f_2^2(t)` | `d_locus=m2^2/M_Pl^2` | `a/b` (proxy) | `lambda_min(eta_+)` proxy |
|---:|---:|---:|---:|---:|
| 0 | 0.80 | 0.400 | 0.714 | 0.286 |
| 40 | 0.201 | 0.100 | 0.909 | 0.091 |
| 400 | 0.0260 | 0.0130 | 0.987 | 0.0128 |
| 2000 | 0.00533 | 0.00266 | 0.9973 | 0.00266 |
| 4000 | 0.00267 | 0.00134 | 0.9987 | 0.00134 |

`f_2^2(t) > 0` at **every finite `t`** (strictly PT-unbroken; `m2^2 > 0`), decreasing **monotonically**
toward 0. `d_locus` falls by >100× yet never reaches 0. `lambda_min(eta_+)` (E's grading eigenvalue)
tracks it down toward 0 — the grading is progressively degenerating as the flow approaches the locus, but
never degenerate at finite scale.

*(The `a/b` proxy `a/b = 1/(1+d_locus)` is a stated monotone reparametrization, not a derived identity;
its only load-bearing content is that distance-to-locus is monotone in `f_2^2` and →0 iff `f_2^2→0`. The
proven physics is the `f_2^2` column, from the imported beta.)*

### (ii) Analytic — leading-log closed form
`df2/dt = −kappa b_2 f2^2` integrates exactly:
```
      1/f2(t) = 1/f2_0 + kappa b_2 t    ⇒    f2(t) = f2_0 / (1 + kappa b_2 f2_0 t)  ~  1/(kappa b_2 t).
```
So `d_locus = f2/2 → 0` **only as `t = ln mu → ∞`**, logarithmically; at every finite `t` it is strictly
positive. The exceptional locus `m2^2 = 0 ⇔ f2 = 0` **IS the UV Gaussian fixed point itself**, not a
finite-RG-time crossing.

### Agreement (two-derivations discipline — the standard that caught a real bug before)
At `t=4000`: analytic `f_2^2 = 2.6736e−3`, numeric `2.6736e−3`, **rel.err 1.5e−15**. Measured
`d(1/f2)/dt = 0.0931938 = kappa b_2` to 1e−6. The two derivations **agree**: strictly PT-unbroken at
every finite scale; locus touched only at the free UV endpoint.

---

## 4. The spin-0 conformal mode — where the verdict could go outright NEGATIVE

W46's fixed-ratio analysis: on the AF-complete trajectory `f_2 → 0`, the UV-complete variable is the
ratio `r = f_0^2/f_2^2`, whose ODE bracket `(5/6+d) r^2 + (5+b_2) r + 5/3 = 0` has **both roots
negative** (`r* = −0.085, −23.58` at the anchor; product `>0`, sum `<0`). So the UV-complete trajectory
sits at `f_0^2/f_2^2 = r* < 0`, i.e. (with `f_2^2 > 0`) **`f_0^2 < 0` — a wrong-sign conformal mode**.

If `f_0^2 < 0` then the spin-0 pole `M_0^2 = (1/2) f_0^2 M_Pl^2 < 0` — a **tachyonic** scalar, with
imaginary frequency `±i|M_0|`, a **complex-conjugate pair**. In E's language that is **PT-broken**: the
scalar sector would already sit **past** the exceptional locus. That would flip the spin-0 verdict to
**CROSSES**.

**Honest grade: PLAUSIBLE, not proven.** The status of the wrong-sign conformal mode is genuinely open:
in Euclidean quantum gravity the conformal factor famously has wrong-sign action but is a
gauge/unphysical mode (Gibbons–Hawking–Perry rotation), *not* a physical instability. Whether the
agravity UV-complete `f_0^2 < 0` is a physical tachyonic spectrum (→ PT-broken, CROSSES) or the
unphysical conformal-factor direction (→ no positivity obstruction) is the **load-bearing open
question**. W46 itself flagged this exact point ("admissibility of that sign IS the positivity
question"). I do not manufacture a kill from it.

---

## 5. Self-critical pass (specialist / adversary / referee, inline)

**Specialist** computes: spin-2 `d_locus = (1/2) f_2^2(mu)`, monotone → 0, strictly positive at finite
`mu`, locus = UV FP; two derivations agree to 1e−15. Spin-0 fixed ratio `r* < 0`.

**Adversary** attacks:
1. *"Wrong convention for `m2^2`?"* — Addressed §2: inverting it flips to STAYS-CLEAR, but the agravity
   convention (`m2^2 ∝ f_2^2`) is the standard one and is stated as the load-bearing assumption. Verdict
   is convention-honest, not convention-rigged.
2. *"Is the locus really `m2^2 → 0`, or the ratio?"* — Both are examined. The **spin-2 within-sector
   Jordan collision** (E's `a/b→1`) is `m2^2→0`; the **spin-0 wrong-sign** is a *distinct* possible
   crossing, reported separately and graded PLAUSIBLE. Neither is defaulted.
3. *"BOUNDARY is a dodge — which way does it break?"* — Sharpened: at every **finite (interacting)**
   scale it is strictly PT-unbroken (grading exists); the touch is exactly at `f_2^2 = 0`, the **free**
   point where the ghost decouples and (Branch A) the negative cut that needs the interaction switches
   off. So the spin-2 degeneration is a **free-theory** degeneration, harmless — but it does mean
   keep-and-grade does **not** get a clean interior *all the way up*; the interior pinches onto the locus
   (`||C|| → ∞`, E repair-4c) at the endpoint.

**Referee** grades: spin-2 BOUNDARY **PROVEN** (two derivations, standard convention). Spin-0 CROSS
**PLAUSIBLE** (physical-vs-gauge status open). Net: **BOUNDARY**, leaning against a clean STAYS-CLEAR
proof-of-concept.

---

## 6. Verdict, load-bearing assumption, confidence

**VERDICT: BOUNDARY.**

- **Spin-2 (proven two ways).** The AF trajectory is **strictly PT-unbroken** (`m2^2 = (1/2) f_2^2 M_Pl^2
  > 0`, grading well-defined) at **every finite RG scale**. Because `m2^2 ∝ f_2^2`, the flow moves
  **toward** E's exceptional locus (`m2^2 → 0`) and reaches it **only at the UV Gaussian fixed point**
  (`f_2^2 = 0`), where the theory is **free** and the ghost **decouples**. **No finite-time crossing.**
  This is a *qualified positive* for keep-and-grade — positivity is RG-stable across the whole
  **interacting** flow — but **not** the clean "interior all the way to the UV" proof-of-concept: the
  grading pinches onto the locus at the free endpoint. It is a **boundary** result.
- **Spin-0 (plausible-broken, open).** The UV-complete trajectory carries a wrong-sign conformal mode
  (`f_0^2/f_2^2 = r* < 0`). If physical, that is a tachyonic (PT-broken) scalar already **past** the
  locus (→ CROSSES for spin-0). Graded **PLAUSIBLE**, physical-vs-gauge status **open**.

**Net reading for the orchestrator.** This is **not** the clean STAYS-CLEAR that would certify
keep-and-grade as a proof-of-concept for AF 4th-order gravity. Keep-and-grade survives the entire
finite-scale spin-2 flow (real content, a genuine partial positive), but (a) the AF endpoint sits exactly
**on** the locus, so there is no RG-stable *interior* up to the UV — the positive metric degenerates in
the UV limit — and (b) the UV-complete conformal mode plausibly already sits **past** the locus. The
**removal-based (fakeon / Lee-Wick, branches A/D)** route — which moves the ghost pole off the real axis
and buys unitarity at a bounded causality cost — remains the safer one, especially for the conformal
mode. Branch E's burden is **not** discharged into a clean pass: it is answered BOUNDARY.

**Construction used.** Exceptional locus = physics-face spin-2 pole collision `m2^2→0` (A/D),
cross-identified with E's native grading degeneration `a/b→1`. Ghost = kept (keep-and-grade), pole-level
grading-agnostic. Mass–coupling = **standard agravity** `m2^2 = (1/2) f_2^2 M_Pl^2` (Salvio–Strumia).
Positivity object = positive Born-rule inner product.

**Load-bearing assumption.** `m2^2 = (1/2) f_2^2 M_Pl^2` with `M_Pl` the **fixed** transmutation scale, so
the dimensionless distance-to-locus is `(1/2) f_2^2` and AF drives it to 0. **Inverting** the convention
(`m2^2 ~ M_Pl^2/f_2^2`, ghost → heavy in UV) would flip the verdict to STAYS-CLEAR. The standard agravity
convention (ghost mass *proportional* to the AF coupling) is what makes the flow move **toward** the
locus and is what the BOUNDARY verdict rests on.

**Confidence.** Spin-2 BOUNDARY: **rigorous within the one-loop AF truncation** (imported KNOWN/ported
betas; two agreeing derivations; standard convention). Spin-0 CROSS: **plausibility** (open physical
status of the wrong-sign conformal mode). Truncation-bounded (one loop, 2-coupling gravity sector; RS at
anchor). No loop amplitude computed here.

## What this does NOT do

No GU/Stelle loop amplitude computed. No claim that the spin-2 ghost pole crosses the locus at finite RG
time (it does **not**). No proof that the spin-0 wrong-sign mode is a physical PT-breaking (it is
**plausible**, open). No change to `CANON.md`, `RESEARCH-STATUS.md`, claim status, verdicts, or public
posture. H59 remains **OPEN**. The deliverable is a graded BOUNDARY answer to branch-E's decisive
reduced question, connecting E (locus) + A/D (pole picture) + W45/46/47 (flow), with the spin-0 conformal
mode isolated as the sharp remaining sub-question.

## Next valid swing

1. Settle the spin-0 status: is the agravity UV-complete `f_0^2 < 0` a physical tachyonic spectrum
   (PT-broken, CROSSES) or the unphysical conformal-factor / gauge mode (no obstruction)? This decides
   whether the net verdict is BOUNDARY-leaning-positive or CROSSES.
2. Cross-file against Branch D: the RG (coupling-driven) face gives `m2^2 → 0` (real Jordan collision at
   the UV FP); D's loop-driven face gives `m2^2 → complex` (Lee-Wick pair). Do both faces of E's locus
   bite the *same* trajectory, or does the loop-complexification (D) pre-empt the real collision by
   moving the pole off-axis before `m2^2` reaches 0?
