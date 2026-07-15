---
artifact_type: exploration
label: W243
created: 2026-07-15
status: exploration
posture: adversarial; truth-seeking; native-object first; construction-fork explicit; coherence-first then kill; no verdict movement; does NOT decide the W235 record bit
title: "W243 charged-corridor closure: the one escape W240 left open (a Z2-even but Z-CHARGED, non-adjoint higher-rank VEV) is CLOSED for the EXTREMAL-weight case. THEOREM: in a non-compact real reductive group with a semisimple boost grading Z in p, a Z-charged EXTREMAL-weight vector is annihilated by a raising/lowering NILRADICAL of the Z-parabolic q(Z) = z_g(Z) + (nilradical), so that nonzero nilpotent subalgebra lies in its stabilizer; a subalgebra containing a nonzero nilpotent cannot be compact; hence the stabilizer ALWAYS retains a non-compact parabolic. Rank-independent (verified so(3,3), so(4,4), so(5,5) with a matched anticommuting boost; the argument is generic). RECONCILIATION with the SO(2,1) counterexample: the timelike escape vector is charged-but-NON-extremal (not a Z-eigenvector; it straddles the +/-1 Z-weight spaces), an interior/closed-orbit vector whose compact stabilizer is a different orbit type; the escape strictly requires non-extremality and does NOT generalize to extremal weights. In the fundamental of so(n,n) EVERY charged Z-eigenvector is null/extremal with a parabolic stabilizer. CONSEQUENCE: channel S (additive Z-charge -4, all-mirror = MINIMAL charge) is extremal, so even if it had an order parameter its stabilizer would be non-compact by the theorem (a second, isotropy-level reason independent of W240's emptiness). EXPORT STATUS: the no-go is UNCONDITIONAL for the Z-charged EXTREMAL-weight class -- hence for every definite-charge / definite-chirality order parameter GU builds (condensates are extremal tensor components); combined with W240 (A)/(B)/(C) the chirality-safe good-stable is blocked for everything GU builds. It remains SCOPED only against exotic NON-extremal charged vectors (interior Z-eigenvectors or non-eigenvector timelike vectors), which are not GU-native condensate order parameters."
grade: "EXACT for: the ad(Z) 3-grading g = g_- + g_0 + g_+ of the faithful so(n,n) model (eigenvalues {-2,0,+2}, max|imag|=1.1e-16, max|real|=2.00); every nonzero element of the nilradicals g_+ / g_- being matrix-nilpotent hence ad-nilpotent; the raising (resp. lowering) nilradical annihilating the top (resp. bottom) Z-charge vector; the extremal charged Z-eigenvector of the fundamental being NULL with a non-compact stabilizer (dim 21 in so(4,4)); the SO(2,1) timelike vector having a compact stabilizer SO(2) yet not being a Z-eigenvector; and the channel-S additive charge = -4 = 4*(-1) being the minimal (extremal) achievable additive charge. STRUCTURAL / rank-independent for the theorem 'an extremal-weight Z-charged vector retains the boost-parabolic nilradical (nonzero nilpotents) in its stabilizer, hence a non-compact parabolic' -- proved by the highest/lowest-Z-weight annihilation argument (nothing beyond the extremal charge) plus 'a real subalgebra containing a nonzero nilpotent is non-compact', both verified in so(3,3)/so(4,4)/so(5,5) with a matched anticommuting boost (same finite-model status as W216/W224/W234/W237/W240), plus the exact 8256/4160/4096 arena arithmetic. STRUCTURAL for the reconciliation (the SO(2,1) escape requires non-extremality and does not lift to extremal weights). CONDITIONAL on the W235 record bit for channel D availability (the whole comparison lives on the favorable, record-conserved branch). HONEST-OPEN residual: NON-extremal charged VEVs (interior Z-eigenvectors, or non-eigenvector timelike vectors) -- the SO(2,1)-type orbit -- are NOT closed by this theorem; they are shown to be the only surviving mathematical escape, and they are not GU-native condensate order parameters (which are extremal tensor components). OPEN for the interacting source action, the physical state space, and the observable algebra. Machine regression: tests/W243_charged_corridor_closure.py (26/26, exit 0, positive controls first). No canon, RESEARCH-STATUS, verdict, bar(b), H59, or generation-count change; the W235 record bit is FLAGGED not decided."
depends_on:
  - explorations/W240-z2even-compact-image-nogo-2026-07-15.md
  - explorations/W241-dynamical-vacuum-coincidence-escape-2026-07-15.md
  - explorations/W237-channel-s-condensate-isotropy-2026-07-15.md
  - explorations/W235-central-bit-mirror-record-vs-redundancy-2026-07-15.md
  - explorations/W234-condensate-vev-isotropy-gate-2026-07-15.md
  - explorations/W224-native-good-stable-dynamical-vacuum-2026-07-15.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W243_charged_corridor_closure.py
