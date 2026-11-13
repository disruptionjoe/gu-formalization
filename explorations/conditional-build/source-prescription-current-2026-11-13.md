---
title: "Source primitive variations and the native-trace current test"
status: exploration
doc_type: structural-result
created: '2026-11-13'
program_target: X-P1-P2
tier: T2
expected_delta: Test complete source-category membership without discarding independent fields or changing observation silently
actual_delta: "Constrained - source full-parent current has rank128 native-trace defect in held field coordinates"
classification: INTERNAL_STRUCTURAL_ONLY
target_claim: NONE-NOT-A-KILL
bears_on: [SC-OP-04, SC-OP-05]
canon_verdict_change: none
---

# Source primitive variations and the native-trace current test

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Its result binds only the
> named model and does not adjudicate Weinstein's source-native mechanism
> without a typed bridge. Read `lab/methods/source-native-comparator-routing.md`
> and follow its source-native pointers. Classification: `INTERNAL_STRUCTURAL_ONLY`.

program_target: X-P1-P2
tier: T2
expected_delta: Apply prior current and full operator tests to the same source-guided geometric prescription
actual_delta: Constrained - source full-parent current has rank128 native-trace defect in held field coordinates

```gu-typed-objects
result: Source primitive variations and the native-trace current test
carrier: full complex Dirac S128; independent one-form and scalar fields with four independent bars/unbarred slots LAYER=ambient+observed BRIDGE=literal-section-plus-gamma-trace CHIRALITY=S-FULL-DIRAC
pairing: fixed nondegenerate density dual; held versus transported current and primitive connection variations separately typed ON=declared_carrier
real_structure: complex Clifford identities; K77 real and K95 quaternionic structures separately typed; no signature transfer inferred
grading: ambient spin labels, auxiliary operator grade and effective physical chirality remain distinct
action_owner: repository-construction -- structural comparison of source-print ingredients; no selected full action
target: source-primitive current compatibility MAP-TYPE=intertwiner
```

## 1. Source custody and the distinction that is already settled

Read the primary 2021 draft §§3.6,5–9,12 from the fresh PDF with SHA256 `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`, using the rendered section9 transcription for the operator cells. Relevant full records: SC-GRP-02/03/06, SC-GEO-51/55, SC-OP-02/04/05 and SC-META-56. Current comparator routing applies; the source's nonchiral total/effective 2+1 construction is not replaced by a standard chiral-family model. The main source group is U(64,64), not the stale unconditional Sp entry in the guide. K77 assertion and K95 geometric arithmetic remain distinct.

The source is NOT silent about which connection is varied. Its primitive fields are the metric section g, epsilon in the gauge group, and the independent ad-valued one-form varpi, plus four independent fermionic fields. At a temporarily fixed g, §6 constructs the reference connection A0[g]; equations (6.18)–(6.22) and (7.3) define

    A = A0 + varpi,
    B = A0^epsilon = A0 + epsilon^-1 d_A0 epsilon,
    T = A-B = varpi-epsilon^-1 d_A0 epsilon.             (C1)

The displayed translation variation (9.7), again (9.12), changes varpi by s alpha with epsilon and g fixed. Section5 defines the translation module as ALL Omega1(Y,ad P_H), with H=U(64,64) fixed in §3.6. The metric-induced A0 is a distinguished origin in the affine space of connections; it does not restrict A to its gauge orbit. Restricting varpi to a stabilizer or to a function of epsilon is an additional constraint, not the source's displayed primitive translation slice.

This is inherited knowledge, not a new discovery: `lab/sources/gu-moving-shiab-epsilon-green-source-reinspection-2026-08-05.md`, `selected-k77-common-field-dupsilon-varpi-block-source-reinspection-2026-08-08.md` and `selected-k77-principal-ward-gamma-epsilon-reconciliation-source-reinspection-2026-08-08.md` already own fixed-epsilon translation and primitive-epsilon separation. The June24 `misc/constraint-first-ig-tangent-space-gate` separately notes that a tau graph does not restrict the entire IG variation space. The new result below is applying that settled source prescription to the SAME native-trace adapter and its actual cross-current response.

**Source sign custody.** The draft's footnote7, p.36, acknowledges conflicting sign conventions. Some subsequent proofs print a minus sign in a tilted action and then use a plus sign in the expansion; the prose after (7.4) also reverses A/B names. All formulas here use the explicit definitions (6.22),(7.3), the standard right connection transformation A0^epsilon=epsilon^-1 A0 epsilon+epsilon^-1 d epsilon, and the independently fixed translation test (9.7). No inconsistent intermediate equivariance line is treated as a new source law.

