---
artifact_type: exploration
status: exploration
doc_type: conditional_build_observer_reduction_typing_gate
created: 2026-08-16
work_item: CB-4B-H210
channel: high_energy_two_plus_one_prediction
target_claim: SC-GEN-53
title: "CB-4B H210: a nonzero observation graph cannot preserve the fixed Pati--Salam embedding; a co-moving embedding preserves equivariance but needs an additional reduction cocycle"
grade: "EXACT rational representation and O(7,7) arithmetic plus source/operator typing. The fixed-PS mixed centralizer has dimension zero; an exact nonzero graph lift, conjugated PS algebra, block-stabilizer ambiguity, conjugacy relation, equation-9.16 cell ledger, and five firing claim plants are checked without floats. CONDITIONAL on H210. H210-ALIGN is separate. A preferred co-moving PS reduction, source action/background/section/family row, physical quotient, mass, scale, threshold, and observable are not supplied."
disposition: FIXED_PS_NONZERO_GRAPH_EXCLUDED__COMOVING_PS_EQUIVARIANCE_EXACT_BY_COVARIANCE__REFERENCE_PS_TRANSPORT_DESCENDS_ONLY_UP_TO_CONJUGACY__PS_REDUCTION_COCYCLE_TYPE_MISSING__FREE_144_LABEL_UPSTREAM_ONLY
canon_verdict_change: none
steering_effect: "Do not demand that a nonzero co-moving observation graph preserve one fixed PS embedding. Carry H210 through a chosen co-moving PS reduction only under an explicit additional reduction/cocycle horn; covariance proves equivariance, not source selection. Keep CB-2's free 144 label upstream of literal contraction and retain both halves, H210-ALIGN, fixed-Hq, and the full d0+varpi collision."
depends_on:
  - lab/active-research/joe-directed/high-energy-two-plus-one/he4-path-reprioritization-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb1-h210-k77-rs-intertwiner-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb2-h210-equation916-cross-half-composition-2026-08-16.md
  - lab/active-research/joe-directed/high-energy-two-plus-one/cb3-wave-h210-observation-reprioritization-2026-08-16.md
  - lab/sources/source-claim-register.yaml
  - lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md
  - explorations/conditional-build/selected-k77-finite-section-projector-atlas-descent-2026-08-12.md
  - explorations/conditional-build/selected-k77-canonical-section-jet-cartan-spin-prolongation-2026-08-12.md
  - lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md
scripts:
  - tests/channel-swings/joe_directed_cb4_h210_ps_observer_typing_probe.py
---

> [!IMPORTANT]
> **GU-COMPARATOR-ROUTING — CONDITIONAL BUILD, H210.** This gate uses the
> complex Pati--Salam labels only as the already-typed bridge for Weinstein's
> F/Q/Z, `2+1`, reunification, and emergent-chirality proposal. Ordinary family
> indices, net-chirality tests, scalar-Higgs VEVs, and conventional mass models
> do not adjudicate it. The source imposter is F-shaped; the internal `144` is
> its distinct predicted partner.
> Read `lab/methods/source-native-comparator-routing.md` before reuse.
>
> Deriving or varying an action, choosing a background or section, fitting a
> family row, or importing an external datum is outside this lane.
>
> Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`.

# CB-4B — fixed versus co-moving Pati--Salam typing

## Verdict first

The CB-3 naturality problem has a forced fork.

At the reference `4+10` split, let the external four-plane `H_4` be
Pati--Salam trivial and let the internal vector restrict as

```text
V_10 |_PS = (6,1,1) + (1,2,2).
```

Neither summand contains `(1,1,1)`. Therefore

```text
Inv_PS(V_10) = 0,
Hom_PS(H_4,V_10) = H_4* tensor Inv_PS(V_10) = 0.
```

The mixed graph generator `q(J)` commutes with the **fixed** PS embedding only
when `J=0`. A nonzero observation graph cannot simultaneously co-move and keep
the same fixed subgroup acting trivially on the new horizontal plane. This is
an exact representation obstruction, not a failure of H210.

There is a consistent co-moving horn. Given a chosen local orthogonal lift
`g_J` of the graph, define

```text
PS_J = g_J PS g_J^-1,
T_J  = rho_out(g_J) T rho_in(g_J)^-1.
```

If the banked H210 tensor obeys `rho_out(p)T=T rho_in(p)`, then for
`p_J=g_J p g_J^-1`, direct substitution gives

```text
rho_out(p_J) T_J = T_J rho_in(p_J).
```

Thus the tensor remains equivariant under `PS_J` by covariance. That theorem
does not say the source, action, graph projector, or observation geometry
selects a preferred `PS_J`.

The distinction is decisive. The graph projector determines a nondegenerate
four-plane and its orthogonal complement. It does **not** determine any
Pati--Salam reduction of the complement. Once the reference PS embedding is
imported from H210, its local transports are lift-independent only up to
conjugacy. A preferred subgroup or reduction requires another conditional
reduction/cocycle horn.

Name that additional horn explicitly:

```text
H210-PSRED = the observer-normal frame cocycle reduces at least to N(PS);
             a principal PS reduction requires the stronger PS-valued overlaps.
