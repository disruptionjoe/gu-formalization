# H10 -- The PPN / weak-field solar-system bar for GU gravity

Wave 22. A cheap falsifier. Test: `tests/wave22/H10_ppn_weak_field.py` (deterministic, exit 0).

**One-line verdict: GATED-ON-mu_DW, effectively PASSES.** GU's tree-level gravity does *not*
force a solar-system-visible deviation. `gamma` and `beta` return to their GR values as an
*exponentially suppressed* Yukawa from the massive spin-2; the pass requires the free DeWitt
scale `mu_DW` above a floor of `~1e-17 eV`, which the natural `mu_DW ~ M_Pl` clears by ~45 orders
of magnitude. The solar-system PPN bar is far weaker than the pre-existing ghost-decoupling gate
(BAR 2) and adds no new binding constraint.

## The object

GU gravity (Waves 1-10) is a tree-level Stelle-clear: induced Einstein-Hilbert `R^X` + a `Weyl^2`
(Bach, 4th-order) term + a DeWitt `Lambda`, conditional on the soldering postulate + `mu_DW`. On
the transverse-traceless graviton the operator is `box(box + m2^2)` (H15/H25): a healthy massless
graviton plus one *distinct massive spin-2* of mass `m2`. The repo's computed inputs:

- H15: `|II|^2 = |H|^2 - R^X`; in 4D `int R^X` is dynamical -> Stelle `R + Weyl^2`, flat-ambient `m^2 = +1/2`.
- H25: curved-ambient `m^2_eff = 1/2 + C_RY`, with `C_RY` **computed positive** by two independent
  methods (`+1/3 -> m^2_eff = 5/6`; `+3/4 -> m^2_eff = 5/4`). Sign robust, O(1), positive.
- H24/H25 BAR 2: the physical mass is `m2^2 = m^2_eff * mu_DW^2`. `mu_DW` is the source-action overall
  scale (dimensionless ratios geometric, dimensionful magnitude free); natural `mu_DW ~ M_Pl`.

**Key structural fact (decisive for PPN):** GU's action is `R^X + Weyl^2 + Lambda` with **no `R^2` term**.
In quadratic gravity the massive spin-0 mass obeys `m0^2 ~ 1/beta_{R^2}`; with `beta_{R^2} = 0` the
scalar decouples (`m0 -> oo`). So GU gravity is *pure Einstein-Weyl* (`R + Weyl^2`): a massless
graviton + one massive spin-2, and **no propagating scalar ghost**. This is the cleanest PPN case.

## Q1 -- The modified Newtonian potential (COMPUTED structure + ARGUED solution)

General quadratic-gravity point-mass potential (Stelle 1978, GRG 9, 353):
`V(r) = -(GM/r)[1 + (1/3)e^{-m2 r} - (4/3)e^{-m0 r}]`. GU has no `R^2` term, so `m0 -> oo` kills
the `(4/3)` scalar Yukawa. The two Newtonian-order potentials:

```
Phi(r) (g_00) = -(GM/r)[1 + (1/3) e^{-m2 r}]
Psi(r) (g_ij) = -(GM/r)[1 - (1/3) e^{-m2 r}]
```

The massive spin-2 flips sign between the temporal and spatial potentials (the vDVZ `1/3`-trace
structure: massive spin-2 projector carries `-1/3` trace vs `-1/2` for the massless graviton). As
`m2 -> oo` both potentials collapse to the pure Newtonian `-GM/r`.

- **COMPUTED (this repo):** the `box(box + m2^2)` TT operator and `m^2_eff > 0` (H15/H25).
- **ARGUED (high confidence, cross-checked):** the explicit `Phi, Psi` are the standard linearized
  Einstein-Weyl solution of *that* operator, taken from Stelle 1978, not re-derived from GU's full
  `|II|^2` action here. Cross-checked against the vDVZ `gamma = 1/2` endpoint (Q2).

## Q2 -- PPN gamma and beta (COMPUTED)

`gamma(r) = Psi/Phi = (1 - (1/3)e^{-m2 r}) / (1 + (1/3)e^{-m2 r})`.

Cross-checks against known literature endpoints (guard against a linearization error):

- `gamma(m2 r -> 0) = 1/2` -- the vDVZ / Fierz-Pauli massive-graviton value (light bending 3/4 of GR).
- `gamma(m2 r -> oo) = 1` -- GR recovered.

Both endpoints reproduce the known Stelle / massive-spin-2 results, so the interpolation is
anchored, not an artifact. For the solar-system regime (`m2 r >> 1`):

`gamma - 1 = -(2/3) e^{-m2 r} + O(e^{-2 m2 r})` -- exponentially suppressed.

`beta -> 1` likewise (the nonlinear Yukawa correction is also `O(e^{-m2 r})`). The Cassini `gamma`
bound is ~4x tighter than the LLR `beta` bound, so `gamma` sets the binding lower bound on `m2`.

## Q3 -- The m2 lower bound and mu_DW consistency (COMPUTED)