## 2. Complete primitive first-variation map

Write alpha=delta varpi, eta=epsilon^-1 delta epsilon, and beta=delta A0. In a fixed local bundle identification, beta=(D_g A0)[h] for a metric variation h; any separate spinor/Clifford identification is transported explicitly. The exact linearization of (C1) is

    delta A = beta + alpha,
    delta B = Ad_(epsilon^-1) beta + D_B eta,
    delta T = alpha + (Id-Ad_(epsilon^-1))beta-D_B eta. (C2)

For fixed g, the conjugated invariant Shiab tensors satisfy

    Phi_i^epsilon = epsilon^-1 Phi_i epsilon,
    delta Phi_i^epsilon = [Phi_i^epsilon,eta].           (C3)

For moving g, add Ad_(epsilon^-1)(delta_g Phi_i), plus the actual metric/Hodge/density derivatives; these are separate primitive owners. They are not derivatives with respect to varpi. Thus:

| Primitive direction | delta A | delta B | delta T | Hodge/metric/density |
|---|---|---|---|---|
| varpi only | alpha | 0 | alpha | fixed |
| epsilon only | 0 | D_B eta | -D_B eta | fixed unless an extra dependence is declared |
| metric only | beta | Ad_(epsilon^-1)beta | beta-Ad_(epsilon^-1)beta | vary with g |

In particular a source-geometric trace adapter C[g]=c(t[g]) is independent of varpi during the first row. Moving the physical metric section changes C, A0, Hodge and the observation together, but cannot cancel an independently polarized varpi Euler coefficient by being included in the wrong primitive row.

For a functional expressed in (B,T,Phi,g,fermions), let E_B,E_T be its partial Euler covectors with the listed other arguments held, and let ! denote formal dual differential operation in the variation pairing. Then the chain gives

    E_varpi = E_T,
    E_epsilon = D_B^!(E_B-E_T) + Phi/explicit-epsilon terms,
    E_g = explicit metric terms
          + (D_g A0)^!(E_T + Ad_(epsilon^-1)^!(E_B-E_T)).  (C4)

Fermionic wrapper changes contribute their own epsilon terms. These identities specify the primitive routing, not a selected functional or a computed full metric Hessian. They do not identify source D_omega Upsilon with the Frechet derivative D_epsilon Upsilon. They also do not require a separate action for the proposed odd graded structure (SC-META-56).

## 3. The actual displayed candidate cross vertex

Equation (9.16) has NE cross block d_A from the independent scalar nu to the one-form spinor row. Its four varpi cells are the four blocks of the spin action of varpi. On the primitive varpi slice,

    delta_varpi d_A[alpha] nu = rho(alpha) nu,

and for a simple alpha=xi tensor T,

    delta_varpi d_A[alpha] nu = xi tensor rho(T) nu.      (C5)

This is an operator-cell statement authenticated by the displayed matrix, not an inference from the mere monomial names in (9.18). It is independent of which Shiab contraction occupies NW. Independent field polarization sets zeta=0 and bar-nu=0 and therefore isolates this NE coefficient; no NW self-current or SE rival term can cancel its bar-zeta/nu bilinear while those fields remain independent.

At fixed epsilon the rho(epsilon) and rho(epsilon^-1) wrappers are fixed invertible row/column maps. They transport (C5); they do not add delta-epsilon or delta-g terms to it. A local expression that treats epsilon as epsilon[varpi] changes the primitive field space and requires the full chain rule. The source does not impose that restriction in (9.7).

To turn (C5) into equality of density-valued currents, supply the same fixed nondegenerate one-form/spinor density map B1 on both sides. Its actual numerical coefficients are not needed for the injectivity argument. The source already supplies a nondegenerate spinor-form framework, but this proof does not invent its global density, boundary, real-form or action completion. If the eventual source current is projected or degenerate, its additional kernel must be typed and this theorem applied after that projection. Equation (9.18) by itself remains insufficient to identify an arbitrary completed physical current.

The current test is therefore sharper than both extreme readings:

- It is too weak to say that the varpi connection direction is wholly unknown: the source fixes it and gives the actual cross-arrow variation.
- It is too strong to claim that the complete physical current/density/domain is uniquely fixed by (9.18): it is not.

## 4. Source full-parent variation removes the sterile freedom

The source main group on the full complex Dirac carrier contains the central generator iI. At any point choose alpha=i xi I with a nonzero covector xi and compact support locally. This is an allowed primitive varpi variation. Since multiplication by iI is invertible on the full complex Dirac S, the common kernel Z of all rho(T) is zero. This conclusion does not depend on any PS/SM/colorEM branching or on the source's effective low-curvature chirality claim. If an additional real/quaternionic-preserving connection restriction removes iI, the central test below must not be transferred to that restricted category; use its actual nonzero charged-support theorem instead. A source full-U parent and a smaller real-structure-preserving subgroup are different variation spaces.

