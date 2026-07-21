---
artifact_type: exploration
status: exploration (W202; TEAM SIGNATURE-CRUX-BACH; five personas inline, one worker, no sub-agents; deterministic test, exit 0, positive controls first)
created: 2026-07-14
wave: W202
label: W202
posture: coherence-first (Joe 2026-07-14); exploration grade; conditional register; truth-seeking (report value under either outcome); RUTHLESS self-verification; tri-repo gating STRICT
title: "W202 -- the (9,5)-vs-(7,7) signature crux, the Bach-branch strong-field gravity test, and the DECOUPLING of the reservoir Krein sign (#1) from the signature choice. THREE RESULTS. (a) SIGNATURE: confirmed UNDER_DETERMINED (building on the 2026-07-04 BIG-SWING), sharpened -- the sole lever is the base Lorentzian convention sign(d), d = #space - #time, via the closed form p-q = d + d^2/2 (d=+2 -> (9,5)/M(64,H)/J^2=-1; d=-2 -> (7,7)/M(128,R)/J^2=+1); the three candidate GU-internal selectors the charge names all FAIL to fire as selectors: the SM/generation spinor content is a signature-relative FILTER not a selector (SG1: even-parity wall is (9,5)-specific; (7,7) removes the obstruction but does not supply 3), the finality frontier (q=5 vs q=7) is a TaF-gated interpretation, and the Cartan involution is DOWNSTREAM of p-q (circular, same status as J). (b) BACH BRANCH: the Schwarzschild/Kerr Bach-flatness (H1) is GENERIC to any conformal (Weyl^2) gravity -- Einstein => Bach-flat is a theorem true of every Einstein vacuum, NOT a GU-specific cancellation; the GU-specific content is entirely OQ2-A (is GU's functional the conformal/Bach-Willmore combination), and W161 shows GU's actual April-2021 law is LINEAR in curvature (c_R=0), so Bach is the induced |II|^2 SHADOW branch, not the law. (c) THE #1 BIT: the W168 relative Krein signature (record-count/conformal NEGATIVE vs geometric/graviton POSITIVE = OPPOSITE) is computed on the DeWitt fiber (6,4), which is INVARIANT under eta -> -eta (the DeWitt form is quadratic in eta^-1); hence the reservoir Krein sign is IDENTICAL on (9,5) and (7,7) and is DECOUPLED from the signature crux. NET FOR #1: fixing the signature does NOT fix or move the reservoir Krein sign, and resolving #1 does NOT require resolving the signature -- the single most decisive bit is ROBUST to the entire (9,5)/(7,7) ambiguity. Deterministic test tests/W202_signature_crux_bach_branch.py, 22/22 exit 0, positive controls first."
grade: "exploration / strong on (a) and (c) (both are exact linear-algebra + arithmetic facts, machine-checked), structural on (b) (genericity is a cited theorem of conformal gravity plus the W161 linear-law fact). COMPUTED (tests/W202_signature_crux_bach_branch.py, 22/22 exit 0): PC1 the (9,5)/(7,7) arithmetic and the q=5/q=7 frontier; PC2 the BIG-SWING closed form p-q=d+d^2/2 for d=+-2; PC3 the W168 conformal flip G(eta,eta)=-4 at source-native lambda=1/2 on the (6,4) fiber. NEW-DERIVED: A1 the DeWitt fiber Gram matrix is BYTE-IDENTICAL for eta and -eta (full 10x10 symbolic zero-difference); A2 fiber signature (6,4) for BOTH base conventions; A3 the total (9,5)/(7,7) split comes only from the base (3,1)/(1,3) pullback; B1-B3 the per-block Krein signs (conformal NEG, graviton POS, ADM shift NEG) identical on both signatures; B4 the DECISIVE invariance -- relative Krein signature OPPOSITE (-1) and IDENTICAL across the crux; C1 the algebraic Bach term R^{cd}C_{acbd}=0 for any Einstein metric (generic); C3 the W161 linear-law c_R=0. CITED (not re-derived): BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED (the four GU-native angles, the closed form, the fiber invariance), W168 (the block Krein signs on the (6,4) fiber), H1/tests/wave1/H1_bach_flat_exact_vacua.py (exact Schwarzschild Bach=0 all orders, Kerr Ricci-flat), W161 (GU's linear action), SG1/sg1_signature_carrier_parity_77.py (the C-07 wall dissolves on (7,7)). No canon / RESEARCH-STATUS / claim-status / verdict / posture change; the debit count is unmoved; no forbidden target {3,8,24,chi(K3),Ahat} assumed or inserted. Zero em dashes."
construction: "program-native where the objects are GU's (Y14=Met(X4), the gimmel/DeWitt vertical fiber metric, its signature (9,5)=(3,1)+(6,4) or (7,7)=(1,3)+(6,4), the O(3)xO(1) isotypic split of Sym^2(T*X4), the record-count/conformal and geometric/graviton modes, the q-frontier). Standard-field where the machinery binds any construction (real Clifford / Bott periodicity fixing J^2 from p-q mod 8; the DeWitt supermetric and its conformal-mode sign; the Einstein-implies-Bach-flat theorem of conformal gravity; the Cartan involution of a real form). Every analogy PORTED and labelled; none asserted of GU. Forks named per GEOMETER-VS-PHYSICS-OBJECTS.md. Tri-repo gating STRICT: the signature and the fiber Krein signs are computed GU-side; only the finality INTERPRETATION (whether the Krein grading is physically operative, and whether the finality frontier fixes q) is flagged TaF-owned; NO cross-repo identity asserted."
depends_on:
  - explorations/big-swing-2026-07-03/BIG-SWING-signature-9-5-vs-7-7-UNDER-DETERMINED.md
  - explorations/W168-reduction-krein-signature-2026-07-14.md
  - explorations/W161-lens-foundational-action-2026-07-14.md
  - explorations/wave1/H1-gravity-shadow-bach-branch-2026-07-11.md
  - explorations/sequential-goals-2026-07-09/SG1-signature-carrier-parity-77.md
  - explorations/willmore-residual-computed-and-buildbench-reconciliation-2026-07-11.md
  - canon/no-go-quaternionic-parity-generation-sector.md
  - canon/w2-y14-spin-structure.md
  - GEOMETER-VS-PHYSICS-OBJECTS.md
