---
title: "OQ-RK1 Attempt: Target-Independent rank_H(Pi_RS . E_+ . Pi_RS) in M(64,H)"
date: 2026-06-26
problem_label: "oq-rk1-rs-rank-attempt"
status: reconstruction
verdict: BLOCKED_NEEDS_SPEC
verdict_scope: >
  The decisive OQ-RK1 quantity rank_H(Pi_RS . E_+ . Pi_RS) (= 4 => 3 generations,
  = 8 => 4 generations, Candidate B) is NOT computable from current repo data.
  Pi_RS is not pinned down as a concrete operator on S = H^64: the only concrete
  RS object in the repo is the raw 14D gamma-trace kernel projector, which lives on
  the 896_H vector-spinor space (M(896,H)), not on S = H^64, and has rank_H = 416
  (NOT 4, NOT 8). The effective/physical projector E_RS^eff that would yield 4 or 8
  is undefined (gauge/BRST quotient + K-theory symbol class + ch_2(F) + H-trace +
  Y14->K3 bridge all missing). E_+ alone IS pinnable (rank_H = 32, verified by
  explicit matrix computation). No fabricated rank is produced.
executable:
  - tests/oq_rk1_cl95_explicit_rep.py
depends_on:
  - explorations/oq-rk1-rs-rank-first-principles-2026-06-23.md
  - explorations/oq-rk1-cas-matrix-rank-2026-06-23.md
  - explorations/generation-count-rs-clifford-projector-computation-2026-06-24.md
  - explorations/cycle1-generation-rs-rank-direct-gate-2026-06-24.md
  - explorations/cycle2-physical-rs-projector-effective-operator-certificate-2026-06-24.md
  - explorations/three-generation-route-alternatives-after-rs-failure-2026-06-26.md
  - canon/shiab-existence-cl95.md
gates_for_resolved:
  - "A concrete, source-derived definition of the effective RS projector E_RS^eff (or Pi_RS^phys) as an H-linear idempotent on ONE common right-H module, NOT obtained by dividing the target 8 by A-hat(K3)=2."
  - "An unambiguous fixing of which operator 'E_+' denotes: the global Cl(9,5) chirality (1+omega)/2 OR the VZ Schur-complement E-block (FC-VZ-1, not yet extracted from source-closed D_GU)."
  - "A type-correct statement of the ambient algebra: the raw Pi_RS acts on M(896,H), not M(64,H); the effective object must be shown to live in a definite M(n,H)."
---

# OQ-RK1 Attempt: rank_H(Pi_RS . E_+ . Pi_RS) in M(64,H)

> **Bottom line: BLOCKED_NEEDS_SPEC.** The factors of the decisive expression are not all
> pinned down. `E_+` is pinnable and I verified it explicitly (rank_H = 32). `Pi_RS` is NOT
> pinned as an operator on `S = H^64`: the only concrete RS projector in the repo is the raw
> 14D gamma-trace kernel, which acts on the 896-quaternion-dimensional vector-spinor space
> (`M(896,H)`, not `M(64,H)`) and has `rank_H = 416` — neither 4 nor 8. The number `4` has
> only ever appeared via the forbidden target-division `8 / A-hat(K3) = 8/2`. I did **not**
> fabricate an operator to hit 4 or 8. This is the same error class as CORRECTION
> FC4-HOLONOMY-01 ("fabricate a formula to hit the answer"); repeating it would be the worst
> outcome, so the honest result is a precise specification of what is missing.

---

## 1. What OQ-RK1 Asks and Why It Is Decisive

The 3-generation claim is `ind_H(D_GU) = 16 + 8 = 24`, generations `= 24/8 = 3`. The
`16` leg (`8 * A-hat(K3)`) is exact topology. The `8` leg (`ind_H(D_RS) = 8`) is the weak
point: every analytic route to it failed (scalar BC1, A3 Harish-Chandra, tau-twisted), and
the surviving APS/K3 route is **circular** — it sets `rank_H(S_RS^+) = ind_H(D_RS)/A-hat(K3)
= 8/2 = 4` and then multiplies back to "recover" 8. `[verified — see oq-rk1-rs-rank-first-
principles-2026-06-23.md correction banner; cycle1-generation-rs-rank-direct-gate-2026-06-24.md]`

OQ-RK1 breaks the circularity by demanding the **target-independent** quaternionic rank of
the projected chirality operator directly:

```
rank_H( Pi_RS . E_+ . Pi_RS )  in M(64,H)   ->  4  (3 generations)  or  8  (4 generations).
```

If this rank can be computed from the Clifford data alone, without ever inserting `8`, it
decides Candidate A (3 gen) vs Candidate B (4 gen, undismissed). That is why it is the
highest-leverage test in the program.

---

