---
artifact_type: exploration
label: "Wave A-1 (anchor council queue): Q2 + DQ2"
created: 2026-08-03
status: exploration
posture: adversarial; truth-seeking; preregistered both ways; no verdict movement
title: "Chirality grading of the imposter 128 under both real forms (Q2) and the (7,7) rerun of the trichotomy's two legs (DQ2)"
grade: "DETERMINISTIC FINITE NUMERICAL COMPUTATION plus analytic structural identities / pre-deposit / claim_status_change: none"
canon_verdict_change: none
hostile_review_status: "MUST-FIX findings absorbed; PH-K1 split into kinematic and physical gates"
verdict_gate: "Results here are PRE-DEPOSIT. No bar, verdict, canon claim, count, H59, or LANE-STATE entry moves on this artifact. Hostile review confirms only PH-K1-KINEMATIC; PH-K1-PHYSICAL remains OPEN/BLOCKED."
kill_conditions_declared_before_computation: true
depends_on:
  - lab/process/anchor-council-2026-08-03/seat3-particle-flavor.md
  - lab/process/anchor-council-2026-08-03/seat1-quantum-foundations.md
  - lab/process/anchor-council-2026-08-03/adjudication.md
  - lab/process/hinge-panel-synthesis-2026-08-03.md
  - explorations/observable-algebra-commutant-trichotomy-2026-08-03.md
  - lab/process/hostile-reviews/2026-08-03-trichotomy-review.md
  - tests/oq_rk1_cl95_explicit_rep.py
  - tests/generation-sector/gen_sector_bridge.py
  - tests/generation-sector/signature_77_rerun.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/generation-sector/q2_imposter_chirality_grading.py
  - tests/observable-algebra/dq2_trichotomy_77_rerun.py
---

# Chirality grading of the 128 (Q2) and the (7,7) trichotomy rerun (DQ2)

> **Hostile-review correction (2026-08-03; controls this artifact).** The
> computation establishes `PH-K1-KINEMATIC = CONFIRMED` for imposter Reading A.
> It does **not** establish a physical third generation, a Standard Model
> weak-current contradiction, or a gauge anomaly. `PH-K1-PHYSICAL` remains
> `OPEN/BLOCKED` on the unresolved imposter A/B referent and the unbuilt
> observation/VEV/BRST/reality/SM-gauge map. The `(7,7)` conclusions are for
> the chosen compression algebra and canonical `J`-fixed real form; they do
> not finish M-H4's actual stabilizer computation or select the GU signature.
> Numerical commutant and spectrum certificates are reported as numerical,
> while the displayed Clifford identities retain their analytic status.

Anchor-council Wave A-1 (adjudication §3). Both computations were preregistered
below BEFORE any script was written or run; the preregistration text was
committed to this file first and has not been edited after the runs (results
were appended below it).

## 0. Layer-0 typing (before use; per the standing rule)

