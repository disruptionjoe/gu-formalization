---
artifact_type: exploration
status: exploration
created: 2026-07-04
title: "GU non-compact -> compact reduction audit: is 'take the maximal compact subgroup of Spin(6,4)/SU(3,2)' FORCED by GU-native structure, or is it an EXTERNAL firewall move imposed to match observed compact, unitary gauge theory? HONEST OUTCOME: REDUCTION_EXTERNAL. GU's own machinery produces the OPPOSITE of what the maximal-compact restriction needs -- an INDEFINITE (Krein) invariant fermion form, machine-checked pseudo-anti-Hermitian (residual 0e+00) with generation-triplet signature EXACTLY (+96,-96,0) and full-RS (+896,-896). By the Weyl unitarian trick a positive-definite invariant form exists IFF the acting group is compact; GU's internal group is non-compact (q=4), so no GU-native positive form can exist. The positivity that selects the maximal compact K is therefore imposed from outside -- logically identical to re-imposing the Distler-Garibaldi DG-A3 'compact internal G' assumption GU deliberately dropped. Verdict reached WITHOUT importing compactness/unitarity/observed-SM: it follows from (a) GU's machine-checked indefinite form and (b) a general representation-theory theorem. Signature-INDEPENDENT: firewall persists in (9,5), (7,7), and (14,0)."
grade: "exploration / strong. The load-bearing fact is a genuine theorem (non-compact semisimple => no invariant positive-definite Hermitian form on any nontrivial finite-dim module, Weyl unitarian trick) corroborated by two independent machine computations, not a coincidence of a chosen form. The one open residual -- whether an UNBUILT GU source action could dynamically realize a ghost-parity superselection that carves a positive-norm sector -- is honestly external/unbuilt and dynamics-contingent, so it does not upgrade the verdict to FORCED. Nothing here derives 3; this audits GU AS A PHYSICS PROPOSAL and does NOT grade the generation count."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - canon/six-axis-candidate-krein-positivity-dg.md
  - canon/firewall-boundary-hypothesis.md
scripts:
  - tests/generation-sector/ghost_parity_krein.py
  - scratchpad/inv_check_v2.py
---

# GU non-compact -> compact reduction: forced by GU-native structure, or an external firewall?

**The swing.** GU's internal/vertical sector is the *indefinite, non-compact* `Spin(6,4)` (equivalently
`SU(3,2)`): the 10D vertical fiber of `Y14` carries signature `(6,4)` after trace-reversing the
Frobenius/DeWitt metric on the space of metrics, and Weinstein explicitly rejects the compact `Spin(10)` GUT
("this spin 10 is not right"). The Standard Model is then recovered as the **maximal compact subgroup**:
`Spin(6,4) -> Spin(6)xSpin(4) = Pati-Salam -> SM`, or in the SU picture
`SU(3,2) -> S(U(3)xU(2)) = SU(3)xSU(2)xU(1) = SM`. The maximal-compact isomorphisms are definition-level real
form group theory. **The audit question is the physics one:** is "take the maximal compact" *forced* by
GU-native structure, or is it an *external* choice imposed to match observed compact, unitary gauge theory --
a boundary/firewall move? A FORCED verdict must exhibit a GU-native positive-definite invariant inner product
on the fermion module; an EXTERNAL verdict shows that positive form must be imported.

**Honest outcome: REDUCTION_EXTERNAL (the firewall holds).** GU's own construction supplies the *opposite* of
the positive form the maximal compact preserves. FORCED is actively ruled out, not merely unproven.

---

## What the maximal-compact restriction actually turns on

Identifying `K` imports nothing: the conjugacy class of a maximal compact subgroup is a canonical invariant
of the real form, so naming `Spin(6)xSpin(4)` / `S(U(3)xU(2))` is free. The load-bearing question is **why
physical states restrict to representations of `K` rather than of the full non-compact `G`.** In physics that
restriction is forced by exactly one thing: a **positive-definite invariant (Hermitian) inner product on the
fermion module**. By the Weyl unitarian trick run in reverse, a finite-dimensional module carries an invariant
positive-definite form **iff the acting group is compact**, and the maximal such acting group is `K`. So:

