---
artifact_type: exploration
status: exploration (W170; 5-persona inline team; one deterministic test 18/18 exit 0; the Turok-Bateman non-perturbative question adjudicated against the primary source, R1, W132)
created: 2026-07-14
hypothesis: the Turok-Bateman mechanism / [P_ghost, S] = 0 (in service of H59, the keystone W167/W168 convergence)
branch: "Team TUROK-BATEMAN (W170): does the Bateman-Turok non-perturbative mechanism, applied to GU keep-and-grade, establish [P_ghost, S] = 0 / the Krein grading OPERATIVE non-perturbatively, or clear the FREE / TREE theory only?"
title: "W170 VERDICT: FREE-ONLY-NARROWED. Turok-Bateman is a PARITY (pseudo-unitarity) statement NON-PERTURBATIVELY / to all orders and a POSITIVITY statement at TREE LEVEL ONLY. The O(1,1) two-field embedding gives the ghost parity as an EXACT symmetry, so the parity leg [P_ghost, S] = 0 / the optical theorem S^dag eta S = eta survives interactions to all orders (this is the non-perturbative content). But probability POSITIVITY -- the leg that clears bar (b) -- is proved only at tree level in the primary source (arXiv:2607.00096); loop positivity is never claimed and is delegated to a resummation conjecture plus a to-appear companion. The bridge is R1's two-line theorem: [P,S]=0 with P^2=I gives positivity IFF eta*P > 0, so commutation is NECESSARY but NOT SUFFICIENT; the extra datum eta*P_ghost > 0 at loop level IS the interacting C-operator, which W132 already reduced keep-and-grade positivity to WITHOUT REMAINDER (priced non-local by W54, QM-only by branch B / R1). Machine-checked separation: one pseudo-unitary S is simultaneously (i) [P_ghost, S] = 0 exact, (ii) naive-physical-subspace-positivity-VIOLATING (A^dag A = P+ + B^dag B, row sum 1.0075 > 1), (iii) C-metric-unitary. GU-specific narrowing: TB's PROVEN positive sector is the conformal factor of quadratic gravity with the spin-2 graviton AND its ghost DECOUPLED; GU's keep-and-grade matter Krein space (RS module, self-dual triplet, record/RS source-action vertex) is the gauged/matter case TB relegate to 'presented elsewhere' -- outside even the tree theorem. Bar (b) is RE-POSED, not cleared. H59 remains OPEN."
grade: "EXACT for the finite-dimensional separation identities (A^dag A = P+ + B^dag B; the C-metric coexistence; R1's two-line theorem both directions; machine-verified to 1e-10). TOY-CHECKED for the W120 graded odd-ghost cut (closed form). AUDITED-SOURCE for the primary-source claim table (VG-SC intake of arXiv:2607.00096: optical theorem all orders / positivity tree-only / loop positivity never claimed / gauged versions unbuilt). STRUCTURAL for the application to GU's keep-and-grade matter sector (no GU source action exists; the transfer is CONSISTENT_UNCOMPUTED per R1). ARGUED for the non-perturbative-parity-not-positivity reading (the O(1,1) embedding is exact; positivity remains order-by-order). Test: W170 18/18 exit 0, with positive controls (Bateman free clearing; W120 graded cut) and a negative control (commutation-without-positivity gives complex spectrum). NO canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN."
depends_on:
  - canon/ghost-parity-krein-synthesis.md
  - explorations/big-swing-2026-07-06/VG-SC-bateman-turok-loop-and-degenerate.md
  - explorations/big-swing-2026-07-06/R1-pu-pt-vs-ghost-parity.md
  - explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md
  - explorations/H59-krein-loop-positivity-gate-2026-07-12.md
  - tests/W120_path2_target2_keepgrade_vs_clop.py
scripts:
  - tests/W170_turok_bateman_nonperturbative.py
