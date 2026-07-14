---
artifact_type: exploration
status: "exploration (W189; adversarial joint attack on law/shadow plus boundary selection; conditional register; no claim, canon, or status movement; one lightweight deterministic discriminator supplied but not executed in this worker)"
created: 2026-07-14
wave: W189
label: W189
posture: coherence-first; ruthless countermodel discipline; exploration grade; no manufactured coherence
hypothesis: "Stories 2 and 3 can form an explanatory architecture only if the law fixes its observable shadow independently, the boundary selector is prior and compressed, and the selected TOTAL keep-and-grade dynamics is healthy. Otherwise the combination can redescribe any outcome without explaining it."
title: "W189: three countermodels to law/shadow plus boundary selection, and the minimum conditions for the combination to explain rather than relabel"
verdict: "CONDITIONAL-SURVIVAL, NOT-YET-EXPLANATORY. Three exact countermodels kill the unrestricted story. A: the same bulk law with two admissible shadow maps has opposite apparent stability, so simplicity of the parent law does not explain the observed shadow. B: the same bulk mode, shadow energy, reservoir energy, and coupling magnitude has a real total spectrum for a like-Krein-signed reservoir and a complex pair for an opposite-signed reservoir, so openness does not select health. C: a full-rank boundary-to-observable map absorbs every residual and leaves prediction codimension zero, so boundary selection becomes an epicycle. What survives is a narrower and testable architecture: one independently derived shadow map; one prior, economical, target-independent selector that resolves the W186 bistability; a real-spectrum positive-total-C result for the selected total dynamics; at least one boundary-insensitive observable relation; and no knob shared between shadow choice and boundary repair. The current GU work has candidates for each ingredient but has not jointly met them."
grade: "EXACT for the finite countermodels and rank/discriminant certificates in tests/W189_countermodel_discriminators.py: A uses exact Krein quadratic forms +1 and -1 over the same eta and law-level c_R=0; B uses exact 2x2 K-pseudo-Hermitian matrices with discriminants +5 and -3; C uses exact rational ranks 3 and 1 and an identity right-inverse certificate; the discriminator is purely structural and contains no target values. STRUCTURAL for the lift to GU: these are countermodels to an inference form, not derivations of GU's dressed shadow or source kernel. Their job is to state what the missing calculation must rule out. No test/build run by this worker."
construction: "Program-native objects are named where GU is implicated: noncompact Sp(32,32;H) with its indefinite Krein form; KEEP-AND-GRADE via a total C-operator/[P,S]=0 rather than positive-Hilbert ghost removal; Z/3 torsion rather than a Z index for generation count; base X4 metric separated from the gimmel/DeWitt metric on Met(X4); GU's actual linear/shiab-Einstein law separated from the induced |II|^2 self-energy; and the native ker(Gamma) projector/record current separated from a physicist cubic decay vertex. Standard machinery is used only as portable diagnostics: pullback quadratic forms, 2x2 Krein spectral theory, Fano/Friedrichs reservoir blocks, and exact rank. Every kill below states whether it survives the alternate construction."
depends_on:
  - GEOMETER-VS-PHYSICS-OBJECTS.md
  - explorations/W167-reduction-direct-sign-alpha-beta-2026-07-14.md
  - explorations/W176-build-reduction-x4-effective-2026-07-14.md
  - explorations/W179-build-c-operator-allorders-2026-07-14.md
  - explorations/W180-build-matter-connection-bridge-c3-2026-07-14.md
  - explorations/W182-external-input-source-selfenergy-2026-07-14.md
  - explorations/W183-external-input-open-system-reframe-2026-07-14.md
  - explorations/W184-mirror-superselection-decay-2026-07-14.md
  - explorations/W186-source-content-reservoir-krein-type-2026-07-14.md
scripts:
  - tests/W189_countermodel_discriminators.py
---

# W189: law, shadow, boundary, or relabel?

## 0. Result first

The strong joint version of Stories 2 and 3 is not yet an explanation. It is an explanatory
*architecture with missing selection theorems*.

The attractive version says:

> A simple law on a larger geometry has a controlled observable shadow, while a small boundary or
> history datum selects which admissible world is actual.

The unrestricted version says:

> Choose whichever shadow makes the bulk look healthy, then choose whichever boundary datum makes
> the resulting world match observation.

Those sentences sound similar. They are scientifically opposite. Three minimal countermodels locate
the difference:

1. The law does not explain the shadow if more than one admissible shadow map changes stability.
2. The boundary does not explain health if both a healthy and a pathological total are allowed and
   nothing prior selects between them.
3. The boundary does not explain actuality if its free response spans every observable residual.

The architecture survives only as a constrained conjunction: **fixed shadow, prior selector,
healthy total, predictive surplus**. Any one missing term turns the story into a relabel.

## 1. Construction-fork ledger

The countermodels are deliberately small, but the inferences are construction-sensitive. This is the
mandatory fork ledger.

| Load-bearing object | Construction used here and why | Alternate construction and transfer of the result |
|---|---|---|
| Gauge group | GU-native noncompact `Sp(32,32;H)` / indefinite Krein structure. Countermodels A and B need the relative Krein type that noncompactness supplies. | Compact `Sp(64)` with a positive Hilbert metric removes this exact sign geometry. It does not refute A's broader map-underdetermination or C's rank no-go, but B's specific opposite-type exceptional point is native-Krein-specific. |
| Ghost treatment | GU-native **KEEP-AND-GRADE**. Health means a real total spectrum with a positive total `eta_+ = eta C`, or the corresponding dynamical condition such as `[P,S_tot]=0`. No negative sector is projected away. | Positive-Hilbert ghost removal makes B inapplicable because it deletes the tested state. That is not a rescue unless the removal itself is derived. Open positive-Hilbert systems still need a prior reservoir and still face C. |
| Generation count | No integer-index argument is used. If generation count enters the boundary story, its native arena is `Z/3` torsion, not a `Z` index. | A `Z`-index derivation cannot reach the native 3-primary object. Calling `3` a boundary selection may be honest, but then it is selected, not geometrically derived. Countermodel C applies to either arena. |
| Metric | The base spacetime metric on `X4` and the gimmel/DeWitt metric on `Y14 = Met(X4)` are kept distinct. Countermodel A's `eta = diag(+1,-1)` is the minimal field-space/Krein block, not the spacetime metric. | A one-metric positive-definite reduction cannot realize this exact sign flip. It still must prove its shadow map is unique. The GU-specific stability flip lives on the two-metric, indefinite side. |
| Law versus shadow | GU's actual law is the linear, shiab-Einstein `I1B` law with law-level `c_R=0` (W167). `|II|^2` is treated as a distinct induced bending/self-energy construction unless the missing bridge identifies it. | A standard freely chosen `R^2/Weyl^2` action starts at the shadow level and cannot establish the GU law-to-shadow map. Countermodel A kills the inference from a simple parent law until that map is built; it does not kill either candidate shadow. |
| Source / soldering | The native boundary candidate is W180's projector/current construction: `Psi in ker(Gamma)` and `J^a = Re<Psi,K_S e_a Psi> = delta S_D/delta A_a`. Countermodel B uses a standard 2-channel Krein block only to diagnose what the unbuilt native kernel must decide. | The physicist cubic ghost-to-two-graviton vertex is a different construction. W184's parity violation is decisive for that vertex, not automatically for the native projector/current. Conversely, the native current being an exact EL derivative does not prove its dressed spectral density has the healthy sign. |

The rule is not to favor the native side. It is to prevent a result on one fork from silently
masquerading as a result on the other.

## 2. Countermodel A: same law, different shadow, different stability

### Construction

Take the law-level scalar coefficient to be the W167 value

```text
c_R^law = 0.
```

Give the parent field space the minimal indefinite metric

```text
eta = diag(+1,-1).
```

Now admit two one-dimensional shadow maps from the same parent object:

```text
R_+ x = (x,0),       R_- x = (0,x).
```

Their pulled-back quadratic forms are exact:

```text
R_+^T eta R_+ = +1,       R_-^T eta R_- = -1.
```

The bulk law and parent metric are identical. Only the shadow map changes. One observer calls the
mode stable; the other calls it unstable.

This is not a claim that either `R_+` or `R_-` is GU's reduction. It is the minimal proof that the
sentence "the fundamental law is simple, therefore the complicated shadow is harmless" is invalid
until the law fixes its shadow map.

