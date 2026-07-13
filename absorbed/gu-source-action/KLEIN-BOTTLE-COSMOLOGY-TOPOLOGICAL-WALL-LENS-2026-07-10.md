# Klein Bottle Cosmology Topological-Wall Lens

Date: 2026-07-10

Status: external exploration lens, not GU evidence and not a source-action result.

## Source

External paper:

```text
Brian Greene, Daniel Kabat, Janna Levin, Massimo Porrati
"Klein Bottle Cosmology"
arXiv:2511.23447
https://arxiv.org/abs/2511.23447
```

The paper studies a higher-dimensional universe modeled as Minkowski space times
a nonorientable Klein bottle.  The useful pattern for this repo is that global
nonorientable topology breaks symmetries, enforces a localized fermion
condensate wall/order parameter, and can make brane fermion production depend on
motion through that wall.

## Why This Is Relevant Here

The current GU source-action blocker is:

```text
DERIVATIVE-TAU-HOMOMORPHISM
```

The finite-fiber source-Noether/tau solve in
`SOURCE-NOETHER-TAU-CARRIER-PACKET-2026-07-10.md` derives the projected map

```text
A = Pi_ker(Gamma) d_A
```

as a Schur complement, but Noether alone leaves arbitrary tangent maps in
`ker Gamma` unselected.  That means a real source action still needs a
derivative-level or global datum that selects the tangent part without falling
back to a fixed projector rule.

The Klein-bottle paper is useful as a model template because the order parameter
is not chosen locally.  It is forced by global topology and boundary conditions.
That is the kind of mechanism the GU source-action search needs to test:

```text
Can a global/topological boundary condition force the tau tangent selector?
```

## Guardrails

This note does not assert any of the following:

- GU has Klein-bottle extra dimensions.
- GU's `Y^14` should be replaced by a Klein bottle.
- The paper supports the generation count.
- A condensate wall is already the GU source action.
- CP violation, baryogenesis, or brane motion in the paper should be imported as
  GU data.

The paper is only an external analogy for a mechanism class:

```text
global topology -> forced localized order parameter -> tangent/source selection
```

## Repo-Useful Tests Suggested By The Lens

1. **Topology-forced tangent selector probe.**
   Try to model an involutive or nonorientable boundary condition that produces
   a nonzero tangent map `Z : S -> ker Gamma`, then test whether
   `Gamma(Pi_ker(Gamma)d_A + Z) = 0` while `Z` is not a fixed-projector choice.

2. **Order-parameter carrier test.**
   Require the proposed tangent selector to arise as a source current or wall
   order parameter, not as an arbitrary element of `ker Gamma`.

3. **Anti-projector absorber test.**
   If the construction returns `Z = 0`, or if `Z` is picked only by minimizing a
   norm, classify it as the already-known Schur-projector solution rather than a
   new source carrier.

4. **Anchor preservation test.**
   Any wall/topology-inspired carrier must preserve:

   ```text
   ||Pi_RS M_D - M_D Pi_RS|| = 58.7215
   ||Gamma M_D Pi_RS|| = 155.3625
   ```

5. **No-target-import test.**
   The carrier may not use `24`, `24/8`, `chi(K3)=24`, `ch2=24`, fitted
   holonomy, fitted rank, or the paper's baryogenesis target as GU input.

## Decision

Do not update canon or scientific status from this paper.  Use it only to shape
the next source-action exploration:

```text
TOPOLOGICAL-WALL-TAU-SELECTOR
```

That swing should ask whether a global boundary/topology condition can supply a
nonzero tangent selector `Z` that the finite-fiber Noether equation cannot
choose by itself.

Update after `TOPOLOGICAL-WALL-TAU-SELECTOR-PACKET-2026-07-10.md`: the wall analogy does generate nonzero
tangent selectors in the GU carrier, but multiple spacelike wall choices pass the same checks. The next step
is not another wall scan; it is specifying the actual global boundary condition or source current that would
select one.