```

`H210-PSRED` is independent of `H210-ALIGN`. It is available as a declared
conditional input for downstream composition; constructing it from an action,
background, preferred graph, or external datum is outside this lane.

## Conditional-build contract

Horn `H210` is assumed compatible and nonzero; no `54` is added. The separate
horn

```text
H210-ALIGN = identify M_3/ker(r) with the source's F/imposter provenance line
```

is preserved and not derived. This artifact adds no family row and does not
name a family. It tests only how the already-banked port can be typed relative
to observation geometry. `H210-PSRED` names the separate co-moving subgroup
descent assumption; it is neither supplied by the graph projector nor inferred
from covariance.

Both effective packages remain:

```text
A: 16 -> 144bar,
B: 16bar -> 144.
```

No luminous half is selected. Fixed trace-`H_q` remains the adverse
`TYPE_MISSING` subhorn from CB-1. The released full `d0+varpi` derivative-half
collision remains open. No action, background, selected section, physical
quotient, mass, scale, threshold, or observable is constructed.

## Eight-lens assessment

### 1. Exact PS representation lens

The internal vector has the two irreducible blocks `A_6=(6,1,1)` and
`B_4=(1,2,2)`. Neither is trivial. Since PS acts trivially on every copy in
`H_4`, an equivariant map sends each external basis vector to a PS-fixed vector
of `V_10`; there are none. The exact probe realizes the vector image as
`so(6)+so(4)`, stacks all 21 generator constraints, and obtains rank `10` on
`V_10` and rank `40` on `Hom(H_4,V_10)`. The invariant dimensions are zero.

### 2. Homogeneous/principal-bundle geometry lens

The finite graph prior art owns

```text
P_J = L_J (L_J^T eta L_J)^-1 L_J^T eta.
```

Any local lift is ambiguous by `g_J -> g_J k`,
`k in O(H_4) x O(V_10)`, without changing `P_J`. The probe chooses an exact
rational nonzero `g_J in O(7,7)` and an exact vertical block-stabilizer boost
`k` mixing the `A_6` and `B_4` blocks. It verifies

```text
g_J P_0 g_J^-1 = (g_J k) P_0 (g_J k)^-1,
```

while the corresponding PS subalgebras differ.

The two subalgebras remain conjugate. Hence, **given the imported reference PS
embedding**, the lift-independent remainder is at most its conjugacy/embedding
type. The graph alone owns no PS reduction. A locally transported preferred
subgroup descends on overlaps only if the vertical stabilizer cocycle reduces
from `O(V_10)` to the normalizer `N_O(V_10)(PS)`. A principal PS reduction
requires the stronger PS-valued transition data (up to any explicitly admitted
normalizer automorphism). The banked graph projector supplies neither. Calling
either one a new source selection would be claim inflation.

### 3. Operator and equation-9.16 lens

Before literal observation, CB-2's zero-order labels remain correctly typed:

| effective package | cell | upstream arrow |
|---|---|---|
| A | `(1,2)`, `varpi_-+` part of `d0+varpi_-+` | `16 -> 144bar` |
| B | `(0,3)`, `varpi_+-` part of `d0+varpi_+-` | `16bar -> 144` |

The reverse cells `(2,1)` and `(3,0)` remain displayed partners. The bare
`varpi_++/varpi_--` cells remain exact wrong-channel controls. Co-moving
conjugation transports the zero-order operator and its representation labels
together; it does not repair the derivative term in the full cell.

### 4. Observation/functor lens

The free `144bar` or `144` label belongs to the upstream internal
vector-spinor codomain. Literal differential-form pullback contracts its normal
covector leg and returns

```text
O_J T : 16 -> T*X tensor s^*S
```

and the conjugate map. A successful co-moving square therefore proves
equivariance and rank survival of this contracted map. It does not prove that a
free `144` remains in the observed codomain. Associated restriction may retain
the F/Z representation sectors at the previous stage; the two functors are not
interchangeable.

### 5. Source-criticism lens

`SC-GEN-03/05` attach the imposter to the F-shaped equation-(12.22) term.
`SC-GEN-06` preserves the unresolved p.53 naming ambiguity but does not rename
the whole `144`. `SC-PRE-52` separately names the roughly 144-dimensional
partner and Pati--Salam recombination. `SC-GEN-53` supplies no subgroup
reduction, scale, or discriminator. The co-moving horn is repository-derived
typing, not a quotation from those rows.

### 6. Emergent-chirality lens

Conjugation transports both H210 arrows and both ambient K77 halves. It does
not create an effective-half selector. Ambient chirality, internal Weyl
duality, equation-9.16 signs, and observed 4D chirality remain separate types.
Deleting the conjugate map makes the certificate's semantic plant fire.

### 7. Family-alignment lens

The PS reduction fork does not close `H210-ALIGN`. Even if `T_J` is exactly
`PS_J`-equivariant, covariance says nothing about which quotient line of
`M_3` has F provenance. The family kernel remains basis-free. Promoting the
alignment makes a separate plant fire.

### 8. Falsifier and claim-inflation lens

The fixed-PS horn is killed for every nonzero mixed graph, not merely for the
test point. The co-moving horn survives locally and conditionally, but advances
to an intrinsic bundle statement only if a PS reduction/normalizer cocycle is
declared and the H210 tensor plus contraction descend through it. Failure of
that descent demotes H210; it does not authorize construction of an action,
background, section, or external selector.

## Fixed versus co-moving ledger

| fork | exact result | interpretation |
|---|---|---|
| fixed PS, `J=0` | compatible | reference point only |
| fixed PS, `J != 0` | excluded by `Hom_PS(H_4,V_10)=0` | no nonzero PS-invariant mixed generator |
| chosen `g_J`, `PS_J=g_J PS g_J^-1` | H210 equivariance preserved exactly | covariance, not selection |
| graph projector without PS reduction | subgroup depends on local lift | given reference PS, only conjugacy/embedding type is lift-independent |
| overlaps in `N_O(V_10)(PS)` | conditional subgroup-descent horn | preferred subgroup family can descend; not supplied here |
| overlaps in `PS` | conditional principal-reduction horn | stronger PS reduction data; not supplied here |
| general `O(V_10)` overlap | preferred PS subgroup fails to descend | exact block-stabilizer counterexample |

## Exact certificate and plants

The pure-Python certificate uses rational arithmetic only. It verifies the
`10=6+4` restriction, zero invariant space, all 40 mixed constraints, K77
orthogonality, failure of fixed-PS centralization, exact co-moving conjugation,
same-projector/different-subgroup lift ambiguity, and preservation of the
conjugacy class.

Five mutants must fire:

1. insert a false PS singlet in `V_10`;
2. allow fixed PS under nonzero `J`;
3. delete the conjugate H210 arrow;
4. promote `H210-ALIGN` from a separate conditional horn; and
5. call covariance a source selection.

Reproduce with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb4_h210_ps_observer_typing_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 tests/channel-swings/joe_directed_cb4_h210_ps_observer_typing_probe.py --selftest
```

## Claim ceiling and next gate

This artifact proves a fixed-embedding obstruction and a local conjugation
theorem. It does not prove that the source/action selects a co-moving PS
reduction, that the graph projector supplies one, that the free internal `144`
survives contraction, or that the full equation-9.16 cell, fixed trace-`H_q`,
physical quotient, domain, chirality selection, family identity, mass, scale,
threshold, or observable closes.

If `H210-PSRED` is retained, descent of the complete H210 contraction square
under normalizer-valued overlaps is a well-typed later gate. If only the graph
projector is admitted and no PS reduction is declared, CB-4 has found the exact
stopping point: covariance is locally true, but a preferred globally typed PS
channel is absent.