### What it attacks in the current arc

W167 already exhibits the real version of this logical gap:

- law level: linear/shiab-Einstein, `c_R=0`;
- first-order Ricci-class shadow: `c_R=-1/6` under a positive inner product;
- geometric `|II|^2` shadow: a different Weyl-carrying point, `c_R=-4/9`;
- Krein interpretation: the trace mode can flip the physical sign.

The countermodel says those distinctions cannot be narrated away. The explanatory burden is a
unique covariant construction from `I1B` and the two metrics to the observable vertical Hessian.

### Strength and transfer of the kill

- **Killed:** stability inferred from the parent law without a fixed reduction functor.
- **Not killed:** the possibility that GU's actual reduction uniquely fixes a healthy shadow.
- **Native specificity:** the exact positive/negative flip uses the indefinite gimmel/Krein metric.
- **Survives the positive-Hilbert fork:** the broader underdetermination remains whenever two
  effective maps generate inequivalent coefficients, even if both norms are positive.

The test includes a matched control: a mere `K`-isometric relabel of the same positive direction does
not change its sign. The failure is a construction change, not a coordinate artifact.

## 3. Countermodel B: same law and shadow, different reservoir, different total

### Construction

Keep fixed:

- one bulk/shadow mode at energy `0`;
- one reservoir mode at energy `1`;
- coupling magnitude `|g|=1`;
- KEEP-AND-GRADE quantization.

Change only the reservoir's Krein type relative to the ghost.

Like-signed reservoir:

```text
K_like = diag(-1,-1),       H_like = [[0,1],[1,1]].
```

Opposite-signed reservoir:

```text
K_opp  = diag(-1,+1),       H_opp  = [[0,1],[-1,1]].
```

Both satisfy the correct exact condition

```text
K H = H^T K.
```

But their characteristic discriminants differ:

```text
Delta_like = +5  -> two distinct real eigenvalues -> positive total metric is available;
Delta_opp  = -3  -> a complex-conjugate pair -> no positive total C-metric.
```

With the channel removed, both reduce to the same real diagonal spectrum. The pathology is caused by
the interaction and relative Krein type, not by naming one state "reservoir."

### What it attacks in the current arc

This is the smallest exact version of the W183/W186 fork:

- W183 showed that a like-signed reservoir can make the total real while the reduced subsystem looks
  non-unitary, but an opposite-signed reservoir can drive a total exceptional point.
- W186 showed that a favorable C-positive fixed point and a pathological fixed point can both be
  self-consistent and stable.
- W184 showed that the Cartan grading alone is not a selector: the cubic cross vertex used in that
  model is parity-odd, so superselection requires the additional dynamical fact `[P,S]=0`.

Therefore "the world is open" does not rescue anything by itself. Openness adds a selector-shaped
question. It does not answer it.

### Strength and transfer of the kill

- **Killed:** boundary openness as an unconditional explanation of stability or unitarity.
- **Killed:** existence of a healthy self-consistent fixed point as selection of that fixed point.
- **Not killed:** a prior law of boundary selection that chooses the like-signed branch and produces a
  positive total `C`-metric.
- **Construction bound:** the exact exceptional-point model is the native keep-and-grade/Krein fork.
  Removing the ghost makes it irrelevant, but that moves to a different theory.
- **Source bound:** this does not assert that W180's native record current realizes either matrix.
  That relative sign is the missing calculation. The W184 parity result transfers only if GU's
  native source kernel really contains the tested cubic vertex.

## 4. Countermodel C: enough boundary freedom absorbs every observable

### Construction

Let a fixed law and shadow predict a vector `p` of three observables. Let the boundary contribution be

```text
O = p + A b.
```

If

```text
A = I_3,
```

then `rank(A)=3`. Every residual direction has a boundary preimage. For any observed vector `y`, one
can choose `b=y-p` and fit it exactly. The prediction codimension is

```text
3 - rank(A) = 0.
```

The test certifies this without supplying any targets: each standard basis residual is in the image
of `A`, hence by linearity every residual is. This is a structural epicycle certificate, not a bad
fit statistic.

The positive control uses one shared boundary scalar,