## 2. STEP 1 — Are Pi_RS and E_+ Pinned Down as Concrete M(64,H) Data?

I read every primary RS/rank source (synthesis, first-principles, CAS-matrix, Clifford-
projector, both direct-gate cycles, the physical-projector certificate, the canon Cl(9,5)
file, and today's route-alternatives file). The finding is sharp and matches the existing
repo consensus.

### 2.1 E_+ — PINNED (and I verified it explicitly)

`E_+` read as the **global Cl(9,5) chirality projector** `(1 + omega)/2` is completely
well-defined. I built an explicit complex `128x128` representation of `Cl(9,5)`
(`= M(64,H)` complexified to `M(128,C)`) — which the repo did **not** previously contain (it
only had a `Cl(4,0)` toy in `tests/rs_clifford_projector_model.py`) — and verified by actual
matrix computation:

| quantity | computed | grade |
|---|---|---|
| `{e_a, e_b} = 2 eta_ab` (signature (9,5)) | max error `0.0` | `[verified]` |
| `omega^2 = +I`, `tr(omega) = 0` | error `0.0` | `[verified]` |
| `E_+ = (I+omega)/2` idempotent | error `0.0` | `[verified]` |
| `rank_C(E_+) = 64` -> `rank_H(E_+) = 32` | exact | `[verified]` |

So the `E_+` factor contributes `rank_H = 32` — exact, no approximation, no target.

**Ambiguity flag (does NOT block by itself, but must be resolved):** the OQ-RK1 prompt calls
`E_+` the "E-block / chirality projector," treating the two as synonyms. In the repo they are
**different objects**: the VZ "E-block" `E(xi)` is the Schur-complement block of the GU
principal symbol, and it has **not** been extracted from the source-closed `D_GU` (FC-VZ-1 is
OPEN; `cycle2-vz-actual-operator-e-block-certificate-2026-06-24.md`). If OQ-RK1 means the
global chirality, `E_+` is pinned (above). If it means the VZ E-block, `E_+` is itself
undefined. `[verified — repo status of FC-VZ-1]`

### 2.2 Pi_RS — NOT PINNED as an operator on S = H^64

This is the blocker. The RS constraint is `Gamma^{14D} Psi = sum_a c(e_a) Psi_a = 0`, a map
**from** the vector-spinor space `(R^14)* (x) S` **to** `S`. It does **not** define a
projector on the 64-quaternion spinor module `S = H^64`. There are three inequivalent
"`Pi_RS`" objects in play, and they live in different algebras with different ranks:

| candidate Pi_RS | ambient algebra | rank_H | status |
|---|---|---|---|
| raw 14D gamma-trace kernel `ker(Gamma^14)|_{S^+}` | `M(896,H)` | **416** | `[verified]` exact, computed below |
| raw 4D pulled-back kernel `ker(Gamma^4)|_{S^+}` | `M(256,H)` | 96 (->64 post-gauge) | `[verified]` exact, prior files |
| effective APS coefficient `E_RS^eff` (would give 4 or 8) | undefined | **UNDEFINED** | missing object |

I verified the raw 14D object in the explicit representation:

```
Gamma^14|_+ : C^896 -> C^64  is surjective (rank_C = 64),
rank_C(ker) = 896 - 64 = 832  ->  rank_H(ker) = 416.
```

`[verified — tests/oq_rk1_cl95_explicit_rep.py; confirms the abstract rank-nullity of
oq-rk1-cas-matrix-rank-2026-06-23.md in a genuine explicit M(64,H) representation]`

**The point:** the only concrete `Pi_RS` available gives `rank_H = 416` and lives in
`M(896,H)`, not `M(64,H)`. It is neither 4 nor 8. The desired effective object `E_RS^eff`
(of `rank_H` 4 or 8) is the gauge/BRST-quotiented, K-theory-symbol-class object, and it is
**not constructed anywhere** — `cycle1-generation-rs-rank-direct-gate` and
`cycle2-physical-rs-projector-effective-operator-certificate` both record it as
`UNDERDEFINED`. The `4` arises only by `8 / A-hat(K3) = 8/2`, the forbidden target-division.

### 2.3 Conclusion of Step 1

```
E_+      : PINNED (global chirality reading), rank_H = 32, verified.
           AMBIGUOUS if "E-block" reading intended (FC-VZ-1 open).
Pi_RS    : NOT PINNED on S = H^64.
           Concrete raw object -> 416_H in M(896,H) (not 4, not 8, wrong algebra).
           Effective object E_RS^eff that would give 4 or 8 -> UNDEFINED.
=> OQ-RK1 is NOT computable as stated. Do not run a rank and call it 4 or 8.
```

---

## 3. STEP 2 — What I Computed (the well-defined pieces only)

I did **not** fabricate `Pi_RS^eff`. I ran the pieces that ARE well-defined, to (a) give the
repo its first explicit `Cl(9,5) = M(64,H)` representation and (b) make concrete exactly how
far the well-defined raw object (416) sits from the target (4 or 8).

`tests/oq_rk1_cl95_explicit_rep.py` output:

```
dimension_C = 128  (= 2^7; M(64,H) complexified)
Clifford {e_a,e_b}=2 eta_ab : ok=True (max err 0.00e+00)
omega^2 = +I : True (err 0.00e+00); tr(omega)=0.000

OPERATOR (1) E_+ = (I+omega)/2  [the chirality / E-block projector]:
  idempotent err = 0.00e+00
  rank_C(E_+) = 64  ->  rank_H(E_+) = 32.0

OPERATOR (2) Pi_RS^raw via 14D gamma-trace kernel on S^+ vector-spinors:
  c(e_a): S^+ -> S^- for all a : True
  Gamma^14|_+ : C^896 -> C^64, rank_C=64 (surjective=True)
  rank_C(ker) = 832  ->  rank_H(ker) = 416.0
```

Construction (so it is auditable): 14 Jordan-Wigner Hermitian gammas of size 128
(`G_{2k+1}=s3^{(x)k}(x)s1(x)I`, `G_{2k+2}=s3^{(x)k}(x)s2(x)I`); signature (9,5) via
`e_a = G_a` (a<9) and `e_a = i G_a` (a>=9); `omega = e_0...e_13`; H-rank `= C-rank/2` because
`M(64,H)(x)_R C = M(128,C)` and an H-linear idempotent of H-rank `r` has complex rank `2r`.
`[verified]`

These numbers (32, 416) are exact and target-free. **Neither is the decisive OQ-RK1
quantity.** They bracket the problem: the raw RS object is 416_H; getting to 4 or 8 requires a
reduction by a factor of ~100, and that reduction is precisely the unspecified physical/
K-theoretic content.

---

## 4. Precise Specification: What Must Be Defined for OQ-RK1 to Be Computable

For `rank_H(Pi_RS . E_+ . Pi_RS)` to be a well-typed number that decides 4 vs 8, the
following must be supplied. (This is the deliverable of a BLOCKED_NEEDS_SPEC verdict.)

**S1. Disambiguate `E_+`.** State whether `E_+ =` (a) global Cl(9,5) chirality `(1+omega)/2`
(pinned, rank_H 32), or (b) the VZ Schur-complement E-block `E(xi)` (requires first closing
FC-VZ-1: extracting `E(xi)` from source-closed `D_GU`). These are different operators.

**S2. Fix the common module `M^src` (one right-H module).** Specify the single right-H module
on which `Pi_RS`, `E_+`, and the composite all act. It cannot be inferred from the raw fiber:
it must say whether the setting is compact K3, weighted/projected `Y^14`, or an APS
compactification, and give the bundle, right-H action `J` (`J^2=-1`), and connection/domain.

**S3. Define `Pi_RS` as an H-linear idempotent on `M^src`.** Not the gamma-trace map (a map
between different spaces) and not merely the raw gamma-trace kernel projector (416_H on
`M(896,H)`). It must be `Pi_RS^phys`: the projector onto physical RS degree-zero states, i.e.
one of {gauge-fixed quotient representatives, BRST harmonic representatives, degree-zero
cohomology of an elliptic RS complex, the projected tau-discrete sector}. This requires the
gauge map, gauge-fixing/ghost complex, and symbol-level ellipticity — all currently missing.

**S4. Replace "`rank`" by an index/Chern computation, or certify a fiberwise H-trace.** In
dimension 4 the difference between a raw fiber rank and an effective (APS) rank is exactly the
degree-4 Chern data. Either (i) supply the K-theory symbol class of the gauge-fixed operator
and compute its degree-0 and degree-4 Chern character components, or (ii) certify an H-linear
trace `Tr_H` so that `rank_H = Tr_H(E_RS^eff)` is meaningful. A bare complex rank halved to
"48_H" is not a proof object, and is still not 4 or 8.

**S5. Fix the source-selected background `F = s*S(6,4)` and `ch_2(F)[K3]`.** If `ch_2(F)=0`
is used it must be **proved** flat for the actual GU `Sp(64)` background, not imported because
it makes `8 = 2*4` work. A nonzero `ch_2(F)` shifts the index off 8.

**S6. Supply the same-operator `Y^14 -> K3` bridge.** A unitary discrete-sector bridge OR an
APS bridge with `eta`, `h`, spectral-flow, and end terms, transporting the **same** physical
RS complex, right-H structure, background, and symbol class. Compact K3 arithmetic is
control-only until this closes.

**S7. Forbidden shortcut (rollback guard).** Any value obtained as
`rank_H(E_RS^eff) = ind_H(D_RS)/A-hat(K3)` where `ind_H(D_RS)` was itself the target 8 must be
labeled `INVALID_TARGET_DIVISION` and rejected.

Shortest statement of the obstruction: **the repo has `Pi_RS^raw` (416_H, `M(896,H)`); it does
not have `Pi_RS^phys` / `E_RS^eff` on a common right-H module in any definite `M(n,H)`.**
Until S1-S6 exist, `Pi_RS . E_+ . Pi_RS` has no unique rank, and "4" is target-fed.

---

## 5. Verdict and Falsifiability

**Verdict: BLOCKED_NEEDS_SPEC** (equivalently OPEN, blocked on operator definition).

This is a clean negative: the decisive computation cannot be run because two of its three
inputs (`Pi_RS^phys`, and `E_+` under the E-block reading) are not defined, and the one
well-defined raw `Pi_RS` is in the wrong algebra with rank 416. Candidate A (3 gen) and
Candidate B (4 gen) both remain **OPEN, not derived**.

**Failure conditions (what would overturn this BLOCKED verdict — i.e. show OQ-RK1 *is*
computable now):**

1. **FC-RK1-A:** Someone exhibits a concrete H-linear idempotent `E_RS^eff` on a stated
   right-H module, with its rank computed without dividing by `A-hat(K3)`, returning a definite
   integer. (Would move to RESOLVED/CONDITIONALLY_RESOLVED depending on whether 4, 8, or other.)
2. **FC-RK1-B:** Someone shows the raw 14D object (416_H) reduces to 4 or 8 by an *explicit*
   gauge/BRST quotient + Chern correction, with every factor sourced (no `8/2`). My computed
   416 is the falsifiable anchor: any such reduction must start from 416_H (or 96_H in 4D) and
   account for every removed dimension.
3. **FC-RK1-C:** Someone proves the OQ-RK1 expression is well-typed in `M(64,H)` directly —
   i.e. produces a genuine projector "`Pi_RS`" that acts on `S = H^64` itself (not on the
   vector-spinor space). My finding is that no such natural projector exists, because the RS
   constraint is intrinsically a vector-spinor (index-carrying) condition; a counterexample
   here would overturn the type analysis in Section 2.2.

**Self-flagged risks / limits of this attempt:**

- I did not attempt to *construct* `E_RS^eff` (correctly — that is the missing physics, and
  fabricating it is the FC4-HOLONOMY-01 error). So I have not advanced the positive program;
  I have only sharpened the blocker and added an exact explicit-representation anchor.
- The `rank_H = rank_C/2` identification assumes the standard `M(64,H)(x)C = M(128,C)`
  dictionary; I verified the complex ranks (64, 832) directly but did not construct the
  quaternionic structure map `J` explicitly. For `E_+` and the raw kernel this is the standard,
  uncontested identification (same one the repo uses for `S(6,4)=C^16=H^8`).
- "BLOCKED_NEEDS_SPEC" restates, with a new explicit-rep anchor, what
  `cycle1-generation-rs-rank-direct-gate` and `cycle2-physical-rs-projector-effective-operator-
  certificate` already concluded. It is not a new mathematical result; it is a verified
  confirmation that the decisive test remains genuinely uncomputable on current data, plus a
  consolidated spec of the missing object.

---

## 6. DERIVATION-PROGRESS Entry (proposed)

```
OQ-RK1 (decisive generation-count rank) — BLOCKED_NEEDS_SPEC (2026-06-26).
Attempted the target-independent rank_H(Pi_RS . E_+ . Pi_RS). Built the repo's first
explicit Cl(9,5)=M(64,H) (~M(128,C)) representation (tests/oq_rk1_cl95_explicit_rep.py):
verified {e_a,e_b}=2 eta_ab, omega^2=+I, E_+ rank_H=32, and the raw 14D RS gamma-trace
kernel rank_H=416 (all machine-exact). Decisive 4-vs-8 number NOT computable: Pi_RS is not
pinned as an operator on S=H^64 — the only concrete RS projector (416_H) lives on the
vector-spinor space M(896,H), and the effective E_RS^eff that would give 4 or 8 is undefined
(missing: gauge/BRST quotient, K-theory symbol class, ch_2(F), H-trace, Y14->K3 bridge).
"4" appears only via the forbidden 8/A-hat(K3)=8/2. E_+ also ambiguous (global chirality vs
VZ E-block FC-VZ-1). Candidate A (3 gen) and Candidate B (4 gen) both remain OPEN, not derived.
No fabrication (avoided the FC4-HOLONOMY-01 error class). Full spec S1-S7 in
explorations/oq-rk1-rs-rank-attempt-2026-06-26.md Section 4.
```
