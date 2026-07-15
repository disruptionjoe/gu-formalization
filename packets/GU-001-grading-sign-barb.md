# GU-001 -- grading-sign / bar (b) founding-case packet (human-readable companion)

Companion to `packets/GU-001-grading-sign-barb-v0.2.json` (Frozen-Packet Contract v0.2).
This document is a reader's guide; the JSON is authoritative. Packaging only: no GU
verdict, claim status, canon, bar (b), H59, or count is moved. Zero em dashes.

## What GU-001 is

The origin object of the Possibility-to-Capability interface: the grading-sign /
bar (b) founding case. Take the good-stable fixed point as GIVEN (real total spectrum;
positive-definite total metric `eta_+ = eta.C`; C-operator operative). GU-001 asks whether
the C-operator grading SIGN (whether the record-count mode is Krein-negative on the (6,4)
DeWitt fiber, equivalently whether the interacting C-operator is operative so `eta_+ = eta.C`
is the physical positive-definite inner product, which is exactly bar (b)) is FORCED inside
GU or is a residual Z/2 that must be posited.

GU-002 (the good-stable no-go) builds downstream of this object; GU-001 is UPSTREAM of GU-002.

## Pinned source revision

- Repository: `gu-formalization`
- Revision: `d62a82f3a74731b322a5d65b5ee15a2b861e2855`
- All manifest `content_sha256` values are computed from the committed git-object bytes
  (`git show HEAD:<path>`), not the working tree, so the bundle is reproducible cross-platform
  (repo `core.autocrlf` is on).

## The Schur-forced action and the signature decoupling (context, W202 / W203)