external_refs:
  - "Bateman & Turok, Escape from Ostrogradsky via Hidden Ghost Parity, arXiv:2607.00096 (July 2026) -- four-derivative UV-complete QFT quantized on a Krein space; ghost parity via O(1,1) embedding; optical theorem to all orders; tree-level positivity"
  - "Bender & Mannheim, No-ghost theorem for the fourth-order Pais-Uhlenbeck model, arXiv:0706.0207 = PRL 100, 110402 (2008) -- the dynamics-derived C-operator"
  - "'t Hooft & Veltman, Diagrammar, CERN 73-9 -- largest-time equation, pseudo-unitarity diagram by diagram"
---

# W170 -- the Turok-Bateman non-perturbative mechanism, applied to GU keep-and-grade

**Role.** The keystone convergence (W167/W168) reduced the whole ghost question to ONE object:
is GU's keep-and-grade Krein grading physically OPERATIVE = `[P_ghost, S] = 0` at LOOP level =
does the interacting C-operator exist? OPERATIVE => the tachyon is spurious, the ghost is a
record, bar (b) CLEARS; NOT-OPERATIVE => the tachyon is physical / a record-accretion engine,
bar (b) is re-posed. The repo anchors the keep-and-grade rescue to Bateman & Turok's Bateman
dual-oscillator / hidden-ghost-parity construction (canon `ghost-parity-krein-synthesis.md`).
This team asks the TB-specific form: does the Turok-Bateman mechanism ESTABLISH the grading
operative NON-PERTURBATIVELY (bypassing the loop-order obstruction the perturbative route hits),
or does it clear the FREE / TREE theory only? Five personas ran inline; one deterministic test
`tests/W170_turok_bateman_nonperturbative.py` (18/18, exit 0).

## 0. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md discipline)

| Object | Constructions in play | Handling |
|---|---|---|
| **"The Turok-Bateman statement"** | (i) PARITY: pseudo-unitarity `S^dag eta S = eta` / optical theorem + `[P_ghost, S] = 0`; (ii) POSITIVITY: Born-rule probability positivity, i.e. `eta_+ = eta P_ghost > 0` | BOTH computed; the verdict is stated per leg -- this fork IS the result |
| **"Non-perturbative"** | (i) the O(1,1) two-field embedding is exact (structural); (ii) an order-by-order loop claim | the embedding gives exact-symmetry PARITY; POSITIVITY stays order-by-order |
| **The ghost parity `P_ghost`** | the `Z2` swapping generation `<->` mirror (null-half swap, C-like); NOT the fundamental symmetry `eta` (sign of norm) | kept distinct: `[P_ghost, S] = 0` is not `[eta, S] = 0`; the C-operator is `P_ghost` AND `eta P_ghost > 0` |
| **"The physical subspace"** | free-grading positive sector `H_+`; the C-positive subspace | both characterized; positivity holds on `H_+` only at tree (`B = 0`) |

## 1. Persona 1 -- Turok-Bateman / cosmology specialist: what the mechanism actually is

The Bateman dual-oscillator move is a NON-perturbative recasting, not a loop resummation. The
free four-derivative theory (`box^2 phi`, double-pole propagator `-i/(p^2)^2`) is EMBEDDED in a
two-derivative, two-field `O(1,1)`-symmetric model; the ghost parity is the discrete `Z2` that
becomes explicit under that embedding. In GU-relevant form (canon fact 3, reproduced in the test,
A1-A3): each self-dual-triplet generation is bound to its mirror in a hyperbolic (null) pair,
`K = [[0,1],[1,0]]`; the ghost parity `u <-> v` labels `u+v` as `+`-norm physical and `u-v` as
`-`-norm ghost, norms `+/- 2<u,v>`. The propagator side is the partial-fraction split
`D(s) = (1/M^2)[1/s - 1/(s-M^2)]` into a normal pole (residue `+1/M^2`) and a ghost pole
(residue `-1/M^2`); the ghost parity is the residue-sign flip made explicit by the two-field
embedding.

