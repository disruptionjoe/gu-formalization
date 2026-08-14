---
artifact_type: exact_full_lie_algebra_bfv_closure_and_reducibility_result
created: 2026-08-14
status: FULL_91_GHOST_CLASSICAL_MASTER_EQUATION_CLOSES__FROZEN_ACTION_RANK70_STABILIZER_SO34_DIM21__ZERO_LEVEL_NONREGULAR__PROPER_RESOLUTION_OPEN
source_return: SOURCE_OWNS_FULL_MOVING_FRAME_AND_SOURCE_SHAPED_ACTION_GRAMMAR__REPO_DERIVES_EXACT_FINITE_BFV_CLOSURE_AND_FROZEN_STABILIZER__SOURCE_SILENT_PROPER_REDUCIBILITY_RESOLUTION_FUNCTIONAL_PHASE_SPACE_AND_ANALYTIC_DOMAIN
ledger_rows: [RA-G2, LT-SM3, AC-F1, AC-G1a]
registry: lab/process/selected-k77-full-bfv-master-equation-gate.json
canon_verdict_change: none
---

# Selected K77 full BFV master-equation gate

## Result first

The retained charged edge completion admits the complete algebraic classical
BFV charge for all 91 `so(7,7)` generators.  In the normalized bivector basis

```text
E_ab=(1/2)e_a e_b,
J_a=P([E_a,T]),
Omega=c^a J_a-(1/2) f_ab^c c^a c^b b_c,
```

the exact cotangent moment map is equivariant and the Lie structure constants
satisfy Jacobi.  Consequently

```text
{Omega,Omega}=0
```

at classical algebraic grade.  The exact probe verifies all 4,095 unordered
action commutators and all 121,485 independent distinct-generator Jacobi
triples.  The normalized `J_a` are one half of the predecessor's raw-bivector
charges `Q_ab`; this changes neither support nor the zero locus.

Closure does not make the constraint presentation regular or proper.  At the
frozen selected distortion, the infinitesimal action map has exact rank 70,
not 91.  Its complete 21-dimensional kernel is the odd-axis `so(3,4)` algebra:

```text
ker(ad_T)=span{E_ab : a,b in {1,3,5,7,9,11,13}},
dim ker(ad_T)=21.
```

At the zero-level point `(T,P=0)`, the moment-map differential therefore has
rank 70.  Zero is not a regular value of the full 91-component map.  The
two-term charge closes as a Chevalley--Eilenberg/BFV algebra, but a proper
Koszul--Tate resolution of the zero locus is not yet constructed.  The next
gate is a stabilizer-aware reducibility and ghost-for-ghost completion on a
source-owned orbit-type stratum.  The analytic boundary domain remains
downstream of that gate.

## Layer 0

| phrase | exact object | kept distinct from |
| --- | --- | --- |
| 91 ghosts | one ghost for each full `so(7,7)` generator | 91 independent constraints |
| classical BFV closure | exact algebraic master equation | proper resolution or physical cohomology |
| rank 70 | rank of `X -> [X,T]` at the frozen distortion | support 15 of the endpoint charge |
| stabilizer 21 | odd-axis `so(3,4)` centralizer of this `T` | 51-dimensional W-polarization stabilizer |
| nonregular zero | rank deficiency at `(T,0)` in the zero locus | failure of every orbit-type stratum |
| retained edge carrier | full charged frame endpoint with BFV algebra | functional/Sobolev boundary phase space |

The predecessor's `51+40` decomposition is fixed by the W/mirror base-normal
polarization.  The present `21+70` decomposition is fixed by the centralizer of
the selected distortion.  They answer different questions and must not be
identified.

## Exact master-equation theorem

For the cotangent-lifted adjoint action on the retained full-frame carrier,

```text
J_a(T,P)=P([E_a,T]).
```

The canonical cotangent Poisson bracket and the representation identity give

```text
{J_a,J_b}=f_ab^c J_c.
```

The `J`-linear terms in `{Omega,Omega}` cancel between the moment-map bracket
and the ghost/ghost-momentum bracket.  The remaining cubic-ghost coefficient
is the antisymmetrized expression

```text
f_[ab^e f_c]e^d,
```

which vanishes by Jacobi.  No higher term is needed for algebraic closure of
this Lie-algebra action.

The certificate is basis-exact.  It uses the actual K77 coordinate signature
order `(+,---,++++++,----)`, which has total signature `(7,7)`, and normalized
Clifford bivectors.  It independently checks that their commutator action on
the selected `T` realizes the same structure constants before invoking the
master cancellation.

