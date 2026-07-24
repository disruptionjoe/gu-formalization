---
title: "Sigma external-Z2 claim-dependency packet"
status: exploration
doc_type: claim_dependency_packet
created: 2026-07-23
run_id: RUN-20260723-214037-gu-formalization-progress
lane_id: "3"
source_revision: 1fa73423a39d4a2f5dc30b33938f931643ba91d0
claim_status_change: none
canon_verdict_change: none
public_posture_change: none
external_action: none
---

# Sigma external-Z2 claim-dependency packet

## Bottom line

There is not currently a theorem that GU requires an external `Z/2` datum.
The strongest unconditional result is a GU-independent finite-dimensional
classification of commuting fundamental symmetries for compact stabilizers.
Applied to both the `SO(9) x SO(5)` frame surrogate and the program-native
kinematic `Sp(32) x Sp(32)` Cartan centralizer, it gives a **unique**
fundamental symmetry, not a free bit.

A different statement survives conditionally: if the physical internal
observable algebra is exactly the alpha-even class for the grading flip, then
Schur equivariance makes the channel from `sigma` to that class constant and
its Shannon capacity zero. The load-bearing premise — that GU's actual
interacting internal observables are alpha-even — is open. The existing Lean
`no_invariant_valuation` result is a codomain fixed-point tautology and does not
prove this domain premise or exclude an alpha-equivariant reader.

This packet is therefore a dependency audit and stop rule, not a paper seed,
claim promotion, or physics result.

## Grade vocabulary

| label | meaning in this packet |
|---|---|
| `proved` | written mathematical argument whose stated hypotheses and conclusion are supported independently of a GU interpretation |
| `finite/model exact` | exact computation or finite-dimensional theorem for a declared proxy, carrier, or representation |
| `structural rendering` | faithful reformulation of an established result that does not add a theorem |
| `proposal` | plausible construction or interpretation not yet supported by the needed object/map |
| `open bridge` | a required implication whose source and target are named but whose map/theorem is absent |
| `circular` | the claimed output is supplied in the construction or action used to derive it |
| `refuted` | a stated implication or candidate construction has a counterexample or exact incompatible result |

## Claim-dependency DAG

Edges point from prerequisites to claims that depend on them.

```text
finite compact-stabilizer classification [proved]
  -> kinematic Cartan application [finite/model exact]
       -> no free Z/2 at the built kinematic level [finite/model exact]

alpha-even decomposition [finite/model exact]
  + internal-observables = alpha-even [open bridge]
  -> zero-capacity sigma-read theorem [proved conditional]
       -> internal forcing/external requirement [open bridge]

grading flip -> w1(L_time) [open bridge]
  -> dark-energy sign [open bridge]
  -> time orientation / arrow [open bridge]

source-owned operator/domain/deck packet [absent]
  -> determinant/Pfaffian/spectral-flow/domain line [open bridge]
       -> w1 of that specified line [open bridge]
            + Omega^Pin+_14 ~= Z/2 [proved ambient receptacle]
            -> specific nonzero GU anomaly class [open bridge]
                 -> anomaly-protected external bit [proposal]

interacting state space + observable algebra + grading operator [absent]
  -> observable descent [open bridge]
  -> physical GU application [open bridge]
```

## Headline-leg register

| headline leg | strongest present support | grade | dependency / failure mode |
|---|---|---|---|
| Residual grading bit | The invariant-form space and the space of admissible fundamental symmetries are distinct; shared positive/negative irreducibles can yield continuous moduli | `proved` in finite dimensions | The canonical compact stabilizers used in GU have no shared constituent and yield a singleton, not a bit |
| Internal-forcing claim | No alpha-even map can read an alpha-odd sign; the induced two-row channel is constant | `proved conditional` | Requires `internal observables = alpha-even`, presently an `open bridge` |
| `w1(L_time)` identification | A nontrivial real sign line over `RP3` can carry nonzero `w1` | `proved` as topology / `proposal` as GU identification | No constructed map from the grading datum or physical operator family to this line |
| Dark-energy sign | Conditional theta-sector constructions keep the non-phantom sign | `structural rendering` / construction-conditional | The map from the proposed `w1` datum to the action coefficient/sign is not built |
| Time orientation / arrow | A line orientation and an arrow can both be represented by `Z/2` data | `structural rendering` | Equality of these roles is an `open bridge`; shared cardinality is not identity |
| Pin receptacle | `Omega^Pin+_14 ~= Z/2` | `proved` for the ambient bordism group | Receptacle order does not construct a GU cycle or class |
| Specific anomaly class | None | `open bridge` | No closed degree-14 GU cycle, proper Fredholm realization, family line, or nonzero detector |
| Observable descent | None at interacting grade | `open bridge` | Native state quotient, observable algebra, source action, and symmetry-compatible descent are unbuilt |