scripts:
  - tests/W202_signature_crux_bach_branch.py
external_refs:
  - "DeWitt, Phys. Rev. 160 (1967) 1113 -- the supermetric on the space of metrics; the conformal-mode sign"
  - "Bach, Math. Z. 9 (1921) 110 -- the Bach tensor; conformal (Weyl^2) gravity"
  - "Riegert, Phys. Lett. A 105 (1984) 110 -- Einstein metrics are vacua of conformal Weyl gravity (Bach-flat)"
  - "Besse, Einstein Manifolds (Springer 1987) Sec 1.G, 4.76 -- Sym^2 isotypic decomposition; Bach tensor of Einstein metrics"
  - "Cartan / Helgason, Differential Geometry, Lie Groups, and Symmetric Spaces (1978) -- real forms and Cartan involutions of so(p,q)"
---

# W202 -- the signature crux, the Bach branch, and why the reservoir Krein sign does not care

## 0. The charge and the three-line answer

Three swings, one worker, five personas inline. The charge: resolve or sharply advance (9,5) vs (7,7),
run the Bach-branch strong-field gravity test, and say how the signature choice fixes or constrains the
reservoir Krein sign (the #1 cross-repo bit). The answers:

1. **Signature: UNDER_DETERMINED, sharpened.** No GU-native structure fixes it. The sole lever is the
   base Lorentzian convention `sign(d)`, `d = (#space - #time)` in the base, through the closed form
   `p - q = d + d^2/2`: `d = +2` (mostly-plus (3,1)) gives (9,5)/`M(64,H)`/`J^2=-1`; `d = -2`
   (mostly-minus (1,3)) gives (7,7)/`M(128,R)`/`J^2=+1`. This confirms the 2026-07-04 BIG-SWING; my
   contribution is to test the three candidate selectors the charge names and show each fails to fire.

2. **Bach branch: the clearance is GENERIC, not GU-specific.** H1 computed that exact Schwarzschild is
   Bach-flat at all orders and Kerr is Ricci-flat. But `Einstein => Bach-flat` is a theorem of any
   conformal (Weyl^2) gravity, true of every Einstein vacuum. So the Schwarzschild/Kerr cancellation
   does NOT distinguish GU from generic Weyl^2 gravity. The GU-specific question is entirely OQ2-A --
   is GU's functional the conformal/Bach-Willmore combination -- and W161 shows GU's actual law is
   LINEAR in curvature (`c_R = 0`), so Bach is the induced `|II|^2` SHADOW branch, not the law.

3. **The #1 bit is DECOUPLED from the signature.** The W168 relative Krein signature
   (record-count/conformal NEGATIVE vs geometric/graviton POSITIVE = OPPOSITE) is computed on the
   DeWitt fiber (6,4), and the DeWitt fiber metric is INVARIANT under `eta -> -eta` (it is quadratic in
   `eta^-1`). So every block Krein sign, and the decisive relative sign, is IDENTICAL on (9,5) and
   (7,7). Fixing the signature neither fixes nor moves the reservoir Krein sign; resolving #1 does not
   require resolving the signature. The single most decisive bit is ROBUST to the whole ambiguity.

Deterministic test `tests/W202_signature_crux_bach_branch.py`, 22/22 exit 0, positive controls first.

## 1. Construction forks (GEOMETER-VS-PHYSICS-OBJECTS.md), named

| Object | Construction used | Why |
|---|---|---|
| Total space / fiber | `Y14 = Met(X4)`, fiber `Sym^2(T*X4)`, gimmel/DeWitt vertical metric | GU's verified object (W131; canon/w2-y14). |
| Signature | (9,5)=(3,1)+(6,4) or (7,7)=(1,3)+(6,4) | the DECLARED base convention selects between them (C-04). |
| Real form / J | `M(64,H)` (`J^2=-1`) vs `M(128,R)` (`J^2=+1`) | fixed by `p-q mod 8` via real Clifford / Bott periodicity. |
| Krein modes | conformal/record-count (full-trace) vs geometric/graviton (`Sym^2_0(R^3)` TT) | W130/W168; the #1 relative sign lives here. |
| Gravity functional | the conformal/Bach-Willmore combination vs the linear shiab-Einstein law | H1/W161 fork (OQ2-A: is GU's functional Bach?). |
| Finality frontier | q=5 (under (9,5)) or q=7 (under (7,7)) | GATED to TaF; not used to select the signature here. |

## 2. Persona 1 (differential geometer): the Cartan involution and where the signature actually enters

The two candidates are distinct real forms of `so(14,C)`: `so(9,5)` has maximal compact
`so(9) (+) so(5)` and Cartan involution `theta_{95}`; `so(7,7)` has maximal compact `so(7) (+) so(7)`
and involution `theta_{77}`. It is tempting to hope the Cartan involution is a GU-native selector.
It is not: the Cartan involution of `so(p,q)` is `theta(X) = -X^T` in the orthonormal frame of the
form of signature `(p,q)`, i.e. it is DEFINED by the signature. Using it to pick the signature is the
same circularity the BIG-SWING flagged for `J` (`J` is the consequence of `p-q=4`, not its cause) and
that the reconstruction pipeline hardcodes as `eta = [1]*9 + [-1]*5`. The involution, the antiunitary
`J`, and the reality class `M(64,H)` vs `M(128,R)` are all DOWNSTREAM of `p-q mod 8`; none of them can
seed it.

The single point of entry (BIG-SWING, from `shiab-existence-cl95.md` Step 1) is: base `(3,1)` or `(1,3)`
tautological pullback, plus fiber `Sym^2(T*X4)` with the trace-reversed DeWitt form. The fiber is the
same object for both base conventions, so the entire crux is `sign(d)`. My test reproduces the closed
form `p-q = d + d^2/2` (PC2) and the base/fiber split (A3): `(6,4) + (3,1) = (9,5)`,
`(6,4) + (1,3) = (7,7)`.

## 3. Persona 2 (GR/gravity): the Bach test, and why the strong-field clearance is generic

H1 (`tests/wave1/H1_bach_flat_exact_vacua.py`, exit 0) is a real, strong-field computation: on exact
Schwarzschild the divergence of the Weyl tensor is identically zero at all orders in `M` while the Weyl
tensor itself is nonzero, so the full nonlinear Bach tensor vanishes; Kerr is Ricci-flat hence
Bach-flat. That decisively clears the strong-field wall that BLOCKED the Willmore-only branch. I do NOT
re-derive it; I build on it and ask the skeptic's question: is this GU-specific?

It is not. `Einstein => Bach-flat` is a theorem of any conformal (Weyl^2) gravity: for `Ric = Lambda g`,
the algebraic Bach term `R^{cd}C_{acbd} = Lambda g^{cd}C_{acbd} = 0` because Weyl is totally trace-free,
and for Ricci-flat metrics `div-Weyl = 0` as well (Cotton = 0 via `Schouten P = 0`). Every Einstein
metric is a vacuum of conformal Weyl gravity (Riegert 1984; Besse 4.76). My test verifies the algebraic
piece symbolically for a generic trace-free Weyl-type tensor contracted against a pure-trace Ricci (C1):
it vanishes identically, metric-agnostically. So the Schwarzschild/Kerr clearance is inherited from a
generic conformal-gravity fact and does NOT by itself distinguish GU from any Weyl^2 theory.

The GU-specific content is therefore entirely in the trace/conformal sector -- exactly where H1 PART 4
found Bach and the naive `|H|^2`-Willmore operator DIFFER -- i.e. in the single datum OQ2-A: is GU's
functional the conformally-invariant Willmore (Bach) combination? And W161 sharpens the stakes: GU's
ACTUAL April-2021 action is LINEAR in curvature (shiab-projected Einstein), whose covariant scalaron
coupling is `c_R = a + b/3 + c/3 = 0` (all curvature-squared coefficients zero; test C3). A linear law
is second-order Einstein, NOT fourth-order Bach. So the Bach reading is the INDUCED `|II|^2` shadow
branch (H1's PART 4 / W161's branch A), not GU's law. The honest Bach-branch verdict:

- The strong-field cancellation is REAL but GENERIC (any conformal gravity clears exact vacua).
- Whether GU IS in the Bach branch is the unresolved OQ2-A / shadow-vs-law fork, and at the LAW level
  GU is linear (no Bach mode). The Willmore-residual note (2026-07-11) already localizes the residual
  imbalance to `O(M^1)` for the `|II|^2`-class and `O(M^2)` (self-closing) for the `|H|^2`-conformal
  class, welding the functional choice to the theta-sector -- consistent with this reading.

Information value under either outcome: if GU's functional IS conformal/Bach, gravity clears (generic
theorem, plus a real ghost/unitarity cost inherited from conformal gravity, H1 note); if GU's law is
the linear shiab-Einstein, there is no Bach mode and the whole question is moot at the law level. Either
way the Bach clearance is NOT evidence FOR GU specifically -- a clean, non-rooting negative.

## 4. Persona 3 (rep-theorist): does the Standard-Model / three-generation content select the signature?

This is the charge's sharpest candidate selector, and the answer is a clean, asymmetric NO.

SG1 (`sg1_signature_carrier_parity_77.py`, exit 0) computed the C-07 quaternionic-parity no-go on BOTH
signatures with bit-exact certificates: on (9,5)/`M(64,H)` (`J^2=-1`) Kramers forces every GU-native
self-adjoint carrier to have EVEN signature, so an odd generation index (3) is native-OBSTRUCTED; on
(7,7)/`M(128,R)` (`J^2=+1`) Kramers is inactive and a genuine rank-3 J-commuting projector exists, so 3
is native-ADMISSIBLE. So the generation-parity structure is SIGNATURE-RELATIVE: it is a filter INSIDE a
chosen class, not a selector BETWEEN classes.

The asymmetry is the sharp part. If one imposes as a physical INPUT that three generations must arise
NATIVELY (as a forced GU-internal integer, not a declared choice), then only (7,7) is compatible -- the
generation content would point to (7,7). But canon holds the generation count as LOCATED, NOT FORCED
(C-06 under-determination; SG1 qualifier 1: (7,7) removes the obstruction, it does not supply 3). Since
the count is not forced, it does not force the signature either. So the SM/generation content does NOT
select (9,5): the perturbative anomaly at `D=14` is order `Tr F^8` (even Casimir, reality-class-blind,
BIG-SWING Angle 1), chirality exists in both (both `q` odd), and the 16-state hypercharge content
embeds identically. The only GU-internal asymmetry between the two signatures is the generation-parity
wall, and it is a conditional-on-(9,5) theorem, not a selector.

Rep-theorist verdict: the spinor/SM content is signature-AGNOSTIC except for the parity wall, which is
signature-relative and does not fire as a selector while the count stays located-not-forced.

## 5. Persona 4 (synthesizer): mapping the signature choice onto the q=5 relative Krein sign (#1)

Here is the load-bearing new computation. The reservoir Krein sign #1 is the relative Krein signature of
the record-count/conformal mode vs the geometric/graviton mode (W168). W168 computed it on the gimmel
DeWitt fiber and got OPPOSITE (conformal NEGATIVE, graviton POSITIVE). The question the charge poses: does
fixing (9,5) vs (7,7) fix or narrow this?

**It does neither, because the two modes and their DeWitt norms live entirely in the fiber, which is
convention-invariant.** The DeWitt vertical metric is
`G_lambda(S,T) = tr(eta^-1 S eta^-1 T) - lambda (tr_eta S)(tr_eta T)`. It is QUADRATIC in `eta^-1`: under
`eta -> -eta`, `eta^-1 -> -eta^-1`, the first term is invariant (two factors) and each `tr_eta` picks up
a sign that cancels in the product. So `G_lambda` is exactly invariant under the base-sign flip. My test
proves this at the level of the FULL `10x10` Gram matrix (A1: byte-identical for `eta` and `-eta`), and
the consequences:

- fiber signature (6,4) for BOTH conventions (A2);
- conformal/record-count mode `G(eta,eta) = 4 - 16 lambda = -4 < 0` at source-native `lambda=1/2`
  (Krein-NEGATIVE) on BOTH (B1);
- geometric/graviton `Sym^2_0(R^3)` mode POSITIVE on BOTH (B2);
- ADM shift block NEGATIVE on BOTH (B3);
- **relative Krein signature = OPPOSITE (product `-1`), IDENTICAL on (9,5) and (7,7)** (B4).

So the map from the signature choice to the #1 bit is CONSTANT. The base convention moves the total
signature (9,5) <-> (7,7) and the reality class `M(64,H)` <-> `M(128,R)` (which governs the generation
parity wall), but it does NOT touch the fiber isotypic Krein signs on which #1 rides. The q=5 vs q=7
frontier LABEL changes (the frontier is the negative-directions count), but the RELATIVE sign of the two
physical modes within the fiber does not.

Synthesis verdict: **fixing the signature does not fix or narrow the reservoir Krein sign -- it is
already fixed (OPPOSITE) and is INVARIANT under the crux.** Equivalently, the #1 bit and the signature
crux are ORTHOGONAL: #1 can be resolved (its remaining gate is the ACTIVATION reading -- whether the
indefinite Krein form, not a positive-definite `H_C+` restriction, is physically operative, W168's
TaF-owned residual) without ever resolving (9,5) vs (7,7), and conversely resolving the signature would
give zero new information about #1's sign.

