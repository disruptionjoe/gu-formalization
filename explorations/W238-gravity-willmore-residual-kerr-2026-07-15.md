---
artifact_type: exploration
label: W238
created: 2026-07-15
status: exploration (GRAVITY LEG, the LAST independent gravity frontier; imported exact Kerr; surviving conservative IG branch; Psi=0 gravitational vacuum; linear order in M with rotation parameter a carried EXACTLY; harmonic (Lorenz) gauge; personas inline, one worker, no sub-agents; deterministic sympy test with a rotation-sector non-harmonic positive control that FIRES on a real linear-in-M-and-a residual, plus the a->0 Schwarzschild-zero control, exit 0)
posture: coherence-first (Joe 2026-07-14); exploration grade; adversarial, native-object first, truth-seeking (clearing the Willmore term on Kerr EXTENDS the gravity cheap-read to the rotating metric; a nonzero non-gauge-removable linear residual would have been an EARLY DISPROOF SIGNAL; reported either way, no rooting)
title: "W238 -- native Willmore mean-curvature residual alpha_W W_s on imported exact Kerr (the last independent gravity frontier; closes the Kerr Willmore term W236 left open)"
leg: GRAVITY -- ELProjectedGRShadowTheorem, imported-metric slice, alpha_W W_s term on KERR
grade: "alpha_W W_s = alpha_W Delta H^(1) = 0 IDENTICALLY at linear order in M on imported Kerr, a carried exactly: COMPUTED (sympy, exact -- the native mean curvature H^(1)_ab of the linearized graph section, built by the same W225/willmore_el_order machinery now with the Kerr gravitomagnetic h_0i and the a^2 mass quadrupole, has Delta H^(1)_ab = 0 for all 10 components). STRUCTURAL (the residual is a constant-coefficient linear image of the per-component Laplacian Delta h; linearized STATIONARY VACUUM in Lorenz gauge gives nabla^2 h_mn = 0 componentwise, so H^(1) is a const-coeff linear combination of harmonic functions -> harmonic -> Delta H^(1)=0, for the FULL a-exact Kerr multipole tower, not just leading a; verified with free-coefficient generic harmonic combo). a->0 consistency: EXACT (reproduces the Schwarzschild H^(1)=(M/r)eta_ab with zero off-diagonal, W225/RFAIL-03). Assembly with W225 (four other terms) + W236 (theta, rotation-independent): COMPUTED/SOURCE-AUDIT. Gauge-removability of any non-harmonic appearance in a non-harmonic chart (e.g. raw Boyer-Lindquist): STRUCTURAL (harmonicity is a gauge statement; the harmonic chart exists)."
depends_on:
  - explorations/W225-gravity-projected-shadow-schwarzschild-cheap-read-2026-07-15.md
  - explorations/W236-gravity-theta-sector-residual-built-action-2026-07-15.md
  - canon/schwarzschild-weak-field-rfail.md
  - tests/chase/MOVE-3/willmore_el_order.py
  - explorations/geometry-curvature-emergence/exact-schwarzschild-kerr-el-gate-2026-06-24.md
  - explorations/geometry-curvature-emergence/gr-shadow-recovery-certificate-2026-06-24.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W238_gravity_willmore_residual_kerr.py
primary_source:
  - "Geometric_UnityDraftApril1st2021.pdf (E. Weinstein), sec 9 (Bosonic action, shiab, section equation)"
external_refs:
  - "R. P. Kerr, Phys. Rev. Lett. 11 (1963) 237 -- the rotating vacuum solution"
  - "R. M. Wald, General Relativity, U Chicago Press 1984, ch. 6/11 (Kerr, multipoles, Lense-Thirring)"
  - "T. J. Willmore, Riemannian Geometry, OUP 1993 (Willmore energy, first variation Delta H)"
  - "R. Geroch (1970) / R. Hansen (1974) -- stationary-vacuum multipole moments (Kerr: M_l = M(ia)^l), harmonic in Lorenz gauge"
---

# W238 -- native Willmore residual alpha_W W_s on imported exact Kerr (the last independent gravity frontier)

## Result in one paragraph