---

# W243 charged-corridor closure

## Result in one paragraph

**THE VERDICT: the charged corridor is CLOSED for the EXTREMAL-weight case; the scoped no-go
UPGRADES to UNCONDITIONAL for everything GU actually builds.** W240 hardened the chirality-safe
compactification no-go to three rank-independent classes (Z-neutral, adjoint, maximal-compact
target) and left exactly ONE escape open: a Z2-even but `Z`-CHARGED (additive boost-charge
`!= 0`), non-adjoint, higher-rank VEV, non-empty in abstract Lie theory because an `SO(2,1)`
timelike vector has a compact stabilizer `SO(2)` yet is boost-charged. W243 closes that corridor
for the case that matters. **THEOREM (rank-independent, GU-independent):** grade the algebra by the
boost `Z in p`, `g = g_- + g_0 + g_+` (a `|1|`-grading; in the faithful `so(n,n)` model `ad(Z)` has
eigenvalues `{-2,0,+2}`). The pieces `g_+`, `g_-` are the raising / lowering NILRADICALS of the
`Z`-parabolic `q(Z) = z_g(Z) + g_+`; every nonzero element of them is NILPOTENT. Let `w` be a
`Z`-EIGENVECTOR at the EXTREMAL (maximal or minimal) additive `Z`-charge in its representation.
Raising past the maximum (or lowering past the minimum) lands in a zero weight space, so the
corresponding nilradical ANNIHILATES `w`; hence that nilradical lies in `stab(w)`. It is nonzero
(`Z` is a non-central boost) and nilpotent, and **a real subalgebra containing a nonzero nilpotent
cannot be compact** (a compact real Lie algebra has no nonzero nilpotents -- all elements are
elliptic). Therefore `stab(w)` ALWAYS retains a non-compact parabolic. **RECONCILIATION with
`SO(2,1)`:** the timelike escape vector `t = e_3` is charged-but-NOT-a-`Z`-eigenvector (`Z t = e_1`
straddles the `+/-1` weight spaces); it is an interior / closed-orbit vector whose compact
stabilizer is a different orbit type. The escape strictly requires NON-extremality and does NOT lift
to extremal weights -- in the fundamental of `so(n,n)` every charged `Z`-eigenvector is null /
extremal with a parabolic stabilizer. **CONSEQUENCE:** channel S (`(16bar)^4`, additive `Z`-charge
`-4`, all-mirror = the MINIMAL achievable charge) is EXTREMAL, so even if it had an order parameter
its stabilizer would be non-compact by the theorem -- a SECOND, isotropy-level reason on top of
W240's emptiness. **EXPORT STATUS:** the no-go is UNCONDITIONAL for the `Z`-charged EXTREMAL-weight
class, hence for every definite-charge / definite-chirality order parameter GU builds (condensates
are extremal tensor components). It remains SCOPED only against exotic NON-extremal charged vectors
(interior `Z`-eigenvectors or non-eigenvector timelike vectors), the sole surviving mathematical
escape, which are not GU-native condensate order parameters. `bar(b)`, `H59`, and the count remain
OPEN / unchanged; the W235 record bit is FLAGGED, not decided.

## 1. Construction fork (mandatory)

The load-bearing object is a `Z`-charged extremal-weight VEV read as a vector in a representation of
the internal arena `Sp(32,32;H)`, and its isotropy (stabilizer) subgroup. This is the program's
recurring Krein / native fork at the level of definite-charge order parameters.

