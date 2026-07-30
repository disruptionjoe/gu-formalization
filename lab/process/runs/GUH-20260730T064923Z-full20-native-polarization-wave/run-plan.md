---
run_id: GUH-20260730T064923Z-full20-native-polarization-wave
status: complete
repository: gu-formalization
workflow: joe-directed-north-star-construction
mode: execute
run_type: progress
lane_id: "1"
work_item: SOURCE-OWNED-CHIMERIC-BV-CAMPAIGN-S3-NATIVE-POLARIZATION
starting_revision: 852e57915b9f
opened_at: 2026-07-30T06:49:23Z
closed_at: 2026-07-30T07:43:04Z
claim_status_change: none
canon_change: none
public_posture_change: none
external_action_authorization: github_commit_and_push_only
write_boundary:
  - lab/process/runs/GUH-20260730T064923Z-full20-native-polarization-wave/run-plan.md
  - explorations/full20-native-polarization-closure-wave-2026-07-30.md
  - tests/channel-swings/full20_native_polarization_probe.py
  - tests/channel-swings/full20_observer_projector_support_probe.py
  - explorations/README.md
  - tests/README.md
---

# Full-20 native-polarization and conditional closure wave

## Authorization and purpose

Joe asked for a large swing orchestrating and running the full next
recommendation after the full-20 symbol/Noether pre-screen. This Run executes
that recommendation in its dependency order:

1. construct the program-native Krein pairing and graded polarization on the
   coarse \(S\oplus I\oplus R\) carrier independently of
   \(\det M(\mathbf h)\);
2. derive the native formal adjoints of \(c,T,\delta,Q\), test whether the
   written nine-block family is closed under them, and enlarge only if the
   action generates an out-of-family natural map;
3. intersect the independently admissible coefficient family with the raw
   principal kernel condition \(\det M(\mathbf h)=0\);
4. only if that intersection survives at the honest native grade, evaluate
   the five lower-principal remainders on the actual
   \(\operatorname{Sym}^2T^*X\) fibre; and
5. in parallel, harden the 20-projector support claim and hostile-check the
   already-owned `SA-Y8` Layer-0 disposition.

The Run does not select pairing phases, a domain, or a determinant root from
P1, P2, P3, a preferred retract, a generation count, or desired cohomology.
It does not identify a compact-support formal adjoint with a unique global
closed realization.

## Collision and owner check

The completed S2 owner is
`explorations/full20-irrep-symbol-noether-wave-2026-07-29.md` at revision
`852e579`. The completed, untracked
`GUH-20260729T131135Z-b5-native-packet-source-audit` is an input outside this
Run's write boundary and remains untouched. Existing owners also include:

- `explorations/shiab-operator/b5-krein-mirror-orbit-reduction-2026-07-25.md`;
- `explorations/sa-y8-majorana-layer0-and-vertical-krein-weld-2026-07-29.md`;
- `explorations/vertical-source-action-reduction-and-hessian-start-2026-07-29.md`;
- `tests/channel-swings/actual_fibre_cperp_b5_naturality_probe.py`; and
- `tests/shiab_b5_native_packet_contract.py`.

This Run must absorb, narrow, or extend those results rather than restating
them as new.

## Layer 0

| shared term | object in this Run | object it must not be collapsed with |
| --- | --- | --- |
| pairing | invariant Hermitian Krein form on \(S\), and the induced \(g\otimes K\) form on \(V\otimes S\) | a positive-Hilbert inner product or an arbitrary phase table on 20 labels |
| adjoint | formal adjoint of a differential expression under that pairing and a named Green formula | support transpose, ordinary conjugate transpose, or a selected closed realization |
| polarization | real graded Hessian of \(\frac12\operatorname{Re}\int\langle Z,DZ\rangle_K\) | the raw carrier endomorphism \(D\) |
| domain | compactly supported smooth core or one explicitly constructed common closed extension | an unspecified boundary condition or the existence of some extension |
| closure | invariance of the written natural-map family under the native formal adjoint | graph connectivity, 136-cell support saturation, gauge closure, or BV nilpotency |
| kernel condition | nonzero kernel of the raw principal coefficient matrix after native admissibility | a Noether identity, physical zero mode, cohomology, or generation count |
| lower remainder | actual differential/composition defect after the principal equations | a formal spanning symbol name or a compensator chosen from the desired endpoint |
| Majorana block | the exact domains/codomains recorded by the existing `SA-Y8` Layer-0 owner | a same-named but differently typed scalar/endormorphism channel |

The initial verdict is `SAME-OBJECT` for the coarse program-native
pairing/projector calculation, `HOMONYM` for the already-adjudicated two
Majorana uses, and `UNCERTAIN` for transfer from the compact-support formal
packet to a unique global closed operator or to normalized 20-slot phases.

