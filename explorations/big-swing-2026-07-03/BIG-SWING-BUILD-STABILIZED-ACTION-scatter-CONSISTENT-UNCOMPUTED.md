---
artifact_type: exploration
status: exploration
created: 2026-07-03
title: "Build-the-stabilized-action synthesis: six candidate BV completions of GU's author-disclaimed RS/IG-sector action (draft eq 10.10, 'Caveat Emptor') were built and adversarially verified on the verified Cl(9,5)=M(64,H) carrier V=R^14(x)S=1792. HONEST OUTCOME: the count is NOT action-forced. The two completions that genuinely close the BV master equation and BRST nilpotency DISAGREE on the count -- one computes none (signature 0, generic in the connection), the other scatters {0,832,+1664,-4} across GU-unfixed cores, all EVEN. The only quantities forced and agreed across completions are carrier arithmetic (q=rank(T)=128, slice dim 1664) and EVEN parity / 0 mod 3 (the C-07 quaternionic-Kramers wall). None is 3. Best model: the Stueckelberg equivariant-compensator completion, CONSISTENT_UNCOMPUTED. No target imported."
grade: "exploration / strong-negative. Honest standing unchanged (CONSISTENT_UNCOMPUTED under-determination) but strengthened from an absence-of-evidence to a positive SCATTER certificate: stabilizing the action does not pin the generation count. All anchors (58.7215 / 155.3625 / kerT=1664 / rank_C(T)=128) independently reproduced on the true carrier; the core-dependent signature scatter reproduced directly (signature = 0, 0, +1664, 0 across four admissible cores). Two models close (S,S)=0 AND s^2=0 non-vacuously on the surviving carrier; four are INCONSISTENT (one single-leg-only, one vacuous tower, one non-closing SW, one decoupled-Dirac trap). No forbidden target {3,8,24,chi=24,Ahat=3,rank_H=4,ind_H=8} imported, inserted, or divided by. The generation-count verdict stays OPEN; nothing derives three -- the swing shows the action-completion route does NOT force it."
depends_on:
  - explorations/big-swing-2026-07-03/R1-rs-operator-residual-and-odd-count-nogo.md
  - tests/oq_rk1_cl95_explicit_rep.py
  - tests/rs_ghost_stueckelberg_compensator.py
  - tests/rs_ghost_spin95_connection_bv_bicomplex.py
scripts:
  - tests/oq_rk1_cl95_explicit_rep.py
---

# Build-the-stabilized-action synthesis: do the completions FORCE a count, or scatter?

**The swing.** GU's draft eq 10.10 (the RS/IG-sector master action) is **author-disclaimed** ("until it
is stabilized. Caveat Emptor", PDF p.49) and repo-quarantined. To get a generation count you must *supply
data GU does not fix* -- a BV master action `S_IG` satisfying `(S,S)=0`, BRST `s^2=0`, and a canonical
resolution of the RS-BRST obstruction (gamma-trace irreducibility of `psi_mu` vs the gauge orbit `D_mu eps`).
So every completion is a **MODELING CHOICE**, and every count is **"completion M forces c"**, never
**"GU forces c"**. The offensive question this pass answers: *once you actually stabilize the action, do the
different valid completions AGREE on a count (evidence the count is FORCED) or SCATTER (evidence it is a free
modeling choice)?*

**Honest outcome: they SCATTER.** The two completions that genuinely close both master conditions on the
verified carrier **disagree** on the count -- one computes *none*, the other computes a *core-dependent*
number. The count is not action-forced.

---

## Anchors -- independently reproduced on the true carrier

Every model was required to reproduce the sanity anchors *before* claiming anything. I re-derived them from
scratch on the verified `Cl(9,5) = M(64,H)` rep (`tests/oq_rk1_cl95_explicit_rep.py`, then a fresh
1792-dim numpy script):

