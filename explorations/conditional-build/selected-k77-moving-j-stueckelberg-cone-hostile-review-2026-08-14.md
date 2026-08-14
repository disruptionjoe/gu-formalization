---
artifact_type: hostile_field_specialist_review
created: 2026-08-14
status: RESULT_STANDS_AFTER_FIBREWISE_LOCAL_AND_NATURAL_CANDIDATE_SCOPE
reviewed_artifact: explorations/conditional-build/selected-k77-moving-j-stueckelberg-cone-2026-08-14.md
reviewed_probe: tests/channel-swings/selected_k77_moving_j_stueckelberg_cone_probe.py
target_claim: NONE-NOT-A-KILL
fork_assumed: SELECTED_CL77__4_PLUS_10_SPLIT_ORBIT__LOCAL_PRINCIPAL_SYMBOL__ASSOCIATED_REAL_SPINOR_BUNDLE
search_space_dim: "complete 40-dimensional split orbit, complete 51-dimensional stabilizer, scalar invariant-endomorphism commutant"
free_object_delta: 0
residue_touched: none
canon_verdict_change: none
ledger_row_changes: none
---

# Hostile review: moving-`J` Stueckelberg cone

## Verdict

The result stands after enforcing three scope fences:

1. the contractible-pair theorem is local and principal-symbol algebra, not a
   global BV quasi-isomorphism;
2. the complex structure is fibrewise on the associated spinor bundle, not on
   the entire coupled field tangent; and
3. the commutant no-go kills the natural split-stabilizer-invariant complex
   structure on the orbit tangent, not every dynamical, nonlocal or
   phase-space complex structure.

Within those fences the partial theorem is exact.  The full forty-dimensional
mixed ghost maps isomorphically to the moving-split tangent, the dressed
connection map contracts that pair for every covector, and `J10` is basic for
the residual stabilizer on the associated spinor bundle.

## Independent exact controls

```text
new moving-J cone probe:                 66/66 PASS
RF-1 reverse-J probe:                    43/43 PASS
twistor/moving-BV probe:                 47/47 PASS
J10/BV/Green probe:                     112/112 PASS
```

The new receipt uses rational matrix arithmetic and exact Clifford blade
arithmetic.  Timelike, spacelike, null, generic and zero covectors all satisfy
the same exact sequence.  The wrong dressing sign fails for every nonzero
control, and freezing the reduction leaves the mixed gauge shift at rank 40.

## Three standing charges

### Charge 1: where the summary could outrun the artifact

“The moving `J` descends” would be too broad.  What descends is a fibrewise
endomorphism of `G x_H S`, and what contracts is a local split-orbit/ghost
subcomplex.  No action-owned total `K`, total `L`, quotient topology, positive
pairing or closed domain has been supplied.  The reviewed artifact uses
“associated spinor `J`” and “partial symbol cone” throughout.

The output label about a “full coupled bosonic complex structure” is also
read only with its explicit candidate qualifier: the no-go covers the natural
split-invariant block acting on the orbit tangent.  It does not classify a
complex structure that mixes connection and reduction variables, arises from
Hamiltonian evolution, uses positive-frequency splitting, or is nonlocal.

### Charge 2: where rigor could defend a mistyped object

The dangerous substitution is the normal twistor orbit

```text
O(6,4)/U(3,2), dim_R=20
```

for the moving split orbit

```text
Spin(7,7)/(Spin(1,3)xSpin(6,4)), dim_R=40.
```

The first has an invariant complex structure after selecting `J_N`; the
second has scalar stabilizer commutant on its tangent.  They are not contrary
computations on one object.  The normal-twistor route survives as an extra
reduction hypothesis, and no spin lift identifies `J_N` with `J10` here.

The second mistyping would be to apply spinor `J10` directly to the bosonic
`Cl1` connection tangent.  RF-1 already proved that left multiplication exits
`Cl1`, while conjugation is a square-plus-one reflection.  This result instead
uses `J10` only on the associated spinor fibre.

### Charge 3: what must change if the result stands

| downstream surface | disposition | reason |
| --- | --- | --- |
| reverse-falsification target chain | dissolved | its T3 successor was an unbuilt partial moving-`J` cone; this result closes the local split-orbit subcone and names the next composed-residual gate |
| RF-1 reverse-`J` census | survives | fixed failure and moving-family survival are the inputs this cone resolves locally |
| J10/BV/Green gate | survives | its moving-BV and domain obligations remain correctly open |
| twistor/BV seven-gate | survives | normal `J_N`, spinor `J10` and base twistor remain distinct; full BV and positive state space remain open |
| total twisted Yang--Mills current gate | survives | its demand for a coupled cone is partially met, but its action-owned Euler/residual composition is still unbuilt |
| frozen-frame residual-zero background | survives | concurrent `969c56e2` sharpens its missing native owner to the explicit Zorro connection and labelled curvature one-jet; branch-specific stabilizer remains missing and no ranks are imported |
| conditional physics ledger v0.258 | survives | no row owns this reverse-channel partial cohomological comparator and no verdict changes |
| `CURRENT-STATE.yaml`, `RESEARCH-STATUS.md`, `NEXT-STEPS.md` | survives | the repository-wide missing total complex, legal background, domain and positivity remain governing |
| canon and source-claim register | survives | no canon theorem or source polarity changes |