The gravity cheap-read had ONE independent term left whose Schwarzschild clear was not known to
survive rotation: the native Willmore mean-curvature residual `alpha_W W_s` on Kerr. W225 cleared
it on Schwarzschild because the native mean curvature is `H^(1)_ab = (M/r) eta_ab`, which is
HARMONIC (`Delta(M/r)=0`, canon RFAIL-03); W236 cleared the theta sector on both Schwarzschild AND
Kerr (rotation-independent, needs only `Psi=0`). The open worry was that W225's harmonicity looked
like a STATIC-ISOTROPIC accident (`h_ij = 2phi delta_ij`), and rotation breaks static isotropy --
Kerr adds a gravitomagnetic frame-dragging cross term `h_0i` and anisotropic mass multipoles.
**Computed on IMPORTED exact Kerr in harmonic (Lorenz) gauge, `Psi=0` vacuum, conservative IG
branch, at linear order in `M` with the rotation parameter `a` carried EXACTLY: the native mean
curvature `H^(1)_ab` (built by the SAME W225/`willmore_el_order` machinery, now including the
gravitomagnetic `h_0i` and the `a^2` mass quadrupole) has `Delta H^(1)_ab = 0` for ALL ten
components, so the linear-in-M native Willmore-EL residual `alpha_W W_s = alpha_W Delta H^(1) = 0`
identically, for any finite `alpha_W`.** The reason W225's clear survives is structural and settles
the worry: W225's harmonicity was SUFFICIENT but not NECESSARY. The native mean curvature is a
CONSTANT-COEFFICIENT LINEAR functional of the metric-perturbation components
(`H^(1)_ab = eta^{mn}(d_m d_n h_ab + alg_lin(h))`), so it is harmonic whenever EACH component
`h_ab` is harmonic -- regardless of anisotropy, off-diagonal cross terms, or rotation. And
linearized STATIONARY VACUUM Einstein gravity in Lorenz gauge gives exactly that
(`nabla^2 hbar_mn = -16pi T_mn = 0` in vacuum), so every Cartesian component of Kerr's linear-in-M
field is harmonic; rotation only changes WHICH harmonic functions appear (adds `h_0i` and the
`a`-dependent multipoles), never whether they are harmonic. Isotropy was never load-bearing.
**VERDICT SIGNAL: the native Willmore residual CLEARS on imported Kerr at linear order; combined
with W236 (theta clears on Kerr) and W225's other rotation-independent terms, ALL FIVE `R_s` terms
are zero at linear order on the ROTATING metric too -- the gravity cheap-read EXTENDS TO KERR, a
genuine-YES SIGNAL for the imported-metric slice, with NO EARLY DISPROOF.** The `a->0` limit
reproduces the Schwarzschild `H^(1)=(M/r)eta_ab` with zero off-diagonal exactly. This does NOT
clear the gravity leg: `G^X=0` is trivial (any vacuum), `W_s` is nonzero at `O(M^2)` (the standing
`Q(B)` quadratic obstruction, same as Schwarzschild, safe for `M/r<<1`), so exact Kerr is NOT a
Willmore-critical GU section; a non-vacuum matter section (`Psi != 0`) remains; and the theta clear
still rides the W154 posit (W236). Verdict is Joe-gated; canon `schwarzschild-weak-field-rfail.md`
stays OPEN.

## Construction fork (stated, not defaulted)

Three GU objects have a native-vs-physics fork here; each is named per
`GEOMETER-VS-PHYSICS-OBJECTS.md`:

1. **Gravity functional -- PROGRAM-NATIVE `|II|^2`.** The section residual `W_s` is the
   Euler-Lagrange residual of the Willmore energy `E[s] = integral |II_s^H|^2` (native second
   fundamental form of `X^4 -> Y^14`), NOT a free `R^2 / Weyl^2` Lagrangian. This is the
   construction the table settled toward the native side (row: Gravity functional), and it is the
   object whose linear residual `Delta H^(1)` I compute. I use the identical `B^(1)`/`H^(1)`
   machinery as W225 (`tests/chase/MOVE-3/willmore_el_order.py`), only swapping the imported base
   metric.