## Constraint geometry and reducibility

The selected distortion has Clifford support only on the seven even-labelled
directions.  Every odd-odd bivector commutes with it.  Exact rank reduction
proves that these 21 visible generators exhaust the centralizer; there are no
hidden additional kernel combinations.  The odd seven-plane has signature
`(3,4)`, so the stabilizer is `so(3,4)`.

Thus the full 91-component constraint presentation has 21 first-stage linear
relations at the frozen point and only 70 independent cotangent directions.
Because `(T,0)` lies in `J^{-1}(0)` and `dJ/dT` vanishes there while `dJ/dP`
has rank 70, the full zero level is not regular.  This is enough to reject a
global regular Marsden--Weinstein quotient claim.

It is not enough to construct a global reducibility bundle.  Away from the
frozen point, stabilizer dimension and embedding can change by orbit type.
The 21 coordinate relations are therefore a frozen-stratum certificate, not
a globally fixed set of reducibility functions.  A proper BFV treatment must
either derive a source-owned constant-orbit-type stratum and its relation
bundle or handle the singular stratification explicitly.

## Broad route-changing lens census

- **Symplectic/BFV — selected:** the universal cotangent moment map supplies
  the two-term charge; equivariance and Jacobi decide classical closure.
- **Exact Lie algebra — decisive:** exhaustive structure and Jacobi checks
  make closure a certificate rather than a formal slogan.
- **Constraint geometry — adverse:** rank 70 and the 21-dimensional
  stabilizer prevent a regular full-91 zero-level claim.
- **Representation theory — clarifying:** the stabilizer is exactly the
  odd-axis `so(3,4)`, distinct from the W-polarization `so(1,3)+so(6,4)`.
- **Koszul--Tate/homological — route switch:** algebraic BFV closure survives,
  but properness now requires stabilizer-aware relations and ghosts-for-ghosts.
- **Variational ownership — bounded:** the moment map uses the action-owned
  endpoint pairing; no generic fitted momentum is installed.
- **Analytic/PDE — deferred:** a Green domain cannot repair a nonregular
  constraint resolution and remains downstream.
- **Source criticism — strict:** the source owns the moving frame and action
  grammar, not the new proper resolution, functional phase space or domain.
- **Philosophy of science — anti-counting:** neither 91 ghosts, rank 70, nor
  stabilizer dimension 21 is a particle, chirality or generation count.

The selected structural route dominated a reduced 70-generator complement:
no canonical complement was derived, and a complement need not be a Lie
subalgebra.  It also dominated fitting only the 15 live endpoint coordinates,
which would confuse support with rank.  The preregistered fallback fired at
the properness seam: retain the closed algebraic charge and resolve its
stabilizer relations before analytic work.

## Hostile boundary

The strongest overclaim would be “the BFV problem is solved.”  Only the
classical algebraic master equation is solved.  Nilpotence of the
Chevalley--Eilenberg/BFV differential does not prove that its cohomology is the
desired reduced algebra, that the Koszul--Tate sector is acyclic, or that a
functional operator is closed.

The strongest contrary construction is a source-derived constant-orbit-type
constraint surface on which a 70-dimensional independent presentation and a
21-relation bundle become regular.  The present result does not exclude it; it
states the exact burden required to construct it.  Conversely, the point
`(T,0)` is an explicit counterexample to any claim that the full 91-component
zero level is regular everywhere.

The weakest reproducibility seam is global phase-space ownership.  The probe
fully reproduces the finite algebra and fixture rank, but no source-owned
Sobolev carrier, preboundary two-form, global orbit-type stratification,
ghost-for-ghost bundle or closed operator domain is available.

## Progress and next gate

The larger charged edge horn now passes its first algebraic closure gate.  The
next exact construction is the stabilizer-aware reducibility/Koszul--Tate
completion on a derived source-owned orbit-type stratum, including transition
behavior if the stabilizer jumps.  Only after properness may work begin on a
codimension-one analytic Green/BFV domain.

No ledger verdict, residue, datum, quotient, canon claim, physical cohomology,
W/mirror selection, chirality, generation count or public posture changes.

## Reproduction

```sh
uv run --with sympy==1.14.0 python \
  tests/channel-swings/selected_k77_full_bfv_master_equation_gate_probe.py
```

The exact probe passes `27/27`, including the predecessor bank, exhaustive
Lie identities, rank/centralizer certificate, master cancellation and registry.