Published bounds (comparison only, cited; not imported as targets):
- Cassini: `|gamma - 1| < 2.3e-5` (Bertotti, Iess, Tortora, Nature 425, 374 (2003)).
- LLR/Mercury: `|beta - 1| < 8e-5` (Williams, Turyshev, Boggs, PRL 93, 261101 (2004)).

`(2/3) e^{-m2 r} < 2.3e-5` gives `m2 r > 10.3`. Over a solar-system scale:

| scale `r` | `m2` lower bound | Yukawa range `1/m2 <` |
|---|---|---|
| 1 AU (`1.50e11 m`) | `6.9e-11 /m = 1.4e-17 eV` | `0.10 AU` |
| 1.6 R_sun (`1.11e9 m`) | `9.2e-9 /m = 1.8e-15 eV` | `0.16 R_sun` |

The bound on `m2` is fantastically small (`~1e-17 eV`): solar-system data only requires the
massive spin-2's Yukawa range to be shorter than `~0.1 AU`.

GU's `m2 = sqrt(m^2_eff) * mu_DW`, `m^2_eff in [5/6, 5/4]` (O(1), positive). Translating the floor:
`mu_DW > 1.5e-17 eV`. The natural `mu_DW ~ M_Pl = 1.2e28 eV` clears this by **~45 orders of magnitude**
(GU's massive spin-2 is Planckian, Yukawa range `~1e-35 m`, utterly unobservable). Critically, the
Cassini floor on `mu_DW` (`~1e-17 eV`) is *far weaker* than the ghost-decoupling bar (BAR 2, which
wants `mu_DW ~ M_Pl`): **the solar-system test adds no new binding constraint.**

## Q4 -- Verdict: GATED-ON-mu_DW, effectively PASSES

- **NOT FALSIFIED.** GU does not force a solar-system-visible deviation. `gamma, beta -> 1` as an
  exponentially suppressed Yukawa, not a structural O(1) shift. The wrong outcome (a light,
  long-range massive mode) is *not* forced: `m^2_eff` is O(1) and positive, so `m2` tracks `mu_DW`.
- **GATED-ON-mu_DW.** The pass is conditional on `mu_DW > ~1e-17 eV` (inverse-`~0.1 AU`). This floor
  is ~45 orders below the natural (and BAR-2-required) `M_Pl`; any non-pathological scale clears it.
- The adversarial cross-check (vDVZ `gamma = 1/2`; GR `gamma = 1`) confirms no linearization error.

## COMPUTED vs ARGUED

| Claim | Status | Confidence |
|---|---|---|
| GU = Einstein-Weyl (no `R^2` -> no scalar Yukawa) | COMPUTED (repo: `R^X + Weyl^2 + Lambda`) | high |
| TT operator `box(box + m2^2)`, `m^2_eff > 0` | COMPUTED (H15/H25) | high |
| `Phi, Psi` explicit form, `+1/3` coefficient | ARGUED (Stelle 1978 solution of that operator) | high (cross-checked to vDVZ) |
| `gamma(r)`, `gamma - 1 = -(2/3)e^{-m2 r}`, endpoints `1/2`, `1` | COMPUTED (from `Phi, Psi`) | high |
| `m2 > ~1e-17 eV`, `mu_DW > ~1e-17 eV` floor | COMPUTED (Cassini + `m^2_eff`) | high |
| natural `mu_DW ~ M_Pl` clears by ~45 decades | COMPUTED | high (given the natural-scale premise) |

## Honest limits

- The potential and the `+1/3` coefficient are the standard linearized Einstein-Weyl (Stelle 1978)
  solution of `box(box + m2^2)`, not a from-scratch linearization of GU's full `|II|^2` action. This
  is legitimate because the repo already computed that GU's TT operator *is* `box(box + m2^2)`; only
  the known weak-field solution of that operator is imported, and it is cross-checked to the vDVZ
  endpoint.
- The absence of the scalar Yukawa rests on GU having no `R^2` term. If a source-action build later
  induces an `R^2` term, a second spin-0 Yukawa `-(4/3)e^{-m0 r}` appears; its `m0` would need the
  same (trivially cleared) heavy-mass floor. Not currently present.
- `mu_DW`'s dimensionful value is not derived (H24/H25 BAR 2). The solar-system bar constrains it
  only to `> ~1e-17 eV` -- far weaker than BAR 2's `~M_Pl`.
- Loop-level unitarity (BAR 1) is untouched; PPN is a purely tree-level / classical test.

## RE-RANK signal

**GATED-ON-mu_DW** (bound: `mu_DW > ~1e-17 eV`, i.e. inverse-`~0.1 AU`), cleared by ~45 orders for
the natural `mu_DW ~ M_Pl` -> **effectively PASSES**. The solar-system PPN test does not falsify GU
and does not tighten the pre-existing `mu_DW` gate.

**Single next object:** the ghost-mass scale `mu_DW` itself (H24/H25 BAR 2) -- the one dimensionful
datum the whole gravity sector now hangs on. Every gravity bar (ghost decoupling, PPN) reduces to
whether the source action pins `mu_DW ~ M_Pl`. PPN confirms this is the binding question and that
its solar-system floor is 45 orders below the natural value.
