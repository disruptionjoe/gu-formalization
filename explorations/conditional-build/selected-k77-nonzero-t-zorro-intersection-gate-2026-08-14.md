---
artifact_type: exact_composition_and_scope_correction
created: 2026-08-14
status: KNOWN_NONZERO_T_SOURCE_STATIONARY_BRANCHES_EXIST__BOTH_EXCLUDED_BY_CANONICAL_ZORRO_TRACE_CURVATURE__NATIVE_INTERSECTION_OPEN
lane_id: SRC-RES-COH-01
registry: lab/process/selected-k77-nonzero-t-zorro-intersection-gate.json
canon_verdict_change: none
---

# Selected-K77 nonzero-T/Zorro intersection gate

## Result first

GU does not need to construct an arbitrary nonzero-`T` stationary branch from
scratch. The repository already owns two exact homogeneous branches

```text
t_+ = (-2+sqrt(3))/208,  b_+ = 1/208-sqrt(3)/312,
t_- = (-2-sqrt(3))/208,  b_- = 1/208+sqrt(3)/312,
```

that solve the selected local source-variable bulk equations on the frozen
frame. All 1,470 known low-grade `varpi` rows, the 91 selected primitive-
epsilon bulk rows, the metric-volume row and the transported observation
covector vanish. Their endpoint momentum remains nonzero.

Neither branch is a native background for the canonical Zorro/DeWitt
reconstruction. That dependent connection has zero curvature on all nine
labelled trace--traceless planes, while each `B=b Phi1` branch is nonzero on
all nine. The intersection of the **currently owned homogeneous branch
family** with canonical `B_Z` legality is therefore empty.

The live construction is sharper:

```text
solve the true source Euler equations with canonical B_Z and nonzero T,
or derive a rival Zorro connection with nonzero mixed trace curvature.
```

The 14-row action cokernel from the predecessor remains exact but is
`T=F_varpi=0` scoped. It does not exclude a genuinely nonzero-`T` solve.

## Exact composition

The homogeneous equations are

```text
312(b+t)^2+t = 0,
624(b^2+bt+t^2/3)+t = 0.
```

Eliminating `b` gives

```text
97344 t^2 (43264 t^2+832 t+1)=0,
```

so the two displayed nonzero branches exhaust that frozen-frame family. The
source-tangent receipt separately proves bulk stationarity in the actual
local variables `(g,varpi,epsilon)`; an independent `B` variation at fixed
`T` remains a reconstruction diagnostic and endpoint momentum, not a missing
source bulk equation.

The newer curvature signature is independent of those Euler polynomials. Its
nine zero/nonzero comparisons are gauge invariant in the labelled canonical
reconstruction, so changing the representative inside either homogeneous
branch cannot repair the mismatch.

## Hostile ceiling

This result does not prove that Weinstein's abstract Zorro chain is unique,
that no nonzero-`T` canonical branch exists, or that GU has no stationary
background. The source still does not print the induced-`Y` connection
formula or a uniqueness theorem. A rival reconstruction is admissible only
after deriving its metric/connection formula and its nonzero mixed trace
curvature; relabelling `b Phi1` as distinguished is not admissible.

`SR-1` remains `BACKGROUND-MISSING` and `SR-2` remains blocked. No ledger,
canon, residue, quotient, datum or public-posture change follows. No positive
physical cohomology or superposition law is inferred.

## Reproduction

```bash
uv run --with-requirements requirements.txt python \
  tests/channel-swings/selected_k77_nonzero_t_zorro_intersection_gate_probe.py
```

The exact composition probe passes `25/25`.