2. **The metric -- STANDARD-physics import, in HARMONIC (Lorenz) GAUGE.** The exact Kerr BASE
   metric is imported as the vacuum solution; its linear-in-M part is taken in harmonic-gauge
   Cartesian coordinates -- the physics-standard choice, and the one that makes the slice "cheap"
   (no source action needed). Naming the gauge is LOAD-BEARING here in a way it was not for
   Schwarzschild: harmonicity of the components is a GAUGE statement. In raw Boyer-Lindquist
   coordinates the `M=0` background is flat space in oblate spheroidal coordinates (not literal
   `eta`), and a naive component read there is not manifestly harmonic. The harmonic chart is where
   the native clear is manifest, and the "gauge-removable" branch of the pre-declared verdict is
   exactly the statement that any apparent non-harmonic piece in a non-harmonic chart is removed by
   transforming to the harmonic chart (which exists for any linearized stationary vacuum field). I
   do NOT conflate the imported base metric with the gimmel/fiber metric-on-metrics; `H^(1)` is the
   mean curvature of the graph section into the fiber `Met(X^4)`.

3. **Signature `(9,5)` vs `(7,7)` -- fork does NOT bite.** As in W225, the only datum that moves
   `p-q` is the base metric-sign convention, physically vacuous here. `Delta H^(1) = 0` is
   convention-independent, so the cheap-slice verdict is identical on both sides of the signature
   fork.

Because the load-bearing result (a vanishing linear residual by per-component harmonicity) holds on
the native functional, is convention-independent, and is gauge-manifest in the harmonic chart,
there is no surviving construction in which this slice produces a linear falsifier on Kerr. That is
the honest reason there is no EARLY DISPROOF.

## The residual, term by term (on imported Kerr, Psi=0, IG branch, linear in M, a exact)

`R_s = alpha_W W_s + E_s^YM + E_s^theta + E_s^Phi + E_s^cross`.

| term | what it is | linear-in-M part on Kerr | grade |
|---|---|---|---|
| `alpha_W W_s` | Willmore section EL residual (native `|II|^2`) | **`alpha_W Delta H^(1) = 0` (harmonic on Kerr too)** | **COMPUTED/STRUCTURAL (THIS WAVE)** |
| `E_s^YM` | gauge-curvature contribution `~ F_A^2` | `0` (`F_A ~ O(M^2)`, F2; rotation-independent) | COMPUTED/SOURCE-AUDIT (W225) |
| `E_s^theta` | branch-fixed geometric-theta residual | `0` (`Psi=0 => J=0 => theta=0`; rotation-independent) | COMPUTED/STRUCTURAL (W236 C6) |
| `E_s^Phi` | scalar/Higgs source | `0` (`Phi = 0` in vacuum; rotation-independent) | EXACT (W225) |
| `E_s^cross` | cross terms | `0` (vanishing `Psi/Phi` factor; rotation-independent) | EXACT (W225) |

The single term whose Schwarzschild argument was rotation-fragile (`alpha_W W_s`) is now closed on
Kerr. Every term contributes zero at linear order on the rotating metric; the leading BUILT
contribution is quadratic `O(M^2)` -- the standing `Q(B)` obstruction, the SAME object as
Schwarzschild -- which is safe for `M/r << 1`.

## Worked computation

**The imported metric (harmonic gauge, linear in M, a exact).** I take the linear-in-M part of
exact Kerr in the standard stationary weak-field harmonic form
`g_00 = -(1+2Phi)`, `g_ij = (1-2Phi) delta_ij`, `g_0i = h_0i`, with:

```
phiN = M/r                                  Newtonian monopole
quad = M a^2 (3 z^2 - r^2) / (2 r^5)        Kerr mass quadrupole (M_2 = -M a^2, l=2 solid harmonic)
Phi  = phiN + quad
h_0i ~ (S x x)_i / r^3,  S = (0,0,M a)      gravitomagnetic frame drag (Lense-Thirring):
       h_0x = -4 * (-M a y / r^3),  h_0y = -4 * (M a x / r^3),  h_0z = 0
```

so `h_00 = 2Phi`, `h_ii = 2Phi`, plus the off-diagonal `h_0i`. The gravitomagnetic term is the
genuinely NEW rotation structure with no Schwarzschild analog; it is linear in `M a` and switches
off as `a->0`. (Exact overall coefficients of `h_0i` are irrelevant to the residual, which tests
harmonicity; the physically correct frame-drag FORM is used.)