For the earlier frozen scalar-only family

    K' = f diag(I,U) K diag(I,V),

held equality of the tested cross vertices implies

    f V = I,   f U = I,                                 (C6)

when the typed SW response is also retained. NE alone forces the first equation. Thus the sterile-coordinate freedom that survived a restricted SM or colorEM effective current disappears for the actual full-parent primitive translation test. A separately authenticated effective projection or restricted connection space changes the test; a vacuum stabilizer alone does not.

**Central guard against false epsilon escapes.** Conjugation preserves iI. Hence any fixed epsilon conjugation or other invertible common frame transport preserves the full-support test. A connection chosen to preserve a background trace also has central iI in its stabilizer, so merely imposing trace-parallelism does not restore a global odd scalar current-preserving map. Removing the central variation would require a further traceless/restricted variation prescription, not a consequence of having a trace adapter.

## 5. Native trace: full-rank defect for the actual paired repairs

Use the source-adapted trace result supplied by the companion geometry proof: the selected metric horizontal lift makes the metric section horizontal, its vertical trace t is an actual normal vector, and in the native DeWitt normalization

    <t,t> = -4,
    C=c(t),  C^2=-4I.                                  (C7)

This does not transfer K77 reality conventions to K95; it is a Clifford identity on the explicitly declared metric branch and its complex Dirac module. It also does not imply C is parallel for the full ambient reference connection.

For the two preceding odd-adapter repairs, with all paired density maps retained:

1. NW/dual repair: R_-=diag(I,C^-1), B^C D_- = lambda B R_- D R_-, lambda=-4. Its NE scalar factor is lambda C^-1=C.
2. Cross-arrow repair: R_+=diag(I,C), B D_+=B R_+ D R_+. Its NE scalar factor is C.

Neither step commutes B through C; in density-row coordinates the left factor is B R B^-1. Both repairs therefore change the isolated held NE vertex from B1(xi tensor rho(T)) to B1(xi tensor rho(T) C), with fixed epsilon wrappers transported consistently.

At the central variation T=iI the defect is

    Delta V_NE = i B1 (xi tensor (C-I)).                 (C8)

Because

    (C-I)(C+I) = -5I,
    (C-I)^-1 = -(C+I)/5,                               (C9)

this defect is injective on the entire scalar S and has complex rank128, for nonzero xi and nondegenerate B1. The written polynomial identity proves the full rank; the small exact control is not a sampled 128-dimensional rank claim. Epsilon's fixed invertible wrappers preserve this rank. No Shiab selector, ordinary family count, physical positivity or global spectral computation is needed.

For a real nonzero scalar renormalization f, (fC-I)(fC+I)=-(4f²+1)I, so the full-rank defect persists. If complex normalizations are allowed, f=±i/2 can make the defect singular on one eigenspace, but it still cannot make fC=I because C is odd with respect to a nontrivial ambient grading. Consequently full-rank *defect* is convention-sensitive under arbitrary complex normalization, whereas nonzero held-current incompatibility is not. A scalar scale with physical dimensions must be fixed before comparing to I; equations (C8)-(C9) concern precisely the normalized repair conventions of the prior notes.

This excludes equality of the original and repaired *literal candidate* cross-current on the source primitive slice. It does not exclude a changed-current rival, a scalar/row redefinition with transported observables, a degenerate physical readout, or an action in the full declared class C. These categories were never all required to preserve this literal candidate vertex.

## 6. Why moving geometry and an adapted connection do not erase this current

On the source metric connection, the companion geometry proof reuses the owned identity along the section

    nabla^A0_X t = (1/2) X^H,
    nabla^A0_X C = (1/2)c(X^H).                         (C10)

Thus horizontal trace-norm preservation is not full ambient parallelism. The exact cross-arrow compensation is e nabla C, so at the reference connection it includes the explicit e c(X)/2 term. For the NW repair it is -e(nabla C)C^-1. These lower-order terms are required for differential equivalence, and their variation must be retained.

A metric/spin connection adjustment may make C parallel; for X orthogonal to t,

    K_X = c(X)C/16,
    [K_X,C] = -(1/2)c(X).                              (C11)

Then A*=A0+K has nabla^A* C=0 along those directions. The parent connection field admits such an adjustment whenever its actual metric-spin inclusion and reality category are supplied. This is a structural connection alternative, not a selected stationary solution, and it does not by itself repair all traceless second-fundamental-form leakage.