No new substrate candidate is proposed, so L1--L7 are not refilled. L7 stays
on the indefinite/Krein branch.

## Construction fork

The load-bearing construction is:

- \(Y^{14}=\operatorname{Met}(X^4)\) with
  \(TY=TX\oplus\operatorname{Sym}^2T^*X\), not the exterior `6+4`
  numerical comparator;
- the program-native `Cl(9,5)` and `Sp(32,32;H)`/Krein keep-and-grade
  structure, not `U(128)` or positive-Hilbert ghost removal;
- the geometric gamma-traceless Rarita--Schwinger carrier, not the
  ghost-subtracted gravitino; and
- the full bilinear \(\langle Z,DZ\rangle_K\), never the operator \(D\)
  with the pairing treated as inert bookkeeping.

Any kill must name whether it applies only to this construction and whether
it transfers to the standard comparator.

## Preregistered expectation, kill, and go

Before computing the new packet, the expected result is:

```text
COARSE-S-I-R-KREIN-ORTHOGONALITY-CLOSES
NINE-BLOCK-FORMAL-EXPRESSION-FAMILY-ADJOINT-CLOSED
DET-M-INTERSECTION-NONEMPTY-LIKELY
GLOBAL-CLOSED-DOMAIN-AND-NORMALIZED-20-SLOT-PHASES-REMAIN-OPEN
```

The expectation is not a target. Exact adjoint phases, coefficient equations,
determinant factorization, residual rank, and lower-remainder outcome are
held out.

**Packet kill:** if the native pairing fails to make \(I\) and \(R\)
orthogonal, or if the formal adjoint generates a natural first-order map
outside the nine written blocks, the current family does not close. Enlarge
it by the generated maps before evaluating any determinant.

**Leakage kill:** if a pairing phase, adjoint sign, coflip, boundary form, or
domain is chosen because it makes \(\det M=0\), void the result. The native
packet must be frozen or carried symbolically first.

**Intersection kill:** if every independently admissible native coefficient
family has \(\det M\ne0\), kill only this primitive
\(S\to S\oplus I\oplus R\) gauge ansatz on the symmetric-fibre/geometric-RS
fork. Do not call it a global GU kill.

**Domain stop:** if only a compact-support formal Green identity can be
constructed, report `FORMAL-PACKET-CLOSED/GLOBAL-DOMAIN-OPEN`; do not promote
it to the five-field packet or native B5 exactness.

**Lower-order go:** evaluate the five spanning remainders only on coefficient
families surviving both native polarization and the principal kernel
condition. An out-of-span defect may type an enlargement; a coefficient
equation is not a new field.

**Projector go:** upgrade the 136-cell evidence only if all 20 normalized
provenance projectors/embeddings are independently constructed and every
matrix element is recomputed with planted omission, provenance-collapse, and
formula-blind controls. Otherwise retain the analytic-manifest grade and name
the exact residual.

## Parallel wave

- operator branch: derive \(K_{\mathcal E}\), \(S/I/R\) orthogonality,
  primitive adjoints, coefficient closure, and determinant intersection;
- source-action branch: build the Green/polarization/domain packet as far as
  the owned action permits and type the actual symmetric-fibre lower-order
  evaluation;
- hostile branch: rerun `SA-Y8` Layer 0, search existing owners, and audit
  target leakage, construction transfer, and all-20 projector evidence;
- integrator: reconcile the branches, implement one executable certificate,
  and preserve rival outcomes if their assumptions differ.

Branches begin read-only. Their synthesis does not replace conflicting
inputs.

## Controls and validation

1. Verify the full `Cl(9,5)` relations and invariance/nondegeneracy of \(K\).
2. Derive \(\Gamma^\times\), \(j^\times\), and
   \(P_I^\times=P_I\) rather than assuming orthogonality.
3. Plant an ordinary-Hilbert projector/adjoint and require the native test to
   distinguish it where signatures matter.
4. Check every primitive adjoint both algebraically and by random finite
   vectors; delete one metric sign as a planted failure.
5. Derive coefficient constraints before importing the raw \(M\) equations;
   hash or API-fence the native packet against determinant and P1/P2/P3
   inputs.
6. Compute determinant/intersection exactly where possible and use a
   nonzero-kernel witness plus perturbation and \(r=0\) rejection.
7. Separate compact-support formal closure, Green boundary form, and global
   closed-domain closure.
8. Keep support, formal-expression closure, Noether closure, and BV
   nilpotency as four different verdicts.
9. Re-run S1, S2, the observer ledger, orbit reduction, native packet
   fail-closed contract, vertical--Krein weld, and actual-fibre naturality
   controls.
10. Compile new probes, run relevant tests serially, run index gates, and run
    `git diff --check`.