| Term | Type | Ruling for THIS artifact |
|---|---|---|
| "128" | **HOMONYM (three-way, seat 3)** | Here "the 128" means sense (c): the imposter block `S(V_4) (x) S(W_10) ⊂ ker Γ` — the (10,−4) relative gamma-trace antidiagonal of the hinge panel. It is numerically equal to (a) `dim_R` of the Cl(7,7) Majorana module and to (b) `dim_C S` in one canon file; structurally unrelated to both. Nothing below trades on the equality. |
| "chirality" | **HOMONYM (four-way, ruling R5)** | The grading operator computed here is the AMBIENT 14D volume word `ω = e_0…e_13` restricted to `ker Γ` (the same `ω_V` as the trichotomy probe). It is NOT 4D Weyl chirality of a physical field, NOT the `Cl^0` complex-structure choice (audit B16), and NOT a base-Lorentz label. The bridge from ω-balance to "vectorlike" runs through the joint `(ω_4, ω_10)` grading of the source module `S`, computed separately, and through the kinematic-only identification `ψ ↦ x_ψ` below. |
| "(9,5)" | **HOMONYM (split vs signature; pack fix 68a3013)** | Everywhere below "(9,5)"/"(7,7)" is the AMBIENT SIGNATURE. The split used is 4+10, even/even, so the 2+1 product rule applies under either signature. Allocations of signs to the 4+10 split are swept explicitly (five per signature). |
| "imposter" | **HOMONYM (A vs B, unadjudicated)** | This artifact computes READING A only: the 128-dim `S(V)⊗S(W)` block (spin-1/2 shaped). Reading B (the RS spin-3/2 family, 384) is a different subspace; W221's SURVIVES depends on (B). Q1 (the adjudication row) is a separate Wave-A-3 item; nothing here adjudicates it. |
| "vectorlike" | **DEFINED HERE** | A block is called vectorlike when, under the equivariant identification with its source module, every complexified ten-factor chirality component appears with BOTH base-side chiralities in equal multiplicity. This is a KINEMATIC statement about the block's module structure; the ten-factor is physically allocated as `Spin(6,4)`, and the kinematic carrier is not the physical carrier (`Π_RS^phys` does not exist, OQ-RK1 BLOCKED_NEEDS_SPEC). |
| multiplicity vs count | **FENCE (Rung 1)** | Nothing below reads a decomposition as a generation count. 384/1152/128 are multiplicities; blocks ≠ generations (five buttresses). |
| "F" / fundamental symmetry | **HOMONYM (seat 1)** | `F` below is the admissible set of LINEAR commuting involutions with the positivity-majorant property against the constructed Krein form (the probe's `F_A(η_V)` sense). Antilinear involutions are counted separately and never silently merged into `F`. |
| "residual family" | **DEFINED HERE (two sectors)** | The linear residual family = commuting linear involutions beyond ±I. The antilinear candidate family = antilinear involutions `cJ` with `(cJ)^2 = +1`. Seat 1's preregistered outcome (i) is read against BOTH sectors, reported separately. |

Construction fork (GEOMETER-VS-PHYSICS-OBJECTS.md): everything below is the
program-native KINEMATIC construction — the verified explicit Clifford fixtures
(`tests/oq_rk1_cl95_explicit_rep.py` shape), the `ker Γ` projector reading of
the RS cure (:29), and the Krein (keep-and-grade) apparatus (:20, :21). No
physical/BRST quotient, no positive Hilbert space, no Porrati-Rahman vertex is
used. Kills below are kills IN THIS CONSTRUCTION; the carrier-split fork (:24,
three options) is not adjudicated here — the signature fork is swept instead.

## 1. PREREGISTRATION (written before computing)

### 1.1 Q2 — chirality grading of the imposter 128, both real forms

Object: ambient vector-spinor space `C^14 (x) C^128` with the explicit
Jordan-Wigner Clifford representation; `Γ = Σ_a e_a x_a : C^1792 → C^128`;
record sector `ker Γ`, `dim_C = 1664`. Split 14 = 4+10 (indices B, F); metric-dual
embeddings `ι_B(ψ)_a = η_aa e_a ψ` (a ∈ B), `ι_F` likewise, so `Γ∘ι_B = 4·I`,
`Γ∘ι_F = 10·I` (allocation-invariant); imposter block = image of `10·ι_B − 4·ι_F`
(the (10,−4) antidiagonal), `dim_C = 128`, inside `ker Γ`. Grading operator:
`ω_V` = restriction of `I_14 (x) ω`, `ω = e_0…e_13`. Both signatures (9,5) and
(7,7); all five sign allocations to the 4+10 split per signature.

**Predictions (registered):**

- P-Q2-1: the imposter block is `ω_V`-invariant with grading **64 + 64
  (balanced)** under BOTH real forms and ALL allocations.
- P-Q2-2: the full block structure grades as **192+192 / 576+576 / 64+64**
  (blocks 384 = `ker Γ_B`, 1152 = `ker Γ_F`, 128 = imposter), summing to the
  banked 832+832 on `ker Γ`.
- P-Q2-3: the joint `(ω_4, ω_10)` grading of the source module `S = C^128` is
  32/32/32/32, so each internal chirality half pairs with both base-side
  chiralities in equal multiplicity through the identification `ψ ↦ x_ψ`.

**Preregistered readout (both ways):**

- Balanced (64+64) ⇒ the imposter Reading-A block is **VECTORLIKE** at the
  kinematic level ⇒ **PH-K1-KINEMATIC CONFIRMS**. The physical consequence is
  conditional: if Reading A descends unchanged as an observed generation,
  with no chiral selection or mirror decoupling, it conflicts with measured
  V−A weak currents. This is not, by itself, a gauge-anomaly claim.
- Unbalanced ⇒ PH-K1-KINEMATIC is **CLEARED**: the block carries a nonzero
  kinematic ω-index and the vectorlike kinematic objection dies — which would
  ALSO contradict the seat-3 mechanism argument
  (`ω` anticommutes with every `e_a`), so an unbalanced result additionally
  flags an error in the mechanism derivation and must trigger a hand audit
  before being cited.

### 1.2 DQ2 — the (7,7) rerun of the trichotomy's two legs

Object: the same compression-algebra construction as the M-C3 probe
(`tests/observable-algebra/commutant_trichotomy_probe.py`) re-parameterised to
signature (7,7): 44 compressed generators on `V = ker Γ` (dim 1664), anchors
expected signature-identical (bare 58.72, C2 155.36). Under Cl(7,7) ≅ M(128,R)
the commuting antiunitary `J` has `J² = +1` (verified in-repo, firewall Round
2, `tests/generation-sector/signature_77_rerun.py`), so antilinear candidates
`cJ` have `(cJ)² = +|c|²` and are legitimate involutions for |c| = 1 — the "at
most one" conclusion is not automatic.

**Preregistered outcomes (seat 1 DQ2, verbatim both ways):**

- (i) larger candidate set ⇒ nonzero residual family ⇒ seat-1 H5 and the
  "at most one" holding are **(9,5) artifacts**;
- (ii) the `O(p,q)`-type Krein structure **forces the sign** (9,5) leaves open
  ⇒ register M-H4's conjecture lands and the anchor gets its first positive
  result.

Both outcomes improve the envelope count (adjudication §1). We additionally
register the possibility that the result lands in NEITHER preregistered shape
(e.g. the candidate set enlarges only in the antilinear sector while the linear
classification and the existence leg both persist); if so, that is reported as
such, against both (i) and (ii), with the structural reason.

**Specific checks registered:**

- D-1 (fixtures): (7,7) Clifford relations; anchors bare ≈ 58.7215,
  C2 ≈ 155.3625, `dim ker Γ = 1664`; `J² = +1` on the spinor factor AND on `V`.
- D-2 (classification leg): graph-certificate complex commutant of the 44
  compressed generators on `V` (two seeds, three thresholds). Prediction:
  `dim_C = 1`. Real commutant then = `span_R{I, iI, J, iJ}` with `J² = +1` —
  the SPLIT quaternions ≅ M(2,R), NOT the division algebra H: the Kramers wall
  is ABSENT at algebra level (H5 is (9,5)-only, as fenced). On the real form
  `V^J` (dim_R 1664) the algebra is predicted R-irreducible with real
  commutant `R·I` (direct real graph certificate).
- D-3 (candidate sets): linear commuting involutions = {±I} (unchanged);
  antilinear involutions `{cJ : |c| = 1}` EXIST (a U(1) family) — the enlargement
  is real but confined to the antilinear sector.
- D-4 (the M-H4 sign question): under (7,7) the spinor Krein symmetry is
  forced to be `β = i·e_0…e_6` (p = 7 ≡ 3 mod 4; unique up to real scalar), and
  the `i` makes `J` ANTI-commute with `β`. Prediction: `η_V(Jx, Jy) = −conj(η_V(x,y))`,
  so the restricted pairing on the real points `V^J` is SKEW (symplectic,
  Sp(1664,R)-type), NOT an O(p,q) form — there is no real orthogonal signature
  and the sign-forcing route of M-H4 closes structurally. (If the computation
  instead finds `η_V` J-real, outcome (ii) is live and the real signature is
  computed and reported.)
- D-5 (existence leg): the η_V-skew diagonal boost `D = M_{09}⊗I + I⊗σ_{09}`
  is still inside the algebra ((0,9) is still a boost pair under (7,7)), with
  exponential growth witness (rate ≈ +1.5; exact `Re spec(D) = {±1/2, ±3/2}`)
  and a compact rotation contrast (rate ≈ 0). By Prop 1's necessity leg
  (which uses no property of η), `F = ∅` for EVERY nondegenerate form and every
  invariance structure containing that direction — predicted signature-robust.
- D-6 (neutrality): `ω β + β ω = 0` still exact under (7,7) ⇒ signature of
  `η_V` on `V` is (832, 832) FORCED (both ω-halves isotropic), so ±I both fail
  positivity independently of D-5.

**Kill conditions registered:** if D-2 returns `dim_C > 1`, the (7,7)
classification leg lands on the REDUCIBLE branch and the residual-family data
are reported per fence (3) of the probe. If D-4 finds a J-real `η_V` with a
definite restricted signature, M-H4 lands (outcome ii). If D-5's boost fails to
grow, the existence-leg transfer fails and the (9,5) `F = ∅` is signature-
conditional — a finding against seat-1 E-exports.

---

## 2. RESULTS (appended after the runs; preregistration above unedited)

Both scripts green on 2026-08-03, hard asserts throughout:

- `tests/generation-sector/q2_imposter_chirality_grading.py` — **318 checks
  passed, elapsed 14–17 s, exit 0.**
- `tests/observable-algebra/dq2_trichotomy_77_rerun.py` — **70 checks passed,
  elapsed 68–82 s, exit 0.**
- `process_gates/certificate_shape_audit.py` (P-C3 gate) — **4/4 OK, exit 0**
  after both scripts were added (both carry asserts + exit coupling; neither
  is a library module).

### 2.1 Q2 — every preregistered kinematic prediction confirmed; physical PH-K1 remains open

Fixtures reproduced under BOTH signatures (the anchors are signature-identical
to 4 decimals as banked): bare `||[Pi_RS, M_D]|| = 58.7215`, `C2 = 155.3625`,
`dim ker Γ = 1664`; Clifford relations exact to machine zero.

| Prediction | Result |
|---|---|
| P-Q2-1: imposter 64+64 | **CONFIRMED**: `(64, 64)` under (9,5) AND (7,7), all five allocations each (ten runs, identical). Invariance residuals ~2e-16; the mechanism identity `(I⊗ω)∘ι = −ι∘ω` holds to 0. |
| P-Q2-2: 192+192 / 576+576 / 64+64 | **CONFIRMED** in all ten runs; sums to `(832, 832)` = the trichotomy probe's certified inertia, re-derived from the block side (the hinge panel's L5 bonus, now with the grading refinement). |
| P-Q2-3: joint `(ω_4, ω_10)` grading of S = 32/32/32/32 | **CONFIRMED**, with `tr(ω_4) = 0` exactly inside EACH ω-half of S — every internal chirality half appears with both base-side chiralities in equal multiplicity. |