> "Take the maximal compact" is FORCED **iff** GU natively supplies that positive-definite fermion form, and
> EXTERNAL **iff** the positive form must be imposed from outside -- which is logically identical to
> re-imposing Distler-Garibaldi assumption **DG-A3 ("compact internal G")** that GU dropped.

This framing does not import the answer: unitarity/positivity is used only as the *sole lever that could
force* the reduction, and we then ask whether GU's own geometry pulls that lever.

---

## Certificate A -- repo canon: GU's native invariant form is Krein, not Hilbert (`ghost_parity_krein.py`)

GU's native `so(p,q)`-invariant form on the matter module is `K = eta_V (x) beta_S`, with
`beta_S =` product of spacelike gammas. The repo's `tests/generation-sector/ghost_parity_krein.py` (RUN this
session, exit 0) shows it is **pseudo-anti-Hermitian** (`beta_S sigma + sigma^dagger beta_S = 0`, residual
`0e+00`) and hence indefinite/Krein:

> `(9,5)`, `(7,7)`, `(14,0)`: beta pseudo-anti-Herm residual `0e+00` | triplet Krein signature **`(+96, -96, 0)`** -> NEUTRAL/hyperbolic.

The 192-dim generation triplet is *maximally neutral*, and the full 1792-dim Rarita-Schwinger module is
`(+896, -896)`. GU's machinery produces a **Krein space, not a Hilbert space**: the positive-definite
invariant fermion form is provably absent.

---

## Certificate B -- independent reproduction: positive-definite IFF compact (`scratchpad/inv_check_v2.py`)

Built from scratch this session (numpy, no repo imports): construct `Cl(p,q)` gammas by Jordan-Wigner,
form the spin generators `sigma_{ab} = 1/4 [gamma_a, gamma_b]`, and construct the canonical invariant
Hermitian form `B` (product of the timelike gammas) that makes every `sigma_{ab}` `B`-anti-Hermitian. Then
read its signature. Machine result (anti-Hermiticity residual `0.0e+00` in both load-bearing cases):

| real form | compact? | invariant Hermitian form signature `(pos, neg, zero)` |
|---|---|---|
| `so(10,0)` | yes (control) | **`(1024, 0, 0)` -- POSITIVE-DEFINITE** |
| `so(6,4)` (GU's fiber) | **no** (`q=4`) | **`(512, 512, 0)` -- exactly neutral / INDEFINITE** |

This is the Weyl unitarian trick *by machine*: the invariant Hermitian form is positive-definite **only** when
`q = 0`, and GU's internal group has `q = 4`. The indefiniteness is not an artifact of the chosen `B` --
Schur's lemma makes the invariant sesquilinear form unique up to scale on an irreducible factor, so
indefiniteness is forced by non-compactness regardless of convention. (Certificate A independently covers the
`(9,5)/(7,7)/(14,0)` cases with the physical `eta_V (x) beta_S` form.)

**Conclusion of A+B:** no GU-native positive-definite fermion form exists. The positive form that selects `K`
must be imposed from outside -- a scope-exit, not a derivation.

---

## The four GU-native forcing candidates, and why each fails

1. **Positive-definite invariant fermion form from GU's construction** -- DISPROVEN. Native form is
   machine-checked Krein `(+896,-896)` / `(+96,-96,0)`; GU produces the opposite of a positive form.
2. **"Unitary chimeric spin bundle" (Weinstein)** -- DISPROVEN as a positive candidate. Spinors on an
   indefinite `(6,4)` vertical metric carry a pseudo-Hermitian pairing, so "the unitary group of those
   spinors" is really pseudo-unitary `U(p,q)`, itself non-compact; supplies no positive form.
3. **Pulled-back Weyl content / reality structure** -- does not force positivity. It governs the parity/index
   leg (`Cl(9,5)=M(64,H)` Kramers wall vs `Cl(7,7)=M(128,R)` no wall), a separate axis from compactness.
4. **Turok-Bateman ghost-parity `Z_2`** -- a `+`-norm sector (min `K`-eig `+1.000`) does exist and a
   Krein-unitary toy dynamics is consistent (`S^dagger K S = K`, residual `2.7e-14`), BUT the split is
   basis/convention-dependent (spacelike vs timelike gamma adjoint), non-canonical, and is a symmetry only if
   the **unbuilt** source-action dynamics satisfies `[P_ghost, S] = 0`. A `G`-equivariant ghost parity
   coincides with the reality structure and *re-symmetrizes rather than selects*. External/unbuilt; does not
   force the reduction.

The repo's own A0-audit canon (`six-axis-candidate-krein-positivity-dg.md`,
`ghost-parity-krein-synthesis.md`) reaches the identical conclusion: dropping Hilbert positivity to keep the
indefinite Krein form is "logically equivalent to negating Distler-Garibaldi assumption DG-A3 (compact
internal G): a SCOPE-EXIT." This audit matches the repo's canonical grade.