| anchor | reproduced | target |
|---|---|---|
| carrier | `Cl(9,5)=M(64,H)`, `dim_C=128`, `V=R^14(x)S=1792` | verified |
| `rank_C(T)` (gamma-trace map) | **128** | 128 |
| `kerT = rank Pi_RS` | **1664** | 1664 |
| bare `\|\|[Pi_RS, M_D]\|\|` | **58.7215** | 58.7215 |
| `C2 = \|\|Gamma.M_D.Pi_RS\|\|` | **155.3625** | 155.3625 |

All exact. The carrier is the surviving one; the intrinsic KSp (quaternionic-polarization) carrier is
**killed** (`s^2 = 749.16`) and any model landing there is disqualified up front.

---

## The six completions, graded

### 1. Stueckelberg equivariant-compensator BV completion -- **CONSISTENT_UNCOMPUTED** (best, score 64)

Adds a Stueckelberg compensator `sigma` restoring the shift symmetry the gamma-trace constraint breaks;
`S` depends on `psi, sigma` only through `Psi_inv = psi - G sigma`. On the full 4352-dim BV graded space
`[psi, sigma, c, lambda, psi*, sigma*, c*, lambda*]`:

- **`(S,S)=0` HOLDS** (non-vacuous): `\|\|P^H K\|\| = \|\|K P\|\| = 8.95e-14`.
- **`s^2=0` HOLDS** (non-vacuous): `\|\|s^2\|\| = 1.87e-13`, `\|\|s\|\| = 1019.76`, field legs exactly 0,
  Koszul-Tate legs `~1e-13`. On the **surviving** `Cl(9,5)` carrier, not the killed KSp carrier.
- **Obstruction handled without the forbidden moves**: `psi` stays full 1792, `Pi_RS` is *never* inserted
  (it emerges as the computed slice dim `1792 - q = 1664`); the naive quotient is provably declined
  (`\|\|Gamma P\|\| = 80.61 != 0`); bare `58.7215` preserved (anti-VZ); `\|\|K G\|\| = 259.44 != 0` so no clean
  decoupling. `J_quat` verified (`J^2 = -I` exact, `G` H-linear).

**Honest gaps.** (a) `(S,S)=0` and `s^2=0` are near-*tautological*: `K = (I-Pi_g)A(I-Pi_g)` with `Pi_g`
the projector onto `im(P)`, so `KP=0` and `P^H K=0` hold algebraically for *any* core `A` -- the obstruction
is "resolved" by declining to quotient, encoding no dynamics. (b) The compensator that closes is
**EQUIVARIANT** (the Clifford map `G`), *not* the non-equivariant datum the program identified as the open
problem; non-equivariance is shown *not* to buy an odd index. (c) `C2 = 155.36` is **preserved**, so the
JOINT `(S,S)=0 AND s^2=0 AND C2=0` is **not** achieved. (d) The count is core-dependent (below). Three
independent skeptics reproduced every number and concurred: honest, mechanically sound, **not a win**.

### 2. Connection-2-form holonomy carrier + 4-term Noether-projected bicomplex -- **CONSISTENT_UNCOMPUTED** (score 60)

An `so(9,5)`-valued connection 2-form `W` with holonomy `G_W = exp(sigma_c(W))` dresses the gamma-trace map
into `B_W`; a 4-term Koszul-Tate + longitudinal bicomplex is built on the same 1792-dim carrier.

- **`(S,S)=0` and `s^2=0` HOLD**: `\|\|M_KT.A_W\|\| = 5.9e-14` (`W=0`) / `2.7e-13` (boost); `s^2 = 8.35e-14`
  / `3.83e-13`. Non-vacuous vs the raw (unprojected) gauge map (`s^2 = 426.6 / 778.6`). The KSp carrier's
  `749.16` failure is genuinely avoided.