**Every component is harmonic (C1).** Direct sympy: `Delta(M/r) = 0`,
`Delta(M a^2 (3z^2-r^2)/(2r^5)) = 0` (an `l=2` solid harmonic), `Delta(M a y/r^3) = 0` and
`Delta(M a x/r^3) = 0` (since `x_j/r^3 = -partial_j(1/r)`, the gradient of a harmonic function).
This is the general fact: linearized stationary vacuum in Lorenz gauge has
`nabla^2 hbar_mn = -16 pi T_mn = 0`, so each Cartesian component is harmonic. Kerr's linear-in-M
field is the Lorenz-gauge field of the Kerr multipole tower (`M_l = M(ia)^l` and the
angular-momentum/current tower), ALL linear in `M`; every multipole is an exterior harmonic
function.

**Native mean curvature and its residual (C2).** Using the identical W225 machinery -- the
literal-graph vertical second fundamental form `B^(1)_{mn,ab} = d_m d_n h_ab + alg_lin(h)` (flat
reference subtracted) and `H^(1)_ab = eta^{mn} B^(1)_{mn,ab}` -- on the Kerr `h`, sympy returns a
nonzero mean-curvature vector carrying `a`:

```
H^(1)_00 = M(a^2 x^2 + a^2 y^2 - 2 a^2 z^2 - 2 r^4)/(2 r^5)      [ = -M/r - (a^2 quadrupole piece) ]
H^(1)_ii = -H^(1)_00   (i=1,2,3)                                  [ = +M/r + (a^2 quadrupole piece) ]
H^(1)_0i : the frame-drag contribution (nonzero at O(M a))
```

and then `Delta H^(1)_ab = 0` for ALL ten symmetric components (exact sympy). Hence
`alpha_W W_s = alpha_W Delta H^(1) = 0` on imported Kerr at linear order, for any finite `alpha_W`.
The harmonicity of `H^(1)` is inherited: `H^(1)_ab = Box h_ab + (const-coeff linear combo of h_cd)`
is a constant-coefficient linear image of harmonic functions.

**a->0 consistency (C3).** Setting `a=0`: the gravitomagnetic term and the `a^2` quadrupole vanish,
and `H^(1)_ab` collapses to `diag[-M/r, M/r, M/r, M/r] = (M/r) eta_ab` with all off-diagonal
components (including the frame-drag `H^(1)_0i`) zero -- EXACTLY W225 / RFAIL-03. `Delta H^(1) = 0`
in the limit, reproducing the Schwarzschild zero. The rotation sector switches off cleanly.

**Structural, a-exact (C4).** The vanishing used ONLY per-component harmonicity of the linearized
vacuum field and the constant-coefficient-linear structure of the mean-curvature functional. To
witness that it is not tied to the sampled `a`-terms, I feed a GENERIC harmonic multipole
combination with FREE coefficients `c0 (M/r) + c1 (M a y/r^3) + c2 (M a^2 (3z^2-r^2)/(2r^5))` into
the same machinery: it is harmonic for all `c_i`, and `Delta H^(1) = 0` for all `c_i`. So the clear
holds for the FULL `a`-exact Kerr multipole tower, not just leading rotation order.

**Positive controls (PC1, PC2) -- teeth, including in the rotation direction.** PC1: a NON-harmonic
mock frame-drag `h_0i ~ M a y/r^2` (wrong radial power) has `Delta(M a y/r^2) = -2 M a y/r^4 != 0`,
a linear-in-M residual that is ALSO linear in `a` (vanishes as `a->0`) -- so a genuine
ROTATION-induced Willmore residual WOULD register; the `a`-carried vacuum vanishing is not a blind
spot in `a`. PC2: the retracted premise `H = M/r^2` has `Delta(M/r^2) = 2M/r^4 != 0` (same teeth as
W225 PC2). Both controls fire.

## Reconciliation with priors

- **W225 (Schwarzschild Willmore).** W238 is the direct rotation generalization. W225's
  `H^(1)=(M/r)eta` harmonicity is the `a->0` special case (C3). The apparent "static-isotropy
  accident" is explained: harmonicity of `H^(1)` needs only per-component harmonicity of `h`, which
  isotropy sufficed to supply but did not monopolize.
- **W236 (theta sector).** W236 C6 already showed the theta sector clears on Kerr
  (rotation-independent, needs only `Psi=0`) and explicitly named the Willmore term on Kerr as "the
  highest-value remaining gravity computation." W238 closes exactly that term. Together W236+W238
  clear the two rotation-fragile-looking terms; W225's remaining terms are rotation-independent.