**PH-K1-KINEMATIC status: CONFIRMED. PH-K1-PHYSICAL: OPEN/BLOCKED.** The
Reading-A block is vectorlike under the computed ambient/ten-factor grading,
under both real forms. Transport to measured V−A currents requires the
unbuilt physical carrier, observation/VEV/BRST/reality/SM-gauge map, and an
adjudication that Reading A is the intended third-family referent. Vectorlike
matter is anomaly-free in the ordinary gauge-anomaly sense, so no anomaly
claim is made here. No bar moves on this artifact.

New facts found while computing (not preregistered, `CHEAP_NEW_COMPUTATION`):

1. **The three blocks are mutually ORTHOGONAL** — max principal cosine between
   the imposter and `ker Γ_B ⊕ ker Γ_F` is 0 to machine zero (all ten runs).
   Reason, visible in the construction: the metric-dual embedding is exactly
   the adjoint of the partial trace, `ι_B = Γ_B^†`, so the imposter
   `im(10 ι_B − 4 ι_F)` is orthogonal to `ker Γ_B` and `ker Γ_F` by
   construction. The 3:9:1 decomposition is an orthogonal direct sum, not
   merely a direct sum. Also `X^†X = 560·I` exactly (X = 10ι_B − 4ι_F): the
   antidiagonal is an exact tight frame, `560 = 100·4 + 16·10`.