## 6. Persona 5 (skeptic): is the signature genuinely underdetermined, and is the decoupling too cheap?

Two adversarial pushes.

**Is the underdetermination real, or did I just fail to find the selector?** The BIG-SWING already ran
four independent GU-native angles (anomaly-freedom, H-structure/shiab, Clifford reconstruction,
under-determination adversary) all returning UNDER_DETERMINED and surviving adversarial scrutiny; I added
the three the charge named (generation content, finality frontier, Cartan involution) and each fails as a
selector for a distinct reason (filter / TaF-gated / circular-downstream). The honest limit is
unchanged: "no GU selector for `sign(d)`" is an absence-of-forcing argument, not a proof that none could
exist. But the burden is on FORCING, and no forcing is exhibited anywhere in the reconstruction. One
reality-sensitive channel (the 2-primary Witten/Dai-Freed `Z/2`) stays OPEN, and it is ASYMMETRIC -- it
could EXCLUDE the H-class (push toward (7,7)/dissolution), never FORCE it. So the verdict cannot flip
toward FORCES_9_5; at most it could move toward (7,7), which would REOPEN the count -- and that is the
one live way this matters. I do not claim it is closed; I claim (9,5) is not forced.

**Is the decoupling too cheap -- true of any fiber metric?** No. The decoupling is specific to the fact
that the DeWitt form is quadratic in `eta^-1` AND that the #1 modes are fiber-isotypic. A DIFFERENT
gravitational inner product that was LINEAR in the base metric (e.g. a term contracting a fiber tensor
against the base pullback) WOULD carry the base sign and could flip #1. The BIG-SWING's own Angle-4
lever is exactly such a linear-in-`g` object -- the base pullback -- which is why it moves `p-q`. The
content of the result is that #1 lives in the trace-reversed FIBER form (quadratic, sign-blind), not in
the base pullback (linear, sign-carrying). So the decoupling is a genuine structural fact about WHERE the
#1 modes sit, not a triviality. It would BREAK if the reservoir grading were shown to be governed by a
base-index inner product rather than the fiber DeWitt form -- which is exactly the "base-index vs
fiber-index transfer" soft joint W168 flagged (its Section 4, residual 1). That joint is the one place
the decoupling could fail, and it is named, not hidden.