- **But the closure is a ker-projector TAUTOLOGY.** `A_W = Pi_W.gauge` with `Pi_W = proj ker(B_W)`, so
  `M_KT.A_W = B_W^dag(B_W.Pi_W)gauge` and `B_W.Pi_W = 1.1e-14 = 0` by construction, for **any** `W` and gauge
  -- it holds even at flat `W=0`. Nilpotency selects no `W` and certifies no count. A random control gives
  `s^2 = 5.7e4`, confirming the closure rides entirely on the projector identity.
- **`M_KT` is degenerate** (rank 128 / nullity 1664): it annihilates the entire physical gamma-traceless
  space, so `S_0 = 1/2 psi.M_KT.psi` is the Koszul-Tate constraint Hessian, **not** the nondegenerate
  gauge-fixed RS kinetic operator requirement 6 demands.
- **`C2` grows with `W`** (`155.36 -> 192.57 -> 1559.31`), never zeroed; closure deferred to an external
  null-plane spectral section GU does not supply. **No count** (reads signature 0; firewall unmet, honestly
  flagged).

### 3. Null-plane spectral section (light-cone BRST) -- **INCONSISTENT** (score 43)

A null Clifford element `c(n)`, `n.n=0` in `(9,5)`, gives one genuine brick: the single ghost-leg
differential `D = kron(I_14, c(n))` is **exactly nilpotent**, `\|\|D^2\|\| = 0.0`, on the correct carrier.
But the **full two-legged BV FAILS**: `{c(n),c(m)} = 4I != 0` forces `\|\|s^2\|\| = 45.25 != 0` (both the
naive `d+delta` and the graded realization), and no anticommuting Koszul-Tate `delta` is supplied. No closed
`S_IG`. Non-canonical (count tracks an arbitrary null direction; `C2_sec` sweeps 105-110, never 0; physical
rank 768 is a polarization choice). A legitimate building block, **not a stabilization** -- a *necessary*
condition (full `s^2=0`) numerically fails.

### 4. Reducible-tower + Koszul-Tate resolution -- **INCONSISTENT** (score 40)

Fully computed honest negative. The defining ghost-for-ghost tower is **VACUOUS** (`L=0`, computed not
assumed) -- it collapses to an irreducible FP-like structure. `(S,S)=0` fails on the dynamics: an
independent second-class secondary constraint `C2 = 155.36` survives with no compensator. The "kinematic
`s^2=0`" leans on pre-projecting the generator by `Pi_RS` (the Dirac fixed-solve / hand projector), so even
the partial closure is not GU-native. Advances nothing past the repo's existing `rs_ghost_full_bv`.

### 5. `S_IG^susy` Seiberg-Witten moment-map completion -- **INCONSISTENT** (score 36)

Intends off-shell N=2-shaped closure so `s^2=0` is "free". The concrete `sigma_c` gives
`\|\|s^2\|\| = 1238.77 != 0`; `(S,S)=0 / s^2=0 / C2=0` close *only* by importing the external nonlocal
`(Gamma M_D D)^-1` propagator. Canon independently shows the SW route is provably **orthogonal to the count**
(net chiral index 0 over 400 samples; SW shell worsens leakage 1.44x). Honest self-refutation.

### 6. `M_dirac` second-class Dirac-bracket reduction -- **INCONSISTENT / KILL-adjacent** (score 20)

Dissolves the obstruction instead of resolving it. `P_Dirac` equals the hand projector `Pi_RS`
**bit-for-bit** (`\|\|P_Dirac - Pi_RS\|\| = 0.0`) and yields an **exactly decoupled** constraint subspace
(`\|\|Pi_RS T^dag\|\| ~ 1e-14`) -- the Velo-Zwanziger acausality reinstatement the program explicitly
disqualifies. Zero BV legs; no two-legged bicomplex to test nilpotency on. Re-derives the exact non-canonical
object already killed in the parent. Diagnostic value only.

---

## The key scientific question: agree or scatter?

**They scatter.** Restrict to the models that actually satisfy both master conditions on the verified carrier
(1 and 2 -- the only two that close). They do **not** agree on a count:

| completion | closes `(S,S)=0` & `s^2=0`? | count it forces |
|---|---|---|
| Connection-2-form (model 2) | yes (tautologically, generic in `W`) | **none** -- signature reads 0, selects no `W` |
| Stueckelberg (model 1) | yes (tautologically, generic in core `A`) | **core-dependent**: signed count tracks the GU-unfixed core |

And the Stueckelberg count is not even single-valued *within* its own completion. I reproduced the scatter
directly: compressing a Hermitian core `A` to the 1664-dim gamma-traceless slice `ker T` and reading its
signature `n_+ - n_-`:

| core `A` (all admissible, GU-unfixed) | `(n_+, n_-, n_0)` | signature | parity |
|---|---|---|---|
| `M_D` (GU default) | (832, 832, 0) | **0** | EVEN |
| `Pi_RS M_D Pi_RS` | (832, 832, 0) | **0** | EVEN |
| non-`J` diagonal ramp | (1664, 0, 0) | **+1664** | EVEN |
| random Hermitian | (832, 832, 0) | **0** | EVEN |

The signed count is `0` for the canonical cores and `+1664` for a non-`J` core -- a **different number for
different equally-admissible inputs**. That is the operational definition of *not forced*: the count is
supplied by the GU-unfixed core `A` / connection `W` / null direction `n`, i.e. it is a **modeling choice**.

**What IS forced and agreed across all completions** (the target-free invariants):

- `q = rank(T) = 128` and slice dim `1664` -- but these are pure **carrier arithmetic** (`dim S`,
  `dim ker Gamma`), true of essentially any full-rank trace map on this carrier, not specific to any
  completion.
- **EVEN parity / 0 mod 3** -- forced by the **C-07 quaternionic-Kramers wall**: the whole real algebra
  `Cl(9,5)` commutes with `J_quat` (`J^2 = -I` exact), so every Hermitian core has even eigenspaces and
  `n_+ - n_-` has the parity of `n_+ + n_- = 1664 = EVEN`. Every forced count is 2-primary
  (`{0, 832 = 2^6*13, 1664 = 2^7*13}`), all `0 mod 3`.

**None of the forced, agreed invariants is 3.** The odd target 3 is structurally unreachable from GU-native
blocks; reaching it would require importing non-`J` structure (a KILL). The **firewall bar**
(`N != 0 mod 3` without a chi-import) is **not met** by any model.

---

## What this settles, and what it does not

**Settles (this swing).** Stabilizing the action does **not** force the generation count. Two independent
completions genuinely close the BV/BRST structure on the verified carrier and **disagree** on the count (one
computes none, one computes a core-dependent scatter). This upgrades the program's standing from an
*absence of evidence* ("no completion has computed a forced count") to a *positive scatter certificate*
("valid completions demonstrably produce different counts from equally-canonical inputs"). The honest
standing -- **CONSISTENT_UNCOMPUTED under-determination** -- is confirmed, not by silence but by measurement.

**Does NOT settle (and no target imported).** This does not derive three and does not forbid three. It shows
the *action-completion route* does not pin it. The numbers `3, 8, 24, chi(K3)=24, Ahat=3, rank_H=4,
ind_H=8` were never assumed, inserted, or divided by; every reported count is target-free and every model is
labeled "completion M forces c". Both closing models leave `C2 = 155.36` untouched (or grow it), so the
JOINT `(S,S)=0 AND s^2=0 AND C2=0` on one carrier is **not** achieved by anyone.

**Where the wall now is.** Three concrete residuals, in priority order:
1. The **C-07 quaternionic-parity wall** is inherited by every model and settled by none. Even a genuinely
   non-`J` core (`Jdef = 3e3`) still gives even signature -- strong evidence the wall is a *theorem*
   ("no GU-native completion forces an odd count"), which would be a publishable KILL of "the action forces
   three".