2. **Product-rule scalar**: `ω_4 ω_10 = c·ω` with `c = (−1)^{q_B}` (the parity
   of minus-directions allocated to the base): observed `+1, −1, +1, −1, +1`
   across the five allocations, both signatures. Unimodular in every case —
   the even/even product rule holds with an allocation-dependent SIGN, which
   any later `ω_4`-vs-`ω`-grading bookkeeping must carry.
3. `Γ∘ι_B = 4·I` and `Γ∘ι_F = 10·I` confirmed exactly, allocation-invariant,
   both signatures (the hinge-panel mechanism numbers).

### 2.2 DQ2 — the (7,7) rerun: the result lands in NEITHER preregistered shape, and both legs transfer

Fixtures: (7,7) anchors `bare = 58.7215`, `C2 = 155.3625`, `ker Γ = 1664`
reproduced; `J² = +1` on the spinor factor (residual 5.8e-12) and on `V`
(2.1e-11); J commutes with all 14 generators (max defect 4.4e-12).

**Classification leg.** The 44-generator compression family is adjoint-closed
(1.1e-16); census: exactly 1/44 ambient counterparts preserves `ker Γ` (the
volume word; margin 1.3e-2) — A is a COMPRESSION algebra under (7,7) too, and
the covariant (Dirac-sense) contrast lands on the REDUCIBLE branch under (7,7)
too (all 91 diagonal generators preserve `ker Γ`, residual 4e-18; `ω_V`
non-scalar, distance 40.8). Graph certificate: **`dim_C commutant = 1`** (two
seeds, three thresholds, min gaps 2.2e-3 / 9.6e-4). Real commutant of the
complex carrier: `span_R{I, iI, J, iJ}` with `J² = +1` = the **SPLIT
quaternions ≅ M(2,R)** — proper real-linear idempotents `(1±J)/2` exhibited —
NOT the division algebra `H`. On the real form `V^J` (`dim_R = 1664`,
constructed as the +1-eigenspace of the symmetric orthogonal involution
`T = [[Re U_V, Im U_V],[Im U_V, −Re U_V]]`, eigenvalues exactly 1664/1664):
all 44 generators restrict to REAL operators (max rel imag 3.4e-13) and the
real graph certificate gives **real commutant `R·I`** (min gap 6.0e-4,
threshold-stable). So: the quaternionic Kramers wall is **ABSENT** at algebra
level under (7,7) — seat-1 H5 is (9,5)-ONLY, exactly as fenced — but the
LINEAR involution candidate set is UNCHANGED: `{cI : c² = 1} = {±I}`, so the
"at most one admissible fundamental symmetry" holding **TRANSFERS** (it rests
on commutant triviality, not on the wall).