- **Standard-physics reading.** Treat a charged order parameter as "some Higgs multiplet gets a
  VEV" and assume, from ordinary compact-group intuition, that a charged direction generically has a
  compact residual stabilizer (as a charged vector in a compact group would). Under this default one
  imports the very compactification the whole question is about, and one conflates a generic charged
  vector (which CAN have a compact stabilizer, e.g. the `SO(2,1)` timelike vector) with an
  EXTREMAL-weight charged vector (which cannot).
- **Program-native reading.** The arena is `Sp(32,32;H)`, the non-compact real form whose
  non-compactness IS the Krein / indefinite form (GEOMETER-VS-PHYSICS-OBJECTS, gauge-group row). The
  grading `Z = tau3(null) = sigma1(definite)` is a genuine non-compact boost (`Z in p`, `ad(Z)` real
  nonzero, W240). A definite-charge condensate order parameter is an EXTREMAL component of a tensor
  power of the matter reps (top / bottom weight of the product), NOT a generic interior vector. In
  the non-compact real form, an extremal-weight vector sits on the null cone / closed-orbit boundary,
  and the correct object controlling its stabilizer is the `Z`-parabolic and its nilradical, not a
  compact residual.

**Which side, and why.** The answer lives on the native side and it is decisive in a way the physics
reading misses in BOTH directions. The physics reading would over-claim the corridor OPEN (charged
`=>` maybe compact, as in a compact group). The native reading exposes the exact distinction W240's
`SO(2,1)` example only hinted at: a charged vector has a compact stabilizer only if it is
NON-extremal (interior / non-eigenvector), while a definite-charge condensate is EXTREMAL and thus
pinned by the boost-parabolic nilradical to a non-compact stabilizer. Per the fork discipline the
result is checked in the OTHER construction: in the standard compact-group picture the theorem is
vacuous (no boost, no `p`), so the phenomenon is intrinsically a non-compact-real-form fact -- which
is exactly the Krein-native regime GU lives in. This is a GU-INDEPENDENT real-form Lie-theory
theorem that GU's native charged objects (extremal condensates) inescapably obey.

## 2. The Z-parabolic and its nilradical (verify, do not assert)

`Z in p` is a non-zero semisimple boost, so `ad(Z)` is diagonalizable with REAL eigenvalues and
grades the algebra:

```
g = g_-  (+)  g_0  (+)  g_+ ,     g_j = { X : [Z, X] = j X } .
```

In the faithful `so(4,4)` model with `Z = [[0, I_4],[I_4, 0]]` the eigenvalues are exactly
`{-2, 0, +2}` (`max|imag| = 1.1e-16`, `max|real| = 2.00`) -- a `|1|`-grading after rescaling. The
Levi is `g_0 = z_g(Z)` (the centralizer of `Z`) and the parabolic is `q(Z) = g_0 + g_+`, with
nilradical `g_+` (and opposite nilradical `g_-`). Machine facts (checks B1-B4):

```
ad(Z) eigenvalues on so(4,4) : {-2, 0, +2}         -> |1|-grading, Z-parabolic q(Z) = g_0 + g_+
g_+  (dim 6) : every nonzero element MATRIX-NILPOTENT  -> ad-nilpotent (ad X = L_X - R_X, commuting nilpotents)
g_-  (dim 6) : every nonzero element MATRIX-NILPOTENT
```

A nonzero matrix-nilpotent element is ad-nilpotent, and a compact real Lie algebra contains NO
nonzero nilpotents (every element is elliptic, `ad` with purely imaginary spectrum). So any
subalgebra containing a nonzero element of `g_+` or `g_-` is NON-compact. This is the certificate
used throughout.

## 3. The closure theorem (extremal-weight charged VEVs)

**Theorem.** Let `G` be a non-compact real reductive group, `Z in p` a non-zero semisimple (boost)
element, and `w` a vector in a finite-dimensional representation `V` with `dR(Z) w = lambda w` where
`lambda` is the EXTREMAL (maximal or minimal) `Z`-charge occurring in `V`. Then the nilradical
`g_+` (if `lambda` maximal) or `g_-` (if `lambda` minimal) annihilates `w`, so it lies in `stab(w)`;
that nilradical is nonzero and nilpotent, hence `stab(w)` is NON-compact and contains a non-compact
parabolic.

