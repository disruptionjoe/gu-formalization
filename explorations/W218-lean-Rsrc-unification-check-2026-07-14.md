---
artifact_type: exploration
label: W218
created: 2026-07-14
posture: coherence-first; exploration grade; conditional register; truth-seeking (a clean DISTINCT is as valuable as a coincidence); RUTHLESS skeptic; tri-repo gating STRICT
title: "W218 VERDICT: DISTINCT + VECTORLIKE. Building the twisted-Rarita-Schwinger source re-grading R_src EXPLICITLY on the verified Cl(9,5)=M(64,H) rep -- as the (6,4)-fiber Clifford-trace pushforward Pi_RS (sum_a c(e^a) M_D c(e_a)) Pi_RS restricted to the explicit (+96,-96) cross-chirality triplet carrier (dim 192 = 3x64, the top-Casimir j=1 eigenspace of the self-dual SU(2)+ on ker Gamma) -- and running the two decisive type reads settles W201's open computation (Sec 6). R_src is chirality-ODD and K-SELF-adjoint, but the Hermitian K_c R_src has signature (96,96): R_src is the K-NULL / K-indefinite type, NOT the C-operator's K-DEFINITE (192,0). It is Frobenius-ORTHOGONAL to C = sign(K_c) (best-fit coefficient ~ 1e-16, residual = full norm) and [R_src, K_c] != 0 while [C, K_c] = 0. So TEST 1 (unification) = DISTINCT: R_src is NOT the unitarity grading eta_+ = eta*C, and is not even the same operator type. TEST 2 (chiralize vs vectorlike) = VECTORLIKE: chi = tr(omega sign(R_src)) = 0, FORCED exactly by {R_src, omega} = 0 (chirality-odd => sign is odd => tr(omega sign) = 0; core-theorems Theorem 3) and structurally witnessed by the vanishing chirality-diagonal blocks (R_src is purely off-diagonal in chirality, the [[0,B],[B',0]] form). Robust across the (6,4)-fiber / all-14 / no-Pi / (3,1)-horizontal channels. This CONFIRMS W201's coherence lean at the operator level -- the generation-count source operator and the unitarity/finality C-operator are NOT the same object, and the source operator, being index-conserving on the carrier, cannot by itself deliver a count: a SEPARATE Z/3 self-dual import is still required. Test tests/W218_lean_Rsrc_unification_check.py 21/21 exit 0, positive controls first."
grade: "EXACT / machine-verified (21/21, deterministic, tests/W218_lean_Rsrc_unification_check.py) for: the Cl(9,5)=M(64,H) Clifford relations, K_S(64,64), chirality omega_S(64,64) (Block A); the explicit (+96,-96) carrier -- ker Gamma=1664, triplet=192=3x64 with top Casimir 8.0, carrier chirality omega_c(96,96), carrier Krein K_c(96,96) CROSS-CHIRALITY (K_c omega_c + omega_c K_c = 0 to 1e-15), and eta_+=eta*C positive-definite (192,0) with C=sign(K_c) chirality-odd, K-definite, [C,K_c]=0 (Block B); R_src built as the fiber-Clifford-trace pushforward (Block C); the two TYPE READS -- chirality-ODD ({R_src,omega}=0 to 8e-15), K-SELF-adjoint (R_src^dag K_c - K_c R_src = 0 to 8e-15), the STABLE discriminator sig(K_c R_src)=(96,96) K-null, and the vanishing chirality-diagonal blocks (2.6e-15) (Block D); TEST 1 DISTINCT (R_src perp C, residual = full norm; [R_src,K_c] != 0) and TEST 2 VECTORLIKE (chi=0 forced) (Block E); and channel-robustness plus the Clifford-trace disqualifier (Block F). STRUCTURAL / RECONSTRUCTION for the identification of this ultralocal fiber-Clifford-trace with the geometric pi_! pushforward W201/located-not-forced hold OPEN (the non-convex GL(4,R)/O(3,1) fiber), and for the SHIAB-03 intertwiner-level RS-channel selection (fixed here by the ker-Gamma triplet carrier; the note reports test-1 as conditional on that fixing). ULTRALOCAL. No canon / RESEARCH-STATUS / claim-status / verdict / posture change; bar(b) and H59 stay OPEN; the count stays {1,3}; no Z/3 count VALUE, no nonlocal Z_U completion, no Krein SIGN for GU."
construction: "program-native where the objects are GU's (the Cl(9,5)=M(64,H) rep; ker(Gamma) RS sector; the self-dual SU(2)+ j=1 triplet carrier 192=3x64; the cross-chirality (+96,-96) Krein form; the C-operator eta_+ = eta.C; the RS Dirac symbol M_D; the (9,5)=(3,1)+(6,4) split; the fiber-Clifford-trace standing in for pi_!). Standard-field where the machinery binds any construction (Clifford-contraction; Krein-space K-self-adjoint / K-anti-self-adjoint typing; the sign/signature functional calculus; the chirality-odd => zero-spectral-flow argument). Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md; no cross-repo identity asserted; the reservoir Krein SIGN and the coupling ratio r* remain GATED TI/TaF finality objects (one-way rule respected -- W218 computes only the GU-side operator TYPE, not the sign)."
depends_on:
  - explorations/W201-count-external-datum-characterization-2026-07-14.md
  - explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md
  - explorations/W177-build-connection-curvature-c2-2026-07-14.md
  - explorations/W192-explicit-carrier-kernel-spectral-gate-2026-07-14.md
  - canon/shiab-existence-cl95.md
  - canon/core-theorems-symbolic-proof-RESULTS.md
  - canon/external-by-structure-synthesis-RESULTS.md
  - tests/wave16/H39_sourceaction_kclass.py
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W218_lean_Rsrc_unification_check.py
cross_repo:
  - "time-as-finality / temporal-issuance: W201 named the one open computation (Sec 6) that would settle whether the count's chiral projection is LITERALLY the operative C-operator whose SIGN is the reservoir/finality datum #1. W218 runs it (ultralocally) and returns DISTINCT: the source operator R_src is NOT the C-operator eta_+=eta.C -- it is the K-null / index-conserving type. So the count and the finality sign do not even share the LITERAL operator, only the arena (both K-self-adjoint chirality-odd on the same carrier). This TIGHTENS W201's 'shared as operator' to 'shared arena, distinct operator'. No TI/TaF claim moves; the reservoir SIGN and r* stay TI/TaF-owned; one-way rule respected."