---

## Signature-dependence: does (9,5) vs (7,7) change the landing?

**No -- the firewall is signature-independent.** The gauge/SM content lives entirely in the **vertical (6,4)
block**, fixed by the trace-reversed Frobenius metric on the 10D fiber alone. `(7,7)=(6+1,4+3)` and
`(9,5)=(6+3,4+1)` differ only in whether the horizontal Lorentz block is counted `(1,3)` or `(3,1)` -- a sign
convention on the *horizontal*, not on the internal fiber -- so both route through the **same** internal
`Spin(6,4) -> Spin(6)xSpin(4) = Pati-Salam -> SM`. The Krein neutrality is machine-robust: triplet signature
is exactly `(+96,-96,0)` and net chiral asymmetry `0` in `(9,5)`, `(7,7)`, **and** Euclidean `(14,0)`.

What signature *does* change is only the **spinor module reality type** (the quaternionic Kramers/parity wall
is a `(9,5)` artifact, `M(64,H)`, that dissolves under `(7,7)`, `M(128,R)`) -- and that governs the
**parity/generation-count leg**, a different axis, NOT the compact reduction.

**Honest caveat.** At the *total-space* level the real form genuinely changes (max compact of
`Spin(7,7)=Spin(7)xSpin(7)`, of `Spin(9,5)=Spin(9)xSpin(5)`). But GU never reduces the whole `Spin(14)` -- it
reduces only the isolated vertical `Spin(6,4)` -- so the SM landing is protected by the vertical/horizontal
split, *contingent on that split being genuinely part of the construction* (transcript states it is).

---

## What this settles, and how it relates to the generation-count firewall