**Is the Bach clearance too cheap?** Yes, and that is the point (Section 3): the strong-field Bach=0 is
generic to conformal gravity, so it is not evidence for GU. The skeptic ENDORSES treating H1 as a
generic-conformal fact, not a GU confirmation, and holds the gravity clearance CONDITIONAL on OQ2-A
(functional identity) and, if the conformal branch is taken, on paying conformal gravity's known ghost /
lensing-sign costs.

## 7. Synthesis -- the return data

| Question | Verdict | Basis |
|---|---|---|
| Is (9,5) forced by GU-native structure? | NO -- UNDER_DETERMINED | BIG-SWING 4 angles + PC2/A3; sole lever is `sign(d)` |
| Does the SM/generation content select it? | NO (asymmetric) | SG1: parity wall is (9,5)-specific; (7,7) admits 3 but count is located-not-forced |
| Does the finality frontier select it? | NO (TaF-gated) | q=5 vs q=7 is the frontier LABEL; the interpretation is TaF-owned |
| Does the Cartan involution select it? | NO (circular) | `theta` and `J` are DOWNSTREAM of `p-q mod 8` |
| Single decisive datum that WOULD fix it | `sign(d)` = mostly-plus vs mostly-minus base convention | closed form `p-q = d + d^2/2`; no GU selector |
| Is Schwarzschild/Kerr Bach-flatness GU-specific? | NO -- GENERIC | C1: `Einstein => Bach-flat` for any conformal gravity; H1 all-orders |
| Is GU's functional the Bach combination? | UNRESOLVED (OQ2-A); LAW is linear (`c_R=0`) | H1 PART 4 + W161/C3 |
| Fiber (6,4) under (9,5) vs (7,7) | IDENTICAL | A1 (Gram byte-identical), A2 |
| record-count/conformal Krein sign | NEGATIVE on both | B1: native `G(eta,eta)=-4` at `lambda=1/2` |
| geometric/graviton Krein sign | POSITIVE on both | B2 |
| relative Krein sign (#1) across the crux | **OPPOSITE, INVARIANT** | B4 |
| Does fixing the signature fix/narrow #1? | NO -- DECOUPLED | B4; DeWitt form quadratic in `eta^-1` |

## 8. What this teaches toward the Krein-sign question (#1)

The parent's #1 decisive bit is the reservoir Krein SIGN -- whether `[P_ghost,S]=0` / the interacting
C-operator exists / the Krein grading is physically operative, the single cross-repo bit that clears or
re-poses bar (b). This swing teaches three things toward it:

1. **The signature crux does NOT gate #1.** The reservoir relative Krein sign is computed on the
   convention-invariant fiber (6,4) and is OPPOSITE on BOTH (9,5) and (7,7) (B4). So the long-standing
   (9,5)-vs-(7,7) ambiguity -- which has sat as a background worry over the whole program -- is
   ORTHOGONAL to #1. #1 can be resolved without touching the signature, and the signature can stay
   declared-not-forced without leaving #1 undetermined. This REMOVES the signature crux from the #1
   critical path. That is the most decision-relevant output: the team can attack #1 directly and ignore
   the signature question for this purpose.

2. **It sharpens WHERE #1's remaining risk actually lives.** #1 is NOT at risk from the signature; the
   SIGN is settled (OPPOSITE) and robust. #1's two genuine remaining gates are exactly W168's named
   residuals: (i) the base-index-to-fiber-index TRANSFER of the fiber Krein sign into the effective
   `(alpha,beta)` shape weights (the ONE place the decoupling could break, because a base-index inner
   product WOULD carry the signature sign), and (ii) the ACTIVATION reading -- whether the indefinite
   Krein form rather than a positive-definite `H_C+` restriction is the operative physical inner product
   (TaF-owned). The #1 question reduces cleanly to these two, with the signature explicitly excluded.

3. **It tells us which further work moves #1 and which does not.** Resolving (9,5) vs (7,7) -- the
   2-primary Witten anomaly, the source-convention question with the author -- gives ZERO new information
   about #1's sign (decoupled). What DOES move #1: building the `I1B -> X4`-shadow reduction map that
   carries the fiber Krein sign through to the `(alpha,beta)` weights (gate i), and the TaF activation
   determination (gate ii). The generation-count / signature line and the #1 line are separate programs;
   this note draws the boundary between them.

Net for #1: the reservoir Krein sign is **OPPOSITE and signature-invariant**; the #1 bit is decoupled
from the signature crux; its residual risk is the base-to-fiber transfer and the finality activation, not
the signature. The single most decisive bit is robust to the entire (9,5)/(7,7) ambiguity.

## 9. Gates and honest limits

- Exploration grade; conditional register throughout. Nothing asserts GU, asserts a vacuum, or changes
  any verdict. All results are computed statements about the DeWitt fiber form, the closed-form
  signature arithmetic, and the generic conformal-gravity Bach fact, with BIG-SWING/W168/H1/W161/SG1
  positive controls -- not assertions about GU.
- The signature verdict remains UNDER_DETERMINED (not FORCES_7_7, not FORCES_9_5); C-04 confirmed; the
  C-07 wall genuinely conditional. The generation count stays LOCATED, NOT FORCED. No canon movement.
- The Bach clearance is generic; it is NOT evidence for GU. The GU-specific gate is OQ2-A, unresolved;
  GU's law is linear (`c_R=0`).
- The decoupling's single failure mode (base-index vs fiber-index transfer) is named, not hidden; it is
  W168's residual 1 and gate (i) for #1.
- Tri-repo gating STRICT: the signature and fiber Krein signs are GU-computed; the finality frontier
  interpretation and the grading ACTIVATION are TaF-owned; no cross-repo identity asserted. No
  RESEARCH-STATUS / claim-status / verdict / posture change; the debit count is unmoved; no forbidden
  target assumed or inserted. Zero em dashes in paper-facing text.

*Filed 2026-07-14 by Team SIGNATURE-CRUX-BACH (W202). Coherence-first; truth-seeking (value reported
under either outcome); RUTHLESS self-verification. Five personas inline in one worker (differential
geometer; GR/gravity specialist; Cl(9,5)/Cl(7,7) rep-theorist; synthesizer; adversarial skeptic); no
sub-agents. Reproducible: `python -u tests/W202_signature_crux_bach_branch.py` (22/22, exit 0; positive
controls first). Exploration grade; conditional register; no canon movement; tri-repo gating strict.
Three results: signature UNDER_DETERMINED (sharpened, three named selectors fail); Bach clearance
GENERIC not GU-specific; the reservoir Krein sign OPPOSITE and DECOUPLED from the signature crux.*