## Strongest theorem currently supportable

### Unconditional GU-independent theorem

Let `(V, eta)` be a finite-dimensional real Krein space and let a group `H`
act through a representation with compact closure. Decompose `V` into real
isotypic components

```text
V = direct_sum_lambda U_lambda tensor_{D_lambda} M_lambda,
```

where `D_lambda` is `R`, `C`, or `H`, and the multiplicity-space Hermitian form
has signature `(a_lambda,b_lambda)`. The space of `H`-commuting,
`eta`-self-adjoint involutions `C` for which `eta(.,C.)` is positive definite
is the product of the corresponding noncompact symmetric spaces and has real
dimension

```text
sum_lambda dim_R(D_lambda) a_lambda b_lambda.
```

It is a singleton exactly when no irreducible type occurs on both the positive
and negative sides.

This is the strongest clean theorem in the current paper orbit. It is likely
standard compact/Krein representation theory and is not claimed as novel.

### Conditional zero-capacity corollary

Let alpha be a `Z/2` grading flip and suppose the complete physical internal
observable algebra is alpha-even. Then any equivariant map from the sign
representation carrying `sigma` to the internal trivial representation
vanishes. The associated classical channel has identical rows and capacity
zero.

This conclusion is mathematical once the premise is supplied. GU does not yet
derive the premise for its interacting state space. Therefore the corollary
cannot presently be advertised as “GU needs an external bit.”

## Novelty and absorber map

| candidate contribution | nearest absorber | disposition |
|---|---|---|
| Nonuniqueness of positive metrics or `C` operators | pseudo-Hermitian / PT-symmetric metric-operator literature (Mostafazadeh; Bender-family work) | prior-art absorber; not a novelty claim |
| Selection of a metric by additional observables/dynamics | existing quasi-Hermitian and physical-state reconstruction programs | prior-art absorber; external choice is not generally necessary |
| No internal invariant valuation for a fixed-point-free codomain action | Lawvere/Yanofsky-style diagonal or fixed-point framing | too weak as presently formalized; the Lean result is codomain-trivial |
| Limits on self-measurement | Breuer-style self-measurement results | possible conceptual absorber; no novelty claim until the GU domain and comparison theorem are explicit |
| `w1` of a real orientation/sign line | standard orientation-line topology | standard mathematics; GU-specific content would have to be the constructed line/descent |
| Degree-14 `Pin+` target | standard bordism/anomaly classification | ambient group is known; novelty, if any, must lie in a specific GU class and nonzero detector |
| Compact-stabilizer classification | standard real/complex/quaternionic isotypic representation theory and symmetric spaces | likely standard; useful as a corrective theorem, not presently a novelty basis |

No current result is demonstrably stronger than these absorbers in a
construction-specific physical sense.

## Failure ledger

1. **Trivial-codomain correction (`refuted` as substantive externality).**
   `no_invariant_valuation` applies alpha to the output label and proves that a
   fixpoint-free codomain has no fixed output. It does not model a domain action
   and does not exclude an alpha-equivariant reader.
2. **Domain-to-alpha-even bridge (`open bridge`).** The actual interacting GU
   internal observable algebra is not constructed, so it is not proved to be
   the alpha-even class.
3. **Free-bit claim at the built compact stabilizers (`refuted`).** Both the
   `SO(9) x SO(5)` surrogate and the native kinematic
   `Sp(32) x Sp(32)` Cartan centralizer satisfy the non-coincidence condition
   and yield a unique admissible fundamental symmetry.
4. **Five-method independence (`refuted`).** The routes share the same
   representation split; the honest inventory is one invariant-theory
   theorem, one conditional operator lemma, one unbuilt BRST route, and two
   analogies.
