---
artifact_type: exact_boundary_stationarity_and_regular_symplectic_realization_result
created: 2026-08-14
status: BARE_FREE_BOUNDARY_FORCES_ZERO_CHARGE__NONZERO_FIXTURE_NEEDS_FIXED_GENERATED_OR_EDGE_HORN__LOCAL_MINIMUM_98__GLOBAL_EQUIVARIANT_MINIMUM_OPEN
source_return: SOURCE_CONFIRMS_SELECTED_ACTION_AND_ENDPOINT_GRAMMAR__SOURCE_SILENT_BOUNDARY_FUNCTIONAL_EDGE_FIELD_CHARGE_DISPOSITION_AND_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-boundary-stationarity-symplectic-realization-gate.json
canon_verdict_change: none
---

# Selected K77 boundary stationarity and symplectic-realization gate

## Result first

The selected bare action does not supply a nonzero boundary law that locks the
seven regular `so(7,7)` coadjoint invariants. Its already-derived endpoint
potential is

```text
Theta = p_0 delta g_0 - p_2 delta g_3.
```

If both endpoint fields are varied freely, stationarity forces

```text
p_0=p_2=0.
```

The endpoint moment map `Q_eta=p_0 eta_0-p_2 eta_3` then vanishes for every
parameter, its trace-dual coadjoint element is zero, and all seven invariants
are locked only at zero. The exact nonzero regular fixture used by the previous
packets is therefore not on this free stationary boundary locus.

Fixed endpoint data makes `Theta` vanish because `delta g=0`, but it does not
constrain `p` or its seven invariant values. Transformations that move the
fixed data are then boundary symmetries, not gauge directions supplied by the
bare variational problem. A nonzero Robin/generated graph can relate `p` and
`g`, but it requires a boundary functional `F` for which the restricted
potential is `delta F`. Neither the inspected source nor the selected action
owns such an `F`. At a regular charge, locking the orbit values imposes the
seven independent tangent conditions

```text
d I_k(L) (dL(v)) = 0,       k=1,...,7.
```

The carrier horn also sharpens. The regular Lie--Poisson space has dimension
91, rank 84 and corank seven. Any symplectic realization submersing onto an
open regular charge neighborhood has dimension at least

```text
91 + 7 = 98.
```

This is sharp locally: Weinstein splitting gives an 84-dimensional symplectic
leaf times `T*R^7`, adding one conjugate variable for each transverse Casimir.
Thus the previous 84-dimensional orbit is minimal only for one fixed invariant
value; a local carrier spanning the seven values needs fourteen more
dimensions. The canonical global equivariant fallback `T*Spin(7,7)` is
182-dimensional and has a surjective moment map. The smallest *global
equivariant* realization is not proved: it lies between 98 and 182.

## Plain English

The action offers a clean zero-charge boundary condition, but it does not
select a nonzero fixed charge. Keeping the nonzero endpoint either treats its
transformations as physical boundary symmetry, adds a still-unowned boundary
law, or adds an edge carrier.

One symmetry orbit was too small because it could move only within fixed orbit
labels. Locally, the smallest possible symplectic system that also carries all
seven labels has 98 dimensions. A completely canonical global construction
exists with 182 dimensions, but proving a smaller global equivariant carrier
remains real work.

## Variational classification

### 1. Free endpoint variation

Arbitrary independent `delta g_0` and `delta g_3` make the coefficients of the
boundary variation vanish separately. Hence `p_0=p_2=0`, so `Q_eta=0` and the
coadjoint element `L=0`. This is action-owned and exact, but it excludes the
nonzero endpoint fixture rather than explaining it.

### 2. Fixed endpoint data

Dirichlet data sets the admitted variations to zero. It places no equation on
the endpoint momenta. A gauge transformation with nonzero endpoint parameter
generally moves the fixed datum; it is not an admitted degeneracy of this
boundary problem. The predecessor's exact `(B,T)->lambda(B,T)` direction shows
that the seven invariant values can vary when the momentum is left free.

### 3. Generated or mixed boundary graph

A Lagrangian boundary graph can make `Theta` exact, schematically

```text
p_0 = partial F / partial g_0,
p_2 = - partial F / partial g_3.
```

This is a valid mathematical route, not a result of the bare action. A
candidate `F` must be sourced or independently derived and then pass all seven
invariant-tangency equations. Merely naming a Robin condition or choosing the
desired orbit values would fit the missing owner.

## The 98-dimensional lower bound

Let `J:(M,omega)->g*` be a Poisson submersion over the regular locus. If
`dim(M)=2m` and `dim(g*)=n`, then `ker dJ` has dimension `2m-n`. Every covector
in the corank-`c` kernel of the Lie--Poisson tensor lifts to a Hamiltonian
vector lying in `ker dJ` and its symplectic orthogonal. Therefore

```text
2m-n >= c,
2m >= n+c.
```

Here `n=91` and `c=7`, so `dim(M)>=98`. In regular Weinstein split
coordinates, the Poisson neighborhood is a symplectic leaf of dimension 84
times seven zero-Poisson transverse coordinates. Replacing the transverse
factor by its cotangent bundle constructs

```text
M_local = O_mu x T*R^7,     dim M_local=84+14=98,
```

and projection supplies the local Poisson realization. This proves local
sharpness. It does not prove global `Spin(7,7)` equivariance or source
ownership.

This is the standard regular-coordinate realization: Cannas da Silva and
Weinstein describe a regular Poisson chart with leaf coordinates `(q,p)` and
corank coordinates `c`, then adjoin conjugates `d` so projection from
`(q,p,c,d)` is a symplectic realization. See *Geometric Models for
Noncommutative Algebras*, sec. 6.3
([author manuscript](https://math.berkeley.edu/~alanw/Models.pdf)).

Left or right cotangent lift on `T*Spin(7,7)` supplies a canonical equivariant
moment map whose image is all of `so(7,7)*`. Its dimension is `2*91=182`.
Consequently

```text
98 <= smallest global equivariant carrier dimension <= 182.
```

No sharper global minimum is claimed.

## Route comparison and hostile boundary

- **Variational structure** dominates an immediate analytic domain: it already
  decides what the bare action can and cannot impose at the endpoint.
- **Regular Poisson geometry** dominates a coordinate edge-field search: it
  proves the lower bound and local construction without fitting variables.
- **Cotangent-group geometry** is retained as a global fallback, not mislabeled
  as minimal.
- **Charged boundary symmetry** remains the zero-import horn when fixed
  endpoint data is selected.
- **A generated boundary functional** remains the strongest contrary route,
  but it must be derived and must pass seven independent tangency equations.

The strongest overclaim would be that a 98-dimensional physical edge theory
has been derived. Only a local symplectic realization is proved. No kinetic
term, source owner, global bundle, polarization, Green domain, positive
pairing, reduced phase space or physical cohomology follows.

No ledger verdict, residue, quotient, datum, canon claim, W/mirror choice,
chirality, generation count or public posture changes. Weinstein's total
theory remains explicitly non-chiral.

## Next gate

Either derive a concrete source/action boundary functional and test all seven
invariant tangencies on its graph, or construct a global equivariant
symplectic realization smaller than the 182-dimensional cotangent fallback.
Only after that comparison should the program choose charged boundary symmetry
versus gauge completion and enter the analytic BFV domain.

## Reproduction

```sh
python tests/channel-swings/selected_k77_boundary_stationarity_symplectic_realization_gate_probe.py
```

The probe imports the exact predecessor registry and certifies the
stationarity controls, seven-invariant transversality, regular Poisson bound,
local sharp model, cotangent fallback and claim ceilings.