- W203 (Schur-forced action): the branch-3 source action is BUILT and its relative coefficients
  are FORCED. Equivariance under the Krein-anti-self-adjoint gauge action pins the kernel by Schur
  to a one-dimensional space (`nulldim = 1`) whose generator is the Clifford metric `eta`
  (signature (9,5), indefinite). The sole undetermined number is the overall scale `kappa`
  (Newton's G), undetermined by normalization, not fitted.
- W202 (signature decoupling): the reservoir Krein sign is computed on the DeWitt (6,4) fiber,
  which is invariant under `eta -> -eta`, so the sign is IDENTICAL on (9,5) and (7,7) and is
  DECOUPLED from the still-under-determined signature choice.

## The binary grading datum

Everything the program needs for unitarity of the good stable reduces to ONE bit: the C-operator
grading SIGN. Conditioning on the good stable (preserving both the indefinite `eta` and the
positive-definite `eta_+ = eta.C`) forces admissible deformations to commute with `C = sign(eta)`,
so the stabilizer is the C-commutant = maximal compact SO(9)xSO(5). Under it the 14-frame is
reducible (`R^9 (+) R^5`), so the invariant-symmetric-form space GROWS from 1 to 2 (basis
`{eta, eta.C}`). The relative record-count block sign is a FREE Z/2. Symmetry reduction LIBERATES
the sign; it does not force it.

## The five methods and their grades

All five are exploration-grade and machine-checked; every per-method grade is copied verbatim in
the JSON `method_ledger`. Each reproduces the W203 `nulldim = 1` guardrail as a positive control.

| method | route | test | verdict |
|---|---|---|---|
| W206 (R16) | counterfactual-invariance (Klein/Erlangen: metric from its stabilizer) | 29/29 exit 0 | RESIDUAL-BIT-STANDS |
| W207 (R9)  | Dirac-BRST / constraint cohomology (physical inner product on H^0(Q)) | 31/31 exit 0 | RESIDUAL-BIT-STANDS |
| W208 (R7)  | Lawvere / Cantor diagonal fixed point | 31/31 exit 0 | RESIDUAL-BIT-STANDS |
| W209 (R12) | topos internal logic / sheaf semantics | 32/32 exit 0 | RESIDUAL-BIT-STANDS |
| W210 (R1)  | Helmholtz inverse problem of the calculus of variations | 32/32 exit 0 | RESIDUAL-BIT-STANDS |

Joint argument / synthesis: W211 (`tests/W211_five_method_convergence.py`, exit 0).

## bar (b) status (copied from the source)

bar (b) does NOT self-clear. This is LOCATED-NOT-FORCED at the deepest level: the central unitarity
bit is fully LOCATED (one Z/2, exact fiber location) but GU cannot FORCE it. bar (b) UNCHANGED /
OPEN; H59 OPEN; count `{1,3}`; no canon movement. Two honest paths remain and only two: (a) obtain
the sign externally from TI / time-as-finality (now proven necessary, not merely convenient), or
(b) posit a Krein-positivity axiom and state GU's result conditionally. "Compute harder inside GU"
is ruled out by the convergence.

## The five-method independence typing (the crux)

`raw_method_count = 5`; `raw_method_count_is_independence_count = false`. Convergence is NOT
independence. The five methods share ALL load-bearing premises:

- `P-SCHUR-ETA` -- W203's Schur-forced ungraded `eta` / `nulldim = 1` guardrail;
- `P-STABILIZER-LIBERATION` -- the good-stable stabilizer = C-commutant = maximal compact
  SO(9)xSO(5) that liberates the invariant-form space from 1 to 2;
- `P-FIBER-KREIN` -- the (6,4)-fiber geometric-positive / record-count-negative Krein split;
- `P-CL95-REPCANON` -- the Cl(9,5)=M(64,H) rep-canonicity caveat;
- `P-EXTERNAL-C-OPERATOR` -- the single external Z/2 posit (the unbuilt interacting C-operator /
  C2-closing Y14-curvature spectral section) that every method reduces to.

`shared_load_bearing_premise_ids` therefore equals all five premise IDs: the methods are NOT five
independent evidential units. There are no method-to-method dependency edges; the coupling is
entirely through the shared premises. The source records the convergence as "unanimous" (5/5
RESIDUAL-BIT-STANDS), which is copied as `convergence = "unanimous"`; independence is typed
separately as `independence_type = "proof_theoretic_independence"` (the source's own
Godel-independence characterization of the RESULT: the sign is true in the good model and false in
the pathological model of the same self-consistency theory), never as an evidential-independence
count of the five methods.

One-line typing used: five methodologically distinct routes reaching one unanimous
RESIDUAL-BIT-STANDS by dependence-driven shared-premise convergence (all five share every
load-bearing premise and reduce to one external Z/2 posit), NOT five independent evidential units;
`raw_method_count = 5`, `raw_method_count_is_independence_count = false`.

## TI / TaF boundary fields

The `interfaces` block requests a typed interface to `time-as-finality` for the
finality-reservoir metric signature / interacting-C-operator activation (the single external Z/2).
These boundary fields are GU-side descriptions and typed-interface requests only. NO TI/TaF or
cross-repository identity is asserted; the datum stays gated.

## Three digests (canonical `ptc-frozen-bundle-v1`)

- `manifest_digest` : `964f398f3292c96e649a84477f75e4734c564507e2402c7bfcb29ca852c42562`
- `packet_digest`   : `a3f7fc5d99f3810ad86b783365e130749d137e227e6ac97021c26a54a9fff1be`
- `bundle_digest`   : `ab64dbeaf3c949d84bfb39ce19afc2c259164535698c5f09c44e75465a23bc30`
  (equals `integrity.digest`, the v0.1-compatible alias)

## Honest residuals

- bar (b) and H59 OPEN and Joe-gated; count `{1,3}`; no debit added or cleared.
- The interacting C-operator / C2-closing spectral section is UNBUILT; the C-positive pin uses a
  proxy (the +1 eigenspace of the Hermitian Krein form K_S).
- The overall scale `kappa` is undetermined by normalization (not fitted); the nonlocal `Z_U`
  completion is unbuilt (W203 is ultralocal).
- The STRUCTURAL lifts are faithful finite renderings, not full M(64,H) recomputations.
- The Cl(9,5)=M(64,H) rep-canonicity caveat stands; the (9,5)/(7,7) signature is UNDER_DETERMINED.
- The branch-3 action still assumes the W154 marble/wood identification, localized through `J`.

## Verification status

Internal-tier: five deterministic machine regressions (all exit 0, positive controls first) plus
the W211 convergence certificate. No independent external replication and no Lean/Lake build was
run; issued at exploration-grade interface per the GU-001 issuance plan. p2c runs its own gates and
owns any receiving-independence assessment (it may preserve the source type or weaken it to
`unknown_or_contested`, never strengthen it).