**Settles.** "Take the maximal compact subgroup" is **not** a theorem of GU-native structure. GU natively
delivers the indefinite Krein pairing that non-compactness predicts; the positive-definite metric that selects
`K` is imported from outside to match observed compact, unitary gauge theory -- a firewall/boundary move,
logically identical to re-imposing the DG-A3 compactness assumption GU deliberately dropped. Weinstein owns the
non-compactness in his own words ("we wasted the seventies avoiding indefinite signature on the Killing form";
"I don't know what to do because we're in a maximally compact subgroup"; "shielded experimentally from ... the
indeterminacy of the Killing form"). This is an explicit owner-concession that no GU-native mechanism forces
compactness, and the maximal compact is the observed *shadow*.

**Relation to the generation-count firewall.** This is a **distinct** firewall of the **same** "located but
not forced" character, and it sits strictly **upstream** of the count. The compactness reduction is the more
fundamental boundary -- a kinematic/representation-theoretic necessity: GU provably cannot supply the positive
form while the internal group is non-compact. The generation-count firewall (the mod-3 anomaly arena is empty;
the count is external) presupposes an already-compactified, unitary SM sector. Confirming the compactness
firewall *strengthens* the standing conclusion that the count is external: the very Hilbert-space positivity a
generation-selecting dynamics would require is itself imported here, before the count question is even posed.

**Does NOT settle (and no target imported).** This does not derive three and does not grade the count. The
number 3 was never assumed. No `8`, no `24`, no `chi(K3)`, no `Ahat`. The verdict follows only from GU's own
machine-checked indefinite form plus the general Weyl-unitarian-trick theorem.

---

## Next steps

1. **Build the missing GU source action** and test whether its dynamics realizes a `G`-equivariant
   ghost-parity superselection `[P_ghost, S] = 0` that carves a positive-norm physical sector -- the only
   (external, currently unbuilt) route by which compactness could ever become *dynamically* forced. Verify
   whether index conservation re-symmetrizes (kills selection) or genuinely selects.
2. **Formalize the no-go as a standalone theorem**: no positive-definite `Spin(6,4)`-invariant Hermitian form
   on any nontrivial finite-dim module, with the Schur uniqueness-up-to-scale step making it
   convention-independent (not tied to `eta_V (x) beta_S`).
3. **Promote the vertical/horizontal split** from a stated construction assumption to an explicit audited
   premise, since the signature-independence of the SM landing is contingent on GU reducing only the isolated
   vertical `Spin(6,4)` rather than the full `Spin(14)` whose real form IS signature-sensitive.
4. **Cross-link** this compactness firewall to the generation-count firewall in the firewall-boundary canon as
   an upstream/downstream pair.
5. **Complete the corroboration script**: extend `inv_check_v2.py` normalization to cleanly print
   `so(7,3)/so(9,5)/so(7,7)` (its Hermitian-phase fix currently completes only for `so(10,0)` and `so(6,4)`);
   `ghost_parity_krein.py` already covers the rest, so this is completeness only.

**Grade: REDUCTION_EXTERNAL.** The firewall is confirmed, signature-independent, and upstream of the
generation count. Exploration-grade; no canon edited, nothing committed.
---

## Verifier's note (main-loop review, 2026-07-04)

Synthesis of a 20-agent ultracode audit (`wf_db81a5ff-a76`, 0 errors). Main-loop honesty review:

- **Backbone is a rigorous standard theorem, not a soft claim.** The verdict rests on the **Weyl unitarian
  trick**: a non-compact semisimple Lie group admits **no** invariant positive-definite Hermitian form on any
  nontrivial finite-dimensional module (positive invariant forms exist iff the group is compact -- the same
  fact that gives non-compact groups no nontrivial finite-dim unitary reps). GU's internal group is
  **non-compact** (`Spin(6,4)`, `q=4` non-compact directions -- Weinstein's own construction), so no GU-native
  positive form can exist. That alone forces REDUCTION_EXTERNAL, reached WITHOUT importing compactness /
  unitarity / the observed SM. Sound.
- **The machine corroboration aligns with established repo canon.** The claimed indefinite Krein signature
  `(+96, -96, 0)` is the repo's *central, session-long, many-times-verified* cross-chirality object; the audit
  cites the persisted `tests/generation-sector/ghost_parity_krein.py`. I could not re-run it in-window (heavy
  Cl(9,5), timed out at 100s), but the `(+96, -96)` Krein form is not in doubt. The independent scratchpad
  positivity check (definite `(1024,0,0)` only for `so(10,0)`, indefinite `(512,512,0)` for `so(6,4)`) is
  scratchpad-only and corroborative, not load-bearing -- the theorem carries the verdict.
- **Honest caveat the audit flagged (kept):** signature-independence relies on GU reducing **only** the
  isolated vertical `Spin(6,4)`, not the full `Spin(14)` (whose real form *is* signature-sensitive:
  `max-compact Spin(9,5) = Spin(9)xSpin(5)` vs `Spin(7,7) = Spin(7)xSpin(7)`). The transcript supports the
  vertical/horizontal split; promoting it from stated-assumption to audited premise is a real next step.

**Bottom line (main-loop concurrence):** REDUCTION_EXTERNAL is right and rigorous, and it is the **strongest
confirmation of the firewall hypothesis yet**: the maximal-compact reduction is a genuine external boundary
crossing, signature-independent, and it sits strictly **upstream** of the generation-count firewall (positivity
of the physical Hilbert space is imported *before* one can even ask which mechanism pins the count). Two stacked
firewalls, same "located, not forced" phenomenon. Note the convergence with the running Mirror-Boundary audit:
the very `(+96, -96)` indefinite Krein form that makes the reduction external IS the cross-chirality structure
whose `-96` sector the mirror hypothesis is testing -- these are the same object. No target imported; count OPEN.