**Proof.** `g_+` raises the `Z`-charge (maps `V_mu` into `V_{mu + (positive)}`). If `lambda` is the
maximal charge, `dR(g_+) w` lies in a charge-`> lambda` space, which is `0`; hence `dR(g_+) w = 0`
and `g_+` is in the isotropy algebra of `w`. `g_+ != 0` because `Z` is a non-central boost (its
centralizer `g_0` is proper). A nonzero element of `g_+` is nilpotent (Section 2), and a real Lie
algebra containing a nonzero nilpotent is non-compact. Symmetrically for minimal `lambda` with
`g_-`. QED.

**Machine verification (checks C1-C5, D1).** In `so(4,4)` the top-`Z`-charge vector `v_+ = e_1 + e_5`
is annihilated by all of `g_+`, is NULL (`v_+^T beta v_+ = 0`), and its stabilizer (dim 21) contains
a nonzero nilpotent -> non-compact. The bottom-charge vector `v_- = e_1 - e_5` gives the same via
`g_-` (this is the channel-S side, additive charge `-4 <-> -1` after rescaling). Rank independence:
`so(3,3)`, `so(4,4)`, `so(5,5)` each show the top-grade nilradical annihilating the extremal charged
vector and a non-compact stabilizer. The argument uses only the `Z`-grading and nilpotency, so it is
generic in the rank -- it transfers to `Sp(32,32;H)` (real rank 32, restricted-root system of
`C`/`BC` type), where `Z` is the boost of W240 and the extremal condensate charges (all-generation
or all-mirror monomials) sit at the ends of the `Z`-weight chain.

## 4. Reconciliation with the SO(2,1) counterexample

W240's escape witness was the `SO(2,1)` timelike vector `t = e_3`: stabilizer `SO(2)` (compact,
dim 1) yet boost-charged. Why does this NOT contradict the theorem, and why does it not generalize?

- `t` is charged-but-NOT-a-`Z`-eigenvector. Under the boost `Z_{13}`, `Z t = e_1`, which is not a
  multiple of `t`; `t` straddles the `+1` and `-1` `Z`-weight spaces (`t = (u_+ - u_-)/...` in the
  null basis `u_{+/-} = e_1 +/- e_3`). It is an INTERIOR / non-extremal vector (check PC2b, E1).
- Its compact stabilizer is the reductive stabilizer of a CLOSED (Riemannian, mass-hyperboloid)
  orbit `SO(2,1)/SO(2) = H^2`. That is a different orbit type from the extremal / null-cone orbit,
  whose stabilizer is a parabolic.
- The theorem applies to EXTREMAL `Z`-EIGENVECTORS. In the `SO(2,1)` vector rep the only charged
  `Z`-eigenvectors are the NULL vectors `u_{+/-}` (extremal), whose stabilizers ARE non-compact
  parabolics; the timelike `t` that has the compact stabilizer is simply not one of them.

So the `SO(2,1)` escape is real but STRICTLY confined to non-extremal charged vectors. In the
fundamental of `so(n,n)` every charged `Z`-eigenvector is null / extremal with a parabolic
stabilizer (check C2, E2), so there is no extremal charged vector that inherits the `SO(2,1)`
escape (check E3). The low-rank compact-stabilizer case does not generalize to `Sp(32,32;H)` with
the boost `Z` because the objects GU builds are extremal (Section 5), and the escape needs
non-extremality, which extremality precludes.

## 5. Does any native GU object realize the surviving (non-extremal) escape?

The only surviving mathematical escape is a NON-extremal charged VEV -- either an interior
`Z`-eigenvector (a definite but non-extremal charge, requiring a `Z`-weight chain long enough to
have an interior charged level) or a non-eigenvector "timelike" combination (the `SO(2,1)` type).
Both are NOT how a definite-charge / definite-chirality condensate order parameter is built:

- A GU condensate order parameter is a fermion-bilinear or higher tensor with DEFINITE charge and
  chirality; as the primary breaking channel it is an EXTREMAL component of the tensor product (top
  or bottom weight), not an interior superposition across `Z`-weight spaces. This is precisely the
  regime the theorem closes.
- Channel S, the corridor's only GU-native tenant (W231/W237), is the mirror-only `(16bar)^4` with
  additive `Z`-charge `4 * (-1) = -4`. All-mirror is the MOST NEGATIVE achievable additive charge,
  so channel S is at the MINIMAL `Z`-weight -- EXTREMAL (check F1, F2). By the theorem its stabilizer
  would contain the lowering nilradical `g_-` and be non-compact EVEN IF it had a nonzero order
  parameter. This is a second, isotropy-level closure on top of W240's independent finding that
  channel S has zero order parameter at all (channel B empty) -- the corridor's one native object is
  now closed twice over, by disjoint arguments (check F3).

A non-extremal charged VEV with a compact stabilizer (the pure `SO(2,1)` analog) would be the exact
object H59 needs. It is not exhibited by any GU-native construction here: GU's charged order
parameters are extremal. So the escape, where it survives mathematically, is GU-non-native.

## 6. Verdict

```
Z-CHARGED corridor in Sp(32,32;H) -- the escape W240 left open:

  Z-parabolic:  ad(Z) grades g = g_- + g_0 + g_+;  g_+/g_- are NILPOTENT nilradicals (boost, Z in p).

  EXTREMAL-weight Z-charged VEV w (max or min Z-charge):
      raising/lowering past the extreme -> 0, so the nilradical annihilates w
      => nilradical in stab(w) => stab(w) contains a nonzero NILPOTENT => NON-compact parabolic.
      -> CLOSED. Rank-independent (so(3,3), so(4,4), so(5,5); generic argument).

  RECONCILE SO(2,1): the timelike escape vector is charged-but-NON-extremal (not a Z-eigenvector);
      compact stabilizer = a different (closed Riemannian) orbit type. The escape needs
      non-extremality and does NOT lift to extremal weights.

  CHANNEL S (additive Z-charge -4, all-mirror = MINIMAL): EXTREMAL => non-compact stabilizer by the
      theorem even if nonempty. Closed twice (isotropy-level here + emptiness in W240).

  => The no-go is UNCONDITIONAL for the Z-charged EXTREMAL-weight class -- every definite-charge /
     definite-chirality order parameter GU builds. With W240 (A)/(B)/(C): chirality-safe dynamical
     compactification is blocked for EVERYTHING GU builds in Sp(32,32;H).

  SCOPED residual (honestly OPEN, GU-non-native): NON-extremal charged VEVs (interior Z-eigenvectors
     or non-eigenvector timelike vectors) -- the SO(2,1)-type orbit. Not a GU condensate order
     parameter. If one existed and were native, it is exactly the object H59 needs.

CONDITIONAL on the W235 record bit (NOT decided): on the record-CONSERVED branch (chirality
protected), no native VEV -- neutral, adjoint, or charged-extremal -- compactifies while preserving
chirality. W224's singlet input-failure STANDS, now hardened across the last open class.
```

## 7. Neutral-export status (UNCONDITIONAL vs SCOPED)

Stated as a repo-independent (neutral) result:

- **UNCONDITIONAL, GU-independent.** "In a non-compact real reductive group `G` with a semisimple
  boost grading `Z in p`, the stabilizer of any EXTREMAL-weight `Z`-charged vector contains the
  nilradical of the `Z`-parabolic and is therefore non-compact." This is a clean real-form Lie-theory
  theorem (Section 3), proved rank-independently. Combined with the W240 no-go classes, the neutral
  statement "a Krein good-stable with an anticommuting grading boost admits no chirality-safe
  maximal-compact reduction for any neutral, adjoint, or charged-EXTREMAL order parameter" is
  UNCONDITIONAL.
- **SCOPED (still).** The fully unconditional Lie-theory claim "NO `Z`-charged VEV of any kind
  compactifies" is FALSE (the `SO(2,1)` non-extremal timelike vector is a genuine charged compact-
  stabilizer counterexample). The residual escape is exactly the NON-extremal charged class, which
  this theorem does not close and which GU does not build. So the neutral export is UNCONDITIONAL for
  the EXTREMAL-weight class and SCOPED (open, but GU-non-native) for the non-extremal class.