- **canon/schwarzschild-weak-field-rfail (RFAIL-03).** RFAIL-03's harmonicity mechanism
  (`Delta(M/r)=0`) is the Schwarzschild instance of the general per-component-harmonicity structural
  fact this wave isolates. No canon movement; RFAIL stays OPEN.
- **exact-schwarzschild-kerr-el-gate (2026-06-24).** That gate warned "Kerr has the same structural
  danger plus rotation-dependent residuals" and quoted the RETRACTED `H_Schw ~ M/r^2` premise. W238
  resolves the linear-order part of that danger: at linear order in `M` there is NO rotation-induced
  Willmore residual; the "danger" is the `O(M^2)` quadratic `Q(B)` obstruction, the same standing
  safe object as Schwarzschild, not a linear falsifier.

## What this slice can and cannot settle (honest limits)

- **Can settle (imported-metric, Psi=0 vacuum, linear order, a exact):** there is NO linear-in-M
  falsifier from the native Willmore term on Kerr; `Delta H^(1) = 0` for all components, structurally
  and a-exactly; combined with W225's other terms and W236's theta term (both rotation-independent),
  the full `R_s` has NO linear-in-M falsifier on the rotating metric and the leading built residual
  is quadratic `O(M^2) = Q(B)`, safe. The imported-metric cheap-read EXTENDS TO KERR: a genuine-YES
  SIGNAL, with NO EARLY DISPROOF.
- **Cannot settle (needs the full ceiling):**
  1. A genuine YES for the gravity leg. `G^X = 0` is trivial (any vacuum), and `W_s` is nonzero at
     `O(M^2)`, so exact Kerr is NOT a Willmore-critical GU section. "Cheap-read clear on Kerr" is not
     "leg cleared."
  2. The `O(M^2)` quadratic residual on Kerr. `Q(B)` is nonzero and rotation now enters it; whether
     the rotating `O(M^2)` residual differs structurally from Schwarzschild's is a separate (higher
     -order) computation. It is the standing genuine obstruction, safe for `M/r<<1`, not a linear
     falsifier -- but it is not zero.
  3. The theta-sector conditionality (inherited from W236): the theta clear rides the W154 posit
     (`c_kin=0`, marble/wood emergence, only its sign forced).
  4. A NON-vacuum (matter, `Psi != 0`) section, where `J != 0`, `theta = G*J != 0`, and the source
     terms are genuine nonlocal functionals -- outside the vacuum cheap-read.

## Binding

Exploration grade. NO canon / RESEARCH-STATUS / verdict movement:
`canon/schwarzschild-weak-field-rfail.md` stays OPEN; the gravity-leg verdict is Joe-gated. This
note reports a genuine-YES SIGNAL for the imported-metric slice on the ROTATING (Kerr) metric --
the last independent gravity frontier at linear order -- and explicitly does NOT declare the leg
verdict. No EARLY DISPROOF was found; no Joe-gated verdict was touched (the clear is reported as a
SIGNAL only). No Lean/Lake build was run (Python/sympy only; a Lean port of the
per-component-harmonicity -> Willmore-residual-vanishing lemma is a possible follow-up, noted not
done). Personas inline (GR/Kerr-curvature specialist; Willmore/immersion-variational specialist;
Lorenz-gauge/linearized-vacuum specialist; ruthless skeptic); one worker, no sub-agents.
Reproducible: `python -u tests/W238_gravity_willmore_residual_kerr.py` (exit 0; rotation-sector
non-harmonic and non-harmonic-H positive controls FIRST, both fire on real linear-in-M residuals,
PC1 also linear in a). Zero em dashes in paper-facing text.

*Filed 2026-07-15 by the gravity Willmore-on-Kerr wave (W238). Leg: GRAVITY /
ELProjectedGRShadowTheorem, imported-metric slice, `alpha_W W_s` term on Kerr. VERDICT SIGNAL: the
last independent gravity frontier CLEARS -- the native Willmore residual vanishes on imported Kerr
at linear order (`a` exact), so the gravity cheap-read EXTENDS TO KERR; no early disproof; Joe-gated
leg verdict untouched.*