**Candidate sets.** The enlargement is real and confined to the ANTILINEAR
sector: `(cJ)² = +1` verified for c = 1, i, e^{iπ/4} — a raw U(1) phase orbit
of antilinear involutions exists, where (9,5) had none (`(cJ)² = −|c|²`
there). Scalar phase conjugation is transitive on this orbit, so it is not a
residual modulus. Linear residual family: dimension 0, unchanged.

**The canonical `J`-fixed kinematic route in the M-H4 sign question closes
structurally, against that sub-conjecture.** Under
(7,7) the spinor Krein symmetry implementing `β e_a β^{-1} = e_a^†` is forced
to be `β = i·e_0…e_6` (the real 7-word squares to −I since p = 7 ≡ 3 mod 4;
the spinor-factor commutant is certified `C·I`, so β is unique up to a REAL
scalar). The factor `i` makes J ANTI-commute with β (residual 5.8e-12), hence
`η_V(Jx, Jy) = −conj(η_V(x, y))` (J-skewness residual 5.0e-13 vs J-reality
residual 2.0 — maximal). Consequence, verified directly: the restriction of
`η_V` to the real points `V^J` is PURELY IMAGINARY (rel Re part 2.4e-13) and
its imaginary part is a nondegenerate SKEW form (`s_min/s_max = 1.0`) — the
real form carries an **Sp(1664,R)-type symplectic structure, not an O(p,q)
form**. There is no real orthogonal signature, hence no sign to force:
M-H4's proposed `O(p,q)` signature has no object on this particular fixed real
form. The underlying realification still carries the symmetric form
`Re eta_V`, and the actual `(7,7)` stabilizer commutant remains uncomputed.

**Existence leg — transfers intact.** The η_V-skew diagonal boost
`D = M_{09}⊗I + I⊗σ_{09}` lies inside the constructed algebra (residual
<1e-8), preserves `V`, and has witnessed log-growth rate **+1.500000** (the
compact rotation contrast: 5.6e-17). Its numerically resolved spectrum on `V`:
`Re spec(D) = {−3/2, −1/2, +1/2, +3/2}` with multiplicities
`{64, 768, 768, 64}` (max |Im| = 7.9e-16) — vector weight 1 + spinor weight
1/2, identical in form to the reviewed (9,5) value. By Prop 1's necessity leg
(which uses no property of η), `F = ∅` for every nondegenerate form and every
invariance structure containing that direction. The neutrality is also forced
under (7,7): `ωβ + βω = 0` exactly, both ω-halves totally isotropic
(1.6e-16), signature `(832, 832)`.

**Preregistration readout (against §1.2, both outcomes):** the result lands in
NEITHER preregistered shape as stated.