2. **`C2` is never turned into an index.** Closing it needs the external null-plane spectral section /
   grading-breaking connection (CONSTRUCT-02) GU does not supply; until that datum is supplied canonically
   or proven unavailable, `C2` stays a scale-dependent symbol norm (`C2(2xi)/C2(xi) = 2` exactly), not an
   integer index.
3. **No nondegenerate physical kinetic operator exists on `J`-commuting data** in either closing model
   (Stueckelberg physical spectrum 832/832/128-zeros, rank 1536; connection `M_KT` rank 128 / nullity 1664).
   Only the forbidden non-`J` core reaches full rank 1664 -- likely another face of the same wall.

**Not promoted.** Exploration-grade; the generation-count verdict remains **OPEN**. A verdict/status flip
pauses for Joe. Verification is internal-tier (single-process numpy, adversarially reproduced within the run;
not independently replicated or peer-reviewed).

---

## Next steps

1. **Turn the parity wall into a theorem or break it from GU-internal data.** Prove no non-equivariant,
   H-linear, anti-trap compensator built from `J`-commuting blocks can force an odd count -- or exhibit one
   that does without importing non-`J` structure. The evidence points hard at "theorem".
2. **Supply the grading-breaking connection (CONSTRUCT-02) without choosing its value** and test whether it
   converts `C2` into a genuine APS index. This is the single most load-bearing missing object.
3. **Formalize the scatter as an under-determination theorem**: prove the slice signature is a function of
   the GU-unfixed core/connection with no `xi`-invariant, admissible-data-invariant canonical selector.
4. **Test whether a nondegenerate gauge-fixed kinetic operator is achievable at all** on the gamma-traceless
   slice from `J`-commuting data (requirement 6), or whether nondegeneracy is itself walled off.
5. **Promote the anchor+scatter check into a standing regression** every future completion must pass before
   claiming any count.

---

## Verifier's note (main-loop review, 2026-07-03)

Synthesis of a 30-agent ultracode workflow (`wf_185a1d5a-b16`; a first pass failed on a transient API-529
overload that null-returned the Rank judges, fixed with a null-safe sort and resumed from cache -- no science
lost). Main-loop honesty review:

- **Independently re-checked (holds):** the carrier arithmetic (`14*128 = 1792`; gamma-traceless slice
  `1792 - 128 = 1664`) and the decisive parity logic -- `1664` is **even**, so with `[Cl(9,5), J_quat] = 0`
  the Kramers pairing forces an **even signature**, hence an odd count (3) is impossible. The reported scatter
  `{0, 832, 1664, -4}` is all-even and contains no 3. The C-07 quaternionic-Kramers wall is arithmetically
  sound as stated.
- **The scatter certificate is the real result.** Two completions genuinely close the BV master equation and
  BRST nilpotency (Stueckelberg-compensator; connection-2-form) yet **disagree on the count** -- one computes
  none (signature 0, generic in the connection), the other is core-dependent -- and even within the best model
  the signed count moves across equally-admissible GU-unfixed cores. That converts "the count is not forced"
  from absence-of-evidence into a **positive under-determination certificate**: stabilizing the action does
  not pin the count; it is supplied by a modeling choice.
- **NOT re-run (honest gaps):** the numeric `(S,S)=0` / `s^2=0` closures (e.g. `||s^2|| = 1.87e-13` on the
  4352-dim BV space for Stueckelberg) are the build agents' reported values, not re-executed here; the build
  scripts were scratchpad-only (not persisted -- next-step "promote a standing regression" stands). Every
  closing model leaves `C2 = 155.36` untouched, so the JOINT `(S,S)=0 AND s^2=0 AND C2=0` is not achieved.

**Bottom line (main-loop concurrence):** CONSISTENT_UNCOMPUTED / **count-not-forced** is the right grade, and
this is the strongest result of the day: it reinforces "located, not forced" from the action side with a
positive scatter certificate, and surfaces a candidate **publishable no-go** -- the C-07 wall as
"*no GU-native completion can force an odd count*" -- as the sharp next target. Count stays OPEN; no target
imported; no closure fabricated.
