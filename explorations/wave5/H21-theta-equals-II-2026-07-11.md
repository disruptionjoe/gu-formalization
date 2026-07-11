---
title: "H21 -- Proving P1: s*(theta) = II_s OFF-SHELL, convention-fixed (the Gauss-formula hardening)"
artifact_type: exploration
status: exploration
updated_at: "2026-07-11"
wave: 5
depends_on:
  - "tests/wave5/H21_theta_equals_II_proof.py"
  - "explorations/wave4/H18-forcing-computation-2026-07-11.md"
  - "explorations/geometry-curvature-emergence/ii-s-coordinate-formula-2026-06-23.md"
  - "explorations/geometry-curvature-emergence/4d-reduction-section-pullback-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/dd1-distortion-tensor-literature-check-2026-06-22.md"
  - "explorations/geometry-curvature-emergence/ii-s-moving-frames-2026-06-23.md"
  - "canon/dark-energy-theta-divergence-free.md"
verdict: "PROVEN (off-shell, full-tensor) in the canonical gauge; convention resolved as a non-trace additive shift; residual = canonical-connection/bundle identification (NOT a trace obstruction)"
---

# H21 -- The Hardening Move: prove `s*(theta) = II_s` off-shell

**Discipline.** Exploration-grade. Compute -> adversarially verify -> honest grade. The
reproducible check is `tests/wave5/H21_theta_equals_II_proof.py` (exit 0, 9/9 PASS). Nothing
imported; exact rational arithmetic; no field equation used anywhere.

---

## The question H21 settles