---

# W218 -- LEAN check: is the generation-count operator the same object as eta_+ = eta*C?

**Role and charge.** W201 typed the external generation-count datum and its relation to the reservoir
Krein-sign datum, and named exactly one open computation (its Section 6): build the twisted
Rarita-Schwinger Y14-fiber source re-grading `R_src` on the cross-chirality `(+96,-96)` carrier and
test whether it is *literally* the W173/W186 C-operator `eta_+ = eta . C` (the unitarity / physical-vs-ghost
grading whose sign is the finality datum #1), and whether it chiralizes or stays vectorlike. This LEAN
single-worker check (NOT part of a wave) does that computation directly, in the verified `Cl(9,5) = M(64,H)`
representation, and settles the two decisive tests.

The answer is clean and truth-symmetric: **DISTINCT + VECTORLIKE.** `R_src` is *not* the operator
`eta_+ = eta . C`; it is not even the same operator TYPE (K-null vs K-definite); and it does not chiralize
the carrier. Deterministic test `tests/W218_lean_Rsrc_unification_check.py`, 21/21, exit 0, positive
controls first.

## 1. The explicit carrier and the two objects being compared

The `(+96,-96)` cross-chirality carrier is not treated symbolically here (as
`canon/core-theorems-symbolic-proof` does) but built EXPLICITLY as the object
`tests/wave16/H39` already exhibits: inside `ker(Gamma)` (dim 1664) the top-Casimir eigenspace of the
self-dual `SU(2)+` triplet is the `j=1` carrier `W`, dimension `192 = 3 x 64` (`3 = dim Lambda^2_+(R^4)`,
Casimir 8.0). On `W`:

- the chirality involution `omega_c` (from `kron(I_14, omega_S)`) has signature `(96,96)` (`W_+ = W_- = 96`);
- the Krein form `K_c` (from `kron(diag(eta), K_S)`, `K_S = e_0...e_8`) has signature `(96,96)` and is
  **cross-chirality**: `K_c omega_c + omega_c K_c = 0` to `1e-15`. This is precisely the paper's carrier.

The **unitarity grading** `eta_+ = eta . C`: take `eta = K_c` and `C = sign(K_c)` (the C-operator, the
fundamental symmetry that makes the Krein form definite, W173/W186). Then `eta_+ = K_c . C = |K_c|` is
positive-definite `(192,0)`. The C-operator `C` is **chirality-ODD** (`{C, omega_c} = 0`), **K-DEFINITE**
(`sig(K_c C) = (192,0)`), and **commutes with the Krein form** (`[C, K_c] = 0`). This is the
"K-definite non-chirality re-grading" W201 Sec 6 asks about.

## 2. Building R_src (the fiber-Clifford-trace pushforward, RS channel)

The Section-6 object is

```text
R_src = Pi_RS ( sum_{a in (6,4) fiber} c(e^a) M_D c(e_a) ) Pi_RS   |_carrier
```

with `M_D = kron(I_14, c(xi))` the RS Dirac symbol (W177/W203), `c(e^a) = kron(I_14, e_a)` Clifford
multiplication on the spinor factor (`e^a = eta[a] e_a`), `Pi_RS` the projector onto `ker(Gamma)`, and the
sum over the `(6,4)` fiber directions of the `(9,5) = (3,1) + (6,4)` split (`HIDX = (0,1,2,9)`). The
fiber-Clifford-trace is the **ultralocal algebraic pushforward** standing in for the geometric `pi_!` that
W201 / located-not-forced hold undefined over the non-convex `GL(4,R)/O(3,1)` fiber -- so the whole result
is ULTRALOCAL by construction, and honestly labelled so.

The **RS channel is fixed** (SHIAB-03: the shiab family has a Clifford-trace `S+` channel and a
Rarita-Schwinger `omega_1 + omega_6` channel) by restricting to the `ker(Gamma)` gamma-traceless triplet
carrier; the Clifford-trace `S+` channel is carried as the pre-declared DISQUALIFYING control (Section 5).

## 3. The two type reads

Two one-shot reads classify `R_src` (a `192 x 192` operator on the carrier):

- **Chirality-commutation.** `{R_src, omega_c} = 0` to `8e-15` (and `[R_src, omega_c] != 0`): `R_src` is
  **chirality-ODD**.
- **Krein-adjointness.** `R_src^dag K_c - K_c R_src = 0` to `8e-15` (the `+` residual is order `||R_src||`):
  `R_src` is **K-SELF-adjoint** -- the same Krein type as the C-operator, so the two DO share the operator
  arena (K-self-adjoint, chirality-odd, on the same carrier).

The decisive discriminator between the two candidate types must avoid the ill-conditioned matrix-sign of
the highly non-normal `R_src` (`||R_src - R_src^dag|| ~ 700`; a naive `signm`/eigenvector sign is numerically
unreliable here). The **stable** discriminator is the signature of the Hermitian matrix `K_c R_src`
(Hermitian because `R_src` is K-self-adjoint):

```text
K-definite   sig(K_c R_src) = (192, 0)   <->  eta_+ = eta*C type
K-null/indef sig(K_c R_src) = (96, 96)   <->  net index 0 -> vectorlike
```

Computed: `sig(K_c R_src) = (96, 96)`. `R_src` is the **K-NULL / K-indefinite** type -- NOT the
C-operator's K-definite `(192,0)`. And structurally, `R_src`'s chirality-diagonal blocks vanish
(`||W_+^dag R_src W_+|| = ||W_-^dag R_src W_-|| ~ 3e-15`): `R_src` is purely chirality-OFF-DIAGONAL, the
Theorem-3 form `D = [[0, B],[B', 0]]`.

## 4. The two tests

**TEST 1 (unification): DISTINCT.** `R_src` is Frobenius-ORTHOGONAL to `C = sign(K_c)` -- the best-fit
scalar `c` in `R_src ~ c C` is `~ 1e-16`, residual = full norm. `sig(K_c R_src) = (96,96)` (K-null) is not
`eta_+`'s `(192,0)` (K-definite). And `[R_src, K_c] != 0` (`1.41 ||R_src||`) while `[C, K_c] = 0`. So
**`R_src` is not the operator `eta_+ = eta . C`, up to the C-positive stabilizer or any scalar** -- it is not
even the same operator type. This settles W201 Sec 6's identity question in the **negative**: the count's
chiral projection is NOT literally the operative C-operator; the two external datums **share the arena
(K-self-adjoint chirality-odd on the carrier) but not the operator**. This is CONDITIONAL on the RS-channel
fixing (the ker-Gamma triplet-carrier restriction standing in for the SHIAB-03 intertwiner selection); it is
robust across the fiber / all-14 / no-Pi / horizontal channels computed here.

**TEST 2 (chiralize vs vectorlike): VECTORLIKE.** The net chiral index
`chi = tr(omega_c . sign(R_src)) = 0`, and this is **forced exactly**, not merely measured: since
`{R_src, omega_c} = 0` and `sign` is an odd function, `omega_c sign(R_src) omega_c = sign(-R_src) =
-sign(R_src)`, so `tr(omega_c sign(R_src)) = -tr(omega_c sign(R_src)) = 0` (core-theorems Theorem 3). The
machine-exact witness is the vanishing chirality-diagonal blocks of Section 3 (a `[[0,B],[B',0]]` operator
has chirality-balanced positive/negative spectral subspaces). This is **channel-type-invariant** -- every
channel variant gives the same vectorlike result. So even had the arena-sharing risen to a literal identity,
the shared operator would still not deliver a count: `R_src` conserves the net chiral index at 0. A
**separate, CRT-disjoint `Z/3` self-dual import** is still required (exactly W201's coherence gap, now
confirmed on the explicit `R_src`, and consistent with `external-by-structure`: any odd count is an external
topological / self-dual-flux index, not an interior Krein-isometric datum).

## 5. Controls and honesty

- **Channel robustness.** The full-Clifford-trace (all 14), no-`Pi` ambient, and `(3,1)`-horizontal channels
  each reproduce: chirality-odd, `sig(K_c R) = (96,96)` K-null, vanishing diagonal blocks, `R perp C`. Both
  tests are robust here (test-2 as required; test-1 more robust than the honesty caveat demands).
- **Clifford-trace disqualifier.** The pure Clifford trace `sum_a e^a c(v) e_a` of a single gamma stays
  proportional to that gamma (`= -12 c(v)`, residual 0): the `S+` Clifford-trace channel is chirality-odd and
  K-self-adjoint but structurally cannot produce the K-definite `eta_+ = eta*C` grading -- consistent with
  SHIAB-05 (`dim Hom(S+ (x) S+, Lambda^0) = 0`).
- **What is NOT claimed.** ULTRALOCAL: the fiber-Clifford-trace is a stand-in for the geometric `pi_!`; the
  nonlocal `Z_U` completion is untouched. No `Z/3` count VALUE, no Krein SIGN for GU, no reservoir bit. No
  canon / RESEARCH-STATUS / claim-status / verdict / posture change; `bar(b)` and `H59` stay OPEN; the count
  stays `{1,3}`. The result is the unification bit (DISTINCT) and the chiralize/vectorlike bit (VECTORLIKE),
  nothing more.

## 6. What this settles toward the program

W201 held open, as its single settling computation, whether the count's source operator IS the C-operator.
W218 answers: **no, not even as the same operator type.** The honest tightening of W201's headline is:

> The count-external datum and the reservoir/finality Krein-sign datum share the OPERATOR ARENA
> (K-self-adjoint, chirality-odd, on the cross-chirality `(+96,-96)` carrier) but they do NOT share the
> operator: the source operator `R_src` is K-NULL / index-conserving, the C-operator is K-DEFINITE. So even
> favorably resolving the finality sign #1 (switching on the C-operator) does not populate the count with the
> source operator's chirality -- `R_src` is vectorlike, and the count remains a second, separate `Z/3`
> self-dual import. The "operator-level unification" W201 flagged as the only available one is, on this
> ultralocal computation, NOT realized.

**Artifacts:** this file + `tests/W218_lean_Rsrc_unification_check.py` (21/21, exit 0).

*Filed 2026-07-14. LEAN single-worker check (not a wave). Coherence-first; exploration grade; conditional
register; truth-seeking (a clean DISTINCT is as informative as a coincidence); RUTHLESS skeptic. No
sub-agents. Reproducible: `python -u tests/W218_lean_Rsrc_unification_check.py` (21/21, exit 0; positive
controls first). No canon movement; bar(b) and H59 remain OPEN.*