```text
A = (1,1,1)^T.
```

It has rank `1`, so two target-independent relations survive. Such a boundary datum can select an
overall level while still making two predictions.

### What it attacks in the current arc

Story 3 is strongest when it says laws constrain the space of worlds and a small historical datum
selects one. It becomes empty when every unexplained constant, generation, sign, epoch, and spectrum
feature is promoted to a separate boundary choice.

In particular:

- calling the generation count a boundary datum can be honest, but it is not a derivation of the
  native `Z/3` torsion class;
- calling the reservoir type a boundary datum can be honest, but it must be fixed independently of
  the pole it is invoked to repair;
- calling the source magnitude a boundary datum can be honest, but it must leave invariant relations
  among observables rather than absorb the full residual vector.

### Strength and transfer of the kill

This is the strongest and most portable no-go in the wave. It does not depend on the gauge group,
metric signature, ghost prescription, or source vertex. A full-rank free boundary response is
non-predictive under every construction fork.

## 5. The minimum joint conditions

The law/shadow plus boundary-selection picture becomes explanatory rather than a relabel only if all
of the following hold jointly.

### J1. Shadow stability is invariant under every admissible shadow construction

The theory must derive the map from the linear `I1B` law on `Y14` to the effective operator over a
section `sigma:X4->Y14`. Coordinate or gauge-equivalent versions may differ, but all admissible maps
must agree on qualitative pole/stability data. One cannot select after the fact among the
shiab-Einstein shadow, geometric `|II|^2`, or a sign-flipped Krein reading.

### J2. The boundary selector is specified prior to the targets and resolves the basin

The sign, type, and measure on admissible boundary data must be supplied before consulting the
observables they are meant to explain. In the W186 language it must select between the two stable
fixed points, not merely prove the favorable one exists. A prior probability law could qualify, but
only if it gives non-retrofitted likelihoods rather than an unconstrained existence claim.

### J3. The selected TOTAL dynamics is healthy in the native keep-and-grade sense

The reduced geometry need not be unitary by itself. The selected total system must have a real
spectrum and a positive total `eta_+ = eta C` or an equivalent all-orders result. Bare Cartan grading
is insufficient; W184 shows the relevant dynamic commutator must be checked. This condition must be
tested on `Sp(32,32;H)`/Krein data, not replaced silently by compact `Sp(64)` or ghost removal.

### J4. Boundary freedom is compressed and leaves predictive surplus

For `n` independent observables and boundary response Jacobian `A`, require at minimum

```text
rank(A) < n
```

and an economical declared boundary dimension. At least one relation must be invariant under every
allowed boundary choice and available as a holdout prediction. A better theory should yield a large
prediction codimension, not merely one.

### J5. Shadow and boundary knobs are independent

The same parameter may not choose the shadow map, flip its stability sign, select the reservoir, and
fit the observable magnitude. Otherwise the two stories repair one another in a closed loop. The
shadow is derived first; the boundary acts on that fixed shadow; predictions follow last.

### J6. Every construction fork is declared at the claim site

This is substantive, not editorial. A claim about a `Z` index is not a claim about `Z/3`; a
physicist vertex is not the native projector/current; the spacetime metric is not the gimmel metric;
an induced `|II|^2` self-energy is not the linear law; positive-Hilbert removal is not keep-and-grade.
Without the declaration, the explanatory score is undefined.

The accompanying discriminator splits these into seven machine-checkable gates: shadow invariance,
prior selector, predictive surplus, boundary economy, positive total `C`, level independence, and
fork declaration. The architecture passes only if all seven pass. The score is diagnostic; the
Boolean conjunction is the verdict.

## 6. What the lightweight test proves

`tests/W189_countermodel_discriminators.py` uses only the Python standard library and exact rational
arithmetic. It is deterministic and contains no observed targets.

It supplies:

- exact `+1/-1` pullback signs for countermodel A;
- exact `K H = H^T K` checks and `+5/-3` spectral discriminants for countermodel B;
- exact ranks and a right-inverse certificate for countermodel C;
- a positive architecture control that passes every gate;
- matched failures in which A fails shadow invariance, B fails prior selection, and C fails predictive
  surplus plus boundary economy.

