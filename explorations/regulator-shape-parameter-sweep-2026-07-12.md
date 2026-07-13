---
artifact_type: exploration
status: exploration
created: 2026-07-12
hypothesis: "W85 condition (i) follow-up: does the Reuter fixed point robustness survive a regulator shape-parameter sweep, not merely a single second regulator?"
branch: "W86 regulator-shape sweep over r_s(y)=s*y/(e^y-1)"
grade: "computed / proxy. Deterministic test tests/W86_regulator_shape_sweep.py, exit 0. The sweep computes threshold positivity, reduced fixed-point existence/value motion, a positive f0 relevance-drive proxy, and RS anti-screening sign stability across the reduced-model viability window s in {0.35,0.50,0.75,1.00,1.20}. It does not run the full combined f(R)+Weyl^2 + ker-Gamma spin-3/2 FRG computation."
depends_on:
  - explorations/second-regulator-reuter-fp-2026-07-11.md
  - tests/W85_second_regulator_reuter.py
  - explorations/frg-fr-weyl-af-as-fork-2026-07-11.md
  - tests/W83_frg_fr_weyl_af_as.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W86_regulator_shape_sweep.py
---

# Regulator Shape-Parameter Sweep

## Role

W85 brought one genuinely different second regulator, the exponential shape
`r(y)=y/(e^y-1)`, against the W81/W83 Litim baseline. Its next valid swing named a third-regulator /
shape-parameter sweep. W86 executes the bounded version:

```text
r_s(y) = s*y/(e^y-1),  s in {0.35, 0.50, 0.75, 1.00, 1.20}
```

The goal is not to freeze non-universal fixed-point coordinates. In FRG those values are allowed to move.
The check is whether the qualitative gates W85 depends on stay intact across a shape family.

## Construction Forks

| Object | Construction Used | Boundary |
|---|---|---|
| Regulator | Calculational FRG shape convention, not a physics primitive | Values may move; invariant-style signs and existence are the meaningful checks. |
| Fixed point | Reduced Reuter proxy with regulator dependence carried by threshold weights | Tests existence/value-motion discipline, not a full functional FRG computation. |
| `f0` relevance | Positive de-slaving/relevance-drive proxy, `g*` times positive threshold weight | Does not compute the combined critical exponent. |
| RS sign | W85 factorization: heat-kernel/spin coefficient sign times positive threshold | Checks sign stability; magnitude and ker-Gamma projection remain open. |

## Result

`tests/W86_regulator_shape_sweep.py` passes. The sweep finds:

- Threshold functions `Phi_n^p(0)` remain positive and finite for every sampled shape.
- The sweep is nontrivial: threshold values move substantially as `s` changes.
- The reduced Reuter fixed point exists for every sampled shape.
- `g*` and `lambda*` move, as expected for regulator-dependent coordinates.
- The mapped `g*lambda*` band stays finite/order-stable in the reduced proxy.
- The `f0` relevance-drive proxy stays positive across the sweep.
- GU's ker-Gamma RS anti-screening sign is unchanged: `A_tot` remains positive and adding RS raises it for every sampled shape.
- The scalar-heavy refutation guard remains live, so the preservation is still content-conditional rather than automatic.

Verdict: **SHAPE-STABLE at first-swing/proxy grade**.

## What This Changes

W86 strengthens W85 condition (i) by showing that the qualitative support is not tied to one exponential
normalization. The AS/Reuter branch remains less fragile than the AF escape route needs it to be.

## What It Does Not Change

This is still not a full combined `f(R)+Weyl^2 + ker-Gamma spin-3/2` FRG run. The W85 residual remains:

- I2/I3 are still partly ported from known FRG robustness rather than recomputed for the full combined GU object.
- The ker-Gamma RS coefficient magnitude under a full second-regulator heat-kernel remains uncomputed.
- The W79 tachyon-genuineness / beyond-fourth-order `|II|^2` gate is untouched.

No claim status, canon verdict, `RESEARCH-STATUS.md`, `CANON.md`, public posture, or absorbed-source file is
changed.

The pass/fail sweep is deliberately restricted to the reduced model's viability window `0 < lambda* < 1/2`.
Wider amplitudes are diagnostic for regulator sensitivity, but this receipt does not count them as fixed-point
existence checks for the reduced proxy.

## Next Valid Swing

The highest-value follow-up is still the full combined functional computation. If that is too large for an
hourly run, the next bounded swing should attack W85's condition (ii): whether the W79 tachyon is a genuine IR
inconsistency once beyond-fourth-order `|II|^2` invariants are allowed.