For GU specifically: since every definite-charge order parameter GU builds is extremal, the no-go is
UNCONDITIONAL for everything GU builds; the remaining escape is a mathematical object GU does not
realize.

## 8. Joe-gated items borne on but NOT moved

- **The W235 record / redundancy bit**: this result is stated CONDITIONAL on it and does NOT decide
  it. FLAGGED, not moved. W243 shows the located flaw survives on the FAVORABLE (record-conserved)
  reading now for the last open (charged-extremal) class as well.
- **H59 / bar(b)**: unchanged. This SHARPENS what H59 must build. After W240 the target was "a
  Z2-even, `Z`-charged, non-adjoint, higher-rank order parameter with a compact-image stabilizer";
  W243 shows that if such an object is EXTREMAL (as every definite-charge condensate is) it is
  impossible, so H59 would need a NON-extremal charged VEV with a compact stabilizer -- an object GU
  does not currently build. No debit added or cleared; a located input-failure hardened across the
  last open class is a sharpened gap, not a new falsification. FLAGGED, not moved. This bears on
  `bar(b)`; it is CHARACTERIZATION only, verdict-relevant, Joe-gated.
- **Generation count / RESEARCH-STATUS / verdicts / canon**: untouched. No verdict flip.

## 9. Follow-up this unlocks

1. **The interior-charged residual.** The one class not touched is an INTERIOR `Z`-eigenvector (a
   definite but non-extremal charge). Determine whether an interior charged eigenvector in
   `Sp(32,32;H)` can ever have a compact-image stabilizer, or whether a refinement (e.g. the
   restricted-root string through an interior weight always contains a non-compact root vector in the
   isotropy) closes it too. If it also closes, the neutral export becomes unconditional for ALL
   `Z`-eigenvectors, leaving only the non-eigenvector timelike class.
2. **The W241 front door.** The DYNAMICAL vacuum isotropy reducing to a smaller, coincidence-
   admitting group in which the grading is no longer a boost (orthogonal to this corridor closure).
3. **Lean port (follow-up ONLY, no Lean/Lake run here per the machine-wide serialized-build rule).**
   The theorem is finite and exact: the `ad(Z)` grading, the nilpotency of `g_+`/`g_-`, the
   extremal-annihilation, and "a subalgebra with a nonzero nilpotent is non-compact" are all
   Lean-portable. A sibling worker may be concurrent; do not overlap Lean runs.

## 10. Machine receipt

```
python -u tests/W243_charged_corridor_closure.py
```

26/26 checks passed, exit 0. Positive controls run FIRST and each fires on a real falsifier: the
non-compactness detector FIRES (non-compact) on a genuine null-rotation nilpotent (built from the
`g_+` nilradical of a boost-graded `so(2,2)`) and stays SILENT (compact) on `so(2)`, so a non-compact
parabolic cannot be misclassified compact nor a compact algebra as non-compact; and the `SO(2,1)`
timelike vector reproduces the charged-but-COMPACT-stabilizer fact while being shown NOT to be a
`Z`-eigenvector (non-extremal), so the escape is real but only for non-extremal vectors. The actual
checks then verify the `ad(Z)` 3-grading and nilpotency of both nilradicals, the extremal-weight
closure (raising/lowering nilradical annihilates the extreme-charge vector -> non-compact
stabilizer), rank-independence (`so(3,3)/so(4,4)/so(5,5)`), the `SO(2,1)` reconciliation, and that
channel S sits at the extremal (minimal) charge so it is closed twice over.

## Governance

Exploration grade only. No canon, RESEARCH-STATUS, verdict, `bar(b)`, `H59`, or generation-count
change. The W235 record bit is flagged and coupled, not decided. No cross-repository identity
asserted; the reservoir Krein sign and the Y14 spectral-section / record datum stay gated
temporal-issuance / time-as-finality objects. `bar(b)` and `H59` remain OPEN. This is
characterization, verdict-relevant and Joe-gated; no verdict is moved. Zero em dashes.