- Outcome (i) FAILS for the linear family: the candidate set is still `{±I}`,
  the linear residual family is 0, and "at most one admissible fundamental
  symmetry" is NOT a (9,5) artifact — it transfers. Outcome (i) HOLDS for the
  antilinear sector only: the raw U(1) phase orbit `{cJ : |c| = 1}` of
  antilinear involutions exists under (7,7) and not under (9,5), but is not a
  residual modulus; H5's algebra-level
  Kramers sentence is (9,5)-only (already fenced; the fence is now a
  computation).
- Outcome (ii) DIES only for the canonical `J`-fixed kinematic route: the
  restricted form is symplectic and supplies no orthogonal sign. M-H4's actual
  stabilizer/signature row remains open.
- Seat-1 K3's framing ("either way the anchor as stated does not survive
  intact") is refined: H5 restates to its fenced (9,5)-conditional form; the
  `F = ∅` existence result and the "at most one" classification result are
  SIGNATURE-ROBUST and survive intact. The (9,5) `F = ∅` is NOT a (9,5)
  artifact.

**Instrument note (honest disclosure).** The real-form graph certificate
initially FAILED on the bare generator span: over R the symmetric span of the
44 restricted generators is only the ~22 Hermitian directions (the
`i(K − K^†)` Hermitian directions available over C do not restrict to real
operators), and that thin span is exactly degenerate (a Clifford-vector
combination has multiplicities 768/768/64/64 on `V^J`; observed min gap
exactly 0). The certificate was repaired by drawing the generic element from
the algebra properly: 60 random second-order words `K_a K_b` added (any
commutant element must commute with words), after which the spectrum is
simple (min gap 6.0e-4) and threshold-stable. This is a genericity failure of
the LINEAR span, not of the method; the complex certificates were unaffected.

### 2.3 Layer-0 typing of the results

- The confirmed PH-K1-KINEMATIC result is typed against "chirality" sense: ambient ω-grading plus
  the joint `(ω_4, ω_10)` refinement — NOT a 4D Weyl index. Note computed en
  route: `ω_4` alone does NOT preserve the imposter block (only the total ω
  does; `ι_B` and `ι_F` intertwine with opposite signs under `ω_4`), so any
  future "4D chirality of the imposter" claim must route through the
  identification `ψ ↦ x_ψ`, not through a naive `ω_4` restriction.
- The DQ2 result keeps `F_A(η_V)` (algebra sense) and `F_H(η)` (group sense)
  separate as the corrected trichotomy note requires; the boost subgroup is
  the Prop-1 object.
- All results are on the KINEMATIC carrier; nothing transports to the
  interacting theory (rankN `Π_κ` fence, seat-1 E4).
- Labels: Q2 results and DQ2 legs `CHEAP_NEW_COMPUTATION`; the M-H4 closure is
  a computed kill of a `REFEREE_CONJECTURE` at kinematic scope; the
  block-orthogonality and tight-frame facts are `CHEAP_NEW_COMPUTATION`.

### 2.4 Named gates moved (P-H28 accounting; statuses are proposals to the orchestrator, not enacted here)

- **PH-K1-KINEMATIC**: `OPEN -> CONFIRMED` for Reading A.
- **PH-K1-PHYSICAL**: remains `OPEN/BLOCKED`; no V−A or anomaly verdict moves.
- **Signature fork (A3⊕A4)**: both Wave-A-1 targets now have both-form
  answers; the Q2 answer is fork-INDEPENDENT (64+64 both ways); the DQ2
  answer splits per leg (wall (9,5)-only; `F = ∅` and "at most one"
  fork-robust; the canonical `J`-fixed sign route dead, M-H4 still open).
- **Seat-1 H5/K3**: H5's fence is now a computation; K3's "does not survive
  intact" resolves to "restates, with the two legs surviving".

P-H29 note: none of the cited numbers is an FD-read null. The probes use
deterministic NumPy finite linear algebra with machine-zero-to-1e-11 residuals,
randomized generic elements, and thresholded graph certificates. Analytic
Clifford identities are exact; numerical commutant and spectrum conclusions
remain numerical until an exact/interval certificate is supplied.

## 3. What this artifact does NOT do

No verdict, bar(b), H59, canon, count, or LANE-STATE movement. The kinematic
carrier is not the physical carrier. Blocks are multiplicities, not
generations. The carrier-split fork (:24), the imposter A/B fork, the actual
stabilizer computation, and the physical chirality map remain open; nothing
transfers across them silently. The ten-dimensional factor is the
complexified ten-factor chirality object (physically allocated as
`Spin(6,4)`), not a completed compact `Spin(10)` or Standard Model reduction.
