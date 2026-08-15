---
title: "Selected-K77 VRS-5 curvature/VEV reopener qualification"
status: active_research
doc_type: exact_composition_and_rerank
created: "2026-08-14"
registry: lab/process/selected-k77-vrs5-curvature-vev-reopener-qualification.json
probe: tests/channel-swings/selected_k77_vrs5_curvature_vev_reopener_qualification_probe.py
grade: "EXACT BRANCH/CURVATURE DISJOINTNESS AND REVERSE-SCAFFOLD RERANK"
canon_verdict_change: none
---

# Selected-K77 VRS-5 curvature/VEV reopener qualification

## Result first

The repository's strongest action-owned trace hypothesis is real, but it does
not reopen the canonical SR-1C branch just killed.

The 2026-08-09 scalar-jet construction closes its trace inside the selected
first action without a new field, coupling or counterterm:

```text
B = Phi1/208,   T = -Phi1/104,   r = 1/129792.
```

That remains a high-conviction result. Exact composition with the canonical
Zorro receipts now shows that it is a **different carrier**. Its full
`B` curvature is

```text
F_B = (b^2+r)(Phi1 wedge Phi1)
    = (1/32448)(Phi1 wedge Phi1).
```

It is nonzero on all nine labelled trace--traceless planes on which the
canonical Zorro/DeWitt curvature is zero. The canonical curvature `F_BZ` is
also not a scalar multiple of `C=Phi1 wedge Phi1`: `C` has 91 cells, `F_BZ`
has 107 coefficients on 25 form legs, their supports overlap in only 25
cells, and the overlap already has six distinct ratios.

The branches are algebraically disjoint as well. The old amplitude
`t=-1/104` evaluates the SR-1C polynomial to

```text
28392t^2+91t-351 = -1397/4.
```

Therefore the old source-owned trace closure receives **no vote as a direct
graft onto SR-1C**. It retains high conviction as a distinct scalar-jet
background hypothesis whose missing task is a canonical connection
realization and full derivative Euler/atlas descent.

The highest-information next swing is `SR-1D`: test the nonparallel canonical
source-graph image before constructing another large branch. Build the exact
combined second-jet map subject to differentiated translation and Bianchi
rows, then ask whether its primitive-epsilon kernel can emit the opposite of
the known rank-one metric trace through

```text
(D_g B_Z)^!(E_B-E_T) = -rho L1.
```

An image witness reopens the same two point roots with a genuinely different
two-jet. A cokernel certificate kills **all** compatible nonparallel two-jets
over both roots at once and promotes the search to a distinct canonical
branch or reconstruction.

## The generous no-fit control

Even ignoring the curvature-orbit mismatch and importing the old scalar cell
with its own finite-model action normalization gives no automatic
cancellation. On the current quadratic algebra, the scalar value needed to
cancel the metric density is

```text
r_required = (27+728t^2)/4368 = 3/364-t/1872.
```

It is root-dependent, not one fixed rational value on both embeddings. The
old solved value `1/129792` cancels neither root. If the new curvature is
placed in canonical `F_B` and its change is compensated in `DT` to preserve
the endpoint curvature, transgression supplies half the response and the
required value is still root-dependent:

```text
r_required_endpoint = 3/182-t/936.
```

These are counterfactual controls, not permission to add `r`. For canonical
`B_Z`, curvature is metric-derived and fixed; an independently chosen scalar
cell would be a new reconstruction degree of freedom unless derived from the
same metric/connection jet.

## Rerank

1. **First — canonical nonparallel source-graph image/cokernel gate.** It is
   the nearest action-owned mechanism capable of producing the exact opposite
   trace without a new coefficient. Solve only after the constrained image is
   known.
2. **Second — genuinely distinct canonical branch or connection jet.** Enter
   this horn if the combined SR-1D cokernel excludes the current roots.
3. **High conviction, not a current vote — scalar curvature/VEV branch.** Its
   no-fit action cancellation is exact, but its canonical realization and
   full derivative Euler remain missing and its curvature orbit is disjoint
   from `B_Z`.

## Successor scaffold

The next series should be narrower than another unconstrained branch solve:

```text
SR-1D-A  serialize the allowed nonparallel second-jet variables;
SR-1D-B  assemble differentiated E_T and inherited Bianchi constraints;
SR-1D-C  restrict to primitive-epsilon zero;
SR-1D-D  project the fixed-varpi graph adjoint onto the one-dimensional
         metric-trace receiver;
SR-1D-E  compute image rank and an exact witness or left-cokernel certificate;
SR-1D-F  only for a witness, recompute every translation, epsilon and total
         metric row on the same algebraic carrier and prolong once.
```

The branch polynomial should be retained symbolically until the final image
test so one calculation covers both real embeddings. A witness must not reuse
the parallel `j1p=0` certificate; a kill must not claim source-global
nonexistence.

## Claim ceiling

This qualification does not retract the scalar-jet closure, prove that it has
no canonical realization, exclude every action-owned trace sector, or kill
every canonical branch. It proves only that the owned scalar construction is
not the current canonical SR-1C carrier and does not cancel its trace without
a new root-dependent graft.

`SR-1` remains `BACKGROUND-MISSING`, `SR-2` remains blocked and VRS-6 has no
background premise. No ledger, canon, residue, quotient datum or public
posture changes. No physical cohomology, superposition law, Born rule,
spectrum or empirical prediction follows.

Reproduce with:

```bash
sage -python \
  tests/channel-swings/selected_k77_vrs5_curvature_vev_reopener_qualification_probe.py
```

The exact qualification probe passes `34/34`.
