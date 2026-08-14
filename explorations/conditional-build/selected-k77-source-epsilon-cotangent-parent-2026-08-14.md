---
artifact_type: exact_source_epsilon_preboundary_cotangent_parent_composition
created: 2026-08-14
status: SOURCE_EPSILON_UNRESTRICTED_PREBOUNDARY_IS_CANONICAL_TSTAR_SPIN77_PARENT__REGULAR_CARTAN_RESTRICTION_NOT_ACTION_SELECTED
source_return: SOURCE_CONFIRMS_EPSILON_VARIATION_AND_TWO_CONNECTION_GRAMMAR__REPOSITORY_DERIVES_COTANGENT_IDENTIFICATION__SOURCE_SILENT_CARTAN_RESTRICTION_OPPOSITE_COPY_AND_PHYSICAL_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-source-epsilon-cotangent-parent.json
canon_verdict_change: none
---

# Selected K77 source-epsilon cotangent parent

## Result first

The selected first-order action already owns the formal preboundary parent in
which the 98-dimensional Cartan-slice construction lives.  For the right
logarithmic epsilon variation

```text
eta = epsilon^-1 delta epsilon
```

the previously derived unrestricted boundary term is

```text
Theta_epsilon = <lambda, epsilon^-1 delta epsilon>,
lambda = i_n(E_B-E_T).
```

This is exactly the canonical cotangent one-form on the left-trivialized
bundle

```text
T*Spin_0(7,7) = Spin_0(7,7) x so(7,7)*.
```

Its field-space exterior derivative has the standard exact matrix at the
selected endpoint,

```text
Omega_full = [ -K_mu  -G ]
             [   G      0 ],
```

where `G` is the nondegenerate trace pairing and `K_mu` is the Kirillov
matrix.  The exact probe gives rank `182`, and the left-action moment
differential `[K_mu,G]` has rank `91`.

The previously constructed Cartan carrier is literally the symplectic
restriction of this parent.  If `H` embeds the seven Cartan-dual directions,
then the inclusion `diag(I_91,H)` satisfies

```text
iota* Omega_full = Omega_C,
rank Omega_C = 98.
```

Thus the 182-dimensional cotangent fallback is no longer merely an abstract
mathematical possibility: at formal unrestricted-preboundary grade, it is the
action-owned epsilon boundary parent.  The source owns the epsilon field and
the two-connection definitions; the cotangent identification is a repository
derivation from their variation.

## What is not owned

The action does not impose the seven-dimensional condition
`lambda in C`, so it does not select the 98-dimensional Cartan restriction
from the 182-dimensional parent.  It also does not introduce a second epsilon
field, reverse the actual endpoint momentum, or supply an opposite-sign edge
copy.  Dirichlet epsilon data kills the flux rather than generating this
unrestricted cotangent phase space.

The result is formal preboundary geometry.  It is not a closed analytic phase
space, a source-selected domain, a proper BFV quotient, a positive pairing or
physical cohomology.

## Layer 0

Keep distinct:

1. the source epsilon field and its unrestricted boundary trace;
2. the conjugate endpoint covector `lambda=i_n(E_B-E_T)`;
3. the full `T*Spin_0(7,7)` preboundary parent;
4. its conditionally restricted `G x C` symplectic subcarrier;
5. an independent opposite-sign compensating edge copy; and
6. the diagonal product of endpoint and compensator systems.

One source epsilon cannot be counted once as the endpoint charge and again as
an independent compensator.

## Exact composition

The predecessor's trace form is nondegenerate on all 91 generators.  Therefore

```text
rank Omega_full = 182,
rank dJ_full = 91,
dim ker dJ_full = 91.
```

Restricting the momentum directions from all of `g*` to the exact Cartan dual
replaces `G` by `G H=E` and gives precisely the already-certified
98-dimensional matrix.  No coordinate fitting or new coefficient is used.

At the selected fixture `epsilon=e`, the source momentum is the same exact
nonzero `mu` with support 30 used by the endpoint packets.  It has the same
sign as the endpoint charge because it is the endpoint charge's canonical
preboundary realization.

## Disposition

```text
full 182-dimensional epsilon cotangent parent:  ACTION-OWNED FORMALLY
98-dimensional regular Cartan restriction:      MATHEMATICALLY ADMITTED
action selection of that restriction:           OPEN
independent opposite compensator:                NOT OWNED
analytic/physical phase space:                   OPEN
```

The immediate successor must decide whether the opposite compensator can be a
dependent equivariant construction from the charge and existing epsilon data,
or necessarily requires an independently owned boundary frame/action.

No ledger verdict, residue, quotient, datum, canon claim, W/mirror choice,
chirality, generation count or public posture changes.

## Reproduction

```sh
sage -python tests/channel-swings/selected_k77_source_epsilon_cotangent_parent_probe.py
```