## Conditional-match disposition tuple

```text
fork_assumed:
  selected real Cl(7,7), author-declared (1,3)+(6,4) split;
  homogeneous moving split orbit;
  local observed principal-symbol comparator;
  associated real spinor bundle

search_space_dim:
  complete 91-dimensional so(7,7) generator census;
  51-dimensional stabilizer plus 40-dimensional mixed complement;
  complete 40-dimensional split tangent and ghost pairing;
  invariant orbit-tangent endomorphism commutant dimension one

free_object_delta: 0

residue T-grades: none; no conditional-ledger residue or external datum touched
```

The reverse-channel T ladder remains:

```text
T0 endpoint and carrier typing
T1 pointwise complex/commutant construction
T2 selected-local fixed/moving gauge and symbol tests
T3 extended partial cone on a common owned subcarrier
T4 total physical cohomology, positive pairing and closed Lorentzian domain
```

| conditional match | grade after | disposition |
| --- | --- | --- |
| moving split/ghost subcone | T3 local partial EXACT | advances from longitudinal covariance to an exact contractible symbol sequence |
| associated spinor `J10` | T3 fibrewise EXACT | advances from moving covariance to exact `H`-basic associated-bundle descent |
| invariant complex structure on split-orbit tangent | T2 CANDIDATE KILLED | scalar commutant excludes `I^2=-1` for this natural candidate class |
| full coupled moving-`J` residual complex | T3 TYPE-MISSING | no action-owned residual map has been composed |
| intrinsic physical complex state space | T4 OPEN | no positive quotient, domain or evolution |

## Global and lower-order attack

The contraction uses one homogeneous orbit chart and a symbol covector.  It
can fail to globalize if the reduction bundle has nontrivial transition data,
if orbit type changes, or if boundary-nonvanishing transformations are
charged.  Lower-order curvature can also add a differential on the dressed
connection sector even though the algebraic pair remains locally
contractible.  These are successor obligations, not defects in the exact
partial statement.

The zero-covector control is useful but limited.  It shows contraction does
not depend on dividing by `k`; it does not prove propagation, Green
hyperbolicity, closedness or a physical zero-mode theorem.

## Source return

`SOURCE-SILENT`.  `SC-GRP-01`, `SC-FER-05` and `SC-CHI-03` confirm the parent,
split and half-carrier inputs.  They do not state the partial cone, its
contracting coordinate, the associated-bundle `J10` theorem or a physical
superposition interpretation.

## Trap capture

No trap is appended to `lab/process/path-dependencies.yaml`.  The main hazards
are already named by existing fixed-versus-moving and conditional-versus-
settled fences, and no repeatable new failure escaped into a filed result.

## Licensed propagation

Only the channel-owned reverse target chain requires a content update now.
Ledger, canon, current state, repository-wide agenda and source register have
explicit empty change sets.  The next in-channel work is to compose this
contractible pair with one branch-specific action-owned gauge/residual map;
it is not a GU-wide frontier rerank.

## Reconciliation and bounded mailbox disposition

```text
starting computation basis: 7fd3b872414dadc5f784d45dc88bb63595dc6133
concurrent disjoint reconciliation basis: 969c56e2e223cbc174dd17242e3cce010ee29217
latest ledger inspected: v0.258
ledger meter effect: none; no row owns this partial reverse-J comparator
active source directive: preserve the non-chiral total target and do not infer
  physical cohomology or superposition from a moving reduction alone
overlapping active work after serialization: none on the four declared paths
high-fanout premise changed outside channel: native background legality was
  sharpened from pointwise curvature orbit to explicit Zorro labelled
  curvature one-jet; this corrects the successor wording but does not alter
  the cone ranks, associated-bundle theorem or candidate no-go
mailbox disposition: NO_MATERIAL_DELTA
```

The one bounded mailbox read found no non-archived GU proposal.  It confirms
the in-channel successor and does not correct or reorder the result.

## Validation disposition

Green checks:

```text
moving-J cone exact probe                    66/66
RF-1 reverse-J replay                        43/43
twistor/moving-BV replay                     47/47
J10/BV/Green replay                         112/112
kill_target_claim_audit                       PASS
changed_public_path_hygiene_audit             PASS
public_path_hygiene_audit                     PASS
path_dependency_audit                         PASS
explorations_readme_surface_map_audit         PASS
k77_split_layer_commutant_action_parent_audit PASS
```

One repository-wide gate remains red on a pre-existing surface outside this
result's footprint: `lab_active_research_readme_surface_map_audit.py` has a
stale expected-row list that omits the already-present source-residual and
triplet rows.  It resolves every target and does not implicate any changed
path.  This run does not widen into that stewardship repair.