## Held-out wall

Forbidden selectors and conclusions:

- P1/P2/P3, endpoint transport, or target count;
- desired `3E+` versus `3E-` cohomology;
- a chosen determinant root, vacuum, mass, or compensator;
- a positive-Hilbert replacement of the Krein pairing;
- the exterior `6+4` comparator;
- interpreting support/projector completeness as a domain theorem; and
- interpreting a raw principal kernel as a generation, index, or master
  equation.

## Execution and result

The operator, source-action, hostile Layer-0, and integration branches were
run. The integrated result is:

```text
NATIVE-SPINOR-KREIN-FORM-FIXED-UP-TO-SCALE
INDUCED-I/R-PAIRING-ORTHOGONAL
S/I-MULTIPLICITY-GRAM-NOT-FORCED
NINE-BLOCK-FORMAL-EXPRESSION-FAMILY-ADJOINT-CLOSED
ODD-POLARIZED-FULL-SUPPORT-DET-LOCUS-NONEMPTY
OBSERVER-COMPLEX-20-PROJECTOR-SUPPORT-REDERIVED
AUXILIARY-S/I-FORMAL-GAUGE-COMPLEX-EXACT
W177-ACTUAL-SYM2-CURVATURE-OBSTRUCTS-GENUINE-R-GAUGE-CLOSURE
FORMAL-GREEN-PACKET-BUILT/GLOBAL-NATIVE-DOMAIN-OPEN
NO-COMPENSATOR-SELECTED
```

The preregistered coarse-orthogonality expectation required one correction.
The induced \(I/R\) splitting is Krein-orthogonal, but the separate
isomorphic \(S\) and \(I\) fields admit a nontrivial invariant
\(2\times2\) multiplicity Gram. The nine-block family remains formally
adjoint-closed for that coarse freedom.

The candidate Grassmann-odd polarization retains the normalized \(Q\) block
and has an exact all-nine-block/all-three-gauge-component principal kernel.
Its determinant equation is one real constraint in eight real parameters,
so its bare constraint surplus is \(-7\): feasible, not confirmatory. The
opposite polarization erases \(Q\) and therefore cannot retain the full
136-cell support.

The five lower-principal remainders collapse exactly to two curvature maps:

\[
\mathcal C_S=\tfrac12\gamma^a\gamma^b\Omega_{ab},\qquad
\mathcal C_{RR}=P_R(\gamma^a\Omega_{ab}),
\]

with
\(\mathcal C_{II}=\mathcal C_{RI}=0\) and
\(\mathcal C_{IR}=-2j\mathcal C_S\). This exposes an exact
\(r_R=0\), all-nine-carrier-block auxiliary gauge complex on every
compatible background.

At the actual W177 symmetric-fibre point, the correctly frame-aligned
three-scale computation gives

```text
Scal              ~= -10.000000
||C_S||           ~= 28.28427
||C_RR||          ~= 21.04321
rank(C_RR:S->R)   = 128
||Gamma C_RR||    < 4.6e-15
```

so the current ansatz has no genuine \(r_R\ne0\) gauge identity there. This
is a local background/ansatz obstruction, not a global GU no-go; W177 is
already nonstationary.

One in-wave numerical pass was voided before disposition. It contracted
W177's grouped \((+^9,-^5)\) frame with the interleaved native \(4+10\)
gamma/sign order, producing the spurious
`Scal ~= -0.640428` and `||C_RR|| ~= 15.879645`. The final probe permutes
the frame labels, independently matches a grouped Clifford realization, and
retains the unpermuted computation as a planted failure.

The hostile branch confirmed that the two existing `SA-Y8` “Majorana
blocks” are homonyms, not a contradiction. The physical four-dimensional
odd-form bilinear remains open. The independent thin-embedding probe builds
all 20 provenance-labelled observer slots and reproduces all
\(68+68=136\) cells with a \(6.35\times10^{14}\) zero/nonzero gap.

## Validation receipt

Passed serially:

- `tests/channel-swings/full20_native_polarization_probe.py`;
- `tests/channel-swings/full20_observer_projector_support_probe.py`;
- the S1 and S2 full-20 probes;
- the complete observer multiplicity ledger;
- the Krein mirror-orbit reduction;
- the fail-closed native packet contract;
- the vertical--Krein weld;
- actual-fibre coflip/B5 naturality;
- normalized transport from the written differential; and
- the W177 ambient Yang--Mills nonstationarity gate.

Both new probes compile. The exploration surface map, exploration top-level
boundary, tests-root inventory, research-posture, root-entrypoint, and public
path-hygiene process gates pass. `git diff --check` passes.

The completed, untracked
`GUH-20260729T131135Z-b5-native-packet-source-audit` remains outside this
Run's boundary and was not modified.