H18 (Wave 4, Condorcet #1) forced **Branch A** (II-class -> gravity CLEARS) at **structural**
grade, conditional on two reconstruction/transcript premises. The load-bearing one is

> **P1.** `s*(theta) = II_s`, with `II_s` the **FULL** second fundamental form (both spacetime
> indices free, not a trace), **off-shell** (no field equation), convention-fixed.

`ii-s-coordinate-formula` sec 7 called this a "reconstruction claim"; DD1 is `PARTIALLY_NAMED`;
H18 flagged the **literal-graph vs horizontal-normalized** convention as the open gate and
warned that an obstruction "by a trace piece ... could re-open the |II|^2-vs-|H|^2 question."

H21's job: **prove P1 (convention-fixed) or name the precise obstruction** -- and in particular
decide whether the convention ambiguity is a trace piece (which would re-open H15/H18's fork)
or something harmless.

## What theta and II_s are (the two objects, made precise)

- **theta (canon).** `theta = pi - Ad(epsilon^{-1}) B` (`dark-energy-theta-divergence-free.md`),
  the gauge-equivariant distortion 1-form: schematically **any connection minus the
  gauge-transformed Levi-Civita** (DD1 sec 1.2, transcript). In the canonical/tautological
  gauge this is `theta = nabla^gimmel - A_adapted`, where `nabla^gimmel` is the Levi-Civita
  connection of the gimmel metric on `Y = Met(X)` and `A_adapted` is the connection adapted to
  the section (its tangential pullback = the induced Levi-Civita connection).
- **II_s (ii-s sec 4).** The second fundamental form of the graph section `s(x)=(x,g(x))`
  immersed in `(Y, gimmel)`: `II_s(T_mu,T_nu) = nabla^gimmel_{T_mu} T_nu - ds(nabla^gbar_{mu} nu)`,
  a **full** symmetric-2-tensor valued in the normal (vertical) bundle `~= Sym^2 T*X`.

## The proof (what the test computes, exactly)

The identity is, structurally, the **Gauss formula** of Riemannian submanifold geometry:

```
s*(nabla^gimmel)  =  nabla^LC(s*gimmel)  (+)  II_s          [GAUSS]
   (ambient LC          (TANGENTIAL part =      (NORMAL part =
    along section)       induced-metric LC)      the FULL SFF)
```

so `s*(theta) = s*(nabla^gimmel) - nabla^LC(s*gimmel) = II_s`, exactly. [GAUSS] is **metric
compatibility of the ambient Levi-Civita connection** -- a theorem that uses **no field
equation**. The test builds the FULL ambient gimmel metric as an explicit metric on
`Y = R^n x Sym^2(R^n)` (tautological horizontal block `gimmel_{mu nu} = h_{mu nu}`,
trace-reversed Frobenius vertical block `V_h`), computes its Levi-Civita connection **from
scratch**, and verifies along the graph section, off-shell (`g, dg, ddg` free, EOM-unconstrained):

| Check | Statement | Result |
|---|---|---|
| **1** | tangential part `gimmel(nabla_T T, T) = Koszul_gbar` = LC of the **induced** metric `gbar = s*gimmel` (the core of [GAUSS] and hence of P1) | PASS, 12 pts, off-shell |
| **2 / 2b** | residual `II_s = nabla_T T - tangential` is gimmel-perp to `TX`, symmetric in its two indices | PASS |
| **3** | `II_s` traceless (graviton) part generically **nonzero** -> P1 delivers the **FULL** tensor, not the trace | PASS |
| **4a** | convention shift `S = II_s|_{dg=ddg=0}` equals ii-s 6.1's `-(1/2)(g_{a(mu}g_{nu)b} - 1/2 g_ab g_mn)` **exactly** (at native `n=4`) | PASS |
| **4b** | that shift `S` is itself a **FULL** tensor (traceless part nonzero) -> **NOT** a trace | PASS |
| **5** | identity holds for **arbitrary EOM-unrelated** `ddg` -> off-shell certificate | PASS |
| **0a/0b** | ii-s sec2 cross-Christoffel; induced `gbar = g + V_g(dg,dg)` (ii-s sec3) | PASS |

**Method note (honest).** `n=2` is *degenerate* for the trace-reversed fibre metric (the
trace coefficient `1/2` equals the critical `1/n` exactly at `n=2`), so the main proof runs at
`n=3` (ambient dim 9; the Gauss identity is dimension-universal and `n=3` already exercises the
traceless sector), and the exact ii-s 6.1 slice coefficient is checked at the **native `n=4`**.
Full symbolic simplification over 9/14 dims is intractable, so the tensor identities are
verified by **exact rational evaluation at many independent random integer points**
(Schwartz-Zippel): each sample returns **exactly 0**. For bounded-degree rational identities
this is decisive, but it is exact-sampling grade, not a closed-form symbolic proof.

## Convention: PINNED, and the trace fear is REFUTED

The clean identity uses **reference = Levi-Civita connection of the INDUCED metric
`gbar = s*gimmel`** (the literal-graph induced metric, `gbar = g + V_g(dg,dg) != g`). This is
not a free choice: the tangential part of *any* ambient Levi-Civita connection along a
submanifold is *automatically* the LC of the induced metric (Check 1) -- so `gbar` is forced.

The **horizontal-normalized** convention differs from the literal-graph one only by the
**fixed background slice** `S = II_s|_{dg=ddg=0}` (Check 4a) -- the second fundamental form of
the *constant* metric slice, a tensor depending on `g` **pointwise** (no derivatives). The
decisive adversarial finding (Check 4b):

> **`S` is a FULL tensor (its traceless-in-`(mu,nu)` part is nonzero), NOT a trace.**

Therefore the literal-vs-horizontal convention is an **additive full-tensor background shift**,
never a trace projection. **It cannot collapse `|II|^2` to `|H|^2`.** H18's specific fear -- an
obstruction "by a trace piece" re-opening the `|II|^2`-vs-`|H|^2` fork -- **does not
materialize.** Both conventions deliver the full rank-`(dim Sym^2)` `II_s`.

## VERDICT: (PROVEN) off-shell, full-tensor, in the canonical gauge

`s*(theta) = II_s` **is the Gauss formula** for the graph section into `(Y=Met(X), gimmel)`,
in the canonical/tautological gauge (`theta = nabla^gimmel - A_adapted`). Verified explicitly
for the gimmel metric, **off-shell** (Check 5), with `II_s` the **FULL** SFF (Check 3), and the
convention ambiguity resolved as a **non-trace** additive shift (Checks 4a/4b). This **upgrades
P1 from "reconstruction claim" to a proven geometric identity** -- *conditional on one
structural assumption named below*.

**Confidence.** HIGH on the geometry (the Gauss formula is a theorem; verified explicitly and
off-shell for the exact gimmel metric). MEDIUM-HIGH that the canonical gauge is GU's intended
one (it is the tautological choice used in DD1 sec 1.1 and `4d-reduction` sec B1.4).

### Honest caveats / the residual (this is NOT a trace obstruction)

1. **Canonical-connection / bundle identification (the real residual).** The proof holds in the
   gauge where the GU connection `A` is the **ambient gimmel Levi-Civita** connection. GU's
   *dynamical* `theta = pi - Ad(epsilon^{-1})B` lives in `Omega^1(Y, ad P)` on the **Sp(64)**
   bundle `P`, while `nabla^gimmel` lives on the **frame bundle SO(9,5)** of `Y`. Equating them
   requires the spin-lift/embedding `SO(9,5) -> Sp(64)` and that GU's connection reduces to the
   gimmel LC in the relevant sector. This is a **bundle/gauge structural assumption** -- the
   same class as the unbuilt GU **source action** (canon `dark-energy` Assumption 3), **not** a
   trace-dropping obstruction and **not** a field-equation smuggle.
2. **Grade of the numerics.** Exact-sampling (Schwartz-Zippel), not closed-form symbolic. 12
   off-shell points for the core identity; the ii-s 6.1 slice coefficient checked symbolically-
   exactly at 2 points in native `n=4`. A closed-form `n=4` symbolic proof was not produced
   (intractable simplify).
3. **Not re-derived here.** The gimmel signature (9,5), the Sp(64)/Cl(9,5) rep theory, ghost
   clearance (Bateman-Turok), and the YM action *type* (P2) are taken from canon/H15/H18.

## RE-RANK signal

- **Gravity: STRUCTURAL -> HARD, modulo one residual (the same one H18 already named).** P1 is
  now a **proven geometric identity** (Gauss formula), off-shell, full-tensor. The gravity clear
  hardens accordingly; the *only* remaining gate on the P1 leg is the canonical-connection /
  bundle-identification assumption (item 1), which coincides with the unbuilt-source-action gate
  that also holds P2. So the gravity leg is **HARD-clear modulo the single unbuilt piece** (GU's
  source action fixing `A` and the `|theta|^2` action), not modulo two independent reconstruction
  premises.
- **The fork does NOT re-open.** The obstruction H18 feared -- a trace piece from the convention
  choice -- is **refuted** (Check 4b): the convention shift is a full tensor. `|II|^2`-vs-`|H|^2`
  is untouched; II-class is **robust to the convention**. The entropic/H5 (Branch B) route does
  **not** rise.
- **Next reflection should focus on:** (i) **H16** (Stelle viability -- right sign/magnitude of
  the induced Einstein `R^X` once the ambient DeWitt `R^Y` is included) -- now clearly **#1**;
  (ii) the **canonical-connection identification** `A = spin-lift(nabla^gimmel)` on `P`, i.e.
  the same move as writing GU's source action -- the single piece that converts H21's
  "PROVEN-in-canonical-gauge" into an unconditional HARD clear.

---

*Filed 2026-07-11. Wave 5, hardening move for H18. Reproducible:
`python tests/wave5/H21_theta_equals_II_proof.py` (exit 0, 9/9 PASS). Exploration-grade; not
promoted to canon.*