The test is an audit of explanatory form. It does not compute GU's actual shadow, actual dressed
reservoir, or actual observable Jacobian.

## 7. Ruthless verdict

### Killed

1. **"The parent law is simple, therefore the observed higher-order instability is only apparent."**
   Killed as an inference. Simplicity at law level does not determine a shadow map.
2. **"Opening the geometry makes the ghost an issuance channel, therefore the total is healthy."**
   Killed as an unconditional inference. The reservoir's relative Krein type decides the total.
3. **"A self-consistent healthy solution exists, therefore that is the realized solution."**
   Killed by the bistable countermodel already exposed in W186 and compressed here to B.
4. **"Whatever remains unexplained is boundary/history."**
   Killed whenever the boundary response is full rank. That formulation can absorb every world.
5. **"The Cartan grading automatically forbids the bad channel."**
   Killed for the W184 cubic-vertex construction. A grading is not a conserved superselection rule;
   the dynamic commutator is load-bearing.

### Survives

1. **A simple linear parent law can organize a complicated effective world.** It survives if the
   observable shadow is uniquely derived rather than selected.
2. **Boundary/history can select actuality without being an epicycle.** It survives if the datum is
   low-dimensional, prior, independently constrained, and leaves invariant predictions.
3. **A reduced non-unitary subsystem can belong to a healthy total keep-and-grade system.** W183's
   structural possibility survives, but only after the actual total `C`-operator is built.
4. **GU may be valuable as an admissibility/compression framework even without deriving every
   constant.** This is the modest Story 3. Its value is measured by prediction codimension after the
   declared boundary datum is fixed.

### Present status of the joint story

**Not false, not established, and not yet explanatory.** Its plausible version is now precise enough
to fail. That is progress. The story earns explanatory force only by removing choices, not by naming
where choices live.

## 8. Cheapest decisive next calculation

Do not build the full 14-dimensional interacting theory. Compute one projected quadratic block at a
fixed section `sigma:X4->Y14`, with all construction forks visible:

```text
                 [ H_shadow(k)       V_J(k)          ]
H_total(k)  =    [ V_J^sharp(k)      H_reservoir(k)  ],

K_total     = diag(K_(6,4), K_reservoir).
```

Derive the block from the actual linear `I1B` action plus W180's native current
`J=delta S_D/delta A`; do not insert a generic cubic vertex unless the projection produces it. The
same low-rank Schur-complement calculation should output three target-free invariants:

1. **Shadow bit:** the unique spin-0/trace coefficient and its Krein type, deciding whether the
   vertical Hessian is the Ricci-class shiab shadow, the geometric `|II|^2` shadow, or neither.
2. **Boundary bit:** the relative Krein sign and on-shell spectral-density sign of `V_J`, deciding
   whether the actual source couples the ghost to the like-signed record reservoir or the
   opposite-signed graviton continuum, and whether the selected total spectrum is real.
3. **Compression bit:** the exact rank of the source/boundary Jacobian into a predeclared small set of
   observables, deciding whether a prediction codimension survives.

This is the cheapest joint calculation because it attacks all three countermodels at their shared
hinge: the actual reduction/source map. It avoids a full `Y14` build, reuses W176's vertical-Hessian
strategy and W180's exact EL current, and directly computes the missing sign, selector, and rank rather
than narrating them.

## 9. Honest limits

- These countermodels refute unrestricted inference forms, not GU itself.
- Countermodel A does not choose between the shiab and `|II|^2` constructions.
- Countermodel B does not derive W180's dressed reservoir kernel. It proves why that kernel is
  decisive.
- Countermodel C does not say every boundary theory is empty. Its rank-1 positive control shows the
  opposite: a boundary datum can coexist with predictions.
- No generation-count result is claimed. Any future count claim must remain in the native `Z/3`
  torsion arena unless it is explicitly labeled a selected datum.
- No total C-operator is constructed; no physical-sheet verdict moves; H59 remains whatever its
  governing status surface says. This exploration moves no status.
- No test or build was run in this worker, per the serialized low-memory instruction.

*Filed 2026-07-14 as a conditional exploration. Two new artifacts only: this note and
`tests/W189_countermodel_discriminators.py`. No index, canon, claim-status, or external action.*