**What the embedding buys, precisely.** Because it is exact, the ghost parity is an EXACT
symmetry, and provided the interaction Lagrangian is ghost-parity-Hermitian, pseudo-unitarity
`S^dag eta S = eta` (the optical theorem) holds TO ALL ORDERS -- BT's headline claim, resting on
't Hooft-Veltman's largest-time equation. This is genuinely non-perturbative content: it is not a
tree fact. It is the PARITY leg.

**What it does not buy.** The generalized Born rule (probability positivity) is a SEPARATE
theorem, and BT prove it at TREE LEVEL ONLY. The primary-source fine print (VG-SC intake of
arXiv:2607.00096, four independent fetches) is unambiguous:

| property | order | status in the paper |
|---|---|---|
| optical theorem / pseudo-unitarity (PARITY) | all orders | claimed, from the Krein spectral property + Hermitian interaction |
| positivity of transition probabilities (POSITIVITY) | tree level | proved (the paper's theorem) |
| loop-level positivity | loop | **never claimed anywhere** |
| stated obstacle | loop | collinear IR of asymptotic states, "carefully regulated and resummed" (conjecture) + to-appear companion |

So the answer to the framing question is already visible: **Turok-Bateman is a PARITY statement
non-perturbatively, and a POSITIVITY statement at tree level only.** The non-perturbative
character lives on the parity axis, not the positivity axis. There is no non-perturbative
positivity theorem in TB (test F3).

## 2. Persona 2 -- Krein / PT specialist: is it a positivity or a parity statement?

Reuse W132's commutation-vs-positivity distinction, sharpened. Pseudo-unitarity gives, for a
physical in-state and the free grading `eta = P_+ - P_-`,

    A^dag A = P_+ + B^dag B,   A = P_+ S P_+,  B = P_- S P_+,

an EXACT, all-orders operator identity (test D1). Consequences: the physical-subspace S-matrix is
an EXPANSION, physical-channel probability sums to `1 + ||B|i>||^2 >= 1`, equality iff `B = 0`.
Pseudo-unitarity (PARITY) is exactly this identity's premise and survives to all orders; it does
NOT deliver `B = 0`. Positivity (probability conservation on the physical world) is the separate
statement `B = 0`, i.e. `S` commutes with the grading -- which by W132's Bognar note is precisely
the C-operator condition.

The bridge is R1's two-line theorem (re-verified here, test E1/E2): if `P^2 = I`, `[P, S] = 0`,
and `G := eta P` is POSITIVE definite, then `S` is `G`-unitary => real spectrum, diagonalizable,
positivity-compatible. So:

- **`[P_ghost, S] = 0` (PARITY) is NECESSARY but NOT SUFFICIENT for positivity.** The missing
  datum is `eta P_ghost > 0`.
- **`eta P_ghost > 0` at loop level IS the interacting C-operator** (`C = P_ghost`, `eta_+ = eta C
  > 0`). W132 reduced keep-and-grade positivity to it WITHOUT REMAINDER; W54 prices it non-local;
  branch B / R1 have it order-by-order in QM only.

Verdict of this persona: **TB is fundamentally a PARITY statement**; its positivity content is a
tree-level corollary that does NOT lift, because the lift requires `eta P_ghost > 0` at loop
level, which is exactly the open interacting-C object. The machine-checked separation (test D4):
ONE pseudo-unitary `S` is simultaneously `[P_ghost,S]=0`-consistent, naive-positivity-VIOLATING
(row sum `1.0075 > 1`, `||B|| = 0.096`), and C-metric-unitary (`min eig(eta_+) = 0.687 > 0`,
`C^2 = I`, `[S,C] = 0`). Parity survives; positivity is contingent on the C-metric.

## 3. Persona 3 -- GU-model specialist: does interaction preserve the graded pair in GU?

Two GU-specific narrowings, both cutting toward FREE-ONLY.

**(i) TB's proven sector is not GU's matter sector.** BT's tree-positivity theorem covers the
conformal factor of quadratic gravity; in that limit the spin-2 graviton AND its ghost counterpart
DECOUPLE (VG-SC section 3.3, CHECKED). GU's keep-and-grade object is the Rarita-Schwinger matter
Krein module -- the `192`-dim self-dual triplet with signature `(+96,-96,0)`, the `96` hyperbolic
(generation, mirror) pairs, and (once built) the record / RS source-action vertex. That is the
gauged/matter case BT explicitly relegate to "we have also studied gauged versions: the results
will be presented elsewhere" (unbuilt). So even the TREE positivity theorem does not transfer to
GU's actual structure (test F2); the transfer is `CONSISTENT_UNCOMPUTED` (R1), because GU supplies
no `S`.

**(ii) The interaction is where the graded pair is tested, and GU has no interaction built.** The
kinematic graded pair (the `Z2` swapping the null halves) EXISTS as a linear map -- canon and R1
both confirm the Krein structure survives everywhere, including the degenerate boundary. What is
open is whether GU's eventual source action realizes `eta P_ghost > 0` under loops. R1 sharpened
canon's condition to a property of `S` alone: `[P_ghost, S] = 0` with a positivity-compatible
parity is EQUIVALENT to `S` Krein-diagonalizable with real spectrum on the matter module, and
named a new failure mode (the equal-frequency Jordan locus, where NO positivity-compatible ghost
parity exists at all). TB does not remove that gate; it supplies the tree corollary that lives
above it.

## 4. Persona 4 -- symbolic engineer: the tests (W170, 18/18, exit 0)

Positive controls (the mandate's "reproduce the Bateman free clearing and W120's graded cut"):

- **A1-A3** reproduce the Bateman FREE clearing in GU-relevant hyperbolic-pair form: `K` signature
  `(+1,-1)`, ghost-parity even/odd = `+/-`-norm (norms `+/- 2<u,v>`), and the O(1,1)
  normal/ghost residue split of the four-derivative propagator.
- **B1-B2** reproduce W120's graded odd-ghost cut: `-pi(1 - M^2/s) < 0`, opening at `s = M^2`, so
  `B != 0` at any loop with an open odd channel (the interacting regime).

The interacting-survival check:

- **C1** PARITY survives: `S = e^{Q/2} e^{ih} e^{-Q/2}` (W132 construction, `Q` Hermitian and
  `eta`-odd, `h` Hermitian and `[h,eta] = 0`) is pseudo-unitary, `||S^dag eta S - eta|| = 4e-16`.
- **D1-D4** POSITIVITY does not survive on the free grading: `A^dag A = P_+ + B^dag B` exact; row
  sum `1.0075 > 1`; positivity restored only by the C-metric `eta_+ = e^{-Q} > 0`; the three
  statements coexist on the SAME `S`.
- **E1** positive-metric branch: `eta P > 0` => real spectrum (positivity-compatible). **E2**
  NEGATIVE control: commutation `[P,S]=0` WITHOUT `eta P > 0` (indefinite) gives COMPLEX spectrum
  -- positivity fails despite the parity. This is the discriminating control: the machinery
  genuinely separates parity from positivity.

## 5. Persona 5 -- adversarial skeptic: steelman FREE-THEORY-ONLY, then attack it

**The steelman, at full strength (test F1).** TB clear the FREE ghost decisively: the O(1,1)
embedding is exact, the ghost parity is an exact symmetry, tree positivity is proved, and
pseudo-unitarity holds to all orders. But every loop-level positivity statement in the published
record is either absent or promissory: loop positivity is NEVER claimed; the sole loop obstacle
BT name (collinear IR of asymptotic states) is delegated to a resummation CONJECTURE plus a
to-appear companion; the gauged/matter sector (GU's actual object) is "presented elsewhere." On
the audited primary source, TB is a free/tree-plus-all-orders-parity result. Applied to GU's
interacting keep-and-grade matter sector, it establishes NOTHING at loop level about positivity.

**Attacks on FREE-ONLY (each answered):**
1. *"The all-orders optical theorem IS a non-perturbative loop result, so the grading is operative
   non-perturbatively."* Answered: it is a non-perturbative PARITY result. It is `S^dag eta S =
   eta`, not `eta P_ghost > 0`. W132's `A^dag A = P_+ + B^dag B` shows pseudo-unitarity coexists
   exactly with positivity FAILURE. Bar (b) needs the positivity leg, which the optical theorem
   does not carry.
2. *"The O(1,1) embedding is exact, so if the ghost parity commutes non-perturbatively, positivity
   follows."* Answered by R1's two-line theorem and E2: commutation is necessary, not sufficient;
   `eta P_ghost` can be indefinite while `[P_ghost, S] = 0`, giving complex spectrum / positivity
   failure. The extra datum `eta P_ghost > 0` is the interacting C-operator, open (branch B: QM
   only; W54: non-local).
3. *"BT's IR obstacle is 'just' QCD-like resummation, not a ghost-consistency problem, so it will
   resolve."* Answered: possibly, but that is a CONJECTURE with a to-appear companion; honest
   grading cannot upgrade a promissory note to an established non-perturbative positivity theorem,
   and even if granted it addresses IR-finiteness of asymptotic states, not the Born-rule
   positivity of loop-level `|M|^2` processes, which is a separate open item.

**Skeptic's residue (honest).** If GU's eventual source action turns out to be Krein-diagonalizable
with real simple spectrum on the matter module (R1's PT-unbroken condition), then `P_ghost = C`
would be derived and the grading operative -- but that is a condition ON THE UNBUILT `S`, not
something TB supply. TB relocate and sharpen the open condition; they do not discharge it.

## 6. Verdict

**FREE-ONLY-NARROWED.**

- **Positivity or parity?** Turok-Bateman is a PARITY (pseudo-unitarity / optical-theorem)
  statement NON-PERTURBATIVELY / to all orders, AND a POSITIVITY (Born-rule) statement at TREE
  LEVEL ONLY. The non-perturbative content is the exact-symmetry ghost parity from the O(1,1)
  embedding; it lives on the parity axis. There is no non-perturbative positivity theorem in TB.
- **Does it survive interactions?** The PARITY leg survives to all orders (pseudo-unitarity holds
  for any ghost-parity-Hermitian interaction). The POSITIVITY leg does NOT survive to loops in the
  primary source: loop positivity is never claimed; on the free grading it FAILS exactly
  (`A^dag A = P_+ + B^dag B`, `B != 0` by W120); it is restored only by the C-metric `eta_+ =
  eta P_ghost > 0`, which at loop level IS the interacting C-operator -- open (branch B: QM only;
  W54: non-local; R1: `= Krein-diagonalizability of the unbuilt S`). Commutation is necessary, not
  sufficient (R1 two-line theorem).
- **Effect on bar (b).** Bar (b) is RE-POSED, NOT cleared. TB do not bypass the loop-order
  positivity obstruction; they relocate GU's open source-action condition and sharpen it, exactly
  matching H59 / W132: keep-and-grade positivity reduces WITHOUT REMAINDER to the interacting
  C-operator. Applied to GU's matter sector the situation is a fortiori open, since even TB's tree
  theorem covers only the conformal factor (spin-2 ghost decoupled), not GU's RS / record / source
  vertex (the unbuilt gauged case).

**H59 remains OPEN.** No canon / RESEARCH-STATUS / claim-status / verdict / posture change.

## 7. What this does NOT do

No claim that keep-and-grade is dead: the C-metric route remains open exactly to the extent the
QFT C-operator question is open. No claim that TB are wrong -- their free/tree result is exact and
their all-orders pseudo-unitarity is genuine; what is NARROWED is the reach of the mechanism to
the interacting positivity that bar (b) needs. No GU loop amplitude computed; no GU source action
built (the transfer is `CONSISTENT_UNCOMPUTED`). The finite-dimensional separation is a faithful
model of the operator identities, not a field-theory computation; its role is to exhibit, exactly,
that parity and positivity are independent and that TB deliver the first non-perturbatively and the
second only at tree.

**Artifacts:** this file + `tests/W170_turok_bateman_nonperturbative.py` (18/18, exit 0).