The key current point is independent of that geometric choice. At a background where nabla^A C=0, varying the primitive varpi still gives

    delta_varpi(nabla^A C) = [rho(alpha),C].             (C12)

A vanishing coefficient at one background does not imply its derivative vanishes. In particular the compensated cross arrow d_A composed with C has vertex rho(alpha)C; the rewriting C d_A+nabla^A C has the same vertex, since C rho(alpha)+[rho(alpha),C]=rho(alpha)C. The central alpha makes the commutator zero but leaves the factor iC, which is already enough for (C8). Thus neither the native A0 compensation nor trace-parallel background tuning is a fixed-current escape.

If the allowed connection space is genuinely constrained to trace-preserving connections, tangent variations satisfy [rho(alpha),C]=0. This constraint still includes iI; its current is still iC rather than iI. A smaller, explicitly supplied physical response could annihilate the defect, but that is an observation/current map to be derived—not an implication of parallelism.

## 7. Primitive epsilon wrapper response and the surviving branch

Let E=rho(epsilon), choose column notation, and write the wrapped density operator as K_epsilon=E D_epsilon E^-1, suppressing the correctly typed fixed density dual. For eta=E^-1 delta E, the exact derivative is

    delta_epsilon K_epsilon
       = E( delta_epsilon D_epsilon + [eta,D_epsilon] )E^-1. (C13)

The commutator is of differential operators; on d_A it is -D_A eta, not a bare coefficient commutator. Direct delta_epsilon D includes the moving Shiab contraction (C3). Integration by parts in (C13) yields the independent barred/unbarred matter Euler chain terms. This is compatible with the source's combined total Euler architecture, without asserting that the printed redundant Xi relation alone supplies all these terms.

The exact coordinate-transport branch remains nonempty: define new fields and independent bars through the actual invertible R/L maps, and transport the density, source observation, physical-current readout, grading and common domain. The old current evaluated on the old fields equals its pullback evaluated on the new fields. That is a legitimate equivalence and not the held-current condition (C6). Source wrappers already demonstrate the relevance of moving frames; they do not select the additional scalar trace-coordinate change or authenticate its physical readout.

Consequently the fastest next genuine discriminator is the literal-versus-transported scalar/current identification in the source's observed fermions, not another generic question about which primitive connection direction exists. If literal nu/current is retained, the above source-candidate compatibility test is already decisive. If scalar/current coordinates are transported, the next test is their actual observation/physical-sector and domain map. Full-parent and effective-current comparisons must remain distinct.

## Acceptance and prior-art limits

The retained primitive/current suite supplies exact supporting controls: full primitive matrix jet (C2), fixed-epsilon translation, moving invariant-tensor derivative, wrapper differential commutator, native-trace current defect and its inverse, complex normalization countercontrol, and trace-parallel commutator control. No full matrix current rank sampling or action search is needed.

The source-variable dictionary, Maurer–Cartan derivative and generic chain rule were already owned in August. The new contribution is their complete primitive routing against the November13 same-trace repairs, elimination of false epsilon/metric/parallel-background escapes, and the full-rank central-current defect (C8)-(C9). No source-level falsification, physical chirality claim, family count or change in class C follows.

## Evidence and acceptance

- [Primary 2021 draft](https://geometricunity.nyc3.digitaloceanspaces.com/Geometric_Unity-Draft-April-1st-2021.pdf), §§3–4,6–7,9,11–12. Retrieved content SHA256: `3f28d742234a9841fc8e51ff172053200aa3eddf3ece38154a3328b9ebd186d4`.
- Source claim custody: `lab/sources/source-claim-register.yaml`; displayed operator: `lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md`.
- Prior symbol/receiver theorem: `explorations/conditional-build/source-symbol-quotient-membership-2026-11-12.md`.
- Prior joint tests: `explorations/conditional-build/source-joint-symmetry-current-2026-11-13.md` and `explorations/conditional-build/source-moving-repair-2026-11-13.md`.
- Companion: `explorations/conditional-build/source-chimeric-trace-compatibility-2026-11-13.md`. Replay: `tests/program-focus/source_prescription_probe.py`; dependency hashes and evidence: `lab/process/source-prescription.json`.

Independent specialist cross-review and four exact supporting/contrary suites
support conditional T2 acceptance. Written universal proofs carry the claims;
reduced-dimensional controls do not prove source selection or physical dynamics.
No Lean, full-action derivation, source/class-C verdict or physical prediction
is claimed. Matrix18/18 remains constrained and the triple intersection open.
