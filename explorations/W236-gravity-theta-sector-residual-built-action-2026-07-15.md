---
artifact_type: exploration
label: W236
created: 2026-07-15
status: exploration (GRAVITY LEG, closing W225's ONE open term; imported exact Schwarzschild; surviving conservative IG branch; Psi=0 gravitational vacuum; W229-built theta field equation; personas inline, one worker, no sub-agents; deterministic sympy test with nonzero-source and non-harmonic positive controls that FIRE on real linear-in-M residuals, exit 0)
posture: coherence-first (Joe 2026-07-14); exploration grade; adversarial, native-object first, truth-seeking (closing the theta term FULLY CLEARS the gravity cheap-read, conditional on ONE named posit; a nonzero linear residual would have been an EARLY DISPROOF SIGNAL; reported either way, no rooting)
title: "W236 -- theta-sector residual E_s^theta on imported exact Schwarzschild with the W229-built source action (closes W225's one open gravity term)"
leg: GRAVITY -- ELProjectedGRShadowTheorem, imported-metric slice, E_s^theta term
grade: "E_s^theta = 0 IDENTICALLY (all orders in M) in the Psi=0 vacuum: STRUCTURAL (the record current J[Psi] is a Krein bilinear in Psi, so J[Psi=0]=0 exactly, EXACT; the screened-Poisson operator O = -Z_U D_A* D_A + c_theta eta is invertible for any finite kappa (c_theta=1/kappa>0, sign forced W230), so O theta=0 forces theta=0, COMPUTED sympy; the theta-sector section residual is >= linear in theta so E_s^theta[theta=0]=0, STRUCTURAL). Independence of {kappa, Z_U}: STRUCTURAL (needs only J[0]=0 and c_theta>0; verified across a 4-point {kappa,Z_U} sweep and the massless kappa->inf edge). Assembly with W225 (other four terms zero at linear order): COMPUTED/SOURCE-AUDIT. CONDITIONAL on the W154 posit theta=J (W230: one named axiom, only its sign forced)."
depends_on:
  - explorations/W225-gravity-projected-shadow-schwarzschild-cheap-read-2026-07-15.md
  - explorations/W229-close-a2-source-action-znu-completion-2026-07-14.md
  - explorations/W230-close-a4-derive-w154-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W154-reverse-engineered-source-action-2026-07-14.md
  - canon/schwarzschild-weak-field-rfail.md
  - explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md
  - explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W236_gravity_theta_sector_residual.py
primary_source:
  - "Geometric_UnityDraftApril1st2021.pdf (E. Weinstein), sec 9 (Bosonic action, shiab, section equation)"
external_refs:
  - "A. D. Sakharov 1967 -- induced gravity (the connection carries no fundamental kinetic term; the stance under which Z_U is an induced stiffness)"
  - "T. Jacobson, Phys. Rev. Lett. 75 (1995) 1260 -- Einstein equations as an equation of state (induced / no-fundamental-kinetic-term stance)"
---

# W236 -- theta-sector residual E_s^theta on imported Schwarzschild (closes W225's open term)

## Result in one paragraph

W225 computed every term of the projected section-equation residual
`R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross` on an IMPORTED exact
Schwarzschild solution (conservative IG branch, `Psi = 0` gravitational vacuum) and found
every BUILT term has an identically-zero linear-in-M residual EXCEPT one it could not settle:
`E_s^theta`, which needed the branch-fixed SOURCE ACTION. That action is now built (W229): the
theta/U field equation is the screened-Poisson / induced-Yang-Mills law
`(-Z_U D_A* D_A + c_theta eta) theta = J` with `c_theta = 1/kappa` and nonlocal solution
`theta = G * J`, the Green's function of the record current `J`. The decisive structural fact
(W229 test W154-1) is that the theta field is sourced ONLY by `J = J[Psi]`, and `J[Psi]` is a
Krein BILINEAR in the record field `Psi` (`J^a = Re<Psi, K_S e_a Psi>`). **In the `Psi = 0`
gravitational vacuum `J[Psi=0] = 0` identically, so the screened (massive, `c_theta = 1/kappa >
0`) operator -- which is invertible for every finite `kappa` -- forces `theta = 0`; hence
`E_s^theta = 0` NOT merely at linear order in `M` but at ALL orders, joining `E_s^Phi` and
`E_s^cross` as an exact-in-vacuum zero.** The vanishing is STRUCTURAL in the two free scales
`{kappa, Z_U}` (it uses only `J[0] = 0` and `c_theta > 0`, the sign of which is forced by
W230/C-positivity), verified across a `{kappa, Z_U}` sweep and the massless `kappa -> inf` edge;
no admissible value produces a linear falsifier. **VERDICT SIGNAL: this CLOSES W225's single
open term -- all five terms of `R_s` now have identically-zero linear-in-M residual, the
leading BUILT contribution is quadratic `O(M^2/r^4) = Q(B)` (safe), so the gravity cheap-read
on imported Schwarzschild is FULLY CLEAR at the computable (linear) order: a genuine-YES SIGNAL
for the imported-metric slice, with NO EARLY DISPROOF.** This is CONDITIONAL on the W154 posit
`theta = J` (W230 reduced it to one named axiom -- the connection distortion has no fundamental
kinetic term, marble/wood emergence -- of which only the sign is forced); it is NOT
unconditional. It does NOT clear the gravity leg (`G^X = 0` is trivial; `W_s` is nonzero at
`O(M^2)`, so Schwarzschild is not an exact GU section; Kerr's Willmore term and a non-vacuum
matter section remain). Verdict is Joe-gated; canon `schwarzschild-weak-field-rfail.md` stays
OPEN.

## Construction fork (stated, not defaulted)

The load-bearing object here has a genuine native-vs-physics fork, named per
`GEOMETER-VS-PHYSICS-OBJECTS.md`. There are TWO `theta`'s (W230 Section 0):

1. **The theta field -- RECORD-CURRENT side (the side the built action lives on).** W229's
   action couples the connection distortion to the record current via `-<theta, J[Psi]>` and
   its field equation is `(-Z_U D_A* D_A + c_theta eta) theta = J[Psi]`. On-shell, `theta` is
   the Green's-function functional of `J[Psi]`. This is the construction the BUILT action
   commits to, and it is the one I use: under it, `Psi = 0` gives `J = 0` gives `theta = 0`.
   The alternative reading -- the bare geometric distortion `theta = pi - eps^{-1} B eps`
   (Psi-INDEPENDENT), which need not vanish on Schwarzschild -- is a DIFFERENT construction
   that discards W229's source structure entirely. I name the fork and take the record side
   because that is where the built action (the object this wave was unblocked to use) lives.
   The W154 posit `theta = J` is precisely the bridge that identifies the two; using the built
   action IS using that posit, which is the source of the conditionality below.

2. **The gravity functional / metric / signature forks -- inherited from W225, do NOT re-bite.**
   `E_s^theta` is a matter-sector (source) term, not the Willmore `|II|^2` term; the native
   `|II|^2` fork and the imported-Schwarzschild-metric fork are W225's and are unchanged. The
   `(9,5)`-vs-`(7,7)` signature fork does not enter: the vanishing rests on `J` being a
   bilinear in `Psi` (`J[0]=0`), a statement independent of the base metric sign convention.
   So, as in W225, the cheap-slice verdict is identical on both sides of the signature fork.

Because the load-bearing result (a vanishing source in vacuum) holds on the record-side
construction that the built action actually uses, and is convention-independent, there is no
surviving construction -- within the built action -- in which this term produces a linear
falsifier. That is the honest reason there is no EARLY DISPROOF.

## The residual, term by term (updating W225 with the theta row now closed)

`R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross`.

| term | what it is | linear-in-M part | grade |
|---|---|---|---|
| `alpha_W W_s` | Willmore section EL residual (native `|II|^2`) | `alpha_W * Delta H^(1) = 0` (harmonic) | COMPUTED (W225) |
| `E_s^YM` | gauge-curvature contribution `~ F_A^2` | `0` (`F_A ~ O(M^2)`, F2) | COMPUTED/SOURCE-AUDIT (W225) |
| `E_s^theta` | branch-fixed geometric-theta residual | **`0` (all orders): `J[Psi=0]=0` => `theta=0`** | **COMPUTED/STRUCTURAL (THIS WAVE)** |
| `E_s^Phi` | scalar/Higgs source | `0` (`Phi = 0` in vacuum) | EXACT (W225) |
| `E_s^cross` | cross terms | `0` (vanishing `Psi/Phi` factor) | EXACT (W225) |

The single OPEN row of W225 is now closed. Every term contributes zero at linear order; the
leading BUILT contribution is quadratic `O(M^2/r^4)` -- the standing `Q(B)` obstruction --
which is safe for `M/r << 1`.

## Worked computation

**The theta field equation, and its vacuum source (C1).** W229 built the branch-3 source
action to nonlocal order; its `E_U` field equation is the screened-Poisson / induced-YM law
`(-Z_U D_A* D_A + c_theta eta) theta = J`, `c_theta = 1/kappa`, with solution `theta = G * J`.
The source is the record current `J^a = Re<Psi, K_S e_a Psi>`, a Krein BILINEAR (homogeneous
degree 2) in the record field `Psi`. A faithful scalar model `J = S11 Psi1^2 + 2 S12 Psi1 Psi2
+ S22 Psi2^2` satisfies `J[2 Psi] = 4 J[Psi]` (degree 2) and `J[Psi=0] = 0` for ALL couplings
`S` (sympy, exact). So in the `Psi = 0` gravitational vacuum the theta source is identically
zero at all orders in `M` -- there is simply no matter field to source the connection
distortion. (W229 test W154-1 states exactly this: all `Psi`-dependence enters through `J`, so
`theta = 0` when `J = 0`.)

**Zero source forces theta = 0 (C2).** The screened-Poisson operator
`O = -Z_U D_A* D_A + c_theta eta` is, for any finite `kappa` (so `c_theta = 1/kappa > 0`, a
mass/screening term whose sign is forced positive by W230 / C-positivity), a SPD invertible
operator: `O theta = 0` has only `theta = 0` as a (decaying) solution -- a massive field has no
long-range source-free zero mode. I witness this exactly as W229 did, on a periodic base
lattice: `O = -Z_U * Laplacian + c_theta * I` (6 sites); with zero source `O theta = 0` gives
`theta = 0` and `det O != 0` for every sampled `{kappa, Z_U}` in
`{(1,1), (1/7,5), (10,1/3), (3,100)}` (sympy `LUsolve`, exact). The vacuum `theta` is the
UNIQUE trivial solution.

**E_s^theta[theta=0] = 0 (C3).** The theta-sector action
`S_theta = (1/2kappa)<theta, M theta> - <theta, J> - (Z_U/2)<D_A U, D_A U>` is AT LEAST LINEAR
in the distortion field; its section (`s`) variation `delta S_theta / delta s` carries at least
one factor of `theta` / `D_A U` (the section enters through the fiber metric `M ~ eta`, the
Hodge inner products, and `D_A`). A functional with no theta-independent piece, evaluated on
the vacuum on-shell `theta = 0`, gives `E_s^theta = 0` -- and because `theta = 0` at all orders
in `M` (not just linear), so is `E_s^theta`. This is STRONGER than the linear-order vanishing
W225 needed: `E_s^theta` joins `E_s^Phi` and `E_s^cross` as an exact-in-vacuum zero.

**Structural in {kappa, Z_U} (C4, C5).** The vanishing used only (i) `J[Psi=0] = 0`
(independent of the scales) and (ii) `O` invertible (true for every finite `kappa > 0`, any
`Z_U >= 0`). So NO admissible `{kappa, Z_U}` yields a nonzero `theta`, hence none yields a
linear falsifier. The clear is robust even at the massless boundary `kappa -> inf`
(`c_theta -> 0`, `O -> -Z_U D_A* D_A`): a source-free vacuum with decaying boundary conditions
still selects `theta = 0`; and even a harmonic `theta ~ (M/r)` would give `Delta(M/r) = 0`, the
SAME harmonicity (RFAIL-03) that clears `alpha_W W_s` in W225 -- so the linear residual
vanishes either way. There is no corner of the two-scale family that manufactures a linear
falsifier.

**Rotation independence -> Kerr (C6).** The vacuum vanishing used ONLY `Psi = 0` (matter-free),
never static isotropy or base-metric harmonicity. So unlike `alpha_W W_s` -- whose harmonicity
argument is special to static-isotropic Schwarzschild and BREAKS for Kerr (W225 limit 3) -- the
theta sector clears identically on Kerr and on any matter-free vacuum. The remaining gravity
frontier is therefore the WILLMORE term on Kerr, not the theta term.

**Positive controls (PC1, PC2) -- teeth.** PC1: feeding a NONZERO linear-in-M source (a mock
`J ~ M` from a nonzero `Psi`) through the screened-Poisson Green's function returns a NONZERO
`theta` (`theta[0] = 9M/20`, linear in `M`) -- the detector fires when a real source exists, so
the vacuum vanishing is not a blind spot. PC2: a non-harmonic candidate `theta = M/r^2` returns
`Delta(M/r^2) = 2M/r^4 != 0`, a linear-in-M falsifier -- the residual-operator detector fires on
a genuine nonzero residual. Both controls fire.

## Conditionality on the W154 posit (explicit, not buried)

This result is NOT unconditional. It uses the W229 BUILT action, whose source coupling
`-<theta, J[Psi]>` hard-codes the W154 identification `theta = J` (the branch-3 IG current = the
record current). W229 itself flags that it "secretly assumes W154." W230 adjudicated that posit:
`theta = J` is a REQUIRED independent assumption (NOT forced by Noether II / equivariance / gauge
/ shiab -- those leave a full 14-dimensional space of equivariant divergence-free currents), and
it is equivalent to ONE named axiom -- the connection distortion has no fundamental kinetic term
(`c_kin = 0`, GU's marble/wood emergence, route-beta), of which only the SIGN of the coupling is
forced (C-positivity) while the magnitude and the induced-vs-fundamental status stay UNBUILT.
So: `E_s^theta = 0` **if and only if** the built (record-sourced) theta is the operative object,
which is exactly the marble/wood posit. Under the alternative construction (bare geometric
distortion, `c_kin > 0`), the theta need not vanish on Schwarzschild and the term would require
genuine computation -- W230's `[NEC]` sweep shows a nonzero `c_kin` breaks `theta = M^{-1} J`
smoothly. The honest statement is: **the gravity cheap-read is FULLY CLEAR given the one W154
posit, and only given it.** This is a conditional clear, reported at that grade, not an
unconditional YES.

## What this slice can and cannot settle (honest limits)

- **Can settle (imported-metric, Psi=0 vacuum, given the W154 posit):** `E_s^theta = 0` at all
  orders in `M`, structurally in `{kappa, Z_U}`; combined with W225's four other zero terms,
  the full `R_s` has NO linear-in-M falsifier and the leading built residual is quadratic
  `O(M^2/r^4) = Q(B)`, safe. The imported-metric cheap-read is FULLY CLEAR at linear order --
  a genuine-YES SIGNAL for THIS slice, with NO EARLY DISPROOF.
- **Cannot settle (needs the full ceiling):**
  1. A genuine YES for the gravity leg. `G^X = 0` is trivial (any vacuum), and `W_s` is nonzero
     at `O(M^2/r^4)`, so exact Schwarzschild is NOT a Willmore-critical GU section. "Cheap-read
     clear" is not "leg cleared."
  2. The conditionality. The clear rides the W154 posit (`c_kin = 0`); if GU's connection
     carries any fundamental stiffness, the identity `theta = J` degrades and the theta term
     would need direct evaluation.
  3. A NON-vacuum (matter, `Psi != 0`) section. There `J != 0`, `theta = G * J != 0`, and
     `E_s^theta` is a genuine nonlocal Green's-function functional to be computed -- outside the
     vacuum gravity cheap-read.
  4. Kerr's Willmore term. The theta sector clears on Kerr (C6), but `alpha_W W_s` does not
     obviously clear there (harmonicity breaks); that is the highest-value remaining gravity
     computation.

## Binding

Exploration grade. NO canon / RESEARCH-STATUS / verdict movement:
`canon/schwarzschild-weak-field-rfail.md` stays OPEN; the gravity-leg verdict is Joe-gated. This
note reports a genuine-YES SIGNAL for the imported-metric slice (now with ALL FIVE `R_s` terms
accounted) and explicitly does NOT declare the leg verdict; the clear is CONDITIONAL on the one
W154 posit. No Lean/Lake build was run (Python/sympy only; a Lean port of the screened-Poisson
vacuum-source vanishing is a possible follow-up, noted not done). Personas inline
(IG-branch/theta specialist; screened-Poisson / induced-YM specialist; Krein-current / record
specialist; ruthless skeptic); one worker, no sub-agents. Reproducible:
`python -u tests/W236_gravity_theta_sector_residual.py` (exit 0; nonzero-source and
non-harmonic positive controls FIRST, both fire on real linear-in-M residuals). Zero em dashes
in paper-facing text.

*Filed 2026-07-15 by the gravity theta-sector wave (W236). Leg: GRAVITY /
ELProjectedGRShadowTheorem, imported-metric slice, `E_s^theta` term. VERDICT SIGNAL: W225's one
open term CLOSED -- imported Schwarzschild cheap-read FULLY CLEAR at linear order (conditional on
the W154 posit), no early disproof; Joe-gated leg verdict untouched.*