5. **`sigma = w1` (`open bridge`).** A sign line can carry `w1`, but no physical
   operator/domain family has been shown to induce the claimed line.
6. **`sigma^4` detector (`refuted` for the cheap route).** On the proposed
   `RP3` base, the cheap sigma-free Stiefel-Whitney route vanishes; it cannot
   establish a nonzero degree-14 class.
7. **Pin-class non-evaluation (`open bridge`).** The ambient group is exactly
   `Z/2`, but no closed GU cycle or proper Fredholm class is presently defined.
8. **Operator-grade circularity (`circular`).** Supplying the deck/sign action
   whose externality is at issue cannot establish that GU internally generates
   or requires that same datum.
9. **Observable descent (`open bridge`).** The physical quotient, interacting
   grading/operator, observable algebra, and compatible descent are absent.
10. **Physics weld (`open bridge`).** Grading sign, `w1(L_time)`, dark-energy
    sign, and time arrow are four obligations; common `Z/2` typing does not
    identify them.

## Source-safe title and abstract

### Title

**Commuting fundamental symmetries of compact actions on finite-dimensional
Krein spaces**

### Abstract

We classify the fundamental symmetries commuting with a compact group action
on a finite-dimensional real Krein space. In real isotypic coordinates the
space is a product of symmetric spaces determined by the positive and negative
multiplicities over `R`, `C`, and `H`; its real dimension is
`sum dim_R(D_lambda) a_lambda b_lambda`. The commuting fundamental symmetry is
unique exactly when no irreducible type occurs with both signs. Consequently
the canonical `O(p) x O(q)` example has a unique symmetry, whereas proper
subgroups with shared constituents can leave continuous moduli rather than a
single binary choice. We use the classification to correct a proposed
grading-sign argument arising from a Geometric Unity model: the currently
constructed compact stabilizers lie in the unique case, while the interacting
state space, observable algebra, and grading operator needed for a physical
application remain open.

This title and abstract support only the finite-dimensional corrective result.
They do not claim internal undecidability, an external `Z/2`, a GU anomaly, a
dark-energy prediction, or a time-arrow theorem.

## Evidence needed for the broader title

A broader “external sign” title becomes supportable only if all of the
following land:

1. a source-owned interacting state space and complete physical observable
   algebra;
2. a theorem that the internal algebra is alpha-even, or an equally strong
   characterization that excludes every alpha-equivariant internal reader;
3. an independently constructed grading/sign datum rather than a supplied
   `C`, deck action, or positive majorant;
4. a specified operator/domain family and functorial real line whose `w1` is
   computed;
5. a non-circular map from that class to `w1(L_time)`;
6. separate constructed maps to the dark-energy sign and time orientation;
7. a closed degree-14 GU cycle or proper Fredholm family and a nonzero detector
   for its class in `Omega^Pin+_14`; and
8. an absorber/novelty review showing that the resulting theorem is stronger
   than standard metric-operator selection, self-measurement, fixed-point,
   orientation-line, and anomaly-classification results.

## Stage B decision

Stage B should not begin by computing more ambient Pin groups or by repeating
the five-method convergence. The single load-bearing bridge is:

```text
Characterize the actual internal observable algebra and prove or refute that
every physical internal sigma-reader lies in the alpha-even class.
```

The exact wake is a source-owned interacting state/observable packet with the
group action, grading flip, physical quotient, and admissible reader class.
Without that packet, further “external bit” proof work is source-gated.

## Source trail

- `papers/drafts/structurally-forced-internally-undecidable/draft-skeleton.md`
- `papers/drafts/structurally-forced-internally-undecidable/HARDENING-REPORT.md`
- `explorations/prereg-oracle-relative-thesis-swing-2026-07-21.md`
- `explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md`
- `explorations/operator-to-anomaly-closure-campaign-2026-07-22.md`
- `explorations/pin-smith-class-realization-ultimatum-2026-07-22.md`
- `GEOMETER-VS-PHYSICS-OBJECTS.md`

## Boundary

Exploration-tier dependency audit. It changes no claim status, canon verdict,
identity, Lane control, public posture, publication state, or external system.
No cross-repository identity is asserted. `bar (b)` and H59 remain OPEN.
